def save_name(the_file):
    my_file = open(the_file, "a")
    current_name = input("Enter your name :")
    my_file.write(current_name + "\n")
    my_file.close()

def haim(avi)
    print(avi)
def show_names(the_file):
    my_file = open(the_file, "r")
    for name in my_file.readlines():
        print(name, end='')
    my_file.close()

for i in range(5):
    save_name("names.txt")
show_names("names.txt")
