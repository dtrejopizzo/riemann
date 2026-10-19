# [amended per R155_002, MINOR-7] the archived file is tk_ceiling.py, and the path
# is now resolved relative to this script so the sweep runs as archived.
import os
_d = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(_d, 'tk_ceiling.py')).read().split('print("S(0)")')[0].split('from scipy.integrate')[0])
from scipy.integrate import simpson
from scipy.linalg import toeplitz
def bnd(Mloc,tau0):
    dl=2*T/Mloc; Pl=2*np.pi/dl; n=1<<18
    x=np.linspace(tau0,tau0+Pl,n+1); Sv=S(x)
    cs=np.array([simpson(Sv*np.exp(1j*l*dl*x),x=x)/Pl for l in range(Mloc)])
    return np.linalg.eigvalsh(toeplitz(np.conj(cs),cs))[0]
for Ml in [4,8,12,16,19,24,32,48,64]:
    Pl=2*np.pi/(2*T/Ml)
    vals=[(bnd(Ml,t0),t0) for t0 in [-Pl/2,-Pl/4,0.0,Pl/8]]
    b,t=min(vals)
    print(f"M={Ml:3d} P={Pl:8.2f} best bound={b: .4e} at tau0={t:8.2f}   (tau0=0: {bnd(Ml,0.0): .4e})")
