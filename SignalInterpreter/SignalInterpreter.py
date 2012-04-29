import numpy as np
import scipy as sp
import pylab


dbvls=np.genfromtxt('deforvertical.csv', delimiter=';')

radios=dbvls[0][1:]
theta=[]
data=[]
for row in dbvls:
	theta.append(row[0])
	data.append(row[1:])

lon=len(dbvls)
for i in range(lon):
	theta.append(360-dbvls[lon-1-i][0])
	data.append(dbvls[lon-1-i][1:])
		


theta=np.pi*np.array(theta)/180
R,T=np.meshgrid(radios,theta)



X=R*np.cos(T)
Y=R*np.sin(T)

print data

pylab.contourf(X,Y,data)
pylab.show()
