n,m = map(int,input().split())
s = [0 for row in range(n)]


for p in range(m):
    i,j,k = map(int,input().split())
    #i ~j바구니에 k - 공번호적힌 공을 넣음
    #이미 공이 있으면 공 빼고 마지막 넣은 공만 넣음.
    for q in range(i-1,j):
        if s[q] == 0:   
            s[q] = k
        else :
            s[q] = k

for i in s:
    print(i, end=' ')
