#ftcs

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

xmax = 100  # Length in x direction
v = 1  # Velocity
tmax = 30  # How many seconds
dx = 0.1  # Spatial step size
dt = 0.1  # Time step size
xi = np.arange(0,xmax,dx) # Spatial grid
ti = np.arange(0,tmax,dt)  # Time grid
nx = len(xi)  # Number of spatial steps
nt = len(ti)  # Number of time steps
r = v * dt / (2*(dx)) # CFL condition parameter

u = np.zeros((nt, nx))  # Initialize the solution array

# Initial Condition

def gaussian(x, mu, sig):
    return (1.0/ (np.sqrt(2.0 * np.pi) * sig)) * np.exp(- np.power((x-mu) / sig, 2.0) / 2)

for x in range(nx):
    mu = 500
    u[0, x] = gaussian(x, mu, 15)

# Boundary Conditions
for t in range(nt):
    u[t, 0] = 0
    u[t, nx-1] = 0

# FTCS Algorithm
for t in range(nt-1):  # Time step loop
    for x in range(1, nx-1):  # Spatial loop
        u[t+1, x] = u[t, x] - r * (u[t, x+1] -  u[t, x-1])


fig, ax = plt.subplots()
line, = ax.plot(xi, u[0])

def update(frame):
    line.set_ydata(u[frame])  # Update y-data of the line plot
    ax.set_title(f'Time Evolution of u at t={frame * dt} seconds')
    return line,

ani = FuncAnimation(fig, update, frames=nt, interval=25, blit=True)
plt.xlabel('Position (x)')
plt.ylabel('u')
plt.grid(True)
plt.show()


time_slice_index = 50  # Adjust this index to plot at different time slices
plt.plot(xi, u[time_slice_index])
plt.xlabel('Position (x)')
plt.ylabel('Function u')
plt.title(f'u at Time t={ti[time_slice_index]}')
plt.grid(True)
plt.show()
