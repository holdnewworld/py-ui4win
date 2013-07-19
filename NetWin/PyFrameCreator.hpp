
#ifndef PYFRAME_HPP
#define PYFRAME_HPP

#include<boost/python.hpp>
#include "PyFrameUI.hpp"

using namespace boost::python;


class PyControlUI
{
public:
	PyControlUI(ULONG pControlUI) {m_pyControlUI = (CControlUI*)pControlUI;}
	~PyControlUI() {}
	ULONG GetSelf() {return (ULONG)m_pyControlUI;}

	void SetName(LPCSTR pstrName) {m_pyControlUI->SetName(pstrName);};
	void ApplyAttributeList(LPCSTR pstrList) {m_pyControlUI->ApplyAttributeList(pstrList);}
	void SetText(LPCSTR caption) { m_pyControlUI->SetText(caption); }
	std::string GetText() { return std::string(m_pyControlUI->GetText().GetData()); }
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
	PyLabelUI(ULONG pControlUI) {m_pyControlUI = (CLabelUI*)pControlUI;}
	~PyLabelUI() {}
	ULONG GetSelf() {return (ULONG)m_pyControlUI;}

	void SetName(LPCSTR pstrName) {m_pyControlUI->SetName(pstrName);};
	void ApplyAttributeList(LPCSTR pstrList) {m_pyControlUI->ApplyAttributeList(pstrList);}
	void SetText(LPCSTR caption) { m_pyControlUI->SetText(caption); }
	std::string GetText() { return std::string(m_pyControlUI->GetText().GetData()); }
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
	PyButtonUI(ULONG pControlUI) {m_pyControlUI = (CButtonUI*)pControlUI;}
	~PyButtonUI() {}
	ULONG GetSelf() {return (ULONG)m_pyControlUI;}

	void SetName(LPCSTR pstrName) {m_pyControlUI->SetName(pstrName);};
	void ApplyAttributeList(LPCSTR pstrList) {m_pyControlUI->ApplyAttributeList(pstrList);}
	void SetText(LPCSTR caption) { m_pyControlUI->SetText(caption); }
	std::string GetText() { return std::string(m_pyControlUI->GetText().GetData()); }
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
	PyOptionUI(ULONG pControlUI) {m_pyOptionUI = (COptionUI*)pControlUI;}
	~PyOptionUI() {}
	ULONG GetSelf() {return (ULONG)m_pyOptionUI;}

	void SetName(LPCSTR pstrName) {m_pyOptionUI->SetName(pstrName);};
	void ApplyAttributeList(LPCSTR pstrList) {m_pyOptionUI->ApplyAttributeList(pstrList);}
	bool IsVisible() {return m_pyOptionUI->IsVisible();}
	void SetVisible(bool bVisible = true){m_pyOptionUI->SetVisible(bVisible);}
	bool IsEnabled() {return m_pyOptionUI->IsEnabled();}
	void SetEnabled(bool bEnable = true){m_pyOptionUI->SetEnabled(bEnable);}

protected:
	COptionUI* m_pyOptionUI;   // dui��ʵ�ֵ�ui����
};

class PyCheckBoxUI
{
public:
	PyCheckBoxUI(ULONG pControlUI) {m_pyCheckBoxUI = (CCheckBoxUI*)pControlUI;}
	~PyCheckBoxUI() {}
	ULONG GetSelf() {return (ULONG)m_pyCheckBoxUI;}

	void SetName(LPCSTR pstrName) {m_pyCheckBoxUI->SetName(pstrName);};
	void ApplyAttributeList(LPCSTR pstrList) {m_pyCheckBoxUI->ApplyAttributeList(pstrList);}
	bool IsVisible() {return m_pyCheckBoxUI->IsVisible();}
	void SetVisible(bool bVisible = true){m_pyCheckBoxUI->SetVisible(bVisible);}
	bool IsEnabled() {return m_pyCheckBoxUI->IsEnabled();}
	void SetEnabled(bool bEnable = true){m_pyCheckBoxUI->SetEnabled(bEnable);}
	bool GetCheck() {return m_pyCheckBoxUI->GetCheck();}
	void SetCheck(bool bCheck = true){m_pyCheckBoxUI->SetCheck(bCheck);}

protected:
	CCheckBoxUI* m_pyCheckBoxUI;   // dui��ʵ�ֵ�ui����
};

class PyProgressUI
{
public:
	PyProgressUI(ULONG pControlUI) {m_pyProgressUI = (CProgressUI*)pControlUI;}
	~PyProgressUI() {}
	ULONG GetSelf() {return (ULONG)m_pyProgressUI;}

	void SetName(LPCSTR pstrName) {m_pyProgressUI->SetName(pstrName);};
	void ApplyAttributeList(LPCSTR pstrList) {m_pyProgressUI->ApplyAttributeList(pstrList);}
	bool IsVisible() {return m_pyProgressUI->IsVisible();}
	void SetVisible(bool bVisible = true){m_pyProgressUI->SetVisible(bVisible);}
	bool IsEnabled() {return m_pyProgressUI->IsEnabled();}
	void SetEnabled(bool bEnable = true){m_pyProgressUI->SetEnabled(bEnable);}
	int GetValue() {return m_pyProgressUI->GetValue();}
	void SetValue(int nValue) {m_pyProgressUI->SetValue(nValue);}

protected:
	CProgressUI* m_pyProgressUI;   // dui��ʵ�ֵ�ui����
};

class PyAnimationUI
{
public:
	PyAnimationUI(ULONG pControlUI) {m_pyAnimationlUI = (CAnimationUI*)pControlUI;}
	~PyAnimationUI() {}
	ULONG GetSelf() {return (ULONG)m_pyAnimationlUI;}

	void SetName(LPCSTR pstrName) {m_pyAnimationlUI->SetName(pstrName);};
	void ApplyAttributeList(LPCSTR pstrList) {m_pyAnimationlUI->ApplyAttributeList(pstrList);}
	bool IsVisible() {return m_pyAnimationlUI->IsVisible();}
	void SetVisible(bool bVisible = true){m_pyAnimationlUI->SetVisible(bVisible);}
	bool IsEnabled() {return m_pyAnimationlUI->IsEnabled();}
	void SetEnabled(bool bEnable = true){m_pyAnimationlUI->SetEnabled(bEnable);}
	void StartAnimation(){m_pyAnimationlUI->StartAnimation();}
	void StopAnimation(){m_pyAnimationlUI->StopAnimation();}

protected:
	CAnimationUI* m_pyAnimationlUI;   // dui��ʵ�ֵ�ui����
};

class PyHorizontalLayoutUI
{
public:
	PyHorizontalLayoutUI(ULONG pControlUI) {m_pyHorizontalLayoutUI = (CHorizontalLayoutUI*)pControlUI;}
	~PyHorizontalLayoutUI() {}
	ULONG GetSelf() {return (ULONG)m_pyHorizontalLayoutUI;}

	void SetName(LPCSTR pstrName) {m_pyHorizontalLayoutUI->SetName(pstrName);};
	void ApplyAttributeList(LPCSTR pstrList) {m_pyHorizontalLayoutUI->ApplyAttributeList(pstrList);}
	bool IsVisible() {return m_pyHorizontalLayoutUI->IsVisible();}
	void SetVisible(bool bVisible = true){m_pyHorizontalLayoutUI->SetVisible(bVisible);}
	bool IsEnabled() {return m_pyHorizontalLayoutUI->IsEnabled();}
	void SetEnabled(bool bEnable = true){m_pyHorizontalLayoutUI->SetEnabled(bEnable);}

	void SetAttribute(LPCSTR pstrName, LPCSTR pstrValue) {m_pyHorizontalLayoutUI->SetAttribute(pstrName, pstrValue);}
	bool Add(ULONG pControl) { return m_pyHorizontalLayoutUI->Add((CControlUI*)pControl); }

protected:
	CHorizontalLayoutUI* m_pyHorizontalLayoutUI;   // dui��ʵ�ֵ�ui����
};

class PyVerticalLayoutUI
{
public:
	PyVerticalLayoutUI(ULONG pControlUI) {m_pyVerticalLayoutUI = (CVerticalLayoutUI*)pControlUI;}
	~PyVerticalLayoutUI() {}
	ULONG GetSelf() {return (ULONG)m_pyVerticalLayoutUI;}

	void SetName(LPCSTR pstrName) {m_pyVerticalLayoutUI->SetName(pstrName);};
	void ApplyAttributeList(LPCSTR pstrList) {m_pyVerticalLayoutUI->ApplyAttributeList(pstrList);}
	bool IsVisible() {return m_pyVerticalLayoutUI->IsVisible();}
	void SetVisible(bool bVisible = true){m_pyVerticalLayoutUI->SetVisible(bVisible);}
	bool IsEnabled() {return m_pyVerticalLayoutUI->IsEnabled();}
	void SetEnabled(bool bEnable = true){m_pyVerticalLayoutUI->SetEnabled(bEnable);}

	void SetAttribute(LPCSTR pstrName, LPCSTR pstrValue) {m_pyVerticalLayoutUI->SetAttribute(pstrName, pstrValue);}
	bool Add(ULONG pControl) { return m_pyVerticalLayoutUI->Add((CControlUI*)pControl); }

protected:
	CVerticalLayoutUI* m_pyVerticalLayoutUI;   // dui��ʵ�ֵ�ui����
};

class PyTabLayoutUI
{
public:
	PyTabLayoutUI(ULONG pControlUI) {m_pyControlUI = (CTabLayoutUI*)pControlUI;}
	~PyTabLayoutUI() {}
	ULONG GetSelf() {return (ULONG)m_pyControlUI;}

	void SetName(LPCSTR pstrName) {m_pyControlUI->SetName(pstrName);};
	void ApplyAttributeList(LPCSTR pstrList) {m_pyControlUI->ApplyAttributeList(pstrList);}
	void SetText(LPCSTR caption) { m_pyControlUI->SetText(caption); }
	std::string GetText() { return std::string(m_pyControlUI->GetText().GetData()); }
	bool IsVisible() {return m_pyControlUI->IsVisible();}
	void SetVisible(bool bVisible = true){m_pyControlUI->SetVisible(bVisible);}
	bool IsEnabled() {return m_pyControlUI->IsEnabled();}
	void SetEnabled(bool bEnable = true){m_pyControlUI->SetEnabled(bEnable);}
	bool IsFocused() {return m_pyControlUI->IsFocused();}
	void SetFocus(){m_pyControlUI->SetFocus();}

	bool Add(ULONG pControl) { return m_pyControlUI->Add((CControlUI*)pControl); }
	bool SelectItem(int iIndex) { return m_pyControlUI->SelectItem(iIndex); }

protected:
	CTabLayoutUI* m_pyControlUI;   // dui��ʵ�ֵ�ui����
};

class PyListUI
{
public:
	PyListUI(ULONG pControlUI) {m_pyListUI = (CListUI*)pControlUI;}
	~PyListUI() {}
	ULONG GetSelf() {return (ULONG)m_pyListUI;}

	void SetName(LPCSTR pstrName) {m_pyListUI->SetName(pstrName);};
	void ApplyAttributeList(LPCSTR pstrList) {m_pyListUI->ApplyAttributeList(pstrList);}
	bool IsVisible() {return m_pyListUI->IsVisible();}
	void SetVisible(bool bVisible = true){m_pyListUI->SetVisible(bVisible);}
	bool IsEnabled() {return m_pyListUI->IsEnabled();}
	void SetEnabled(bool bEnable = true){m_pyListUI->SetEnabled(bEnable);}
	bool Add(ULONG pControl) { return m_pyListUI->Add((CControlUI*)pControl); }

protected:
	CListUI* m_pyListUI;   // dui��ʵ�ֵ�ui����
};

class PyListContainerElementUI
{
public:
	PyListContainerElementUI(ULONG pControlUI) {m_pyListContainerElementUI = (CListContainerElementUI*)pControlUI;}
	~PyListContainerElementUI() {}
	ULONG GetSelf() {return (ULONG)m_pyListContainerElementUI;}

	void SetName(LPCSTR pstrName) {m_pyListContainerElementUI->SetName(pstrName);};
	void ApplyAttributeList(LPCSTR pstrList) {m_pyListContainerElementUI->ApplyAttributeList(pstrList);}
	bool IsVisible() {return m_pyListContainerElementUI->IsVisible();}
	void SetVisible(bool bVisible = true){m_pyListContainerElementUI->SetVisible(bVisible);}
	bool IsEnabled() {return m_pyListContainerElementUI->IsEnabled();}
	void SetEnabled(bool bEnable = true){m_pyListContainerElementUI->SetEnabled(bEnable);}
	bool Add(ULONG pControl) { return m_pyListContainerElementUI->Add((CControlUI*)pControl); }

protected:
	CListContainerElementUI* m_pyListContainerElementUI;   // dui��ʵ�ֵ�ui����
};

class PyUIFactory
{
public:
	PyUIFactory() {}
	~PyUIFactory() {}

	ULONG CreateControlUI(){return (ULONG)(new CControlUI());}
	ULONG CreateLabelUI(){return (ULONG)(new CLabelUI());}
	ULONG CreateButtonUI(){return (ULONG)(new CButtonUI());}
	ULONG CreateOptionUI(){return (ULONG)(new COptionUI());}
	ULONG CreateCheckBoxUI(){return (ULONG)(new CCheckBoxUI());}
	ULONG CreateProgressUI(){return (ULONG)(new CProgressUI());}
	ULONG CreateAnimationUI(){return (ULONG)(new CAnimationUI());}
	ULONG CreateTabLayoutUI(){return (ULONG)(new CTabLayoutUI());}
	ULONG CreateHorizontalLayoutUI(){return (ULONG)(new CHorizontalLayoutUI());}
	ULONG CreateVerticalLayoutUI(){return (ULONG)(new CVerticalLayoutUI());}
	ULONG CreateListUI(){return (ULONG)(new CListUI());}
	ULONG CreateListContainerElementUI(){return (ULONG)(new CListContainerElementUI());}
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

	ULONG FindControl(LPCSTR ControlName)
	{
		CControlUI* pControl = m_pyFrameUI->FindControl(ControlName);
		return (ULONG)pControl;
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
	virtual ULONG FindControl(LPCSTR ControlName) { return this->PyUIBase::FindControl(ControlName); }
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