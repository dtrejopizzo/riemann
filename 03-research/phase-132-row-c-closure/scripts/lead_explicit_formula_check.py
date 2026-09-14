# Lead's independent check of the Weil explicit formula in the corpus convention
#   Phi_F(s) = int F(t) e^{(s-1/2)t} dt ,  g(s) = Phi_F(s) Phi_F(1-s)
#   sum_rho g(rho) = 2 Phi_F(0) Phi_F(1) + <A F, F>
#   <A F,F> = (1/2pi) int |F^(tau)|^2 [Re psi(1/4+i tau/2) - log pi] dtau
#             - sum_n Lambda(n) n^{-1/2} [h(log n)+h(-log n)],  h = F * F^dagger
# F(t) = exp(-a t^2) truncated smoothly? use Gaussian (not compactly supported, but
# rapidly decreasing: the formula holds for Schwartz F). Illustration only.
import mpmath as mp
mp.mp.dps = 20
a = mp.mpf('50')
Fhat = lambda tau: mp.sqrt(mp.pi/a)*mp.exp(-tau**2/(4*a))       # F^(tau)=int F e^{-i tau t}
Phi  = lambda s: mp.sqrt(mp.pi/a)*mp.exp((s-mp.mpf(1)/2)**2/(4*a))
h    = lambda x: mp.sqrt(mp.pi/(2*a))*mp.exp(-a*x**2/2)          # (F*F^dagger)(x)
NZ = 300
zeros = [mp.zetazero(k).imag for k in range(1, NZ+1)]
zs = sum(2*mp.re(Phi(mp.mpf(1)/2+1j*g)*Phi(mp.mpf(1)/2-1j*g)) for g in zeros)  # rho and conj
polar = 2*Phi(0)*Phi(1)
gamma_term = mp.quad(lambda t: Fhat(t)**2*(mp.re(mp.digamma(mp.mpf(1)/4+1j*t/2))-mp.log(mp.pi)), [-mp.inf, mp.inf])/(2*mp.pi)
def Lam(n):
    for p in range(2, n+1):
        if n % p == 0:
            m = n
            while m % p == 0: m //= p
            return mp.log(p) if m == 1 else 0
    return 0
prime = sum(Lam(n)/mp.sqrt(n)*(h(mp.log(n))+h(-mp.log(n))) for n in range(2, 4000))
rhs = polar + gamma_term - prime
print("sum over first %d zero pairs :"%NZ, zs)
print("polar + gamma - prime        :", rhs)
print("polar, gamma, prime          :", polar, gamma_term, prime)

# --- supplement: the meromorphic colimit symbol vanishes identically ---
def A(s): return mp.log(mp.pi)/2 - mp.digamma(s/2)/2 - mp.zeta(s,derivative=1)/mp.zeta(s)
for s in [mp.mpc(0.3,2), mp.mpc(0.5,14.0), mp.mpc(2,0.7), mp.mpc(-0.4,3.1)]:
    print("A(s)+A(1-s) at", s, "=", mp.nstr(A(s)+A(1-s), 5))
