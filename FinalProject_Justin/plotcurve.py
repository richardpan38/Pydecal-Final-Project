import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

effect_mass = 0
vel = 0
effect_velocity = [1,vel]
radi = 0
effect_radius = [1,radi]

def new_mass(mass, radi):
    effect_mass = mass * (effect_radius)**3 / radi**3
    return effect_mass

def new_vel(effect_mass, effect_radius):
    effect_velocity = np.sqrt(sp.G * effect_mass / effect_radius)
    return effect_velocity



x = effect_radius
y = effect_velocity

plt.plot(x,y)
plt.axis([0, 1000000000, 0, 100000000000])
plt.show()
