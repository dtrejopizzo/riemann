"""Profile F0 of Paper 47 thm:oneprofile and the kernels Arch(d), c0(d).
g(t)=e^{bt}1_[0,a], T0=2a, G0=g*g~*g*g~, F0=(1/4-d^2)G0 normalised to ||F0||=1.
Fourier side: Fhat0(tau) = N (tau^2+1/4)|ghat(tau)|^4,  ghat(z)=(e^{(b+iz)a}-1)/(b+iz).
c0 = autocorrelation of F0  (c0hat = Fhat0^2), Arch(d) = (1/2pi) int m Fhat0^2 cos(tau d), m = Re psi(1/4+i tau/2) - log pi.
Everything is computed by the trapezoidal rule on a tau grid (spectrally accurate: integrand analytic in |Im tau|<1/2,
poles of psi at tau=-2i(k+1/4)) and an FFT gives Arch and c0 on a uniform d grid; cubic splines interpolate.
Precision is tracked by a second run with h/2, taumax*2 (see check()).
"""
import numpy as np
from scipy.special import digamma
from scipy.interpolate import CubicSpline

LOGPI = np.log(np.pi)
C0 = digamma(0.25) - LOGPI   # -5.3721834...

def m_arch(tau):
    return digamma(0.25 + 0.5j*tau).real - LOGPI

class Profile:
    def __init__(self, T0, b=1.0, h=0.05, taumax=1.0e5, dmax=None):
        self.T0, self.b, self.a = T0, b, T0/2.0
        self.h, self.taumax = h, taumax
        N = int(np.ceil(taumax/h))
        N = 1 << int(np.ceil(np.log2(N)))     # power of two for FFT
        self.N = N
        tau = h*np.arange(N)
        a, b = self.a, b
        g2 = (np.exp(2*b*a) - 2*np.exp(b*a)*np.cos(a*tau) + 1.0)/(b*b + tau*tau)   # |ghat|^2
        F = (tau*tau + 0.25)*g2*g2
        # normalisation: ||F0||^2 = (1/pi) int_0^inf F^2 (trapezoid)
        n2 = (h/np.pi)*(np.sum(F*F) - 0.5*F[0]*F[0])
        self.norm = 1.0/np.sqrt(n2)
        F *= self.norm
        self.Fhat_grid = F
        m = m_arch(tau)
        F2 = F*F
        # trapezoid for (1/pi) int_0^inf f(tau) cos(tau d) dtau  on d_j = 2 pi j/(N h)
        def cos_transform(f):
            f = f.copy(); f[0] *= 0.5
            return (h/np.pi)*np.fft.rfft(f).real      # length N/2+1 ... (real part of sum f_j e^{-2 pi i jk/N})
        self.dgrid = 2*np.pi*np.arange(N//2 + 1)/(N*h)
        self.arch_grid = cos_transform(m*F2)
        self.c0_grid = cos_transform(F2)
        self.dd = self.dgrid[1]
        # splines on the needed range
        if dmax is None:
            dmax = 20.0
        kmax = int(dmax/self.dd) + 8
        self.arch_spl = CubicSpline(self.dgrid[:kmax], self.arch_grid[:kmax])
        kc = int(2*T0/self.dd) + 8
        self.c0_spl = CubicSpline(self.dgrid[:kc], self.c0_grid[:kc])
        self.a0 = self.arch_grid[0]       # archimedean energy of F0 = B(0) when 2T0<log2
        self.dmax = dmax

    def arch(self, d):
        d = np.abs(np.asarray(d, dtype=float))
        return self.arch_spl(d)

    def c0(self, d):
        d = np.abs(np.asarray(d, dtype=float))
        out = np.zeros_like(d)
        msk = d < 2*self.T0
        out[msk] = self.c0_spl(d[msk])
        return out

    def Fhat(self, tau):
        """analytic continuation of Fhat0 (complex tau allowed)"""
        a, b = self.a, self.b
        gp = (np.exp((b + 1j*tau)*a) - 1)/(b + 1j*tau)
        gm = (np.exp((b - 1j*tau)*a) - 1)/(b - 1j*tau)
        return self.norm*(tau*tau + 0.25)*(gp*gm)**2

def check(T0, b=1.0, pts=(0.0, 0.01, 0.1, 0.5, 1.0, 3.0, 7.0, 9.0)):
    """convergence check: coarse vs fine quadrature"""
    P1 = Profile(T0, b, h=0.05, taumax=1e5)
    P2 = Profile(T0, b, h=0.025, taumax=2e5)
    pts = np.array(pts)
    da = np.max(np.abs(P1.arch(pts) - P2.arch(pts)))
    pc = pts[pts < 2*T0]
    dc = np.max(np.abs(P1.c0(pc) - P2.c0(pc)))
    return dict(T0=T0, b=b, a0=P1.a0, a0_fine=P2.a0, c0_0=P1.c0(0.0), max_dArch=da, max_dc0=dc,
                c0_min=float(P1.c0_grid[:int(2*T0/P1.dd)].min()))

if __name__ == "__main__":
    import time
    for T0 in (0.05, 0.15, 0.3):
        for b in (1.0, 2.0, -1.0):
            t = time.time(); r = check(T0, b); r['secs'] = time.time()-t
            print(r)
