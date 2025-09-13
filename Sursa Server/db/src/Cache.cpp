#include "stdafx.h"
#include "Cache.h"

#include "QID.h"
#include "ClientManager.h"
#include "Main.h"
#include <fmt/fmt.h>

extern CPacketInfo g_item_info;
extern int g_iPlayerCacheFlushSeconds;
extern int g_iItemCacheFlushSeconds;
extern int g_test_server;
// MYSHOP_PRICE_LIST
extern int g_iItemPriceListTableCacheFlushSeconds;
// END_OF_MYSHOP_PRICE_LIST
//
extern int g_item_count;

#ifdef __SKILL_COLOR_SYSTEM__
extern int g_iSkillColorCacheFlushSeconds;

CSKillColorCache::CSKillColorCache()
{
	m_expireTime = MIN(1800, g_iSkillColorCacheFlushSeconds);
}

CSKillColorCache::~CSKillColorCache()
{
}

void CSKillColorCache::OnFlush()
{
	char query[QUERY_MAX_LEN];
	snprintf(query, sizeof(query),
		"REPLACE INTO skill_color%s (`player_id`, "
		"`s1_col1`, `s1_col2`, `s1_col3`, `s1_col4`, `s1_col5`, "
		"`s2_col1`, `s2_col2`, `s2_col3`, `s2_col4`, `s2_col5`, "
		"`s3_col1`, `s3_col2`, `s3_col3`, `s3_col4`, `s3_col5`, "
		"`s4_col1`, `s4_col2`, `s4_col3`, `s4_col4`, `s4_col5`, "
		"`s5_col1`, `s5_col2`, `s5_col3`, `s5_col4`, `s5_col5`, "
		"`s6_col1`, `s6_col2`, `s6_col3`, `s6_col4`, `s6_col5`, " // end of skills
		"`s7_col1`, `s7_col2`, `s7_col3`, `s7_col4`, `s7_col5`, " // begin buffs
		"`s8_col1`, `s8_col2`, `s8_col3`, `s8_col4`, `s8_col5`, "
		"`s9_col1`, `s9_col2`, `s9_col3`, `s9_col4`, `s9_col5`, "
		"`s10_col1`, `s10_col2`, `s10_col3`, `s10_col4`, `s10_col5`, "
		"`s11_col1`, `s11_col2`, `s11_col3`, `s11_col4`, `s11_col5`) "
		"VALUES (%d, "
		"%d, %d, %d, %d, %d, "
		"%d, %d, %d, %d, %d, "
		"%d, %d, %d, %d, %d, "
		"%d, %d, %d, %d, %d, "
		"%d, %d, %d, %d, %d, "
		"%d, %d, %d, %d, %d, " // end of skills
		"%d, %d, %d, %d, %d, " // begin buffs
		"%d, %d, %d, %d, %d, "
		"%d, %d, %d, %d, %d, "
		"%d, %d, %d, %d, %d, "
		"%d, %d, %d, %d, %d)", GetTablePostfix(), m_data.player_id,
		m_data.dwSkillColor[0][0], m_data.dwSkillColor[0][1], m_data.dwSkillColor[0][2], m_data.dwSkillColor[0][3], m_data.dwSkillColor[0][4],
		m_data.dwSkillColor[1][0], m_data.dwSkillColor[1][1], m_data.dwSkillColor[1][2], m_data.dwSkillColor[1][3], m_data.dwSkillColor[1][4],
		m_data.dwSkillColor[2][0], m_data.dwSkillColor[2][1], m_data.dwSkillColor[2][2], m_data.dwSkillColor[2][3], m_data.dwSkillColor[2][4],
		m_data.dwSkillColor[3][0], m_data.dwSkillColor[3][1], m_data.dwSkillColor[3][2], m_data.dwSkillColor[3][3], m_data.dwSkillColor[3][4],
		m_data.dwSkillColor[4][0], m_data.dwSkillColor[4][1], m_data.dwSkillColor[4][2], m_data.dwSkillColor[4][3], m_data.dwSkillColor[4][4],
		m_data.dwSkillColor[5][0], m_data.dwSkillColor[5][1], m_data.dwSkillColor[5][2], m_data.dwSkillColor[5][3], m_data.dwSkillColor[5][4], // end of skills
		m_data.dwSkillColor[6][0], m_data.dwSkillColor[6][1], m_data.dwSkillColor[6][2], m_data.dwSkillColor[6][3], m_data.dwSkillColor[6][4], // begin buffs
		m_data.dwSkillColor[7][0], m_data.dwSkillColor[7][1], m_data.dwSkillColor[7][2], m_data.dwSkillColor[7][3], m_data.dwSkillColor[7][4],
		m_data.dwSkillColor[8][0], m_data.dwSkillColor[8][1], m_data.dwSkillColor[8][2], m_data.dwSkillColor[8][3], m_data.dwSkillColor[8][4],
		m_data.dwSkillColor[9][0], m_data.dwSkillColor[9][1], m_data.dwSkillColor[9][2], m_data.dwSkillColor[9][3], m_data.dwSkillColor[9][4],
		m_data.dwSkillColor[10][0], m_data.dwSkillColor[10][1], m_data.dwSkillColor[10][2], m_data.dwSkillColor[10][3], m_data.dwSkillColor[10][4]);

	CDBManager::instance().ReturnQuery(query, QID_SKILL_COLOR_SAVE, 0, NULL);

	if (g_test_server)
		sys_log(0, "SkillColorCache::Flush :REPLACE %u (%s)", m_data.player_id, query);

	m_bNeedQuery = false;
}
#endif

CItemCache::CItemCache()
{
	m_expireTime = MIN(1800, g_iItemCacheFlushSeconds);
}

CItemCache::~CItemCache()
{
}

void CItemCache::Delete()
{
	if (m_data.vnum == 0)
		return;

	if (g_test_server)
		sys_log(0, "ItemCache::Delete : DELETE %u", m_data.id);

	m_data.vnum = 0;
	m_bNeedQuery = true;
	m_lastUpdateTime = time(0);
	OnFlush();
}

void CItemCache::OnFlush()
{
	if (m_data.vnum == 0)
	{
		char szQuery[QUERY_MAX_LEN];
		snprintf(szQuery, sizeof(szQuery), "DELETE FROM item%s WHERE id=%u", GetTablePostfix(), m_data.id);
		CDBManager::instance().ReturnQuery(szQuery, QID_ITEM_DESTROY, 0, NULL);

		if (g_test_server)
			sys_log(0, "ItemCache::Flush : DELETE %u %s", m_data.id, szQuery);
	}
	else
	{
		TPlayerItem *p = &m_data;
		const auto setQuery = fmt::format(FMT_COMPILE("id={}, owner_id={}, `window`={}, pos={}, count={}, vnum={},"
														" socket0={}, socket1={}, socket2={}, "
														"attrtype0={}, attrvalue0={}, "
														"attrtype1={}, attrvalue1={}, "
														"attrtype2={}, attrvalue2={}, "
														"attrtype3={}, attrvalue3={}, "
														"attrtype4={}, attrvalue4={}, "
														"attrtype5={}, attrvalue5={}, "
														"attrtype6={}, attrvalue6={}, "
#ifdef ENABLE_SPECULAR_SYSTEM
														"specular_color0={}, specular_color1={}, specular_color2={}, specular_color3={}")
#endif
														, p->id,
														p->owner,
														p->window,
														p->pos,
														p->count,
														p->vnum,
														p->alSockets[0],
														p->alSockets[1],
														p->alSockets[2],
														p->aAttr[0].bType, p->aAttr[0].sValue,
														p->aAttr[1].bType, p->aAttr[1].sValue,
														p->aAttr[2].bType, p->aAttr[2].sValue,
														p->aAttr[3].bType, p->aAttr[3].sValue,
														p->aAttr[4].bType, p->aAttr[4].sValue,
														p->aAttr[5].bType, p->aAttr[5].sValue,
														p->aAttr[6].bType, p->aAttr[6].sValue,
#ifdef ENABLE_SPECULAR_SYSTEM
														p->bSpecularColor[0],
														p->bSpecularColor[1],
														p->bSpecularColor[2],
														p->bSpecularColor[3]
#endif
		); // @fixme205

		const auto itemQuery = fmt::format(FMT_COMPILE("INSERT INTO item{} SET {} ON DUPLICATE KEY UPDATE {}"),
														GetTablePostfix(), setQuery, setQuery);

		if (g_test_server)
			sys_log(0, "ItemCache::Flush :REPLACE  (%s)", itemQuery.c_str());

		CDBManager::instance().ReturnQuery(itemQuery.c_str(), QID_ITEM_SAVE, 0, NULL);

		++g_item_count;
	}

	m_bNeedQuery = false;
}

//
// CPlayerTableCache
//
CPlayerTableCache::CPlayerTableCache()
{
	m_expireTime = MIN(1800, g_iPlayerCacheFlushSeconds);
}

CPlayerTableCache::~CPlayerTableCache()
{
}

void CPlayerTableCache::OnFlush()
{
	if (g_test_server)
		sys_log(0, "PlayerTableCache::Flush : %s", m_data.name);

	char szQuery[QUERY_MAX_LEN];
	CreatePlayerSaveQuery(szQuery, sizeof(szQuery), &m_data);
	CDBManager::instance().ReturnQuery(szQuery, QID_PLAYER_SAVE, 0, NULL);
}

// MYSHOP_PRICE_LIST
//
// CItemPriceListTableCache class implementation
//

const int CItemPriceListTableCache::s_nMinFlushSec = 1800;

CItemPriceListTableCache::CItemPriceListTableCache()
{
	m_expireTime = MIN(s_nMinFlushSec, g_iItemPriceListTableCacheFlushSeconds);
}

void CItemPriceListTableCache::UpdateList(const TItemPriceListTable* pUpdateList)
{
	std::vector<TItemPriceInfo> tmpvec;

	for (uint idx = 0; idx < m_data.byCount; ++idx)
	{
		const TItemPriceInfo* pos = pUpdateList->aPriceInfo;
		for (; pos != pUpdateList->aPriceInfo + pUpdateList->byCount && m_data.aPriceInfo[idx].dwVnum != pos->dwVnum; ++pos)
			;

		if (pos == pUpdateList->aPriceInfo + pUpdateList->byCount)
			tmpvec.emplace_back(m_data.aPriceInfo[idx]);
	}

	if (pUpdateList->byCount > SHOP_PRICELIST_MAX_NUM)
	{
		sys_err("Count overflow!");
		return;
	}

	m_data.byCount = pUpdateList->byCount;

	thecore_memcpy(m_data.aPriceInfo, pUpdateList->aPriceInfo, sizeof(TItemPriceInfo) * pUpdateList->byCount);

	int nDeletedNum;

	if (pUpdateList->byCount < SHOP_PRICELIST_MAX_NUM)
	{
		size_t sizeAddOldDataSize = SHOP_PRICELIST_MAX_NUM - pUpdateList->byCount;

		if (tmpvec.size() < sizeAddOldDataSize)
			sizeAddOldDataSize = tmpvec.size();
		if (tmpvec.size() != 0)
		{
			thecore_memcpy(m_data.aPriceInfo + pUpdateList->byCount, &tmpvec[0], sizeof(TItemPriceInfo) * sizeAddOldDataSize);
			m_data.byCount += sizeAddOldDataSize;
		}
		nDeletedNum = tmpvec.size() - sizeAddOldDataSize;
	}
	else
		nDeletedNum = tmpvec.size();

	m_bNeedQuery = true;

	sys_log(0,
			"ItemPriceListTableCache::UpdateList : OwnerID[%u] Update [%u] Items, Delete [%u] Items, Total [%u] Items",
			m_data.dwOwnerID, pUpdateList->byCount, nDeletedNum, m_data.byCount);
}

void CItemPriceListTableCache::OnFlush()
{
	char szQuery[QUERY_MAX_LEN];

	snprintf(szQuery, sizeof(szQuery), "DELETE FROM myshop_pricelist%s WHERE owner_id = %u", GetTablePostfix(), m_data.dwOwnerID);
	CDBManager::instance().ReturnQuery(szQuery, QID_ITEMPRICE_DESTROY, 0, NULL);

	for (int idx = 0; idx < m_data.byCount; ++idx)
	{
		snprintf(szQuery, sizeof(szQuery),
				"REPLACE myshop_pricelist%s(owner_id, item_vnum, price) VALUES(%u, %u, %u)", // @fixme204 (INSERT INTO -> REPLACE)
				GetTablePostfix(), m_data.dwOwnerID, m_data.aPriceInfo[idx].dwVnum, m_data.aPriceInfo[idx].dwPrice);
		CDBManager::instance().ReturnQuery(szQuery, QID_ITEMPRICE_SAVE, 0, NULL);
	}

	sys_log(0, "ItemPriceListTableCache::Flush : OwnerID[%u] Update [%u]Items", m_data.dwOwnerID, m_data.byCount);

	m_bNeedQuery = false;
}

CItemPriceListTableCache::~CItemPriceListTableCache()
{
}

// END_OF_MYSHOP_PRICE_LIST
//martysama0134's 8e0aa8057d3f54320e391131a48866b4
