"""
Simple Command line app that returns address when user inputs a location.
This application uses google maps public API
written using python 2.7 !!!
install requests module to make sure this works !! pip install requests
enter "quit" when prompted for location to quit the program
"""

import urllib
import requests
maps_api = "https://maps.googleapis.com/maps/api/geocode/json?address="

while True:
	address = raw_input("Please Enter an Location: " )
	if address == "quit":
		break

	url = maps_api + urllib.quote(address)



	data = requests.get(url).json()


	api_status = data['status']
	print "API Status: %s" %api_status

	if api_status == "OK":
		for each in data['results'][0]['address_components']:
			print each['long_name']
