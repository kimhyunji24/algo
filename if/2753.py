a = int(input())

if 1<=a<=4000 and a%4 == 0:
    if a%100 != 0 or a%400 == 0:
        print(1)
    else :
        print(0)
else :
    print(0)
