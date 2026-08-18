"""
Decisive end-to-end check, inside Connes-Consani's prime-free window.

Test function: Gcal = sum_j c_j * bump(t - mu_j),  bump(u)=cos^8(pi u/(2w)) on |u|<=w.
  support(Gcal) subset [-0.32, 0.32] subset (-log sqrt2, log sqrt2) = (-0.34657, 0.34657)
  => support(g * g^vee) subset (1/2, 2)  => K(f,f) = 0 exactly (no prime power inside).

Constraints (the T^0 / CC conditions), using Gcalhat(tau) = Psi(tau) * sum_j c_j e^{i tau mu_j}:
  sum c_j = 0            (Gcalhat(0)=0)
  sum c_j e^{-mu_j/2}=0  (Gcalhat(i/2)=0)
  sum c_j e^{+mu_j/2}=0  (Gcalhat(-i/2)=0)

Then the explicit formula, with K=0 and the pole term killed, forces EXACTLY
       Z := sum over nontrivial zeros of |Gcalhat(gamma)|^2   ==   -G_infty(f,f).
Both sides are computed independently below.  Agreement verifies:
  (i) our sign convention,  (ii) the identification G_infty = -W_infty^{CC},
  (iii) row (d) numerically on the window (= Connes-Consani Theorem 1 regime).
"""
import mpmath as mp
mp.mp.dps = 25

w   = mp.mpf('0.08')
mus = [mp.mpf(x) for x in ('-0.24','-0.08','0.08','0.24')]

# nullspace of the 3x4 constraint matrix
A = mp.matrix(3,4)
for j,mu in enumerate(mus):
    A[0,j] = 1
    A[1,j] = mp.e**(-mu/2)
    A[2,j] = mp.e**( mu/2)
# solve with c_4 = 1
M = mp.matrix(3,3); rhs = mp.matrix(3,1)
for i in range(3):
    for j in range(3): M[i,j] = A[i,j]
    rhs[i] = -A[i,3]
sol = mp.lu_solve(M, rhs)
c = [sol[0], sol[1], sol[2], mp.mpf(1)]
print("coefficients c =", [mp.nstr(x,10) for x in c])
for i,nm in enumerate(["sum c","sum c e^{-mu/2}","sum c e^{+mu/2}"]):
    print("   constraint %-16s = %s" % (nm, mp.nstr(mp.fsum([c[j]*A[i,j] for j in range(4)]), 5)))

def Psi(tau):
    return mp.quad(lambda u: mp.cos(mp.pi*u/(2*w))**8 * mp.cos(tau*u), [-w, 0, w])

def P(tau):
    s = mp.fsum([c[j]*mp.e**(mp.mpc(0,1)*tau*mus[j]) for j in range(4)])
    return abs(s)**2

def Hhat(tau):            # = |Gcalhat(tau)|^2 >= 0
    return Psi(tau)**2 * P(tau)

# ---- side 1 : archimedean integral ----
TAUMAX = mp.mpf(160)
mGinf = mp.quad(lambda tau: (mp.re(mp.digamma(mp.mpf('0.25')+mp.mpc(0,0.5)*tau)) - mp.log(mp.pi))
                * Hhat(tau), [0, 5, 20, 60, TAUMAX])/mp.pi
print("\n  -G_infty(f,f)                      = %s" % mp.nstr(mGinf, 15))

# ---- side 2 : sum over the nontrivial zeros ----
NZ = 200
print("  computing %d zeta zeros ..." % NZ, flush=True)
tot = mp.mpf(0); last = None
for k in range(1, NZ+1):
    g = mp.im(mp.zetazero(k))
    tot += 2*Hhat(g)
    if k % 50 == 0:
        print("     after %3d zeros (gamma=%8.2f):  Z = %s" % (k, float(g), mp.nstr(tot,15)), flush=True)
    last = g
print("  sum over zeros  Z                  = %s   (tail past gamma=%.1f, |Hhat|=%.2e)"
      % (mp.nstr(tot,15), float(last), float(Hhat(last))))

print("\n  Z - (-G_infty)  = %s" % mp.nstr(tot - mGinf, 6))
print("  relative        = %s" % mp.nstr((tot - mGinf)/mGinf, 6))
