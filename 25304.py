#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 25304                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: hunyji3 <boj.kr/u/hunyji3>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/25304                          #+#        #+#      #+#     #
#    Solved: 2025/08/19 17:53:34 by hunyji3       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
x = int(input())
n = int(input())
sum = 0
for i in range(n):
    a,b = map(int, input().split())
    sum = sum + (a*b)

if x == sum:
    print("Yes")
else:
    print("No")