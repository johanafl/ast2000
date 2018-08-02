import numpy as np
import matplotlib.pyplot as plt

L_0     = 200                   # [years], distanse to P2 in lightyears
v_0     = 0.99                  # [], initial speed of spaceship
c       = 299792458             # [m/s], speed of light
g       = (-0.1/c)*60**2*24*365 # [1/years], acceleration of spaceship after P2
delta_T = -v_0/g                # [years], time after P2 untill velocity is 0


def x_Y(T_Y):
    return L_0+v_0*T_Y+0.5*g*T_Y**2

def v_T_Y(T_Y):
    return v_0+g*T_Y

def t_y():
    N  = int(1e5)
    tY,ty = np.zeros(2*N),np.zeros(2*N)

    for i in range(N):
        tY[i]   = (L_0*i)/(v_0*N)
        tY[N+i] = L_0/v_0+delta_T*i/N

        ty[i]   = tY[i]*(1-v_0**2)
        ty[N+i] = -x_Y(delta_T*i/N)*np.sqrt(v_T_Y(delta_T*i/N)**2)+tY[N+i]

    return tY,ty

TY,Ty = t_y()

plt.plot(TY,Ty)
plt.title("How time moves on planet P1 seen from the spaceship during the journy")
plt.xlabel("Time on planet P1 (planet frame), [years]")
plt.ylabel("Time on planet P1 (spaceship frame), [years]")
plt.savefig("time")
plt.show()

"""
Terminal>
"""
