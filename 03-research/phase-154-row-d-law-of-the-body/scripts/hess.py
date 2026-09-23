"""R154 script 3: (B1) exact Hessian of lambda(v) at w_zeta, apex prediction; (B2) T-scan for kinks."""
import math, sys, numpy as np, scipy.linalg as sla
sys.path.insert(0, '/home/trabajo/Documentos/research/riemann/03-research/phase-153-row-d-sign-carrying-endpoint/scripts/round6')
import core

def hessian(T, Kdim, contacts):
    v = {n: 2*core.wgt(n) for n in contacts}
    B = core.Body(T, Kdim, contacts=contacts)
    M = B.op(1.0, {n: -v[n] for n in contacts})
    w, V = sla.eigh(M, B.G)
    R = np.linalg.cholesky(B.G)
    # orthonormalise in the G metric: V columns already G-orthonormal from eigh(M,G)
    lam = w[0]; f = V[:, 0]
    x = {n: float(f @ B.Mn[n] @ f) for n in contacts}
    grad = np.array([-x[n] for n in contacts])
    H = np.zeros((len(contacts), len(contacts)))
    for i, n in enumerate(contacts):
        for j, mnt in enumerate(contacts):
            s = 0.0
            for k in range(1, len(w)):
                s += (f @ B.Mn[n] @ V[:, k])*(f @ B.Mn[mnt] @ V[:, k])/(lam - w[k])
            H[i, j] = 2*s
    return lam, x, grad, H, v

for Kdim in (240, 320):
    lam, x, g, H, v = hessian(math.log(2), Kdim, [2, 3])
    print(f"K={Kdim} lambda={lam:.8e} x={ {k: round(val,7) for k,val in x.items()} }")
    print("  grad =", np.round(g, 7), " Hessian =\n", H)
    ev = np.linalg.eigvalsh(H); print("  Hessian eigenvalues:", ev)
    # apex: max delta_2 with lam + g.d + 0.5 d'Hd = 0  (H neg def)
    # Lagrange: e2 = mu (g + H d); d = H^{-1}(e2/mu - g)
    Hi = np.linalg.inv(H); e2 = np.array([1.0, 0.0])
    a = e2 @ Hi @ e2; b = e2 @ Hi @ g; c = g @ Hi @ g
    # lam + g'd + .5 d'Hd  with d = Hi(e2/mu - g):
    # = lam + (b/mu - c) + .5(a/mu^2 - 2b/mu + c) = lam + .5 a/mu^2 - .5 c
    # set = 0 -> mu^2 = .5a/(.5c - lam)
    mu2 = 0.5*a/(0.5*c - lam); mu = math.sqrt(mu2)*(1 if a > 0 else -1)
    for s in (+1, -1):
        mu = s*math.sqrt(abs(mu2))
        d = Hi @ (e2/mu - g)
        print(f"   apex branch mu={mu: .4f}: delta=({d[0]:+.3e},{d[1]:+.3e})  v2*={v[2]+d[0]:.7f} v3={v[3]+d[1]:.7f}")
    print("   first-order-only apex offset (delta2 with H=0 impossible); linear estimate lam/x2 =", lam/x[2])
