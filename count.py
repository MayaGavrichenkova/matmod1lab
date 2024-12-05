import matplotlib.pyplot as plt
import numpy as np

fig,ax=plt.subplots()
plt.xlabel("t,c")
plt.ylabel("H,кг*м2/с2")
v=0.003
h_max=0.054
x=np.linspace(0,2500,10000000)
y=(np.exp(-1*v*x))*h_max
plt.plot(x,y)
plt.show()


