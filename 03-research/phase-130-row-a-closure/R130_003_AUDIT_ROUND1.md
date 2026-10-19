# R130.003 — Audit of the phase-130 build (round 1)

Scope: independent
re-derivation of the theorems added by the construction in R130.001, read directly
in Paper 43 `main.md`, before and independently of the audit
R130.002.

## 1. Re-derived and found correct

| statement | check performed |
|---|---|
| Thm 9.14a (a)–(e) | recomputed `λ_±(F_n)`, `F̂_n`, the exponential bound `e^{−na/2}‖ψ‖_1`; `F_n ∈ D_A` (smooth, compact support, even, constant on `∏Z_q^×`); strong-dual convergence via Lemma 9.14a0 |
| Thm 9.14b | direct; both summands closed, projections continuous, `†` preserves |
| Thm 9.14c(b) | independent computation: `G_m^† = F_m`, so `I_A(F_n,G_m) = T(F_n⋆F_m)`, whose profile is `e^{−t/2}φ_{n,m}(t)` with `φ_{n,m}` a probability density supported in `[(n+m)a,(n+m)b]`; every `W_p` term is `(log p)Σ_{j≥1}p^{−j}φ(j log p)` and `W_∞` is `O(e^{−(n+m)a})`; at fixed finite `S` all terms → 0 exponentially. Confirms `I_A`-nullity of the rulings |
| Thm 9.7b (a),(b) | re-derived the Mittag–Leffler forms and residues by hand; numerically `scripts/ml_check.py` (`p=2,3,7`; residues `∓i` for `Ŵ_2`, `Ŵ_∞`) |
| Thm 9.7b (d),(e) | contour orientation, PW decay, horizontal boundedness, vertical decay by periodicity — correct; numerically `scripts/contour_check2.py`: axis integral `= W_p` direct `= 0.594347…`, residue sum `= Poisson = 1.986329…`, `res + contour = W_p` to 15 digits (the review's first script had a quadrature failure on the oscillatory integrand; replaced) |
| Thm 8A.7b (a)–(e) | submultiplicativity with constant 1 (`N(F⋆G) ≤ ‖G‖_1N(F)`), interchange by dominated convergence, principal-Log additivity from the disc-of-radius-one argument |
| Thm 8A.7c | support window and stabilization; `λ_∓∘J = λ_∓` |
| Thm 10.3b | nets; positivity of `λ_±` on the cone; AM–GM `‖F‖_1 ≤ ½(λ_++λ_−)`; `ℓ = 0` |
| Thm 10.6a | from Thm 9.5 / Thm 9.12(T3)(i) |
| Thm 10.7 (a),(b),(d),(e),(g), Thm 10.8 | as written; (e) is the sum of 9.14a/b and 10.8 — see §2.1 for what its content is and is not |
| Thm 10.9 (a)–(c) | `Tor_1 = I/I²`; `∂_±` kill `I²` and are jointly onto `C²` |
| Thm 8A.10, 8A.11, Thm 3.8, Prop 3.9 | as written |

## 2. Findings

**F1 (MAJOR, precision) — Thm 8A.9(a).**  The text says the origin class
`C[0]` is "assigned the weight `τ_p(w_p) = p^{−|v_p(w_p)|/2}` by the
half-density normalization".  `τ_p(σ) = |σ|_p^{1/2}/|1−σ|_p` is the product of
the half-density `|σ|^{1/2}` **and** the fixed-point (Lefschetz) weight
`1/|1−σ|_p`.  For `v_p(σ) > 0` the latter is `1`; for `v_p(σ) < 0` it is
`p^{−|v_p|}` and the half-density is `p^{+|v_p|/2}`, whose product is again
`p^{−|v_p|/2}` (Lemma 8.4: `τ_p(x^{−1}) = τ_p(x)`, Appendix D.2).  The theorem
is true but the sentence attributes the whole weight to the half-density.
Repair: state the Haar-regularized rank as `1/|1−σ|_p` (the orbital/Lefschetz
weight of the fixed point `0`), the half-density as `|σ|^{1/2}`, and their
product as `τ_p`, citing Lemma 8.2, Lemma 8.4 and Appendix D.2 for the
negative-valuation shells.

**F2 (MINOR) — Thm 10.9(c).**  `I ⊆ D_A^+` contains elements `a·1 + F`, and the
proof that `∂_±` kill `I²` is written for `F,G ∈ D_A` only.  It extends: for
`a1+F, b1+G ∈ I` one has `a = −λ_∓(F)`, `b = −λ_∓(G)` on each Tate point, and
`∂_±((a1+F)(b1+G)) = a∂G + b∂F + ∂(F⋆G) = a∂G + b∂F − b∂F − a∂G = 0`.  Add
the two lines.

**F3 (NOTE, on content) — Thm 10.7(e).**  The second component of `λ_RR` on
`D_A` is `λ_per∘M` by definition, so the statement "restricts on the ruling
plane to `λ_per`" carries, in that slot, no content beyond Theorem 9.14a/b
(the rulings exist as subobjects; the completion splits).  The content of
A.8's closure is therefore exactly: (i) 9.14a/b, (ii) 10.8 (the analytic
determinant is trivial on the rulings — a theorem), (iii) the resulting
necessity of the vector target, (iv) the laws (a)–(d),(f).  The paper should
say this in one sentence after Theorem 10.7 so that no reader takes (e)'s
second slot for a theorem.  Not an error.

**F4 (NEW THEOREM to add; label `CLASSICAL`) — the finite-chart negative
Theorem 10.8 is a chart artifact, and the colimit scalar form IS hyperbolic
on the rulings, by Mertens' theorem.**  On the colimit `D_A^∞` of
Theorem 8A.7c, with the same spread Tate characters `F_n`, `G_m`
(`G_m^† = F_m`), the profile of `F_n⋆G_m` is `e^{−t/2}φ_{n,m}(t)` with
`φ_{n,m}` a smooth probability density on `[(n+m)a,(n+m)b]` and
`∫|φ'_{n,m}| → 0`.  Then

    Σ_{all p} W_p(F_n⋆G_m) = Σ_{N≥2} (Λ(N)/N)·φ_{n,m}(log N),

(only `j ≥ 1` shells meet the support; `p^{−j/2}·p^{−j/2} = p^{−j}`), and by
partial summation against Mertens' theorem `Σ_{N≤x}Λ(N)/N = log x + O(1)`
(elementary; no zeta zero) this equals `∫φ_{n,m} + O(∫|φ'_{n,m}|) → 1`;
`W_∞(F_n⋆G_m) = O(e^{−(n+m)a}) → 0`.  Hence

    lim_{n,m→∞} I_∞(F_n, G_m) = 1 = β_T(e_+, e_−),   lim I_∞(F_n,F_n) = 0,

uniformly in the order of limits.  **So in the colimit the scalar
determinant `L_∞ = (C, e^{I_∞})` extends `λ_per` on the rulings** — Weil's
`e_1·e_2 = 1` — and the value `1` is the prime number theorem in Mertens'
form: the logarithmic density of prime powers.  At every finite chart the
value is `0` (Theorem 10.8) because the primes carrying it are outside `S`.
This must be written as Theorem 10.8b with label `CLASSICAL` (Mertens),
placed after Theorem 10.8 and cross-referenced in §14.1 as what row A hands
to row C: the vector-valuedness of `λ_RR` at finite `S` is the finite-chart
shadow of a scalar hyperbolic global pairing.  It is **not** to be counted
toward any clause of A (A.10), and the paper must say so; the per-chart
theory is where the clauses are proved.  (The review has checked the
computation; the construction must write the proof, including the total-variation
estimate and the uniformity of the double limit.)

**F5 (NOTE) — Remark 9.7c item 1** says `λ_+` is "a summand of the
archimedean local trace" by (9.7b.6).  True for the even component; state
that the odd component (`ε=1`) has no Tate pole (poles of `ψ(3/4+iτ/2)` at
`i(2n+3/2)`), consistent with `λ_±` living on `𝔠_0` only.

**F6 (NOTE) — the renaming test.**  Remark 9.7a: `T̂` is verbatim the prime
side of the explicit formula.  The review's view: the explicit formula is an
*identity* between that side and a sum over zeros; nothing in A.2–A.8 uses
the identity, and Theorems 9.8, 9.13, 9.14a–c, 10.3b, 10.8, 10.9 are
statements about the geometric side alone that the explicit formula neither
states nor implies.  A.5's `T` is a construction of that side from
fixed-point data, not a renaming of the identity.  Final verdict deferred to
the audit R130.002 and the review's reconciliation.

## 3. Instruction for the construction (round 2)

Repair F1, F2, F5; add the sentence of F3; write Theorem 10.8b of F4 with
its `CLASSICAL` label and the §14.1 cross-reference; then address every
finding of R130.002 (the audit), and re-issue the verdict block
honestly.
