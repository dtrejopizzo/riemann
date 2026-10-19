# R170_840 — Bilateral collar law: normal form, no-go, and minimal virial datum

Continuation of R162_406--408 and R170_838--839.
Paper 47 is not modified.

## 0. Verdict

The requested bilateral law **does not exist as a consequence of the
current carriers**. This is proved below for the precise class formed by:

1. the minimality identity between windows $T$ and $T+\delta$;
2. the two orientations of the collar and the reflection $J$;
3. finite PC, raw or renormalized, before or after the cancellation
   $\Lambda*1=\log$;
4. the compressed Chebyshev identity;
5. the finite detector $R_L$, the Gamma--Euler collar and the exact
   Schur/Feshbach of R162_408.

The result does not claim it is impossible to prove D by a new arithmetic
identity. It claims something more bounded and verifiable: every bilateral
expression obtained with the above operations has the normal form

\[
 \boxed{
 \mathfrak C_{M,N;T,\delta}(F,F_\delta)
 =-\langle\ell_L^\varepsilon(R_LF),f_{\delta,c}\rangle
  +\langle\widehat\xi_F^{>L},f_{\delta,c}\rangle
  +\mathcal R^Z_{M,N;T,\delta}(F,F_\delta),}
 \tag{0.1}
\]

where $f_{\delta,c}=1_{C_\delta}F_\delta$. Here
$\widehat\xi_F^{>L}$ contains the Gamma tail, all the Euler translates and
the possible threshold atom, but not the Tate vector. The local Tate term
cancels **exactly** when passing from the minimality identity to the PC
scalar. The price is the nonlocal residual

\[
 \mathcal R^Z_{M,N;T,\delta}
 =\langle1_{C_\delta}(Z_N-I)A_ME_TF,f_{\delta,c}\rangle .
 \tag{0.2}
\]

If one works directly with minimality, without the PC filter, the normal
form is

\[
 \boxed{
 \lambda_\delta\langle F_\delta,E_TF\rangle
 =-\langle\ell_L^\varepsilon(R_LF),f_{\delta,c}\rangle
  +\langle\widehat\xi_F^{>L},f_{\delta,c}\rangle
  -\langle r_F,f_{\delta,c}\rangle .}
 \tag{0.3}
\]

This accounts, without ellipses, for the three residues of the question:
tail, Tate and nonlocal transport. The two orientations do not give two
independent inequalities. In the selected parity sector, the right and
left local contributions are equal; their sum doubles them and their
difference vanishes. Any asymmetry that survives the $Z_N$ filter belongs
to (0.2) and does not inherit the sign of $\lambda_\delta$.

The exact cancellation

\[
 \delta_\Lambda(k)=\sum_{d\mid k}\Lambda(d)-\log k=0
 \tag{0.4}
\]

is indeed used, and is localized before recombining PC. The no-go theorem
proves that (0.4) eliminates a block of coefficients, but does not orient
any of the three terms of (0.1)--(0.3). After recombination, the form
returns to \(Z_NA_ME_TF\) and forgets the arithmetic reason why that block
disappeared.

The minimal datum that overcomes this no-go is not another collar norm.
Under the regularity needed for the window derivative to exist, it is a
bilateral law of **first-contact Euler-product virial**:

\[
 \boxed{
 \mathcal V_{\Lambda,T}|_{N_T^\varepsilon}\preceq0,
 \qquad
 \mathcal V_{\Lambda,T}(G)
 \ge c_T\langle R_LG,(I-D_{N,L})R_LG\rangle,
 \qquad c_T>0.}
 \tag{0.5}
\]

The first inequality must be obtained before recombining PC and must use
(0.4) essentially; the second must separate the detector from all the
residues of the normal form. Neither of the two is available as a pair in
the corpus. It is shown in §8 that, if both were proved with the
quantifiers indicated there, the virial selected by minimality would force
$R_LF=0$. We present that implication as a proof of sufficiency and of
logical strength, not as a conditional proof of D.

## 1. Quantifiers and scales

Let $T>0$ be a hypothetical first contact window and

\[
 N_T^\varepsilon
 =\{F\in\ker H_T:JF=\varepsilon F\},
 \qquad \varepsilon\in\{+1,-1\}.
 \tag{1.1}
\]

Let $F\in N_T^\varepsilon$ be the normalized limit of a subsequence of
ground states $F_\delta$ from the right. We choose their phases so that

\[
 a_\delta:=\langle F_\delta,E_TF\rangle>0,
 \qquad a_\delta\longrightarrow1,
 \tag{1.2}
\]

and write $H_{T+\delta}F_\delta=\lambda_\delta F_\delta$, with
$\lambda_\delta<0$.

The scale choices can be made unambiguously. Set

\[
 n_1(T):=\min\{n\in\mathbb N:n>e^{2T}\},
 \qquad
 \delta_{\rm gap}(T)
 ={1\over2}\min\!\left\{\log{n_1(T)\over e^{2T}},\log2\right\}.
 \tag{1.3}
\]

We will take, for example,

\[
 \delta_j=2^{-j}\delta_{\rm gap}(T),\quad
 T_j=T+\delta_j,\quad
 N_j=\lceil e^{2T_j}\rceil,\quad M_j=N_j,
 \qquad j\ge1.
 \tag{1.4}
\]

Then $0<\delta_j<\delta_{\rm gap}(T)$, $M_j\ge N_j$ and
$M_j\ge e^{2T_j}$. Therefore:

- the comb acting inside $I_{T_j}$ is complete;
- the truncation residual $\rho_M^\delta$ of R170_838 (3.4) is zero;
- the cancellation of coefficients $k\le N_j$ is justified;
- between $e^{2T}$ and $e^{2T_j}$ only the threshold integer $e^{2T}$
  can appear, and only if it is an integer.

Since $N_T^\varepsilon$ is finite-dimensional and the complete family of
Gamma moments is faithful, there exists

\[
 L_T:=\min\{L\ge1:R_L|_{N_T^\varepsilon}\text{ is injective}\}.
 \tag{1.5}
\]

This definition is exact, but the corpus gives no computable bound for
$L_T$, nor a bound uniform in $T$. This fact will be one of the
uniformity obstructions, not a choice we will hide in a constant.

Write

\[
 C_\delta^+=(T,T+\delta),\qquad
 C_\delta^-=(-T-\delta,-T),\qquad
 C_\delta=C_\delta^+\cup C_\delta^-.
 \tag{1.6}
\]

All the pairings below are $\mathcal Q_{\log}'$--$\mathcal Q_{\log}$ form
pairings. On the regular kernel they coincide with the written $L^2$
products.

## 2. Normal form in one orientation

On the right collar, R162_406 gives

\[
 \xi_{F,+}^\delta(t)
 =-\gamma_F(t)-\Pi_{\Lambda,T}^\delta F(t)-r_F(t),
 \qquad t\in C_\delta^+,
 \tag{2.1}
\]

where

\[
 \gamma_F(t)=\sum_{m\ge1}e^{-a_mt}\mu_F(a_m)
 \tag{2.2}
\]

(the mode (a_0=1/2) vanishes by primitivity), and

\[
 \Pi_{\Lambda,T}^\delta F(t)
 =\sum_{2\le d<e^{2T}}{\Lambda(d)\over\sqrt d}
      F(t-\log d)
 +\theta_T\varepsilon{\Lambda(n_0)\over\sqrt{n_0}}
      F(2T-t).
 \tag{2.3}
\]

Here $n_0=e^{2T}$ and $\theta_T=1$ only when $n_0$ is a prime power. At
an integer threshold that is not a prime power, the last summand is zero
exactly by compressed Chebyshev.

With the normalization of Paper 47 there exists the injective map

\[
 \ell_L(R_LF)(t)=\sum_{m\le L}e^{-a_mt}\mu_F(a_m).
 \tag{2.4}
\]

The factors $b_m$, $e^{a_m(T+\delta_0)}$ and the parity can be absorbed
into the definition of $\ell_L$, as in R162_406 Proposition 4.1. We
define the Tate-free tail by

\[
 \widehat\xi_{F,+}^{>L}(t)
 :=-\sum_{m>L}e^{-a_mt}\mu_F(a_m)
   -\Pi_{\Lambda,T}^\delta F(t).
 \tag{2.5}
\]

Then, exactly,

\[
 \boxed{
 \xi_{F,+}^\delta
 =-\ell_L(R_LF)+\widehat\xi_{F,+}^{>L}-r_F.}
 \tag{2.6}
\]

The notation $\xi_F^{>L}$ of R162_406 includes $-r_F$; therefore

\[
 \xi_F^{>L}=\widehat\xi_F^{>L}-r_F.
 \tag{2.7}
\]

This distinction avoids double-counting Tate in the PC form.

The signed minimality identity becomes

\[
 \lambda_\delta a_\delta
 =-\langle\ell_L^\varepsilon(R_LF),f_{\delta,c}\rangle
  +\langle\widehat\xi_F^{>L},f_{\delta,c}\rangle
  -\langle r_F,f_{\delta,c}\rangle .
 \tag{2.8}
\]

This is (0.3). No term has been estimated and no orientation has been
lost.

## 3. The two orientations do not generate two signs

By construction,

\[
 JF=\varepsilon F,\qquad JF_\delta=\varepsilon F_\delta,
 \qquad J\xi_F^\delta=\varepsilon\xi_F^\delta,
 \qquad Jr_F=\varepsilon r_F.
 \tag{3.1}
\]

If $u_+$ is any of the local terms of (2.6) on
$C_\delta^+$, its left copy is $u_-=\varepsilon Ju_+$, and
$f_{\delta,-}=\varepsilon Jf_{\delta,+}$. Since $J$ is unitary,

\[
 \langle u_-,f_{\delta,-}\rangle_{C_\delta^-}
 =\langle u_+,f_{\delta,+}\rangle_{C_\delta^+}.
 \tag{3.2}
\]

Consequently,

\[
 \begin{aligned}
  \langle u,f_{\delta,c}\rangle_{C_\delta}
     &=2\langle u_+,f_{\delta,+}\rangle,\\
  \langle u_+,f_{\delta,+}\rangle
     -\langle u_-,f_{\delta,-}\rangle&=0.
 \end{aligned}
 \tag{3.3}
\]

This holds separately for $\ell_L(R_LF)$, the Gamma tail, the Euler
comb, the threshold atom and Tate. Therefore a symmetric bilateral
combination only doubles (2.8), and an antisymmetric combination cancels
it. There is no system of two equations with which to eliminate the tail.

The one-sided filter $Z_N$ does not commute with $J$ nor with the
restriction to the collar. If $Z_N$ is used on the right and its
reflection $JZ_NJ$ on the left, (3.2) holds again. If the same one-sided
filter is used on both sides, the remaining difference is precisely part
of the nonlocal residual (0.2). That difference is not a second
minimality scalar.

## 4. PC normal form and exact cancellation of Tate

Set

\[
 g_{M,T}(F):=A_ME_TF.
 \tag{4.1}
\]

For $M\ge e^{2(T+\delta)}$, R170_838 proves on the collar

\[
 1_{C_\delta}g_{M,T}(F)=r_F+\xi_F^\delta.
 \tag{4.2}
\]

With

\[
 \mathfrak C_{M,N;T,\delta}(F,F_\delta)
 :=\langle1_{C_\delta}Z_Ng_{M,T}(F),f_{\delta,c}\rangle,
 \tag{4.3}
\]

inserting $Z_N=I+(Z_N-I)$ gives

\[
 \mathfrak C
 =\lambda_\delta a_\delta
  +\langle r_F,f_{\delta,c}\rangle
  +\mathcal R^Z_{M,N;T,\delta}.
 \tag{4.4}
\]

Substituting (2.8), the explicit Tate term cancels:

\[
 \boxed{
 \mathfrak C
 =-\langle\ell_L^\varepsilon(R_LF),f_{\delta,c}\rangle
  +\langle\widehat\xi_F^{>L},f_{\delta,c}\rangle
  +\mathcal R^Z_{M,N;T,\delta}.}
 \tag{4.5}
\]

This is the normal form (0.1). In the notation of R162_406 it reads

\[
 \mathfrak C
 =-\langle\ell_L^\varepsilon(R_LF),f_{\delta,c}\rangle
  +\langle\xi_F^{>L},f_{\delta,c}\rangle
  +\langle r_F,f_{\delta,c}\rangle
  +\mathcal R^Z.
 \tag{4.6}
\]

The two formulas are identical by (2.7). The Tate cancellation in (4.5)
is a bookkeeping advance, not a sign law.

The nonlocal residual is fully expanded as

\[
\begin{aligned}
 \mathcal R^Z_{M,N;T,\delta}
 ={}&\sum_{2\le n\le N}{1\over\sqrt n}
 \langle1_{C_\delta}\tau_{\log n}g_{M,T}(F),f_{\delta,c}\rangle\\
 &-\langle1_{C_\delta}C_N^{\rm pol}g_{M,T}(F),f_{\delta,c}\rangle .
\end{aligned}
 \tag{4.7}
\]

The first line reads $g_{M,T}(F)$ outside the collar; the second does
the same via the polar continuum. Although the restriction (4.2) is
stabilized once $M\ge e^{2(T+\delta)}$, that condition alone does not
stabilize (4.7): $g_{M,T}(F)$ can still acquire outer translates that
$Z_N$ returns to the collar. For fixed $N$ there is a larger cutoff,
depending on $N$ and on the support geometry, beyond which no more terms
appear; it is not the local cutoff (4.2). The choice
$M=N=\lceil e^{2(T+\delta)}\rceil$ of (1.4) fixes an admissible value, but
does not give it a sign or make it local.

## 5. Where the arithmetic of \(\mathbb Z\) exactly enters

For weights $a(d)$, let

\[
 \delta_a(k)=\sum_{d\mid k}a(d)-\log k,
 \qquad
 \mathcal D_a^{\le N}
 =\sum_{k\le N}{\delta_a(k)\over\sqrt k}\tau_{\log k}.
 \tag{5.1}
\]

If $M\ge N$, the raw hyperbola decomposes as

\[
 H_{M,N}^a=\mathcal D_a^{\le N}+H_{M,N}^{a,>N},
 \tag{5.2}
\]

and PC contains the inner block

\[
 -J\mathcal D_a^{\le N}
 -\mathcal D_a^{\le N}\mathscr F.
 \tag{5.3}
\]

For $a=\Lambda$, the exact integer identity gives

\[
 \mathcal D_\Lambda^{\le N}=0
 \quad\hbox{coefficient by coefficient.}                    \tag{5.4}
\]

This is the essential and localized use of $\Lambda*1=\log$. For a
finite modification, an isolated translate, Type I weights or
Davenport--Heilbronn, block (5.3) generally reappears.

But PC also gives

\[
 K_N=L_M^aS_N-H_{M,N}^a.
 \tag{5.5}
\]

On recombining (5.5), the variation of $L_M^aS_N$ cancels against the
full variation of $H_{M,N}^a$, and one recovers the operator $K_N$, which
does not depend on $a$. In particular, the PC expansion of (4.3) and the
normal form (4.5) are the same equality written in two bases. The
disappearance of (5.3) does not produce an additional inequality on $F$,
$F_\delta$ or $R_LF$.

This decides the real role of the available arithmetic:

```text
Lambda*1=log before recombining PC         eliminates an inner block
PC recombination                           returns to K_N / Z_N A_M
collar normal form                         retains no extra scalar
sign of lambda_delta                       only acts on the full xi
```

The cancellation is necessary for a future proof to pass the
falsifiers, but the zero value of a coefficient monitor carries no sign
and does not dominate the Gamma detector.

## 6. No-go for separating the three parts

### 6.1. The tail is not at a scale below the finite detector

R162_408 Proposition 5.1 proves that the boundary jets of
$\xi_F^\delta$ and the moments $R_LF$ are linearly independent data in
the ambient space. In particular, for normalized smooth sources the jets
produced by a Euler translate can be made arbitrarily large while
$R_LF\to0$. There also exist subspaces of codimension less than
$L-k-1$ where the first $k$ jets vanish and $R_L$ does not.

By duality, there is no universal estimate on the collar carrier of the
form

\[
 |\langle\widehat\xi_F^{>L},w_\delta\rangle|
 \le o(1)\,|\langle\ell_L(R_LF),w_\delta\rangle|
 \tag{6.1}
\]

for all $F$ and collar test functions $w_\delta$. It suffices to choose
the test aligned with the residual germ of the sources of R162_408
Proposition 5.1(a). The statement remains false if the right-hand side is
replaced by (o(1)\|R_LF\|\|w_\delta\|).

This does not construct a counterexample within the unknown radical. It
proves exactly the statement needed here: (6.1) is not a consequence of
the collar operators. An estimate valid only for the selected first-
contact vector would have to be a new relation on $N_T^\varepsilon$.

Moreover, the limit $\delta\downarrow0$ does not automatically favor the
observed part. For fixed $L$, $\ell_L(R_LF)$ is a sum of bounded
exponentials at the boundary. The germ of $\widehat\xi_F^{>L}$ contains
the boundary behavior of the whole Gamma series and interior values
independent of $F$. R162_408 shows that the Schur scale can range from
$\delta/\log(1/\delta)$ down to quantities smaller than any power,
depending on that germ. There is no universal rate that can be used to
choose $L$ before knowing $N_T^\varepsilon$.

### 6.2. Tate is not eliminated by orientation

In the direct identity (2.8), Tate has the same parity as the other
terms. By (3.2), the bilateral sum doubles it and the difference cancels
it together with the signed term. There is no combination of orientations
that preserves minimality and eliminates only Tate.

In the PC form, the local Tate term does cancel algebraically, as shown
by (4.5). This cancellation does not define an exterior Tate port.
R170_834 proves that reflection-compatible extensions change the port by
an arbitrary block of the form

\[
 \delta\Theta=\mathcal A^*K,
 \tag{6.2}
\]

and that the bilateral sum doubles that ambiguity on the correct parity
branch. Therefore the exterior Tate term is only intrinsic after
compressing to $\ker\mathcal A=\{F:r_F=0\}$, a reduction that does not
control the remaining Tate directions of the radical.

### 6.3. The nonlocal residual is not a small truncation error

Formula (4.7) shows that $\mathcal R^Z$ depends on exterior values of
$A_ME_TF$. Initially increasing $M$ beyond $e^{2(T+\delta)}$ does not
change (4.2), but it can change (4.7) up to the $N$-dependent support
cutoff. Hence no estimate using only $\xi_F^\delta$, $r_F$ and
$f_{\delta,c}$ can compute $\mathcal R^Z$.

Fixing (M=N\) via (1.4) removes the freedom of choice, not the term. The
translation operators and the polar continuum of (4.7) are bounded at
collar scale, but an absolute bound has the same problem as (6.1): it
destroys the cancellations and is not strictly smaller than the
contribution of $R_LF$. No sign is known for (4.7).

### 6.4. Feshbach orients the full sum, not its components

R162_408 writes the form in blocks

\[
 \begin{pmatrix}0&b_\delta\\b_\delta^*&A_\delta\end{pmatrix},
 \qquad
 b_\delta(F,w)=\langle\xi_F^\delta,w|_{C_\delta}\rangle,
 \tag{6.3}
\]

and proves

\[
 \lambda_\delta
 =-q_\delta(1+O(q_\delta)),\qquad
 Q_\delta(F,F)
 =\langle b_\delta(F,\cdot),A_\delta^{-1}
             b_\delta(F,\cdot)\rangle .
 \tag{6.4}
\]

If $u_F=-\ell_L(R_LF)$ and
$v_F=\widehat\xi_F^{>L}-r_F$, then

\[
 Q_\delta(F,F)
 =\langle u_F+v_F,A_\delta^{-1}(u_F+v_F)\rangle
 \tag{6.5}
\]

in the shorthand notation for the boundary functional. The expansion
contains

\[
 Q_\delta(u_F)+2\operatorname{Re}Q_\delta(u_F,v_F)+Q_\delta(v_F).
 \tag{6.6}
\]

The positivity of $A_\delta^{-1}$ only orients (6.5). It does not orient
the cross term nor allow recovering $Q_\delta(u_F)$ from the sign of the
sum. The two orientations have already been incorporated into $A_\delta$;
they do not diagonalize (6.6).

### 6.5. No-go theorem for the current carrier

**Theorem 6.1.** Fix $T$, $\delta$, $L$, $M$ and $N$ as in §1.
Every **two-window** scalar identity whose only argument of the larger
window is \(F_\delta\), obtained by linear compositions of finite PC,
compressed Chebyshev, reflection, restriction to the two collars,
pairing against $F_\delta$, the weak equation and the minimality
identity, reduces to a combination of:

1. the normal form (2.8) or (4.5);
2. invertible operator change-of-basis identities;
3. the null monitor $\mathcal D_\Lambda^{\le N}=0$.

Additional fixed-window identities, such as the balance
\(0=2c_{N,L}+Q_{N,L}\) of Paper 47, remain separate: they recompose the
weak equation and contain neither \(F_\delta\) nor the sign of
\(\lambda_\delta\).

None of these three classes implies a strict estimate of the tail, Tate
or $\mathcal R^Z$ by the $R_LF$ part. Therefore no law carrying the sign
of $\lambda_\delta$ through to $R_LF=0$ can be derived from that carrier.

*Proof.* Renormalized PC is the equality
$Z_NA_M\mathscr F=\mathfrak P_{M,N}^{\rm ren}$; $\mathscr F^2=I$
converts every PC--collar pairing into (4.3). Inserting
$Z_N=I+(Z_N-I)$ and using (4.2) gives (4.4). The only signed part of
(4.4) is the minimality identity, and its exact decomposition is (2.8).
This proves the reduction to (2.8)/(4.5).

Compressed Chebyshev uses an invertible unipotent operator and only
changes the basis of the finite algebra of translations (R162_406
Theorem 6.1). Decomposition (5.2) keeps, before recombining, block (5.3);
for $\Lambda$, (5.4) makes it zero. Recombining via (5.5) recovers the
same PC identity, so that no other scalar appears. Finally, §3 proves
that the second orientation equals the first in all local terms, and
§§6.1--6.4 prove that no sign or domination of components follows from
the normal form. The tests \(S_LF\) at fixed window give the Paper 47
balance; its spectral identity also holds for positive eigenvectors and
creates no coupling with \(F_\delta\). ∎

The theorem is pointwise in $T$. Consequently, the difficulty is not due
to a failure to uniformly optimize $L,M,N,\delta$.

## 7. Uniformity and falsifiers

### 7.1. No uniform quantifiers are available

Rules (1.3)--(1.4) are explicit for each $T$, but

\[
 \inf_T\delta_{\rm gap}(T)=0,
 \tag{7.1}
\]

because $e^{2T}$ can approach an integer from below. Moreover,
$N_j\asymp e^{2T}$ and there is no known bound for $L_T$. The equivalence
constants between the boundary energy, the Gamma energy and
$\|R_{L_T}F\|^2$ depend on the unknown radical. Hence the current
carriers do not provide a uniform choice in $T$ with an explicit
positive margin.

This lack of uniformity is not the main cause of the no-go: Theorem 6.1
already fails for fixed $T$ and fixed choices.

### 7.2. Positive eigenvectors

In a window with strictly decreasing fundamental eigenvalue
$\lambda(T)>0$, one has the covariant identity

\[
 (\lambda(T+\delta)-\lambda(T))
 \langle F_\delta,E_TF\rangle
 =\langle\xi_F^\delta,f_{\delta,c}\rangle,
 \tag{7.2}
\]

with the same normal forms (2.8) and (4.5). R162_408 proves the same
Schur/Feshbach, now around $\lambda(T)$, and Paper 47 gives
$R_LF\ne0$. Therefore any argument using only the sign of the descent,
bilaterality and the above operator identities would also falsely cancel
a positive eigenvector. The no-go passes F1.

### 7.3. Positive weights and Davenport--Heilbronn

The collar formulas, the Schur argument and the independence between
jets and moments hold for general weights. Davenport--Heilbronn has a
first contact, so a weight-blind law concluding $R_LF=0$ would be false
there.

The only piece that is not weight-blind is (5.4). For the falsifiers,
(5.3) appears, but its absence for $\Lambda$ alone does not produce a
sign. This explains simultaneously:

- why the no-go does detect the exact arithmetic of $\mathbb Z$;
- why that arithmetic still does not close the problem;
- what a new piece must use in a non-reversible way.

## 8. The minimal datum that would overcome the no-go

R162_407 identifies the first quantity that distinguishes a first
contact from a mere collar identity: the one-sided window derivative.
Under the regularity hypothesis (REG), and in the threshold regime with
the boundary regularity that eliminates the birth term, its form on the
radical is

\[
\begin{aligned}
 \mathcal V_{\Lambda,T}(F)
 ={}&{1\over2\pi}\int_{\mathbb R}
       \tau m'(\tau)|\widehat F(\tau)|^2\,d\tau\\
 &-\sum_{n<e^{2T}}{2\Lambda(n)\over\sqrt n}\,
       \log n\;c_F'(\log n)
 +2\operatorname{Re}\langle F,t r_F'\rangle .
\end{aligned}
 \tag{8.1}
\]

For the vector $G$ selected from the right,

\[
 \lambda_A(T+\delta)
 =-{\delta\over T}\mathcal V_{\Lambda,T}(G)+o(\delta),
 \qquad
 \mathcal V_{\Lambda,T}(G)
 =\max_{\substack{F\in N_T^\varepsilon\\\|F\|=1}}
     \mathcal V_{\Lambda,T}(F)\ge0.
 \tag{8.2}
\]

The minimal new law can now be stated without hidden residues.

**Open datum VIR--EP.** For every hypothetical first window $T$ and
sector $N_T^\varepsilon\ne0$:

1. the radical vectors have the regularity needed for (8.1) and, at a
   prime-power threshold, the birth term is $o(\delta)$;
2. there exist computable functions
   $L_*(T,\varepsilon)\in\mathbb N$ and $c_*(T)>0$, independent of
   the unknown radical, such that with
   \[
     L=L_*(T,\varepsilon),\qquad
     N=M=\lceil e^{2T}\rceil,\qquad c_T=c_*(T),
   \]
   the following two orientations hold. The scheme must hold for every
   \(T\); on every compact set of \(T\) one requires
   \(\sup L_*<\infty\) and \(\inf c_*>0\);

\[
 \boxed{
 \begin{aligned}
  \mathcal V_{\Lambda,T}(F)&\le0
       &&(F\in N_T^\varepsilon),\\
  \mathcal V_{\Lambda,T}(G)&\ge
       c_T\langle R_LG,(I-D_{N,L})R_LG\rangle
       &&(G\text{ selected by }F_\delta).
 \end{aligned}}
 \tag{8.3}
\]

3. the first line of (8.3) is proved on the PC hyperbola before (5.5):
   it projects the coefficients $k\le N$, uses
   $\mathcal D_\Lambda^{\le N}=0$, and retains the boundary contribution
   $k>N$. This requirement excludes a proof based only on
   $\Lambda(n)\ge0$, formal Chebyshev or contraction of $D_{N,L}$;
4. the second line is obtained from an estimate of the normal form
   (2.8) or (4.5) that accounts for the complete tail, Tate and
   $\mathcal R^Z$, and that does not use the a posteriori inverse of
   $R_L|_{N_T^\varepsilon}$.

VIR--EP is a single bilateral law on the radical: the first line is the
arithmetic tangency from the right and the second is the Gamma detection
with the opposite orientation. The virial formulation absorbs the Gamma,
Euler and Tate terms of (8.1), instead of declaring each part small
separately. The nonlocal residual $\mathcal R^Z$ must be eliminated via a
pre-filter identity or controlled in condition 4; omitting it does not
satisfy VIR--EP.

Condition 3 is load-bearing. If $\Lambda$ is replaced by $a$, the PC side
acquires block (5.3), and the first line of (8.3) must cease to be
derivable. For Davenport--Heilbronn, or for any weight system that has a
nontrivial first contact, (8.2) and the positivity of the reserve prove
that the two lines of (8.3) cannot hold simultaneously. In a positive
window the premise $H_TF=0$ of VIR--EP is not satisfied; if a covariant
extension to the ground state were attempted, the first line would fail
whenever the maximal virial measuring the eigenvalue's descent were
positive. Thus VIR--EP passes the falsifiers by its content, not merely
by a label.

**Proposition 8.1 (exact sufficiency of VIR--EP).** If VIR--EP holds at a
hypothetical first window, then the selected vector $G$ satisfies
$R_LG=0$.

*Proof.* The first line of (8.3), together with (8.2), gives

\[
 0\le\mathcal V_{\Lambda,T}(G)\le0.
 \tag{8.4}
\]

Hence $\mathcal V_{\Lambda,T}(G)=0$. The second line of (8.3) and the
uniform contraction of Paper 47,

\[
 I-D_{N,L}\succeq(1-q_0)I,
 \qquad q_0={\log2\over4}+{1\over16}<1.
 \tag{8.5}
\]

give

\[
 0=\mathcal V_{\Lambda,T}(G)
 \ge c_T(1-q_0)\|R_LG\|^2,
 \tag{8.6}
\]

and $R_LG=0$. If $R_L|_{N_T^\varepsilon}$ is injective, then
$G=0$, contradicting $\|G\|=1$. ∎

The proposition does not prove VIR--EP. It shows that its sign is not a
pending technical estimate: it has exactly the strength needed to
exclude first contact. R162_407 had already anticipated this conclusion
by reducing an $o(\delta)$ bound to a virial inequality on the radical.

Without (REG), the equivalent minimal datum must be formulated with the
ratio of dilation forms and must simultaneously prove the existence of
its limit. R162_408 allows flat profiles for which all polynomial rates
fail; hence that part of VIR--EP cannot be omitted nor replaced by a
universal rate in $\delta$.

## 9. Ledger

```text
choices delta_j, N_j, M_j for each T                        PROVED / EXPLICIT
finite L_T detecting the radical                             PROVED / NOT UNIFORM

xi=-ell_L(R_LF)+hatxi^(>L)-r                               PROVED
direct bilateral form (0.3)                                PROVED
equality of the two local orientations by parity             PROVED
second independent inequality from antisymmetry              FALSE

PC normal form (0.1)/(4.5)                                 PROVED
cancellation of local Tate inside the PC form                PROVED
fully expanded nonlocal residual R^Z                          PROVED
stabilization of R^Z upon stabilizing the collar              FALSE

delta_Lambda(k)=0 for k<=N, M>=N                           PROVED / EXACT
localization of the arithmetic block before recombining PC    PROVED
sign produced by the cancellation of that block               FALSE
preservation of an arithmetic scalar after recombining PC      FALSE

universally o-observed tail part                              FALSE
elimination of Tate by bilateral sum                          FALSE
control of R^Z via local collar data                          FALSE
sign of Q_delta on each component of xi                       FALSE
no-go for the current PC/Chebyshev/collar carrier              PROVED

REG and threshold trace for all contact vectors               OPEN
VIR--LB: V_Lambda|N <= 0                                     OPEN
VIR--DET: V_Lambda(G) >= c D_Delta(G)                        OPEN
load-bearing use of Lambda*1=log to prove VIR--LB             OPEN
complete control of tail/Tate/R^Z to prove VIR--DET            OPEN
computable quantifiers uniform in T for L and c_T             OPEN
VIR--EP implies R_LF=0                                      PROVED

D                                                               OPEN
```

The next piece is no longer another collar rewriting. It is to prove or
refute VIR--EP via a coefficient operation on the finite hyperbola that
survives as a window virial. If that operation is first recombined into
$K_N$, it falls back into the no-go of this document.
