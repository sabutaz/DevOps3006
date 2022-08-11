is_true = False
a = 2
b = 2.5
strOne = "One"
strThree = "Three"
print(a == b)
print(type(a == b))
print(type(a))

if a < b and (strOne != "Moshe" or not strThree == "Three"):
    print("a is smaller")
elif a == b:
    print("a equal b")
elif b > 1:
    print("b is bigger then 1")
else:
    print("b is smaller")


names = ["chanan", "tom", "zack", "aharon"]
name_to_find = "tom"
if names[0] == name_to_find or names[1] == name_to_find or names[2] == name_to_find or names[3] == name_to_find:
    print("we found ", name_to_find)
else:
    print("no")
if name_to_find in names:
    print(f"we found {name_to_find}")
else:
    print("no")
other_list = ["saby"]
if other_list:
    print("other list has value", len(other_list))
else:
    print("list is empty")


k = 5
f = 5
#list
t = [1, 2, 3]
e = [1, 2, 3]
# tupple
r = (1, 2, 3)
j = (1, 2, 3)
print(k == f)
print(k is f)
print(type(k) is int)
print(t == e)
print(t is e)
print(r == j)
print(r is j)
