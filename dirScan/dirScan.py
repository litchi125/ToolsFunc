# -*- coding: utf-8 -*-
# @Time     : 2024/7/10 14:11
# @Author   : H
# @File     : DirScan.py

import os


def dirScan(work_dir, getType="file", recursion=True, prefix=None, postfix=None):
    """
    目录遍历工具
    @param work_dir: 待遍历目录
    @param getType: 默认为"file"；[ 获取文件夹路径"dir"、文件"file"、都有"both" ]
    @param recursion: 是否递归遍历，默认为True； [ 若为True则递归；若为数字，则为递归深度；若为False，则不递归 ]
    @param prefix: 检查文件前缀
    @param postfix: 检查文件后缀
    @return: 检索到的文件或文件夹绝对路径列表
    """

    # filePathList：返回文件绝对路径列表
    filePathList = []
    # fileDirList：返回文件夹绝对路径
    fileDirList = []
    # 最终返回列表
    resultList = []

    getType = str(getType).lower()
    if getType not in ["dir", "file", "both"]:
        return ["[!]ERROR: param 'getType'not in ['dir','file','both']"]

    base_depth = work_dir.count(os.sep)

    for parent, dirnames, filenames in os.walk(work_dir):

        if getType != "file":
            for dir in dirnames:
                resultList.append(os.path.join(parent, dir))
        if getType != "dir":
            for filename in filenames:
                if prefix and postfix:
                    if filename.startswith(prefix) and filename.endswith(postfix):
                        resultList.append(os.path.join(parent, filename))
                elif prefix:
                    if filename.startswith(prefix):
                        resultList.append(os.path.join(parent, filename))
                elif postfix:
                    if filename.endswith(postfix):
                        resultList.append(os.path.join(parent, filename))
                else:
                    resultList.append(os.path.join(parent, filename))
        if isinstance(recursion, bool):
            # 控制是否递归
            if recursion:
                continue
            else:
                # 清空 dirnames 列表，防止 os.walk 进入子目录
                dirnames[:] = []
                break  # 只遍历第一层，之后跳出循环
        elif isinstance(recursion, int):
            # 控制递归深度
            curren_depth = parent.count(os.sep) - base_depth
            if curren_depth >= recursion:
                # 清空 dirnames 列表，防止 os.walk 进入子目录
                dirnames[:] = []
                break  # 只遍历第一层，之后跳出循环

    return resultList
