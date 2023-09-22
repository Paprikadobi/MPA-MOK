#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Peter Cíbik"
__email__ = "xcibik00@vutbr.cz"
__copyright__ = "Copyright 2022, MPA-MOK"
__credits__ = ["Peter Cíbik" , "Sara Ricci"]


def ex1():
    print((29 + 32 + 17 + 84)/4)

def add(a, b):
    return (a + b)

def sub(a, b):
    return (a - b)

def mul(a, b):
    return (a * b)

def div(a, b):
    return (a / b)

def ex2():
    a = 12
    b = 6

    print(str(add(a, b)))
    print(str(sub(a, b)))
    print(str(mul(a, b)))
    print(str(div(a, b)))

def ex3(a, b):
    if (a < b):
        return -1
    elif (a == b):
        return 0
    else:
        return 1

def ex4():
    a = 36
    for num in range(a):
        print(num)

def ex5():
    a = [13,45,1,-10,273]
    i = 0
    sum = 0

    while i < len(a):
        sum += a[i]
        i += 1

    print(sum)

ex1()
ex2()
ex3(5, 6)
ex4()
ex5()