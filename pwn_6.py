from pwn import *

r = remote('140.110.112.192','2116')

r.recvuntil(':)')
r.recvuntil('\n')
magic = 0x79487ff

r.sendline(p32(magic))

r.recvuntil('\n')
for i in range(1000):
    s = r.recvuntil('?').split(' ')
    print(s)

    n1 = int(s[0])
    n2 = int(s[2])
    
    if s[1] == '+':
        r.sendline(str(n1+n2))
    elif s[1] == '-':
        r.sendline(str(n1-n2))
    else :
        r.sendline(str(n1*n2))

r.interactive()
