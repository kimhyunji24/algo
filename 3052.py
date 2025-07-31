m = []
for i in range(10):
    x = int(input())
    if int(x%42) not in m:
        m.append(x%42)
print(len(m))