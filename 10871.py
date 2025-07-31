n,x = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = []
for i in arr1:
    if i < x :
        arr2.append(i)

for i in arr2:
    print(i, end=' ')
