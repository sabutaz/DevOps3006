import datetime
import requests
from time import sleep

response = requests.get("https://github.com")
if response.status_code == 200:
    print("Github is up and running")
print(datetime.datetime.now())
sleep(10)
print(datetime.datetime.now())

