# Q2_LADDER_001: Q2 candidate ("ladder" μ → μ/p), Lemma Q2.1 for p = 2 (phase 200, round 2)

There are only exact integer checks and a pointwise evaluation of Mori's μ = 15 data
(NUMERICAL, mpmath).

**Verdict: Q2 is NO-GO (PROVED, given Guo L4.4).**
- The "ladder positivity" 𝒲[Ψ̌^{[μ]} − Ψ̌^{[μ/2]}] is **identically zero** for every g of the core with A(g) = 0.
- The level Gram matrix is constant: 𝔊_{YY′} ≡ W_T(g).
- The "step 2" (the even-index sublattice) is **radical**. Its contribution to W_T is exactly 0, not −0.481 W*.
- By the death criterion of the spec itself (§Q2.5), Q2 dies.
- It does not die from C6. It dies from tautology: it is REF-D in the sense of P10 of AUDIT_200_SPEC_002, because
  everything reduces to 𝒲[g].

---

## 0. Readings, corpus and index

**Read:**
- SPEC_SIGN_OBJECT_002 complete (T.1, T.2, T.3, the c_{pN} rule, Q2, Lemma Q2.1, P1–P9), AUDIT_200_SPEC_001 and
  K1_OSG_001 (R-K1).
- PROOF_L_SHARP_FF_001 (FF.1), GG_001 (GG.0, GG.1, §2, §4) and MORI15_EXTREMAL_001 together with its data
  p0_eig.json.
- AUDIT_L_SHARP_16 §6: resonances (1, n) = −0.48/−0.30/−0.20 W*.
- Paper 46: def:ext, thm:ext-half, rem:ext-killing, prop:ext-gauge.
- ROUTES-TRIED index, "Phase 200" section, and the entries E_001, F_001, J_001, INV_H_001 and INV_J.

**Clash with the index (declared).** The index entry for **AUDIT_200_SPEC_002** (audit of this same round,
published in parallel) already records: "Q2 ladder NO-GO (𝔊_{YY′} ≡ W_T(g); mollifier difference radical,
𝒲 = 0)."
- This memo **does not retry** that route. It does the construction work the spec asked for: stating Q2.1
  exactly.
- The result agrees with the audit and confirms it independently.
- It adds what the audit lacks:
  - (a) The correct ladder rule. The spec's is misstated.
  - (b) The class-p subcomb is radical for every prime p, not only the level difference.
  - (c) The μ = 15 test solved exactly: step 2 = 0.
  - (d) The NUMERICAL amplitude of the difference at g*.
  - (e) The rough-comb representation, as a new restriction.
- E_001, F_001 and J_001 (ratio classes before cancellation) and INV_H (regrouped Möbius) are not retried. Here
  class 2 is read on c_N, and the result is that this reading has no content: it is radical.

**Notation** (SPEC_002):
- μ ≥ 5, a = T = ½log μ, g even in the core (C² on [−a, a] and vanishing to second order at ±a),
  A(g) = ∫g e^{x/2} = B(g).
- c^{(Y)}_N = Σ_{d|N, d<Y} μ(d) and c_N = c^{(μ)}_N.
- For a finite Dirichlet polynomial P(s) = Σ_d p_d d^{−s} write P(∂)h := Σ_d p_d d^{−½}τ_{log d}h, with
  τ_s h = h(· − s).
- ζ(∂)g := Σ_{N≥1} N^{−½}τ_{log N}g. It is locally finite, because g has compact support.
- Ψ̌^{[Y]} := Σ_{N≥Y} c^{(Y)}_N N^{−½}τ_{log N}g.

---

## 1. Tool: every comb ζP(∂)g is radical (Lemma R; PROVED, given Guo L4.4)

**Lemma R.** Let g be in the core with A(g) = 0, and let P be a finite Dirichlet polynomial. Then
R_P := (ζP)(∂)g satisfies |R_P(y)| ≤ C e^{−3y/2} for large y, and moreover 𝒲(R_P, X) = 0 for every X of the
def:ext class (the complete Weil form on the line, with its polar term).

*Proof.*

1. **(Summation map.)** Set F(t) := t^{−½}g(−log t) for t > 0, extended evenly. Then
   ζ(∂)g(y) = e^{−y/2}Σ_{N≥1}F(Ne^{−y}) = Φ_F(−y), with Φ_F the summation map of def:ext.
   - F has support in [e^{−a}, e^{a}] and F(0) = 0.
   - 𝓕F(0) = 2∫_0^∞F = 2∫g(s)e^{−s/2}ds = 2B(g) = 0.
   - F is C², because g vanishes to second order at ±a.
   - Hence F satisfies the hypotheses of Guo's radical lemma (L4.4), the same ones prop:ext-gauge uses for
     φ ∈ 𝒢_T, and Φ_F is radical. **CITED + PROVED.**
2. **(Decay.)** By Poisson, Σ_N h(N) = ∫h + Σ_{k≠0}ĥ(k), with h(t) = t^{−½}g(y − log t).
   - ∫h = e^{y/2}A(g) = 0.
   - Two integrations by parts in ĥ(k) = e^{y/2}∫g(s)e^{−s/2}e^{−2πike^{y−s}}ds give
     |ĥ(k)| ≲ e^{y/2}e^{−2y}k^{−2}.
   - Hence ζ(∂)g = O(e^{−3y/2}). **PROVED.**
3. **(Shifts.)** 𝒲 is translation invariant: c_Ψ, the m term and the product
   A(τ_sΨ)B(τ_sΦ) = A(Ψ)B(Φ) do not change. Hence τ_{log d}ζ(∂)g is radical, and
   R_P = Σ_d p_d d^{−½}τ_{log d}ζ(∂)g is too, by linearity. □

**Immediate consequence.** For every Y ≥ 2 one has Ψ̌^{[Y]} = R_{M_Y} − g, because c^{(Y)}_1 = 1 and
c^{(Y)}_N = 0 on [2, Y). Then:

 **𝔊_{YY′} := 𝒲(Ψ̌^{[Y]}, Ψ̌^{[Y′]}) = 𝒲[g] = W_T(g)  for every Y, Y′ ≥ 2 (also Y > μ).**  (PROVED)

For Y = 2 (M_2 = 1) this is the Guo identity with a_n ≡ 1. The level μ only serves to keep the datum
**exterior** (support at y > T), which is what gives meaning to the leak ℓ and to P2. **The level contributes
nothing to the value of 𝒲.**

For A(g) ≠ 0 the rank-one rows of GG.0 are added. This changes nothing that follows in the A = 0 sector, which is
that of T.1.

---

## 2. Task 1: the exact Lemma Q2.1 for p = 2

### 2.1 The correct ladder rule

The spec states: "the projection of 𝒟_pΨ̌^{[μ]} onto p ∤ N is Ψ̌^{[μ]} − Ψ̌^{[μ/p]}." **This is not exact.** The
correct form is as follows.

**Lemma Q2.1(a) (Euler factorization of the mollifier; PROVED).**
 M_μ(s) = M^{o}_μ(s) − 2^{−s}M^{o}_{μ/2}(s),  where M^{o}_Y(s) := Σ_{d<Y, d odd} μ(d)d^{−s}.

*Proof.* Squarefree even d are d = 2d′ with d′ odd, and μ(2d′) = −μ(d′); also d < μ ⟺ d′ < μ/2. □

**Lemma Q2.1(b) (coefficient rule; PROVED).** For every M ≥ 1:
- c_{2M} = c_M − [2 ∤ M]·c^{(μ/2)}_M. For M even, c_{2M} = c_M, because 2N and N have the same squarefree
  divisors.
- In closed form, c_{2M} = Σ_{d|M, d odd, μ/2 ≤ d < μ} μ(d).

*Proof of the closed form.*
1. Let O_Y(s) be the odd part of ζM_Y. Then O_Y(s) = (1 − 2^{−s})ζ(s)M^o_Y(s).
2. By (a), the even part of ζM_μ is ζM_μ − O_μ = 2^{−s}ζ(s)[M^o_μ(s) − M^o_{μ/2}(s)].
3. Read off the coefficient. □

Exact check: 0 failures for 5 ≤ μ < 60 and M < 3000 (integer arithmetic).

At μ = 15, the odd band [7.5, 15) is {11, 13}, so c_{2M} = −[11 | M] − [13 | M]:
- c_22 = c_26 = c_44 = c_66 = c_78 = −1;
- c_30 = 0;
- c_286 = −2.

This reproduces the pairs of K1 and the spec's data.

**Lemma Q2.1(c) (functional ladder; PROVED).** Let Ψ̌_{ev} be the part of Ψ̌^{[μ]} with N even, and
𝒟_2Ψ := 2^{½}Ψ(· + log 2). Then
 𝒟_2Ψ̌_{ev} = Σ_{M≥1} c_{2M}M^{−½}τ_{log M}g = R_{Q_2} = Ψ̌^{[μ]} − Ψ̌^{[μ/2]}_{odd},
with Q_2(s) := Σ_{d odd, μ/2≤d<μ} μ(d)d^{−s} (the odd-band polynomial) and
Ψ̌^{[μ/2]}_{odd} := Σ_{N odd ≥ μ/2} c^{(μ/2)}_N N^{−½}τ_{log N}g.
- The equality is pointwise: each side is a locally finite sum.
- The N = 1 term cancels between g + Ψ̌^{[μ]} and g + Ψ̌^{[μ/2]}_{odd}.
- **Correction to the spec:**
  - level μ/2 enters only with N **odd**;
  - it enters **with the boundary** N ∈ [μ/2, μ);
  - on that boundary c^{(μ/2)}_N = −μ(N) (PROVED: the proper divisors of N < μ are ≤ N/2 < μ/2, and
    Σ_{d|N}μ(d) = 0).

### 2.2 The ladder identity for W_T (quadratic form)

**Theorem Q2.1 (PROVED, given Guo L4.4).** For g in the core with A(g) = 0:
1. Ψ̌_{ev} = 2^{−½}τ_{log 2}R_{Q_2} is **radical**: 𝒲(Ψ̌_{ev}, X) = 0 for every admissible X.
2. Hence W_T(g) = 𝒲[Ψ̌^{[μ]}] = 𝒲[Ψ̌_{od}]. In other words: **the complete step 2 (diagonal plus even–odd
   cross term) contributes exactly 0.**
3. For every prime p, the subcomb Ψ̌_{p|N} is 𝒟_p^{−1}R_{Q_p}, with Q_p := Σ_{p∤d, μ/p≤d<μ} μ(d)d^{−s}, and is
   radical. If p ≥ μ, Q_p contains d = 1, and it is still radical by Lemma R.
4. For every finite set S of primes, W_T(g) = 𝒲[Ψ̌_{S-coprime}].
   - For S ⊇ {p < μ} the mollifier coprime with S is 1, and one gets
     **W_T(g) = 𝒲[Σ_{N>1, P⁻(N)≥μ} N^{−½}τ_{log N}g]**: a 0/1-coefficient comb over the μ-rough integers.
   - It is an Eratosthenes sieve inside the radical (PROVED).

*Proof.*
- (1): Lemma R applied to Q_2, plus translation invariance.
- (2): bilinearity.
- (3): the same computation for the p-divisible part, ζ(M^{(p∤)}_μ − M^{(p∤)}_{μ/p}).
- (4): the generating function of the S-coprime part is Π_{p∈S}(1 − p^{−s})·ζ·M^{S}_μ, which is ζ times a
  finite polynomial, minus 1. □

**Status of each step.**

| Step | Label |
|---|---|
| Rule (a), (b) and its closed form | PROVED |
| Functional ladder (c) | PROVED |
| e^{−3y/2} decay of the subcomb | PROVED (Poisson + 2 IBP) |
| Radicality | CITED (Guo L4.4), by the same route as prop:ext-gauge |
| Theorem Q2.1 (1)–(4) | PROVED given L4.4 |
| "Ladder identity" target of the spec: W = Σ_p v_p p^{−½}(𝔊_{μμ} − 𝔊_{μ,μ/p})·… | **degenerates**: each 𝔊_{μμ} − 𝔊_{μ,μ/p} = 0, so the identity has no content |

---

## 3. Task 2: the nature of the radicality defect

The spec feared the following: radicality at level μ/2 fails, because g of level μ exceeds the level-μ/2
window, leaving an O(1) edge of type C6. **It is not so: the radicality defect is exactly 0** (Lemma R).
- Radicality of the comb ζP(∂)g **does not depend on the support of g relative to any window**. It only uses
  A(g) = 0 and g being C².
- What fails at level μ/2 is **exteriority**: the shifts with N ∈ [μ/2, μ) fall into (a − log 2, …) and
  overlap the window.
- Exteriority does not enter the value of 𝒲. It enters the reading of the datum as an aliasing tail of an
  admissible f at level μ/2 and in its leak.

**Answer to the binary question.**
- It is an exact identity: the boundary is −Σ_{N∈[μ/2,μ)} μ(N)N^{−½}τ_{log N}g, and it collapses by
  Σ_{d|N}μ(d) = [N = 1] in the step c^{(μ/2)}_N = −μ(N).
- No Möbius correlation bound is needed. Q2 **is not C6**.

Precisely because it is exact, the identity has no content:
- The boundary is part of R_{M_μ} − R_{M_{μ/2}}, which is radical.
- The level-μ/2 energy of the same g **is not** W_{T−½log 2} of any admissible datum. It is again
  𝒲[g] = W_T(g).
- The spec's "induction in μ" compares W_T(g) with itself.

There is an alternative reading: take at level μ/2 a different admissible g′, with support in
(−a + ½log 2, a − ½log 2).
- Then there is no identity linking g with g′. Q2.1(c) uses the **same** g at both levels: the c_{pN} rule is
  an identity between coefficients, not between windows.
- Linking g with g′ requires a window-restriction operator. That is another route, not Q2, and is close to the
  T-flow routes (H_001 and restriction 11). It is not attempted here.

---

## 4. Task 3: the 𝒫 of Q2

𝒫_2 := 𝒲[Ψ̌^{[μ]} − Ψ̌^{[μ/2]}].
- The difference is Σ_{N≥μ/2}(c^{(μ)}_N − c^{(μ/2)}_N)N^{−½}τ_{log N}g = R_{M_μ − M_{μ/2}}.
- It has no N = 1 term, because the band starts at d ≥ μ/2 > 1.

**Is it a genuine square?**
- It is a Weil square of a radical vector: **𝒫_2 ≡ 0 (PROVED, given L4.4)**.
- There is no positivity to extract: the spec's "post-cancellation square" is zero.
- The Erdős-band intuition (N with a divisor in [μ/2, μ)) is correct about the coefficients, but the
  arithmetic support gets absorbed into the ζ factor: R = ζ·(band polynomial).

**P2 (leak scale)?**
- As a function, the difference is **not** post-cancellation. NUMERICAL at Mori's g*, μ = 15 (p0_eig.json,
  mpmath dps 50):
  - at y = a + 0.7 and a + 1.5 it equals −0.117 and −0.125;
  - with |g*(0)| = 1.598, its order is 10^{−1}‖g‖;
  - ℓ*^{½} ≈ (2.1–2.9)·10^{−35}.
- The amplitude violates P2 by 34 orders of magnitude, and yet 𝒲 = 0. It is the 70-digit cancellation of
  restriction 25, seen from the radical.

**P1 (gauge)?**
- 𝒫_2 is trivially gauge invariant, because it is 0.
- The piece the spec wanted, 𝔊_{μμ} − 𝔊_{μ,μ/p}, is too.

**P3 and P6 (false in the identity for cΛ with c < 1, Beurling, DH and a_P)?**
- cΛ with c < 1 and Beurling: there is no radical ζP(∂), so Lemma R does not exist and the ladder is not
  defined. The failure is in the identity, as P3(b) requires.
- DH: the inverse coefficients are not multiplicative, so the Q2.1(b) rule fails.
- a_P: shares FF.1 (GG §4), and so also shares Lemma R, with ζ_P in place of ζ.
- This does not rescue Q2: in every system where the object is defined it equals 0, so there is nothing to
  separate. In the language of AUDIT_200_SPEC_002, P10 directly gives "it reduces to 𝒲[g]," and that is
  NO-GO.

---

## 5. Task 4: Lemma M and the ladder

Lemma M (PROVED, AUDIT_198) says that, for a fixed comb, T ↦ λ_A(T) is non-increasing. Certified negativity
propagates **upward in T**. Positivity propagates **downward**.

- **Direction.** The spec's output is "W_T ≥ (count) × (leak), by induction in μ, from μ/2 to μ," i.e. from
  T − ½log 2 to T: going up in T. Lemma M transports positivity only in the opposite direction (from T to
  T′ < T). An ascending induction would need the converse of Lemma M, which is false in general (the certified
  falsifiers are negative above and positive below).
- **The ladder does not contradict Lemma M.** It does not compare λ_A(T) with λ_A(T − ½log 2): for fixed g it
  gives 𝔊_{μ/2,μ/2} = 𝔊_{μμ}.
  - That is not a bound on W_{T′} by W_T. It is the same quantity.
  - An inequality W_μ ≤ W_{μ/2} in the wrong direction does not appear: the trivial equality appears instead.
- **Conclusion.** The ladder is compatible with Lemma M and transports nothing. It is not a flow in T
  (restriction 11 intact) nor does it give a relation between infima at different T.

---

## 6. Task 5: the μ = 15 test

**Design (per the spec).**
- (i) Amplitude of Ψ̌^{[15]} − Ψ̌^{[7.5]} at g* against ℓ*^{½}.
- (ii) Contribution of step 2 against the resonance (1, 2) = −0.481 W* (AUDIT_16 §6), with a death criterion
  outside the factor-2 range.

**Result of (ii): EXACT, without numerics (PROVED given L4.4).**
- Step 2 := 𝒲[Ψ̌_{ev}] + 2𝒲(Ψ̌_{od}, Ψ̌_{ev}) = 0, by Theorem Q2.1(1).
- 0 is not within the factor-2 range of −0.481 W*, so **Q2 dies by its own criterion**.
- This does not contradict the −0.481 of AUDIT_16. That resonance is the 𝒲_ext coupling between the prolate
  tail m = 1 and the Möbius-cell content in the **dilation** basis (n = 2 as a dilation of r). It is not the
  even-index subcomb of c_N.
- The two "class 2" objects are different. Q2's is radical; AUDIT_16's is not. Identifying them was Q2's bet,
  and it is false.

**Result of (i): NUMERICAL** (p0_eig.json; g* Legendre of degree ≤ 1662; script in the scratchpad, not in the
repo).

| y | mollifier difference | even subcomb Ψ̌_ev |
|---|---|---|
| a − 0.3 | −3.1e−19 | 0 |
| a + 0.1 | −8.3e−6 | 0 |
| a + 0.7 | −0.1169 | 4.9e−10 |
| a + 1.5 | −0.1253 | 0.2452 |

- Comparison scale: ℓ*^{½} ≈ 2.5e−35. The amplitude is O(10^{−1}).
- The datum is not post-cancellation (fails P2) and its 𝒲 equals 0.
- Ψ̌_ev is O(10^{−1}) starting from y ≈ log 22 − a ≈ a + 0.39 (first nonzero even shift, N = 22). Its energy is
  also 0.
- 𝒲[Ψ̌_ev] = 0 was not evaluated numerically, because it requires the full form at 70 digits. It is an exact
  corollary of a cited lemma, not a conjecture, and the numerics are not strictly necessary.

---

## 7. Final

**Label for Q2: NO-GO (PROVED, given Guo L4.4).**
- Tautological: 𝔊 ≡ W_T(g)·𝟙𝟙ᵀ, 𝒫_2 ≡ 0, step 2 ≡ 0.
- It is not C6: the boundary defect is an exact identity.
- Its method class is "level or class coordinates inside the radical ζ·(finite polynomial)," which reduces to
  𝒲[g] (P10).
- Agrees with AUDIT_200_SPEC_002's verdict on Q2.

**New restriction (R-Q2).**
- For every g of the core with A(g) = 0 and every finite Dirichlet polynomial P, (ζP)(∂)g is radical.
- Consequently, **no object built with arithmetic restrictions on the shift indices** has sign content, as long
  as those restrictions have generating function ζ·(finite polynomial). This includes:
  - mollifier levels;
  - class-p subcombs (p | N);
  - S-coprime parts;
  - divisor bands in [μ/p, μ).
- Only the representative of the coset g + radical changes. Example:
  W_T(g) = 𝒲[0/1 comb over the N > 1 μ-rough integers].
- Any P9 candidate must leave this class, for example with non-periodic weights in N or with zero-density
  restrictions not expressible as ζ·(finite polynomial). If it does not, it is NO-GO without building it.

**Entry for the index:**
> - **Q2_LADDER_001 (phase 200; ladder μ → μ/p): NO-GO (PROVED given Guo L4.4), agrees with
>   AUDIT_200_SPEC_002.** Exact rule: M_μ = M^o_μ − 2^{−s}M^o_{μ/2}, c_{2M} = Σ_{d|M, d odd, μ/2≤d<μ}μ(d) (the
>   spec's version, without "odd" or the boundary, was inexact). Lemma R: (ζP)(∂)g is radical ∀P finite
>   (A(g) = 0) ⇒ 𝔊_{YY′} ≡ W_T(g), 𝒲[Ψ̌^{[μ]} − Ψ̌^{[μ/2]}] = 0, subcomb p | N radical ∀p, step 2 = 0 ≠
>   −0.481 W*. Exact boundary defect (not C6). Restriction R-Q2: levels, classes p, S-coprime parts and
>   divisor bands are coordinates inside the radical; W_T(g) = 𝒲[μ-rough 0/1 comb]. Do not retry ladders or
>   level inductions with the same g. Row D OPEN.

**Remains OPEN:**
- (1) A bridge between different windows (g at level μ, g′ at level μ/2) by restriction. It is not Q2, and is
  close to H_001 and restriction 11.
- (2) Whether the 0/1 μ-rough comb (positive, without Möbius) works as a coordinate for some object other than
  Toeplitz. As a datum it is not exterior (N ≥ μ, but it is not the aliasing tail of f) nor post-cancellation,
  so it violates P2 as is.
- (3) Q3 and the rest of the program. Row D: OPEN. L′♯: OPEN. No sign is claimed.
