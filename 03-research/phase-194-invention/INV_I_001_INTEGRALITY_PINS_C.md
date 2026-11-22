# INV_I_001 — Integrality as a constraint on the comb: the c = 1 pin, its exact orbit, and the (1, Λ) forms (track I, phase 194)

Track I. Labels PROVED / CITED / CONDITIONAL / ARGUED / OPEN /
NO-GO / REF-D; pure mathematics, no numerics. Notation of Paper 46: 𝔞_T^{(a)}(F) = 𝔪_T(F) − Σ_{n∈N_T} 2a(n)n^{−½} c_F(log n), N_T = {n ≥ 2 :
log n < 2T}, μ_T(v) = λ_A(T; v) concave (lem:degen), WP_T(a) = "𝔞_T^{(a)} ≥ 0 on 𝒫_T". Track H (additive structure of ℕ) is not touched.

## 0. Corpus / index check
Searched ROUTES-TRIED-INDEX (README, 01–06, 05b, all audits), grid, crossword, phase 163, phase 193 audit, phase 194 memos; grep
"integrality", "Selberg", "Λ²", "1*Λ", "O_4", "ζ^c", "lem:shape-scale". Relevant indexed entries:
- R163_1001 Thm O / W-identification (04_PHASES row "W-identification"): integrality enters only as *identification*; class collapses to {ζ}.
- W3′ integer-frequency blindness (R163_1001 Thm O; falsifier f_χ): integrality of frequencies does not separate ζ at q>1.
- N_BUILD_022 (06_OPEN_RESIDUES "exact matrix identity from 1*Λ = log beyond divisors", NO-GO): ZΔ = [L,Z] exact; Near is a discretization defect.
- C_BT = {0 ≤ a ≤ Λ} (R155_053): closed sieve upper-bound class, no sign. O_3 tail deletion, O_6 Euler deletion (prop:shape-eulerdel).
- Selberg / Λ² sieve: NG-A4 (parity), NG-B1; instruction: do not reduce to Selberg/Λ² weights.
- INV_F_001 Thm F2 (cone premises on log ζ are O_4-closed); residue = this memo's task.
**New reason (not a retry).** R163_1001 used integrality as one global identifying property (ζ vs. falsifiers at conductor q); N_022 sought an
*identity* from 1*Λ = L. Neither computed the *exact intersection of the O_4/O_6 orbits with the hierarchy of coefficient-integrality
constraints* ({0,1} ⊂ ℤ_{≥0} ⊂ {≡1}), nor asked whether a *positive form* (inequality, not identity) in the pair (1, a) can be
non-homogeneous in a. These are the objects here (Theorems I1–I4).

## 1. Setup: the comb ↔ coefficient dictionary (PROVED)
For a real weight vector a = (a_n)_{n≥2} put f_a = exp(Σ_{n≥2} a_n (log n)^{−1} n^{−s}) = Σ b_n n^{−s}, b_1 = 1. Differentiating:
  (E)  L·b = b ∗ a,  i.e.  b_n log n = Σ_{d|n, d>1} a_d b_{n/d}   (n ≥ 2).
(E) is triangular in the divisor order: a ↦ b is a bijection between weight vectors and coefficient vectors with b_1 = 1, and a|_{[2,N]} is
determined by b|_{[1,N]} (and conversely). For a = Λ: b ≡ 1 and (E) is 1∗Λ = L. Under O_4 (a ↦ ca): f_{ca} = f_a^c, b ↦ d_c-type coefficients;
for ζ: b_n = d_c(n) = Π_{p^k‖n} binom(c+k−1, k).

## 2. Theorem I1 (the three integrality classes; PROVED)
Let 𝒞_{01} = {a ≥ 0 : b ∈ {0,1}^ℕ}, 𝒞_ℤ = {a ≥ 0 : b ∈ ℤ_{≥0}^ℕ}, 𝒞_1 = {a : b ≡ 1}.
(i) 𝒞_1 = {Λ} (Möbius inversion of (E)). On a window: b_n = 1 for n < e^{2T} ⟺ a = Λ on N_T.
(ii) Rigid bound on 𝒞_{01}: if a ≥ 0 and b ∈ {0,1} then 0 ≤ a_n ≤ b_n log n ≤ log n for all n, and a_p ∈ {0, log p} at primes.
  *Proof.* In (E) every term is ≥ 0 and the term d = n is a_n b_1 = a_n, so a_n ≤ b_n log n. At n = p: b_p log p = a_p, b_p ∈ {0,1}. ∎
  So on primes Λ is the *maximal* element of 𝒞_{01}, and 𝒞_{01} ⊂ {0 ≤ a ≤ L}.
(iii) O_4-orbit intersections: {c > 0 : cΛ ∈ 𝒞_{01}} = {1} (b_p = c); {c > 0 : cΛ ∈ 𝒞_ℤ} = ℕ (b_p = c forces c ∈ ℕ; conversely d_k(n) ∈ ℕ);
  {c : cΛ ∈ 𝒞_1} = {1}. Hence 𝒞_{01} and 𝒞_1 break O_4 completely; 𝒞_ℤ breaks it only to its integer sub-orbit O_4^ℕ.
(iv) Closures: 𝒞_{01} contains 0 (f = 1) and is closed under O_6 (a_P = Λ·1{p ≥ P}: b = 1 on P-rough n) and under any prime-set deletion
  Λ·1_{𝒮} (b = 1_{⟨𝒮⟩}); 𝒞_ℤ is closed under O_4^ℕ, under O_6, and under products f_a f_{a′} (a + a′). Not convex (INV_F C3 type:
  (1+2^{−s}) has a_4 < 0, and averages leave {0,1}).

## 3. Theorem I2 (integrality NO-GO trichotomy; PROVED, using Paper 46 lem:shape-scale, cor:Tarch, prop:shape-eulerdel)
Let 𝒜 be a deduction class whose arithmetic premises are membership in one of the classes of I1 plus cone premises on log f (INV_F Thm F2) plus
comb-generic identities (thm:shape B″).
(a) 𝒞_ℤ: 𝒜 contains no valid deduction of WP_T at any T > ½log2. *Proof.* The proof of lem:shape-scale (c large) uses c → ∞ only:
  take c = k ∈ ℕ, ζ^k ∈ 𝒞_ℤ, and 𝔞_T^{(kΛ)}(F_+) = 𝔪_T(F_+) − k v_2‖φ‖² < 0 for k large. ∎
(b) 𝒞_{01}: no valid deduction at any T ≥ 0.60. *Proof.* a = 0 ∈ 𝒞_{01} and μ_T(0) = λ_{∞,P}(T) < 0 for T ≥ 0.60 (cor:Tarch). ∎
  (Also O_6: a_P fails on [0.60, ½log P], prop:shape-eulerdel.)
(c) 𝒞_1: the class is the singleton {Λ}; a deduction from it is a computation with Λ itself (thm:shape Cor (a),(b)); integrality here is
  identification, exactly R163_1001 Thm O. No class content.
**Corollary (PROVED).** Coefficient integrality breaks H_cone (it is not conic: c = 1 is isolated in 𝒞_{01}), but every *inequality* form of it
is downward-closed (contains 0 or deletions) or upward-closed along O_4^ℕ, and the only form that excludes both is the equality b ≡ 1 on the
window, which pins a = Λ there. Integrality therefore pins c = 1 but carries no sign beyond identification. Hypothesis to break next:
**H_mono** — every pointwise integrality premise is monotone (down-closed or ℕ-scale-closed) or identifying.

## 4. Positive forms in (1, Λ) jointly (task item 2)
**Proposition I3 (the divisor Gram form; PROVED).** For finitely supported x, y on ℕ (support ≤ N):
  Q(x,y) := Σ_{d≥2} Λ(d) Σ_m |x_{dm} − y_m|² 1{dm ≤ N} ≥ 0  (free: sum of squares, Λ ≥ 0),
and by 1∗Λ = L used *as a constraint* (not inverted), Σ_d Λ(d)Σ_m |x_{dm}|² = Σ_n |x_n|² log n. Hence
  2 Re Σ_d Λ(d) C_{x,y}(d) ≤ Σ_n |x_n|² log n + Σ_m |y_m|² ψ(N/m),  C_{x,y}(d) = Σ_m x_{dm} ȳ_m (multiplicative correlation at lag d).
*Reading.* The comb correlation is dominated by the L-diagonal plus a ψ-term. The bound is linear in Λ with Λ ≥ 0, hence homogeneous: under
a ↦ ca both sides scale by c once the diagonal is written as Σ_d a(d)Σ_m|x_{dm}|² (the collapse to log n is the only place b ≡ 1 enters, and
for f_a^c it becomes the d_c-weighted identity). Its inequality content is the cone C2 bound; its continuous transfer to 𝔞_T on 𝒫_T is the
trivial bound (C_0 − 𝒜_T)‖F‖², and the exact transfer beyond divisors is N_022 §3 (Near defect). PROVED; no new sign.
**Theorem I4 (degree obstruction; PROVED).** Let Q be a form whose free positivity is an SOS identity in (1, a) polynomial of degree ≤ 1 in a,
using 1∗a = L (or (E)) only as a linear constraint. Then Q's inequality content is invariant under O_4 or reduces to a = Λ on the window.
*Proof.* Degree-≤1 SOS in a with a ≥ 0 coefficients is a positive combination of a-linear terms plus a-free terms; the constraint (E) with b ≡ 1
is linear in a and pins a on N_T (I1(i)); if it is used, Q is evaluated only at Λ (identification); if not, the a-linear part scales by c and
the a-free part is fixed, i.e. Q's class is that of INV_F F2 / I2. ∎
**Consequence.** A non-homogeneous, non-identifying positive form must be of degree ≥ 2 in a. The first exact degree-2 relation in (1, Λ) is
the second ∂_s-jet ζ″/ζ = (ζ′/ζ)′ + (ζ′/ζ)², i.e. ΛL + Λ∗Λ = μ∗L² (Selberg symmetry), which is genuinely non-homogeneous (c vs c²) and pins c = 1
for b ≡ 1 — but it is the Selberg/Λ² identity, indexed and excluded by the task. Not developed. Stated as the boundary: **between the
degree-1 pin (identification) and the degree-2 pin (Selberg) there is no further polynomial (1, Λ)-constraint** (ARGUED: the ring of exact
relations among the jets of ζ at σ > 1 is generated by ζ^{(k)}/ζ = Bell polynomials in (log ζ)^{(j)}; the degree-k relation is the k-th Bell
identity, each one Selberg-type for k ≥ 2).

## 5. Partial positivity actually obtained (task item 3)
**Proposition I5 (WP for the whole {0,1}-class on short windows; PROVED given CITED inputs).** For 0 < T ≤ ½log3, WP_T(a) holds for every
a ∈ 𝒞_{01} and every a ∈ [0,1]·Λ.
*Proof.* N_T = {2}; by I1(ii) a|_{N_T} ∈ {0, Λ(2)}. WP_T(0): arch form PD on 𝒫_{½log3} (cor:Tarch, interval arithmetic, CITED-in-paper).
WP_T(Λ): proved through log 2 (Theorem A / D.12-α, Paper 46). μ_T concave ⇒ WP on the segment. ∎
For ½log3 < T < 0.58: 𝒞_{01}|_{N_T} = {0, Λ, Λ1_{2}, Λ1_{3}}; the first two hold (same citations); **Λ1_{3} and Λ1_{2} are OPEN** (they are
vertices of the box, not reached by concavity). Honest status: I5 is implied by known facts; it does not extend the T-range of WP_T(Λ).

## 6. Self-check
- thm:shape(A): I2 shows 𝒞_ℤ is O_4^ℕ-closed (lem:shape-scale applies with integer c), 𝒞_{01} contains 0 / O_6 falsifiers. Consistent.
- (A′): O_4^ε is broken by 𝒞_{01} (isolated c = 1); the falsifier (1+ε)Λ is not in 𝒞_{01} — so (A′) does not exclude 𝒞_{01}; (b) of I2 does.
- (B), (B′): nothing estimated; I3 is the trivial bound. (B″): (E) for general a is comb-generic; with b ≡ 1 it is identification.
- Problem (R): no clause met beyond (R)-type "uses Λ exactly" via identification only; (R)(4) zero-side not used.
- REF-D: none of I1–I5 restates the target. Theorem F2: I4 is its degree-1 completion.
- Corpus: I2(c) = R163_1001 Thm O (not claimed new); I3 overlaps N_022 §1 (identity) — new only as the inequality and its homogeneity.

## 7. Verdict
PROVED: (E), I1(i)–(iv), I2(a)–(c) and Corollary, I3, I4; I5 (given cor:Tarch and Theorem A, both in Paper 46).
ARGUED: Bell-jet boundary after I4. OPEN: WP_T for Λ1_{2}, Λ1_{3} at ½log3 < T < 0.58; H_mono (find a non-monotone, non-identifying
integrality premise); degree-≥2 forms not reducing to Selberg. NO-GO: integrality classes 𝒞_{01}, 𝒞_ℤ as class premises (I2); degree-≤1 (1,Λ) forms (I4).
No contact with the sign.
