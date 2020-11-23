import matplotlib.pyplot as plt
import math
import numpy as np
t = np.arange(0,2.5,0.1)
y1 = np.sin(math.pi*t)
y2 = np.sin(math.pi*t+math.pi/2)
plt.plot(t,y1,'b*',t,y2,'gs')
#plt.plot(y1,t,'g')
plt.legend(['pi * t','pi/2'])
plt.show()
