// vim: ts=8 sw=4
#ifndef __INC_MONEY_LOG
#define __INC_MONEY_LOG

#include <map>

class CMoneyLog : public singleton<CMoneyLog>
{
    public:
	CMoneyLog();
	virtual ~CMoneyLog();

	void Save();
#ifdef ENABLE_REMOVE_LIMIT_GOLD
	void AddLog(BYTE bType, DWORD dwVnum, unsigned long long iGold);
#else
	void AddLog(BYTE bType, DWORD dwVnum, int iGold);
#endif

    private:
	std::map<DWORD, int> m_MoneyLogContainer[MONEY_LOG_TYPE_MAX_NUM];
};

#endif
//martysama0134's 8e0aa8057d3f54320e391131a48866b4
