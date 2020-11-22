import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

### from https://realpython.com/linear-regression-in-python/ ###

x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1,1))
y = np.array([5,20,14,32,22,38])
  

print(x)
print(y)

model = LinearRegression()
model.fit(x,y)

r_sq = model.score(x,y)
print('Coefficient of determination: ', r_sq)
print('Intercept:', model.intercept_)
print('Slope: ', model.coef_)


plt.plot(x,y,'gs')
plt.show()