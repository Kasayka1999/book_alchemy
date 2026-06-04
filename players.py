# -*- coding: utf-8 -*-
"""
Fenerbahçe kadro + teknik ekip verisi.

NOT: Liste 2025-26 sezonu bilgilerine dayanır; transfer dönemlerinde değişebilir.
Düzenlemek için sadece bu dosyayı değiştir.

Oyuncu alanları:
  id      -> detay sayfası adresi (benzersiz, küçük harf)
  number  -> forma numarası
  name    -> oyuncu adı
  role    -> mevki (ör. "Stoper")
  country -> uyruk bayrağı (emoji)
  age     -> yaş
  photo   -> (opsiyonel) gerçek fotoğraf URL'si — boşsa isimden avatar üretilir
  stats   -> sezon istatistikleri (placeholder; gerçek rakamlarla güncelle)
"""


def _stats(mac=0, gol=0, asist=0):
    return {"mac": mac, "gol": gol, "asist": asist}


TEAM_INFO = {
    "name": "Fenerbahçe SK",
    "season": "2025-26 Sezonu",
    "stadium": "Ülker Stadyumu — Şükrü Saracoğlu",
    "founded": 1907,
    "motto": "Bir kere Fenerbahçeli olan, daima Fenerbahçelidir.",
}

SQUAD = [
    {
        "group": "Kaleciler",
        "icon": "🧤",
        "players": [
            {"id": "ederson",        "number": 1,  "name": "Ederson",             "role": "Kaleci", "country": "🇧🇷", "age": 32, "photo": "", "stats": _stats()},
            {"id": "livakovic",      "number": 50, "name": "Dominik Livaković",   "role": "Kaleci", "country": "🇭🇷", "age": 31, "photo": "", "stats": _stats()},
            {"id": "egribayat",      "number": 34, "name": "İrfan Can Eğribayat", "role": "Kaleci", "country": "🇹🇷", "age": 27, "photo": "", "stats": _stats()},
            {"id": "tarik-cetin",    "number": 35, "name": "Tarık Çetin",         "role": "Kaleci", "country": "🇹🇷", "age": 28, "photo": "", "stats": _stats()},
        ],
    },
    {
        "group": "Defans",
        "icon": "🛡️",
        "players": [
            {"id": "skriniar",       "number": 37, "name": "Milan Škriniar",      "role": "Stoper",  "country": "🇸🇰", "age": 31, "photo": "", "stats": _stats()},
            {"id": "soyuncu",        "number": 4,  "name": "Çağlar Söyüncü",      "role": "Stoper",  "country": "🇹🇷", "age": 30, "photo": "", "stats": _stats()},
            {"id": "diego-carlos",   "number": 5,  "name": "Diego Carlos",        "role": "Stoper",  "country": "🇧🇷", "age": 33, "photo": "", "stats": _stats()},
            {"id": "oosterwolde",    "number": 3,  "name": "Jayden Oosterwolde",  "role": "Sol Bek", "country": "🇳🇱", "age": 24, "photo": "", "stats": _stats()},
            {"id": "archie-brown",   "number": 13, "name": "Archie Brown",        "role": "Sol Bek", "country": "🏴", "age": 23, "photo": "", "stats": _stats()},
            {"id": "semedo",         "number": 19, "name": "Nélson Semedo",       "role": "Sağ Bek", "country": "🇵🇹", "age": 32, "photo": "", "stats": _stats()},
            {"id": "muldur",         "number": 2,  "name": "Mert Müldür",         "role": "Sağ Bek", "country": "🇹🇷", "age": 27, "photo": "", "stats": _stats()},
            {"id": "osayi-samuel",   "number": 17, "name": "Bright Osayi-Samuel", "role": "Sağ Bek", "country": "🇳🇬", "age": 28, "photo": "", "stats": _stats()},
            {"id": "levent-mercan",  "number": 24, "name": "Levent Mercan",       "role": "Sol Bek", "country": "🇹🇷", "age": 25, "photo": "", "stats": _stats()},
        ],
    },
    {
        "group": "Orta Saha",
        "icon": "⚙️",
        "players": [
            {"id": "ismail-yuksek",  "number": 6,  "name": "İsmail Yüksek",       "role": "Ön Libero",    "country": "🇹🇷", "age": 26, "photo": "", "stats": _stats()},
            {"id": "amrabat",        "number": 8,  "name": "Sofyan Amrabat",      "role": "Ön Libero",    "country": "🇲🇦", "age": 29, "photo": "", "stats": _stats()},
            {"id": "edson-alvarez",  "number": 28, "name": "Edson Álvarez",       "role": "Ön Libero",    "country": "🇲🇽", "age": 28, "photo": "", "stats": _stats()},
            {"id": "fred",           "number": 17, "name": "Fred",                "role": "Merkez O.S.",  "country": "🇧🇷", "age": 32, "photo": "", "stats": _stats()},
            {"id": "talisca",        "number": 10, "name": "Anderson Talisca",    "role": "10 Numara",    "country": "🇧🇷", "age": 32, "photo": "", "stats": _stats()},
            {"id": "szymanski",      "number": 7,  "name": "Sebastian Szymański", "role": "10 Numara",    "country": "🇵🇱", "age": 26, "photo": "", "stats": _stats()},
            {"id": "irfan-kahveci",  "number": 14, "name": "İrfan Can Kahveci",   "role": "Ofansif O.S.", "country": "🇹🇷", "age": 30, "photo": "", "stats": _stats()},
            {"id": "mert-hakan",     "number": 88, "name": "Mert Hakan Yandaş",   "role": "Merkez O.S.",  "country": "🇹🇷", "age": 31, "photo": "", "stats": _stats()},
        ],
    },
    {
        "group": "Forvet & Kanat",
        "icon": "⚡",
        "players": [
            {"id": "en-nesyri",      "number": 9,  "name": "Youssef En-Nesyri",   "role": "Santrfor",  "country": "🇲🇦", "age": 28, "photo": "", "stats": _stats()},
            {"id": "duran",          "number": 11, "name": "Jhon Durán",          "role": "Santrfor",  "country": "🇨🇴", "age": 22, "photo": "", "stats": _stats()},
            {"id": "saint-maximin",  "number": 20, "name": "Allan Saint-Maximin", "role": "Sol Kanat", "country": "🇫🇷", "age": 28, "photo": "", "stats": _stats()},
            {"id": "cengiz-under",   "number": 21, "name": "Cengiz Ünder",        "role": "Sağ Kanat", "country": "🇹🇷", "age": 28, "photo": "", "stats": _stats()},
            {"id": "oguz-aydin",     "number": 97, "name": "Oğuz Aydın",          "role": "Sağ Kanat", "country": "🇹🇷", "age": 24, "photo": "", "stats": _stats()},
            {"id": "dorgeles-nene",  "number": 30, "name": "Dorgeles Nene",       "role": "Sol Kanat", "country": "🇲🇱", "age": 22, "photo": "", "stats": _stats()},
        ],
    },
]

# Teknik ekip & yönetim — isimleri kendi bilgine göre doğrulayıp güncelle.
STAFF = [
    {"role": "Teknik Direktör",      "name": "Güncellenecek", "country": "⚽", "photo": ""},
    {"role": "Yardımcı Antrenör",    "name": "Güncellenecek", "country": "⚽", "photo": ""},
    {"role": "Kaleci Antrenörü",     "name": "Güncellenecek", "country": "🧤", "photo": ""},
    {"role": "Atletik Performans",   "name": "Güncellenecek", "country": "🏃", "photo": ""},
    {"role": "Kulüp Başkanı",        "name": "Güncellenecek", "country": "👔", "photo": ""},
]


def total_players():
    return sum(len(group["players"]) for group in SQUAD)


def get_player(player_id):
    """ID'ye göre oyuncuyu ve mevki grubunu döndürür (yoksa None, None)."""
    for group in SQUAD:
        for p in group["players"]:
            if p["id"] == player_id:
                return p, group["group"]
    return None, None
