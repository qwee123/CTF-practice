from z3 import *
x = Int('x')
y = Int('y')
s = Solver()
s.add(x + y == 10)
s.add(6*x+y==20)
print(s.check())
print(s.model())
