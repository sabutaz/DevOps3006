# A
x = 9
y = 8
if x > y:
    print("X is Bigger")
elif x < y:
    print("X is Smaller")
elif x == y:
    print("X equal Y")
else:
    print("parameters error")

# B
for i in range(5):
    print(f"I is {i}")

# C
var = 3
if var == 1:
    print("summer")
elif var == 2:
    print("winter")
elif var == 3:
    print("fall")
elif var == 4:
    print("spring")

# D - 10 times
count = 1
while count < 11:
    print(count)
    count = count + 1

# E
age = 47
first_letter = "s"
currency_rate = 3.47
boolean_aboard = True
apartment_number = 7
print(f"age {age} first letter {first_letter} dollar rate {currency_rate} \nDid you flew abroad {boolean_aboard} apartment number {apartment_number}")
print(currency_rate+age)

# F
phone_number = input("what is your phone number : ")
print(f"your phone number is {phone_number}")

# G
def printHello():
    print("hello")

def calculate():
    print(5+3.2)

printHello()
calculate()

# H
def my_name(name):
    print(name)

def div_it(num1):
    num1 = num1 / 2
#    print(int(num1))
    return num1

my_name("saby")
print(f"the number is {div_it(8)}")

# I
def two(number1,number2):
    return number1 + number2

def space(str1,str2):
    return str1 + " " + str2

print(two(3,8))
print(space("saby","behar"))

# K option 1
for j in range(10):
    print("*" * j)

# K option 2
for j in range(10):
    for k in range(10):
        if j < k :
            print("*", end="")
    print()

# L
ranger = 7
for m in range(ranger):
    for n in range(ranger):
        if (m == n) or (n + m == ranger - 1):
            print("*", end="", sep="")
        else:
            print(" ", end="", sep="")
    print()


# M
def Read_from_user():
    print("type number :")
    return int(input())
w = Read_from_user()
v = int(w / 10)
x = int(w % 10)
print(int(v+x))







