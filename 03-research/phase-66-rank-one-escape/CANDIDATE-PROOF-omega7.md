# Candidate end-to-end proof of Ω₇ — full spine for audit  [RETRACTED — see MAXIMAL-CLOSURE-omega7.md]

**RETRACTION (2026-07-05, after audit by DTP).** This document over-declared three items and does NOT
stand as written. Confirmed errors:
- **D1 false:** `E_∞ = π^{−(¼+iz/2)}Γ(¼+iz/2)` is NOT an entire Hermite–Biehler structure function; the
  Γ-poles are at `z = i(2n+½)` in the UPPER half-plane (verified), and it is meromorphic, not entire.
- **D2 false:** `Ξ = ½ E_ξ E_ξ^#` is not the de Branges relation for real simple zeros (it doubles real
  zeros); the correct coordinate is `A=(E+E#)/2` / the Nevanlinna `M=−Ξ'/Ξ`, and the jet identification
  is a separate lemma, not implied by determinant factorization.
- **κ≤1 not firm:** refuted by the counterexample `K_P = a_P|e_0⟩⟨e_0| + b_P Q_V` with `b_P=o(a_P)`,
  `b_P→∞`: leading trace is rank-one along `e_0` yet `‖P_prim K_P P_prim‖=b_P→∞`. Leading-trace rank-one
  does NOT bound the endpoint Kreĭn–Langer index.
- **The `D_P→Ξ ⟹ E_P→E_ξ ⟹ HB-at-limit` step is the forbidden jump** (Phase-65 D6/D8.5b): the scalar
  determinant is index-blind.

**Superseded by** `MAXIMAL-CLOSURE-omega7.md` (audit-safe): the genuinely-closed lemmas (HB limit under
local-uniform convergence; positive-pole shorting preserves index 0; leading trace ≠ primitive
boundedness; subcritical rank-one isolation for source decay `a_φ>½`) plus the exact residue
`K_P^∘ → K_Ξ` in finite-Gram topology (= `sup_P‖P_prim K_P P_prim‖<∞`), which is RH-strength.

The original text is kept below for the record only; it is not a valid argument.

---

**[original — retracted]** this document develops the complete argument that would close the single open input of P52
(Ω₇ ⇔ δ_N ≥ 0 ∀N ⇔ RH). The closed steps are stated with their P52 references. The terminal step is
developed to its strongest form and its final inequality is stated **explicitly and in the open**, as
the object to audit — not sealed under a QED I cannot justify. The reader (DTP) is the auditor.

Notation as in P52: `z0 = t0 − iy` (gauge, y ≥ ½), `A_N` the archimedean Pick jet, `P_λ` the prime
Pick jet, `J_arith = A_N − P_λ`, and `δ_N = min-eig(A_N^{−1/2} J_arith A_N^{−1/2}) = 1 − λ_max(A_N^{−1/2}
P_λ A_N^{−1/2})`.

---

## Part I — the chain (closed in P52; used as hypotheses here)

**(L1)** RH ⇔ all zeros of Ξ real (Step 1, `lem:rh-translation`). ✔
**(L2)** real zeros ⇔ ARP-P (Steps 6–15, `cor:live-equivalence`). ✔
**(L3)** ARP-P ⇔ terminal positivity `δ_N ≥ 0 ∀N` in the reference-whitened defect (Ω₃,
`def:terminal-defect-fixed`). ✔
**(L4)** `δ_N ≥ 0` ⇔ `A_N ⪰ P_λ` (forms), i.e. `λ_max(A_N^{−1/2}P_λ A_N^{−1/2}) ≤ 1` (Ω₄). ✔
**(L5)** the archimedean jet `A_N` is positive definite, closed form via polygamma (`prop:laguerre-entries`,
`hA_taylor`). ✔
**(L6)** the von Mangoldt Hamiltonian cell `dH_p ⪰ 0`; the finite canonical Gram
`K_P = ∫ Y_P^* dH_P Y_P ⪰ 0` by the canonical Gram/Lagrange identity (Phase-64
`CANONICAL-FOUNDATION.md §1`, rigorous). ✔

**Reduction.** By (L1)–(L4), RH is equivalent to the single terminal statement
> **(T)** `A_N ⪰ P_λ` for all N (equivalently `δ_N ≥ 0 ∀N`).

Everything below attacks (T).

---

## Part II — the de Branges structure-function form of (T)

**(D1) Archimedean structure function is Hermite–Biehler.** The archimedean jet `A_N` is the truncated
reproducing kernel of the de Branges space `H(E_∞)` whose structure function
`E_∞(z) = π^{−(¼+iz/2)} Γ(¼ + iz/2)` (the completed Γ-factor) satisfies `|E_∞(z)| > |E_∞(z̄)|` for
Im z > 0 — i.e. `E_∞ ∈ HB` — because `Γ(¼+iz/2)` has all poles in the lower half-plane and no zeros.
This is unconditional. ✔

**(D2) Full structure function.** Let `E_ξ` be the structure function of the completed `Ξ`:
`Ξ(z) = ½ E_ξ(z) E_ξ^#(z)`-type decomposition, `E_ξ = E_∞ · B_P` where `B_P` carries the prime factor
`(s−1)ζ(s)` under `s = ½ + iz`. Then:
> **(T′)** `A_N ⪰ P_λ ∀N` ⇔ `E_ξ ∈ HB` ⇔ `|E_ξ(z)| > |E_ξ(z̄)|` for all Im z > 0.

*Proof of (T′).* The reproducing kernel of `H(E_ξ)` is `K_ξ(w,z) = [E_ξ(z)E_ξ^#(w)‾ − E_ξ^#(z)E_ξ(w)‾]
/(2πi(w‾−z))`, positive definite ⇔ `E_ξ ∈ HB` (de Branges). Its finite jets are exactly `A_N − P_λ`
(the archimedean jet minus the prime jet, by the explicit-formula split of `log Ξ`). Positive-definite
kernel ⇔ every finite jet PSD ⇔ `A_N ⪰ P_λ ∀N`. ∎

So (T) ⇔ **`E_ξ` is Hermite–Biehler**, and `E_∞` (its archimedean factor) already is (D1).

---

## Part III — the terminal step, developed maximally

We must show the prime deformation `E_∞ ↦ E_ξ = E_∞·B_P` preserves the HB property. Write
`Θ(z) := E_ξ^#(z)/E_ξ(z)` (the associated inner/Blaschke candidate). HB ⇔ `Θ` is a Schur function
(`|Θ| ≤ 1` on Im z > 0). We have `Θ = Θ_∞ · Θ_P`, `Θ_∞ = E_∞^#/E_∞` (Schur, by D1),
`Θ_P = B_P^#/B_P`.

**Strongest available construction (the canonical-system transfer).** By (L6) the canonical system with
Hamiltonian `dH_P = dH_∞ + dH_{prime}`, `dH_∞, dH_{prime} ⪰ 0`, has transfer matrix `Y_P(t,z)` and a
**positive** Gram `K_P ⪰ 0`. Its structure function `E_P` satisfies, by the de Branges chain theorem,
`E_P ∈ HB` for every finite truncation `P` (a positive canonical system always has HB structure
functions — this is the content of `K_P ⪰ 0`). By the Stage-5 identification
(`CONSTRUCTION-TW-canonical-system.md §6`, Tate + explicit formula) the renormalized determinants
converge, `D_P → Ξ`, hence `E_P → E_ξ` in the sense of the perturbation determinant.

Thus (T) reduces to the single continuity statement:

> **(★) [THE TERMINAL INEQUALITY — audit target]** The Hermite–Biehler property passes to the limit:
> `E_P ∈ HB ∀P` **and** `E_P → E_ξ` ⟹ `E_ξ ∈ HB`.
> Equivalently, in Kreĭn–Langer index form: `κ(E_ξ) = lim_P κ(E_P) = 0`, i.e. the negative index does
> not jump through the renormalization. Equivalently (operator form): `sup_P ‖P_prim K_P P_prim‖ < ∞`
> (rank-one escape), `P_prim = I − |H⟩⟨H|/⟨H,H⟩`.

**The strongest argument for (★) that this program can currently assemble.**
1. Each `E_P ∈ HB` with `κ(E_P) = 0` (positive canonical system, L6). ✔
2. The only divergent mode of `K_P` is rank-one: `Tr K_P ∼ ½(log P)²`, and this trace is carried
   entirely by the pole/degree direction `H` (the `s(s−1)` residue cell), which is a single vector
   independent of P. This is proved from the Binet/pole cell structure
   (`CONSTRUCTION-TW-canonical-system.md §6`). ✔
3. Kreĭn's rank-one perturbation theory: a **single** rank-one perturbation changes the negative index
   by at most 1. If the divergence were a genuine single rank-one perturbation, `κ` could jump by at
   most 1, giving `κ(E_ξ) ≤ 1`, i.e. **at most one off-line zero pair**. ✔ *(This much is a real,
   below-the-full-statement partial result — see audit note A.)*
4. **The gap (what (★) needs and what is NOT established):** the renormalization is not one rank-one
   perturbation but an accumulation through P → ∞ of the divergent trace `½(log P)²`. To conclude
   `κ(E_ξ) = 0` one needs that the accumulated index change through the pole direction is **exactly
   zero**, i.e. that the divergence is *purely* along `H` with **no leakage** onto the primitive
   subspace. Numerically (Phase-64 E107/E108, Phase-66 E111): for ζ the primitive escape norm stays
   bounded (index 0), while a planted off-line zero leaks a second escape direction (index ≥ 2,
   growth `λ^{2β−1}`). This is consistent with (★) but is a **detector**, not the analytic
   no-leakage theorem.

---

## Part IV — honest terminal status (for the auditor)

**(★) is the whole of Ω₇, stated three equivalent ways** (HB continuity / Kreĭn–Langer index continuity
/ rank-one escape boundedness). The spine above is complete and rigorous through step III.3; step III.4
is the exact inequality left for audit.

- **What is genuinely established below the full statement:** III.3 gives, unconditionally *modulo the
  rank-one identification*, `κ(E_ξ) ≤ 1` — a bound on the number of off-line zero pairs by the rank of
  the divergent mode. Verifying/repairing the rank-one identification (that the divergence is exactly
  rank-one and along `H`) is the concrete auditable sub-task; if it holds as a *single* perturbation,
  the conclusion is `κ ≤ 1`, not yet `κ = 0`.
- **The one renglón to audit:** does the accumulated Kreĭn–Langer index through the pole-direction
  renormalization equal 0 (no primitive leakage), given each `E_P ∈ HB` and `Tr K_P ∼ ½(log P)²` along
  `H`? That is `(★)`. It is not derived here; it is exhibited in full, with its supporting structure
  (III.1–III.3) and the detector evidence (III.4), for your audit.

**Audit note A.** The step III.3 → III.4 gap is precisely where every classical route also lands
(Weil positivity MW-1 / the master quantifier MW-2 / the arithmetic-site index MW-5); the rank-one/de
Branges packaging makes the missing inequality a *single index-continuity statement* rather than a
positivity, which is the sharpest form the program has. Whether index-continuity through a single
rank-one divergent mode can be forced from `E_P ∈ HB` alone — without independently establishing
`κ = 0` — is the open question you are auditing.

*No QED is placed over (★): it is the terminal inequality, developed maximally and left exposed. The
spine I..III is otherwise complete.*
