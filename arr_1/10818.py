n = int(input())
arr1 = list(map(int, input().split()))

arr1.sort()
print(arr1[0], arr1[-1])