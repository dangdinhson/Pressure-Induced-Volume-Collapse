import numpy as np
from scipy.optimize import brentq

NA = 6.02214076e23  # 1/mol

compounds = ["SmS","SmSe","SmTe"]
a0 = {"SmS":5.97, "SmSe":6.22, "SmTe":6.63}          # Angstrom (Jayaraman et al. 1970; Svane et al. 2004)

# --- V0 recomputed from a0 (NaCl structure -> 4 f.u. per conventional cell) ---
V0 = {}
for c in compounds:
    a_cm = a0[c]*1e-8
    V0[c] = NA*a_cm**3/4   # cm^3/mol
    print(c, "V0 (calc) =", round(V0[c],2), "cm3/mol")

# --- experimental bulk moduli, literature-sourced (kbar) ---
# SmS: Benedict & Holzapfel (1993) 42(3),50.3, 47.6(5.0) GPa -> average
B0exp_GPa = {"SmS": np.mean([42,50.3,47.6]), "SmSe": 40.0, "SmTe": 40.0}
B0exp = {c: B0exp_GPa[c]*10 for c in compounds}   # kbar
for c in compounds:
    print(c, "B0(exp) =", round(B0exp[c],1), "kbar")

# --- Anderson-Nafe-type power law refit: B0 = A * V0^-x ---
V = np.array([V0[c] for c in compounds])
B = np.array([B0exp[c] for c in compounds])
lnV = np.log(V); lnB = np.log(B)
# least squares linear fit lnB = lnA - x lnV
Xmat = np.vstack([np.ones_like(lnV), lnV]).T
coef, *_ = np.linalg.lstsq(Xmat, lnB, rcond=None)
lnA, negx = coef
x = -negx
A = np.exp(lnA)
print("\nFit: B0 = A * V0^-x")
print("A =", A, " x =", x)

B0calc = {c: A*V0[c]**(-x) for c in compounds}
for c in compounds:
    print(c, "B0(calc, refit) =", round(B0calc[c],1), "kbar")

# deviations
for c in compounds:
    dB = abs(B0calc[c]-B0exp[c])/B0exp[c]*100
    eB = (B0calc[c]-B0exp[c])/B0exp[c]*100
    kappa = 1/B0calc[c]
    print(c, "delta_B=%.1f%%"%dB, "eps_B=%.1f%%"%eB, "kappa=%.3e kbar^-1"%kappa)
