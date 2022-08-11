def print_hello(name):
    print(f"hello {name}")

def great_names (name, exluded_name="michael", greeting_word="hello"):
    if name != exluded_name:
        print(f"{greeting_word} {name}" )

def multiply (x,y):
    result = x * y
    return result


great_names("saby")
bla = multiply(10, 4)
print(bla)


user_name = input("enter your name : ")
print(great_names(user_name))

