__author__ = 'huqinghua'
# coding=gbk

import string, os, commands, time
import threading
import shutil
from distutils import dir_util
from shutil import make_archive
from ftplib import FTP
import zipfile
import ctypes

from PyUI import *
from MsgBox import *
from PyFrameBase import *
import UICommon

from CommonUtil import CommonUtils

TRUNC_DIR = r"E:\root_release"
#TRUNC_DIR = r"E:\360mobile_svn\OneKeyRoot\trunk"
YOURNAME = r"\\sign1\input\huqinghua"
OUTPUTNAME = r"\\sign1\output\huqinghua"

def unzip_file(zipfilename, unziptodir):
    if not os.path.exists(unziptodir): os.mkdir(unziptodir, 0777)
    zfobj = zipfile.ZipFile(zipfilename)
    for name in zfobj.namelist():
        name = name.replace('\\','/')

        if name.endswith('/'):
            os.mkdir(os.path.join(unziptodir, name))
        else:
            ext_filename = os.path.join(unziptodir, name)
            ext_dir= os.path.dirname(ext_filename)
            if not os.path.exists(ext_dir) : os.mkdir(ext_dir,0777)
            outfile = open(ext_filename, 'wb')
            outfile.write(zfobj.read(name))
            outfile.close()

def ftp_up(filename, ftpdir):
    while True:
        try:
            ftp=FTP()
            ftp.set_debuglevel(2)#�򿪵��Լ���2����ʾ��ϸ��Ϣ;0Ϊ�رյ�����Ϣ
            ftp.connect('10.18.56.47','21')#����
            ftp.login('image','Image#4321')#��¼�����������¼���ÿմ����漴��
            #print ftp.getwelcome()#��ʾftp��������ӭ��Ϣ
            ftp.cwd(ftpdir) #ѡ�����Ŀ¼
            bufsize = 1024#���û�����С
            file_handler = open(filename,'rb')#�Զ�ģʽ�ڱ��ش��ļ�
            ftp.storbinary('STOR %s' % os.path.basename(filename),file_handler,bufsize)#�ϴ��ļ�
            ftp.set_debuglevel(0)
            file_handler.close()
            print "ftp up OK"
            return
        except Exception, e:
            PyLog().LogText(str(e))
        finally:
            ftp.quit()

def ftp_rename(filename1,filename2, ftpdir):
    while True:
        if not ftp_exist(filename1, ftpdir):
            return
        try:
            ftp=FTP()
            ftp.set_debuglevel(2)#�򿪵��Լ���2����ʾ��ϸ��Ϣ;0Ϊ�رյ�����Ϣ
            ftp.connect('10.18.56.47','21')#����
            ftp.login('image','Image#4321')#��¼�����������¼���ÿմ����漴��
            #print ftp.getwelcome()#��ʾftp��������ӭ��Ϣ
            ftp.cwd(ftpdir) #ѡ�����Ŀ¼
            ftp.rename(filename1,filename2)#�ϴ��ļ�
            ftp.set_debuglevel(0)
            print "ftp rename OK"
            return
        except Exception, e:
            PyLog().LogText(str(e))
        finally:
            ftp.quit()

def ftp_delete(filename, ftpdir):
    while True:
        if not ftp_exist(filename, ftpdir):
            return
        try:
            ftp=FTP()
            ftp.set_debuglevel(2)#�򿪵��Լ���2����ʾ��ϸ��Ϣ;0Ϊ�رյ�����Ϣ
            ftp.connect('10.18.56.47','21')#����
            ftp.login('image','Image#4321')#��¼�����������¼���ÿմ����漴��
            #print ftp.getwelcome()#��ʾftp��������ӭ��Ϣ
            ftp.cwd(ftpdir) #ѡ�����Ŀ¼
            ftp.delete(filename)#�ϴ��ļ�
            ftp.set_debuglevel(0)
            print "ftp delete OK"
            return
        except Exception, e:
            PyLog().LogText(str(e))
        finally:
            ftp.quit()

def ftp_mkdir(ftpdir):
    while True:
        try:
            ftp=FTP()
            ftp.set_debuglevel(2)#�򿪵��Լ���2����ʾ��ϸ��Ϣ;0Ϊ�رյ�����Ϣ
            ftp.connect('10.18.56.47','21')#����
            ftp.login('image','Image#4321')#��¼�����������¼���ÿմ����漴��
            #print ftp.getwelcome()#��ʾftp��������ӭ��Ϣ

            try:
                ftp.cwd(ftpdir)
                return
            except Exception, e:
                PyLog().LogText(str(e))

            ftp.mkd(ftpdir)#�ϴ��ļ�
            ftp.set_debuglevel(0)
            print "ftp mkdir OK"
            return
        except Exception, e:
            PyLog().LogText(str(e))
        finally:
            ftp.quit()

def ftp_down(filename, ftpdir):
    while True:
        try:
            if os.path.isfile(filename):
                os.remove(filename)
            ftp=FTP()
            ftp.set_debuglevel(2)
            ftp.connect('10.18.56.47','21')#����
            ftp.login('image','Image#4321')#��¼�����������¼���ÿմ����漴��
            #print ftp.getwelcome()#��ʾftp��������ӭ��Ϣ
            ftp.cwd(ftpdir) #ѡ�����Ŀ¼
            bufsize = 1024
            file_handler = open(filename,'wb') #��дģʽ�ڱ��ش��ļ�
            ftp.retrbinary('RETR %s' % os.path.basename(filename),file_handler.write,bufsize)#���շ��������ļ���д�뱾���ļ�
            ftp.set_debuglevel(0)
            file_handler.close()
            print "ftp down OK"
            return
        except Exception, e:
            PyLog().LogText(str(e))
        finally:
            ftp.quit()

def ftp_exist(filename, ftpdir):
    while True:
        try:
            ftp=FTP()
            ftp.set_debuglevel(2)#�򿪵��Լ���2����ʾ��ϸ��Ϣ;0Ϊ�رյ�����Ϣ
            ftp.connect('10.18.56.47','21')#����
            ftp.login('image','Image#4321')#��¼�����������¼���ÿմ����漴��
            #print ftp.getwelcome()#��ʾftp��������ӭ��Ϣ
            ftp.cwd(ftpdir) #ѡ�����Ŀ¼
            fileNameList = ftp.nlst()
            if filename in fileNameList:
                ret = True
            else:
                ret = False
            ftp.set_debuglevel(0)
            return ret
        except Exception, e:
            PyLog().LogText(str(e))
        finally:
            ftp.quit()

def execute_dos_cmd(cmd):
    output = os.popen(cmd)
    for line in output:
        PyLog().LogText(line)

def PyThreadEncrypt(PyClassInstance, solution_path):
    try:
        PyClassInstance.EncryptAndPack(solution_path)
    except Exception, e:
        PyLog().LogText(str(e))

    PyLog().LogText('PyThreadEncrypt exit')

def PyThread_compile_featureUI_RELEASE(PyClassInstance, ):
    try:
        PyClassInstance.compile_featureUI_RELEASE()
    except Exception, e:
        PyLog().LogText(str(e))
    PyClassInstance.StopCompileAnimation()
    PyLog().LogText('PyThread_compile_featureUI_RELEASE exit')

def PyThread_compile_featureUI_DEBUG(PyClassInstance, ):
    try:
        PyClassInstance.compile_featureUI_DEBUG()
    except Exception, e:
        PyLog().LogText(str(e))
    PyClassInstance.StopCompileAnimation()
    PyLog().LogText('PyThread_compile_featureUI_DEBUG exit')

def PyThread_root_compileAndSign(PyClassInstance, ):
    try:
        PyClassInstance.root_compileAndSign()
    except Exception, e:
        PyLog().LogText(str(e))
    PyClassInstance.StopCompileAnimation()
    PyLog().LogText('PyThread_root_compileAndSign exit')

def PyThread_compile_sjzs_DEBUG(PyClassInstance, ):
    try:
        PyClassInstance.compile_sjzs_DEBUG()
    except Exception, e:
        PyLog().LogText(str(e))
    PyClassInstance.StopCompileAnimation()
    PyLog().LogText('PyThread_compile_sjzs_DEBUG exit')

def PyThread_compile_sjzs_RELEASE(PyClassInstance, ):
    try:
        PyClassInstance.compile_sjzs_RELEASE()
    except Exception, e:
        PyLog().LogText(str(e))
    PyClassInstance.StopCompileAnimation()
    PyLog().LogText('PyThread_compile_sjzs_RELEASE exit')

def PyThreadExecuteCompile(PyClassInstance, ):
    try:
        PyClassInstance.ExecuteCompile()
    except Exception, e:
        PyLog().LogText(str(e))
    PyClassInstance.StopCompileAnimation()
    PyLog().LogText('PyThreadExecuteCompile exit')

def PyThreaddiagnose(PyClassInstance, ):
    try:
        PyClassInstance.diagnose()
    except Exception, e:
        PyLog().LogText(str(e))

    PyLog().LogText('PyThreaddiagnose exit')

class MainFrame(PyFrameBase):
    def __init__(self):
        super(MainFrame, self).__init__()
        #PyFrameBase.__init__(self)
        self.msg = 'msg origer'
        self.clsName = self.__class__.__name__
        self.skinFileName = self.__class__.__name__ + '.xml'

    #virtual LPCSTR GetSkinFile();
    def GetSkinFile(self):
        return self.skinFileName

    #virtual LPCSTR GetWindowClassName() const;
    def GetWindowClassName(self):
        return self.clsName

    #virtual void OnPrepare(LPCSTR sendor, WPARAM wParam, LPARAM lParam);
    def OnPrepare(self, sendor, wParam, lParam):
        self.funcTabLayout = self.PyFindTabLayout("FunctionTabs")
        self.edtRomPath = self.PyFindControl("edtRomPath")
        self.txtDiagnose = self.PyFindControl("txtDiagnose")
        self.txtInstallLog = self.PyFindControl("txtInstallLog")
        self.LblStatus = self.PyFindControl("LblStatus")
        self.btnPyTest = self.PyFindControl("btnPyTest")
        self.AnimationJuhua = self.PyFindAnimation("Juhua")
        self.AnimationJuhua1 = self.PyFindAnimation("Juhua1")
        self.txtPlain = self.PyFindControl("txtPlain")
        self.LblStatus.SetText('��������')
        self.txtEnc = self.PyFindControl("txtEnc")
        self.ChkRoot = self.PyFindCheckBox("ChkRoot")
        self.ChkUIDebug = self.PyFindCheckBox("ChkUIDebug")
        self.ChkUIRelease = self.PyFindCheckBox("ChkUIRelease")
        self.ChkZsDebug = self.PyFindCheckBox("ChkZsDebug")
        self.ChkZsRelease = self.PyFindCheckBox("ChkZsRelease")
        self.ChkZsSign = self.PyFindCheckBox("ChkZsSign")
        self.DecTab = self.PyFindVerticalLayout("DecTab")
        #self.btnPyTest.SetVisible(False)
        self.btnPyTest.SetText('������')
        #PyWinUtils().SetTimer(self.GetHWnd(), 1, 10)
        #PyWinUtils().SetTimer(self.GetHWnd(), 2, 10000)

    #virtual LPCSTR GetWindowClassName() const;
    def TestObj(self, msg):
        self.msg = msg

    #virtual void OnNotify(LPCSTR sendor, LPCSTR sType, WPARAM wParam, LPARAM lParam);
    def OnNotify(self, sendor, sType, wParam, lParam):
        if sType == "itemselect":
            pass
        if sType == "click":
            if sendor == "BtnClose":
                #execute_dos_cmd('adb kill-server')
                self.ExitApp()

#            elif sendor == "btnPyTest":
#                self.funcTabLayout.SelectItem(0)
#                #UICommon.ShowMessageBox(self.GetHWnd(), '�Ի������', '�����˶Ի���ť')
#                infPath = PyWinUtils().SelectFile(self.GetHWnd(), "py(*.py)\0*.py\0")
#                if len(infPath) > 0:
#                    dirs = infPath.split('\\')
#                    dirname = dirs[-1]
#                    module = dirname.split('.')
#                    PyScript().RunPy(module[0], 'test')

            elif sendor == "btnStartAnimation":
                self.AnimationJuhua.StartAnimation()

            elif sendor == "btnStopAnimation":
                self.AnimationJuhua.StopAnimation()

            elif sendor == "btnPyTest":
                self.funcTabLayout.SelectItem(3)

            elif sendor == "test_add_btn":
                UICommon.ShowMessageBox(self.GetHWnd(), '�Ի������', '������test_add_btn')

            elif sendor == "btnPyDec":
                self.funcTabLayout.SelectItem(4)
                self.newbtn = self.PyCreateButton()
                attrlist = """name="test_add_btn" text="����ʱ����" float="true" pos="278,346,0,0" width="175" height="53" textcolor="#00FFFBF0" disabledtextcolor="#FFA7A6AA" font="1" align="center" normalimage="reboot.png" hotimage="file='reboot-hot.png' corner='20,20,20,20'" pushedimage="reboot.png" focusedimage="reboot.png""
                """
                self.newbtn.ApplyAttributeList(attrlist)
                self.DecTab.Add(self.newbtn.GetSelf())

            elif sendor == "btnEncrypt":
                self.funcTabLayout.SelectItem(3)
                self.txtDiagnose.SetText('')
                solPath = PyWinUtils().SelectFolder(self.GetHWnd(), "��ѡ����������:", "solutionpath")
                if len(solPath):
#                    PyWinUtils().SetWaitCursor()
#                    self.EncryptAndPack(solPath)
#                    PyWinUtils().SetArrowCursor()
                    t = threading.Thread(target=PyThreadEncrypt,args=(self,solPath))
                    t.start()
                    #t.join(1)

            elif sendor == 'btnExcuteCompile':
                t = threading.Thread(target=PyThreadExecuteCompile,args=(self,))
                t.start()
                #self.ChkRoot.SetCheck(False)
#
#            elif sendor == 'ButtonRoot':
#                t = threading.Thread(target=PyThread_root_compileAndSign,args=(self,))
#                t.start()
#
#            elif sendor == 'ButtonUIDebug':
#                self.txtDiagnose.SetText('')
#                t = threading.Thread(target=PyThread_compile_featureUI_DEBUG,args=(self,))
#                t.start()
#
#            elif sendor == 'ButtonUIRelease':
#                self.txtDiagnose.SetText('')
#                t = threading.Thread(target=PyThread_compile_featureUI_RELEASE,args=(self,))
#                t.start()
#
#            elif sendor == 'ButtonZSDebug':
#                self.txtDiagnose.SetText('')
#                t = threading.Thread(target=PyThread_compile_sjzs_DEBUG,args=(self,))
#                t.start()
#
#            elif sendor == 'ButtonZSRelease':
#                self.txtDiagnose.SetText('')
#                t = threading.Thread(target=PyThread_compile_sjzs_RELEASE,args=(self,))
#                t.start()

            elif sendor == "btnDriverDiagnose":
                self.funcTabLayout.SelectItem(3)
                #self.diagnose()
                t = threading.Thread(target=PyThreaddiagnose,args=(self,))
                t.start()

            elif sendor == 'btnOpenLog':
                if os.path.isfile(PyWinUtils().GetExeDirectory() + '\\applog.ini'):
                    PyWinUtils().ShellExcute(0, 'open', PyWinUtils().GetExeDirectory() + '\\applog.ini', '', '', 1)
                else:
                    UICommon.ShowMessageBox(self.GetHWnd(), '����', '��־�ļ�������')
                #win32api.ShellExecute(0, 'open', 'e:\\applog.ini', None, "", 1)

            elif sendor == 'btnClearLog':
                self.txtDiagnose.SetText('')
                if os.path.isfile(PyWinUtils().GetExeDirectory() + '\\applog.ini'):
                    os.remove(PyWinUtils().GetExeDirectory() + '\\applog.ini')
                #win32api.ShellExecute(0, 'open', 'e:\\applog.ini', None, "", 1)

            elif sendor == 'btnDriverInstall':
                self.funcTabLayout.SelectItem(1)
                self.txtInstallLog.SetText('')

            elif sendor == 'btnChooseInf':
                infPath = PyWinUtils().SelectFile(self.GetHWnd(), "inf(*.inf)\0*.inf\0")
                if len(infPath) > 0:
                    self.edtRomPath.SetText(infPath)

            elif sendor == 'btnDecSolution':
                msg = self.txtEnc.GetText()
                UICommon.ShowMessageBox(self.GetHWnd(), '����', '��֧��')

            elif sendor == 'btnInstallDriver':
                msg = self.edtRomPath.GetText()
                UICommon.ShowMessageBox(self.GetHWnd(), '����', '��֧��')

    def waitForSignal(self, fileName):
        while True:
            try:
                if ftp_exist(fileName, "./root/sign/"):
                    return
                else:
                    self.AppendAndLog(fileName + "������")
                    time.sleep(5)
            except Exception, e:
                PyLog().LogText(str(e))

    def ExecuteCompile(self):
        self.txtDiagnose.SetText("")
        self.AnimationJuhua1.StartAnimation()

        if self.ChkRoot.GetCheck():
            PyLog().LogText('root_compileAndSign')
            self.root_compileAndSign()
        if self.ChkUIDebug.GetCheck():
            PyLog().LogText('compile_featureUI_DEBUG')
            self.compile_featureUI_DEBUG()
        if self.ChkUIRelease.GetCheck():
            PyLog().LogText('compile_featureUI_RELEASE')
            self.compile_featureUI_RELEASE()
        if self.ChkZsDebug.GetCheck():
            PyLog().LogText('compile_sjzs_DEBUG')
            shutil.copyfile(r"E:\360DesktopUIKernel\Src\Lib\Debug\UiAssistLib.lib" ,r"E:\360mobile_svn\360mobilemgr\branches\360MobileMgr_For_SysClean\lib\share\UiAssistLib.lib")
            shutil.copyfile(r"E:\360DesktopUIKernel\Bin\Debug\UiFeatureKernel.dll" ,r"C:\Program Files\360\360Safe\mobilemgr\UiFeatureKernel.dll")
            shutil.copyfile(r"E:\360MMUiFeatureControlSrc\Bin\UiFeatureModule\Debug\UiFeatureNormalControl.dll", r"C:\Program Files\360\360Safe\mobilemgr\UiFeatureNormalControl.dll")
            self.compile_sjzs_DEBUG()
        if self.ChkZsRelease.GetCheck():
            PyLog().LogText('compile_sjzs_RELEASE')
            shutil.copyfile(r"E:\360DesktopUIKernel\Src\Lib\Release\UiAssistLib.lib" ,r"E:\360mobile_svn\360mobilemgr\branches\360MobileMgr_For_SysClean\lib\share\UiAssistLib.lib")
            shutil.copyfile(r"E:\360DesktopUIKernel\Bin\Release\UiFeatureKernel.dll" ,r"E:\360mobile_svn\360mobilemgr\branches\360MobileMgr_For_SysClean\src\Release\UiFeatureKernel.dll")
            shutil.copyfile(r"E:\360MMUiFeatureControlSrc\Bin\UiFeatureModule\Release\UiFeatureNormalControl.dll", r"E:\360mobile_svn\360mobilemgr\branches\360MobileMgr_For_SysClean\src\Release\UiFeatureNormalControl.dll")
            self.compile_sjzs_RELEASE()
        if self.ChkZsSign.GetCheck():
            PyLog().LogText('SignZS')
            self.SignZS()

        self.AnimationJuhua1.StopAnimation()

    def compile_sjzs_DEBUG(self):
        self.txtDiagnose.SetText("")
        self.AnimationJuhua1.StartAnimation()
        self.ShowAndLog(time.strftime( '%Y-%m-%d %X', time.localtime() ))
        self.AppendAndLog("1 ���ڱ���360�ֻ�����...")
        os.chdir(r'E:\360mobile_svn\360mobilemgr\branches\360MobileMgr_For_SysClean')
        os.system(r'TortoiseProc.exe /command:update /path:"E:\360mobile_svn\360mobilemgr\branches\360MobileMgr_For_SysClean\" /closeonend:3')
        CommonUtils.ReverseToExePath()
        output = os.popen(r'compile_debug.bat ' + r'E:\360mobile_svn\360mobilemgr\branches\360MobileMgr_For_SysClean\src\WholeAll.sln')
        msg = self.txtDiagnose.GetText()
        for line in output:
            msg = msg + line
            self.txtDiagnose.SetText(msg)
        self.AppendAndLog( "����360�ֻ����ֽ��� �ɹ�")
        self.AnimationJuhua1.StopAnimation()

    def compile_sjzs_RELEASE(self):
        self.txtDiagnose.SetText("")
        self.AnimationJuhua1.StartAnimation()
        self.ShowAndLog(time.strftime( '%Y-%m-%d %X', time.localtime() ))
        self.AppendAndLog("1 ���ڱ���360�ֻ�����...")
        os.chdir(r'E:\360mobile_svn\360mobilemgr\branches\360MobileMgr_For_SysClean')
        os.system(r'TortoiseProc.exe /command:update /path:"E:\360mobile_svn\360mobilemgr\branches\360MobileMgr_For_SysClean\" /closeonend:3')
        CommonUtils.ReverseToExePath()
        output = os.popen(r'compile.bat ' + r'E:\360mobile_svn\360mobilemgr\branches\360MobileMgr_For_SysClean\src\WholeAll.sln')
        msg = self.txtDiagnose.GetText()
        for line in output:
            msg = msg + line
            self.txtDiagnose.SetText(msg)
        self.AppendAndLog( "����360�ֻ����ֽ��� �ɹ�")
        self.AnimationJuhua1.StopAnimation()

    def StopCompileAnimation(self):
        self.AnimationJuhua1.StopAnimation()

    def compile_featureUI_RELEASE(self):
        self.AnimationJuhua1.StartAnimation()
        self.ShowAndLog(time.strftime( '%Y-%m-%d %X', time.localtime() ))
        self.AppendAndLog("1 ���ڱ���360DesktopUIKernel...")
        os.chdir(r'E:\360DesktopUIKernel')
        os.system(r'TortoiseProc.exe /command:update /path:"E:\360DesktopUIKernel\" /closeonend:3')
        CommonUtils.ReverseToExePath()
        output = os.popen(r'compile.bat ' + r'E:\360DesktopUIKernel\UiFeature.sln')
        msg = self.txtDiagnose.GetText()
        for line in output:
            msg = msg + line
            self.txtDiagnose.SetText(msg)
        #os.chdir(r'E:\360DesktopUIKernel')
        #        output = os.popen(r'CopyUiFeatureKernelToProject-huqinghua.bat')
        #        msg = self.txtDiagnose.GetText()
        #        for line in output:
        #            msg = msg + line
        #            self.txtDiagnose.SetText(msg)
        dir_util.copy_tree(r"E:\360DesktopUIKernel\Src\Inc", r"E:\360MMUiFeatureControlSrc\UiFeature\Src\Inc")
        shutil.copyfile(r"E:\360DesktopUIKernel\Src\Lib\Release\UiAssistLib.lib" ,r"E:\360MMUiFeatureControlSrc\UiFeature\Src\Lib\Release\UiAssistLib.lib")
        shutil.copyfile(r"E:\360DesktopUIKernel\Bin\Release\UiFeatureBuilder.exe" ,r"E:\360MMUiFeatureControlSrc\Bin\UiFeatureModule\Release\UiFeatureBuilder.exe")
        shutil.copyfile(r"E:\360DesktopUIKernel\Bin\Release\UiFeatureRun.exe" ,r"E:\360MMUiFeatureControlSrc\Bin\UiFeatureModule\Release\UiFeatureRun.exe")
        shutil.copyfile(r"E:\360DesktopUIKernel\Bin\Release\UiFeatureKernel.dll" ,r"E:\360MMUiFeatureControlSrc\Bin\UiFeatureModule\Release\UiFeatureKernel.dll")
        shutil.copyfile(r"E:\360DesktopUIKernel\Src\Lib\Release\UiAssistLib.lib" ,r"E:\360mobile_svn\360mobilemgr\branches\360MobileMgr_For_SysClean\lib\share\UiAssistLib.lib")

        self.AppendAndLog("2 ���ڱ���360MMUiFeatureControlSrc...")
        os.chdir(r'E:\360MMUiFeatureControlSrc')
        os.system(r'TortoiseProc.exe /command:update /path:"E:\360MMUiFeatureControlSrc\" /closeonend:3')
        CommonUtils.ReverseToExePath()
        output = os.popen(r'compile.bat ' + r'E:\360MMUiFeatureControlSrc\360DesktopUi.sln')
        msg = self.txtDiagnose.GetText()
        for line in output:
            msg = msg + line
            self.txtDiagnose.SetText(msg)

#        os.chdir(r'E:\360MMUiFeatureControlSrc')
#        output = os.popen(r'UiFeatureNormalControlTosjzs-huqinghua.bat')
#        msg = self.txtDiagnose.GetText()
#        for line in output:
#            msg = msg + line
#            self.txtDiagnose.SetText(msg)
#        self.AppendAndLog( "  ��ʼ�����ļ�")
        shutil.copyfile(r"E:\360DesktopUIKernel\Bin\Release\UiFeatureKernel.dll" ,r"E:\360mobile_svn\360mobilemgr\branches\360MobileMgr_For_SysClean\src\Release\UiFeatureKernel.dll")
        shutil.copyfile(r"E:\360MMUiFeatureControlSrc\Bin\UiFeatureModule\Release\UiFeatureNormalControl.dll", r"E:\360mobile_svn\360mobilemgr\branches\360MobileMgr_For_SysClean\src\Release\UiFeatureNormalControl.dll")
        self.AppendAndLog( "  ���� �ɹ�")
        self.AnimationJuhua1.StopAnimation()

    def compile_featureUI_DEBUG(self):
        self.AnimationJuhua1.StartAnimation()
        self.ShowAndLog(time.strftime( '%Y-%m-%d %X', time.localtime() ))
        self.AppendAndLog("1 ���ڱ���360DesktopUIKernel...")
        os.chdir(r'E:\360DesktopUIKernel')
        os.system(r'TortoiseProc.exe /command:update /path:"E:\360DesktopUIKernel\" /closeonend:3')
        CommonUtils.ReverseToExePath()
        #os.system(r'compile.bat ' + TRUNC_DIR + r'\360MM\Src\360MM.sln')
        output = os.popen(r'compile_debug.bat ' + r'E:\360DesktopUIKernel\UiFeature.sln')
        msg = self.txtDiagnose.GetText()
        for line in output:
            msg = msg + line
            self.txtDiagnose.SetText(msg)
#        os.chdir(r'E:\360DesktopUIKernel')
#        output = os.popen(r'CopyUiFeatureKernelToProject-huqinghua.bat')
#        msg = self.txtDiagnose.GetText()
#        for line in output:
#            msg = msg + line
#            self.txtDiagnose.SetText(msg)
        dir_util.copy_tree(r"E:\360DesktopUIKernel\Src\Inc", r"E:\360MMUiFeatureControlSrc\UiFeature\Src\Inc")
        shutil.copyfile(r"E:\360DesktopUIKernel\Src\Lib\Debug\UiAssistLib.lib",r"E:\360MMUiFeatureControlSrc\UiFeature\Src\Lib\Debug\UiAssistLib.lib")
        shutil.copyfile(r"E:\360DesktopUIKernel\Bin\Debug\UiFeatureBuilder.exe" ,r"E:\360MMUiFeatureControlSrc\Bin\UiFeatureModule\Debug\UiFeatureBuilder.exe")
        shutil.copyfile(r"E:\360DesktopUIKernel\Bin\Debug\UiFeatureRun.exe" ,r"E:\360MMUiFeatureControlSrc\Bin\UiFeatureModule\Debug\UiFeatureRun.exe")
        shutil.copyfile(r"E:\360DesktopUIKernel\Bin\Debug\UiFeatureKernel.dll" ,r"E:\360MMUiFeatureControlSrc\Bin\UiFeatureModule\Debug\UiFeatureKernel.dll")
        shutil.copyfile(r"E:\360DesktopUIKernel\Src\Lib\Debug\UiAssistLib.lib" ,r"E:\360mobile_svn\360mobilemgr\branches\360MobileMgr_For_SysClean\lib\share\UiAssistLib.lib")

        self.AppendAndLog("2 ���ڱ���360MMUiFeatureControlSrc...")
        os.chdir(r'E:\360MMUiFeatureControlSrc')
        os.system(r'TortoiseProc.exe /command:update /path:"E:\360MMUiFeatureControlSrc\" /closeonend:3')
        CommonUtils.ReverseToExePath()
        #os.system(r'compile.bat ' + TRUNC_DIR + r'\360MM\Src\360MM.sln')
        output = os.popen(r'compile_debug.bat ' + r'E:\360MMUiFeatureControlSrc\360DesktopUi.sln')
        msg = self.txtDiagnose.GetText()
        for line in output:
            msg = msg + line
            self.txtDiagnose.SetText(msg)
#        os.chdir(r'E:\360MMUiFeatureControlSrc')
#        output = os.popen(r'UiFeatureNormalControlTosjzs-huqinghua.bat')
#        msg = self.txtDiagnose.GetText()
#        for line in output:
#            msg = msg + line
#            self.txtDiagnose.SetText(msg)
        shutil.copyfile(r"E:\360DesktopUIKernel\Bin\Debug\UiFeatureKernel.dll" ,r"C:\Program Files\360\360Safe\mobilemgr\UiFeatureKernel.dll")
        shutil.copyfile(r"E:\360MMUiFeatureControlSrc\Bin\UiFeatureModule\Debug\UiFeatureNormalControl.dll", r"C:\Program Files\360\360Safe\mobilemgr\UiFeatureNormalControl.dll")
        self.AppendAndLog( "  ���� �ɹ�")
        self.AnimationJuhua1.StopAnimation()

    def SignZS(self):
        self.AnimationJuhua1.StartAnimation()
        self.ShowAndLog(time.strftime( '%Y-%m-%d %X', time.localtime() ))

        #���
        CommonUtils.ReverseToExePath()
        self.sendSignal("clearall.txt")
        self.AppendAndLog( "1 �ȴ���ͤ���")
        self.waitForSignal("forcleared.txt")

        #�����ļ���ǩ��������
        self.AppendAndLog( "2 ����bin��ǩ��������")
        while True:
            try:
                PyWinUtils().CreateDirectory(YOURNAME + r"\bin")
                os.chdir(r"E:\360mobile_svn\360mobilemgr\branches\360MobileMgr_For_SysClean\src\Release")
                shutil.copyfile(r"E:\360mobile_svn\360mobilemgr\branches\360MobileMgr_For_SysClean\src\Release\UiFeatureKernel.dll", YOURNAME + r"\bin\UiFeatureKernel.dll")
                shutil.copyfile(r"E:\360mobile_svn\360mobilemgr\branches\360MobileMgr_For_SysClean\src\Release\UiFeatureNormalControl.dll", YOURNAME + r"\bin\UiFeatureNormalControl.dll")
                shutil.copyfile(r"E:\360mobile_svn\360mobilemgr\branches\360MobileMgr_For_SysClean\src\Release\360MobileMgr.exe", YOURNAME + r"\bin\360MobileMgr.exe")
                shutil.copyfile(r"E:\360mobile_svn\360mobilemgr\branches\360MobileMgr_For_SysClean\sign_config.ini", YOURNAME + r"\sign_config.ini")
                shutil.copyfile(r"E:\360mobile_svn\360mobilemgr\branches\360MobileMgr_For_SysClean\upload.ok", YOURNAME + r"\upload.ok")
                break
            except Exception, e:
                PyLog().LogText(str(e))
                self.AppendAndLog( " ����bin�ļ�ʧ�ܣ�����")

        self.AppendAndLog( " �ȴ�ǩ��")
        while (True):
            if os.path.isfile(YOURNAME + r"\upload.ok"):
                time.sleep(5)
            else:
                break
        self.changeSignal("forcleared.txt", "binuploaded.txt")
        self.AppendAndLog( "7 �ȴ�ȡbin")
        self.waitForSignal("binsinged.txt")

        if os.path.isfile("bin.zip"):
            os.remove(r"bin.zip")
        if os.path.isdir("bin"):
            dir_util.remove_tree("bin")
        ftp_down(r"bin.zip", "./root/sign/")
        ftp_delete(r"bin.zip", "./root/sign/")
        unzip_file(r"bin.zip", "bin")
        shutil.copyfile(r"c:\Program Files\360\360Safe\mobilemgr\clean.ufd", r".\bin\clean.ufd")

        self.AppendAndLog( "  ���� �ɹ�")
        self.AnimationJuhua1.StopAnimation()

    def root_compileAndSign(self):
        self.AnimationJuhua1.StartAnimation()
        self.ShowAndLog(time.strftime( '%Y-%m-%d %X', time.localtime() ))

        self.AppendAndLog("1 ���ڱ������...")
        if os.path.isfile(TRUNC_DIR + "\\360MM\\Bin\\Release\\360Root.exe"):
            os.remove(TRUNC_DIR + "\\360MM\\Bin\\Release\\360Root.exe")
        os.chdir(TRUNC_DIR)
        os.system(r'TortoiseProc.exe /command:update /path:"E:\root_release\" /closeonend:3')
        CommonUtils.ReverseToExePath()
        #os.system(r'compile.bat ' + TRUNC_DIR + r'\360MM\Src\360MM.sln')
        output = os.popen(r'compile.bat ' + TRUNC_DIR + r'\360MM\Src\360MM.sln')
        msg = self.txtDiagnose.GetText()
        for line in output:
            msg = msg + line
            self.txtDiagnose.SetText(msg)
            self.ProcessMessages()

        if os.path.isfile(TRUNC_DIR + "\\360MM\\Bin\\Release\\360Root.exe"):
            self.AppendAndLog( "  �ɹ�")
            os.remove(TRUNC_DIR + "\\360MM\\Bin\\Release\\adb.exe")
        else:
            self.AppendAndLog( "  ʧ��")
            return

        self.AppendAndLog( "2 ����pdb�ļ�")
        dest = TRUNC_DIR + "\\pdb\\" + time.strftime( '%Y-%m-%d %X', time.localtime() ).replace(":", "-") + r" 360Root.pdb"
        src = TRUNC_DIR + r"\360MM\Bin\Release\360Root.pdb"
        shutil.copyfile(src, dest)
        ftp_up(dest, "./root/pdb/")
        self.AppendAndLog( "  �ɹ�")

        self.AppendAndLog( "3 ��������Release�ļ����ǵ�Debug��,Ȼ��DebugĿ¼����������trunk/install/Bin/�¸���bin")
        dir_util.copy_tree(TRUNC_DIR + r"\360MM\Bin\Release", TRUNC_DIR + r"\360MM\Bin\Debug")
        dir_util.remove_tree(TRUNC_DIR + r"\install\Bin\bin")
        dir_util.copy_tree(TRUNC_DIR + r"\360MM\Bin\Debug", TRUNC_DIR + r"\install\Bin\bin")
        self.AppendAndLog( "  �ɹ�")

        self.AppendAndLog( "4 �����ļ�")
        os.chdir(TRUNC_DIR + r"\install")
        output = os.system(r'CopyFile.bat')
        #for line in output:
        #    self.AppendAndLog( line)
        self.AppendAndLog( "  �ɹ�")

        #���
        CommonUtils.ReverseToExePath()
        self.sendSignal("clearall.txt")
        self.AppendAndLog( "5 �ȴ���ͤ���")
        self.waitForSignal("forcleared.txt")

        #�����ļ���ǩ��������
        self.AppendAndLog( "6 ����bin��ǩ��������")
        while True:
            try:
                PyWinUtils().CreateDirectory(YOURNAME + r"\bin")
                dir_util.copy_tree(TRUNC_DIR + r"\install\sign-Bin\bin", YOURNAME + r"\bin")
                #dir_util.copy_tree(TRUNC_DIR + r"\install\sign-Bin\dll", YOURNAME + r"\dll")
                shutil.copyfile(TRUNC_DIR + r"\install\sign-Bin\sign_config.ini", YOURNAME + r"\sign_config.ini")
                shutil.copyfile(TRUNC_DIR + r"\install\sign-Bin\upload.ok", YOURNAME + r"\upload.ok")
                break
            except Exception, e:
                PyLog().LogText(str(e))
                self.AppendAndLog( " ����bin�ļ�ʧ�ܣ�����")

        self.AppendAndLog( " �ȴ�ǩ��")
        while (True):
            if os.path.isfile(YOURNAME + r"\upload.ok"):
                time.sleep(5)
            else:
                break
        self.changeSignal("forcleared.txt", "binuploaded.txt")
        self.AppendAndLog( "7 �ȴ�ȡbin")
        self.waitForSignal("binsinged.txt")

        #���ɰ�װ��
        self.AppendAndLog( "8 ���ɰ�װ��")
        if os.path.isfile("bin.zip"):
            os.remove(r"bin.zip")
        if os.path.isdir("bin"):
            dir_util.remove_tree("bin")
        ftp_down(r"bin.zip", "./root/sign/")
        ftp_delete(r"bin.zip", "./root/sign/")
        unzip_file(r"bin.zip", "bin")
        dir_util.copy_tree(r"bin", TRUNC_DIR + r"\install\Bin\bin")
        os.chdir(TRUNC_DIR + r"\install")
        if os.path.isfile("360RootSetup.exe"):
            os.remove(r"360RootSetup.exe")
        os.system("\"C:\Program Files (x86)\NSIS\makensis.exe\" 360һ��Root.nsi")
        os.chdir(TRUNC_DIR + r"\install")
        shutil.copyfile("360RootSetup.exe", YOURNAME + r"\360RootSetup.exe")
        shutil.copyfile("sign_config.ini", YOURNAME + r"\sign_config.ini")
        shutil.copyfile("upload.ok", YOURNAME + r"\upload.ok")
        self.AppendAndLog( " �ȴ�ǩ��")
        while (True):
            if os.path.isfile(YOURNAME + r"\upload.ok"):
                time.sleep(5)
            else:
                break
        CommonUtils.ReverseToExePath()
        self.AppendAndLog( "  �ı�״̬binsinged -> exeuoloaded")
        self.changeSignal("binsinged.txt", "exeuoloaded.txt")
        self.AppendAndLog( "9 �ȴ���ȡǩ���İ�װ��")
        self.waitForSignal("exesinged.txt")

        #��ȡǩ���İ�װ��
        self.AppendAndLog( "10 ��ȡǩ���İ�װ��")
        if os.path.isfile(r'360RootSetup.exe'):
            os.remove(r'360RootSetup.exe')
        ftp_down(r"360RootSetup.exe", "./root/sign/")
        ftp_delete(r"360RootSetup.exe", "./root/sign/")
        self.delSignal("exesinged.txt")

        ftp_mkdir("./root/install/"+time.strftime( '%Y%m%d', time.localtime() ))
        timestr = time.strftime( '%X', time.localtime() )
        rootname = "360RootSetup-svn000" + time.strftime( '-%m%d-', time.localtime() ) + timestr[0:2] + timestr[3:5] + ".exe"
        PyLog().LogText( rootname)
        os.rename("360RootSetup.exe", rootname)
        ftp_up(rootname, "./root/install/"+time.strftime( '%Y%m%d', time.localtime() ))
        self.AppendAndLog( "  ���� ��װ��ǩ���ɹ�")
        self.AnimationJuhua1.StopAnimation()

    def OnCustomTimer(self, wParam, lParam):
        if wParam == 1:
            pass
            #time.sleep(0)
            #PyLog().LogText( 'OnCustomTimer()')
        elif wParam == 2:
            self.compileAndSign_jinting()

    def compileAndSign_jinting(self):
        while True:
            try:
                #���
                if ftp_exist("clearall.txt", "./root/sign/"):
                    self.ShowAndLog(time.strftime( '%Y-%m-%d %X', time.localtime() ))
                    self.AppendAndLog( "���")
                    CommonUtils.ReverseToExePath()
                    if os.path.isfile(r"\\sign1\output\huqinghua\360RootSetup.exe"):
                        os.remove(r"\\sign1\output\huqinghua\360RootSetup.exe")
                    if os.path.isdir(r"\\sign1\output\huqinghua\bin"):
                        dir_util.remove_tree(r"\\sign1\output\huqinghua\bin")
                    self.changeSignal("clearall.txt", "forcleared.txt")
                    self.AppendAndLog( "������")
                    continue

                #��ȡbin
                if ftp_exist("binuploaded.txt", "./root/sign/"):
                    self.ShowAndLog(time.strftime( '%Y-%m-%d %X', time.localtime() ))
                    self.AppendAndLog( "��ȡbin")
                    CommonUtils.ReverseToExePath()
                    if os.path.isdir(r"bin"):
                        dir_util.remove_tree(r"bin")
                    dir_util.copy_tree(r"\\sign1\output\huqinghua\bin", r"bin")
                    #dir_util.copy_tree(r"huqinghua\bin", r"bin")
                    if os.path.isfile(r'bin.zip'):
                        os.remove(r'bin.zip')
                    os.chdir(PyWinUtils().GetExeDirectory() + r"\bin")
                    make_archive(PyWinUtils().GetExeDirectory() + r"\bin", 'zip', '.', '.')
                    CommonUtils.ReverseToExePath()
                    ftp_delete(r"bin.zip", "./root/sign/")
                    ftp_up(r"bin.zip", "./root/sign/")
                    self.changeSignal("binuploaded.txt", "binsinged.txt")
                    self.AppendAndLog( "��ȡbin���")
                    continue

                #��ȡ��װ��
                if ftp_exist("exeuoloaded.txt", "./root/sign/"):
                    self.ShowAndLog(time.strftime( '%Y-%m-%d %X', time.localtime() ))
                    self.AppendAndLog( "��ȡ��װ��")
                    CommonUtils.ReverseToExePath()
                    if os.path.isfile(r'360RootSetup.exe'):
                        os.remove(r'360RootSetup.exe')
                    shutil.copyfile(r"\\sign1\output\huqinghua\360RootSetup.exe", r"360RootSetup.exe")
                    #shutil.copyfile(r"huqinghua\360RootSetup.exe", r"360RootSetup.exe")
                    ftp_delete(r"360RootSetup.exe", "./root/sign/")
                    ftp_up(r"360RootSetup.exe", "./root/sign/")
                    self.changeSignal("exeuoloaded.txt", "exesinged.txt")
                    self.AppendAndLog( "��ȡexe��װ�����")
                    continue

                break
            except Exception, e:
                PyLog().LogText(str(e))

    def changeSignal(self, name1, name2):
        while True:
            try:
                if ftp_exist(name1, "./root/sign/"):
                    ftp_delete(name1, "./root/sign/")
                if not ftp_exist(name2, "./root/sign/"):
                    ftp_up(name2, "./root/sign/")
                return
            except Exception, e:
                PyLog().LogText(str(e))

    def sendSignal(self, name):
        while True:
            try:
                if not ftp_exist(name, "./root/sign/"):
                    ftp_up(name, "./root/sign/")
                return
            except Exception, e:
                PyLog().LogText(str(e))

    def delSignal(self, name):
        while True:
            try:
                if ftp_exist(name, "./root/sign/"):
                    ftp_delete(name, "./root/sign/")
                return
            except Exception, e:
                PyLog().LogText(str(e))

    def AppendAndLog(self, line):
        PyLog().LogText( line)
        msg = self.txtDiagnose.GetText()
        self.txtDiagnose.SetText(msg + '\n' + line)

    def ShowAndLog(self, line):
        PyLog().LogText( line)
        self.txtDiagnose.SetText(line)

    def diagnose(self):
        CommonUtils.ReverseToExePath()
        os.system('adb devices')
        #pid = subprocess.Popen(["adb", "devices"]).pid
        #subprocess.Popen("adb devices")
        #self.ShowAndLog( "\n")
        ISOTIMEFORMAT='%Y-%m-%d %X'
        self.ShowAndLog(time.strftime( ISOTIMEFORMAT, time.localtime() ))
        self.AppendAndLog( "----------------------------------------------�ֻ�ģʽ���----------------------------------------------")
        self.AppendAndLog( 'adb devices ���:')
        output = os.popen('adb devices')
        for line in output:
            self.AppendAndLog( line)
        self.AppendAndLog(os.linesep)

        self.AppendAndLog( 'fastboot devices ���:')
        output = os.popen('fastboot devices')
        for line in output:
            self.AppendAndLog( line)

        self.AppendAndLog( "----------------------------------------------�ֻ��豸���----------------------------------------------")
        output = os.popen(r'devcon find usb\*')
        for line in output:
            if line.find('VID_04E8') != -1:
                line = line.replace('\n', '')
                self.AppendAndLog(line)
                self.AppendAndLog('����')
            elif line.find('VID_19D2') != -1:
                line = line.replace('\n', '')
                self.AppendAndLog( line)
                self.AppendAndLog( '����')
            elif line.find('VID_19D2') != -1:
                line = line.replace('\n', '')
                self.AppendAndLog( line)
                self.AppendAndLog( '����')
            elif line.find('VID_12D1') != -1:
                line = line.replace('\n', '')
                self.AppendAndLog( line)
                self.AppendAndLog( '��Ϊ')
            else:
                line = line.replace('\n', '')
                self.AppendAndLog( line)

            if line.find('ADB') != -1:
                self.AppendAndLog( "***********************")
        print ""
        return True

    def generateConfig(self, solutionPath):
        flag = ''
        commonFile=file(solutionPath + '\\common.lua','r')
        shuajiFile=file(solutionPath + '\\shuaji.lua','r+')

        temp=file(solutionPath + '\\tmp.lua','w+')
        for line in commonFile:
            temp.write(line)
        temp.write('\n')
        for line in shuajiFile:
            temp.write(line)
        temp.write('\n')
        temp.flush()
        temp.close()

        shuajiFile.close()
        os.remove(solutionPath + '\\shuaji.lua')
        if os.path.isfile(solutionPath + '\\config.lua'):
            os.remove(solutionPath + '\\config.lua')
        os.rename(solutionPath + '\\tmp.lua', solutionPath + '\\config.lua')

    def generatebackup(self, solutionPath):
        flag = ''
        commonFile=file(solutionPath + '\\common.lua','r')
        shuajiFile=file(solutionPath + '\\systembackup.lua','r+')

        temp=file(solutionPath + '\\tmp.lua','w+')
        for line in commonFile:
            temp.write(line)
        temp.write('\n')
        for line in shuajiFile:
            temp.write(line)
        temp.write('\n')
        temp.flush()
        temp.close()

        shuajiFile.close()
        os.remove(solutionPath + '\\systembackup.lua')
        os.rename(solutionPath + '\\tmp.lua', solutionPath + '\\systembackup.lua')

    def generaterecovery(self, solutionPath):
        flag = ''
        commonFile=file(solutionPath + '\\common.lua','r')
        shuajiFile=file(solutionPath + '\\systemrestore.lua','r+')

        temp=file(solutionPath + '\\tmp.lua','w+')
        for line in commonFile:
            temp.write(line)
        temp.write('\n')
        for line in shuajiFile:
            temp.write(line)
        temp.write('\n')
        temp.flush()
        temp.close()

        shuajiFile.close()
        os.remove(solutionPath + '\\systemrestore.lua')
        os.rename(solutionPath + '\\tmp.lua', solutionPath + '\\systemrestore.lua')

    def EncryptAndPack(self, solutionPath):
        CommonUtils.ReverseToExePath()
        ISOTIMEFORMAT='%Y-%m-%d %X'
        self.ShowAndLog(time.strftime( ISOTIMEFORMAT, time.localtime() ))
        self.AppendAndLog('���Ŀ¼ = %s' % solutionPath )

        if not os.path.isfile(solutionPath + '\\shuaji.lua'):
            self.AppendAndLog('%s ���ǽ������Ŀ¼' % solutionPath )
            return

        dirs = solutionPath.split('\\')
        dirname = dirs[-1]
        self.AppendAndLog( dirname)
        tmpdir = solutionPath + '_tmp'
        if os.path.isdir(tmpdir):
            dir_util.remove_tree(tmpdir)
        #PyWinUtils().CreateDirectory(tmpdir)
        dir_util.mkpath(tmpdir)
#        time.sleep(10)
#        i = 0
#        while i<100:
#            i = i + 1
#            self.AppendAndLog('%d' % i )
#            time.sleep(1)
        dir_util.copy_tree(solutionPath, tmpdir)

        if os.path.isfile(tmpdir + '\\shuaji.lua'):
            self.AppendAndLog('�ϳ�ˢ������')
            self.generateConfig(tmpdir)
        if os.path.isfile(tmpdir + '\\systembackup.lua'):
            self.AppendAndLog('�ϳɱ��ݷ���')
            self.generatebackup(tmpdir)
        if os.path.isfile(tmpdir + '\\systemrestore.lua'):
            self.AppendAndLog('�ϳɻָ�����')
            self.generaterecovery(tmpdir)

        os.remove(tmpdir + '\\common.lua')

        self.AppendAndLog('���')
        if os.path.isfile(tmpdir + '.zip'):
            os.remove(tmpdir + '.zip')
        os.chdir(tmpdir)
        make_archive(tmpdir, 'zip', '.', '.')

        if os.path.isfile(solutionPath + '.zip'):
            os.remove(solutionPath + '.zip')
        os.rename(tmpdir + '.zip', solutionPath + '.zip')
        os.chdir(solutionPath)
        dir_util.remove_tree(tmpdir)

        self.AppendAndLog('�ɹ�')

def PyAppInit():
    CommonUtils.SaveExePath()
    pyFrameObj = PyFrameCreator()
    obj = pyFrameObj.CreateForm(0, 'PyMain', 'MainFrame')
    obj.TestObj('msg changed')
    pyFrameObj.ShowModal()


