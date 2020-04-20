#!/usr/bin/env python
# encoding: utf-8


def sum_num(*args):
    res = 0
    for num in args:
        res += num
    return res

result = sum_num(1,2,3,4,5,6,7,8)
print(result)

def sum_num2(**kwargs):
    result = 0
    print(kwargs)
    for x in kwargs:
        result += kwargs[x]
    return result

sum_num2(a=1,b=2)