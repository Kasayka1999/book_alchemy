# -*- coding: utf-8 -*-
"""
Fenerbahçe kadro verisi.

NOT: Bu liste 2025-26 sezonu bilgilerine dayanmaktadır. Transfer dönemlerinde
kadro değişebilir. Oyuncu eklemek/çıkarmak veya bilgileri güncellemek için
sadece bu dosyayı düzenlemen yeterli. Gerçek oyuncu fotoğrafı eklemek için
ilgili oyuncunun "photo" alanına bir resim URL'si yapıştır; boş bırakırsan
isimden otomatik bir avatar oluşturulur.

Alanlar:
  number   -> forma numarası
  name     -> oyuncu adı
  role     -> mevki detayı (ör. "Stoper", "Sol Bek")
  country  -> uyruk (bayrak emojisi)
  age      -> yaş
  photo    -> (opsiyonel) gerçek fotoğraf URL'si
"""

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
            {"number": 1,  "name": "Ederson",              "role": "Kaleci", "country": "🇧🇷", "age": 32, "photo": ""},
            {"number": 50, "name": "Dominik Livaković",    "role": "Kaleci", "country": "🇭🇷", "age": 31, "photo": ""},
            {"number": 34, "name": "İrfan Can Eğribayat",  "role": "Kaleci", "country": "🇹🇷", "age": 27, "photo": ""},
            {"number": 35, "name": "Tarık Çetin",          "role": "Kaleci", "country": "🇹🇷", "age": 28, "photo": ""},
        ],
    },
    {
        "group": "Defans",
        "icon": "🛡️",
        "players": [
            {"number": 37, "name": "Milan Škriniar",       "role": "Stoper",  "country": "🇸🇰", "age": 31, "photo": ""},
            {"number": 4,  "name": "Çağlar Söyüncü",       "role": "Stoper",  "country": "🇹🇷", "age": 30, "photo": ""},
            {"number": 5,  "name": "Diego Carlos",         "role": "Stoper",  "country": "🇧🇷", "age": 33, "photo": ""},
            {"number": 3,  "name": "Jayden Oosterwolde",   "role": "Sol Bek", "country": "🇳🇱", "age": 24, "photo": ""},
            {"number": 13, "name": "Archie Brown",         "role": "Sol Bek", "country": "🏴",  "age": 23, "photo": ""},
            {"number": 19, "name": "Nélson Semedo",        "role": "Sağ Bek", "country": "🇵🇹", "age": 32, "photo": ""},
            {"number": 2,  "name": "Mert Müldür",          "role": "Sağ Bek", "country": "🇹🇷", "age": 27, "photo": ""},
            {"number": 17, "name": "Bright Osayi-Samuel",  "role": "Sağ Bek", "country": "🇳🇬", "age": 28, "photo": ""},
            {"number": 24, "name": "Levent Mercan",        "role": "Sol Bek", "country": "🇹🇷", "age": 25, "photo": ""},
        ],
    },
    {
        "group": "Orta Saha",
        "icon": "⚙️",
        "players": [
            {"number": 6,  "name": "İsmail Yüksek",        "role": "Ön Libero",   "country": "🇹🇷", "age": 26, "photo": ""},
            {"number": 8,  "name": "Sofyan Amrabat",       "role": "Ön Libero",   "country": "🇲🇦", "age": 29, "photo": ""},
            {"number": 28, "name": "Edson Álvarez",        "role": "Ön Libero",   "country": "🇲🇽", "age": 28, "photo": ""},
            {"number": 17, "name": "Fred",                 "role": "Merkez O.S.", "country": "🇧🇷", "age": 32, "photo": ""},
            {"number": 10, "name": "Anderson Talisca",     "role": "10 Numara",   "country": "🇧🇷", "age": 32, "photo": ""},
            {"number": 7,  "name": "Sebastian Szymański",  "role": "10 Numara",   "country": "🇵🇱", "age": 26, "photo": ""},
            {"number": 14, "name": "İrfan Can Kahveci",    "role": "Ofansif O.S.", "country": "🇹🇷", "age": 30, "photo": ""},
            {"number": 88, "name": "Mert Hakan Yandaş",    "role": "Merkez O.S.", "country": "🇹🇷", "age": 31, "photo": ""},
        ],
    },
    {
        "group": "Forvet & Kanat",
        "icon": "⚡",
        "players": [
            {"number": 9,  "name": "Youssef En-Nesyri",    "role": "Santrfor",  "country": "🇲🇦", "age": 28, "photo": ""},
            {"number": 11, "name": "Jhon Durán",           "role": "Santrfor",  "country": "🇨🇴", "age": 22, "photo": ""},
            {"number": 20, "name": "Allan Saint-Maximin",  "role": "Sol Kanat", "country": "🇫🇷", "age": 28, "photo": ""},
            {"number": 21, "name": "Cengiz Ünder",         "role": "Sağ Kanat", "country": "🇹🇷", "age": 28, "photo": ""},
            {"number": 97, "name": "Oğuz Aydın",           "role": "Sağ Kanat", "country": "🇹🇷", "age": 24, "photo": ""},
            {"number": 30, "name": "Dorgeles Nene",        "role": "Sol Kanat", "country": "🇲🇱", "age": 22, "photo": ""},
        ],
    },
]


def total_players():
    return sum(len(group["players"]) for group in SQUAD)
