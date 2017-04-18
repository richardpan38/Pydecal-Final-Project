def graph(a,b):
	import scipy as sp
	import numpy as np
	import matplotlib.pyplot as plt

	mass = None
	radius = None
	a = mass
	b = radius
	effect_velocity = [1,velocity]
	#effect_mass = [1,mass]
	effect_radius = [1,radius]

	def new_mass(mass, radius):
		effect_mass = mass * (effect_radius)**3 / radius**3
		return effect_mass

	def new_vel(effect_mass, effect_radius):
		effect_velocity = np.sqrt(sp.G * effect_mass / effect_radius)
		return effect_velocity

	x = effect_radius
	y = effect_velocity

	plt.plot(x,y)
	plt.axis([0, 1000000000, 0, 100000000000])
	plt.show()
