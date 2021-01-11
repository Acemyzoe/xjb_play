
from functools import partial
class F(partial):
    '6行代码实现管道'
    def __ror__(self, other):
        if isinstance(other, tuple):
            return self(*other)
        return self(other)

# 求十以下所有奇数的合：
print(range(10) | F(filter, lambda x: x % 2) | F(sum))

# 筛选字典中值为真的数据：
dict = {'q':1,'w':0}
print(dict | F(lambda d: {k: v for k, v in d.items() if v}))


'''Python 中的偏函数(functools.partial)'''
# 应用的场景是当我们要频繁调用某个函数时，其中某些参数是已知的固定值.

# 第一种做法：
def add(*args):
    return sum(args)
print(add(1, 2, 3) + 100)
print(add(5, 5, 5) + 100)

# 第二种做法
def add(*args):
    # 对传入的数值相加后，再加上100返回
    return sum(args) + 100
print(add(1, 2, 3))  # 106
print(add(5, 5, 5))  # 115 

def add(*args):
    return sum(args)
add_100 = partial(add, 100)
print(add_100(1, 2, 3))  # 106
add_101 = partial(add, 101)
print(add_101(1, 2, 3))  # 107

# partial 函数的功能就是：把一个函数的某些参数给固定住，返回一个新的函数。
basetwo = partial(int, base=2)
basetwo.__doc__ = 'Convert base 2 string to an int.'
print(basetwo('10010'),int('10010',2))