# 104_03 — Audit of the binomial contour and of the residues

This document is not the front of Phase 104 and
contains no new estimate of A1.

**Verdict.** The small contour of 103_66 is exact and unconditional. The trivial poles
of \(R\) have the sign expected locally, but **the sum of the bare residues
diverges**. The convergent sum appears only after keeping the canonical genus-one
normalization; then the trivial block is exactly

\[
 \mathcal T_n^{\rm triv}
 =\sum_{a=3,5,\ldots}{1-(1-1/a)^n\over a}
 =\Delta A_n+{\gamma+\log(4\pi)\over2}-1.
\tag{0}
\]

Therefore the trivial residues do not reconstruct \(A_n\) directly: after the canonical
subtraction, they reconstruct its **first difference**, up to the explicit affine term of (0).
A deformation that sums only the residues \((1-1/a)^n/a\) is illegitimate.

---

## 1. The exact local contour

Set

\[
 Z(t)=t\zeta(1+t),\qquad h(t)=\log Z(t),\qquad
 R(t)=-{Z'(t)\over Z(t)}=-{\zeta'\over\zeta}(1+t)-{1\over t}.
\tag{1}
\]

The pole of \(\zeta(1+t)\) at \(t=0\) cancels: \(Z\) is entire, \(Z(0)=1\), and \(R\) is
analytic in a disc around the origin. Write

\[
 R(t)=\sum_{j\ge0}r_jt^j,\qquad
 C_n:=\sum_{j=0}^n{n\choose j}r_j.
\tag{2}
\]

### Theorem 1 (binomial contour)

If \(0<r<\mathrm{dist}(0,\{t:Z(t)=0\})\), then

\[
 \boxed{
 C_n={1\over2\pi i}\int_{|t|=r}
 R(t){(1+t)^n\over t^{n+1}}\,dt.}
\tag{3}
\]

Equivalently, with \(t=z/(1-z)\),

\[
 \boxed{
 \sum_{n\ge0}C_nz^n={1\over1-z}R\!\left({z\over1-z}\right).}
\tag{4}
\]

*Proof.* In (3), the residue at zero of
\(r_jt^j(1+t)^nt^{-n-1}\) is \({n\choose j}\) for \(0\le j\le n\), and zero
for \(j>n\). The sum is finite. For (4), substitute the Taylor series of \(R\) and use
\([z^n]z^j(1-z)^{-j-1}={n\choose j}\). The contour has not been moved across any zero.
\(\square\)

No logarithm branches are needed for (3): \(R=-Z'/Z\) is meromorphic and single-valued. A
branch of \(h=-\int R\) needs to be fixed only if one integrates by parts using the primitive.

### Corollary 1.1 (relation to the Li coefficients)

If \(P_n=\lambda_n-A_n\) is the prime block in the Phase 103 normalization, then

\[
 C_n=-\Delta P_n=\Delta A_n-\Delta\lambda_n,
\qquad
 \boxed{\lambda_N=A_N-\sum_{n=0}^{N-1}C_n.}
\tag{5}
\]

*Proof.* If \(h(t)=\sum_{k\ge1}p_kt^k\), then
\(r_j=-(j+1)p_{j+1}\). The exact formula
\(P_n=\sum_{k=1}^nk{n\choose k}p_k\) from 103_52 gives
\(\Delta P_n=\sum_{k=1}^{n+1}k{n\choose k-1}p_k=-C_n\). Telescoping from
\(\lambda_0=A_0=0\) gives the second identity. \(\square\)

This is why the 103_66 contour controls a first difference and not
\(A_n\) directly.

---

## 2. Singularities and local sign

The poles of \(R\) are the zeros of \(Z\), with multiplicity and negative residue:

* a nontrivial zero \(\rho\) of \(\zeta\) produces \(t_\rho=\rho-1\) and
  \(\mathrm{Res}_{t=t_\rho}R=-m_\rho\);
* the trivial zero \(-2k\) produces
  \(t_k=-(2k+1)=-a_k\), \(a_k=3,5,\ldots\), and
  \(\mathrm{Res}_{t=-a_k}R=-1\).

At \(t=-a\),

\[
 {(1+t)^n\over t^{n+1}}
 =-{1\over a}\left(1-{1\over a}\right)^n,
\tag{6}
\]

so the residue **of the integrand** in (3) is

\[
 +{1\over a}\left(1-{1\over a}\right)^n.
\tag{7}
\]

If a large contour contains that pole, the residue theorem says

\[
 C_n=I_{\rm exterior}-\sum_{\text{crossed poles}}\mathrm{Res}(RK_n).
\tag{8}
\]

That is why the bare contribution of (7) enters \(C_n\) with a negative sign. Both signs —
that of the local residue and that of its transfer into (8) — must be tracked; confusing them
changes the result.

---

## 3. Why the bare sum of residues is false

For \(a=3,5,\ldots\), the term that (8) would try to sum is

\[
 -{1\over a}(1-1/a)^n=-{1\over a}+O_n(a^{-2}),
\tag{9}
\]

and therefore diverges. There is no "sum of all trivial residues" formed with (9).
The exterior arc and the Hadamard normalization cannot be discarded separately.

The canonical genus-one factorization of \(Z\) assigns to the zero \(-a\) the factor

\[
 E_1(-t/a)=(1+t/a)e^{-t/a}.
\tag{10}
\]

Its contribution to the normalized logarithmic derivative is

\[
 -{d\over dt}\log E_1(-t/a)
 ={1\over a}-{1\over a+t}.
\tag{11}
\]

The constant \(1/a\), which is precisely the canonical exponential omitted by the bare
residue, contributes \(1/a\) to the binomial transform. From (11) one obtains

\[
 \boxed{
 C_n[-a]={1-(1-1/a)^n\over a}>0,\qquad n\ge1.}
\tag{12}
\]

Now \(C_n[-a]=O_n(a^{-2})\), so the sum over \(a=3,5,\ldots\) converges
absolutely.

### Theorem 2 (exact relation to the archimedean block)

Let \(c=(\gamma+\log(4\pi))/2\). Then

\[
 \boxed{
 \sum_{a=3,5,\ldots}{1-(1-1/a)^n\over a}=\Delta A_n+c-1.}
\tag{13}
\]

*Proof.* The exact odd formula from Phase 103 gives

\[
 \Delta A_n=-c+\sum_{a\ \mathrm{odd}}{1-(1-1/a)^n\over a}.
\tag{14}
\]

The summand \(a=1\) equals \(1\); separating it proves (13). \(\square\)

This agrees with 103_60: there the trivial factor contributes to \(P_n\)
\(\tau_n(a)=1-(1-1/a)^n-n/a\); since \(C_n=-\Delta P_n\), (12) is recovered.

**Conclusion of the trivial audit.** The claim "the trivial residues reconstruct the odd
harmonic sum of \(A_n\)" was incorrect if taken literally. The correct statement is (13), and
it requires the canonical exponential.

---

## 4. The Cayley line

On \(\Re t=-\tfrac12\),

\[
 |1+t|=|t|,
 \qquad
 \left|{(1+t)^n\over t^{n+1}}\right|={1\over|t|}.
\tag{15}
\]

This is an **unconditional geometric identity for every height**. Under the inverse of
\(t=z/(1-z)\), it is the circle \(|z|=1\). A nontrivial zero produces
\(t_\rho=\rho-1\), and it lies on this line if and only if \(\Re\rho=1/2\).

Two precautions:

1. Platt–Trudgian allows stating that the zeros up to \(H\) lie on the line; it does not make
   identity (15) "legitimate" — it already was. Those zeros are poles **on** the path and
   require specified indentations or principal values.
2. Without RH there can be poles on both sides. Moving the circle of (3) to the line does not
   produce an estimate free of them. The complementary collective identity imported from
   Lagarias must be used with the sign erratum **and the horizontal repair
   \(T=2\sqrt n+\varepsilon_n\)** from 104_02:
   \(\lambda_n=A_n+\lambda_n(\sqrt n)+O(\sqrt n\log n)\). It is neither an automatic
   consequence of (15), nor a lower bound for the incomplete block.

---

## 5. Arcs, branches, and exact scope

The only contour proved here is the local circle of (3). A global deformation
simultaneously requires:

* canonical products so that the pole sums converge;
* an indentation prescription for poles on the path;
* arc bounds for \(R(t)(1+t)^nt^{-n-1}\);
* if \(h=-\int R\) is used, a branch on each component of the cut plane.

The bound \(R(t)=O(\log|t|)\) alone does not repair (9): the problem is the splitting of a
convergent canonical series into two divergent series. For this reason 104_03 **does not
rederive** the corrected global identity audited in 104_02 and does not claim a new
summation-over-zeros formula.

---

## 6. Verifier

tools/contour_binomial_check.py performs two distinct checks.

1. It extracts \(C_n\) from (4) in complex128, reconstructs \(\lambda_N\) via (5), and compares
   it with an independent extraction from \(\xi'/\xi\). It is a diagnostic, not a certificate.
2. With the --certified option, it reconstructs outward intervals for
   \(\lambda_{20},\lambda_{60},\lambda_{149}\) using the same rational engine from 103_51 and
   separately reports strict inclusion of the float64 value and compatibility at its rounding
   floor. Only the interval is certified; the FFT falling outside it due to rounding does not
   refute the identity, and falling inside does not certify the FFT.

Quick run:

    n       lambda(contour)       lambda(xi)       disagreement   radius-stability
    20   8.769276872093   8.769276872093    8.53e-14       0.00e+00
    60  57.133099574875  57.133099574874    2.27e-13       7.11e-15
    149 205.922618629825 205.922618629830   -4.46e-12      -1.47e-11

Radial stability is reported separately and is not turned into a certificate. The trivial
table of the same program
confirms convergence to (13), while the bare sum of (9) keeps drifting
logarithmically.

---

## Status

| claim | state |
|---|---|
| local contour (3)–(4) | **unconditional theorem** |
| signs of the poles and trivial residues | **audited** |
| canonical trivial–archimedean relation (13) | **unconditional theorem** |
| Cayley modulus identity | **unconditional geometric theorem** |
| global deformation without canonical normalization | **no-go: divergent series (9)** |
| full/incomplete collective identity | imported with the corrected sign from 104_02; does not bound the incomplete block from below |
| proof of A1/RH | **not contained here** |
</content>
