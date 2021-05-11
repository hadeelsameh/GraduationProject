import requests
import json
import time


### check for time now
time_now = time.localtime() 
day = time.strftime("%Y-%m-%d",time_now)
timeStamp=time.strftime("%H:%M:%S",time_now)


##dictionary to pass to api
x = {"day":str(day),"time":str(timeStamp)}

## covert dictionary to json object 
sorted_string = json.dumps(x, indent=4, sort_keys=True)
#requesting API
url="http://IP_LOCAL_NETWORK/Database_APIs/NextVisitRobot.php"
r = requests.post(url, json=x)
#the response
try: #there are visits today
    arr=json.loads(r.text)
    patient_id=arr[0]['patientid']
    print(patient_id)
    #arr[0].get('patientid' , "no key")
    isvideocall=arr[0]['isvideocall']
    print(isvideocall)
except: # no upcoming visits today
    print(r.text)