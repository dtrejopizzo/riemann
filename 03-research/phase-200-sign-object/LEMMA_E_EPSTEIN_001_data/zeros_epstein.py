"""LEMMA_E_EPSTEIN_001 (NUMERICO): zeros of Z_Q, Q=x^2+5y^2, via Z_Q = zeta*L(chi_-20) + L(chi_-4)L(chi_5).
Checks: identity against direct lattice sum at s=2.5; FE Lambda_Q(s)=Lambda_Q(1-s); residue pi/sqrt5; Z_Q(0)=-1.
Search: Newton from a grid in 1/2<sigma<1.6, 0<t<TMAX for off-line zeros; counts on-line zeros via Hardy-type phase."""
import mpmath as mp, sys
mp.mp.dps = 30
def kr(D, n):
    from sympy import jacobi_symbol
    from sympy.ntheory import factorint
    r = 1
    for p, e in factorint(n).items():
        v = (0 if D % 2 == 0 else (1 if D % 8 in (1, 7) else -1)) if p == 2 else (jacobi_symbol(D % p, p) if D % p else 0)
        r *= v ** e
    return r
ch = {D: [kr(D, n) if n else 0 for n in range(abs(D))] for D in (-20, -4, 5)}
L = lambda s, D: mp.dirichlet(s, ch[D])
Z = lambda s: mp.zeta(s) * L(s, -20) + L(s, -4) * L(s, 5)
Lam = lambda s: (mp.sqrt(20) / (2 * mp.pi)) ** s * mp.gamma(s) * Z(s)
if __name__ == '__main__':
    s = mp.mpf('2.5'); M = 60
    direct = mp.fsum((x * x + 5 * y * y) ** (-s) for x in range(-M, M + 1) for y in range(-M, M + 1) if (x, y) != (0, 0))
    print('Z_Q(2.5) identity', mp.nstr(Z(s), 15), 'lattice(|x|,|y|<=60)', mp.nstr(direct, 15))
    s = mp.mpc('0.3', '7.1'); print('FE check |Lam(s)-Lam(1-s)|', mp.nstr(abs(Lam(s) - Lam(1 - s)), 5))
    e = mp.mpf('1e-12'); print('residue', mp.nstr(Z(1 + e) * e, 12), 'pi/sqrt5', mp.nstr(mp.pi / mp.sqrt(5), 12), 'Z_Q(0)', mp.nstr(Z(0), 12))
    TMAX = float(sys.argv[1]) if len(sys.argv) > 1 else 60
    found = []
    t = 0.5
    while t < TMAX:
        for sg in (0.6, 0.75, 0.9, 1.05, 1.2):
            try:
                r = mp.findroot(Z, mp.mpc(sg, t), tol=1e-25, maxsteps=60)
            except Exception: continue
            if r.real > 0.5 + 1e-8 and r.imag > 0 and abs(Z(r)) < 1e-15 and not any(abs(r - f) < 1e-8 for f in found):
                found.append(r); print('OFF-LINE zero', mp.nstr(r, 15), flush=True)
        t += 0.5
    print('off-line zeros with Re s>1/2, 0<t<%g:' % TMAX, [mp.nstr(r, 10) for r in sorted(found, key=lambda z: z.imag)])
    # first on-line zeros (sign changes of Lam(1/2+it), which is real)
    on = []; prev = mp.re(Lam(mp.mpc(0.5, 0.05))); tt = 0.05
    while tt < 25:
        tt += 0.02; v = mp.re(Lam(mp.mpc(0.5, tt)))
        if v * prev < 0: on.append(mp.findroot(lambda u: mp.re(Lam(mp.mpc(0.5, u))), tt - 0.01))
        prev = v
    print('on-line zeros 0<t<25:', [mp.nstr(x, 8) for x in on])
