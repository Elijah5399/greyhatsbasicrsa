# import the python pwntools module
from pwn import *

# p = remote("IP / DOMAIN NAME", PORT_NUMBER) # uncomment this line when solving on remote

p = process(["python3", "chall.py"]) # comment this line when solving on remote
# receive the data from the program as bytes
data = p.recvline().split() # split the useful and not useful data 
# print(data)

ax, bx = int(data[1].decode()), int(data[3].decode())
# try to get the flag now! write code below
