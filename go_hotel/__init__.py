from flask import Flask

go_hotel = Flask(__name__)
from .config import config
go_hotel.config.update(**config)

from go_hotel import views
