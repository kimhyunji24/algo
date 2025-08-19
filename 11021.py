#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11021                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: hunyji3 <boj.kr/u/hunyji3>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11021                          #+#        #+#      #+#     #
#    Solved: 2025/08/19 18:23:49 by hunyji3       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
t = int(input())
for i in range(t):
    a,b = sys.stdin.readline().split()
    print("Case #{}".format(i+1))
    print(int(a)+int(b))