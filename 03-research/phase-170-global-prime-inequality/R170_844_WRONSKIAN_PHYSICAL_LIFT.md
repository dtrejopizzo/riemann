# R170_844 — Physical lift of the Wronskian: full expansion, Fredholm obstruction and minimal covariant derivative

Continuation of R161_026, R161_028--029,
R161_069--070 and R170_841--843. Paper 46 is not modified.

## 0. Verdict

The static lift proposed in R170_843,

\[
 \Pi_TG_\delta\mathcal A_{N,N}^{\rm ren}\Pi_T
 =H_T\mathcal K
  +\mathcal B^{\rm pol}
  +\mathcal B^{\rm supp}
  +\mathcal B^{\rm Tate},
 \tag{0.1}
\]

does not derive VIR--LB. Before the sign obstruction there is a domain
obstruction: the interior Gamma observer \(G_\delta\) does not act on the
left polar layer for a small shift. Indeed,

\[
 K_{C_NF}(a)={N^{a+1/2}\over a+1/2}K_F(a).
 \tag{0.1a}
\]

Hence the renormalized expression of (0.1) is only typed with that same
observer if one imposes
\(\delta>\log N\), or if a different exterior observer is constructed.
The first option is useful for auditing the factorization; it does not
identify the small shift of the physical collar.

After that domain repair, there are two exact identities that close the
entire algebraic expansion.

First, if

\[
 \mathcal C_{\beta,N,T,\delta}
 :=\Pi_T\mathscr R_\delta^*D_{\beta,N}
             \mathscr R_\delta\Pi_T>0,
 \tag{0.2}
\]

is the R170_843 Wronskian detector and

\[
 \mathcal P_{N}^{\rm pol}
 :=\dot L_NC_N-L_N\dot C_N,
 \tag{0.3}
\]

then, as a form identity on the physical core and under
\(\delta>\log N\),

\[
 \boxed{
 \Pi_TG_\delta\mathcal A_{N,N}^{\rm ren}\Pi_T
 =-\mathcal C_{\beta,N,T,\delta}
  -\Pi_TG_\delta\mathcal P_N^{\rm pol}\Pi_T.}
 \tag{0.4}
\]

All the requested support and Tate blocks appear upon inserting
\(I=\Pi_T+(P_T-\Pi_T)+(I-P_T)\) between \(G_\delta\) and
\(\mathcal A^{\rm ren}\). But their sum returns exactly to (0.4): there
is no additional term left that can be identified with the virial.

Second, on pairing (0.1) with
\(F\in\ker H_T\), the factorization \(H_T\mathcal K\) disappears. If one
requires the three boundary blocks to sum to

\[
 -\mathcal V_{\Lambda,T}(F)
 -\mathscr E_{N;T,\delta}^{\beta}(F),
 \tag{0.5}
\]

(0.4) shows that the remaining condition is exactly

\[
 \boxed{
 \mathcal V_{\Lambda,T}(F)
 =\operatorname{Re}\langle\mathscr R_\delta F,
      \mathscr R_\delta\mathcal P_N^{\rm pol}F\rangle
 \quad(F\in\ker H_T).}
 \tag{0.6}
\]

(0.6) does not follow from PC, from the compression, nor from first
contact. Its left-hand side contains the Archimedean derivative and the
derivative of the primitive projection; the right-hand side is only the
observed polar Wronskian. In particular, the Tate virial
\(2\operatorname{Re}\langle F,tr_F'\rangle\) depends on
\(\dot\Pi_T\), while all the static blocks of (0.1) depend only on
\(\Pi_T\). Inserting Tate by hand into
\(\mathcal B^{\rm Tate}\) turns (0.6) into the desired statement, not
into a proof.

Moreover, the sign of that polar residue can be decided. After enlarging
the absolute cutoff \(N_0\) once, §3.1 proves

\[
 \operatorname{Re}\langle\mathscr R_\delta F,
      \mathscr R_\delta\mathcal P_N^{\rm pol}F\rangle>0
 \qquad(F\ne0).
 \tag{0.6a}
\]

Hence (0.6) would force
\(\mathcal V_{\Lambda,T}(F)>0\) on every nonzero vector of the radical:
this is the sign opposite to VIR--LB. The static lift with orientation
(0.5) is thereby refuted, not merely left pending.

A Fredholm no-go is also proved: a factorization of the form
\(\mathcal T=H_T\mathcal K+\mathcal B\) exists without a pseudoinverse
only after proving that
\(P_{\ker H_T}(\mathcal T-\mathcal B)=0\). For the choice (0.5), that
condition is precisely the polarization of (0.6). The formal construction
of \(\mathcal K\) uses
\(H_T^\dagger\), the forbidden inverse of the zero mode, and leaves the
radical component unresolved.

Therefore VIR--LB remains open. The minimal datum outside this static
class is determined: one must differentiate **covariantly** the
compressed renormalized PC,

\[
 {d\over dr}\bigl(\Pi_{rT}\mathfrak P_{N,N}^{\rm ren}(r)
                  \Pi_{rT}\bigr)\big|_{r=1},
 \tag{0.7}
\]

before taking the diagonal. (0.7) contains the two terms
\(\dot\Pi_T\), the bulk derived from PC, the synchronized tail \(k>N\),
the signed Wronskian and \(\dot C_N\). It is the first operation in the
chain that can simultaneously produce the Archimedean part, the prime
virial and Tate; the static lift (0.1) cannot do so.

## 1. Domains and quantifiers

Fix a hypothetical first window \(T>0\) and a parity sector. Let

\[
 \mathcal H_T=L^2(-T,T),\qquad
 \Pi=\Pi_T,\qquad P=P_T,
 \qquad R_T=P-\Pi,\qquad Q=I-P.
 \tag{1.1}
\]

The closed primitive form is denoted \(a_T\), its domain by
\(\mathcal Q_T\), and its self-adjoint operator by \(H_T\). Set

\[
 \mathsf N_T=\ker H_T,
 \qquad P_{\mathsf N}=P_{\ker H_T}.
 \tag{1.2}
\]

At a first window, \(0\) is an eigenvalue of finite multiplicity.
Identities involving derivatives of translations are first proved on

\[
 \mathcal D_T=C_c^\infty(-T,T)\cap\operatorname{Ran}\Pi
 \tag{1.3}
\]

and are then read as form identities when the right-hand side has a
continuous extension. It is not claimed that
\(\mathcal A^{\rm ren}\) is bounded on \(L^2\).

Let \(N_0\) be the absolute cutoff of R170_843 Theorem 5.1. Throughout
this document we choose

\[
 M=N\ge\max\{N_0,\lceil e^{2T}\rceil\}.
 \tag{1.4}
\]

This quantifier is uniform in \(T\). For \(m\ge1\), write

\[
 a_m=2m+1/2,\qquad s_m=2m+1,
 \tag{1.5}
\]

and, for an observation shift \(\delta>0\),

\[
 (\mathscr R_\delta F)_m
 =e^{-a_m(T+\delta)}K_F(a_m),
 \qquad
 G_\delta=\mathscr R_\delta^*\mathscr R_\delta.
 \tag{1.6}
\]

\(\mathscr R_\delta:\mathcal H_T\to\ell^2\) is Hilbert--Schmidt. To apply
it to the exterior output of a finite operator one uses the full Laplace
functional on the core, as in R161_070; its adjoint is only taken after
the second argument has returned to \(\mathcal H_T\). This distinction
avoids improperly identifying the interior observer with a bounded
operator on the whole exterior tail.

### 1.1. Polar domain gate

The explicit formula for \(C_N\) and Fubini give, for \(a>0\),

\[
\begin{aligned}
 K_{C_NF}(a)
 &=\int_{\mathbb R}e^{-(a+1/2)t}
     \int_{-\infty}^{t+\log N}e^{u/2}F(u)\,du\,dt\\
 &={N^{a+1/2}\over a+1/2}K_F(a).
\end{aligned}
 \tag{1.6a}
\]

The norm of the coordinate functional of
\(\mathscr R_\delta C_N\) on \(L^2(-T,T)\) is, up to a polynomial
constant in \(a_m\),

\[
 N^{a_m+1/2}e^{-a_m(T+\delta)}
 \left({\sinh(2a_mT)\over a_m}\right)^{1/2}
 \asymp
 {\sqrt N\,e^{-a_m(\delta-\log N)}\over a_m^{3/2}}.
 \tag{1.6b}
\]

Thus \(\mathscr R_\delta C_N\) is bounded if
\(\delta\ge\log N\), but is unbounded if
\(0<\delta<\log N\). The derivatives \(\dot C_N\), \(\dot L_N\) add
polynomial factors in \(a_m\); for the whole polar Wronskian we use the
safe condition

\[
 \boxed{\delta>\log N.}
 \tag{1.6c}
\]

This \(\delta\) is an auxiliary observation shift. It cannot be
identified with the infinitesimal width of the R170_840 window. With
\(0<\delta\ll1\) the expression
\(\Pi G_\delta\mathcal A^{\rm ren}\Pi\) is not defined by the interior
observer; only its raw part is.

Define

\[
 D_{\beta,N}
 =\operatorname{diag}_{m\ge1}
     \{a_mB_{N,N}(s_m)\}.
 \tag{1.7}
\]

By R170_843,

\[
 D_{\beta,N}>0,
 \qquad
 \mathscr E_{N;T,\delta}^\beta(F)
 =\langle\mathscr R_\delta F,
          D_{\beta,N}\mathscr R_\delta F\rangle>0
 \quad(F\ne0).
 \tag{1.8}
\]

## 2. Exact identity for the complete output

Recall

\[
\begin{aligned}
 \mathcal A_{N,N}^{\rm raw}
   &=\dot L_NS_N-L_N\dot S_N,\\
 \mathcal A_{N,N}^{\rm ren}
   &=\dot L_NZ_N-L_N\dot Z_N\\
   &=\mathcal A_{N,N}^{\rm raw}
     -\mathcal P_N^{\rm pol},
\end{aligned}
 \tag{2.1}
\]

with \(Z_N=S_N-C_N\) and \(\mathcal P_N^{\rm pol}\) given by (0.3).

R170_843 (5.4) proves, for every source in the core,

\[
 \boxed{
 \mathscr R_\delta\mathcal A_{N,N}^{\rm raw}F
 =-D_{\beta,N}\mathscr R_\delta F.}
 \tag{2.2}
\]

Multiplying (2.2) on the left by
\(\Pi\mathscr R_\delta^*\) and restricting the argument with
\(\Pi\) gives

\[
 \boxed{
 \Pi G_\delta\mathcal A_{N,N}^{\rm raw}\Pi
 =-\mathcal C_{\beta,N,T,\delta},}
 \tag{2.3}
\]

where \(\mathcal C_\beta\) is (0.2). The raw identity (2.3) holds for
every \(\delta>0\). Under gate (1.6c), subtracting the polar piece of
(2.1) proves (0.4):

\[
 \boxed{
 \Pi G_\delta\mathcal A_{N,N}^{\rm ren}\Pi
 =-\mathcal C_{\beta,N,T,\delta}
  -\Pi G_\delta(\dot L_NC_N-L_N\dot C_N)\Pi.}
 \tag{2.4}
\]

The output of \(\mathcal A\) has not been compressed before observing
it. That is why (2.4) coherently contains all of \(k>N\) and does not yet
have a support concomitant.

On the diagonal, for \(F\in\mathcal D_T\) and \(\delta>\log N\),

\[
\boxed{
\begin{aligned}
 \operatorname{Re}\langle F,
      \Pi G_\delta\mathcal A_{N,N}^{\rm ren}\Pi F\rangle
 ={}&-\mathscr E_{N;T,\delta}^\beta(F)\\
 &-\operatorname{Re}\langle\mathscr R_\delta F,
      \mathscr R_\delta(\dot L_NC_N-L_N\dot C_N)F\rangle.
\end{aligned}}
 \tag{2.5}
\]

(2.5) is the complete value of the left-hand side of (0.1). Any
support/Tate decomposition must again sum to that scalar.

## 3. Computation of polar, support and Tate

### 3.1. Polar

With the dilation convention of R170_841,

\[
\begin{aligned}
 \dot C_Nf(t)={}&(1-t/2)C_Nf(t)
 +e^{-t/2}\int_{-\infty}^{t+\log N}
       {v\over2}e^{v/2}f(v)\,dv\\
 &-(\log N)\sqrt N\,f(t+\log N).
\end{aligned}
 \tag{3.1}
\]

Hence the computed polar block, without ellipses, is the form

\[
\boxed{
 \mathfrak p_{N,T,\delta}(F,G)
 :=\langle\mathscr R_\delta F,
     \mathscr R_\delta(\dot L_NC_N-L_N\dot C_N)G\rangle.}
 \tag{3.2}
\]

Inserting (3.1) in (3.2) gives three terms: the multiple of
\(C_N\), the truncated moment weighted by \(v\), and the face
\(f(t+\log N)\). None has a sign. The real diagonal value is the second
line of (2.5).

The Laplace transform allows recombining those three terms without losing
any. Set \(s=a+1/2\) and

\[
 c_N(s):={N^s\over s},
 \qquad
 \ell_N(s):=\sum_{d\le N}{\Lambda(d)\over d^s}.
 \tag{3.2a}
\]

From (1.6a), \(K_{C_NF}(a)=c_N(s)K_F(a)\). In (3.1), the two terms
containing \(K_F'(a)\) cancel exactly, and one is left with

\[
 \boxed{
 K_{\dot C_NF}(a)
 =c_N(s)\left(1-{1\over2s}-a\log N\right)K_F(a).}
 \tag{3.2b}
\]

Since
\(K_{\dot L_NF}(a)=a\ell_N'(s)K_F(a)\), the polar Wronskian has the
explicit real symbol

\[
\boxed{
\begin{aligned}
 K_{\mathcal P_N^{\rm pol}F}(a)
 &=\pi_N(s)K_F(a),\\
 \pi_N(s)
 &:=c_N(s)\left[
      a\ell_N'(s)
      -\ell_N(s)\left(1-{1\over2s}-a\log N\right)
                \right].
\end{aligned}}
 \tag{3.2c}
\]

Thus, under gate (1.6c),

\[
 \operatorname{Re}\mathfrak p_{N,T,\delta}(F,F)
 =\sum_{m\ge1}\pi_N(s_m)e^{-2a_m(T+\delta)}
       |K_F(a_m)|^2.
 \tag{3.2d}
\]

The sign of \(\pi_N\) is obtained uniformly after enlarging the absolute
cutoff. Define

\[
 \mu_N(s):=-{\ell_N'(s)\over\ell_N(s)},
 \qquad
 M_3:=-{\ell_\infty'(3)\over\ell_\infty(3)}<\infty.
 \tag{3.2e}
\]

\(\mu_N(s)\) is the mean of \(\log d\) for the weights
\(\Lambda(d)d^{-s}\), \(d\le N\). Adding the tail \(d>N\), whose
\(\log d\) values are larger than those of the initial block, can only
increase the mean; moreover
\(\mu_\infty'(s)=-\operatorname{Var}_s(\log d)\le0\). Hence

\[
 \mu_N(s)\le\mu_\infty(s)\le M_3
 \qquad(s\ge3).
 \tag{3.2f}
\]

Replace, without changing notation,

\[
 N_0\leftarrow
 \max\{N_0,\lceil e^{M_3+1}\rceil\}.
 \tag{3.2g}
\]

Since \(a=s-1/2\), (3.2c) rewrites as

\[
 \pi_N(s)
 =c_N(s)\ell_N(s)
   \left[a(\log N-\mu_N(s))-1+{1\over2s}\right]>0
 \qquad(s\ge3,N\ge N_0).
 \tag{3.2h}
\]

All the coefficients of (3.2d) are then strictly positive. Completeness
of the Gamma moments gives

\[
 \boxed{
 \operatorname{Re}\mathfrak p_{N,T,\delta}(F,F)>0
 \quad(F\ne0,\ \delta>\log N).}
 \tag{3.2i}
\]

This is the exact polar residue that survives. Its sign is opposite to
the one that would be needed to turn (5.4) into VIR--LB.

R161_028 uses a different move, \(a=\log N\), and proves
\(\partial_aC_a=e^{a/2}\tau_a\). That cutoff speed must not be confused
with (3.1), which differentiates the coordinated dilation. Both are
explicit, but only (3.1) belongs to the R170_841 scale virial.

### 3.2. Support

Insert \(I=P+Q\) in the output:

\[
\begin{aligned}
 \Pi G_\delta\mathcal A^{\rm ren}\Pi
 ={}&\Pi G_\delta P\mathcal A^{\rm ren}\Pi
    +\Pi G_\delta Q\mathcal A^{\rm ren}\Pi.
\end{aligned}
 \tag{3.3}
\]

The second summand is the exterior port. To exhibit its two
orientations, use

\[
 [P,Z_N]=PZ_NQ-QZ_NP,
 \qquad
 [P,\dot Z_N]=P\dot Z_NQ-Q\dot Z_NP.
 \tag{3.4}
\]

An expansion without commuting factors gives

\[
\boxed{
\begin{aligned}
 Q\mathcal A^{\rm ren}\Pi
 ={}&-[P,\dot L_N]PZ_N\Pi
     -Q\dot L_NQ[P,Z_N]\Pi\\
    &+[P,L_N]P\dot Z_N\Pi
     +QL_NQ[P,\dot Z_N]\Pi.
\end{aligned}}
 \tag{3.5}
\]

In (3.5), \(-QZ_NP\) and \(-Q\dot Z_NP\) are the branches acting on
\(\Pi\). Taking the Hermitian part of (3.3), their adjoints produce the
opposite branches \(PZ_N^*Q\) and \(P\dot Z_N^*Q\). Equivalently, before
taking the diagonal the two blocks of (3.4) remain; neither has been
declared zero.

Define, therefore,

\[
 \mathfrak b_{N,T,\delta}^{\rm supp}(F,G)
 :=\langle\mathscr R_\delta F,
          \mathscr R_\delta Q
             \mathcal A_{N,N}^{\rm ren}\Pi G\rangle.
 \tag{3.6}
\]

(3.5) is its explicit expansion in
\([P,Z_N]\), \([P,\dot Z_N]\), \([P,L_N]\) and
\([P,\dot L_N]\). This is exactly the physical concomitant of
R161_057--065, now with the Wronskian coefficients.

### 3.3. Tate

Inside the window, insert \(P=\Pi+R_T\):

\[
\begin{aligned}
 \Pi G_\delta P\mathcal A^{\rm ren}\Pi
 ={}&\Pi G_\delta\Pi\mathcal A^{\rm ren}\Pi
    +\Pi G_\delta R_T\mathcal A^{\rm ren}\Pi.
\end{aligned}
 \tag{3.7}
\]

The static Tate port is

\[
 \mathfrak b_{N,T,\delta}^{\rm Tate,stat}(F,G)
 :=\langle\mathscr R_\delta F,
          \mathscr R_\delta R_T
             \mathcal A_{N,N}^{\rm ren}\Pi G\rangle.
 \tag{3.8}
\]

It is not the Tate virial. The latter is

\[
 \mathfrak T_T(F)
 =2\operatorname{Re}\langle F,tr_F'\rangle
 \tag{3.9}
\]

and is born from differentiating the primitive condition, i.e. from
\(\dot\Pi_T\). R161_063 already proves the same type distinction for a
compressed power: \(R_TZF\) is not the cross Tate collar. The same
happens here with \(R_T\mathcal A^{\rm ren}F\).

### 3.4. The sum of the blocks is an exact tautology

From (3.3) and (3.7),

\[
\begin{aligned}
 \langle F,\Pi G_\delta\mathcal A^{\rm ren}\Pi G\rangle
 ={}&\langle\mathscr R_\delta F,
       \mathscr R_\delta\Pi\mathcal A^{\rm ren}\Pi G\rangle\\
 &+\mathfrak b^{\rm Tate,stat}_{N,T,\delta}(F,G)
  +\mathfrak b^{\rm supp}_{N,T,\delta}(F,G).
\end{aligned}
 \tag{3.10}
\]

The first line plus the two ports returns to the left-hand side of (2.4).
Adding (3.2) separates raw and renormalized, but likewise creates no new
scalar. Hence the computed blocks cannot, by pure expansion, sum to
anything other than (2.5).

## 4. The synchronized tail \(k>N\)

The antisymmetric channel keeps in \(B_{N,N}(s)\) the sum

\[
 \sum_{N<k\le N^2}{\beta_{N,N}(k)\over k^s}.
 \tag{4.1}
\]

The synchronized channel is independent and also does not disappear.
R170_841 proves

\[
 \dot H_{N,N}^{\Lambda,\rm raw}
 =-\sum_{N<k\le N^2}{h_{N,N}(k)\log k\over\sqrt k}
      \partial_t\tau_{\log k},
 \qquad h_{N,N}(k)\ge0.
 \tag{4.2}
\]

Define

\[
 \Theta_N(s)
 :=\sum_{N<k\le N^2}{h_{N,N}(k)\log k\over k^s}\ge0.
 \tag{4.3}
\]

The same Laplace observation gives

\[
 K_{\dot H_{N,N}^{\Lambda,\rm raw}F}(a)
 =-a\Theta_N(a+1/2)K_F(a).
 \tag{4.4}
\]

Thus the tail \(k>N\) is another multiplier with a known sign in the
observer, not a discarded term.

The master renormalized decomposition is

\[
 2\dot L_NZ_N
 =\dot{\widetilde H}_{N,N}+\dot K_N^Z
  +\mathcal A_{N,N}^{\rm ren}.
 \tag{4.5}
\]

Substituting (2.4) and (4.4) into the observation of (4.5) orients the
two arithmetic channels, but leaves \(\dot K_N^Z\), the polar pieces of
\(\dot{\widetilde H}\) and the ports of (3.5)--(3.9). In particular,
(4.5) by itself does not identify \(2\dot L_NZ_N\) with the derivative
of the compressed Weil form.

For a weight \(a\ne\Lambda\), (4.2) additionally acquires the block
under

\[
 -\sum_{k\le N}{\delta_a(k)\log k\over\sqrt k}
       \partial_t\tau_{\log k},
 \qquad
 \delta_a(k)=\sum_{d\mid k}a(d)-\log k.
 \tag{4.6}
\]

Its Laplace symbol has no sign. (4.6) is the exact line where the
construction fails for altered weights and for Davenport--Heilbronn with
the ordinary comb. The Wronskian positivity on the Gamma lattice, which
by itself can survive for many positive weights, does not eliminate
(4.6).

## 5. Exact comparison with the virial

Under (REG), the virial form polarized on \(\mathsf N_T\) is

\[
\begin{aligned}
 \mathcal V_{\Lambda,T}(F)
 ={}&{1\over2\pi}\int_{\mathbb R}
       \tau m'(\tau)|\widehat F(\tau)|^2\,d\tau\\
 &-\sum_{n<e^{2T}}{2\Lambda(n)\over\sqrt n}
       \log n\,c_F'(\log n)
 +2\operatorname{Re}\langle F,tr_F'\rangle.
\end{aligned}
 \tag{5.1}
\]

The first line of (5.1) is the derivative of the Archimedean
multiplier. The last is the connection of the primitive projection.
Neither is contained in the static expansion (3.10).

Suppose now that (0.1) has been constructed with correct domains and
that, on the radical, its physical blocks satisfy the required value
(0.5). By radicality,

\[
 a_T(F,\mathcal KF)=0.
 \tag{5.2}
\]

By (2.5), the left-hand side of (0.1) is

\[
 -\mathscr E_{N;T,\delta}^{\beta}(F)
 -\operatorname{Re}\mathfrak p_{N,T,\delta}(F,F).
 \tag{5.3}
\]

Comparing (0.5) and (5.3) cancels the Wronskian energy on both sides and
leaves exactly (0.6):

\[
 \boxed{
 \mathcal V_{\Lambda,T}(F)
 =\operatorname{Re}\mathfrak p_{N,T,\delta}(F,F).}
 \tag{5.4}
\]

Thus the requested lift does not reduce the sign to a sum of squares: it
reduces it to the new identity (5.4). The support and static Tate blocks
cannot change that conclusion, since they are already contained in the
exact recombination (3.10). By (3.2i), (5.4) would imply

\[
 \boxed{
 \mathcal V_{\Lambda,T}(F)>0
 \qquad(0\ne F\in\mathsf N_T),}
 \tag{5.5}
\]

which contradicts the inequality \(\mathcal V_{\Lambda,T}\le0\) that the
lift was meant to prove. The static orientation (0.5) is, therefore,
impossible at a hypothetical first window with nontrivial radical.

### 5.1. Incompatibility of first-order data

Consider two differentiable paths of primitive projections
\(\Pi(r)\) that coincide at \(r=1\) but have different derivatives.
All the static objects of (2.4) and (3.2)--(3.10) coincide at
\(r=1\). The connection term of the dilated form changes with
\(\dot\Pi(1)\), and with it (3.9) changes. Thus no functional built only
from

\[
 \Pi(1),\ P,\ Z_N,\ \dot Z_N,\ G_\delta,
 \ \mathcal A^{\rm ren}(1)
 \tag{5.6}
\]

determines the Tate virial. The projection must be differentiated as part
of the identity, not added after compression.

The same problem appears in the Archimedean part: (2.4) contains the
derivative of the two arithmetic legs, but not the derivative of the
multiplier \(m(\tau)\) of (5.1). That enters when differentiating the
full Weil form, or PC with its Fourier orientation.

## 6. Fredholm no-go for the static factorization

The obstruction can be expressed without appealing to domain intuition.

**Theorem 6.1 (first-contact factorization criterion).** Let
\(H=H^*\) be the operator of a closed form with isolated \(0\) and
finite kernel \(\mathsf N\). Let \(\mathcal T\) and \(\mathcal B\) be
continuous sesquilinear forms on a common core. If there exists an
admissible map \(\mathcal K\) such that

\[
 \mathcal T=H\mathcal K+\mathcal B
 \tag{6.1}
\]

in the weak sense, then necessarily

\[
 \boxed{
 P_{\mathsf N}(\mathcal T-\mathcal B)=0.}
 \tag{6.2}
\]

Conversely, under the closed-range condition and the corresponding
domains, the minimal solution on \(\mathsf N^\perp\) is

\[
 \mathcal K
 =H^\dagger(\mathcal T-\mathcal B),
 \tag{6.3}
\]

where \(H^\dagger\) is the pseudoinverse that vanishes on
\(\mathsf N\).

*Proof.* If \(F\in\mathsf N\), then
\(\langle F,H\mathcal KG\rangle
=\langle HF,\mathcal KG\rangle=0\) for every \(G\), which gives
(6.2). On \(\mathsf N^\perp\), \(H\) is invertible on its range; the
minimal orthogonal solution is (6.3). \(\square\)

Apply the theorem with

\[
 \mathcal T=\Pi G_\delta\mathcal A^{\rm ren}\Pi,
 \qquad
 \mathcal B\big|_{\mathsf N}
 =-\mathcal V_{\Lambda,T}-\mathcal C_{\beta,N,T,\delta}.
 \tag{6.4}
\]

Then (6.2), after polarizing, is exactly (5.4) on all of
\(\mathsf N_T\). Therefore:

\[
 \boxed{
 \text{building (0.1) statically}
 \iff
 \text{first proving the radical orthogonality (5.4),}
 }
 \tag{6.5}
\]

unless the pseudoinverse (6.3) is used. Using it would be precisely
inverting the zero mode and is excluded by the statement of the goal.

This result sharpens R161_069--070. It does not claim that an arithmetic
comparison with \(H_T\) is impossible. It claims that the static
comparison of the concrete form (0.1) cannot be built by formal
factorization: its solvability condition is the very radical scalar one
wanted to derive.

## 7. Dependence on \(\delta\) and on the cutoff

The virial (5.1) does not depend on the auxiliary shift \(\delta\). By
contrast, for each \(F\),

\[
 \operatorname{Re}\mathfrak p_{N,T,\delta}(F,F)
 =\sum_{m\ge1}e^{-2a_m(T+\delta)}
    \pi_N(s_m)|K_F(a_m)|^2
 \tag{7.1}
\]

on the core, with normal convergence for \(\delta>0\). Hence it tends to
zero as \(\delta\to\infty\). A family of lifts claiming (5.4) for every
\(\delta>0\) would force

\[
 \mathcal V_{\Lambda,T}(F)=0
 \quad(F\in\mathsf N_T),
 \tag{7.2}
\]

and then, by uniqueness of exponential series, the vanishing of all the
coefficients of (7.1). This is much stronger than an observation identity
at a single fixed \(\delta\). Hence \(\delta\) cannot be left as a free
parameter in a supposed lift; a physical choice would have to be derived
from PC.

The uniform cutoff (1.4) is indeed legitimate for the sign of
\(D_{\beta,N}\). But (5.4) also cannot be demanded for every
\(N\ge\max\{N_0,\lceil e^{2T}\rceil\}\) without proving a stabilization
law for its polar side. R161_070 shows the opposite phenomenon: the
inactive indices disappear from the interior operator and live entirely
in the collar. Varying \(N\) changes the ports even though the compressed
operator has stabilized.

## 8. The minimal operation outside the static class

The information missing in (5.5) is exactly the derivative of the
compression. Let \(\mathfrak P_{N,N}^{\rm ren}(r)\) be the renormalized
PC identity transported to the fixed window via \(U_r\). The next
operation must be

\[
\boxed{
 \nabla^{\rm PC}_{T,N}
 :=\left.{d\over dr}\right|_{r=1}
   \bigl(\Pi_{rT}\mathfrak P_{N,N}^{\rm ren}(r)
                    \Pi_{rT}\bigr).}
 \tag{8.1}
\]

The product rule forces three terms:

\[
\begin{aligned}
 \nabla^{\rm PC}_{T,N}
 ={}&\dot\Pi_T\mathfrak P_{N,N}^{\rm ren}\Pi_T
    +\Pi_T\dot{\mathfrak P}_{N,N}^{\rm ren}\Pi_T\\
   &+\Pi_T\mathfrak P_{N,N}^{\rm ren}\dot\Pi_T.
\end{aligned}
 \tag{8.2}
\]

The two outer terms of (8.2) are the only correct origin of (3.9). The
central term contains, before recombining:

1. the synchronized tail (4.2)--(4.4), which uses
   \(\delta_\Lambda=0\);
2. the Wronskian (2.2), whose sign uses
   \(B_\Lambda(s)>0\);
3. \(\dot C_N\) of (3.1);
4. the two support blocks of (3.4)--(3.5);
5. the derivative of the Fourier orientation, which contributes the
   Archimedean multiplier of (5.1).

Thus (8.1) jointly uses the two required arithmetic inputs and contains
the form data missing in (0.1). It is not a static factorization by
\(H_T\) and does not require \(H_T^\dagger\).

The following load-bearing lemma is reduced to a precise computation:

> **Covariant Ward--PC.** Prove in the form domain that the diagonal of
> (8.2), after the Hankel polarization of the two legs and before
> recombining the hyperbola, equals
> \(-\mathcal V_{\Lambda,T}(F)\) minus the sum of
> \(\mathscr E_{N;T,\delta}^{\beta}(F)\) and the nonnegative energy of
> the synchronized tail (4.4), with the ports (3.2), (3.6) and (3.8)
> cancelled by the two \(\dot\Pi_T\) terms.

This lemma has not been proved here. Unlike (0.1), it is not a static
reformulation: (8.2) contains two new, determined operators,
\(\dot\Pi_T\) and the Fourier derivative of PC, absent from the no-go of
Theorem 6.1.

## 9. Status

```text
domain of the interior/exterior observer                        TYPED
uniform sign D_beta,N for N>=max(N0,ceil(e^(2T)))               INHERITED
full output identity Pi G A_raw Pi=-C_beta                      PROVED
exact renormalized lift with dot C_N, equation (2.4)             PROVED

explicit polar block                                             COMPUTED
PZ_NQ / QZ_NP and their derivatives                              KEPT
exterior support port, equation (3.5)                            COMPUTED
static Tate port R_T A Pi                                        COMPUTED
identification of that port with the Tate virial                 FALSE IN TYPE

antisymmetric tail k>N                                           KEPT
synchronized tail k>N and its positive symbol                    PROVED
defect under delta_a != 0 / DH with ordinary comb                PROVED

necessary condition of the lift: V=Re p_pol on the radical       PROVED
static factorization without inverting the zero mode             BLOCKED BY FREDHOLM
use of H_T^dagger                                                FORBIDDEN / CIRCULAR
VIR--LB                                                          OPEN

covariant derivative of PC with dot Pi, equation (8.2)           FORMALLY BUILT
covariant Ward--PC and signed cancellation of all ports          OPEN
complete bilateral law                                           OPEN
D                                                                OPEN
```

The correct continuation must not attempt another decomposition of
\(\Pi G_\delta\mathcal A\Pi\): (2.4) already gives its complete value
and Theorem 6.1 closes the class of static factorizations. It must
compute the covariant derivative (8.2) on the core, with the Fourier
orientation and the two \(\dot\Pi_T\) terms present from the start.
