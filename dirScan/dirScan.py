#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 14:22
# @Author  : H
# @File    : dirScan.py
import os


def dirScan(work_dir, postfix=None):
    """
    通过os.work()内置模块函数，进行文件遍历
    :param work_dir: 目标路径
    :param postfix: 需要筛选的文件后缀名
    :return:
    """
    # filePathList：返回文件绝对路径列表
    filePathList = []
    # fileDirList：返回文件夹绝对路径
    fileDirList = []
    for parent, dirnames, filenames in os.walk(work_dir):
        # for dir in dirnames:
        #     fileDirList.append(os.path.join(parent, dir))
        for filename in filenames:
            if postfix:
                if filename.endswith(postfix):
                    filePathList.append(os.path.join(parent, filename))
            else:
                filePathList.append(os.path.join(parent, filename))
    return filePathList



