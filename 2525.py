h,m = map(int, input().split())
ml = int(input())
result_h, result_m = h, m

result_m = m+ml

if result_m >= 60 :
    result_h = h + result_m//60
    result_m = result_m%60


if result_h >= 24 :
    result_h = result_h%24

print(result_h, result_m)