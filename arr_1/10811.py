n,m = map(int, input().split())
s = list(range(1,n+1))
# print(s)

#my_list[start_index:end_index+1] = my_list[start_index:end_index+1][::-1]

for k in range(m):
    i,j = map(int, input().split())
    s[i-1:j] = s[i-1:j][::-1]
    # print(s)
for i in s:
    print(i,end=" ")
