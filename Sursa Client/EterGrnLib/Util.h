#pragma once

#include "../UserInterface/Locale_inc.h"
// bool GrannyMeshGetTextureAnimation(granny_mesh* pgrnMesh, float* puVelocity, float* pvVelocity);
// bool GrannyMeshIsTextureAnimation(granny_mesh* pgrnMesh);
bool GrannyMeshIsDeform(granny_mesh* pgrnMesh);

class CGraphicImage;

struct SMaterialData
{
	CGraphicImage * pImage;
	float fSpecularPower;
	BOOL isSpecularEnable;
	BYTE bSphereMapIndex;
#ifdef ENABLE_SPECULAR_SYSTEM
	bool bSpecularColor;
#endif
};

