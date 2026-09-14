"""Phase 130 builder's independent check of the Mittag-Leffler expansions
of the local symbols Whatp, Whatinfty of Paper 43 Theorem 9.7, and of the
Poisson/contour identity of Theorem 9.7b.  Numerics only; not a proof."""
import mpmath as mp
mp.mp.dps = 30

def W_p_closed(p, tau, theta=0.0):
    L = mp.log(p)
    z = p**mp.mpf(-0.5) * mp.e**(1j*(tau*L + theta))   # zeta = p^{-1/2} conj(eta)
    return L * 2*mp.re(z/(1-z))

def W_p_ML(p, tau, K=4000):
    L = mp.log(p)
    s = mp.mpf(0)
    for k in range(1, K+1):
        for sg in (1, -1):
            kk = sg*k
            s += 1/(tau - (0.5j + 2*mp.pi*kk/L)) - 1/(tau - (-0.5j + 2*mp.pi*kk/L))
    s += 1/(tau - 0.5j) - 1/(tau + 0.5j)
    return -1j*s - L

for p in (2,3,7):
    for tau in (0.0, 0.7, 3.1, -2.2):
        a = W_p_closed(p, mp.mpf(tau)); b = W_p_ML(p, mp.mpf(tau))
        print("p=%d tau=%5.2f  closed=%s  ML=%s  diff=%.2e" % (p,tau,mp.nstr(a,10),mp.nstr(b,10),abs(a-b)))

def W_inf_closed(tau):
    return mp.log(mp.pi) - mp.re(mp.digamma(0.25 + 1j*tau/2))

def W_inf_ML(tau, N=200000):
    s = mp.mpf(0)
    for n in range(N):
        w = 1j*(2*n + mp.mpf(0.5))
        s += -1j/(tau - w) + 1j/(tau + w) - mp.mpf(1)/(n+1)
    return mp.log(mp.pi) + mp.euler + s
for tau in (0.0, 1.3, 5.0):
    a = W_inf_closed(mp.mpf(tau)); b = W_inf_ML(mp.mpf(tau))
    print("inf tau=%4.1f closed=%s ML(trunc)=%s diff=%.2e" % (tau, mp.nstr(a,10), mp.nstr(b,10), abs(a-b)))

# residues at +- i/2 by contour integration of the closed forms
def res(f, c, r=0.15, n=4000):
    return sum(f(c + r*mp.e**(2j*mp.pi*k/n))*r*mp.e**(2j*mp.pi*k/n) for k in range(n))/n
def W2_an(tau):
    L = mp.log(2); w = (mp.mpf(0.5)+1j*tau)*L
    return L*(1/(1-mp.e**(-w)) + 1/(1-mp.e**(-mp.conj(w) if mp.im(tau)==0 else (mp.mpf(0.5)-1j*tau)*L*0+ (mp.mpf(0.5)-1j*tau)*L)) - 2)
def W2(tau):
    L = mp.log(2)
    return L*(1/(1-mp.e**(-(mp.mpf(0.5)+1j*tau)*L)) + 1/(1-mp.e**(-(mp.mpf(0.5)-1j*tau)*L)) - 2)
def Winf(tau):
    return mp.log(mp.pi) - (mp.digamma(0.25+1j*tau/2)+mp.digamma(0.25-1j*tau/2))/2
for f,name in ((W2,"W_2"),(Winf,"W_inf")):
    for c in (0.5j, -0.5j):
        print("residue of %s at %s = %s" % (name, mp.nstr(c,4), mp.nstr(res(f,c),8)))
