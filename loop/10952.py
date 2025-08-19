import sys
while True:
    a,b = sys.stdin.readline().split()
    if a == "0" and b == "0":
        break
    else:
        print(int(a)+int(b))
