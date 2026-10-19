#!/usr/bin/env python3
"""E.00 — Reusable counterfactual harness.

Instruments principle P3 of paper 41 (`41/main.tex:1259-1262`):

    "if a proposed argument still holds verbatim in a system with a
     zero off the line, it is already refuted."

Base: 113_14 Thm 3.3 gives a witness generator in closed form -- every zero off
the line produces, by a one-line formula, a real Schwartz datum with
s(f,f) = 4m|a_1|^2 > 0.  This file extracts it into a reusable interface.

USAGE
---
    from importlib import import_module
    H = import_module("114_e_00_counterfactual_harness")

    def my_lemma(w):
        "returns True if the lemma asserts positivity in world w"
        ...
        return some_condition

    H.audit(my_lemma, "prop:shiftchaincoercivity")

VERDICTS
----------
  BLIND            the predicate never consulted the world's spectral data.
                   It cannot be a carrier for row (d): it holds the same with RH and without RH.
  NON-DISCRIMINATING  it consults them, but gives the same value in both worlds.
  DISCRIMINATING   gives different values.  It touches the decisive mechanism.

A BLIND or NON-DISCRIMINATING verdict does not say the lemma is false or useless --
it says that by itself it cannot close row (d), and it is worth knowing the day it is stated.

Requires only mpmath.  It certifies nothing: it is a falsifier.
"""
import mpmath as mp

mp.mp.dps = 30

__all__ = ["World", "on_line_world", "off_line_world", "audit", "witness", "s_form"]


# --------------------------------------------------------------------------- worlds
class World:
    """A spectral model.  Records every access to the zero data.

    zeros: list of (rho, multiplicity).  The world is closed under the orbit
    rho -> conj rho -> 1-conj rho -> 1-rho, as required by the functional equation.
    """

    def __init__(self, zeros, name, rh_holds):
        self._zeros = list(zeros)
        self.name = name
        self.rh_holds = rh_holds
        self.accesses = 0

    @property
    def zeros(self):
        self.accesses += 1
        return self._zeros

    def reset(self):
        self.accesses = 0

    def mirror(self, rho):
        """rho' = 1 - conj rho.  Under RH it coincides with rho."""
        return 1 - mp.conj(rho)

    def s_form(self, fhat):
        """s(f,f) = - sum_rho m_rho f^(rho) conj(f^(rho'))   over D^o.

        fhat: callable s -> C.  Sign: A_T represents -B_nuc, so
        <A_T F, F> = + sum_rho m_rho f^(rho) conj(f^(rho')).
        Here we return s(f,f) = -that sum, the convention of 113_12.
        """
        tot = mp.mpf(0)
        for (rho, m) in self.zeros:
            tot += m * fhat(rho) * mp.conj(fhat(self.mirror(rho)))
        return -tot

    def __repr__(self):
        return f"<World {self.name!r} RH={self.rh_holds} nz={len(self._zeros)}>"


# first zeta-zero heights (Odlyzko); enough for a finite model
GAMMAS = [mp.mpf(g) for g in [
    "14.134725141734693", "21.022039638771555", "25.010857580145688",
    "30.424876125859513", "32.935061587739189", "37.586178158825671",
    "40.918719012147495", "43.327073280914999",
]]


def on_line_world(n=6, name="on-line (RH true)"):
    """Zeros on the critical line, in conjugate pairs."""
    zs = []
    for g in GAMMAS[:n]:
        zs.append((mp.mpc(mp.mpf("0.5"), g), 1))
        zs.append((mp.mpc(mp.mpf("0.5"), -g), 1))
    return World(zs, name, rh_holds=True)


def off_line_world(n=6, sigma="0.8", name="off-line (RH false)"):
    """Same, but the FIRST zero is moved off the line, generating the
    quadruple {sigma+it, sigma-it, 1-sigma+it, 1-sigma-it} of 113_14 C2."""
    w = on_line_world(n, name)
    g0 = GAMMAS[0]
    s0 = mp.mpf(sigma)
    w._zeros = w._zeros[2:]                       # remove the on-line pair
    for rho in [mp.mpc(s0, g0), mp.mpc(s0, -g0),
                mp.mpc(1 - s0, g0), mp.mpc(1 - s0, -g0)]:
        w._zeros.append((rho, 1))
    w.rh_holds = False
    return w


# --------------------------------------------------------------------- 113_14 witness
def witness(rho0, m=1, Gauss=True):
    """113_14 Thm 3.3 case 1: the real witness in D^o with s(f,f) = 4m|a_1|^2 > 0.

    Returns (fhat, quadruple, prediction).  rho0 must be off the line and
    not real.  On a surrogate Xi Xi_S = D4 * G with G(s) = exp((s-1/2)^2).
    """
    q1 = mp.mpc(rho0)
    QUAD = [q1, mp.conj(q1), 1 - mp.conj(q1), 1 - q1]
    G = lambda s: mp.e ** ((mp.mpc(s) - mp.mpf("0.5")) ** 2)
    gg = lambda s: mp.mpc(s) * (mp.mpc(s) - 1) * G(s)     # = s(s-1) Xi_S / D4

    A1 = gg(q1)
    u0 = q1 - mp.mpf("0.5")
    if abs(mp.im(u0 ** 2)) < mp.mpf("1e-25"):
        raise ValueError("rho0 is on the critical line: Im(u_0^2)=0, there is no rotation")
    z = mp.mpc(0, 1) / A1
    c2 = mp.im(z) / mp.im(u0 ** 2)
    c0 = mp.re(z) - c2 * mp.re(u0 ** 2)
    P = lambda s: c0 + c2 * (mp.mpc(s) - mp.mpf("0.5")) ** 2
    fhat = lambda s: P(s) * gg(s)
    return fhat, QUAD, 4 * m


def s_form(fhat, quad, m=1):
    """s(f,f) on the quadruple, with the mirror pairing rho <-> rho'."""
    MIR = [2, 3, 0, 1]
    a = [fhat(q) for q in quad]
    return -m * sum(a[j] * mp.conj(a[MIR[j]]) for j in range(4))


# --------------------------------------------------------------------------- audit
def audit(predicate, label, worlds=None, verbose=True):
    """Evaluates `predicate(world) -> bool` in a world with RH and another without RH.

    Returns (verdict, value_on, value_off, accesses_on, accesses_off).
    """
    if worlds is None:
        worlds = (on_line_world(), off_line_world())
    w_on, w_off = worlds
    w_on.reset(); w_off.reset()
    v_on = bool(predicate(w_on))
    v_off = bool(predicate(w_off))
    a_on, a_off = w_on.accesses, w_off.accesses

    if a_on == 0 and a_off == 0:
        verdict = "BLIND"
        note = "never consulted the zeros; it cannot be a carrier for row (d)"
    elif v_on == v_off:
        verdict = "NON-DISCRIMINATING"
        note = f"consults the zeros ({a_on} accesses) but gives {v_on} in both worlds"
    else:
        verdict = "DISCRIMINATING"
        note = f"RH-world: {v_on}   non-RH-world: {v_off}  -- touches the mechanism"

    if verbose:
        print(f"  [{verdict:<19}] {label}")
        print(f"      {note}")
    return verdict, v_on, v_off, a_on, a_off


# ------------------------------------------------------------------------------ self-test
if __name__ == "__main__":
    print("E.00 — counterfactual harness: self-test\n")

    # 1. the 113_14 witness reproduces
    print("1. Closed witness from 113_14 Thm 3.3")
    fhat, QUAD, pred = witness(mp.mpc("0.8", 6))
    val = s_form(fhat, QUAD)
    assert abs(mp.im(val)) < mp.mpf("1e-18"), "s(f,f) should be real"
    assert mp.re(val) > 0 and abs(mp.re(val) - pred) < mp.mpf("1e-15"), \
        f"s(f,f)={mp.re(val)} != {pred}"
    assert abs(fhat(0)) < mp.mpf("1e-25") and abs(fhat(1)) < mp.mpf("1e-25"), \
        "the witness must be in D^o"
    print(f"   ok  s(f,f) = {mp.nstr(mp.re(val), 15)}  (predicted 4m = {pred}) > 0")
    print(f"   ok  f^(0) = f^(1) = 0, the witness is in D^o")

    # on the critical line the generator must REFUSE to produce a witness
    try:
        witness(mp.mpc("0.5", 14))
        raise AssertionError("should have failed on the critical line")
    except ValueError:
        print("   ok  on Re s = 1/2 there is no witness (Im(u_0^2)=0) — that IS RH")

    # 2. audit of the three row (d) lemmas
    print("\n2. Audit of the current row (d) statements")

    def shift_chain_coercivity(w):
        """prop:shiftchaincoercivity — R_T >= alpha_N I.
        Depends only on Lambda(n) and the geometry of chains."""
        import numpy as np
        from sympy import factorint
        N, T2 = 200, mp.log(200)
        alpha = 0.0
        for n in range(2, N):
            f = factorint(n)
            if len(f) != 1:
                continue
            w_n = float(mp.log(next(iter(f)))) / float(mp.sqrt(n))
            m = int(mp.ceil(T2 / mp.log(n)))
            alpha += w_n * (1 - float(mp.cos(mp.pi / (m + 1))))
        return alpha > 0

    def uniform_witt_moments(w):
        """prop:uniformWittmoments — summability of all depths.
        Also purely arithmetic."""
        return True

    def weil_positivity(w):
        """The row (d) statement itself: s(f,f) <= 0 in D^o.
        Tested with the witness of the world itself."""
        offline = [r for (r, _) in w.zeros if abs(mp.re(r) - mp.mpf("0.5")) > mp.mpf("1e-9")
                   and abs(mp.im(r)) > mp.mpf("1e-9")]
        if not offline:
            return True                      # no zero off the line, no witness
        fh, quad, _ = witness(offline[0])
        return mp.re(s_form(fh, quad)) <= 0

    audit(shift_chain_coercivity, "prop:shiftchaincoercivity  (R_T >= alpha_N I)")
    audit(uniform_witt_moments, "prop:uniformWittmoments")
    audit(weil_positivity, "row (d) itself:  s(f,f) <= 0 in D^o")

    print("\nREADING")
    print("  The first two come out BLIND: they are statements about Lambda(n) and the")
    print("  channel geometry, with no zero at all. This matches the paper's own")
    print("  evaluation (row-d-local-analysis.tex:464-474): they control the")
    print("  reference but do not prove the sharp domination.")
    print("  The third comes out DISCRIMINATING, as it should: it is row (d).")
    print("\n  The harness is calibrated. Use it on every D2 lemma the day it is stated.")
