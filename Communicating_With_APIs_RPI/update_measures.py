import requests
import json
##initial dictionary
x = {'patientid':0 , 'heartrate':0, 'temprature':0 ,'spo':0}
x.update({"patientid": 4}) #patient id based on what visit you are in 
#read sensor data then for example
temprature=40
heartrate=80
spo=30

x.update({"temprature": temprature})
x.update({"heartrate": heartrate})
x.update({"spo": spo})
## covert dictionary to json object 
sorted_string = json.dumps(x, indent=4, sort_keys=True)
#requesting API
url="http://IP_LOCAL_Network/DataBase_APIs/update_VS.php"
r = requests.post(url, json=x)
#only print the response
print(r.text)