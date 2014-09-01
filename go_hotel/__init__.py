from flask import Flask
from flask.ext.cors import CORS
from werkzeug.contrib.fixers import ProxyFix

go_hotel = Flask(__name__)
cors = CORS(go_hotel)
from .config import config
go_hotel.config.update(**config)

go_hotel.wsgi_app = ProxyFix(go_hotel.wsgi_app)

from flask import Flask
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://{username}:{password}@{server}/{db}'.format(**config), echo=True)


from go_hotel import views

