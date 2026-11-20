# CONSTRUCTOR_015 — Completed domain, non-closability and exact PSD cone

2026-10-19. **PROVED, favourable review in AUDIT_015.md:** the completion of the kernel −R_α contains the whole pure arithmetic factor and decomposes as an orthogonal product `L²(P_s)⊕V`. An explicit sequence is constructed proving that the Gaussian operator T is not closable. The global PSD cone in the real space spanned by its three pieces is exactly the non-negative orthant.

V is not identified with the whole Gaussian space, FE invariance is not proved, and no sign for D is obtained.

## 0. Corpus check and written difference

Consulted: the project rules, the ROUTES-TRIED-INDEX index (closability, domain, covariances, products and notes 209), archive 06, grid and crossword; CONSTRUCTOR005, 007, 008 and LINK014. In 008 a sequence of primorial exclusions tended arithmetically to 0 but its Gaussian norm diverged; it neither proved nor refuted closability.

**Exact difference:** the sequence constructed here is not that primorial nor a renaming. It is a product with small positive tilts over many large primes, normalised by its expectation P_s. Its arithmetic variance and its Gaussian norm tend simultaneously to 0 around the constant 1. The decisive bound uses the exponent `r=(s+1)/2>s` of the **same** kernel Π already computed in 011. This produces a new strong limit and settles the domain question that 008 left open.

It is not claimed that tilts of Bernoulli products are novel in themselves nor a source of sign for Q_T. They are applied here to determine exactly the completion of a prescribed kernel. Nor is the characterisation of a three-dimensional cone extrapolated to every positive kernel.

## 1. Domain, spaces and constants

Fix `0<α<1/2`, `s=2α∈(0,1)`, `κ=−Z_α>0`. Let P_t be the product law of geometric valuations of 005, with `E_tX_d=d^(−t)`. L²(P_s) is the space of that product law, equivalently the completion of the valuation cylinders; for s<1 it is **not** a normalisable zeta law on the positive integers.

On the finite divisibility algebra, take the **Haar-centred** domain

`𝒜₀={A: E_1A=0}`.

The Gaussian operator is

`TA(y)=E_yA`, `ℒ_α=L²((0,∞),y^(α−1)τ(y)dy)`.

The isometry of 005–007 is

`ι(A)=(√κ A,TA)` in `L²(P_s)⊕ℒ_α`,

`||ι(A)||²=κ Var_s(A)+κ|E_sA|²+||TA||²`.

Let 𝓗_α be the closure of ι(𝒜₀), as in 007–008. So as not to confuse the means: `E_1A=0` does not mean `E_sA=0`. Precisely that difference allows the following approximation.

Use the bound proved in LINK011:

`||T(X_d−1/d)||_(ℒ_α)≤C_α d^(−r)`, `r=(s+1)/2>s`.     (1)

## 2. Products over blocks of large primes

Choose finite blocks E_j of primes with

`P_j:=min E_j→∞`, `H_j:=Σ_(p∈E_j)p^(−s)→∞`.

For example, take in order all primes p≥max(2,j) until the sum of p^(−s) first reaches j³. This fixes E_j deterministically and satisfies both conditions.

They exist without PNT: the elementary divergence of Σ_p1/p implies that of Σ_pp^(−s), and partial sums can be taken further and further out. To recall the elementary proof, the finite product ∏_(p≤x)(1−1/p)^(−1) contains the harmonic sum up to x, while its logarithm is Σ_(p≤x)1/p+O(1); hence that sum and any of its tails diverge. There is no need to control the length or the largest prime of the block.

Put `t_j=H_j^(−2/3)` and, for u>0,

`Z_(u,j)=∏_(p∈E_j)(1+t_j p^(−u))`.

For brevity, suppress j in the following formulas. Define the finite polynomial

`B_j=∏_(p∈E_j)(1+t_jX_p)/Z_(s,j)`,

`A_j=B_j−Z_(1,j)/Z_(s,j)`.

By independence and because the indices are squarefree,

`E_sB_j=1`, `E_1B_j=Z_1/Z_s`, and `A_j∈𝒜₀`.

## 3. Strong arithmetic convergence to 1

For u_p=p^(−s),

`E_sB_j²=∏_(p∈E_j)[1+t_j²u_p(1−u_p)/(1+t_ju_p)²]`

`≤exp(t_j²H_j)`.

Hence

`Var_s(B_j)≤exp(H_j^(−1/3))−1→0`.                    (2)

Moreover, using `log(1+x)≤x` and `log(1+x)≥x−x²/2`,

`log(Z_r/Z_s)≤t_jΣp^(−r)−t_jH_j+(t_j²/2)Σp^(−2s)`

`≤−t_jH_j[1−P_j^(−(r−s))−t_j/2]→−∞`.              (3)

Here `Σp^(−r)≤P_j^(−(r−s))H_j` and `Σp^(−2s)≤H_j`. Since 1>r, `Z_1≤Z_r`, so

`θ_j:=Z_1/Z_s→0`.

Consequently,

`E_sA_j=1−θ_j→1`,

`E_s|A_j−1|²=Var_s(B_j)+θ_j²→0`.                    (4)

## 4. The Gaussian norm tends to 0, it does not diverge as in 008

Let Q_j be the product of the primes of E_j. The exact centred expansion is

`A_j=(1/Z_s)Σ_(d|Q_j) t_j^(ω(d))(X_d−1/d)`.

The term d=1 is zero. All remaining coefficients are positive. Apply (1) and the triangle inequality in ℒ_α:

`||TA_j||≤(C_α/Z_s)Σ_(d|Q_j,d>1)t_j^(ω(d))d^(−r)`

`=C_α(Z_r−1)/Z_s→0`                                (5)

by (3). This is the norm, not its square; the square also tends to 0.

From (4)–(5),

`ι(A_j)→(√κ·1,0)` strongly.                       (6)

**Key result:** the pure constant arithmetic vector belongs to 𝓗_α. It is not the image of a constant polynomial in the Haar-centred domain; it appears in the completion because that centring is not continuous for the law P_s.

## 5. The whole pure arithmetic factor and decomposition of the completion

The actions D_n of 007 are bounded on 𝓗_α and on both factors of the product. On the arithmetic factor,

`D_n1=X_n`;

on the Gaussian one, `T(D_nA)(y)=q_n(y)TA(n²y)`, a bounded operator that maps 0 to 0. Applying D_n to (6) gives

`ι(D_nA_j)→(√κ X_n,0)`.

Hence 𝓗_α contains all pure arithmetic vectors of the form `(X_n,0)` and their closure. The span of X_n is dense in L²(P_s): finite differences of valuation thresholds give indicators of any pattern of finite valuations; truncating the values of those coordinates and then enlarging the coordinates approximates any L² function of the product law. Thus

`L²(P_s)⊕{0}⊂𝓗_α`.                                 (7)

Define, without enlarging it by hypothesis,

`V:=closure_(ℒ_α){TA:A∈𝒜₀}`.

From each ι(A) one can subtract its pure arithmetic component, available by (7), and obtain `(0,TA)∈𝓗_α`. Taking closures,

`{0}⊕V⊂𝓗_α`.

The reverse inclusion is immediate: all initial images lie in the closed product `L²(P_s)⊕V`. Hence

**Theorem 1 (PROVED).**

`𝓗_α=L²(P_s)⊕V`                                    (8)

as an orthogonal sum, with the normalisation of the embedding ι given in §1.

`V=ℒ_α` is not claimed. Nor is it deduced that the ambient inversion of 008 preserves V: that needs another proof.

## 6. T is densely defined and NOT closable: explicit sequence

The approximation (6) and its D_n show that 𝒜₀ is dense in L²(P_s). Let

`f₂=X_2−1/2∈𝒜₀`, `Tf₂=q_2−1/2=:ψ₂≠0`.

Define

`C_j=D_2A_j−(1/2)A_j∈𝒜₀`,

`F_j=f₂−C_j∈𝒜₀`.

By the continuity on both factors of the actions used,

`C_j→f₂` in L²(P_s), `TC_j→0` in ℒ_α.

Consequently,

`F_j→0` in L²(P_s), `TF_j→ψ₂≠0` in ℒ_α.             (9)

This is the exact violation of the closability criterion. ψ₂ is nonzero because q_2(y)<1/2 for all y>0, and it has finite norm by (1).

**Theorem 2 (PROVED).** The operator `T:𝒜₀⊂L²(P_s)→ℒ_α` is densely defined and not closable.

The primorial sequence of 008 still has the divergence proved there; that proof is not corrected, nor is the strong limit (9) attributed to that sequence.

## 7. The three summands are now true orthogonal projections

In (8), decompose the arithmetic factor into its constant and its subspace of P_s-mean zero:

`𝓗_α=(L²_0(P_s)⊕0) ⊕ (C·1⊕0) ⊕ (0⊕V)`.

The three pieces of the kernel extend to the energies of those projections:

- `κG_s(A)=κ Var_s(A)` is the energy of the first summand.
- `κvv*(A)=κ|E_sA|²` is that of the second.
- `Π(A)=||TA||²` is that of the third.

In particular, for the unit vector `e=(1,0)∈𝓗_α`,

`||Proj_e ι(A)||²=κ|E_sA|²`.

The rank one of 005 **is** now realised as an orthogonal projection onto the pure arithmetic constant, a claim that was not justified before (6)–(8). This does not identify it with the pole of Q_T nor with cosh(x/2). In fact the family of LINK013 has zero cosh moment and M(F_T) of order T: the map 011 does not intertwine those two projections. This new fact about the auxiliary space does not pay for the pole of the paper.

## 8. Exact real PSD cone in the span of the three pieces

For real coefficients a,b,c, consider on **all** of 𝒜₀ the form

`𝔈_(a,b,c)(A)=aκVar_s(A)+bκ|E_sA|²+c||TA||²`.

Each summand is ≤||ι(A)||², so the signed form is continuous in the norm of 𝓗_α and extends to (8).

**Theorem 3 (PROVED).** The form 𝔈_(a,b,c) is PSD on all of 𝒜₀ if and only if

`a≥0`, `b≥0`, `c≥0`.

**Proof.** Sufficiency is 005. For necessity, PSD on the dense domain extends to its completion. Test it on three nonzero pure vectors:

1. `(X_2−2^(−s),0)∈L²_0(P_s)⊕0` forces a≥0.
2. `(1,0)` forces b≥0.
3. `(0,ψ₂)∈0⊕V` forces c≥0.

The three vectors belong to 𝓗_α by (8) and §6; their respective norms are positive. If a coefficient were negative, approximating the corresponding pure vector by images of 𝒜₀ would give an algebraic test of negative value. ∎

There is no need to transfer an inference from positive entries to PSD, nor to use an exploratory divergence.

## 9. Consequence for candidate 011 and limit of the classification

At α=1/4, LINK014 already excludes any uniform domination by Q_T of a fixed **non-negative nonzero** combination of those pieces, applied with exactly the coefficients a_d(F) of the map 011.

Theorem 3 now shows that allowing signed real coefficients does not enlarge the class **if the combination is required to be globally PSD on 𝒜₀**. Every fixed nonzero real combination with that property already belongs to the orthant excluded by 014 for that same map.

**Mandatory limits:**

- Signed forms that are positive only on a particular subspace, for example only on the image of a_d(F), are not classified.
- Transformations of the map, other kernels, T-dependent coefficients and signed cancellations outside this three-dimensional span are not excluded.
- The domain decomposition does not prove invariance/reductivity of V under the ambient FE, nor a link with gamma, comb or polar of Q_T.
- It is not claimed that non-closability prevents every alternative realisation. It is an exact property of the operator T defined here.

**Final status:** domain structure, non-closability and global PSD cone PROVED, favourable audit in AUDIT_015.md. D remains OPEN and active; no paper modified.
