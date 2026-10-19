# R183.019 — Sonin alignment and evaluation direction

## 0. Source, corpus, and verdict

Source: Connes–Consani, *Weil positivity and Trace formula, the archimedean
place*, arXiv:2006.13771; local copy
`03-research/phase-137-row-d-canonical-coupling/cc_2006.13771_text.txt`
(Theorem 1 l.109; Prop. 5.5 l.2168; §6.1–6.7 l.2255–3140; Lemma 6.9,
Lemma 6.10, Theorem 6.11, Remark 6.12). Corpus consulted: R183.001,
.012, .015, .016, .017; grid
`phase-162-row-d-first-contact-closure/grid/R162_2300_MASTER_GRID.md`
(row 25: Riesz → Sonin, E1); `phase-161-.../R161_014_SONIN_GAMMA_COERCIVITY.md`
(Sonin–Gamma coercivity on a product port; a different object, not
duplicated); Paper 47 (`thm:Z`, `thm:Zexh`, `prop:TK`, `thm:index`).

**Main finding (not a new mechanism).** R183.017's alignment is
*exactly* Connes–Consani's proof: their Lemma 6.9 is R183.017's lemma
and their Lemma 6.10 applies it with φ=ζ (top eigenvector), ψ=ξ_0
(normalized constant), b=λ_max−1, c=1−λ_2. What this file adds:

1. explicit e_T, with and without the second Tate moment (§1, PROVED);
2. the identity δ = the form's value on the unique direction of e^⊥ in the
   plane ⟨v,e⟩; hence: alignment ⟺ strict positivity on ker ℓ (§3, PROVED);
3. monotonicity of K_I's eigenvalues and rank-one NO-GO when λ_2>1 (§3);
4. NO-GO for the naive extension with primes: with the archimedean Sonin
   projection fixed, the semilocal remainder is not bounded below in CC's
   norm as soon as a single prime enters the window (§4, PROVED);
5. the correction a|e⟩⟨e| is an explicit-formula certificate for the
   zero measure augmented by an atom at γ=0 (§5): the global Sonin route =
   D on the ideal ker ℓ plus a strictly stronger Sonin bound.

Neither RH nor the closure of D is claimed.

## 1. Normalizations and the evaluation vector e_T

### 1.1 Dictionary (CITED + PROVED)

CC work with g∈C_c^∞(R_+^*), f=g*g^*, ĝ(z)=∫g(u)u^{-iz}d^*u. In the
coordinate x=log u set η(x)=g(e^x), so that ĝ(z)=∫η(x)e^{-izx}dx and
η is R183.015's test h (φ=ĝ on the real line). g's support in
[2^{-1/2},2^{1/2}] ⟺ supp η ⊂ [−T,T] with **T=½log 2**: this is the
prime-free window of R183.015 (k log p ≥ 2T for every p) and coincides
with Paper 47's window T=½log2.

CC only impose ĝ(−i/2)=0 (l.115, Theorem 6.11). With that condition
k(u)=u^{1/2}∫_0^u v^{-1/2}g(v)d^*v has compact support in the same
interval (l.3122) and, with ξ(x)=k(e^x),

    η = ½ξ − ξ'   (Rem. 6.12, l.3136),        ξ ∈ H_T := L²(−T,T).     (1.1)

Proof that (1.1) is a bijection between {η∈C_c^∞(−T,T): ∫η e^{-x/2}=0} and
C_c^∞(−T,T) (PROVED): ξ(x)=−e^{x/2}∫_{−∞}^x e^{−y/2}η(y)dy solves
ξ'−½ξ=−η; it has compact support in [−T,T] exactly when
∫η e^{−y/2}=0. Conversely, for ξ compact, integrating by parts
∫ξ' e^{sx}=−s∫ξe^{sx}, hence

    ∫η e^{sx}dx = (½+s)∫ξ e^{sx}dx.                                     (1.2)

At s=−½ the factor vanishes: moment ĝ(−i/2) is automatic. At s=+½
(moment ĝ(+i/2), the second one of R183.001(4.1)): ∫η e^{x/2}=∫ξe^{x/2}.
At s=0: ĝ(0)=½∫ξ. (CC write k̂(0)=−2ĝ(0) due to their sign convention
on k; the modulus agrees.) □

### 1.2 Riesz representative (PROVED)

ℓ(ξ):=ĝ(0)=½∫_{−T}^{T}ξ = ⟨½·1_{I_T}, ξ⟩. Hence, in CC's space
(one moment):

    e_T = (2T)^{−1/2} 1_{I_T},   ‖ℓ‖² = T/2,   |ĝ(0)|² = (T/2)|⟨e_T,ξ⟩|².   (1.3)

At T=½log2: |ĝ(0)|²=(log2/4)|⟨ξ_0,ξ⟩|², reproducing c=4γ/log2 of
Theorem 6.11 (γ|⟨ξ_0,ξ⟩|² = (4γ/log2)|ĝ(0)|²). Check: correct.

With R183.001/015's two Tate moments (space H'_T = w^⊥,
w=e^{x/2}), the representative is the projection of ½·1:
⟨w,1⟩=4 sinh(T/2), ‖w‖²=2 sinh T, and

    e'_T ∝ 1 − (2 sinh(T/2)/sinh T) e^{x/2},
    ‖ℓ|_{H'_T}‖² = ¼‖P_{w^⊥}1‖² = T/2 − tanh(T/2) = T³/24 + O(T⁵).       (1.4)

(Computation: ‖P1‖² = 2T − 16 sinh²(T/2)/(2 sinh T) = 2T − 4 tanh(T/2).)
Consequence: in the two-moment space, ℓ becomes nearly degenerate
for small T; the coefficient in |ĝ(0)|² equivalent to a|⟨e',ξ⟩|² is
a/‖ℓ|_{H'}‖², which diverges like 24a/T³. For T=½log2 the natural space is
CC's (one moment); the second moment only restricts to a subspace
and, as §3 shows, changing the subspace changes (v,b,c,α).

### 1.3 How it enters a_min

If the form bound holds with unit e, the final inequality is
R ≥ −a_min|⟨e,ξ⟩|² = −(a_min/‖ℓ‖²)|ℓ(ξ)|². In CC: N_I=−½(1+ε)(Id−K_I)
(Prop. 5.5, l.2172; the factor ½(1+ε) is their inner-product
normalization, not reconstructed here). CC choose a≈0.064 (somewhat
larger than a_min, to leave margin ε_2≈0.00441 > ε_1≈0.00122 absorbing
‖K_I−T‖), multiply by that constant, and obtain γ≈2.94355, c=4γ/log2
(CITED; the optimal constant satisfies 13<c<17, Rem. 6.12).

## 2. The negative direction v for S={∞}

### 2.1 Hypothesis H(T) (precise statement)

For I_T=[−T,T], let K_{I} be CC's compact (Hilbert–Schmidt) operator
of Prop. 5.5, (104), defined by a translation kernel Q(exp|v|) on
I (continuous Toeplitz). Prop. 5.5 is proved **only for |I| ≤ log 2**
(l.2168: the formula uses that f=η*ξ^* lives on [−log2,log2]).

**H(T):** |I_T|=2T≤log2, K_{I_T} has exactly one eigenvalue
λ_1(T)>1, with unit eigenvector ζ_T, and λ_2(T)<1. Then

    Id−K_{I_T} = −b_T|ζ_T⟩⟨ζ_T| + R',  R' ≥ c_T(Id−|ζ_T⟩⟨ζ_T|),
    b_T=λ_1(T)−1,  c_T=1−λ_2(T).                                         (2.1)

Status of H: at T=½log2, CITED with CC's computer-assisted numerical
verification (λ_max=1.05158, λ_2≤0.772216 via Lemma 6.8(iii),
‖K_I−T‖≤ε_1≈0.00122). For T<½log2: OPEN as a theorem (CC's Fig. 11
suggests λ_1(T)<1 for small T; then there is no negative direction and
b_T<0, a trivial case).

### 2.2 What v is (CITED)

v=ζ_T is K_I's top eigenvector, **not** the evaluation direction:
CC, Fact 6.5 and §6.7(ii): ⟨ξ_0|ζ⟩≈0.94865, so α²≈0.89994<1. By
Toeplitz theory (CC (107)) ζ is even and its discrete polynomial has
unimodular roots; this explains the large overlap with the constant (ζ
is the lowest-oscillation "wedge"), but gives no rigorous bound on α.

### 2.3 Monotonicity in T (PROVED, in Prop. 5.5's range)

For I⊂I' (both of length ≤log2), K_I = P_I K_{I'} P_I restricted to
L²(I), because (104) is the same translation kernel. By min-max
(Cauchy), λ_j(K_I) ≤ λ_j(K_{I'}) for every j. Hence λ_1(T), λ_2(T) are
nondecreasing in T: b_T increases and c_T decreases. There is no
monotonicity of α_T provable by this argument (ζ_T rotates with T); OPEN.

## 3. Alignment theorem

### Theorem 3.1 (PROVED; abstract)

Let Q be a bounded self-adjoint operator on a Hilbert space H, e a unit
vector, P=Id−|e⟩⟨e|. The following are equivalent:
(a) there exists a<∞ with Q+a|e⟩⟨e| ≥ 0;
(b) PQP ≥ 0 on e^⊥ and Pqe ∈ Ran((PQP)^{1/2}) (q:=Q).
If PQP ≥ κ>0 on e^⊥, (b) holds and

    a_min = max(0, ⟨PQe,(PQP)^{−1}PQe⟩ − ⟨e,Qe⟩).                      (3.1)

Proof. ξ=te+y, y⊥e: (Q+a ee^*)(ξ)=|t|²(⟨e,Qe⟩+a)+2Re(t̄⟨e,Qy⟩)+Q(y).
(a)⇒ PQP≥0 taking t=0; and positivity of the 2×2 form in (t,‖·‖) forces
|⟨PQe,y⟩|² ≤ (⟨e,Qe⟩+a)Q(y) for every y, which is the range condition
(Douglas). (b)⇒(a): the same inequality with a = sup_y |⟨PQe,y⟩|²/Q(y) −
⟨e,Qe⟩, finite by the range condition; if PQP≥κ the sup is (3.1)
(Schur complement). □

### Corollary 3.2 (PROVED): δ is the form's value on e^⊥

In R183.017's model R_0=−b|v⟩⟨v|+c(Id−|v⟩⟨v|), with α<1, the unique
unit vector (up to phase) of span{v,e} orthogonal to e is
u=(v−⟨e,v⟩e)/√(1−α²), and |⟨v,u⟩|²=1−α². Then

    R_0(u) = −b(1−α²) + c α² = (b+c)α² − b = δ,                          (3.2)

and R_0 = c on (span{v,e})^⊥. Hence R_0|_{e^⊥} ≥ min(δ,c), with equality
for δ<c. Thus

    δ>0  ⟺  R_0 > 0 strictly on ker ℓ.                             (3.3)

R183.017's alignment is **not an additional condition**: it is the
positivity (with a gap) of the form on ker ℓ, i.e. exactly the content of
CC's Theorem 1 (ĝ(0)=0). The constant a_min=bc/δ is (3.1) in this model.

### Theorem 3.3 (alignment under H; PROVED given H)

Under H(T), Q=Id−K_{I_T} admits a finite correction on e_T if and only if

    α_T² > b_T/(b_T+c_T) = (λ_1(T)−1)/(λ_1(T)−λ_2(T)),                  (3.4)

and then a_min(T)=b_Tc_T/δ_T on e_T, i.e. the coefficient of
|ĝ(0)|² is a_min(T)/‖ℓ‖² = 2a_min(T)/T (by (1.3)), multiplied by
N_I's normalization constant. (Proof: R183.017 + Cor. 3.2; only the
lower bound R'≥c(Id−ζζ^*) is used, and necessity uses that on ζ^⊥ the
form is exactly ≥c with R'ζ=0 ⇒ the plane span{ζ,e} reduces the problem;
if R' is not exactly c on the plane, (3.4) is sufficient and the exact
condition is that of Theorem 3.1.) □

Evaluation at T=½log2 with CC's constants (CITED, exact arithmetic
on their numbers): b=0.05158, c≥0.227784, α²=0.94865²=0.899937;
threshold b/(b+c)=0.18463; δ=0.279364·0.899937−0.05158=0.19983>0;
a_min=0.011749/0.19983=0.0588. CC use a≈0.064 ≥ a_min (consistent).
The margin is large: (3.4) admits α² down to 0.185, i.e. α≥0.43.

### Proposition 3.4 (rank-one NO-GO; PROVED)

If for some T (in any extension where Id−K_{I_T} remains the
remainder) λ_2(K_{I_T})>1, no correction a|e⟩⟨e|, for any fixed e,
restores positivity. Proof: Id−K has a 2-dimensional subspace V with
negative-definite form; V∩e^⊥≠0 and there a|e⟩⟨e| vanishes. □

**Exact failure mechanism as T grows.** By §2.3, b_T↑ and c_T↓. By
(3.4) δ_T≤0 can occur via (i) c_T→0 (λ_2 rises to 1: then (3.4)
requires α_T→1 and generically fails at the crossing, and beyond it
Prop. 3.4 gives a NO-GO for every e), or (ii) loss of overlap α_T. Since
λ_1(½log2)≥1.0503>1 and the eigenvalues of Toeplitz compressions do not
exceed the symbol's supremum, the symbol's supremum of K ≥1.05; if the
symbol is continuous, the set {symbol>1} has positive measure and by
Landau–Widom the number of eigenvalues >1 of the compression grows
linearly in |I| (CONDITIONAL: the extension of (104) to |I|>log2 without
changing the kernel is not in CC). Under that extension, mechanism (i) is
unavoidable for large T. The crossing T_2 with λ_2(T_2)=1 is OPEN (not
computed; no numerics by rule). Comparison: Paper 47 `thm:index` shows
that the full archimedean form A_∞ on P_T has n_−=0 up to T≈0.58 and
n_−=1 up to T≥log2: CC's negative direction belongs to the **remainder**
relative to Sonin, not to W_∞ (which is positive with no correction at
T=½log2 on P_T). The Sonin route loses information relative to W_∞ in
this window.

## 4. Interaction with primes: S ⊋ {∞}

Let p be prime with a:=log p < 2T (otherwise the increment is 0 by
support, R183.015). By R183.015 the increment is

    Π_p(η) = −2(log p) Σ_{k: ka<2T} p^{−k/2} Re c_η(ka),  η=½ξ−ξ'.       (4.1)

In CC's ξ variable, for ξ∈C_c^∞(I_T): c_η(a)=⟨(½−∂)ξ,τ_a(½−∂)ξ⟩ =
⟨ξ,(¼−∂²)τ_aξ⟩. Π_p is a Toeplitz form with symbol
−2Σ_k (log p)p^{−k/2}(¼+s²)cos(ks log p): **growing like s²**, while
Id−K_I is bounded on L²(I). It is not a small rotation of v.

### Theorem 4.1 (NO-GO for the naive remainder; PROVED)

Let T>0, S⊇{∞,p} with log p<2T, and define the
remainder with CC's fixed archimedean Sonin projection,
R_{S,T} := −E + Σ_{p∈S} Π_p on ξ∈C_c^∞(I_T), where −E is any
bounded form on L²(I_T) (this is CC's archimedean term when
Prop. 5.5 applies). Then for every M>0 and every N there is a subspace
of dimension N, contained in ker ℓ ∩ {∫ξe^{x/2}=0}, where
R_{S,T}(ξ) ≤ −M‖ξ‖². In particular no bound
R_{S,T} ≥ −b|v⟩⟨v|+c(Id−|v⟩⟨v|) with b<∞ exists, and R183.017's
Obligation 2 is false for this remainder.

Proof. Let a=log p₀<2T with p₀∈S, and L={k log q: q∈S prime, k≥1,
k log q<2T}, a finite set. Choose ε>0 with a+2ε<2T and 4ε < the
distance from a to L∖{a} (p₀ prime: a=k log q only for q=p₀, k=1). Let
φ∈C_c^∞(−ε,ε) be real nonzero, ψ_n=φ(x)cos(nx), and for j=1..N+3 points
x_j with [x_j−ε, x_j+a+ε]⊂I_T, chosen so all differences
x_i−x_j, x_i−x_j±a (i≠j) are more than 2ε away from L∪{0} (possible:
avoiding a finite number of bands of width 4ε in an interval of length
2T−a−2ε, taking ε small). Set ξ_j = ψ_n(·−x_j) + ψ_n(·−x_j−a).
Supports are disjoint, so the ξ_j are orthogonal; η_j=(½−∂)ξ_j
has the same support. For b∈L, c_{Σt_jη_j}(b) only receives the
contribution of each pair at offset exactly a, and equals
Σ|t_j|²‖(½−∂)ψ_n‖² at b=a and 0 at b≠a; also ‖(½−∂)ψ_n‖² =
¼‖ψ_n‖²+‖ψ_n'‖² (∫ψψ'=0). Thus, for ξ=Σt_jξ_j,
ΣΠ(ξ) = −2(log p₀)p₀^{−1/2}Σ|t_j|²(¼‖ψ_n‖²+‖ψ_n'‖²).
Since ‖ψ_n'‖²/‖ψ_n‖² → ∞ (≈n²) and ‖ξ‖²=2Σ|t_j|²‖ψ_n‖²,
ΣΠ(ξ)/‖ξ‖² ≤ −(log p₀)p₀^{−1/2} n²(1+o(1)), and −E contributes ≤‖E‖‖ξ‖².
With N+3 pairs and large n, the (N+3)-dimensional subspace is negative
≤−M; its intersection with the three linear conditions (ℓ and two Tate
moments in the variable η; all three are continuous functionals) has
dimension ≥N. □

Remark (consistency, not a proof). The full form W_S may still be
positive on these vectors: the Sonin trace grows like
∫(¼+s²)log|s||ξ̂|² ~ n²log n ≫ n². The NO-GO says that the decomposition
"W_S = Tr(archimedean Sonin) + remainder with a single negative mode" is
false as soon as a prime is in the window; it does not refute W_S≥0.

### Consequence and sufficient condition

With the fixed Sonin projection there is no condition (S,T) under which
alignment survives except the trivial one: S∩{p: log p<2T}=∅, i.e.
T≤½log2 (CC's case). For T>½log2 a semilocal Sonin projection
**depending on (S,T)** is needed whose trace absorbs the s²-growing part
of the Π_p (a semilocal Sonin form; CC only have it at ∞). Building it is
R183.017's Obligation 1: OPEN. "Rotating v" would only make sense after
that construction: if the new remainder R^{new}_{S,T} is bounded on L²
with a single negative eigenvalue, Theorem 3.1/3.3 apply verbatim, and
the condition is (3.4) with its constants.

## 5. Crossing with Paper 47: certificate or outside the class?

### Proposition 5.1 (PROVED)

For F∈L²(I_T), |F̂(0)|² = (1/2π)∫ k̂_c(τ)|F̂(τ)|²dτ with
k_c=1_{[−2T,2T]} (constant kernel restricted to the difference window),
k̂_c(τ)=2 sin(2Tτ)/τ; and also = (1/2π)∫2π δ_0(τ)|F̂(τ)|²dτ. Hence
W_T + a|F̂(0)|² is Weil's form with modified symbol
S_T + 2πa δ_0 (or, modulo kernels supported on |u|≥2T, S_T+a k̂_c).

Proof: F̂(0)=∫F; ∫∫F(x)F̄(y)·1 dxdy and 1=k_c(x−y) for x,y∈I_T. □

### Corollary 5.2 (reading in terms of Theorem Z; PROVED except for the
dual, which is CONDITIONAL)

By `thm:Z`(ii), a flat certificate f_w(τ)=Σ_ρ ŵ(τ−γ_ρ). Adding
a|F̂(0)|² amounts to adding to the zero side a term c_a·ŵ(τ−0), i.e. a
fictitious multiplicity (proportional to a) at γ=0: this is exactly the
certificate for the zero measure augmented by an atom at γ=0, i.e.
CC's "ζ(z)(z−½)^{17}" (Cor. 2, l.128–135; CITED, not a new observation).
In Paper 47's formulation it is the class of `thm:Zexh`(ii) with a third
multiplier β_2 on the function ĝ_c=k̂_c (besides β_0,β_1
on ĝ_0,ĝ_1). The claim that the dual of that enlarged problem
coincides with the primal (analogous to `thm:Zexh`) is CONDITIONAL: it
has not been verified that Paper 47's proof passes with the third
restriction.

### Answer to question 5

* It is not a certificate of `thm:Z`/`prop:TK`'s class (β∈R²): it is a
  certificate of an enlarged class (β∈R³), whose value is ≥ that of the
  original class for each T. `prop:TK`'s ceiling TK is defined for
  β∈R²; its proof (bound on the minimal eigenvalue of S_β's Toeplitz
  matrix) only uses that S_β is a combination of bounded functions and
  extends to β∈R³ (CONDITIONAL: sketch, not rewritten). It is neither
  "below" nor "above": it lives in a different class, with its own
  ceiling ≥ the previous one.
* Globally (for all T): Weil positivity on ker ℓ for every T ⟺ RH,
  because ζ(½)≠0 (CC, comment after (4), l.112–114: the conditions
  ĝ(0)=ĝ(±i/2)=0 "do not compromise" the criterion; CITED). Hence the
  Sonin route with fixed e is **D restricted to the codimension-one
  ideal ker ℓ** — a reformulation of D, not a weakening — **plus** the
  bound W ≥ Tr(ϑSϑ^*) on ker ℓ, which is strictly stronger than W≥0
  and is not known to be implied by RH (by CC Cor. 2 it is equivalent to
  the zeros dominating the Sonin trace). Verdict: a genuinely stronger
  sufficient condition than D; not a weaker one.
* `thm:index`: CC's n_−≤1 (for Id−K_I) and Paper 47's n_−∈{0,1,2}
  (for A_∞ on P_T) are different objects; at T=½log2 the former equals 1
  and the latter 0. There is no contradiction nor transfer.

## Status

* Evaluation representative e_T, ‖ℓ‖²=T/2; two-moment version
  ‖ℓ|_{H'}‖²=T/2−tanh(T/2): **PROVED**.
* Dictionary η=½ξ−ξ', automatic moment ĝ(−i/2): **PROVED**
  (matches CC; CITED).
* Identification v=ζ_T, α≈0.94865, b≈0.05158, c≥0.2278 at T=½log2:
  **CITED** (CC's numerical verification).
* Theorem 3.1 (exact rank-one correction criterion) and
  Cor. 3.2 (δ = value on e^⊥; alignment ⟺ positivity with a gap on ker ℓ):
  **PROVED**.
* Theorem 3.3 (α_T²>(λ_1−1)/(λ_1−λ_2)): **PROVED** given H(T); H(T)
  **CITED** at T=½log2, **OPEN** in general; δ(½log2)≈0.1998>0 with CC's
  constants.
* Monotonicity λ_j(T)↑ for 2T≤log2: **PROVED**; monotonicity of α_T: **OPEN**.
* Prop. 3.4 (λ_2>1 ⇒ no fixed e works): **PROVED**; Landau–Widom-type
  growth of #{λ_j>1} for |I|>log2: **CONDITIONAL**.
* Theorem 4.1 (with fixed archimedean Sonin, the remainder with one
  prime in the window is unbounded below, infinite negative index):
  **NO-GO PROVED**.
* Semilocal Sonin depending on (S,T): **OPEN** (Obligation 1).
* Prop. 5.1/Cor. 5.2: correction = atom at γ=0 (CC Cor. 2, **CITED**);
  global Sonin route = D on ker ℓ + Sonin bound, **stronger** than D:
  **PROVED** except for the enlarged dual equivalence (**CONDITIONAL**).
* Row D: **OPEN**. RH is not claimed.

**Exact missing lemma.** Build, for S⊇{p: log p<2T}, a semilocal Sonin
projection S_{S,T} such that R_{S,T}:=W_S − Tr(ϑ S_{S,T} ϑ^*) is a
*bounded* form on L²(I_T) (variable ξ) with λ_2(R_{S,T}) ≥ c_{S,T}>0
(a single negative mode) and α_{S,T}² > b_{S,T}/(b_{S,T}+c_{S,T}).
By Cor. 3.2, the last condition is positivity with a gap on ker ℓ.

## Review points

1. §2.2–3.3 depend on CC's numerical constants (λ_max, λ_2, α); only
   the arithmetic is redone, not the certification. N_I's normalization
   ½(1+ε) was not reconstructed: the final coefficient of |ĝ(0)|² is
   compared with CC only via a≈0.064 ≥ a_min≈0.0588.
2. Theorem 4.1 assumes the archimedean part of the remainder is bounded
   on L²(I_T) also for 2T>log2 (CC prove this only for |I|≤log2, Prop.
   5.5; Theorem 3.6 gives another compact operator for general I). If for
   |I|>log2 the unbounded archimedean term exactly compensated the
   Π_p, the NO-GO would reduce to "CC's decomposition does not extend
   without changing S"; check against Theorem 3.6's form.
3. Cor. 5.2: the identification with Paper 47's class with β∈R³ and
   the extension of the TK ceiling are sketched, not proved; the
   equivalence "Weil on ker ℓ ∀T ⟺ RH" is cited from CC and the classical
   argument, not re-proved here.
