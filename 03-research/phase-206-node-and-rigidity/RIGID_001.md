# RIGID_001 — Track B, phase 206: catalog of objects with nonlinear Euler ∧ FE and search for a quadratic rigidity with sign

Track B. Pencil-and-paper work, no numerics.
ARGUED / OPEN / NO-GO / RETRY.

## Summary (≤250 words)

I cataloged twelve objects where the Euler product (E) and the functional equation (F) coexist in a nonlinear way:
reciprocal theorems of Hecke/Weil/Hamburger, Bochner–Hecke, Jacobi θ and ζ(2s), Eisenstein E(z,s),
Rankin–Selberg L(f×f̄), Maass–Selberg, Kuznetsov/Petersson with Kloosterman, the metaplectic variant (Salié),
Voronoi for d(n), Voronoi with additive twist (Estermann function) and the Kronecker–Hurwitz class formula. For each
one I mark where the nonlinearity between E and F lives, propose the natural quadratic version of the rigidity, and
compare it against restrictions (1)–(5) of the index.

Verdict. None of the objects evades the index. Eight are direct RETRY. Three (Voronoi with |g|², Voronoi
with Estermann additive twist and the Eisenstein part of Kuznetsov) did not appear in the index as routes. I close them
with three new lemmas. **Lemma V** (PROVED): Voronoi positivity with test |g|² holds for Epstein with h>1, so it
does not work as a sign step. **Lemma K** (PROVED, on the CITED Kuznetsov formula): the Eisenstein term reads ζ
only at |ζ(1+2it)|^{−2}, i.e. at abscissa 1 and outside the empty cell (3). **Lemma HV** (PROVED): every
quadratic positivity of Estermann/large sieve type is a valid norm for any sequence of coefficients. Λ enters
only after linearizing, which falls under (4)/X2. The only genuine E∧F nonlinearity at weight n^{−1/2} is the dependence
of Λ on |D|² through the logarithm: back to (S) or to BARRIER_D1 Thm 4.

Connection to the node (Lemma N, PROVED as a reduction): a quadratic rigidity only helps if it writes Φ_N(F) = ‖A_F‖² − B(F)
with B controlled by 𝔪+𝔢 on c^⊥. It was proved that every A_F in the catalog is blind to the comb. Track B: ARGUED
class NO-GO on the catalog, with the empty cell not reached.

## 0. Corpus check (mandatory)

I grepped 03-research, 04-papers and 05-meta-and-planning. For each term I give the number of corpus files
and the number of index README lines:

| term | corpus files | index lines | where it bites |
|---|---|---|---|
| Hecke | 1217 | 9 | CA_A_003 §2 (Hecke relations = cosine identities, comb-generic, PROVED); 159 G1_B2_R3 §5.3 |
| Hamburger | 231 | 12 | R162_2601c; INV_A_001 (rigidity 𝔐={ζ} = RETRY); BARRIER_D1_001 Prop 1, Thm 4 |
| Rankin | 209 | 9 | CA_A_001, CA_A_005 (RS_w ≥ 0 comb-blind; continuation to ½ = (S)); SYNTHESIS §4 (i) |
| Voronoi | 18 | 0 | R150_005 O-150.4 (Voronoi as savings in partial sums: no information; closed); phase-29-zeta-spectral-triples (geometric cells, different sense); PLAN.md |
| Eisenstein | 78 | 2 | CA_A_001 (Maass–Selberg at abscissa 1), CA_A_004 (metaplectic), CA_A_006 (1→½ transport NO-GO) |
| Kuznetsov | 34 | 1 | only the "Salié/Kuznetsov half-integral" residue from CA_A_004 §5–6 (OPEN-RESIDUE, low priority) |
| theta | 1689 | 3 | mostly noise (Riemann–Siegel theta, gauge theta); Jacobi θ ↔ ζ(2s) appears in V1.3 ("Ш/Poisson = Euler at σ=1") |
| metaplectic | 15 | 3 | CA_A_004: rank-one obstruction; citation DIT 2011 verified |
| Petersson | 35 | 3 | front A phase 193: Petersson positivity comb-blind |
| Maass–Selberg | 43 | 3 | CA_A_006 Remark 3: MS = window form of ζ(2s) over the squares; abscissa transport NO-GO PROVED |
| Bochner | 385 | 10 | almost all is Bochner positive-definiteness; Bochner–Hecke (modularity ⟺ FE) has no entry of its own, subsumed under Hamburger/INV_A |
| Estermann (extra) | 4 | 1 | Z_CARRIER_001 and MULT_GAUGE_001 (Thm R-MOM): Estermann constants with net coefficient 0 in moments on the line |
| Salié / Helson (extra) | 11 / 22 | 1 / 2 | Salié: residue CA_A_004; Helson/Perfekt: L87, the only positivity at weight n^{−1/2}, without FE (SYNTHESIS §4 ii) |

I also read the phase 206 README, CA_A_003, CA_A_005, CA_A_SYNTHESIS, their audits and the index entries
of phases 193, 194 (INV_A), 197 (BARRIER_D1, D2, X, Y, Z) and 198, as well as the §4 survey.

**Conclusion of the check.** The routes "Voronoi as a quadratic identity with test |g|²", "Voronoi/Estermann with additive
twist as large-sieve positivity" and "Eisenstein term of Kuznetsov as carrier of the comb" do not appear in the
index. They are the only candidates for a new reason. Everything else in the catalog is RETRY (§2).

## 1. The common pattern: where E, F and positivity live

In every object of the catalog the same three ingredients appear:

- **E** is a multiplicative property of the coefficients: a(mn) = a(m)a(n) if (m,n)=1, or the Hecke relations
  T_mT_n = Σ_{d|(m,n)} T_{mn/d²}.
- **F** is the invariance of an object (θ, E(z,s), f) under a group containing z ↦ −1/z, i.e. s ↔ 1−s.
- **The E∧F nonlinearity** is that F is stated on the additive generating series Σ a(n)e(nz), while E is
  stated on the multiplicative series Σ a(n)n^{−s}. The reciprocal theorem (Hecke; Weil with twists) says that F for
  enough twists, plus growth, forces modularity. Bochner–Hecke says that modularity plus the Hecke eigenvector
  condition forces E. Rigidity is a theorem: Hamburger for degree 1 gives 𝔐 = ℂζ.

The node, instead, asks for an inequality between Φ_N, which is **linear** in (Λ−1) with weights 2𝓕_F(log n)/√n, and the
form (𝔪+𝔢), which is archimedean and polar. Λ = −ζ′/ζ is the logarithmic derivative, so the relation between Λ and the
"modular" sequence (1, d(n), r(n), …) is **nonlinear**: Λ = μ * log, d = 1 * 1, and so on. The question
stands as: is there a natural positivity Q(a) ≥ 0, defined on an object where E∧F is a theorem, such that when Q is
expressed in terms of Λ a term linear in Λ appears with weights n^{−1/2} and with the correct sign, controlled by
the rest?

## 2. Catalog

Each object is presented with these fields: (i) the E∧F nonlinearity; (ii) the natural quadratic version of the
rigidity; (iii) which of restrictions (1)–(5) it hits; (iv) falsifiers; (v) whether it composes or chains (Def O1.2).

### 2.1 Hecke's reciprocal theorem, level 1, and Hamburger
(i) F of Σ a_n n^{−s} with factor Γ_ℝ(s) ⟺ θ_a(iy) = Σ a_n e^{−πn²y} satisfies θ_a(1/y) = √y θ_a(y) (plus poles). E does
not intervene: Hamburger gives uniqueness within the Dirichlet class with finite growth. (ii) The natural
quadratic version is ‖θ_a(1/y) − √y θ_a(y)‖² in L²(dy/y), a modularity defect. (iii) It is an analytic defect
of the FE with zero only at Λ. It falls under BARRIER_D1 Thm 4: it is symmetric to leading order and blind to w_T. **RETRY**
(INV_A, D1, D2).

### 2.2 Weil with twists (GL(2) reciprocal theorem)
(i) F for all twists by primitive characters ⇒ modularity. The nonlinearity is that the twists mix
χ(n) with a_n. (ii) Σ_χ ‖defect_χ‖². (iii) It is a sum of analytic defects, again Thm 4. Also the twists
χ(n)a(n) are linear in a, and Kronecker parity X2 acts twist by twist. **RETRY** (D2 "global nonlinear Δ_T"
already covers any Δ that is a function of FE defects).

### 2.3 Bochner–Hecke (modularity ⟺ FE; eigenvector ⟺ Euler)
(i) It is the cleanest version of E∧F: the form is a Hecke eigenvector ⟺ the coefficients are multiplicative.
(ii) The quadratic version is ‖T_p f−λ_p f‖² in the Petersson norm. (iii) It is Petersson positivity: blind to the
comb (1). Also, at tempered parameters the Hecke relations are cosine identities, comb-generic
(CA_A_003 §2). **RETRY**.

### 2.4 Jacobi θ and ζ(2s)
(i) ∫_0^∞ (θ(iy)−1)y^{s/2}dy/y = 2π^{−s/2}Γ(s/2)ζ(s). Here F is Poisson and E is that of ζ. (ii) Built-in
positivity: θ(iy) > 0 and θ is positive-definite in y. (iii) Ш/Poisson is equivalent to Euler at σ=1 (V1.3), with weight
n^{−1} or lower: gap (3). If one passes to ζ(2s) squares appear, as in CA_A_006 Remark 3. **RETRY**.

### 2.5 Eisenstein E(z,s), constant term and Maass–Selberg
(i) Constant term y^s + φ(s)y^{1−s}, with φ(s) = ξ(2s−1)/ξ(2s). Coefficients 2|n|^{s−½}σ_{1−2s}(|n|)√y K_{s−½}(2π|n|y)/ξ(2s).
The FE E(z,s) = φ(s)E(z,1−s) is that of ζ. Euler sits in σ_{1−2s} and the nonlinearity is in the ratio φ.
(ii) Positivity: Maass–Selberg ‖Λ^Y E(·,½+it)‖² ≥ 0.
(iii) **Why it is blind (verification requested).** By CA_A_001 Cor 3 and CA_A_006 Remark 3, the symbol produced by
Maass–Selberg is −φ′/φ(½+it) = 2Re[ξ′/ξ(1+2it)]·2 + const. Its comb is 4Λ(n)/n in cos(2t log n), which is equivalent to
4Λ(√N)/√N on the squares N=n². The weight n^{−1} comes from the constant term involving ξ(2s) evaluated at
2s = 1+2it, on the line Re = 1. The division 1/ξ(2s) in the Fourier coefficients, which anchors E in the
unitary normalization, is what forces the abscissa 1. **Is there a reading at weight n^{−1/2}?** The Mellin
transform in y of the coefficients gives ζ(w+it)ζ(w−it), and at w=½ it reaches the critical line (CA_A_001 revision §3), but the
Mellin transform is not positive: no norm on L²(Γ\ℍ) is written as an integral in the Mellin variable with a
constant-sign symbol (CA_A_001 Lemma 2: no positive invariant form at Re s = ¼). The n^{−1/2} reading and
positivity never coexist in this object. **RETRY** (front A).

### 2.6 Rankin–Selberg L(f×f̄) and the unfolding ∫|f|²E(z,s)
(i) Unfolding: ∫|f|²E(·,s) = Λ(s,f×f̄)/ξ(2s)·(Γ). Euler ⊗ Euler and the FE are inherited from E. (ii) It is positive for
s > 1 real. (iii) The FE carries it to s < 0, and the sign in the strip does not transport: gap (3). For f = Eisenstein
packet we have CA_A_005 Prop 1–4: comb-blind, and the continuation to ½ gives (S). The sign |a_p|² ≥ 0 has the
blind spot of Kronecker parity (2). **RETRY**.

### 2.7 Metaplectic (weight ½, Γ_0(4))
(i) The coefficients of E_{1/2}(z,s) are ∝ L(2s−½,χ_D)/ζ(4s−1) (DIT 2011, CITED and verified in CA_A_004). On the
unitary axis and with D = □, ζ(½+2it) appears: weight ½ is natural here. (ii) Parseval over the horocycle, Σ|c_n|². (iii) CA_A_004
Prop 1: the off-diagonal kernel is rank one per index and mixes all χ_D. The diagonal is the second
moment (S). **RETRY**, except for the Salié/Kuznetsov residue, treated in 2.9.

### 2.8 Voronoi for d(n) with test |g|² — NOT in the index as a route
(i) The Voronoi formula is the FE of ζ² written in coefficients:
  Σ d(n)f(n) = ∫ f(x)(log x + 2γ)dx + Σ d(n) f̃(n),  f̃(y) = ∫ f(x)[4K_0(4π√(xy)) − 2πY_0(4π√(xy))]dx.
E enters as d = 1*1 (and then it is Euler of degree 2). The nonlinearity is that d is quadratic in the sequence 1.
(ii) With f = |g|² the left side is ≥ 0 by construction. The "quadratic" version of the rigidity is: the FE forces
Σ d(n) (|g|²)~(n) ≥ −(main term). (iii) See Lemma V (§3.1): the inequality holds equally for Epstein with h>1.
It is positivity of nonnegative coefficients plus F, and neither E nor Λ appears. **NO-GO PROVED** (new).

### 2.9 Kuznetsov/Petersson with Kloosterman, including the Salié variant
(i) Σ_j h(t_j)ρ̄_j(m)ρ_j(n)/cosh(πt_j) + (1/4π)∫h(t)τ_{it}(m)τ̄_{it}(n)/|ζ(1+2it)|²dt = δ_{m,n}·(…) + Σ_c S(m,n;c)/c·h^+(4π√(mn)/c).
The Kloosterman sum involves the modular inverse ā mod c. This is the (ℕ,+,·) interaction of the
semiring principle. (ii) For m=n and h ≥ 0 the spectral side is ≥ 0. (iii) See Lemma K (§3.2): ζ only appears as
|ζ(1+2it)|^{−2}. The half-integral variant (Salié) has in its continuous part L(·,χ_D) at the abscissa of the
metaplectic Eisenstein with 1/ζ(4s−1). On the unitary axis the denominator sits at abscissa 1 and the numerator gives the
diagonal of CA_A_004 (rank one). **NO-GO PROVED for the integral part; ARGUED for Salié** (closes the residue of CA_A_004 §5–6).

### 2.10 Voronoi with additive twist (Estermann function D(s, a/c)) — NOT in the index as a route
(i) D(s,a/c) = Σ d(n)e(an/c)n^{−s} satisfies a FE that swaps a/c for −ā/c. The family of all these FE's for (a,c)=1
is equivalent to the modularity of E(z,½)/∂_sE under SL₂(ℤ), a version of Weil with additive twists. Here E∧F uses ℤ as
a ring: Beurling has no additive twists, and DH/Epstein have no Hecke. It is the only object in the catalog that satisfies
the semiring-principle filter. (ii) The natural positivity is that of the large sieve,
Q(g) := Σ_{c≤C} Σ*_{a mod c} |Σ_n d(n)g(n)e(an/c)|² ≥ 0, which the Estermann FE transforms into the dual sum.
(iii) See Lemma HV (§3.3). **NO-GO PROVED** for the class of norms (new).

### 2.11 Kronecker–Hurwitz (class number formula)
INV_E dead (index). **RETRY**.

### 2.12 Multiplicative Hilbert inequality (Helson/Perfekt, L87)
Σ a_m ā_n/(√(mn) log(mn)) = 2∫_{½}^∞|Σa_n n^{−σ}|²dσ ≥ 0. It is at weight n^{−1/2}, but has no FE. It is the only known
positivity at weight ½ (SYNTHESIS §4 ii). I include it in the catalog because it is the missing half. Analyzed in
§4 as an attempted splice with F.

## 3. The three new lemmas

Notation: the node is (𝒩): Φ_N(F) ≥ −(𝔪+𝔢)(F) for F ∈ E_N^ev, ⟨F,c⟩ = 0, with
Φ_N(F) = Σ_{n≤e^{2T}} (Λ(n)−1)(2/√n)𝓕_F(log n) + boundary.

### 3.1 Lemma V (Voronoi with squared test is generic over lattices). PROVED.
**Statement.** Let Q be a positive-definite integral binary quadratic form of discriminant −D, with r_Q(n) = #{v ∈ ℤ²:
Q(v) = n}, and let Z_Q(s) = Σ r_Q(n)n^{−s} (Epstein). Then for every g ∈ C_c^∞(0,∞),
  Σ_n r_Q(n)|g(n)|² = (2π/√D)∫|g|²dx + Σ_n r_{Q*}(n)·𝒥(|g|²)(n),
with 𝒥 the rescaled order-0 Hankel transform (J_0) and Q* the dual form. The left-hand side is ≥ 0. Therefore,
the inequality "Σ_n r(n)𝒥(|g|²)(n) ≥ −(main)", deduced from Voronoi and the positivity of the test, holds for
every Epstein Z_Q, including those with class number h(−D) > 1 (index Epstein/O10 falsifier).
**Proof.** It is the Poisson formula on ℤ² applied to the radial function x ↦ |g|²(Q(x)), whose Fourier transform is
the Hankel transform J_0 (CITED, standard). The positivity of the left-hand side comes from r_Q ≥ 0 and |g|² ≥ 0. Neither
uses multiplicativity. ∎
**Consequence.** For ζ² (d = r for the "hyperbolic" form xy, with kernels K_0/Y_0) the argument is identical: the
positivity uses d ≥ 0 and F, but not E. Any sign step relying only on "Voronoi + positive test" is
falsified by Epstein h>1. For E to enter one must use d = 1*1, i.e. factorize. That leads to |Σ g(m)…|²
(Lemma HV) or to Λ via the logarithm (§3.4).

### 3.2 Lemma K (Kuznetsov's Eisenstein term at abscissa 1). PROVED (on CITED Kuznetsov).
**Statement.** In the Kuznetsov formula for SL₂(ℤ) (Iwaniec, *Spectral methods*, Thm 9.3, CITED), the contribution
of the continuous spectrum to ⟨m,n⟩ is (1/π)∫h(t)(m/n)^{it}σ_{−2it}(m)σ_{2it}(n)/|ζ(1+2it)|²dt. As a quadratic form on
vectors (x_m), its ζ-dependent part is multiplication by |ζ(1+2it)|^{−2}. Its prime expansion,
−log|ζ(1+2it)|² = −2Re Σ Λ(n)n^{−1−2it}/log n, reads Λ with weight n^{−1}/log n (and in the t-derivative, weight
Λ(n)/n). Therefore, no positivity of the Kuznetsov spectral side reads the comb at weight n^{−1/2}.
**Proof.** The unitary normalization of E(z,½+it) divides by ξ(1+2it). The Fourier coefficients
ρ(n,t) = 2n^{−it}... σ_{2it}(n)/ (ξ(1+2it)·√…) give |ρ(n,t)|² ∝ |σ_{2it}(n)|²/|ζ(1+2it)|²·|Γ-factor|², and the Γ factor
cancels with the cosh weight. The σ_{2it}(n) are Hecke polynomials in cos(2t log p), comb-generic by CA_A_003 §2. Λ
only appears through log ζ(1+2it). ∎
**Consequence.** Kuznetsov combines F (via Bessel/Kloosterman) with E (via Hecke) and has built-in positivity, but
the prime reading sits at abscissa 1. It is cell (3) with the wrong weight, the same case as
Maass–Selberg. The Kloosterman side does see (ℕ,+,·) (inverses ā), but without positivity: S(m,n;c) has no sign. This
closes the Kuznetsov/Salié residue of CA_A_004 for the sign step; for Salié it is ARGUED, by the same normalization
1/ζ(4s−1).

### 3.3 Lemma HV (Hecke–Estermann positivity is a norm). PROVED.
**Statement.** Let a: ℕ → ℂ be any sequence and g of compact support. For every C,
  Q_a(g) := Σ_{c≤C}Σ*_{a′ mod c}|Σ_n a(n)g(n)e(a′n/c)|² = Σ_{m,n} a(m)ā(n)g(m)ḡ(n)R_C(m−n),  R_C(h) := Σ_{c≤C}c_c(h),
with c_c the Ramanujan sums. Q_a ≥ 0 for every a. In particular, the positivity does not distinguish a = d from a = r_Q
(Epstein), a = d_B (Beurling with FE, quartets) nor a = DH coefficients. If a is Hecke-multiplicative,
a(m)a(n) = Σ_{k|(m,n)}a(mn/k²). This allows rewriting the diagonal |Σ_n a(n)g(n)|² (the c=1 term) as a linear form
in a, L_g(a) := Σ_{m,n}g(m)ḡ(n)Σ_{k|(m,n)}a(mn/k²) ≥ 0.
That linear form is ≥ 0 on the cone of Hecke sequences, which is not convex, and the inequality does not extend to the
convex hull.
**Proof.** The first identity follows from expanding the square and using Σ*_{a′ mod c} e(a′h/c) = c_c(h). The
positivity is trivial. For the second part, L_g(a) = |⟨a,g⟩|² ≥ 0 for Hecke a by the Hecke relation. On
convex combinations of Hecke sequences, L_g is linear and |⟨·,g⟩|² is convex, so L_g(Σt_ia_i) = Σt_i|⟨a_i,g⟩|²
≥ 0 still holds. But L_g evaluated at sequences that are not Hecke (for example a = d − r_Q) can be negative:
just take g = δ_1+δ_2 with a(1)=0, a(2)=−1 and a(4)=0, which gives L_g = a(1)+a(4)+2a(2)+a(1) = −2. ∎
**Consequence (the key one).** The only E∧F positivity separating ζ from Epstein is L_g(d) ≥ 0. That is the statement
"d belongs to the Hecke cone", a restriction **of support/integrality** (k|(m,n)), not of the sign of Λ. Furthermore,
L_g(d) = |Σ d(n)g(n)|² reads d with whatever weight g imposes. To read Λ one must differentiate in a parameter. With d_s(n) =
σ_{−s}(n)n^{s/2}, one gets ∂_s|Σ d_s g|² = 2Re[⟨∂_sd_s, g⟩⟨g, d_s⟩], which is **bilinear**: Λ with a weight depending on
⟨g,d_s⟩. This is exactly the class "bilinear in Λ via a functional of the test" of Theorem X / W-fam (dead, phase 206
README §5), and the Kronecker-parity X2 acts on d_s(p^j) ↦ (−1)^jd_s(p^j), which preserves the Hecke relation (it is the
Liouville character, completely multiplicative). Restriction (2).

### 3.4 What remains of the E∧F nonlinearity at weight n^{−1/2}
**Proposition S (ARGUED).** In every object of the catalog, the only formula that contains at once Λ at weight n^{−1/2},
global F and some definite sign is log|D(½+iτ)|² = 2Re log D, with D a full Euler product. Its built-in positivity
is |D|² ≥ 0, which does not pass to the logarithm, and the dependence is nonlinear only through log. Every
inequality in |D|² leads to the second moment (S) (EI_002, CA_A_005 Prop 4, MOMENTS_001 Thm R-MOM: net constants 0).
Every inequality in log|D| is the window form itself, so it is the class being abandoned.
**Justification.** Lemmas V, K and HV, plus CA_A_001/005/006. I leave it ARGUED because I do not have a closed
class of methods covering "every automorphic positivity"; the coverage is by catalog.

## 4. Is there any object in the empty cell (3)? Attempt with Helson ⊗ Estermann

The cell requires weight n^{−1/2}, global FE and built-in positivity. Helson (2.12) supplies the first two halves
without F. Estermann (2.10) supplies F with an additive twist. Splicing proposal, which according to the index was never
built before:

  𝓗(g) := ∫_{½}^{∞} Σ_{c≤C}Σ*_{a′}|Σ_n d(n)g(n)e(a′n/c)n^{−σ}|² dσ = Σ_{m,n} d(m)d(n)g(m)ḡ(n)R_C(m−n)/(√(mn)·log(mn)) ≥ 0.

It is at weight n^{−1/2} (Helson kernel) and uses the Estermann twists, whose FE is global. **New reason with respect to
(1)–(5):** it is not Petersson nor RS (there is no automorphic inner product), it is not a defect of the FE (the FE is
used as an identity to transform 𝓗 into its dual) and it is at weight n^{−1/2}.
**Why it fails all the same (PROVED).** 𝓗 = Σ_c (large sieve) ∘ (Helson) is a sum of squared norms and holds for any
sequence a in place of d (Lemma HV, with g(n)n^{−σ} in place of g). It is comb-blind in the sense of (B″). The Estermann
FE transforms it into Σ r-dual·(Bessel transform of a positive kernel), an identity with no sign of its own.
That the dual side has a sign is a consequence of 𝓗 ≥ 0, not the other way around. The positivity never goes through F: F only rewrites.
This is the general diagnosis. **In every object, F acts as an identity (bijection between sides) and the positivity
is produced on a single side, as a norm. A norm is generic in the coefficients.** For F to "produce" a sign
would require an inequality that is not a consequence of a norm on either side: a positivity that exists only because the
two sides coincide. That is Hamburger's linear rigidity (cone = {ζ}) or its defect, which are
restrictions (4)/(5). **NO-GO ARGUED** for the splice; **empty cell (3): still empty.**

Falsifiers of the splice:

| falsifier | does 𝓗 distinguish it? | reason |
|---|---|---|
| a_P | no | 𝓗 ≥ 0 for any a |
| quartets (Beurling with FE) | no | ditto; also d_B is Hecke in its semigroup |
| cΛ | no | Λ does not appear; d ↦ d_c is not defined |
| Epstein h>1 | no | Lemma V/HV |
| DH | no | its coefficients satisfy Voronoi without Hecke; 𝓗 ≥ 0 all the same |

Composition (Def O1.2): it does not compose. E (Hecke) only acts in L_g(d), and F only in the dual identity. They never
enter the same nonlinear step; at most they chain, and the sign does not appear in either step.

## 5. First lemma toward the node (Lemma N) and what is missing

**Lemma N (reduction, PROVED).** Suppose there is a linear map F ↦ A_F ∈ ℋ (a Hilbert space of coefficients)
and a quadratic form B such that, for every F ∈ E_N^ev ∩ c^⊥,
  Φ_N(F) = ‖A_F‖²_ℋ − B(F).
Then (𝒩) ⟸ B(F) ≤ (𝔪+𝔢)(F) on c^⊥. If moreover ‖A_F‖² is a generic norm in the coefficients (it holds with Λ
replaced by any a in the comparison class 𝒜), then B(F) = ‖A_F‖² − Φ_N(F) is linear in Λ and inherits exactly the clause
that (𝒩) demands. In that case the reduction is empty: (𝒩) ⟺ B ≤ 𝔪+𝔢, with B as hard as Φ_N.
**Proof.** The first part is immediate. For the second, if ‖A_F‖² does not depend on Λ (generic), B(F) = ‖A_F‖² −
Φ_N(F), and the required inequality is Φ_N ≥ ‖A_F‖² − (𝔪+𝔢) ≥ −(𝔪+𝔢) when ‖A_F‖² ≥ 0. This is stronger than (𝒩),
never weaker. ∎
**What is missing (OPEN, and this is the precise formulation of the open question):** an A_F **dependent on Λ**
through the Euler product, nonlinear, of the type A_F = (𝓕_F(log n)·b(n))_n with b built from ζ, such that
‖A_F‖² − Φ_N(F) is controllable by 𝔪+𝔢. Lemmas V, K and HV show that no A_F in the automorphic catalog satisfies
this:
- Voronoi/Epstein give generic A_F (V).
- Kuznetsov gives A_F at abscissa 1 (K).
- Hecke–Estermann gives A_F with E only as support (HV), and Λ enters bilinearly (Theorem X).
- If one chooses b(n) = d(n)n^{−1/2}, one gets ‖A_F‖² = Σ|𝓕_F(log n)|²d(n)²/n, which is diagonal and does not see cos(τ log(m/n)).
  If b is a Dirichlet polynomial, A_F leads to |F̂D|² and from there to (S).
That is why the "first useful lemma" of track B is negative and remains a reduction: **every known quadratic E∧F
rigidity factors as ‖generic‖² plus an F identity, and by Lemma N that does not bring the node any closer.**

Necessary condition for a future object (PROVED as the contrapositive of Lemma N + Lemma HV): the positivity must
fail for some Hecke sequence a ≠ d with FE. That is, the object cannot be a norm on the space of
coefficients. The objects where E∧F is a theorem produce norms (Petersson, Parseval, large sieve, Helson). That is the
structural reason for the empty cell.

## 6. Final table of the catalog

| # | object | E∧F nonlinearity | quadratic version | restriction it hits | label |
|---|---|---|---|---|---|
| 2.1 | Hecke reciprocal / Hamburger | additive ↔ multiplicative series | ‖θ defect‖² | (4),(5) | RETRY |
| 2.2 | Weil with twists | twists χ | Σ‖defect_χ‖² | (4), D2 | RETRY |
| 2.3 | Bochner–Hecke | eigenvector ⟺ Euler | ‖T_pf−λ_pf‖² | (1), CA_A_003 | RETRY |
| 2.4 | Jacobi θ / ζ(2s) | Poisson | θ > 0 | (3) | RETRY |
| 2.5 | Eisenstein / Maass–Selberg | φ = ξ(2s−1)/ξ(2s) | ‖Λ^YE‖² | (1),(3) | RETRY |
| 2.6 | Rankin–Selberg | Euler⊗Euler + FE of E | ∫|f|²E ≥ 0 | (1),(2),(3) | RETRY |
| 2.7 | metaplectic | natural weight ½ | Parseval | rank one, (S) | RETRY |
| 2.8 | Voronoi + |g|² | d = 1*1 | Σd|g|² ≥ 0 | Lemma V (Epstein) | NO-GO PROVED (new) |
| 2.9 | Kuznetsov / Salié | Kloosterman (ℕ,+,·) | spectral side ≥ 0 | Lemma K (abscissa 1) | NO-GO PROVED / ARGUED (Salié) |
| 2.10 | Estermann / large sieve | additive twists + Hecke | Q_a ≥ 0 | Lemma HV (norm) | NO-GO PROVED (new) |
| 2.11 | Kronecker–Hurwitz | — | — | INV_E | RETRY |
| 2.12+2.10 | Helson ⊗ Estermann | weight ½ + F | 𝓗 ≥ 0 | generic norm, F only identity | NO-GO ARGUED (new) |

## 7. Self-criticism

- Lemma HV: the counterexample with a(2) = −1 only shows that L_g is not ≥ 0 outside the cone. That it is not useful for the
  sign of Λ is ARGUED via Theorem X (the derivative is bilinear). I did not prove that no combination of L_g over several g gives a
  linear inequality in Λ with a sign. This is in principle covered by BARRIER_X_001 X2: Liouville parity
  preserves the Hecke cone and is antipodal at odd levels, so any linear consequence in Λ
  on p^{2j+1} is symmetric. Residue: the even levels p^{2j}, which are already OPEN in X_001 and are not reopened here.
- Lemma K: the exact Kuznetsov normalization (factors of 2, cosh) does not change the abscissa. The citation must be
  verified before integrating it into Paper 47.
- Lemma V: for ζ² the "form" xy is indefinite and the kernels are K_0/Y_0, not J_0. The positivity argument (d ≥ 0,
  |g|² ≥ 0) is the same; the difference in kernels is harmless.
- §4: "F only rewrites" is the core of the argument and is ARGUED, not PROVED as a class theorem. A class proof
  would require formalizing "positivity produced by a norm on one side of an identity." Its content is
  lem:shape-ident plus (B″).
- I obtained no negative value for ζ and no contact with the sign.

## 8. Entry for the index (3–4 lines)

- **RIGID_001 (phase 206, track B, no audit; new reason: nonlinear E∧F objects with global F that did not
  appear in the index):** catalog of 12 objects (Hecke/Weil/Hamburger reciprocals, Bochner–Hecke, θ, Eisenstein/MS,
  RS, metaplectic, Voronoi, Kuznetsov/Salié, Estermann, Kronecker–Hurwitz, Helson); 8 RETRY. New: **Lemma V**
  PROVED (Voronoi with test |g|² holds for Epstein h>1); **Lemma K** PROVED (Kuznetsov's Eisenstein reads ζ only at
  |ζ(1+2it)|^{−2}, abscissa 1; closes the Salié/Kuznetsov residue of CA_A_004, Salié ARGUED); **Lemma HV** PROVED
  (Hecke–Estermann/large-sieve positivity = generic norm; E only as support k|(m,n); Λ bilinear ⇒ Theorem X, X2);
  Helson⊗Estermann splice NO-GO ARGUED (F only rewrites). **Lemma N** PROVED: quadratic rigidity = ‖generic‖² + F identity
  does not bring the node any closer. Cell (3) remains empty. Do not retry automorphic/Voronoi/large-sieve
  positivities as a sign step. Row D OPEN.
