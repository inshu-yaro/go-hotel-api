from flask import jsonify
from go_hotel import go_hotel

@go_hotel.route('/')
def index():
    return jsonify({})
