import requests
import json
from datetime import datetime
import os
def get_weather():
	result = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Brooklyn,USA&APPID=5911c537ec91cabcb8af2291800e0c38")
	
	if result.status_code == 200 :
		json_data = result.json()
		file_name = str(datetime.now().date()) + '.json'
		dir_name = os.path.join(os.path.dirname(__file__), 'data')
		tot_name = os.path.join(dir_name, file_name)
		if not os.path.exists(dir_name):
			os.makedirs(dir_name)

		with open(tot_name, 'w') as outputfile:
			json.dump(json_data, outputfile)
	else:
		print("error in API call")


if __name__ == "__main__":
	get_weather()