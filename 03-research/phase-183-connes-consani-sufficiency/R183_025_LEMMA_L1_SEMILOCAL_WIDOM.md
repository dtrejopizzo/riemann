# R183.025 — Lemma L1 (semilocal Widom): exact reduction, two-edge model, and the only missing estimate

Phase 183.
Neither RH nor the closure of row D is claimed.

Inputs: R183_018 (§3, §4, Thm 5.1), R183_020, R183_021 (Prop 3.3, Lemma
(CF-S), Thm 3.4), R183_024 (§2.1–2.4, Lemma 2.3, Prop 2.4), R162_2602
(Thm 4). Source: CCM 2310.18423 `mainc2m24fine.tex` l. 940–1060 (Prop
sonintensor, (ms1), Prop groundstatedual (iii)); CC 2006.13771 Thm 4.7,
(83)–(90).

Notation. S = {∞,p}, a := log p, ε := p^{−1/2}. Logarithmic variable
t = log|x| (f side) and t_F = log|y| (Ff side). In L²(R)^{ev} with the
unitary normalization, τ f(x) := p^{−1/2} f(x/p) is translation
t ↦ t+a and Fτ = τ^{−1}F. For h ∈ C_c^∞(I_T), C := ϑ(g) and C^*C has
convolution kernel c_h in t (R183_024 §2.3). For an operator X, write
⟨X⟩_h := Tr(C X C^*). K := S(1,1) (archimedean Sonin, λ = 1), Π := Π_∞.

---

## 0. Verdict

1. **(PROVED) Exact reduction.** G := θ_S^*θ_S is the *compression*
   Π|m|²Π on K (not a multiplication on L²), with
   |m(s)|² = 1 − 2ε cos(sa) + ε². The semilocal Sonin space, carried to
   the archimedean side, is (1−ετ)K. It is contained in
   K' := S(1, p^{−1}) (Fourier condition relaxed to |y| < 1/p), and
   K' ⊖ (1−ετ)K = D := Π_{K'} F^{−1}(E), where E is an explicit space of
   "geometric continuations" of length a at the Fourier edge (Thm 1).
2. **(PROVED) Two-edge model, all orders.** When K is replaced by
   L²[0,L] (two hard edges at distance L), one obtains

       ⟨Π_S⟩_h − ⟨Π⟩_h = −2 log p Σ_{k≥1} p^{−k/2} Re c_h(k log p) + O(p^{−⌊L/a⌋}),

   and the error vanishes as L → ∞ (Thm 2). This improves R183_024's
   Lemma 2.3 and Prop 2.4, which were first-order and on the half-line,
   to an exact identity at all orders with two edges. The factor log p is
   real: it is the length a of the defect space. There is a discrete
   numerical check, agreeing to 10^{−14}.
3. **(PROVED) R183_021's (CF-S) heuristic is false in the model.** There
   the local density L plays the role of ν(s) ~ log|s|. One has
   ρ_S − ρ_∞ = O(1), not o(1), and the relative error is O(1/L), not
   O(L^{−2}). The Christoffel asymptotics exactly misses the
   boundary-layer term (Cor 2.2).
4. **L1 for the true Sonin space: CONDITIONAL**, in the weak form L1′
   (δε_p ∈ L²_loc, which suffices for all the consequences), on **one**
   isolated estimate: (E′), requiring the edge-interaction density
   r_p(s) to be in L²(ds) (Thm 3). There is also a routine, non-arithmetic
   input (Λ), CC Thm 4.7's scaling law on S(λ,λ). The dichotomy is sharp:
   **(CF-S) ⟺ r_p does not decay, but exactly cancels the prime
   oscillation** (Cor 3.2). R183_021 and R183_024 rest on the same number
   r_p.
5. Consequence (CONDITIONAL on (E′)+(Λ)): Son_S absorbs the bump-pair
   family; R'_S = −∫c_h ε_S is Hilbert–Schmidt, and Thm 5.1's NO-GO of
   R183_018 does not apply to the partition Son_S + R'_S. What remains
   afterward is N_T (R183_024 §2.5), which carries all the arithmetic
   content.

L1 is not decided unconditionally. Everything except (E′) is proved, and
(E′) is a prolate estimate with no primes in its core (§4).

---

## 1. Exact reduction (PROVED)

**1.1 The metric G.** By (ms1), U_S θ_S U_∞^{−1} is multiplication by
m(s) = 1 − p^{−1/2−is} restricted to U_∞K. Since U_S and U_∞ are unitary,

    θ_S^*θ_S = Π |m|² Π  (as an operator on K),    |m|² = 1 − 2ε cos(sa) + ε².

In t, m is 1 − ετ: positive translation preserves support t ≥ 0. For
even f, |x| suffices (the ev restriction is compatible, because τ and F
preserve parity). ϑ(g) commutes with θ_S, because both are
multiplications in s. Thus Son_S(h) = ⟨Π_{(1−ετ)K}⟩_h, and the formula
Π_{(1−ετ)K} = (1−ετ)Π(ΠGΠ)^{−1}Π(1−ετ)^* holds (R183_024). Source's Prop
4.7(iii) (η_S = (θ_S^*)^{−1}) is the dual version. (CITED + computation.)

**Theorem 1 (exact description of the defect; PROVED).** Let
K' := {f ∈ L²(R)^{ev} : f = 0 on |x|<1, Ff = 0 on |x|<1/p}. Then:

(i) (1−ετ)K ⊂ K'.

(ii) f ∈ K' belongs to (1−ετ)K if and only if Ff ⊥ E, where

    E := { e_u := Σ_{k≥0} ε^k τ^{k} u : u ∈ L²(R)^{ev}, supp u ⊂ {−a ≤ t_F < 0} }.

    The e_u form a closed space, and u ↦ (1−ε²)^{1/2} e_u is unitary
    from L²(layer) onto E.

(iii) K' ⊖ (1−ετ)K = D := closure of Π_{K'}F^{−1}E.

*Proof.* (i) If g ∈ K, (1−ετ)g vanishes on |x|<1, and
F(1−ετ)g = (1−ετ^{−1})Fg, which vanishes on |y| < 1/p.

(ii) Given f ∈ K', the only candidate is g = (1−ετ)^{−1}f = Σ_k ε^kτ^k f
(Neumann series, ‖ετ‖ < 1), which vanishes on |x|<1. Also
Fg = Σ_k ε^k τ^{−k}Ff. On t_F < 0, since Ff = 0 on t_F < −a, the
condition Fg = 0 on t_F<0 reads
Σ_k ε^k (τ^{−k}Ff)(t_F) = 0 on [−a,0) (in unitary form,
⟨τ^{−k}Ff, u⟩ = ⟨Ff, τ^k u⟩), i.e. ⟨Ff, e_u⟩ = 0 for every u of the
layer. By parity, t_F ∈ [−a,0) suffices. Unitarity follows because the
τ^k u have disjoint supports.

(iii) By (ii), (1−ετ)K = K' ∩ (F^{−1}E)^⊥, and the orthogonal complement
within K' is Π_{K'}F^{−1}E. ∎

Hence, exactly,

    Son_S − Son_∞ = [⟨Π_{K'}⟩_h − ⟨Π⟩_h] − ⟨Π_D⟩_h.          (1.1)

---

## 2. Two-edge model (PROVED, all orders)

**Theorem 2.** K is replaced by L²[0,L] in t (support edge at 0,
"Fourier" edge at L) and K' by L²[0,L+a]. Let c be continuous and
bounded, and let M_c be convolution by c. Then, with Π_S the projection
onto (1−ετ)L²[0,L],

    Tr(M_c(Π_S − Π_{[0,L]})) = −2a Σ_{k≥1} ε^k Re c(ka) + O(a‖c‖_∞ ε^{2⌊L/a⌋}/(1−ε)²).

*Proof.* It is Thm 1 in the model: v ∈ L²[0,L+a] is orthogonal to the
image if and only if v(x) = εv(x+a) on [0,L]. Then v = Σ_{k≤⌊…⌋} ε^k
τ^{−k}u with u on the layer [L,L+a]. If the series were infinite (no
left edge), the orthonormal basis would be (1−ε²)^{1/2}Σε^kτ^{−k}u_j, and

    Tr(M_cΠ_D) = (1−ε²)Σ_{k,l≥0}ε^{k+l} a c((k−l)a) = a Σ_{n∈Z} ε^{|n|} c(na),

because Σ_{k−l=n} ε^{k+l} = ε^{|n|}/(1−ε²). The truncation at x = 0
changes the norm and the terms by O(ε^{2⌊L/a⌋}). Since
Tr(M_cΠ_{[0,L+a]}) − Tr(M_cΠ_{[0,L]}) = a c(0), it follows that

    Tr(M_c(Π_S − Π)) = a c(0) − a c(0) − 2aΣ_{k≥1}ε^k Re c(ka) + O(·). ∎

Check (control only, discrete): N = 400, shift d = 7, ε = 2^{−1/2}, c a
modulated Gaussian. Left side 3.013268195290493 versus right side
3.013268195290484.

**Corollary 2.1.** With c = c_h and a = log p, the model produces
*exactly*, at every k, the prime term
−2 log p Σ_k p^{−k/2} Re c_h(k log p): Λ(p^k) comes out of the defect's
length a multiplied by geometric weights. This improves R183_024's
Lemma 2.3 and Prop 2.4. The defect lives on the **Fourier** edge (the
right one); the support edge contributes nothing, consistent with
R183_024 §2.3.

**Corollary 2.2 (refutation of mechanism (CF-S) in the model).** In the
model, the diagonal density is ρ_∞ = L/2π (constant) and
2π(ρ_S − ρ_∞)(s) = −2a Σ_k ε^k cos(ksa). It is O(1) and independent of
L. Since L plays the role of local density ν(s) ~ log|s| (R183_021),
Christoffel's relative error is Θ(1/ν), not O(ν^{−2}). R183_021 §3.3's
heuristic omits exactly the boundary layer. **Heuristic (CF-S) is false
in the model;** R183_021 Thm 3.4 loses its heuristic support. (PROVED in
the model; see Cor 3.2 for the true Sonin space.)

---

## 3. True Sonin space: L1 conditional on one estimate

From Thm 1 and (1.1) two pieces remain.

**(Λ) Archimedean scaling law (CONDITIONAL, routine, no primes).** K'
is unitarily equivalent, by the dilation x ↦ p^{−1/2}x (which commutes
with ϑ), to S(λ,λ) with λ = p^{−1/2}. CC's Thm 4.7 proof, (85)–(90),
copied with the cutoffs P_λ, P̂_λ (local trace formula (43) with its term
2 log(1/λ)·f(1), CITED) gives

    ⟨Π_{K'}⟩_h − ⟨Π⟩_h = a·c_h(0) + ∫ c_h ε'_p,   ε'_p continuous.

(In the source only λ = 1 is written; in the model the piece equals
a c(0) exactly.)

**Let F^{−1}Π_E F be the projection onto F^{−1}E.** E lives on a
half-line (t_F ≥ −a, no left edge), and ϑ is transported by F into
ϑ(ǧ), which has the same c_h in real part. Thm 2's computation, now
**with no truncation error**, gives, PROVED:

    ⟨F^{−1}Π_E F⟩_h = a c_h(0) + 2a Σ_{k≥1} ε^k Re c_h(ka).

**Definition (edge-interaction density).** Define
R_edge := F^{−1}Π_E F − Π_D and

    ⟨R_edge⟩_h =: (1/2π)∫ |φ(s)|² r_p(s) ds.

R_edge = 0 if and only if F^{−1}E ⊂ K', i.e. if the support (|x| ≥ 1)
and the Fourier layer were independent. In the model, R_edge = O(ε^{2L/a}).

**Theorem 3 (PROVED as an identity; L1 CONDITIONAL).** Exactly,

    Son_S − Son_∞ = −2 log p Σ_{k≥1} p^{−k/2} Re c_h(k log p)
                    + ∫ c_h ε'_p + (1/2π)∫ |φ|² r_p.            (3.1)

Hence:

* under (Λ) and **(E′): r_p ∈ L²(R, ds)**, **L1′** holds, L1's form with
  δε_p := ε'_p + F^{−1}r_p ∈ L²(−2T,2T);
* under (Λ) and (E): r_p ∈ L¹, L1 holds as stated (δε_p continuous).

*Proof.* (3.1) is (1.1) plus the two pieces above. If r_p ∈ L², by
Plancherel ∫|φ|²r_p = ∫c_h·(F^{−1}r_p) with F^{−1}r_p ∈ L². If
r_p ∈ L¹, the transform is continuous. ∎

**Corollary 3.1 (consequence; CONDITIONAL on (Λ)+(E′)).** The form
R'_S(h) := E_S(h) − Son_S(h) = −∫c_h ε_S, with
ε_S = ε_∞ + δε_p ∈ L²(−2T,2T) (ε_∞ continuous, CC (83)), is a
Hilbert–Schmidt integral operator on L²(I_T), and hence compact. On the
family of R183_018 Thm 5.1, R'_S(x)/‖x‖² → 0 (R183_024 §2.4, with the
same bound and ‖·‖_{L²} instead of ‖·‖_∞ via Cauchy–Schwarz on
‖c_x‖_{L²} ≤ ‖x‖₁‖x‖₂ = O(√(Nw))‖x‖₂²). Thm 5.1's NO-GO does not apply
to Son_S + R'_S. n₋ below −δ is finite for every δ > 0.

**Corollary 3.2 (sharp dichotomy; PROVED given (Λ)).** R183_021's
(CF-S) (ρ_S − ρ_∞ → 0) is equivalent to

    r_p(s) = +2a Σ_{k≥1} ε^k cos(ksa) + o(1),

i.e. to the edge interaction **not** decaying, and exactly cancelling
the geometric layer's prime oscillation. Under (E′) (or with just
r_p → 0 on average), (CF-S) is false and R183_021 Thm 3.4 becomes vacuous.
The opposite conclusions of R183_021 and R183_024 are the two branches
of **a single number**: the behavior of r_p at infinity.

---

## 4. The missing estimate, (E′), and why it is expected

Write Γ := P_E F Π_{K'} F^{−1} P_E = 1 − Y on E, with
Y = P_E F(1−Π_{K'})F^{−1}P_E. Then Π_D is the projection onto
Π_{K'}F^{−1}E, with Gram Γ, and R_edge is linear in Y to first order.
1 − Π_{K'} is generated (CC §4) by S(λ,λ)'s prolates, i.e. by functions
concentrated on |x| < λ or in their transform. **Y contains no primes**:
it is the overlap between the geometric Fourier layer
(|y| ∈ p^{k}[1/p,1), weights ε^k) and the support condition on |x| < 1.
This makes (E′) a statement of archimedean harmonic analysis plus the
parameter a.

Heuristic (not a proof). In phase space (t,s), K is the band
0 ≤ t ≤ L(s), with L(s) := 2θ'(s) ~ log(|s|/2π). The model gives
interaction ε^{2L(s)/a} = e^{−L(s)} ≍ 1/|s|. Hence
r_p(s) = O(|s|^{−1}) ∈ L² \ L¹. If this is confirmed, (E′) and L1′ hold,
and L1 with continuous δε can fail only via a logarithmic singularity at
x = 0, harmless for all consequences.

Suggested proof route. Neumann-series expansion of Γ^{−1} in Y. One must
bound ‖P_{|s|∼S} Y P_{|s|∼S}‖_{S_1} ≲ S^{−1}·(width) using CC's
superexponential-decay bounds λ(n) (77)–(84), the same ones giving ε's
continuity in CC (84). A warning: Y is **not** globally trace class (the
k layers each contribute O(1) in Hilbert–Schmidt norm). One must work
with the weighted trace ⟨·⟩_h and localize in frequency, not in t.

---

## Status

| Statement | Label |
|---|---|
| θ_S^*θ_S = Π\|m\|²Π (compression), \|m\|² = 1−2ε cos(sa)+ε² | PROVED (from CITED (ms1)) |
| Thm 1: (1−ετ)K ⊂ K' = S(1,1/p), defect D = Π_{K'}F^{−1}E | PROVED |
| Thm 2: two-edge model, exact prime term at every k | PROVED (and numerical control) |
| Cor 2.2: (CF-S) heuristic false in the model | PROVED (model) |
| (Λ): CC Thm 4.7's scaling law on S(λ,λ) | CONDITIONAL (routine, no primes) |
| ⟨F^{−1}Π_EF⟩_h = a c_h(0) + 2aΣε^k Re c_h(ka) | PROVED |
| Identity (3.1) | PROVED (given (Λ)) |
| (E′): r_p ∈ L²(ds) | OPEN (the only substantive estimate) |
| L1′ (δε ∈ L²) / L1 (δε continuous) | CONDITIONAL on (Λ)+(E′) / (Λ)+(E) |
| Cor 3.1: Hilbert–Schmidt R'_S; R183_018 Thm 5.1 does not apply | CONDITIONAL on (Λ)+(E′) |
| Cor 3.2: (CF-S) ⟺ r_p cancels the prime oscillation | PROVED (given (Λ)) |
| R183_021 Thm 3.4 (semilocal Sonin NO-GO) | remains CONDITIONAL on (CF-S); no heuristic support |
| Positivity / N_T / row D | OPEN; not claimed |

What remains: (1) prove (E′) (§4); (2) write (Λ) with the source; (3)
even with L1, the route only reaches C_T = I_S ∧ N_T of R183_024. N_T,
the compact remainder's inertia, carries all the arithmetic content and
is not touched here. L1 removes one NO-GO; it adds no positivity.
R162_2602 Thm 4 deals with the cutoff carrier R_Λ, not Π_S, and does not
conflict.

## Review points

1. **2π normalization / signs.** In (3.1) the prime term's sign is fixed
   by Thm 2 and the numerical control. It should be checked against
   R183_018 §3's normalization of E_S: c_h(x) = ∫h(t)\overline{h(t−x)}dt
   and ⟨X⟩_h = ∫∫X(x,y)c_h(y−x).
2. **Thm 1(ii).** Check the direction of translation on the Fourier side
   (Fτ = τ^{−1}F in the unitary normalization) and that the layer is
   t_F ∈ [−a,0) and not (0,a]. If it were the other, E would fall within
   the forbidden support and the defect would be empty, contradicting
   (1−ετ)K ≠ K' (infinite codimension).
3. **(Λ)** is assumed from the structure of CC's proof, which is only
   written for λ = 1. If the scaling term is not exactly a·c_h(0), (3.1)
   changes by a multiple of c_h(0), which is local and does not affect
   the prime atoms.
4. **(E′) versus (E).** L1 as stated requires continuous δε. Here it is
   proved that δε ∈ L² suffices for all consequences (Hilbert–Schmidt).
   §4's heuristic suggests r_p ≍ 1/|s|, in L² but not L¹. Check that in
   Cor 3.1 the bound on the pair family uses ‖c_x‖_{L²}, not ‖c_x‖_∞.
5. **The trace** ⟨Π_S⟩_h is finite and difference (1.1) is well defined:
   all projections are compressed by C, and C Π C^* is trace class
   because Π_K is so locally (CC Thm 4.7). The subtractions in (1.1) are
   done between finite quantities.
6. **No circularity with zeros.** Neither Y, E, nor K' involve ζ, only p
   and archimedean prolates.
