# -*- coding: utf-8 -*-
"""
Fenerbahçe 2025-26 sezonu güncel kadro & teknik ekip.
Kaynak: Transfermarkt / Wikipedia (Haziran 2026)
Fotoğraflar: Wikimedia Commons (CC lisansı) — test/eğitim amaçlı.
"""

WIKI = "https://commons.wikimedia.org/wiki/Special:FilePath/"
AVATAR = "https://ui-avatars.com/api/?background=0a1228&color=ffd700&bold=true&font-size=0.4&size=300&name="


def photo(filename):
    return WIKI + filename if filename else ""


def _s(mac=0, gol=0, asist=0, sari=0, kirmizi=0):
    return {"mac": mac, "gol": gol, "asist": asist, "sari": sari, "kirmizi": kirmizi}


TEAM_INFO = {
    "name": "Fenerbahçe SK",
    "short": "FB",
    "season": "2025-26",
    "stadium": "Chobani Stadyumu (Şükrü Saracoğlu)",
    "capacity": "47.430",
    "founded": 1907,
    "league": "Trendyol Süper Lig",
    "motto": "Bir kere Fenerbahçeli olan, daima Fenerbahçelidir.",
    "market_value": "€247.9M",
    "colors": ["#14213d", "#ffd700"],
}

# Son maçlar (gerçek sonuçlar 2025-26)
RECENT_MATCHES = [
    {"home": "Fenerbahçe", "away": "Galatasaray", "score": "0-3", "date": "26 Nis 2026", "competition": "Süper Lig", "result": "L"},
    {"home": "Fenerbahçe", "away": "Gençlerbirliği", "score": "3-1", "date": "9 Şub 2026", "competition": "Süper Lig", "result": "W"},
    {"home": "Nottingham F.", "away": "Fenerbahçe",  "score": "2-1", "date": "20 Feb 2026", "competition": "Avrupa Ligi", "result": "L"},
    {"home": "Fenerbahçe", "away": "Galatasaray",    "score": "2-0", "date": "10 Oca 2026", "competition": "Süper Kupa", "result": "W"},
    {"home": "Fenerbahçe", "away": "Trabzonspor",    "score": "1-0", "date": "28 Mar 2026", "competition": "Süper Lig", "result": "W"},
]

# Süper Lig puan durumu (sezon sonu yaklaşık)
LEAGUE_TABLE = [
    {"pos": 1, "team": "Galatasaray",  "played": 34, "won": 24, "drawn": 6, "lost": 4,  "gf": 72, "ga": 35, "pts": 78, "highlight": False},
    {"pos": 2, "team": "Fenerbahçe",   "played": 34, "won": 22, "drawn": 7, "lost": 5,  "gf": 68, "ga": 33, "pts": 73, "highlight": True},
    {"pos": 3, "team": "Beşiktaş",     "played": 34, "won": 18, "drawn": 8, "lost": 8,  "gf": 58, "ga": 42, "pts": 62, "highlight": False},
    {"pos": 4, "team": "Trabzonspor",  "played": 34, "won": 17, "drawn": 6, "lost": 11, "gf": 54, "ga": 48, "pts": 57, "highlight": False},
    {"pos": 5, "team": "Başakşehir",   "played": 34, "won": 15, "drawn": 9, "lost": 10, "gf": 49, "ga": 44, "pts": 54, "highlight": False},
]

SQUAD = [
    {
        "group": "Kaleciler",
        "group_en": "Goalkeepers",
        "icon": "🧤",
        "color": "#1a3a5c",
        "players": [
            {
                "id": "ederson", "number": 1, "name": "Ederson",
                "role": "Kaleci", "country": "🇧🇷", "country_name": "Brezilya",
                "age": 32, "height": "1.88m", "foot": "Sol",
                "photo": photo("Ederson_(Manchester_City)_2022.jpg"),
                "stats": _s(mac=28, gol=0, asist=1),
                "market_value": "€10M",
            },
            {
                "id": "egribayat", "number": 34, "name": "İrfan Can Eğribayat",
                "role": "Kaleci", "country": "🇹🇷", "country_name": "Türkiye",
                "age": 27, "height": "1.93m", "foot": "Sağ",
                "photo": photo(""),
                "stats": _s(mac=6),
                "market_value": "€600K",
            },
            {
                "id": "biterge", "number": 39, "name": "Engin Can Biterge",
                "role": "Kaleci", "country": "🇹🇷", "country_name": "Türkiye",
                "age": 19, "height": "1.96m", "foot": "Sağ",
                "photo": photo(""),
                "stats": _s(mac=0),
                "market_value": "€100K",
            },
            {
                "id": "tarik-cetin", "number": 13, "name": "Tarık Çetin",
                "role": "Kaleci", "country": "🇹🇷", "country_name": "Türkiye",
                "age": 37, "height": "1.96m", "foot": "Sağ",
                "photo": photo(""),
                "stats": _s(mac=0),
                "market_value": "€500K",
            },
        ],
    },
    {
        "group": "Defans",
        "group_en": "Defenders",
        "icon": "🛡️",
        "color": "#1a3a3a",
        "players": [
            {
                "id": "skriniar", "number": 37, "name": "Milan Škriniar",
                "role": "Stoper", "country": "🇸🇰", "country_name": "Slovakya",
                "age": 31, "height": "1.87m", "foot": "Sağ",
                "photo": photo("Milan_%C5%A0kriniar_2016.jpg"),
                "stats": _s(mac=22, gol=1, asist=1),
                "market_value": "€10M",
            },
            {
                "id": "soyuncu", "number": 4, "name": "Çağlar Söyüncü",
                "role": "Stoper", "country": "🇹🇷", "country_name": "Türkiye",
                "age": 30, "height": "1.85m", "foot": "Sağ",
                "photo": photo("%C3%87a%C4%9Flar_S%C3%B6y%C3%BCnc%C3%BC_2022.jpg"),
                "stats": _s(mac=20, gol=0, asist=0, sari=3),
                "market_value": "€15M",
            },
            {
                "id": "becao", "number": 5, "name": "Rodrigo Becão",
                "role": "Stoper", "country": "🇧🇷", "country_name": "Brezilya",
                "age": 29, "height": "1.90m", "foot": "Sağ",
                "photo": photo(""),
                "stats": _s(mac=18, gol=1, asist=0),
                "market_value": "€12M",
            },
            {
                "id": "djiku", "number": 14, "name": "Alexander Djiku",
                "role": "Stoper", "country": "🇫🇷", "country_name": "Fransa",
                "age": 30, "height": "1.90m", "foot": "Sağ",
                "photo": photo("Alexander_Djiku_2023.jpg"),
                "stats": _s(mac=14, gol=0, asist=0),
                "market_value": "€7M",
            },
            {
                "id": "oosterwolde", "number": 3, "name": "Jayden Oosterwolde",
                "role": "Sol Bek", "country": "🇳🇱", "country_name": "Hollanda",
                "age": 24, "height": "1.89m", "foot": "Sol",
                "photo": photo("Jayden_Oosterwolde_2023.jpg"),
                "stats": _s(mac=25, gol=2, asist=3),
                "market_value": "€20M",
            },
            {
                "id": "archie-brown", "number": 22, "name": "Archie Brown",
                "role": "Sol Bek", "country": "🏴󠁧󠁢󠁥󠁮󠁧󠁿", "country_name": "İngiltere",
                "age": 23, "height": "1.90m", "foot": "Sol",
                "photo": photo(""),
                "stats": _s(mac=12, gol=0, asist=1),
                "market_value": "€9M",
            },
            {
                "id": "semedo", "number": 18, "name": "Nélson Semedo",
                "role": "Sağ Bek", "country": "🇵🇹", "country_name": "Portekiz",
                "age": 31, "height": "1.77m", "foot": "Sağ",
                "photo": photo("N%C3%A9lson_Semedo_2018.jpg"),
                "stats": _s(mac=20, gol=0, asist=2),
                "market_value": "€7M",
            },
            {
                "id": "muldur", "number": 27, "name": "Mert Müldür",
                "role": "Sağ Bek", "country": "🇹🇷", "country_name": "Türkiye",
                "age": 27, "height": "1.84m", "foot": "Sağ",
                "photo": photo("Mert_M%C3%BCld%C3%BCr_2022.jpg"),
                "stats": _s(mac=16, gol=1, asist=2),
                "market_value": "€15M",
            },
            {
                "id": "levent-mercan", "number": 24, "name": "Levent Mercan",
                "role": "Sol Bek", "country": "🇹🇷", "country_name": "Türkiye",
                "age": 25, "height": "1.85m", "foot": "Sol",
                "photo": photo(""),
                "stats": _s(mac=10, gol=0, asist=1),
                "market_value": "€5M",
            },
        ],
    },
    {
        "group": "Orta Saha",
        "group_en": "Midfielders",
        "icon": "⚙️",
        "color": "#1a2a3a",
        "players": [
            {
                "id": "kante", "number": 17, "name": "N'Golo Kanté",
                "role": "Defensif Orta Saha", "country": "🇫🇷", "country_name": "Fransa",
                "age": 35, "height": "1.68m", "foot": "Sağ",
                "photo": photo("Ngolo_Kante_2017.jpg"),
                "stats": _s(mac=12, gol=1, asist=2),
                "market_value": "€4M",
                "badge": "YENİ",
            },
            {
                "id": "edson-alvarez", "number": 8, "name": "Edson Álvarez",
                "role": "Defensif Orta Saha", "country": "🇲🇽", "country_name": "Meksika",
                "age": 27, "height": "1.90m", "foot": "Sağ",
                "photo": photo("Edson_%C3%81lvarez_2022.jpg"),
                "stats": _s(mac=28, gol=2, asist=1, sari=6),
                "market_value": "€27M",
            },
            {
                "id": "ismail-yuksek", "number": 6, "name": "İsmail Yüksek",
                "role": "Defensif Orta Saha", "country": "🇹🇷", "country_name": "Türkiye",
                "age": 26, "height": "1.83m", "foot": "Sağ",
                "photo": photo(""),
                "stats": _s(mac=26, gol=2, asist=4, sari=5),
                "market_value": "€20M",
            },
            {
                "id": "guendouzi", "number": 94, "name": "Mattéo Guendouzi",
                "role": "Merkez Orta Saha", "country": "🇫🇷", "country_name": "Fransa",
                "age": 26, "height": "1.85m", "foot": "Sağ",
                "photo": photo("1_Matt%C3%A9o_Guendouzi_2018_(cropped).jpg"),
                "stats": _s(mac=30, gol=3, asist=6),
                "market_value": "€28M",
                "badge": "YENİ",
            },
            {
                "id": "fall", "number": 60, "name": "Abdou Aziz Fall",
                "role": "Merkez Orta Saha", "country": "🇸🇳", "country_name": "Senegal",
                "age": 25, "height": "1.82m", "foot": "Sağ",
                "photo": photo(""),
                "stats": _s(mac=18, gol=1, asist=2),
                "market_value": "€8M",
            },
            {
                "id": "asensio", "number": 21, "name": "Marco Asensio",
                "role": "Ofansif Orta Saha", "country": "🇪🇸", "country_name": "İspanya",
                "age": 30, "height": "1.82m", "foot": "Sağ",
                "photo": photo("Marco_Asensio%2C_UEFA_U21_2017_c_(cropped).jpg"),
                "stats": _s(mac=32, gol=8, asist=9),
                "market_value": "€15M",
                "badge": "⭐",
            },
            {
                "id": "szymanski", "number": 7, "name": "Sebastian Szymański",
                "role": "Ofansif Orta Saha", "country": "🇵🇱", "country_name": "Polonya",
                "age": 26, "height": "1.76m", "foot": "Sol",
                "photo": photo("Sebastian_Szyma%C5%84ski%2C_Fenerbah%C3%A7e_v_Gaziantep_FK_13082023.jpg"),
                "stats": _s(mac=28, gol=5, asist=7),
                "market_value": "€22M",
            },
            {
                "id": "irfan-kahveci", "number": 11, "name": "İrfan Can Kahveci",
                "role": "Ofansif Orta Saha", "country": "🇹🇷", "country_name": "Türkiye",
                "age": 30, "height": "1.79m", "foot": "Sağ",
                "photo": photo(""),
                "stats": _s(mac=24, gol=4, asist=5),
                "market_value": "€7M",
            },
            {
                "id": "mert-hakan", "number": 9, "name": "Mert Hakan Yandaş",
                "role": "Ofansif Orta Saha", "country": "🇹🇷", "country_name": "Türkiye",
                "age": 31, "height": "1.74m", "foot": "Sağ",
                "photo": photo(""),
                "stats": _s(mac=22, gol=3, asist=4),
                "market_value": "€6M",
            },
        ],
    },
    {
        "group": "Forvet & Kanat",
        "group_en": "Forwards",
        "icon": "⚡",
        "color": "#2a1a1a",
        "players": [
            {
                "id": "kerem", "number": 9, "name": "Kerem Aktürkoğlu",
                "role": "Sol Kanat", "country": "🇹🇷", "country_name": "Türkiye",
                "age": 25, "height": "1.73m", "foot": "Sağ",
                "photo": photo("Muhammed_Kerem_Akt%C3%BCrko%C4%9Flu.png"),
                "stats": _s(mac=34, gol=12, asist=8),
                "market_value": "€22M",
                "badge": "⭐",
            },
            {
                "id": "duran", "number": 20, "name": "Jhon Durán",
                "role": "Santrfor", "country": "🇨🇴", "country_name": "Kolombiya",
                "age": 21, "height": "1.83m", "foot": "Sağ",
                "photo": photo("Jhon_Dur%C3%A1n_2023.jpg"),
                "stats": _s(mac=30, gol=18, asist=4),
                "market_value": "€35M",
                "badge": "🔥",
            },
            {
                "id": "dorgeles-nene", "number": 45, "name": "Dorgeles Nene",
                "role": "Sağ Kanat", "country": "🇲🇱", "country_name": "Mali",
                "age": 23, "height": "1.74m", "foot": "Sol",
                "photo": photo(""),
                "stats": _s(mac=26, gol=6, asist=5),
                "market_value": "€20M",
            },
            {
                "id": "oguz-aydin", "number": 70, "name": "Oğuz Aydın",
                "role": "Sol Kanat", "country": "🇹🇷", "country_name": "Türkiye",
                "age": 25, "height": "1.76m", "foot": "Sağ",
                "photo": photo(""),
                "stats": _s(mac=24, gol=4, asist=6),
                "market_value": "€7M",
            },
            {
                "id": "musaba", "number": 20, "name": "Anthony Musaba",
                "role": "Sol Kanat", "country": "🇳🇱", "country_name": "Hollanda",
                "age": 24, "height": "1.77m", "foot": "Sol",
                "photo": photo(""),
                "stats": _s(mac=16, gol=3, asist=3),
                "market_value": "€12M",
            },
            {
                "id": "emre-mor", "number": 26, "name": "Emre Mor",
                "role": "Sağ Kanat", "country": "🇹🇷", "country_name": "Türkiye",
                "age": 28, "height": "1.69m", "foot": "Sol",
                "photo": photo("Emre_Mor_2018.jpg"),
                "stats": _s(mac=14, gol=2, asist=3),
                "market_value": "€500K",
            },
        ],
    },
]

STAFF = [
    {
        "role": "Teknik Direktör (Vekâleten)",
        "name": "Zeki Murat Göle",
        "country": "🇹🇷",
        "note": "Tedesco'nun 27 Nisan'da ayrılmasının ardından göreve geldi",
        "photo": "",
    },
    {
        "role": "Yardımcı Antrenör",
        "name": "Gökhan Gönül",
        "country": "🇹🇷",
        "note": "Efsane sağ bek, antrenör olarak devam ediyor",
        "photo": photo("Gökhan_Gönül_2018.jpg"),
    },
    {
        "role": "Kaleci Antrenörü",
        "name": "Sandro Zufic",
        "country": "🇭🇷",
        "note": "",
        "photo": "",
    },
    {
        "role": "Atletik Performans",
        "name": "Halil Filik",
        "country": "🇹🇷",
        "note": "",
        "photo": "",
    },
    {
        "role": "Kulüp Başkanı",
        "name": "Sadettin Saran",
        "country": "🇹🇷",
        "note": "6-7 Haziran'da seçim — adaylığını koymayacak",
        "photo": "",
    },
]

PHOTO_CREDIT = "Fotoğraflar: Wikimedia Commons (CC lisansı) — Eğitim/test amaçlı"
TM_URL = "https://www.transfermarkt.com/fenerbahce/kader/verein/36"


def total_players():
    return sum(len(g["players"]) for g in SQUAD)


def get_player(player_id):
    for group in SQUAD:
        for p in group["players"]:
            if p["id"] == player_id:
                return p, group["group"]
    return None, None
