n,m = map(int, input().split())
s = [0 for rows in range(n)]
for i in range(n):
    s[i] = i+1
# print(s)

temp = 0
for k in range(m):
    i,j = map(int, input().split())
    # print(i,j)
    x = s[i-1]
    y = s[j-1]
    s[i-1] = y
    s[j-1] = x
# print(s)
for i in s:
    print(i,end=' ')