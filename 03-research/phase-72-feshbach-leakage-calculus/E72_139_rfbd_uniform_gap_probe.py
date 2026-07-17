#!/usr/bin/env python3
# ======================================================================================
# E72.139 -- RFBD uniform-gap test: does eta_H stay < 1 as L grows, or -> 1 (MW-6 disguise)?
#
# RFBD (E72.138):  eta_H(x) = sup_v (-<v,Delta_arith v>)_+ / <v,C_model v>  <= eta_H < 1.
# Equivalently theta_H(x) = 1 - eta_H(x) = lambda_min(C_model^{-1/2} C_actual C_model^{-1/2}).
#
# The whole closure rests on eta_H < 1 UNIFORMLY in L (and x). This is the same discipline that
# separated "detector" from "proof" in every prior phase: does the relative margin have a UNIFORM
# GAP below 1, or does it degrade to the marginal MW-6 / MW-1 wall as L grows?
#
# DECISIVE:
#   * if theta_H(L) stabilizes at a positive floor (eta_H bounded < 1) as L grows -> RFBD is a
#     genuine coercivity gap, provable from the arithmetic structure, NOT MW-1/MW-6.
#   * if theta_H(L) -> 0 (eta_H -> 1) -> RFBD is marginal = the wall in Feshbach clothing.
#
# Also decomposes the numerator: measure the NEGATIVE-part energy of Delta_arith and the model
# floor separately, to see their L-scaling (the honest arithmetic content of RFBD).
# ======================================================================================
import sys
import numpy as np
from numpy.linalg import cholesky, eigvalsh, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402


def generalized_min(a, b):
    """min generalized eigenvalue of a v = lam b v (b>0): = lambda_min(b^{-1/2} a b^{-1/2})."""
    ch = cholesky(b)
    x = solve(ch, a)
    rel = solve(ch, x.T).T
    rel = 0.5 * (rel + rel.T)
    return eigvalsh(rel)


def neg_part_energy(delta, cmodel):
    """largest ratio (-<v,delta v>)_+ / <v,cmodel v>  = -min generalized eig of delta rel cmodel,
    clipped at 0. This is exactly eta_H."""
    ge = generalized_min(delta, cmodel)
    return max(0.0, -ge[0]), ge


def run():
    print("E72.139 RFBD uniform-gap probe")
    print(" lam    L    theta_H=minGen   eta_H=1-theta   modelFloor/L   ||Delta||/L   negEnergy(eta)")
    rows = []
    for lam, n_modes in [(8, 24), (12, 30), (16, 38), (20, 46), (24, 54), (30, 66), (36, 78)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        delta = c_actual - c_model
        theta = generalized_min(c_actual, c_model)[0]
        eta = 1.0 - theta
        eta2, _ = neg_part_energy(delta, c_model)   # should equal eta when theta<1
        model_floor = eigvalsh(c_model)[0] / L
        dnorm = np.linalg.norm(delta, 2) / L
        print(f"{lam:4.0f} {L:6.3f} {theta:14.4f} {eta:14.4f} {model_floor:14.4f} "
              f"{dnorm:12.4f} {eta2:14.4f}")
        rows.append((L, theta, eta, model_floor, dnorm))
    rows = np.array(rows)
    print("\n" + "=" * 78)
    print(" TREND ANALYSIS")
    Ls, thetas, etas = rows[:, 0], rows[:, 1], rows[:, 2]
    # linear fit theta vs L
    A = np.polyfit(Ls, thetas, 1)
    print(f"  theta_H vs L: slope={A[0]:+.4f}  intercept={A[1]:+.4f}")
    print(f"  theta_H range: [{thetas.min():.4f}, {thetas.max():.4f}]  (eta in [{etas.min():.4f},{etas.max():.4f}])")
    # log-log of eta gap to 1? check if theta decays toward 0
    if thetas.min() > 0.15 and abs(A[0]) < 0.02:
        print("  -> theta_H STABILIZES at a positive floor: RFBD looks like a GENUINE uniform gap.")
    elif A[0] < -0.01:
        print("  -> theta_H DECAYS with L: RFBD margin degrades -> marginal wall risk (MW-6).")
    else:
        print("  -> inconclusive over this range; extend L.")
    print("=" * 78)


if __name__ == "__main__":
    run()
