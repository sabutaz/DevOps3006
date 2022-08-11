string_to_print = "hello world"

print(string_to_print)
print(string_to_print)

print(list(range(17, 2, -3)))

for i in range(7):
    print("hello saby")


pets = ["chanan", "tom", "zack", "aharon"]
for pet in pets:
    print(pet, end=' ')

for i in range(len(pets)):
    print(pets[i])

a = 0
while a < 5:
    print(a)
    a = a + 1

for pet in pets:
    if pet == "cat":
        break
    print(pet)


