num = int(input())
arr1 = list(map(int, input().split()))
int1 = int(input())
cnt = 0
# print(arr1)

for i in range(len(arr1)):
    if arr1[i] == int1:
        cnt+=1

print(cnt)