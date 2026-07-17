"""
E22: PASO 1 de la ruta nueva a 2.3.F.
Reconstruir la coordenada portadora theta(y) y verificar que QW_lambda|bulk es
Dirichlet PLANO -d_theta^2: autofunciones f_k(y) = C_k sin((k+1) theta(y)),
un UNICO mapa theta(y) para todos los k.

Tests:
 (T1) cos(theta) propto f_1/f_0  debe ser LINEAL en y   (mapa portador)
 (T2) f_k/f_0 = U_k(cos theta)   Chebyshev 2a clase     (= sin((k+1)theta))
Si pasan: PASO 1 validado; theta(y) es el objeto a derivar analiticamente.
"""
import numpy as np, mpmath as mp
mp.mp.dps = 40
GAMMA = mp.euler; LOG4PI = mp.log(4*mp.pi)

def q_func(m, n, L):
    if m == n: return lambda y: 2*(1-y/L)*mp.cos(2*mp.pi*n*y/L)
    c = 1/(mp.pi*(n-m))
    return lambda y: (mp.sin(2*mp.pi*m*y/L)-mp.sin(2*mp.pi*n*y/L))*c
def QW_entry(m, n, L, lam):
    q = q_func(m, n, L); q0 = q(mp.mpf(0))
    W02 = mp.quad(lambda y: q(y)*(mp.e**(y/2)+mp.e**(-y/2)), [0, L])
    def wr(y):
        if y < mp.mpf('1e-12'):
            h = mp.mpf('1e-8'); return ((q(h)-q0)/h+q0/2)/2
        return (mp.e**(y/2)*q(y)-q0)/(2*mp.sinh(y))
    WR = (LOG4PI+GAMMA)*q0/2 + mp.quad(wr, [0, L]) + q0*mp.log(mp.tanh(L/2))/2
    arith = mp.mpf(0); mx = int(lam*lam); sv = [True]*(mx+1)
    for i in range(2, int(mx**0.5)+1):
        if sv[i]:
            for j in range(i*i, mx+1, i): sv[j] = False
    for p in range(2, mx+1):
        if sv[p]:
            lp = mp.log(p); pm = p; me = 1
            while pm <= mx:
                arith += lp*(mp.mpf(pm)**mp.mpf('-0.5'))*q(me*lp); pm *= p; me += 1
    return W02 - WR - arith

def chebyU(k, x):
    if k == 0: return np.ones_like(x)
    if k == 1: return 2*x
    Um1 = np.ones_like(x); U = 2*x
    for _ in range(2, k+1):
        Um1, U = U, 2*x*U - Um1
    return U

def run(lam, N):
    L = float(2*mp.log(mp.mpf(lam))); dim = 2*N+1; idx = list(range(-N, N+1))
    M = mp.zeros(dim)
    for a in range(dim):
        for b in range(a, dim):
            v = QW_entry(idx[a], idx[b], float_L:=2*mp.log(mp.mpf(lam)), mp.mpf(lam)); M[a,b]=v; M[b,a]=v
    E, V = mp.eigsy(M)
    order = sorted(range(dim), key=lambda j: E[j])
    eg = [float(E[order[k]]/E[order[0]]) for k in range(6)]
    print(f"\nlambda={lam} N={N} dim={dim} L={L:.4f}  ratios={[round(x,3) for x in eg]}")

    # reconstruir f_k(y) en grilla
    Ny = 600; ys = np.linspace(0, L, Ny)
    def recon(k):
        c = np.array([float(V[i, order[k]]) for i in range(dim)])
        # f(y)=sum c_n e^{2pi i n y/L}; tomar parte real/imag dominante
        fr = np.zeros(Ny); fi = np.zeros(Ny)
        for i, n in enumerate(idx):
            ph = 2*np.pi*n*ys/L
            fr += c[i]*np.cos(ph); fi += c[i]*np.sin(ph)
        f = fr if np.max(np.abs(fr)) >= np.max(np.abs(fi)) else fi
        return f
    f = [recon(k) for k in range(5)]
    # signo: f_0 > 0 en el centro
    for k in range(5):
        if abs(f[k][Ny//2]) > 1e-6 and f[k][Ny//2] < 0 and k == 0: f[k] = -f[k]

    # bulk: donde |f_0| es grande
    a0 = np.max(np.abs(f[0]))
    bulk = np.abs(f[0]) > 0.20*a0
    yb = ys[bulk]
    # (T1) cos theta propto f_1/f_0 lineal en y
    ratio10 = f[1][bulk]/f[0][bulk]
    A = np.vstack([yb, np.ones_like(yb)]).T
    coef, *_ = np.linalg.lstsq(A, ratio10, rcond=None)
    fit = A@coef; resid = np.std(ratio10-fit)/(np.std(ratio10)+1e-12)
    print(f" (T1) f1/f0 vs y  LINEAL: pendiente={coef[0]:.4f} resid_rel={resid:.4f}")

    # (T2') theta EXTRAIDO de f1/f0 (sin asumir linealidad): cos theta = (f1/f0)/rho
    rho = np.max(np.abs(ratio10))
    costh_emp = np.clip(ratio10/rho, -1, 1)
    print(" (T2') Dirichlet-plano en theta EMPIRICO (cos theta = (f1/f0)/rho):")
    for k in range(2, 5):
        target = f[k][bulk]/f[0][bulk]
        model = chebyU(k, costh_emp)
        sc = np.sum(target*model)/np.sum(model*model)
        r = np.std(target - sc*model)/(np.std(target)+1e-12)
        cc = np.corrcoef(target, model)[0,1]
        print(f"   k={k}: corr={cc:+.4f} resid_rel={r:.4f}")
    # (T1') es theta(y) tal que cos theta lineal en y? cos theta_emp vs y
    th_emp = np.arccos(costh_emp)
    A2 = np.vstack([yb, np.ones_like(yb)]).T
    cf2, *_ = np.linalg.lstsq(A2, costh_emp, rcond=None)
    rr = np.std(costh_emp - A2@cf2)/(np.std(costh_emp)+1e-12)
    print(f" (T1') cos(theta_emp) vs y lineal: resid_rel={rr:.4f} pend={cf2[0]:.4f}")
    # (T1'') es THETA(y) afin en y?  theta_emp vs y lineal -> entonces QW|bulk=-d_y^2 Dirichlet
    cf3, *_ = np.linalg.lstsq(A2, th_emp, rcond=None)
    rr3 = np.std(th_emp - A2@cf3)/(np.std(th_emp)+1e-12)
    # ancho efectivo: theta va 0..pi -> W=pi/|pend|
    Weff = np.pi/abs(cf3[0])
    print(f" (T1'') theta_emp vs y LINEAL (=> -d_y^2 Dirichlet): resid_rel={rr3:.4f} pend={cf3[0]:.4f} W_eff={Weff:.3f} margen=(L-W)/2={(L-Weff)/2:.3f}")
    center = (yb.min()+yb.max())/2; halfw = (yb.max()-yb.min())/2
    margin = (L - (yb.max()-yb.min()))/2; a_slope = abs(cf2[0])
    print(f"   ESCALAS: centro={center:.3f}(L/2={L/2:.3f}) semiancho={halfw:.3f} MARGEN={margin:.3f} a={a_slope:.4f} a*L={a_slope*L:.3f}")
    print(f"            hipotesis margen~const: a=2/(L-2m), 2/(L-2*0.75)={2/(L-1.5):.4f}")

for lm, NN in [(7.0,14),(9.0,16),(11.0,18),(13.0,21)]:
    run(lm, NN)
