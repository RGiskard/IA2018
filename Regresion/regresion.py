import numpy as np
import csv

#definimos variables globales
iteraciones = 1500;
alpha = 0.01;
theta=np.matrix(np.random.rand(2)).T
x=[]
y=[]
m=0
#leer de archivo
def csv_reader(file_obj):
    reader = csv.reader(file_obj)
    for row in reader:
    	x.append(float(row[0]))
    	y.append(float(row[1]))
    m=len(reader)	


def cargar(name):
	with open(name) as f_obj:
		csv_reader(f_obj)

def getXY():
	cargar("ex1data1.txt")
	ghost=[]
	for i in range(len(x)):
		ghost.append(1)
	parte=[ghost,x]	
	X=np.matrix(parte)
	X=X.T
	Y=np.matrix(y)
	ghost=[X,Y]
	return ghost
def main():
	print("Hello")
	cargar("ex1data1.txt")
