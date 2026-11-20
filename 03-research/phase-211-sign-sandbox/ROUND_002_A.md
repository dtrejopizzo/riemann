# Round 002 A — Coercivity floor of the complement block A_𝒞𝒞, the floor-only Schur inequality, and the mesh form of near-coincidence

Object: the exact two-sector reduction (L2′) of ROUND_001_C (Theorem 1, Lemmas 1–3), at T = ½log5 + ε and at T = 1, 1.25.
Notation as there: ω_k = πk/2T, s_k = s^{α,c}_k = s_T(ω_k + α) + c(−1)^k (here α = 0), even coordinates c_j = ⟨F, e_j⟩,
odd coordinates (Hc)_l = ⟨F, e'_l⟩, H = (h_{l−j}) real unitary, h_m = 2(−1)^m/(π(2m+1)),
a_T(F) = ⟨c, A c⟩, A = ½(D_e + HᵀD_oH), 𝒩 = {k : s_k ≤ 0}, 𝒞 = P_T ∩ 𝒩_η^⊥, S = A_{N′N′} − A_{N′𝒞}A_{𝒞𝒞}^{−1}A_{𝒞N′}.
x_n := log n/2T, A_T = Σ_{n∈N_T} v_n, ε_T = ∫_{2T}^∞ K.

---------------------------------------------------------------------------------------------------
## 0. Corpus check

- ROUND_001_C §2 ("cost of shrinking the block"), §4 and its "Next concrete step": the complement constant there is
  c_* = ½(s^e_+ + s^o_+), and the smallest positive gauged sample was reported as 8.8·10⁻⁵.
- Routes-tried index (04_PHASES_100-189 lines 70–72): S^low_η certificate (PARTIAL/NO-GO for all T because d_η ≳ λ_A^{−1/p}),
  circulant cone (FALSIFIED), pointwise Nyquist positivity (false). README line 392: a layer-cake device appears inside
  the class 𝓒_G (min/hyperbola balance), a different object.
- Grid R162_2300 item 41: exact Nyquist identity, S^low numerics. No entry on a coercivity floor of the exact
  complement block, on the two-projection bound with the H-coupling, or on the mesh near-coincidence identity.
What differs: S^low_η removes the complement inverse by an inversion-free bound at large η; here the exact Schur
complement at η ↓ 0 is kept and only A_𝒞𝒞 is bounded below, by a new bound (Theorem F) built from the angle between
the even and odd shallow-sample subspaces. The recorded failure of S^low (dimension blow-up at large η) does not apply
because the block is the minimal one. The failure that does apply is found below (Proposition L) and is new.

---------------------------------------------------------------------------------------------------
## 1. Correction of the data of ROUND_001_C §4 [NUMERICAL, re-checked]

At T = ½log5 + 10⁻⁴, α = 0, the gauges with the minimal count 11 form the interval c ∈ [1.211, 1.237] (grid step 10⁻³).
- The sample 8.8·10⁻⁵ is k = ±18 (even sector) at the left end c = 1.211 of that interval. It is an artefact of the
  choice of c inside the interval: at c = 1.224 the smallest positive samples are s_{18} = 0.01309 (even) and
  s_{1} = 0.01324 (odd); the maximal η_0 over the interval is ≈ 0.0131.
- The modes k = 102, 144, 158 (mesh images of 2^54 ≈ 3^34, 2^49 ≈ 3^31) are raw-negative EVEN samples; the gauge adds
  +c to every even sample, and their gauged values are 1.205, 1.104, 0.913 (c = 1.211), i.e. they are of order one, not
  small. The statement of ROUND_001_C §4 that the deep near-coincidences "sit as small positive samples" in the
  complement is false at this window. The near-coincidences moved into the complement as samples of size ≈ c − |raw|,
  not as small samples. The small positive samples (k = 1, 6, 18, 32, 56 at c = 1.211–1.237) are low modes, unrelated to
  deep coincidences.
Block at c = 1.224: even k ∈ {0, ±14}, odd k ∈ {±3, ±5, ±9, ±23}, as in ROUND_001_C.

---------------------------------------------------------------------------------------------------
## 2. The coercivity floor

For t > 0 let W_t := {k ∉ 𝒩 : 0 < s_k ≤ t} (finite, since s_k → +∞; ROUND_001_C Theorem 1), split as W^e_t (even k = 2j)
and W^o_t (odd k = 2l+1), and let G_t := [h_{l−j}]_{2j∈W^e_t, 2l+1∈W^o_t} (a finite real matrix; G_t := 0 if one of the two
sets is empty).

**Lemma P (two projections). [PROVED]** For orthogonal projections P, Q on a Hilbert space and every x,
‖Px‖² + ‖Qx‖² ≤ (1 + ‖PQ‖)‖x‖².
Proof. Let ‖x‖ = 1, u = Px, v = Qx, Σ := ‖u‖² + ‖v‖². Then Σ = ⟨x, u + v⟩ ≤ ‖u + v‖, and
‖u+v‖² = Σ + 2Re⟨Px, Qx⟩, with |⟨Px,Qx⟩| = |⟨Px, PQ Qx⟩| ≤ ‖PQ‖‖u‖‖v‖ ≤ ½‖PQ‖Σ. So Σ² ≤ (1 + ‖PQ‖)Σ. ∎
(The bound is sharp: ‖P + Q‖ = 1 + ‖PQ‖.)

**Theorem F (coercivity floor of the complement). [PROVED]** For every F ∈ 𝒟_T ∩ 𝒩_η^⊥ (in particular on 𝒞),
a_T(F) ≥ c_floor ‖F‖², c_floor := ½ ∫_0^∞ (2 − ν_t) dt,
ν_t := 0 if W^e_t = W^o_t = ∅; 1 if exactly one of them is empty; 1 + ‖G_t‖ if both are nonempty.
The integrand lies in [0, 2]. With s^e_+, s^o_+ the smallest positive even and odd samples,
c_floor ≥ ½(s^e_+ + s^o_+) = c_* (the constant of ROUND_001_C Theorem 1), with strict gain ½∫_{max(s^e_+,s^o_+)}^∞ (1 − ‖G_t‖)dt,
and for every finite partition 0 = t_0 < … < t_R, c_floor ≥ ½ Σ_r (t_r − t_{r−1})(2 − ν_{t_r}) (computable from finitely many
samples and entries of H; exact up to t_R when the partition contains all sample values below t_R).
Proof. On 𝒩_η^⊥ the coordinates c_j (2j ∈ 𝒩) and (Hc)_l (2l+1 ∈ 𝒩) vanish, so 2a_T(F) = Σ'_j s_{2j}|c_j|² + Σ'_l s_{2l+1}|(Hc)_l|²
with only positive samples (ROUND_001_C, Explicit data of S; absolutely convergent for F ∈ 𝒟_T). Write s = ∫_0^∞ 1[s > t] dt
and use Tonelli:
2a_T(F) = ∫_0^∞ ( Σ_{s_{2j}>t}|c_j|² + Σ_{s_{2l+1}>t}|(Hc)_l|² ) dt.
For fixed t, let P_t be the coordinate projection onto {j : 2j ∈ W^e_t ∪ 𝒩} and Q_t onto {l : 2l+1 ∈ W^o_t ∪ 𝒩}. The coordinates
with indices in 𝒩 vanish, and ‖Hc‖ = ‖c‖ (H unitary), so the integrand equals
2‖c‖² − ‖P_t c‖² − ‖Q_t Hc‖² = 2‖c‖² − ‖P′_t c‖² − ‖H*Q′_tH c‖²,
P′_t, Q′_t the projections onto the indices in W^e_t, W^o_t only. P′_t and H*Q′_tH are orthogonal projections and
‖P′_t H*Q′_t H‖ = ‖P′_t H* Q′_t‖ = ‖G_t‖. If both are nonzero, Lemma P gives ‖P′_tc‖² + ‖Q′_tHc‖² ≤ (1 + ‖G_t‖)‖c‖²; if one is
zero the sum is ≤ ‖c‖²; if both are zero it is 0. So the integrand is ≥ (2 − ν_t)‖c‖² ≥ 0, and ‖c‖ = ‖F‖. ∎ For t below
min(s^e_+, s^o_+) the integrand is 2, between the two minima it is 1, which gives c_floor ≥ c_*. ν_t is non-decreasing in t,
which gives the partition bound.

**Corollary F1 (explicit Schur-test version). [PROVED]** |h_{l−j}| = 2/(π|k_o − k_e|) with k_e = 2j, k_o = 2l+1. Hence
‖G_t‖ ≤ (max_{k∈W^e_t} Σ_{k′∈W^o_t} 2/(π|k−k′|) · max_{k′∈W^o_t} Σ_{k∈W^e_t} 2/(π|k−k′|))^{1/2}.
So the floor can be small only if, at every level t ≳ c_floor, the shallow set W_t contains even and odd indices at
bounded mesh distance in sufficient number. A single isolated shallow sample of either parity costs nothing.

**Theorem F does what was asked.** The floor does not collapse to the smallest sample: a single small sample in one
sector costs at most half its deficit, the other sector carries ½·(its smallest sample), and the layer integral adds the
contribution of all levels at which the shallow even and odd subspaces are at a positive angle. The coupling H lifts the bottom exactly by the angle
between the shallow even and the shallow odd subspaces.

**NUMERICAL (validation).** Partition of [0, 1.5] into 60 steps, exact ‖G_t‖:

| T | gauge c | block dim | η_0 (smallest positive sample) | c_* (ROUND_001_C) | single level max_t t(1−‖G_t‖)/2 | c_floor (Thm F, levels ≤ 1.5) | λ_min(A_𝒞𝒞), truncated model |
|---|---|---|---|---|---|---|---|
| ½log5 + 10⁻⁴ | 1.224 | 11 | 1.31·10⁻² | 0.013 | 0.115 | 0.156 | 1.109 |
| ½log5 + 10⁻⁴ | 1.211 | 11 | 8.8·10⁻⁵ | 0.013 | — | 0.147 | — |
| 1 | 0.585 | 41 | 3.8·10⁻⁴ | — | 0.199 | 0.251 | 1.018 |
| 1.25 | −0.24 | 125 | 4.4·10⁻³ | — | 0.221 | 0.338 | not computed |

(Truncated model: |j| ≤ 600–1500, |l| ≤ 4000–12000; compression, so its λ_min is an upper estimate of the true one; the
value was stable under doubling.) At ½log5 + ε with the left-end gauge 1.211, η_0 = 8.8·10⁻⁵ but c_floor = 0.147: the floor is insensitive to it.
The floor grows with T in these data; the shallow samples of opposite parity are separated on the mesh (‖G_{0.2}‖ = 0.23,
0.10, 0.045 at the three windows) and only become strongly coupled at t ≈ 0.3–0.8.

---------------------------------------------------------------------------------------------------
## 3. The sufficient inequality and its exact limit

**Proposition S (floor-only Schur inequality). [PROVED]** Let 0 < c ≤ λ_min(A_𝒞𝒞) (e.g. c = c_floor). If
(I_c)  a_T(x) ≥ c^{−1} ‖P_𝒞 A x‖²  for all x ∈ N′,
then S ⪰ 0 and λ_A(T) ≥ 0. Here ‖P_𝒞Ax‖² = sup_{y∈𝒞∩𝒟_T, ‖y‖=1}|a_T(x,y)|², and (I_c) reads
A_{N′N′} − c^{−1} A_{N′𝒞}A_{𝒞N′} ⪰ 0, an inequality on a matrix of size dim N′ ≤ 11 whose entries are: the block samples
(through A_{N′N′}), the coupling entries ⟨Ax, y⟩ (absolutely convergent series in s_k and h_m, ROUND_001_C), and c.
Proof. For x ∈ N′, y ∈ 𝒞∩𝒟_T: a_T(x+y) = a_T(x) + 2Re a_T(x,y) + a_T(y) ≥ a_T(x) − 2‖P_𝒞Ax‖‖y‖ + c‖y‖² ≥ a_T(x) − ‖P_𝒞Ax‖²/c.
Take the infimum over y (ROUND_001_C Theorem 1(ii)). ∎

**Proposition L (limit of the class). [PROVED]** (i) (I_c) is monotone in c, so the best member of the class is
c = λ_min(A_𝒞𝒞) =: C, and no floor can do better. (ii) If (I_C) holds, then for every x ∈ N′, with b = P_𝒞Ax,
S(x) ≥ ⟨b, (C^{−1} − A_𝒞𝒞^{−1}) b⟩ ≥ 0.
So the class certifies S ⪰ 0 only with a margin: at every x, S(x) must dominate the defect of replacing A_𝒞𝒞^{−1} by
its top eigenvalue on b. When S has eigenvalues near 0 (near-threshold windows) the class can certify only if b lies
(almost) in the bottom eigenspace of A_𝒞𝒞.
Proof. (i) c ↦ c^{−1} is decreasing. (ii) S(x) = a_T(x) − ⟨b, A_𝒞𝒞^{−1}b⟩ (Theorem 1 of ROUND_001_C; A_𝒞𝒞 ≥ C > 0 so its
Friedrichs inverse is bounded with norm ≤ C^{−1}), and (I_C) gives a_T(x) ≥ C^{−1}‖b‖². ∎

**NUMERICAL (validation only; method test).** Truncated model as above, exact Tate constraints.
- T = ½log5 + 10⁻⁴, c = 1.224, dim N′ = 11: ‖A_{N′𝒞}‖ = 0.67; λ_min of A_{N′N′} − c^{−1}A_{N′𝒞}A_{𝒞N′} at c = 0.115 (single-level floor) = −2.94; the
  smallest c for which (I_c) holds is c_need = 2.10, larger than λ_min(A_𝒞𝒞) ≈ 1.11. By Proposition L(i) NO floor
  certifies this window, not even the exact λ_min. The eigenvalues of S in the model are ≤ 3·10⁻⁵ in four directions
  (near-threshold), which is the mechanism of Proposition L(ii).
- T = 1, c = 0.585, dim 41: ‖A_{N′𝒞}‖ = 1.08, c_need = 3.54, λ_min(A_𝒞𝒞) ≈ 1.02, c_floor = 0.251. Fails by a larger factor
  (c_need/λ_min: 1.9 at ½log5, 3.5 at 1).
- T = 1.25: not computed (block reaches |k| ≈ 9·10³; the model needs |j| ≳ 5·10³).
Answer to (2): the inequality does not certify the sign at ½log5 + ε (where it is known by other means); what defeats it
is not a collapse of c_floor at the near-coincidence modes (there is none: c_floor grows from 0.156 to 0.338 between ½log5
and 1.25, and the 2^b ≈ 3^a modes are not shallow), but the Cauchy–Schwarz loss of Proposition L, which grows with T.

---------------------------------------------------------------------------------------------------
## 4. Mesh form of the near-coincidence principle

**Proposition M (sample identity). [PROVED]** For every k ∈ ℤ and gauge c,
s_k = m(ω_k) + r_T(ω_k) − A_T + c(−1)^k + 2 Σ_{n∈N_T} v_n sin²(π k log n /(4T)),
and with ‖·‖ the distance to ℤ,
8 Σ_n v_n ‖k log n/4T‖² ≤ s_k − m(ω_k) − r_T(ω_k) + A_T − c(−1)^k ≤ 2π² Σ_n v_n ‖k log n/4T‖².
Equivalently the gauge is a fictitious contact at u = 2T of weight −c: c(−1)^k = c − 2c sin²(πk/2).
Proof. cos(πk x_n) = 1 − 2sin²(πk x_n/2) with k x_n/2 = k log n/4T, Σ v_n = A_T; 4‖y‖² ≤ sin²(πy) ≤ π²‖y‖². ∎

**Corollary M1 (depth forces simultaneous near-integrality). [PROVED]** If s_k ≤ σ then
D_k := Σ_n v_n ‖k log n/4T‖² ≤ (σ + A_T + ε_T − c(−1)^k − m(ω_k))/8,
and m(ω_k) ≥ log(ω_k/2π) − 1/ω_k − 1/(2ω_k²) (lem:mbounds). So a nonpositive sample at large k requires k log n/4T to be
within O(((A_T + ε_T − c(−1)^k − log(k/4T))/8v_n)^{1/2}) of an integer for EVERY n ∈ N_T simultaneously (the depth budget
shrinks like the gap A_T − log k). Conversely, if D_k ≤ δ then s_k ≤ m(ω_k) + ε_T − A_T + c(−1)^k + 2π²δ.

**Corollary M2 (the integer coincidence behind a deep sample). [PROVED]** Let q_n be the integer nearest to k log n/4T and
δ_n = k log n/4T − q_n. For n, n′ ∈ N_T,
|log(n′^{q_n} / n^{q_{n′}})| = |δ_{n′} log n − δ_n log n′| ≤ |δ_n| log n′ + |δ_{n′}| log n.
Proof: q_n log n′ − q_{n′} log n = −δ_n log n′ + δ_{n′} log n (the term k log n log n′/4T cancels). ∎
So a deep sample at k produces the integer near-coincidence n′^{q_n} ≈ n^{q_{n′}} (two integers M ≈ M′ with
M = n′^{q_n}, M′ = n^{q_{n′}}), with relative error ≤ |δ_n| log n′ + |δ_{n′}| log n ≤ C(D_k)^{1/2}. Example k = 158 at ½log5+ε:
q_2 = 34, q_3 = 54, 3^34/2^54 = e^{−0.15}; k = 144: q_2 = 31, q_3 = 49, 3^31/2^49 ≈ e^{−0.09}. This is the mesh form of
m ≈ k·n of STATEMENT_001 §4: the mesh sees a near-coincidence among the multiplicative semigroup generated by N_T
whenever 4T/k lies near a common "period". The sign of the cosine enters through the parity of q_n: near-integrality of
k log n/2T with q odd gives a POSITIVE contribution 2v_n; deep negativity needs near-integrality at the half-scale k log n/4T.

**Corollary M3 (what sets the floor). [PROVED from Theorem F + Proposition M]** c_floor depends only on the level sets
W_t, and by Proposition M, k ∈ W_t forces D_k ≤ (t + A_T + ε_T − c(−1)^k − m(ω_k))/8. Deep coincidences
(D_k small) with the gauge sign c(−1)^k ≥ 0 have s_k ≈ c − |raw| and, by Theorem F, affect c_floor only through ‖G_t‖ at
t ≈ s_k. A collapse of c_floor needs shallow samples of OPPOSITE parity at bounded mesh distance at every level t ≳ c_floor
(Corollary F1). Two samples k, k+1 differ by one mesh step, which moves every k log n/4T by x_n/2 ∈ [log2/4T, ½): the
near-integrality pattern of Corollary M1 is not preserved under k ↦ k+1, so a single near-coincidence does not produce an
adjacent opposite-parity pair. [ARGUED: no quantitative version; a pair (k,k+1) both shallow requires a second, unrelated
Diophantine event, and the data show ‖G_{0.2}‖ ≤ 0.23 at all three windows.] Answer to the scaling question: the near-coincidence
collapse at 2^b ≈ 3^a, 2^b ≈ 5^a, 3^b ≈ 5^a does not defeat the floor; it is not where the bottom of A_𝒞𝒞 lives.

---------------------------------------------------------------------------------------------------
## 5. Falsifier test

Theorem F, Lemma P, Corollary F1, Propositions S, L, M and Corollaries M1–M2 are statements about an arbitrary sample
sequence (any weights v_n ≥ 0, any gauge); they hold verbatim for (a) cΛ, (b) a_P, (c) Beurling systems, (d) finite
modifications. None of them is a sign step, and none claims one. Proposition S is a sufficient condition: for a falsifier
system with λ_A(T) < 0 at a window, (I_c) is false there for every c ≤ λ_min(A_𝒞𝒞) (it would otherwise imply S ⪰ 0), so it
cannot certify a falsified window; this is soundness, not sign content. Any sign step built on (I_c) would have to come
from the arithmetic of the coupling vectors b = P_𝒞Ax, which this memo does not supply.

---------------------------------------------------------------------------------------------------
## Result

PROVED piece, with a NO-GO for a method class.
PROVED piece: Theorem F, an explicit coercivity floor for the complement block, c_floor = ½∫(2 − ν_t)dt ≥ c_*,
computable from finitely many samples and entries of H; it does not collapse to the smallest sample (0.156, 0.251, 0.338 at
½log5+ε, 1, 1.25 vs η_0 = 1.3·10⁻², 3.8·10⁻⁴, 4.4·10⁻³; NUMERICAL values). Proposition M: the exact identity between gauged
samples and simultaneous near-integrality of {k log n/4T}, with the integer near-coincidence n′^{q_n} ≈ n^{q_{n′}} behind every
deep sample.
NO-GO (class: floor-only Schur inequalities (I_c), i.e. any certificate that replaces A_𝒞𝒞^{−1} by a scalar ≤ λ_min(A_𝒞𝒞)^{−1}):
Proposition L shows the class needs a margin S(x) ≥ ⟨b,(C^{−1} − A_𝒞𝒞^{−1})b⟩; NUMERICAL: it fails already at ½log5 + ε
(c_need = 2.10 > λ_min(A_𝒞𝒞) ≈ 1.11) and the gap grows at T = 1 (3.54 vs 1.02).

## What was proved

- Lemma P (two-projection bound), Theorem F (layer-cake floor via the H-angle), Corollary F1 (Schur-test version).
- Proposition S (sufficient finite inequality with block samples, coupling entries and a floor) and Proposition L (its best
  member is c = λ_min(A_𝒞𝒞); the margin it requires).
- Proposition M and Corollaries M1–M2 (mesh form of the near-coincidence principle; deep samples ⟹ n′^{q_n} ≈ n^{q_{n′}}).
- Correction: the 8.8·10⁻⁵ sample is k = 18 at the end of the gauge interval; the 2^b ≈ 3^a modes are not shallow.

## What failed and why

- The floor-only Schur inequality: replacing A_𝒞𝒞^{−1} by a scalar loses the alignment of b = P_𝒞Ax with the spectrum of
  A_𝒞𝒞, and the near-zero directions of S leave no margin. This is not a conditioning collapse; c_floor is fine.
- No sign: everything here is comb-generic (§5).
- Quantitative separation of opposite-parity shallow samples (Corollary M3) is ARGUED only.

## Next concrete step

Replace the scalar by a finite-rank-plus-scalar lower bound of A_𝒞𝒞: A_𝒞𝒞 ⪰ R + c_floor(1 − Π) on 𝒞 with Π the projection onto
the span of the coupling vectors {P_𝒞Ae_k : k ∈ 𝒩} together with the modes of W_{t_1}, and R the exact compression of A
there (finite, explicit). Then S ⪰ A_{N′N′} − B(R ⊕ c_floor)^{−1}Bᵀ is a finite sufficient inequality whose loss is
confined to the component of b outside a finite subspace; test at ½log5 + ε whether this residual component is below
the margin of S, and identify (via Proposition M) which integer coincidences the subspace must contain.
