__author__ = 'huqinghua'
# coding=gbk

import string, os, commands, time
import threading
from distutils import dir_util
from shutil import make_archive
import win32api

from PyUI import *
from MsgBox import *
from PyFrameBase import *

def execute_dos_cmd(cmd):
    output = os.popen(cmd)
    for line in output:
        PyLog().LogText(line)


def generateConfig(solutionPath):
    flag = ''
    commonFile=file(solutionPath + '\\common.lua','r')
    shuajiFile=file(solutionPath + '\\shuaji.lua','r+')

    temp=file(solutionPath + '\\tmp.lua','w+')
    for line in commonFile:
        temp.write(line)
    temp.write('\n')
    for line in shuajiFile:
        temp.write(line)
    temp.flush()
    temp.close()

    shuajiFile.close()
    os.remove(solutionPath + '\\shuaji.lua')
    if os.path.isfile(solutionPath + '\\config.lua'):
        os.remove(solutionPath + '\\config.lua')
    os.rename(solutionPath + '\\tmp.lua', solutionPath + '\\config.lua')

def generatebackup(solutionPath):
    flag = ''
    commonFile=file(solutionPath + '\\common.lua','r')
    shuajiFile=file(solutionPath + '\\systembackup.lua','r+')

    temp=file(solutionPath + '\\tmp.lua','w+')
    for line in commonFile:
        temp.write(line)
    temp.write('\n')
    for line in shuajiFile:
        temp.write(line)
    temp.flush()
    temp.close()

    shuajiFile.close()
    os.remove(solutionPath + '\\systembackup.lua')
    os.rename(solutionPath + '\\tmp.lua', solutionPath + '\\systembackup.lua')

def generaterecovery(solutionPath):
    flag = ''
    commonFile=file(solutionPath + '\\common.lua','r')
    shuajiFile=file(solutionPath + '\\systemrestore.lua','r+')

    temp=file(solutionPath + '\\tmp.lua','w+')
    for line in commonFile:
        temp.write(line)
    temp.write('\n')
    for line in shuajiFile:
        temp.write(line)
    temp.flush()
    temp.close()

    shuajiFile.close()
    os.remove(solutionPath + '\\systemrestore.lua')
    os.rename(solutionPath + '\\tmp.lua', solutionPath + '\\systemrestore.lua')

def encrypt(solutionPath):
    log = PyLog()
    log.LogText('���Ŀ¼ = %s' % solutionPath )

    if not os.path.isfile(solutionPath + '\\shuaji.lua'):
        log.LogText('%s ���ǽ������Ŀ¼' % solutionPath )
        return

    dirs = solutionPath.split('\\')
    dirname = dirs[-1]
    log.LogText( dirname)
    tmpdir = solutionPath + '_tmp'
    if os.path.isdir(tmpdir):
        dir_util.remove_tree(tmpdir)
    dir_util.mkpath(tmpdir)
    dir_util.copy_tree(solutionPath, tmpdir)

    if os.path.isfile(tmpdir + '\\shuaji.lua'):
        log.LogText('�ϳ�ˢ������')
        generateConfig(tmpdir)
    if os.path.isfile(tmpdir + '\\systembackup.lua'):
        log.LogText('�ϳɱ��ݷ���')
        generatebackup(tmpdir)
    if os.path.isfile(tmpdir + '\\systemrestore.lua'):
        log.LogText('�ϳɻָ�����')
        generaterecovery(tmpdir)

    os.remove(tmpdir + '\\common.lua')

    log.LogText('����')
    if os.path.isfile(tmpdir + '\\config.lua'):
        execute_dos_cmd(os.getcwd() + '\\aes256.exe -e default_key ' + tmpdir + '\\config.lua')
    if os.path.isfile(tmpdir + '\\systembackup.lua'):
        execute_dos_cmd(os.getcwd() + '\\aes256.exe -e default_key ' + tmpdir + '\\systembackup.lua')
    if os.path.isfile(tmpdir + '\\systemrestore.lua'):
        execute_dos_cmd(os.getcwd() + '\\aes256.exe -e default_key ' + tmpdir + '\\systemrestore.lua')

    log.LogText('���')
    if os.path.isfile(tmpdir + '.zip'):
        os.remove(tmpdir + '.zip')
    os.chdir(tmpdir)
    make_archive(tmpdir, 'zip', '.', '.')

    if os.path.isfile(solutionPath + '.zip'):
        os.remove(solutionPath + '.zip')
    os.rename(tmpdir + '.zip', solutionPath + '.zip')
    os.chdir(solutionPath)
    dir_util.remove_tree(tmpdir)

    log.LogText('�ɹ�')

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
                #win32api.MessageBox(0, "����һ��������Ϣ", "��Ϣ�����")
                funcTabLayout = self.PyFindTabLayout("FunctionTabs")
                funcTabLayout.SelectItem(3)
                self.SetText("LblStatus", '������bug��ⰴť')
                self.SetText("txtDiagnose", '������bug��ⰴť')
                encrypt(r'E:\360mobile_svn\360shuaji_doc\trunk\demo\google_galaxy-nexus')

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


