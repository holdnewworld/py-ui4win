
#ifndef PYFRAME_HPP
#define PYFRAME_HPP

#include<boost/python.hpp>
#include "PyFrameUI.hpp"
#include "duilib-python.h"

using namespace boost::python;

class PyControlUI
{
public:
	PyControlUI(PControlUI pControlUI) {m_pyControlUI = (CControlUI*)pControlUI;}
	~PyControlUI() {}
	PControlUI GetSelf() {return (PControlUI)m_pyControlUI;}

	void SetName(LPCSTR pstrName) {m_pyControlUI->SetName(pstrName);};
	void ApplyAttributeList(LPCSTR pstrList) {m_pyControlUI->ApplyAttributeList(pstrList);}
	void SetText(LPCSTR caption) { m_pyControlUI->SetText(caption); }
	CDuiString GetText() { return m_pyControlUI->GetText(); }
	bool IsVisible() {return m_pyControlUI->IsVisible();}
	void SetVisible(bool bVisible = true){m_pyControlUI->SetVisible(bVisible);}
	bool IsEnabled() {return m_pyControlUI->IsEnabled();}
	void SetEnabled(bool bEnable = true){m_pyControlUI->SetEnabled(bEnable);}
	bool IsFocused() {return m_pyControlUI->IsFocused();}
	void SetFocus(){m_pyControlUI->SetFocus();}

protected:
	CControlUI* m_pyControlUI;   // dui��ʵ�ֵ�ui����
};

class PyLabelUI
{
public:
	PyLabelUI(PControlUI pControlUI) {m_pyControlUI = (CLabelUI*)pControlUI;}
	~PyLabelUI() {}
	PControlUI GetSelf() {return (PControlUI)m_pyControlUI;}

	void SetName(LPCSTR pstrName) {m_pyControlUI->SetName(pstrName);};
	void ApplyAttributeList(LPCSTR pstrList) {m_pyControlUI->ApplyAttributeList(pstrList);}
	void SetText(LPCSTR caption) { m_pyControlUI->SetText(caption); }
	CDuiString GetText() { return m_pyControlUI->GetText(); }
	bool IsVisible() {return m_pyControlUI->IsVisible();}
	void SetVisible(bool bVisible = true){m_pyControlUI->SetVisible(bVisible);}
	bool IsEnabled() {return m_pyControlUI->IsEnabled();}
	void SetEnabled(bool bEnable = true){m_pyControlUI->SetEnabled(bEnable);}
	bool IsFocused() {return m_pyControlUI->IsFocused();}
	void SetFocus(){m_pyControlUI->SetFocus();}

protected:
	CLabelUI* m_pyControlUI;   // dui��ʵ�ֵ�ui����
};

class PyButtonUI
{
public:
	PyButtonUI(PControlUI pControlUI) {m_pyControlUI = (CButtonUI*)pControlUI;}
	~PyButtonUI() {}
	PControlUI GetSelf() {return (PControlUI)m_pyControlUI;}

	void SetName(LPCSTR pstrName) {m_pyControlUI->SetName(pstrName);};
	void ApplyAttributeList(LPCSTR pstrList) {m_pyControlUI->ApplyAttributeList(pstrList);}
	void SetText(LPCSTR caption) { m_pyControlUI->SetText(caption); }
	CDuiString GetText() { return m_pyControlUI->GetText(); }
	bool IsVisible() {return m_pyControlUI->IsVisible();}
	void SetVisible(bool bVisible = true){m_pyControlUI->SetVisible(bVisible);}
	bool IsEnabled() {return m_pyControlUI->IsEnabled();}
	void SetEnabled(bool bEnable = true){m_pyControlUI->SetEnabled(bEnable);}
	bool IsFocused() {return m_pyControlUI->IsFocused();}
	void SetFocus(){m_pyControlUI->SetFocus();}

protected:
	CButtonUI* m_pyControlUI;   // dui��ʵ�ֵ�ui����
};

class PyOptionUI
{
public:
	PyOptionUI(PControlUI pControlUI) {m_pyControlUI = (COptionUI*)pControlUI;}
	~PyOptionUI() {}
	PControlUI GetSelf() {return (PControlUI)m_pyControlUI;}

	void SetName(LPCSTR pstrName) {m_pyControlUI->SetName(pstrName);};
	void ApplyAttributeList(LPCSTR pstrList) {m_pyControlUI->ApplyAttributeList(pstrList);}
	bool IsVisible() {return m_pyControlUI->IsVisible();}
	void SetVisible(bool bVisible = true){m_pyControlUI->SetVisible(bVisible);}
	bool IsEnabled() {return m_pyControlUI->IsEnabled();}
	void SetEnabled(bool bEnable = true){m_pyControlUI->SetEnabled(bEnable);}

protected:
	COptionUI* m_pyControlUI;   // dui��ʵ�ֵ�ui����
};

class PyCheckBoxUI
{
public:
	PyCheckBoxUI(PControlUI pControlUI) {m_pyControlUI = (CCheckBoxUI*)pControlUI;}
	~PyCheckBoxUI() {}
	PControlUI GetSelf() {return (PControlUI)m_pyControlUI;}

	void SetName(LPCSTR pstrName) {m_pyControlUI->SetName(pstrName);};
	void ApplyAttributeList(LPCSTR pstrList) {m_pyControlUI->ApplyAttributeList(pstrList);}
	bool IsVisible() {return m_pyControlUI->IsVisible();}
	void SetVisible(bool bVisible = true){m_pyControlUI->SetVisible(bVisible);}
	bool IsEnabled() {return m_pyControlUI->IsEnabled();}
	void SetEnabled(bool bEnable = true){m_pyControlUI->SetEnabled(bEnable);}
	bool GetCheck() {return m_pyControlUI->GetCheck();}
	void SetCheck(bool bCheck = true){m_pyControlUI->SetCheck(bCheck);}

protected:
	CCheckBoxUI* m_pyControlUI;   // dui��ʵ�ֵ�ui����
};

class PyProgressUI
{
public:
	PyProgressUI(PControlUI pControlUI) {m_pyControlUI = (CProgressUI*)pControlUI;}
	~PyProgressUI() {}
	PControlUI GetSelf() {return (PControlUI)m_pyControlUI;}

	void SetName(LPCSTR pstrName) {m_pyControlUI->SetName(pstrName);};
	void ApplyAttributeList(LPCSTR pstrList) {m_pyControlUI->ApplyAttributeList(pstrList);}
	bool IsVisible() {return m_pyControlUI->IsVisible();}
	void SetVisible(bool bVisible = true){m_pyControlUI->SetVisible(bVisible);}
	bool IsEnabled() {return m_pyControlUI->IsEnabled();}
	void SetEnabled(bool bEnable = true){m_pyControlUI->SetEnabled(bEnable);}
	int GetValue() {return m_pyControlUI->GetValue();}
	void SetValue(int nValue) {m_pyControlUI->SetValue(nValue);}

protected:
	CProgressUI* m_pyControlUI;   // dui��ʵ�ֵ�ui����
};

class PyAnimationUI
{
public:
	PyAnimationUI(PControlUI pControlUI) {m_pyControlUI = (CAnimationUI*)pControlUI;}
	~PyAnimationUI() {}
	PControlUI GetSelf() {return (PControlUI)m_pyControlUI;}

	void SetName(LPCSTR pstrName) {m_pyControlUI->SetName(pstrName);};
	void ApplyAttributeList(LPCSTR pstrList) {m_pyControlUI->ApplyAttributeList(pstrList);}
	bool IsVisible() {return m_pyControlUI->IsVisible();}
	void SetVisible(bool bVisible = true){m_pyControlUI->SetVisible(bVisible);}
	bool IsEnabled() {return m_pyControlUI->IsEnabled();}
	void SetEnabled(bool bEnable = true){m_pyControlUI->SetEnabled(bEnable);}
	void StartAnimation(){m_pyControlUI->StartAnimation();}
	void StopAnimation(){m_pyControlUI->StopAnimation();}

protected:
	CAnimationUI* m_pyControlUI;   // dui��ʵ�ֵ�ui����
};

class PyHorizontalLayoutUI
{
public:
	PyHorizontalLayoutUI(PControlUI pControlUI) {m_pyControlUI = (CHorizontalLayoutUI*)pControlUI;}
	~PyHorizontalLayoutUI() {}
	PControlUI GetSelf() {return (PControlUI)m_pyControlUI;}

	void SetName(LPCSTR pstrName) {m_pyControlUI->SetName(pstrName);};
	void ApplyAttributeList(LPCSTR pstrList) {m_pyControlUI->ApplyAttributeList(pstrList);}
	bool IsVisible() {return m_pyControlUI->IsVisible();}
	void SetVisible(bool bVisible = true){m_pyControlUI->SetVisible(bVisible);}
	bool IsEnabled() {return m_pyControlUI->IsEnabled();}
	void SetEnabled(bool bEnable = true){m_pyControlUI->SetEnabled(bEnable);}

	void SetAttribute(LPCSTR pstrName, LPCSTR pstrValue) {m_pyControlUI->SetAttribute(pstrName, pstrValue);}
	bool Add(PControlUI pControl) { return m_pyControlUI->Add((CControlUI*)pControl); }

protected:
	CHorizontalLayoutUI* m_pyControlUI;   // dui��ʵ�ֵ�ui����
};

class PyVerticalLayoutUI
{
public:
	PyVerticalLayoutUI(PControlUI pControlUI) {m_pyControlUI = (CVerticalLayoutUI*)pControlUI;}
	~PyVerticalLayoutUI() {}
	PControlUI GetSelf() {return (PControlUI)m_pyControlUI;}

	void SetName(LPCSTR pstrName) {m_pyControlUI->SetName(pstrName);};
	void ApplyAttributeList(LPCSTR pstrList) {m_pyControlUI->ApplyAttributeList(pstrList);}
	bool IsVisible() {return m_pyControlUI->IsVisible();}
	void SetVisible(bool bVisible = true){m_pyControlUI->SetVisible(bVisible);}
	bool IsEnabled() {return m_pyControlUI->IsEnabled();}
	void SetEnabled(bool bEnable = true){m_pyControlUI->SetEnabled(bEnable);}

	void SetAttribute(LPCSTR pstrName, LPCSTR pstrValue) {m_pyControlUI->SetAttribute(pstrName, pstrValue);}
	bool Add(PControlUI pControl) { return m_pyControlUI->Add((CControlUI*)pControl); }

protected:
	CVerticalLayoutUI* m_pyControlUI;   // dui��ʵ�ֵ�ui����
};

class PyTabLayoutUI
{
public:
	PyTabLayoutUI(PControlUI pControlUI) {m_pyControlUI = (CTabLayoutUI*)pControlUI;}
	~PyTabLayoutUI() {}
	PControlUI GetSelf() {return (PControlUI)m_pyControlUI;}

	void SetName(LPCSTR pstrName) {m_pyControlUI->SetName(pstrName);};
	void ApplyAttributeList(LPCSTR pstrList) {m_pyControlUI->ApplyAttributeList(pstrList);}
	void SetText(LPCSTR caption) { m_pyControlUI->SetText(caption); }
	CDuiString GetText() { return m_pyControlUI->GetText(); }
	bool IsVisible() {return m_pyControlUI->IsVisible();}
	void SetVisible(bool bVisible = true){m_pyControlUI->SetVisible(bVisible);}
	bool IsEnabled() {return m_pyControlUI->IsEnabled();}
	void SetEnabled(bool bEnable = true){m_pyControlUI->SetEnabled(bEnable);}
	bool IsFocused() {return m_pyControlUI->IsFocused();}
	void SetFocus(){m_pyControlUI->SetFocus();}

	bool Add(PControlUI pControl) { return m_pyControlUI->Add((CControlUI*)pControl); }
	bool SelectItem(int iIndex) { return m_pyControlUI->SelectItem(iIndex); }

protected:
	CTabLayoutUI* m_pyControlUI;   // dui��ʵ�ֵ�ui����
};

class PyListUI
{
public:
	PyListUI(PControlUI pControlUI) {m_pyControlUI = (CListUI*)pControlUI;}
	~PyListUI() {}
	PControlUI GetSelf() {return (PControlUI)m_pyControlUI;}

	void SetName(LPCSTR pstrName) {m_pyControlUI->SetName(pstrName);};
	void ApplyAttributeList(LPCSTR pstrList) {m_pyControlUI->ApplyAttributeList(pstrList);}
	bool IsVisible() {return m_pyControlUI->IsVisible();}
	void SetVisible(bool bVisible = true){m_pyControlUI->SetVisible(bVisible);}
	bool IsEnabled() {return m_pyControlUI->IsEnabled();}
	void SetEnabled(bool bEnable = true){m_pyControlUI->SetEnabled(bEnable);}
	bool Add(PControlUI pControl) { return m_pyControlUI->Add((CControlUI*)pControl); }

protected:
	CListUI* m_pyControlUI;   // dui��ʵ�ֵ�ui����
};

class PyListContainerElementUI
{
public:
	PyListContainerElementUI(PControlUI pControlUI) {m_pyControlUI = (CListContainerElementUI*)pControlUI;}
	~PyListContainerElementUI() {}
	PControlUI GetSelf() {return (PControlUI)m_pyControlUI;}

	void SetName(LPCSTR pstrName) {m_pyControlUI->SetName(pstrName);};
	void ApplyAttributeList(LPCSTR pstrList) {m_pyControlUI->ApplyAttributeList(pstrList);}
	bool IsVisible() {return m_pyControlUI->IsVisible();}
	void SetVisible(bool bVisible = true){m_pyControlUI->SetVisible(bVisible);}
	bool IsEnabled() {return m_pyControlUI->IsEnabled();}
	void SetEnabled(bool bEnable = true){m_pyControlUI->SetEnabled(bEnable);}
	bool Add(PControlUI pControl) { return m_pyControlUI->Add((CControlUI*)pControl); }

protected:
	CListContainerElementUI* m_pyControlUI;   // dui��ʵ�ֵ�ui����
};

class PyUIFactory
{
public:
	PyUIFactory() {}
	~PyUIFactory() {}

	PControlUI CreateControlUI(){return (PControlUI)(new CControlUI());}
	PControlUI CreateLabelUI(){return (PControlUI)(new CLabelUI());}
	PControlUI CreateButtonUI(){return (PControlUI)(new CButtonUI());}
	PControlUI CreateOptionUI(){return (PControlUI)(new COptionUI());}
	PControlUI CreateCheckBoxUI(){return (PControlUI)(new CCheckBoxUI());}
	PControlUI CreateProgressUI(){return (PControlUI)(new CProgressUI());}
	PControlUI CreateAnimationUI(){return (PControlUI)(new CAnimationUI());}
	PControlUI CreateTabLayoutUI(){return (PControlUI)(new CTabLayoutUI());}
	PControlUI CreateHorizontalLayoutUI(){return (PControlUI)(new CHorizontalLayoutUI());}
	PControlUI CreateVerticalLayoutUI(){return (PControlUI)(new CVerticalLayoutUI());}
	PControlUI CreateListUI(){return (PControlUI)(new CListUI());}
	PControlUI CreateListContainerElementUI(){return (PControlUI)(new CListContainerElementUI());}
};

// An abstract base class
class PyUIBase : public boost::noncopyable
{
public:
	virtual ~PyUIBase() {};
	virtual LPCSTR GetSkinFile(){return NULL;};
	virtual LPCSTR GetWindowClassName(){return NULL;};	

	virtual void OnFinalMessage(ULONG hWnd){};
	virtual void InitWindow(){};;
	virtual LRESULT HandleMessage(UINT uMsg, WPARAM wParam, LPARAM lParam){return 0;};
	virtual LRESULT HandleCustomMessage(UINT uMsg, WPARAM wParam, LPARAM lParam){return 0;};
	virtual void OnNotify(LPCSTR sendor, LPCSTR sType, WPARAM wParam, LPARAM lParam){};
	virtual void OnPrepare(LPCSTR sendor, WPARAM wParam, LPARAM lParam){};
	virtual void OnExit(LPCSTR sendor, WPARAM wParam, LPARAM lParam){};
	virtual void OnTimer(LPCSTR sendor, WPARAM wParam, LPARAM lParam){};

	virtual void Show() {m_pyFrameUI->ShowWindow();};
	virtual UINT ShowModal() {return m_pyFrameUI->ShowModal();};

	virtual void SetHWnd(ULONG hWnd) { m_hWnd = hWnd;};
	virtual ULONG GetHWnd() { return m_hWnd;};
	virtual void CloseWindow() { ::PostMessage((HWND)m_hWnd, WM_CLOSE, 0L, 0L); }
	virtual void HideWindow() { ::ShowWindow((HWND)m_hWnd, SW_HIDE); }
	virtual void ExitApp() { ::ExitProcess(0); }
	ULONG ProcessMessages() { return m_pyFrameUI->ProcessMessages();}

	PControlUI FindControl(LPCSTR ControlName)
	{
		CControlUI* pControl = m_pyFrameUI->FindControl(ControlName);
		return (PControlUI)pControl;
	}
	// Ϊ����ʹ�ü���
	virtual void SetText(LPCSTR ControlName, LPCSTR caption)
	{
		CControlUI* pControl = m_pyFrameUI->FindControl(ControlName);
		pControl->SetText(caption);
	}
	// �ӿ����ӷ���:
	// ���ӷ�������Ҫ��PyUIBaseWrap����2���ӿڷ�װ, ��Ҫ��app��ģ�鶨����ͷ�����Ӧ�ĺ�������

	virtual void SetPyFrameUI(PyFrameUI *PyFrameUI) { m_pyFrameUI = PyFrameUI;};

protected:
	ULONG	m_hWnd;
	PyFrameUI* m_pyFrameUI;   // dui��ʵ�ֵ�ui����
};

// Familiar Boost.Python wrapper class for Base
struct PyUIBaseWrap : PyUIBase, wrapper<PyUIBase>
{
	virtual PControlUI FindControl(LPCSTR ControlName) { return this->PyUIBase::FindControl(ControlName); }
	virtual ULONG ProcessMessages() { return this->PyUIBase::ProcessMessages(); }
	virtual UINT ShowModal() { return this->PyUIBase::ShowModal(); }
	UINT default_ShowModal() { return this->PyUIBase::ShowModal(); }
	virtual void Show() { this->PyUIBase::Show(); }
	void default_Show() { this->PyUIBase::Show(); }
	virtual void ExitApp()
	{
		if (override oSetHWnd = this->get_override("ExitApp"))
			oSetHWnd(); 
		else
			this->PyUIBase::ExitApp();
	}
	void default_ExitApp() { this->PyUIBase::ExitApp(); }
	virtual void HideWindow()
	{
		if (override oSetHWnd = this->get_override("HideWindow"))
			oSetHWnd(); 
		else
			this->PyUIBase::HideWindow();
	}
	void default_HideWindow() { this->PyUIBase::HideWindow(); }
	virtual void CloseWindow()
	{
		if (override oSetHWnd = this->get_override("CloseWindow"))
			oSetHWnd(); 
		else
			this->PyUIBase::CloseWindow();
	}
	void default_CloseWindow() { this->PyUIBase::CloseWindow(); }

	virtual void SetText(LPCSTR ControlName, LPCSTR caption)
	{
		if (override oSetHWnd = this->get_override("SetText"))
			oSetHWnd(ControlName, caption); 
		else
			this->PyUIBase::SetText(ControlName, caption);
	}
	virtual void default_SetText(LPCSTR ControlName, LPCSTR caption) { this->PyUIBase::SetText(ControlName, caption); }
	virtual void SetHWnd(ULONG hWnd)
	{
		if (override oSetHWnd = this->get_override("SetHWnd"))
			oSetHWnd(hWnd); 
		else
			this->PyUIBase::SetHWnd(hWnd);
	}
	void default_SetHWnd(ULONG hWnd) { this->PyUIBase::SetHWnd(hWnd); }
	virtual ULONG GetHWnd()
	{
		if (override oGetHWnd = this->get_override("GetHWnd"))
			return oGetHWnd(); 
		else
			return this->PyUIBase::GetHWnd();
	}
	ULONG default_GetHWnd() { return this->PyUIBase::GetHWnd(); }

	virtual LPCSTR GetSkinFile() { return this->get_override("GetSkinFile")(); }
	LPCSTR default_GetSkinFile() { return this->get_override("GetSkinFile")(); }
	virtual LPCSTR GetWindowClassName() { return this->get_override("GetWindowClassName")(); }
	LPCSTR default_GetWindowClassName() { return this->get_override("GetWindowClassName")(); }
	virtual void OnFinalMessage(ULONG hWnd) { this->get_override("OnFinalMessage")(hWnd); }
	void default_OnFinalMessage(ULONG hWnd) { this->get_override("OnFinalMessage")(hWnd); }
	virtual void InitWindow() { this->get_override("InitWindow")(); }
	void default_InitWindow() { this->get_override("InitWindow")(); }
	virtual LRESULT HandleMessage(UINT uMsg, WPARAM wParam, LPARAM lParam) { return this->get_override("HandleMessage")(uMsg, wParam, lParam); }
	LRESULT default_HandleMessage(UINT uMsg, WPARAM wParam, LPARAM lParam) { return this->PyUIBase::HandleMessage(uMsg, wParam, lParam); }
	virtual LRESULT HandleCustomMessage(UINT uMsg, WPARAM wParam, LPARAM lParam) { return this->get_override("HandleCustomMessage")(uMsg, wParam, lParam); }
	LRESULT default_HandleCustomMessage(UINT uMsg, WPARAM wParam, LPARAM lParam) { return this->PyUIBase::HandleCustomMessage(uMsg, wParam, lParam); }
	virtual void OnNotify(LPCSTR sendor, LPCSTR sType, WPARAM wParam, LPARAM lParam) { this->get_override("OnNotify")(sendor, sType, wParam, lParam); }
	void default_OnNotify(LPCSTR sendor, LPCSTR sType, WPARAM wParam, LPARAM lParam) { this->PyUIBase::OnNotify(sendor, sType, wParam, lParam); }
	virtual void OnPrepare(LPCSTR sendor, WPARAM wParam, LPARAM lParam) { this->get_override("OnPrepare")(sendor, wParam, lParam); }
	void default_OnPrepare(LPCSTR sendor, WPARAM wParam, LPARAM lParam) { this->PyUIBase::OnPrepare(sendor, wParam, lParam); }
	virtual void OnExit(LPCSTR sendor, WPARAM wParam, LPARAM lParam) { this->get_override("OnExit")(sendor, wParam, lParam); }
	void default_OnExit(LPCSTR sendor, WPARAM wParam, LPARAM lParam) { this->PyUIBase::OnExit(sendor, wParam, lParam); }
	virtual void OnTimer(LPCSTR sendor, WPARAM wParam, LPARAM lParam) { this->get_override("OnTimer")(sendor, wParam, lParam); }
	void default_OnTimer(LPCSTR sendor, WPARAM wParam, LPARAM lParam) { this->PyUIBase::OnTimer(sendor, wParam, lParam); }
};

// ������python��ui������, python��createform�ӿ�ͨ��PyFrameUI�������ڣ�
// ������ͨ��PyUIBase������python��ҵ���߼�
class PyFrameCreator
{
public:

	PyFrameCreator();
	~PyFrameCreator();

public:
	object CreateForm(ULONG hParent, LPCSTR pyModule, LPCSTR pyClassName);
	void Show();
	UINT ShowModal();

protected:
	CDuiString m_xmlSkinFile;
	CDuiString m_pyModule; 
	CDuiString m_pyClassName;
	PyFrameUI* m_pyFrameUI;   // dui��ʵ�ֵ�ui����
	object m_Module;
	object m_ClassUI; 
	object m_InstanceUI;

	PyUIBase* m_pyBaseUI;  // ��python��ʵ�ֵĵ�ҵ�����
};

#endif // PYFRAME_HPP