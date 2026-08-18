# Strong margin: the maximal collective Gram decomposition and its defect

## Result

Put

\[
 D_n=2\lambda_n-A_n,
 \qquad A_n=\lambda_n^{\rm arch}.
 \tag{1}
\]

This note tests a direct alternative to the false first-difference route.
It does not assume, or try to prove, that \(\Delta D_n\) has one sign.  The
functional symmetries of the zero divisor give an exact collective Hilbert
square for the angular part of \(2\lambda_n\).  Off the critical line there
is, however, one additional radial term:

\[
 \boxed{
 D_n=\|V_n\|^2-A_n-R_n,
 \qquad
 R_n=8\sum_Q\{\cosh(na_Q)-1\}\cos(n\theta_Q).
 }
 \tag{2}
\]

Here \(Q\) runs over the noncritical reciprocal quartets and
\(w_Q=1-1/\rho_Q=e^{-a_Q+i\theta_Q}\), with \(a_Q>0\).  Formula (2) is
unconditional and all its series converge absolutely for each fixed
\(n\).  It is the desired collective Gram decomposition as far as the
functional equation alone permits.  Its defect \(R_n\) has both signs and
cannot be absorbed by the fixed archimedean term: for
\(\theta_Q=\pi/2\) and \(4\mid n\), the Gram component of that quartet
vanishes while its radial defect is strictly positive.

There is a second exact obstruction.  Any Hilbert-space factorization of
the completed Fejer form which preserves its polarized Toeplitz form would
imply full Loewner positivity.  That positivity is false.  In fact, the
boundary argument of `103_25` needs no RH assumption: reality of
\(\xi(1/2+it)\) is unconditional.  Thus an operator domination of the
negative part by the positive part is impossible for the actual completed
symbol.  Restricting the domination only to the Dirichlet prefixes gives
exactly (1), so it is a valid RH-strength target but not a derived lemma.

Consequently (2) is a non-circular alternative formulation, not a proof of
the missing sign.  It identifies the irreducible task: control the signed
radial defect using special arithmetic information about the actual zeta
divisor (equivalently the collectively coupled von Mangoldt cells of
`103_61`).  No assertion of A1 or RH is made here.

## 1. An unconditional angular Gram square

For a nontrivial zero \(\rho\), counted with multiplicity, write

\[
 w_\rho=1-{1\over\rho}.
 \tag{3}
\]

Conjugation and the functional equation act by

\[
 w_{\bar\rho}=\overline {w_\rho},\qquad
 w_{1-\rho}=w_\rho^{-1},\qquad
 w_{1-\bar\rho}=\overline {w_\rho}^{-1}.
 \tag{4}
\]

For every noncritical quartet choose its member with
\(\Re\rho>1/2\).  Then \(|w_\rho|<1\), so there are unique
\(a_Q>0\) and \(\theta_Q\in(-\pi,\pi]\) such that

\[
 w_\rho=e^{-a_Q+i\theta_Q}.
 \tag{5}
\]

For a critical-line conjugate pair write instead
\(w_\rho=e^{i\theta_C}\).  The exact Li divisor identity, grouped before
summing, gives the following contributions to \(2\lambda_n\):

\[
 \begin{split}
 \text{critical pair }C:&\quad
 4\{1-\cos(n\theta_C)\}
   =2|1-e^{in\theta_C}|^2,\\
 \text{noncritical quartet }Q:&\quad
 8-8\cosh(na_Q)\cos(n\theta_Q).
 \end{split}
 \tag{6}
\]

The second line splits identically as

\[
 8-8\cos(n\theta_Q)
 -8\{\cosh(na_Q)-1\}\cos(n\theta_Q)
 =4|1-e^{in\theta_Q}|^2-R_{Q,n}.                 \tag{7}
\]

To make the first terms in (6)--(7) one candid Gram square, take the
Hilbert direct sum with one complex coordinate for every critical pair and
every noncritical quartet.  Define increments \(v_j\), \(j\ge0\), by

\[
 \begin{split}
 (v_j)_C&=\sqrt2\,(1-e^{i\theta_C})e^{ij\theta_C},\\
 (v_j)_Q&=2(1-e^{i\theta_Q})e^{ij\theta_Q}.
 \end{split}                                                     \tag{8}
\]

Then

\[
 V_n:=\sum_{j=0}^{n-1}v_j,qquad
 (V_n)_C=\sqrt2(1-e^{in\theta_C}),\qquad
 (V_n)_Q=2(1-e^{in\theta_Q}).                                   \tag{9}
\]

These vectors belong to the direct sum.  Indeed,
\(|1-w_\rho|=1/|\rho|\), while (5) and
\(|w_\rho|^2=1-(2\Re\rho-1)/|\rho|^2\) give, outside a finite set,

\[
 |1-e^{i\theta_Q}|
 \le |1-w_\rho|+|1-e^{-a_Q}|\ll |\rho|^{-1}.                   \tag{10}
\]

The standard symmetric zero count implies
\(\sum_\rho|\rho|^{-2}<\infty\), so (8) is square summable.  It also
gives \(a_Q=O(|\rho|^{-2})\); hence, for fixed \(n\),
\(\cosh(na_Q)-1=O_n(|\rho|^{-4})\).  Thus both the Gram sum and the
radial sum in (2) converge absolutely.  Summing (6)--(7) proves

\[
 2\lambda_n=\|V_n\|^2-R_n,                                     \tag{11}
\]

and subtraction of \(A_n\) proves (2).  No zero-location hypothesis has
entered this derivation.

## 2. Exact quartet obstruction to controlling the defect

The radial term in (2) is not a remainder with a favorable sign.  Fix
\(0<r<1\), put

\[
 w=ir,qquad \rho={1\over1-ir},
 \tag{12}
\]

and include \(\rho,\bar\rho,1-\rho,1-\bar\rho\).  All four points lie in
the critical strip, obey both symmetries, and have
\(a=-\log r>0\), \(\theta=\pi/2\).  If \(4\mid n\), then

\[
 4|1-e^{in\theta}|^2=0,qquad
 R_{Q,n}=8\{\cosh(na)-1\}>0.                                   \tag{13}
\]

Accordingly the quartet contribution to \(2\lambda_n\) is exactly

\[
 -8\{\cosh(na)-1\}<0.                                          \tag{14}
\]

Repeating the quartet with multiplicity \(M\) multiplies (14) by \(M\)
without changing the functional symmetries.  Equivalently, one may take
the finite real polynomial having precisely those four zeros, and then its
\(M\)-th power.  Thus no inequality of the form

\[
 R_n\le \|V_n\|^2-A_n                                           \tag{15}
\]

can follow from the Gram square, the strip, the functional equation,
conjugation, or a fixed archimedean allowance.  At (13) the proposed
positive side contributed by that quartet is zero, whereas its adverse
defect is arbitrarily large with multiplicity.

The opposite sign occurs just as exactly whenever
\(\cos(n\theta_Q)<0\).  Therefore replacing \(R_n\) by \(|R_n|\) loses
the only possible collective cancellation.  This is the zero-side image
of the alternating Laguerre-lobe matrix in `103_61`, not an independent
error that can be bounded absolutely.

There is no circular use of (15) here.  For the actual zeta divisor,
(2) shows that (15) is *identically equivalent* to \(D_n\ge0\).  It is a
precise possible theorem to prove from arithmetic, but it cannot be cited
as an auxiliary consequence of generic divisor symmetry.

## 3. The polarized Hilbert alternative collapses to false Loewner

Let \(g_m^{\rm SM}\) be the completed second-difference coefficients of
`103_26`, and on analytic polynomials define the Hermitian Toeplitz form

\[
 \mathcal B(p,q)=
 \sum_{j,k}p_j\overline{q_k}\,g_{j-k}^{\rm SM},
 \qquad g_{-m}^{\rm SM}=\overline{g_m^{\rm SM}}.                \tag{16}
\]

For the Dirichlet prefix

\[
 P_n(z)=1+z+\cdots+z^{n-1},                                    \tag{17}
\]

twice summation by parts gives the exact scalar identity

\[
 \mathcal B(P_n,P_n)=D_n.                                      \tag{18}
\]

Suppose that a collective Hilbert construction preserved not only the
diagonal numbers (18), but their natural polarization: there were a linear
map \(U\) from polynomials to a Hilbert space such that

\[
 \mathcal B(p,q)=\langle Up,Uq\rangle.                          \tag{19}
\]

Then \(\mathcal B(p,p)\ge0\) for every polynomial.  This is precisely
positivity of every Toeplitz section, hence full Loewner positivity of the
strong-margin symbol.  It is enough to assume (19) only on the span of the
prefixes: since

\[
 1=P_1,qquad z^{n}=P_{n+1}-P_n,                                \tag{20}
\]

those prefixes span all polynomials.

This implication explains why a Cauchy--Schwarz estimate between different
Fejer prefixes cannot be imported for free.  Such an estimate requires the
positive polarized form (19), not merely the desired diagonal signs (18).
If one assigns unrelated vectors of length \(\sqrt{D_n}\) only after
assuming \(D_n\ge0\), the result is tautological and supplies no
polarization.

## 4. The Loewner obstruction is unconditional

The boundary computation in `103_25` can be strengthened slightly.  The
RH qualifier in its equation for the completed xi symbol is unnecessary.
The functional equation and reality imply, for every real \(t\),

\[
 \xi(1/2+it)=\xi(1/2-it)=\overline{\xi(1/2+it)}\in\mathbb R.    \tag{21}
\]

At a point which is not a zero, differentiating
\(\Xi(t)=\xi(1/2+it)\) gives

\[
 {\Xi'(t)\over\Xi(t)}
 =i{\xi'\over\xi}(1/2+it)\in\mathbb R,
 \qquad
 \Re{\xi'\over\xi}(1/2+it)=0.                                \tag{22}
\]

This uses only the functional equation, not the location of any zero.
The explicit Binet estimate already proved in `103_25` says

\[
 \Re\mathfrak C_{\rm arch}(1/2+it)>0\qquad(|t|\ge30).          \tag{23}
\]

The exact completed relation
\(\mathfrak C_{\rm SM}=\mathfrak C_1-\frac12
\mathfrak C_{\rm arch}\), together with
\(\mathfrak C_1=2\xi'/\xi\), therefore yields, at every nonzero boundary
point in this range,

\[
 \Re\mathfrak C_{\rm SM}<0.                                   \tag{24}
\]

Zeros are discrete, so such points exist.  Local meromorphic continuation
and the conformal map \(z=1-1/s\) transfer the strict sign to nearby
interior points.  The one-point Loewner kernel is consequently negative
there.  If an off-line zero already places a pole inside the disk, global
Caratheodory analyticity fails even earlier; it does not rescue positivity.

Thus (19), and any operator inequality that dominates the entire negative
part of the completed symbol by a positive Gram part, is false
unconditionally.  A decomposition
\(\mathcal B=\mathcal G-\mathcal H\) with
\(\mathcal G,\mathcal H\succeq0\) does not help:

* operator domination \(\mathcal H\preceq\mathcal G\) would make
  \(\mathcal B\succeq0\), contradicting (24);
* domination only on \(P_n\),
  \(\mathcal H(P_n,P_n)\le\mathcal G(P_n,P_n)\), is exactly
  \(D_n\ge0\) by (18).

This is the precise circularity boundary for an ``archimedean negative
part controlled by a collective Gram square.''

## 5. Surviving arithmetic theorem

The analysis leaves one exact direct target which does not mention first
differences:

\[
 \boxed{
 R_n+A_n\le\|V_n\|^2\qquad(n\ge150).
 }
 \tag{25}
\]

Together with the rigorous finite certificate through \(149\), (25) would
prove the strong margin and hence A1 and RH.  Equation (25) is not being
assumed: by (2), it is exactly the missing theorem.

The quartet example proves that (25) cannot be obtained from a local zero
square or from functional symmetries.  The unconditional Loewner
obstruction proves that it cannot be strengthened to operator domination.
Any proof must instead use special collective arithmetic of the actual
von Mangoldt weights.  Under the quantile transport of `103_61`, that same
information is the signed cancellation between different prime towers and
consecutive Laguerre lobes.  Establishing it remains open in this phase.
