# 106.103 — Clean heat Rayleigh flow and the shifted-moment gate

## 1. Purpose

The relative observable of 106_100 detects the bottom of the physical
operator by comparing \(S\) with \(S+V\). The comparison is not needed for
the detection itself. A single trace-class heat matrix element already has
the exact exponent, an exact monotone Rayleigh flow, and a literal
ordinary-prime--Gamma source expansion.

This note proves that statement and then audits the two strongest scalar
successors:

1. shifted odd heat moments; and
2. operator-monotone changes of spectral variable.

Both audits are decisive. Every unshifted heat moment and every unshifted
Hankel moment matrix is automatically positive, even in the presence of a
subthreshold state. Conversely, eventual positivity of **any one** odd
moment shifted to the physical threshold is already equivalent to the
physical surplus. The same is true after every strictly increasing
operator-monotone change of variable. Thus these transforms neither prove
nor weaken the missing sign.

Throughout, let

\[
 \mathscr C=(\mathbf 1\oplus\mathcal R)^\perp,
 \qquad A=L|_{\mathscr C}\geq0,
 \qquad S=A+\frac12I.
 \tag{1}
\]

The physical surplus is

\[
 \boxed{A\geq\frac12I,}
 \tag{2}
\]

or, equivalently, \(S\geq I\).

## 2. One faithful trace-class heat state

Choose an orthonormal basis \((u_j)_{j\geq1}\) of \(\mathscr C\) inside the
proved heat core and put

\[
 V=\sum_{j\geq1}2^{-j}|u_j\rangle\langle u_j|.
 \tag{3}
\]

Then \(V>0\) in the strict quadratic-form sense, \(\ker V=\{0\}\), and
\(\operatorname {Tr}V=1\). Define, for \(t>0\),

\[
 \boxed{Z_V(t)=\operatorname {Tr}(Ve^{-tS}).}
 \tag{4}
\]

Unlike an absolute heat trace, (4) is finite without compact resolvent:

\[
 Z_V(t)
 =\|e^{-tS/2}V^{1/2}\|_{\mathfrak S_2}^2
 \leq e^{-t/2}\|V\|_1.
 \tag{5}
\]

Let \(E_S\) be the spectral resolution of \(S\), and define the finite
positive measure

\[
 d\nu_V(\lambda)
 =\operatorname {Tr}\!\left(
 V^{1/2}E_S(d\lambda)V^{1/2}\right).
 \tag{6}
\]

Then

\[
 Z_V(t)=\int_{[1/2,\infty)}e^{-t\lambda}\,d\nu_V(\lambda).
 \tag{7}
\]

### Lemma 1 — The heat state sees the complete spectrum

\[
 \boxed{\operatorname {supp}\nu_V=\sigma(S).}
 \tag{8}
\]

#### Proof

If an open set \(O\) meets \(\sigma(S)\), then \(E_S(O)\ne0\). If
\(\nu_V(O)=0\), then

\[
 0=\operatorname {Tr}(V^{1/2}E_S(O)V^{1/2})
  =\|E_S(O)V^{1/2}\|_{\mathfrak S_2}^2.
\]

Hence \(E_S(O)V^{1/2}=0\). Since \(V^{1/2}\) has dense range, this would
give \(E_S(O)=0\), a contradiction. The reverse inclusion in (8) follows
directly from the definition of the spectral measure. \(\square\)

## 3. Exact monotone source-rate flow

For every integer \(k\geq0\), spectral calculus and trace cyclicity give

\[
 \boxed{
 (-1)^kZ_V^{(k)}(t)
 =\operatorname {Tr}(VS^ke^{-tS})
 =\int\lambda^ke^{-t\lambda}\,d\nu_V(\lambda)\geq0.}
 \tag{9}
\]

All operators \(S^ke^{-tS}\) are bounded for \(t>0\), so no domain
interchange is hidden in (9).

Put

\[
 \Gamma_t=e^{-tS/2}Ve^{-tS/2},
 \qquad
 \mathcal E_V(t)=\operatorname {Tr}(A\Gamma_t),
 \tag{10}
\]

where the second trace is understood in the positive form sense. Then

\[
 \boxed{
 R_V(t):=\frac{\mathcal E_V(t)}{Z_V(t)}
 =-\partial_t\log Z_V(t)-\frac12.}
 \tag{11}
\]

The density

\[
 d\mathbb P_t(\lambda)
 =Z_V(t)^{-1}e^{-t\lambda}\,d\nu_V(\lambda)
 \tag{12}
\]

is a probability measure. Differentiating (11) therefore proves the exact
variance law

\[
 \boxed{
 R_V'(t)=-\operatorname {Var}_{\mathbb P_t}(\lambda)\leq0.}
 \tag{13}
\]

Let

\[
 \alpha=\inf\sigma(A),
 \qquad \lambda_*=\inf\sigma(S)=\alpha+\frac12.
 \tag{14}
\]

The elementary Laplace concentration lemma gives

\[
 \boxed{\lim_{t\to\infty}R_V(t)=\alpha.}
 \tag{15}
\]

Indeed, for every \(\varepsilon>0\), Lemma 1 gives positive
\(\nu_V\)-mass in \([\lambda_*,\lambda_*+\varepsilon]\), while the mass in
\([\lambda_*+2\varepsilon,\infty)\) is exponentially smaller after tilting
by \(e^{-t\lambda}\). Truncating the remaining first moment and then
letting the truncation grow proves convergence of the tilted mean to
\(\lambda_*\).

Most importantly, (10) retains the literal source. Tonelli's theorem for
positive closed forms gives

\[
\boxed{
 \begin{aligned}
 \mathcal E_V(t)={}&
 \int_0^\infty
 \frac{e^{-u/2}}{1-e^{-2u}}
 \mathcal J_u[\Gamma_t]\,du\\
 &+\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \mathcal J_{\log n}[\Gamma_t].
 \end{aligned}}
 \tag{16}
\]

There is no \(sV\) boost in (16), and hence no \(O(t^{-1})\) boost error.
Equations (11), (15), and (16) yield the boost-free physical criterion

\[
 \boxed{
 A\geq\frac12I
 \quad\Longleftrightarrow\quad
 \lim_{t\to\infty}
 \frac{
 \displaystyle
 \mathscr E_\Gamma[\Gamma_t]
 +\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \mathcal J_{\log n}[\Gamma_t]}
 {\operatorname {Tr}\Gamma_t}
 \geq\frac12.}
 \tag{17}
\]

Formula (17) is exact, but it is not a proof of its right-hand side.

## 4. The shifted odd-moment theorem

Shift the heat transform to the target threshold:

\[
 Y_V(t)=e^tZ_V(t)
 =\int e^{-t(\lambda-1)}\,d\nu_V(\lambda).
 \tag{18}
\]

For every integer \(m\geq0\),

\[
 \boxed{
 (-1)^mY_V^{(m)}(t)
 =\int(\lambda-1)^m e^{-t(\lambda-1)}
 \,d\nu_V(\lambda).}
 \tag{19}
\]

### Theorem 2 — One odd shifted moment already has full strength

For every fixed odd integer \(m\geq1\), the following are equivalent:

1. \(A\geq\frac12I\);
2. \((-1)^mY_V^{(m)}(t)\geq0\) for every \(t>0\);
3. \((-1)^mY_V^{(m)}(t)\geq0\) for all sufficiently large \(t\).

For every even \(m\), the quantity in (19) is nonnegative
unconditionally and contains no threshold information.

#### Proof

If \(A\geq1/2\), then \(\operatorname {supp}\nu_V\subset[1,\infty)\),
and (19) proves both positivity statements.

Conversely, suppose \(\lambda_*<1\). Divide (19) by \(Y_V(t)>0\). The
same Laplace concentration argument used for (15), now applied to the
continuous function \((\lambda-1)^m\) after a harmless high-energy
truncation, gives

\[
 \frac{(-1)^mY_V^{(m)}(t)}{Y_V(t)}
 \longrightarrow(\lambda_*-1)^m<0
 \qquad(t\to\infty).
 \tag{20}
\]

Thus eventual positivity fails. Lemma 1 converts
\(\lambda_*\geq1\) back to \(S\geq I\), which is (2). When \(m\) is
even, the integrand in (19) is pointwise nonnegative on the whole real
line. \(\square\)

In particular, complete monotonicity of \(Y_V\) is not an accumulation of
weaker facts: its first shifted derivative is already the missing physical
surplus in the heat state, and every fixed odd derivative has exactly the
same asymptotic force.

## 5. Raw Hankel positivity versus the shifted localizer

For every \(d\geq0\), the raw heat Hankel matrix is

\[
 H_d^{(0)}(t)
 =\left[(-1)^{i+j}Z_V^{(i+j)}(t)\right]_{i,j=0}^d
 =\int v_d(\lambda)v_d(\lambda)^*
 e^{-t\lambda}\,d\nu_V(\lambda)\succeq0,
 \tag{21}
\]

where \(v_d(\lambda)=(1,\lambda,\ldots,\lambda^d)^T\). This is automatic
Stieltjes positivity for support in \([0,\infty)\).

The threshold localizing matrix is instead

\[
 \boxed{
 H_d^{(1)}(t)
 =\int(\lambda-1)v_d(\lambda)v_d(\lambda)^*
 e^{-t\lambda}\,d\nu_V(\lambda).}
 \tag{22}
\]

Its first entry is

\[
 H_0^{(1)}(t)
 =-Z_V'(t)-Z_V(t)
 =Z_V(t)\left(R_V(t)-\frac12\right).
 \tag{23}
\]

Thus the all-order positivity of (21), including every principal minor,
does not imply even the first scalar localizer (23). If a subthreshold
state exists, (20) with \(m=1\) makes (23) strictly negative for all large
\(t\), while every matrix (21) remains positive semidefinite.

This is the heat-moment version of the ordered-transfer obstruction in
106_99: generalized-von-Mangoldt positivity can populate the raw moment
cone, but support at the shifted physical threshold requires a new signed
localizer.

## 6. Operator-monotone transforms do not weaken the threshold

Let \(\phi:(0,\infty)\to\mathbb R\) be a nonconstant operator-monotone
function. The Löwner representation

\[
 \phi(x)=a+bx+\int_{(0,\infty)}
              \frac{x}{x+s}\,d\rho(s),
 \qquad b\geq0,
 \tag{24a}
\]

with the usual integrability condition on the positive measure \(\rho\),
shows that a nonconstant \(\phi\) is strictly increasing: either \(b>0\)
or
\(\phi'(x)=b+\int s(x+s)^{-2}\,d\rho(s)>0\).
The same representation gives at most affine growth. Define

\[
 \mathcal R_{\phi,V}(t)
 =\frac{
 \operatorname {Tr}\!\left(
 V\{\phi(S)-\phi(1)I\}e^{-tS}\right)}
 {Z_V(t)}.
 \tag{24}
\]

The trace is finite for \(t>0\). Spectral calculus gives

\[
 \mathcal R_{\phi,V}(t)
 =\int\{\phi(\lambda)-\phi(1)\}\,d\mathbb P_t(\lambda).
 \tag{25}
\]

### Theorem 3 — Operator-monotone transform wall

For every nonconstant operator-monotone \(\phi\),

\[
 \boxed{
 A\geq\frac12I
 \quad\Longleftrightarrow\quad
 \mathcal R_{\phi,V}(t)\geq0
 \text{ for all sufficiently large }t.}
 \tag{26}
\]

#### Proof

If \(S\geq I\), operator monotonicity gives
\(\phi(S)-\phi(1)I\geq0\), hence (24) is nonnegative.
Conversely, Laplace concentration and the at-most-affine growth of
\(\phi\) give

\[
 \lim_{t\to\infty}\mathcal R_{\phi,V}(t)
 =\phi(\lambda_*)-\phi(1).
 \tag{27}
\]

Strict monotonicity makes the right side negative exactly when
\(\lambda_*<1\). Apply Lemma 1. \(\square\)

Therefore fractional powers, logarithms, negative resolvents, and
complete-Bernstein
changes of the heat generator do not create an intermediate estimate. A
sign after any such strictly increasing transform is another exact detector
of the same spectral floor.

## 7. Consequence for the physical-surplus attack

The single-state flow improves 106_100 in two technical respects:

* it removes the perturbation average \(S+sV\); and
* it removes the accompanying \(O(t^{-1})\) boost contribution.

It also makes the remaining sign maximally explicit:

\[
 \boxed{
 R_V(t)=
 \frac{
 \mathscr E_\Gamma[\Gamma_t]
 +\sum_{n\ge2}\Lambda(n)n^{-1/2}
       \mathcal J_{\log n}[\Gamma_t]}
 {\operatorname {Tr}\Gamma_t}
 \downarrow\inf\sigma(A).}
 \tag{28}
\]

The unresolved estimate is precisely

\[
 \boxed{\lim_{t\to\infty}R_V(t)\geq\frac12.}
 \tag{29}
\]

Raw heat complete monotonicity, raw Hankel positivity, odd shifted moments,
and operator-monotone transforms do not prove (29): the first two are valid
below threshold, while either of the latter two already has the full force
of (29).

Accordingly, a successful successor must establish a signed lower estimate
for the literal source numerator in (28). It cannot arise solely from
scalar heat-transform positivity or from a monotone change of spectral
coordinate.

## 8. Status

Proved here:

* the boost-free trace-class heat observable (4);
* full spectral faithfulness (8);
* the exact monotone source-rate flow (11)--(16);
* the odd shifted-moment equivalence (Theorem 2);
* the separation between raw Hankel positivity and the threshold localizer;
* the operator-monotone transform wall (Theorem 3).

Not proved here:

\[
 \inf\sigma(A)\geq\frac12,
\]

or equivalently (29). No statement in this note is used as a substitute
for that physical surplus.
