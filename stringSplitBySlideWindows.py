#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/11 16:41
# @Author  : H
# @File    : stringSplitBySlideWindows.py
from itertools import islice


def window(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ..."
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def windowSliding(seq, n):
    return ["".join(x) for x in window(seq, n)]


print(windowSliding("123456789",3))