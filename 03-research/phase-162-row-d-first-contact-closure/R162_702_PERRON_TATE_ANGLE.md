# R162_702 — O504.1: Perron–Tate angle and second eigenvector under Λ ≥ 0 plus arithmetic support

Task O504.1 (R162_504 §6). Pure mathematics, no numerics.
**Status: NO-GO** for a sign or a lower bound on c_T or μ_2 at first contact. PROVED: Lemma 1
(Perron–Hellmann–Feynman monotonicity), Theorem 2 (support-class blindness), Corollary 3 (the
support of W = μ*log² adds nothing to the support of Λ). Gate 1: OPEN. Row D: OPEN.

Notation as in R162_504: A_T, ψ_T > 0 (Thm 1 there), φ_ev = cosh(t/2)1_{I_T},
c_T = ⟨ψ_T, φ_ev⟩/‖φ_ev‖, μ_1 < μ_2 ≤ …, ψ_2 the second eigenvector. X = e^{2T}, PP = prime powers.
The comb is Σ_{n<X} v_n c_F(log n) with v_n = v_n(a) = 2a(n)n^{-1/2} (prop:finite).

## 0. The two mandatory lines, stated first

- **(i) DH line.** Every statement below uses Perron (R162_504 Thm 1), whose only arithmetic step is
  (iii) "v_n ≥ 0". For Davenport–Heilbronn/Epstein/Λχ₂ the coefficients change sign, the comb is not
  positivity preserving, ψ_T need not be positive or even, and c_T may vanish. This is the one
  line that fails for DH. It is the same line as in R162_504, and nothing new is added.
- **(ii) Finite-modification line (thm:finmod).** The argument would need to fail for a = Λ + η, η ≥ 0.
  It does **not** fail. Theorem 2 shows that no conclusion drawn from the pair
  (a ≥ 0, supp a ⊂ PP), or from (W_a ≥ 0, supp W_a ⊂ {ω ≤ 2}), can separate Λ from the κ-models
  of R162_103 (a = κΛ on {2,3,4}, a = Λ on n ≥ 5). Those models have genuine first contacts
  (R162_103 Thm 4.1). The models also satisfy supp a = PP exactly, with a > 0 on every prime power.
  So even the strict version of the support hypothesis is F3-blind. **F3: FAIL**, and the failure is
  structural, not a weakness of this memo.

## 1. Corpus check

- R162_504 Prop 4.3 (alignment bound) was killed by Theorem M. §5(iii) there already noted that Perron
  uses only Λ ≥ 0. R162_501 §3 noted that (W1) survives η ≥ 0 and that (W2)/(W3) are finite data.
- D4 Cor 5.2 / U-11: finitely many exact values of Λ can be flipped by a finite-codimension
  perturbation. R162_103 Thm 4.1: κ-models with first contacts in the chamber.
- What is new here: the observation that (W2) is implied by supp a ⊂ PP for **every** a (Cor 3). It
  is therefore not an independent arithmetic datum. Theorem 2 then closes the whole
  "positivity + support" class at once, for every functional of (T, v), including c_T, μ_2 and ψ_2.

## 2. Lemma 1 (Perron–Hellmann–Feynman) — PROVED

For fixed T, the maps v ↦ μ_1(T; v) and v ↦ ψ_T(v) are real-analytic on the open orthant
{v_n > 0}. Moreover ∂μ_1/∂v_n = −c_{ψ_T}(log n) < 0 for every n < X.

*Proof.* μ_1 is simple (R162_504 Thm 1), and A_T depends affinely on v through bounded shift
operators, so analytic perturbation theory applies (Kato). By Hellmann–Feynman,
∂μ_1/∂v_n = −c_{ψ}(log n). Since ψ > 0 a.e. on I_T and log n < 2T = |I_T|, the sets I_T and
I_T + log n overlap in positive measure. Hence c_ψ(log n) = ∫ψ(t)ψ(t − log n)dt > 0. ∎

Corresponding statements for c_T and μ_2: ∂c_T/∂v_n = Σ_{k≥2} c_{ψ,ψ_k}(log n)⟨ψ_k,φ̂⟩/(μ_1−μ_k)
(first-order perturbation), and ∂μ_2/∂v_n = −c_{ψ_2}(log n). Neither has a determined sign: ψ_2
changes sign, and the cross-correlations c_{ψ,ψ_k} are unsigned. So Perron makes only the **bottom**
monotone in the arithmetic. The angle and the second eigenvalue are not monotone.

## 3. Theorem 2 (support-class blindness) — PROVED

Let 𝒫_T be any property of (T, v) (for example "c_T ≥ β(T)", "μ_2(A_T) ≥ 0 at a first contact",
"ψ_2 ⊥ S for a given S", or "the first contact is of Type II"). Let 𝒞 be the class of weights a with
a ≥ 0 and supp a = PP. If 𝒫 is derived using only a ∈ 𝒞, together with Perron and the
spectral/resolvent structure of R162_504 §§2–4, then 𝒫 holds for every a ∈ 𝒞. In particular 𝒫 holds for
the κ-models. Therefore 𝒫 cannot imply "no first contact", and it cannot imply a sign at first contact
that excludes Type I/II, unless it is false for ζ or vacuous.

*Proof.* Spectral data of A_T depend on a only through v_T(a) ∈ R^{N_T} (prop:finite). R162_504
Thms 1–3 and Props 4.1–4.3 hold verbatim for every a ≥ 0 (their F3 line). The κ-models of R162_103
(κ ≠ 1) lie in 𝒞: they are supported on PP and positive there. They also have first contacts
(R162_103 Thm 4.1). A derivation valid on 𝒞 therefore applies to a model that has a first contact.
∎

**Corollary 3 ((W2) is a consequence of support).** For every a supported on PP,
W_a := a·log + a*a is supported on {ω(n) ≤ 2}, and W_a ≥ 0 if a ≥ 0.
*Proof.* a·log is supported on PP (ω = 1). (a*a)(n) = Σ_{de=n} a(d)a(e) is nonzero only when
n = p^i q^j (ω ≤ 2, including p = q). Nonnegativity is clear. ∎
So the Selberg datum (W2) of R162_501 is not a second arithmetic input. It is the support of Λ read
through the derivation identity, and it inherits Theorem 2. Only (W3), the exact values
W(p^k) = (2k−1)log²p and W(p^iq^j) = 2log p log q, distinguishes Λ from 𝒞. At a fixed T_* (W3) is
equivalent to Λ|_{n<X}, a finite list of numbers (D4 Cor 5.2), and a derivation from it must be uniform
in T (Thm finZ). Using exact values on c_T is Prop 4.3 again, which Theorem M kills.

## 4. Orthogonality obstructions: what survives

The hoped-for mechanism was: Perron positivity plus PP-support forces an orthogonality obstruction
to a first-contact vector F. What survives is only the following.
- Type I (A F = 0, F ⊥ ψ_T): positivity gives F sign-changing. That is all. PP-support constrains
  the shifts that couple F to ψ_T, but the shift set {log p^k} is ℚ-independent over primes. By the
  Müntz/Kronecker argument (R162_408 Prop 5.1, R162_501 Prop 3.1(a)), the correlation vector
  (c_{F,ψ}(log n))_{n∈PP} takes both signs on every subspace of small codimension. No obstruction
  follows.
- Type II (F = c A^{-1}φ, f(0) = 0): the Perron decomposition
  f_ev(0) = −c_T²‖φ‖²/|μ_1| + Σ_{k≥2}⟨ψ_k,φ⟩²/μ_k is an identity in v. Lemma 1 orients only the
  first term, and only through μ_1: it moves monotonically in each v_n, while c_T does not. So f_ev(0)
  has no monotone dependence on the arithmetic, and the zero set {f_ev(0) = 0} meets 𝒞 (κ-models).
- The sign of μ_2 at first contact is fixed by parity alone (R162_504 Thm 3: odd ⇒ μ_2 ≤ 0,
  even ⇒ μ_2^ev ≥ 0). Arithmetic adds nothing beyond that on 𝒞.

## 5. Falsifiers

- F1: Lemma 1 holds at every λ. It is not λ = 0-specific, and it does not close anything.
- F2: Perron is orientation-sensitive (it fails for −Λ). That is its only merit, and R162_504
  already recorded it.
- F3: FAIL for every statement using (a ≥ 0, supp ⊂ PP), with or without W (Thm 2, Cor 3). The only
  discriminating data are exact values. At fixed T they are finite (D4 Cor 5.2), and quantitatively
  they are blocked by M.
- F4: not applicable.

## 6. Verdict and residue for R162_590 §1c

"O504.1 (Perron + support on c_T/ψ_2): NO-GO. The class 𝒞 = {a ≥ 0, supp = PP} contains the κ-models,
which have first contacts. (W2) follows from the support (Cor 3). Perron orients only μ_1 (Lemma 1),
not c_T or μ_2. Killers: F3 (κ-models), M." Residue: an admissible input must distinguish Λ within 𝒞
by something other than finitely many values per window. Equivalently, it must use the identity
Λ*1 = log in a non-symbol, non-estimate form. The corpus contains no such form (R162_403, R162_406,
D4 Thm 5.1).

Files edited: this file only. Numerics: none.
