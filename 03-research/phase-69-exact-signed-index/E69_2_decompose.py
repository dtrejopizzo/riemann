"""
E69.2 -- decompose the Nevanlinna function N = N_arch + N_prime and study the sign structure.

N(z) = -d/dz log xi(1/2+iz),  xi = [1/2 s(s-1)] pi^{-s/2} Gamma(s/2) zeta(s).
  N_arch  = -d/dz log( [1/2 s(s-1)] pi^{-s/2} Gamma(s/2) )   (archimedean + pole cell)
  N_prime = -d/dz log zeta(1/2+iz)                            (Euler product; carries the zeros)

Questions:
 (1) Is Im N_arch >= 0 on the upper half z-plane? (archimedean = Nevanlinna, Gamma in Laguerre-Polya)
 (2) Sign and size of Im N_prime for zeta (RH), and does Im N_arch + Im N_prime >= 0 hold with the
     arch part providing a positive cushion?
"""
import mpmath as mp
mp.mp.dps=30
def arch(s): return 0.5*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)
def Narch(z):
    return -mp.diff(lambda w: mp.log(arch(mp.mpf('0.5')+1j*w)), z)
def Nprime(z):
    return -mp.diff(lambda w: mp.log(mp.zeta(mp.mpf('0.5')+1j*w)), z)
print("z = x + i y (upper half).  Im N_arch, Im N_prime, and their sum for zeta (RH).\n")
print("   x     y      Im N_arch    Im N_prime    Im sum")
for x in (15,25,40,60):
    for y in (0.2,0.5,1.0):
        z=mp.mpf(str(x))+1j*mp.mpf(str(y))
        ia=float(mp.im(Narch(z))); ip=float(mp.im(Nprime(z)))
        print(f"  {x:3d}   {y:.1f}    {ia:+9.4f}    {ip:+9.4f}    {ia+ip:+8.4f}")
print("\n(1) Im N_arch >= 0 everywhere? (archimedean Nevanlinna)")
print("(2) does arch cushion dominate so that the sum stays >= 0 for zeta?")
