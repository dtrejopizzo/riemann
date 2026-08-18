# D.174 — Gamma endpoint-log Carleson gate

## Verdict

The exact endpoint identity

\[
 G_\Gamma F(t)=-\frac12F(t)\log(T^2-t^2)+R_F(t)       \tag{0.1}
\]

locates the only possible source of the two logarithms required by the
phase-defect layer estimate of D.171.  It does **not** by itself prove that
estimate.  The remainder in (0.1), although analytic when evaluated on a
fixed polynomial, is a nonlocal operator of logarithmic order on the full
form domain.  Treating it as an (L^2)-bounded perturbation is invalid.

The correctly typed endpoint theorem is the output-resolvent estimate

\[
 \boxed{
 \bigl\|L_\partial\,\mathcal T_\partial
 E_{D_{\rm out}}((0,\delta])y_N\bigr\|^2
 \le C_N\delta,\qquad
 L_\partial(t)=1+\left|\log {\rho(t)\over\rho_0}\right|,} \tag{0.2}
\]

where (\mathcal T_\partial) is the exact boundary trace/synthesis appearing
in the normalized born-cell column, not an arbitrary pointwise trace.  If
the normalized born cell has width comparable to (\delta), (0.2) gives

\[
 \mu_N^y((0,\delta])
 \ll {C_N\delta\over(1+|\log\delta|)^2},              \tag{0.3}
\]

and therefore the desired output capacity.  Thus the endpoint route and
the return-moment route D.172 ask for the same extra power of logarithmic
boundary decay.

Known boundary regularity for the logarithmic Laplacian only gives
(|u(x)|=O(|\log\rho(x)|^{-\tau})) for every
(\tau<1/2) under a positive maximum principle.  Squaring this gives a
power strictly smaller than one, whereas (0.3) requires power two.
Moreover, the maximum principle for that operator is equivalent to
positivity of its first Dirichlet eigenvalue.  Hence neither statement can
be imported as the missing row-D estimate.

## 1. Why a reciprocal logarithm is the exact threshold

Put (\rho=T-|t|) and let (0<\ell<\rho_0).  On the endpoint strip
(\rho<\ell),

\[
 L_\partial(t)\ge 1+\log(\rho_0/\ell).               \tag{1.1}
\]

Consequently every vector-valued function (u) satisfies

\[
 \|1_{\{\rho<\ell\}}u\|^2
 \le {\|L_\partial u\|^2
       \over(1+\log(\rho_0/\ell))^2}.                \tag{1.2}
\]

Apply this to the boundary realization of
(E_{D_{\rm out}}((0,\delta])y_Ne).)  With
(\ell\asymp\delta), (0.2) and (1.2) yield (0.3), after
undoing the already fixed born-cell normalization.  No sign is used in
this implication: all the substantive content is in (0.2).

The exponent two is sharp for the dyadic Stieltjes summation.  If instead

\[
 \mu_N^y((0,2^{-j}])\le C2^{-j}(1+j)^{-\alpha},       \tag{1.3}
\]

then

\[
 \int d^{-1}\,d\mu_N^y(d)
 \lesssim C\sum_{j\ge0}(1+j)^{-\alpha}.              \tag{1.4}
\]

The right side is finite exactly for (\alpha>1).  A pointwise amplitude
(|\log\rho|^{-\tau}) gives (\alpha=2\tau); the standard range
(\tau<1/2) is therefore strictly on the divergent side of (1.4).

## 2. Why the analytic polynomial remainder is not a bounded operator

For a polynomial (F), D.173 writes the remainder in (0.1) using

\[
 \int q(|t-s|){F(t)-F(s)\over t-s}\,ds.              \tag{2.1}
\]

The apparent singularity is removable pointwise for a fixed smooth (F),
which is why the resulting function is analytic on each contact cell.
But on oscillatory functions (F_\xi(t)=\chi(t)e^{i\xi t}), (2.1) has
size comparable to (\log|\xi|)F_\xi) in the interior.  This is the same
logarithmic order as the Fourier symbol
(\mathrm{Re}\,\psi(5/4+i\xi/2)).  Therefore no estimate

\[
 \|R_F\|_2\le C_T\|F\|_2                             \tag{2.2}
\]

holds on the full form domain.  Any argument which solves (0.1) for (F)
by dividing by the endpoint logarithm and uses (2.2) has discarded the
principal nonlocal part of the Gamma operator.

The exact polynomial collapse remains decisive for directed finite
certificates, because there the degree is fixed and every remainder is
enclosed.  It cannot be promoted to a uniform spectral-layer estimate
without controlling the graph norm of (2.1).

## 3. Comparison with logarithmic-Laplacian boundary theory

Chen and Weth's Dirichlet theory for the logarithmic Laplacian proves, for
bounded forcing and a domain with a uniform exterior sphere condition,

\[
 |u(x)|=O\bigl(|\log\rho(x)|^{-\tau}\bigr),
 \qquad 0<\tau<\frac12.                              \tag{3.1}
\]

Their barrier is explicitly (|\log\rho|^{-\tau}).  The same work proves
that its weak maximum principle holds exactly when the first Dirichlet
eigenvalue is positive.  These results confirm that (0.1) has the correct
boundary scale, but they do not furnish (0.2):

1. (3.1) loses more than the logarithmic power needed in (1.4);
2. it concerns solutions with bounded forcing, not the operator-valued
   defect spectral projection in (0.2);
3. its maximum-principle hypothesis is itself a positivity assertion and
   cannot replace row D.

Primary reference: H. Chen and T. Weth, *The Dirichlet Problem for the
Logarithmic Laplacian*, arXiv:1710.03416, especially Theorems 1.8 and
1.11.

## 4. The usable synthesis with D.172

D.172 gives the exact positive return moments

\[
 c_k(N)=y_N^*K_N^ky_N,
 \qquad K_N=Y_0R_0^\dagger Y_0^*.                    \tag{4.1}
\]

Estimate (0.2) implies the dyadic layer bound (0.3), hence

\[
 \sum_{k\ge0}c_k(N)
 =y_N^*(I-K_N)^\dagger y_N<\infty.                  \tag{4.2}
\]

Conversely, (4.2) implies the necessary layer estimate
(\mu_N^y((0,\delta])\le\delta\,(4.2)).  Thus the endpoint theorem
must supply a summable improvement over the bare necessary estimate.

The next admissible step is not another Gamma norm bound.  It is either:

* prove (0.2) for the exact boundary synthesis by retaining the two Tate
  moments and all prime-power translations in the graph equation; or
* prove the equivalent summable return estimate directly from (4.1).

Both formulations retain the complete Gamma place, all (p^k), and the
two A--B--C primitive moments.  Neither assumes the sign being sought.
