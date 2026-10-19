# SPEC_SIGN_OBJECT_003: the quotient 𝒬_μ, the bridge between windows and three candidates filtered by P10 (phase 200, round 3)

Synthesizer. Pure mathematics, no new numerics (the μ = 15 data are cited from MORI15_EXTREMAL_001 and
K3_GAMMA_001, NUMERICAL). Row D and Lemma L′♯ are treated as independent goals; no
equivalence with any other statement is invoked or used.
**No sign is proved. L′♯ OPEN. Row D OPEN.**

**Read.** Phase 200 README; SPEC_SIGN_OBJECT_002; AUDIT_200_SPEC_002 (P9′, P10); Q2_LADDER_001 (Lemma R, R-Q2,
Theorem Q2.1, rough 0/1 comb, "bridge between windows" residual); K1_OSG_001 (R-K1); K3_GAMMA_001 (K3.1); LEDGER_L5_META §2
(negative space, areas 1–11); LEDGER_L1 (S1–S7); phase 199: AUDIT_CONSTRAINTS_001, MORI15_EXTREMAL_001; Paper 47:
def:ext, rem:ext-killing, prop:ext-gauge, lem:ext-ellbound, lem:monoT ("Lemma M" of monotonicity in T), definitions of
𝔞_T, P_T, λ_A. ROUTES-TRIED index: full README "Phase 200"; 06_OPEN_RESIDUES (L2_016 "Frobenius doubling induction in T",
W-loc); 03_PHASES (P37-2 "inertia readers (winding)", P49-2 Maslov); AUDIT_PHASE193 row 82 (Bohr–Jessen).

**Notation.** μ ≥ 5, T = ½log μ, λ = e^T = √μ. Admissible at T, leak, summation map Φ_f, E, Ψ_f, r_f = 𝓕f|_{(λ,∞)}, Z, 𝒢_T,
𝒢̄_T, ℓ(g), core: as in def:ext. Ψ̌_f(y) = Ψ_f(−y) = (Zr_f)(e^y), y > T. 𝒲 = complete Weil form on the line.
D_μ = ζM_μ − 1, c_N as in SPEC_002. For a function F supported on (0,∞), Φ_F is its summation image.

---

## A. The quotient 𝒬_μ, described concretely

### A.1 What 𝔑_μ is inside the exterior (PROVED)

P9′ asks for 𝒬_μ := (exterior data)/𝔑_μ, with 𝔑_μ the extended radical: translates τ_s Z_h of summation images (Lemma R)
plus 𝒢̄_T. The concrete question is **which elements of that radical live in the exterior** y=−x>T, because only those act
on the exterior datum. The answer is exact.

**Lemma A.1 (the exterior summation radical is the gauge; PROVED).** Let h be in the core of some T_h, with B(h) = 0, and let
F_h(t) = t^{−½}h(−log t) (Lemma R, step 1), so Z_h := ζ(∂)h = Φ_{F_h}(−·).
- (a) For every s ∈ ℝ, τ_s Z_h = e^{s/2}·Φ_{F_{h,s}}(−·) with F_{h,s}(t) := F_h(e^s t). If s ≥ T + T_h, then
  supp F_{h,s} ⊂ [0, e^{T_h−s}] ⊂ [0, 1/λ], and F_{h,s} (extended evenly) belongs to 𝒢_T.
- (b) Conversely, if G is even, C², with compact support, G(0) = 𝓕G(0) = 0, and Φ_G ≡ 0 on (−T, ∞), then
  supp G ⊂ [−1/λ, 1/λ], i.e. G ∈ 𝒢_T.
- (c) Consequently, the subspace of 𝔑_μ formed by summation images supported in the exterior coincides with
  {Φ_φ : φ ∈ 𝒢_T}, and its closure in r coordinates is 𝒢̄_T.

*Proof.* (a) Change of variable: e^{(y−s)/2}·Σ_N F_h(Ne^{−(y−s)}) = e^{s/2}·e^{y/2}... is rearranged as in Lemma R. F_h
has support in [e^{−T_h}, e^{T_h}], so F_{h,s} has it in [e^{−T_h−s}, e^{T_h−s}]. For s ≥ T + T_h the right endpoint is
≤ e^{−T} = 1/λ. F_{h,s} vanishes near 0 (C² and F(0) = 0) and 𝓕F_{h,s}(0) = 2e^{−s}∫F_h = 4e^{−s}B(h) = 0.
(b) Let S(v) := Σ_{m≥1} G(mv). By hypothesis S(v) = 0 for v > 1/λ. For u > 1/λ, every nu with n ≥ 1 satisfies nu > 1/λ, and
Möbius inversion (finite sum, G of compact support) gives G(u) = Σ_n μ(n)S(nu) = 0.
(c) Combination of (a) and (b) with prop:ext-gauge. □

Particular case (Lemma Q2.1 and Lemma R): the combs R_P with P supported on d ≥ μ are translates with s = log d ≥ 2T, which is (a)
with T_h = T. **The whole "ladder", every sub-comb p | N and every difference of mollifiers are, in the exterior, gauge.**

**Corollary A.2 (P9′ = prop:ext-gauge; PROVED).** With 𝔑_μ^{sum} := exterior summation radical,
 𝒬_μ^{sum} := L²(λ,∞)/𝒢̄_T (coordinates r, via Ψ̌ = Zr),  ‖[r]‖²_𝒬 := dist²(r, 𝒢̄_T),
and for g in the core, **‖[r_f]‖²_𝒬 = ℓ(g)/2** (prop:ext-gauge, CITED from Paper 47 itself). The "new" quotient structure of
P9′ is exactly the escape quotient the paper already has. The natural norm of 𝒬_μ **is the escape**, and K3.1 describes it at the
extremal: ℓ(f*) ≈ d₄‖f*‖²/(1 + r²), with r = ψ₄(0)/ψ₀(0) = 0.6073 at μ = 15 (coincidence 0.7306 = 0.7306, NUMERICAL).

**Open A.3.** Is the complete radical of 𝒲 intersected with the exterior larger than 𝔑_μ^{sum}? That is, are there exterior
functions, with decay e^{−3y/2}, in the radical of 𝒲 that are not summation images? By A.4 below, this is equivalent to
knowing whether the kernel of the zero-coordinates in the exterior is the closure of 𝒢̄_T. **ARGUED** that yes (Beurling–
Malliavin-type density of summation images in the kernel of zero evaluation); **OPEN** as a statement.

### A.4 Coordinates that separate points of 𝒬_μ

The four candidates of the target are examined.

**(i) Zero-coordinates.** For each nontrivial zero ρ, z_ρ([Ψ]) := Φ_Ψ(ρ) (Mellin transform of the reflected datum).
- It is well defined on 𝒬_μ^{sum}: if φ ∈ 𝒢_T, Φ_φ has Mellin ζ(s)·𝓜φ(s), which vanishes at ρ. **PROVED.**
- On the datum: z_ρ([Ψ̌_g]) = ĝ(γ)·D_μ(ρ) = −ĝ(γ) (rem:ext-killing (iii); D_μ(ρ) = −1). **PROVED.** The value **does not depend on μ**.
- 𝒲 descends and in these coordinates it is 𝒲[Ψ] = Σ_ρ z_ρ([Ψ])·z_{1−ρ}([Ψ]) (rem:ext-killing (iii), with the polar term null
  because A(Ψ̌) = 0, T.1(b)). **PROVED** in the A = 0 sector.
- Injectivity on the image ℐ_μ := {[Ψ̌_g] : g ∈ core_T}: if ĝ(γ) = 0 at every ordinate, then ĝ (entire of exponential type ≤ T)
  has a zero-counting function ≳ (t/2π)log t, which exceeds the Jensen bound O(t) for finite exponential type;
  hence g = 0. **PROVED** (Jensen + Riemann–von Mangoldt, CITED).
- Injectivity on all of 𝒬_μ^{sum}: this is A.3. **OPEN.**
- **Dimension.** For any J, the map g ↦ (ĝ(γ_1),…,ĝ(γ_J)) from the core to ℂ^J is surjective (the functions
  e^{iγ_j x} are linearly independent in L²(−T,T)), so dim ℐ_μ = ∞ and dim 𝒬_μ = ∞. **PROVED** (infinitude of zeros,
  CITED Hardy).

**Usage warning (P4, cor:void C_zeros).** The zero-coordinates **describe** 𝒬_μ, but they are not admissible working
coordinates for the sign: every argument that reads 𝒲 as a function of the z_ρ is on the zero side and is excluded (P4, index:
"zero-side reverse engineering always negative", P8-ThmC). In this memo they are used only for two structural facts: (α) 𝒬_μ
is infinite-dimensional; (β) the class of the datum does not depend on μ.

**(ii) Moments at the poles of Γ_ℝ (s = −2k).** These are not coordinates: Φ_Ψ(−2k) only converges for k = 0 with decay
e^{−3y/2}, and on summation images it equals ζ(−2k)𝓜φ(−2k) = 0 for k ≥ 1 (when it exists). 𝒲 does not see them (the sum of
rem:ext-killing runs over nontrivial zeros; the poles of Γ_ℝ cancel against the trivial zeros inside ξ, SPEC_002 A.1).
**PROVED: they separate nothing.**

**(iii) The escape ℓ.** It is not a coordinate: it is the **norm** of the quotient (Corollary A.2). **PROVED.**

**(iv) The rough 0/1 comb.** It is not a coordinate: it is a **canonical representative** of the class. By Theorem Q2.1(4),
[Ψ̌_g] = [Ψ_rug(g)] with Ψ_rug(g) := Σ_{N>1, P⁻(N)≥μ} N^{−½}τ_{log N}g, and z_ρ(Ψ_rug) = ĝ(γ)(ζ(ρ)Π_{p<μ}(1−p^{−ρ}) − 1) = −ĝ(γ).
New and elementary fact: **in the rough representative there are no exact window alignments**. If N, N′ are μ-rough and
N′ = nN with 2 ≤ n < μ, then n has a prime factor < μ dividing N′: contradiction. Consequently, for the
rough representative the T.3 summands with 2 ≤ n < μ vanish identically (c_N c_{nN} = 0). **PROVED.** The window
atoms only act through near-alignments N′/N ≈ n, never through the sub-lattice Λ_n. (This is **not** a contradiction with
SPEC_002 T.3: T.3 refers to the c_N representative; the two representatives differ by gauge.)

**Summary of A.4.** 𝒬_μ (summation version) = L²(λ,∞)/𝒢̄_T with norm ℓ/2; known separating coordinates = zero
values (injective on ℐ_μ, PROVED; on all of 𝒬, OPEN); the form 𝒲 descends (PROVED, by definition of the radical and by
rem:ext-killing's formula); Γ_ℝ's moments do not separate; ℓ is the norm; the rough comb is a representative with no exact
alignments.

### A.5 The bridge between windows (open residual of Q2), formalized as a map between quotients

Let T′ = T − ½log 2 (level μ/2), λ′ = λ/√2.

**Lemma A.5 (the bridge; PROVED).**
- (a) 𝒢_T ⊂ 𝒢_{T′} (support [−1/λ, 1/λ] ⊂ [−1/λ′, 1/λ′]) and L²(T,∞) ⊂ L²(T′,∞). Hence the inclusion induces a well-defined
  linear map ι: 𝒬_μ → 𝒬_{μ/2}, [Ψ]_T ↦ [Ψ]_{T′} (in Ψ̌ coordinates).
- (b) For g ∈ core_{T′} ⊂ core_T, let 𝒜_T(g) := {f admissible at T, E_T f = g}. Then **𝒜_T(g) ⊂ 𝒜_{T′}(g)**: if
  f ∈ 𝒜_T(g), Φ_f(x) = g(x) = 0 for x ∈ [T′, T); for e^x ∈ [λ′, λ) one has ne^x ≥ 2λ′ > λ if n ≥ 2, hence f(e^x) = 0, i.e. f = 0
  on [λ′, λ), and f is admissible at T′. The reflected datum is the **same function**: Ψ_f^{(T′)} = Ψ_f^{(T)}, because Φ_f = g = 0 on
  (−T, −T′].
- (c) ι([Ψ̌^{(μ)}_g]) = [Ψ̌^{(μ/2)}_g]. Moreover, in comb coordinates, Ψ̌^{[μ]} − Ψ̌^{[μ/2]} = R_{M_μ−M_{μ/2}}, whose translates have
  d ≥ μ/2 and are gauge at T′ by A.1(a) (e^{T′}/d ≤ 1/λ′).
- (d) 𝒲 is compatible: 𝒲[ι[Ψ]] = 𝒲[[Ψ]]. This is the exterior version of lem:monoT: there, extension by zero
  core_{T′} ↪ core_T leaves 𝔞 and W unchanged; here the dual map between quotients leaves 𝒲 unchanged.
- (e) The zero-coordinates commute with ι (z_ρ∘ι = z_ρ). On ℐ, the bridge is the **identity** in zero-coordinates.

**What is NOT compatible: the norm.** ‖ι[r]‖_{𝒬_{μ/2}} versus ‖[r]‖_{𝒬_μ}: by (b) the infimum at T′ runs over a
larger set (𝒜_{T′} ⊃ 𝒜_T), but it measures the escape outside a narrower band (leak_{λ′} ≥ leak_λ). The two effects compete.
- **OPEN (Lemma B.1 below):** is ℓ_{T′}(g) ≥ ℓ_T(g) for g ∈ core_{T′}?
- Indication (K3.1, ARGUED): in the sector that saturates K3.1, ℓ_T ≍ d₄(c_T)‖f‖², with d₄ = 1 − λ₄(c) decreasing
  super-exponentially in c ≍ μ; if the optimizer at T′ is comparable, ℓ_{T′}/ℓ_T is huge and the inequality holds with
  margin.

**Verdict on Q2's residual.** The bridge exists, is canonical, and is **isometric for 𝒲** (PROVED). Therefore it cannot be a
source of sign by itself: it is Q2's ladder, now as a map. Its only nontrivial content is the **ratio of norms
ℓ_{T′}/ℓ_T** on ℐ_{μ/2} ↪ ℐ_μ. That ratio contains no Λ (it is a prolate-spheroidal problem plus a linear restriction, like K3.1).
- Q2's residual: **closed as a sign source** (NO-GO, PROVED: isometry for 𝒲).
- Q2's residual: **reopened as a tool** for transporting L′♯ between levels (B.1).

**Exact consequence (CONDITIONAL on B.1).** If ℓ_{T′} ≥ ℓ_T on core_{T′}, then L′♯ at level μ/2 implies L′♯ at
level μ **on the old directions** core_{T′}, with the same constant up to the factor 2^{A}. All of the content of the step
μ/2 → μ lies in the **new directions**, orthogonal under 𝒲 to ℐ_{μ/2}. These are the ones that see the contacts
n ∈ [μ/2, μ) and the coefficients c_N = −μ(N) of the block [μ, 2μ).

**Index warning.** 06_OPEN_RESIDUES records "Frobenius doubling induction in T: NO-GO (Tate not transported),
L2_016". Difference, stated in writing:
- There, the Tate moments did not transport between windows.
- Here, the transport happens in the exterior quotient, where the polar row is gauge (GG.0; A(Ψ̌) = 0, T.1(b)). The
  Tate moments do not travel: they are quotiented out.
- Bridge A.5 is exact in 𝒲.
- What does not transport is ℓ, and that is a problem with no arithmetic in it.
- The new reason holds for the map; for the full inductive step see C1.

---

## B. P10 filter on the areas of the negative space, and three candidates

### B.0 Prior filter (applied before proposing)

Operative rule derived from A: **every quadratic functional invariant under 𝔑_μ^{sum} is a form on ℐ_μ ⊂ 𝒬_μ. The form 𝒲 is
one of them, and it does not depend on μ in zero-coordinates.** A candidate can only contribute something if it is (1) a
functional distinct from 𝒲 that is compared to 𝒲, (2) a comparison between levels μ, or (3) an integer invariant of the pair
(𝒲, ℓ). Any rewriting of 𝒲 in another representative is P10-tautological.

**Area 5 (geometry of numbers over log ℕ), naive form: NO-GO by P10 (PROVED).**
- The datum has integer coefficients c_N on the translates N^{−½}τ_{log N}g.
- The exterior generators of 𝔑^{sum} with integer coefficients are the rows e_d = 1_{d|·}, with d ≥ μ (A.1(a), with h = g).
- The system {e_d}_{d≥μ} is unitriangular. The finite integer reduction of c on [μ, X) is unique and leaves exactly the
  representative c^{(X)} (level-X mollifier): it is Q2's ladder and 𝒲 = W_T(g) holds for every X.
- The "complete" reduction (X → ∞) does not converge (Σc_N²/N = ∞, SPEC_002 T.2).
- Successive minima and Hermite/Minkowski reduction in this lattice only pick representatives of the same class. By P10
  any statement about 𝒲 of the reduced form is 𝒲[g].

**Area 6 (×2,×3 rigidity on zero-coordinates): NO-GO by P10 + P4 (PROVED).**
- In zero-coordinates, τ_{log p} acts as unimodular diagonal multiplication z_ρ ↦ p^{−iγ}z_ρ (up to the normalization's
  p^{½} factor), and 𝒲 is translation-invariant.
- The dilation action on the f side (f ↦ f(p·)) produces the sub-comb p | N, which is radical (Q2.1(3)). On 𝒬_μ it acts as **zero**
  on the class.
- The ×2,×3 semigroup then acts trivially on the class, or diagonally by phases on z_ρ. The latter is the
  Kronecker line on the phase torus (γ log p): front H, "Near" = Kronecker − Haar, already in the index.
- No invariant measure sees 𝒲, which is invariant.

Areas 1 (variational stability), 7 (dimension/index), and, for the third candidate, a version of 5 that does not
reduce representatives but **counts near-alignments** in the rough representative (A.4(iv)), remain.

---

### C1. Duplication stability in the quotient (area 1: quantitative variational stability)

**Definition.** Let ℛ_μ([r]) := 𝒲[[r]]/‖[r]‖²_𝒬 on ℐ_μ \ {0}, i.e. ℛ_μ(g) = 2W_T(g)/ℓ_T(g). Let κ(μ) := inf_{ℐ_μ} ℛ_μ. Let
ℐ_μ^{new} := {[Ψ̌_g] : g ∈ core_T, 𝒲([Ψ̌_g], ι^{−1}ℐ_{μ/2}) = 0} be the 𝒲-orthogonal complement of the old directions. Define the
**duplication deficit**
 δ_μ := inf_{ℐ_μ^{new}} ℛ_μ − θ·κ(μ/2),
and the **escape comparison constant** β_μ := inf_{g∈core_{T′}} ℓ_{T′}(g)/ℓ_T(g).

**Target theorem C1 (duplication stability).** There exist θ ∈ (0,1] and μ₀ such that, for μ ≥ μ₀: (i) β_μ ≥ 1; (ii)
δ_μ ≥ 0; and (iii) the cross term between old and new directions is null in 𝒲 (it is, by construction) and is bounded
in ℓ by (1 − θ′)·(ℓ_old + ℓ_new) ("angle" in 𝒬 between ℐ_{μ/2} and ℐ_μ^{new} bounded below).

**⇒ L′♯.** (i)–(iii) give κ(μ) ≥ θθ′·min(κ(μ/2), …), and by induction κ(μ) ≥ κ(μ₀)·(θθ′)^{log₂(μ/μ₀)} = c·μ^{−A}. With
κ(15) > 0 certified (Mori: Schur margin 2.40·10⁻⁷⁰ against ℓ(g*) ≤ 8.5·10⁻⁷⁰; CITED/NUMERICAL), that is exactly the
form of L′♯: W_T ≥ cμ^{−A}ℓ. The output is a **square**: ℓ = 2dist² in 𝒬.

**Explicit P10.**
- (i) contains no Λ: it is a statement about prolate functions plus gauge.
- (iii) is the geometry of two subspaces in a Hilbert space.
- All Λ falls into (ii), restricted to ℐ_μ^{new}. (ii) is **not** 𝒲[g]: it is 𝒲 on a fixed infinite codimension compared to
  κ(μ/2), a number from another level. It is not tautological.
- It is indeed a quantitative positivity statement on a subspace: the REF-D risk lies in (ii) and is declared.

**Where exact Λ enters.** Only in ℐ_μ^{new}. The new directions are determined by two things:
- the new contacts n ∈ [μ/2, μ) (weights v_n = 2Λ(n)n^{−½} with log n ∈ [2T′, 2T));
- in the exterior, the block c_N = −μ(N) on [μ, 2μ) (SPEC_002, PROVED). Equivalently, in the rough representative: the
  primes of [μ/2, μ) stop being rough when passing from μ/2 to μ.

The step μ/2 → μ is literally "expelling the primes of [μ/2, μ) from the rough comb". It is an operation of (ℕ, ·) indexed
by (ℕ, +, order), compatible with the semiring principle.

**Failure in the identity for the falsifiers.**
- **cΛ, c < 1:** A.1(a) uses Lemma R, which uses Poisson on ℤ with a_n ≡ 1. For c ≠ 1 the series is ζ^c and there is no radical
  summation image (GG §4, ARGUED). The quotient 𝒬^{(c)} is not defined as L²/𝒢̄: the right-hand side of A.2 is missing. **ARGUED.**
- **Beurling:** there is no ℕ lattice nor Poisson. 𝔑^{sum} does not exist and A.1(b) (Möbius inversion over multiples nu) makes no
  sense. **PROVED** for Beurling without additive structure.
- **DH:** periodic Poisson exists (conductor 5), so there is a twisted gauge 𝒢^{DH}. The rule "expel primes of [μ/2, μ)"
  fails because the truncated inverse is not multiplicative: the block [μ, 2μ) is not −μ_{DH}(N). The identity of the new
  step fails. **ARGUED** (the DH analogue of SPEC_002 must be written).
- **a_P (deleted primes):** shares A.1, A.2 and A.5 (only v_n changes). Hence (ii) must fail: at the level where the
  CERT_FALSIFIERS battery certifies negativity, δ_μ < 0. **The candidate passes this test only if the proof of (ii) uses the exact
  list of primes of [μ/2, μ).**
- **cΛ, c > 1:** cor:ext-cfals gives κ_c(μ) < 0 eventually. For integer c (c = 2, ζ² = Σd(n)n^{−s}) Poisson and summation do
  exist (divisors), so A.1–A.5 have analogues. (ii) must fail there. This is the **hard test**.

**Index (new reason).**
- L2_016 (doubling induction in T, NO-GO by Tate): see A.5. There, the window form was transported with Tate moments.
  Here, the exterior class is transported, where the polar row is gauge, and the transport is 𝒲-isometric (PROVED).
- W-loc / thm:nolocal: C1 does not localize in x. It separates by levels of μ in the quotient; there is no partition of unity nor IMS
  errors (which would be O(‖g‖²) and would violate P2).
- lem:contA / Gate 1 (continuity of λ_A in T): those routes read λ_A, which is the L² norm bound. Here the norm is ℓ, and the
  monotonicity reduces to B.1, which was not in the index.
- **Declared risk:** if (ii) can only be proved with a prime-counting estimate in [μ/2, μ) (Chebyshev/short PNT), it
  falls into an exhausted tool (phase 200 README).

**Test at Mori μ = 15.**
- κ_emp(15) = W/ℓ ∈ [0.56, 1.09] (MORI15 §2, NUMERICAL).
- C1 predicts that, in the step 7.5 → 15, the extremal g* is **almost entirely in ℐ^{new}**:
  - g* is a bump of width σ ≈ 0.21 centered (MORI15); it lives in core_{T′} with T′ = ½log 7.5 = 1.007 only
    approximately;
  - the new contact in [7.5, 15) is n ∈ {8, 9, 11, 13}.
- Falsifiable prediction: the 𝒲-orthogonal projection of g* onto core_{T′} has ℓ_{T′} ≥ ℓ_{15}. This is the pointwise
  version of B.1.
- It can be computed with Mori's matrices at μ = 7.5, if they are among those released (AUDIT_ZENODO_FRONTIER §B1). **Not
  computed here.**

**Exact first lemma (B.1, no sign, no Λ).** *For g ∈ core_{T′}, ℓ_{T′}(g) ≥ ℓ_T(g).*
- Route: take the optimizer f′ ∈ 𝒜_{T′}(g) and correct it by φ ∈ 𝒢_{T′} supported on [1/λ, 1/λ′] so that the result
  lies in 𝒜_T(g).
- One must bound leak_λ(f′ + φ) ≤ leak_{λ′}(f′). It is a double-orthogonality problem for prolate functions on two bands (c_T, c_{T′}),
  with restrictions f(0) = 𝓕f(0) = 0.
- If B.1 fails, C1 dies at (i), with an explicit falsifier.

**Risk.** High at (ii): partial REF-D and risk of a prime-counting wall. Low at (i), which is pure prolate-function theory.

---

### C2. Index of the exterior symbol (area 7: positivity by dimension/index)

**Definition.** The symbol of 𝒲 on the datum is |ĝ(t)|²·|D_μ(½+it)|²·(…) (T.1). In 𝒬_μ, the factor that depends on μ is the
almost-periodic function D_μ(½+it) = Σ_{N≥μ} c_N N^{−½−it}, with no constant term (c_1 = 0 in D_μ). Define the **exterior
index**
 𝔦_μ := −ind T_{D_μ} = number of zeros (with multiplicity) of D_μ(s) at ½ < Re s, counted by mean motion
 (Bohr; Jessen–Tornehave for almost periodic functions in strips, CITED),
normalized by height: 𝔦_μ(H) := #{s : D_μ(s) = 0, Re s > ½, |Im s| ≤ H}. Together with n₋(μ) := negative index of 𝒲 − εμ^{−A}ℓ
on ℐ_μ.

**Target theorem C2.** n₋(μ) ≤ lim sup_H [𝔦_μ(H) − 𝔦^{model}_μ(H)], where 𝔦^{model} is the model's count with the same
initial block c_N, N < X. And the right-hand side is 0 because the zeros of D_μ = ζM_μ − 1 to the right of ½ are 1-points of
ζM_μ, whose count by height is given by a-point theory (Levinson; CITED, to be verified in the index). **Output =
count.**

**Explicit P10.**
- n₋(μ) by itself is the inertia of W_T on the core: P10-tautological. It is not proposed as the object.
- The object is 𝔦_μ: an invariant of D_μ alone, without 𝒲, an integer, which is not 𝒲[g].
- The inequality n₋ ≤ 𝔦 is the content. **Passes P10.**

**Where exact Λ enters.** In D_μ, a_n ≡ 1 enters (via ζ) and μ(d) (via M_μ). Λ enters the symbol of 𝒲 through
m − Σv_n cos(t log n). By rem:ext-killing (ii), once in the exterior the comb appears only via Λ∗1 = log, i.e. via
a_n ≡ 1. **The index sees Λ only as "entire ζ".**

**Failure in the identity.**
- **cΛ, non-integer c:** D^{(c)} = ζ^c M^{(c)} − 1 has branch points where ζ vanishes. T_{D^{(c)}} is not Fredholm in the
  standard almost-periodic sense, so 𝔦 is not defined. **PROVED** (for c ∉ ℤ, the branch is not single-valued).
- **c = 2:** D^{(2)} is almost periodic and meromorphic, and 𝔦 is defined. The inequality must fail there (cor:ext-cfals).
  It is the hard test.
- **Beurling:** there is no M_μ with a gap (the gap c_N = 0 on [2, μ) uses ℕ), so 𝔦 changes shape.
- **DH:** D^{DH}_μ exists (periodic Dirichlet series) and has zeros to the right (DH has them in Re s > 1 in positive count
  by height, CITED Davenport–Heilbronn). 𝔦^{DH} > 0 is compatible with n₋^{DH} > 0. **Consistent, not a proven separator.**
- **a_P:** D_μ is the same (a_n ≡ 1 does not change). 𝔦 is identical and n₋ differs. **C2 does not separate a_P in the index: partial
  NO-GO (PROVED)**, unless the model 𝔦^{model} depends on Λ, which reintroduces the comb.

**Index (new reason).** P37-2 "inertia readers (winding): NO-GO, winding wall = sieve wall"; P49-2 Maslov; row 82
Bohr–Jessen (retry R164_102, falsifier ζ·E). New reason stated:
- The symbol here is exterior and mollified (c_1 = 0, gap), not the window one.
- But **R-Q2 forbids mollifiers as coordinates**, and M_μ enters the symbol.
- Also the a_P falsifier is blind by construction.

**Filter verdict: C2 is proposed only as a control statement, with REF-D risk in the inequality and partial
NO-GO against a_P (PROVED).**

**Test Mori μ = 15.** 𝔦_15(H) is computable in principle: the zeros of ζM_15 − 1 to the right of ½. For large Re s,
D_15 ~ −15^{−s}, so there are no zeros for Re s ≥ σ₀. C2's prediction: n₋(15) = 0 (certified). Then 𝔦_15 − 𝔦^{model} ≥ 0.
It does not discriminate.

**Exact first lemma.** Mean motion formula for D_μ: 𝔦_μ(H) = (H/π)·(log μ)·(…) + O(1)?
- This is the Jessen–Tornehave law applied to −μ^{−s}(1 + Σ_{N>μ}(c_N/(−μ(μ)))(N/μ)^{−s}) in the strip.
- No sign.

**Risk.** Very high: blind to a_P and in tension with R-Q2.

---

### C3. Near-alignments in the rough representative (area 5, counting version; area 11 in its S⁺ form)

**Definition.** In the canonical representative Ψ_rug (A.4(iv)) exact alignments with 2 ≤ n < μ do not exist (PROVED). The entire
effect of the window comb on the class goes through **near-alignments**: rough pairs (N, N′) with |log(N′/(nN))| < 2T. Define
the **near-alignment measure**
 𝔄_μ^{(n)}(du) := Σ_{N,N′ rough, N′≠N} (NN′)^{−½}δ_{log(N′/(nN))}(du), restricted to |u| < 2T,
and the functional 𝔅_μ(g) := Σ_{n<μ} v_n·⟨𝔄_μ^{(n)}, c_g⟩ (comb part of 𝒲 on the rough representative), versus the
archimedean part 𝔇_μ(g) := 𝒲_∞[Ψ_rug].

**Explicit P10 (and P2).**
- 𝔇_μ − 𝔅_μ = 𝒲[Ψ_rug] = W_T(g): the difference is tautological.
- Each piece separately **diverges**: Ψ_rug ∉ L² in absolute sense, because Σ_{p≥μ}1/p = ∞ and the series converges only as a
  class. Violates P2.
- The truncated version (N, N′ ≤ X) has O(1)·‖g‖² pieces versus W ~ 10⁻⁷⁰ in Mori.
- **NO-GO by P2/P10 in this form (PROVED: divergence).**

**Surviving variant.** Do not use 𝔄 as a piece, but as a **counting datum inside C1's new step**. Passing from μ/2 to
μ, the difference of rough representatives is Ψ_rug^{(μ/2)} − Ψ_rug^{(μ)} = Σ_{N rough at μ/2, with some p | N, p ∈ [μ/2, μ)}.
That comb now has exact alignments with the new contacts n = p ∈ [μ/2, μ): the pairs (N, pN). This is the only
exact appearance of the lattice Λ_p, and the count of those pairs is the T.3 sub-lattice restricted to p ∈ [μ/2, μ).

Goal C3′: **in ℐ_μ^{new}, the contribution of the new contacts is a count of pairs (N, pN) on the rough lattice,
and the positivity of (ii) of C1 reduces to a counting inequality** of the type
 Σ_{p∈[μ/2,μ)} v_p·#{weighted exact alignments} ≤ (1 − θ)·(archimedean diagonal term in ℐ^{new}).

**Exact Λ.** Exactly v_p, p ∈ [μ/2, μ), and the rough lattice (which uses multiplicative ℕ).

**Falsifiers.**
- **a_P** with P ∩ [μ/2, μ) ≠ ∅ changes the count: separates.
- **Beurling:** the rough lattice of generalized primes exists, but there is no radical summation (A.1 fails): the identity
  fails.
- **cΛ, c < 1:** same as C1.
- **DH:** not multiplicative, no rough lattice with c_N = 1: the identity fails. **ARGUED** in all three cases.

**Index.** E_001/F_001 (pre-cancellation ratio classes), INV_C (pair counts, Farey), INV_H.
- New reason: the count is done **in the quotient, in the rough representative**, only on the new directions and only with
  new contacts.
- The ratio classes of E/F were on the complete datum c_N, with all contacts.
- Risk: **if the diagonal term in ℐ^{new} is O(1)·‖g‖²**, C3′ inherits the violation of P2. One must prove that ℐ^{new}
  is at scale ℓ.

**Test Mori μ = 15.**
- New contacts in [7.5, 15): primes 11, 13 (n = 8 and n = 9 are powers of old primes and remain non-rough at
  both levels).
- The difference comb between 7.5 → 15 has coefficients 1 on N rough-at-7.5 divisible by 11 or 13: 11, 13, 121, 143, 169,
  11·17, ….
- It matches the block c_{2M} = −[11|M] − [13|M] of Lemma Q2.1(b) at μ = 15. **Exact consistency (PROVED).**
- Falsifiable prediction: the pairs (11, 121), (13, 143), (11, 143), … are the only exact window atoms, and their total
  weight at g* must be at scale ℓ*.

**Exact first lemma.** Closed formula for the difference of rough representatives between μ/2 and μ, as a comb
ζ_{≥μ/2}·(1 − Π_{p∈[μ/2,μ)}(1 − p^{−s})) (PROVED in one line via the Euler product), and its exterior radicality. It is expected
not to be radical (it is not ζ times a finite polynomial, because it contains ζ_{≥μ/2}). Determine which part is gauge at T and which
part stays in ℐ^{new}.

**Risk.** Medium: P2 at the diagonal.

---

## C. Ranking and lemma to launch

1. **C1 (duplication stability in the quotient).** It is the only candidate that (a) uses this round's new structure (the
   bridge A.5, 𝒲-isometric, PROVED), (b) isolates all the arithmetic in a fixed-codimension subspace (the new
   directions: contacts [μ/2, μ), block c_N = −μ(N)), (c) has a square output (ℓ = 2dist²), and (d) separates a_P and c = 2 only
   if the proof uses the exact list of new primes.
2. **C3′** as the arithmetic content of (ii) of C1: count of new exact alignments in the rough representative. It is not an
   independent candidate.
3. **C2**: control only. Blind to a_P (PROVED), in tension with R-Q2.

**Lemma to launch: B.1 (escape comparison along the bridge).**
*For every μ ≥ μ₀ and g ∈ core_{T′}, T′ = T − ½log 2: ℓ_{T′}(g) ≥ ℓ_T(g).*
- It is exact, with no sign, no Λ. Attacked with double orthogonality of prolate functions on two bands plus the restrictions
  f(0) = 𝓕f(0) = 0 (K3.1's framework).
- Its falsification kills C1 at (i) with an explicit counterexample.
- Its proof turns the transport of L′♯ between levels into a statement about the new directions only.
- Optional numerical test: Mori's matrices at μ = 7.5, if they exist.
- Second lemma, in parallel and with no sign: the closed formula for C3′ and the determination of which part of the rough
  difference is gauge at T.

**New restrictions for AUDIT_CONSTRAINTS.**
- **R-Q3 (PROVED):** in the exterior, the summation radical is the gauge (A.1). Hence every "quotient structure" is
  prop:ext-gauge and its norm is ℓ. No object may ask for another natural norm without justifying A.3.
- **R-Q4 (PROVED):** the bridge between windows is 𝒲-isometric (A.5(d)). All content between levels lies in ℓ or in the
  new directions.
- **R-Q5 (PROVED):** in the rough representative there are no exact window alignments (A.4(iv)).

**For the index (round 3):**
- Naive number geometry on log ℕ in the quotient: NO-GO, P10 (it is the ladder).
- ×2,×3 on the class: NO-GO, P10 + P4.
- Q2's "bridge" residual: closed as a sign source (isometry) and reopened as B.1.
- C3 in piece form: NO-GO by P2 (divergence).
- C2: partial NO-GO against a_P.

Row D: OPEN. L′♯: OPEN.

---

## Summary (≤300 words)

**A. What 𝒬_μ is.**
- Lemma A.1 (PROVED): in the exterior, the summation radical (translates of Z_h, ladder, sub-combs p|N) is exactly the gauge
  𝒢_T. By Möbius inversion, every summation image null on (−T, ∞) has support in [−1/λ, 1/λ].
- Hence 𝒬_μ = L²(λ,∞)/𝒢̄_T, its natural norm is ℓ/2 (prop:ext-gauge) and P9′ adds no new structure.
- Zero-coordinates z_ρ = −ĝ(γ): well defined, independent of μ, and injective on the image of the core (PROVED, Jensen).
  They give dim ∞ (PROVED). Their injectivity on all of 𝒬 is OPEN (A.3). P4 forbids using them for the sign.
- Γ_ℝ's moments do not separate points (PROVED).
- In the rough representative there are no exact window alignments (PROVED).

**Bridge between windows (A.5, PROVED).** There is a canonical map ι: 𝒬_μ → 𝒬_{μ/2}, with 𝒜_T(g) ⊂ 𝒜_{T′}(g).
- ι is isometric for 𝒲 and is the identity in zero-coordinates. It is the exterior version of lem:monoT.
- As a sign source: NO-GO.
- The only nontrivial content is the ratio ℓ_{T′}/ℓ_T: this is Lemma B.1, OPEN and Λ-free.

**B. Candidates.** The P10 filter kills naive number geometry (integer reduction = ladder) and ×2,×3 rigidity (the class
is invariant or broken by phases).
- **C1, duplication stability:** κ(2μ) ≥ θκ(μ) plus Mori's κ(15) give L′♯. All the Λ lies in the new directions
  (contacts [μ/2, μ), block −μ(N)). Risk: prime-counting wall.
- **C2, index of the exterior symbol D_μ:** blind to a_P (partial NO-GO) and in tension with R-Q2.
- **C3, rough near-alignments:** the pieces diverge (NO-GO by P2). C3′ survives, which is the count of pairs (N, pN) with
  p new inside C1, and matches exactly Q2.1(b) at μ = 15.

**C. Ranking:** C1 > C3′ (as a sub-step) > C2. Lemma to launch: B.1, ℓ_{T′} ≥ ℓ_T on core_{T′}.

No sign. L′♯ OPEN.
