
#if !defined(AFX_STDAFX_H__A9DB83DB_A9FD_11D0_BFD1_444553540000__INCLUDED_)
#define AFX_STDAFX_H__A9DB83DB_A9FD_11D0_BFD1_444553540000__INCLUDED_

#pragma once

#define WIN32_LEAN_AND_MEAN	
#define _CRT_SECURE_NO_DEPRECATE

#include <windows.h>
#include <objbase.h>
#include "resource.h"

// ���� wtl �ı��뾯��
#define _CRT_SECURE_NO_WARNINGS
#define _CRT_NON_CONFORMING_SWPRINTFS

// ���η� strsafe.h �����ı��뾯��
#define STRSAFE_NO_DEPRECATE

#define __ENABLE_CSTRING_CLASS__

#define ARRSIZEOF(x) (sizeof(x)/sizeof(x[0]))

#include <atlbase.h>
#include <atlcoll.h>
#include <atlstr.h>
#define _WTL_NO_CSTRING
#define _WTL_NO_WTYPES
#include <strsafe.h>

enum WIN_OS_TYPE
{
	WIN_UNKOWN = 0,
	WIN_XP = 1,
	WIN_WIN7
};

enum BROWSER_STATUS
{
	ON_UNKOWN = 0,
	ON_LOGIN_PAGE = 1,                  // ���̵�½����
	ON_EAZFILE_DOWNLOAD_PAGE   // �������ݽ���
};

enum WORK_STATUS
{
	FREE_STATUS = 0, 
	TO_GET_CONFIG,
	SHOW_ADV,
	CHECK_DOWNLOADED_FILES, //
	TO_OPEN_URL_YET , // ��û�д�ҳ��
	TO_LOGIN, // ѡ����ϵͳ, ���ǻ�û�е�½
	LOGINED,     // �Ѿ���½
	OPEN_BAIDU,
	GET_DOWNLOAD_FILE_LINK,
	EAZ_DOWNLOAD,
	EAZ_DWONLOADING,
	EAZ_DOWNLOAD_FINISH,
	ALL_EAZ_DOWNLOADED,
	EAZ_FILE_GENERATED,
};

#define STR_MESS	L"adv"
#define STR_NAME	L"adv1"
#define STR_PWD		L"adv2"
#define STR_LOGOUTINDEX		L"adv3"
#define STR_USEBAIDU		L"bd"
#define STR_APIVERSION		L"api"
#define STR_EAZTOOLS	L"tools"
#define STR_CHECKBASE	L"checkbase"

#define NW_API_VERSION			1
#define DOWNLOAD_FILES			6


enum DOWNLOAD_STATUS
{
	NOT_DOWNLOAD,
	DOWNLOADING,
	DOWNLOADED,
};

typedef struct _EAZFILE
{
	CString		fileName;    // �ļ���
	int			index;		 // �����������
	ULONG		size;		 // �ļ���С
	ULONG		downloadBytes;
	CString		md5;         // md5ֵ

	DOWNLOAD_STATUS		status;
	BOOL		isEaztools;
	CString		url;

	_EAZFILE()
	{
		fileName = L"";
		index = 0;
		downloadBytes = 0;
		size = 0;
		md5 = L"";
		status = NOT_DOWNLOAD;
		isEaztools = FALSE;
		url = L"";
	}

} EAZFILE;


typedef struct _ADV_INFO
{
	CString		imgfileUrl;    // ����
	CString		advUrl;         // ����
	CString     fileName;

	_ADV_INFO()
	{
		imgfileUrl = L"";
		advUrl = L"";
		fileName = L"";
	}

} ADV_INFO;

#include "..\DuiLib\UIlib.h"
#include "Util.h"
using namespace DuiLib;
#ifdef _DEBUG
#pragma comment(lib, "..\\Lib\\DuiLib_d.lib")
#else
#pragma comment(lib, "..\\Lib\\DuiLib.lib")
#endif

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_STDAFX_H__A9DB83DB_A9FD_11D0_BFD1_444553540000__INCLUDED_)
