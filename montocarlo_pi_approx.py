import numpy as nump

def np():
    xx = 2*nump.random.rand(2) - 1
    return not (xx[0]**2 + xx[1]**2 > 1)
nInCircle = 0

n = int(input("n = "))

for x in range(n):
    nInCircle += np()

print(4 * nInCircle / n)
