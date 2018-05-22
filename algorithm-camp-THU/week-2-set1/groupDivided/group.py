#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
描述
有n个正整数排成一排，你要将这些数分成m份（同一份中的数字都是连续的，不能隔开），同时数字之和最大的那一份的数字之和尽量小。

输入
输入的第一行包含两个正整数n，m。

接下来一行包含n个正整数。

输出
输出一个数，表示最优方案中，数字之和最大的那一份的数字之和。

样例1输入

5 2
2 1 2 2 3

样例1输出
5

样例1解释
若分成2和1、2、2、3，则最大的那一份是1+2+2+3=8；

若分成2、1和2、2、3，则最大的那一份是2+2+3=7；

若分成2、1、2和2、3，则最大的那一份是2+1+3或者是2+3，都是5；

若分成2、1、2、2和3，则最大的那一份是2+1+2+2=7。

所以最优方案是第三种，答案为5。
"""
