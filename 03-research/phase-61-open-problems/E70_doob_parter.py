"""
P2 del plan 2.3.F-CLOSE. Test DECISIVO de separabilidad forma/signo.

Idea: Doob-conjugar QW_lambda por su estado base u_0>0. La forma cociente de Doob
  G(v) = A(u_0 v, u_0 v) - eps_0 ||u_0 v||^2     (PSD, nucleo = constantes)
es self-adjoint respecto del peso w(y)=u_0(y)^2, autovalores e_k = eps_k - eps_0,
autofunciones v_k = f_k/u_0. Si G es un operador LOCAL de 2do orden (Sturm-Liouville)
   G v = -(1/w) (C w v')'  con C(y) ~ const,
entonces por Parter(2.3.B)+Doob(2.3.A)+Dirichlet-BC(2.3.F-Box) los ratios son (k+1)^2.

TEST: extraer C(y) del modo MAS BAJO v_1 via
   C(y) w(y) v_1'(y) = -e_1 \int_0^y w v_1            (de (C w v_1')' = -e_1 w v_1)
y verificar:
  (A) C(y) es PLANO (constante) en el bulk  -> LOCAL 2do orden.
  (B) cross-validacion: el MISMO C(y) reproduce e_2,e_3 con ratios (k+1)^2 (Parter).
  (C) separar ARCH vs PRIME: que C tiene cada termino (cual aporta la localidad).
  (D) falsador DH: C NO debe aplanar / cross-validar.
Si (A)+(B) pasan -> 2.3.F-Loc validado (la forma se separa del signo). Si C oscila
(Kronecker) o el mode-2 pide otro C -> wall-equivalente (forma != signo).
"""
import numpy as np, mpmath as mp
mp.mp.dps = 40
GAMMA = mp.euler; LOG4PI = mp.log(4*mp.pi); LOG5 = mp.log(5)

# ---- engine QW_entry (de E22), con kind para falsador DH ----
def q_func(m, n, L):
    if m == n: return lambda y: 2*(1-y/L)*mp.cos(2*mp.pi*n*y/L)
    c = 1/(mp.pi*(n-m))
    return lambda y: (mp.sin(2*mp.pi*m*y/L)-mp.sin(2*mp.pi*n*y/L))*c

def parts_entry(m, n, L, lam, kind='zeta'):
    """devuelve (ARCH, PRIME) por separado.  A = ARCH - PRIME."""
    q = q_func(m, n, L); q0 = q(mp.mpf(0))
    even = (kind == 'zeta')
    W02 = mp.quad(lambda y: q(y)*(mp.e**(y/2)+mp.e**(-y/2)), [0, L])
    def wr(y):
        if y < mp.mpf('1e-12'):
            h = mp.mpf('1e-8'); return ((q(h)-q0)/h+q0/2)/2
        return (mp.e**(y/2)*q(y)-q0)/(2*mp.sinh(y))
    C = LOG4PI + GAMMA + (0 if even else LOG5)
    WR = C*q0/2 + mp.quad(wr, [0, L]) + q0*mp.log(mp.tanh(L/2))/2
    ARCH = W02 - WR
    # primos: zeta = Lambda(n); DH = Lambda con chi(n) modulado (5-adic) -> usamos arith con signo
    arith = mp.mpf(0); mx = int(lam*lam); sv = [True]*(mx+1)
    for i in range(2, int(mx**0.5)+1):
        if sv[i]:
            for j in range(i*i, mx+1, i): sv[j] = False
    for p in range(2, mx+1):
        if sv[p]:
            lp = mp.log(p); pm = p; me = 1
            while pm <= mx:
                w = lp*(mp.mpf(pm)**mp.mpf('-0.5'))
                if kind == 'DH':
                    # Davenport-Heilbronn: factor con chi mod 5 (caracter no principal) sobre el primo base
                    chi = {1:1,2:1,3:-1,4:-1,0:0}[p % 5]
                    w = w*chi
                arith += w*q(me*lp); pm *= p; me += 1
    return ARCH, arith

def build(lam, N, kind='zeta'):
    L = float(2*mp.log(mp.mpf(lam))); dim = 2*N+1; idx = list(range(-N, N+1))
    Larch = mp.zeros(dim); Lpr = mp.zeros(dim)
    Lm = 2*mp.log(mp.mpf(lam))
    for a in range(dim):
        for b in range(a, dim):
            ar, pr = parts_entry(idx[a], idx[b], Lm, mp.mpf(lam), kind)
            Larch[a,b]=ar; Larch[b,a]=ar; Lpr[a,b]=pr; Lpr[b,a]=pr
    A = Larch - Lpr
    return A, Larch, Lpr, L, idx

def recon_grid(coef, idx, L, Ny=1200):
    ys = np.linspace(0, L, Ny)
    fr = np.zeros(Ny); fi = np.zeros(Ny)
    for i, n in enumerate(idx):
        ph = 2*np.pi*n*ys/L
        fr += coef[i]*np.cos(ph); fi += coef[i]*np.sin(ph)
    f = fr if np.max(np.abs(fr)) >= np.max(np.abs(fi)) else fi
    return ys, f

def extract_C(ys, w, v1, e1, bulk):
    """C(y) w v1' = -e1 cumint(w v1).  Devuelve C(y) en bulk."""
    dy = ys[1]-ys[0]
    v1p = np.gradient(v1, dy)
    integ = np.concatenate([[0], np.cumsum(0.5*(w[1:]*v1[1:]+w[:-1]*v1[:-1])*dy)])
    # constante de integracion: el flujo C w v1' debe anularse en el centro del bulk por simetria?
    # mejor: ajustar offset para que C sea mas plano (minimiza no usado); usamos integ cruda.
    num = -e1*integ
    den = w*v1p
    C = np.where(np.abs(den) > 1e-9*np.max(np.abs(den)), num/den, np.nan)
    return C

def run(lam, N, kind='zeta'):
    A, Larch, Lpr, L, idx = build(lam, N, kind)
    dim = len(idx)
    E, V = mp.eigsy(A)
    order = sorted(range(dim), key=lambda j: E[j])
    eps = [float(E[order[k]]) for k in range(6)]
    ratios = [eps[k]/eps[0] for k in range(6)]
    print(f"\n{'='*64}\n{kind}  lambda={lam} N={N} L={L:.4f}")
    print(f"  eps_k = {[f'{e:.3e}' for e in eps[:4]]}")
    print(f"  ratios eps_k/eps_0 = {[round(r,3) for r in ratios]}  (target (k+1)^2=1,4,9,16,25)")

    # estado base y modos en grilla
    def gridmode(k):
        c = np.array([float(V[i, order[k]]) for i in range(dim)])
        ys, f = recon_grid(c, idx, L)
        return ys, f
    ys, u0 = gridmode(0)
    Ny = len(ys);
    if u0[Ny//2] < 0: u0 = -u0
    w = u0**2
    a0 = np.max(np.abs(u0)); bulk = np.abs(u0) > 0.20*a0
    yb = ys[bulk]

    fk = []
    for k in range(1, 4):
        _, f = gridmode(k); fk.append(f)
    # v_k = f_k/u0
    eps0 = eps[0]
    print(f"  bulk: y in [{yb.min():.3f},{yb.max():.3f}]  (L={L:.3f})")

    # (A) extraer C(y) del modo 1.  C lleva la escala rho_lambda~e^{-cL}~1e-20 (Parter tau_N);
    #     lo que importa es la FORMA: C(y)/mean(C) debe ser ~1 (plano) en el bulk.
    e1 = eps[1]-eps[0]
    v1 = np.where(np.abs(u0) > 1e-9*a0, fk[0]/np.where(np.abs(u0)>1e-12,u0,1e-12), 0.0)
    C = extract_C(ys, w, v1, e1, bulk)
    inner = (np.abs(u0) > 0.45*a0)
    Ci = C[inner]; Ci = Ci[np.isfinite(Ci)]
    if len(Ci) > 5:
        cstar = np.mean(Ci)
        flat = np.std(Ci)/(abs(cstar)+1e-300)
        # perfil normalizado en 5 puntos del bulk interior
        yin = ys[inner]; prof = (C[inner]/cstar)
        sel = np.linspace(0, len(yin)-1, 5).astype(int)
        prof5 = [f"{yin[s]:.2f}:{prof[s]:+.2f}" for s in sel]
        print(f"  (A) C(y) modo-1 (escala~{cstar:+.2e}): FORMA C(y)/mean en bulk = {prof5}")
        print(f"      std/|mean|={flat:.3f}  => {'PLANO (local 2do orden)' if flat<0.25 else 'NO plano (oscila / no-local)'}")
    else:
        cstar = np.nan; print("  (A) C no extraible")

    # (B) cross-validacion: con C=cstar constante, el operador -1/w (cstar w v')' debe dar
    #     e_k con ratios (k+1)^2-1 (Doob). Equivale a: Rayleigh de v_k con forma cstar∫w v'^2
    #     dividido por ∫ w v^2  ->  debe ~ e_k. Test ratio e_k/e_1 vs (k+1)^2-1 over 3.
    def rayleigh(vv):
        dy = ys[1]-ys[0]; vp = np.gradient(vv, dy)
        numr = np.trapz((w*vp**2)[bulk], yb)
        den = np.trapz((w*vv**2)[bulk], yb)
        return numr/den
    if np.isfinite(cstar):
        print(f"  (B) cross-val (Rayleigh local con w=u0^2):")
        R = []
        for k in range(1,4):
            vk = np.where(np.abs(u0)>1e-9*a0, fk[k-1]/np.where(np.abs(u0)>1e-12,u0,1e-12),0.0)
            Rk = cstar*rayleigh(vk); R.append(Rk)
            ek = eps[k]-eps[0]
            print(f"      k={k}: R_local={Rk:+.4e}  e_k=eps_k-eps_0={ek:+.4e}  R/e={Rk/ek if ek!=0 else float('nan'):.3f}")
        if R[0]!=0:
            rr = [r/R[0] for r in R]
            tgt = [( (k+2)**2-1)/(3) for k in range(3)]  # (k+1)^2-1 normalizado, k=1->3
            print(f"      ratios R_k/R_1 = {[round(x,3) for x in rr]}  target (Doob k(k+2)) = {[round(t,3) for t in tgt]}")

    # (C) balance ARCH/PRIME via coeficientes EXACTOS del autovector (sin grilla):
    #     u0 v_k = f_k = autovector c_k. ARCH_k=<c_k|Larch|c_k>, PRIME_k=<c_k|Lpr|c_k>,
    #     ARCH_k - PRIME_k = eps_k (eigenvalor). Muestra la balanza (E24) y que la energia
    #     LOCAL (k+1)^2 vive en el residuo e^{-cL} de ARCH=PRIME.
    print(f"  (C) balance ARCH=PRIME (coef exactos), residuo = energia local (k+1)^2:")
    for k in range(0,4):
        ck = mp.matrix([V[i, order[k]] for i in range(dim)])
        ar = float((ck.T*Larch*ck)[0]); pr = float((ck.T*Lpr*ck)[0])
        print(f"      k={k}: ARCH={ar:+.5f}  PRIME={pr:+.5f}  ARCH-PRIME={ar-pr:+.3e}  (=eps_k={eps[k]:+.3e})")

# ---- ejecutar: zeta a varios lambda + falsador DH ----
for lm, NN in [(7.0,14),(9.0,16),(11.0,18)]:
    run(lm, NN, 'zeta')
run(7.0, 14, 'DH')
