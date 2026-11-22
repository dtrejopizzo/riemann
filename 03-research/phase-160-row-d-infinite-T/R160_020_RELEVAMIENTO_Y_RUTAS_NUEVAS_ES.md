# Phase 160 — Full survey up to phase 160 and new routes to close D

## 0. Executive conclusion

1. **D is not proved.** It is "closed in the map" in the sense that the program identified exactly its
   content: row D is equivalent to RH. It is not closed in the mathematical sense of having proved its inequality.
2. The cleanest analytic state is:
   - primitive form: positivity proved for `0<T≤log 2`;
   - full form: positivity cited (Zhu, not re-verified in the repository) for `T≤0.8`;
   - **for `T>0.8`, no sign is proved in either form**.
3. Phase 159 built neither object G1 nor mechanism G2. Its real contribution is walls/no-gos and an important
   quantitative result: the margin per window can be at most doubly exponentially small.
4. Phase 160 did a complete survey of the corpus, 18 first-round memos, and only two of the five attacks chosen
   for the second round (`D2`, `D4`). There is no `R160_099_SYNTHESIS.md`; hence phase 160 is incomplete.
5. The bottleneck is no longer finding another equivalent formulation. It is proving, using the exact arithmetic
   of ζ, a uniform sign in `T`, with no margin, no finite truncation, no term-by-term or prime-by-prime positivity,
   and in a way that fails explicitly for the corpus's falsifiers.
6. The route with the best novelty/falsifiability ratio after phase 160 is question `O-D4.1`: use **in the same
   quadratic step** the exact multiplicative identity `Λ*1=log` and the additive/Poisson-Fourier structure. The second
   route is the negative-witness/first-contact program, but it must incorporate that same separating datum so as not to be
   another universal identity.

## 1. What exactly "closing D" means

Three objectives must be distinguished.

### Minimal analytic D

Prove either of the two equivalent statements:

1. `λ^A_T≥0` for all `T>0` (primitive form), or
2. `λ^W_T≥0` for all `T>0` (full form).

Since the initial interval is already covered, the new minimal target is:

> **Theorem D∞.** For all `T>0.8` and every admissible test of the corresponding form, the Weil form of ζ is
> nonnegative.

By Paper 45, Thm 10.4/Bombieri–Weil, this closes D and proves RH. Proving it for each `T` by a different algorithm does not
suffice as a structural explanation: the proved difficulty is the uniform quantifier.

### D in the carrier of rows A–C

Besides the above sign, an internal closure of the program requires that the form on `Frob⋆Δ^rad` be nonnegative
on the primitive/radial part and that the comparison with the analytic form be a theorem. A–C deliver carrier,
composition, dagger, trace and explicit formula, but do not deliver a section, `h⁰`, effective cone or Hodge–Rosati
theorem that produces an inequality.

### Strong geometric D / reopening of Paper 47

The reopening rule requires a single object in the adelic square that simultaneously satisfies:

1. being a positive square after every twist, in the Rankin sense;
2. having a polar divisor determined by local data;
3. having a holomorphic zero contribution to the left of that pole a priori;
4. reading phase and failing for `Ξ_a`;
5. using sum and product at once, failing for `Ξ_Q` and Beurling systems;
6. being uniform across the number field.

This objective is much stronger than finding a new equivalence with RH.

## 2. Map of what has been tried across the whole corpus

The five phase 160 surveys cover the entire corpus up to phase 159. The following compression keeps the
logically distinct families; within each arc there were many computational variants and reformulations.

### Arc I — phases 0–20: locating the inequality

- Hermite–Gauss Gram matrix of the Weil functional, Connes compressions and semibounded realization.
- Kreĭn `E*JE` factorization, de Branges/canonical systems and search for an `A*A` square.
- Place-by-place positivity, Osterwalder–Schrader, Carleson/Bessel and semilocal models.
- de Bruijn–Newman flow, Jensen/hyperbolicity, multiplicative chaos, `ω(n)` classes and Landau anchors.
- Cohomological turn: Hodge, Lefschetz, Arakelov, prismatic, SURF and GL₂/Eisenstein.

Result: it was correctly identified that the target is a global positivity. Prime-by-prime positivity,
purely dynamical propagation, and statistical mechanisms that only give density/proportion all died.

### Arc II — phases 21–40: negative index and finite deficit

- Pontryagin index `κ=2m`, off-line quadruples, local profiles and deficit bounds.
- APS/η, K-theory, transverse energy, Maslov, Fourier interpolation, Nyman–Beurling and entropy.
- CCM/Jacobi program, traces, measures, moments and the Connes–Consani bridge.
- Search for `m<∞⇒m=0`, LP-112 and index-amplification mechanisms.

Result: good detectors and equivalences, no forcer. Some conjectures weaker than RH persist, but
none alone reaches the sign of D.

### Arc III — phases 41–59: Hodge, foliations and closure of method classes

- Tropical Hodge on `C_p×C_p`, dynamical/foliated Hodge, Deninger and Kähler–Riemann polarizations.
- Correspondence categories, defect theory, Weil–Toeplitz/Fredholm and local purity.
- Diophantine routes with `{log p}`, crossed products/KMS, homotopy, Stone, dBN and index dynamics.
- Audit of fifteen mechanisms, Tauberian theorems and closure of an axiomatized detector class.

Result: the finite-field model does not transport its positivity to `Spec Z`; the metric that unitarizes is usually the
same Weil form. The independence of `log p` lives on the value side, but does not by itself cross over to the sign.

### Arc IV — phases 60–90: CCM, Ω₇ and the detector/forcer anatomy

- CCM discriminant, Doob operator, `2×2` Tate transfer, Cesàro and quaternionic polarization.
- Connes route, signature continuity, rank-one escape, q-index and GLT.
- Lee–Yang, Feshbach, Cauchy projections, numerator divisibility, adjugates and Weyl limit-point.
- Endpoint modules, parity defect, Abel, deformations and Kato–Euler currents.

Result: a large library of identities and detectors, but the decisive arithmetic datum always reappears in an
equivalent condition (`Ω₇`, EG_LOCK, etc.). Attribution of positivity to ζ was not obtained.

### Arc V — phases 91–106: determinants, cofactors and A1

- Projectivization via adjugates, bordered anchors, global cofactors and response to primes.
- Covariant currents and the `Ω₇/A1` campaign; modular-star audits.

Result: exact factorizations and finite-source no-gos; A1 and its variants retain RH strength.

### Arc VI — phases 107–122: backward reconstruction of the four rows

- Lefschetz reconstruction, construction of row A, one-sided pairing, principal divisibility and Schwartz data.
- Effective cone, trace, four rows, mixed class, Green extension and Schur angle.
- Transfer measurement, exact threshold, finite compression, global polarization and negative-witness rigidity.
- Minimal specification of a row D object.

Result: it was precisely isolated where D should live, but the positive lifts suffer the locality–phase–sign
trilemma. The negative-witness program was left without its conservation law.

### Arc VII — phases 123–133: construction and audit of A, B, C

- Common carrier; closure of A (space), B (Frobenius family) and C (explicit/Lefschetz formula).
- Adversarial audit, reconstruction and final panel.

Result: A–C are `WEIL-STRENGTH-COMPLETE` on the declared carrier, with record caveats. They imply no sign,
create no Hodge index, and contribute no inequality. D remains exactly equivalent to RH.

### Arc VIII — phases 134–151: direct geometric attack on D

- Canonical class, map, coupling, detector cones, falsifiers, Frobenius squares and traces.
- Clause, trace-positive cone, fixed index, function-field model, coupled pairing, Galois ring.
- Mixed effectivity, additive pencil, method theorems and the bridge.

Result: Paper 47 organizes the no-gos. RR/`h⁰`, Deligne extraction, nonnegative family, finite-S,
local factorization, tropical effectivity and the Künneth product all fail. The conceptual closure of the map is not a proof
of the sign.

### Arc IX — phases 152–156: finite form, duality and the law of the window

- FUP/Dolgopyat/Berkovich; cross-term identity for `Ξ_a`; dual certificates and flat-top theory.
- Flat kernel criterion, zero truncation, archimedean index, Schur/parity and polar capacity.
- Rigorous certificates in small windows and Galerkin diagnostic audits.

Result: Paper 46 turns each window into a decidable finite problem, but it proves there is no dual reached,
no uniform finite truncation, no ascending induction in `T`, and the margin tends to zero.

### Arc X — phases 157–160: exhaustive search for a mechanism or object

- Phase 157 imposes filters F1–F5 on new mechanisms.
- Phase 158 attempts the object MW-5/OT-5′ and shows that the known adèle class space is a reformulation.
- Phase 159 runs two fronts with 30 profiles and five rounds.
- Phase 160 surveys the whole corpus and tests routes that seemed untried.

Result: no sign appears either. The region where a new argument could exist is drastically narrowed.

## 3. Phase 159: what it actually produced

### Front G1 — the object

Scaling site, Deninger laminations, condensed/function fields, Arakelov/Faltings–Hriljac,
Borger/Witt/Bost–Connes, operator algebras, motives, canonical systems, transport from function fields and
probabilistic ladders were all tested.

No candidate gained acceptance as the object. The positive outcome of the campaign is a wall:

> An OT-5′ object cannot be local at primes, factorizable in the tail, algebraic, covariant, finite-trace conformal,
> ergodic-conformal, or a canonical crossed product in which the zeros appear as installed atoms.

The design consequence —heuristic, not an existence theorem— is that the object would have to be simultaneously:

- infinitely entangled across primes;
- non-algebraic;
- non-covariant;
- with supercritical topology;
- with positivity defined prior to the spectrum;
- and with a Lefschetz formula that produces, not installs, the zeros.

Structural results worth preserving: the `W♯` tail wall, the six-exponentials rationality wall,
Witt–Kronecker, the orbit law, and prime-local and codimension-one carrier exclusions. These are no-gos, not sign.

### Front G2 — the mechanism

Structure versus randomness, bootstrap in `T`, Hermitian squares, SOS/Positivstellensatz,
de Branges, finite/random zero universes, near periodicity, Lee–Yang/Pólya–Schur, jump calculus and mollifiers were tested.

All `∀T` targets recovered RH: von Koch–Landau, KEP, `κ=0`, `cor:RH` or Weil. The campaign showed that the following
do not work:

- properties of a comb class closed under deletion/amplification;
- twist-covariant arguments;
- fixed or convergent boundary profiles;
- resolvent certificate rules;
- a proportion of zeros on the line;
- separate arithmetic/archimedean squares.

The most important quantitative result is Theorem M:

`λ^W_T ≤ λ^prim_T ≤ λ^A_T ≤ exp(-exp((2-ε)T))`

for large `T`. That is why compactness/continuity cannot be used with a uniform gap: any mechanism must
work with zero margin.

### Audit debt from 159

Part of B8, B10 and of rounds 3 and 5 were left without a panel. S5 did a pre-audit, not a final verification. None of
those unaudited items claim the sign, but they must not be promoted to published theorem without reviewing their proofs and imports.

## 4. Phase 160: actual state at the end of the directory

### Survey

It is complete:

- S1: phases 0–40, papers 01–15 and root;
- S2: phases 41–90, papers 16–30;
- S3: phases 91–133, papers 31–45 and rows A–C;
- S4: phases 134–156, papers 46–47;
- S5: phases 157–159 and references.

### Round 1

There are 18 evaluated memos. None reached G1 or G2; the best score was 3/10. The test that failed the most routes was that
the proposed identity remained valid for `Λχ₂`, `Ξ_a`, Davenport–Heilbronn, Epstein or the model combs.

Two new design walls:

- a holomorphic flow with one pole carries at most one `L²` zero pair;
- every continuous positive form compatible with `Θ` on Meyer's `H¹` leaves the off-line blocks in its radical.

Hence a future carrier would have to fail Torelli / not be holomorphic up to isotopy, or use inhomogeneous positivity.

### Round 2

Five routes were chosen, but only the memos D2 and D4 exist.

- **D2:** extended the wall in Meyer's carrier. There are many inhomogeneous positive forms, but every natural
  transfer of the sign returns to RH. Conclusion: in this carrier G1 collapses to G2.
- **D4:** found the cleanest separating datum: `Λ*1=log` (multiplicative structure) together with Fourier/Poisson
  (additive structure). It proved that using each piece separately, via convolution identities or the Li limit,
  returns to an equivalence. It left `O-D4.1` as a precise residue.
- **D1, D3, D5:** were not written. There was also no round-2 panel or final synthesis.

The handoff says Stage 2 had not started; this is historically correct at that date but was superseded
by the already-produced D2 and D4 memos.

## 5. What is proved and what is missing

### Proved and reusable

- Each window is decidable from finite data, but the uniform problem is not.
- Above a certain frequency the symbol dominates; the possible negative sign lives in a finite alignment band.
- From approximately `T=0.58–0.60`, the archimedean part is indefinite: the primes must create the positivity.
- The parity–Schur reduction separates the primitive form and the polar capacity.
- No finite dual certificate is reached; a fixed finite quantity of zeros or primes does not suffice.
- No uniform margin exists; the upper margin is doubly exponentially small.
- Positivity can never be proved term by term on zeros nor prime by prime.
- Finite/summable modifications of the comb and resolvent profiles are excluded.
- A field-uniform argument is admissible, but then it must sustain GRH for all fields and overcome the
  non-abelian `S_3` falsifier if it uses unitarity.

### Exactly what is missing

One of these two pieces would suffice:

1. **Mechanism G2:** a global inequality, uniform in `T`, that proves `A_T|P_T≥0` or `W_T≥0` using exact values of
   `Λ`, and whose decisive line uses a datum that fails for all falsifiers.
2. **Genuine object G1:** a positive polarization prior to the spectrum and an independent Lefschetz formula that,
   upon comparison, produces the full form; it cannot install zeros or define the metric with the Weil form itself.

In Meyer's carrier, option 2 has already collapsed into option 1. Consequently, unless a genuinely new carrier is
built, the priority work must be G2.

## 6. New options, ordered by information value

### Option 1 — sum×product square (`O-D4.1`) — top priority

**Idea.** Build a quadratic object in which, in a single equality/inequality, one uses together:

- the multiplicative identity `Λ*1=log`, and
- Poisson/Fourier on the additive inclusion `N⊂Z`.

It must not be an identity in the group ring of `Q_{>0}`, a separate square, a Li limit, nor a window
translation. It is the only phase 160 proposal that simultaneously specifies the ζ-specific datum and the operation
missing from the frame (sum in addition to product).

**First falsifiable lemma.** For every `F∈P_T`, canonically construct `Q_T(F)≥0` and a decomposition

`A_T[F] = Q_T(F) + R_T(F)`

in which the proof of `R_T(F)≥0` jointly invokes `Λ*1=log` and Poisson, and in which that line is false for
`Λχ₂`, `Ξ_a`, `Ξ_Q`, DH/Epstein and Beurling. If the proposed `Q_T` turns out to be a translated convolution or a Li form,
the route is immediately refuted by D4.

### Option 2 — first contact + arithmetic conservation law

**Idea.** Assume the first `T₀` with a negative/radical test and derive an impossible configuration. Phase 121 already gives
the normal form and parabolic rigidity, but a conserved trace of opposite metric is still missing.

**New combination insight.** The conserved trace should not be built only from the spectral or geometric datum:
it must incorporate the ring defect `δ_a=a*1-log`. Then the conservation is exact for ζ and fails for the falsifiers.

**First falsifiable lemma.** At a first-contact state, prove a transport identity

`d/dT Tr_op(M_T)=0`

whose proof uses `δ_Λ=0`; then prove that the normal form with `λ=0` forces `Tr_op(M_T)` to change sign.
This avoids a uniform margin and ascending induction. If the trace is conserved for any comb or for `Λχ₂`, it is useless.

### Option 3 — exact bilinear inequality in the alignment band

**Idea.** The negativity can only live in a band of alignment frequencies. Apply
Heath–Brown/Friedlander–Iwaniec identities to the full quadratic form, not to a linear sum of primes, and keep the
exact datum `Λ*1=log` to the end.

**First falsifiable lemma.** A signed bound for the low-frequency block of `A_T|P_T`, uniform in `T`, where the
main term is a sum×product square and the error is absorbed without using a positive gap. A bound in absolute value
or on average is not enough; M7 already showed that the operatorial computation merely rewrites the form.

### Option 4 — complete D3: converse from primitive to full window

**Idea.** Prove, for ζ and `T>0.8`, that `RD_T` forces the positivity of the polar/Schur capacity, perhaps with an
effective window shift.

**Value.** It is a clear, auditable technical piece, and it would eliminate the duplication of forms. It does not prove D by
itself: `RD_T` would still be needed for all `T`. It should be considered infrastructure, not endgame.

**First falsifiable lemma.** The inequality proposed in the round-2 plan:

`W_*(Y_1) ≥ <(A_T|P_T)^{-1}b_T,b_T>` under `RD_T`,

with rigorous constants and domains for `T>0.8`.

### Option 5 — Torelli-failing carrier / lamination with fixed points

**Idea.** Build the non-compact/non-ergodic lamination that Deninger–Singhof does not offer: derived leafwise Hodge,
arithmetic fixed points in the measure-zero orbit set, and Torelli failure.

**First falsifiable lemma.** Existence of an explicit class of laminations where the Álvarez López–Kordyukov
polarization survives and the theorem "one pole ⇒ at most one `L²` zero pair" fails under an identifiable hypothesis.
Afterward the Lefschetz formula still has to be built. It is the most conceptual and costliest route.

### Option 6 — mixed single/double contour class in Meyer

**Idea.** D2 leaves `S+D` open: a canonical kernel `G` might add a useful prime×prime square.

**Evaluation.** Low priority. D2 proves that any effective transfer of the sign in that carrier is already G2;
the additional square is structurally sterile unless it contributes precisely the missing mechanism. Continue only if
a prime-side identity that does not hold for the falsifiers is exhibited first.

## 7. What should not be repeated

- Another equivalence: Li/Keiper, Nyman–Beurling, de Branges, KEP, Herglotz, dBN, `κ=0`, global square.
- Place-by-place positivity, finite-S, sub-combs or sums of local positive forms.
- Bootstrap or continuity in `T`; fixed boundary profiles; compactness with a gap.
- Certificates with a fixed finite basis, finite truncation of zeros or finitely many exact values of `Λ`.
- Class arguments based on PNT, zero-free regions, density, sieve upper bounds or zero proportion.
- A metric chosen to make the flow unitary, or zeros installed as spectrum.
- Hodge/RR via a real-valued `h⁰` on the already excluded domains.
- Direct transport from finite fields without a new operation that controls sum and product simultaneously.
- Galerkin numerology as a sign: several positive values are only upper bounds of the bottom.

## 8. Concrete program for the next campaign

1. **Short audit:** verify D4 Theorems 2.1–5.2 and D2 Theorems AF/T/Z; do not re-audit the 150 memos of 159.
2. **Close the state:** write the missing phase 160 synthesis stating that D1/D3/D5 were not executed and that D2/D4
   are walls, not solutions.
3. **Main campaign:** three lines of work focused only on O-D4.1:
   - an algebraic/Poisson one to seek the sum×product square;
   - an analytic/bilinear one for the alignment band;
   - an adversarial one that tests every candidate against the five falsifiers before developing it.
4. **Secondary campaign:** one line on first contact with `δ_Λ=0` and one on D3.
5. **Early kill criterion:** abandon in the first round any candidate whose decisive line is valid for
   `Λχ₂`, `Ξ_a`, DH/Epstein or a comb obtained by deleting/amplifying finitely many coefficients.
6. **Real partial-success criterion:** a lemma uniform in `T` that jointly uses sum and product and produces a
   signed inequality, even if it does not yet dominate the whole form. A new sign-free identity does not count.

## 9. Final verdict

The corpus contains no proof of D nor an almost-closed route missing a single technical detail. It contains something valuable:
a very narrow characterization of the missing piece.

The missing piece is not "more geometry," "more spectrum," or "more numerical computation" in the abstract. It is a source of sign
that simultaneously satisfies four properties:

1. exact for the coefficients of ζ;
2. global and uniform over the window;
3. sensitive to phase and to the joint use of sum and product;
4. compatible with zero margin and with infinitely many degrees of freedom.

Today the most concrete formulation of that piece is `O-D4.1`. If it does not exist, the next high-value result would be a
no-go excluding every reasonable sum×product square; that would justify moving the effort to a radically
new carrier. Until one of those two things is obtained, repeating the previous families will grow the archive, but will not bring D closer.
