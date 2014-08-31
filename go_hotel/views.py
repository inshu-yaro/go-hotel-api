from flask import jsonify, request, Response
from go_hotel import go_hotel
from rakuten import RakutenClient
import json

@go_hotel.route('/')
def index():
    return jsonify({})

@go_hotel.route('/hotel')
def send_hotels():
	client = RakutenClient("1023510790824912140")
	# response = client.travel.vacant_hotel_search(checkin_date="2014-10-01", checkout_date="2014-10-01", latitude=128440.51,longitude=503172.21,searchRadius=1)
	response = client.travel.vacant_hotel_search(**request.args)
	return json.dumps(response, ensure_ascii=False)