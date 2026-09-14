# R138.000 — Lead blueprint, phase 138: the primitive radial sector and detecting cones

*Lead: Fable 5.1. Date 2026-09-13. Owner's direction (verbatim, translated): "I would investigate a single
thing: what intrinsically distinguishes the primitive radial sector from the positive directions that make
`I_A` indefinite? Theorem F already shows that space has enough spectral resolution to detect any off-line
zero. You do not need to control all of `D_A`. You only need a non-circular reason why the relevant
arithmetic classes lie in a cone or domain where `I_∞(F,F) ≤ 0`. Avoid proving the sign directly from the
explicit formula, since that risks being RH rewritten. Row D must come from a structure that exists before
one speaks of zeros."*

Standing rules: pure mathematics; numerics only to certify a constant, with a stated robustness margin;
every arrow labelled (PROVED / PROVED-IN-REPOSITORY / CLASSICAL / RESTATEMENT / IMPORTED / CANDIDATE /
HEURISTIC / REFUTED / NOT-APPLICABLE / OPEN); nothing defined through the location of zeros, `ξ` admissible
as data; every theorem run against the falsifier `Ξ_a(s) = ξ(s+a)ξ(s−a)` (and, where rank-one polar
divergence is used, note the `ζ_K` gap recorded in R137_007 §2.2); a statement that with Paper 46 Thm 3.7
would prove RH or ¬RH is FATAL — flag, do not fix. Builder + hostile auditor, rounds as in phases 131–137.

## 0. Setting (Paper 45 §§9–11, Paper 46 §§11–12; RESTATEMENT of record)

Weil class `D^W` (real `C²` functions with decay `e^{−(1+ε)|t|}`); `Φ_F(s) = ∫F(t)e^{(s−½)t}dt`;
`I_∞(F,G) = Φ_F(0)Φ_G(1)+Φ_F(1)Φ_G(0) − Σ_ρ Φ_F(ρ)Φ_G(1−ρ)` (polarization Lemma 11.4a);
rulings `deg⁺F := Φ_F(1) = ∫Fe^{t/2}`, `deg⁻F := Φ_F(0) = ∫Fe^{−t/2}`, `deg F = deg⁺F + deg⁻F`;
primitive sector `P := {deg⁺ = deg⁻ = 0}`; on `P`, `I_∞(F,F) = −Σ_ρ Φ_F(ρ)Φ_F(1−ρ) = −W(F⋆F^∨)`;
canonical class `K` (Pólya kernel), `Φ_K = ξ`, `K > 0`, `deg⁺K = deg⁻K = ½`, `I_∞(K,K) = ½`,
`I_∞(F,K) = ½ deg F`; radical `𝓝_∞ ⊇ Λ_W` (Frobenius translates of `ΠK`). Theorem F (Paper 45 Thm 11.3):
if `ξ(ρ_0) = 0` with `Re ρ_0 ≠ ½` there is a real primitive `F ∈ C_c^∞` with `I_∞(F,F) > 0`.

**Definition 0.1 (detecting cone).** A convex cone `C ⊂ D^W` (not necessarily inside `P`) is *detecting*
if for every zero `ρ_0` of `ξ` off `Re s = ½` there is `F ∈ C` with `I_∞(F,F) > ½ (deg F)²`, i.e. the
Hodge-index inequality `I_∞(F,F)·I_∞(K,K) ≤ I_∞(F,K)²` fails at `F`. (On `P` this is `I_∞(F,F) > 0`.)

**Observation 0.2 (RESTATEMENT, to be proved in D.15).** RH ⟺ Hodge index on `D^W` ⟺ Hodge index on
any detecting cone. So the sign is needed only on a detecting cone, and the question of the phase is:

> **Q.** Is there a cone `C` that is (i) *detecting*, (ii) defined without reference to zeros, and
> (iii) such that `I_∞ ≤ ½ deg²` on `C` follows from a structure of the carrier (polar block, Frobenius
> lattice, positivity of kernels, convexity) rather than from the explicit formula plus zero information?

The corpus already has (ii)+(iii) without (i) (Connes–Consani window `2T ≤ log 2`, cluster B of the
phase-136 map: no finite window detects) and (i) without (iii) (Theorem F's annihilator classes). The
phase must locate the exact operation that separates them.

## D.15 — Intrinsic characterization of the primitive sector (target: PROVED as RESTATEMENT)

1. Prove: `P` is the common kernel of the two rulings, equivalently the radical of the polar block
   `B_pol(F,G) = Φ_F(0)Φ_G(1)+Φ_F(1)Φ_G(0)` (hyperbolic plane `[[0,1],[1,0]]` in the basis `(deg⁻,deg⁺)`);
   `P = K^⊥ ∩ K_odd^⊥` where `K_odd` is any class with `deg⁺K_odd = −deg⁻K_odd ≠ 0`; `P` is
   `I_∞`-orthogonal to `K` and `K` is the unique (up to scale) `I_∞`-positive direction in `span(K,K_odd)`.
2. Prove the Lorentzian criterion: for a symmetric bilinear form `Q` with `Q(K) > 0`, the following are
   equivalent — (a) `Q ≤ 0` on `K^⊥`; (b) `Q(F,K)² ≥ Q(F)Q(K)` for all `F`; (c) `Q(F,G)² ≥ Q(F)Q(G)` for
   all `F,G` in any convex cone with nonempty interior (in the relevant topology) containing `K`. Apply to
   `Q = I_∞` on `D^W` with the **effective cone** `E := {F ∈ D^W : F ≥ 0}` (nonempty interior around `K`
   since `K > 0` with known decay). Conclude: RH ⟺ reverse Cauchy–Schwarz on `E` (Hodge–Riemann /
   Khovanskii–Teissier shape). Label RESTATEMENT; state precisely which topology gives the interior.
3. Compute the polar block's own reverse Cauchy–Schwarz slack: `½ deg²F − B_pol(F,F) = ½(deg⁺F − deg⁻F)²
   = ½(∫F·2sinh(t/2))²`. Hence Hodge index ⟺ `Σ_ρ Φ_F(ρ)Φ_F(1−ρ) ≥ −½(deg⁺F − deg⁻F)²` for all `F`;
   on even `F` this is Weil positivity verbatim. Record: the polar block alone satisfies Hodge index, and
   the whole content sits in the zero sum on the *odd-degree-corrected* class. (PROVED, elementary.)
4. Falsifier: for `Ξ_a`, exhibit the failure of (c) on the effective cone `E_a` explicitly — which
   `F,G ≥ 0` witness it and what support/oscillation they need. This is the first data point for D.16.
5. Answer the owner's question in one paragraph with labels: what distinguishes `P` is isotropy for both
   rulings; the indefiniteness of `I_A` at charts (Paper 43 Thm 14.1) is the absence of the polar block's
   Lorentzian normalization there, which appears only in the Weil completion through `K`.

## D.16 — Detecting closure (target: a theorem about operations)

1. Let `Ops` be a set of linear operations on `D^W`: translations `τ_u`, the multiplier `Π = −∂² + ¼`
   (⟷ `s(1−s)`), polynomial differential operators `p(∂)` (⟷ `p(s−½)`), convolution with fixed kernels,
   dilation. Define the *detecting closure* `⟨C⟩_Ops`. Prove or refute: (a) the CC window cone
   `C_{log2} := {F : supp F ⊂ [−¼log2, ¼log2]}` (so `supp F⋆F^∨ ⊂ [−½log2, ½log2]`) is not detecting
   (PROVED-IN-REPOSITORY, cluster B); (b) its closure under `p(∂)` alone is not detecting (support does
   not grow); (c) its closure under translations alone — is it detecting? Translations move
   `Φ_F(s) ↦ e^{(s−½)u}Φ_F(s)` and produce the exponential growth `e^{a|u|}` at an off-line zero that
   Theorem F's argument needs. Determine the minimal `Ops` such that `⟨C_{log2}⟩_Ops` is detecting.
2. For each operation in the minimal set, decide whether CC's positivity proof (2006.13771, archimedean
   block, Sonin space) survives it. The expected answer is that translation is the operation that both
   creates detection and destroys the support hypothesis of the structural proof. Prove this as a
   statement: *no cone closed under translations and contained in a finite window exists* (trivial) and
   *every detecting cone contains classes whose `F⋆F^∨` has support reaching arbitrarily far* (to prove:
   detection needs `e^{a|u|}` growth, which needs unbounded support — or refute via a bounded-support
   detector, which would be a major finding).
3. Corollary to formulate: the sign on a detecting cone is a statement about **the interaction between the
   polar block and prime powers at arbitrarily large modulus**. Compare with the phase-136 meta-theorem
   and the D.11 requirement `Q(m) ≫ m√log m` (corrections at prime powers `≳ m`). Same phenomenon or not?
   State precisely.

## D.17 — A zero-free cone candidate: the Pólya cone (target: decide detection; locate the zero input)

1. **Pólya's criterion (CLASSICAL, Pólya 1949; Lukacs, *Characteristic functions*, Thm 4.3.1):** an even
   real function `h` with `h(0) = 1`, convex and decreasing on `(0,∞)`, `h → 0` at `∞`, is positive
   definite (a characteristic function). Hence `h = F⋆F^∨` for some `F` (Bochner/Fourier square root),
   without any zero information. Define the **Pólya cone** `C_Pó := {h : even, convex decreasing on
   (0,∞), in the Weil class}` and its Weil functional `W(h) = Σ_ρ Φ_h(ρ)` (= `−I_∞(F,F)` for the
   square root `F`, on the primitive part; handle the polar terms exactly).
2. Decide: is `C_Pó` detecting? Candidate argument: triangles `h_T(t) = (1−|t|/T)_+` (so `F` = indicator
   of `[−T/2,T/2]`), `Φ_{h_T}(ρ) = (2 sinh((ρ−½)T/2)/((ρ−½)))²/T`; an off-line pair contributes
   `~ e^{aT}cos(γT+θ)/(|ρ−½|²T)` while on-line zeros contribute `Σ_γ 4sin²(γT/2)/(γ²T) ≥ 0` of size
   `O(log T)`; the family `T ↦ W(h_T)` therefore goes negative for suitable `T` if some off-line zero
   exists — **but** the maximal real part need not be attained and the tail must be controlled; adapt
   Theorem F's annihilator method (Paper 45 §11) or Landau's lemma to the one-parameter family, or show
   the family is insufficient and enlarge the cone minimally (e.g. `h_T` convolved with Pólya-type
   kernels). Outcome must be: `C_Pó` detecting (PROVED), or a specific obstruction (OPEN with the exact
   missing estimate).
3. On `C_Pó`, write `W(h)` through the explicit formula (Paper 45 Thm 9.4; classical form with
   `Λ(n)n^{−1/2}(h(log n)+h(−log n))`, the archimedean distribution `Ŵ_∞(0,τ) = log π − Re ψ(¼+iτ/2)`
   from Paper 43, and the polar term `Φ_h(0)+Φ_h(1)`) as a **real inequality about `ψ(x)`** with no zero
   appearing: `W(h) ≥ 0 ⟺ Σ_n Λ(n)n^{−1/2}·2h(log n) ≤ ∫h(t)2cosh(t/2)dt + (archimedean term)`. Then:
   (a) show which part is unconditional (Chebyshev's `ψ(x) ≤ 1.04x`-type bounds, monotonicity of `h`,
   Abel summation) and (b) isolate the exact remainder that is not — expected: the remainder is
   `Σ_ρ Φ_h(ρ)` itself after the main terms cancel, i.e. the PNT error term of size `e^{T/2−c√T}` which
   dominates every unconditional term. If so, **say so**: "on the Pólya cone the sign is the PNT error
   term; no structural proof is available on this cone" (label RESTATEMENT, no-go recorded). If not — if
   some structural cancellation appears (e.g. from the convexity of `h` against the convexity of
   `x ↦ ψ(x)` in Chebyshev's sense, or from Mertens-type second moments) — that is the phase's finding.
4. Falsifier: on the `Ξ_a` version, `Λ_a(n) = Λ(n)(n^a+n^{−a})`, polar points `{−a,a,1−a,1+a}` (rank 4).
   Run the same computation. Which term of the real inequality fails, and for which `T`? Does the failure
   come from the polar block (four rulings, no single Lorentzian normalization) or from the prime sum? The
   phase-136 meta-theorem predicts: from the *coupling* — the prime sum's main term matches the polar
   term's `e^{(½+a)T}` growth only under unimodularity of the local roots. Verify.

## D.18 — Synthesis (lead, after the rounds)

One page: the answer to Q as a labelled theorem-or-obstruction; the operation that separates structural
from detecting cones; what the Pólya cone teaches; whether any cone in the corpus (CC window, Pólya,
Frobenius effective cone `mK + Λ_W`, Theorem-F annihilator cone) is both detecting and structurally
signed; and the recommendation for phase 139.

## Deliverables and rounds

`R138_001_BUILDER_ROUND1.md` (D.15 complete; D.16 items 1–2; D.17 items 1–3; D.17.4 at least for the
triangle family), then `R138_002_HOSTILE_AUDIT.md`, repairs `R138_003`, confirmation `R138_004`, lead
decision `R138_005`. README with a table of files. Scripts only if a constant must be certified
(`scripts/`, `--fast` mode, stated margin). No edits to the papers in this phase; corrections of record go
to a "paper-facing list" in the builder report.

## Explicit warnings to the builder

* The Lorentzian criterion (D.15.2) is a statement about quadratic forms; do not let the topology be vague
  — the interior of `E` must be shown nonempty in the topology in which `I_∞` is continuous (Paper 46
  Thm 11.14 gives `|I_∞(E,F)| ≤ C_F deg E`; use it).
* Do not "prove" `W(h) ≥ 0` on any cone by an argument whose error term is the PNT remainder; identify it
  and stop. That is the honest outcome of D.17.3(b), not a failure.
* Do not relabel CC's window result as detecting; do not relabel Theorem F's classes as structural.
* Every new cone must be checked to be a cone (convexity) and to lie in the Weil class (decay, `C²`).
