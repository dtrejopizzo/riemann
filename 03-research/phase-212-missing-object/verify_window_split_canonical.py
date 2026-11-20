"""Reparto local dependiente de la ventana: cuadratura de alta precision, P primos, y reparto canonico.

Arch(F) = C0||F||^2 + int_0^inf eps_F K du = <F, PotW F> + (1/4) iint_{IxI} K(|t-s|)(F(t)-F(s))^2,
donde PotW (multiplicacion por W) se obtiene por resta.  Pieza del primo p:
  q_p(F) = <F, U_p F> + (1/4) iint th_p(t,s) K (F(t)-F(s))^2 - Pi_p(F),
  th_p >= 0, sum_p th_p = 1, sum_p U_p = PotW, U_p = sum_i W_{p,i} 1_{celda i}.
uso: python3 verify_window_split_canonical.py T N NC [c] [modo]
  modo 'exist' : maximo tau con q_p >= tau para todo p (softmin, P primos)
  modo 'canon' : (P=2) reparto mas suave con q_p >= tau0
"""
import sys, pickle, numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import digamma
from scipy.optimize import minimize
from scipy.linalg import eigh

T = float(sys.argv[1]); N = int(sys.argv[2]); NC = int(sys.argv[3])
cw = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
mode = sys.argv[5] if len(sys.argv) > 5 else 'exist'
C0 = digamma(0.25) - np.log(np.pi)
K = lambda u: 0.5/np.sinh(u/2) + 0.5/np.cosh(u/2)
G = lambda u: np.log(np.tanh(u/4)) + 2*np.arctan(np.exp(u/2))
om = np.pi/(2*T); kk = np.arange(1, N+1)
def S(t):
    t = np.atleast_1d(np.asarray(t, float))
    out = np.sin(kk[:, None]*om*(t[None, :]+T))/np.sqrt(T)
    out[:, (t < -T) | (t > T)] = 0.0
    return out
def gl(a, b, n):
    x, w = leggauss(n); return (a+b)/2 + (b-a)/2*x, (b-a)/2*w

# --- autocorrelacion exacta (integrando analitico) ---
def Cmat(u):
    x, w = gl(-T+u, T, 96)
    A = (S(x)*w) @ S(x-u).T
    return 0.5*(A+A.T)
ug, uw = gl(0, 2*T, 160)
Arch = (C0 + np.pi - G(2*T))*np.eye(N) + sum(w*K(u)*(np.eye(N)-Cmat(u)) for u, w in zip(ug, uw))
xt, wt = gl(-T, T, 160)
M = np.vstack([(S(xt)*wt) @ np.exp(xt/2), (S(xt)*wt) @ np.exp(-xt/2)])
Z = np.linalg.svd(M)[2][2:].T
pr = lambda A: Z.T @ A @ Z

# --- contactos ---
def primes_upto(x):
    return [p for p in range(2, int(x)+1) if all(p % q for q in range(2, int(p**0.5)+1))]
import os
BYN = os.environ.get('BYN') == '1'          # una pieza por potencia de primo n en lugar de por primo
PR0 = [p for p in primes_upto(np.exp(2*T)) if np.log(p) < 2*T]
Pi = {}
for p in PR0:
    k = 1; Mx = np.zeros((N, N))
    while k*np.log(p) < 2*T and (k == 1 or os.environ.get('NOPOW') != '1'):
        term = cw*2*np.log(p)/p**(k/2)*Cmat(k*np.log(p))
        if BYN: Pi[p**k] = term
        else: Mx += term
        k += 1
    if not BYN: Pi[p] = Mx
PR = sorted(Pi)
P = len(PR)
a_form = Arch - sum(Pi.values())
lamA = np.linalg.eigvalsh(pr(a_form))
print(f"T={T} N={N} NC={NC} c={cw} primos={PR}  fondo a|P={lamA[0]:.6e}  segundo={lamA[1]:.4e}  "
      f"fondo Arch|P={np.linalg.eigvalsh(pr(Arch))[0]:.4e}", flush=True)

# --- piezas de la integral doble por celdas ---
mg = 10
edges = np.linspace(-T, T, NC+1); h = 2*T/NC
nodes = [gl(edges[i], edges[i+1], mg) for i in range(NC)]
Sc = [S(n[0]) for n in nodes]
Pot = [(Sc[i]*nodes[i][1]) @ Sc[i].T for i in range(NC)]
pairs = [(i, j) for i in range(NC) for j in range(i, NC)]
x1, w1 = gl(0, 1, 14)
Gp = []
for (i, j) in pairs:
    if i == j:
        a = edges[i]
        tt = a + h*x1[:, None]*np.ones((1, 14)); ss = a + h*x1[:, None]*x1[None, :]
        ww = h*h*x1[:, None]*w1[:, None]*w1[None, :]
        D = S(tt.ravel()) - S(ss.ravel())
        Wt = (ww*K(tt-ss)).ravel()
        Gp.append(0.5*(D*Wt) @ D.T)                      # 1/4 * 2 triangulos
    else:
        D = Sc[i][:, :, None] - Sc[j][:, None, :]
        Wt = nodes[i][1][:, None]*nodes[j][1][None, :]*K(np.abs(nodes[i][0][:, None]-nodes[j][0][None, :]))
        Gp.append(0.5*np.einsum('kab,lab,ab->kl', D, D, Wt))   # 1/4 * 2 ordenes
Gp = np.array(Gp); Pot = np.array(Pot)
PotW = Arch - Gp.sum(0)
Wfun = lambda t: C0 + 0.5*((np.pi-G(T-t)) + (np.pi-G(T+t)))
Wc = np.array([np.sum(nodes[i][1]*Wfun(nodes[i][0]))/h for i in range(NC)])
chk = PotW - np.tensordot(Wc, Pot, 1)
print(f"control: |sum Pot - I|={np.abs(Pot.sum(0)-np.eye(N)).max():.1e}  "
      f"|PotW - sum Wc_i Pot_i| en P (norma op)={np.abs(np.linalg.eigvalsh(pr(chk))).max():.2e}", flush=True)
PG = np.array([pr(g) for g in Gp]); PP = np.array([pr(g) for g in Pot]); PW = pr(PotW)
PPi = [pr(Pi[p]) for p in PR]
npair = len(pairs)
ceil_ = lamA[0]/P

def pieces(th, W):          # th: P x npair, W: P x NC (ultima fila = resto)
    return [np.tensordot(th[p], PG, 1) + np.tensordot(W[p], PP, 1) - PPi[p] if p < P-1 else
            np.tensordot(th[p], PG, 1) + PW - sum(np.tensordot(W[q], PP, 1) for q in range(P-1)) - PPi[p]
            for p in range(P)]

def exist(z0=None, betas=(3e2, 3e3, 3e4, 3e5, 3e6, 3e7)):
    nz = P*npair + (P-1)*NC
    x = np.zeros(nz) if z0 is None else z0.copy()
    if z0 is None:
        x[P*npair:] = np.tile(Wc/P, P-1)
    def unpack(x):
        z = x[:P*npair].reshape(P, npair); z = z - z.max(0)
        th = np.exp(z); th /= th.sum(0)
        return th, x[P*npair:].reshape(P-1, NC)
    def val(x):
        th, W = unpack(x); return min(np.linalg.eigvalsh(q)[0] for q in pieces(th, W))
    for beta in betas:
        def f(x):
            th, W = unpack(x); Q = pieces(th, W)
            ev = [eigh(q) for q in Q]; m = min(e[0][0] for e in ev)
            ex = [np.exp(-beta*(e[0]-m)) for e in ev]; Zs = sum(e.sum() for e in ex)
            rho = [(e[1]*x_) @ e[1].T/Zs for e, x_ in zip(ev, ex)]
            gth = np.array([-np.einsum('ab,jab->j', r, PG) for r in rho])      # d/d th_p
            gz = th*(gth - (th*gth).sum(0))
            gW = np.array([-np.einsum('ab,jab->j', rho[p], PP) + np.einsum('ab,jab->j', rho[P-1], PP)
                           for p in range(P-1)])
            return -m + np.log(Zs)/beta, np.concatenate([gz.ravel(), gW.ravel()])
        res = minimize(f, x, jac=True, method='L-BFGS-B', options=dict(maxiter=6000, maxfun=9000, ftol=1e-16, gtol=1e-13))
        x = res.x
        print(f"  beta={beta:.0e} tau={val(x):.6e} nit={res.nit}", flush=True)
    th, W = unpack(x)
    return x, th, W, val(x)

def exist_box(betas=(3e2, 3e3, 3e4, 3e5, 3e6, 3e7, 3e8)):
    """P = 2, problema convexo: th en [0,1], W2 libre."""
    PA = pr(Arch)
    def parts(xv):
        Rm = np.tensordot(xv[:npair], PG, 1) + np.tensordot(xv[npair:], PP, 1)
        return Rm - PPi[0], PA - Rm - PPi[1]
    xv = np.concatenate([np.full(npair, 0.5), Wc/2])
    for beta in betas:
        def f(xv):
            Q2, Q3 = parts(xv); w2, V2 = eigh(Q2); w3, V3 = eigh(Q3); m = min(w2[0], w3[0])
            e2 = np.exp(-beta*(w2-m)); e3 = np.exp(-beta*(w3-m)); Zs = e2.sum()+e3.sum()
            D = (V2*e2) @ V2.T/Zs - (V3*e3) @ V3.T/Zs
            return -m + np.log(Zs)/beta, -np.concatenate([np.einsum('ab,jab->j', D, PG), np.einsum('ab,jab->j', D, PP)])
        res = minimize(f, xv, jac=True, method='L-BFGS-B', bounds=[(float(os.environ.get('TH_LO', 0)), float(os.environ.get('TH_HI', 1)))]*npair+[(-1e4, 1e4)]*NC,
                       options=dict(maxiter=20000, maxfun=30000, ftol=1e-16, gtol=1e-13))
        xv = res.x
    Q2, Q3 = parts(xv)
    return xv, min(np.linalg.eigvalsh(Q2)[0], np.linalg.eigvalsh(Q3)[0])
if mode == 'box' and P == 2:
    xv, tb = exist_box()
    print(f"[BOX] T={T} N={N} NC={NC} c={cw}  tau={tb:.6e}  techo={ceil_:.6e}  fondo Arch|P={np.linalg.eigvalsh(pr(Arch))[0]:.4e}  en cotas 0:{(xv[:npair]<1e-6).sum()} 1:{(xv[:npair]>1-1e-6).sum()} de {npair}", flush=True)
    sys.exit()
if mode in ('mclass', 'transfer') and P == 2:
    # mclass  : max tau con th = phi(|i-j|) en [0,1] y W2 por celda libre (clase M).
    # transfer: th(t,s) en [0,1], W2 libre, mas una forma de transferencia X = Xp - Xm entre las dos piezas;
    #           se minimiza tr Xp + tr Xm (norma nuclear) con ambas piezas >= T0 (por defecto -1e-6).
    import cvxpy as cp
    PA = pr(Arch); d = PA.shape[0]; sym = lambda A: 0.5*(A + A.T); I_ = np.eye(d)
    AG = np.array([sym(g).ravel() for g in PG]).T; AP = np.array([sym(g).ravel() for g in PP]).T
    form = lambda thv, Wv: cp.reshape(AG @ thv + AP @ Wv, (d, d), order='C')
    def solve(pb):
        for tol in (1e-12, 1e-10, 1e-9, 1e-8):
            try:
                pb.solve(solver=cp.CLARABEL, tol_gap_abs=tol, tol_gap_rel=tol, tol_feas=tol, max_iter=1000)
                if pb.status in ('optimal', 'optimal_inaccurate'): return tol
            except Exception as e: pass
        return None
    Wv = cp.Variable(NC)
    if mode == 'mclass':
        phi = cp.Variable(NC); Sel = np.zeros((npair, NC))
        for k, (i, j) in enumerate(pairs): Sel[k, j-i] = 1
        Rm = form(Sel @ phi, Wv); tau_ = cp.Variable()
        pb = cp.Problem(cp.Maximize(tau_), [Rm - sym(PPi[0]) >> tau_*I_, sym(PA) - Rm - sym(PPi[1]) >> tau_*I_, phi >= 0, phi <= 1])
        tol = solve(pb)
        np.set_printoptions(linewidth=250, precision=2, suppress=True)
        print(f"[M] T={T} N={N} NC={NC} c={cw} tau={tau_.value:.6e} techo={ceil_:.6e} estado={pb.status} tol={tol}")
        print("  phi(distancia):", phi.value)
        sys.exit()
    thv = cp.Variable(npair); Xp = cp.Variable((d, d), PSD=True); Xm = cp.Variable((d, d), PSD=True)
    Rm = form(thv, Wv); t0 = float(os.environ.get('T0', -1e-6)); X = Xp - Xm
    pb = cp.Problem(cp.Minimize(cp.trace(Xp) + cp.trace(Xm)),
                    [Rm - sym(PPi[0]) + X >> t0*I_, sym(PA) - Rm - sym(PPi[1]) - X >> t0*I_, thv >= 0, thv <= 1,
                     Wv >= -200, Wv <= 200])
    tol = solve(pb)
    Xv = sym(Xp.value - Xm.value); e, V = np.linalg.eigh(Xv); o = np.argsort(-np.abs(e))
    print(f"[TRANSFER] T={T} N={N} NC={NC} c={cw} norma nuclear={pb.value:.6e} estado={pb.status} tol={tol}")
    print("  autovalores de X (por modulo):", e[o][:8])
    ea, Va = np.linalg.eigh(pr(a_form)); l_ = V[:, o[0]]
    print("  solapamiento de l con los 4 autovectores mas bajos de a|P:", np.abs(Va[:, :4].T @ l_), " autovalores:", ea[:4])
    R_ = (AG @ thv.value + AP @ Wv.value).reshape(d, d); q2 = R_ - sym(PPi[0]); q3 = sym(PA) - R_ - sym(PPi[1])
    e2, V2 = np.linalg.eigh(q2); e3, V3 = np.linalg.eigh(q3)
    print("  q2 sin transferencia: autovalores mas bajos", e2[:3], " solapamiento de l con el mas bajo:", abs(V2[:, 0] @ l_))
    print("  q3 sin transferencia: autovalores mas bajos", e3[:3], " l'q3 l =", l_ @ q3 @ l_, " l'q2 l =", l_ @ q2 @ l_)
    tg = np.linspace(-T, T, 29); Sg = S(tg)
    np.set_printoptions(linewidth=250, precision=3, suppress=True)
    print("  t:", tg)
    for r in range(3):
        f = Sg.T @ (Z @ V[:, o[r]]); f = f*np.sign(f[np.argmax(np.abs(f))])
        print(f"  autofuncion {r+1} (autovalor {e[o[r]]:+.4e}):", f)
    pickle.dump(dict(T=T, N=N, NC=NC, X=Xv, Z=Z, th=thv.value, W2=Wv.value, edges=edges),
                open(f"transfer_{T}_{N}_{NC}.pkl", "wb"))
    sys.exit()
if mode in ('sdp', 'dual') and P == 2:
    # programa semidefinido (requiere cvxpy + clarabel).  Paso 1: max tau con th en [0,1].
    # Paso 2: th = u - n2 + n3, minimo prestamo (area) con q_p >= techo/2.
    import cvxpy as cp
    PA = pr(Arch); d = PA.shape[0]; sym = lambda A: 0.5*(A + A.T)
    area = np.array([h*h if i == j else 2*h*h for (i, j) in pairs])/(4*T*T)
    kw = dict(solver=cp.CLARABEL, tol_gap_abs=1e-13, tol_gap_rel=1e-13, tol_feas=1e-13, max_iter=500)
    def lin(thv, Wv):
        return sum(thv[k]*sym(PG[k]) for k in range(npair)) + sum(Wv[i]*sym(PP[i]) for i in range(NC))
    thv = cp.Variable(npair); Wv = cp.Variable(NC); tau_ = cp.Variable()
    Rm = lin(thv, Wv)
    pb = cp.Problem(cp.Maximize(tau_), [Rm - sym(PPi[0]) >> tau_*np.eye(d), sym(PA) - Rm - sym(PPi[1]) >> tau_*np.eye(d),
                                         thv >= 0, thv <= 1])
    pb.solve(**kw)
    print(f"[SDP-MAX] T={T} N={N} NC={NC} tau={tau_.value:.6e} techo={ceil_:.6e} estado={pb.status}", flush=True)
    if mode == 'dual':
        # par obstructor: Y2, Y3 >= 0, tr Y2 + tr Y3 = 1, misma densidad por celda
        Y2 = sym(pb.constraints[0].dual_value); Y3 = sym(pb.constraints[1].dual_value)
        D = np.einsum('ab,jab->j', Y2 - Y3, PG); dW = np.einsum('ab,jab->j', Y2 - Y3, PP)
        val = -np.sum(Y2*PPi[0]) + np.sum(Y3*(PA - PPi[1])) + np.maximum(D, 0).sum()
        e2, V2 = np.linalg.eigh(Y2); e3, V3 = np.linalg.eigh(Y3)
        print(f"[DUAL] tr Y2={np.trace(Y2):.6f} tr Y3={np.trace(Y3):.6f} valor dual={val:.6e} max|dens2-dens3| por celda={np.abs(dW).max():.2e}")
        print("  autovalores Y2:", e2[::-1][:6]); print("  autovalores Y3:", e3[::-1][:6])
        tg = np.linspace(-T, T, 29); Sg = S(tg)
        np.set_printoptions(linewidth=250, precision=3, suppress=True)
        print("  t:", tg)
        for nm, Y, V, e in (("2", Y2, V2, e2), ("3", Y3, V3, e3)):
            sg = Z @ Y @ Z.T
            print(f"  densidad sigma_{nm}:", np.einsum('ka,kl,la->a', Sg, sg, Sg))
            for r in (1, 2):
                f = Sg.T @ (Z @ V[:, -r]); f = f*np.sign(f[np.argmax(np.abs(f))])
                print(f"  autofuncion {r} de sigma_{nm} (peso {e[-r]:.4f}):", f)
        def full(v):
            Mx = np.zeros((NC, NC))
            for k, (i, j) in enumerate(pairs): Mx[i, j] = Mx[j, i] = v[k]
            return Mx
        Df = full(D); sc = np.abs(D).max()
        print("  signo de D(t,s) = energia de par de sigma_2 menos la de sigma_3 (+: theta=1, -: theta=0, .: |D|<1e-3 max):")
        for i in range(NC): print("   ", "".join('+' if Df[i, j] > 1e-3*sc else '-' if Df[i, j] < -1e-3*sc else '.' for j in range(NC)))
        print("  theta optimo:"); np.set_printoptions(precision=1); print(full(thv.value))
        pickle.dump(dict(T=T, N=N, NC=NC, Y2=Y2, Y3=Y3, Z=Z, D=Df, TH=full(thv.value), W2=Wv.value, edges=edges),
                    open(f"dual_{T}_{N}_{NC}.pkl", "wb"))
        sys.exit()
    u = cp.Variable(npair); n2v = cp.Variable(npair); n3v = cp.Variable(npair); Wv = cp.Variable(NC)
    Rm = lin(u - n2v + n3v, Wv); t0 = float(os.environ.get('T0', 0.5*ceil_))
    pb = cp.Problem(cp.Minimize(area @ (n2v + n3v)),
                    [Rm - sym(PPi[0]) >> t0*np.eye(d), sym(PA) - Rm - sym(PPi[1]) >> t0*np.eye(d),
                     u >= 0, u <= 1, n2v >= 0, n3v >= 0, n2v <= 5, n3v <= 5, Wv >= -200, Wv <= 200])
    for tol in (1e-12, 1e-10, 1e-9, 1e-8):
        try:
            pb.solve(solver=cp.CLARABEL, tol_gap_abs=tol, tol_gap_rel=tol, tol_feas=tol, max_iter=1000)
            if u.value is not None: print("  tolerancia", tol, flush=True); break
        except Exception as e: print("  fallo con tolerancia", tol, str(e)[:80], flush=True)
    if u.value is None:
        pb.solve(solver=cp.SCS, eps=1e-9, max_iters=400000); print("  SCS", pb.status, flush=True)
    xv = np.concatenate([u.value, n2v.value, n3v.value, Wv.value])
    thf = u.value - n2v.value + n3v.value
    R_ = np.tensordot(thf, PG, 1) + np.tensordot(Wv.value, PP, 1)
    print(f"[SDP-PRESTAMO] estado={pb.status} prestamo={pb.value:.6e} (th<0: {area @ n2v.value:.3e}, th>1: {area @ n3v.value:.3e}) "
          f"min q2={np.linalg.eigvalsh(R_-PPi[0])[0]:.3e} q3={np.linalg.eigvalsh(PA-R_-PPi[1])[0]:.3e}", flush=True)
    def full(v):
        Mx = np.zeros((NC, NC))
        for k, (i, j) in enumerate(pairs): Mx[i, j] = Mx[j, i] = v[k]
        return Mx
    cen = (edges[:-1] + edges[1:])/2
    np.set_printoptions(linewidth=250, precision=2, suppress=True)
    print("centros de celda:", cen)
    print("exceso th - clip(th,0,1):"); print(full(n3v.value - n2v.value))
    print("th completo:"); print(full(thf))
    print("W2 - W/2:", Wv.value - Wc/2)
    pickle.dump(dict(T=T, N=N, NC=NC, TH=full(thf), n2=full(n2v.value), n3=full(n3v.value), W2=Wv.value, Wc=Wc, edges=edges),
                open(f"sdp_{T}_{N}_{NC}.pkl", "wb"))
    sys.exit()
if mode == 'signed' and P == 2:
    # th = u - n2 + n3, u en [0,1], n2,n3 >= 0: minimo prestamo (area) con q_p >= tau0 = techo/2
    PA = pr(Arch); tau0 = 0.5*ceil_
    area = np.array([h*h if i == j else 2*h*h for (i, j) in pairs])/(4*T*T)
    def parts(xv):
        thv = xv[:npair] - xv[npair:2*npair] + xv[2*npair:3*npair]
        Rm = np.tensordot(thv, PG, 1) + np.tensordot(xv[3*npair:], PP, 1)
        return Rm - PPi[0], PA - Rm - PPi[1]
    xv = np.concatenate([np.full(npair, 0.5), np.zeros(2*npair), Wc/2])
    bnd = [(0, 1)]*npair + [(0, 5)]*(2*npair) + [(-1e4, 1e4)]*NC
    for rho in (1e2, 1e4, 1e6, 1e8, 1e10, 1e12, 1e14):
        def f(xv):
            obj = area @ (xv[npair:2*npair] + xv[2*npair:3*npair]); g = np.zeros_like(xv)
            g[npair:2*npair] = area; g[2*npair:3*npair] = area
            Q2, Q3 = parts(xv); pen = 0.0
            for Q, sgn in ((Q2, 1.0), (Q3, -1.0)):
                w_, V = eigh(Q); d = np.maximum(0, tau0 - w_)
                if d.any():
                    pen += np.sum(d**2); Mx = (V*d) @ V.T
                    gt = -2*sgn*np.einsum('ab,jab->j', Mx, PG)
                    g[:npair] += rho*gt; g[npair:2*npair] -= rho*gt; g[2*npair:3*npair] += rho*gt
                    g[3*npair:] += -2*rho*sgn*np.einsum('ab,jab->j', Mx, PP)
            return obj + rho*pen, g
        res = minimize(f, xv, jac=True, method='L-BFGS-B', bounds=bnd,
                       options=dict(maxiter=30000, maxfun=40000, ftol=1e-18, gtol=1e-14))
        xv = res.x; Q2, Q3 = parts(xv)
        print(f"  rho={rho:.0e} prestamo={area @ (xv[npair:2*npair]+xv[2*npair:3*npair]):.6e} "
              f"min q2={np.linalg.eigvalsh(Q2)[0]:.3e} q3={np.linalg.eigvalsh(Q3)[0]:.3e} nit={res.nit}", flush=True)
    def full(v):
        Mx = np.zeros((NC, NC))
        for k, (i, j) in enumerate(pairs): Mx[i, j] = Mx[j, i] = v[k]
        return Mx
    n2 = full(xv[npair:2*npair]); n3 = full(xv[2*npair:3*npair]); U = full(xv[:npair])
    cen = (edges[:-1] + edges[1:])/2
    print(f"[SIGNED] T={T} N={N} NC={NC} prestamo total={area @ (xv[npair:2*npair]+xv[2*npair:3*npair]):.6e} "
          f"(parte th<0: {area @ xv[npair:2*npair]:.3e}, parte th>1: {area @ xv[2*npair:3*npair]:.3e})  max n2={n2.max():.3f} max n3={n3.max():.3f}")
    np.set_printoptions(linewidth=250, precision=2, suppress=True)
    print("centros de celda:", cen)
    print("th - clip(th,0,1) (filas t, columnas s):"); print(n3 - n2)
    pickle.dump(dict(T=T, N=N, NC=NC, U=U, n2=n2, n3=n3, W2=xv[3*npair:], Wc=Wc, edges=edges),
                open(f"signed_{T}_{N}_{NC}.pkl", "wb"))
    sys.exit()
x, th, W, tau = exist()
print(f"[EXIST] T={T} N={N} NC={NC} c={cw} P={P}  tau={tau:.6e}  techo={ceil_:.6e}  tau/techo={tau/ceil_ if ceil_>0 else float('nan'):.4f}", flush=True)

if mode == 'canon' and P == 2 and tau > 0:
    tau0 = 0.5*tau
    idx = {p_: k for k, p_ in enumerate(pairs)}
    def full(v):
        Mx = np.zeros((NC, NC))
        for k, (i, j) in enumerate(pairs): Mx[i, j] = Mx[j, i] = v[k]
        return Mx
    alpha = 1.0
    def R(xv):
        TH = full(xv[:npair]); dW = xv[npair:] - Wc/2
        d1 = TH[1:, :] - TH[:-1, :]
        r = 2*np.sum(d1**2) + alpha*h*np.sum(dW**2)
        gT = np.zeros((NC, NC)); gT[1:, :] += 4*d1; gT[:-1, :] -= 4*d1
        gT = gT + gT.T                                   # simetria (dos direcciones)
        g = np.array([gT[i, j] if i != j else gT[i, i]/2 for (i, j) in pairs])
        return r, np.concatenate([g, 2*alpha*h*dW])
    xv = np.concatenate([th[0], W[0]])
    lo = [0]*npair + [-1e3]*NC; hi = [1]*npair + [1e3]*NC
    def parts(xv):
        Rm = np.tensordot(xv[:npair], PG, 1) + np.tensordot(xv[npair:], PP, 1)
        return Rm - PPi[0], pr(Arch) - Rm - PPi[1]
    for rho in (1e3, 1e5, 1e7, 1e9, 1e11):
        def f(xv):
            r, g = R(xv); Q2, Q3 = parts(xv)
            pen = 0.0; gp = np.zeros_like(xv)
            for Q, sgn in ((Q2, 1.0), (Q3, -1.0)):
                w_, V = eigh(Q); d = np.maximum(0, tau0 - w_)
                if d.any():
                    pen += np.sum(d**2)
                    Mx = (V*d) @ V.T
                    gp[:npair] += -2*sgn*np.einsum('ab,jab->j', Mx, PG)
                    gp[npair:] += -2*sgn*np.einsum('ab,jab->j', Mx, PP)
            return r + rho*pen, g + rho*gp
        res = minimize(f, xv, jac=True, method='L-BFGS-B', bounds=list(zip(lo, hi)),
                       options=dict(maxiter=20000, maxfun=30000, ftol=1e-16, gtol=1e-12))
        xv = res.x; Q2, Q3 = parts(xv)
        print(f"  rho={rho:.0e} R={R(xv)[0]:.6f} min eig q2={np.linalg.eigvalsh(Q2)[0]:.3e} q3={np.linalg.eigvalsh(Q3)[0]:.3e} nit={res.nit}", flush=True)
    TH = full(xv[:npair]); W2 = xv[npair:]
    Q2, Q3 = parts(xv)
    print(f"[CANON] T={T} N={N} NC={NC}  R={R(xv)[0]:.6f}  R_theta={R(xv)[0]-alpha*h*np.sum((W2-Wc/2)**2):.6f}  "
          f"min q2={np.linalg.eigvalsh(Q2)[0]:.3e} min q3={np.linalg.eigvalsh(Q3)[0]:.3e}  en cotas 0:{(xv[:npair]<1e-6).sum()} 1:{(xv[:npair]>1-1e-6).sum()} de {npair}", flush=True)
    pickle.dump(dict(T=T, N=N, NC=NC, TH=TH, W2=W2, Wc=Wc, edges=edges, lamA=lamA, Z=Z,
                     vec=eigh(pr(a_form))[1][:, 0], Q2=Q2, Q3=Q3),
                open(f"canon_{T}_{N}_{NC}.pkl", "wb"))
