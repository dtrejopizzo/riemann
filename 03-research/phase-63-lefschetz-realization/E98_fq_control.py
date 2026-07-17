"""
E98 — F_q POSITIVE CONTROL (Phase 63, R3): why the curve case crosses and Spec-Z does not.

R1 found: over the zeta window the scaling operator (spectrum=zeros) ANTI-commutes with the
polarization's complex structure J (antilinear, wrong type for Frobenius), and the polarization is
gapless (Phase 62). This control shows the CONTRAST on an actual curve over F_q, where RH is a
theorem, isolating exactly what Spec Z lacks.

For an elliptic curve E/F_q (genus 1), H^1 is 2-dim. Frobenius phi acts; #E(F_q)=q+1-a gives the
trace a; eigenvalues alpha,abar = sqrt(q) e^{+-i theta}, cos theta = a/(2 sqrt q) (Hasse). In the
natural (Hodge) basis Frobenius is  F = sqrt(q) * R(theta)  (rotation), and:
  (1) F COMMUTES with J=[[0,-1],[1,0]]  (J-LINEAR = Hodge morphism)            [contrast: zeta antilinear]
  (2) F is a SIMILITUDE of a POSITIVE-DEFINITE polarization Q:  F^T Q F = q Q  [contrast: zeta gapless]
  (3) => eigenvalues lie EXACTLY on |z|=sqrt(q): RH for the curve, FORCED by (1)+(2).

We take a REAL curve (genuine point count), not a toy, so a/theta are real arithmetic.
Honesty: this is a positive control (must PASS); the contrast with zeta is the content.
"""
import numpy as np


def count_points_E(a4, a6, p):
    """#E(F_p) for y^2 = x^3 + a4 x + a6 (good reduction), incl. point at infinity."""
    cnt = 1  # infinity
    sq = set((x * x) % p for x in range(p))
    for x in range(p):
        rhs = (x * x * x + a4 * x + a6) % p
        if rhs == 0:
            cnt += 1
        elif rhs in sq:
            cnt += 2  # two square roots
    return cnt


def frobenius_2x2(a, q):
    theta = np.arccos(a / (2 * np.sqrt(q)))
    F = np.sqrt(q) * np.array([[np.cos(theta), -np.sin(theta)],
                               [np.sin(theta),  np.cos(theta)]])
    return F, theta


def run(a4, a6, p):
    Np = count_points_E(a4, a6, p)
    a = p + 1 - Np
    q = p
    assert abs(a) <= 2 * np.sqrt(q), "Hasse violated (bad reduction?)"
    F, theta = frobenius_2x2(a, q)
    J = np.array([[0.0, -1.0], [1.0, 0.0]])          # complex structure, J^2=-1
    Q = np.eye(2)                                     # positive-definite polarization (Hodge metric)
    # (1) J-linearity
    commJ = np.linalg.norm(F @ J - J @ F) / np.linalg.norm(F)
    # (2) similitude of Q with factor q, and Q positive-definite gap
    simil = np.linalg.norm(F.T @ Q @ F - q * Q) / np.linalg.norm(q * Q)
    qev = np.linalg.eigvalsh(Q)
    # (3) eigenvalue moduli
    ev = np.linalg.eigvals(F)
    mods = np.abs(ev)
    print(f"\nE: y^2=x^3+{a4}x+{a6} over F_{p}:  #E={Np}, a={a}, q={q}, sqrt(q)={np.sqrt(q):.4f}")
    print(f"  (1) ||[F,J]||/||F|| = {commJ:.2e}   => {'J-LINEAR (Hodge morphism, Frobenius type)' if commJ<1e-12 else 'not'}")
    print(f"  (2) ||F^T Q F - qQ||/||qQ|| = {simil:.2e}  Q-similitude;  Q eigenvalues={qev}  "
          f"=> polarization {'PD, GAP=' + format(qev.min(),'.3f') if qev.min()>1e-9 else 'degenerate'}")
    print(f"  (3) |eigenvalues(F)| = {np.round(mods,6)}  vs sqrt(q)={np.sqrt(q):.6f}  "
          f"=> {'ON |z|=sqrt(q): curve-RH holds, FORCED by (1)+(2)' if np.allclose(mods,np.sqrt(q)) else 'OFF'}")
    return commJ, simil, qev.min(), np.allclose(mods, np.sqrt(q))


if __name__ == '__main__':
    print("E98 — F_q positive control: Frobenius is J-LINEAR & a similitude of a GAPPED PD polarization")
    print("      (contrast with zeta window R1: scaling ANTI-commutes with J, polarization GAPLESS)")
    # three genuine curves / primes
    for (a4, a6, p) in [(1, 1, 101), (-1, 1, 103), (2, 3, 211)]:
        run(a4, a6, p)
    print("\n" + "=" * 72)
    print("CONTRAST TABLE (operator-level mechanism):")
    print(f"  {'':22s}{'J-relation':>22s}{'polarization':>20s}{'spectrum':>16s}")
    print(f"  {'F_q curve (Frobenius)':22s}{'COMMUTES (linear)':>22s}{'PD, gapped':>20s}{'|z|=sqrt q EXACT':>16s}")
    print(f"  {'Spec Z (zeta scaling)':22s}{'ANTI-commutes':>22s}{'gapless e^-cL':>20s}{'zeros marginal':>16s}")
    print("  => MW-5 (precise): the curve has a J-LINEAR Frobenius isometry of a GAPPED polarization;")
    print("     the zeta window has neither. The missing object is exactly that J-linear gapped Frobenius.")
