# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 09:18:32 2022

@author: Stefan
"""

import numpy as np

a = np.array([1, 2, 3])
c = np.zeros_like(a, dtype=bool)

print("a=", a)
print("c=", c)

print("a[c]=", a[c])
print("~c=", ~c)
print("a[~c]=", a[~c])

c = a > 1
print("a > 1:", c)
print("a[a > 1]:", a[c])

a2 = 2 * a[c]
print("2 * a[c]=", a2)

x = np.linspace(0, 2, 3)
y = np.linspace(0, -2, 3)

X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

print("Z=", Z)
c = abs(Z) > 1
print("abs(Z) > 1=", c)
