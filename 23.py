import requests
response = requests.get("http://localhost:5001/whatismyname")
expected = "saved new car"
actual = response.text
assert expected == actual
