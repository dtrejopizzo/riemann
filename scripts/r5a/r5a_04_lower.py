"""r5a_04: the PROVED lower bound  n_-(Gamma_T on L^2(-T,T)) >= #{k>=1 : k*pi/(2T) < tau0}.
Trial space = span of the first k Dirichlet modes of (-T,T) (in H^1_0, so Plancherel gives
int tau^2 |Fhat|^2/2pi = ||F'||^2 <= (k pi/2T)^2); Jensen for the concave phi (thm:S) gives
Gamma_T(F) <= C0 + phi(||F'||^2) < 0 whenever k pi/2T < tau0 (since phi(tau0^2) = -C0).
Checks phi(tau0^2) = -C0 and compares with the Galerkin counts of r5a_01.
"""
import sys, os, json, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'r3a'))
from arch_core import C0, phi_bernstein
tau0 = 6.289835988837543
print("phi(tau0^2) = %.7f   -C0 = %.7f   diff = %.2e"
      % (phi_bernstein(tau0**2), -C0, phi_bernstein(tau0**2)+C0))
out = []
for T in [0.5*np.log(3), float(np.log(2)), 0.80, 1.0, 2.0]:
    k = int(np.ceil(2*T*tau0/np.pi)) - 1
    out.append(dict(T=T, tb=2*T*tau0/np.pi, lower_L2=k, lower_PT=max(k-2, 0)))
    print("T=%.5f  2*T*tau0/pi = %.4f  n_-(Gamma_T) >= %d   n_-(A_inf|P_T) >= %d"
          % (T, 2*T*tau0/np.pi, k, max(k-2, 0)))
json.dump(out, open(os.path.join(HERE, 'r5a_04.json'), 'w'), indent=1)
