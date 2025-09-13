#include "StdAfx.h"
#include "PythonApplication.h"


PyObject* renderTargetSelectModel(PyObject* poSelf, PyObject* poArgs)
{
	BYTE index = 0;
	if (!PyTuple_GetByte(poArgs, 0, &index))
		return Py_BadArgument();

	int modelIndex = 0;
	if (!PyTuple_GetInteger(poArgs, 1, &modelIndex))
		return Py_BadArgument();

	CRenderTargetManager::Instance().GetRenderTarget(index)->SelectModel(modelIndex);

	return Py_BuildNone();
}
PyObject* renderTargetSetArmor(PyObject* poSelf, PyObject* poArgs)
{
	BYTE index = 0;
	if (!PyTuple_GetByte(poArgs, 0, &index))
		return Py_BadArgument();

	int modelIndex = 0;
	if (!PyTuple_GetInteger(poArgs, 1, &modelIndex))
		return Py_BadArgument();

#ifdef ENABLE_SPECULAR_SYSTEM
	bool bIsColor;
	if (!PyTuple_GetBoolean(poArgs, 2, &bIsColor))
		bIsColor = false;

	CRenderTargetManager::Instance().GetRenderTarget(index)->SetArmor(modelIndex, bIsColor);
#else
	CRenderTargetManager::Instance().GetRenderTarget(index)->SetArmor(modelIndex);
#endif

	return Py_BuildNone();

}

PyObject* renderTargetSetHair(PyObject* poSelf, PyObject* poArgs)										 
{
	BYTE index = 0;
	if (!PyTuple_GetByte(poArgs, 0, &index))
		return Py_BadArgument();

	int modelIndex = 0;
	if (!PyTuple_GetInteger(poArgs, 1, &modelIndex))
		return Py_BadArgument();

#ifdef ENABLE_SPECULAR_SYSTEM
	bool bIsColor;
	if (!PyTuple_GetBoolean(poArgs, 2, &bIsColor))
		bIsColor = false;

	CRenderTargetManager::Instance().GetRenderTarget(index)->ChangeHair(modelIndex, bIsColor);
#else
	CRenderTargetManager::Instance().GetRenderTarget(index)->ChangeHair(modelIndex);
#endif

	return Py_BuildNone();

}

PyObject* renderTargetSetWeapon(PyObject* poSelf, PyObject* poArgs)
{
	BYTE index = 0;
	if (!PyTuple_GetByte(poArgs, 0, &index))
		return Py_BadArgument();

	int modelIndex = 0;
	if (!PyTuple_GetInteger(poArgs, 1, &modelIndex))
		return Py_BadArgument();

#ifdef ENABLE_SPECULAR_SYSTEM
	bool bIsColor;
	if (!PyTuple_GetBoolean(poArgs, 2, &bIsColor))
		bIsColor = false;

	CRenderTargetManager::Instance().GetRenderTarget(index)->SetWeapon(modelIndex, bIsColor);
#else
	CRenderTargetManager::Instance().GetRenderTarget(index)->SetWeapon(modelIndex);
#endif

	return Py_BuildNone();

}

#ifdef ENABLE_ACCE_SYSTEM
PyObject* renderTargetSetSash(PyObject* poSelf, PyObject* poArgs)
{
	BYTE index = 0;
	if (!PyTuple_GetByte(poArgs, 0, &index))
		return Py_BadArgument();

	int modelIndex = 0;
	if (!PyTuple_GetInteger(poArgs, 1, &modelIndex))
		return Py_BadArgument();

#ifdef ENABLE_SPECULAR_SYSTEM
	bool bIsColor;
	if (!PyTuple_GetBoolean(poArgs, 2, &bIsColor))
		bIsColor = false;

	CRenderTargetManager::Instance().GetRenderTarget(index)->SetSash(modelIndex, bIsColor);
#else
	CRenderTargetManager::Instance().GetRenderTarget(index)->SetSash(modelIndex);
#endif

	return Py_BuildNone();

}
#endif

#ifdef ENABLE_SHINING_SYSTEM
PyObject* renderTargetSetShining(PyObject* poSelf, PyObject* poArgs)
{
	BYTE index = 0;
	if (!PyTuple_GetByte(poArgs, 0, &index))
		return Py_BadArgument();

	int modelIndex = 0;
	if (!PyTuple_GetInteger(poArgs, 1, &modelIndex))
		return Py_BadArgument();

	CRenderTargetManager::Instance().GetRenderTarget(index)->SetShining(modelIndex);

	return Py_BuildNone();

}
#endif

PyObject* renderTargetSetVisibility(PyObject* poSelf, PyObject* poArgs)
{
	BYTE index = 0;
	if (!PyTuple_GetByte(poArgs, 0, &index))
		return Py_BadArgument();

	bool isShow = false;
	if (!PyTuple_GetBoolean(poArgs, 1, &isShow))
		return Py_BadArgument();

	CRenderTargetManager::Instance().GetRenderTarget(index)->SetVisibility(isShow);

	return Py_BuildNone();
}

PyObject* renderTargetSetBackground(PyObject* poSelf, PyObject* poArgs)
{
	BYTE index = 0;
	if (!PyTuple_GetByte(poArgs, 0, &index))
		return Py_BadArgument();

	char * szPathName;
	if (!PyTuple_GetString(poArgs, 1, &szPathName))
		return Py_BadArgument();

	CRenderTargetManager::Instance().GetRenderTarget(index)->CreateBackground(
		szPathName, CPythonApplication::Instance().GetWidth(),
		CPythonApplication::Instance().GetHeight());
	return Py_BuildNone();
}

PyObject* renderSetRenderingPosition(PyObject* poSelf, PyObject* poArgs)
{
	BYTE index = 0;
	if (!PyTuple_GetByte(poArgs, 0, &index))
		return Py_BadArgument();

	bool bRender = false;
	if (!PyTuple_GetBoolean(poArgs, 1, &bRender))
		return Py_BadArgument();

	CRenderTargetManager::Instance().GetRenderTarget(index)->SetRenderingPosition(bRender);
	return Py_BuildNone();
}

PyObject* renderSetMove(PyObject* poSelf, PyObject* poArgs)
{
	BYTE index = 0;
	if (!PyTuple_GetByte(poArgs, 0, &index))
		return Py_BadArgument();

	bool bMove = false;
	if (!PyTuple_GetBoolean(poArgs, 1, &bMove))
		return Py_BadArgument();

	CRenderTargetManager::Instance().GetRenderTarget(index)->SetMove(bMove);
	return Py_BuildNone();
}

PyObject* renderSetZoom(PyObject* poSelf, PyObject* poArgs)
{
	BYTE index = 0;
	if (!PyTuple_GetByte(poArgs, 0, &index))
		return Py_BadArgument();

	bool bZoom = false;
	if (!PyTuple_GetBoolean(poArgs, 1, &bZoom))
		return Py_BadArgument();

	CRenderTargetManager::Instance().GetRenderTarget(index)->SetZoom(bZoom);
	return Py_BuildNone();
}

PyObject* renderResetSettings(PyObject* poSelf, PyObject* poArgs)
{
	BYTE index = 0;
	if (!PyTuple_GetByte(poArgs, 0, &index))
		return Py_BadArgument();

	CRenderTargetManager::Instance().GetRenderTarget(index)->ResetSettings();
	return Py_BuildNone();
}

PyObject* renderTargetSetEffect(PyObject* poSelf, PyObject* poArgs)
{
	BYTE index = 0;
	if (!PyTuple_GetByte(poArgs, 0, &index))
		return Py_BadArgument();

	CRenderTargetManager::Instance().GetRenderTarget(index)->SetEffect();
	return Py_BuildNone();
}

#ifdef ENABLE_SPECULAR_SYSTEM
PyObject* renderTargetUpdateSpecularColor(PyObject* poSelf, PyObject* poArgs)
{
	BYTE index = 0;
	if (!PyTuple_GetByte(poArgs, 0, &index))
		return Py_BadArgument();

	BYTE bType;
	if (!PyTuple_GetByte(poArgs, 1, &bType))
		return Py_BadArgument();

	BYTE r,g,b,a = 0;
	if (!PyTuple_GetByte(poArgs, 2, &r))
		return Py_BadArgument();
	if (!PyTuple_GetByte(poArgs, 3, &g))
		return Py_BadArgument();
	if (!PyTuple_GetByte(poArgs, 4, &b))
		return Py_BadArgument();
	if (!PyTuple_GetByte(poArgs, 5, &a))
		return Py_BadArgument();
		
	CRenderTargetManager::Instance().GetRenderTarget(index)->UpdateSpecularColor(bType, r, g, b, a);
	return Py_BuildNone();
}
#endif

void initRenderTarget() {
	static PyMethodDef s_methods[] =
	{
		{ "SetEffect", renderTargetSetEffect, METH_VARARGS },
		{ "ResetSettings", renderResetSettings, METH_VARARGS },
		{ "SetRenderingPosition", renderSetRenderingPosition, METH_VARARGS },
		{ "SetMove", renderSetMove, METH_VARARGS },
		{ "SetZoom", renderSetZoom, METH_VARARGS },
		{ "SelectModel", renderTargetSelectModel, METH_VARARGS },
		{ "SetVisibility", renderTargetSetVisibility, METH_VARARGS },
		{ "SetBackground", renderTargetSetBackground, METH_VARARGS },
		{ "SetArmor", renderTargetSetArmor, METH_VARARGS },
		{ "SetHair", renderTargetSetHair, METH_VARARGS },
		{ "SetWeapon", renderTargetSetWeapon, METH_VARARGS },
#ifdef ENABLE_ACCE_SYSTEM
		{ "SetSash", renderTargetSetSash, METH_VARARGS },
#endif
#ifdef ENABLE_SHINING_SYSTEM
		{ "SetShining", renderTargetSetShining, METH_VARARGS },
#endif
#ifdef ENABLE_SPECULAR_SYSTEM
		{ "UpdateSpecularColor", renderTargetUpdateSpecularColor, METH_VARARGS },
#endif
		{nullptr, nullptr, 0 },
	};

	PyObject* poModule = Py_InitModule("renderTarget", s_methods);

}