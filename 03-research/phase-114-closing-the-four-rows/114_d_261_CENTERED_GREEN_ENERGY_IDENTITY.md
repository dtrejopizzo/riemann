# D.261 — Exact Green energy of the centered Chebyshev channel

## Verdict

The remaining inverse term of D.214 can be written exactly as the Green
energy of the single signed measure \(dA=d\Psi-dx\), plus its cross with
the complete archimedean remainder.  This is an identity, not an
estimate.

It replaces the opaque expression \(q_N^*D_N^\dagger q_N\) by an explicit
operator-valued two-point kernel.  The kernel is positive definite because
it is a Green Gram.  What remains is an upper energy bound for the centered
measure with the exact born budget; positivity of the kernel alone does not
give that bound.

## 1. Normalized two-sided translation column

Use the old/born normalized coordinates of D.175.  On the common compact
smooth primitive core define, for \(1\le x\le N\),

\[
 \mathcal K_N(x)
 :=R_0^{\dagger/2}P_O\Pi_T
 x^{-1/2}(S_{\log x}+S_{-\log x})
 \Pi_TP_ES_E^{\dagger/2}.                          \tag{1.1}
\]

At a prime power \(x=p^k\), integration of (1.1) against the atom
\(\Lambda(p^k)\delta_{p^k}\) gives the exact weight

\[
 {\Lambda(p^k)\over\sqrt{p^k}}
 (S_{k\log p}+S_{-k\log p}).                       \tag{1.2}
\]

Integration against \(dx\) gives the continuous Chebyshev synthesis in
the same normalization.  Endpoint restrictions are read in the closed
form sense used in D.175.

Let

\[
 A(x)=\Psi(x)-x+1,
 \qquad dA=d\Psi-dx.                               \tag{1.3}
\]

Then the centered finite part of the normalized cross is

\[
 \boxed{
 q_{N,{\rm ar}}=-\int_{[1,N]}\mathcal K_N(x)\,dA(x).
 }                                                   \tag{1.4}
\]

The sign agrees with \(Q_N=-B_{{\rm nuc},N}\).  Formula (1.4) is the
operator-valued form of D.260(1.3).

## 2. Archimedean remainder and endpoint convention

Let \(q_{N,\infty}\) denote the remainder in the exact D.175 cross after
(1.4) is removed.  In (1.4) the \(dx\) term is compressed by the actual
support projections, so its endpoint Volterra pieces are already included
there and must not be counted twice.  With this convention the remainder
contains:

* the complete digamma/Gamma screw cross;
* the \(\beta\)-line and \(Q_{1/2}\) cross;
* the same Tate projection and reference normalizations as (1.1).

If one instead separates the continuous synthesis before support
compression, its endpoint Volterra terms move from (1.4) into
\(q_{N,\infty}\); the sum (2.1) and the energy (4.1) are unchanged.  We
use the first convention throughout this note.

This is a definition by an already proved termwise decomposition, not a
new unspecified correction.  Thus

\[
 \boxed{q_N=q_{N,\infty}+q_{N,{\rm ar}}.}           \tag{2.1}
\]

## 3. The Green kernel

Let \(D_N=I-T_N\ge0\) be the proved old-cell defect.  Define the
operator-valued kernel

\[
 \mathcal G_N(x,y)
 :=\mathcal K_N(x)^*D_N^\dagger\mathcal K_N(y).     \tag{3.1}
\]

It is positive definite in the extended-form sense: for any finite
\(x_j\) and born vectors \(e_j\),

\[
 \sum_{i,j}\langle e_i,\mathcal G_N(x_i,x_j)e_j\rangle
 =\left\|D_N^{\dagger/2}
   \sum_j\mathcal K_N(x_j)e_j\right\|^2\ge0.       \tag{3.2}
\]

If the vector in (3.2) has an unsupported component, both sides are
\(+\infty\).  Hence the formula carries the range condition rather than
silently discarding it.

## 4. Exact energy expansion

Substitute (1.4) and (2.1) into the D.214 inverse term.  Polarization gives

\[
\boxed{
\begin{aligned}
 q_N^*D_N^\dagger q_N
={}&q_{N,\infty}^*D_N^\dagger q_{N,\infty}\\
 &-2\mathrm{Re}
   \int_{[1,N]}
   \mathcal K_N(x)^*D_N^\dagger q_{N,\infty}\,dA(x)\\
 &+\int_{[1,N]}\!\int_{[1,N]}
   \mathcal G_N(x,y)\,dA(x)\,dA(y).
\end{aligned}}                                      \tag{4.1}
\]

All integrals are first finite Stieltjes sums plus an ordinary continuous
integral on the compact form core.  Their closed-form limits define (4.1).

Formula (4.1) retains the arithmetic--Gamma cross.  Estimating the three
lines separately would generally lose the sharp cancellation and is not
an admissible proof strategy.

## 5. Exact carrying inequality

With \(\mathcal M_N\) from D.214, the remaining cell condition is exactly

\[
\boxed{
 \mathcal E_N[dA]
 :=\mathcal M_N-q_N^*D_N^\dagger q_N\ge0,
}                                                    \tag{5.1}
\]

where the second term is the source expression (4.1).  Equality includes
the supported-range condition.

A noncircular closure may now take either of two equivalent forms:

1. factor \(\mathcal E_N[dA]=Z_N^*Z_N\) directly from the adelic
   Fourier/Poisson transport of \(dA\) and \(q_{N,\infty}\); or
2. construct \(\mathfrak V_N\) from the same data with
   \(q_N=D_N^{1/2}\mathfrak V_N\) and
   \(\mathfrak V_N^*\mathfrak V_N\le\mathcal M_N\).

Neither \(Z_N\) nor \(\mathfrak V_N\) may be defined by the pseudoinverse
appearing in (4.1).

## 6. What has been reduced

The unresolved mathematics is no longer a sum over separate powers or an
unspecified “Gamma correction”.  It is the sign of one explicit Green
energy functional of the centered Chebyshev measure, with a completely
specified archimedean cross.

The next source calculation is to insert the paired Blaschke-delay
representation of D.249 into \(q_{N,\infty}\) and determine whether the
three lines of (4.1) combine with \(\mathcal M_N\) into a square before any
absolute-value estimate.

## 7. Classification

* Translation-column formula (1.1)--(1.4): **PROVED FROM D.175/D.260**.
* Complete remainder decomposition (2.1): **PROVED BY DEFINITION FROM
  THE TERM-BY-TERM CROSS**.
* Green kernel positivity (3.2): **PROVED OPERATOR IDENTITY**.
* Exact energy expansion (4.1): **PROVED**.
* Sharp energy inequality (5.1): **OPEN; EQUIVALENT TO THE D.214 GATE**.
* Source square/contractive transport: **OPEN**.
* Row D: **OPEN**.
