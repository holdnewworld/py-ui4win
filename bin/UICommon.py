__author__ = 'huqinghua'
# coding=gbk

import string, os, commands, time

from PyUI import *
from MsgBox import *
from PyFrameBase import *

def ShowMessageBox(hwnd, title, caption):
    mbox1 = PyFrameCreator()
    obj = mbox1.CreateForm(hwnd, 'MsgBox', 'MsgBox')
    obj.SetText("LblCaption", title)
    obj.SetText("txtMsg", caption)
    mbox1.ShowModal()

