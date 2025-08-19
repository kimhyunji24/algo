n = int(input())
s = list(map(int,input().split()))
#print(s)
m = max(s)
#print(m)
sum = 0
# print(len(s))

for i in range(n):
    #print(s)
    x = (s[i]/m)*100
    s[i]=x
    sum = sum + x

print(sum/n)
