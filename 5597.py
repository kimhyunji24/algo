s = [0 for rows in range(30)]
# print(s)
for i in range(28):
    p = int(input())
    s[p-1] = 1
    # print(s)

for i in range(len(s)):
    if s[i] == 0:
        print(i+1)