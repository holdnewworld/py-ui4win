__author__ = 'huqinghua'
# coding=gbk

import string, os, commands, time

class CommonUtils():
    """������session"""
    exeRoot = ''

    @classmethod
    def SaveExePath(cls):
        cls.exeRoot = os.path.abspath(os.curdir)

    @classmethod
    def ReverseToExePath(cls):
        os.chdir(cls.exeRoot)