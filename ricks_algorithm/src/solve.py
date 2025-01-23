from pwn import *
from Crypto.Util.number import *
from sympy import gcd


# context.log_level = 'debug'

e = 0x557
p = process(["python3","chall.py"])
# p = remote("43.217.80.203", 33862)

p.sendlineafter(b"Enter option: ", b"1")
p.sendlineafter(b"encrypt: ", long_to_bytes(69))
p.recvuntil(b"message: ")
c1 = int(p.recvline()[:-1].decode())
d1 = c1 - pow(69, e)
p.sendlineafter(b"Enter option: ", b"1")
p.sendlineafter(b"encrypt: ", long_to_bytes(1337))
p.recvuntil(b"message: ")
c2 = int(p.recvline()[:-1].decode())
d2 = c2 - pow(1337,e)
n = int(gcd(d1, d2))
p.sendlineafter(b"Enter option: ", b"3")
p.recvuntil(b"Encrypted flag: ")
ct = int(p.recvline()[:-1].decode())
fake = pow(ct, -1, n)
p.sendlineafter(b"Enter option: ", b"2")
p.sendlineafter(b"decrypt: ", str(fake).encode())
p.recvuntil(b"message: ")
pt_inv = int(p.recvline()[:-1].decode())
m = pow(pt_inv, -1, n)
print(long_to_bytes(m))