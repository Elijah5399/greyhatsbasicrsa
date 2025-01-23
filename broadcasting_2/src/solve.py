from Crypto.Util.number import long_to_bytes
from sympy.ntheory.modular import crt
from gmpy2 import iroot

e = 5

f = open('output.txt', 'r')

# Generate the encrypted flag with 5 different RSA key
ciphertexts, moduli = [],[]

for _ in range(e):
    ci, ni = int(f.readline()[:-1]), int(f.readline()[:-1])
    ciphertexts.append(ci)
    moduli.append(ni)

flag_pow_e = crt(moduli, ciphertexts)[0]
flag = int(iroot(flag_pow_e,e)[0])
print(long_to_bytes(flag))