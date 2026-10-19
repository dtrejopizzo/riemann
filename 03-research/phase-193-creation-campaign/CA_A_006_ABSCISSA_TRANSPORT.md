# CA_A_006 — Seed (f): moving the abscissa-1 Maass–Selberg positivity to ½ — options (i) Hecke average, (ii) Y-integration

Phase 193. Pen and paper.

## 0. Hard pre-screen against the record
- **MW-2** (03_, NO-GO pattern over ≥5 mechanisms): propagating Euler-product data from Re s>1 into the strip stalls.
- **NT_013/014 and Target E** (06_ lines 163–166): crossing (1,3/2] is ⟺ a zero-free half-plane (forward PROVED, converse
  ARGUED). Target E is excluded.
- **L2_027**: (M) propagation is OPEN; conjugation is a NO-GO. **L2_026**: FE symmetrization is void (antisymmetry).
The seed is a σ-transport from 1 to ½, so it starts inside the MW-2 pattern. The two options are tested below for whether
they escape it.

## 1. Data (CITED, standard; Iwaniec, *Spectral methods*, Prop. 6.8)
For s=½+iτ, Y≥1:
  M_Y(τ):=‖Λ^Y E(·,½+iτ)‖² = 2log Y − (φ′/φ)(½+iτ) + [φ(½−iτ)Y^{2iτ} − φ(½+iτ)Y^{−2iτ}]/(2iτ) ≥ 0,
with φ(s)=ξ(2s−1)/ξ(2s). On the line |φ|=1, and −(φ′/φ)(½+iτ)=4Re(ξ′/ξ)(1+2iτ) (by the FE).

## 2. Option (ii): integrating over Y against a positive measure — cannot move the arithmetic abscissa (NO-GO, PROVED)
Let μ≥0 be a finite measure on [1,∞) with ∫log Y dμ<∞, and write μ̂(u):=∫Y^{iu}dμ(Y) (a positive-definite function of u).
**Lemma 1 (exact).** ∫M_Y(τ)dμ(Y) = 2∫log Y dμ + μ([1,∞))·4Re(ξ′/ξ)(1+2iτ) + [φ(½−iτ)μ̂(2τ) − φ(½+iτ)conj μ̂(2τ)]/(2iτ).
*Proof.* M_Y is linear in the three Y-dependences 1, log Y, Y^{±2iτ}; integrate term by term (Fubini, dominated). ∎
**Theorem 2 (NO-GO for (ii), PROVED).** For every positive μ, the integrated inequality depends on ζ only through ζ(1±2iτ)
and its derivative:
- the additive arithmetic term is c_μ·Σ_n 4Λ(n)n^{−1}cos(2τ log n), with weights fixed at 1/n and c_μ=μ([1,∞));
- the oscillatory term contains ζ only through the unimodular phase φ(½±iτ)=ξ(1∓2iτ)/ξ(1±2iτ), again at abscissa 1;
- μ enters only through the scalars μ([1,∞)), ∫log Y dμ and the multiplier μ̂(2τ), none of which contains Λ.
So Y-integration acts on the archimedean and polar parts (log Y moment, oscillatory multiplier) and leaves the arithmetic
abscissa unchanged. To produce weights 2Λ(n)/√n, μ̂ would have to contain ζ data on the critical line. A μ built that way
makes "μ ≥ 0" a positive-definiteness statement about a function of ζ on the line, i.e. an exact restatement of window
positivity (Paper 47: positivity at every window ⟺ positive definiteness of one explicit function). *Proof.* Lemma 1, read
coefficientwise; the last sentence is the definition of μ̂ plus the cited equivalence. ∎
**Remark 3 (what the abscissa-1 form really is, PROVED).** cos(2τ log n)=cos(τ log n²) and 4Λ(n)/n=4Λ(√N)/√N at N=n².
So in the τ variable, M_Y is a Weil-type form with the window normalization 1/√N, but for the Dirichlet series ζ(2s),
whose comb sits on the squares. ζ(2s) has no zeros on Re s≥½, because ζ has none on Re≥1 (CITED, PNT-strength). The
Maass–Selberg positivity is therefore positivity for a "ζ(2s)" comb, which is the 𝒞_PNT class. Moving it to the comb of ζ(s)
means filling in the non-square positions, i.e. MW-2 / part (b) (zero-free half-plane information). This is consistent
with NT_013/014.

## 3. Option (i): Hecke average Σ n^{−½}T_n on the Eisenstein part — this is (S) (PROVED)
On E(·,½+iτ) the normalized T_n has eigenvalue a_τ(n), and Σ_n a_τ(n)n^{−w}=ζ(w+iτ)ζ(w−iτ) (Re w>1). At w=½ (continued),
the averaged operator A has Eisenstein eigenvalue |ζ(½+iτ)|². So for a packet f_g,
⟨Af_g,f_g⟩ = (1/4π)∫|g(τ)|²|ζ(½+iτ)|²dτ (plus truncation terms). That is the second-moment form, EI_002 Thm 1 / (S),
restatement of D. Its positivity is the trivial |ζ|²≥0 and does not contain the log-derivative symbol σ_T. The truncated
average Σ_{n≤N}n^{−½}T_n has eigenvalue Σ_{n≤N}n^{−½}a_τ(n), which is real but not of one sign, so positivity is lost.
(PROVED, given the standard Hecke eigenvalues.)

## 4. Result
**Seed (f) NO-GO: (ii) PROVED (Theorem 2); (i) PROVED to be (S).** Moves YES→NO: "Maass–Selberg positivity at abscissa 1 can
be carried to the window abscissa by positive operations on the Eisenstein side" → NO. The obstruction is exactly MW-2:
arithmetic enters as ζ(2s) on the squares, and filling in the other positions needs zero-free information.
Record note: (M) propagation (L2_027) is unchanged in general. This memo closes only its Maass–Selberg/Hecke instance.

## 5. Self-review
- Theorem 2 covers positive measures in Y. Signed measures would lose positivity, and the result would be an estimate (B′).
- Weight-k Eisenstein series or other truncation operators change only the archimedean factors, and the arithmetic part is
  still φ. The same conclusion holds (ARGUED).
- Remark 3 is a neat restatement but not a barrier theorem in Paper 47 terms. It is labelled PROVED as an identity only.
- No sign contact. No negative value for ζ.

## 6. Seed from a different family (proposed, not pre-screened)
All of CA_A_001–006 fail for one reason: the positivity comes from a norm or a pointwise sign, so it is blind to the comb
and to h*. A different family should take positivity from the *variational* structure in weight space and use the
openness lemma directly:
**Homotopy / no-crossing in weight space.** Take a path a_c from a comb known positive at every window (Paper 47: smooth
and atomic positive combs exist) to Λ. Track λ_A(T;a_c). A sign change requires a crossing c* where the minimizer h*_{c*}
satisfies ∂_c λ = Σ ∂_c v_n·c_{h*}(log n) = 0 together with λ=0. The ζ-specific input would be a property of Λ that makes
crossings impossible along a path chosen with Euler × FE (e.g. a_c=Λ restricted to p≤P_c, with the FE restored by a
completed factor). Pre-screen checklist: corpus entries "rigid-perturbation cone" (600), "Cayley signed index" (632),
"Kreĭn flux" P121, and the O8 lesson (the barrier must involve h*).
