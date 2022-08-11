a = int(input("enter number"))
b = int(input("enter number"))
result = a / b
print(result)

import requests
try:
    respons = requests.get("httpr://saby.com")
except Exception as e:
    print("something went wrong")
    print(e.args)
print("END")

try:
    f = int(input("enter number"))
    r = 5 / 0
except ZeroDivisionError:
    print("divided by ZERO error")
except ValueError:
    print("enter legal numbers")
except BaseException as e:
    print("somethink went wrong, here is why")
    print(e.args)

