# R130.002 — Audit, round 1 (phase 130, row A closure)

phase-130 rebuild, against `R130_000_BLUEPRINT.md`,
`R130_001_REPORT.md` and `P123_A_ACCEPTANCE_SPECIFICATION.md` §§2, 4.
Standard: `R129_006_AUDIT_ROUND3.md`.  Everything below was re-derived; the
"What survives" section lists what I checked line by line and found correct.

---

## 1. Findings

### F1 (FATAL, repairable) — Def. 10.6c and Thm 10.7(b): `M` is not defined on `𝓐_tr`, so `λ_RR` is not defined there, and 10.7(b) is false as stated

*Location:* Definition 10.6c ("for `F,G ∈ 𝓐_tr`, `λ_RR(F,G) := (L_S(F,G),
λ_per(MF,MG))`"); Theorem 10.7(b) ("`λ_RR` is continuous on `𝓐_tr × 𝓐_tr` …
for `‖·‖_tr`").

*The error.*  `λ_±` are **unbounded** for `‖·‖_tr`, hence do not extend to the
completion, and `λ_per(MF,MG)` is undefined for a general element of `𝓐_tr`.
The paper's own spread Tate characters are the counterexample.  For `F_n` of
(9.21): `‖F_n‖_{L^1} = ∫ψ(s)e^{−ns/2}ds ≤ ‖ψ‖_1 e^{−na/2}`, and by the
two-integration-by-parts bound used in Thm 9.14c(b),
`|\hat F_n(τ)| ≤ min(‖ψ‖_1 e^{−na/2}, C_ψ/(n²τ²))`, so
`N(F_n) = O(e^{−na/2}) + O(n^{−2}) → 0`.  Hence `‖F_n‖_tr → 0` **while
`λ_+(F_n) = 1` exactly**.  Therefore `λ_+` is unbounded on the `‖·‖_tr`-unit
ball (`λ_+(F_n/‖F_n‖_tr) → ∞`), `M` has no continuous extension to `𝓐_tr`,
and the second component of `λ_RR` is neither defined nor continuous there.
The proof of 10.7(b) half-admits this ("on `𝓐_tr` the functional
`λ_∓(F) = \hat F(∓i/2)` is the analytic continuation, and (b) is asserted on
`D_A` and its `N_A^{dist}` completion") — i.e. the proof does not prove the
statement.

*Why it matters.*  "Convergence" is one of the five things clause A.8 names,
and §14's A.8 line cites "(b), on the Banach algebra `𝓐_tr`".  As written,
A.8's convergence is proved only for the **scalar** component.

*Repair (cheap).*  Replace `𝓐_tr` in Def. 10.6c/10.7(b) by the completion of
`D_A` for `‖F‖_tr^{Tate} := ‖F‖_tr + ∫|F(w)|(|w|_S^{1/2}+|w|_S^{−1/2})d^*w`.
This is still submultiplicative (`λ_±` are characters, so the weight is
sub-multiplicative), `M` extends continuously by construction, and every other
statement of 8A.7b goes through verbatim.  Then say explicitly that `𝓐_tr`
itself carries only the scalar half of `λ_RR`.

### F2 (MAJOR) — Thm 10.8 and Thm 10.7(e): "the continuous extension of `L_S` to `σ(B_T)`" is not a well-defined object

*Location:* Thm 10.8 statement and proof; Thm 10.7(b) last clause; Def. 10.6c's
third line (`λ_RR(σ(b),σ(b')) := (unit, λ_per(b,b'))`).

*The gap.*  `L_S` is a pairing of two elements; `N_A^{dist}` is a numerical
**module**, and the paper itself quotes P123.017 §6 (§9.3.6) that "products of
two arbitrary elements are not defined" there.  What Thm 10.8 proves is that
**along the two particular sequences** `F_n, G_m` of (9.21) one has
`I_A(F_n,G_m) → 0`.  It does **not** prove that the double limit is
independent of the approximating nets, and it cannot follow from convergence
in `D_A'`: strong-dual convergence controls `I_A(F_α,G)` only for `G` ranging
over **bounded** subsets of `D_A`, and `{F_n}` is unbounded in `D_A` (its
supports grow linearly in `n`).  So "the continuous extension of `L_S` to
`σ(B_T)×σ(B_T)` is trivial" is an assertion about an extension whose existence
and uniqueness are unproved; Def. 10.6c in fact **declares** the value by fiat.

*Consequence.*  Thm 10.7(e)'s first display
(`λ_RR|_{σ(B_T)×σ(B_T)} = (unit, λ_per)`) is a definition, not a theorem, and
Thm 10.8's slogan "the vector target is forced" is supported only in the weaker
form: *there exist approximating sequences of the rulings along which the
scalar line degenerates to the unit while the Tate line tends to `λ_per`.*

*Repair.*  Either (i) prove net-independence — e.g. show
`lim I_A(F_α,G_β) = 0` for **all** nets with `J(F_α)→σ(e_+)`,
`J(G_β)→σ(e_−)` and a uniform `‖·‖_tr`-type bound, and state that bound as a
hypothesis in the definition of the extension; or (ii) restate 10.8 as the
sequence-wise statement it proves, and state 10.7(e) on `σ(B_T)` as a
definition consistent with those limits.

### F3 (MAJOR) — Thm 10.7(e) has almost no content beyond Thms 9.14a–c, and (10.10) is bi-additivity

*Location:* Thm 10.7(e), display (10.10); §14's A.8 line; §14.2 status block.

Since `λ_RR := (L_S, λ_per∘(M×M))` **by Definition 10.6c**, part (e) reads:
the second component of a pair is its second component, and the first
component of `σ(m)` is `0`.  The proof of (e) is three lines of exactly that.
In logarithms (10.10) is
`(I_A(F,G), β_T(MF,MG)) = (I_A(F,G),0) + (0,β_T(MF,MG))`, i.e. the
decomposition of an ordered pair.  The **non-tautological** content of "A.8
extends `λ_per`" is therefore exactly: (i) Thm 9.14a — the rulings are limits
of test classes in `N_A^{dist}`; (ii) Thm 9.14b — the canonical splitting;
(iii) Thm 9.14c(b) — `I_A(F_n,G_m)→0` while `β_T → 1`; plus the consistency of
the fiat value in Def. 10.6c (F2).  That should be said in those words in
Thm 10.7(e) and in §14; as written, (e) and (10.10) read as substantive
theorems and are not.  This is the single largest inflation in the rebuild.

### F4 (MAJOR) — Thm 8A.9 (O-A5-5): (8A.24) conflates "Haar-regularized rank" with the half-density weight; at non-unit shells the regularized rank is `1`, not `τ_p`

*Location:* Thm 8A.9(a) vs (b) vs (c), display (8A.24).

Part (a) says: at `v_p(w_p) ≠ 0` the local shadow factor is `C[0]` of **rank
1**, and "the half-density normalization of §5.2 assigns it the weight
`τ_p(w_p) = p^{−|v_p|/2}`".  Part (b) says: at a unit the **regularized rank
itself** is `1/|1−w_p|_p = τ_p`.  These are two different quantities: in (a)
the rank is `1` and the factor `p^{−|k|/2}` comes from a *separate declared
normalization* (§5.2 half-density), in (b) it is the regularized rank.  The
paper's own §7.2 says this in as many words: "At a non-unit twist the same
trace is the half-density `|σ_p|^{1/2}` alone."  Hence (c)'s justification —
"the integrand `τ_v` of (8.5) **is** the Haar-regularized rank" — is false at
the non-unit shells unless `rk^{Haar}` is *defined* to include the
half-density, in which case (8A.24) is a definition, not a comparison.

*Effect on the clause.*  (O-A5-5) asked for a comparison of the categorical
shadow with `Tr_A`.  What is proved is the unit-shell half (b); the non-unit
half is a relabelling.  Rem. 8A.9a's honesty note ("the regularization is a
declaration") softens but does not remove this: the declaration is *different*
in the two regimes.  Repair: state (8A.24) with `rk^{Haar}` replaced by
"Haar-regularized rank **times** the §5.2 half-density", and say that at
non-unit shells the shadow contributes only the rank `1` and all arithmetic is
in the half-density (which is the true and interesting statement, and is
Remark 7.3).

### F5 (MAJOR) — Thm 10.6a does not prove the round-4 requirement (A.8-I) unsatisfiable; its hypothesis is smuggled in

*Location:* Thm 10.6a, its *Consequence*, §13.8 item 1, §14.0 row `A.8-I`.

Thm 10.6a as stated is **correct**: no functor whose value depends *only* on
`M(s(K))` can determine `Tr_A` (Thm 9.5 + Thm 9.12(T3)(i) give two classes with
equal `M` and different `T`).  But round 4's (A.8-I) (§10.2) asks for a monoidal
functor `Φ_det : Corr_A^{tr} → (ruling category)` carrying `Tr_A` to `λ_per`
and `M` to the two ruling directions — it does **not** stipulate that `Φ_det`
factors through `M(s(K))`.  A functor into a Picard category of lines can carry
strictly more information than the bidegree (the line's metric is a continuous
parameter).  So the conclusion "there is none, **for any construction
whatsoever**" is a non sequitur; what is proved is "there is none *of the
Tate-fibre-factoring type*".  Since the withdrawal of (A.8-I) is the hinge of
the entire A.8 reformulation, this must be repaired: either add the factoring
hypothesis to the withdrawal ("the requirement, read as a functor through the
Tate fibre, is unsatisfiable; read otherwise it is not addressed here"), or
prove the stronger statement.  (I believe the stronger statement is provable —
"carries `M` to the ruling directions" plus monoidality is close to forcing the
factorization — but it is not proved in the paper.)

### F6 (MAJOR) — §14.1 item 4: the "chart artifact" inference is backwards

*Location:* §14.1, "What rows B, C and D must take from this", item 4.

The text argues: outside the support window the colimit form differs from the
chart form by the finite sum (8A.21), "whose terms are **positive** for
`F ≥ 0`; so the positive part of the index in Theorem 14.1(b) at finite `S` is,
beyond the window, an artifact of having truncated the place set".  The sign of
the correction points the other way: for real `F ≥ 0`, `H = F⋆F^† ≥ 0`, so
`W_ℓ(J H) ≥ 0` and `I_∞(F,F) ≥ I_A^S(F,F)`.  Adding places makes the form
**more** positive, not less; nothing here suggests the finite-`S` positive
index is an artifact.  (The honest statement is: inside the window the two
forms agree exactly, and outside it the comparison is only known on the
positive cone, where the correction is non-negative.)  Since this paragraph is
the paper's hand-off to rows B and D on signature, the error is not cosmetic.

### F7 (MAJOR) — the carrier is split: A.1/A.2 are discharged on the colimit `D_A^∞`, A.6–A.8 only per chart `S`, and the colimit numerical theory is admitted unproved

*Location:* Thm 3.8(e); §3.3bis A.1/A.2 verdicts; Thm 8A.7c; §13.8's closing
paragraph (`𝓝_∞ = 0` NOT CLAIMED); §14 ledger.

Specification §1 demands that all the structure "belong to one theory on one
carrier".  In the rebuilt paper: A.1 and A.2 are closed **by** the chart system
and its colimit `D_A^∞` / `Corr_A^{tr,∞}`; A.5's chart-invariance (O-A5-2) is
closed **on** `D_A^∞`; but A.6 (`𝓝 = 0`, nondegeneracy, `N_A = D_A`), A.7's
completion `N_A^{dist}`, the ruling plane `σ(B_T)` and A.8's `λ_RR` all live at
a **fixed finite `S`**, and §13.8 states that the colimit analogue `𝓝_∞ = 0`
is not claimed and is believed to need zeta zeros.  Thm 3.8(e)'s phrase "the
colimit … carrying `T_∞`, `I_∞`, `M` **and the exact Tate sequence (9.17)**" is
therefore misleading: (9.17) has middle term `N_A = D_A`, an identification
that rests on `𝓝 = 0`, which is exactly what is not available on `D_A^∞`.
Moreover Thm 9.7b(c) shows the chart dependence is not formal: the Tate
residue of `T̂_S` is `∓i(|S_f|+1)`, so the numerical theory genuinely moves
with `S`.  This is not fatal — one may declare the carrier to be a fixed chart
with the chart system as extra structure — but the paper must **say which**,
and §14's "PROVED on the declared carrier" must name it.  As written, each
clause picks the carrier that suits it.

### F8 (MAJOR) — A.2, "closed under its declared completion": the completions are of the test algebra, not of the category

*Location:* §3.3bis, "Clause A.2: `PROVED`"; §14 A.2 line.

The evidence offered is: "the analytic completion of the section algebra is
`𝓐_tr` (Thm 8A.7b(a)) and the numerical completion is `N_A^{dist}`".  But
`Corr_A^{tr}` is the category of **presented complexes of smeared objects
`E_F`, `F ∈ D_A`** (Def. 8A.1).  No object `E_H` is constructed for
`H ∈ 𝓐_tr ∖ D_A` (the Fell-section construction of Cor. 3.4 is for `D_A`),
and `N_A^{dist}` is not an algebra at all, so it does not index objects.  So
the category is **not** shown closed under either completion; two completions
of the coefficient algebra are shown to exist.  A.2 should read `PARTIAL`
unless objects over `𝓐_tr` are constructed (which looks routine: extend
`F ↦ E_F` by `‖·‖_tr`-continuity using Thm 8A.10(ii)'s `λ`-realization).

### F9 (MAJOR) — internal contradiction about the boundary radical `R_∂`, and the identification with P123.007 §4 is not a proof

*Location:* §9.3.6 ("Obstacle (O-A6-2) is closed … P123.007 §4's `R_∂` … does
**not survive**") versus Thm 9.14c(a) and Rem 9.14d(3) ("Theorem 9.14c computes
it: it is **exactly the ruling plane**", two-dimensional) and §14.0's
`O-A6-2` row ("Thm 9.14c identifies P123.007 §4's `R_∂` **exactly**").

Both sentences are about the same named object and they say opposite things
(zero vs two-dimensional).  Worse, they are about *different* pairings and
*different* completions: P123.007 (4.2) defines
`R_boundary = {x ∈ completion(N_A^c) : I_A(x,y) = 0 ∀ y ∈ completion(N_A^c)}` —
a radical taken against the whole completion of a **different** ambient object
(`N_A^c`, P123.007's own completion), whereas (9.24) defines `R_∂` against the
**dense test sector** `D_A` inside this paper's `N_A^{dist}`.  Since `I_A` does
not extend to pairs from the completion (the paper says so), P123.007's
definition cannot even be evaluated here.  So "`σ(B_T)` **is** P123.007 §4's
`R_∂`" is an analogy, not a theorem, and it is used rhetorically three times
(Thm 9.14c title, Rem 9.14d(3), Rem 10.8a(3), §14 A.6 line).  Repair: keep
(9.24) as a **definition internal to this paper**, prove `R_∂ = σ(B_T)` (which
is correct and is a one-line consequence of 9.14b), and drop or heavily qualify
the identification with P123.007; and fix the §9.3.6 sentence.

### F10 (MINOR) — Thm 8A.7b(a): the "realization" of `𝓐_tr` is asserted, not proved

The proof shows the natural map `𝓐_tr → L^1(C_S)` is injective and that limits
have the stated norm.  It does **not** show that every `H ∈ L^1` with
`∫|\hat H|(|T̂|+|c|)dχ < ∞` is in the image — i.e. that `D_A` is dense in that
space for `‖·‖_tr`.  (Plausible by mollification, but the simultaneous
convergence of `\hat F_j → \hat H` in `L^1((|T̂|+|c|)dχ)` needs an argument.)
Either prove it or state the realization as an inclusion.

### F11 (MINOR) — Def. 8A.7d reason (iii): "the intrinsic Mittag–Leffler constant" is not canonical, so the claimed uniqueness of `c := 0` is empty

A Mittag–Leffler expansion is canonical only up to an entire function, and the
constant term depends on the chosen convergence-factor grouping: in (9.7b.2)
the constant `log π + γ` is what is left after grouping the poles with
`−1/(n+1)`; a different (equally standard) grouping moves a constant between
the bracket and the constant term.  Likewise at `p`, `−log p` is the constant
relative to the symmetric grouping in (9.7b.8).  So reason (iii) — "`c = 0` is
the unique choice for which the identity coefficient is the sum of the
intrinsic local constants and nothing else" — has no invariant content.  The
the construction was right to strike the blueprint's reason (ii); reason (iii) is the
same kind of claim.  What survives, and is enough: `c` is a declared parameter
(reason (i)), must be chart-independent (reason (ii)), and `c := 0` is a
declaration.  Say only that.  (Note the consequence is real: by Thm 14.1(b) the
signature of the theory is a function of `c`, so a declared `c` means a
declared signature.)

### F12 (MINOR) — Rem. 9.7c(3) and Rem. 10.8a(2): "no normalization of `I_A^S` gives hyperbolic coefficient 1" is false as literally stated

Rescaling `T̂ ↦ T̂/(|S_f|+1)` is a normalization and gives residue `∓i`.  The
true statement is the one 9.7b(c) proves — the residue is `|S_f|+1` times the
archimedean one and therefore **chart-dependent**, so no *chart-independent*
normalization does it.  Fix the wording; the argument of Rem 10.8a is not
otherwise affected.

### F13 (MINOR) — (8A.13) is not corrected in place, and Thm 10.5(i) is declared to "stand" while asserting it

Thm 8A.7's display (8A.13) at line 1478 still reads as an unconditional
identity, with the correction appearing only 350 lines later (Rem. 8A.7e) and
in §13.8.  Thm 10.5 carries the marker "parts (i)–(vi) below stand", and part
(i) is precisely "*existence and convergence*: (8A.13)".  So the paper does
still use (8A.13) unconditionally, in a passage explicitly blessed as standing,
contradicting "Nothing in this paper uses (8A.13)".  Repair: mark (8A.13) in
place, and amend 10.5(i) to (8A.13′).

### F14 (MINOR) — Thm 10.9(c): the unitization is ignored in the `I²` step

`I = ker(M : D_A^+ → B_T)` contains elements `F + c·1` with `λ_±(F) = −c ≠ 0`;
the proof writes "if `F,G ∈ I` then `\hat F(±i/2) = 0`", which is false for
those elements.  The argument is repaired by working with the symbol
`\hat F + c` of `F + c·1` (the unit has symbol `1`), for which the double-zero
argument goes through verbatim, and `∂_±` is unchanged since `∂_τ c = 0`.  The
conclusion `I/I² ↠ C²` is correct (see "What survives").

### F15 (MINOR) — §11bis item 5(iii): the "span Weil's proof uses" is not in the trace-class domain

`Δ = E_1` and the `E_a` are delta-type graph objects; Remark 8.11 states that
`Δ` is **not** trace class, and `Corr_A^{tr}` consists of smeared objects.
So "`Δ = E_1`, the normalized Frobenius powers are `E_a`, … the span is
available" is a statement about `G`, not about the domain on which `Tr_A`,
`I_A`, `M` and `λ_RR` are defined.  The rulings, by 9.14a, are in yet a third
object (`N_A^{dist}`).  The three live in three places; item 5(iii) should say so.

### F16 (NOTE) — "compatible with determinant" (A.5) is definitionally true

`Det_S^{rel} := \exp T` (Def. 8A.2).  So the determinant-compatibility bullet
of §8A.4 asserts that `exp` of the trace is `exp` of the trace, continuously.
The genuine content is 8A.7b(d)–(e) (the germ and its multiplicativity), which
is real work; the bullet should be phrased as such rather than as compatibility
with an independently given determinant.  Similarly, the enlarged target
`T_A = Pic_b(B_T)` is declared for A.8's sake while `Tr_A` lands in the first
factor only; A.5 is therefore verified against a target whose second factor it
never uses.

### F17 (NOTE) — Thm 10.7(a) `†`-compatibility: the proof chain is garbled, the conclusion is right

The displayed chain "`I_A(F^†,G^†) = T(F^†⋆G) = \overline{T(G^†⋆F)} =
\overline{I_A(G,F)} = I_A(F,G)`-conjugate" mislabels the middle terms
(`G^†⋆F = F⋆G^† = I_A(F,G)` by commutativity, not `I_A(G,F)`).  The correct
one-liner is `(F^†)^∧ = \overline{\hat F}` and `T̂` real, whence
`I_A(F^†,G^†) = \overline{I_A(F,G)}`, matching the Tate component's
`β_T(MF^†,MG^†) = \overline{β_T(MF,MG)}`.  Verified; only the prose needs fixing.

### F18 (NOTE) — A.7's "to the extent needed by Riemann–Roch" is discharged against a Riemann–Roch that asserts no inequality

Thm 10.3c is (a) positivity of the bidegree, (b) stability, (c) `e^{−x} ≤ 1`
for `x ≥ 0`, (d) an explicit refusal to assert a sign, (e) a restatement.  That
is a correct but very thin reading of the clause; it is *fair*, because the
clause's own text is weak and A.8 supplies no sign, and Rem. 10.3d's argument
that `C*`-factorization-lifting belongs to a different cone (Thm 10.2(e)) is
sound.  Recorded so that no one later reads A.7 as more than this.

### F19 (NOTE) — Thm 9.7b is proved for the even archimedean component only

(9.7b.2) and (9.7b.6) are stated and proved for `ε = 0`, and the paper says the
odd symbol has no closed form in the corpus.  That is enough for everything
that uses it (the rulings live on `𝔠_0`), and Thm 9.7(b)'s asymptotic covers
both parities.  No defect; recorded because the A.8 narrative ("every place has
the universal Tate residue") is a statement about `𝔠_0` only.

### F20 (NOTE) — A.1's reading

The construction's self-report is accurate and I endorse the way it is flagged: what
is constructed is a filtered chart system with a retraction and a
chart-invariant global trace.  Clause A.1 says "Restriction, descent and the
coefficient comparison maps must be constructed"; it does not define "descent".
Reading it as the chart datum is defensible; reading it stack-theoretically
makes A.1 `PARTIAL`.  I do not call this a finding against the paper — but the
label in §14 must carry the reading note, which it does.

---

## 2. What survives

Re-derived in full and found **correct**:

1. **Thm 9.7b(a)** — the Mittag–Leffler form of `Ŵ_p`.  I recomputed
   `2Re(ζ/(1−ζ)) = 1/(1−e^{−w}) + 1/(1−e^{−w̃}) − 2` with
   `w = L/2 − i(τL+θ_p)`; `1/(1−e^{−z}) = ½ + ½\coth(z/2) = ½ + Σ^{sym}1/(z−2πik)`;
   `w̃ − 2πik = iL(τ − τ_k^+)`, `w − 2πik = −iL(τ − τ_{−k}^−)`; hence the
   constant `−\log p`, the poles at height `±½` only, simple, residues `−i`
   at `τ_k^+` and `+i` at `τ_k^−`.  The re-indexing inside the symmetric sum
   is legitimate.  Periodicity `2π/L` verified.
2. **Thm 9.7b(b)** — from Gauss's series for `ψ`,
   `n+¼±iτ/2 = (±i/2)(τ ∓ ω_n)`, giving
   `Re ψ(¼+iτ/2) = −γ + Σ[1/(n+1) + i/(τ−ω_n) − i/(τ+ω_n)]` and hence
   (9.7b.2), simple poles at `±ω_n`, residues `∓i`, `ω_0 = i/2`.  Consistent
   with (a): the universal residue is genuine.
3. **Thm 9.7b(c)** — `θ_p = 0` on `𝔠_0`, so the total residue is `∓i(|S_f|+1)`.
4. **Thm 9.7b(d)** — the contour identity.  Poles of `Ŵ_p` lie exactly at
   heights `±½`, so shifting to `Im τ = h > ½` crosses only the family at
   `+½`; verticals at `Re τ = 2π(j+½)/L` avoid all poles by periodicity and
   `|Ŵ_p|` is bounded there uniformly in `j`; on the horizontal lines
   `|e^{−w}| = e^{−L/2−yL}`, `|e^{−w̃}| = e^{−L/2+yL}` stay away from `1`, so
   `Ŵ_p` is bounded; Paley–Wiener decay of `\hat F` kills the sides and makes
   the residue sum absolutely convergent.  Orientation and the factor
   `2πi(−i) = 2π` check out.  **(9.7b.5)** is Poisson for `g = f e^{t/2}`,
   `Σ_k \hat g(2πk/L) = LΣ_m g(mL)`, correct.  **(9.7b.6)** likewise
   (`ω_1 = 5i/2`, so `½ < h < 5/2` isolates `ω_0`).
   Normalization `dχ|_𝔠 = dτ/2π` is consistent with Thm 9.7(d).
5. **Lemma 9.14a0** — correct: bounded sets of a strict LF space sit in one
   Fréchet step, `U_N`-invariance leaves finitely many components, two
   integrations by parts give `|\hat G| ≤ C\min(1,τ^{−2})` uniformly, and
   `|T̂| = O(\log(2+|τ|))` by Thm 9.7(a),(b).
6. **Thm 9.14a (a)–(e)** — fully correct, and stronger than the blueprint.
   `F_n ∈ C_c^∞(C_S)` genuinely (smooth in the `R^×` coordinate, constant on
   the compact part, compact support).  `λ_+(F_n) = 1` exactly,
   `λ_−(F_n) = ∫ψ(s)e^{−ns}ds = O(e^{−na})`,
   `\hat F_n(τ) = ∫ψ(s)e^{−ns(½+iτ)}ds` supported on `𝔠_0` with
   `\sup_τ|\hat F_n| ≤ ‖ψ‖_1 e^{−na/2}` — the construction's correction of the
   blueprint's `O(1/n)` to an exponential bound is right.  Convergence
   `J(F_n) → (0,e_+)` is in the **strong** dual (uniformly on bounded sets),
   with the bound proved via 9.14a0.  The eigenvector statement (e) is correct
   and is, as Rem. 9.14d(1) says, true **by definition** of the module
   structure on the `B_T` component.
7. **No contradiction with Thm 9.13(a)** — verified.  9.13(a) is a statement
   about `D_A`-eigenvectors inside `N_A = D_A`, whose proof compares
   `\hat a(χ_0)` on the unitary axis with `\hat a(∓i/2)` off it; the limit
   vectors have zero distribution component and lie outside `J(N_A)`
   (Thm 9.14c(c), which I checked: `J(F) ∈ R_∂ ⇒ F ∈ 𝓝 = 0`).
8. **Thm 9.14b** — correct, including the point the checklist asks about:
   `(ℓ,m) ∈ N_A^{dist}` and `σ(m) ∈ N_A^{dist}` give `(ℓ,0) ∈ N_A^{dist}` by
   linearity of a closed subspace; `σ` is a `D_A`-module map because the action
   on the second factor is through `M`; both summands are closed and the
   projections continuous.  The splitting is genuinely canonical.
9. **Thm 9.14c(b)** — correct: two integrations by parts in `s` give
   `|\hat G_m(τ)| ≤ C_ψ\min(1,(m|τ|)^{−2})`, hence `N(G_m)` bounded uniformly
   in `m` (indeed `O(m^{−1}\log m)`), so `|I_A(F_n,G_m)| ≤ ‖ψ‖_1C_ψC_S e^{−na/2}`
   → 0 uniformly in the other index, in both parities and on all components
   (only `𝔠_0` is met), with the `\log` growth of `T̂` correctly absorbed.
   `β_T(MF_n,MG_m) → 1`.  This is the real content behind A.8(e) and it holds.
10. **Thm 8A.7b(a)–(e)** — correct, modulo F10.  `‖F⋆G‖_tr ≤ ‖G‖_{L^1}‖F‖_tr
    ≤ ‖F‖_tr‖G‖_tr`: submultiplicative with constant **1**, as the construction
    claims against the blueprint's `2`.  `‖F^†‖_tr = ‖F‖_tr`.  Power estimate
    (8A.17) correct.  The germ converges on `|z| < 1/‖F‖_{L^1}`, the
    interchange in (8A.19) is dominated correctly, and (8A.20) is exact — the
    principal-branch argument (`1+z\hat F` and `1+z\hat G` in the disc of
    radius 1 about 1, so arguments in `(−π/2,π/2)`) is right.  (f) is a correct
    bound for the unit-packet germ.
11. **Thm 8A.7c(a)–(e)** — correct.  `|δ_S(ℓ^{−k})|_S = ℓ^{−k}` gives the
    support window; stabilization and exact chart-invariance of `T_∞` follow
    from (8A.12) once `c` is chart-independent; `M∘J_{ST} = M` is a correct
    computation from the measure normalization.
12. **Thm 8A.10** — injectivity of `F ↦ E_F` is proved, twice, and both proofs
    are valid (the second uses faithfulness of the regular representation of
    `L^1` of a LCA group, correctly argued).  **Thm 8A.11**: deleting
    requirement (a) is justified by the correct classical observation
    `Tr(nΓ) = n\,Tr(Γ)` with `nΓ` and `Γ` having the same support; and the
    the construction was right to refuse the blueprint's bogus `E_{2F} ≅ E_F`.
13. **Thm 10.3b (O-A7-1)** — correct and is, in my judgement, the best new
    argument in the phase.  Nets rather than sequences (right, the strong dual
    need not be metrizable); `M(F) ∈ R_{≥0}²` on the cone with both limits in
    the closed quadrant forcing `m = 0`; AM–GM `|w|^{1/2}+|w|^{−1/2} ≥ 2` giving
    `‖F‖_{L^1} ≤ ½(λ_++λ_−) → 0`; then `\sup|\hat F_α| → 0` and
    `ℓ = 0` by 9.14a0.  Clean.
14. **Thm 10.6a** — the statement (as opposed to its "consequence", F5) is
    correct.
15. **Thm 10.9(b),(c)** — `Tor_1^R(R/I,R/I) ≅ I/I²` is the standard
    computation, correctly done; `∂_±(F) = ∂_τ\hat F(±i/2)` kills `I²`
    (double zero) and `(∂_+,∂_−)` is onto `C²` because
    `e^{t/2}, e^{−t/2}, te^{t/2}, te^{−t/2}` are linearly independent — I
    verified the four-functional surjectivity argument.  So `M` is not a
    homological epimorphism and P123.008 §7's Tor is nonzero of dimension
    `≥ 2`.  Strict monoidality on **based free** complexes is trivially true as
    stated (`R^m⊗_R R^n = R^{mn} ↦ B_T^{mn}`) — correct, though it is a
    statement about free modules and not about `Corr_A^{tr}`.
16. **Thm 3.8(b)** — `R_{TS} = (π_{TS})_*` is well defined, lands in `D_A(S)`,
    is a `†`-algebra homomorphism (Weil's integration formula with the
    probability normalization), and `R∘J = \mathrm{id}`.  **Prop 3.9** and its
    structural reason are correct.
17. **Norm conventions** — (8A.10″) `‖1‖ = |s|^{−1/2}` reproduces
    `A_MIXED_METRIC_WORK` (6)–(7) (`‖1‖ = \exp(−I/2)`) and Paper 42's fixed
    ruling line `‖1‖ = \exp(−d_1d_2)` from `‖1‖² = \exp(−Re β_T)`.  Consistent
    across Def. 8A.2, Def. 8A.2′, Def. 10.6a–b.  No defect found here.
18. **A.10 / the imports** — I found no use anywhere in the phase-130 passages
    of a zeta zero, of RH, of `Λ(n)` as an input, of Meyer's explicit formula
    or of positivity.  `\log p` enters as a shell volume and `p^{−|k|/2}` as a
    proved orbital integral.  Thm 9.7b uses only `\coth` and `ψ`.  And the
    paper does **not** claim `𝓝_∞ = 0`: §13.8 states the non-claim explicitly,
    and I could find no place where the colimit radical is used (subject to
    F7's wording issue in Thm 3.8(e)).

---

## 3. The renaming test (closure rule §4)

The rule: the label requires an adversarial audit confirming that **none of
A.2–A.8 is merely a renaming of the scalar explicit formula**.

*The case for the prosecution.*  Remark 9.7a concedes that `T̂` is **verbatim**
the prime-power-plus-Gamma side of the explicit formula.  Everything numerical
in A.5–A.8 is then Fourier analysis of that one symbol: `I_A(F,G) =
∫\hat F\overline{\hat G}\,T̂`, `𝓝 = 0` is "`T̂` is not a.e. zero", `λ_±` are the
two Tate values `\hat F(∓i/2)`, Thm 9.7b is the classical pole/residue analysis
that *proves* the explicit formula, and (9.7b.4)–(9.7b.6) is literally the
contour derivation of it.  A.8's object `λ_RR = \exp(I_A, β_T∘M)` is the pair
(explicit-formula pairing, Tate degrees), and its "equality formula" (10.10) is
the statement that a pair is the sum of its components (F3).  On that reading
A.8 *is* a renaming — of the explicit formula plus two of its residues.

*The case for the defence.*  (i) A.2–A.4 are not numerical statements at all;
they are category/involution/excision statements on `G` and are not renamings of
anything analytic.  (ii) A.6's content — `𝓝 = 0`, the canonical exact sequence,
the *non*-existence of a module splitting (9.13(a)), and the existence of the
rulings in the completion with a canonical splitting there (9.14a–b) — is a
genuine structural theorem about the module `D_A` over itself; it is not a
consequence of any explicit formula and uses only the *size* of the symbol.
(iii) A.7's Thm 10.3b is a real theorem with a real proof and no analogue in
the scalar formula.  (iv) A.5's Banach algebra and germ (8A.7b) and the colimit
trace (8A.7c) are constructions, not restatements.

*Verdict on the test.*  **A.2–A.7: PASS.**  They are not renamings; several are
statements the scalar explicit formula cannot express.  **A.8: FAIL as
currently written** — not because the underlying mathematics is a renaming
(9.14a–c are not), but because the clause is discharged by a definition
(Def. 10.6c) plus bi-additivity, so the only thing A.8 adds beyond A.6 is
Thms 9.14a–c, which are already what closes A.6.  A.8 restated honestly — "the
ruling determinant is the Tate component of `λ_RR`, and the consistency of that
definition with the test sector is Thms 9.14a,c" — would be a true and modest
theorem, and would *then* pass the test as a non-renaming, because 9.14a–c are
not restatements of the explicit formula.  As displayed, it does not.

---

## 4. Clause-by-clause verdict

| clause | verdict | reason |
|---|---|---|
| A.1 | **PROVED on the declared reading** (PARTIAL under a stack reading) | §3.3bis is a genuine construction; the reading note is correctly flagged by the construction (F20).  Subject to F7 (name the carrier). |
| A.2 | **PARTIAL** | additive/stable/localized: yes.  "Closed under its declared completion": **not proved** — no objects over `𝓐_tr`, and `N_A^{dist}` is not an object index (F8). |
| A.3 | PROVED on `G` (unchanged) | not re-audited this round. |
| A.4 | PROVED on `G` (unchanged) | not re-audited this round. |
| A.5 | **PROVED with repairs** | O-A5-1a/1b, O-A5-2, O-A5-6 stand (items 10–12 of §2).  O-A5-3 is a legitimate declaration but reason (iii) must go (F11).  O-A5-5 is **not** closed as stated (F4): repair (8A.24) or downgrade to "unit shells proved, non-unit shells by declaration".  F10, F13, F16 minor. |
| A.6 | **PROVED** (amended wording) | and genuinely strengthened by 9.14a–b, which I verified.  Fix the `R_∂` contradiction and the P123.007 identification (F9). |
| A.7 | **PROVED** | 10.3b is correct and is the real theorem; 10.3c is thin but the clause is thin (F18).  Rem. 10.3d's scope reading is fair. |
| A.8 | **NOT EARNED as written; EARNED-WITH-REPAIRS available** | F1 (the vector determinant is not defined on the declared completion — convergence, one of the clause's five named requirements, fails for the Tate component), F2 (the extension to the ruling plane is a fiat, not a proved continuous extension), F3 (part (e) and (10.10) are definitional), F5 (the withdrawal of (A.8-I) is argued under a hypothesis it does not state). |
| A.9 | PASSED for the formalism (unchanged) | |
| A.10 | **PROVED** | verified across every phase-130 passage; `𝓝_∞ = 0` is indeed not claimed (§2 item 18). |

---

## 5. Final verdict

**`WEIL-STRENGTH-COMPLETE` is NOT EARNED at this round.**

It is *close*, and the distance is short and concrete.  What blocks it:

1. **A.8 is not proved as stated** — F1 is a false statement in the theorem
   (the Tate component of `λ_RR` is not defined, let alone continuous, on
   `𝓐_tr`, by the paper's own Thm 9.14a); F2 is an undefined object; F3 means
   that once F1 and F2 are repaired, what remains of A.8 beyond A.6 must be
   restated in its true, much smaller, form.  All three are repairable — F1 by
   changing one norm, F2 by either a uniformity hypothesis or an honest
   restatement, F3 by rewriting (e) — and none requires new mathematics.
2. **A.2 is PARTIAL** (F8) until objects over the completion are constructed.
3. **O-A5-5 is not closed** in the form (8A.24) (F4).
4. **The renaming test fails for A.8 as displayed** (§3), and the closure rule
   makes that test a condition of the label, not a courtesy.
5. Two statements must be corrected because they are handed downstream:
   §14.1 item 4 (F6, the sign inference is backwards) and the `R_∂`
   contradiction (F9).
6. The carrier must be named once and used consistently (F7).

If F1, F2, F3, F4, F6, F8 and F9 are repaired and A.8 is restated honestly, I
would grade the result **EARNED-WITH-REPAIRS** with A.1 carrying its reading
note and A.8 carrying the explicit statement that its content is Thms 9.14a–c.
I would not, on this corpus, grade A.8 as an independent theorem of the
strength the §14 block currently suggests.

What I did **not** find: any error in Thm 9.7b, Thm 9.14a–c, Thm 10.3b,
Thm 8A.7b(a)–(e), Thm 8A.7c, Thm 8A.10, Thm 10.9(c), or any violation of A.10.
Those are real, they are new, and they are correct.
