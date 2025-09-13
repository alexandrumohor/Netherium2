#include "stdafx.h"

#include <boost/pool/object_pool.hpp>

#include "affect.h"

boost::object_pool<CAffect> affect_pool;

CAffect* CAffect::Acquire()
{
	return affect_pool.malloc();
}

void CAffect::Release(CAffect* p)
{
	affect_pool.free(p);
}
//martysama0134's 8e0aa8057d3f54320e391131a48866b4
