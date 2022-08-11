x_boom = 7
for i in range(1, 101):
    if i % x_boom != 0 and not str(x_boom) in str(i):
        print(i)
    else:
        print(i % x_boom)


