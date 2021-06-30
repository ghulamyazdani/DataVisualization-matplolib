import sklearn
import matplotlib.pyplot as plt
import numpy as np
import random


x = list(range(0,50))
y=[1.8*F+32+random.randint(-3,3) for F in x]
print(f'X: {x}')
print(f'Y: {y}')

plt.plot(x,y,'-*r')
plt.show()