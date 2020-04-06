#!/usr/bin/python3



from jk_flexdata import *
from jk_infodatatree import DictValue



dataTree = FlexObject({
	"host_name": "test"
})



spath, data = FlexDataSelector("|host_name").getOne(dataTree)
print(repr(data))

d = DictValue(data, None, None)
d.dump()







