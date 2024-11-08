import datetime

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    game = load_today_game()
    return "<p>Hello, World!</p>"


def load_today_game():
    game = Game(datetime.datetime.now().date, "Aproz Cristal", None, None, 3.50)
    return game


class Game:
    date = None
    item_name = None
    migros_link = None
    migros_image = None
    price = None
