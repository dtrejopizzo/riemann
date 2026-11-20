# Round 12, A: the residue L161.4 and its passage to all of P_T

Notation of the common brief. P_T is the primitive carrier and H_T the self-adjoint operator of the form a_T on P_T.
The first-contact radical at T* is ker H_{T*}: PAPF = 0, i.e. AF = r = αe^{−t/2} + βe^{t/2} on the window.

**Result.** L161.4 does not connect with global positivity by a route of its own. The leakage square L^sc is
strictly positive on every F ≠ 0, and it is so for any weight of the current: cΛ, deletion of a prime
power, exact Λ (Lemma A). Hence the clause «the first contact annihilates the left-hand side» is equivalent, via
the first-contact chain, to ker H_{T*} = {0}, which is the goal itself. The version on all of P_T exists
(Prop. B). It is a Lyapunov-type kernel certificate, L^sc(F) = Re⟨H_T F, M_T F⟩, and in it L^sc can be
replaced by any positive definite form (for example ‖F‖²). The two canonical normalizations dictated by the
lattice fall back onto R161_052 and R161_056 (tangent with the wrong orientation). Verdict: selection NO-GO. It is a
reformulation (B3, B9), and the square has a sign blind to the weight. The reopening operation of §4 remains.

## 0. Step 0, in primary sources

I read R161_015, 016, 017, 018, 019, 020, 024, 052 and 075 in full. Of R161_003 I read §§0–1, of R161_040 §§2–6, of
R161_056 §§1 and 4, and of R161_073 and R161_081 the headers. I also read ROUND_010_A, ROUND_011_A, RULES_AVOID
B, E, J, K, L, T and U, and ANNEX_161_FILES_1 §(c).

**Search.** I searched for «L161.4», «R161_020», «leakage square» and «cuadrado de fuga» across the whole corpus, the index and
the grid. The citations that follow are all there are.
- R161_021, 024, 030, 034, 039, 049, 052.
- README 161 and R161_099 §269.
- Index 04 G1C-R161_020-021, with status PARTIAL.
- Index README l.2454: «correct squares without identity with the PC defect».
- Grid, cell 1C: live residue X_T, not realized.
- ANNEX_161_FILES_1 and _2, LEDGER l.45, RULES_AVOID K1 and U2, ROUND_011_A.

«C_log», «E_N^ren» and «graph limit» appear in about fifty files (phases 106, 114, 116, 161 and 162). The
relevant ones are those cited below.

### 0.1 Objects

- **C_log.** Normalized logarithmic cosine: self-adjoint, unitary and involutive. In Mellin,
  M(C_log u)(s) = χ(s)M(u)(1−s) (R161_017 (1.6)).
- **Product port g.** It is the inverse boundary transform of
  G_+^can(s) = −ζ'(s)K_F(s−½) − ζ(s)Q_+(s−½) − c_+(F)ζ(s)Θ_T(s), with Θ_T(s) = e^{−T(s−1)}/s (R161_015 (1.1)–(1.3)).
  - Q_+ is the transform of the compact prehistory q_+ of the right Euler current B_+F.
  - Hence G_+ = ζ·(transform of the exterior tail h_+ of B_+F). g is supported on [T,∞) and is linear in the weight.
- **P_+.** Multiplication by 1_{[T,∞)}. H_T^± are the corresponding Hardy projections.
- **E_N^ren.** It is S_N^ren𝓕 − JS_N^ren, with S_N^ren = S_N − C_N(D). S_N has unit weights n^{−1/2} and C_N(D) is the
  Euler–Maclaurin polar continuum (R161_003). In Mellin e_N = A_N u − B_N, with A_N = Z_N(s) and B_N = Z_N(1−s)
  (R161_052 (1.1)).
- **Radical.** The supposed first-contact vector F ∈ ker H_{T*}, with parity ε.
- **V_{M,N,T}.** A normalization to be defined, linear in F, inherited from the zeta product and the crossed Tate
  terms. It cannot be defined from L^sc.

### 0.2 What is PROVED

- Unitary compression rigidity (R161_020 Lemma 1.1).
- L^sc(g) = ‖(I−P_+)C_log g‖² = ‖g‖² − ‖P_+C_log g‖² (R161_020 (0.2)), and its Hardy form (4.3).
- Exact defect G_+ + χG_− = ζW_ε (R161_017 Thm. 2.1), with interior restriction W_ε^∨ = r_ε (R161_017 (3.3)).
- Gamma pole lattice: W^0 holomorphic at s = 3, 5, 7, … implies F = 0 (R161_019, R161_024 Thm. 1.1).
- Equivalence of R161_024 §2: removability is equivalent to the vanishing of the reflected port at the trivial zeros.
- Norm slope N_T'(0+) = −2∫(t−T)|g|² (R161_015 Thm. 3.1).
- Finite unitary colligation θ_N = A_N u/B_N, with |θ_N| = 1 and Toeplitz defect equal to exact leakage
  (R161_052 §§1–2).

### 0.3 Open statement

lim ‖H_T^− E_N^ren V_{M,N,T}F‖² = L^sc_T(F) (R161_020 (5.2)), and moreover the finite first-contact identity annihilates
the left-hand side. The finite version is R161_052 (5.1): ‖T_N x‖² − ‖x‖² → 0, with x = x_{M,N,T}(F) taken from
(PC-ren).

### 0.4 Why it stopped

E_N^ren F → 0 on Schwartz data (R161_003). Consequently, every bounded strong limit of linear maps
built with E_N^ren acts as zero and kills both sides (R161_016 §3, PROVED in that class). Rescaling would require
a new uniform graph bound plus the inverse typing, and none of that comes out of (PC-ren). Moreover, the unitary
tangent of R161_052 carries the mean U+V and not the difference U−V (R161_056).

### 0.5 Exclusion of R161_018 and its audit

R161_018 claims ZA_∞ = [Z,D_Γ] = 0, whence every linear limit of (PC-ren) would be tautological (Thm. 2.1, Cor. 5.1).

R161_075 shows that this identification is not established. Product in L², distributional product and meromorphic
identity are three different things: in L², ZAf = 0 would imply Af = 0, and in the distributional sense
z·δ_γ = 0. The exclusion remains unproved. It is not used below.

## 1. Four-point filter

1. **Closest antecedent.** R161_020 §5 and R161_052 §5 (the same target in finite form), plus R161_024 §2.
   For the passage to all of P_T: R161_073 (stabilized inverse on ker H) and R161_081 (extension of Q outside the
   radical; fails on eigenvectors with λ ≥ 0).
2. **What is new.** (i) Lemma A: L^sc is positive definite and its kernel is trivial for every weight of the current.
   (ii) Prop. B: the exact form that L161.4 would have on all of P_T.
   Both are analysis of the target. Neither is a sign mechanism.
3. **Why it would avoid the difficulty.** It does not. Lemma A shows that the only open link is precisely
   ker H_{T*} = {0}.
4. **Link with global positivity.** It would be the first-contact chain of §2(a). Its open link is the
   goal itself.

A strict cross-check detects repetition (B3/B9). I do no long derivation beyond the structural
lemmas that prove it.

## 2. Step 1

### (a) What L161.4 would give if it were true

The chain is the following.

1. λ_A(T) > 0 for small T. CITED: certificates of Paper 47.
2. T ↦ λ_A(T) is continuous (P47 lem:contA) and decreasing; H_T has compact resolvent, so λ_A is attained
   (P47, paragraph before lem:contA). CITED.
3. If a_T takes a negative value for some T, there exist T* and F* ≠ 0 with H_{T*}F* = 0. PROVED from 1 and 2.
4. The reflection t ↦ −t preserves W, K and P_T, so ker H_{T*} decomposes by parity and one can take F* with
   parity ε. PROVED. Simplicity is not needed.
5. L161.4 (identity plus vanishing on the radical) gives L^sc(F*) = 0. OPEN: it is the target.
6. L^sc(F*) = 0 implies F* = 0, without using the sign σ. It is Lemma A, below: PROVED.
7. Contradiction, and hence a_T ≥ 0 on P_T for all T.

**Lemma A (PROVED).** Let F ∈ L²(I) with port g ∈ L² built with any sequence of weights of the current
(Λ, cΛ, or Λ with a prime power deleted), keeping the unit-weight multiplier ζ. If
(I−P_+)C_log g = 0, then F = 0.

*Proof.*
1. If C_log g is supported on [T,∞), its transform H(s) is holomorphic of Hardy class in Re s > ½
   (Paley–Wiener, with the convention of R161_015 (2.2)).
2. On the line, its boundary values agree a.e. with M(s) = χ(s)G^can(1−s) (R161_017 (1.6)).
3. M is holomorphic in a strip around the line, because the only poles of G^can are at s = 0 and s = 1.
4. Then H − M has non-tangential limit 0 a.e. on one side of a strip. By the Lusin–Privalov uniqueness
   theorem, H ≡ M in the strip and, by continuation, in Re s > ½.
5. χ has simple poles with non-zero residue at s_m = 2m+1, m ≥ 1. Hence G^can(1−s_m) = G^can(−2m) = 0.
6. At −2m one has ζ(−2m) = 0 (CITED: simple trivial zero, with ζ'(−2m) ≠ 0), while Q_+ is entire and Θ_T is
   finite. Hence G^can(−2m) = −ζ'(−2m)K_F(−2m−½), and one gets ∫F(t)e^{(2m+½)t}dt = 0 for all m ≥ 1.
7. The change x = e^{2t} and the completeness argument of R161_019 Thm. 3.1 (powers x^m with m ≥ 1 on a
   compact interval separated from 0) give F = 0. ∎

The weight of the current only enters in Q_+ and in the residue c_+. Both appear multiplied by ζ(−2m) = 0.

**Consequences.**
- L^sc(F) > 0 for all F ≠ 0, for Λ, for 2Λ and for deletion. PROVED.
- Link 5 is exactly equivalent to ker H_{T*} = {0}: L^sc(F*) = 0 is impossible for F* ≠ 0. The clause
  «the first contact annihilates the left-hand side» is therefore the assertion that there is no first contact.
- The chain 1–4, 6–7 is PROVED or CITED, and all the weight falls on link 5. That link is the goal (B9:
  the sign remains in a statement about the minimizer). I stop, as the brief asks.
- Neither σ nor the compression of R161_020 (3.5) is needed. It suffices that the leakage vanish, as
  R161_024 §2 already observed.

### (b) Statement outside the radical

**Proposition B (PROVED).** For each T statements (i) and (ii) are equivalent. In (ii), Ł_T is any
bounded positive definite injective form on P_T, for example L^sc (if bounded on the domain) or ‖·‖².
- (i) ker H_T = {0}.
- (ii) There exists an operator M_T, with dom H_T ⊂ dom M_T, such that Ł_T(F) = Re⟨H_T F, M_T F⟩ for all F ∈ dom H_T.

*Proof.*
- From (ii) to (i): if H_T F = 0, then Ł_T(F) = 0 and F = 0.
- From (i) to (ii): with compact resolvent and trivial kernel, H_T^{−1} exists and is bounded. It suffices to take
  M_T = H_T^{−1}Ł_T. ∎

Thus the candidate is «L^sc_T(F) = lim‖H_T^−E_N^ren V F‖² + Re⟨H_T F, M_T F⟩ on all of P_T», with an extra
term vanishing on the radical. It exists in that form, and only in it: any extra term vanishing
exactly on ker H_T is a function of H_T F.

Combined with chain (a), which applies to all T at once, it gives a_T ≥ 0 for all T. But it adds no mechanism, for
three reasons.
1. The only general solution, M_T = H_T^{−1}Ł_T, inverts the form. It is circular in the sense of J3.
2. By Lemma A, L^sc has no privileged role compared with ‖F‖². Choosing the leakage square contributes nothing
   as long as M_T has no formula of its own.
3. In finite dimension, the identity 2Ł = HM + M*H > 0 gives In(H) = In(M) (Ostrowski–Schneider; CITED). The
   sign obligation passes to the spectrum of M. This falls into L6 (inertia) and B3 (reformulation).

### (c) The normalization V

**Freedom.** V is a linear family V_{M,N,T}: P_T → L²(ℝ). It may depend on the prime cutoff M, the
lattice cutoff N and T, through S_N, C_N(D), B_± and the Tate coefficients.

**Non-circularity.** H_T^{−1}, the minimizer, L^sc and any root or factorization of the form
(J3) are forbidden. The identity would have to be proved after writing V.

**Canonical choices of the lattice.**

1. *Polar renormalization to half density (R161_003).* It is already inside S_N^ren and is precisely what makes
   E_N^ren → 0. It leaves no freedom.

2. *Division by the opposite orientation (R161_052).* e_N = B_N(θ_N − 1), with θ_N unimodular. It is the only
   normalization dictated by the lattice alone that leaves an object of order one.
   - Since e_N → 0 and B_N → ζ(1−s) where it does not vanish, one has θ_N → 1 in measure, and by dominated convergence
     M_{θ_N} → I strongly. ARGUED: the step «B_N → ζ(1−s) in measure» is not verified in primary sources.
   - Hence ‖(I−P)M_{θ_N}x‖ → 0 for fixed x. For the limit to survive, x_N has to move.
   - Rescaling by the rate leads to the tangent, i.e. to the phase current (R161_052 §3), and that
     current carries U+V, not U−V (R161_056, PROVED there).
   - This choice thus falls back onto an already withdrawn tangent.

3. *Scalar rescaling λ_N V with λ_N → ∞.* The rate of E_N^ren V F → 0 is fixed by the regularity of 𝓕VF at the upper
   endpoint n ≈ N (Euler–Maclaurin) and depends on F.
   - A finite non-zero limit for all F in a dense subspace would require a uniform rate, i.e. a
     term of fixed order. That term is again the jet of option 2.
   - ARGUED, not PROVED: I do not have the proof that no λ_N gives a non-trivial limit.

**Conclusion of (c).** No written canonical choice leaves both sides finite and non-zero with the correct
orientation. Those that exist are recorded (R161_052, R161_056, R161_016 §3). ARGUED, with the cited pieces
PROVED in their memos.

### (d) Checks

- **Left side.** E_N^ren contains no Λ: only the lattice and n^{−1/2}. So say Lemma 2 of ROUND_011_A
  and channel (β) of ROUND_010_A. Λ could only enter through V.
- **Right side.** g is linear in the weight, so L^sc is multiplied by c². But its positive definiteness is
  blind to the weight (Lemma A).

**cΛ with c = 2.** L^sc_2 = 4L^sc is positive definite. Moreover, the interior link (R161_017 (3.3)) changes: with
current 2B_± and a form whose first contact is D_ΓF − 2(B_++B_−)F = r, the interior restriction of W becomes
r + D_ΓF·(something non-zero) instead of r. This is indicated by the computation of R161_017 (2.2) with c: (c−1)d_ΓK_F remains.
ARGUED: the exact normalization of D_Γ against Arch is not recomputed.

If there exists T with λ_A(T; 2Λ) < 0 (battery E, CITED), there is a radical vector F_2 ≠ 0 with L^sc_2(F_2) > 0. Then
no identity of Prop. B, with any M, can hold for c = 2 at that T. PROVED, conditional on that citation.

Which named term loses the sign? None: both squares remain ≥ 0. What fails is the equality (the
vanishing clause). By rule R3-i this is the automatic case. There is no signed remainder that ceases to be ≥ 0,
because the statement has no signed remainder.

**Deletion of a prime power.** Same analysis: L^sc remains positive definite (Lemma A), and the breakdown,
if there is a first contact, is again in the equality.

**Beurling.** There is no multiplier ζ with trivial zeros nor a functional equation. g and C_log g are not defined in
the same way, and Lemma A does not apply. The statement cannot be formulated: it remains undefined, not falsified.

**Conclusion of (d).** The signed part of the statement (the two squares and the strict positivity of L^sc) is
blind to c and to deletion. All the discriminating content lies in an equality whose only known realizer is
H_T^{−1}. By the criterion of Lemma 2 of round 11, extended from «Λ-free» to «positivity invariant under the
checks», the statement is blind and is rejected as a sign mechanism.

## 3. Step 2: verdict

L161.4 does not connect with global positivity by any route other than the first-contact chain, and in that
chain its open link is exactly ker H_{T*} = {0} (Lemma A). Its version on all of P_T is Prop. B: a
Lyapunov-type kernel certificate, which is equivalent to injectivity of H_T and whose general solution is
M = H^{−1}Ł (J3).

**Class that closes it.** «Square = square identities with vanishing on the radical, where the strict
positivity of the squares is invariant under cΛ and deletion.» It is a reformulation (B3) with the sign in the
minimizer (B9). The canonical normalizations fall back onto R161_052 and R161_056.

## 4. Operation that would reopen it

An operator M_T (or a V) with its own formula is needed, built with E_N^ren, the Euler current and the
Tate coefficients, without H_T^{−1}. For it one would then have to prove the identity L^sc = lim‖H^−E V F‖² +
Re⟨H_T F, M_T F⟩. Moreover, it must be shown why it fails at c = 2, pointing to the line of its construction that uses
Σ_{d|n}Λ(d) = log n and not only linearity in the weight.

**First case.** Chamber 0.8 < T < ½log5, contacts 2, 3 and 4, with Z_{T,−}^{−1} = I − K + K² (R161_005 §4). There M_T
would be an explicit matrix on the channels 2, 3, 4, plus the Gamma head. R161_016 §5 warns that this only
controls the first collar.

**Falsifier.** c = 2 with δ = log 2 at k = 2 (R161_001 Thm. 4.1). Without that formula there is no candidate.

## Claims and labels

1. Objects and statuses of Step 0, according to R161_015–020, 024, 052, 056 and 075: CITED.
2. The exclusion of R161_018 is not established (R161_075): CITED. Not used.
3. Lemma A: vanishing leakage implies F = 0, for every weight of the current, without σ: PROVED (uses the CITED ζ'(−2m) ≠ 0,
   Lusin–Privalov and R161_019 Thm. 3.1).
4. L^sc is positive definite on P_T for Λ, 2Λ and deletion: PROVED (corollary of 3).
5. First-contact chain, links 1–2: CITED (P47 lem:contA, compact resolvent, certificates).
   Links 3–4 and 6: PROVED. Link 5 (L161.4): OPEN, and equivalent to the goal: PROVED, by 3.
6. Neither σ nor the compression (3.5) of R161_020 is needed: PROVED (by 3; already implicit in R161_024 §2).
7. Prop. B (version on all of P_T ⇔ ker H_T = {0}; general solution H^{−1}Ł): PROVED.
8. Inertia: 2Ł = HM + M*H > 0 gives In H = In M in finite dimension: CITED (Ostrowski–Schneider).
9. θ_N → 1 in measure and M_{θ_N} → I strongly: ARGUED.
10. The canonical normalizations fall back onto R161_052/056: ARGUED (the cited pieces are PROVED).
11. No scalar rescaling gives a uniform non-trivial limit: ARGUED.
12. The interior of W under cΛ receives a term proportional to (c−1)d_ΓK_F: ARGUED (normalization not recomputed).
13. Under c = 2 Prop. B fails for every M if there is a first contact: PROVED, conditional on battery E (CITED).
14. Positivity of the squares blind to c and to deletion; statement blind as a sign mechanism: PROVED (by 3)
    / selection NO-GO.
15. Beurling: undefined statement: ARGUED.
16. Verdict: L161.4 does not pass the gate. It is a reformulation with the sign in the radical (B3, B9): selection
    NO-GO. Reopening according to §4: OPEN.
17. Global sign of a_T: OPEN.
