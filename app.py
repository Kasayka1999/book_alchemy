from flask import Flask, render_template
from players import SQUAD, TEAM_INFO, total_players

app = Flask(__name__)


@app.route('/')
def squad():
    return render_template(
        'squad.html',
        squad=SQUAD,
        team=TEAM_INFO,
        total=total_players(),
    )


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
