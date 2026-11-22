# SKELETON_001 — Skeleton of the object that composes E and F (phase 205)

Four new elementary identities have a NUMERICAL quadrature
check (scratchpad, not part of the proof).

## Summary (≤300 words)

I build the skeleton from Corollary C of A∞, the only form of the sign left by phase 204. There are five pieces and a graph.

- **P1 (PROVED as necessity, not as ⟺).** I use the even Dirichlet basis E_N^ev. Even positivity requires
  n₋(𝔪_N + Π_N) ≤ 1. The Schur split by frequency E_N ⊕ E_N^⊥ is exact, but the block 𝔪_⊥ ≥ 0 is OPEN and not
  trivial, because the sines are not band-limited. Also, P1 "composes" only in the trivial sense: it is the target
  itself, compressed.
- **P2a (PROVED, new).** The entries of the comb matrix in the Dirichlet basis have a closed formula G_kl(u). They
  are not Toeplitz−Hankel of the sampled symbol (that reading is ARGUED-approximate).
- **P3 (PROVED, new). Pole Green identity.** The comb's main part (density 2e^{u/2}) gives, in the even sector,
  exactly **M(F) = ‖g‖²_{H¹_¼} − β_T⟨F,χ_ev⟩²** with g = −sinh(|·|/2)∗F and β_T = 1 + ½sinh T.
  That is, the pole contributes a positive energy plus a single negative direction, the polar one. The coefficients
  of χ_ev in the sines are all positive: c_k = 2ω_k cosh(T/2)/(√T(¼+ω_k²)).
- **P2b (core, OPEN = REF-D).** What remains is 𝔅_T = 𝔪 + E_G + Φ_E ≽ 0 (Φ_E = form of ψ(x) − x). Under H1PLUS's
  normalizations, 𝔅_T = Z_T + (β_T − 2)ℓ² (CONDITIONAL on the normalization). Hence the core is the zero form
  written in frequency coordinates, with a rank-one polar slack. **The "comb tail" of the condition is empty on
  P_T** (H1PLUS §4.2) and **the pointwise criterion m − σ_T ≥ 0 dies at τ = 0** (m(0) − σ_T(0) ≈ −4e^T).
- **P4.** All falsifiers in the identity come out explicit (residue, Lévy, E_P(x) of a_P).
- **P5.** Exact 3×3 formula for the calibrator at Mori μ=15. Prediction: n₋ = 1, δ_5 ≈ 0.075, χ with 91.2% in E_5^ev.

Verdict: the skeleton is constructible and honest. **It does not yet contain a composed sign step.** The only live
spot is lemma L205.★ (§7), with its statement and death criterion. P5 and P3 are built first.

---

## 0. Index, corpus, grid and crossword check (mandatory)

I ran grep on `05-meta-and-planning/ROUTES-TRIED-INDEX/README.md` (623 lines) for each piece:

| term | hits | relevant entries |
|---|---|---|
| Toeplitz | 8 | l.462 PROOF_L_SHARP_Q_001 (Toeplitz+Hankel of 𝔔 on the **exterior**, class 𝒦_{T+H} NO-GO; lists G8A-118/W3, G4C-R161, G8D-R164_502c, P45-1, G3D-159 "window compression with indefinite symbol"); l.398 INV_K_001 (window symbol m − 2Re[ζ·Q], gauge-invariant Toeplitz form) |
| Hankel | 9 | l.208 (Hankel mean, fails with an atom), l.462, l.534 COSH_DEFECT (Hankel in mn) |
| symbol | 27 | l.164/178 EI_003 (σ_T = 2Θ_X′; "rigidity" demoted to a tautology), l.527 Z_CARRIER (null symbol F4) |
| Haynsworth / Schur | 4 | l.536 SPEC_004 N3 (block inertia = D in block), l.595 L2_INTERLACE, l.601 P2_SCHUR, l.538 LEMMA_I3 |
| short intervals | 1 | l.42: sieves / short intervals / BV / BT closed (N_021 Thm 2, cor:void) |
| Green | 5 | l.391 INV_D_001: Lévy/Green function of the killed process (106_17, Beurling–Deny), **not** the kernel e^{\|x−y\|/2} of the pole |
| semiseparable, "e^{\|", 1/(¼+τ²), "Dirichlet sines," "partial sum" (as an object) | 0 | — |
| Müntz / polar mode | 3 | l.527 Z_CARRIER "after subtracting the polar mode (Müntz)" (multiplier side, not window) |

In phase 204: H1PLUS_001 §4 already contains the reading "m ≈ partial sum of the comb in low band = explicit formula
in frequency, error = Z_T." There it is NO-GO as an identity (PROVED) and as a class of methods that only use
bounds on E(x) (ARGUED). It also says "there is no tail to bound" (§4.2). COMPOSE_EF Theorem C2 (FE as a fingerprint
on the prime side ⇒ a_P common falsifier), AUDIT_204_CSTAR (E as identity ⇒ chains) and LEMMA_AINF_001 (Theorem A∞,
Corollary C) are the PROVED inputs.

**New and explicit reason, per piece**
- P2a and P3 are elementary identities that do not appear in the index (0 hits): the closed entries of the
  truncated translations in the Dirichlet basis and the Green decomposition of the polar kernel e^{|x−y|/2}. They do
  not reopen any route. They are tools.
- The Toeplitz−Hankel reading of the symbol (Piece 2) **is not used as a sign step**: it is the window compression
  with indefinite symbol (l.462, list G8A-118…G3D-159) and the explicit formula in frequency (H1PLUS §4). I record
  it as an identity and declare it REF-D in §4.
- The frequency-block Schur (P1) is new as a partition (by t₀, a Γ_ℝ datum, instead of by gauge, Euler, or
  k-blocks). I use it only as a reduction tool, not as a sign step, because l.536 (N3) already fixes that block
  inertia does not give a sign by itself.

---

## 1. Notation (verified against LEMMA_AINF_001 §2 and P46)

- I_T = (−T,T). For real F, c_F(u) = ∫F(x+u)F(x)dx, supported on [−2T,2T].
- 𝔪_T(F) = (1/2π)∫ m|F̂|² = C₀‖F‖² + Lev(c_F), where m(τ) = Re ψ(¼+iτ/2) − log π, C₀ = −5.37218…,
  K(u) = 2e^{3u/2}/(e^{2u}−1) and t₀ = 6.28984… (P46 lem:K, thm:S; LEMMA_AINF §2).
- Π_T(F) = −Σ_{n ≤ X} v_n Re c_F(log n), with v_n = 2Λ(n)/√n and X := e^{2T}. 𝔄 := 𝔪_T + Π_T is the prop:WT form
  (no pole). W^ev = 𝔄 + 2ℓ², with ℓ(F) := ⟨F,χ_ev⟩ and χ_ev = cosh(x/2)1_{I_T}.
- Even positivity ⟺ n₋(𝔄_ev) = 1 ∧ q_ev < −½ (prop:WT, WT_HALVES).
- Dirichlet basis: e_k(x) = T^{−½} sin(ω_k(x+T)), with ω_k = πk/(2T). Odd k gives even functions (I3 of A∞).
  E_N^ev = span{e_k : k ≤ N, k odd}, N = N(T) = ⌈2Tt₀/π⌉ − 1.
- Zero formula (H1PLUS (1.4), PROVED): 𝔄_ev = Z_T − 2ℓ², Z_T = W^ev_T = Σ_ρ Φ_F(ρ)².
- E(t) := ψ(t) − t.

---

## 2. Piece 1 — Reduction to E_N^ev and archimedean-frequency Schur

### 2.1 What is necessity (PROVED)
**P1.a (Corollary C, PROVED, LEMMA_AINF §5).** Let Π_N^ev be the compression of Π_T to E_N^ev. Then
n₋(𝔄_ev) ≥ #{j : μ_j(Π_N^ev) < δ_N}, with δ_N = B(t₀² − ω_N²) − m(t₀) > 0 (and m(t₀) = 0).
Hence n₋(𝔄_ev) = 1 requires n₊(Π_N^ev ≥ δ_N) ≥ ⌈N/2⌉ − 1.

**P1.b (PROVED, min–max).** Let 𝔄_N^ev be the compression of 𝔄_ev to E_N^ev. Then n₋(𝔄_N^ev) ≤ n₋(𝔄_ev).
So even positivity implies n₋(𝔄_N^ev) ≤ 1. That is **only necessity**: E_N^ev ≠ L²_ev(I_T).

### 2.2 The exact Schur and what is missing for ⟺
Let L²_ev = E_N^ev ⊕ (E_N^ev)^⊥, with (E_N^ev)^⊥ = cl span{e_k : k > N odd}. In blocks,
𝔄_ev = [[𝔪_N + Π_N, X], [Xᵀ, 𝔪_⊥ + Π_⊥]]. Haynsworth (CITED, standard for closed forms with a coercive lower block)
gives that, if 𝔄_⊥ := 𝔪_⊥ + Π_⊥ ≻ 0,

  n₋(𝔄_ev) = n₋(𝔄_N − X 𝔄_⊥⁻¹ Xᵀ).   (2.1)

**P1.c (OPEN, with an exact statement).** 𝔄_⊥ ≻ 0 on (E_N^ev)^⊥.
Correction to the formulation: it is **not** true that 𝔪_⊥ ≥ 0 by construction. Dirichlet sines are not
band-limited. ê_{N+2} has tails O(1/τ²) and mass O(1/N) in |τ| < t₀, so the bound 𝔪 ≥ 0 does not follow from
‖F′‖² ≥ ω_{N+1}²‖F‖². A lower bound on m by a parabola would be needed, and m grows like log while the parabola
grows like τ². That is exactly the "upper bound of A∞" that LEMMA_AINF Obs. 4 left OPEN (there: n₋(𝔪_T) = N(T)
exact at five T, NUMERICAL). Also Π_⊥ has indefinite sign.
*Death criterion of P1.c:* that the Galerkin version of 𝔄_ev restricted to (E_N^ev)^⊥ gives n₋ ≥ 1 at some
certified T.
In that case (2.1) fails and the reduction to a finite matrix stops being ⟺ (P1.b still holds).
If P1.c holds, (2.1) reduces even positivity to the inertia of a finite matrix **plus** the Schur term X𝔄_⊥⁻¹Xᵀ,
which is not explicit.

### 2.3 Is P1 a composition (Def O1.2)?
Yes, but only in the trivial sense, and I say so explicitly. Read as a sign step, the inequality
"Π_N^ev dominates −𝔪_N^ev except for one direction" uses F (via t₀, δ_N, m, Γ_ℝ conductor 1) and E (via exact Λ)
**in the same inequality**. The abstract falsifier (change the comb and keep t₀) exists: a_P and Epstein. In them
the inequality fails because Π_N changes. But this holds for any reformulation of the target. P1 **is** the
compressed target, and by O1.A(c)/O1.B every formulation of the target "uses" E∧F. Def O1.2 asks for more: a
**proof** whose margin step uses both channels. P1 does not supply that step; it only says where it has to occur
(in E_N^ev, with margin δ_N). Label: **P1 = PROVED localization tool, not a sign step.**

---

## 3. Piece 2a — Closed entries of the comb matrix (PROVED, new)

For 0 ≤ u ≤ 2T let G_kl(u) := ⟨τ_u e_l, e_k⟩ = T^{−1}∫_{−T}^{T−u} sin(ω_k(x+T)) sin(ω_l(x+u+T)) dx. With the change
y = x + T, the product-to-sum identity, and using 2T(ω_k ∓ ω_l) = π(k ∓ l), s := (−1)^{k+l}:

  **G_kl(u) = (1/2T)·[ (sin ω_l u − s·sin ω_k u)/(ω_k − ω_l) + (sin ω_l u + s·sin ω_k u)/(ω_k + ω_l) ]**   (k ≠ l)
  **G_kk(u) = (1/2T)·[ (2T − u)cos ω_k u + sin(ω_k u)/ω_k ]**.

*Proof.* It is an elementary integral. The upper boundary terms simplify by
sin(π(k∓l) − ω_k u) = −(−1)^{k∓l} sin ω_k u. ∎ (NUMERICAL: quadrature, T = ½log15, (k,l,u) = (1,3,0.7) and
(1,1,0.7), agreement to 1e−7.) In the even sector k, l are odd, so s = +1.

Matrices:
  Π_N^ev(k,l) = −Σ_{2≤n≤X} v_n·G^s_kl(log n),  G^s := ½(G_kl + G_lk);
  𝔪_N^ev(k,l) = (C₀ + κ_T)δ_kl + ∫_0^{2T}(δ_kl − G^s_kl(u))K(u)du,  κ_T = ∫_{2T}^∞K.

The entries are elementary in log n and T, with weights Λ(n)/√n. This form of the matrix is new (0 hits).

**On the formulation's Toeplitz−Hankel reading (ARGUED-approximate, not exact).** One has
Π_N(k,l) = −(1/2π)∫σ_T(τ)ê_k(τ)\overline{ê_l(τ)}dτ, with σ_T(τ) = Σ_{n≤X}v_n cos(τ log n). That this is
T(σ_T) − H(σ_T) sampled at ω_k would be exact only if the sines were exponentials on a torus. In the window, ê_k is
a sinc-type kernel centered at ±ω_k, and the factor (2T − u) and the denominators 1/(ω_k ∓ ω_l) in G are exactly the
correction. I use the exact formula and discard the sampling. As a sign object, the symbol reading is the window
compression with indefinite symbol (index l.462) and is not retried.

---

## 4. Piece 2: the "tail" and the pointwise criterion (verdict)

**4.1 The tail is empty (PROVED; already in H1PLUS §4.2).** For F ∈ P_T, c_F(log n) = 0 if n > X. Then
𝔄(F) = (1/2π)∫(m − σ_T)|F̂|² and the "tail Σ_{n>X}" does not appear in the form. The formulation's identity
"m − σ_T = comb tail" only makes sense after completing σ_T to the full series. That series does not converge on
the line and its regularization as a distribution is the explicit formula: m − σ_∞ = (zero measure) − (pole). Hence,
on P_T, **the form of m − σ_T is Z_T − 2ℓ²**, which is H1PLUS (1.4). The Toeplitz−Hankel matrix of m − σ_T on
E_N^ev is the compression of the zero form: it is REF-D in frequency coordinates. What is new is only the
coordinate (P2a), not the content.

**4.2 The pointwise criterion dies (PROVED, elementary).** A Toeplitz with symbol ≥ 0 is ≽ 0, so the question posed
is whether m − σ_T ≥ 0 on |τ| < t₀. At τ = 0: σ_T(0) = 2Σ_{n≤X}Λ(n)/√n = 4X^{½}(1 + o(1)) = 4e^T(1 + o(1)) (by
partial summation with ψ(x) ~ x, CITED PNT; the lower bound ≫ e^T is elementary by Chebyshev). Then m(0) − σ_T(0) =
C₀ − 4e^T(1 + o(1)) < 0. The deficit is concentrated at |τ| ≲ 1/T: it is the polar direction (§5). So the pointwise
version is false in the low-frequency window, and its "except for the pole" version is what §5 constructs.

---

## 5. Piece 3 — Pole Green identity (PROVED, new)

### 5.1 The comb's main part
By partial summation over (1, X], with dψ = dt + dE:

  Π_T(F) = M(F) + Φ_E(F),
  M(F) := −∫_1^X 2t^{−½} Re c_F(log t) dt = −∫_{−2T}^{2T} e^{|u|/2} c_F(u) du = −∫∫ F(x)F(y) e^{|x−y|/2} dx dy,
  Φ_E(F) := −∫_{(1,X]} 2t^{−½} Re c_F(log t) dE(t).

(Exact. Using c_F(−u) = c_F(u) for real F, Λ(1) = 0, and that c_F(2T) = 0 eliminates the upper boundary.)

### 5.2 The kernel e^{|s|/2} is a Green function plus rank 2
With s = x − y, e^{|s|/2} = cosh(s/2) + sinh(|s|/2), and:
- cosh((x−y)/2) = cosh(x/2)cosh(y/2) − sinh(x/2)sinh(y/2) has rank 2 and signature (1,1) on span{e^{±x/2}};
- (∂² − ¼)sinh(|s|/2) = δ (the derivative jump is 1). Then g := G F, with G the operator of kernel
  −sinh(|x−y|/2), satisfies −g″ + ¼g = F on I_T.

Integrating by parts, ⟨F, G F⟩ = ∫_{I_T}(g′² + ¼g²) − [g g′]_{−T}^{T}. In the even sector, g is even, g′ is odd, and
g(T) = −sinh(T/2)ℓ(F), g′(T) = −½cosh(T/2)ℓ(F). Hence [gg′] = 2g(T)g′(T) = ½sinh T·ℓ(F)².

**Theorem P3 (PROVED).** For F ∈ L²_ev(I_T):

  **M(F) = E_G(F) − β_T ℓ(F)²,  E_G(F) := ∫_{−T}^{T}(g′² + ¼g²) ≥ 0,  g = −sinh(|·|/2) ∗ F,  β_T := 1 + ½ sinh T.**

(NUMERICAL: T = ½log15 with random even F, −17.022383 against −17.022385, quadrature error.)

**Reading.** The comb's main part (the one coming from the residue 1 at s = 1, density 2e^{u/2}) is exactly a
positive H¹ energy of a Green potential, whose formal symbol is 1/(¼+τ²), **minus a single negative direction,
χ_ev, with weight β_T ~ e^T/4**. This turns the phrase "except for one (the polar one)" into an identity. It is the
exact, windowed version of the first half of H1PLUS §4.1 (there only as an order of magnitude).

In the odd sector the same computation gives M = E_G − β′_T⟨F, sinh(x/2)⟩² with β′_T = ½sinh T − 1. The sign of
the cosh term flips, contributing −⟨F,ch⟩² + ⟨F,sh⟩², as does the boundary. I leave this as
PROVED-by-the-same-computation, to be written up in P3-odd.

### 5.3 χ_ev in the Dirichlet basis (PROVED)
For odd k, ⟨χ_ev, e_k⟩ = c_k := 2ω_k cosh(T/2)/(√T(¼ + ω_k²)) > 0. (Using sin(ω_k(x+T)) = (−1)^{(k−1)/2}cos ω_k x
and cos(ω_k T) = 0.) Also ‖χ_ev‖² = T + sinh T. The fraction of χ_ev in E_N^ev is Σ_{k≤N odd}c_k²/(T + sinh T).
Asymptotically it is 1 − O(1/π²) (the tail Σ_{k>N}1/ω_k² ≈ 2T²/(π²N)). At T = ½log15, N = 5 gives **0.9124**
(NUMERICAL). The polar direction lives almost entirely, but not entirely, in E_N^ev. The correction is what enters
the Schur term X of (2.1).

### 5.4 Structural consequence (PROVED given P3)
𝔄_ev = 𝔅_T − β_T ℓ², with **𝔅_T := 𝔪_T + E_G + Φ_E**. By rank-one interlacing (as in H1PLUS (2.1)):
n₋(𝔅_T) ≤ n₋(𝔄_ev) ≤ n₋(𝔅_T) + 1. In particular, **𝔅_T ≽ 0 on L²_ev ⟹ n₋(𝔄_ev) ≤ 1** (the H1⁺ half of prop:WT).
The other half, q_ev < −½, is not given by 𝔅.

---

## 6. Piece 2b — The core: 𝔅_T and why it is REF-D as it stands

**Translation identity (CONDITIONAL on χ_ev's normalization and the "2" of H1PLUS (1.4) matching those of §1).**
Subtracting H1PLUS (1.4) from §5.4:

  **𝔅_T = Z_T + (β_T − 2)ℓ² = Z_T + (½ sinh T − 1)ℓ².**   (6.1)

So 𝔅_T ≽ 0 is "the zero form, plus a rank-one slack in the polar direction." The slack is positive if
sinh T > 2 (T > 1.4436) and grows like e^T/4. As the weight β_T → ∞, 𝔅_T ≽ 0 tends to Z_T|_{ker ℓ} ≽ 0, which is
𝔄_ev|_{ker ℓ} ≽ 0: the H1⁺ target again. **Verdict: the core of P2 is REF-D in frequency coordinates, with the
polar slack explicit.** It is not an object with its own sign step. (At Mori T = 1.354 the slack is −0.095ℓ²,
negative: in that window 𝔅 is not even weaker than Z_T.)

**What the skeleton adds even though it is REF-D:** it splits the comb into three parts with different statuses:
(i) the polar mass, rank 1, weight β_T, PROVED and explicit;
(ii) a Green energy ≥ 0, PROVED, which is **free help** because its symbol 1/(¼+τ²) is positive exactly on
   |τ| < t₀, where m < 0;
(iii) Φ_E, the only term where the primes beyond the density live.
On (ii): is the help enough? At τ = 0, m(0) + 1/(¼) = C₀ + 4 = −1.37 < 0. So 𝔪 + E_G still has negative
directions. Its count is OPEN: it is the zero t₀′ of m(τ) + 1/(¼+τ²), estimated as NUMERICAL-pending in the
range 2–6. **Φ_E has to cover ⌈2Tt₀′/π⌉/2 directions with margin.** H1PLUS §4.2 already closed (ARGUED as a class)
every proof that bounds Φ_E only by the size of E(x): Chebyshev and dlVP give the wrong size by a factor of e^{T}
or e^{T−c√T}.

---

## 7. The live lemma L205.★ (OPEN), with an exact statement and death criterion

**L205.★ (OPEN).** There exists T₁ such that for every T ≥ T₁ and every F ∈ E_N^ev ∩ ker ℓ,

  𝔪_T(F) + E_G(F) + Φ_E(F) ≥ 0,

and the proof has a margin step that uses at once:
(E) the identity Λ = μ ∗ log, or the Euler factorization, applied **inside** Φ_E. It must not be a bound on
|E(x)|: that is dead by H1PLUS §4.2. It must be nonlinear in Λ, for example via
Φ_E = −∫2t^{−½}Re c_F(log t)d(μ∗log − 1)(t), with the semiring structure at m ≈ kn from project-semiring-principle;
(F) the explicit form of m and of E_G, i.e. Γ_ℝ of conductor 1 and residue 1, **in the same inequality**, not as a
prior identity.

**Death criteria for L205.★:**
- (K1) If the sign step only uses size bounds on E(x) or its transform → dead (H1PLUS §4.2, ARGUED as a class).
- (K2) If the step rewrites as "Z_T ≽ −(β−2)ℓ²" with zero information → REF-D (6.1).
- (K3) If the step is linear in Λ, i.e. an affine bound in the weights (wall W-lin of the index) → dead.
- (K4) If the step uses the FE only as symmetry or a fingerprint of the form (Lemma C1), a_P is a common falsifier
  (Theorem C2) → dead.
- (K5) If some falsifier from §8 satisfies **all** the step's premises → dead by lem:transfer.
- (K6) If there is a certified window T with n₋(𝔅_T|E_N^ev ∩ ker ℓ) ≥ 1 in ζ → the statement is false as it
  stands (computation in §9).

**Honest status: I have no candidate for the step L205.★ asks for.** The skeleton isolates where it has to be.
That place is Φ_E, the form of ψ(t) − t on (1, e^{2T}] in translated Dirichlet sines, and the step has to compare
it with 𝔪 + E_G, which is explicit and comes from F, in a way that is nonlinear in Λ. The three registered modes
for Λ to enter nonlinearly (h*, tests with ζ coefficients, inversion via Möbius → 1/ζ) are in the index (EI_003
l.164; FINAL_204). Any proposal for L205.★ has to state in writing why it is none of those three.

---

## 8. Piece 4 — Falsifiers in the identity (PROVED except where noted)

All are read off the decomposition 𝔄_ev^a = 𝔪^a + r_a(E_G − β_T ℓ²) + Φ^a. Here r_a is the residue at s = 1 and
Φ^a is the form of the fluctuation Σ a_n − r_a t.

| model | 𝔪 (F) | polar part (E) | Φ (E) | where it breaks |
|---|---|---|---|---|
| ζ | m, t₀ = 6.29 | r = 1: E_G − β_Tℓ² | E = ψ − t | (target) |
| Epstein x²+5y² (Lemma E) | m^Q: C₀^Q = −4.607, Lévy 1/sinh(u/2), Γ_ℝ(s)Γ_ℝ(s+1), conductor 20 | r_Q ≠ 1 (residue of Z_Q) | E_Q = ψ_Q − r_Q t with Λ_Q < 0 at n = 36, 54, 84… | 𝔪^Q and Φ^Q change at once. The hyperbolic pair (H1PLUS) appears as a negative direction of 𝔅^Q outside ker ℓ. Frequency: OPEN, to the calibrator |
| DH | degree 1, conductor 5 | r = 0: **no polar term**, M ≡ 0, β ≡ 0 | Φ = the whole series, b_n with sign | no exceptional direction; n₋(𝔄^DH_ev) = 0 or hyperbolic pair. Consistent with H1PLUS (DH: 0) |
| a_P | m (unchanged) | r = Π_{p∈P}(1−1/p), polar weight changes | E_P(t) = E(t) − Σ_{p∈P}log p·⌊log t/log p⌋ + (1−r)t | **explicit matrix**: Φ^{a_P} − Φ^ζ = Σ_{p∈P,k: p^k≤X} 2log p·p^{−k/2}G^s(k log p), plus the polar change. Breaks n₋ ≤ 1 on T ∈ [0.60, ½log P] (P46). Calibratable with P2a |
| cΛ | m | r = c: c(E_G − β_Tℓ²) | E_c = c·E | c > 1: more polar mass and more Green. c < 1: less. That it fails for c ≠ 1 is read off the margin of 𝔪 + cE_G + cΦ_E (ARGUED, as in l.462) |
| Beurling | no Γ_ℝ: **no m, t₀, δ_N or E_N** | r depends on the system | E_B | the skeleton is undefined. P1 has no Dirichlet space: F absent |
| quartets | m (FE preserved) | — | arithmetic side with an a.c. part | not a series over ℕ: G^s(log n) is integrated against a continuous measure. E absent |

**Reading for Def O1.2.** In the identity, E lives in r_a and Φ^a, and F lives in 𝔪^a, t₀, δ_N and E_G (the form
−∂² + ¼ is that of Γ_ℝ with conductor 1 via e^{u/2}, together with the residue). Each falsifier violates at least
one, and none violates only "one fixed intermediate object." This is necessary to compose, but **not sufficient**:
Def O1.2 is decided at the L205.★ step, which does not exist yet.

---

## 9. Piece 5 — Mori μ = 15 test

T = ½log15 = 1.354025…, X = 15, N(T) = 5, even sector k ∈ {1,3,5}, ω_k = πk/(2T) ∈ {1.1601, 3.4803, 5.8004}.
- Comb: n ∈ {2,3,4,5,7,8,9,11,13} (n = 15 contributes nothing: Λ(15) = 0 and also c_F(2T) = 0), v_n = 2Λ(n)/√n,
  Π(k,l) = −Σ v_n G^s_kl(log n), with G from §3.
- Archimedean: 𝔪(k,l) = (C₀ + κ_T)δ_kl + ∫_0^{2T}(δ_kl − G^s_kl(u))K(u)du, κ_T = ∫_{2T}^∞K(u)du.
- Polar and Green: β_T = 1 + ½sinh T = 1.90474. c = (c_1, c_3, c_5) from §5.3. E_G(k,l) via the formula of §5.2, or
  directly M(k,l) = −∫∫e_k e_l e^{|x−y|/2}.

**Predictions to verify (to be certified with interval arithmetic):**
1. n₋(𝔪_3^ev) = 3 with λ_max ≤ −δ_5, δ_5 = B(t₀² − ω_5²) ≈ 0.01267·(39.56 − 33.64) ≈ 0.075 (PROVED-bound; the
   value is NUMERICAL).
2. n₋(𝔄_3^ev) = 1 (by P1.b it is ≤ 1; it is = 1 if the Rayleigh vector of c, which carries 91.2% of χ, is negative).
3. The three matrices 𝔪_3, 𝔪_3 + E_G, Φ_E, their inertias, and the negative eigenvector of 𝔄_3 against c/|c|.
4. The same table for a_P with P = {2} and for Epstein (n₋ = 2 expected at T = 2, N^ev = 4).
5. n₋(𝔅_3|ker ℓ) (criterion K6).

---

## 10. Dependency graph, labels and order

```
 thm:S (m Bernstein, concave) ──► A∞ (PROVED) ──► P1.a CorC (PROVED) ──► P1.b (PROVED, necessity)
                                                      │
                     P1.c (OPEN: 𝔄_⊥ ≻ 0; = upper bound of A∞) ──► (2.1) Schur ⟺ (CONDITIONAL on P1.c)
 P2a closed G_kl (PROVED) ──────────────────────────► explicit matrices ──► P5 calibration (NUMERICAL, pending)
 partial summation ψ = t + E (PROVED) ──► P3 Green: M = E_G − β_Tℓ² (PROVED) ──► §5.4 n₋(𝔅) ≤ n₋(𝔄_ev) ≤ n₋(𝔅)+1
 §5.3 coefficients c_k (PROVED) ─────────────────────────────────────────────┘
 H1PLUS (1.4) (PROVED) + normalization (CONDITIONAL) ──► (6.1) 𝔅 = Z_T + (β−2)ℓ²  ⇒ P2b = REF-D
 P4 falsifiers in the identity (PROVED; Epstein frequency OPEN)
 L205.★ (OPEN; K1–K6) ◄── the only node that would contain the composed sign step
```

| piece | label |
|---|---|
| P1.a, P1.b | PROVED (necessity) |
| P1.c | OPEN (death criterion: Galerkin n₋ ≥ 1 in the complement) |
| (2.1) ⟺ | CONDITIONAL on P1.c |
| P2a (G_kl) | PROVED |
| sampled Toeplitz−Hankel | ARGUED-approximate; as a sign object, already in the index (l.462) |
| formulation's "tail" | empty on P_T (PROVED, H1PLUS §4.2) |
| pointwise criterion m − σ_T ≥ 0 | NO-GO (PROVED, τ = 0) |
| P3 (pole Green), §5.3 | PROVED (plus NUMERICAL check) |
| (6.1) | CONDITIONAL on the normalization |
| P2b (𝔅_T ≽ 0) | REF-D (not a sign step) |
| P4 | PROVED in the identity; the Epstein pair's frequency is OPEN |
| P5 | pending (calibrator) |
| L205.★ | OPEN, no candidate |

**Global death criterion of the skeleton.** The skeleton dies as an "object that composes E and F" if (a) or (b) holds:
(a) every formulation of L205.★ that survives K1, K3 and K4 reduces by (6.1) to K2;
(b) P5 gives n₋(𝔅_3|ker ℓ) ≥ 1 in ζ (K6), and the version restricted to ker ℓ with slack cannot be repaired.
In that case the skeleton remains a **PROVED tool** (P2a, P3, §5.3, the P4 table) for any future object.

**Construction order.**
1. **P5 first** (calibrator): it is cheap and explicit, and decides K6. It also fixes the normalization of (6.1),
   comparing 𝔄_3 computed via P2a with Z_T − 2ℓ² from H1PLUS.
2. **P3 and P3-odd**, for integration into P46 after prop:WT. It is the "except for one" turned into an identity,
   with text for the editor.
3. **P1.c** (upper bound of A∞): without it, the reduction to a finite matrix is only necessity.
4. **L205.★**, only with a proposal that passes K1–K5 in writing and that states how it differs from h*, from tests
   with ζ coefficients, and from inversion via Möbius.

---

## 11. Entries for the index (ROUTES-TRIED-INDEX), for the editor

- **SKELETON_001 (phase 205).** New PROVED tools:
  (P2a) closed entries G_kl(u) of the truncated translations in Dirichlet sines;
  (P3) pole Green identity, M = E_G − (1 + ½sinh T)ℓ² in the even sector (kernel e^{|x−y|/2} = rank 2 + Green
  function of −∂² + ¼);
  (§5.3) c_k = 2ω_k cosh(T/2)/(√T(¼+ω_k²)), with 91.2% of χ in E_5^ev at Mori.
  NO-GO: the "comb tail in the window" is empty, and pointwise m − σ_T ≥ 0 is false at τ = 0 (−4e^T).
  REF-D: 𝔅_T ≽ 0 is Z_T + (½sinh T − 1)ℓ² ≽ 0 (CONDITIONAL on the normalization).
  OPEN: P1.c (= upper bound of A∞) and L205.★ with K1–K6. There is no composed sign step yet.
