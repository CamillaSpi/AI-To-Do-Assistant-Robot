# importing the requests library 
import requests 
import os
import json
# api-endpoint 
REF_PATH = os.path.dirname(os.path.abspath(__file__))
sender_id = '5'
URL = "http://localhost:5005/conversations/{"+sender_id+"}/tracker"
# sending get request and saving the response as response object 
print(URL)
r = requests.get(url = URL) 
# extracting data in json format 
data = r.json()
print("sono in load")
try:
    with open(REF_PATH + '/data/recognize_user.json', 'w') as out_file:
        json.dump(data, out_file)
except:
    print('gscrst')
print(data)
