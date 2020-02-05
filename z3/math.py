from z3 import *
from pwn import *
import sys

ip = "ctf.balqs.nctu.me"
port = 9001
r = remote(ip,port)
context.arch='amd64'

tmp = r.recv()
while 1:
    print(tmp)
    tmp2 = r.recv()
    print(tmp2)
    tmp = str(tmp, encoding="utf-8")
    tmp2 = str(tmp2, encoding="utf-8")
    tmp = tmp.split(' ')
    tmp2 = tmp2.split(' ')

    a1 = tmp[0]
    a2 = tmp[4]
    a3 = tmp[8][:-1]
    a4 = tmp2[0]
    a5 = tmp2[4]
    a6 = tmp2[8][:-1]

    print(a1,a2,a3,a4,a5,a6)
    print(type(a1))
    x = Int('x')
    y = Int('y')
    s = Solver()
    s.add(int(a1)*x+int(a2)*y==int(a3))
    s.add(int(a4)*x+int(a5)*y==int(a6))
    assert s.check() == sat
    xa = s.model()[x]
    ya = s.model()[y]
    r.sendline(str(xa))
    r.recvuntil('= ')
    r.sendline(str(ya))

    tmp = r.recv()
