# CA_A_004 — Candidate (d): weight-½ (metaplectic) Eisenstein series on Γ₀(4) as escape from line doubling

Phase 193. Pen and paper; one literature lookup (citation only), no numerics.

## 0. Citation check (done first; CITED, verified against the source text)
Source read: W. Duke, Ö. Imamoḡlu, Á. Tóth, *Cycle integrals of the j-function and mock modular forms*, Ann. of Math.
(2) **173** (2011), 947–981 (author PDF www.math.ucla.edu/~wdduke/preprints/annals-fin.pdf), §2, Prop. 2 and Lemma 4,
eqs. (2.23)–(2.25); DIT attribute the formulas to Ibukiyama–Saito (MPI preprint) and cite Goldfeld–Hoffstein,
Invent. Math. **80** (1985) 185–208, for the same Eisenstein series.
- P₀⁺(τ,s): the weight-½ Eisenstein series on Γ₀(4), Kohnen plus space (coefficients on n≡0,1 mod 4),
  Δ_{1/2}P₀⁺=(s−¼)(¾−s)P₀⁺. Unitary axis: Re s=½ (eigenvalue 1/16+t², real), so line doubling of CA_A_001 Lemma 2
  does **not** apply here.
- For D a fundamental discriminant, m≥1 (eq. 2.25):
  b₀(Dm²,s)=2^{2−4s}π^{s+¼}|D|^{s−¼} · L_D(2s−½)/ζ(4s−1) · Σ_{n|m} μ(m/n)(D/(m/n))(m/n)^{−½}... n^{3/2−2s}σ_{4s−2}(n)
  (finite divisor sum; exact form in DIT (2.25)).
- Constant term (2.24): b₀(0,s)=π^{½}2^{5/2−6s}Γ(2s)ζ(4s−2)/ζ(4s−1).
My memory version "L(2s−½,χ_n)/ζ(4s−1)" in CA_A_001/003 is **confirmed** (with χ_n=χ_D, n=Dm², plus a finite
multiplicative correction in m).

At s=½+it: square indices n=m² (D=1) carry ζ(½+2it)/ζ(1+4it)·(finite Dirichlet polynomial in m); n=Dm², D≠1, carry
L(½+2it,χ_D)/ζ(1+4it). The constant term carries ζ(4it)/ζ(1+4it), the weight-0 scattering shape at abscissa 1.

## 1. Pre-screen against (R) and thm:shape (the coordinator's three questions first)

**Q1. Does the family mix ζ with every χ_D?** Yes, necessarily. Every Γ₀(4)-invariant positivity statement involves
the whole Fourier expansion. Restricting to n=□ is a Fourier-side projection that commutes with no Hecke or Γ₀(4)
operator (it is not U₄, W₄ or pr⁺). After the projection the positivity is the trivial Σ_m|·|²≥0 (§2). With the full
expansion, every D enters with conductor |D|>1. That is row 18 of the input map (Euler × FE at q>1, UNKNOWN), and (R)(2)
asks for conductor 1. Verdict: (2) holds for the D=1 slice only, and that slice carries no structure-giving positivity.

**Q2. Survives O10 / O12?** The construction does not contain Λ, so O1–O6 act on it trivially: they change σ_T and
leave P₀⁺ untouched. Any sign step inside the object is therefore comb-independent (lem:shape-ident pattern, as for
Lewis–Zagier in CA_A_002). For O12, half-integral-weight Eisenstein series over totally real K exist, with coefficients
L_K(·,χ) (Shimura; CITED in outline, not checked), so the same Parseval positivity holds there. O10 (Epstein) has no
weight-½ analogue (binary theta series have weight 1), so it is structurally destroyed. That is not enough: (11) needs
the *sign step* to be ζ-specific, and the sign step (§2) is Parseval, which holds for every Fourier series.

**Q3. Do off-diagonal Parseval terms reproduce the σ_T-correlation without Shimura?** No. See §2, Prop. 1: per index n
the off-diagonal kernel is **rank one** in (t,t′).

## 2. What was built (PROVED, elementary given §0)
Let h∈C_c^∞(ℝ) and form the wave packet E_h(τ)=∫h(t)P₀⁺(τ,½+it)dt (no poles on Re s=½ away from finitely many points;
DIT, CITED). Horocycle Parseval at height y gives
  ∫₀¹|E_h(x+iy)|²dx = Σ_n |∫h(t) b₀(n,½+it) W_n(y,½+it) dt|²  (+ constant-term square).
**Proposition 1 (PROVED).** For each n the (t,t′) kernel is K_n(t,t′)=g_n(t)·conj(g_n(t′)) with
g_n(t)=b₀(n,½+it)W_n(y,½+it). It has rank one. So the Parseval form in h is Σ_n|⟨h,ḡ_n⟩|², a sum of squares of linear
functionals of the values L_D(½+2it)/ζ(1+4it).
**Corollary 2 (PROVED).** A Parseval identity of this type can equal the window form 𝔞_T(F)=(1/2π)∫σ_T|F̂|²
(a multiplication operator in τ) only through a decomposition σ_T(τ)δ(τ−τ′)=Σ_n g_n(τ)conj(g_n(τ′)) on the test class.
That requires the family {g_n} to resolve a multiplication operator: an orthogonality (large-sieve / Selberg-orthogonality)
statement for {L_D(½+2it)}_D. Such statements are asymptotic means with remainders (Goldfeld–Hoffstein's own application:
the mean value of L(½,χ_D)). Under thm:shape(B′) that is an estimate with a remainder, excluded at the sign step.
**Corollary 3 (ARGUED).** The pieces are squares of ζ- and L-values, so the decomposition is an arithmetic square
decomposition of 𝔞_T. Clause (3) and Theorem sos (no arithmetic square decomposition for T≥½log3 without a free positive
definite part) apply. ARGUED: I have not checked that thm:sos's notion of "arithmetic square" literally covers squares of
smeared L_D(½+2it).
**Remark 4 (wrong functional, PROVED).** σ_T is affine in the log-derivative data (Λ). Parseval produces |ζ(½+2it)|²-type
data, the second moment. Passing from |ζ|² to Re ζ′/ζ needs a t-derivative of log, which is not a positive operation.
This is the same second-moment residue as CA_A_003 §3 and EI_002 (= (S), a restatement of D).
**Remark 5 (Shimura).** On the diagonal t=t′ the D=1 square is |ζ(½+2it)|²/|ζ(1+4it)|². Its numerator is the central value
L(½,E(·,½+2it))=ζ(½+2it)ζ(½−2it) of the weight-0 Shimura image (a Waldspurger-type identity, CITED in outline). So the
diagonal passes through Shimura automatically. The off-diagonal t≠t′ avoids Shimura but is rank one (Prop. 1) and carries
no correlation structure beyond the product g(t)conj(g(t′)).

## 3. Pre-screen table
| clause | verdict | reason |
|---|---|---|
| line ½ at a unitary parameter | YES (new vs CA_A_001) | DIT (2.25), D=1 |
| (1) exact Λ(n), n<e^{2T} | NO | object contains no Λ; Λ enters only through the identification with 𝔞_T |
| (2) Euler × FE, conductor 1, jointly | NO | the Γ₀(4)-invariant object mixes every χ_D (row 18) |
| (3) non-linear, no bare squares | NO (ARGUED) | Parseval = arithmetic squares without a free positive definite part |
| (4) | YES | no zeros used |
| (8) correlation inside P_T | NO | off-diagonal kernel rank one per n (Prop. 1) |
| (11) ζ-specific sign step | NO | Parseval holds for every Fourier series; ζ-specificity would sit in the identification, which is an orthogonality estimate (B′) or a restatement of D |
| key test Λ→a_P, Λ+cδ₂ | survives trivially | object is comb-independent ⇒ excluded (lem:shape-ident pattern) |

## 4. Result
**NO-GO for (d) as a sign carrier (Prop. 1 and Cor. 2 PROVED; the exclusion of the full class is ARGUED through Cor. 3).**
The metaplectic series genuinely escapes line doubling: ζ(½+2it) appears at a unitary parameter, which CA_A_001 left
OPEN. But the only positivity it offers is Parseval. Parseval is comb-generic, rank one per Fourier index, and mixes all
quadratic twists. Reproducing 𝔞_T would need either an orthogonality estimate (B′) or an SOS restatement of D (clause 3).
Moves YES→NO: "metaplectic Parseval can carry the σ_T-correlation inside P_T without Shimura" → NO (rank-one obstruction).
Development beyond pre-screen: not undertaken, by the coordinator's rule (develop only if it passes).

## 5. Self-review
- Prop. 1 is per-n rank one. Summing over n gives arbitrary rank, so the obstruction is not "rank one overall". It is that
  diagonalizing the sum needs D-orthogonality (Cor. 2). An exact orthogonality could come from a Kuznetsov/Petersson
  trace formula in half-integral weight: exact, with a geometric side of Kloosterman (Salié) sums. Salié sums for weight ½
  are explicit and evaluate in terms of quadratic congruences √n mod c, which is ℤ-integrality as mechanism. **This is the
  one unexcluded variant.** It is an exact identity, not an estimate, but it is valid for every Maass/Eisenstein spectrum on
  Γ₀(4), hence comb-independent. To be ζ-specific at the sign step it would need a positivity on the Salié side that fails
  for a_P, which nothing here provides. Status: OPEN, not built (next candidate CA_A_005).
- Cor. 3 is ARGUED pending a check of thm:sos's exact class.
- No sign contact. No negative value for ζ.

## 6. Addendum after the round-1 review (CA_A_00x_HOSTILE_REVIEW.md, CAMPAIGN_LEDGER.md)
(R1) **Line doubling is withdrawn as a general barrier.** It holds only for the invariant-form class of CA_A_001 Lemma 2.
A Mellin transform in y of the constant term, or Rankin–Selberg in w (∫^reg |E|²E(·,w) gives ζ(w±2iτ)²/ζ(2w)-type
products), reaches ζ(½+iτ) on the unitary axis at weight 0. So the "escape" in §0 is **one of several**, not the unique
one. Prop. 1 and Cor. 2 do not use line doubling and stand. The weight-0 Mellin/RS routes are alternatives. They inherit
the same diagnosis: their positivity (Petersson norm, E(·,w)>0 for real w>1) is a Hilbert-norm or pointwise positivity,
so the obstruction in R2–R3 applies to them too. This is ARGUED, not built.
(R2) **O8/O7 lesson applied.** The P₀⁺ object does not even depend on the comb, and a ζ-specific property of the comb alone
survives the quartet modification O7 and the deformation f_t (O8), because those keep the comb. The sign step must couple
to the form or minimizer h* without passing through zeros. CA_A_004 couples only through the identification Parseval ↔ 𝔞_T,
i.e. Cor. 2 (D-orthogonality, an estimate) or an SOS restatement. Its exclusion is confirmed on this ground as well.
(R3) **Openness at scale λ_A/κ_T** (CA_B_004: positivity on an ℓ^∞ ball of radius ~λ_A/κ_T around Λ). An exact identity
singling out Λ cannot be the sign carrier. The carrier must be a property that is open in the weights at that scale. The
Salié-side variant flagged in §5 is an exact trace formula, so to be admissible it would have to supply an *inequality*
that is stable under weight changes of size λ_A/κ_T and still couples to h*. As stated it does not. The variant is
downgraded from "next candidate" to OPEN-RESIDUE (low priority).
**Updated next candidate:** an object coupled to the minimizer, e.g. the minimizer's Dirichlet polynomial
D_h(τ)=Σ b_m m^{−½−iτ} (phase 190: b_m≈m^{−½}w(m/M)) inserted as the test vector of a Rankin–Selberg integral
∫^reg |Σ b_m E-type|² E(·,w). The Petersson positivity would then be a statement on h*, open in the weights. It still has
to pass (11): not a comb-generic identity (B″) and not the second moment (S). Pre-screen not yet done.
