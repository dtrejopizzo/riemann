"""
STATUS: TIMED OUT (exit 124 at 900 s).  Only the first row completed.
This test design is SUPERSEDED by 115_08_prime_free_window_crosscheck.py.

Two defects, kept on record (see 115_08 section 5.1):
  1. Not a sign discriminator: L = D - G_infty and L = D + G_infty are both
     positive on the one row obtained, so the test cannot separate the two
     sign conventions.
  2. The Gaussian test functions are NOT in T^0 -- the run reports
     |Gcalhat(+-i/2)| = 0.504.  CC's theorems require the vanishing conditions,
     so any check of them must impose those first.

Retained only as the record of a failed test design.  Do not rerun as is.
"""
"""
Test Connes-Consani's UNCONDITIONAL positivity  L(f) = D(f) + W_infty(f) >= 0
(their eq. (9), stated with NO support restriction) in OUR normalisation,
to confirm the sign identification  W_infty^{CC} = -G_infty^{ours}.

Additive coordinates t = log rho, d*rho = dt.
  Gcal(t) real test function ;  H = autocorrelation of Gcal  (so H = g*g^* )
  Hhat(tau) = |Gcalhat(tau)|^2 >= 0 ,  Gcalhat(tau) = int Gcal(t) e^{i tau t} dt

  -G_infty = (1/2pi) int (Re psi(1/4+i tau/2) - log pi) Hhat(tau) dtau
  D(h)     = int_R H(t) delta(e^{|t|}) dt
  delta(rho) = 2 rho^{1/2} ( Si(2pi(1+rho))/(2pi(1+rho)) + Si(2pi(rho-1))/(2pi(rho-1)) ),  rho>=1

If the sign identification is right, L = D - G_infty must be >= 0 for EVERY
positive-definite h, with no support restriction.  If I have the sign backwards
it will come out systematically negative.
"""
import mpmath as mp
mp.mp.dps = 20

def Si(x):
    return mp.si(x)

def delta(rho):
    rho = mp.mpf(rho)
    if rho < 1:
        rho = 1/rho
    a = 2*mp.pi*(1+rho)
    t1 = Si(a)/a
    b = 2*mp.pi*(rho-1)
    t2 = mp.mpf(1) if b == 0 else Si(b)/b
    return 2*mp.sqrt(rho)*(t1+t2)

def make_test(centers, widths, coeffs):
    """Gcal(t) = sum coeffs_j * exp(-(t-c_j)^2/(2 w_j^2))"""
    def G(t):
        return mp.fsum([c*mp.e**(-(t-mu)**2/(2*w**2)) for mu,w,c in zip(centers,widths,coeffs)])
    def Ghat(tau):
        # analytic FT of the Gaussian sum, valid for complex tau
        return mp.fsum([c*w*mp.sqrt(2*mp.pi)*mp.e**(-w**2*tau**2/2)*mp.e**(mp.mpc(0,1)*tau*mu)
                        for mu,w,c in zip(centers,widths,coeffs)])
    return G, Ghat

def analyse(name, centers, widths, coeffs, TAUMAX=None, TMAX=None):
    G, Ghat = make_test(centers, widths, coeffs)
    wmax = max(widths); span = max(abs(c) for c in centers)
    if TAUMAX is None: TAUMAX = 18/min(widths)
    if TMAX   is None: TMAX   = 2*span + 14*wmax

    Hhat = lambda tau: abs(Ghat(tau))**2                  # tau real
    # H(t) = autocorrelation = (1/2pi) int Hhat(tau) e^{-i tau t} dtau  (real, even-ish)
    def H(t):
        return mp.quad(lambda tau: Hhat(tau)*mp.cos(tau*t), [0, TAUMAX])/mp.pi

    mGinf = mp.quad(lambda tau: (mp.re(mp.digamma(mp.mpf('0.25')+mp.mpc(0,0.5)*tau)) - mp.log(mp.pi))
                    * Hhat(tau), [0, TAUMAX])/mp.pi        # even integrand, folded
    Dh = 2*mp.quad(lambda t: H(t)*delta(mp.e**t), [0, TMAX/2, TMAX])

    # T^0 defect: Ghat at +- i/2  (both real for real Gcal)
    v_p = Ghat(mp.mpc(0, 0.5)); v_m = Ghat(mp.mpc(0,-0.5))
    print("%-28s  -G_inf=% .8f   D=% .8f   L=D-G_inf=% .8f   |Ghat(i/2)|=%.2e |Ghat(-i/2)|=%.2e"
          % (name, float(mGinf), float(Dh), float(Dh+mGinf), float(abs(v_p)), float(abs(v_m))), flush=True)
    return float(mGinf), float(Dh)

print("Testing  L = D + W_infty^{CC} = D - G_infty^{ours}  >= 0   (CC eq. 9, no support restriction)\n")
analyse("narrow, at 1",        [0.0],            [0.20],       [1.0])
analyse("narrow, at 1 (w=.4)", [0.0],            [0.40],       [1.0])
analyse("wide, at 1 (w=1.0)",  [0.0],            [1.00],       [1.0])
analyse("wide, at 1 (w=2.0)",  [0.0],            [2.00],       [1.0])
analyse("off-centre t=log2",   [0.6931],         [0.20],       [1.0])
analyse("off-centre t=log3",   [1.0986],         [0.20],       [1.0])
analyse("two bumps +-log2",    [0.6931,-0.6931], [0.20,0.20],  [1.0,1.0])
analyse("signed pair",         [0.6931,-0.6931], [0.20,0.20],  [1.0,-1.0])
analyse("far bump t=3",        [3.0],            [0.30],       [1.0])
