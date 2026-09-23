"""dlib.py -- phase 155, R155_011: "D for 1000 zeros".

Same weight class as revlib2 (C^2 flat-top: psi-edge + cubic B-spline lattice),
but the zero side is evaluated through the identity

    f_w(tau) = sum_{rho} what(tau - gamma_rho)
             = 4 int_0^Umax w(u) cos(tau u) Z(u) du,     Z(u) = sum_{gamma>0} cos(gamma u),

which makes every basis row and every fine-grid evaluation a single matrix product.
ALL NUMBERS DIAGNOSTIC unless explicitly certified on the prime side.
"""
import numpy as np, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import revlib as R1, revlib2 as R2          # reuse conventions + prime side

# ------------------------------------------------------------------ geometry
class Win:
    def __init__(self, T, M=24, Ushoulder=6.5, Umax=14.0,
                 svals=(3.0, 6.0, 12.0, 24.0), dp=0.01, ngl=12):
        self.T = T; self.M = M; self.h = h = 2*T/M
        self.J = J = int(round(Ushoulder/h))
        self.ujs = 2*T + h*np.arange(2, 2+J)          # JOFF = 2, as revlib2
        self.Uspl = 2*T + h*(J+1) + 2*h               # end of B-spline support
        self.Umax = max(Umax, self.Uspl + 1.0)
        self.sv = np.array(svals, float)
        self.A_T = R1.A_const(T)
        self.taumax = 2*np.pi*np.exp(self.A_T)
        # --- quadrature panels: knot-aligned, width <= dp
        edges = [0.0, 2*T]
        kn = list(2*T + h*np.arange(0, J+3))
        edges += [k for k in kn if k > 2*T]
        edges += [self.Uspl, self.Umax]
        edges = sorted(set(round(e, 12) for e in edges))
        pans = []
        for a, b in zip(edges[:-1], edges[1:]):
            k = max(1, int(np.ceil((b-a)/dp)))
            xs = np.linspace(a, b, k+1)
            pans += list(zip(xs[:-1], xs[1:]))
        xg, wg = np.polynomial.legendre.leggauss(ngl)
        A = np.array([p[0] for p in pans]); B = np.array([p[1] for p in pans])
        self.u = (0.5*(B-A)[:, None]*xg[None, :] + 0.5*(A+B)[:, None]).ravel()
        self.wq = (0.5*(B-A)[:, None]*wg[None, :]).ravel()
        self.npan = len(pans); self.ngl = ngl

    # basis functions phi_c(u) on the node set: [box, psi_1..4, beta_1..J]
    def basis_matrix(self):
        u = self.u; T = self.T; h = self.h
        cols = [np.where(u <= 2*T + 1e-13, 1.0, 0.0)]
        v = u - 2*T
        for s in self.sv:
            cols.append(np.where(v > 0, R2.psi_edge(np.maximum(v, 0.0), s), 0.0))
        for uj in self.ujs:
            cols.append(R2.beta_spline((u-uj)/h))
        return np.array(cols)                      # (nc, nq)

    def w_of_u(self, u, y, x):
        v = np.asarray(u, float) - 2*self.T
        out = np.where(v <= 1e-13, 1.0, 0.0)
        m = v > 1e-13
        if m.any():
            acc = np.zeros(m.sum())
            for i, s in enumerate(self.sv): acc += y[i]*R2.psi_edge(v[m], s)
            for k, uj in enumerate(self.ujs):
                acc += x[k]*R2.beta_spline((np.asarray(u, float)[m]-uj)/self.h)
            out[m] = acc
        return out

# ------------------------------------------------------------------ zero side
def Zfun(u, gam, chunk=256):
    u = np.asarray(u, float); out = np.zeros_like(u)
    for a in range(0, len(gam), chunk):
        out += np.cos(np.outer(gam[a:a+chunk], u)).sum(0)
    return out

def rows(win, Phi, Z, tau, tblk=4000, ublk=2000):
    """Phi_c(tau) = 4 int phi_c cos(tau u) Z du, for all basis columns."""
    nc = Phi.shape[0]; nt = len(tau)
    out = np.zeros((nc, nt))
    G = Phi * (4.0*win.wq*Z)[None, :]                      # (nc, nq)
    for a in range(0, len(win.u), ublk):
        b = min(a+ublk, len(win.u)); uu = win.u[a:b]
        for c in range(0, nt, tblk):
            d = min(c+tblk, nt)
            out[:, c:d] += G[:, a:b] @ np.cos(np.outer(uu, tau[c:d]))
    return out

def fvals(win, Z, y, x, tau, tblk=8000, ublk=2000):
    """f_w(tau) directly (no per-column storage)."""
    g = 4.0*win.wq*Z*win.w_of_u(win.u, y, x)
    out = np.zeros(len(tau))
    for a in range(0, len(win.u), ublk):
        b = min(a+ublk, len(win.u)); uu = win.u[a:b]
        for c in range(0, len(tau), tblk):
            d = min(c+tblk, len(tau))
            out[c:d] += g[a:b] @ np.cos(np.outer(uu, tau[c:d]))
    return out

def what(win, y, x, t, tblk=20000, ublk=2000):
    """what(t) = 2 int_0^Umax w(u) cos(t u) du  (the smoothing kernel)."""
    t = np.asarray(t, float)
    g = 2.0*win.wq*win.w_of_u(win.u, y, x)
    out = np.zeros(t.shape)
    tf = t.ravel(); of = np.zeros(len(tf))
    for a in range(0, len(win.u), ublk):
        b = min(a+ublk, len(win.u)); uu = win.u[a:b]
        for c in range(0, len(tf), tblk):
            d = min(c+tblk, len(tf))
            of[c:d] += g[a:b] @ np.cos(np.outer(uu, tf[c:d]))
    return of.reshape(t.shape)

# ------------------------------------------------------------------ f'' bound
def d2_bound(win, y, x, Zenv):
    """B2 >= ||f''||_inf : |f''(tau)| = |4 int u^2 w cos(tau u) Z du| <= 4 int u^2|w| |Z|."""
    return float(4.0*np.sum(win.wq*win.u**2*np.abs(win.w_of_u(win.u, y, x))*Zenv))

def Zenvelope(win, gam, du=2e-5):
    """Panelwise upper bound of |Z(u)| on the quadrature nodes (running max on a fine u-grid)."""
    n = int(np.ceil(win.Umax/du)) + 1
    ug = np.linspace(0.0, win.Umax, n)
    Zg = np.abs(Zfun(ug, gam))
    slack = float(np.sum(gam))*du            # |Z'| <= sum gamma
    ngl = win.ngl
    env = np.empty(len(win.u))
    for p in range(win.npan):
        sl = slice(p*ngl, (p+1)*ngl)
        a, b = win.u[sl][0], win.u[sl][-1]
        i0 = max(0, int(np.floor(a/du))-1); i1 = min(n, int(np.ceil(b/du))+2)
        env[sl] = Zg[i0:i1].max() + slack
    return env
