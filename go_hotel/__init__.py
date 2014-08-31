from flask import Flask

go_hotel = Flask(__name__)
from .config import config
go_hotel.config.update(**config)

from flask import Flask
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://{username}:{password}@{server}/{db}'.format(**config), echo=True)


from go_hotel import views

