# R163_201 — Construction of the multi-prime Euler gate and its obstruction

Round 31, construction of step (G). Pure mathematics, no numerics.
**Cell:** 4B (Euler product × contact kernel vector); the global lemma (§3) falls into 5D. Walls the route would need to evade: W1 (gate ⟺ conclusion), W5, W12. Nearest route: R163_161/162.
**Verdict:** the multi-prime construction is PROVED (§1–§3). Deriving (G) from the contact equation plus an integer exterior identity stays as a **NO-GO**: the only exterior identity using log ℕ's integrality and acting on the Euler modes annihilates them **for every source G**. So it carries no first-contact information (§4). Neither RH nor D is asserted.

I read R163_290. I agree with its point (U)⇒ circularity: for fixed T and θ(P)>2T, (G) ⟺ F=0. This note therefore limits itself to the question that remains alive: does a **derivation** of (G) exist?

Conventions (R163_161/162): `K_F(s)=∫F(u)e^{(s−1/2)u}du`, `G=VJF`, `K_G(s)=K_F(1−s)/(1−s)`, `U_p=p^{1/2}τ_{−log p}`, `ℓ_p=log p`, F primitive (`K_F(0)=K_F(1)=0`), support in [−T,T].

## 1. Semilocal scale action and transform

On `K`, `U_p` acts as multiplication: `K_{U_pD}(s)=p^{s}K_D(s)`. The `U_p`, p∈P, commute and generate the action of the group ⟨P⟩⊂ℚ₊^* on ℝ = log ℝ₊^*. It is the scale part of `C_S`'s action on the semilocal space `X_S`, S={∞}∪P (Connes 1999).
The multi-prime resolvent equation is

```
∏_{p∈P}(I−U_p) D = G   ⟺   K_D(s)·∏_{p∈P}(1−p^{s}) = K_G(s).            (1.1)
```

- **Stable solution** `D_-^P`: (1.1) is inverted over Re s=1/2, where |p^s|=√p>1 and the symbol does not vanish. It is the unique L² solution and coincides with ∏_p D_-^{(p)}.
- **Causal-dual solution** `D_+^P=E_P^∨G` (R163_162 (4)): inverted over Re s<0, where the geometric series in p^{s} converges. It is locally finite.

## 2. Joint homogeneous modes (PROVED)

**Proposition 2.1.** If G∈C_c^∞, then `H^P_G:=D_+^P−D_-^P` is the sum of residues of `K_G(s)e^{−(s−1/2)u}/∏_p(1−p^s)` on the line Re s=0:

```
H^P_G(u)= Σ_{ω∈Λ_P} c_ω e^{(1/2−iω)u} + e^{u/2}Q_G(u),
c_ω = K_F(1−iω)/[(1−iω)·ℓ_p·∏_{q∈P,q≠p}(1−q^{iω})]   (ω=2πk/ℓ_p, k≠0),
```

with `Λ_P=⋃_p (2π/ℓ_p)(ℤ∖0)`. Q_G is a polynomial of degree ≤|P|−2.

*Proof.* K_G is entire and decays rapidly in vertical strips, so shifting the contour from Re s<0 to Re s=1/2 is legitimate. The poles must be checked.
- The zeros of ∏(1−p^s) on 0≤Re s≤1/2 all lie on iℝ.
- Away from 0 they are simple and disjoint across primes, because `k ℓ_q=j ℓ_p` ⟹ `q^k=p^j` ⟹ k=j=0 (unique factorization).
- At s=0 the zero has order |P|. Since K_G(0)=K_F(1)=0, the pole has order |P|−1, giving the polynomial Q_G. ∎

**Corollary 2.2 (joint spectral object).** `H^P_G=0` ⟺ the following two conditions hold:
(i) `K_F(1+iω)=0` for every ω∈Λ_P;
(ii) `K_G^{(j)}(0)=0` for 1≤j≤|P|−2.

System (ii) is triangular with non-zero diagonal, and in particular `K_G'(0)=−K_F'(1)`. In other words, (G) is the condition that `K_F(s)·Z_P(1−s)/(1−s)` be holomorphic on Re s=1, with `Z_P=∏_{p∈P}(1−p^{−s})^{−1}`. **(G) is exactly the annihilation, by K_F, of the reflected truncated Euler product's polar divisor.**

For |P|≥2, extra Tate jets appear at s=1 (`K_F'(1)`,…) that primitivity does not give. Moreover, the joint invariant subspace `{D: U_pD=D ∀p∈P}` is the line `e^{u/2}·ℂ`: ⟨P⟩ is dense in ℝ₊^*, and a distribution invariant under dense translations is constant. The "quotient" ℝ/(Σℤℓ_p) is a Kronecker foliation, not a space. That is why the k≠0 modes of several primes do not assemble into a joint projector. The product of R163_161's `H^{(p)}` diverges, and the correct object is the sum of residues of 2.1.

## 3. The entire exterior identity: the global dual resolvent (PROVED)

**Theorem 3.1.** Let G∈C_c^∞ and let `E_ℕ^∨G(u)=Σ_{n≥1} n^{1/2}G(u−log n)`, which is locally finite (R163_162 (6)). Then

```
K_{E_ℕ^∨G}(s)=ζ(−s)K_G(s)  (Re s<−1),
E_ℕ^∨G = D_-^ℕ + κ_G e^{3u/2},     κ_G = −K_G(−1) = −K_F(2)/2,            (3.1)
```

where `D_-^ℕ` is the inversion of ζ(−s)K_G(s) over Re s=1/2 and lies in L².

*Proof.* ζ(−s) is meromorphic for Re s≥−1−ε, with a single pole at s=−1 of residue −1, and grows polynomially in vertical strips. K_G decays rapidly. Shifting from Re s<−1 to Re s=1/2 picks up only the pole s=−1. ∎

**Consequence.** In the limit P→all primes, *every* Euler mode Λ_P of §2 disappears, with no condition on F. Only the polar mode `e^{3u/2}` survives, whose coefficient is K_F(2). Z_P(1−s)'s poles on Re s=1 are cutoff artefacts, and ζ(1−s) has no poles there.

**Where integrality enters, exactly.** It enters at two points:
- (I1) `b(n)=1`, by unique factorization, so that E_P^∨→E_ℕ^∨ locally (R163_162).
- (I2) The meromorphic continuation of ζ(w) up to Re w≥−1/2 with a single pole and polynomial growth. It comes from Poisson/Euler–Maclaurin for the comb ℤ (the sawtooth of ⌊x⌋).

For a Beurling–DMV system with N(x)=cx+O(x^θ), ζ_B only continues to Re w>θ. The shift in (3.1) cannot cross Re w=θ>−1/2, and the modes on Re s=0 (i.e. Re w=0) **do not** cancel in general. So (3.1) fails for DMV precisely because of (I2), as the battery requires. In (U), integrality only enters in distinguishing Λ_P's points, and for (U) counting with multiplicity would suffice.

Falsifiers against (3.1):
- Z_K (factor of 2 raised to K+1): the symbol is ζ(−s)(1−2^{s})^{−K}, with poles of order K at 2πik/ℓ₂, so the modes of 2 **survive**. ✓
- Λχ₂: L(−s,χ₂) is entire and no mode remains. ✓
- DH/Epstein: have continuation with finitely many poles, so they also satisfy the "polar modes only" version of (3.1). (3.1) is, therefore, class-blind in the sense of W3/T2. This is not a failure of (3.1), but the signal that it carries no sign.

## 4. Does a derivation of (G) exist? NO-GO, with a precise obstruction

An identity 𝓘 is needed that simultaneously uses the contact equation (R163_161 (9)–(10)), the exterior terms, and (I1)–(I2), and that implies H^P_G=0 for the window's primes (T_*>0.8047 ⟹ P⊇{2,3,5}, θ=log 30>2T).

**Obstruction 4.1 (independence from F).** Every identity moving the Λ_P modes via (I1)–(I2) goes through §3's contour shift, i.e. through ζ(1−s)'s pole. That shift is valid for **every** G∈C_c^∞, not only for G=VJF with F a contact. So:
(a) in the global object, the modes are already zero for every F, and there is nothing to force;
(b) in the truncated object P, the modes are `c_ω∝K_F(1−iω)`, and their vanishing is not a consequence of (3.1). If it were, for every primitive F, (U) would give F≡0 for every F, which is absurd.

The part of (3.1) that distinguishes a first contact would have to be the *difference* E_ℕ^∨−E_P^∨ = sum over n∉⟨P⟩. In that difference the Λ_P modes appear with the opposite sign, and the balance is again an identity for every G (W12).

**Obstruction 4.2 (the contact equation does not see the modes).** R163_161's (10) gives `⟨A_locF,G⟩=a_F·conj(K_F'(0))`, a scalar with no k≠0 component. This note's multi-prime version only adds the jets `K_F^{(j)}(1)` of §2(ii), likewise with no k≠0 component. T_*'s minimality gives, via Hellmann–Feynman, a boundary condition on |F(±T_*)|², which is monotone in the weights (W3). λ=0 annihilates any term λ·(…) (W5). The collars (R163_162 (8)–(9)) are positive squares of F's mass on strips: they do not see phases K_F(1+iω). The Tate jets are finite in number, and (U) requires infinitely many conditions.

**Obstruction 4.3 (two-atom curve).** On the curve s₂≈0.9998 of R162_2001/2190, Type I contact is genuine, with T_*≈0.55–0.61. For T_*>½log3, P={2,3} and θ=log 6>2T_*, so (U) forces some mode of 2 or 3 to be ≠0. A derivation of (G) would have to use the exact weight b(2)=1 *discontinuously*: fail at distance 2.4·10⁻⁴. (3.1) depends on the weights meromorphically across the whole product (completed ζ) and has no version for a two-atom comb. There is no analogue of (3.1) seeing s₂'s deviation in a single coordinate without invoking global continuation (I2), and that continuation is F-independent (4.1).

**Conclusion.** No exterior identity constructible with (I1)–(I2), the Tate endpoints, the collars, the polar term, λ=0, and T_*'s minimality forces (G). The only entire identity acting on the Euler modes (Theorem 3.1) eliminates them for every source. That is the obstacle: integrality eliminates the truncated polar divisor **uniformly**, and so it cannot select the stable solution *at contact*. (G) ends up with the same status as R_LF=0 (W1). I stop here.

## 5. Residuals

- O163.201a: one must look for an F-dependent statement using (I2) **non-linearly** in the source (W7 suggests the linear version dies). None is on record.
- The PROVED results that can be reused are 2.1/2.2, which identify (G) with annihilation of Z_P(1−s)'s polar divisor on Re s=1, and 3.1, which gives the global cancellation with a single polar mode K_F(2).
