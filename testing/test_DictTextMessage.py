#!/usr/bin/python3



import jk_flexdata
import jk_infodatatree







msg = jk_infodatatree.DictTextMessage("abc{{|asd}}def{{name}}ghi", None)

dataTree1 = jk_flexdata.FlexObject({
	"asd": {
		"dt": "int",
		"v": 123,
	},
})
dataTree2 = jk_flexdata.FlexObject({
	"asd": None,
})

result1 = msg.format(dataTree1, {
})

print(repr(result1))
assert result1 == "abc123def???ghi"

result2 = msg.format(dataTree1, {
	"name": jk_infodatatree.DictValue({
		"dt": "str",
		"v": "FOO",
	}, None, None),
})

print(repr(result2))
assert result2 == "abc123defFOOghi"

result3 = msg.format(dataTree2, {
	"name": jk_infodatatree.DictValue({
		"dt": "str",
		"v": "FOO",
	}, None, None),
})

print(repr(result3))
assert result3 == "abc???defFOOghi"






print("Success.")



