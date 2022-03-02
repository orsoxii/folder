import os
import random

a = 1
f=open("file2","w+")
f.write(str(a))
while a < random.randint(-10240, 410240):
    a = a + random.randint(-8, 8)
    f.write(str(a))
os.system("mv file2 results/a")