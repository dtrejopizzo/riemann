# R11_2_ORIGIN_001 — R11.2: coupling "lattice origin / polar term" × multiplicativity in the window form

Phase 200, round 13.
Pure mathematics; no new numerics (only already-PROVED certificates from the corpus are cited).

## Summary (≤250 words)

The anatomy of the polar term is made exact. (1) **Lemma O1 (PROVED):** for g = F∗F̃, the pole's contribution in the
explicit formula is ĝ(i/2)+ĝ(−i/2) = 2Re(AB̄), A = ∫F e^{t/2}, B = ∫F e^{−t/2}; it depends on the **order** of the pole of −L′/L,
not on the **residue**. Hence the premise "the residue of L_P is Π(1−1/p) ≠ 1, incompatible with ζ's polar term" is false
at the level of the form: a_P has a simple pole and ψ_{a_P}(X) ~ X (the finite deletion does not change the density). (2) **Lemma O2
(PROVED, Poisson):** the form of the falsifier a_P is exactly W_ζ + Σ_{p<P} L_p, with L_p(g) = Σ_j Ĝ_p(2πj/log p) −
(log p)g(0), Ĝ_p = ĝ ∗ (Cauchy kernel of width ½) ≥ 0: the deletion is "smoothed lattice sampling minus mass",
not a change of the polar term. (3) **Theorem O3 (NO-GO PROVED, given P47 prop:shape-eulerdel and Lemma E):** the two
relevant falsifiers (a_P for T∈[0.60, ½log P]; Epstein x²+5y² for T ≥ 1.59) fail **in P_T**, where A = B = 0.
The polar term — and with it the lattice origin / Tate mode / residue — is identically zero on the witnesses;
no polar×multiplicativity coupling can be what fails. The only place where the pole couples to the comb is
the 2×2 polar capacity 𝔊_T (P47 thm:parityschur), which comes after λ_A. (4) The Selberg identity (order 2,
elementary) is C-data and comb-generic (satisfied by a_P, Epstein, Beurling-DMV): NO-GO, duplicate of AUDIT_B 7.7 / TB-3.
New restriction **C-pol**. R11.2 is closed; next lemma: none in this channel.

## 0. Index and corpus check

grep in `05-meta-and-planning/ROUTES-TRIED-INDEX/` and in `03-research/phase-200-sign-object/` for «polar»,
«residue», «Tate mode», «origin», «constant term», «theta», «Poisson», «a_P», «deleted primes», «C-Guo», «GUO_QUANT»,
«PI4», «Selberg», «Chebyshev», «C-data», «C-hom»:

| Record | What it closes | Relation to R11.2 |
|---|---|---|
| GUO_QUANT_001 §2(i),(iii) (README l.529) | κ = [pole]+[L(0)≠0]: Epstein has κ=2 ⇒ the pole does not separate (C-Guo); "Tate's theorem": Lemma 2.1 makes the Tate part positive ∀ divisor in the band ⇒ NO-GO | R11.2 asks about the coupling, not about the pole alone. New reason: it measures where the witnesses live (P_T vs. complement). |
| PI4_JUMPS_001 (README l.526) | Tate mode −½f♯(0)e^{−y/2} in the exact tail | It is the same Poisson constant term seen in the tail; here it is shown that over P_T its weight in the form is 0. |
| SPEC_SIGN_OBJECT_005 §4.3, Lemma H, R11.2 open (l.329) | a_P loses the constant term of ϑ (Σ_{d|P}μ(d)=0); C-hom | This memo answers the open question l.329–331. |
| LEMMA_I3_001 l.106 | arch|_𝒢 = (3,0,6), (arch+2AB)|_𝒢 = (2,0,7) | Used in §1.3: the polar term shifts a sign in the gauge, but not in P_T. |
| R11_1_CUTS_001 §7 | C-data | Applies to the Selberg identity (§4). |
| AUDIT_B l.60, l.96 ("Selberg identity is blind", Beurling DMV); 06_OPEN_RESIDUES R7 (TB-3: "generalized Selberg holds ∀b, Λ∗Λ ≥ 0 trivial") | Selberg identity | §4 is a duplicate: not retried as a route; only recorded that the "order-2 residue-comb relation" variant falls the same way. |
| INV_V_002, GUO_QUANT §2 | cΛ: 𝒲_c = (1−c)·arch | §2.3. |
| P47 prop:shape-eulerdel (l.8455–8465) | a_P fails WP_T ∀T∈[0.60,½log P]; breaks only the FE | Key fact of §3. |
| LEMMA_E_EPSTEIN_001 | Epstein negative **in P_T** for T ≥ 1.59 (PROVED, intervals) | Key fact of §3. |

New reason stated (index rule): no previous entry asked whether the falsifiers' witnesses have a nonzero polar
component. That question decides R11.2 without constructing any object.

## 1. Exact anatomy of the polar term

### 1.1 Notation

Complete form W_T(F) = 𝔞_T(F) + 2Re(A(F)·conj B(F)) on L²(−T,T) (P47 l.73, l.345), with
A(F) = ∫F(t)e^{t/2}dt, B(F) = ∫F(t)e^{−t/2}dt; 𝔞_T = m_T + Π_T, where Π_T(F) = −Σ_n v_n·c_F(log n) (with P47's
normalization eq:Aform; v_n = 2Λ(n)/√n), c_F = F∗F̃ autocorrelation, supported on [−2T,2T]. Primitive subspace
P_T = {F : A(F) = B(F) = 0} (moment conditions).

### 1.2 Lemma O1 (the polar term is pole order, not residue; PROVED)

For g = c_F, ∫g(x)e^{x/2}dx = ∫∫F(s)conj F(s−x)e^{x/2} = (∫F(s)e^{s/2}ds)(∫conj F(u)e^{−u/2}du) = A·conj(B); with F real
this is A·B; in general ĝ(−i/2) = A·conj(B) and ĝ(i/2) = B·conj(A), summing to 2Re(AB̄). In Weil's explicit formula for an L-function
with −L′/L = Σ a(n)n^{−s} and a pole of order m at s = 1 (and its mirror at 0), the polar term is m·(ĝ(i/2)+ĝ(−i/2)): it comes from the
residue of −L′/L, which is the order m, not from the residue of L. **Consequence:** the "residue Π(1−1/p)" of ζ_{a_P} does not appear in
any window form. For a_P, ζ_{a_P} = ζ·Π_{p<P}(1−p^{−s}) has a simple pole at 1: m = 1, same as ζ.
Correction to the task's premise: ψ_{a_P}(X) = ψ(X) − Σ_{p<P}Σ_{p^k≤X}log p = X + O(… ) ~ X, **not**
Π(1−1/p)·X (that factor is the density of integers coprime to P, i.e. of the indices of ϑ_P, not of the comb). The "Chebyshev
law = residue" that the form sees is "pole order = average density of the comb", and a_P satisfies it.

### 1.3 Rank and inertia of the polar term

2Re(AB̄) = ½(|A+B|² − |A−B|²): rank 2, signature (1,1) on span{e^{t/2}, e^{−t/2}} (projected to L²(−T,T)). It is the only
indefinite finite-rank piece that separates W_T from 𝔞_T. LEMMA_I3 verifies it in the gauge 𝒢 (9 modes): it goes from (3,0,6) to
(2,0,7), i.e. it removes exactly one negative square from arch (consistent with the (1,1) signature of the polar term plus a cross term).
On P_T the polar term is 0 by definition: P_T **is** "nulling the polar/Tate mode".

### 1.4 Where the pole couples with the comb (what is already PROVED in P47)

Decomposing L²(−T,T) = P_T ⊕ E, E = span of the Riesz representatives of A, B, the form W_T has block
[[𝔞_T|P, X],[X*, 𝔞_T|E + polar]], X = cross block of 𝔞_T (containing m_T and the comb Π_T). By Schur complement
(P47 thm:parityschur, prop:polarcap): λ_W > 0 ⟺ λ_A > 0 and 𝔊_T ≻ 0, with 𝔊_T = (𝔞_T|E + polar) − X*(𝔞_T|P)^{−1}X, a
2×2 matrix diagonal by parity. **This is the exact polar×comb coupling:** the comb enters 𝔊_T only through the
primitive resolvent (𝔞_T|P)^{−1} evaluated in the e^{±t/2} directions. That is: the coupling exists, it is an explicit
2×2 object, and it is conditioned on λ_A > 0. It is not new (P47).

## 2. The form of the falsifier a_P, exactly

### 2.1 Lemma O2 (deletion = smoothed lattice sampling; PROVED)

Let g = c_F be even and L_p(g) := log p·Σ_{k≠0} p^{−|k|/2}g(k log p). The window form of the falsifier a_P (P47, with arch and
polar term of ζ and comb a_P = Λ·1{p ≥ P}) is
  W_T^{a_P}(F) = W_T(F) + Σ_{p<P} L_p(c_F).
With G_p(x) = g(x)e^{−|x|/2}, Poisson on the lattice (log p)ℤ gives
  L_p(g) = Σ_{j∈ℤ} Ĝ_p(2πj/log p) − (log p)·g(0),   Ĝ_p = ĝ ∗ P_{1/2},
P_{1/2}(ξ) = (1/2π)·1/(ξ²+¼), the Cauchy kernel (transform of e^{−|x|/2}), positive. Since ĝ = |F̂|² ≥ 0, Ĝ_p ≥ 0;
g(0) = ‖F‖². So each deleted prime contributes (≥0 sampling of |F̂|² smoothed at the zeros 2πij/log p of 1 − p^{−s})
− (log p)‖F‖².

Reading: the part "−(log p)‖F‖²" is exactly the lost Poisson constant term (SPEC_005 §4.3: the lattice
origin), seen from the side of the form: in ϑ_P, Σ_{d|P}μ(d) = 0 removes the constant term; in the form, each deleted prime
shifts the spectrum by −log p and compensates it with a positive sampling on the line Re s = 0. **It does not touch A or B.**

### 2.2 Is W^{a_P} the Weil form of some distribution with an FE?

ζ_{a_P} has no FE of Γ type (P47 l.8465). The symmetrized function E(s) = ξ(s)Π_{p<P}(1−p^{−s})(1−p^{s−1}) is indeed
symmetric under s ↔ 1−s and has zeros on Re s = 0 and Re s = 1, but (1−p^{s−1}) is not a Dirichlet series for Re s > 1, so
its "comb" is not a_P. Answer (ARGUED, by Lemma O2): W^{a_P} is the Weil distribution of ζ plus, per prime,
the measure Σ_j δ_{2πj/log p} convolved with P_{1/2} minus a (log p)δ-mass; it is not the zero distribution of any
function in the Selberg class (the zeros 2πij/log p have real part at distance ½ from the critical line, and the kernel
P_{1/2} is not that of a zero off the line, which would be cosh((β−½)x), not e^{−|x|/2}). So the intuition "comb and
polar term of different functions" is correct as a **broken FE**, not as a different residue.

### 2.3 Table "same Selberg function" and density

| Object | pole order (form) | comb density | FE with the Γ used | Euler | witness in P_T |
|---|---|---|---|---|---|
| ζ | 1 | 1 | yes | yes | — (positive, PROVED up to ½log15 Mori) |
| a_P | 1 | 1 | **no** | yes | yes (P47, T∈[0.60,½log P]) |
| Epstein x²+5y² | 1 | 1 | yes (degree 2) | no | yes (Lemma E, T ≥ 1.59) |
| cΛ, c≠1 | 1 (Γ of ζ) | c | no | no (c∉ℕ) | cΛ: 𝒲_c=(1−c)·arch (INV_V_002) |
| DH mod 5 | 0 | 0 | yes (conductor 5) | no | complete form |
| Beurling-DMV | 1 | 1 | no | yes | CONDITIONAL (GUO) |

The relation "pole order = density" only distinguishes cΛ, already closed. The property "comb and polar term of the same
Selberg function of conductor 1 with Euler" separates the table, but it is a global property (simultaneous FE + Euler + pole) and not
a quantity inside the form; by C-hom (Lemma H) and C-data it cannot enter 𝔞_T except as an identity between data.

## 3. Theorem O3 (NO-GO PROVED): the polar term is invisible in the falsifiers' witnesses

**Statement.** Let 𝒦_pol be the class of sign-object candidates whose action on the window form goes through the polar
term (residue, Tate mode, Poisson constant term/lattice origin), or through its coupling with the comb via
A, B. Then no element of 𝒦_pol separates ζ from a_P or from Epstein.

**Proof.** (i) a_P: by P47 prop:shape-eulerdel, WP_T(a_P) is λ_inf^P(T) ≥ 0 on P_T, false for T ∈ [0.60, ½log P];
the witness F lives in P_T, so A(F) = B(F) = 0 and the polar term and block E of §1.4 do not intervene. Moreover, for
e^{2T} ≤ P the comb of a_P is empty in N_T: the form is just m_T and the failure is that of arch without primes. (ii) Epstein: by
Lemma E, there exists F = G(t/T) ∈ P_T with 𝔞_T^Q(F)/‖F‖² < −0.0599 at T = 1.59, and the polar term of Epstein is that of ζ
(LEMMA_E l.83). Again A = B = 0. (iii) Every action of 𝒦_pol on W_T factors through (A(F),B(F)) (Lemma O1 and
§1.4: the polar term is a function of A,B; the coupling with the comb is 𝔊_T, which acts on E). Restricted to P_T it is null.
Hence, on the witnesses, the value of any candidate of 𝒦_pol for ζ and for the falsifier coincide (= that of
the primitive form), and it cannot invert the sign. ∎

**Corollary O3′.** The loss of the constant term of ϑ_P (SPEC_005 §4.3) is not the cause of a_P's failure in the
window form: the cause lives in P_T and, for e^{2T} ≤ P, is the absence of comb mass at the primes < P (Lemma O2:
the term −(log p)‖F‖² is offset by a ≥0 sampling, but that offset is exactly what ζ uses in P_T
to win over arch). Put differently: what a_P loses is **the comb of the small primes**, and the "origin"
lost in ϑ_P is its Poisson shadow, not an independent factor.

**Corollary O3″ (reinforced C-Guo).** C-Guo said: the pole alone does not separate because Epstein has it too. O3 says more: neither
the pole nor any coupling of the pole with multiplicativity separates, because the witnesses have zero polar moment.
The coupling 𝔊_T of §1.4 only matters once λ_A > 0 has been won, and it is the second condition of P47's Schur, not the
separator.

## 4. Order-2 candidate: the Selberg identity

**Formulation.** Σ_{n≤X}Λ(n)log n + Σ_{mn≤X}Λ(m)Λ(n) = 2X log X + O(X), equivalently ζ″/ζ = (ζ′/ζ)′ + (ζ′/ζ)² has a
triple pole with coefficient 2. It is elementary, zero-free, and uses Λ∗Λ (product m·n: the semiring principle).

**Does it enter the form?** The comb of 𝔞_T is linear in v_n (Lemma H: 0-homogeneous in theta, linear in Λ). Λ∗Λ does not appear
as a term of 𝔞_T for any test; a test c_F∗c_F still gives Σ v_n·(c_F∗c_F)(log n), linear in Λ. For
Λ∗Λ to appear it must be imposed as a relation between data v_n in the LP/SDP of def:PD: by R11_1 Theorem C1 that is
**C-data** (equality between data, null multiplier column ⇒ dual value invariant). NO-GO PROVED by C-data.

**Comb-generic filter.** The identity (as an asymptotic with O(X)) is satisfied by: a_P (finite deletion changes ψ by O(1)·log
and Λ_P∗Λ_P by O(X)) — PROVED elementary; Beurling-DMV (AUDIT_B 7.7, CITED); Epstein: Z_Q does not vanish near s=1 and has a
simple pole, so Z″/Z has a triple pole with coefficient 2 and the Tauberian version holds (ARGUED; the elementary version with
O(X) requires more, irrelevant here). Comb-generic ⇒ does not separate. Duplicate of TB-3 (06_OPEN R7) and AUDIT_B 7.7: **not
retried**; only the "order-2 residue-comb relation" variant is recorded.

Montgomery's variance, Hardy–Littlewood for Λ(n)Λ(N−n): zero side / additive sum (INV_J_001); not opened.

## 5. Full filter by candidate

| Candidate | REF-D | comb-generic | C-data | C-hom | zero side | Verdict |
|---|---|---|---|---|---|---|
| residue of L (value) | — | — | — | — | — | invisible in the form (Lemma O1) |
| pole order = density (Chebyshev) | no | yes (a_P, Epstein, Beurling) | yes | — | no | NO-GO (only cΛ, already closed) |
| constant term of ϑ / origin | no | — | — | yes (Lemma H) | no | NO-GO by O3 (witnesses in P_T) |
| Tate mode | no | yes (Lemma 2.1 GUO) | — | — | no | NO-GO (duplicate GUO) |
| 𝔊_T polar×comb coupling | no | — | — | — | no | PROVED exists (P47), does not separate (O3) |
| "same Selberg function" | high risk | no | yes if imposed | yes | no | global, not quantitative in the form: OPEN as classifier, NO-GO as motor |
| Selberg identity | no | yes | yes | — | no | NO-GO (duplicate) |
| fine ψ−X (next order) | yes | — | — | — | yes | discarded |

## 6. Tests

**Mori μ = 15 (T = ½log15).** Mori's extremal is the lower eigenvector of the primitive form of ζ (GUO §3 data
MORI15, L = T): it lives in P_T, A = B = 0, polar term null. Epstein's value at Mori's extremal is +1.975 (LEMMA_E); the
difference from ζ is attributed by LEMMA_E to the Γ factor (degree 2), not to the comb or the pole. Consistent with O3: the pole does not
participate. Nothing new to compute.

**Lemma E.** Witness in P_T (T = 1.59): the polar term is 0 on it (PROVED by construction, F ∈ P_T). The
decomposition Λ_Q = ½(Λ_K+Λ_ψ)+Λ_cosh localizes the defect in Λ_cosh (C-E). R11.2 provides no control over Λ_cosh.

## 7. Labels, new restriction, index, next

**Labels.**
- Lemma O1 (polar term = 2Re(AB̄), counts pole order, not residue): PROVED.
- Correction: ψ_{a_P}(X) ~ X (not Π(1−1/p)X): PROVED.
- Lemma O2 (deletion = Cauchy sampling on (2π/log p)ℤ − (log p)‖F‖²): PROVED.
- §2.2 (W^{a_P} is not the Weil form of a function in the Selberg class): ARGUED.
- Theorem O3 (polar term/origin/Tate and its coupling invisible in the witnesses): NO-GO PROVED (given P47 prop:shape-eulerdel
  and Lemma E, both PROVED).
- Selberg identity as separator: NO-GO (C-data PROVED; comb-generic PROVED for a_P, CITED Beurling, ARGUED Epstein).

**New restriction C-pol (PROVED).** Every sign-object candidate whose action on the window form factors
through the moments (A(F), B(F)) = (∫Fe^{t/2}, ∫Fe^{−t/2}) — residue, pole, Tate mode, Poisson constant term,
lattice origin, polar capacity 𝔊_T — is null on P_T and cannot separate ζ from a_P or Epstein, whose witnesses
live in P_T. Before proposing a "polar" object, check that it acts nontrivially on P_T.

**Entry for the index (README, phase 200 section):**
- **R11_2_ORIGIN_001 (round 13): R11.2 closed, NO-GO PROVED (Theorem O3).** The polar term 2Re(AB̄) counts pole order, not
  residue (O1); ψ_{a_P}~X; the form of a_P = W_ζ + Σ_{p<P}[Cauchy sampling on (2π/log p)ℤ − (log p)‖F‖²] (O2). The witnesses
  of a_P (P47 shape-eulerdel) and Epstein (Lemma E) are in P_T ⇒ pole/residue/Tate/origin/𝔊_T invisible; the "lost origin"
  of ϑ_P is the Poisson shadow of the deleted primes. Selberg identity: C-data + comb-generic (dup. TB-3/AUDIT_B 7.7).
  Restriction **C-pol**.

**Next lemma.** None in the polar channel. What remains alive after O3 is strictly primitive: the separator must
act on P_T and, for a_P, must already show up when the comb in N_T is empty or nearly empty — i.e. it is a lower bound of the
comb mass of the small primes against m_T in P_T (the terrain of λ_A, Thm A/thm:Tarch of P47), and for Epstein it must
control Λ_cosh (C-E). Proposal (OPEN, not constructed): formulate the separator as a functional of P_T that uses the
offset of Lemma O2 in reverse — the Cauchy sampling on (2π/log p)ℤ of the primes that *are present* — and check it
against C-hom/C-data before building.
