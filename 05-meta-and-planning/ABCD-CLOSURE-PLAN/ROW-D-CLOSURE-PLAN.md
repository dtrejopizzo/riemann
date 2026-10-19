# Row D closure plan —

Inputs: a sweep of the corpus by four independent reviews (route catalog, Connes
material, inventory 134–149, analogies examined) and an adversarial audit review of `R149_001`
(recorded in `R149_002_AUDIT.md`). Everything that follows cites a file; nothing is reconstructed.*

---

## 0. State in one page

* Rows A, B, C: WEIL-STRENGTH-COMPLETE (Papers 43–45). Row D: **no label, no sign**.
* Phase 149 (additive sheaf, Deligne route): round 1 delivered, **adversarial audit done**.
  Verdicts: D.59 STANDS (it is Hölder `‖·‖_∞ ≤ ‖·‖_{2k}`, not Weil I 3.2); D.60 STANDS with D.60.7
  downgraded in scope; **D.61.10 DOWNGRADE** ("there is no transport" is false: Parseval over `χ` and
  Goldston–Montgomery do transport moments; what does not cross is the polar/positive structure);
  **(P149) DOWNGRADE**: it is the Hardy–Littlewood `k`-tuple conjecture dressed as Deligne, not a
  new object. Minimal repairs listed in `R149_002` §5. Still missing: `R149_003` (repairs) and
  `R149_005` (decision), both short.
* Paper 46: Parts I–III closed; Part IV (phases 145–149) pending the author's decision.

## 1. What already exists and is NOT reconstructed

Verified inventory (independent review; detail in Paper 46 §23 and the `R1xx_005` files):
canonical class `K` and duality `σ_K` (PROVED, §11–12); transfer theorem 12.3 conditional on
`h⁰` and its unconditional trace version 12.3-B4 (§20.17); method T1 (uniform in the field) and T2
(must use the Euler product; fails for Epstein `Ξ_Q`) (§18); **frame defect theorem**
(no `h⁰` on `D^W` satisfies (a),(b′),(c); `s* = 0.99846…`; it also holds on a curve
where RH is a theorem: the defect is in the cone, not in the zeros) (§19.7, §21); computed Frobenius
diagonal, indefinite, blind to the zeros; "Spec Z is terminal, there is no `Z[π]`" (§22.17);
Galois ring inert in `ζ` (147); mixed effectivity = tropical condition, cone unchanged (148);
additive sheaf: extraction D.59, wall `c = 1/2`, `κ(d) = d/φ(d)`, "the exponents add in the additive
square and subtract in the multiplicative one" (149, D.61.8–9: the good idea of the phase).

Live open problems that matter: (36) *a class over the square carrying a PHASE datum
(unimodularity of the local roots) and not a magnitude*; O-148.2 = O-149.5 (a kernel over the
square with a nonzero finite pairing between fiber classes and diagonal invariance); (P145′) a mechanism
with `𝔈 ≠ D^W`.

## 2. The six invariant conclusions of the corpus (why the sign never arrives)

1. Magnitude does not see the sign; only the phase coherence of `cos(t log n)` (phase 60, 136; NG-F1).
2. Every unconditional positivity is a LOWER bound; RH is an UPPER bound (05-MASTER-CLOSING VII).
3. The arithmetic of `Re s > 1` does not propagate to the strip; no prime "owns" a zero (MW-2, NG-B1).
4. There is no `+` over the correspondences: only the semigroup `{π^n}` (145–148; Thm 22.17).
5. There is no arithmetic site with `H¹`, Frobenius, and a positive form (MW-5); row D ≡ RH twice over (113, 118).
6. T1 ∧ T2: uniform in `K` and essentially Euler; everything built is `Ξ_a`-uniform or a restatement.

Full catalog of 57 routes with verdict: review report dumped into §7 below
in compressed form; primary source `NO-GO-LIST.md`, `ROW-D-MAP-b.md`,
`PHASE_136_MAP_SYNTHESIS_AND_PLAN.md`.

## 3. Diagnosis (new)

**3.1 The five walls are one, and it has a classical name.** The "two squares" of D.61.10 are the two
quotients of the adelic square: the **additive** one `A/Q` (compact solenoid; its rational points are
the Farey sheaf `e(na/q)` of phase 149, and its archimedean direction is the sheaf `n^{it}`), and the
**multiplicative** one `A/Q^×` (Connes's adele class space, the scaling site). The only unconditional bridge
between the two is the Fourier–Mellin duality of Tate's thesis: Poisson over `Q ⊂ A`
⇒ functional equation (= Poincaré duality). The "phase datum" from open problem (36) already exists for
`GL(1)`: these are the **local ε factors** `ε_v(s,χ_v,ψ_v)`, unimodular, whose product is the root
number (product formula). What is missing is not the datum: it is how the datum constrains zeros.

**3.2 De la Vallée Poussin is Deligne with `k = 1` on the archimedean sheaf.** `3+4cos θ+cos 2θ =
2(1+cos θ)² ≥ 0` is the Rankin square; the pole at `s = 1` is the a priori coinvariants block;
Landau gives the region `1 − c/log t`. Its optimality for **Beurling prime systems**
(Diamond–Montgomery–Vorhauer, 2006: systems exist with an Euler product, `Λ ≥ 0`, a pole, and zeros
at `1 − c/log t`) shows that positivity + pole + Euler product do NOT reach `β ≤ 1 − δ`:
the ADDITIVE structure of `Z` is needed (the one producing Poisson and the functional equation).
**Consequence: third method theorem T3** — every proof of `β ≤ 1−δ` must separate `Z` from a
Beurling system; a Beurling system is a **new falsifier** (with Euler, without `+`),
complementary to `Ξ_Q` (with `+`/functional equation, without Euler) and to `Ξ_a` (non-unimodular Euler).
Corpus check: `Vorhauer` 1 incidental occurrence (E101_089); "Beurling primes" 0. **NEW.**

**3.3 The only unconditional transport from the additive square to the zeros is Vinogradov–Korobov**, and
it transports magnitude: additive energy of the moment curve (Vinogradov's mean value theorem;
today decoupling) ⇒ `|ζ(1+it)| ≪ (log t)^{2/3}` ⇒ region `1 − c/(log t)^{2/3}(log log t)^{1/3}`.
This is consistent with conclusion 1: energy reaches the zeros only through `|ζ|`. The new object
must bring additive energy to the zeros **through the phase**, not through the magnitude.

**3.4 Finiteness is not the essential point in Deligne.** Weil I 3.2 uses the finiteness of `H¹_c` only to know
that the block of zeros is NUMERATOR (holomorphic) and contributes no singularities; Landau only needs
the first real singularity of the family's `L`-function to be the a priori pole. A finiteness-free
reformulation of the Missing Lemma 5.3 (Doc 106): *the contribution of the zeros to the family's series must
be holomorphic to the left of the a priori pole* — equivalently (auditor R149_002 §3):
**promote the singular density series to a polar divisor.** Over `F_q` this is done by Künneth + weight
filtration on `H_c(X×X)`; over `Z`, nobody has done it.

**3.5 The Weil conjectures were proved by four routes, and the corpus transposed two.**

| route | central mechanism | transposition in the corpus |
|---|---|---|
| Hasse–Weil 1948 | ring of correspondences, Rosati/Castelnuovo–Severi | phases 107–148: negative (no `+`) |
| Deligne 1974 (Weil I) | tensor powers, Landau, monodromy coinvariants, extraction | phase 149: negative ((P149) = `k`-tuples) |
| **Laumon 1987** (Weil II via Fourier) | **ℓ-adic Fourier transform** (`+`/`×` transport), stationary phase (local monodromy at `∞`), **unimodular Gauss sums** `|g| = √q`, product formula for the ε's | **0 occurrences** (`Laumon`, `Gauss sum`, `Hasse–Davenport`: 0) |
| **Kedlaya 2006** (p-adic, same architecture) | Fourier on rigid cohomology | **0 occurrences** |
| Bombieri–Stepanov (curves) | auxiliary function, Riemann–Roch, `deg div f = 0` | only as an audit (116) |

The Laumon route is the only one whose central mechanism is exactly what row D says is missing:
a transport between the additive and multiplicative squares whose purity reduces to a **unimodular
phase datum** (Gauss sums). It is lateral candidate number one.

## 4. Lateral candidates, ranked, with corpus check

**L1 — Laumon's route over `Z`: the Fourier transform as transport between squares.**
Over `F_q`: `FT_ψ(L_χ) = g(χ,ψ)·L_{χ̄}` — multiplicative characters are eigenvectors of the
additive Fourier transform with eigenvalue of modulus `√q`; the purity of `FT` (Katz–Laumon) and stationary
phase reduce the weights of an arbitrary sheaf to Gauss sums. Over `Z`: `FT` on the sheaf `A/Q` is the
functional equation of `L(s,χ)` with root number `τ(χ)/√q`; the "stationary phase at `∞`" is the Gamma
factor (the polar block `K` of rows A–C); the "purity of `FT`" in its weak form is D.59.3
(ATRH ⟹ GRH), trivial. What needs to be found out, and is the **acid test**: (a) exactly where
Laumon uses finiteness (constructibility of `FT(F)`, Deligne's semicontinuity) and whether that use is
replaceable by holomorphy (3.4); (b) whether the deduction "arbitrary weights ⇐ Gauss sums" has
an avatar "zeros of `ζ` ⇐ root numbers of `L(s,χ)`" — none is known today; (c) Kedlaya as a
second independent instance of the same architecture. Risk: finiteness reappears in
constructibility. Gates: `Ξ_a` (roots `p^{±a}` break `|g|=√q`: the candidate must fail there),
`Ξ_Q` (no Euler, no Gauss sums), Beurling (no `+`, no Fourier). **Phase 150.**

**L2 — Upper bound without positivity: Dolgopyat and the fractal uncertainty principle.**
Bourgain–Dyatlov (Ann. Math. 2018) prove, for every convex-cocompact hyperbolic surface, a
resonance-free band `Re s < 1/2 − β` beyond the unitarity threshold, without positivity: a resonant
state cannot concentrate on the trapped set simultaneously in position and frequency. It is the
only known mechanism producing an **upper bound** (conclusion 2) on real parts of
zeros of a dynamical zeta function with infinitely many zeros. For the modular surface the resonances are
exactly `ρ/2` (poles of `φ(s) = ξ(2s−1)/ξ(2s)`): RH ⟺ resonances at `Re s = 1/4`. The
mechanism literally fails (δ = 1, no fractality); the lateral question is whether **arithmetic
rigidity** (Hecke; Lindenstrauss) substitutes for fractality for the resonant states
`E*(z,ρ/2)`. Dolgopyat itself is a mechanism of **phase non-coherence** (UNI) — conclusion 1.
Baladi–Vallée proved it for the Gauss operator near `Re s = 1`. Corpus: `Dyatlov`,
`Dolgopyat`, `Baladi`, `fractal uncertainty`, `Lindenstrauss`: **0**. **Phase 151** (literature
check + a precise statement (P151) or quick death).

**L3 — The "same square" that already exists: Mayer's transfer operator and Lewis–Zagier
period functions.** A single object carries the `+` (Farey, `x ↦ x+1`, `SL₂(Z)`) and the `×` (`ζ(2s)` in
the Fredholm determinant); the zeros of `ζ` are eigenvalue-1 parameters (periods of the
Eisenstein series); the three-term equation `ψ(x) = ψ(x+1) + (x+1)^{−2s}ψ(x/(x+1))` is a transport
`+`/`×` at the level of eigenfunctions. Prediction, verified by hand: the Perron–Frobenius
positivity of the real operator is magnitude and by domination gives only `Re ρ ≤ 1` (conclusion 1,
as it should). The non-magnitude part is the three-term equation. Corpus: `Lewis`, `period function`,
`Gauss map`: 0; `Mayer` 1; Knauf (Farey chain, `ζ(s−1)/ζ(s)`, ferromagnetic) 1 (CAND-3: Lee–Yang
fails). Cheap. **Phase 152**, one round.

**L4 — Beurling calibration (T3).** Not a route: it is the missing falsifier (3.2). It is
incorporated as a mandatory gate from phase 150 onward and as a method theorem in Paper 46 §18.

**L5 — Honest closure of (P149).** Record that it is the `k`-tuple conjecture (auditor §4);
O-149.5 is merged with O-148.2. Not pursued.

**Discarded after checking (with reason):** Taylor–Wiles (patching = a free family over the group
algebra ⇒ fiber at `χ = 1`: this is phase 147 in another language, inert in `ζ`); Kudla (arithmetic
intersection numbers = values/derivatives of Eisenstein series, not zeros); Lee–Yang (Fisher zeros in
temperature: no theorem; CAND-3); Kesten/Haagerup/Ramanujan graphs (finiteness or local Plancherel;
"tempered" ≠ global zeros); Maass–Selberg/Eisenstein (reaches only `Re s = 1`,
Shahidi); Rankin–Selberg toward Ramanujan (bounds local parameters `α_p`, not zeros: Deligne over
`Q` already exists and is Kim–Sarnak).

## 5. Circuit (same as 138–149: constructor + adversarial auditor; pure mathematics)

| phase | content | deliverables | gates |
|---|---|---|---|
| 149 (closure) | `R149_003` repairs (i)–(vi) of `R149_002` §5; `R149_004` confirmation; `R149_005` decision: D.61.8–9 finding; D.61.10 rewritten; (P149) = `k`-tuples | three short files; `PLAN.md`; Paper 46 Part IV if the author decides | FATAL |
| **150** | **T3 + Laumon**: (0) CORPUS_CHECK; (1) T3 with the DMV construction as a formal falsifier `ζ_P`; (2) a technical reading of Laumon 1987 §§ on the purity of `FT`, stationary phase, use of finiteness; Kedlaya 2006 in parallel; (3) a `F_q → Z` dictionary (table as in §3.5); (4) statement (P150): the `Z`-avatar of "purity of `FT` ⇐ Gauss sums", or an impossibility theorem with the exact point where finiteness is not replaceable | `R150_000…005` | `Ξ_a`, `Ξ_Q`, `ζ_K`, **Beurling** |
| 151 | Dolgopyat / FUP: resonances of the modular surface; what substitutes for fractality; (P151) or death | `R151_000…005` | same |
| 152 | Mayer / Lewis–Zagier: the three-term equation as transport; any non-magnitude inequality at `s = ρ/2`? | `R152_000…003` (one round) | same |
| 153 | Synthesis: either an object with the five properties (§6), or closure of D in the map with T1–T3 and Part IV | author's decision | — |

Current rules: numerics only for identities; never relabel; "what holds builds the object, it does not
go around it"; every idea passes through CORPUS_CHECK before being built.

## 6. Success criterion (what closes D) and negative closure criterion

D is closed by an object `𝒪` on the adelic square such that: (1) it is a square (Rankin
positivity, stable under twisting); (2) its polar divisor is determined by local data
(`κ`, `𝔖`, ε factors) — the singular series promoted to a pole; (3) the contribution of the zeros is
holomorphic to the left of that pole (3.4); (4) it reads phase: it fails for `Ξ_a`; (5) it uses `+` and `×`:
it fails for `Ξ_Q` and for every Beurling system; and (6) it is uniform in the field (T1).
If phases 150–152 end with impossibility theorems, D is closed in the map with T1, T2, T3
and the 3.4 reformulation as the exact statement of the wall, and Part IV of Paper 46 is written.

## 7. Compressed catalog of dead routes (so as not to repeat them)

(a) Hilbert–Pólya/operator: OS-reflection (NG-E5, NG-E1), distributional eigenvectors (NG-C3),
Bost–Connes KMS (Thm 161.9), CCM spectral triples (CAND-1, open but every mechanism closed:
NG-66/67/68/69), Deninger foliations (136 C), eight positivity paradigms (P7–P13: all
RH-equivalent, "capstone of the wrong sign"), multiplicative chaos (N7).
(b) Weil/explicit formula: λ_min (NG-A8, NG-E2), global Cauchy–Schwarz (NG-E3), relative forms
(NG-E4), pointwise comb (NG-E6), Carleson (NG-F1), Cesàro (NG-62), quaternionic HR
(NG-62b), `J`-linear Frobenius (NG-63), MW-1, RH-PROOF phase 65 (refuted in 137).
(c) Connes–Consani: archimedean prolate (proved, `∞` only), absolute RR (=CAP), arithmetic site
(MW-5), `Δ→Σ` does not transfer (137 D.13-γ open), Deninger–Morishita (NG-107).
(d) Arakelov/Hodge: Weil transcription (107_241), form `Q` (33), `h⁰_RR⁺` (NG-113 O1–O3),
divisibility by `ξ` (NG-110), row d ≡ RH (113, 118), Toeplitz/Hankel (NG-118), log Schur
(NG-116), `c_N` (NG-117), class `K`/transfer (135–144: restatements), T1/T2 (138–139), model
`E/F_2` (145), degree form (146), diagonal (146), Galois ring (147), mixed effectivity (148).
(e) `F_q`: Weng (CAND-2), tropical toy `C_p×C_p` (41/125), phase 145.
(f) Analytic: Hasse–Minkowski (NG-C1, MW-3), family positivity (item 5, open/risk),
Rankin–Selberg `Γ·Γ ≥ 0` (M1: reduces, does not solve), 15 classical mechanisms (NG-B1, MW-2),
Kurasov–Sarnak (=Lee–Yang), boundary anchors (=CAP), integrality index (=Deninger), 149.
(g) Others: multiplicative anatomy S1, ω/BRW hierarchy S2 (RH-independent).

## 8. Re-examination (second pass) — novelty and value, with no overselling

Author's request: reconsider whether this is new, whether it is absent from the corpus, and whether it is worth doing.

**8.1 Novelty relative to the corpus (verified by grep).** Laumon, Kedlaya, Gauss sums,
Hasse–Davenport, Dyatlov, Dolgopyat, Baladi, fractal uncertainty, Lindenstrauss, Lewis, period
functions, Gauss map, Beurling primes: **0 occurrences** (Vorhauer: 1, incidental). "Weil II": 5
files, none about the Fourier-route proof. Mayer: 1, motivic context. Modular surface and
scattering determinant: 0. **But** Doc 106 (phase 36) already contains: (a) "the machinery
guaranteeing that the poles do not move is cohomological finiteness"; (b) **Form B**: "finiteness +
rationality (index assumption) instead of positivity"; (c) Problem 5.4 (is the arithmetic
side of the two-variable Weil formula over `p_1p_2` autonomous?); (d) "vacuity of the
Rankin–Selberg family of `ζ`". So my 3.4 is a **refinement** of Form B (finiteness → holomorphy
of the zero block to the left of the a priori pole; Landau does not need finiteness), not a new idea.
The discarding of Rankin–Selberg→Ramanujan was already in the corpus.

**8.2 Laumon (L1), downgraded on reconsideration.** What Laumon changes relative to Deligne is *where
the coinvariants block is computed*: locally at `∞` (stationary phase, local Fourier
transforms, Gauss sums) instead of globally (Lefschetz sheaf, large monodromy). What Laumon
does **not** change, as the final audit recalls about the structure of the proof and must be confirmed in the
source: it still uses Rankin (tensor powers), Landau, and the **rationality** of the family's `L`.
Over `Z` the coinvariants block is already computed (singular series, `κ`, phase 149): Laumon's
gain attacks a part that is **not the wall**. The wall is 3.4 (holomorphy / rationality
of the zero block) and Laumon inherits it intact. Real value of L1: the dictionary (major arcs =
pointwise part of `FT`; local monodromy at `∞` = Gamma factor = polar block `K` of rows A–C;
singular series = weights of the pointwise part), which for the first time connects the polar block with the
singular series. **Reclassified: round 0 of dictionary-building (one constructor, one auditor), not a full phase;
expectation: it relocates the wall, it does not remove it.**

**8.3 Bourgain–Dyatlov (L2).** It is the only mechanism with the correct form (upper bound without
positivity) and it is new. But: fractal uncertainty requires `δ < 1`; the modular surface has
`δ = 1` and the band `β(δ) → 0`; the resonant states at `ρ/2` are the Eisenstein series
`E*(z,ρ/2)` and their non-concentration off the line is unknown; the Eisenstein QUE on the
line (Luo–Sarnak) uses bounds on `ζ` (circular). Low probability. **Reclassified: a one-round
literature check, exploratory.**

**8.4 Mayer / Lewis–Zagier (L3).** It is an object with `+` and `×`, but it is a spectral realization of
`ζ(2s)` via the modular surface: it belongs to family (a) Hilbert–Pólya of the catalog. The
Perron–Frobenius positivity is magnitude (domination ⇒ `Re ρ ≤ 1`, verified). That the zeros are
eigenvalue-1 parameters is obtained by building the period function **with** `ζ`: a restatement, the
same lesson as "Connes (1999) does not construct a self-adjoint operator". **Probable RESTATEMENT; a
cheap round or nothing.**

**8.5 Beurling / T3 (L4).** New to the corpus, cheap, and a genuine method theorem: it turns
invariant conclusion 4 ("there is no `+`") into a statement with a concrete class of counterexamples
(Diamond–Montgomery–Vorhauer): Euler product + `Λ ≥ 0` + pole do not suffice for `β ≤ 1−δ`. It closes the
falsifier triangle: `Ξ_a` (non-unimodular Euler), `Ξ_Q` (`+` without Euler), Beurling (Euler without
`+`). **Worth doing; done first.**

**8.6 Honest verdict.** After the second pass, none of L1–L3 is a credible bet for
producing the sign; their value is sharpening the wall. The structurally correct objective remains
3.4/Form B: making the zero block holomorphic to the left of the a priori pole, and phase 149 already
showed (D.62.2) that in the additive sheaf this is of RH strength. The accumulated corpus evidence points to
D closing **in the map**, with T1, T2, T3, and 3.4 as the exact statement of the wall, and Part IV of
Paper 46. Revised circuit: **150 = T3 (one round) + round 0 of the Laumon dictionary; 151 =
author's decision** between closing D in the map or spending exploratory rounds on L2/L3.

## 9. Third pass: "it cannot be impossible" — what can really be done

**9.1 Corpus finding that changes the map.** Phase 114 / Paper 42 (`certificates/row_d_log2`, reproduced and
diagnosed in phase 118 `W4_CERTIFIED_RANGE.md`): `A_T ≥ 0` over all of `P_T` for `0 < T ≤ log 2` —
Weil positivity **with primes 2 and 3 coupled to the archimedean block**, certified in Arb; final margin
`8.63·10⁻⁸`; the endpoint `½·log 5` (three contacts) was attempted and **withdrawn**. The limit is not
numerical (precision and quadrature have 5–10× slack): it is the thinness of the margin — the
exponential cascade `V₊` of NG-62b seen from the certificate. Phase 119 closed with the DH gate. So "the
smallest non-trivial sign theorem" **already exists** in the corpus, and its extension measures exactly the wall.

**9.2 Quantitative reformulation of the wall (verified by hand).** Over `P_T`, the trivial bound is
`A_T ≥ −C e^{T}‖F‖²` (`Σ_{n≤e^{2T}} Λ(n)/√n ≍ e^{T}`), which is equivalent to `β ≤ 1`. Any
`λ_min(A_T) ≥ −C e^{aT}` with `a < 1` is equivalent to the band `β ≤ (1+a)/2`; `a = 0` (or subexponential) is RH.
This is the "λ_min" form of NG-62 (secular growth `λ^{2β−1}`): the negativity of the Weil form on
support `T` grows exactly like the worst zero. Nothing new, but it fixes the scale: **each prime added to the
certificate costs an exponential factor of margin, and no finite certificate can reach `a<1`.**

**9.3 What I discarded in this pass, with the reason.** Families `{ζ_{K_d}}` (ζ is a constant summand: Deligne
does not prove the purity of a constant summand); the quadratic family `{L(s,χ_d)}` with a Weyl-group multiple
Dirichlet series (a priori poles exist, but the fiber `d = □` is ζ and its pole at `w = ½` is
dominated by the family pole at `w = 1`; the large quadratic sieve excludes squares); the
archimedean sheaf `t` with the Montgomery–Vaughan mean value theorem (same wall `c = ½`: the
family computable by Parseval has size `≥ N^k` and the extraction vanishes; Guth–Maynard is progress on the
large values conjecture, i.e. on the archimedean (P149), and gives density, not RH); averaged Goldbach with
power saving (Bhowmik–Ruzsa) = integrated PNT error; Voronin / Bagchi universality (RH ⟺
self-approximation: a restatement); zero-based Fourier interpolation (Bondarenko–Radchenko–Seip) and
Radchenko–Viazovska (do not assume RH; the reality of the nodes reduces to de Branges); Burgess (no
complete sum over `Z`). **Smooth regime:** every unconditional cancellation method (Vinogradov, van der
Corput, Vaughan, restriction) operates when the frequency is ≥ the length; RH lives at fixed frequency and
length `→ ∞`, where `n^{-iγ}` is piecewise constant and the sum is `ψ(N) − N` itself. That is the wall in
one sentence, and it is a method statement (candidate T4).

**9.4 What can honestly be done.**
(i) **New method theorems**: T3 (Beurling), T4 (smooth regime: every known cancellation requires
frequency ≥ length), T5 (non-extraction: every moment bound obtained by `L²` orthogonality has
family size ≥ fiber length and extracts the trivial bound). All three are provable in one round and
turn the map of no-gos into theorems.
(ii) **Extending the certificate** from `log 2` to `½·log 5` (three contacts), fixing the withdrawn attempt: a
real theorem, computer-assisted, not a route; its value is measuring the decay of the margin against the
prediction `e^{-cT}`.
(iii) **The only creative avenue that does not collapse by construction**: the square of the Connes–Consani
scaling site with Form B (finiteness/holomorphy instead of positivity), i.e. MW-5 — open for
decades; the corpus already has the dictionary. If the author wants to "create the object," this is it; there is no shortcut.
**Recommendation**: do (i) in phase 150, decide (ii) according to budget, and do not open (iii) without a
concrete idea for the pointwise/smooth part of the square.

## 10. After closure in the map (night session): the bridge and the unanalyzed mechanisms

**10.1 Phase 151 (T6) closed.** Every family with fibers as nonnegative summands has, by
Pringsheim–Landau, abscissa `≥ 2kβ_max`: Deligne's "bridge" over `Z` is the theorem itself at each `k`
(restatement of Thm 26.4 + Cor 27.10a; new only Lemma 2.4). Auditor correction, recorded finding:
spectral positivity `⟨Hf,f⟩ = Σλ_j|⟨f,e_j⟩|²` is also a nonnegative sum; **the axis is summand vs.
numerator**. Deligne works because the zeros of the fibers enter the family's trace formula with
numerator sign (odd cohomology). Over `Z` the only numerator-sign mechanism is de la Vallée
Poussin's, and its depth `1/log γ` is fixed by the archimedean sea (Doc 111 §3.2, phase 37; quantified
in `R151_005` §2.2: penalty `(P(0)−a_0)(½)log γ`, Fejér bound `a_1 ≤ 2a_0`).

**10.2 Corpus sweep, fourteen non-positivity mechanisms.**
ANALYZED and closed: sum-product/additive combinatorics (150), arithmetic differential equations /
prismatic (15, M6), dBN zero dynamics (33, 70: reduced to the q-resolvent identity, open but
mapped), probabilistic/Cramér/Harper (12–13, 19: escapes the capstone, collides with N7), Langlands
functoriality (30), quantum chaos/Berry–Keating (53, 67), Fourier interpolation (35/101), Voronin–Bagchi
universality (35/102: CLOSED ROUTE). **NEVER ANALYZED**: (1) fractal uncertainty principle /
Dolgopyat / resonance gaps (0); (2) global Berkovich spaces over `Z` (Poineau; the corpus itself
marks this as a gap: "No Berkovich space over Spec Z … anywhere"); (3) measure rigidity of the
`×p` semigroup (Furstenberg, Rudolph, Lindenstrauss: 0–1); (4) model-theoretic methods (0); (5) auxiliary
functions / transcendence / Pila–Wilkie (0; the corpus's only "Stepanov" is a namesake).
Lax–Phillips: 9 occurrences, as coligation, not as scattering theory for the modular surface;
Eisenstein/resonant state: 0–2.

**10.3 What a new approach has to be, given what has been proved.** Either a numerator-sign mechanism with
bounded archimedean penalty (none known), or a mechanism that is not positivity. The five from 10.2 are the only
unanalyzed candidates; none today has a formulated statement that produces the sign. **Phase 152 = feasibility
round 0** on (1) and (2), with a death criterion set in advance; (3)–(5) in reserve.

**10.4 Phase 152, round 0 (closed the same night).** Auditor's verdict, accepted: *no path
found; no impossibility proved*. On record: Prop A.4 (the branch series of the Gauss map has
abscissa `Re s = ½`: the Dolgopyat route via branch sums is MW-2 in dynamical form) and Prop B.3 (potential
theory on the tree `M(Z)` is branch-wise, blind to the coupling between places where the sign lives). Withdrawn:
Cor A.5 (on the Mayer disk a Dolgopyat-type bound IS statable), "phase 16 already covers this"
(overstated), Q6 (category error). What remains formulated and new in the corpus: **(P152.1)** a
Dolgopyat-type bound for the Mayer operator continued via the Lewis–Zagier three-term equation (correct logical
form, no method; the archimedean gate fails as stated); **(P152.2)** a difference kernel over the
Berkovich line `A^{1,an}_Z`, with a cheap decisive test for Beurling-blindness; (P152.3) hygiene.
Recommendation: a single bounded round on the (P152.2) test; (P152.1) to §28.3 of Paper 46.
