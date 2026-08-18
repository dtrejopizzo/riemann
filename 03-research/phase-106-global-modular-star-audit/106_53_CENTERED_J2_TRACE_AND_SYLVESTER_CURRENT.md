# 106.53 — Centered \(j_2\) trace and the Sylvester current

## Purpose

The projected Riccati formula 106.52 leaves two objects which must not be
estimated independently:

\[
 2\operatorname {Tr}\widetilde P(B+B^*),\qquad
 4\|[X,P_\mu]P_\mu\|_{\rm HS}^2.                    \tag{1}
\]

This note calculates both. Coefficient positivity of \(j_2\) has the
opposite sign after the scalar part of the translation is centered, while
the position leakage is the exact Sylvester response to the marked full
prime--Gamma current.

## 1. Centering the \(j_2\) connection

Use the unitary map \(\mathcal U:L^2(\mu_K)\to L^2(dx)\) of 106.52.
For a full-generator cluster \(P_\mu\), write
\(\widetilde P=\mathcal UP_\mu\mathcal U^{-1}\). Since \(\mathcal U\)
commutes with \(X\),

\[
 \|[X,\widetilde P]\widetilde P\|_{\rm HS}
 =\|[X,P_\mu]P_\mu\|_{\rm HS}.                       \tag{1a}
\]

At a finite Euler cutoff write

\[
 B_N=\sum_{2\le n\le N}b_nS_{\log n},\qquad
 b_n=\frac{j_2(n)}{\sqrt n}\ge0,\qquad
 \kappa_N^{(2)}=\sum_{2\le n\le N}b_n.               \tag{2}
\]

Define the nonnegative symmetric translation generator

\[
 G_N^{(2)}
 =\sum_{2\le n\le N}b_n
 \left(I-\frac{S_{\log n}+S_{-\log n}}2\right).      \tag{3}
\]

Then, as an operator identity on \(L^2(\mathbb R,dx)\),

\[
\boxed{
 B_N+B_N^*=2\kappa_N^{(2)}I-2G_N^{(2)}.}             \tag{4}
\]

### Theorem 1 — Exact centered cluster trace

For every finite-rank orthogonal projection \(P\) in \(L^2(dx)\), with orthonormal basis
\(q_1,\ldots,q_m\),

\[
\boxed{
\begin{aligned}
 2\operatorname {Tr}\{P(B_N+B_N^*)\}
 ={}&4m\kappa_N^{(2)}
      -4\operatorname {Tr}(PG_N^{(2)})\\
 ={}&4m\kappa_N^{(2)}
 -2\sum_{n\le N}b_n\sum_{k=1}^m
   \|q_k-S_{\log n}q_k\|_2^2.
\end{aligned}}                                       \tag{5}
\]

#### Proof

Equation (4) gives the first line. For a unitary shift,

\[
 \|q-S_aq\|_2^2
 =2\|q\|_2^2-2\operatorname {Re}\langle q,S_aq\rangle.
                                                               \tag{6}
\]

Summing (6) over the orthonormal basis and then over \(n\) proves the
second line. \(\square\)

The conclusion is decisive for signs. The inequality \(j_2(n)\ge0\) makes
\(G_N^{(2)}\ge0\), but the centered \(j_2\) contribution in (5) is
*negative*. The diverging scalar \(4m\kappa_N^{(2)}\) must be cancelled or
renormalized jointly with Gamma, the pole, and the threshold term. It is
invalid to discard the scalar and then cite \(j_2\ge0\) as positivity.

## 2. The full marked current

Let \(L\) be the full generator 106.41(7), and use the symmetric oriented
displacement measure

\[
 d\nu_\zeta(s)
 =g(|s|)\,ds
 +\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
   \{\delta_{\log n}+\delta_{-\log n}\}(ds).          \tag{7}
\]

Thus the restriction to either open half-line is the positive measure
106.31(6). No factor \(1/2\) is inserted: integration over the two
orientations must reproduce both terms in 106.41(7).

Then

\[
 (Lf)(x)=\int c_s(x)\{f(x)-f(x+s)\}\,d\nu_\zeta(s),
 \qquad c_s(x)=\frac{c_KK(x+s)}{h(x)}.                \tag{8}
\]

### Lemma 2 — Position commutator

On the common core,

\[
\boxed{
 ([L,X]f)(x)
 =-\int s\,c_s(x)f(x+s)\,d\nu_\zeta(s).}             \tag{9}
\]

#### Proof

The multiplication factors \(c_s(x)\) commute with \(X\). For each
oriented move,

\[
\begin{aligned}
 &(L_sXf)(x)-x(L_sf)(x)\\
 &\quad=c_s(x)\{xf(x)-(x+s)f(x+s)
              -xf(x)+xf(x+s)\}\\
 &\quad=-s\,c_s(x)f(x+s).
\end{aligned}
\]

Integration gives (9). \(\square\)

Thus the current driving the position leakage retains, in one expression,
all signed prime logarithms and the Gamma continuum.

## 3. Exact Sylvester equation for a reducing cluster

Let \(P_\mu\) be a finite Riesz projection of \(L\) in \(L^2(\mu_K)\),
let \(Q_\mu=I-P_\mu\), and set

\[
 L_P=P_\mu LP_\mu,\quad L_Q=Q_\mu LQ_\mu,\quad
 Y=Q_\mu XP_\mu.                                    \tag{10}
\]

Since \(P_\mu\) reduces \(L\),

\[
\boxed{
 L_QY-YL_P=Q_\mu[L,X]P_\mu.}                        \tag{11}
\]

#### Proof

\[
\begin{aligned}
 Q_\mu[L,X]P_\mu
 &=Q_\mu LXP_\mu-Q_\mu XLP_\mu\\
 &=L_QQ_\mu XP_\mu-Q_\mu XP_\mu L_P=L_QY-YL_P.
\end{aligned}
\]

\(\square\)

If \(q_k\) is an orthonormal eigenbasis of
\(\operatorname {Ran}P_\mu\), with
\(Lq_k=\lambda_kq_k\), the spectral theorem gives the exact formula

\[
\boxed{
 \|[X,P_\mu]P_\mu\|_{\rm HS}^2
 =\sum_{k=1}^m\int_{\sigma(L_Q)}
 \frac{d\|E_Q(\lambda)[L,X]q_k\|^2}
      {|\lambda-\lambda_k|^2}.}                      \tag{12}
\]

In particular, if

\[
 d(P_\mu)=\operatorname {dist}
 \{\sigma(L_P),\sigma(L_Q)\}>0,                      \tag{13}
\]

then

\[
 \|[X,P_\mu]P_\mu\|_{\rm HS}
 \le d(P_\mu)^{-1}\|Q_\mu[L,X]P_\mu\|_{\rm HS}.      \tag{14}
\]

Formula (12), rather than (14), is the useful identity. The bound (14)
loses the exact spectral denominators and cannot yield a uniform
subthreshold exclusion when a cluster approaches \(1/2\).

## 4. The corrected joint target

Substitution of (5), with \(P=\widetilde P\), into 106.52(14) gives,
at finite Euler cutoff,

\[
\boxed{
\begin{aligned}
 \operatorname {Tr}(\widetilde PH_N^2)
={}&\|C_N\widetilde P+2[X,\widetilde P]\widetilde P\|_{\rm HS}^2
 +4m\kappa_N^{(2)}\\
&-4\operatorname {Tr}(\widetilde PG_N^{(2)})
 -4\|[X,P_\mu]P_\mu\|_{\rm HS}^2.
\end{aligned}}                                       \tag{15}
\]

The physical three-point formula must combine the renormalized limit of
the first two terms in (15) with the Gamma--polar contribution before
comparing it to the last two positive quantities. Equivalently, the
force-bearing estimate has the shape

\[
\boxed{
\begin{aligned}
 &\bigl[\text{joint current square}
       +\text{Gamma--polar scalar completion}\bigr](P)\\
 &\qquad\ge
 4\operatorname {Tr}(\widetilde PG^{(2)})
 +4\|[X,P_\mu]P_\mu\|_{\rm HS}^2,                   \tag{16}
\end{aligned}}
\]

with all cutoffs removed jointly. The second term on the right can be
replaced exactly by (12), and its numerator is the full marked current
(9).

Equation (16) is stronger information than the primitive statement
\(j_2\ge0\): it asks the same joint current to pay both the centered
\(j_2\)-jump energy and its off-cluster position response. No component of
(16) can be estimated by itself without destroying the cancellation of
\(\kappa_N^{(2)}\).

## 5. Relation to earlier work

The compression shell in (11) is the Riesz-projection version of the
finite Fourier-position shell in E101.063. The new point is not the
existence of a Sylvester equation. It is the simultaneous identification,
in the Phase-106 full generator, of:

1. the wrong centered sign of the \(j_2\) translation trace;
2. the exact prime--Gamma marked current driving the shell; and
3. the two positive quantities which a closing joint estimate must
   dominate in (16).

No sign conclusion for (16) is asserted here.

### Subsequent cutoff correction

Document 106.55 proves that neither side of the proposed centered prime
comparison has a separate infinite-cutoff interpretation. Formula (16)
must therefore be read only at common finite cutoff, before the primitive
\(j_2\) term is cancelled against its intermediate-position defect. It is
not a valid standalone limiting inequality.
