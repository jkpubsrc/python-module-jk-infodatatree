#!/usr/bin/python3




from jk_infodatatree import DictValue




v_int_A = DictValue(123, None, None)
v_int_B = DictValue(234, None, None)



assert v_int_A.test_lt(v_int_B)
assert v_int_B.test_gt(v_int_A)
assert v_int_B.test_ne(v_int_A)

assert v_int_A.test_le(v_int_A)
assert v_int_A.test_ge(v_int_A)
assert v_int_A.test_eq(v_int_A)
assert v_int_B.test_le(v_int_B)
assert v_int_B.test_ge(v_int_B)
assert v_int_B.test_eq(v_int_B)

assert not v_int_A.test_isEmpty()
assert not v_int_B.test_isEmpty()





v_int_K = DictValue([], None, None)
v_int_L = DictValue([ "a" ], None, None)
v_int_M = DictValue([ "a", "b" ], None, None)
v_int_N = DictValue([ "a", "b" ], None, None)

assert v_int_K.test_isEmpty()
assert not v_int_L.test_isEmpty()
assert not v_int_M.test_isEmpty()

assert not v_int_L.test_lt(v_int_M)
assert not v_int_L.test_gt(v_int_M)

assert not v_int_L.test_eq(v_int_M)
assert v_int_L.test_ne(v_int_M)
assert v_int_M.test_eq(v_int_N)
assert not v_int_M.test_ne(v_int_N)






print("Success.")


