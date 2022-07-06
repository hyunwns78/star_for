# star2_print.py
for i in range(1,6): #1부터 6-1까지
    for j in range(i):
        print('*',end="")
    for j in range(5-i):
        print(' ',end="")
    print('')