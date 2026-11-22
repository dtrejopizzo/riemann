# R162_1302 — The q-difference Riemann–Hilbert problem of the first-contact kernel — **NO-GO (PROVED)**, three exact structures

Round 13. Pure mathematics, no numerics. Inputs: README (F1–F4, rounds 1–12), R162_590,
R162_1201 (Lemma 1.1, Thm 1.2, Thm 2.2, Prop 4.2, Thm 5.1), R162_903 (BCH log Z), R162_1001 (torsion cocycle),
R162_1004 (tensor lift), Paper 46 eq:symbol, lem:firstcontact.

**Question.** Prop 4.2 of R162_1201 recast HF = 0 (F ∈ N = ker H_{T_*}, H ≥ 0, λ = 0) as a q-difference
Riemann–Hilbert (RH) problem on the cut Γ = [e^{−2T}, e^{2T}]. Write that problem down exactly, and ask whether the
arithmetic of the dilation group (free abelian on primes) gives a Liouville theorem that forces g_F ≡ 0.

**Labels.**
- Lemma 1.1 (normalised transform: jump = πiF, exact dilation covariance) PROVED.
- Thm 2.1 (the exact scalar RH problem: archimedean part = finite-part endpoint value of the *running* Cauchy
  transform, plus the inversion q ↦ 1/q) PROVED. **New.**
- Prop 2.2 (connection 0 ↔ ∞: the two expansions of ĝ are the even lattice ½+2ℕ and the odd lattice 3/2+2ℕ of one
  entire function X_F, joined by Mellin–Barnes) PROVED. **New as a statement; elementary.**
- Prop 3.1 (dilation torus; Euler product ⟺ separability of the Laurent symbol; P_Λ = E log Z) PROVED. **New.**
- Thm 3.2 (maximal monodromy: the Euler curve is Zariski dense in the dilation torus) PROVED (classical input).
- Thm 4.1 (Liouville for jointly dilation-invariant functions) PROVED (classical); Thm 4.2 (it does not apply: one
  additive equation, not a consistent system; the cut destroys the group action) PROVED. **NO-GO.**
- Thm 5.1 (falsifier transport: DH, deletion/κ, Beurling, Λχ₂; F1 λ-blindness) PROVED.
Gate 1 OPEN. No label moves.

## 0. Corpus check

Grep "q-difference", "Birkhoff", "q-dilation", "Adams", "Schäfke", "Bohr", "separab", "torus" over phases 150–162:
only R162_1201 Prop 4.2 (the dictionary) and phase 159 G1_B3_R3 (Grothendieck–Birkhoff *splitting* on P¹, a different
object) hit. The Bohr torus is implicit in R162_1004 (tensor lift) and R162_903 (log Z = M_T(Λ/log)); the torsion
cocycle of R162_1001 is the only prior object that separates Λχ₂ and Beurling. Everything in §§2–4 below is new to the
corpus as written; the verdict repeats the round-6 lesson (ζ-data enter only through support/inequalities).

## 1. Normalisation

For F ∈ P_T (primitive, parity ε, supported on I = [−T,T]) put, for q ∉ Γ ∪ (−∞,0],

  ĝ(q) := q^{1/4} ∫_I F(u) e^{u/2} / (1 − q e^{2u}) du = q^{1/4} Σ_{m≥0} x_m q^m,   x_m = ∫_I F e^{a_m u}, a_m = 2m+½.

(x_0 = 0 by primitivity, so ĝ = q^{1/4} g_F with g_F of R162_1201 Prop 4.2.)

**Lemma 1.1.** (a) ĝ(q) = ½ q^{1/4} ∫_Γ F(−½log p) p^{−1/4} dp/(p − q), so ĝ is analytic off Γ ∪ (−∞,0] and, for
p = e^{−2t} ∈ Γ̊, the jump is  ĝ_+(p) − ĝ_−(p) = πi F(t)  (upper minus lower boundary value).
(b) For ℓ = log n and (S_ℓF)(u) = F(u−ℓ) on ℝ: ĝ_{S_{±ℓ}F} = σ_{n^{±2}} ĝ_F, where (σ_c h)(q) = h(cq). No weight
appears (the q^{1/4} normalisation absorbs n^{±1/2}).
(c) Hence the comb C = Σ_{n∈N_T} w_n(S_{ℓ_n}+S_{−ℓ_n}), w_n = Λ(n)n^{−1/2}, becomes the q-difference operator

  L_Λ := Σ_{n∈N_T} Λ(n) n^{−1/2} (σ_{n²} + σ_{n^{−2}}),

and CF = (πi)^{−1}·jump(L_Λ ĝ), the compression to I being "keep the jump on Γ, discard the jumps on n^{∓2}Γ ∖ Γ".
*Proof.* (a) substitute p = e^{−2u}; Sokhotski–Plemelj gives jump ½q^{1/4}·2πi·F p^{−1/4} at q = p. (b) change
variables u ↦ u+ℓ: e^{(u+ℓ)/2}q^{1/4} = (n²q)^{1/4}e^{u/2}, qe^{2(u+ℓ)} = (n²q)e^{2u}. (c) jump of σ_{n²}ĝ at p is
the jump of ĝ at n²p, i.e. πiF(t − log n). ∎

## 2. The exact RH problem (answer to "write it")

For a density on a sub-interval J ⊂ I write ĝ_J for the transform of F·1_J (cut e^{−2J}).

**Thm 2.1 (running Cauchy transform).** For every F ∈ P_T and every t ∈ ℝ, with p = e^{−2t},

  (𝒦F)(t) = FP { ĝ_{[−T,t]}(p) + ε ĝ_{[−T,−t]}(1/p) },                                                  (2.1)

(an empty interval gives 0; FP = Hadamard finite part at the endpoint, the log-free 1/|v| singularity of κ absorbed
in c_0 exactly as in R162_1201 Lemma 1.1). Consequently F ∈ N (HF = 0, λ = 0) iff there are α, β with

  c_0 F(t) − FP{ĝ_{[−T,t]}(e^{−2t}) + εĝ_{[−T,−t]}(e^{2t})} − (πi)^{−1} jump(L_Λ ĝ)(e^{−2t}) = αe^{t/2} + βe^{−t/2},  t ∈ I,  (RH)

together with jump(ĝ) = πiF on Γ, ĝ(q) = O(q^{5/4}) at 0 (primitivity) and the B-moment condition. Outside I the
same left side is free (it is the exterior AF); for t > T, (2.1) reduces to 𝒦F(t) = ĝ(e^{−2t}) (R162_1201 Thm 1.2),
for t < −T to εĝ(e^{2t}).
*Proof.* For u < t, q = e^{−2t}: q^{1/4}e^{u/2}/(1 − e^{2(u−t)}) = e^{−(t−u)/2}/(1 − e^{−2(t−u)}) = κ(t−u). For u > t
the reflected transform: u ↦ −u, F(−u) = εF(u), gives ε(1/p)^{1/4}... = e^{−(u−t)/2}/(1−e^{−2(u−t)}) = κ(u−t).
Sum = ∫κ(|t−u|)F(u)du. The Tate right side is e^{±t/2} = p^{∓1/4}. ∎

So the archimedean operator is **not** a q-difference operator: it is a *Volterra* object in the order of Γ (endpoint
value of the running transform) composed with the inversion ι: q ↦ 1/q (the functional-equation / parity symmetry).
The arithmetic operator L_Λ lives in the group algebra ℂ[Γ_T] of the dilation group

  Γ_T := ⟨ n² : n ∈ N_T ⟩ = ⊕_{p ≤ e^{2T}} ℤ·(p²)  ⊂ ℚ_{>0}^×   (free abelian, rank π(e^{2T})).

(RH) is a scalar problem with one cut, one inversion, finitely many incommensurable dilations, and a Volterra
archimedean term; the missing data (collar jumps on n^{∓2}Γ∖Γ, exterior AF) are free. It is equivalent to HF = 0
(bijective change of unknowns F ↔ ĝ), hence Gate 1 ⟺ (ĝ ≡ 0 for every solution) ⟺ N = {0}: **E1, as R162_1201
Thm 2.2**. What the q-picture adds is the separation of structure in §§2.2–3.

**Prop 2.2 (connection 0 ↔ ∞).** Let X_F(a) := ∫_I F e^{au} (entire, exponential type T). Then
 ĝ(q) = q^{1/4} Σ_{m≥0} X_F(2m+½) q^m near 0,  ĝ(q) = −ε q^{−3/4} Σ_{j≥0} X_F(2j+3/2) q^{−j} near ∞,
and both are the two residue expansions of the Mellin–Barnes integral
 ĝ(q) = −q^{1/4}(2i)^{−1} ∫_{Re s = c} X_F(2s+½) (−q)^s ds / sin(πs),   −1 < c < 0 (closed to the right: s = m ≥ 0; to the left: s = −j−1),
valid for |arg(−q)| < π (i.e. off the positive axis, consistent with Γ ⊂ ℝ_{>0}).
*Proof.* Large-q expansion 1/(1−qe^{2u}) = −Σ_{j≥1}q^{−j}e^{−2ju}, then u ↦ −u. Mellin–Barnes: X_F(2s+½) is
bounded on each vertical line (F ∈ L¹(I)), while 1/sin(πs) decays like e^{−π|Im s|} and |(−q)^s| ≤ C e^{|arg(−q)||Im s|};
residues at s = m ≥ 0 and s = −j−1, X_F(−2j−3/2) = εX_F(2j+3/2) by parity. ∎

Reading: the "Birkhoff/Adams connection data" of ĝ between the regular singular points 0 and ∞ are the interlaced
samples X_F(½ + ℕ): the ζ Gamma lattice at 0 and the odd-character (DH, R162_1201 Thm 5.1(ii)) lattice at ∞. The
connection kernel is 1/sin(πs), periodic under s ↦ s+1 = monodromy q ↦ e^{2πi}q around 0, **not** under any dilation
period s ↦ s + πi/log n. A genuine q-difference connection matrix (Birkhoff 1913, Adams 1928; Sauloy's theta
quotients) would be σ_{n²}-elliptic; nothing in (RH) produces one (§4).

## 3. The dilation group: what "independence of primes" really encodes (answer to (i))

Characters of Γ_T: 𝕋_T := Hom(Γ_T, ℂ^×) ≅ (ℂ^×)^{π(e^{2T})}, z = (z_p). The monomial q^{1/4+s}·(…) is a joint
eigenfunction: σ_{p²} ↦ z_p = p^{2s}. The **Euler curve** is E: s ↦ (p^{2s})_p ⊂ 𝕋_T.

**Prop 3.1 (Laurent symbol).** For any weight vector a on N_T, L_a := Σ a(n)n^{−1/2}(σ_{n²}+σ_{n^{−2}}) ∈ ℂ[Γ_T]
corresponds to P_a(z) = Σ_n a(n)n^{−1/2}(z^{v(n)} + z^{−v(n)}), v(n) = exponent vector of n. Then
(a) a is supported on prime powers ⟺ P_a is **separable**: P_a = Σ_p π_p(z_p) (one-variable Laurent polynomials).
(b) For a = Λ: P_Λ^+ = 𝔈 log Z (truncated to N_T), Z(z) = Π_p (1 − p^{−1/2}z_p)^{−1}, 𝔈 := Σ_p (log p) z_p∂_{z_p}.
𝔈 is the vector field tangent to E (d/ds along z_p = p^{2s} up to the factor 2). So Λ*1 = log ⟺ "the symbol is the
logarithmic derivative, along the Euler curve, of a product of one-variable factors".
*Proof.* (a) z^{v(n)} is one-variable iff n is a prime power. (b) z_p∂_{z_p} log(1−p^{−1/2}z_p)^{−1} = Σ_k p^{−k/2}z_p^k,
multiplied by log p = Λ(p^k). ∎ (Same content as R162_903 Thm 3.2, now in torus coordinates.)

**Thm 3.2 (maximal monodromy).** The Zariski closure of E in 𝕋_T is 𝕋_T, and the closure of E(iℝ) in the compact
torus (S¹)^π is all of it. Equivalently the difference-Galois torus of the commutative system {σ_{p²}} acting on the
one-variable Mellin functions q^{1/4+s} is the full dilation torus.
*Proof.* The Zariski closure of a one-parameter subgroup s ↦ exp(sλ) of a torus is the subtorus cut out by the
integer relations Σ k_p λ_p = 0; λ_p = 2log p has none (unique factorisation). Kronecker for the compact part
(CITED: Bohr's correspondence, e.g. Titchmarsh, *Theory of the Riemann zeta-function*, §11.5). ∎

**Consequence.** The independence of prime dilations is maximal genericity: it imposes **no** algebraic relation on
the kernel. And it is a property of ℕ (of the index set of the dilations), not of Λ: DH, deletions/κ at any n, and
Λχ₂ use the same group Γ_T; generic Beurling systems have a free group on their own primes. The Euler product lives
in separability (Prop 3.1(a)) and Λ*1 = log in the 𝔈 log Z form (3.1(b)) — not in the group.

## 4. Liouville (answer to (ii))

**Thm 4.1 (joint-invariance Liouville; classical).** Let h be meromorphic on ℂ^× with h(c_1q) = h(q) = h(c_2q),
c_1, c_2 > 1 multiplicatively independent. Then h is constant. More generally (CITED: R. Schäfke, M. F. Singer,
*Consistent systems of linear differential and difference equations*, J. Eur. Math. Soc. 21 (2019)), a formal power
series satisfying a linear c_1-difference and a linear c_2-difference equation with c_1, c_2 multiplicatively
independent is rational.
*Proof of the first part.* h∘exp has real periods log c_1, log c_2, ℚ-independent, hence a dense period group in ℝ;
by continuity h∘exp is constant on each horizontal line, so ∂_x h∘exp ≡ 0 and by analyticity h is constant. ∎

This is the only Liouville mechanism in which the arithmetic of the dilation group bites. It requires **one equation
per independent generator** (a consistent system).

**Thm 4.2 (NO-GO).** (a) (Full line, no cut.) The solutions of L_Λ-type equations are not rigid: for the full-line
operator A_ℝ = c_0 − 𝒦 − C (symbol s_T(τ) = m(τ) − 2Σ_{N_T} w_n cos(τ log n), Paper 46 eq:symbol) and any zero τ_0
of s_T, q^{1/4 − iτ_0/2} (i.e. e^{iτ_0 t}) solves the homogeneous equation; s_T is a real-analytic almost-periodic
function minus a log-growing digamma term, and each of its (complex) zeros gives a solution. So a single additive equation has an infinite-dimensional
non-rational solution space; Thm 4.1 needs separate relations σ_{p²}h = c_p h, which would force every z_p = p^{2s}
to be a root of its own π_p — no such factorisation of (RH) exists, because the archimedean term (2.1) is not in
ℂ[Γ_T] and couples all primes through the one variable s.
(b) (With the cut.) Γ_T does not act on N: σ_{n²} moves the cut Γ to n^{−2}Γ, and compression discards the displaced
jump (Lemma 1.1(c)). The only group-like structure on the window is the partial semigroup {n² : log n < 2T} with
collar leakage (R162_202). Hence there is no function on ℂ^× built from F ∈ N that is σ_{p²}-invariant or
σ_{p²}-eigen for even one p, and Thm 4.1 has no input.
(c) (Separable lift.) Lifting ĝ to the torus (Bohr lift of the Mellin variable) would linearise the problem prime by
prime; but the lift of an interval-supported density is not interval-supported in any coordinate (the interval in
log q is not a Γ_T-invariant set), and the tensor/multivariable lift is idempotent at contact (R162_1004). ∎

## 5. Falsifiers (answer to (iii)) and F1

**Thm 5.1.** (i) DH: the dilations are by the same n² (Γ_T identical, independence identical); the coefficient
vector −L'/L of DH is supported on all n, so P_DH is non-separable. Hence independence cannot separate ζ from DH; only
separability does. (ii) But separability is shared by: deletions/κ at prime powers, Λχ₂ (P_{Λχ} = P_Λ(χ(p)z_p), a
torus translate), and Beurling systems with free generators, including the Diamond–Montgomery–Vorhauer systems with
zeros off the line (00-references/beurling-dmv); these have first contacts (R162_1001, R162_702 support-class
blindness). Moreover the 𝔈 log Z form of Prop 3.1(b) holds verbatim for Λχ₂ and Beurling. So neither independence nor
separability nor 𝔈 log Z passes F3. (iii) Non-integer (Beurling) dilations change Γ_T but not Thm 2.1, Prop 2.2,
Thm 3.2 (for free generators) or Thm 4.2. (iv) Deletion/κ at composite n breaks separability, but R162_204 shows the
regularised jet is invariant under every finite modification, so separability of the finite window vector is itself
not read by Gate 1 at fixed T_*.
**F1.** λ enters (RH) only as c_0 ↦ c_0 − λ, a scalar commuting with ℂ[Γ_T], with ι and with the running transform;
every structure above is λ-blind and holds for eigenvectors with λ > 0, where x_m ≠ 0 (Müntz). H ≥ 0 is the
inequality c_0 ≥ 𝒦 + C on P_T; in q-language it is a Plemelj energy ∫_Γ jump·(RH-left side) ≥ 0 whose kernel κ is
completely monotone (Σ δ_{a_k}); that is exactly the Kreĭn/Stieltjes residual handed to R162_1301, not a q-difference
statement.
**F2.** (RH) is linear; no orientation. **F4.** Everything is exact at finite T_* (finite Γ_T, finite comb);
not a graph limit.

## 6. Verdict

**NO-GO (PROVED).** The q-difference RH problem is written exactly (Thm 2.1): jump πiF on Γ, arithmetic part the
group-algebra element L_Λ ∈ ℂ[Γ_T], archimedean part the finite-part endpoint value of the running Cauchy transform
composed with the inversion q ↦ 1/q; connection 0 ↔ ∞ = interlaced even/odd Gamma lattices of X_F (Prop 2.2). The
dictionary is a bijective change of unknowns, so Gate 1 ⟺ ĝ ≡ 0 ⟺ N = {0} (E1). The hoped-for mechanism fails in a
precise way: independence of prime dilations gives *maximal* monodromy (Thm 3.2), i.e. no constraint, and is a
property of ℕ shared by DH; the arithmetic Liouville theorem (Thm 4.1, Schäfke–Singer type) needs one equation per
prime, whereas (RH) is one additive equation whose archimedean term couples all primes through one Mellin variable,
and the cut destroys the group action (Thm 4.2). The Euler product appears as separability of the Laurent symbol and
Λ*1 = log as P_Λ = 𝔈 log Z (Prop 3.1) — both shared by Λχ₂ and Beurling DMV (F3 fails), both λ-blind (F1 fails).

**Residual (sharp).** A closing Liouville argument would need a *consistent system*: for each prime p a separate
relation satisfied by some object built from F ∈ N. The only per-prime objects in the corpus are the one-prime Euler
stripping increments (R162_201) and the torsion cocycle ℒ_pΦ − Φ = log p(δ_0 − Leb) (R162_1001, the one object that
fails for Λχ₂ and Beurling). Candidate: a per-prime q-difference relation for the torsion distribution Φ_Λ paired
with ĝ, which would put Thm 4.1 in play. Not attempted; check R162_1101 (torsion atoms collapse to Sonin range) first.

Add to R162_590 §1c: "q-difference RH problem / dilation-group Liouville — R162_1302 — maximal monodromy, single
additive equation, cut breaks the action; separability shared by Λχ₂, Beurling | F1, F3, E1".

Files edited: this file only.
