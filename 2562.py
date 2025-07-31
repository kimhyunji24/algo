arr1 = []
for i in range(9):
    x = int(input())
    arr1.append(x)

arr2 = arr1.copy()
arr1.sort()
# print(arr2)
print(arr1[-1])
print(arr2.index(arr1[-1])+1)
