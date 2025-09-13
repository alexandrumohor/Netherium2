#pragma once

#include <memory>
#include "GrpRenderTargetTexture.h"
#include "../UserInterface/Locale_inc.h"

class CInstanceBase;
class CGraphicImageInstance;

class CRenderTarget
{
	using TCharacterInstanceMap = std::map<DWORD, CInstanceBase*>;
	
	public:
		CRenderTarget(DWORD width, DWORD height);
		~CRenderTarget();


		void SetVisibility(bool isShow);
		void RenderTexture() const;
		void SetRenderingRect(RECT* rect) const;

		void SelectModel(DWORD index);
		bool CreateBackground(const char* imgPath, DWORD width, DWORD height);
		void RenderBackground() const;
		void UpdateModel();
		void DeformModel() const;
		void RenderModel() const;
#ifdef ENABLE_SPECULAR_SYSTEM
		void UpdateSpecularColor(BYTE bType, BYTE r = 0, BYTE g = 0, BYTE b = 0, BYTE a = 0);
		void SetArmor(DWORD vnum, bool bIsColor = false);
		void ChangeHair(DWORD vnum, bool bIsColor = false);
		void SetWeapon(DWORD vnum, bool bIsColor = false);
		void SetCrown(DWORD vnum, bool bIsColor = false);
#else
		void SetArmor(DWORD vnum);
		void ChangeHair(DWORD vnum);
		void SetWeapon(DWORD vnum);
		void SetCrown(DWORD vnum);
#endif
#ifdef ENABLE_ACCE_SYSTEM
#ifdef ENABLE_SPECULAR_SYSTEM
		void SetSash(DWORD vnum, bool bIsColor = false);
#else
		void SetSash(DWORD vnum);
#endif
#endif
#ifdef ENABLE_SHINING_SYSTEM
		void SetShining(DWORD dwShining);
#endif
		
		void CreateTextures() const;
		void ReleaseTextures() const;
		
		void SetRenderingPosition(bool bRender);
		void SetMove(bool bMove);
		void SetZoom(bool bZoom);
		void ResetSettings();
		void SetAll();
		void SetEffect();
	
	private:
		std::unique_ptr<CInstanceBase> m_pModel; 
		std::unique_ptr<CGraphicImageInstance> m_background;
		std::unique_ptr<CGraphicRenderTargetTexture> m_renderTargetTexture;
		float m_modelRotation;
		bool m_visible;
		float f_zoom;
		float f_target_z;
};
