# D128.001 — row An audit: findings and dispositions

Target: Paper 43.

## Accepted (verified)

**A1. Clause A.5 is never addressed.**  `grep` for `A.5` in `main.md` and
`appendix.md` returns nothing; the section headers discharge A.1, A.2 (§3),
A.3 (§4), A.4 (§5), A.9 (§6), A.6 (§9), A.7/A.8 (§10), A.10 (§11).  A.5 (trace
class domain, trace target `T_A`, cyclicity, restriction/determinant
compatibility) is absent.  The only note that ever discharged it, A125.014
Thm 7.1, argued from A125.014 Thm 1.1, which A125.016 refutes and A125.017
refutes again.  **So "A.1–A.10 closed" is false on a count.**  `ACCEPTED`.

**A2. Definition 8.1 is not well posed.**  `T(E_w)` is defined as the
logarithm of the P123.109–110 germ "evaluated on `β_w`"; those germs are
constructed for *small external Bruhat tests* at *one* normal place, and `β_w`
is an automorphism, not such a test.  The lattice expression (8.2) is stated
to be non-convergent and is never proved equal to the germ — yet Theorem 9.3
computes with (8.2).  **The paper defines `T` by one object and computes with
another.**  `ACCEPTED`.

**A3. The ruling plane of Theorem 9.1 uses a descent P123.008 says is refuted.**
P123.008's own status block: "`OPEN` for descent of this representation to the
external idele-class dynamics (P123.013 proves it cannot descend ...)".
`ρ_T` is defined on the internal gauge-label algebra `C_Q`; `N_A` is built from
external classes.  Theorem 9.1 has no proof.  Clause A.6 requires the ruling
plane; it is not established.  `ACCEPTED`.

**A4. Five numbered results have no proofs**: Prop. 3.2, Thm. 6.1, Thm. 9.1,
Thm. 10.2, Thm. 10.5.  `ACCEPTED`.

**A5. Theorem 10.5 (A.8, Riemann–Roch) asserts what its citations disclaim.**
P123.108: "It is **not** identified with the geometric biextension or
arithmetic RR correction."  P123.109: "Its geometric RR identification remains
open."  `ACCEPTED`; A.8 is not closed.

**A6. Theorem 9.3 quotes a withdrawn theorem.**  Its hypothesis reads "for
`u,u'` as in Theorem 7.4", and Theorem 7.4 is withdrawn in §13.5; the
conclusion still asserts "their shadows are isomorphic", which Appendix D.3
refutes.  `ACCEPTED` (repairable: state the hypotheses inline, delete the
clause).

**A7. Appendix D.2 is wrong for negative valuation.**  It says that for
`v_p(σ_p) ≠ 0` the factor is "the half-density `|σ_p|^{1/2}` alone".  For
`v_p(σ_p) < 0` one has `|σ_p|_p > 1`, hence `|1−σ_p|_p = |σ_p|_p` and
`τ_p = |σ_p|_p^{−1/2}`.  The correct uniform statement is
`τ_p(σ) = p^{−|v_p(σ)|/2}`, which is what P123.042 actually writes
("`x = p^k u`, `k≠0`, gives `p^{−|k|/2}`").  Since `Γ_S` is a full lattice,
negative valuations occur in every lattice sum.  `ACCEPTED`.

**A8. Appendix D.3/D.4's orbit count is stated only for `u ≡ 1 mod p`.**
`HH_0` is spanned by the characters trivial on the closure of `⟨u⟩`, and that
closure is `1+p^kZ_p` with `k = v_p(1−u)` **only when `k ≥ 1`**.  For
`u ≢ 1 mod p` the correct count is `[Z_p^× : closure⟨u⟩]`, and the claimed
identity "regularized rank `= 1/|1−u|_p`" fails: for `p=7`, `u=−1`, the index
is `3` while `|1−u|_7 = |2|_7 = 1`.  So D.4's unification holds on
`1 + pZ_p` and not on all units.  `ACCEPTED`.

**A9. Systematic status inflation.**  P123.039 is `CONSTRUCTED` and says
"must not be called ... the full A.5 shadow"; P123.074 says "not their full
numerical/RR descent on the stable category"; `A_DUALITY_WORK` says its
complex "is not being identified with the full Hochschild complex".  Each is
cited at a strength its own status forbids.  `ACCEPTED`.

**A10. Appendix A.2 misreads P123.039 (4.1).**  In (4.1) the summand is
(weight `p^{−k/2}`) × (log-torsion `log p`), a product of a multiplicative
weight with a logarithm.  It is not "`log` of (half-density × determinant)",
and `log τ_p(p^k) = −(k/2)log p ≠ (log p)p^{−k/2}`.  `ACCEPTED`.

**A11. "One citation beyond the repository" is false.**  `T(Δ)` rests on
P123.012, whose status is `IMPORTED` (Connes's cutoff-determinant theorem).
Also line 438 still labels Thm. 7.1(b) `IMPORTED (I-1)` while §12 says I-1 is
proved.  `ACCEPTED`.

**A12. The sector contains only invertible twists.**  Every generator `E_a` is
the graph of an automorphism.  In Weil's proof the content is carried by
`Γ_{F^k}`, of bidegree `(q^k,1)`, non-invertible.  §13.1 dismisses phase 123's
prescription ("add non-invertible objects") on the strength of Corollary 7.5,
which is about *additive invariants*, not about the sector.  That inference is
a non sequitur.  `ACCEPTED as a limitation of scope`: the honest statement is
that row A is constructed on the automorphism-graph sector.  (Mitigating, and
recorded: in the adelic setting the idele class group does act by invertible
dilations, and the explicit formula's weights arise from them — so the sector
is not empty for rows C/D.  But "equality of structural burden" with Weil's
proof is not established.)

## Rejected (verified wrong)

**R1. "The local factor (8.1) does not exist pointwise at a unit twist."**
The audit claims P123.042 shows the cutoff trace diverges inside `Z_p^×`.  It
does not.  (2.1) reads `Tr(E_{MN}D_x) = |x|_p^{1/2} min(p^L, |1−x|_p^{−1})`.
For a **fixed** `x ∈ Z_p^×` with `x ≠ 1`, `k := v_p(1−x)` is finite and
`min(p^L, p^k) = p^k` for every `L ≥ k`: the value is **exactly**
`|x|^{1/2}/|1−x|_p`, eventually constant in `L`, with no divergence.  The
divergence P123.042 (3.1) exhibits (`I_L = L+1`) is in the **integral** over
the unit group, because `p^{v_p(1−u)}` is unbounded as `u → 1` — not at any
fixed `u`.  The note's sentence "For `x` outside `Z_p^*` ... for every `L ≥ 0`"
says the bound holds for all `L` there; inside `Z_p^×` it holds for `L ≥ k`.
Theorem 9.3's use at a single unit point is therefore legitimate.  `REJECTED`.

## Disposition

The label `WEIL-STRENGTH-COMPLETE` for row A is **withdrawn**.  See
[D128.004](D128_004_WHAT_SURVIVES.md).
