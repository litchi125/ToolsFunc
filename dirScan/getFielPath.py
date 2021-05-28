#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 14:33
# @Author  : H
# @File    : getFielPath.py


def getfielpath(filepath, sub=[]):
    """
    递归方式实现目录遍历
    :param filepath:
    :param sub:
    :return:
    """
    if os.path.isdir(filepath):
        # 如果绝对路径下的文件夹
        for i in os.listdir(filepath):  # i文件名
            path2 = os.path.join(filepath, i)  # 拼接绝对路径
            if os.path.isdir(path2):  # 判断如果是文件夹,调用本身
                getfielpath(path2, sub)
            else:
                sub.append(path2)
    elif os.path.isfile(filepath):
        # 如果绝对路径下的文件
        sub.append(filepath)
    else:
        print("File or path doesn\'t exit")
    return sub