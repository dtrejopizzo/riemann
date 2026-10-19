# R162_701 — Round 7: (B4.1) via integrality and J-parity — **NO-GO (refuted as stated: (B4.1) is the negation of the definition of N)**

Round 7. Input: R162_502 B1–B4, R162_590, README F1–F4.
Conventions as in R162_502: S = (X+T)^{1/2}, Z = M_T(1), Z^{-1} = M_T(μ), 𝔞_T = 𝔞^∞_T − 2⟨F,M_T(Λ)F⟩ on P_T,
N = ker H_{T_0} on P_T, JF = εF. Real Hilbert space (F real), so all pairings are real.

## 0. DH / Beurling line (stated first, as required)

The integrality input is the identity Σ_{m≤y} μ(m)⌊y/m⌋ = 1 (y ≥ 1), i.e. Σ_{m≤y} μ(m){y/m} = y·Σ_{m≤y}μ(m)/m − 1,
with {·} the fractional part of a quotient of **rational integers**.
- Beurling (DMV/Zhang): the generalized integers 𝒩_B are not ℤ_{>0}; ⌊y/m⌋ is replaced by N_B(y/m), and the
  remainder N_B(u) − ρu is not the sawtooth ψ(u) = {u} − ½. The identity Σμ_B(m)N_B(y/m) = 1 survives, the floor
  identity does not.
- DH: coefficients a(n) with a*b = a·log but a^{-1} of size n^{σ_0−1}; Σ a^{-1}(m)⌊y/m⌋ ≠ 1 because 1*a^{-1} ≠ δ_1.
  The floor identity is specific to the pair (1, μ).
So the line that must fail for Beurling/DH is: "replace the counting measure of the support by u + ψ(u) with ψ
the ℤ-sawtooth". This is Euler–Maclaurin/Poisson over ℤ, i.e. input (i) of R162_502 B3.

## 1. Main result: (B4.1) is an identity with the wrong strict sign (PROVED, elementary)

**Lemma 1.1 (conjugation collapse).** For every F ∈ L²(I_T),

    4⟨SZ^*F, SZ^{-1}F⟩ = 4⟨F, M_T(Λ)F⟩ + 4‖SF‖².

*Proof.* ⟨SZ^*F, SZ^{-1}F⟩ = ⟨F, Z S² Z^{-1}F⟩ = ⟨F, Z(X+T)Z^{-1}F⟩, and by (B2.1)
Z(X+T)Z^{-1} = M_T(Λ) + X + T. ∎

**Corollary 1.2.** For F ∈ P_{T_0}:
    (B4.1)  ⟺  4⟨F,M_T(Λ)F⟩ < 2𝔞^∞_{T_0}(F)  ⟺  𝔞_{T_0}(F) > 0.

**Theorem 1.3 (refutation).** For every 0 ≠ F ∈ N, equality holds in (B4.1):
4⟨SZ^*F,SZ^{-1}F⟩ = 2𝔞^∞_{T_0}(F) + 4‖SF‖². Hence (B4.1) is false on every nonzero first-contact vector,
and "(B4.1) for all 0≠F∈N" is literally the statement N = {0}.

*Proof.* HF ∈ span{g_0,g_1} ⊥ P_{T_0} ∋ F, so 𝔞_{T_0}(F) = ⟨F,HF⟩ = 0; apply Cor 1.2. (This is (B2.4) itself.) ∎

**Consequences.**
- (B4.1) is not a lemma that could close Gate 1 under the hypothesis "first contact exists": it *contradicts* that
  hypothesis at the definitional level, with no arithmetic input. Its content is "λ_A(T_0) > 0", i.e. E1
  (restatement of "no first contact", same class as R162_408 Conjecture 7.1).
- F1 diagnosis: on eigenvectors with λ > 0 one has exactly 4⟨SZ^*F,SZ^{-1}F⟩ = 2𝔞^∞ + 4‖SF‖² − 2λ‖F‖², so
  (B4.1) is precisely "λ > 0". An argument proving (B4.1) would be exactly the perturbative argument F1 forbids.
- Correction to R162_502 B4: the residual should not be recorded as (B4.1). The "aligned − misaligned" difference
  in (B2.2) carries **no information beyond 𝔞 itself**, because the polarization in (B2.2) is undone by Lemma 1.1.
  B2 is a rewriting of the prime side (as R160_M7 Thm 4 was), not a coupled square with independent content.

## 2. Where integrality can enter at all (PROVED, structural)

**Lemma 2.1 (integrality is invisible to the exact algebra).** B1(a)–(d) and (B2.1) hold for every pair
(a, a^{-1}) with a(1) ≠ 0 supported on any discrete multiplicative semigroup of reals ≥ 1 (Beurling included).
In particular Z Z^{-1} = I needs 1*μ = δ_1 only, not Σμ(m)⌊y/m⌋ = 1.
*Proof.* The convexity argument of B1(a) uses only one-sided shifts; (c) uses only the Dirichlet inverse. ∎

**Lemma 2.2 (floor remainders = sawtooth = Poisson).** Write Σ_{m≤X} f(m) = ∫_1^X f(u)du + [boundary] − ∫_1^X f(u)dψ(u).
Then Z = Z_0 − Z_ψ, with Z_0 = P∫_1^X u^{-1/2}τ_{log u}du P (a Volterra operator, archimedean) and Z_ψ the
ψ-Stieltjes part; ψ(u) = −Σ_{k≥1} sin(2πku)/(πk) exhibits Z_ψ as the dual comb of (PC). The floor remainders
{X/m} inside M_T(μ) arise only from this decomposition applied to Z Z^{-1} = I, i.e.
Z_0 Z^{-1} = I + Z_ψ Z^{-1}.
*Proof.* Stieltjes integration against ⌊u⌋ = u − ½ − ψ(u) and the Fourier series of ψ. ∎

So every integrality term is linear in Z_ψ, i.e. in the (PC) comb. Inserting Lemma 2.2 into
⟨SZ^*F,SZ^{-1}F⟩ gives ⟨SZ_0^*F,SZ^{-1}F⟩ − ⟨SZ_ψ^*F,SZ^{-1}F⟩; by Lemma 1.1 the sum is still
4⟨F,M(Λ)F⟩+4‖SF‖², so any split is a re-bracketing of the same number, which on N equals the RHS exactly.

**Proposition 2.3 (Hermite-type identity on the kernel; PROVED, no sign).** For F ∈ N, eliminating Z via
Lemma 2.2 in Theorem 1.3 yields the exact linear-in-ψ law
    ⟨SZ_0^*F, SZ^{-1}F⟩ − ‖SF‖² − ½𝔞^∞_{T_0}(F) = ⟨SZ_ψ^*F, SZ^{-1}F⟩,
the only place where the floor remainders Σ_m μ(m)m^{-1/2}{·/m} (entering through Z^{-1} = M_T(μ) paired with
Z_ψ^*) appear. It is an identity, not an inequality; J-parity (ε = ±1) only restricts both sides to the
ε-sector (Z, Z_ψ do not commute with J, so no parity cancellation occurs), and the hull lemma A5 only fixes the
support length 2T_0. Neither orients it: for λ > 0 eigenvectors the same law holds with −λ‖F‖²/2 added, so
any sign extracted from it is F1-forbidden. Vaaler-type extremal majorants of ψ would turn it into
|RHS| ≤ (1/(K+1))·(mass) + (trigonometric polynomial of degree K in the comb), i.e. a truncated (PC) term
bounded in absolute value — a quadratic-in-comb bound after Cauchy–Schwarz (F2) with losses polynomial in X
against the Theorem M margin.

## 3. Verdict

- Theorem 1.3: (B4.1) is **refuted** on every nonzero F ∈ N (equality, not strict inequality), and as a
  universal statement it is equivalent to N = {0} (E1). No arithmetic input can prove it without proving that the
  first contact does not exist, which is not what Gate 1 asks (Gate 1 asks R_LF = 0 for F ∈ N).
- Integrality enters only through the ψ-sawtooth (Lemma 2.2), i.e. linearly in the (PC) comb; the resulting
  kernel identity (Prop 2.3) carries no sign; majorant compression reassembles (PC) quadratically (F2).
- DH/Beurling line: the floor identity Σμ(m)⌊y/m⌋=1 (§0); it is never used by the exact algebra (Lemma 2.1).
- Recommendation: delete (B4.1) as the open residual of R162_502; record B2 as a restatement (like M7 Thm 4).
  Add to R162_590 §1c: "Möbius-conjugation square / (B4.1) — R162_502/701 — collapses by Z S² Z^{-1} = M(Λ)+S²;
  equivalent to λ_A(T_0) > 0 — E1."

Labels: Lemma 1.1, Cor 1.2, Thm 1.3, Lemma 2.1, Lemma 2.2, Prop 2.3 PROVED. (B4.1): REFUTED / E1. Route: NO-GO.
