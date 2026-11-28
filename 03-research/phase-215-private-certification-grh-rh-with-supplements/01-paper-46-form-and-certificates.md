# Paper 46 Weil form and numerical certificates

**Update from the second audit:** both windows were verified by means of reproducible programs and arguments: [first window](deep-review/NUMERICS-46.md), [second window](deep-review/WINDOW-28022.md) and [functional bridge](deep-review/WINDOW-28022-BRIDGE.md). Z1 was verified by isolation and certified counting of all the zeros up to 21. The detailed sections below keep the initial record; their statements of absent certificates or pending inertias are superseded.


Review of the three points requested, on the local `main.tex` identified in `evidence/sources.json`. The line numbers correspond to that file, not to pages of the PDF. **(a)** means argument checked in the scope indicated; **(b)**, localised failure; **(c)**, step not verified. A conclusion (c) does not assert that the statement is false.

| Point | Verdict | Reason |
|---|---|---|
| Positivity of `W_T` for every T equivalent to RH | **(a)** | Explicit formula, density in the form norm and negative primitive test of paper 45. |
| Bounds `10^-18` and `2.5·10^-12` | **(a)** by reconstruction | Four inertias verified with Arb; analytic remainder and tails checked. Keep directed rounding. |
| Facts Z1–Z3 | **(a)** in the scope used | Z1 isolated and counted with Arb; Z2 and Z3 collated with sources. |
| Bound up to `T=2.8022` and use of Z1–Z3 in it | **(a)** with research annexes | Program found, 17 checks reproduced and functional bridge reviewed twice. The paper by itself omits that development. |

## Equivalence with RH

The definitions are in paper 46, lines 248–316, and the proof of `thm:all-support` in 5460–5505. With the transform `Fhat(τ)=∫F(t)e^{iτt}dt`, the symbol is

`m(τ)=Re ψ(1/4+iτ/2)−log π`,

and each prime power carries `2Λ(n)/sqrt(n)` in the cosine symbol. The explicit formula for an autocorrelation gives

`W_T(F)=Σρ Φ_F(ρ) overline(Φ_F(1−barρ))`.

The polar term is `2Re(A overline B)`, not `|A|²+|B|²`. Under RH each summand is `|Φ_F(ρ)|²`. For smooth real tests the formula is in lines 260–271; the complexification is valid because the cross sum for two real tests is real on pairing conjugate zeros.

The extension to `D_T` does not require assuming a priori convergence of the sum for every rough test: the density in the weighted norm of `lem:form-density` (457–487) and the positivity for differences make the transforms a Cauchy sequence in `ell²`. Convergence in `L²(-T,T)` identifies each coordinate. The argument of contraction of the support followed by mollification proves the density; the continuity of the moments and the logarithmic growth of `m` give continuity of the form.

For the converse I reviewed the concrete proof of paper 45, `thm:sufficiency`, lines 1403–1559. A zero off the line produces an orbit of four points `±z0,±bar z0`. A polynomial annihilates the other zeros of bounded height and the points `±i/2`; a convolution power of a bump controls the tail. The adjustment with `α+βz0²`, possible because `Im(z0²)≠0`, makes the orbit contribute `−4m0`. The tail is `O(4^-N)` with constants independent of N, since `Σ m(z)/(1+|z|)²<∞`. The tests constructed are real, primitive and compactly supported. A sufficiently large window contains the support and has negative form. The support depends on N: it is not asserted that a prefixed window detects all the zeros.

This equivalence does not prove that the form is positive. It is compatible with the later automorphic proof remaining unverified. The classical antecedent is [Connes–Consani, appendix C, with attribution to Yoshida](https://arxiv.org/html/2006.13771).

## Certificates in the window of log 5

The first step that I cannot certify is paper 46, lines **1616–1617**: the ball enclosures would give the four bounds and the program is not reproduced. The text develops the reduction, but the table of pivots (1772–1783) is the result that must be proved, not a substitute for the computational proof.

The proposition `prop:lowercert` (1695–1732) has a correct functional justification: on the complement of the first Legendre functions the operator is bounded below by `q_Y>0`; the Schur complement is dominated by the matrix `R`; the inertia of the border with `c=0` subtracts exactly one negative direction; with `c=−1/2` and `c=+1/2` one recovers, respectively, the even and odd polar terms. The estimates by means of the trace of the compression of the band-limiting operator are also sufficient as a method.

To complete the numerical verification the following are needed:

1. Exact values or intervals with directed rounding for `T`, `s_infty`, nodes, weights, entries and tail bounds.
2. Code of the quadrature and proof of the analytic bound for the remainder that it actually implements.
3. Certified matrices or a reproducible generator of them, with the four values of μ.
4. Verifications of `q_Y>0`, invertibility of the change of basis, sign of the border block and all the pivots of the Schur complement, including the contributions of the tails.

The notebook of paper 58 does not contain the identifying parameters of these certificates: `193.13`, `640` or `120110026807`. Its README declares expressly that it contains small consistency checks, not a proof of the theorems in their range. I did not run those checks as a substitute for the absent inertias.

The script `evidence/check_constants_46.py` reproduces **with multiple precision, without intervals**, these consistencies:

| Quantity | Approximate value |
|---|---|
| `240T` | `193.132549492092…` |
| `A` | `2.94197352522362…` |
| `m(240)−A` | `0.700787608327198…` |
| `Lambda*_280` | `4.4046093678·10^-20` |
| `Lambda*_330` | `3.8625471440·10^-70` |

The last two are consistent with the printed bounds `4.5·10^-20` and `3.9·10^-70`; they do not certify the matrices. There is a necessary editorial correction in the data of line 1766: if `omega_-` is used as the upper bound defined in 1688, then `omega_-≥2A=5.88394705…`; **the decimal `5.8839` is not a valid upper bound**. As a rounded summary it is admissible; as a literal constant of the certificate it must be replaced by an upward bound. It is not inferred from this that the spectral bounds are false. Also `c_*=193.13` is only an abbreviated presentation of `240T`, not its exact value.

## Zeros and larger window

Z2 (1795–1796) uses a height smaller than that of [Platt–Trudgian, theorem 1](https://arxiv.org/pdf/2004.09765): `3·10^12 < 3 000 175 332 800`. This reduction of height is correct and does not assume global RH.

The coefficients and range of Z3 (1797–1798) were collated with the formulation of Rosser reproduced in the article of [Faber–Kadiri](https://www.cs.uleth.ca/~kadiri/articles/New-Bounds-for-Psi-Math-Comp-Faber-Sept2013.pdf). For `N(t)` defined with `γ≤t`, the non-strict version of the inequality is also obtained by taking right limits at the heights of zeros. The step `N(t)≤t log t/(2π)` for `t≥21` is correct: the printed lower difference is positive at 21 and increasing. The Stieltjes integration of `lem:zerosum` keeps the boundary term with the correct sign; discarding it increases the bound.

Z1 (1790–1794) asserts simplicity and non-existence of other zeros up to 21, together with an interval for the first ordinate. It is consistent with the classical values, but I have not reconstructed the counting and isolation from the original certificates: **(c)** for that independent verification. Evaluating `ζ(1/2+it)` numerically would not suffice to rule out omitted zeros off the line.

In `thm:margin` (1864–1890), Z1 eliminates the first pair, Z2 converts the contributions of intermediate height into squares and the counting controls the rest by absolute value. It is an argument for an **upper bound** of the minimal form, not a lower bound. There is no valid deduction of positivity from that upper bound tending to zero, and the text does not make one there.

For the **lower** bound at 2.8022, the first pending step is **1915–1930**, `eq:power-window`: a compact filter, 2048 continuous Schur rows and 17 verifications are announced; their formulas and execution are missing. Z1–Z3 by themselves do not allow the exponent `120110026807` to be checked. The section declares that no other statement of the paper depends on this bound; its lack of certification does not by itself refute the automorphic chain.
