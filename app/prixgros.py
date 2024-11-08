import datetime
import orjson
from dataclasses import dataclass
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    game = load_today_game()
    return game.json()


def load_today_game():
    game = Game(datetime.datetime.now().date(), "Aproz Cristal", None, None, 3.50)
    return game


@app.route("/guess", methods=["POST"])
def submit_guess():
    return request.json


@dataclass
class Game:
    date: datetime
    name: str
    article_link: str
    image_link: str
    price: float

    def __init__(self, date, name, article_link, image_link, price) -> None:
        self.date = date
        self.name = name
        self.article_link = article_link
        self.image_link = image_link
        self.price = price

    def json(self):
        return orjson.dumps(self)
