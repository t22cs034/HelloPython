'''
Created on 2024/10/11
@author:Tokuho

'''

import math
from fibonacci import fibo

print("Hello, Python world!")

a = 10
b = 0.000001
c = "string"
d = 10; e = 0.000001; f = "string"

# This is comment

print(a, b, c)
print(d, e, f)

for x in {1, 2, 3}:
    print(x)
    
if 0 < x < 10:
    print('0<x<10')
else:
    print('x<=0, x>=0')
    
p = 0

while p<10:
    print('p=', p)
    p += 1
    
n = 10

for i in range(n):
    print("Hello, Python world!")
    
print(type(math))
print(math)
print(math.pi)

print(fibo(20))