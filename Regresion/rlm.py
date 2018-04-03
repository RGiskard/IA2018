import numpy as np
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

file='data2.txt'
xdata=np.genfromtxt(file,delimiter=',',usecols=[0,1])
ydata=np.genfromtxt(file,delimiter=',',usecols=[2])
ones=np.ones(len(xdata))
xtemp=xdata

y=(np.array([ydata])).T

alpha = 0.01;
iteraciones = 400;
thetas=np.zeros((3,1))

def normalizardata(x):
	x_norm = x;
	mu = np.zeros((1,x.shape[1]));
	sigma = np.zeros((1,x.shape[1]));
	mu[0,0]=np.sum(x[:,0])/len(x)
	mu[0,1]=np.sum(x[:,1])/len(x)
	sigma=np.std(x, axis=0)
	for i in range (len(x)):
		x_norm[i,:]=np.divide(np.subtract(x[i,:],mu),sigma)
	x=x_norm

def costMulti(x,y,thetas):
	m=len(y)
	j=0;
	j=(np.dot((np.subtract(np.dot(x,thetas),y)).T,np.subtract(np.dot(x,thetas),y)))/(2*m)
	return j

def gradienteDescMulti(x,y,alpha,num_iters):
	m=len(y)
	j_historial= np.zeros((num_iters, 1));
	hipotesis=np.dot(x,thetas)
	j_historial= np.zeros((num_iters, 1));
	global thetas
	for iter in range (num_iters):
		hipotesis=np.dot(x,thetas)
		thetas = np.subtract( thetas,( (alpha/m) * ( ( np.dot( (np.subtract(hipotesis,y)).T , x ) ).T ) ) )
		
	j_historial[iter]=costMulti(x,y,thetas)
	
	
def main():
	
	normalizardata(xtemp)
	x=np.column_stack((ones,xtemp))
	gradienteDescMulti(x,y,alpha,iteraciones)
	
	fig=pyplot.figure()
	
	ax=Axes3D(fig)
	ax.scatter(x[:,1],x[:,2],y)
	
	
	X, Y = np.meshgrid(x[:,1], x[:,2])
	Z=thetas[0]+thetas[1]*X+thetas[2]*Y
	ax = fig.gca(projection='3d')
	surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,linewidth=0, antialiased=False)
	
	pyplot.show()
	
	
	
main()
