#!/usr/bin/env python
# -*- coding: utf8 -*-

# def is_palindrome(n):
#     '回数'
#     return str(n)==str(n)[::-1]
# # 测试:
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')

# # 海象运算符/赋值表达式
# if (age:= 20) > 18:
#     print("已经成年了")

# # 模块重载
# from foo import bar # 1
# import importlib
# importlib.reload(bar) # 2
# bar.__spec__.loader.load_module() # 3

import numpy as np
a = np.linspace(0,100,10**6) # 创建一个长度为100万的数组
from math import sin
import numba as nb

@nb.vectorize()
def nb_vec_sin(a):
    return sin(a)

def demo():
    nb_vec_sin(a)
    # np.sin(a)

if __name__ == "__main__":
    import timeit
    print(timeit.timeit("demo()",setup="from __main__ import demo",number=1000))