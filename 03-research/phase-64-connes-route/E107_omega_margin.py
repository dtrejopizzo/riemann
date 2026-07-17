"""
E107 — probing the omega->0 continuation margin (RH-strength question).

E104/E106: zeta's passivity is marginal but genuine; the absolute Pick min-eig -> 0 as omega->0.
The RH-strength question (Connes' regularized continuation): does a REGULARIZED margin survive the
limit omega->0 as a positive quantity, and is its sign the local RH statement?

Hypothesis from the audit: the RELATIVE margin r(omega) = min_eig / max_eig of the Pick matrix is
nearly omega-independent for zeta (a scale-invariant positive number) -> the regularized positivity
survives omega=0. For an off-line zero at beta, r(omega) must cross 0 at omega = beta-1/2.

Tests (high precision dps=40):
  (1) zeta: r(omega) on a fine omega grid down to 0.002. Does it -> a positive constant? scaling?
  (2) near-line off-line zero beta=0.55 (threshold omega*=0.05): does r cross 0 exactly at 0.05?
  (3) the "regularized margin" R := lim_{omega->0} r(omega) -- estimate it for zeta.
This isolates whether the continuation is forced (R>0 structurally) or merely observed.
"""
import mpmath as mp
mp.mp.dps = 40


def xi(s):
    return mp.mpf('0.5') * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def xi_off_factor(s, betas):
    f = mp.mpf(1)
    for (b, g0) in betas:
        for s0 in (mp.mpf(b)+1j*mp.mpf(g0), mp.mpf(b)-1j*mp.mpf(g0),
                   (1-mp.mpf(b))+1j*mp.mpf(g0), (1-mp.mpf(b))-1j*mp.mpf(g0)):
            f *= (s - s0)
    return f


def Theta(omega, z, betas=None):
    sp = mp.mpf('0.5') + omega + 1j*z; sm = mp.mpf('0.5') + omega - 1j*z
    num = xi(sp); den = xi(sm)
    if betas:
        num *= xi_off_factor(sp, betas); den *= xi_off_factor(sm, betas)
    return num/den


def pick_relmargin(omega, pts, betas=None):
    n = len(pts); Th = [Theta(omega, z, betas) for z in pts]
    R = mp.zeros(2*n)
    for i in range(n):
        for j in range(n):
            v = (1 - Th[i]*mp.conj(Th[j]))/(2*mp.pi*1j*(mp.conj(pts[j]) - pts[i]))
            re, im = mp.re(v), mp.im(v)
            R[i, j] = re; R[n+i, n+j] = re; R[i, n+j] = -im; R[n+i, j] = im
    R = (R+R.T)/2
    E, _ = mp.eigsy(R); ev = [float(E[k]) for k in range(2*n)]
    mn, mx = min(ev), max(ev)
    return mn, mx, mn/mx


if __name__ == '__main__':
    gammas = [14.134725, 21.022040, 25.010858, 30.424876]
    pts = [mp.mpf(g) + 1j*mp.mpf(y) for g in gammas for y in ('0.3', '0.8')]
    omegas = [mp.mpf(s) for s in ['0.5','0.3','0.2','0.1','0.05','0.02','0.01','0.005','0.002']]

    print("E107 — omega->0 continuation margin (dps=40). r = min/max eig of Pick matrix.\n")
    print("(1) zeta: relative margin r(omega) -- does it -> positive constant?")
    print(f"   {'omega':>7} {'min eig':>13} {'max eig':>11} {'r=min/max':>13}")
    rs = []
    for om in omegas:
        mn, mx, r = pick_relmargin(om, pts)
        rs.append((float(om), r))
        print(f"   {float(om):7.3f} {mn:13.3e} {mx:11.3e} {r:13.3e}")
    # is r converging to a constant? report last few
    tail = [r for (o, r) in rs if o <= 0.05]
    print(f"   tail r (omega<=0.05): {[f'{x:.3e}' for x in tail]}")
    print(f"   => regularized margin R = lim r ~ {sum(tail)/len(tail):.3e}  "
          f"({'POSITIVE & stable => survives omega=0' if min(tail) > 0 else 'not stable'})")

    print("\n(2) near-line off-line zero beta=0.55 (predicted threshold omega*=0.05):")
    print(f"   {'omega':>7} {'r=min/max':>13}")
    for om in omegas:
        mn, mx, r = pick_relmargin(om, pts, betas=[(0.55, 22.0)])
        print(f"   {float(om):7.3f} {r:13.3e}  {'PSD' if r > -1e-20 else 'NEG (off-line pole in UHP)'}")
    print("   => sign should flip near omega=0.05 = beta-1/2.")
