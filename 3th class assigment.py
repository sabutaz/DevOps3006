# 1 + 2
try:
    a = 1 / 0
except ZeroDivisionError:
    print("divided by ZERO error")

# 3
try:
    x = 1
finally:
    print("finally")
# finally is specified as a cleanup handel

# 4+5
try:
    a = 1 / 1
except ZeroDivisionError:
    print("divided by ZERO error")
except:
    print("try it")
# expression-less except  must be last and it catch all exceptions, but it is not recommended

# 5
# because it catch all exceptions even one that we want\need to catch

# 6
# except IOError - all error related to input an output such as file open error
# except ZeroDivisionEr
# ror - any divided by zero scenario

# internal help

def write_line_to_file(the_file_name,the_line):
    the_file = open(the_file_name, "a")
    the_file.writelines(the_line)
    the_file.close()

def print_the_file(the_file_name):
    file_to_print = open(the_file_name, "r")
    for name in file_to_print.readlines():
        print(name.strip())
    file_to_print.close()

# 7+8
words_file = "words.txt"
write_line_to_file(words_file,"saby\n")

# 9
print_the_file(words_file)

# 10
write_line_to_file(words_file, "סבי\n")
print_the_file(words_file)

# 11
from PIL import Image, ImageDraw
image_file = "haifa.png"
new_image_file = "shik.png"
haifa = Image.open(image_file)
print(haifa.format, haifa.format_description, f"{haifa.size}X{haifa.mode}")
haifa.show()
haifa.close()

im = Image.new('RGB', (500, 300), (128, 128, 128))
draw = ImageDraw.Draw(im)
draw.ellipse((100, 100, 200, 200), fill=(50, 50, 194), outline=(155, 0, 100))
draw.text((100, 80), text=new_image_file, fill=(50, 194, 194), outline=(0, 0, 0))
im.show()


















