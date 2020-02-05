from z3 import *


#flag = input('Please give me the flag: ')
key = [21, 23, 9, 22, 3, 16, 17, 7, 8, 10, 11, 4, 0, 2, 13, 6, 1, 14, 18, 19, 5, 20, 12, 15]
check_values = [247, 220, 217, 225, 154, 146, 217, 173, 173, 244, 245, 225, 199, 148, 106, 163, 159, 106, 106, 173, 244, 244, 173]

#assert len(flag) == 24
#assert flag[:4] == 'flag'

s = Solver()
for i in range(0,23):
    x = Int('x' + str(key[i]))
    y = Int('x' + str(key[i+1]))
    s.add(x+y == check_values[i])
    s.add(x < 127)

x = Int('x0')
s.add(x == ord('f'))
x = Int('x1')
s.add(x == ord('l'))
x = Int('x2')
s.add(x == ord('a'))
x = Int('x3')
s.add(x == ord('g'))

assert s.check() == sat
m = s.model()

for val in m.decls():
    print(val,chr(m[val].as_long()))
'''
for k1, k2 in zip(key[:-1], key[1:]):
    assert ord(flag[k1]) + ord(flag[k2]) == check_values[0], 'invalid flag'
    check_values = check_values[1:]
'''
#print('YOU GOT IT! ｡:.ﾟヽ(*´∀`)ﾉﾟ.:｡')
