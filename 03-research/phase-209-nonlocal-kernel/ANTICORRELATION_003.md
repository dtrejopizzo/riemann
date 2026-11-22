# ANTICORRELATION_003 — Strict cross sign in the discrete Gaussian without origin

2026-10-18. Pure mathematics. Status: **PROVED, favourable independent review in AUDIT_003.md**. No claim of global bibliographic novelty.
This is not a proof of the node, nor an O1 kernel identified with Q_T.

## 0. Corpus check and written difference

Consulted: the ROUTES-TRIED-INDEX index (README, literature and residues),
SPEC_SIGN_OBJECT_005, CELL_001, CONSTRUCTOR_002 and POSITIVE_ASSOCIATION_002.
PSD covariance by itself is covered by the objections to Gram. Here
**the negative sign of the cross entries** is proved for coprime
divisors, which does not hold for an arbitrary probability. It is distinct from
the positive association of theta with origin and from a homogeneous quadratic
positivity in theta: one works with degree-zero quotients and removes the
origin before computing. PF of the Xi kernel, Bohr/Helson,
and Perron–Frobenius for the node matrix are not reopened. The matrices in this note are
divisibility covariances; they are not the Weil form.

The geometric convexity of theta WITH origin is classical: Faulhuber and
Steinerberger, arXiv:1601.02972, Thm 2.3,
https://arxiv.org/html/1601.02972 . That result is not attributed to this round.
The targeted search did not find in the index the concavity of theta
MINUS one used below; this proves neither priority nor literature exhaustiveness.

## 1. Punctured geometric concavity theorem

Let

    θ(y)=Σ_{n∈Z}exp(-πyn²),  τ(y)=θ(y)-1>0.

**Theorem 1 (PROVED).** For all x∈R,

    d²/dx² log τ(exp x) < 0.

### Proof: y≥1/2

Consider the probability on n≥1 proportional to exp(-πyn²), and set
M=E(n²), V=Var(n²). With D=y∂y:

    D² log τ(y) = (πy)² V - πy M.

M≥1 and V≤E((n²-1)²). Dividing by the weight of n=1,

    V ≤ Σ_{n≥2}(n²-1)² exp[-πy(n²-1)].

Each y exp[-πy(n²-1)] decreases for y≥1/2. Let q=exp(-π/2)<1/4.
Using n²-1≥3(n-1) and (n²-1)²≤n⁴≤16^{n-1},

    πy V ≤ (π/2)Σ_{n≥2}(n²-1)²q^{n²-1}
           ≤ (π/2)Σ_{j≥1}(16q³)^j < π/6 < 1 ≤ M.

Hence D²logτ<0. No numerical evaluation of moments is required.

### Proof: 0<y≤1/2

Poisson gives

    τ(y)=y^(-1/2) A(y),
    A(y)=1-r+ε(y),  r=√y,
    ε(y)=2Σ_{n≥1}exp(-πn²/y).

A>0. Writing ε₁=Dε and ε₂=D²ε,

    A² D²log A
      = -r/4 +(1-r)ε₂ -rε/4 +rε₁ +εε₂ -ε₁²
      ≤ -r/4 +(1+ε)ε₂ +rε₁.                         (1)

Here ε, ε₁, ε₂ are positive. The following bounds are uniform:

    ε < 1/250,  ε₁ < 1/40,  ε₂/r < 11/50.            (2)

To verify them without theta numerics, let q₀=exp(-2π)<1/525.
The inequality q₀<1/525 follows from π>157/50 and
Σ_{k=0}^{20}(157/25)^k/k! > 525 (rational arithmetic).
The functions y^{-j}exp(-πn²/y) increase on 0<y≤1/2 for j=0,1,5/2.
Moreover n²≥1+3(n-1), n²≤4^{n-1}, n⁴≤16^{n-1}. Therefore

    ε ≤ 2q₀/(1-q₀³) < 1/250,
    ε₁ ≤ 4πq₀/(1-4q₀³) < 1/40,
    ε₂/r ≤ 8√2 π² q₀/(1-16q₀³) < 11/50.

The last bound uses ε₂≤2π² y^{-2}Σn⁴exp(-πn²/y).
All final comparisons are obtained with π<22/7, √2<99/70
and q₀<1/525 via rational fractions.
Inserting (2) into (1):

    A²D²log A < r[-1/4+(251/250)(11/50)+1/40]
               = -(103/25000) r <0.

Since logτ=-1/2 log y+log A, the theorem follows. ∎

## 2. Exact anticorrelation of coprime divisors

On Z\{0}, define P_y(N=n)=exp(-πyn²)/τ(y) and X_d=1_{d|N}.
Then

    r_d(y)=E_y X_d=τ(d²y)/τ(y),
    Cov_y(X_d,X_e)=τ(lcm(d,e)²y)/τ(y)-r_d(y)r_e(y).

**Corollary 2 (PROVED).** If d,e>1 are coprime, for all y>0:

    Cov_y(X_d,X_e)<0,

that is

    τ(d²y)τ(e²y)-τ(y)τ(d²e²y)>0.                    (3)

Proof: for f(x)=logτ(exp x), a=2log d>0, b=2log e>0,

    f(x+a+b)+f(x)-f(x+a)-f(x+b)
      =∫₀ᵃ∫₀ᵇ f''(x+u+v) dv du <0.

Exponentiate and use lcm(d,e)=de. ∎
This is a genuine cross sign, not the generic claim Cov≥0 as a matrix.

## 3. A positive matrix operator with additional structure

Let d₁,…,d_m>1 be a finite family of pairwise coprime integers, and
V_y=(Cov_y(X_di,X_dj)). Then:

- V_y is positive definite: if Σa_iX_di were almost surely constant,
  N=1 gives constant zero and N=d_i gives a_i=0.
- The off-diagonal entries are strictly negative by (3).
- V_y^{-1} has all its entries strictly positive.

The third conclusion is elementary: take s≥λ_max(V_y), B=sI-V_y.
B has nonnegative entries, positive off-diagonal ones, and spectral
radius s-λ_min(V_y)<s. Thus

    V_y^{-1}=s^{-1}Σ_{k≥0}(B/s)^k,

with strict positivity of every entry. For m=1 the conclusion is obvious.
V_y and its inverse are not identified with the P46 node.

## 4. Sign between complete prime factors

Let Y_p=v_p(|N|)=Σ_{j≥1}X_{p^j}. Since log|N| has all moments under
P_y, the following series converge absolutely with their weights:

    log|N|=Σ_p(log p)Y_p,
    Cov_y(Y_p,Y_q)=Σ_{j,k≥1}Cov_y(X_{p^j},X_{q^k})<0,  p≠q.

The integrability allowing the interchanges follows from
Σ_p(log p)Y_p=log|N| pointwise and
E(log²|N|)+(Elog|N|)²<∞. The completeness formula is equivalent to
Σ_{d|N}Λ(d)=log|N|; it is not used as a certificate for Q_T.

**Corollary 3 (PROVED, strict inequality).** For all y>0:

    Var_y(log|N|) < Σ_p(log p)² Var_y(Y_p).           (4)

The difference is exactly

    -2Σ_{p<q}(log p)(log q) Cov_y(Y_p,Y_q)>0.

The right-hand sum is finite since Σ_p(log p)²Y_p²≤log²|N|.
The strict sign uses, for example, the pair p=2,q=3. Unlike PSD of
a covariance, (4) expresses a signed cancellation between prime factors.

## 5. Positive Mellin and limits of the result

For a FINITE family of PAIRWISE COPRIME d_i>1 and α>0, the kernel

    M_α(d,e)=∫₀∞y^{α-1}Cov_y(X_d,X_e)dy

converges (CONSTRUCTOR_002, lemma 2), is positive definite and has negative
off-diagonal entries when the d_i are coprime. Its finite inverse is
entrywise positive by the previous argument. This holds at α=1/4.

**Do not confuse α=1/4 with having solved the critical weight of the node:** the
normalisation by τ(y) changes the transform; removing it introduces the
defects and counterterms computed in CONSTRUCTOR_002. It has not been shown
that (3) or (4) dominate the gamma deficit.

Nor is it proved that this sign fails when a prime is removed: the
deletion may preserve the anticorrelation. A specific link is needed
that ceases to be valid for the corresponding falsifier. The positive
result of this note is an auxiliary arithmetic lemma with strict sign,
not the complete object requested in O1 nor the closure of D.

Final review AUDIT_003: proof and constants accepted. The pairwise
coprimality condition of §5 has been made explicit. No Q_T link is proved.
