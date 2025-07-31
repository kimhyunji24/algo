x,y,z = map(int, input().split())

x,y,z = sorted([x,y,z])

if x == y == z:
    print(10000 + x*1000)
elif x == y or y == z or x == z:
    print(1000 + y*100)    
else:
    print(z*100)