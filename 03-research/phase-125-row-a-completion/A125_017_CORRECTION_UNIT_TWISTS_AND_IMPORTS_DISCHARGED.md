# A125.017 — second correction, and the imports discharged

Status: `PROVED-IN-REPOSITORY`.  Consolidated in Paper 43, `appendix.md`.

## 1. Correction
Paper 43 §7.1(c) (after A125.016) claimed every nontrivial finite-place twist
contributes only the origin class, and §7.2 that two unit classes have
isomorphic shadows.  False for unit twists: for `u∈Z_p^×`, `k=v_p(1−u)`, the
twisted shell complex has `HH_0 ≅ C^{N_k}`, `N_k=(p−1)p^{k−1}`, spanned by the
characters trivial on the closure `1+p^kZ_p` of `⟨u⟩`, one copy per shell
(Appendix D.3).  The shadow is infinite-dimensional and not isomorphic across
different `k`.  P123.096 was misapplied to shell translations; it is proved
only for `C(B_q)` and is now used only there.

## 2. What survives, sharpened
Additive invariants of the shadow are constant on the arithmetic family
(origin class only) and undefined on unit twists (infinite rank): no finite
additive invariant separates classes (Cor. 7.5, corrected proof).  The
analytic factor `|σ|^{1/2}/|1−σ|_p` is confirmed as the Haar-regularized
orbit count `N_k/c_p=p^k` at a unit and the half-density at a non-unit
(Appendix D.4).  Theorem 9.3 (the exact mixed computation) is untouched.

## 3. Imports discharged
* I-3 withdrawn: all lattice sums on the declared category are finite
  (Appendix A; P123.039 (4.1)).
* I-2 proved: split augmented excision by a cone argument (Appendix B.2),
  H-unitality from P123.124.
* I-1 proved: unital Eilenberg–Zilber with explicit continuous maps (C.1)
  plus a filtration argument (C.2), using one citation: Wodzicki excision
  for the non-split H-unital ideal `E_P⊂⊗̂E_v^+` (B.3), hypothesis proved.

The label of A125.015 stands with this single citation.
