#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
    动态规划模板，时间复杂度O(weight * count), 空间复杂度O(weight)
    :param W: 背包最大能装的重量
    :param n: 物品数量
    :param weight: 每件物品的重量
    :param value: 每件物品的价值
    :return: 背包装下的最大价值
    """

def dp(W, n, weight, value):

    K=[[0 for i in range(W+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif weight[i-1] > j: #如果第i件物品装不进去
                K[i][j] = K[i-1][j]
            else:  #如果第i件物品可以装进去
                K[i][j] = max(K[i-1][j],K[i-1][j-weight[i-1]]+value[i-1])
    print(K)
    print(K[n][W])
    return K[n][W]

def dp2(W, n, weight, value):
    K=[0 for i in range(W+1)]
    print(K)
    for i in range(n+1):
        for j in range(W,-1,-1):
            if i == 0 or j == 0:
                K[j] = 0
            elif weight[i-1] <= j:
                K[j] =max(K[j],K[j-weight[i-1]]+value[i-1])
    print(K)
    print(K[W])
    return K[W]
if __name__ == '__main__':
    W = 10
    n = 5
    weight = [2, 4, 5, 7, 9]
    value = [3, 5, 7, 8, 11]
    dp(W,n,weight,value)


# def knaspace(S,size,value,n):
#     K=[[0 for i in range(S+1)] for j in range(n+1)]
#     print(K)
#     for i in range(n+1):
#         for x in range(S+1):
#             if i==0 or x==0:
#                 K[i][x]=0
#             elif size[i-1]<=x:   #如果可以装进去
#                 K[i][x]=max(value[i-1]+K[i-1][x-size[i-1]],K[i-1][x])
#             else:  #如果装不进去
#                 K[i][x]=K[i-1][x]
#     return K
# if __name__=="__main__":
#     w=10
#     size=[3,4,5]
#     value=[4,5,6]
#     n=3
#     print("动态规划表：")
#     result=knaspace(w,size,value,n)
#     for list in result:
#         print(list)



