from pwn import *
from Crypto.Util.number import long_to_bytes

context.log_level = 'debug'

p = process(["python3", "chal.py"])
p.recvuntil(b"m = ")
m = int(p.recvline()[:-1].decode())
p.sendlineafter(b"Check flag\n", b"1")
out1 = int(p.recvline()[:-1].decode())
p.sendlineafter(b"Check flag\n", b"1")
out2 = int(p.recvline()[:-1].decode())
p.sendlineafter(b"Check flag\n", b"1")
out3 = int(p.recvline()[:-1].decode())
p.sendlineafter(b"Check flag\n", b"2")
a = (((out3 - out2) % m) * pow(out2 - out1, -1, m)) % m
print(f"out1: {out1}, out2: {out2}, out3: {out3}")
print(f"a: {a}")
p.sendlineafter(b"Whats a?\n", str(a).encode())
c = (out2 - a * out1) % m
p.sendlineafter(b"Whats c?\n", str(c).encode())
p.interactive()