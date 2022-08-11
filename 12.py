my_file = open("read_this.txt")
for line in my_file.readlines():
    print(line, end='')
print("----------------------")
my_file.seek(4)
for line in my_file.readlines():
    print(line.strip())
print("----------------------")

