import numpy as np
import matplotlib as plt

class punto():
	
	def __init__(self, x0, y0):
		self.x=x0
		self.y=y0
		self.r= (self.x**2.0 + self.y**2.0)**(1.0/2.0)

	
	def move(self, dx, dy):
		self.x= self.x + dx
		self.y= self.y + dy
		
	def pos(self):	
		print self.x, self.y, self.r

puntos=punto(4.0,3.0)
puntos.pos()

# arch= open("caminata.txt", "w")

p1=2*(np.random.rand()-0.5)
p2=2*(np.random.rand()-0.5)

print p1, p2

while (r<10):
	puntos.move(p1,p2)
	print puntos.pos()
	



