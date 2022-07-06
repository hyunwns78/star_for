# star3_print.py
for i in range(5,0,-1): #1range(A, B, C) A부터 C 숫자만큼의 간격으로 B-1 까지의 정수 범위를 반환합니다.
    for j in range(5-i):
        print(' ',end="")
    for j in range(i):
        print('*',end="")
        
    print('')
    