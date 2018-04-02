import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
file='data1.txt'
xdata=np.genfromtxt(file,delimiter=',',usecols=[0])
ydata=np.genfromtxt(file,delimiter=',',usecols=[1])
ones=np.ones(len(xdata))
x=np.column_stack((ones,xdata))
y=(np.array([ydata])).T
#print(x)
#print(y)
thetas=np.zeros((2,1))
#print(thetas)
iteraciones=1500;
alpha=0.01;

fig, ax = plt.subplots()
fig.set_tight_layout(True)


#funcionCosto=(np.dot((np.subtract(np.dot(x,thetas),y)).T,np.subtract(np.dot(x,thetas),y)))/(2*m)
def cost(x,y,thetas):
	m=len(y)
	j=0;
	j=(np.dot((np.subtract(np.dot(x,thetas),y)).T,np.subtract(np.dot(x,thetas),y)))/(2*m)
	return j
def gradienteDesc(x,y,thetas,alpha,num_iters):
	m=len(y)
	x0=(np.array([x[:,0]])).T
	x1=(np.array([x[:,1]])).T
	j_historial= np.zeros((num_iters, 1));
	for iter in range (num_iters):
		hipotesis=np.dot(x,thetas)
		temp1=thetas[0] - (alpha/m)* np.sum (np.subtract(hipotesis,y)*x0)
		temp2=thetas[1] - (alpha/m)* np.sum (np.subtract(hipotesis,y)*x1)
		thetas[0]=temp1
		thetas[1]=temp2
		j_historial[iter]=cost(x,y,thetas)
		plt.ion()
		points,= plt.plot(xdata,ydata,"ro")
		line, = plt.plot(xdata, np.dot(x,thetas), 'r-')
		line.set_antialiased(False) # turn off antialising
		plt.draw()
		plt.pause(0.00001)
		plt.clf()
	return thetas
		
def main():
	#print(cost(x,y,thetas))
	gradienteDesc(x,y,thetas,alpha,iteraciones)
	"""plt.ion()
	points,= plt.plot(xdata,ydata,"ro")
	line, = plt.plot(xdata, np.dot(x,thetas), 'r-')
	line.set_antialiased(False) # turn off antialising
	plt.draw()
	plt.pause(10000)"""
	
main()

