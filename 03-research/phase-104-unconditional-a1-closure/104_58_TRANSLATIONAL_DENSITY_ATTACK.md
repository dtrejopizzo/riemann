# 104_58 — Translational attack and density criterion for the quartic margin

**Status.** This document exploits the relaxed target of `104_56A`,

\[
 D_n:=4\lambda_n-A_n>0.                              \tag{1}
\]

A useful result is obtained, but not a closure of (1): if RH is false,
then \(D_n<0\) on a set of integers of positive lower density. Hence it
suffices to prove (1) outside a set of density zero. The same obstruction
survives every translational window of fixed length.

A different question is also answered negatively: the phase bound
\(|\mathcal B_{n,a}|\le3n\) of `104_41`, valid for \(a\ge4\), cannot be
transported to \(a=1\), not even "in density" or after averaging over
fixed windows, without controlling the cross residues. A rational
quadruple proves this exactly.

None of the following proves that the real \(D_n\) are positive in
density one. Hence this document proves neither A1 nor RH.

## 1. No duplication with `104_17`

`104_17` studies the partial sums
\(\sum_{n\le N}Q_n\), their triangular means and radial Abel positivity.
Here different objects are studied:

1. **translated** windows \(\sum_{h<L}D_{N+h}\);
2. the natural density of the set of bad signs;
3. the finite set of dominant singularities if RH fails;
4. the exact change of a window when moving the homotopy \(a\ge4\to1\).

No attempt is made to recover a coefficient from Abel positivity, which is
already ruled out by `104_17`.

## 2. Exact generating function of the blocks

Let

\[
 s(z)={1\over1-z},\qquad
 G(s)=s\pi^{-s/2}\Gamma(s/2),\qquad
 Y_4(s)={\xi(s)^4\over G(s)}.
\]

Li's local identity gives

\[
 \mathcal H(z):=\log{Y_4(s(z))\over Y_4(1)}
 =\sum_{n\ge1}{D_n\over n}z^n.                    \tag{2}
\]

Hence the ordinary generating function is

\[
 \boxed{
 \mathcal D(z):=z\mathcal H'(z)=\sum_{n\ge1}D_nz^n.} \tag{3}
\]

For \(L\ge1\), define the window ending at \(N\)

\[
 S_{N,L}:=\sum_{h=0}^{L-1}D_{N-h},
 \qquad D_j:=0\quad(j\le0).
\]

Then

\[
 \boxed{
 \sum_{N\ge1}S_{N,L}z^N
 ={1-z^L\over1-z}\,\mathcal D(z).}                \tag{4}
\]

Equivalently, for the window starting at \(N\),

\[
 U_{N,L}:=\sum_{h=0}^{L-1}D_{N+h}
 =[z^{N+L-1}],{1-z^L\over1-z}\mathcal D(z).       \tag{5}
\]

Thus averaging over a fixed length only multiplies each singularity
by the polynomial

\[
 A_L(w):=1+w+\cdots+w^{L-1}={1-w^L\over1-w}.       \tag{6}
\]

If \(|w|>1\), then \(A_L(w)\ne0\). Consequently no fixed window
cancels an off-line exterior mode.

## 3. Density lemma for a trigonometric polynomial

**Lemma 3.1.** Let \(0<\theta_j<\pi\) be distinct up to sign, and
\(c_j>0\). Set

\[
 P_n=\sum_{j=1}^Jc_j\cos(n\theta_j),\qquad
 M=\sum_jc_j,\qquad
 \sigma^2={1\over2}\sum_jc_j^2.                  \tag{7}
\]

Then, with \(\varepsilon=\sigma^2/(4M)\),

\[
 \boxed{
 \underline{\mathrm{dens}}
 \{n:P_n>\varepsilon\}\ge {\sigma^2\over4M^2}>0.} \tag{8}
\]

**Proof.** The elementary Cesàro identities

\[
 {1\over N}\sum_{n\le N}e^{in\alpha}\longrightarrow0
 \qquad(\alpha\notin2\pi\mathbb Z)
\]

give

\[
 {1\over N}\sum_{n\le N}P_n\to0,\qquad
 {1\over N}\sum_{n\le N}P_n^2\to\sigma^2.        \tag{9}
\]

Frequencies representing the same cosine were grouped beforehand, so no
constant cross terms remain. Since
\(|P_n|\le M\), we have \(P_n^2\le M|P_n|\). Writing
\(P_n=P_n^+-P_n^-\), (9) implies

\[
 \liminf_{N\to\infty}{1\over N}\sum_{n\le N}P_n^+
 \ge {\sigma^2\over2M}.                           \tag{10}
\]

Finally,

\[
 P_n^+\le\varepsilon+M\mathbf1_{\{P_n>\varepsilon\}}.
\]

Averaging and using (10) gives (8). \(\square\)

The same proof holds for a nonzero real polynomial
\(\mathrm{Re}\,\sum_jd_je^{in\theta_j}\), after grouping
frequencies. Only the positive constant changes.

## 4. Dominant theorem: a violation of RH produces positive bad density

**Theorem 4.1.** If RH is false, there exist \(r>1\), \(1<r_1<r\), a
nonzero real trigonometric polynomial \(P_n\), and a constant \(C\), such
that

\[
 \boxed{
 D_n=-8r^nP_n+O(r_1^n).}                           \tag{11}
\]

In particular,

\[
 \boxed{
 \underline{\mathrm{dens}}\{n:D_n<0\}>0.} \tag{12}
\]

**Proof.** The zeros to the right of the critical line are transformed
into

\[
 z_\rho=1-{1\over\rho},\qquad |z_\rho|<1.          \tag{13}
\]

If any exist, the number

\[
 q:=\min_{\Re\rho>1/2}|z_\rho|<1                  \tag{14}
\]

is attained and the set \(\mathcal Z_0\) of zeros attaining the minimum
is finite: every compact disk of the \(z\)-variable contains only
finitely many zeros, and \(|z_\rho|\to1\) as \(|\Im\rho|\to\infty\).

Choose \(q<q_1<1\) with no other transformed singularities in
\(|z|\le q_1\). Removing from \(Y_4(s(z))\) the factors of the zeros of
\(\mathcal Z_0\) leaves a function holomorphic and nonzero on that disk,
with a holomorphic logarithm. From (2), the logarithmic singularity of a
zero of multiplicity \(m_\rho\) gives

\[
 D_n=-4\sum_{\rho\in\mathcal Z_0}m_\rho z_\rho^{-n}
     +O(r_1^n),                                    \tag{15}
\]

for some \(1<r_1<q^{-1}\); the polynomial factor of a Cauchy bound is
absorbed by enlarging \(r_1\). Grouping conjugates and writing
\(z_\rho=q e^{i\theta_\rho}\),

\[
 D_n=-8q^{-n}\sum_{\substack{\rho\in\mathcal Z_0\\Im\rho>0}}
 m_\rho\cos(n\theta_\rho)+O(r_1^n).               \tag{16}
\]

No frequency \(0\) or \(\pi\) appears, since the nontrivial zeros are
not real. After grouping equal cosines, Lemma 3.1 gives a set of
positive lower density where the polynomial of (16) exceeds a positive
constant. On that set the main term dominates the error for
all sufficiently large \(n\), and \(D_n<0\). \(\square\)

**Corollary 4.2 (density-one criterion).** If

\[
 D_n>0
 \quad\hbox{for all }n\notin\mathcal E,\qquad
 \mathrm{dens}(\mathcal E)=0,               \tag{17}
\]

then RH is true.

This proof does not yield a universal constant \(\delta_0>0\) such
that \(\overline{\mathrm{dens}}(\mathcal E)<\delta_0\) suffices. The
bound of (8) depends on the number and multiplicities of the dominant
zeros; without a uniform bound on that data it can be arbitrarily small.
The robust relaxation is "zero-density exceptions."

## 5. Fixed windows also fail to hide the dominant residues

**Theorem 5.1.** Under the negation of RH, for each fixed length \(L\ge1\),

\[
 \boxed{
 \underline{\mathrm{dens}}
 \left\{N:\sum_{h=0}^{L-1}D_{N+h}<0\right\}>0.}    \tag{18}
\]

**Proof.** Sum (16) over \(n=N,\ldots,N+L-1\). If
\(w_j=q^{-1}e^{-i\theta_j}\), the dominant term becomes

\[
 -8q^{-N}\mathrm{Re}
 \sum_jm_j e^{-iN\theta_j}A_L(w_j).                \tag{19}
\]

Each \(A_L(w_j)\ne0\) because \(|w_j|>1\). After grouping frequencies,
(19) is a nonzero real trigonometric polynomial. Its positive part exceeds
a constant on a set of positive lower density by the proof of Lemma 3.1.
The error is still \(O(r_1^N)\), since \(L\) is fixed, and remains
dominated by \(q^{-N}\). \(\square\)

Hence a theorem proving positivity for a single fixed window length
outside a set of density zero would also prove RH. But the window does not
reduce the residue: it only rotates and rescales its phase.

## 6. Rational falsifier for every fixed window

Take the quadruple from `104_17`

\[
 \rho={1+2i\over5},\qquad w=1-{1\over\rho}=2i.
\]

Its contribution to the Li coefficient is

\[
 Q_n=4-2\mathrm{Re}(w^n+w^{-n}),            \tag{20}
\]

and to margin (1) it is \(D_n^{\mathcal O}=4Q_n\). Hence

\[
 \boxed{
 \sum_{h=0}^{L-1}D_{N+h}^{\mathcal O}
 =16L-8\mathrm{Re}\,\left\{
 w^NA_L(w)+w^{-N}A_L(w^{-1})\right\}.}             \tag{21}
\]

Write \(A_L(2i)=a_L+ib_L\). It is a nonzero Gaussian integer, because
\((2i)^L\ne1\). One of the four quantities
\(\mathrm{Re}(i^jA_L(2i))\) is strictly positive. On the corresponding
class \(N\equiv j\pmod4\), the dominant term of (21) is

\[
 -8\,2^N\mathrm{Re}(i^jA_L(2i)),
\]

while the reciprocal term tends to zero. So (21) is negative for
all sufficiently large \(N\) in that class, which has density
exactly \(1/4\). This holds for **every** fixed \(L\).

## 7. The phase bound does not transport in density

Let \(F(s)=(s-1)\zeta(s)\) and formally multiply by
\(Q_\rho(s)^M\), where \(Q_\rho\) is the polynomial of the previous
quadruple. For

\[
 z_{\eta,a}:=1-{a\over\eta},
\]

the coefficient formula (8) of `104_41` gives the exact change

\[
 \boxed{
 \Delta\mathcal B_{n,a}
 =M\sum_{\eta\in\mathcal O(\rho)}
       \left(z_{\eta,a}^{-n}-1\right).}            \tag{22}
\]

For \(a\ge4\), the identity

\[
 |z_{\eta,a}|^2-1={a(a-2\Re\eta)\over|\eta|^2}>0  \tag{23}
\]

shows that (22) is bounded in \(n\) and tends to \(-4M\). At the
endpoint \(a=1\), reciprocal symmetry gives

\[
 \Delta\mathcal B_{n,1}=-M Q_n,\qquad
 \Delta D_n=4M Q_n.                               \tag{24}
\]

For \(n\equiv0\pmod4\), \(n\ge4\),

\[
 Q_n=4-2(2^n+2^{-n})<0,                            \tag{25}
\]

so the change in \(D_n\) is exponentially negative on a
set of density \(1/4\), even though for \(a\ge4\) the change of (22) is
only bounded. Fixed windows retain the same obstruction by (21).

For \(M=1\), the quadruple factor alone satisfies even the same
numerical output bound as (19) of `104_41` at all target degrees. At
\(a=4\), the four squared moduli of \(z_{\eta,4}\) are
\(73,73,13,13\); by (23) they only increase as \(a\) grows. Hence, for
\(a\ge4\) and \(n\ge2\),

\[
 |\Delta\mathcal B_{n,a}|
 \le4+2\,73^{-n/2}+2\,13^{-n/2}
 \le4+{2\over73}+{2\over13}<6\le3n.               \tag{25a}
\]

So not even preserving the exact scalar inequality
\(|\mathcal B_{n,a}|\le3n\) at the Euler endpoint distinguishes the
falsifier at the target degrees \(n\ge150\).

Moreover \(Q_\rho(1/2+it)>0\), so the critical phase remains identical,
as `104_41` proves. Hence:

\[
 \boxed{
 \text{phase in the Euler half-plane + fixed translational averages}
 \not\Longrightarrow
 \text{density control at }a=1}               \tag{26}
\]

without a separate estimate of the cross residues.

This falsifier does not have the exact Euler weights \(\Lambda(m)\). That is
why (26) rules out mechanisms based only on phase, homotopy and averaging; it
does not rule out a new inequality specific to the real zeta weights.

## 8. Balance

**Proved:**

- exact generating function (3)--(5) of translational windows;
- density-one criterion, Corollary 4.2;
- persistence of the obstruction at every fixed length, Theorem 5.1;
- rational falsifier of density \(1/4\);
- impossibility of transporting \(|\mathcal B_{n,a}|\le3n\) in density or
  in fixed windows without controlling residues.

**Not proved:**

- that \(D_n>0\) for a density-one set of real zeta indices;
- a residue bound using the exact weights \(\Lambda(m)\);
- A1 or RH.

The logical advance is real: the quantifier "all \(n\ge150\)" can
be replaced by "all \(n\) except a density-zero set." The remaining
obstacle is not recovering each coefficient from an average, but
proving an average bound that excludes a **positive density** of
failures.

## 9. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 translational_density_attack_check.py
```

The checker uses only rationals and Gaussian rationals. It verifies
(20)--(25) and the window identities on a finite family of values;
the density claim for every \(L\) is proved algebraically above, not by
sampling.
