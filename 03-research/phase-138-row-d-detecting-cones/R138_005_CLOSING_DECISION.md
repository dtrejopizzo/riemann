# R138.005 — Closing decision, phase 138 (row D, the primitive sector and detecting cones)

verification, working rule), R138_001 (rounds 1–2 applied in place), R138_002 (audit),
R138_003 (repair ledger), R138_004 (confirmation). Checks: the Laplace identity
`∫_0^∞ 4 sinh²(wT/2) e^{−zT} dT = 2w²/(z(z²−w²))` and its summation over zeros to `2z^{−2}(ξ'/ξ)(½+z)`;
the Cauchy–Schwarz step of Theorem D.15.4; residuals C1–C4 of R138_004 applied in R138_001 §7,
§7bis and README.*

## 1. The original question and its answer

**Q ((§1)):** what intrinsically distinguishes the primitive radial sector from the positive directions
that make `I_A` indefinite, and is there a non-circular reason for the relevant arithmetic classes to lie
in a cone where `I_∞(F,F) ≤ 0`?

**Answer of record.**

1. *What distinguishes the sector* (Theorem D.15.1, PROVED): `D^W = Λ ⊥ P^W`, an `I_∞`-orthogonal
   splitting in which `Λ = span(K, K_odd)` is a hyperbolic plane of signature `(1,1)` reading only the two
   rulings `(deg⁻F, deg⁺F)`, with `K_odd = (2 sinh(a/2))^{−1}(τ_aK − τ_{−a}K)` an explicit odd class of the
   Weil completion, and `P^W` the primitive sector carrying the pure zero form. The primitive sector is
   the common isotropic kernel of both rulings; the indefiniteness of `I_A` is entirely the plane `Λ`.
2. *The polar block cannot detect* (Theorem D.15.3, PROVED): on `Λ` the Hodge-index inequality holds
   identically with slack `½(deg⁺F − deg⁻F)²`; no inequality that is a function of the ruling datum alone
   distinguishes `ξ` from a function with off-line zeros.
3. *Detection is cheap and zero-free* (Theorems D.17.2, D.17.2c, D.17.2d, PROVED): the triangle family
   `h_T = (1−|t|/T)_+` detects every off-line zero — `RH ⟺ W(h_T) ≥ 0` for all `T > 0` — by Landau's
   theorem applied to `G(z) = ∫_0^∞ T·W(h_T)e^{−zT}dT = 2z^{−2}(ξ'/ξ)(½+z)`, whose only real singularity
   is `z = 0`. Hence the effective cone `E = {F ≥ 0}` and `C_c^∞` are detecting cones. Novelty of the
   one-parameter criterion: OPEN (literature check D.17-α pending: Fejér-kernel Weil positivity, Yoshida,
   Riesz-mean criteria). The falsifier `Ξ_a` is detected by the same argument.
4. *On the detecting cones the sign is the PNT remainder* (D.17.3, PROVED-IN-REPOSITORY via phase-114
   D.185; convexity of the kernel does not help, Remark D.17.3(d)).
5. *The separating zero-free invariant* (Theorems D.15.4, D.15.4b, PROVED): equimodularity of the polar
   exponents `|p − ½|`. For `ξ` (`P = {0,1}`) the Frobenius translation cone `Λ_ξ^+` satisfies Hodge
   index with slack `⅛(A−B)²`; for `Ξ_a` (`P = {−a,a,1−a,1+a}`) Hodge index fails on the *effective*
   class `τ_uK_a + τ_{−u}K_a` by strict Cauchy–Schwarz — no zero, no prime, no `h⁰`. Ceiling (D.15.4d):
   `ζ_K` is equimodular, so equimodularity is necessary and cannot yield the sign.
6. *The structurally signed cone is maximally non-detecting* (Corollary D.15.4c, Theorem D.16.2‴):
   `Λ_ξ^+ ⊂ 𝓝_∞`, `Φ_X(ρ) = 0` at every zero.
7. *Which operation separates the cones* (D.16.1, PROVED): not translation — Theorem F's own witnesses
   are `q_±(∂)(φ^{⋆N})` with `φ` chosen after the zero; the blueprint's expectation is REFUTED. What
   detection needs is a convolution square root chosen against the zero (unbounded support in the
   `h`-variable follows). Crossing height `2πe·e^{2T}` for the CC window (D.16.2′).

**Verdict on Q.** PROVED in the restricted form (no ruling-datum cone and no Frobenius-side cone is
detecting; every detecting cone the corpus can write carries the PNT remainder as its sign). OPEN in the
existential form: the one remaining quadrant is **clause (iii) on `E`** — a structural proof of
`I_∞(F,F) ≤ ½(deg F)²` on the effective cone, which is zero-free and detecting, subject to the constraint
that any such proof must fail for `ζ_K`-shaped data or prove GRH. Two "open" items of R138_001 were
closed in one line each (√C_Pó = {0}; `E` has empty interior in every vector topology
because it is absorbing at no point).

## 2. Corpus discipline (working rule)

Every idea of the phase was checked against the 137 prior phases first (`CORPUS_CHECK_R138.md`).
Reused, not redone: Hodge/rulings building blocks (phases 107, 113), Theorem F (Paper 45), the `log 2`
certificate (phase 118), the PNT route no-go (phase 114 D.185). Not reopened: Hilbert–Pólya (MW-4),
Laguerre–Pólya/Li/Keiper (phases 28, 103), window extension beyond `log 2`. Genuinely new and built:
the detecting-cone frame, the one-parameter Landau criterion, the hyperbolic-plane splitting with the
explicit `K_odd`, the equimodularity criterion with its `ζ_K` ceiling, the refutation of "translation is
the operation".

## 3. Paper-facing corrections (to enter in Paper 47 at the next Part III pass)

P47-1 fix the `M(F)` convention (§12.1/§12.5 vs §14.1 transposed); P47-2 add the effective-class
falsifier witness (Thm D.15.4) as Remark 12.3c; P47-3 exhibit `K_odd` and the splitting `D^W = Λ ⊥ P^W`;
P47-4 "RH ⟺ Hodge index on the ample cone (absorbing at `K`)" from Thm 11.14(iii), with the caveat that
the ample cone is defined through `I_∞` (fails clause (ii) of Q). Paper 45: no corrections.

## 4. Decision and recommendation for phase 139

Phase 138 **closed; no label change for row D.** FATAL screen clean (the one dangerous place — a sign
from equimodularity — is blocked by the `ζ_K` ceiling and recorded).

Recommendation, in order: (1) **clause (iii) on `E`** as the single target, formulated as a Hodge-index
inequality on nonnegative kernels — and the first task is *negative*: determine whether any inequality
provable from the carrier's structure alone (polar block, unimodular local roots, Frobenius unimodularity
`Frob_n⋆Frob_n^† = Δ^{(n)}`) can distinguish `ξ` from `ζ_K`-shaped data; if not, clause (iii) on `E`
is unreachable by structure and the programme must say so. (2) Equimodularity as a classification of
admissible `Z` (what else it forces on `Λ_Z^+`), never as a sign. (3) The cheap attribution search D.17-α.
(4) Do not reopen: Pólya cone, `log 2` window extension, `h⁰` growth, ample cone without D.15-β.
