#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Render build-time photo downloader.
Transfermarkt kadro sayfasını çekip oyuncu fotoğraflarını indirir.
Kaynak: Transfermarkt (eğitim/test amaçlı — ticari kullanım yok)
"""
import os, re, time, json, sys
import urllib.request, urllib.error

OUT_DIR   = os.path.join(os.path.dirname(__file__), "static", "images", "players")
MAP_FILE  = os.path.join(OUT_DIR, "map.json")
SQUAD_URL = "https://www.transfermarkt.com/fenerbahce/kader/verein/36/plus/1"

# Bilinen TM player ID → uygulama oyuncu slug eşleşmesi
KNOWN = {
    "225083": "kante",
    "382528": "kerem",
    "591361": "oosterwolde",
    "401356": "edson-alvarez",
    "671591": "dorgeles-nene",
    "204069": "skriniar",
    "320748": "szymanski",
    # Diğerleri otomatik keşfedilir
}

PAGE_HEADERS = {
    "User-Agent":      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept":          "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Connection":      "keep-alive",
}
IMG_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Referer":    "https://www.transfermarkt.com/",
    "Accept":     "image/webp,image/apng,image/*,*/*;q=0.8",
}


def fetch_html(url):
    req = urllib.request.Request(url, headers=PAGE_HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            raw = r.read()
            # gzip decompression
            if r.info().get("Content-Encoding") == "gzip":
                import gzip
                raw = gzip.decompress(raw)
            return raw.decode("utf-8", errors="replace")
    except Exception as e:
        return None


def extract_photos(html):
    """
    TM detaylı kadro sayfasından portrait URL'lerini ve oyuncu linklerini çıkarır.
    Döndürür: [ (tm_player_id, photo_url, player_url), ... ]
    """
    results = []
    seen = set()

    # Portrait URL pattern: .../portrait/header/PLAYERID-TIMESTAMP.jpg
    photo_re  = re.compile(
        r'(?:data-src|src)=["\']'
        r'(https://img\.a\.transfermarkt\.technology/portrait/(?:header|medium)/(\d+)-\d+\.(?:jpg|png))'
        r'["\']'
    )
    # Player link pattern: /player-name/profil/spieler/PLAYERID
    link_re = re.compile(r'href=["\'][^"\']*?/profil/spieler/(\d+)["\']')

    # Scan 5000-char windows so we pair photo + ID reliably
    blocks = re.split(r'<td\s+class="[^"]*hauptlink[^"]*"', html)
    for block in blocks:
        pm = photo_re.search(block)
        lm = link_re.search(block)
        if pm and lm:
            pid = pm.group(2)
            if pid not in seen:
                seen.add(pid)
                results.append((pid, pm.group(1)))

    # Fallback: collect all portrait URLs in order
    if not results:
        for m in photo_re.finditer(html):
            pid = m.group(2)
            if pid not in seen:
                seen.add(pid)
                results.append((pid, m.group(1)))

    return results


def download_image(url, dest):
    req = urllib.request.Request(url, headers=IMG_HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = r.read()
        if len(data) < 4096:
            return False, f"too small ({len(data)}B)"
        with open(dest, "wb") as f:
            f.write(data)
        return True, f"{len(data)//1024}KB"
    except urllib.error.HTTPError as e:
        return False, f"HTTP {e.code}"
    except Exception as e:
        return False, str(e)


def run():
    os.makedirs(OUT_DIR, exist_ok=True)

    print("📥 Transfermarkt kadro sayfası çekiliyor...")
    html = fetch_html(SQUAD_URL)
    if not html:
        print("❌ Transfermarkt'a ulaşılamadı — avatarlar kullanılacak.")
        sys.exit(0)

    print(f"   Sayfa uzunluğu: {len(html):,} karakter")

    photos = extract_photos(html)
    print(f"   {len(photos)} oyuncu fotoğrafı bulundu")

    if not photos:
        print("❌ Fotoğraf URL'leri çıkarılamadı — HTML yapısı değişmiş olabilir.")
        sys.exit(0)

    photo_map = {}
    ok = fail = 0

    for tm_id, photo_url in photos:
        dest = os.path.join(OUT_DIR, f"{tm_id}.jpg")
        if os.path.exists(dest) and os.path.getsize(dest) > 4096:
            print(f"  ⏩ {tm_id} zaten mevcut")
            ok += 1
        else:
            success, info = download_image(photo_url, dest)
            if success:
                print(f"  ✅ {tm_id} ({info})")
                ok += 1
            else:
                print(f"  ❌ {tm_id}: {info}")
                fail += 1
            time.sleep(0.4)

        # slug eşleşmesi (bilinen + otomatik)
        slug = KNOWN.get(tm_id)
        if slug:
            photo_map[slug] = f"/static/images/players/{tm_id}.jpg"

    # map.json kaydet — Flask başlarken yükler
    with open(MAP_FILE, "w") as f:
        json.dump(photo_map, f, indent=2)

    print(f"\n✅ {ok} indirildi / ⏩ atlandı  |  ❌ {fail} başarısız")
    print(f"📄 map.json kaydedildi: {len(photo_map)} eşleşme")


if __name__ == "__main__":
    run()
