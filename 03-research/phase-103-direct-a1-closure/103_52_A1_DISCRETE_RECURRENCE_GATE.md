# A1 discrete-recurrence gate: exact binomial calculus and the remaining sign

## Scope and verdict

This note tests a route which is genuinely discrete in the Li index.  Its
object is the strong-margin sequence

\[
 D_n:=2\lambda_n-A_n,\qquad A_n:=\lambda_n^{\rm arch}.
\tag{1}
\]

It does **not** prove \(D_n\geq0\).  It gives exact formulae for every
forward difference of \(D_n\), isolates a completely monotone
archimedean component, and identifies the sole signed arithmetic term as a
binomial transform of \(\log(t\zeta(1+t))\).  Thus a putative induction
has a precise target instead of an unspecified ``recurrence error''.

The conclusion is negative but useful: the elementary index recurrences do
not generate a one-sided forcing term.  Any uniform lower barrier strong
enough to propagate (1) is a new global inequality for that binomial
transform.  Together with the finite Li checks and \(A_n>0\) for \(n\geq8\),
such a barrier is RH-strength.  It must not be presented as a consequence of
Euler-factor signs, real-ray positivity, or functional symmetry alone.

This is independent of the theta--PF3 route.  No numerical value is used as
proof anywhere in this note.

## 1. The exact binomial coordinate

Put

\[
 f(t):=\log\bigl(t\zeta(1+t)\bigr)=\sum_{k\geq1}p_k t^k
 \quad (|t|\text{ small}),\qquad t={z\over1-z}.
\tag{2}
\]

The apparent singularity at \(t=0\) is removable and the constant term is
zero.  If

\[
 t\zeta(1+t)=1+\sum_{k\geq1}q_k t^k,
 \qquad q_k={(-1)^{k-1}\gamma_{k-1}\over(k-1)!},
\tag{3}
\]

then coefficient comparison in \(f'= (t\zeta(1+t))'/(t\zeta(1+t))\)
gives the entirely algebraic recursion already used by the finite verifier,

\[
 p_r=q_r-{1\over r}\sum_{k=1}^{r-1}k p_kq_{r-k}.
\tag{4}
\]

The completed factorization of \(\xi\), with the pole factor included in
\(t\zeta(1+t)\), gives the germ identity

\[
 \log B_D(z)=\log H_{\rm arch}(z)+2f\!\left({z\over1-z}\right),
 \qquad
 B_D(z)=\exp\!\left(\sum_{n\geq1}{D_n\over n}z^n\right).
\tag{5}
\]

Here \(H_{\rm arch}\) is exactly the one in `103_31`, Section 3.  Hence,
without an Euler rearrangement at the singular base point,

\[
 \boxed{\quad D_n=A_n+2P_n,\qquad
 P_n:=n[z^n]f\!\left({z\over1-z}\right)
      =n\sum_{k=1}^n {n-1\choose k-1}p_k.\quad}
\tag{6}
\]

Thus \(P_n=\lambda_n^{\rm prime}\), but (6) is also a usable discrete
definition: it is a finite binomial transform of the Taylor data of a
regular analytic germ.  It agrees with the exact formula in
`103_32`, equation (3).  In particular, no unregularised prime-power sum
has been introduced.

Binomial inversion is equally exact:

\[
 \boxed{\quad
 p_n=\sum_{k=1}^n(-1)^{n-k}{n-1\choose k-1}{P_k\over k}
 ={1\over2}\sum_{k=1}^n(-1)^{n-k}{n-1\choose k-1}{D_k-A_k\over k}.
 \quad}
\tag{7}
\]

So an all-index sign theorem for \(D\) is not a local statement about one
Stieltjes constant: it constrains every order of the logarithm in (2).

## 2. All forward differences, exactly

Write \(\Delta u_n=u_{n+1}-u_n\).  Since

\[
 n{n-1\choose k-1}=k{n\choose k},
 \qquad
 \Delta^r {n\choose k}={n\choose k-r},
\tag{8}
\]

the finite sum in (6) gives, for every \(r\geq0\),

\[
\boxed{\quad
 \Delta^rP_n=\sum_{k=\max\{1,r\}}^{n+r} k{n\choose k-r}p_k.
\quad}
\tag{9}
\]

As usual, a binomial coefficient outside \(0\le k-r\le n\) is zero.  The
first two cases are worth displaying:

\[
 \Delta P_n=\sum_{k=1}^{n+1}k{n\choose k-1}p_k,
 \qquad
 \Delta^2P_n=\sum_{k=2}^{n+2}k{n\choose k-2}p_k.
\tag{10}
\]

There is a short generating-function check which prevents an index shift
from being hidden in (10).  With \(F(z)=f(z/(1-z))\),

\[
 \sum_{n\geq1}(P_{n+1}-P_n)z^n
 ={f'(z/(1-z))\over1-z}-p_1.
\tag{11}
\]

Expanding its right side gives the first formula in (10).

For comparison, the regularised Euler identity of `103_14` gives, at
\(a>1\),

\[
 \Delta\lambda_n^{\rm prime}(a)
 =-a\sum_{m\ge2}{\Lambda(m)\over m^a}
       L_n^{(0)}(a\log m),
\tag{12}
\]

and

\[
\Delta^2\lambda_n^{\rm prime}(a)
={a^2\over n+1}\sum_{m\ge2}{\Lambda(m)\log m\over m^a}
       L_n^{(1)}(a\log m).
\tag{13}
\]

Both identities are absolutely convergent before the limit \(a\downarrow1\).
They follow respectively from
\(L_n^{(1)}-L_{n-1}^{(1)}=L_n^{(0)}\) and
\((n+1)L_{n+1}^{(-1)}(x)=-xL_n^{(1)}(x)\).  The kernel in either line
changes sign.  Thus the regularisation makes the calculation legitimate,
but does not produce a signed forcing term.

## 3. The archimedean part is completely explicit

Let

\[
 c={\gamma+\log(4\pi)\over2},\qquad a_\ell=1-{1\over\ell}.
\tag{14}
\]

The odd-index formula from `262` is

\[
 A_n=1-cn+\sum_{\substack{\ell\ge1\\\ell\ \rm odd}}
 \left(a_\ell^n-1+{n\over\ell}\right).
\tag{15}
\]

Although the three displayed summands in (15) should not be summed
separately, its forward differences are absolutely convergent.  Direct
subtraction yields

\[
 \boxed{\quad
 \Delta A_n=-c+\sum_{\ell\ \rm odd}{1\over\ell}
                  \bigl(1-a_\ell^n\bigr),\quad}
\tag{16}
\]

and, for every \(r\ge2\),

\[
 \boxed{\quad
 \Delta^r A_n=(-1)^r
 \sum_{\ell\ \rm odd}{a_\ell^n\over\ell^r}.
 \quad}
\tag{17}
\]

The convergence in (16) follows from
\(1-(1-1/\ell)^n\le n/\ell\); that in (17) is immediate.  In
particular,

\[
 \Delta^2A_n=\sum_{\ell\ \rm odd}{a_\ell^n\over\ell^2}>0,
 \qquad
 \Delta^3A_n=-\sum_{\ell\ \rm odd}{a_\ell^n\over\ell^3}<0.
\tag{18}
\]

This is a genuine positive Hausdorff-moment sequence at order two: the
measure is \(\sum_{\ell\ \rm odd}\ell^{-2}\delta_{a_\ell}\) on
\([0,1)\).  All lack of sign in \(D\) is therefore visible explicitly in
the binomial transform in (9).  Combining (9) and (17), the requested
difference formula is

\[
 \boxed{\quad
 \Delta^rD_n=
 (-1)^r\sum_{\ell\ \rm odd}{a_\ell^n\over\ell^r}
 +2\sum_{k=r}^{n+r}k{n\choose k-r}p_k,
 \qquad r\ge2,\quad}
\tag{19}
\]

with \(\Delta D_n=\Delta A_n+2\Delta P_n\) from (10) and (16).
This is the exact discrete reduction sought here.

## 4. Recurrence and the only possible barrier

The second difference gives the identity

\[
 D_n=nD_1+\sum_{m=1}^{n-1}(n-m)\Delta^2D_m\qquad(n\ge1),
\tag{20}
\]

where the sum is empty at \(n=1\).  Equivalently, with the strong-margin
Toeplitz coefficients of `103_26`,

\[
 g_m^{\rm SM}={1\over2}\Delta^2D_m\quad(m\ge1),
 \qquad D_n=nD_1+2\sum_{m=1}^{n-1}(n-m)g_m^{\rm SM}.
\tag{21}
\]

This recovers the Fejer identity, but now (19) states exactly what its
discrete forcing is.  For example, the tempting convexity barrier is

\[
 \Delta^2D_m\ge0\quad(m\ge1),\qquad D_1\ge0,
\tag{22}
\]

which would indeed imply \(D_n\ge0\) by (20).  Substitution of (19)
shows that (22) is precisely the family

\[
 2\sum_{k=2}^{m+2}k{m\choose k-2}p_k
 \ \ge\ -\sum_{\ell\ \rm odd}{a_\ell^m\over\ell^2}.
\tag{23}
\]

There is no positivity left to extract from the archimedean side: it occurs
with the *opposite* sign in this sufficient barrier.  Nor does (23) reduce
to signs of individual \(p_k\), because its weights are positive but the
coefficients of \(\log(t\zeta(1+t))\) have no established one-sided sign.

The weaker first-difference induction is just as explicit:

\[
 \Delta D_n\ge0
 \ \Longleftrightarrow\ 
 2\sum_{k=1}^{n+1}k{n\choose k-1}p_k
 \ge c-\sum_{\ell\ \rm odd}{1-a_\ell^n\over\ell}.
\tag{24}
\]

If joined to one initial lower bound, (24) would propagate the target.  It
is not a consequence of (16): it is an all-order signed inequality for the
same completed arithmetic data.  Equations (23)--(24) are therefore valid
*barrier specifications*, not proofs of a barrier.

> **Correction (certificate `103_55`).**  The convexity specification (22),
> equivalently (23), is not merely unproved: it is false for the actual
> zeta sequence.  The exact finite strong-margin enclosure at
> \(n=147,148,149\) certifies \(\Delta^2D_{147}<0\).  Thus (23) is retained
> only as an exact identity exposing its failed sign, and must not be used
> as an open target.  The first-difference barrier (24), which permits this
> negative curvature, survives this particular test but is not proved.

## 5. Audits of the natural sign ansatzes

### 5.1 Euler-factor or Laguerre signs fail exactly

At a legitimate regulator \(a>1\), (12) uses \(L_n^{(0)}\), which has
\(n\) positive simple zeros.  For instance

\[
 L_1^{(0)}(x)=1-x,
\tag{25}
\]

so already the summands in \(\Delta\lambda_1^{\rm prime}(a)\) have both
signs as \(m\) varies.  Formula (13) has the same defect.  This is the
first-difference version of the exact counterexample in `103_14`, where the
\(n=1\) un-differenced local contribution is strictly negative.  Hence
neither \(\Lambda(m)\ge0\) nor the Euler rigidity of prime powers proves
(23) or (24).

### 5.2 Positivity on the real ray has no binomial-sign consequence

The logical failure can be demonstrated without a zeta approximation.  Let

\[
 f_*(t)=t-t^2,\qquad H_*(t)=e^{f_*(t)}.
\tag{26}
\]

Then \(H_*(t)>1\) and \(f_*(t)>0\) for \(0<t<1\), exactly the kind of
real-ray positivity one might try to transfer through (6).  Its coefficients
are \(p_1=1,p_2=-1,p_k=0\ (k\ge3)\), so (6) gives

\[
 P_3=3\left({2\choose0}p_1+{2\choose1}p_2\right)=-3.
\tag{27}
\]

Thus positivity of the underlying real function, even when it is the
exponential of an analytic logarithm, does not control the binomial
transform.  This does not model all special properties of zeta; it exactly
rules out an argument using only that real-ray premise.  The more structural
Stieltjes upgrade is impossible for the actual Li generator because its
nonreal zero images give nonreal poles; see `103_21`.

### 5.3 Functional symmetry plus archimedean convexity also fails

Take the exact quartet from `103_28`,

\[
 \rho={1+2i\over5},\qquad b=1-{1\over\rho}=2i,
\tag{28}
\]

and its real functional-equation-symmetric polynomial

\[
 P(s)=(s-\rho)(s-(1-\rho))(s-\bar\rho)(s-(1-\bar\rho)).
\tag{29}
\]

Multiplying any symmetric completed toy factor by \(P(s)/P(1)\) changes
the Li coefficient by the exact quartet amount

\[
 L_{4j}(\rho)=4-2(2^{4j}+2^{-4j})<0.
\tag{30}
\]

If the archimedean sequence (15) is retained externally, its strong-margin
sequence changes by \(2L_n(\rho)\).  Since \(A_{4j}>0\) for \(4j\ge8\),
the isolated toy factor has

\[
 2L_{4j}(\rho)-A_{4j}<0\qquad(j\ge2).
\tag{31}
\]

This is an exact counterexample to every proposed recurrence proof that
uses only reflection, conjugation, and the positive moment identity (18).
It does not say that the actual zeta has such a quartet; it says precisely
that those formal inputs cannot exclude it.  The actual Euler--Gamma
cancellation would have to supply the missing information.

## 6. RH-strength audit

For \(n\ge8\), the phase has already established \(A_n>0\).  Therefore

\[
 D_n\ge0\quad\Longrightarrow\quad
 \lambda_n={D_n+A_n\over2}>0\qquad(n\ge8).
\tag{32}
\]

An eventual version of (32), supplemented by the finite Li certificates,
would give Li positivity and hence RH.  In particular, either of the
uniform barriers (22) or (24), with its required finite base data, is
RH-strength because it implies (32).  This is not a circular derivation;
it is a scope test for the missing inequality.

Conversely, the identity (19) does not establish that a uniform sign of
\(\Delta D\), \(\Delta^2D\), or a higher difference is equivalent to RH.
Those are stronger proposed sufficient conditions and may fail even if RH
is true.  What is rigorous is only:

* the original all-index strong margin implies RH after the finite base;
* every displayed difference barrier that propagates that margin also
  implies RH after the same base;
* pointwise symbol positivity, a fixed positive Stieltjes representation,
  and coefficientwise Euler positivity are unavailable (`103_26`,
  `103_21`, and `103_25`).

## Status

The discrete route has been reduced to explicit binomial inequalities.  The
second-difference/convexity candidate (23) is eliminated by the rigorous
counterexample in `103_55`; higher-order fixed-sign variants cannot restore
that false premise.  The archimedean difference calculus remains exact, and
the surviving simple induction target is the first-difference inequality
(24), or a cumulative-curvature budget which allows negative second
differences.  No non-circular such barrier has been proved.  Consequently
A1 and RH remain open.
