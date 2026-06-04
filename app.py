from flask import Flask, render_template, abort
from players import (
    SQUAD, STAFF, TEAM_INFO, RECENT_MATCHES, LEAGUE_TABLE,
    PHOTO_CREDIT, TM_URL, total_players, get_player
)

app = Flask(__name__)


@app.route('/')
def squad():
    return render_template(
        'squad.html',
        squad=SQUAD,
        staff=STAFF,
        team=TEAM_INFO,
        matches=RECENT_MATCHES,
        table=LEAGUE_TABLE,
        total=total_players(),
        credit=PHOTO_CREDIT,
        tm_url=TM_URL,
    )


@app.route('/oyuncu/<player_id>')
def player_detail(player_id):
    player, group = get_player(player_id)
    if player is None:
        abort(404)
    return render_template(
        'player.html',
        p=player,
        group=group,
        team=TEAM_INFO,
        credit=PHOTO_CREDIT,
        tm_url=TM_URL,
    )


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
