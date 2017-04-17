import numpy as np
rshift = None
avg_wl = None
delt_wl = None
vertext = None
vel = None
radi = None
mass = None

def get_angdist(rshift):
    Dm = 1130.2
    Da = (Dm/(1+rshift))
    Da = Da * (3.0*10**(22))
    print('Angular distance diameter = ', Da, ' meters.')

def conv_vertext(vertext):
    vertext = (vertext * 0.1185 * np.pi) / (3600 * 180)
    print('Converted vertical extent = ', vertext, ' radians.')

def get_radi(Da,vertext):
    radi = (Da * vertext) / 2
    print('Galactic radius = ', radi, ' meters.')

def get_vel(delt_wl,avg_wl):
    vel = (delt_wl * np.c) / (avg_wl * 2)
    print('Galactic rotation speed = ', vel, ' meters per second.')

def get_mass(radi,vel):
    mass = (radi * (vel**2)) / np.G
    print('Galactic mass = ', mass, ' kilograms.')
