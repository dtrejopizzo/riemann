# 106.67 — Cofinal mode heads and the superexponential Euler-tail gate

## Purpose and verdict

Documents 106.62--106.63 show a moving phenomenon: enlarging a finite
zero-mode span can expose a direction missed by the preceding prime head,
and the next literal prime atom raises that direction.  This note turns the
observation into an exact cofinal theorem.

Let \(V_M\) be a finite space of elementary mean-periodic modes associated
with all zero orbits in a bounded frequency rectangle, including nonreal
zeros and multiplicity jets.  Let

\[
 S_X=\{p^k:p^k\leq X\}.
\]

There are four exact conclusions.

1.  The finite-head Gram matrices increase in Loewner order to the complete
    Gram matrix.
2.  On every fixed \(V_M\), the omitted Euler tail is
    double-exponentially small in the displacement \(U=\log X\):

    \[
      0\preceq H_{M,\infty}-H_{M,X}
      \preceq C_Me^{-cX}N_M
      =C_Me^{-ce^U}N_M.
    \]

3.  A literal finite head is nonnegative on \(V_M\) for some finite \(X\)
    if and only if the complete Gram has a strictly positive gap on
    \(V_M\).  If the complete minimum is zero or negative, no finite head
    and no positive moving average of finite heads can repair it.
4.  A cofinal, vanishing-tolerance head theorem is exactly positivity on
    the elementary spectral-synthesis closure.  It becomes equivalent to
    RH only after proving that the elementary zero modes are a form core of
    the full mean-periodic complement.  That form-norm synthesis theorem is
    not currently proved.  Requiring exact nonnegativity of every finite
    head is stronger: it also excludes finite-dimensional threshold null
    vectors.

Thus the moving-head idea gives an effective finite approximation theorem,
but not an independent sign.  An off-line orbit creates a negative full
state; once a finite Galerkin space detects it, every finite head lies even
lower and repair is impossible.

## 1. Finite mode spaces, including nonreal zeros

Use the frequency normalization

\[
 \Xi(z)=\xi\!\left(\frac12+iz\right).
\]

Every nontrivial zero lies in

\[
 |\mathrm{Im}\,z|<\frac12.                    \tag{1}
\]

For \(M>0\), let \(\mathcal Z_M\) be the finite zero multiset

\[
 \mathcal Z_M
 =\{z:\Xi(z)=0,\ |\mathrm{Re}\,z|\leq M\},     \tag{2}
\]

with representatives chosen modulo \(z\mapsto-z\), and with conjugate
orbits retained.  If \(z\) has multiplicity \(m_z\), define

\[
 \chi_{z,k}(x)
 =\partial_z^k\!\left(\frac{\cos(zx)}{h(x)}\right),
 \qquad 0\leq k<m_z,\qquad h(x)=\cosh(x/2).         \tag{3}
\]

Let

\[
 V_M=\mathrm{span}_{\mathbb C}
 \{\chi_{z,k}:z\in\mathcal Z_M,\ 0\leq k<m_z\}.     \tag{4}
\]

The real even space is the conjugation-fixed part of (4).  No reality of
the zeros is assumed.

The functions in (3) are linearly independent after the
\(z\mapsto-z\) duplication is removed.  Since \(d\mu_K>0\), their norm
Gram matrix

\[
 (N_M)_{\alpha\beta}
 =\langle\chi_\alpha,\chi_\beta\rangle_{L^2(\mu_K)}
                                                               \tag{5}
\]

is positive definite.  The zero and jet identities give

\[
 V_M\subset(1\oplus\mathcal R)^\perp.               \tag{6}
\]

For \(X\geq2\), put

\[
 \mathscr E_X
 =\mathscr E_\Gamma+
 \sum_{\substack{n\leq X\\n=p^k}}
 \frac{\Lambda(n)}{\sqrt n}\mathcal J_{\log n},     \tag{7}
\]

and define \(H_{M,X}\) and \(H_{M,\infty}\) by

\[
\begin{aligned}
 a^*H_{M,X}a
 &=\mathscr E_X(q_a)-\frac12\|q_a\|_{\mu_K}^2,\\
 a^*H_{M,\infty}a
 &=\mathscr E_K(q_a)-\frac12\|q_a\|_{\mu_K}^2,
 \qquad q_a=\sum_\alpha a_\alpha\chi_\alpha.        \tag{8}
\end{aligned}
\]

These are the finite and complete kernels of 106.62 restricted to (4).

## 2. Exact Loewner monotonicity

For a prime power \(n\), let \(V_{n,M}\) be the feature map

\[
 (V_{n,M}a)(x)
 =\sqrt{\frac{\Lambda(n)}{\sqrt n}K(x)K(x-\log n)}
   \{q_a(x)-q_a(x-\log n)\}.                        \tag{9}
\]

### Theorem 1 — Cofinal all-atoms flag

If \(2\leq X\leq Y\), then

\[
 \boxed{
 H_{M,Y}-H_{M,X}
 =\sum_{\substack{X<n\leq Y\\n=p^k}}
 V_{n,M}^*V_{n,M}\succeq0.}                        \tag{10}
\]

Moreover,

\[
 \boxed{
 R_{M,X}:=H_{M,\infty}-H_{M,X}
 =\sum_{\substack{n>X\\n=p^k}}
 V_{n,M}^*V_{n,M}\succeq0.}                        \tag{11}
\]

#### Proof

Subtract (8).  The Gamma and polar terms cancel, and every remaining
prime-power increment is precisely the square (9).  Monotone convergence
gives (11).  \(\square\)

In particular,

\[
 H_{M,X}\preceq H_{M,\infty}                       \tag{12}
\]

for every finite head.  Adding atoms approaches the complete form from
below; it never overshoots it.

## 3. A uniform superexponential tail on every fixed mode space

The theta formula implies the following global kernel bound.

### Lemma 2 — Double-exponential overlap

There are constants \(A,a>0\), independent of \(u\), such that

\[
 K(x)\leq A\exp(-ae^{2|x|})                         \tag{13}
\]

and

\[
 Z(u):=\int_{\mathbb R}K(x)K(x-u)\,dx
 \leq A\exp(-ae^u),\qquad u\geq1.                  \tag{14}
\]

#### Proof

For \(x\geq0\), the theta series is a polynomial in \(e^x\) times
\(\sum_{m\geq1}m^4e^{-\pi m^2e^{2x}}\).  Decreasing the exponential
constant absorbs the polynomial and gives (13); evenness handles
\(x<0\).

For \(0\leq x\leq u\),

\[
 e^{2x}+e^{2(u-x)}\geq2e^u,
\]

so the middle part of the convolution is at most
\(A^2u e^{-2ae^u}\).  On \(x<0\), write \(x=-y\); the exponent contains
\(e^{2(u+y)}\), and its integral is
\(O(e^{-a'e^{2u}})\).  The region \(x>u\) is identical after reflection.
Absorbing \(u\) and decreasing \(a\) proves (14).  \(\square\)

Because \(\mathcal Z_M\) is finite, define

\[
 \sigma_M=\max_{z\in\mathcal Z_M}|\mathrm{Im}\,z|<\frac12,
 \qquad
 d_M=\max_{z\in\mathcal Z_M}(m_z-1).                \tag{15}
\]

The elementary bound

\[
 |\chi_{z,k}(x)|
 \leq2(1+|x|)^{d_M}
 e^{-(1/2-\sigma_M)|x|}                             \tag{16}
\]

and positive definiteness of \(N_M\) imply that there is \(B_M<\infty\)
such that

\[
 \boxed{
 \sup_{x\in\mathbb R}|q(x)|
 \leq B_M\|q\|_{L^2(\mu_K)}
 \qquad(q\in V_M).}                                \tag{17}
\]

The constant is effective once the finite zero enclosures and the smallest
eigenvalue of \(N_M\) are enclosed.

### Theorem 3 — Uniform Euler-tail estimate

There are constants \(C_M,c>0\), with \(c\) independent of \(M\), such
that for \(X\) sufficiently large,

\[
 \boxed{
 0\preceq
 N_M^{-1/2}R_{M,X}N_M^{-1/2}
 \preceq C_Me^{-cX}I.}                             \tag{18}
\]

Equivalently, if the head is parametrized by \(U=\log X\), its omitted
tail is \(O_M(e^{-ce^U})\).

#### Proof

For \(q\in V_M\), (17) and (14) give

\[
\begin{aligned}
 \mathcal J_u(q)
 &\leq4\|q\|_\infty^2Z(u)\\
 &\leq4AB_M^2e^{-ae^u}\|q\|_{\mu_K}^2.             \tag{19}
\end{aligned}
\]

At \(u=\log n\), use \(\Lambda(n)\leq\log n\) and enlarge the sum from
prime powers to all integers:

\[
\begin{aligned}
 q^*R_{M,X}q
 &\leq4AB_M^2\|q\|_{\mu_K}^2
 \sum_{n>X}\frac{\log n}{\sqrt n}e^{-an}\\
 &\leq C_Me^{-cX}\|q\|_{\mu_K}^2.                  \tag{20}
\end{aligned}
\]

This is (18).  \(\square\)

No zero-location assertion enters (18).  Nonreal modes are harmless on
each fixed \(V_M\) because the strict strip margin in (15) makes their
quotients by \(h\) bounded.

## 4. The exact finite-repair criterion

Define the complete generalized minimum

\[
 \boxed{
 \delta_M
 =\lambda_{\min}\!\left(
 N_M^{-1/2}H_{M,\infty}N_M^{-1/2}\right)
 =\inf_{\substack{q\in V_M\\\|q\|_{\mu_K}=1}}
 \left\{\mathscr E_K(q)-\frac12\right\}.}           \tag{21}
\]

### Lemma 4 — The omitted tail is positive definite on \(V_M\)

For every finite \(X\) and every nonzero \(q\in V_M\),

\[
 q^*R_{M,X}q>0.                                    \tag{22}
\]

#### Proof

If (22) failed, every nonnegative omitted atom would vanish.  Since
\(K(x)K(x-\log p)>0\), vanishing of the atoms of two distinct omitted
primes \(p,r>X\) would make \(q\) periodic with periods \(\log p\) and
\(\log r\).  Their ratio is irrational: a rational relation would imply
\(p^a=r^b\) for positive integers \(a,b\).  Continuity and two
incommensurable periods make \(q\) constant.  But every vector in \(V_M\)
is centered by (6), so that constant is zero.  \(\square\)

### Theorem 5 — Finite repair if and only if the full gap is strict

For every fixed \(M\), the following are equivalent:

1. there exists a finite \(X\) such that \(H_{M,X}\succeq0\);
2. \(\delta_M>0\).

More quantitatively, if

\[
 C_Me^{-cX}<\delta_M,                               \tag{23}
\]

then

\[
 H_{M,X}\succeq
 (\delta_M-C_Me^{-cX})N_M\succ0.                   \tag{24}
\]

If \(\delta_M=0\), then \(H_{M,X}\) has a negative direction for every
finite \(X\), although its minimum tends to zero.  If \(\delta_M<0\), the
same negative direction cannot be repaired by any head.

#### Proof

If \(\delta_M>0\), combine (18) with

\[
 H_{M,X}=H_{M,\infty}-R_{M,X}
\]

to get (24).  Conversely, suppose \(H_{M,X}\succeq0\).  Lemma 4 says that
\(R_{M,X}\) is positive definite.  Hence

\[
 H_{M,\infty}=H_{M,X}+R_{M,X}\succ0.
\]

Finite dimensionality makes its generalized minimum strictly positive.
This proves the equivalence.

If \(\delta_M\leq0\), take a unit minimizer \(q_M\).  Then

\[
 q_M^*H_{M,X}q_M
 =\delta_M-q_M^*R_{M,X}q_M<0
\]

when \(\delta_M=0\), and is at most \(\delta_M<0\) when
\(\delta_M<0\).  \(\square\)

This theorem explains the moving numerical rows of 106.62.  A minimum
which stays just below zero and rises superexponentially with the head can
be a genuine full threshold zero; no finite head can certify it as
nonnegative.

## 5. Positive moving averages cannot change the obstruction

Let \(X_1,\ldots,X_J<\infty\), let \(\alpha_j\geq0\), and
\(\sum_j\alpha_j=1\).  Define

\[
 \overline H_M=\sum_{j=1}^J\alpha_jH_{M,X_j}.       \tag{25}
\]

Then

\[
 \boxed{
 \overline H_M
 =H_{M,\infty}-\sum_{j=1}^J\alpha_jR_{M,X_j}
 \preceq H_{M,\infty}.}                            \tag{26}
\]

If \(\delta_M<0\), (26) is negative on a full-Gram minimizing vector.  If
\(\delta_M=0\), Lemma 4 makes it strictly negative there.  The same holds
for any probability average of finite heads, including Cesaro, trimmed or
exponentially weighted moving averages: positive averaging changes the
size of the omitted positive tail, not its sign.

Thus averaging over the cutoff is numerically stabilizing but cannot hide
an off-line negative channel or turn a threshold null vector positive.

## 6. What can be said about \(\delta_M\) without locating zeros

The complete Krein factorization of 106.64 restricts to \(V_M\).  In
\(N_M\)-normalized coordinates, write

\[
 A_M=
 \begin{pmatrix}\mathcal B_0\\ \mathcal B_+\end{pmatrix}
 \bigg|_{V_M}N_M^{-1/2},
 \qquad
 C_M^-=\mathcal B_-\big|_{V_M}N_M^{-1/2}.           \tag{27}
\]

Then

\[
 \boxed{
 N_M^{-1/2}H_{M,\infty}N_M^{-1/2}
 =A_M^*A_M-(C_M^-)^*C_M^-}                         \tag{28}
\]

and consequently

\[
 \boxed{
 \delta_M\geq s_{\min}(A_M)^2-\|C_M^-\|^2.}         \tag{29}
\]

Equation (29) is the sharp available lower-frame comparison.  If every
zero is real, \(C_M^-=0\).  Without that conclusion, the off-line
evaluation channel is present and there is no unconditional reason for
the right side of (29) to be positive.  Proving

\[
 s_{\min}(A_M)>\|C_M^-\|                            \tag{30}
\]

cofinally in \(M\) is the finite-dimensional version of the missing
absorption contraction; it is not supplied by the Euler-tail estimate.

For an individual fixed \(M\), \(\delta_M\) can in principle be bounded
by interval arithmetic using zero enclosures, the explicit kernel of
106.62 and a zero-counted high-frequency tail.  A positive bound uniform
over an exhaustive family, without excluding off-line zeros, would prove
the missing sign rather than precede it.

## 7. Where an off-line orbit prevents finite repair

If RH is false, 106.64 produces a mean-periodic form-domain vector
\(F_*\), with \(q_*=F_*/h\), such that

\[
 \mathscr E_K(q_*)-\frac12\|q_*\|_{\mu_K}^2<0.      \tag{31}
\]

Let \(E_J\) be any nested finite-dimensional form-core exhaustion of the
mean-periodic complement.  Form-norm Galerkin approximation gives

\[
 \delta(E_J)<0                                     \tag{32}
\]

for all sufficiently large \(J\).  Theorems 1 and 5 apply verbatim to
each such \(E_J\), so

\[
 H_{E_J,X}\not\succeq0\qquad\text{for every finite }X. \tag{33}
\]

The off-line orbit is therefore not a tail that sufficiently many primes
can repair.  It is a negative direction of the completed form, and every
finite head lies below that completed value.

For the particular elementary spaces \(V_M\), the implication

\[
 \neg\mathrm {RH}\Longrightarrow
 \delta_M<0\quad\text{for some }M                  \tag{34}
\]

requires the form-norm spectral-synthesis statement

\[
 \boxed{
 \overline{\bigcup_MV_M}^{\,\|\cdot\|_{\mathrm{form}}}
 =\{q:hq*K=0\}.}                                   \tag{35}
\]

Document 106.43 identifies the elementary frequencies but does not prove
(35), and 106.62 explicitly leaves it open.  Ordinary compact-open
mean-periodic synthesis is not enough: the prime--Gamma graph norm must
also converge.  Thus (35), not the Euler tail, is the exact boundary
between the canonical zero-mode heads and the off-line negative
eigenstate.

## 8. Exact cofinal formulations

Assume \(V_M\subset V_{M+1}\), after choosing a nested sequence of
frequency rectangles.  Put

\[
 \mathcal V_{\mathrm{syn}}
 =\overline{\bigcup_MV_M}^{\,\|\cdot\|_{\mathrm{form}}}.              \tag{36}
\]

### Theorem 6 — Exact-head and compensated-head criteria

The following statements hold.

1. The exact cofinal assertion

   \[
   \forall M\ \exists X(M)<\infty:
   H_{M,X(M)}\succeq0                              \tag{37}
   \]

   is equivalent to \(\delta_M>0\) for every \(M\).

2. Let \(\varepsilon_M\downarrow0\).  The compensated cofinal assertion

   \[
   \exists X(M)\uparrow\infty:
   H_{M,X(M)}\succeq-\varepsilon_MN_M              \tag{38}
   \]

   is equivalent to nonnegativity of the complete form on
   \(\mathcal V_{\mathrm{syn}}\), provided \(X(M)\) is chosen so that
   \(C_Me^{-cX(M)}\leq\varepsilon_M\).

3. If the form-core identity (35) holds, (38) is equivalent to RH.
   Under the same identity, an off-line orbit makes (38) fail and makes
   every exact head in the detecting finite Galerkin space fail.

#### Proof

Part 1 is Theorem 5.  If the complete form is nonnegative on
\(\mathcal V_{\mathrm{syn}}\), then (18) gives

\[
 H_{M,X(M)}
 \succeq-C_Me^{-cX(M)}N_M
 \succeq-\varepsilon_MN_M,
\]

which proves one direction of Part 2.

Conversely, fix \(q\in V_m\).  For every \(M\geq m\), evaluate (38) on
the same \(q\).  Since \(H_{M,X(M)}\preceq H_{M,\infty}\), one obtains

\[
 q^*H_{\infty}q
 \geq-\varepsilon_M\|q\|_{\mu_K}^2.
\]

Let \(M\to\infty\).  This proves complete nonnegativity on
\(\bigcup_mV_m\), and closure proves it on (36).  Part 3 follows from
the full-kernel Weil equivalence and (35).  \(\square\)

The exact-head criterion (37) may be stronger than RH unless one also
proves that the complete form has no additional threshold null vector in
any \(V_M\).  The compensated criterion (38) avoids that extra strict-gap
requirement.

## 9. Consequence

The moving-head picture is now exact:

\[
 \boxed{
 H_{M,X}\nearrow H_{M,\infty},\qquad
 \|H_{M,\infty}-H_{M,X}\|_{N_M}
 =O_M(e^{-cX}).}                                   \tag{39}
\]

This gives a rigorous finite approximation scheme for every fixed complex
zero-mode space.  It does not generate the sign of the limit.  Positive
averaging over heads remains below the same limit, and an off-line negative
direction remains negative at every finite stage.

The two possible closing theorems are now separated cleanly:

1. prove the compensated inequalities (38) directly from the literal
   prime--Gamma matrices, together with the form-norm synthesis (35); or
2. prove the complete finite-mode gaps \(\delta_M\geq0\) cofinally by a
   signed zero-divisor Gram factorization.

Either statement contains the missing RH-strength sign.  The
superexponential Euler-tail theorem controls approximation error but does
not supply it.
