__author__ = 'huqinghua'
# coding=gbk

import string, os, commands, time
import threading
from PyUI import *
from MsgBox import *
from PyFrameBase import *

def PyThreadFunc(PyClassInstance):
    try:
        PyClassInstance.EncryptAndPack(PyClassInstance)
    except Exception, e:
        PyLog().LogText(str(e))

    time.sleep(100)

class MainFrame(PyFrameBase):
    def __init__(self):
        super(MainFrame, self).__init__()
        #PyFrameBase.__init__(self)
        self.msg = 'msg origer'

    #virtual LPCSTR GetSkinFile();
    def GetSkinFile(self):
        return 'main.xml'

    #virtual LPCSTR GetWindowClassName() const;
    def GetWindowClassName(self):
        return 'MainFrame'

    #virtual LPCSTR GetWindowClassName() const;
    def TestObj(self, msg):
        self.msg = msg

    def EncryptAndPack(self, selfself):
        selfself.SetText("LblStatus", '������������ϰ�ť')
        selfself.SetText("txtDiagnose", '������������ϰ�ť')

    #virtual void OnNotify(LPCSTR sendor, LPCSTR sType, WPARAM wParam, LPARAM lParam);
    def OnNotify(self, sendor, sType, wParam, lParam):
        if sType == "click":
            if sendor == "BtnClose":
                self.ExitApp()
            elif sendor == "btnPyTest":
                mbox1 = PyFrameCreator()
                obj = mbox1.CreateForm(self.GetHWnd(), 'MsgBox', 'MsgBox')
                obj.SetText("LblCaption", '�Ի������')
                obj.SetText("txtMsg", '�����˶Ի���ť')
                mbox1.ShowModal()
            elif sendor == "btnDriverInstall1":
                PyLog().LogText(self.msg)
                lblStatus = self.PyFindControl("LblStatus")
                msg = lblStatus.GetText()
                lblStatus.SetText(msg + '�����˰�װ������ť')
                txtDiagnose = self.PyFindControl("txtDiagnose")
                txt = txtDiagnose.GetText()
                txtDiagnose.SetVisible(not txtDiagnose.IsVisible())
                txtDiagnose.SetText(txt + '\n' + '�����˰�װ������ť')

            elif sendor == "btnEncrypt":
                funcTabLayout = self.PyFindTabLayout("FunctionTabs")
                funcTabLayout.SelectItem(3)
                self.SetText("LblStatus", '������bug��ⰴť')
                self.SetText("txtDiagnose", '������bug��ⰴť')
            elif sendor == "btnDriverDiagnose":
                funcTabLayout = self.PyFindTabLayout("FunctionTabs")
                funcTabLayout.SelectItem(3)
                txtDiagnose = self.PyFindControl("txtDiagnose")
                txtDiagnose.SetVisible(True)
                self.SetText("txtDiagnose", '')
                self.SetText("LblStatus", '')
                #time.sleep(100)
                t = threading.Thread(target=PyThreadFunc,args=(self,))
                t.start()
            elif sendor == 'btnOpenLog':
                pass
                #win32api.ShellExecute(0, 'open', 'e:\\applog.ini', None, "", 1)
            elif sendor == 'btnDriverInstall':
                funcTabLayout = self.PyFindTabLayout("FunctionTabs")
                funcTabLayout.SelectItem(1)

def PyAppInit():
    pyFrameObj = PyFrameCreator()
    obj = pyFrameObj.CreateForm(0, 'PyMain', 'MainFrame')
    obj.TestObj('msg changed')
    pyFrameObj.ShowModal()


