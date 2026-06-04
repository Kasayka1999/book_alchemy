import os, json
from flask import Flask, render_template, abort
from players import (
    SQUAD, STAFF, TEAM_INFO, RECENT_MATCHES, LEAGUE_TABLE,
    PHOTO_CREDIT, TM_URL, total_players, get_player
)

app = Flask(__name__)

# Render build'de indirilen fotoğraf haritasını yükle (varsa)
_MAP_FILE = os.path.join(os.path.dirname(__file__), "static", "images", "players", "map.json")

def _load_photo_map():
    try:
        with open(_MAP_FILE) as f:
            return json.load(f)
    except Exception:
        return {}

PHOTO_MAP = _load_photo_map()


def _apply_local_photos(squad):
    """map.json'daki yerel fotoğraflarla players listesini zenginleştir."""
    for group in squad:
        for p in group["players"]:
            local = PHOTO_MAP.get(p["id"])
            if local:
                p = dict(p)  # kopya — orijinali bozma
                p["photo"] = local
            # p zaten değiştirildi; orijinal liste etkilenmez
    return squad


@app.route("/")
def squad():
    return render_template(
        "squad.html",
        squad=_apply_local_photos(SQUAD),
        staff=STAFF,
        team=TEAM_INFO,
        matches=RECENT_MATCHES,
        table=LEAGUE_TABLE,
        total=total_players(),
        credit=PHOTO_CREDIT,
        tm_url=TM_URL,
    )


@app.route("/oyuncu/<player_id>")
def player_detail(player_id):
    player, group = get_player(player_id)
    if player is None:
        abort(404)
    # Yerel fotoğraf varsa kullan
    local = PHOTO_MAP.get(player_id)
    if local:
        player = dict(player)
        player["photo"] = local
    return render_template(
        "player.html",
        p=player,
        group=group,
        team=TEAM_INFO,
        credit=PHOTO_CREDIT,
        tm_url=TM_URL,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
