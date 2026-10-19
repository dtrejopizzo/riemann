# Phase 208 — Audit of the node's scope

**D is not closed.**
Result: consolidation of valid restrictions for the next construction;
no new sign route, no reopening of closed routes.

## Sources and method

Directed reading of the routes index (families, residues and
205–207/ZCERT entries); NODE_001 and README 206; CLASS_001 and AUDIT_207_001;
P47 eq:Aform, rem:zcert, prop:H, cor:H1minus; master map and crossword.
The summaries and repair records of P43–45 were consulted for context;
this note is not a full audit of their proofs.
Independent review of the scopes. No new numerics and no new
literature search were used. Statements about the literature are those from the catalog,
not a new survey or a proof of exhaustiveness.

## 1. Statement that is kept

For F real and even from the shape domain on [-T,T], let

    c_F(u) = ∫ F(x)F(x+u) dx,
    ℓ_T(F) = ∫ F(x) cosh(x/2) dx,
    Φ_T(F) = -∫_[1^-,exp(2T)] 2t^(-1/2)c_F(log t) d(ψ(t)-t).

On the orthogonal ℓ_T(F)=0, the node is

    Q_T(F) := (𝔪_T+𝔢_T)(F)+Φ_T(F) ≥ 0.

**CITED / exact identity:** Q_T(F)=𝔞_T(F)=W_T(F) on that orthogonal
(NODE_001 §§1.1–1.4). Here 𝔢 has kernel exp(-|x-y|/2).
The discrete sum with Λ(n)-1 does not replace Stieltjes without a correction.

## 2. Three quantifiers that cannot be suppressed

1. **All modes.** The node on E_N(T)^ev ∩ ker ℓ_T with N(T)≈4T
   is a compression. Its positivity does not control the complement or the
   coupling. RFIN_TRACT_001 leaves P1.c′ OPEN. "Every F of the domain" cannot be
   replaced by that block without an additional theorem.
2. **All windows.** P47 rem:zcert certifies the effectively computed points of
   {0.75,0.76,…,4.24} and 4.245, with cited inputs.
   It does not certify the interval T≤4.25. The continuum between points remains OPEN;
   at 4.25 the certificate fails, without refuting the sign.
3. **Declared sector.** prop:H treats W^ev and the even inertia for every
   window. The phrase "closes D" must also state the treatment of the
   odd sector and the polar term. They are not eliminated by notation.

Counting directions is necessary, not sufficient (NODE_001 §1.5).
Min–max gives μ_N(T)≥μ_∞(T): an upper bound of μ_∞ does not bound μ_N from above.
The observed dimension-dependent decay laws are not uniform theorems.

## 3. Separating arithmetic identification from positivity

**PROVED, elementary; reminder, NOT a new route.** The identity

    ∑_{d|n} a(d) = log n   for all n≥1

characterizes a=Λ without using zeros. Indeed a(1)=0, and for n>1 the recurrence

    a(n)=log n-∑_{d|n,d<n}a(d)

determines all the coefficients; the prime factorization shows that Λ satisfies
the identity. This inversion is not being used as a sign certificate.

To avoid the ambiguity of a_P, let us explicitly define b^(p): it vanishes at
the powers p^k, k≥1, and coincides with Λ at all other integers. It is the datum of
-D′/D for D(s)=ζ(s)(1-p^(-s)) at Re s>1; D keeps the simple pole
at s=1. Then

    ∑_{d|n} b^(p)(d) = log n - v_p(n) log p.

Proof: the divisors removed with nonzero Λ are p,…,p^{v_p(n)}, each
with weight log p. At n=p, the defect is log p.

Hence the statement "there is no zero-free arithmetic property that separates Λ from
the product with a prime removed" is literally false. There are exact,
elementary separators. **What remains open is turning that identification into
the quadratic bound Q_T≥0.** This distinction does not rehabilitate Λ*1=log, Möbius,
Selberg or Gram as routes: their attempts to extract a sign are already recorded
(E.2 / NODE_001 §3.1 / TB-3). They are not repeated here.

**PROVED, locality of the statement; NOT a new route.** If p>exp(2T), b^(p) and Λ
produce the same Q_T on that window, because no modified atom falls within
its support. Thus, conditioned on the sign for Λ on that window, b^(p) also
satisfies it. Global Euler fullness is not a necessary condition
for the sign of ONE window; it can be a hypothesis for proving the uniform
family. Locality of the target does not force the premises of its proof
to be local (AUDIT_207_001 §A.1).

## 4. What the barriers do not prove

- Σ_ρ Φ_F(ρ)^2 is an identity for F real and even; off the line the
  squares are not positive real squares. Do not write moduli.
- Quartets with the same comb have the same node; Epstein/DH with a different
  gamma factor are not points of the same conductor-1 problem.
- A falsifier for one class of premises does not classify every possible Euler
  product. "All the others violate it" does not follow from Theorem B.
- "We found no other bridge in the catalog" does not imply "no other bridge can
  exist", nor that arithmetic fullness can only be expressed through
  zeros. There is no general classification theorem for such proofs.

These are scope corrections, not sign mechanisms. In particular, this
note does NOT impose, as a theorem, that a proof must be nonlinear: the known
exclusions keep their declared classes and hypotheses.

## 5. Operative residue

**OPEN:** build a global arithmetic premise or structure implying
Q_T(F)≥0 for every T and every real even F of the domain with ℓ_T(F)=0.
If built only on the canonical block, the complement and the
coupling remain. If built only on a mesh, the continuum remains.

A subsequent proposal must write down the object, prove its positivity,
and prove its exact link with Q_T. Characterizing Λ without that link gives no
sign; naming Q_T a norm without proving its positivity does not either.
Before building, it must cite the closest route in the index and explain
which new hypothesis or object avoids its reason for failure.

**Balance:** neither the inequality nor an object that proves it was obtained. The
defensible scope of the problem was fixed, and universal conclusions
not authorized by the theorems of phases 206–207 were withdrawn.

Final review of the memo: **PASSES**; the recurrence, the
defect formula and the scope distinctions were checked. No new certificate.
