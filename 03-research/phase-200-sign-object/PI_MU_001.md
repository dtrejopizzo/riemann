# PI_MU_001: the Ramanujan quotient Π_μ (phase 200, round 5)

Pure mathematics, no new computation.
OPEN / NO-GO / REF-D / NUMERICAL. **No sign is proved. L′♯ OPEN. Row D OPEN.**

**Read.** AUDIT_200_AMU_001 (complete); A_MU_FACTORIZATION_001; AUDIT_200_SPEC_002/003; Q2_LADDER_001 (Lemma R,
rough 0/1 comb); SPEC_002 (SQ.0, T.1, T.3); SPEC_003 (A.1); B1_FLAT_001 (ring identity, stacking falsifier);
Paper 47 §22 (def:ext l.9601, lem:ext-mob l.9633, thm:ext-half l.9647, rem:ext-killing, prop:ext-gauge l.9680,
prop:ext-consol (b) l.9729, prop:ext-univ l.9735); phase 199: AUDIT_CONSTRAINTS_001 (rows 3, 9, 11, 17, 19),
MORI15_EXTREMAL_001.

## 0. Index check (done before building)

Grep in `05-meta-and-planning/ROUTES-TRIED-INDEX/README.md` for "Ramanujan", "c_k(N)", "Poisson over", "quotient",
"projector", "orthogonal", "adelic", "Paley", "annihilator", "closed range", "Amrein", "prolate", "edge", "J²",
"Riesz", "Jordan". Relevant hits and their relation to this memo:

| entry | what it records | relation |
|---|---|---|
| l.63, l.396 (INV_H_001) | Ramanujan/Vaughan/Poisson-over-ℤ as a linear identity: NO-GO; "finite Ramanujan = regrouped Möbius" | §1–§2 **confirm** this in the quotient: Ramanujan relations are changes of representative (Lemma Π.2) |
| l.455 (E_001), Lemma E.4 | 𝒲_ext = ã-form − R_Λ (partition by symbol) | the B₊ candidate of §3.2 is that partition; recorded as a duplicate |
| l.456 (F_001) Prop F.0; l.9735 prop:ext-univ | fixed form 𝔔 modulo the fixed radical PW_1 | universal 𝒬_μ: already known; here the annihilator description and the closed range are added |
| l.485 (DD_001) | Schur boards, "Z bounded only with weight ξ^s" | Z unbounded on 𝒦_T (§3.2) |
| l.518–520 (SPEC_003, AUDIT_SPEC_003, C1) | 𝒬_μ = L²/𝒢̄_T, norm ℓ/2; R-Q6; B.1♭ | starting point; B.1♭ FALSE (B1_FLAT) is used in §3.2 |
| l.467 (MORI15) | g*, f* minimal gauge in prolate basis, ℓ* ∈ [4.4,8.5]e−70, edge value | §4 |
| l.479 (TEST_KINKS_001) | jumps of E⁻¹p at λ/m with weights μ(m) | §5: the jump comb of §2.4 is different (inner edge 1/λ, weights n^{−½}, no Möbius); new reason written there |
| Paper 47 prop:ext-consol (b) | ℓ as a prolate form with infimum over the gauge coefficients | §2.3 is its closed form; not new |

No entry describes 𝒢̄_T by its annihilator, nor proves that the gauge image is closed, nor identifies the
Ramanujan relations/Lemma R as an identity on 𝒬_μ. **New reason compared with INV_H (l.396):** INV_H uses the
additive identities *linearly on the form*; here they are used as *quotient relations* (what AUDIT_AMU §6.1 asked
for). The result (§1–§2) is that this difference produces no new object: the relations collapse into the
archimedean orthogonal projector.

---

## 1. The gauge 𝒢̄_T as the kernel of relations

Notation from def:ext: λ = e^T, N = λ², P := multiplication by 1_{[−1/λ,1/λ]} (time), B_λ := band projection
1_{(−λ,λ)}(ξ), Q := 1 − B_λ. For h ∈ L²(λ,∞) let H(ξ) := h(|ξ|)1_{|ξ|>λ} (even extension) and
 (Ch)(x) := 𝓕H(x) = 2∫_λ^∞ h(ξ)cos(2πxξ)dξ ∈ L²(ℝ).

### 1.1 Lemma Π.0 (closed range; PROVED)

Let L²_{0} := {φ ∈ L²(ℝ) even: supp φ ⊂ [−1/λ,1/λ], ∫φ = 0}. Then
 𝒢̄_T = {𝓕φ|_{(λ,∞)} : φ ∈ L²_0},
and the map φ ↦ 𝓕φ|_{(λ,∞)} is injective and bounded below: ‖𝓕φ|_{(λ,∞)}‖² ≥ ½(1 − χ_0)‖φ‖², with χ_0 = χ_0(2π) < 1
the concentration of the first prolate of the pair (time [−1/λ,1/λ], band (−λ,λ)), time–band product 4,
independent of T.

*Proof.* For φ ∈ PL², ‖Q𝓕φ‖² = ‖φ‖² − ‖B_λ𝓕φ‖² = ⟨φ, (1 − PB_λP)φ⟩ ≥ (1 − χ_0)‖φ‖² (Slepian–Landau–Pollak:
‖PB_λP‖ = χ_0 < 1; CITED, classical). The factor ½ comes from parity (positive half). Hence the image of
PL²_{even} is closed, and the image of the L²-closure of {φ ∈ C², φ(0) = 0, ∫φ = 0} is the closure of the image.
The condition φ(0) = 0 is not L²-closed (pointwise evaluation is not continuous) and disappears; ∫φ = 𝓕φ(0) is
continuous and is preserved. □

Consequence: **every element of 𝒢̄_T is the tail of an L² gauge**, not merely a limit. The "closure" of def:ext
adds no singular objects; it only adds φ without C² regularity.

### 1.2 Lemma Π.0′ (explicit annihilator; PROVED)

 𝒦_T := 𝒢̄_T^⊥ = {h ∈ L²(λ,∞) : Ch is constant a.e. on (−1/λ, 1/λ)}.

*Proof.* ⟨𝓕φ|_{(λ,∞)}, h⟩ = ½∫φ·Ch for φ even. This vanishes for every φ ∈ L²_0 ⟺ Ch|_{(−1/λ,1/λ)} ∈ (L²_0)^⊥ =
span{1}. □

Equivalently (via 𝓕): h ∈ 𝒦_T ⟺ ψ := Ch is an even L² function that is **constant on [−1/λ,1/λ] and whose
transform vanishes on (−λ,λ)**. This is a double-annihilation space (Amrein–Berthier/Benedicks type, modulo a
constant), of infinite dimension (CITED: Amrein–Berthier).

**Answers to Task 1.**
- *The system of relations* defining 𝒢̄_T is {⟨r, h⟩ = 0 : h ∈ 𝒦_T}. It is countable if an orthonormal basis of
  𝒦_T is fixed (separable), but **has no arithmetic index**: the natural index is the prolate basis of the
  complement (§2.3).
- *Shape of the relations.* In coordinates r there are neither integer dilations nor shifts: they are relations of
  **two Fourier intervals** (time 1/λ, band λ). ℕ does not appear.
- *Where ℕ appears.* When transporting to the tail variable Ψ̌ = Zr. Poisson over ℤ is exactly the intertwiner
  Z∘(Q𝓕)|_{PL²} = (φ ↦ Φ_φ|_{(−∞,−T)}), i.e. Ψ̌_φ(y) = e^{−y/2}Σ_n φ(ne^{−y}): **Riemann sums** of φ with step
  e^{−y}. In the log variable these are shifts by log n; in the u variable they are dilations by n. The
  relations, transported, read ⟨Ψ̌, (Z^{−1})^*h⟩ = 0, i.e. Σ_m μ(m)m^{−½}⟨Ψ̌(· + log m), h̃⟩ = 0 (h̃ := log form of
  h). These are Möbius relations with log shifts. **ARGUED**: Z⁻¹ is unbounded (C1, B1_FLAT), so the formula only
  holds for h with sufficient decay.
- *Where Guo L4.4 enters.* **It does not enter 𝒢̄_T nor Π_μ.** It enters only in the inclusion 𝒢̄_T ⊂ rad(𝒲)
  (prop:ext-gauge), i.e. in 𝒲 descending to 𝒬_μ.

### 1.3 Correction to AUDIT_200_AMU_001 §4

The auditor writes that "the exact Λ lives in **which the null subspace is**." As a subspace of L²(λ,∞), 𝒢̄_T is
defined solely by T (def:ext; Lemma Π.0′): **it is the same for Λ, a_P, cΛ, Beurling and DH.** What is Λ-exact is
the **inclusion** 𝒢̄_T ⊂ rad(𝒲_Λ). For the falsifiers the inclusion fails (R-Q6). Correct reformulation: *the exact
Λ lives in the fact that the form vanishes on a fixed archimedean subspace, not in the subspace itself.* (PROVED,
by definition.)

### 1.4 Lemma Π.1 (PROVED)

With Π_μ := orthogonal projector of L²(λ,∞) onto 𝒦_T: **Π_μ(𝒢̄_T) = 0** (definition) and
‖Π_μ r‖² = dist²(r, 𝒢̄_T) = ℓ(g)/2 for r = r_f, Ef = g (prop:ext-gauge, only its Möbius part, without Guo).
Π.1 uses neither Guo L4.4 nor Λ.

---

## 2. Π_μ as a projector: formula, image, Ramanujan relations

### 2.1 Closed formula (PROVED)

Let G := Q𝓕P: L²_0 → L²(λ,∞) (even part). By Π.0, G*G = P(1 − PB_λP)P|_{L²_0} is invertible with
‖(G*G)⁻¹‖ ≤ 2/(1−χ_0). Then
 Π_μ = 1 − G(G*G)⁻¹G*,
and in the prolate basis ψ_k (even, of the pair [−1/λ,1/λ] × (−λ,λ)), with the rank-one correction for ∫φ = 0,
 Π_μ r = r − Σ_{k even} (1 − χ_k)⁻¹⟨r, Q𝓕ψ_k⟩ Q𝓕ψ_k + (rank 1).
The double orthogonality of Slepian is used: the Q𝓕ψ_k are orthogonal with norm² (1 − χ_k) (CITED). By
prop:ext-univ, after t = λx everything is **independent of μ** (fixed prolates of product 4).

### 2.2 Lemma Π.2: the Ramanujan/Lemma R relations are the identity in 𝒬_μ (PROVED, without Guo)

Let g be of the core with A(g) = 0 and let P be a finite Dirichlet polynomial such that ζP has coefficients c_1 = 1
and c_N = 0 for 1 < N < μ (for example P = ∏_{p<μ}(1 − p^{−s}), which gives the rough comb of Q2, or the
mollifier M_μ of SQ.0). Let f_P be the "sieve" representative (P(∂)g read in the variable u, extended evenly).
Then f_P is admissible, Ef_P = g, and
 r_{f_P} − r_{f_can} ∈ 𝒢_T-images;  in particular Π_μ r_{f_P} = Π_μ r_{f_can}.

*Proof.* Φ_{f_P} = (ζP)(∂)g = g + Σ_{N≥μ} c_N N^{−½}τ_{log N}g. The shifts by log N ≥ 2T fall outside the window,
so Ef_P = g. By lem:ext-mob (bijection on [1/λ,λ]), f_P − f_can is supported on [−1/λ,1/λ]. It is C² and satisfies
both constraints (A(g) = 0, as in Lemma R), hence it belongs to 𝒢_T. □

**Reading.** The rough 0/1 comb (Q2), the mollifiers of SQ.0 and the class-p subcombs **are not relations distinct
from the gauge: they are points of the same coset.** Π_μ sends them to the same vector. This gives the exact form
of R-Q2 in the quotient: "levels, classes p, divisor bands = coordinates inside the radical" becomes "= the same
point of 𝒬_μ." What the goal calls "Π_μ defined by the Poisson/Ramanujan relations" **coincides with the
archimedean orthogonal projector** of §2.1: the Ramanujan relations only generate movements within each fiber. No
arithmetic coordinate remains in the image.

### 2.3 Coordinates of the image (PROVED; they are not zero-coordinates)

Π_μ r_f = r_{f♯}, with f♯ := f − φ*, the **minimal-leak representative**. Explicitly:
- f♯ = f_can = E⁻¹g on [1/λ, λ] (fixed by g);
- on [−1/λ,1/λ], f♯ solves the second-kind Fredholm equation
  (1 − PB_λP)f♯_in = PB_λ f_out + c·1, with c fixed by ∫f♯_in = −∫f_out. The solution is bounded by (1−χ_0)⁻¹ and
  is real-analytic in the interior (PB_λ regularizes).

Hence the image is parametrized by g, and ‖Π_μ r‖² = ‖Q𝓕(I + K)E⁻¹g‖² with K bounded and explicit. This is the
closed form of prop:ext-consol (b) (infimum over the coefficients of the resolved gauge). **It is not new as a
form of ℓ; it is new as an operator.**

### 2.4 Structural fact: f♯ has jumps at ±1/λ (ARGUED)

Nothing forces continuity of f♯ at ±1/λ: the jump is σ(g) := f_can(1/λ⁺) − φ*-part(1/λ⁻), a linear functional of g.
It is generically ≠ 0 (ARGUED: the equation of §2.3 imposes no boundary condition). Consequence in the tail:
 Ψ̌_{f♯}(y) = e^{−y/2}Σ_n f♯(ne^{−y})
has jumps exactly at y = T + log n, n ≥ 1, of size σ(g)·e^{−(T+log n)/2} = λ^{−½}n^{−½}σ(g). **The canonical
representative of the quotient carries a jump comb with weights a_n ≡ 1 (n^{−½}) at the positions log n.** This is
the only place where (ℕ,·) appears in the image of Π_μ, and it appears as a **singularity**, not as a coefficient.

### 2.5 Is Π_μ = ⊗_p Π_p? (NO-GO, PROVED)

- The "𝔸" of B1_FLAT_001 is the **real ring** (1/√2, 1) ⊂ ℝ, not the adeles (B1_FLAT l.26). The identity
  ∫_1^{√2}|Zϱ|²dX/X = ‖Σ_n h(n·)‖²_{L²(1/√2,1)} is a Riemann-sum identity in one real variable. It has no local
  factors. The "adelic" reading of the goal is a notational misunderstanding.
- Π_μ is archimedean (Π.0′) and commutes with any Euler factor (1 − p^{−½}τ_{log p}) that does not move g. By
  Π.2, the **complete** product ∏_{p<μ} acts as the identity on 𝒬_μ. A partial product (missing some p < μ)
  changes the window: there is N < μ with c_N ≠ 0, so g moves. **No decomposition Π_μ = ⊗_pΠ_p with nontrivial
  Π_p exists.**
- Therefore "a_P fails in the formula due to the missing Π_p factor" is FALSE as a mechanism. a_P fails **in the
  descent** (R-Q6): 𝒲^{a_P} is not invariant under 𝒢̄_T. It also fails in the formula for ℰ (§3), because this
  carries the weights log n = Λ∗1 (R-F1).

---

## 3. The form in the image

### 3.1 𝒲 descends to Π_μ(𝒟) (PROVED, given Guo L4.4)

Let 𝒟 := {r_f : f admissible}. **Lemma Π.3.** If r_f − r_{f′} ∈ 𝒢̄_T with f, f′ admissible, then f − f′ ∈ 𝒢_T (C²,
not merely L²). *Proof.* By Π.0, r_f − r_{f′} = 𝓕φ|_{(λ,∞)} with φ ∈ L²_0. The three functions 𝓕f, 𝓕f′, 𝓕φ are
entire (compact support) and agree on a half-line, so f − f′ = φ. Then φ is C² and satisfies
φ(0) = 𝓕φ(0) = 0. □

With prop:ext-gauge, 𝒲̄(Π_μ r) := 𝒲[Zr] is well defined on Π_μ(𝒟) ⊂ 𝒦_T. L′♯ reads
 𝒲̄(k) ≥ 2κN^{−A₀}‖k‖²  (k ∈ Π_μ(𝒟)),
which is eq:ext-starstar written on 𝒦_T. **PROVED reformulation, with no sign content.**

**Domain warning.** Π_μ r_f = r_{f♯}, and f♯ is not admissible (jumps, §2.4). The formula of thm:ext-half
**evaluated on r_{f♯}** is not proved: Guo L4.4 requires C². 𝒲̄ is defined by the class and not by the formula on
the representative. It remains open whether the formula holds on f♯ (Lemma Π.4, §6).

### 3.2 Search for B

We seek B on 𝒦_T with 𝒲̄ = ‖B·‖² − ℰ_μ, with no free parameter.

**(i) B via spectral decomposition (Jordan).** 𝒲̄ defines a symmetric operator 𝒜_T on 𝒦_T. If one took
B = 𝒜_{T,+}^{½} and ℰ = ‖𝒜_{T,−}^{½}·‖², then ℰ ≥ 0 is trivial but ℰ ≤ (1 − κ′)‖B·‖² is L′♯. Worse, 𝒜_{T,±} are
only known once the spectrum of 𝒲̄ is known. **REF-D.** Another option, B = (𝒜_T + c)^{½}, ℰ = c‖·‖², has the free
parameter c: it is the addition-and-subtraction of AUDIT_AMU §2.3. **NO-GO.**

**(ii) B₊ := m_+^{½}(D_y)∘Z∘Π_μ**, with m = m_+ − m_−, m_± ≥ 0 (m < 0 for |τ| < 6.2898, l.515). With the formula of
thm:ext-half at the representative f♯ (CONDITIONAL on Π.4):
 𝒲̄(Π_μ r) = ‖B₊Π_μ r‖² − ℰ₊,
 ℰ₊ := (1/2π)∫m_−|𝓕ZΠ_μ r|² + 2⟨ZΠ_μ r, Z_logΠ_μ r⟩ − 2A·B(ZΠ_μ r).
The identity is exact and ℰ₊ is explicit. There is no free parameter. And ℰ₊ "sees" Λ only via log n = Λ∗1, which
is false for a_P (the P10 formula holds, trivially). But:
- **P2 fails (PROVED, given B1_FLAT_001).** Z ∘ Π_μ is not bounded from (𝒦_T, ‖·‖) to L²(T,∞): the harmonic
  stacking falsifier of B1_FLAT lies in (𝒢̄_1)^⊥ = 𝒦_1 ("orthogonality to the gauge does not help," B1_FLAT §2)
  and gives ‖Zϱ‖²_{ring}/‖ϱ‖² ≳ log K. With pulses of width K^{−3}, the Mellin frequency is ≍ K³, where
  m_+ ≍ log K. Hence ‖B₊Π_μ r‖²/‖Π_μ r‖² → ∞ and the pieces ‖B₊·‖², ℰ₊ are not at scale ℓ: they cancel each other
  at a larger scale. This is the "canceling base" (C8).
- **Duplicate.** It is the symbol partition of E_001 Lemma E.4 (ã-form − R_Λ, l.455) and the DD_001 board
  (l.485, "the w side is not at leak scale"), evaluated at another representative (f♯ instead of f). The
  representative does not change the value (Π.3) and does not fix P2.
- **Verdict (ii): NO-GO** as a sign object (P2 + duplicate). It is useful only as an exact formula in the
  quotient.

**(iii) B of rank one in the edge channel.** MORI15 (l.198 of the memo) observes
W* ≈ J²·Σ_{γ>0}|ρ|^{−2} = J²·(ξ′/ξ)(1)/2 with J = g*(T) = −1.4208e−34, with a 2% agreement (NUMERICAL). This
suggests B_edge r := ((ξ′/ξ)(1)/2)^{½}·J(r) and ℰ ≈ 0 at r*.
- J is gauge-invariant: Φ_φ(−T) = e^{−T/2}Σ_{n≥1}φ(n/λ) = 0, because φ(1/λ) = 0 and n/λ > 1/λ for n ≥ 2 (PROVED).
- But in the core J ≡ g(±T) = 0 by definition: Mori's g* (Legendre basis) is not in the core. On the core the
  edge channel is a C² boundary layer and not a rank-one functional (row 19 of AUDIT_CONSTRAINTS).
- Imposing "ℰ_edge ≥ 0 at the extremal" is an inequality on the minimizer (row 11). **REF-D.**

**Conclusion §3.** With Π_μ canonical (PROVED), all the arithmetic of B∘Π_μ lies in B and in the descent
(Guo L4.4). The three canonical B's fail: (i) REF-D/addition-and-subtraction, (ii) P2 + duplicate E.4/DD,
(iii) REF-D + outside the core. **No B with ℰ_μ ≥ 0 visible without already knowing 𝒲̄ ≥ 0 was found.** By (i), any
B not given by an *a priori* formula in (ℕ,+,·) is REF-D.

---

## 4. Test μ = 15 (predictions; NUMERICAL only with existing data)

Data from MORI15_EXTREMAL_001: W* = 4.7634661356e−70, ℓ* ∈ [4.4, 8.5]e−70 (81% a₄²(1−λ₄)), J = g*(T) = −1.4208e−34,
Σ_{γ>0}|ρ|^{−2} = 0.0230957; S₁ = 0.432 (SPEC_002 T.3).

| quantity | prediction of the Π_μ framework | value (trivial arithmetic on the data) |
|---|---|---|
| ‖Π_μ r*‖² = ℓ*/2 | Π.1 | ∈ [2.2, 4.25]e−70 |
| 𝒲̄(Π_μ r*) | = W* (Π.3) | 4.763e−70 |
| ratio 𝒲̄/‖Π_μ r*‖² | 2κ_emp | ∈ [1.12, 2.16] (κ_emp ∈ [0.56, 1.08], matches l.467) |
| J² | edge channel scale | 2.019e−68 |
| ℓ*/J² | — | ∈ [0.0218, 0.0421]: comparable to Σ|ρ|^{−2} = 0.0231 |
| jump comb σ(g*) (§2.4) | ≤ O(√ℓ*) ≈ 2–3e−35 | not computed: Mori minimizes in a finite (smooth) prolate basis, so σ is invisible in that data |
| S₁ = 0.432 | Π_μ is blind to S₁ (Selberg basis within the coset, Π.2) | no prediction: it does not enter |

**Observation (NUMERICAL, arithmetic only).** At r* both W* and ℓ* are ≈ J²·Σ|ρ|^{−2}, with
W*/(J²Σ|ρ|^{−2}) = 1.02 and ℓ*/(J²Σ|ρ|^{−2}) ∈ [0.94, 1.82]. If this is not a coincidence at μ = 15, the extremal
is an **edge channel** object whose leak and whose value come from the same rank one. This fits with row 19
(edge 51–78%). It is not used as an argument.

**No computation is run.** The new quantities (σ(g*), ‖B₊Π r*‖², ℰ₊(r*)) require solving the equation of §2.3 in
Mori's basis. By the conclusion of §3 they are not decisive: there is no need to compute them.

---

## 5. Index check by object

| object | grep | entries | new reason | status |
|---|---|---|---|---|
| Π.0 closed range | "closed range", "Amrein", "prolate" | none; l.47 (Sonin/prolate: no sign) | gauge description, not a sign source | PROVED, tool |
| Π.0′ annihilator 𝒦_T | "annihilator", "orthogonal", "Paley" | l.455 (E_001: "Paley–Wiener is the whole additive entry") | describes 𝒢̄_T^⊥ explicitly; E_001 does not | PROVED |
| Π.2 Ramanujan = identity in 𝒬 | "Ramanujan", "c_k(N)", "quotient" | l.63/396 INV_H; l.516–517 (SQ, Q2) | *quotient* relations, not linear (requested by AUDIT_AMU) | PROVED; **closes the "Π by Ramanujan" route** |
| ⊗_pΠ_p | "adelic", "local–global" | l.220 (local–global front C) | reading of B1_FLAT; there are no adeles | NO-GO PROVED |
| B (i) Jordan | "Jordan", "Riesz" | l.257 (Jordan on the staircase: dead); AUDIT_AMU §2.3 | none | REF-D / NO-GO |
| B₊ (ii) | "Z bounded", "Schur", "ã-form" | l.455 E.4, l.485 DD_001, l.520 B.1♭ | only changes the representative (f♯), which Π.3 makes irrelevant | NO-GO (duplicate + P2) |
| B_edge (iii) | "edge", "g*(T)" | l.467 MORI15, row 19, row 11 | new rank one, but at the minimizer | REF-D |
| jump comb of f♯ | "jumps", "kinks" | l.479 TEST_KINKS_001 (jumps of E⁻¹p at λ/m, weights μ(m)) | here: a single jump at the inner edge 1/λ created by the orthogonal projection; image with weights n^{−½} with no Möbius | ARGUED, open as data |

---

## 6. Final

### Labels

| item | label |
|---|---|
| Π.0 (closed gauge image, bound (1−χ_0)) | PROVED (Slepian CITED) |
| Π.0′ (𝒦_T = {Ch constant on (−1/λ,1/λ)}) | PROVED |
| relations in coordinates r: two Fourier intervals, no ℕ | PROVED |
| relations transported to Ψ̌ (Möbius with log m shifts) | ARGUED (Z⁻¹ unbounded) |
| Π.1: Π_μ(𝒢̄_T) = 0, ‖Π_μ r‖² = ℓ/2, without Guo and without Λ | PROVED |
| closed formula of Π_μ in the prolate basis (μ-universal) | PROVED |
| Π.2: sieve/Ramanujan/rough representatives are the same point of 𝒬_μ | PROVED (without Guo) |
| Π.3: 𝒟 ∩ (r_f + 𝒢̄_T) = r_f + 𝒢_T; 𝒲̄ well defined on Π_μ(𝒟) | PROVED (given Guo L4.4) |
| correction to AUDIT_AMU §4 ("Λ in the inclusion, not in the subspace") | PROVED |
| jumps of f♯ at ±1/λ ⇒ jump comb n^{−½} at T + log n | ARGUED |
| ⊗_pΠ_p | NO-GO (PROVED) |
| B Jordan / B + c | REF-D / NO-GO |
| B₊ = m_+^{½}ZΠ_μ | identity CONDITIONAL on Π.4; NO-GO as a sign object (P2 PROVED via B1_FLAT; duplicates E.4/DD) |
| B_edge | REF-D |
| test μ = 15 | NUMERICAL (arithmetic on published data) |
| **object A_μ = B∘Π_μ** | **Π_μ constructed; no valid B. L′♯ OPEN. Row D OPEN.** |

### New restriction R-Π (HARD)

*Every quotient/projector with kernel 𝒢̄_T is archimedean and blind to the comb.* Its relations are of two Fourier
intervals (Π.0′) and the Poisson/Möbius/Ramanujan relations act as the identity on 𝒬_μ (Π.2). Hence, in
A_μ = B∘Π_μ:
- all (ℕ,+,·) and Λ content lies in B and in the inclusion 𝒢̄_T ⊂ rad 𝒲 (Guo L4.4);
- P10-descent is automatic for any gauge-invariant identity, and does not discriminate between constructions;
- the problem reduces to giving B *a priori* on 𝒦_T. No B built only with Z, Z_log or the symbol m is at leak
  scale (Z unbounded on 𝒦_T).

Moreover, the only trace of (ℕ,·) in the canonical representative of each class is the jump comb of §2.4.

### Entry for the index

- **PI_MU_001 (round 5): Π_μ constructed, no sign.**
  - Π.0/Π.0′ PROVED: 𝒢̄_T = Q𝓕(L²_0[−1/λ,1/λ]) has closed range (bound 1−χ_0) and
    𝒦_T = 𝒢̄_T^⊥ = {h : Ch ≡ const on (−1/λ,1/λ)}. The relations are of two Fourier intervals, no ℕ.
  - Π.1 PROVED (‖Π_μ r‖² = ℓ/2, without Guo). Π.2 PROVED: the rough/mollified/sieve representatives are the same
    point of 𝒬_μ ⇒ "Π by Ramanujan" = orthogonal projector. Π.3 PROVED: 𝒲 descends to Π_μ(𝒟).
  - Λ lives in the inclusion 𝒢̄_T ⊂ rad 𝒲, not in the subspace (corrects AUDIT_AMU §4). ⊗_pΠ_p NO-GO
    ("𝔸" = real ring).
  - B Jordan: REF-D. B₊ = m_+^{½}ZΠ: NO-GO (P2 via B1_FLAT; duplicates E.4/DD). B_edge: REF-D.
  - R-Π (HARD): every Π with kernel 𝒢̄_T is archimedean; the arithmetic can only be in B.
  - Do not retry: Π by Ramanujan/Poisson/sieve relations, local factorizations of Π, B = function of Z/symbol.
  - Row D OPEN.

### Next exact lemma

**Lemma Π.4 (formula at the minimal-leak representative; OPEN, without Λ except Guo, without sign).** For every g
of the core, let f♯ = f − φ* be the representative of §2.3 (φ* ∈ L²_0, with jumps at ±1/λ). Then the identity of
thm:ext-half holds for Ψ̌_{f♯}:
 𝒲[Ψ̌_{f♯}] = 𝒲[Ψ̌_f],
with the form evaluated term by term. The Lévy term receives the explicit contribution of the jump comb
λ^{−1}σ(g)²Σ_{m,n}(mn)^{−½}·k(log(m/n)), where k is the Lévy/killing kernel of rem:ext-killing. Equivalently, Guo
L4.4 extends to φ ∈ L²_0 that is real-analytic in the interior with jumps at the boundary.

**Why this lemma.**
- It is the condition for any B∘Π_μ formula to be exact at the canonical representative.
- It isolates the only (ℕ,·) object that Π_μ produces: the quadratic form of the jump comb
  σ(g)²Σ(mn)^{−½}k(log m/n). Its sign and its scale relative to ℓ are the next question. It is a semiring-type
  object in m ≈ kn that has not been examined (versus TEST_KINKS: inner edge, no Möbius).
- If σ(g) = 0 for every g (forced continuity), Π.4 is trivial and the comb disappears: that too is a result.

---

## Summary (≤300 words)

The quotient requested by AUDIT_AMU is constructed.

**Π.0 (PROVED).** The gauge image 𝒢̄_T = Q𝓕(L²_0[−1/λ,1/λ]) is closed. The map is bounded below by
1 − χ_0(prolate), with a universal constant.

**Π.0′ (PROVED).** Its annihilator is 𝒦_T = {h : the cosine transform of h is constant on (−1/λ,1/λ)}, a
double-annihilation space.

The relations defining the gauge are of two Fourier intervals, with no ℕ. Poisson over ℤ is only the intertwiner
r ↦ Ψ̌ (Riemann sums); Möbius is its inverse. Guo L4.4 does not enter Π: it enters only in the inclusion
𝒢̄_T ⊂ rad 𝒲. This corrects AUDIT_AMU §4: Λ lives in that inclusion, not in the subspace, which is the same for
every comb.

**Π.1 (PROVED, without Guo).** Π_μ = orthogonal projector onto 𝒦_T. It satisfies Π_μ(𝒢̄_T) = 0 and
‖Π_μ r‖² = ℓ/2. There is a closed formula in the prolate basis, independent of μ.

**Π.2 (PROVED).** The rough, mollified and sieve representatives (Lemma R, SQ.0, Q2) are the same point of 𝒬_μ.
"Π by Ramanujan relations" is, therefore, the archimedean projector.

**Π.3 (PROVED, given Guo).** 𝒲 descends to Π_μ(𝒟).

**NO-GO.** ⊗_pΠ_p does not exist: the "𝔸" of B1_FLAT is a real ring, not the adeles.

**B.** None works:
- Jordan or B + c: REF-D or addition-and-subtraction.
- B₊ = m_+^{½}ZΠ: exact identity (CONDITIONAL on Π.4), but violates P2 because Z is not bounded on 𝒦_T
  (B1_FLAT falsifier) and duplicates E.4/DD.
- B of rank one at the edge: REF-D.

**μ = 15 (NUMERICAL, arithmetic).** ‖Πr*‖² ∈ [2.2,4.25]e−70 and 𝒲̄/‖Πr*‖² ∈ [1.12,2.16]. W* and ℓ* are both
≈ J²Σ|ρ|^{−2} (edge channel).

**Restriction R-Π (HARD).** Every Π with kernel 𝒢̄_T is archimedean; the arithmetic can only be in B.

**New fact (ARGUED).** The minimal-leak representative f♯ jumps at ±1/λ, and its tail carries a jump comb of
weight n^{−½} at T + log n.

**Next lemma: Π.4.** Prove the formula of thm:ext-half at f♯, i.e. Guo L4.4 for gauges with jumps, and identify
the shape of the jump comb.

L′♯ OPEN. Row D OPEN.
