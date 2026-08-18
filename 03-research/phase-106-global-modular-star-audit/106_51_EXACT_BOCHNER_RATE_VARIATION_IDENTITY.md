# 106.51 — Exact Bochner identity with rate variation

## Purpose

The triangle formula of 106.50 still hides which part of the double current
is a genuine square and which part is caused by the nonconstant theta
weights. This note computes that split exactly for the complete reversible
generator.

The calculation is important for the proposed \(j_2\) closure. It shows
that the raw integrated curvature contains:

1. a nonnegative commuting-translation square;
2. a signed variation of the Doob rates; and
3. the threshold subtraction.

The coefficient \(j_2\) is not the coefficient of the first square alone.
It can occur only after the signed rate-variation term is transformed by
the theta--Möbius identities.

## 1. A commuting-move Bochner formula

Let \(\mathcal S\) be a finite symmetric set of commuting moves. For each
\(s\in\mathcal S\), write \(sx=x+s\) and let \(c_s(x)\ge0\). Use the
standard Markov-sign generator

\[
 (\mathcal Af)(x)=\sum_s c_s(x)\{f(sx)-f(x)\}.        \tag{1}
\]

For a Hilbert-valued function \(F\), put

\[
\begin{aligned}
 a_s(x)&=F(sx)-F(x),\\
 b_{s,t}(x)&=F(stx)-F(sx)-F(tx)+F(x).                \tag{2}
\end{aligned}
\]

The carré du champ is

\[
 \Gamma(F)(x)=\frac12\sum_s c_s(x)\|a_s(x)\|^2.      \tag{3}
\]

### Theorem 1 — Rate-variation Bochner identity

For commuting moves,

\[
\boxed{
\begin{aligned}
 \Gamma_2(F)(x)
={}&\frac14\sum_{s,t}c_s(x)c_t(x)\|b_{s,t}(x)\|^2\\
 &+\frac14\sum_{s,t}c_s(x)
 \{c_t(sx)-c_t(x)\}\\
 &\quad\times\left(
 \|a_t(sx)-a_s(x)\|^2-\|a_s(x)\|^2
 \right).
\end{aligned}}                                       \tag{4}
\]

#### Proof

By definition,

\[
 \Gamma_2(F)=\frac12\{\mathcal A\Gamma(F)
 -2\Gamma(F,\mathcal AF)\}.                          \tag{5}
\]

Commutativity gives

\[
 a_t(sx)=a_t(x)+b_{s,t}(x).                          \tag{6}
\]

Expanding the first term of (5) gives

\[
\frac14\sum_{s,t}c_s(x)
\left[c_t(sx)\|a_t+b_{s,t}\|^2
-c_t(x)\|a_t\|^2\right].                             \tag{7}
\]

The second term is

\[
-\frac12\sum_{s,t}c_s(x)
\operatorname {Re}\left\langle
a_s,\{c_t(sx)-c_t(x)\}a_t+c_t(sx)b_{s,t}
\right\rangle .                                      \tag{8}
\]

Replace \(c_t(sx)\) in the terms not containing a rate difference by
\(c_t(x)\). The mixed expression

\[
 \sum_{s,t}c_s(x)c_t(x)
 \operatorname {Re}\langle a_t-a_s,b_{s,t}\rangle
\]

vanishes after interchanging \(s\) and \(t\), because \(b_{s,t}=b_{t,s}\).
The remaining constant-rate term is the first line of (4). The
rate-difference terms combine as

\[
\begin{aligned}
 &\|b_{s,t}\|^2
 +2\operatorname {Re}\langle a_t-a_s,b_{s,t}\rangle
 +\|a_t\|^2-2\operatorname {Re}\langle a_s,a_t\rangle\\
 &\qquad
 =\|a_t+b_{s,t}-a_s\|^2-\|a_s\|^2,
\end{aligned}
\]

which is the second part of (4). \(\square\)

For translation-invariant rates the second part vanishes, leaving the
usual nonnegative square of the mixed second differences.

## 2. Application to the ordinary-prime--Gamma generator

Use the symmetric displacement space

\[
 s=\sigma u,\qquad u>0,\quad\sigma=\pm1,             \tag{9}
\]

with the common base measure \(d\nu_\zeta(u)\) from 106.49. The rate
density of the standard generator \(\mathcal A=-L\) is

\[
 \boxed{
 c_s(x)=\frac{c_KK(x+s)}{h(x)}.}                     \tag{10}
\]

The detailed-balance identity is

\[
 d\mu_K(x)c_s(x)
 =K(x)K(x+s)\,dx
 =d\mu_K(x+s)c_{-s}(x+s).                            \tag{11}
\]

Formula (4), first with the common cutoff and then by graph-norm closure,
therefore applies to the feature \(\mathbf Q\) of every finite spectral
cluster.

Since \(\mathcal A=-L\), the integrated sign is unchanged at second order:

\[
 \int\Gamma_2(\mathbf Q)\,d\mu_K
 =\sum_j\|Lq_j\|^2=\operatorname {Tr}(PL^2),          \tag{12}
\]

while

\[
 \int\Gamma(\mathbf Q)\,d\mu_K
 =\operatorname {Tr}(PL).                            \tag{13}
\]

Consequently

\[
\boxed{
 \mathfrak T(P)
 =\int\left\{\Gamma_2(\mathbf Q)
 -\frac12\Gamma(\mathbf Q)\right\}d\mu_K,}           \tag{14}
\]

with \(\Gamma_2\) given explicitly by (4), (10).

## 3. The exact signed rate term

For the actual rates,

\[
\boxed{
\begin{aligned}
 c_t(x+s)-c_t(x)
 =c_K\left\{
 \frac{K(x+s+t)}{h(x+s)}
 -\frac{K(x+t)}{h(x)}
 \right\}.                                           \tag{15}
\end{aligned}}
\]

Thus the complete curvature trace is

\[
\begin{aligned}
 \mathfrak T(P)
={}&\frac14\int\sum_{s,t}c_s(x)c_t(x)
 \|b_{s,t}(x)\|^2\,d\mu_K(x)\\
&+\frac14\int\sum_{s,t}c_s(x)
\left\{\frac{c_KK(x+s+t)}{h(x+s)}
-\frac{c_KK(x+t)}{h(x)}\right\}\\
&\qquad\times
\{\|a_t(x+s)-a_s(x)\|^2-\|a_s(x)\|^2\}
\,d\mu_K(x)\\
&-\frac14\int\sum_s c_s(x)\|a_s(x)\|^2\,d\mu_K(x).
                                                               \tag{16}
\end{aligned}
\]

Every prime power and the Gamma continuum occur in both sums. No cross
term has been discarded.

## 4. Coefficient audit for \(j_2\)

In the first line of (16), two opposite prime moves have total displacement
\(\log(mn)\) and hence group with coefficient
\((\Lambda*\Lambda)(mn)\). The remaining two ingredients of (16) are not
Dirichlet-convolution squares:

* equal prime orientations give ratio displacements;
* (15) is a theta/Doob rate variation;
* the last line is the single-jump threshold subtraction;
* prime--Gamma and Gamma--Gamma pairs remain continuous.

Therefore the statement

\[
 \text{“the coefficient of (16) is }j_2\ge0\text{”}
\]

is false before a further identity is supplied. The missing operation is
precisely the spatial realization of the logarithmic derivation
\(\delta\Lambda\). It must convert the signed rate term (15), together
with the mixed continuous pairs and the threshold line, into
\(\delta\Lambda\) plus terms which cancel the ratio channel or have a
controlled sign.

The theta--Möbius identities 106.40(7)--(9) do produce
\(\delta\Lambda+\Lambda*\Lambda\) on the primitive cyclic theta vector.
What has not yet been proved is their lift from that one cyclic vector to
the reducing projection feature \(\mathbf Q\).

## 5. The exact bridge now required

Define \(\mathfrak R_{\rm var}(P)\) to be the last two lines of (16), plus
all ratio and continuous mixed pieces of its first line. Define
\(\mathfrak J_2(P)\) to be the product-channel contribution obtained after
grouping by \(mn\) and adding the desired \(\delta\Lambda\) spatial term.

The required bridge is an identity of the form

\[
\boxed{
 \mathfrak R_{\rm var}(P)
 =\mathfrak J_2(P)+\mathfrak C(P),}                  \tag{17}
\]

where \(\mathfrak C(P)\) must be a sum of full spatial currents or an
\(L\)-commutator whose trace on \(P\) vanishes. If (17) is established with
\(\mathfrak J_2(P)\ge0\) and \(\mathfrak C(P)\ge0\) (or zero after trace),
then (16) proves \(\mathfrak T(P)\ge0\).

Equation (16) prevents a false closure: coefficient positivity of \(j_2\)
alone does not imply (17). The next calculation must construct the
logarithmic spatial derivation on the full theta-index lift and evaluate
its compression against a reducing projection.
