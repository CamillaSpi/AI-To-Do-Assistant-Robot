# importing the requests library 
 import requests 
# api-endpoint 
sender_id = 5
URL = "http://localhost:5005/"+sender_id+"/ali/tracker"
# sending get request and saving the response as response object 
r = requests.get(url = URL) 
# extracting data in json format 
data = r.json()

print(data)
