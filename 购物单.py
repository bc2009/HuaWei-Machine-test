#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 17:03
# @Author  : 一叶知秋
# @File    : 购物单.py
# @Software: PyCharm
"""
题目描述
王强今天很开心，公司发给N元的年终奖。王强决定把年终奖用于购物，他把想买的物品分为两类：主件与附件，附件是从属于某个主件的，下表就是一些主件与附件的例子：
主件	附件
电脑	打印机，扫描仪
书柜	图书
书桌	台灯，文具
工作椅	无
如果要买归类为附件的物品，必须先买该附件所属的主件。每个主件可以有 0 个、 1 个或 2 个附件。附件不再有从属于自己的附件。王强想买的东西很多，为了不超出预算，他把每件物品规定了一个重要度，分为 5 等：用整数 1 ~ 5 表示，第 5 等最重要。他还从因特网上查到了每件物品的价格（都是 10 元的整数倍）。他希望在不超过 N 元（可以等于 N 元）的前提下，使每件物品的价格与重要度的乘积的总和最大。
    设第 j 件物品的价格为 v[j] ，重要度为 w[j] ，共选中了 k 件物品，编号依次为 j 1 ， j 2 ，……， j k ，则所求的总和为：
v[j 1 ]*w[j 1 ]+v[j 2 ]*w[j 2 ]+ … +v[j k ]*w[j k ] 。（其中 * 为乘号）
    请你帮助王强设计一个满足要求的购物单。

输入描述:
输入的第 1 行，为两个正整数，用一个空格隔开：N m

（其中 N （ <32000 ）表示总钱数， m （ <60 ）为希望购买物品的个数。）


从第 2 行到第 m+1 行，第 j 行给出了编号为 j-1 的物品的基本数据，每行有 3 个非负整数 v p q

（其中 v 表示该物品的价格（ v<10000 ）， p 表示该物品的重要度（ 1 ~ 5 ）， q 表示该物品是主件还是附件。如果 q=0 ，表示该物品为主件，如果 q>0 ，表示该物品为附件， q 是所属主件的编号）


输出描述:
 输出文件只有一个正整数，为不超过总钱数的物品的价格与重要度乘积的总和的最大值（ <200000 ）。
示例1
输入
复制
1000 5
800 2 0
400 5 1
300 5 1
400 3 0
500 2 0
输出
复制
2200
"""


def main():
    N, m = map(int, input().split())
    f = [0] * N  # 购物单总价值
    # 分组背包，每组有四种情况，a.主件 b.主件+附件1 c.主件+附件2 d.主件+附件1+附件2
    v = [[0 for i in range(4)] for j in range(m + 1)]  # 每组的资金
    w = [[0 for i in range(4)] for j in range(m + 1)]  # 每组的重要度

    N = N // 10  # 价格为10的整数倍，节省时间
    for i in range(1, m + 1):
        x, y, z = map(int, input().split())
        x = x // 10
        if z == 0:
            # 主件，同时给每个组合初始化主件的金额跟重要度
            for t in range(4):
                v[i][t], w[i][t] = v[i][t] + x, w[i][t] + x * y
        elif v[z][1] == v[z][0]:  # 附件且a==b，意味着附件1没加入，这时候累加b跟d情况
            v[z][1], w[z][1] = v[z][1] + x, w[z][1] + x * y
            v[z][3], w[z][3] = v[z][3] + x, w[z][3] + x * y
        else:  # 附件且a!=b，意味着附件1加入了附件2没加入，这时候累加c跟d情况
            v[z][2], w[z][2] = v[z][2] + x, w[z][2] + x * y
            v[z][3], w[z][3] = v[z][3] + x, w[z][3] + x * y
    # m:加入购物单的物品个数上限
    for i in range(1, m + 1):
        # n:购物总资金上限，只能倒序遍历，因为背包的思维是可用空间从大到小，求当前每个子状态的最优，
        # 如果顺序遍历，背包容量变大，之前遍历的子状态的最优结论就被推翻了
        for j in range(N, -1, -1):
            for k in range(4):
                if j >= v[i][k]:
                    # 将每组的购物资金 整体视为 一个容量，这样才不会出现主件重复放入的情况，这也是其他答案犯错的地方
                    # f[j]：表示总花费为j钱时的最大购物价值
                    f[j] = max(f[j], f[j - v[i][k]] + w[i][k])
    print(10 * f[N])


if __name__ == '__main__':
    main()
