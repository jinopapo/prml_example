import matplotlib.pyplot as plt
import numpy as np


M = 8
N = 10
tx = np.arange(1, 2, 0.01)
x = np.random.rand(N)+1
ty = np.sin(2*np.pi*tx)
y = np.sin(2*np.pi*x) + np.random.rand(N) - 0.5
t = np.sin(2*np.pi*x)
if M == 0:
  w = np.mean(y)
  w = np.ones(len(tx))*w
else:
  a = np.array([x])
  b = y.T
  for i in range(1,M):
    aa = np.array([x**(i+1)])
    a = np.concatenate((a, aa), axis=0)
  w = np.linalg.solve(a.dot(a.T), a.dot(b))
  print(w)
  dy = np.ones(len(tx))*w[0]
  for i in range(1,M):
    dy += (tx**i)*w[i]
  w = dy
plt.plot(tx, ty, 'r')
plt.plot(x, y, 'o')
plt.plot(tx, w)
plt.show()
