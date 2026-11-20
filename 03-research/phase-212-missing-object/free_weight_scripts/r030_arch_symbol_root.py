# ROUND_030_A: simbolo arquimediano Omega(tau) = Re psi(1/4 + i tau/2) - log pi (P47 lem:K, C_0 = Omega(0)).
# Comprueba Omega(0) < 0 y localiza el unico cero positivo tau_0.
from mpmath import mp, digamma, log, pi, re, findroot
mp.dps = 20
Om = lambda t: re(digamma(0.25 + 0.5j*t)) - log(pi)
print("Omega(0) =", Om(0))
print("tau_0 =", findroot(Om, 6))
print("Omega(14.13) =", Om(14.13))
