import numpy as np

x =[1, -3, 4] 
y =[-4, 1, 2] 
p= np.subtract(x,y)
q=np.linalg.norm(p)

print(q)
