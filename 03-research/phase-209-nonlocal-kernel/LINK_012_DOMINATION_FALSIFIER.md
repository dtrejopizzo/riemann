# LINK_012 — Certified falsifier of the domination of map 011

2026-10-19. **PROVED by ball arithmetic and validated integrals with analytic tails:** for the map U of LINK011, with exactly its normalisation, the inequality `Q_T(F)≥||UF||²` is false. An explicit two-mode test is used, not the ZCERT margin nor zeros. This discards that particular domination; D and other maps remain open.

## 0. Corpus and class being tested

Consulted: the project rules, the ROUTES-TRIED-INDEX index (LINK011 entries and their limits, residues 06), master grid, crossword, LINK011/AUDIT011 and the definitions of Paper46 eq:Aform and thm:A. The equality Q_T=||UF||² was already refuted and **is not retried**.

**New written reason:** the Mellin–Gauss map 011 and its scale are kept exactly, and the domination that had remained open is now tested. The question changes to the sign of the remainder `Q_T−||UF||²`. The proof starts from a falsifier; it does not attribute to the remainder the sign of a high-frequency approximation.

An exploratory two-mode diagnostic gave a separation of order 0.25, which motivated the certification below. The diagnostic is not used as proof. No other auxiliary kernel is introduced.

## 1. Explicit polar-free test

Fix

`T=4/5`, `ω=π/(2T)`,

`r=3(ω²+1/4)/(9ω²+1/4)`,

`f(x)=cos(3ωx)+r cos(ωx)`, `|x|≤T`,

`F=f/sqrt(N)`, `N=T(1+r²)`.

Extend by zero outside the interval. The two frequencies are orthogonal, f(±T)=0 and the norm is exactly N.

The polar integral of cos(ωx) is `2ω cosh(T/2)/(ω²+1/4)`; that of cos(3ωx) is `−6ω cosh(T/2)/(9ω²+1/4)`. By the choice of r,

`∫_(−T)^T F(x)cosh(x/2)dx=0`.

F is even and belongs to H¹_0([−T,T]); in particular it has finite gamma energy and lies in the form carrier used for the Dirichlet modes of Paper46.

## 2. Lower bound for the U energy using an already proved term

Use the exact decomposition of CONSTRUCTOR005 with α=1/4, s=1/2,

`S=−R=κG_s+κv_s v_s*+Π`,

`κ=−2π^(−1/4)Γ(1/4)ζ(1/2)>0`, `v_s(d)=d^(−1/2)−d^(−1)`.

Since the other two terms are PSD, for the map 011 one has

`||UF||²≥κ|M(F)|²`, `M(F)=Σ_(d≥2)a_d(F)v_s(d)`.

The series converges absolutely by the bounds of LINK011. Substituting a_d and grouping the integer product k=dn:

`M(f)=2∫_(−T)^T f(x)e^(x/2)`

` ·[2Σ_(k≥1)b_k exp(−πk²exp(2x))−z_c τ(exp(2x))]dx`,

`b_k=Σ_(d|k,d≥2)[d^(−1/2)−d^(−1)]`,

`z_c=ζ(3/2)−ζ(2)`.

Here `Σ_(d≥2)v_s(d)/d=z_c`. This identity avoids truncating the double sum in d,n inconsistently.

### Explicit tail of the profile, with no assumed signs on f

One has `0≤b_k≤k`. Let `a=πexp(−2T)` and truncate at k≤K=12. For t≥K, both exp(−at²) and t exp(−at²) decrease. By comparison with the integral,

`2Σ_(k>K)b_k exp(−ak²)≤exp(−aK²)/a`,

`2Σ_(k>K)exp(−ak²)≤exp(−aK²)/(aK)`.

Since `|f|≤1+r` and exp(x/2)≤exp(T/2), the absolute error in M(f) is bounded by

`ε_M=4T(1+r)exp(T/2) exp(−aK²)/a ·(1+z_c/K)`.

The code evaluates this formula with balls and obtains `ε_M<2.370·10^(−39)`.

## 3. Upper bound for Q_T without zeros nor uncontrolled numerical subtraction

The definition of Paper46 is evaluated directly:

`Q_T(F)=gamma(F)−Σ_(n<exp(2T)) [2Λ(n)/√n]c_F(log n)`.

For T=4/5 the only von Mangoldt terms are n=2,3,4. Their trigonometric autocorrelations are integrated on the exact interval `[−T,T−log n]`.

The Fourier transform of f is evaluated as an entire function:

`f̂(t)=T[sinc((t−3ω)T)+sinc((t+3ω)T)]`

`      +rT[sinc((t−ω)T)+sinc((t+ω)T)]`.

Gamma is integrated on 0≤t≤H=100 with the exact symbol

`m(t)=Re ψ(1/4+it/2)−logπ`.

For complex validation the analytic meromorphic extension is used,

`m_c(z)=[ψ(1/4+iz/2)+ψ(1/4−iz/2)]/2−logπ`,

which coincides with m on the real axis. One hundred unit segments are integrated by acb.integral, with ball enclosures, tolerances 10^(−18) and 128-bit precision. Sinc avoids the false removable poles of the rational formula.

### Explicit gamma tail

For t≥H>6ω, the equivalent rational formula gives

`|f̂(t)|≤A/t²`, `A=(8/3)ω(r+3)`.

Moreover, for t≥1,

`m(t)≤2log t+10`.

**Proof of the last bound:** the Lévy representation uses

`K(u)=1/[2sinh(u/2)]+1/[2cosh(u/2)]≤1/u+1/2`.

Split the integral into `(0,1/t)`, `(1/t,1)` and `(1,∞)`, using respectively `1−cos(tu)≤t²u²/2`, ≤2 and ≤2. The first piece is ≤1/4+1/(12t); the second ≤2logt+1−1/t. In the third,

`∫_1^∞K≤4exp(−1/2)/(1−exp(−2))<28/9`,

since exp(−1/2)<2/3 and exp(−2)<1/7. Twice that tail, plus the other constant terms, is <10. C₀=ψ(1/4)−logπ<0 can be omitted for this upper bound. ∎

Hence the omitted part of the gamma of f has the upper bound

`ε_Γ=(A²/π)H^(−3)[(2/3)logH+2/9+10/3]`.

That tail is not replaced by zero. The certificate obtains `ε_Γ<0.000649818` before normalising by N.

## 4. Reproducible certificate and separate inequalities

Files:

- `LINK012_data/certify.py`: main certificate with python-flint/Arb.
- `LINK012_data/certified.json`: full ball output.
- `LINK012_data/explore.py`: prior diagnostic, with no probative use.

The certificate integrates analytic functions via acb.integral; the only infinite sums or integrals are covered by the explicit bounds above. The real constants Γ and ζ are evaluated with Arb ball arithmetic, without information about zeros.

For the normalised test, the enclosures give

`Q_T(F) < 0.002351`,

`|M(F)| > 0.1812652378`,

`κ > 7.95393245`,

`||UF||² ≥κ|M(F)|² >0.26134304`.

Consequently

`Q_T(F)−||UF||² < −0.25899 <0`.                     (★)

The proof does not need to know the whole matrix of U nor its exact norm: one PSD term of its decomposition suffices. Nor does it presuppose the sign of Q_T; it only uses a direct upper bound.

## 5. If the carrier is formulated on C_c∞ tests

The extended test f is H¹_0, and the margin (★) is strict. It can be approximated by even C_c∞((−T,T)) functions in H¹. Correct its polar moment with a fixed even test χ of nonzero moment; the correction coefficient tends to zero.

Q_T is continuous for H¹ convergence: the gamma symbol grows only like log(2+|t|), and the comb is bounded on L². U is bounded on L² by LINK011. Hence the remainder converges and stays negative for sufficiently close approximants. Thus the domination also fails on that smooth core, not only in the realisation by Dirichlet modes.

## 6. Exact scope

What is refuted is **the inequality with the map 011 and its fixed normalisation**. It is not claimed that every smooth positive form is too large, nor that no rescaling admits domination, nor that no other map from the carrier to −R exists. No general exclusion of compressions or of O1 is obtained.

This result completes the examination of the two direct claims proposed for this candidate: equality failed in LINK011 and domination now fails by the explicit test. The positive kernel −R, its FE and goal D do not change status. No paper was modified.

**Status:** certified falsifier of the domination 011; independent review favourable in AUDIT_012.md. D remains open and active.


## 7. Independent verification of gamma and comb without quadrature

An exact formula, independently reviewed, was also obtained
for I(a)=∫_0^(2T) exp(−au)c_F(u)du of the normalised test:

    I(a)= a/(1+r²)[r²/(a²+ω²)+1/(a²+9ω²)]
          +(1+exp(−2aT))ω²/[T(1+r²)]
             ·[r/(a²+ω²)−3/(a²+9ω²)]².

To check it, let v(x)=∫_(-T)^T exp(−a|x−y|)F(y)dy.
Then v''−a²v=−2aF, with v'(T)=−av(T), v'(−T)=av(−T).
The particular solution for each cosine has coefficient 2a/(a²+ω_k²).
The even homogeneous correction is Ccosh(ax), where
C=2ωexp(−aT)/sqrt(T(1+r²))·[r/(a²+ω²)−3/(a²+9ω²)].
Using I(a)=½∫Fv gives the formula above, including sign and factor 2.

Since K(u)=2Σ_(j≥0)exp(−a_j u), a_j=2j+1/2, one obtains

    gamma(F)=C₀+2Σ_(j≥0)[1/a_j−I(a_j)].

All summands of the Lévy term are non-negative. The inequality
1−c_F(u)≤u²||F'||²/2 gives, for the tail j≥J,

    0≤tail≤2||F'||²[a_J^(−3)+1/(4a_J²)],
    ||F'||²=ω²(r²+9)/(1+r²).

Comparison of the decreasing series with its integral justifies the last
bracket. `LINK012_data/check_laplace.py` evaluates J=200 with Arb 128-bit balls;
the comb is obtained directly from G11,G33,G13 of P46 lem:combsine,
with coefficients (r,−1)/sqrt(1+r²). The independent output is in
`LINK012_data/check_laplace.json` and gives

    Q_T(F)<0.001647953.

This check avoids any quadrature of gamma and comb. The lower
bound for M remains certified by the analytic integral and the Gaussian tail
of the main certificate. The two upper bounds for Q are compatible.
