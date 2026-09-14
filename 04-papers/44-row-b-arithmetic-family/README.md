# Paper 44 — Row B: the arithmetic family inside row A

> **Status, 2026-09-12 (phase 131).**  Rebuilt around the **norm class**
> `Γ_n^rad` (unit average of the graph of `a_S(n)`; on `Q` the ideal `(n)` is
> the level set `|x| = 1/n`).  In row A's proved trace its finite contact is
> `Λ(n)·n^{-1/2}`, with `Λ(p^k) = log p` the Haar volume of the valuation
> shell and `Λ(composite) = 0` because no place has a shell of that modulus
> (Thm 3bis.7, 3bis.7′: the arithmetic is the contact locus of an
> arithmetic-free family).  The `n−1` "unit sector" of the previous version
> is a property of the lift, not a contact (Cor 3bis.3); its row-C obligation
> is withdrawn.  Label ruled by the audit of record
> ([R131.005](../../03-research/phase-131-row-b-closure/R131_005_LEAD_FINAL_AUDIT_AND_LABEL.md)):
> **WEIL-STRENGTH-COMPLETE on Paper 43's declared carrier, conditional on the
> owner's acceptance of the B.4 amendment** (§6.2a′).  Hostile audit
> R131.002 and its disposition R131.004 are in phase 131.

> **Status, 2026-09-12 (phase 131, round 3) — [SUPERSEDED IN ROUNDS 4–5; see
> the round-4 and round-5 blocks below.  In particular the two sentences "the
> Gram matrix … **is** the Weil kernel" and "Weil positivity **implies** the
> Hodge index on this class" are RETRACTED — §9bis W16–W17.]**  The owner **accepted the B.4
> amendment** and asked for the recorded reservations of `R131.005` to be
> dissolved with new mathematics.  Three new sections do that.
>
> **§3ter — the Frobenius family.**  `Frob_{p^k}` := the Haar measure of the
> fixed-point stratum `j_p(p^k Z_p^×)`; `Frob_n := ⋆_{p|n}Frob_{p^{v_p(n)}}`.
> It is **not** radial.  Strong monoidal on `(N,×)` with the **diagonal
> itself** as unit (a point mass, not a projector);
> `Frob_n ⋆ Frob_n^† = Δ^{(n)}`, the averaged half-density form of Weil's
> `Γ_F Γ_F^t = qΔ` (with `Δ^{(n)} ≠ Δ` stated); the `†`-closure is a
> commutative **inverse semigroup** indexed by `Q_{>0}^×` **graded by finite
> prime sets**, idempotents `Δ^{(F)}`; the support determines `n` **and**
> `P(n)`; the finite contact is `Λ(n)n^{−1/2}h(1/n)` **exactly at every
> level**, vanishing at composite `n` because the support meets no stratum.
> And `Γ_n^{rad} = Frob_n ⋆ Δ^{rad}`: averaging is precisely what loses the
> factorization.
>
> **§6bis — the integral shadow.**  `Sh_Z(Frob_n) := [L_S →n→ L_S]`, defined
> on the **object** (gauge-invariant, unaffected by the unit averaging), with
> a transitivity triangle, `H⁰ = Z/n`, and Möbius cofiber `[Z→Φ_n(1)→Z]`:
> the accepted amended B.4 proved **on objects**.  This is the "integral or
> lattice category with a complex realization" that P123.022 §2's *Scope*
> paragraph says must be constructed; its complex realization is acyclic, so
> P123.022's refutation stands and the identification is of **degrees**.
>
> **§8bis — the Gram form, and the infinite genus.**  The Gram matrix of the
> smeared Frobenii **is** the Weil kernel `W(log m − log n)`; primitivity is
> two explicit linear conditions on the coefficients.  **Theorem: the
> regularized self-intersection of the diagonal diverges to `−∞`** — the
> arithmetic curve has infinite genus — with the rate computed from
> `Ŵ_∞ ∼ −log|τ|` and the finite places bounded.  Weil positivity **implies**
> the Hodge index on this class (proved, one direction, `CLASSICAL` input
> named); the converse needs a density statement that is **`OPEN`**, and the
> usual "gaps → 0" argument is shown to **fail** in a fixed window.
> **Row B delivers the Gram form, not the sign.**
>
> No sign, no positivity, no `𝓝_∞ = 0`, and no statement about zeros outside
> a single clause labelled `CLASSICAL`.  Three round-3 blueprint claims are
> **refuted with counterexamples** (§9bis W13–W15).  Builder's report:
> [R131.007](../../03-research/phase-131-row-b-closure/R131_007_BUILDER_ROUND3.md).

> **Status, 2026-09-12 (phase 131, round 4) — [SUPERSEDED IN ROUNDS 5–6; see
> the round-5 and round-6 blocks below.  Two sentences in this block are
> RETRACTED: "a new **negative** theorem: the sign of the pure Frobenius Gram
> form is **not** RH (Thm 8bis.4(iv))" — withdrawn as a non-sequitur, §9bis
> W19 — and "Its diagonal … **diverges** — linearly in `N` … and like
> `−log(1/ε)`" — the rate is normalization-dependent and is no longer
> headlined, §9bis (M5), Cor 8bis.1b′.]**  One FATAL error repaired.  The
> hostile audit `R131.008` found, and the lead `R131.009` independently
> confirmed, that round 3's central §8bis claim — *the Gram form of the
> Frobenius family is the Weil kernel* — is **false**, refuted by this paper's
> own Corollary 3ter.10b.  It is **withdrawn** (§9bis W16–W17), not softened,
> and the correct statement is proved in its place.
>
> **Two Gram forms (Thm 8bis.1′).**  The **Frobenius** family carries only the
> **finite half** `W_fin` of the Weil kernel: its archimedean block is
> multiplied by the arithmetic indicator `∏_{s∉F} 1[s^N | (n−m)]` and vanishes
> for large `N`, because `supp Frob_n` misses `Im j_∞`.  Its diagonal is now
> computed exactly and **diverges** — linearly in `N` at each `r ∤ n`
> (`−(log r)[(r−2)/(r−1) + (N−1)]`) and like `−log(1/ε)` archimedeanly — so
> `I_A` has no limit there (Thm 8bis.1b, Rem 8bis.1c).  The **unit-averaged**
> family `Frob ⋆ Δ^rad = Γ^rad` carries the **full** Weil kernel
> `W_fin + ω_∞`, exactly, at every level (Thm 8bis.1e).  *The averaging
> projector is precisely what converts the finite half into the whole — and
> what forgets the factorization.*  Two readings of one projector.
>
> Also new: `vol(Z_p^×) = log p` is now a **uniqueness theorem** — the unique
> local normalization with a universal Tate residue (Thm 8bis.8), with an
> explicit statement of why chart-invariance cannot force it (Rem 8bis.8b);
> `Sh_Z` is a strict **functor on the divisor poset**, a **function** on the
> monoid, and extends additively to Dirichlet-polynomial correspondences,
> supplying parts (b),(c) of the P123.038 §5 arrow while part (a) is
> **`REFUTED`** (Thm 6bis.3c); the Weil interface is rebuilt on the **radial**
> family, where it is `CLASSICAL` and unconditional and where there is **no**
> density question; and a new **negative** theorem: the sign of the pure
> Frobenius Gram form is **not** RH (Thm 8bis.4(iv)).  The
> Dirichlet-polynomial converse is attempted and closes for per-`n` widths
> under a named classical import, quarantined (§8bis.4), with the single-`ε`
> failure stated exactly.  Builder's report:
> [R131.010](../../03-research/phase-131-row-b-closure/R131_010_BUILDER_ROUND4.md).

> **Status, 2026-09-12 (phase 131, round 5) — quantifiers, conventions, and
> one withdrawn `PROVED`.**  The hostile audit `R131.011` (M1–M6) and the lead
> `R131.012` (LF1–LF4) found no error in §§3ter/6bis and six in §8bis.  All are
> repaired.
>
> * **The chart quantifier (M4, mandatory).**  §8bis now works on the colimit:
>   `T` means `T_∞` on `D_A^∞` and `W_fin` runs over **all** primes (standing
>   convention (C1)).  In particular "`I_∂ ≤ 0` on primitive radial classes ⟺
>   RH" is a **colimit** statement; **at a fixed finite chart it is false**,
>   and both forms are indefinite there.
> * **The divergence rate is not convention-free (M5).**  Corollary 8bis.1b′
>   gives the Frobenius Gram diagonal in **both** normalizations, with the
>   conversion factor `V_N(n) = ∏vol(1+r^NZ_r)`: bare → `0`, ♭ → `−∞`.  **No
>   rate is headlined anywhere now**; what is stated is that
>   `I_A(Frob_n,Frob_n)` **does not exist**.
> * **"The sign of the Frobenius form is not RH" is WITHDRAWN (M1/LF3, W19)**
>   as a non-sequitur — a biconditional between fixed propositions cannot be
>   refuted by comparing two fixed forms.  Replaced by the stronger, proved
>   **Theorem 8bis.4a**: `ω̂_fin(0) = Σ_p(log p)2p^{−1/2}/(1−p^{−1/2}) > 0` at
>   every chart, and `Π(φ(·/T))` is primitive with transform concentrated at
>   `τ = 0`, so **positivity fails on the pure Frobenius form,
>   unconditionally**.  The colimit version is `OPEN` and is not asserted.
> * **The quarantined converse (M2/LF2, M3/LF1)**: the tests are now primitive
>   **by construction** via `Π`, the import is restated with **no Tate clause**
>   (the round-4 clause was false: the polar terms `≍ L²e^L` dominate) and
>   renamed **(Wgr)**; the two-coefficient primitivization (wrong by `e^{5L/4}`)
>   is replaced by a minimal correction of sup norm `O(Le^{−L/2})`; and the
>   partition-of-unity lemma — **false** for a general mass-one bump, by
>   Poisson — is proved with a genuine smooth partition of unity and a
>   **pointwise** argument.
> * **Bookkeeping (M6)**: the P123.038 §5 ledger row is re-graded (announced
>   twice before and not done); §11's "External inputs: none" is replaced by
>   the three named `CLASSICAL` imports of §8bis, each *used by no clause of
>   B.1–B.9*; Theorem 8.2's independence claim carries the carve-out.
>
> Report: [R131.013](../../03-research/phase-131-row-b-closure/R131_013_BUILDER_ROUND5.md).

> **Status, 2026-09-12 (phase 131, round 6) — a false import withdrawn.**  The
> lead audit `R131.015` (LF5) found — the hostile pass did not — that the
> `CLASSICAL` import **(Wgr)** of Theorem 8bis.7 is **false**.  For the
> single-frequency test `g_L = ψ(t/L)e^{−iγ_0t}` with `ψ ≥ 0`, on-line zeros
> contribute `|ĝ_L(ρ)|² ≥ 0` and the **resonant** off-line pair contributes
> `2ĝ_L(ρ_0)ĝ_L(1−ρ̄_0)` with **both factors positive reals**, of sizes
> `e^{δL}` and `e^{−δL/2}` — hence `≍ +e^{δL/2}`: **positive**, with **half**
> the exponent `(Wgr)` claimed.  And structurally, for **any** amplitude
> `w ≥ 0`, `ĝ(ρ_0) = ∫we^{δt} ≥ ∫we^{−δt} = ĝ(1−ρ̄_0) > 0`, so no non-negative
> amplitude and no real tilt can peak the transform at `1−ρ̄_0`.  All of this
> is proved (**Lemma 8bis.6b**); **(Wgr)** is **withdrawn** (§9bis W23) and
> cited nowhere.
>
> **Theorem 8bis.7 is restated as a conditional transfer theorem.**  Its
> analytic machinery is **proved in full** — including new **Lemma 8bis.6a**,
> `‖(g−g_D)′‖_∞ = O(‖g‖_{C¹})`, whose proof turns on the cancellation
> `Σ_kρ′(x−k) ≡ 0` in the partition of unity (without it the naive bound is
> `e^{L}` and the error would **dominate** the main term for `|β−½| < ¼`) — and
> its arithmetic input is isolated as one explicit hypothesis `(H_L)` with a
> scale-invariant ratio, recorded **`OPEN`** with the obstruction quantified.
> So "positivity on Dirichlet-polynomial profiles ⟹ RH" is **`OPEN`** and is
> **not claimed**.  Imports are now **two**, both `CLASSICAL` and quarantined:
> Weil's criterion and Chebyshev.
>
> Also: Thm 8bis.2 is **explicitly exempted** from the colimit convention (N1,
> and under `T_∞` the result is *easier*); the displays themselves are
> renumbered (N2 — round 5 renumbered only the references); and the withdrawn
> symbol-comparison argument is **purged** from §0, the banner, this README's
> round-4 block and §9bis W17 (N4, N5, m5′), the conclusion now citing
> Thm 8bis.4(iii).  Report:
> [R131.016](../../03-research/phase-131-row-b-closure/R131_016_BUILDER_ROUND6.md).

> **Status, 2026-09-12 (phase 131, round 7) — apparatus only.**  The hostile
> audit `R131.017` found that **three repairs reported as done in round 6 were
> not in the file** (§0's withdrawn sentence, the banner bullet, Theorem 8.2's
> garbled carve-out), that round 6 had **recreated** two dangling equation
> references in the very passage written to repair dangling references, and
> that the new hypothesis `(H_L)` covered only **one** of the two error terms
> its own proof produces.  All five `MAJOR` items and all nine minors are
> repaired, and — the hard rule of this round — **every one is verified by a
> pasted `grep`/`sed` output** in
> [R131.018](../../03-research/phase-131-row-b-closure/R131_018_BUILDER_ROUND7.md),
> not described in prose.  A mechanical cross-reference pass over every
> `(8bis.NN)` token now returns an **empty diff** in both directions with no
> double assignment.  `R(L)` in `(H_L)` now covers **both** error terms and the
> unstated side condition is deleted, so Theorem 8bis.7(a) follows from
> `R(L) → 0` alone.  Lemma 8bis.6b gains (ii′) — the conjugate pair is bounded
> by the **same** order, so `(Wgr)`'s *modulus* claim is refuted outright while
> its *sign* claim is refuted only in its mechanism — and (v), the same
> conclusion for the **primitivized** tests, with coefficient `2Re(A²)`
> (**not** `2|A|²`).  §11's import list says **two**, as §10 always did.
> **No new mathematics; no label claimed.**

[main.md](main.md) — complete construction and proofs.  Phase-128 corrections
and phase-131 withdrawals (§9bis, W1–W23) are kept in place.
