# -*- coding: utf-8 -*-
# @Time     : 2024/7/10 14:11
# @Author   : H
# @File     : DirScan.py

import os


def dirScan(work_dir, getType="file", excludeFile=None, excludeDir=None, recursion=True, returnParentDir=False,
            prefix=None, postfix=None):
    """
    目录遍历工具
    @param work_dir: 待遍历目录
    @param getType: 默认为"file"；[ 获取文件夹路径"dir"、文件"file"、都有"both" ]
    @param excludeFile: 排除文件，值类型：字符串或list列表
    @param excludeDir: 排除目录，值类型：字符串或list列表
    @param recursion: 是否递归遍历，默认为True; 值类型：bool、int；[ 若为True则递归；若为数字，则为递归深度；若为False，则不递归 ]
    @param returnParentDir: 遍历目录时，若当前目录存在子目录，则不返回当前目录;默认为False：不返回：值类型：bool ;
    @param prefix: 检查文件前缀；值类型：str
    @param postfix: 检查文件后缀；值类型：str
    @return: 检索到的文件或文件夹绝对路径列表
    """

    # filePathList：返回文件绝对路径列表
    filePathList = []
    # fileDirList：返回文件夹绝对路径
    fileDirList = []
    # 最终返回列表
    resultList = []

    # excludeFile 输入类型，调整
    if excludeFile is None:
        excludeFile = []
    elif type(excludeFile) is str:
        excludeFile = [excludeFile]
    # excludeDir 输入类型，调整
    if excludeDir is None:
        excludeDir = []
    elif type(excludeDir) is str:
        excludeDir = [excludeDir]

    getType = str(getType).lower()
    if getType not in ["dir", "file", "both"]:
        return ["[!]ERROR: param 'getType'not in ['dir','file','both']"]

    base_depth = work_dir.count(os.sep)

    for parent, dirnames, filenames in os.walk(work_dir):

        # 排除 excludeDir 中 目录
        for excludeDirOne in excludeDir:
            if excludeDirOne in dirnames:
                dirnames.remove(excludeDirOne)
        # 排除 excludeFile 中 文件
        for excludeFileOne in excludeFile:
            if excludeFileOne in filenames:
                filenames.remove(excludeFileOne)

        if getType != "file":
            # returnParentDir 当获取目录时，若存在子目录，则不返回本级目录
            if dirnames and not returnParentDir and parent in resultList:
                resultList.remove(parent)
            for dir in dirnames:
                dirPath = os.path.join(parent, dir)
                curren_depth = dirPath.count(os.sep) - base_depth
                # 目录的递归深度控制
                if curren_depth <= recursion or recursion is True:
                    resultList.append(dirPath)

        if getType != "dir":
            for filename in filenames:
                filePath = os.path.join(parent, filename)
                curren_depth = filePath.count(os.sep) - base_depth
                # 文件的递归深度控制
                if curren_depth > recursion and recursion is not True or recursion is False:
                    continue
                if prefix and postfix:
                    if filename.startswith(prefix) and filename.endswith(postfix):
                        resultList.append(filePath)
                elif prefix:
                    if filename.startswith(prefix):
                        resultList.append(filePath)
                elif postfix:
                    if filename.endswith(postfix):
                        resultList.append(filePath)
                else:
                    resultList.append(filePath)

    return resultList
