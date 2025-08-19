#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11022                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: hunyji3 <boj.kr/u/hunyji3>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11022                          #+#        #+#      #+#     #
#    Solved: 2025/08/19 18:26:07 by hunyji3       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
n = int(input())
for i in range(n):
    a,b = sys.stdin.readline().split()
    print("Case #{}: {} + {} = {}".format(i+1,int(a),int(b),int(a)+int(b)))