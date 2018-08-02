import numpy as np
import matplotlib.pyplot as plt
from numba import jit

c=3*10**8
year=60*60*24*365

@jit(nopython=True)
def time_d(L0,a,v0,dt=10**(-5),v_end=0):
    N1=int(L0/dt)
    ty=[]
    ty_mark=[]
    TY=0
    for i in range(N1+1):
        L=(L0/float(N1)*i)
        xy=L+v0*TY+0.5*a*TY**2
        gamma=(1-v0**2)
        ty.append(L/v0)
        ty_mark.append((-xy*(1-gamma)**(0.5))+ty[i])

    N=int((v0-v_end)*c/(a*year)/dt)
    TY_end=(v0-v_end)*c/(a*year)
    for k in range(1,N+1):
        TY=TY_end*k/float(N)
        xy=L0+(v0*c*TY+0.5*a*c/year*TY**2)/c
        ty.append(L0/v0+TY)

        gamma=(1-((v0*c-a*TY*year)/c)**2)
        ty_mark.append(ty[i+k-1]-xy*(1-gamma)**0.5)

    return ty_mark,ty

ty_mark,ty=time_d(200,0.1,0.99)
plt.plot(ty,ty_mark)
plt.xlabel("Planet frame time [Year]")
plt.ylabel("Rocket time [Year]")
plt.title("Time in rocket frame vs time in planet frame")
plt.savefig("time.png")
plt.show()
