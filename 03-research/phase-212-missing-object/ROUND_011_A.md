# Round 11, A: the open residues of (PC) and the one-sided lattice discrepancy

Notation of the common brief. τ_aF(t) = F(t+a); S_N = Σ_{n≤N} n^{−1/2}τ_{log n}; C_N(D) its polar continuum,
(C_N(D)g)(t) = e^{−t/2}∫_{−∞}^{t+log N} e^{y/2}g(y)dy; S_N^ren = S_N − C_N(D); P = P_T; A = A_M the operator of the
form; ℓ_T(F) = (1−P)AF the exterior leakage; 𝓕 the transported additive transform.

**Result.** No candidate passes the gate. The mechanism of signed lattice discrepancy (integral test,
Hermite–Hadamard, first Euler–Maclaurin remainder) dies against L161.3 for two reasons. (a) The remainder Δ^R ℓ_T(F) is
linear in F, and a uniform sign of an odd linear functional is only possible if the functional is identically zero.
(b) The sampling comb has unit weights n^{−1/2}: the Euler–Maclaurin sign does not see Λ and is the same for cΛ,
for deletion and for Beurling. The exchange log n = ∫dx/x via Λ∗1 = log falls back onto the scalar Stieltjes
primitive (R161_004 Cor. 2.1; Paper 41 C4–C5) and onto the signed Bernoulli remainder (106_109 (9)–(10)). Both are
closed.

## 0. Step 0: the four residues, in primary sources

I read R161_004, 005, 006, 020 and 023 in full. Of R161_015, 016, 021, 022, 029, 038, 041 and 050 I read the statement
and status sections. I also read R163_153 and R170_853 §§4–5, RULES_AVOID K, L and T, and ANNEX_161_FILES_1 §(c)
and _2 (038, 050).

### 0.1 L161.3 / PC-port (R161_004 §6, R161_005 §5, R161_006)

- **Open statement.** Let F be a primitive first-contact state: PAPF = r = αe^{−t/2} + βe^{t/2}. The port
  B^ren_{N,T}(F) = PS_N^ren(1−P)AF, in its oriented limit and before any trace, would have to have a non-zero critical normal
  symbol. Moreover, the equality equation together with Tate cancellation would have to annihilate it
  (R161_005 §5).
- **PROVED around it.**
  - (005 Thm. 1.1) PR_{M,N}𝓕F = PS_N r + B_{N,T}(F).
  - (006 Thm. 2.1) B^ren(F)(t) = Δ^R_{N,T}ℓ_T(F)(t) − e^{−t/2}a_−(ℓ_T(F)), with
    Δ^R_{N,T}g(t) = Σ_{e^{T−t}<n≤N} n^{−1/2}g(t+log n) − e^{−t/2}∫_T^{t+log N}e^{y/2}g(y)dy,
    and the corresponding reflection for Δ^L.
  - Chamber 0.8 < T < ½log5: Z_{T,−}^{−1} = I − K + K² (005 §4).
- **Why it stopped.** The square ‖B‖² loses the orientation (005 §2). The scalar trace falls back onto Paper 41 C5
  (004 §2). Bringing it to a divisor history falls back onto the CMO no-go of phase 121 (004 §3).
- **Later memos.** R161_028–029: the polar layer is the exterior image. The norm of the moving discrepancy
  N_f(a) = ‖Z_af‖² has indefinite derivative (2.2) and jumps (3.2); ordinary monotonicity is **FALSE** (029 §7).
  The remaining sign is identified with the inverse Markov gate of R161_016. Closed in the class
  «monotonicity of the discrepancy norm» by a numerical falsifier (script 161_02). The oriented version
  remains OPEN.
- **Checks.** Δ^R has unit weights and contains no Λ. The weights only enter through g = ℓ_T(F). With cΛ and with
  deletion of a prime power g changes and the operator Δ^R stays the same. Beurling changes the lattice of the comb
  (R161_001 Thm. 4.1: the integer Poisson datum is missing).

### 0.2 L161.4 (R161_020 §5)

- **Open statement.** Build V_{M,N,T}F from (PC-ren), inherited from the zeta product and the crossed Tate terms
  and without defining it from L^sc, such that lim‖H_T^−E_N^ren V F‖² = L_T^sc(F) := ‖(I−P_+)C_log g‖².
  The finite first-contact identity would have to annihilate the left-hand side.
- **PROVED around it.**
  - Unitary compression rigidity (Lemma 1.1).
  - Leakage square (0.2).
  - Error (3.4).
  - Hardy form (4.3).
  - Closure by the Gamma pole lattice (R161_019).
- **Why it stopped.** E_N^ren → 0 strongly, so every bounded linear limit kills both sides
  (R161_016 §3 proves it in the class of bounded strong limits). A non-circular V is missing.
- **Later.** K1 of RULES_AVOID: «the leakage squares are correct, but there is no identity connecting them
  with the PC defect». There is neither a no-go nor a falsifier. Remains OPEN.
- **Checks.** L^sc contains no arithmetic weights; only C_log and the support. The arithmetic datum would have to enter
  through V, and therefore the checks cannot be evaluated until V exists.

### 0.3 L161.5–L161.6 (R161_021 §5, R161_022 §4, R161_023 §5)

- **Open statement.** Find an antisymmetric boundary law, obtained from (PC-ren) in two orientations before
  recombining, that drives Re⟨g_N, S_N^ren w_N⟩ → 0. It must distinguish ⟨g_N, S w_N⟩ from ⟨S*g_N, w_N⟩ through the
  moving boundary and cannot follow from a_T(F,H) = 0 for H primitive.
- **PROVED around it.**
  - Criterion X_T(F) = 0 ⇔ C_log g = −εg ⇒ F = 0 (021, 023 (5.1)).
  - Tate projection ⟨r, ΤPy⟩ = ⟨Sr, g⟩ (023 (1.3)).
- **Why it stopped.** The canonical test Π_TP_TZ*g recombines tautologically in (PC-ren). Using the cross matrix
  as a Gram is REJECTED.
- **Later.**
  - R163_153: for a right-supported port, the test is exactly 0 for all N. It is a support and polarity no-go
    valid for any comb with unit weights.
  - R170_853 §4: imposing z_F = 0 repeats L161.6.
  - Index 04, G1C-R161_022-023: REF-D.
- **Checks.** The collapse of R163_153 does not use Λ, so it is blind to the three checks. The sought law does not
  exist yet.

### 0.4 Port minimum / inverse pullback (R161_015 §4, R161_016 §2)

- **Open statement.** On the first-contact radical, N_T(δ) − N_T(0) = ‖D_{EΓ,δ}E^phys_{T,δ}F‖² + R with
  liminf R/δ ≥ 0, built from the sources (016 (2.2)).
- **PROVED around it.**
  - Norm slope −2∫(t−T)|g|² (015 Thm. 3.1).
  - Equivalence with the last upper bound (015).
  - Conditional closure criterion (016 Thm. 2.1).
  - The direct Markov pullback gives the automatic arrow (016 Prop. 1.1).
  - The finite datum 2, 3, 4 controls only the first collar (016 §5).
- **Why it stopped.** A zero-order scattering that inverts input and output is needed, and E_N^ren cannot
  be one.
- **Later.** R161_029 identifies L161.11 with this gate. R161_038 and R161_050 close the formal class
  (involutions + linear (PC) + radicality + parity) by 2×2 and 3×3 countermodels. Remains OPEN outside that
  class.
- **Checks.** Not evaluated.

The four residues are formulated on the radical of a supposed first contact. None is an identity
on all of P_T (warning of ANNEX_161_FILES_1 §(c)).

## 1. Step 1: the lattice discrepancy on L161.3

**(i) The function φ.** In Δ^R I make the change y = t + log x. It becomes
Δ^R g(t) = Σ_{e^{T−t}<n≤N} φ_t(n) − ∫_{e^{T−t}}^{N} φ_t(x)dx, with φ_t(x) = x^{−1/2} g(t + log x) and g = ℓ_T(F).
It is exactly a one-sided lattice discrepancy with moving lower endpoint e^{T−t} (PROVED, direct computation).
φ_t is neither a square nor a product: it is **linear** in F.

**(ii) Monotone or convex ordering for all F.**

- **Lemma 1 (PROVED).** Suppose there is a sign rule σΔ^R ℓ_T(F)(t) ≥ 0 valid for all F in P_T, or
  for all F in a cone containing −F together with F. Then Δ^R ℓ_T(F)(t) = 0.
  *Proof.* The functional is linear and odd. ∎
- To obtain a useful sign one must pass to a quadratic form ⟨h(F), Δ^R ℓ_T F⟩. The resulting summand is
  bilinear, φ_t(n)·(datum of h), and has no uniform monotonicity. Monotonicity of x ↦ x^{−1/2}g(t+log x) on (e^{T−t}, N)
  requires g to be essentially monotone on (T, ∞). The exterior image of A on P_T is not a cone of monotone
  functions (ARGUED: it contains ℓ_T(F) and −ℓ_T(F)).
- **Lemma 2 (PROVED).** Δ^R depends only on the lattice ℤ_{≥1} and the weights n^{−1/2}; it contains no Λ. Hence,
  any sign coming from monotonicity or convexity of φ_t (integral test, Hermite–Hadamard, first Euler–Maclaurin
  remainder with signed B_1) is preserved unchanged for cΛ with c = 2 and for deletion of a prime
  power, because these only modify g. By discipline R3-i, such a sign does not break under two of the three checks.
- **Exchange via Λ∗1 = log.** The inequality log n ≤ Σ_{m<n}1/m (signed error γ + O(1/n)) is a scalar
  statement. Introducing it into Δ^R forces scalarizing the divisor fibre before the port. That is exactly the
  closed class of R161_004 Cor. 2.1: Stieltjes primitive of Paper 41 (3.10), completion C5 with negative square
  and negative interval below log 2. What does break under cΛ is the defect δ_a(k) = Σ_{d|k}a(d) − log k
  (R161_001 Thm. 4.1). That defect is linear in the weight and is not a monotone discrepancy (U1 of ANNEX_161: Λ∗1
  enters only linearly).

**(iii) Cross-check with what is closed.**

- **106_109 §2 (9)–(10), §§5, 8–9.** Gaussian summation by parts leaves a signed Bernoulli remainder whose kernel
  changes sign in each lattice cell. The Euler–Maclaurin sign is already identified and does not transport.
- **POWER_GRAM_SLICES §§8–8.3.** Theta prefixes, the continuous tail and symmetrization do not restore PSD. The
  discrepancy «integers minus continuum» of a theta function belongs to that family.
- **R161_004.** Scalar Stieltjes successors and positive divisor fibres are closed. R161_041 does not
  add a sign: the derivative of E gives U+V and that of C gives U−V.
- **R161_029.** The natural quadratic version, N_f(a) = ‖Z_af‖², has indefinite derivative and jumps, and monotonicity
  is FALSE. This is precisely the «signed lattice discrepancy» applied to the object of the residue: already
  proved and falsified.
- **R161_038 and R161_050.** The countermodels have neither a semigroup of integer translations nor an Euler–Maclaurin
  continuum (038 states it under «Does not model»), so no lattice sign is available in them. This indicates
  that the mechanism lies **outside** their class. But it does not give it content: Lemmas 1 and 2 kill it by linearity and
  by blindness to the weight, independently of those countermodels.

**Net difference: none.** I stop before deriving.

## 2. Step 2: no candidate survives

| Residue | Class that closes it, or missing operation |
|---|---|
| L161.3 | Monotonicity of the moving discrepancy norm is FALSE (029). The linear lattice sign is trivial (Lemma 1) and blind to the weight (Lemma 2). Scalarization is closed (004). Missing: an **oriented** pairing of two orientations whose cross term has the sign of D^Poisson ≥ 0 (029 (6.1)). |
| L161.4 | No no-go. Missing: a non-circular V_{M,N,T}, with projected (not strong) graph convergence, carrying the arithmetic datum. |
| L161.5–6 | The direct conjugate test is tautological (023) and is identically 0 for a right port (R163_153). Missing: a boundary concomitant law that is not a consequence of radicality, inserting 𝓕 before the adjunction. |
| Port minimum | The formal class is closed (038, 050) and the direct pullback gives the automatic arrow (016). Missing: a zero-order scattering that inverts input and output. It is the same gate as L161.11. |

**Order.** I would put **L161.4** first. It is the only residue whose target is an equality between two squares already
PROVED ≥ 0, and nothing in the corpus closes it: neither no-go nor falsifier, only «V is missing». The other three collapse, in
later memos, into one and the same gate: the oriented cross term of 029 (6.1) and 016 (2.2). L161.4 has two
caveats. It inherits the dependence on the radical. And the link (4) with global positivity on all of P_T is not
written anywhere, so it would have to be added before any construction.

## Claims and labels

1. Δ^R ℓ_T(F)(t) = Σ φ_t(n) − ∫φ_t, with φ_t(x) = x^{−1/2}ℓ_T(F)(t+log x) and lower endpoint e^{T−t}: PROVED.
2. Lemma 1 (a uniform sign of an odd linear functional forces it to vanish): PROVED.
3. Lemma 2 (Δ^R contains no Λ; a monotonicity sign is invariant under cΛ and deletion): PROVED.
4. The exterior image ℓ_T(P_T) is not a monotone cone: ARGUED.
5. The exchange log n ↔ Σ1/m falls back onto R161_004 Cor. 2.1 and Paper 41 C5: CITED.
6. The signed Bernoulli remainder is already identified (106_109; POWER_GRAM_SLICES §8): CITED.
7. Monotonicity of the moving discrepancy norm is false (R161_029): CITED (numerical NO-GO of that memo).
8. 038 and 050 lack an integer lattice, and the mechanism falls outside their class without gaining content: PROVED (reading
   of the definitions).
9. The statuses of L161.3, L161.4, L161.5–6 and the port minimum are those of the table of §2: CITED / OPEN.
10. Candidate passing the gate: none. Selection NO-GO in the class «signed lattice discrepancy applied
    to the PC remainders».
11. L161.4 first in the order: ARGUED.
