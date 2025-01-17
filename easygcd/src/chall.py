from Crypto.Util.number import *

flag = open("./flag.txt","rb").read()
flag_long = bytes_to_long(flag) # this converts the flag from bytes to a number
a, b = getPrime(1024), getPrime(1024) # this generates 2 prime numbers named a and b
ax, bx = a * flag_long, b * flag_long 
print(f"ax: {ax} bx: {bx}")