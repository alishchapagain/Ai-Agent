import json
import requests
city_name = input("Enter a City Name: ")
api_key = '59915e99f02069b8fec48f1ac1ab75f0'
api_url = f'https//api.openwhethermap.org/data/2.5/whethermap'
get_server_information = requests.get(api_url)
json_data = get_server_information.json()

preety_data = json.dumps(json_data,indent=4)
print(preety_data)