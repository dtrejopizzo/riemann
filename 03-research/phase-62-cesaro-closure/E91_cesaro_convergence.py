"""
E91 — CESARO CONVERGENCE CURVE of the intrinsic-Jacobi band width (Phase 62, step C1 evidence).

C0 (E90) established the qualitative split: zeta's bulk band width b_bulk(lambda) is BOUNDED,
DH's GROWS. C1's analytic target is to prove b_bulk(lambda) = b_smooth + b_osc where
  - b_smooth(lambda) -> const  (prime side, controlled by PNT: a bounded integral term)
  - (1/Lambda) sum_{lam<=Lambda} b_osc(lambda) -> 0  (zero side, by UNCONDITIONAL zero density)

This script supplies the numerical frame for that claim on a DENSE lambda grid:
  (1) the running Cesaro mean  Bbar(Lambda) = mean_{lam<=Lambda} b_bulk(lambda)
  (2) the fluctuation  f(Lambda) = b_bulk(Lambda) - Bbar(Lambda)  and its envelope decay
  (3) zeta: Bbar flattens, fluctuation envelope shrinks (consistent ~1/log)
      DH  : Bbar diverges (b grows ~linearly) -> Cesaro does NOT converge (falsador)

It does NOT prove C1; it tells us the analytic target (bounded smooth + averaging zero-sum)
is the right one and what decay rate to expect. Honesty: dps>=40, DH mandatory, no proof claimed.
"""
import sys, numpy as np
import E90_cesaro_jacobi as e90  # reuses jacobi_for, lanczos, engine path shim


def b_bulk(lam, N, kind):
    a, b = e90.jacobi_for(lam, N, kind)
    b = np.array(b)
    return float(np.mean(b[2:-2]))


def Nfor(lam):
    """N schedule matching the cached dps=50 builds (resolves the band as L=2 log lam grows)."""
    if lam <= 7:  return 14
    if lam <= 9:  return 16
    if lam <= 13: return 18
    if lam <= 17: return 20
    return 22


def run(grid, kind):
    print(f"\n{'='*72}\nKIND = {kind}")
    lams = [g for g in grid]
    bs = []
    print(f"  {'lam':>5} {'N':>3} {'b_bulk':>9} {'Bbar(cesaro)':>13} {'fluct':>10}")
    for lam in lams:
        N = Nfor(lam)
        bb = b_bulk(lam, N, kind)
        bs.append(bb)
        Bbar = np.mean(bs)
        print(f"  {lam:5.1f} {N:3d} {bb:9.4f} {Bbar:13.5f} {bb-Bbar:10.4f}")
    bs = np.array(bs)
    # Cesaro running mean and its successive movement (does it settle?)
    Bbar_seq = np.array([np.mean(bs[:i+1]) for i in range(len(bs))])
    settle = [abs(Bbar_seq[i]-Bbar_seq[i-1]) for i in range(1, len(Bbar_seq))]
    # trend of b itself: linear-fit slope (DH should be >>0, zeta ~0)
    slope = np.polyfit(lams, bs, 1)[0]
    # fluctuation envelope over 2nd half
    h = len(bs)//2
    env = np.std(bs[h:])
    print(f"  slope(b vs lam) = {slope:+.4f}   (zeta ~0 bounded; DH >0 growing)")
    print(f"  last Cesaro step |dBbar| = {settle[-1]:.3e}   2nd-half std(b) = {env:.4f}")
    return lams, bs, Bbar_seq, slope


if __name__ == '__main__':
    # dense integer grid; intermediate lams trigger new dps=50 builds (cached to .cache_23F)
    grid = list(range(7, 23))  # 7..22
    if len(sys.argv) > 1:
        grid = eval(sys.argv[1])
    print("E91 — Cesaro convergence of b_bulk(lambda): zeta should flatten, DH should diverge")
    lz, bz, Bz, sz = run(grid, 'zeta')
    ld, bd, Bd, sd = run(grid, 'DH')
    print(f"\n{'='*72}\nVERDICT (C1 numerical frame)")
    print(f"  zeta slope = {sz:+.4f}  Cesaro-> {Bz[-1]:.4f}")
    print(f"  DH   slope = {sd:+.4f}  Cesaro-> {Bd[-1]:.4f}")
    ok = abs(sz) < 0.02 and sd > 0.04
    print(f"  => {'BOUNDED zeta vs GROWING DH confirmed on dense grid' if ok else 'inconclusive — inspect'}")
