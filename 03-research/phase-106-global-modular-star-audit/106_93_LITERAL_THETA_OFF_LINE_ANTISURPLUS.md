# 106.93 — Literal theta off-line anti-surplus

## Purpose and conclusion

The rational network falsifier of 106.92 does not use the literal Riemann
translation maps. This note performs the stronger audit inside the actual
ordinary-prime--Gamma system.

If an off-line zero exists, 106.64 produces a negative vector in the Riemann
mean-periodic complement. For that vector, every finite ordinary-prime head
has a negative source pivot, and restoring the complete literal prime tail
does **not** cross the source deficit. More precisely, for every head cutoff
\(X\),

\[
 \boxed{G_X-\delta_X=\mathcal A_\infty(q,q)<0.}                 \tag{1}
\]

Consequently every finite source-balanced bordered minor also has the wrong
sign. This is not a generic graph countermodel: it uses Riemann's kernel
\(K\), the actual translation lengths \(\log p^k\), the ordinary weights
\(\Lambda(p^k)=\log p\), the complete Gamma channel, and the equation
\((hq)*K=0\).

Thus the desired strict surplus cannot be obtained from a formal consequence
of those identities which remains valid in the counterfactual presence of an
off-line zero. Proving the surplus has to exclude that counterfactual; in
this coordinate, that exclusion is exactly the unresolved Riemann sign.

## 1. Literal head and tail forms

Let \(F\) belong to the form domain of the Riemann mean-periodic complement

\[
 \mathcal N_K=\{F:F*K=0\},
 \qquad q=F/h,
 \qquad h(x)=\cosh(x/2).
\]

Write the completed form as

\[
 \mathcal A_\infty(q,q)
 =\mathscr E_\Gamma(q,q)
 +\sum_{n=p^k}\frac{\Lambda(n)}{\sqrt n}
   \mathcal J_{\log n}(q,q)
 -\frac12\|q\|_{\mu_K}^2.                                  \tag{2}
\]

For a finite prime-power head \(n\le X\), put

\[
 \begin{aligned}
 \mathcal A_X(q,q)
 &:=\mathscr E_\Gamma(q,q)
 +\sum_{\substack{n=p^k\\n\le X}}
   \frac{\Lambda(n)}{\sqrt n}\mathcal J_{\log n}(q,q)
 -\frac12\|q\|_{\mu_K}^2,\\
 \mathcal T_X(q,q)
 &:=\sum_{\substack{n=p^k\\n>X}}
   \frac{\Lambda(n)}{\sqrt n}\mathcal J_{\log n}(q,q).
 \end{aligned}                                                \tag{3}
\]

Every summand in \(\mathcal T_X\) is nonnegative, and theta decay makes the
series finite on the common form domain.
The exact decomposition is

\[
 \boxed{\mathcal A_\infty=\mathcal A_X+\mathcal T_X.}          \tag{4}
\]

No prime, Gamma, or polar term has been separated by an estimate in (4).

## 2. The literal off-line anti-surplus theorem

### Theorem 1 — An off-line orbit defeats every literal tail restoration

Assume that \(\Xi\) has an off-line zero orbit. Then there exists a real
even \(F\in\mathcal N_K\) in the common form domain such that, for every
finite \(X\), the following assertions hold.

1. The finite-head scalar pivot is negative:

   \[
    \mathcal A_X(q,q)=-\delta_X<0.                            \tag{5}
   \]

2. With no old mode and no finite radical coordinate, the exact adaptive
   gain is the complete omitted-prime response

   \[
    G_X=\mathcal T_X(q,q).                                    \tag{6}
   \]

3. The source surplus is strictly negative:

   \[
    \boxed{G_X-\delta_X=\mathcal A_\infty(q,q)<0.}             \tag{7}
   \]

4. For every proper finite tail cutoff \(Y>X\),

   \[
    \mathfrak C_X(Y)\le G_X<\delta_X,                         \tag{8}
   \]

   and hence the physical bordered determinant is negative:

   \[
    \boxed{
    \det\!\left(\mathbb C_{X,Y}-\delta_Xe_*e_*^*\right)
    =\mathfrak C_X(Y)-\delta_X<0.}                            \tag{9}
   \]

Here all displacement forms in \(\mathbb C_{X,Y}\) are the literal maps

\[
 q\longmapsto
 \sqrt{K(x)K(x-\log n)}\{q(x)-q(x-\log n)\}
\]

with weights \(\Lambda(n)/\sqrt n\).

#### Proof

By 106.64, Theorem 3, an off-line orbit gives a real even
\(F\in\mathcal N_K\) satisfying

\[
 \mathcal A_\infty(q,q)<0.                                   \tag{10}
\]

For every \(X\), (4) and \(\mathcal T_X(q,q)\ge0\) imply

\[
 \mathcal A_X(q,q)
 =\mathcal A_\infty(q,q)-\mathcal T_X(q,q)
 <0,
\]

which proves (5). In the scalar row there is no old-mode regression and
no radical shorting. Therefore the resolvent in the definition of the
adaptive gain is the identity, giving (6). Combining (4)--(6) gives

\[
 G_X-\delta_X
 =\mathcal T_X(q,q)+\mathcal A_X(q,q)
 =\mathcal A_\infty(q,q),
\]

which is (7).

For a finite \(Y\), nonnegativity of the omitted atoms gives
\(\mathfrak C_X(Y)\le G_X\). Equation (7) gives \(G_X<\delta_X\), proving
(8). With no nuisance coordinate the deleted principal determinant is
\(1\), so the bordered Schur identity of 106.92 reduces exactly to (9).
\(\square\)

## 3. The fully compensated minor inequality also fails

The source identity for (5) is

\[
 \delta_X
 =\frac12\|q\|_{\mu_K}^2-\mathscr E_\Gamma(q,q)
 -\sum_{\substack{n=p^k\\n\le X}}
   \frac{\Lambda(n)}{\sqrt n}\mathcal J_{\log n}(q,q).       \tag{11}
\]

Substitution in (8) gives, for every finite \(Y>X\),

\[
\boxed{
\begin{aligned}
 \mathfrak C_X(Y)+\mathscr E_\Gamma(q,q)
 &+\sum_{\substack{n=p^k\\n\le X}}
   \frac{\Lambda(n)}{\sqrt n}\mathcal J_{\log n}(q,q)\\
 &<\frac12\|q\|_{\mu_K}^2.
\end{aligned}}                                                 \tag{12}
\]

Thus the exact physical inequality proposed in 106.92 does not merely lack
a proof under the off-line counterfactual. It is false there, with the
actual Gamma term, the actual head primes, and the actual omitted-tail
determinant kept together.

## 4. Consequence for admissible proof mechanisms

Theorem 1 separates two logically different statements.

* The positive facts

  \[
  \Lambda(p^k)>0,\qquad K>0,\qquad
  \mathcal J_{\log p^k}(q,q)\ge0,
  \qquad (hq)*K=0
  \]

  hold for the vector constructed under the off-line counterfactual.

* The strict source-balanced domination does not:

  \[
  G_X>\delta_X.
  \]

Therefore positivity of the literal atoms, theta localization, finite
observability, mean periodicity, and ordinary von Mangoldt weights cannot
be arranged into a proof by an implication which is insensitive to the
location of the mean-periodic frequencies. The missing step must use those
same physical data in a way that rules out the off-line frequency itself.

Equivalently, the no-loss identity

\[
 \boxed{G_X-\delta_X=\mathcal A_\infty(q,q)}                   \tag{13}
\]

shows that the desired surplus is not a preliminary estimate from which
completed positivity follows. It is completed positivity evaluated on the
stationary residual. Any proposed proof should therefore be audited at the
first line where (13) is assigned a positive sign: that line is the new
Riemann-strength input.

## 5. Ledger status

The attack on \(G_J>\delta_J\) using the literal theta maps yields an exact
conditional falsifier, not the desired unconditional sign:

\[
 \neg\mathrm{RH}
 \Longrightarrow
 \exists q\in\mathcal N_K\ \forall X\ \forall Y>X:
 \mathfrak C_X(Y)\le G_X<\delta_X.
\]

This strengthens the generic falsifier of 106.92 by placing the obstruction
inside the actual Riemann ordinary-prime--Gamma system. It does not decide
which side the ordinary zeta function occupies. The surviving theorem is
still the exclusion of the off-line mean-periodic frequency, equivalently
the strict source-balanced surplus on an exhaustive physical form core.
