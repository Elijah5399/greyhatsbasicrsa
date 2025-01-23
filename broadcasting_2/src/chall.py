from Crypto.Util.number import getPrime
from Crypto.Util.number import bytes_to_long
from math import gcd 

e = 5
flag = "grey{m0M_Tod4y_1_le4rNt_CRT}"

flag = bytes_to_long(flag.encode())
output_file = open('output.txt', 'w')

# Generate the encrypted flag with 5 different RSA key
for _ in range(e):
    while True:
        p = getPrime(512)
        q = getPrime(512)
        n_i = p * q 
        phi = (p - 1) * (q - 1)

        if gcd(phi, e) == 1: 
            break 

    c_i = pow(flag, e, n_i)

    output_file.write(f'{str(c_i)}\n')
    output_file.write(f'{str(n_i)}\n')