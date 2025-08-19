h,m = map(int, input().split())


if m >= 45 :
    m = m-45

elif m < 45 :
    m_l = 45-m
    m = 60-m_l
    if 0 < h < 24 :
        h = h-1
    else : 
        h = 23

print(h, m)
