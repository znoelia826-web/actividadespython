import numpy as np 
#import pandas as pd 
#import numpy

a=np.array([1,2,3])

print(type(a))
print(a.shape)

print(a[2])

a[0]=100
a[1]+=1000
a[2]-=1000

print(a)

b=np.array([[1,2,3],[1,2,3]])
print(type(b))
print(b.shape)
print(b)
print(b[1,1])

b[1,2]+=100
print(b)


a=np.zeros((4,5))
print(a)
print(a.shape)

b=np.ones((3,4))
print(b)


c=np.eye(4)
print(c)


d=np.full((5,5),8)
print(d)


e=np.random.random([3,3])
print(e)

f=np.random.choice([1,10],size=(3,4))
print(f)

print('****************++++++++++++++++++++')

g=np.random.randint(1,100,(3,4))
print(g)

print('****************++++++++++++++++++++')

submatrixg=g[0:2,1:3]
print(submatrixg)

print('****************++++++++++++++++++++')
g=np.random.randint(11,20,(5,4))
print(g)

a=np.array([[1,2],[3,4],[5,6]])
print(a)
print(a.shape)

mask=(a>2)

print(mask)
print(a[mask])

g = np.arange(101)

# Reshape a matriz 7x7 (tomamos solo los primeros 49 elementos)
matriz = g[:49].reshape(7, 7)
print("Matriz 7x7:")
print(matriz)

# Filtro de valores entre 40 y 60
filtro = matriz[(matriz >= 40) & (matriz <= 60)]
print("\nValores entre 40 y 60:")
print(filtro)
