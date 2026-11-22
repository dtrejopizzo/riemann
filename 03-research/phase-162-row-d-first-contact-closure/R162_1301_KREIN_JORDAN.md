# R162_1301 — Kreĭn/Jordan chains at the bottom via complete monotonicity of κ — **NO-GO (PROVED)**, with two exact structures

Note. Inputs: README (F1–F4, rounds 1–12), R162_590, R162_1201 (§§1–6,
residual), R154_004 (Thm S1, Cor S2), Paper 46 lem:K / thm:S, thm:KEP3, R155_040, R155_046, R160_S3/S4 surveys.

**Labels.**
- Thm 1 (Bernstein/string decomposition of M_I; exterior far field = negative exterior string energy) PROVED. **New form.**
- Lemma 2 (the Jordan resonance is exactly half-saturating for its own string) PROVED. New, minor.
- Thm 3 (Kreĭn Q-function / Douglas form of Gate 1: an inequality that uses λ = 0 as the bottom) PROVED. **Restatement (E1)**, but the first inequality form of Gate 1 in the corpus that passes F1 as a statement.
- Thm 4 (anti-coercivity: the archimedean CM structure gives x_m only upper bounds) PROVED.
- Thm 5 (NO-GO: transport to DH, deletion/κ, Λχ₂, Beurling) PROVED.
Gate 1 OPEN. No label moves.

## 0. Corpus check (done before building)

grep "completely monotone|Bernstein|Kreĭn|Krein|Pontryagin|isotropic|Jordan chain|string|Stieltjes" in phases 15, 150–162,
Paper 46, R160_S1–S5:
- CM of κ and complete-Bernstein φ: **known** — R154_004 Thm S1/Cor S2 (ν(u) = Σ_k e^{−(2k+½)|u|}, pure-jump subordinate
  BM), Paper 46 lem:K/thm:S (m(τ) = C₀ + ∫(1−cos τu)K). Subordination bound S3 is an *upper* bound on λ_min.
- CM ⟹ log-convex ⟹ not PF₂ (Karlin/nodal route): **closed**, R155_046 (R160_S4 item 45).
- Kreĭn *extension problem* / indeterminacy: thm:KEP3 = RH, R155_040 (R160_S4 item 48): restatement.
- Kreĭn *space* / Pontryagin index κ = number of off-line zeros: phase 15/16, Papers 08/11, G1_P3_R4 (K5 = restatement):
  detectors, not forcers (R162_590 rows 21, 24).
- Kreĭn strings / canonical systems / de Branges: arcs I–II, R160_S5 B8 (Romanov chains): equivalences.
- "Jordan chain" in phase 158 (R158_006 Thm J_K) is on Meyer's space (zeros), unrelated to the Gamma-lattice resonance.
Not found anywhere: the Robin-string form of M_I (Thm 1), the Q-function form of Gate 1 at the Gamma lattice (Thm 3).

## 1. Lines first (what any closing inequality must be)

- (L1, F1) It must use that 0 is the **bottom** of σ(H), not merely an eigenvalue: an identity or linear consequence of HF=0
  also holds for λ>0 eigenvectors, where x_m ≠ 0 (R162_1201 Thm 5.1(i)).
- (L2, F3-DH) DH: κ_DH(u) = Σ_k e^{−(2k+3/2)|u|} = e^{−|u|}κ(u) is again CM (Bernstein measure σ_DH = σ(·−1)); DH has
  first contacts with x ≠ 0 (R162_102). So CM of the archimedean kernel cannot be the sign.
- (L3, F3-deletion/Beurling) Same κ, comb weights still ≥ 0, first contacts exist (R162_702, thm:finmod). So
  "CM archimedean part minus a nonnegative comb" cannot be the sign.
- (L4, F3-Λχ₂) Same κ, signed comb.
Hence a Λ-specific inequality must read something of the comb beyond positivity; CM can at most organise the archimedean side.

## 2. Bernstein/string decomposition (Thm 1)

Bernstein: κ(u) = ∫ e^{−a|u|} dσ(a), σ = Σ_{k≥0} δ_{a_k}, a_k = 2k+½. Each e^{−a|u|} has Fourier transform 2a/(a²+τ²),
and ∫_ℝ(1−cos τu)e^{−a|u|}du = 2τ²/(a(a²+τ²)) ≥ 0. So (normalisation of Paper 46 lem:K; this is R154_004 S1 with x=τ²)

  m(τ) = C₀ + Σ_{k≥0} 2τ²/(a_k(a_k²+τ²)),   i.e. M = C₀ + Σ_k (2/a_k − P_{a_k}),  P_a = conv. by e^{−a|·|}.   (2.1)

(The divergent Σ 2/a_k is the finite part of R162_1201 Lemma 1.1; each summand is bounded and ≥ 0; the series is
O(k^{−3}) at fixed τ.)

**Thm 1.** (i) On I = (−T,T), P_{a,I} = 2a(a² + L_a)^{−1}, where L_a = −d²/dt² with Robin conditions f'(T) = −a f(T),
f'(−T) = a f(−T); L_a ≥ 0 with form ∫_I|f'|² + a(|f(T)|²+|f(−T)|²). Hence the compressed archimedean operator is the
positive string sum
  M_I = C₀ + Σ_{k≥0} (2/a_k) L_{a_k}(a_k² + L_{a_k})^{−1}.
(ii) For F ∈ L²(I), f_k := e^{−a_k|·|} * F (on ℝ), x_k = ∫F e^{a_k u}, x̃_k = ∫F e^{−a_k u} (= εx_k on parity vectors):
  ⟨(2/a_k − P_{a_k})F,F⟩ = (2/a_k)‖F‖² − (1/2a_k)∫_I(a_k²|f_k|² + |f_k'|²) − ½e^{−2a_kT}(|x_k|² + |x̃_k|²).
So the Gamma data x_k are exactly the **exterior energies** of the k-th string potential, entering the archimedean form
with a **minus** sign, and the full form is
  𝔥(F) = C₀‖F‖² + Σ_k[(2/a_k)‖F‖² − (1/2a_k)E_{I,k}(f_k)] − ½Σ_{k≥1} e^{−2a_kT}(|x_k|²+|x̃_k|²) − ⟨C_IF,F⟩  (k=0 exterior
  term vanishes on P_T by primitivity).
*Proof.* (i) f = P_{a,I}g solves a²f − f'' = 2ag on I; differentiating ∫_I e^{−a|t−u|}g(u)du at t = ±T gives the Robin
conditions; integration by parts gives the form. (ii) (a²−D²)f_k = 2a_kF on ℝ, so ⟨P_{a_k}F,F⟩ = (1/2a_k)∫_ℝ(a²|f|²+|f'|²);
on t > T, f_k(t) = e^{−a_kt}x_k, whose energy on (T,∞) is a_k e^{−2a_kT}|x_k|²; same at −T with x̃_k. ∎

## 3. The Jordan resonance in string form (Lemma 2)

For v = e^{at}1_I, P_{a,I}v = ((1+2aT)/(2a) − t)e^{at} − e^{−2aT}e^{−at}/(2a) (checked symbolically). The (T−t)e^{at}
term is the secular term of R162_1201 (2.1): e^{a_m t} is annihilated by a_m²−D² but violates the Robin condition at +T,
so it is a *boundary* (defect-space) resonance, not an eigenvector of any piece.
**Lemma 2.** ⟨(2/a−P_a)v,v⟩/‖v‖² → 1/a as T → ∞ (exact closed form at finite T). The m-th string on its own resonance
sits at half of its norm 2/a_m: neither neutral (0) nor saturating. There is no isotropy to exploit: all pieces are
positive operators, the ambient form is definite, and an "H-isotropic" vector v (𝔥(v) = 0) is, by Cauchy–Schwarz for
H ≥ 0, simply an element of N. The Pontryagin/Kreĭn indefinite form one can build from the boundary triple
(Γ₀f = f(±T), Γ₁f = f'(±T), signature (2,2)) is the standard Green form of the Robin strings; its negative directions are
exactly the exterior traces of Thm 1(ii), i.e. x_k again. So "Jordan chain isotropic at the bottom" ⟺ "x_m-direction in N":
a rewording of Gate 1, not a mechanism.

## 4. The inequality form that genuinely uses λ = 0 (Thm 3)

Let e_m := Πe^{a_m t}1_I, q_m(z) := ⟨(H−z)^{−1}e_m,e_m⟩ (Kreĭn Q-function of the rank-one extension along e_m; Nevanlinna).
**Thm 3.** H has compact resolvent on P_T (form weight log(2+|τ|) → ∞ on functions supported in a bounded interval:
Kolmogorov–Riesz). For S ⊂ ℕ with Σ_S 1/m = ∞ the following are equivalent:
 (a) N = {0} (Gate 1 at T_*);
 (b) x_m = 0 on N for all m ∈ S (R162_1201 Thm 4.1);
 (c) for every m ∈ S, q_m(0−) = lim_{ε↓0}⟨(H+ε)^{−1}e_m,e_m⟩ < ∞;
 (d) (Douglas/Kreĭn inequality) for every m ∈ S there is C_m with |⟨G,e_m⟩|² ≤ C_m 𝔥(G) for all G in the form domain.
Moreover −Res_{z=0} q_m = Σ_j |x_m(F_j)|² over an ONB of N.
*Proof.* Spectral theorem: q_m(−ε) = Σ_j |⟨e_m,φ_j⟩|²/(λ_j+ε) is increasing as ε↓0 and finite in the limit iff the λ_j=0
terms vanish (λ_j ≥ λ_1' > 0 otherwise, discreteness). (c)⟺(d): (d) ⟺ e_m ∈ ran H^{1/2} (Douglas), and
sup_G|⟨G,e_m⟩|²/(𝔥(G)+ε‖G‖²) = q_m(−ε). (b)⟺(a) is Müntz–Szász. ∎

Why it matters for F1: (c)/(d) are statements about the **bottom** only; a λ>0 eigenvector produces a pole of q_m inside
the spectrum and is invisible to q_m(0−). (d) is an *inequality* (not an identity) in which Λ enters through 𝔥. This is
the correct target shape asked for in R162_1201 §6. But it is equivalent to Gate 1 (E1): proving (d) for a divergent S
is the whole problem.

## 5. Anti-coercivity (Thm 4): CM cannot supply (d)

**Thm 4.** (i) Every archimedean piece gives |x_k(G)|² ≤ (4/a_k)e^{2a_kT}‖G‖² (from Thm 1(ii) and ≥ 0): upper bounds only.
(ii) (d) holds with 𝔥 replaced by the archimedean form 𝔞 = ⟨ΠM_IΠG,G⟩ (M_I ≥ C₀, compact resolvent, so e_m ∈ ran 𝔞^{1/2}),
with C_m^{arch} = q_m^{arch}(0). The entire content of (d) is the comb: (d) ⟺ sup_G |⟨G,e_m⟩|²/(𝔞(G) − ⟨C_IG,G⟩) < ∞,
i.e. the comb must not saturate 𝔞 along any direction with x_m ≠ 0.
(iii) In Thm 1(ii) the x_k enter 𝔞 with the minus sign: directions with large Gamma data are *cheaper* archimedeanly. So
the CM structure pushes the minimiser toward x ≠ 0, not away; any inequality derived from CM of κ plus H ≥ 0 bounds x
from above by 𝔥-independent quantities and cannot force x = 0.
*Proof.* (i), (iii) read off Thm 1(ii); (ii) as Thm 3 with H replaced by ΠM_IΠ. ∎

## 6. NO-GO (Thm 5) and falsifiers

**Thm 5.** Thms 1–4 hold verbatim for: DH (σ_DH = σ(·−1), κ_DH = e^{−|u|}κ CM; lattice 2m+3/2; no Tate pair at ½ but the
string structure and signs are unchanged — shifting the Bernstein measure right decreases every piece
2τ²/(a(a²+τ²)) pointwise (∂_a < 0), an order relation, not a sign change); deletion/κ and Beurling (same κ, comb ≥ 0);
Λχ₂ (same κ, signed comb). DH and the deletion models have first contacts with x_m ≠ 0, hence q_m(0−) = ∞ there.
Therefore no inequality using only {CM of κ, Robin-string positivity, H ≥ 0, λ = 0 as bottom, sign of the comb} closes Gate 1.

- **F1.** Passed at the level of the statement (Thm 3 is bottom-only), not at the level of proof: no bound on q_m(0−) is
  produced.
- **F2.** Thm 3(d) is quadratic in G through 𝔥, invariant under the comb orientation only via 𝔥 itself; no orientation added.
- **F3.** Failed (Thm 5) for every structural input used here.
- **F4.** Everything is exact at finite T_* (finite comb, geometric Gamma sums, Robin strings on I); no graph limit.

## 7. Verdict and residual

**NO-GO (PROVED).** Complete monotonicity turns the archimedean operator into a positive sum of Robin strings, and the
Gamma data x_k into the exterior energies of those strings, with a minus sign (Thm 1): the Jordan resonance is a boundary
defect of the k-th string, half-saturating (Lemma 2), and "H-isotropy of the chain" is just membership in N. The correct
bottom-sensitive inequality is the Kreĭn Q-function/Douglas bound (Thm 3(d)), equivalent to Gate 1, whose whole content
is that the comb does not saturate the archimedean form along x_m-directions (Thm 4(ii)); CM gives the opposite
tendency (Thm 4(iii)) and transports to DH, deletion, Λχ₂, Beurling (Thm 5).

**Residual (sharp).** Bound q_m(0−) = sup_G |x_m(G)|²/𝔥(G) uniformly on a harmonic-divergent S using a property of the
Λ-comb that deletions and DH lack (Λ*1 = log / the ×p torsion cocycle of R162_1001), *after* the string decomposition:
e.g. a comparison 𝔠(G) ≤ 𝔞(G) − c_m|x_m(G)|² where the comb is realised as a string-boundary coupling. Not attempted.

Add to R162_590 §1c: "Kreĭn/Jordan via CM of κ (Robin-string decomposition, Q-function form of Gate 1) — R162_1301 —
isotropy = membership in N; Douglas bound ⟺ Gate 1; CM anti-coercive; transports to DH/deletion/Λχ₂/Beurling | E1, F3".

Files edited: this file only.
