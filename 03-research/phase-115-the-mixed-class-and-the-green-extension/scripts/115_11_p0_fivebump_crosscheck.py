"""
POINT 0 -- redo the prime-free-window cross-check with FIVE bumps, so that a
NON-ODD element of T^0 is available (with four bumps the null space is
1-dimensional and the solution came out odd, collapsing the two conditions at
+-i/2 into one).

Gcal(t) = sum_j c_j beta(t-mu_j),  beta(u)=cos^8(pi u/(2w)) on |u|<=w.
Closed form (no nested quadrature):
   Psi(tau) = (1/128) sum_{m=0}^{4} a_m (-1)^{m+1} 2 tau sin(tau w)/((m pi/w)^2 - tau^2)
   a = (35,56,28,8,1),  removable poles at tau = m pi / w.
   Gcalhat(tau) = Psi(tau) * sum_j c_j e^{i tau mu_j}   (entire in tau)

Constraints (T^0 + CC):  sum c = 0,  sum c e^{-mu/2} = 0,  sum c e^{+mu/2} = 0.
With K = 0 exactly (support inside the prime-free window), the explicit formula
forces   sum_gamma |Gcalhat(gamma)|^2  ==  -G_infty(f,f).
"""
import mpmath as mp
mp.mp.dps = 30

w    = mp.mpf('0.08')
mus  = [mp.mpf(x) for x in ('-0.24','-0.12','0','0.12','0.24')]
acof = [35, 56, 28, 8, 1]

def Psi(tau):
    tau = mp.mpmathify(tau)
    s = mp.mpf(0)
    st = mp.sin(tau*w)
    for m in range(5):
        al = m*mp.pi/w
        d  = al**2 - tau**2
        if abs(d) < mp.mpf('1e-20'):          # removable singularity tau -> al
            term = acof[m]*(-1)**(m+1)*(-w*mp.cos(tau*w))   # limit of 2 t sin(tw)/(al^2-t^2)
            s += term
        else:
            s += acof[m]*(-1)**(m+1)*2*tau*st/d
    return s/128

# --- null space of the 3 constraints on 5 coefficients (dim 2) ---
def cons_row(mu):
    return [mp.mpf(1), mp.e**(-mu/2), mp.e**(mu/2)]
A = mp.matrix(3,5)
for j,mu in enumerate(mus):
    r = cons_row(mu)
    for i in range(3): A[i,j] = r[i]

# solve for c1..c3 given (c4,c5) free
def solve_with(free4, free5):
    M = mp.matrix(3,3); rhs = mp.matrix(3,1)
    for i in range(3):
        for j in range(3): M[i,j] = A[i,j]
        rhs[i] = -(A[i,3]*free4 + A[i,4]*free5)
    s = mp.lu_solve(M, rhs)
    return [s[0], s[1], s[2], mp.mpf(free4), mp.mpf(free5)]

cand = [solve_with(1,0), solve_with(0,1), solve_with(1,1), solve_with(1,-3)]
def oddness(c):                                  # 0 if perfectly odd
    return max(abs(c[j] + c[4-j]) for j in range(5))/max(abs(x) for x in c)
best = max(cand, key=oddness)
c = best
print("coefficients c =", [mp.nstr(x,10) for x in c])
print("oddness measure (0 = perfectly odd) = %s" % mp.nstr(oddness(c), 8))
for i,nm in enumerate(["sum c","sum c e^{-mu/2}","sum c e^{+mu/2}"]):
    print("   constraint %-16s = %s" % (nm, mp.nstr(mp.fsum([c[j]*A[i,j] for j in range(5)]), 5)))

def P(tau):
    s = mp.fsum([c[j]*mp.e**(mp.mpc(0,1)*tau*mus[j]) for j in range(5)])
    return abs(s)**2
Hhat = lambda tau: Psi(tau)**2 * P(tau)

TAUMAX = mp.mpf(220)
mGinf = mp.quad(lambda tau: (mp.re(mp.digamma(mp.mpf('0.25')+mp.mpc(0,0.5)*tau)) - mp.log(mp.pi))
                * Hhat(tau), [0,2,5,10,20,40,80,140,TAUMAX])/mp.pi
print("\n  -G_infty(f,f)   = %s" % mp.nstr(mGinf, 18))

NZ = 250
tot = mp.mpf(0)
for k in range(1, NZ+1):
    g = mp.im(mp.zetazero(k))
    tot += 2*Hhat(g)
    if k % 50 == 0:
        print("     %3d zeros (gamma=%8.2f):  Z = %s" % (k, float(g), mp.nstr(tot,18)), flush=True)
print("  sum over zeros  = %s   (tail |Hhat|=%.2e)" % (mp.nstr(tot,18), float(Hhat(g))))
print("\n  Z - (-G_infty)  = %s" % mp.nstr(tot-mGinf, 6))
print("  relative        = %s" % mp.nstr((tot-mGinf)/mGinf, 6))
