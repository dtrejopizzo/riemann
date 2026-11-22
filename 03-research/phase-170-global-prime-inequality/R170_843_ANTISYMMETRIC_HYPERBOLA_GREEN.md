# R170_843 — Antisymmetric Green of the hyperbola: Laplace sign, support collision and minimal Hankel lift

Continuation of R161_057--065, R170_840 and
R170_841. Paper 46 is not modified.

**Domain correction (R170_844).** The energy and the collar of
\(\mathcal A^{\rm raw}\) of §§5--6 are valid. However, the
expressions of §§6--7 that apply the same interior observer
\(\mathscr R_\delta\) to \(C_N\), \(\dot C_N\) or
\(\mathcal A^{\rm ren}\) are only formal for an arbitrary shift
\(\delta>0\). R170_844 proves

\[
 K_{C_NF}(a)={N^{a+1/2}\over a+1/2}K_F(a),
\]

so that the renormalized lift with that observer requires the safe gate
\(\delta>\log N\), or a different exterior observer. For the
infinitesimal collar \(\delta\ll1\) the lift proposed in (7.3) is not
typed. R170_844 further proves that, even after repairing the domain,
the static factorization is blocked by the Fredholm condition on the
radical. These corrections do not affect Theorem 5.1 nor the raw sign
(5.18).

## 0. Verdict

The standard antisymmetric Green form, applied directly to

\[
 \mathcal A_{M,N}^{\rm raw}
 :=\dot L_MS_N-L_M\dot S_N,
 \tag{0.1}
\]

**does not** produce VIR--LB. The obstruction is exact:

1. \(\mathcal A_{M,N}^{\rm raw}\) is a Wronskian of coefficients of two
   causal convolutions that commute on the line; it is not an operator
   commutator;
2. upon compressing, any standard mixed Green form becomes literally the
   support concomitant
   \(\langle g,[P_T,\mathcal A_{M,N}]w\rangle\), the family already
   exhausted in R161_057--065;
3. reflection satisfies
   \(J\mathcal A_{M,N}J=\mathcal A_{M,N}^*\). Hence the Hermitian part is
   even and its diagonal does not vanish. The odd part is the
   anti-Hermitian one and its real diagonal does vanish — precisely the
   scalar that cannot orient the virial;
4. before grouping by \(k=dm\), the two derivatives of the same route are
   multiples of the same vector
   \(\partial_t\tau_{\log k}F\). Every alternating polarization of those
   two legs is zero; a Hermitian polarization returns
   \(\beta_{M,N}(k)\) or a second-order square.

However, the attempt produces a positive arithmetic piece that does not
appear in R161_057--065 nor in R170_841. The bilateral Laplace observation
diagonalizes the Wronskian **without** diagonalizing by physical fibers.
If

\[
 B_\Lambda(s):=\sum_{k\ge2}{\beta_\Lambda(k)\over k^s},
 \qquad s>1,
 \tag{0.2}
\]

then

\[
 \boxed{
 B_\Lambda(s)
 =\zeta''(s)-{2\zeta'(s)^2\over\zeta(s)}
 =-\zeta(s)^2\left({1\over\zeta(s)}\right)''>0.}
 \tag{0.3}
\]

The strict inequality is the concavity theorem for
\(1/\zeta\) on \((1,\infty)\). Consequently, for
\(a=s-1/2>1/2\),

\[
 \boxed{
 K_{\mathcal A_\infty^{\rm raw}F}(a)
 =-aB_\Lambda(a+1/2)K_F(a),}
 \tag{0.4}
\]

and the right-hand side has a strict orientation. There is moreover an
absolute cutoff \(N_0\), independent of \(T\), such that for every

\[
 N=M\ge \max\{N_0,\lceil e^{2T}\rceil\}
 \tag{0.5}
\]

the same orientation holds simultaneously on the entire Gamma lattice
\(a_m=2m+1/2\). In that finite statement one literally retains

\[
 \sum_{N<k\le N^2}{\beta_{N,N}(k)\over k^{2m+1}},
 \tag{0.6}
\]

i.e. the incomplete hyperbola \(k>N\); it is not replaced by a complete
convolution.

The result does not prove
\(\mathcal V_{\Lambda,T}(F)\le0\). In passing from (0.4) to the
renormalized physical operator, there appear, with exact equality,

\[
 \dot L_MC_N-L_M\dot C_N,
 \quad P_TZ_N(1-P_T),\quad (1-P_T)Z_NP_T,
 \quad R_T=P_T-\Pi_T,
 \tag{0.7}
\]

and the Tate virial term. None of them inherits the sign of (0.3). The
first-contact equation does not annihilate them either: inserting
\(F_\delta\) replaces the positive overlap
\(\langle F_\delta,E_TF\rangle\) by a filtered overlap with no sign.

The minimal non-diagonal operation identified is the Laplace Hankel Gram
\(G_\omega=R_\omega^*R_\omega\), inserted **before** compressing and
before taking the diagonal. Its bulk already has the sign proved by
(0.3)--(0.6). What is missing is a physical first-contact law equating
its polar, support and Tate ports to the exact virial. This is a real
reduction of VIR--LB: the arithmetic sign of the bulk is no longer a
conjecture; the only open block is its lift to the physical boundary.

## 1. Quantifiers and finite objects

Let \(T>0\) be a hypothetical first window and

\[
 N_T^\varepsilon
 =\{F\in\ker H_T:JF=\varepsilon F\},
 \qquad \varepsilon\in\{+1,-1\}.
 \tag{1.1}
\]

Set

\[
 P=P_T,\qquad Q=I-P,
 \qquad \Pi=\Pi_T,\qquad R=P-\Pi,
 \qquad I=\Pi+R+Q.
 \tag{1.2}
\]

Here \(R\) is the two-dimensional Tate block and \(Q\) is the physical
exterior. Fix initially integers \(M\ge N\ge\lceil e^{2T}\rceil\),
and use the conventions of R170_841:

\[
\begin{aligned}
 S_N&=\sum_{m\le N}m^{-1/2}\tau_{\log m},\\
 L_M&=\sum_{d\le M}{\Lambda(d)\over\sqrt d}\tau_{\log d},\\
 C_Nf(t)&=e^{-t/2}\int_{-\infty}^{t+\log N}e^{u/2}f(u)\,du,\\
 Z_N&=S_N-C_N.
\end{aligned}
 \tag{1.3}
\]

Dilation is

\[
 U_rf(t)=r^{-1/2}f(t/r),\qquad
 B(r)=U_r^{-1}BU_r,
 \qquad \dot B={d\over dr}B(r)\big|_{r=1},
 \tag{1.4}
\]

so that

\[
 \dot\tau_b=-b\,\partial_t\tau_b.
 \tag{1.5}
\]

We distinguish

\[
\begin{aligned}
 \mathcal A_{M,N}^{\rm raw}
   &:=\dot L_MS_N-L_M\dot S_N,\\
 \mathcal A_{M,N}^{\rm ren}
   &:=\dot L_MZ_N-L_M\dot Z_N\\
   &=\mathcal A_{M,N}^{\rm raw}
     -(\dot L_MC_N-L_M\dot C_N).
\end{aligned}
 \tag{1.6}
\]

If
\(\widetilde H_{M,N}=L_MZ_N-K_N^Z\), the master identity is

\[
 \boxed{
 2\dot L_MZ_N
 =\dot{\widetilde H}_{M,N}+\dot K_N^Z
  +\mathcal A_{M,N}^{\rm ren}.}
 \tag{1.7}
\]

The polar continuum has not been omitted: it is present simultaneously
in \(\dot Z_N=\dot S_N-\dot C_N\) and in the last line of (1.6).

For the raw hyperbola define

\[
 \beta_{M,N}(k)
 =\sum_{\substack{dm=k\\d\le M,\ m\le N}}
       \Lambda(d)\log{d\over m}.
 \tag{1.8}
\]

Then, without completing any fiber,

\[
 \boxed{
 \mathcal A_{M,N}^{\rm raw}
 =-\sum_{k\le MN}{\beta_{M,N}(k)\over\sqrt k}
       \partial_t\tau_{\log k}.}
 \tag{1.9}
\]

For \(k\le N\le M\), (1.8) is \(\beta_\Lambda(k)\). For
\(N<k\le MN\) it remains the truncated sum (1.8). In parallel, the
synchronized part of R170_841 is

\[
 \dot H_{M,N}^{\Lambda}
 =-\sum_{N<k\le MN}{h_{M,N}(k)\log k\over\sqrt k}
       \partial_t\tau_{\log k},
 \quad h_{M,N}(k)\ge0.
 \tag{1.10}
\]

(1.10) uses irreversibly
\(\delta_\Lambda(k)=\sum_{d\mid k}\Lambda(d)-\log k=0\) for
\(k\le N\). The two tails (1.8)--(1.10) will be kept separate.

All identities of §§1--5 hold on a compact smooth core. The Laplace
forms extend to \(L^2(-T,T)\) after the positive shift introduced in §5.
The passage to a first-contact vector is only used in §7, where the
missing regularity is made explicit.

## 2. Why \(\mathcal A\) is not a commutator

On the line, \(L_M,S_N,\dot L_M,\dot S_N\) are causal convolution
polynomials. Hence all of them commute with each other. In particular,

\[
 [L_M,S_N]=[\dot L_M,S_N]=[L_M,\dot S_N]=0,
 \tag{2.1}
\]

but (0.1) is not zero: it compares which leg received the derivative. It
is the determinant, or Wronskian, of the two scalar symbols.

### 2.1. Collinearity of the routes at \(r=1\)

Fix a factorization \(k=dm\). The two differentiated contributions to
that route are

\[
 x_{d,m}^{(L)}
 =-(\log d)\partial_t\tau_{\log k}F,
 \qquad
 x_{d,m}^{(S)}
 =-(\log m)\partial_t\tau_{\log k}F.
 \tag{2.2}
\]

They are real multiples of the same vector. Hence, for every alternating
form \(\Omega\),

\[
 \Omega(x_{d,m}^{(L)},x_{d,m}^{(S)})=0.
 \tag{2.3}
\]

A Hermitian form only sees products of \(\log d\) and \(\log m\). Its
linear part is

\[
 \log d-\log m,
 \tag{2.4}
\]

which upon synthesizing gives \(\beta_{M,N}(k)\); its positive
completion is quadratic and returns the variance \(\Sigma_\Lambda(k)\) of
R170_841.

This proves a no-go slightly stronger than the diagonal-fiber one: even
if labels \((d,m)\) are kept until the last step, the physical
alternating polarization disappears at \(r=1\). Declaring the labels
orthogonal before synthesizing would replace the physical PC Gram matrix
with an artificial direct sum and would lose the product/ratio collisions
of R161_031--035 and R163_140.

### 2.2. The finite separation that does avoid the collapse

Before differentiating, define

\[
 \mathcal W_{M,N}(r)
 :=L_M(r)S_N-L_MS_N(r).
 \tag{2.5}
\]

Then \(\mathcal W_{M,N}(1)=0\) and

\[
 \mathcal W_{M,N}'(1)=\mathcal A_{M,N}^{\rm raw}.
 \tag{2.6}
\]

At scale \(r\ne1\), a route \((d,m)\) contains two distinct
translations:

\[
 \tau_{(\log d)/r+\log m}
 -\tau_{\log d+(\log m)/r}.
 \tag{2.7}
\]

(2.7) is the minimal two-scale operation that preserves the legs. Its
renormalized version is obtained by replacing \(S_N\) with \(Z_N\) and
automatically contains \(C_N(r)\). The sign problem is not in defining
(2.7), but in pairing it with the first-contact equation; see §7.

## 3. Reflection audit and Hermitian part

For every real convolution \(B\), \(JBJ=B^*\). Since the factors of
(1.6) commute on the line,

\[
 J\mathcal A_{M,N}^{\rm raw}J
   =(\mathcal A_{M,N}^{\rm raw})^*,
 \qquad
 J\mathcal A_{M,N}^{\rm ren}J
   =(\mathcal A_{M,N}^{\rm ren})^*.
 \tag{3.1}
\]

Also \(JP=PJ\). Consequently,

\[
 J\operatorname{Herm}(P\mathcal AP)J
 =\operatorname{Herm}(P\mathcal AP),
 \tag{3.2}
\]

while

\[
 J{P\mathcal AP-P\mathcal A^*P\over2i}J
 =-{P\mathcal AP-P\mathcal A^*P\over2i}.
 \tag{3.3}
\]

Thus, on a vector of fixed parity \(F\), the scalar forced to zero is the
one in (3.3), not the Hermitian part that contains the real derivative of
the correlation.

The Hermitian part is also not entirely a boundary Hankel term:

\[
 \operatorname{Herm}(P\mathcal AP)
 =P\operatorname{Herm}(\mathcal A)P.
 \tag{3.4}
\]

To see this in a falsifiable way, choose a shift
\(0<b<2T\) present in (1.9) and a smooth function of fixed parity with
support farther than \(b\) from the endpoints. Then the support block of
that translation is zero on \(F\), but, for a generic choice of the
envelope,

\[
 \langle F,\operatorname{Herm}(\partial_t\tau_b)F\rangle\ne0.
 \tag{3.5}
\]

Hence (3.4) contains interior bulk. The hypothesis "parity sends the
Hermitian part to its negative" is refuted by (3.2).

## 4. The compressed Green form collides with R161_065

For any operator \(B\) on a common core and any \(g,w\), define

\[
 \mathfrak K_P(B;g,w)
 :=\langle Pg,PBw\rangle-\langle PB^*g,Pw\rangle.
 \tag{4.1}
\]

An expansion gives the universal identity

\[
 \boxed{
 \mathfrak K_P(B;g,w)=\langle g,[P,B]w\rangle.}
 \tag{4.2}
\]

For \(B=\mathcal A_{M,N}^{\rm ren}\), (4.2) is exactly the support
concomitant of R161_064--065 with another causal polynomial. It is not
an additional physical identity.

### 4.1. The two blocks of \([P,Z_N]\) remain

The Leibniz rule gives

\[
\begin{aligned}
 [P,\mathcal A^{\rm ren}]
 ={}&[P,\dot L_M]Z_N+\dot L_M[P,Z_N]\\
    &-[P,L_M]\dot Z_N-L_M[P,\dot Z_N].
\end{aligned}
 \tag{4.3}
\]

and

\[
 [P,Z_N]=PZ_NQ-QZ_NP.
 \tag{4.4}
\]

Thus the two required orientations appear literally,

\[
 PZ_NQ,\qquad QZ_NP.
 \tag{4.5}
\]

Moreover \(\dot Z_N=\dot S_N-\dot C_N\). The polar derivative is not an
omissible symbol; R170_841 computed

\[
\begin{aligned}
 \dot C_Nf(t)={}&(1-t/2)C_Nf(t)
 +e^{-t/2}\int_{-\infty}^{t+\log N}{v\over2}e^{v/2}f(v)\,dv\\
 &-(\log N)\sqrt N\,f(t+\log N).
\end{aligned}
 \tag{4.6}
\]

The last summand of (4.6) is a boundary face and has no sign when paired
with a contact test.

### 4.2. Tate is not absorbed into the exterior

With primitive compression,

\[
 [\Pi,B]
 =\Pi B(R+Q)-(R+Q)B\Pi.
 \tag{4.7}
\]

(4.7) separates, with no hidden terms, the Tate port \(R\) and the
exterior port \(Q\). Applied to (4.3), it keeps the polar continuum in
each port. The dilation term of the primitive projection is moreover

\[
 \mathfrak T_T(F)
 =2\operatorname{Re}\langle F,tr_F'\rangle,
 \tag{4.8}
\]

which is not annihilated by the two ordinary Tate moments.

Formulas (4.2)--(4.8) are precisely the collision with
R161_057--065:

- R161_057 already preserves the two ports of (4.5);
- R161_059 shows that compressing operators that commute produces
  exterior cross products, not a square;
- R161_063 separates \(R\) and \(Q\), and proves that the Tate diagonal
  has the wrong type;
- R161_065 identifies every standard mixed Green form with (4.2).

Inserting the synchronized derivative changes the coefficients of
\(B\), but does not change the compression algebra. That is why it does
not overcome that no-go.

### 4.3. The tests \(XF\) and \(F_\delta\)

Since \(X\) reverses parity and
\(\operatorname{Herm}\mathcal A\) preserves it,

\[
 \langle XF,\operatorname{Herm}(\mathcal A)F\rangle=0.
 \tag{4.9}
\]

The anti-Hermitian part can be paired with \(XF\), but splitting
\(I=\Pi+R+Q\) reproduces the horizontal-modulation tautology and the
support concomitant of R161_042--044. Its literal Tate part is zero by
opposite parity. Thus \(XF\) does not avoid (4.2).

The state of the larger window \(F_\delta\) has the correct parity and
does not force (4.9). However, the minimality sign lives only in

\[
 \lambda_\delta
 \langle F_\delta,E_TF\rangle<0
 \tag{4.10}
\]

after choosing the phase with positive overlap. For a filter
\(B\), the eigenvalue equation only gives

\[
 \lambda_\delta\langle F_\delta,BE_TF\rangle
 =\langle F_\delta,H_{T+\delta}BE_TF\rangle.
 \tag{4.11}
\]

With \(B=S_N,Z_N,\mathcal W(r)\) or \(\mathcal A\), the new overlap of
(4.11) has no sign. Taking \(B^*B\) does not fix the problem because the
two vectors remain distinct; if \(B\) is placed on both sides, one
obtains a second-order energy and the cross terms audited in R162_503
and R170_840 reappear.

This proves the exact no-go of the standard antisymmetric Green form,
even with the off-diagonal insertion \(XF\) or \(F_\delta\).

## 5. The new sign: Dirichlet Wronskian and Laplace observation

Let

\[
 \ell_M(s)=\sum_{d\le M}{\Lambda(d)\over d^s},
 \qquad
 \sigma_N(s)=\sum_{m\le N}{1\over m^s}.
 \tag{5.1}
\]

The transform of (1.8) is exactly

\[
 \boxed{
 B_{M,N}(s)
 :=\sum_{k\le MN}{\beta_{M,N}(k)\over k^s}
 =\ell_M(s)\sigma_N'(s)-\ell_M'(s)\sigma_N(s).}
 \tag{5.2}
\]

This is the scalar Wronskian corresponding to (0.1). For
\(K_F(a)=\int F(t)e^{-at}\,dt\), integration by parts and translation
give

\[
 K_{\partial_t\tau_{\log k}F}(a)
 =a k^{-a}K_F(a).
 \tag{5.3}
\]

With \(s=a+1/2\), (1.9) and (5.3) imply

\[
 \boxed{
 K_{\mathcal A_{M,N}^{\rm raw}F}(a)
 =-aB_{M,N}(s)K_F(a).}
 \tag{5.4}
\]

No diagonal grouping was performed here: (5.4) coherently observes the
complete hyperbola, including its part \(k>N\).

### 5.1. Full limit and reciprocal concavity

For \(s>1\),

\[
 \ell_\infty(s)=-{\zeta'(s)\over\zeta(s)},
 \qquad \sigma_\infty(s)=\zeta(s).
 \tag{5.5}
\]

Substituting (5.5) in (5.2) gives

\[
\begin{aligned}
 B_\Lambda(s)
 &=\zeta''(s)-{2\zeta'(s)^2\over\zeta(s)}\\
 &=-\zeta(s)^2(1/\zeta(s))''.
\end{aligned}
 \tag{5.6}
\]

The theorem of E. Alkan, *Resolution of a conjecture on the convexity of
zeta functions*, J. Math. Anal. Appl. 472 (2019), 1987--2016,
[doi:10.1016/j.jmaa.2018.12.034](https://doi.org/10.1016/j.jmaa.2018.12.034),
proves that \(1/\zeta\) is strictly concave on \((1,\infty)\).
Since \(\zeta(s)>0\), (0.3) follows from (5.6).

The identity is also obtained coefficient by coefficient. Using
\(\sum_{d\mid k}\Lambda(d)=\log k\),

\[
\begin{aligned}
 \beta_\Lambda(k)
 &=2\sum_{d\mid k}\Lambda(d)\log d-(\log k)^2,\\
 \sum_{k\ge2}{\beta_\Lambda(k)\over k^s}
 &=\zeta''(s)-{2\zeta'(s)^2\over\zeta(s)}.
\end{aligned}
 \tag{5.7}
\]

Here \(\delta_\Lambda=0\) is used irreversibly. For a general weight
\(a\), with \(A(s)=\sum a(n)n^{-s}\), the result is only

\[
 B_a(s)=A(s)\zeta'(s)-A'(s)\zeta(s),
 \tag{5.8}
\]

with no associated concave reciprocal function. With the ordinary comb,
Davenport--Heilbronn falls into (5.8), not into (5.6).

### 5.2. The finite cutoff retains \(k>N\) and the Gamma sign

Take \(M=N\). Then

\[
 B_{N,N}(s)
 =\sum_{k\le N}{\beta_\Lambda(k)\over k^s}
  +\sum_{N<k\le N^2}{\beta_{N,N}(k)\over k^s}.
 \tag{5.9}
\]

The second summand of (5.9) is exactly the incomplete hyperbola. It
cannot be omitted in the argument that follows.

**Theorem 5.1 (finite positivity uniform on the Gamma lattice).**
There is an absolute integer \(N_0\) such that

\[
 B_{N,N}(s)>0
 \qquad(N\ge N_0,\ s\ge3).
 \tag{5.10}
\]

*Proof.* By (0.3), \(2^sB_\Lambda(s)>0\) for \(s\ge3\), and

\[
 \lim_{s\to\infty}2^sB_\Lambda(s)
 =\beta_\Lambda(2)=(\log2)^2.
 \tag{5.11}
\]

Continuity and (5.11) imply

\[
 c_0:=\inf_{s\ge3}2^sB_\Lambda(s)>0.
 \tag{5.12}
\]

On the other hand,

\[
 2^s|B_\Lambda(s)-B_{N,N}(s)|
 \le
 \sum_{\substack{d,m\ge1\\d>N\ \text{or}\ m>N}}
 \Lambda(d)|\log d-\log m|
 \left({2\over dm}\right)^s.
 \tag{5.13}
\]

For \(s\ge3\), the right-hand side is dominated by the convergent series
obtained by substituting \(s=3\). Its tail tends to zero with \(N\),
uniformly in \(s\ge3\). Choose \(N_0\) so that (5.13) is less than
\(c_0/2\). Then
\(2^sB_{N,N}(s)\ge c_0/2\), which proves (5.10). \(\square\)

The quantifier is uniform in the window: for every \(T>0\) it suffices
to choose

\[
 N=M\ge\max\{N_0,\lceil e^{2T}\rceil\}.
 \tag{5.14}
\]

### 5.3. Finite Hankel energy with a sign

Set

\[
 a_m=2m+1/2,\qquad s_m=a_m+1/2=2m+1,
 \qquad m\ge1,
 \tag{5.15}
\]

and, for \(\delta>0\), define

\[
 (R_{T,\delta}F)_m
 :=e^{-a_m(T+\delta)}K_F(a_m).
 \tag{5.16}
\]

This map is bounded from \(L^2(-T,T)\) to \(\ell^2\) and is faithful by
the completeness of the Gamma moments. Indeed,

\[
 \sum_{m\ge1}e^{-2a_m(T+\delta)}|K_F(a_m)|^2
 \le {\|F\|_2^2\over2}
       \sum_{m\ge1}{e^{-2a_m\delta}\over a_m}<\infty.
 \tag{5.17}
\]

From (5.4) and Theorem 5.1,

\[
\boxed{
\begin{aligned}
 \mathscr E_{N;T,\delta}^{\beta}(F)
 &:=-\operatorname{Re}
   \langle R_{T,\delta}F,
           R_{T,\delta}\mathcal A_{N,N}^{\rm raw}F\rangle\\
 &=\sum_{m\ge1}a_mB_{N,N}(s_m)
     e^{-2a_m(T+\delta)}|K_F(a_m)|^2\\
 &>0\qquad(F\ne0),
\end{aligned}}
 \tag{5.18}
\]

for \(N\) as in (5.14). This is an oriented sum of squares born from the
divisor Wronskian, not from \(\Sigma_\Lambda(k)\). The operator pairing
is first proved on the smooth core. Its second line defines by continuity
the form on all of \(L^2(-T,T)\), even though
\(\mathcal A\) contains \(\partial_t\).

In the limit \(N\to\infty\), its Hankel kernel is

\[
 \mathcal K_\beta(v)
 =\sum_{m\ge1}a_mB_\Lambda(s_m)e^{-a_mv}>0,
 \tag{5.19}
\]

and, using absolute convergence,

\[
 \mathcal K_\beta(v)
 =\sum_{k\ge2}{\beta_\Lambda(k)\over\sqrt k}
   \sum_{m\ge1}a_me^{-a_m(v+\log k)}.
 \tag{5.20}
\]

Thus (5.20) is a non-coefficient-by-coefficient telescoping: the
\(\beta_\Lambda(k)\) change sign, but their transform on the Gamma
lattice is strictly positive.

### 5.4. Honest falsifier of the Gamma piece

The positivity of (5.18) is not enough as an arithmetic separation. At
points \(s_m\ge3\), many altered positive weights also have a positive
Wronskian: the comb \(m^{-s_m}\) concentrates much mass at \(m=1\), while
every prime weight lives on \(d\ge2\). Hence (5.18), by itself, cannot be
presented as the load-bearing step of VIR--LB.

The full identity (0.3) is indeed specific to \(\Lambda\) on the whole
half-plane \(s>1\). For example, for the altered weight concentrated at
\(d=2\),

\[
 B_{\delta_2}(s)
 =2^{-s}\zeta(s)
   \left(\log2+{\zeta'(s)\over\zeta(s)}\right),
 \tag{5.21}
\]

which is negative for \(s>1\) sufficiently close to \(1\). A continuous
Laplace observation with support on that interval separates
\(\Lambda\) from that positive weight. The physical Gamma lattice does
not enter that interval; connecting the continuous observation with
PC/polar is a genuinely new part, not a consequence of the already
audited Gamma poles.

The falsifier of R170_841 also remains intact at finite cutoff: for every
altered weight there appears the block under

\[
 -\sum_{k\le N}{\delta_a(k)\log k\over\sqrt k}
       \partial_t\tau_{\log k},
 \tag{5.22}
\]

which is zero for \(\Lambda\) and not for Davenport--Heilbronn with the
ordinary comb. A final proof must jointly use (5.22) and the Wronskian
sign, not only (5.18).

## 6. The physical ledger after the arithmetic sign

The energy (5.18) orients \(\mathcal A^{\rm raw}\). For the renormalized
operator, (1.6) gives the exact equality

\[
\begin{aligned}
 -\operatorname{Re}\langle RF,R\mathcal A^{\rm ren}F\rangle
 ={}&\mathscr E^\beta(F)\\
 &+\operatorname{Re}\langle RF,
   R(\dot L_MC_N-L_M\dot C_N)F\rangle,
\end{aligned}
 \tag{6.1}
\]

where here \(R=R_{T,\delta}\) is the Laplace observation, not the Tate
block of (1.2). The second line contains (4.6) and has no sign.

To avoid that notation collision, write from now on

\[
 \mathscr R_\delta:=R_{T,\delta},
 \qquad G_\delta:=\mathscr R_\delta^*\mathscr R_\delta\ge0.
 \tag{6.2}
\]

Then

\[
 \mathscr E^\beta(F)
 =-\operatorname{Re}\langle F,
       G_\delta\mathcal A^{\rm raw}_{N,N}F\rangle.
 \tag{6.3}
\]

Compressing to the primitive part and inserting
\(I=\Pi+R+Q\), (6.3) decomposes exactly into

\[
\begin{aligned}
 \mathscr E^\beta(F)
 ={}&-\operatorname{Re}\langle F,
       \Pi G_\delta\Pi\mathcal A^{\rm raw}\Pi F\rangle\\
 &-\operatorname{Re}\langle F,
       \Pi G_\delta(R+Q)\mathcal A^{\rm raw}\Pi F\rangle,
 \qquad F\in\Pi L^2.
\end{aligned}
 \tag{6.4}
\]

The second line of (6.4) is the Tate/exterior port generated by the
Hankel Gram. If \(\mathcal A^{\rm raw}\) is replaced by
\(\mathcal A^{\rm ren}\), one adds exactly:

1. the polar block of (6.1), with \(\dot C_N\) given by (4.6);
2. the two blocks \(PZ_NQ\) and \(QZ_NP\) of (4.5), via (4.3);
3. the Tate ports \(R\) of (4.7);
4. the derivative of the primitive projection, whose scalar is (4.8);
5. the synchronized tail \(k>N\) of (1.10), using (1.7) to recover
   \(2\dot L_NZ_N\).

This is the complete ledger requested. Unlike a standard Green form,
\(G_\delta\) is Hankel and does not commute with translations. That is
why it breaks the collision with R161_065 and preserves interferences
between the two legs. Its bulk is already oriented by (5.18).

### 6.1. Exact typed collar of the Wronskian

The analogy with R161_070 can be made literal. Define, first on the
smooth core,

\[
\begin{aligned}
 \mathbb B_{N,T}^{\beta}
   &:=P\mathcal A_{N,N}^{\rm raw}P,\\
 \mathbb E_{N,T,\delta}^{\beta}
   &:=\mathscr R_\delta Q\mathcal A_{N,N}^{\rm raw}P,\\
 D_{\beta,N}
   &:=\operatorname{diag}_{m\ge1}
       \{a_mB_{N,N}(s_m)\}.
\end{aligned}
 \tag{6.5}
\]

In coordinates, the exterior port is

\[
 (\mathbb E_{N,T,\delta}^{\beta}F)_m
 =-e^{-a_m(T+\delta)}
   \sum_{k\le N^2}{\beta_{N,N}(k)\over\sqrt k}
   \int_{\mathbb R\setminus(-T,T)}e^{-a_mt}
      \partial_t\tau_{\log k}F(t)\,dt.
 \tag{6.5a}
\]

The sum in (6.5a) includes, unchanged, the terms
\(N<k\le N^2\). Integrating by parts cuts them into boundary values and
exterior moments; it does not annihilate them.

Splitting the output via \(I=P+Q\) in (5.4) gives

\[
 \boxed{
 \mathscr R_\delta\mathbb B_{N,T}^{\beta}
 =-D_{\beta,N}\mathscr R_\delta P
  -\mathbb E_{N,T,\delta}^{\beta}.}
 \tag{6.6}
\]

By (5.14), \(D_{\beta,N}>0\). Multiplying (6.6) by
\(\mathscr R_\delta^*\), taking Hermitian parts and then the diagonal
produces

\[
\boxed{
\begin{aligned}
 \mathscr E_{N;T,\delta}^{\beta}(F)
 ={}&-\operatorname{Re}
     \langle\mathscr R_\delta F,
             \mathscr R_\delta\mathbb B_{N,T}^{\beta}F\rangle\\
 &-\operatorname{Re}
     \langle\mathscr R_\delta F,
             \mathbb E_{N,T,\delta}^{\beta}F\rangle.
\end{aligned}}
\tag{6.7}
\]

for \(F\in PL^2\) in the form domain. This is a finite, typed, signed
Green law. Its second line is the exact exterior collar; it is not a
truncation error.

For the primitive compression, replace \(P\) by \(\Pi\) and
\(Q\) by \(R+Q\). Thus

\[
\boxed{
 \mathscr R_\delta\Pi\mathcal A_{N,N}^{\rm raw}\Pi
 =-D_{\beta,N}\mathscr R_\delta\Pi
  -\mathscr R_\delta(R+Q)
       \mathcal A_{N,N}^{\rm raw}\Pi.}
 \tag{6.8}
\]

(6.8) contains Tate and exterior separately in the last term. On
replacing \(\mathcal A^{\rm raw}\) by
\(\mathcal A^{\rm ren}\), the difference in each of its three operators
is exactly
\(\dot L_MC_N-L_M\dot C_N\), with \(\dot C_N\) given by (4.6).
Therefore (6.8), and not a formal Green form without ports, is the
maximal physical antisymmetric law obtained algebraically.

The blockage is now visible in a single line: first contact gives
\(H_TF=0\), but not
\(\Pi\mathcal A_{N,N}^{\rm ren}\Pi F=0\). Substituting that latter
vanishing into (6.8) would assume precisely the lift that must be
proved.

## 7. First contact: what is obtained and the missing step

Let \(F_\delta\) be the state of window \(T+\delta\), with the phase of
R170_840:

\[
 H_{T+\delta}F_\delta=\lambda_\delta F_\delta,
 \qquad \lambda_\delta<0,
 \qquad \langle F_\delta,E_TF\rangle>0.
 \tag{7.1}
\]

Applying (2.5) or \(G_\delta\mathcal A\) to the second argument changes
the overlap of (7.1). The resulting identity is (4.11), and it has no
sign. Hence first contact does **not** automatically turn (5.18) into an
inequality on the radical.

The minimal non-diagonal operation is now determined, not postulated: one
must use the renormalized PC identity with the test

\[
 G_\delta E_TF
 \quad\hbox{or, equivalently, the pair of ports}\quad
 (\mathscr R_\delta E_TF,
  \mathscr R_\delta\mathcal A^{\rm ren}E_TF),
 \tag{7.2}
\]

before taking the diagonal. A valid completion must prove a
factorization without inverting the zero mode,

\[
 \boxed{
 \Pi G_\delta\mathcal A_{N,N}^{\rm ren}\Pi
 =H_T\mathcal K_{N,T,\delta}
  +\mathcal B_{N,T,\delta}^{\rm pol}
  +\mathcal B_{N,T,\delta}^{\rm supp}
  +\mathcal B_{N,T,\delta}^{\rm Tate},}
 \tag{7.3}
\]

where the last three operators must be the explicit blocks of
(4.3)--(4.8), not free residues. Pairing (7.3) with
\(F\in N_T^\varepsilon\), the first term vanishes by radicality and the
left-hand side carries the strict bulk (5.18). What remains to be proved
is that the sum of the three physical blocks coincides, with the correct
orientation, with

\[
 -\mathcal V_{\Lambda,T}(F)
 \quad\hbox{minus the positive energy of (5.18).}
 \tag{7.4}
\]

(7.3) is weaker than VIR--LB: its bulk and all its coefficients are
fixed, the cutoff can be chosen uniformly by (5.14), and the only terms
left to compute are the explicit polar term, the two support blocks and
Tate. But (7.3)--(7.4) are not proved in the corpus. Declaring them by
definition would be exactly postulating the desired sign.

### 7.1. Why the usual Green form cannot prove (7.3)

If \(G_\delta\) is replaced by the identity, the left-hand side of
(7.3) returns to (4.2). If it is replaced by a convolution operator that
commutes with \(\mathcal A\), R161_059 returns cross products of the same
ports. The minimal feature avoiding both collapses is

\[
 G_\delta(t,u)=g_\delta(t+u),
 \tag{7.5}
\]

i.e. its Hankel character. This is the concrete non-diagonal insertion
not exhausted by R161_057--065.

### 7.2. Equivalent alternative at finite scale

The family \(\mathcal W_{M,N}(r)\) of (2.5) keeps the two routes before
differentiating. Its polarization against the Hankel Gram satisfies

\[
 {d\over dr}
 \operatorname{Re}\langle F,G_\delta\mathcal W_{N,N}(r)F\rangle
 \big|_{r=1}
 =-\mathscr E_{N;T,\delta}^{\beta}(F)<0.
 \tag{7.6}
\]

(7.6) is the arithmetic antisymmetric Green law obtained. To make it
physical, one must evaluate the same derivative after renormalized PC and
prove that its boundary terms are those of (7.3). Pairing
\(\mathcal W(r)F\) directly with \(F_\delta\) loses the sign by
(4.11), so that the Hankel Gram of (7.2) is indispensable.

## 8. Exact no-go of the attempted class

Let \(\mathscr C_{\rm Green}^{(1)}\) be the class of arguments that:

1. use \(\mathcal A_{M,N}^{\rm raw}\) or
   \(\mathcal A_{M,N}^{\rm ren}\) at first order;
2. compress via \(P\) or \(\Pi\) and apply the mixed Green form (4.1);
3. may use reflection, \(XF\), \(F_\delta\), \(\dot C_N\), the two blocks
   of \([P,Z_N]\) and Tate;
4. do not insert between the two legs a Hankel operator that does not
   commute with translations;
5. do not postulate an additional exterior reciprocity.

**Theorem 8.1.** No argument of
\(\mathscr C_{\rm Green}^{(1)}\) derives VIR--LB.

*Proof.* By (2.2)--(2.3), the route-by-route alternation is zero. After
synthesizing, the only first-order operator is \(\mathcal A\).
By (4.2), every compressed Green form with that operator is
\(\langle g,[P,\mathcal A]w\rangle\), the R161_065 concomitant.
Primitive refinements only separate its blocks \(R\) and \(Q\) by
(4.7). Reflection annihilates the anti-Hermitian part and preserves the
Hermitian part by (3.2)--(3.3). The test \(XF\) gives (4.9) or the
already-audited Green form; the test \(F_\delta\) replaces the signed
overlap by the signless overlap of (4.11). Finally, \(\dot C_N\), support
and Tate are explicit terms but none has an individual sign. Under
conditions 4--5 there remains no operation producing the positive bulk
(5.18) nor orienting its ports. \(\square\)

Hypothesis 4 points exactly to what falls outside the no-go: the Hankel
Gram \(G_\delta\) of (6.2), or its continuous Laplace version supported
on \(s>1\). That operation already produces the sign of the hyperbola;
the remaining problem is exclusively the lift (7.3).

## 9. No-duplication audit and status

The precise comparison with the R161 family is:

| Document | Operation | Result | Difference in this document |
|---|---|---|---|
| R161_057 | Green with \(X\), four ports | leaves wrong-side flow and support | (4.9) proves that \(X\) does not orient the new Wronskian |
| R161_059 | compression of commuting pair | exterior cross products | (4.3) produces the same products with derived coefficients |
| R161_061 | alternating/Lagrangian Green | identically zero diagonal | (2.3) identifies the zero already in each route \((d,m)\) |
| R161_063 | nested Hermitian power | mistyped Tate diagonal | (4.7) preserves the same split \(R\oplus Q\) |
| R161_065 | support concomitant | collides with already audited \([P,S]\) | (4.2) proves the collision for \(\mathcal A\) |
| R161_026 | Gamma energy as Hankel Gram | direct sign is automatic; the inverse first-contact sign is missing | (5.18) changes the multiplier by the Wronskian \(B_{N,N}(s_m)\) |
| R161_028 | Gamma image = speed of the polar layer | localizes the Gram within \(C_N\), but leaves open the moving-discrepancy square | (6.1) shows the new polar residue with the already-oriented Wronskian |
| R161_068--070 | Gamma observation of \(L\) | scalar \(-\zeta'/\zeta(s_m)>0\) | (5.4) observes the Wronskian and gives \(B_\Lambda(s_m)>0\) |
| R161_069--070 | no-go of formal factorization and typed collar | a faithful detector does not vanish by radicality; the exterior cannot be erased | (7.3) is declared open and explicitly keeps support/Tate/polar |
| R170_841 | \(\beta(k)\) by fiber | changes sign; diagonal no-go | (5.18)--(5.20) reassembles those fibers into a positive Hankel form |

The new part is, therefore, the Wronskian multiplier
\(B_\Lambda\), its reciprocal-zeta sign, and the uniform finite
approximation that retains \(k>N\). The Hankel geometry and its polar
layer were already in R161_026--028; this document does not claim them as
new. The combination is neither the mixed Green form of R161_057 nor the
single-leg Gamma--Euler collar of R161_068, but its physical lift falls
under the typing caution of R161_069--070 and that is why it remains
open.

```text
finite Wronskian A_raw with all fibers k>N                       PROVED
collinearity of the two routes when differentiating at r=1        PROVED
compressed Green = support concomitant of R161_065                PROVED
Herm(PAP) entirely a boundary Hankel term                          FALSE
parity annihilates the Hermitian part                              FALSE

explicit retention of dot C_N                                     DONE
retention of PZ_NQ and QZ_NP                                       DONE
separation of Tate R=P-Pi and exterior Q                           DONE
use of the sign lambda_delta after filtering by A or Z              FALSE

identity B_Lambda=-zeta^2(1/zeta)''                                PROVED
sign B_Lambda(s)>0 for all s>1                                     CITED (ALKAN)
uniform finite positivity B_NN(s)>0, s>=3, N>=N0                   PROVED
strict Gamma Hankel energy of A_raw                                PROVED
exact typed collar of A_raw, equations (6.6)--(6.8)                PROVED
weight-separation of that isolated Gamma energy                    FALSE
full half-plane separation for an altered weight                   PROVED

physical Hankel lift with polar/support/Tate, equation (7.3)        OPEN
identification of its boundaries with -V_Lambda,T, equation (7.4)   OPEN
VIR--LB                                                            OPEN
complete bilateral law                                             OPEN
D                                                                   OPEN
```

The next calculation must not apply (4.1) again with
\(B=\mathcal A\): that class is closed by Theorem 8.1. It must expand
renormalized PC against the Hankel test (7.2), keep (4.6)--(4.8) and
decide (7.3) term by term. The bulk that expansion must transport already
has the strict sign (5.18).
