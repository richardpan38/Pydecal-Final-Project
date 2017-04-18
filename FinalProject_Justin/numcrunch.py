import numpy as np
import scipy.constants as sp
def solver(rshift,vertext, avg_wl, delt_wl):
    vel = None
    radi = None
    mass = None
    Dm = 1130.2
    Da = (Dm/(1+rshift))
    Da = Da * (3.0*10**(22))
    print('Angular distance diameter = ', Da, ' meters.')
    vertext = (vertext * 0.1185 * np.pi) / (3600 * 180)
    print('Converted vertical extent = ', vertext, ' radians.')
    radi = (Da * vertext) / 2
    print('Galactic radius = ', radi, ' meters.')
    vel = (delt_wl * sp.speed_of_light) / (avg_wl * 2)
    print('Galactic rotation speed = ', vel, ' meters per second.')
    mass = (radi * (vel**2)) / sp.G
    print('Galactic mass = ', mass, ' kilograms.')

solver(1,1,1,1)


