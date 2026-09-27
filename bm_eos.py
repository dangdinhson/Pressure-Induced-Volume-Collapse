import numpy as np
from scipy.optimize import brentq
import json

B0 = {"SmS":449.3, "SmSe":425.3, "SmTe":390.5}   # kbar, refit values
Bp = 4.0   # standard default Birch-Murnaghan pressure derivative (literature convention)

def P_of_x(x, B0, Bp):
    # x = V/V0
    return 1.5*B0*(x**(-7/3)-x**(-5/3))*(1+0.75*(Bp-4)*(x**(-2/3)-1))

def x_of_P(P, B0, Bp):
    f = lambda x: P_of_x(x,B0,Bp)-P
    return brentq(f, 0.5, 1.0, xtol=1e-8)

curves = {}
Pmax = {"SmS":10, "SmSe":100, "SmTe":90}
for c in B0:
    Ps = np.linspace(0, Pmax[c], 60)
    xs = [1.0]+[x_of_P(p,B0[c],Bp) for p in Ps[1:]]
    curves[c] = {"P":Ps.tolist(), "VV0":xs}

json.dump(curves, open("bm_curves.json","w"))
for c in B0:
    print(c, "V/V0 at 10,30,60 kbar:")
    for p in [5,10,30,60]:
        if p<=Pmax[c]:
            print(" P=",p,"->", round(x_of_P(p,B0[c],Bp),4))
