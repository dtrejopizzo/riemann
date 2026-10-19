# R170_854 — Graded Green law for the exterior Wronskian

## 0. Result and verdict

This record directly attacks the open law R170_853 (5.1), before
recombining the two orientations. In the real parity sector an
exact Green identity is obtained.

Let `P=P_T`, `Q=I-P`, `S=S_N`, `A=A_M` and

\[
 C:=PS^*P,\qquad h:=C^{-1}b,\qquad
 q:=QS^*Ph,                                                    \tag{0.1}
\]

where `b=b_epsilon` is the Tate column of the fixed parity. For a
first-contact vector write

\[
 PAF=\rho b,\qquad \ell:=QAF,\qquad z:=\ell-\rho q.           \tag{0.2}
\]

Keeping `P,h,F,rho` fixed while differentiating, set

\[
 \begin{aligned}
  \dot b^{0}&:=P\dot S^*Ph,&
  \dot q^{0}&:=Q\dot S^*Ph,\\
  \dot a^{0}&:=P\dot AF,&
  \dot\ell^{0}&:=Q\dot AF,\\
  \dot z^{0}&:=\dot\ell^{0}-\rho\dot q^{0}.
 \end{aligned}                                                \tag{0.3}
\]

Use the real product `(u,v)=Re <u,v>`. Then

\[
 \boxed{
 (h,P(S\dot A-\dot S A)F)
 +\bigl((\dot q^{0},z)-(q,\dot z^{0})\bigr)
 =(b,\dot a^{0})-\rho(\dot b^{0},b).}                    \tag{0.4}
\]

In particular, the open law R170_853 (5.1) is exactly equivalent to

\[
 \boxed{
 (h,P(S\dot A-\dot S A)F)
 =(b,P\dot AF)-\rho(P\dot S^*Ph,b).}                         \tag{0.5}
\]

Identity (0.4) is the correctly typed exterior polarization of the
PC curvature. It does not assume exterior reciprocity and does not use
an inverse of the Weil operator.

There is also an independent but compatible arithmetic advance. The
second Chebyshev jet that necessarily appears in the antidiagonal
derivative of PC completes the Wronskian extracted by Möbius:

\[
 -M\mathcal A_\Lambda^{\rm raw}+M K^{(2,\partial)}
 =-2\dot L.                                                   \tag{0.6}
\]

Thus the exact weight `2 Lambda(n) log n` of the prime virial is
already inside the same differentiated identity; Selberg is not added
from outside.
R170_855 develops this coefficient assembly separately.

The terminal sign, however, does not follow from (0.4). First-contact
minimality controls the physical diagonal of the virial on `F`; it
does not control the cross pairing with the causal dual `h`. Therefore
R170_853 (5.1), VIR--LB and D remain open.

## 1. The exterior antidiagonal polarization

Introduce two independent scales, with frozen gauge,

\[
 \begin{aligned}
 q_r&:=QS_N(r)^*Ph,\\
 \ell_s&:=QA_M(s)F,\\
 z_s&:=\ell_s-\rho q_s,
 \end{aligned}                                               \tag{1.1}
\]

and the mixed form

\[
 \mathscr B(r,s):=(q_r,z_s).                                 \tag{1.2}
\]

The antidiagonal derivation literally gives

\[
 \boxed{
 (\partial_r-\partial_s)\mathscr B(r,s)|_{1,1}
 = (\dot q^{0},z)-(q,\dot z^{0}).}                       \tag{1.3}
\]

No derivative of `rho` appears: this is exactly the frozen-velocity
convention of R170_853. A gauge in which `rho` moves adds the
corresponding term and must declare it.

Since the real product is symmetric,

\[
 (\dot q^{0},z)-(q,\dot z^{0})
 =(\dot q^{0},\ell)-(q,\dot\ell^{0});                    \tag{1.4}
\]

the two terms proportional to `rho` cancel. Therefore the mismatch
`z` was not annulled: its antisymmetric current has simply been
isolated, and it coincides with the current of the full outputs
`q` and `ell`.

## 2. Graded Green theorem

### Theorem 2.1

With definitions (0.1)--(0.3), on the common core,

\[
 \boxed{
 \begin{aligned}
 &(S^*Ph,\dot AF)-(\dot S^*Ph,AF)\\
 &\quad=(b,\dot a^{0})-(\dot b^{0},\rho b)
       +(q,\dot\ell^{0})-(\dot q^{0},\ell).
 \end{aligned}}                                             \tag{2.1}
\]

Moreover,

\[
 (S^*Ph,\dot AF)-(\dot S^*Ph,AF)
 =(h,P(S\dot A-\dot S A)F).                                 \tag{2.2}
\]

Consequently (0.4) holds.

### Proof

Insert `I=P+Q` simultaneously in the two pairings on the left-hand
side of (2.1). The orthogonality of `P` and `Q` gives

\[
 \begin{aligned}
 (S^*Ph,\dot AF)
   &=(b,\dot a^{0})+(q,\dot\ell^{0}),\\
 (\dot S^*Ph,AF)
   &=(\dot b^{0},\rho b)+(\dot q^{0},\ell),
 \end{aligned}                                               \tag{2.3}
\]

because `PS^*Ph=b` and `PAF=rho b`. This proves (2.1). Moving the
adjoints in the real product proves (2.2). Finally use (1.4) and
rearrange. No sign condition or asymptotic identity has been used. QED.

The shortest form of the law is

\[
 \boxed{
 \mathfrak W_{\rm bulk}
 +\mathfrak W_{\rm ext}=\mathfrak W_{\rm Tate},}             \tag{2.4}
\]

with

\[
 \begin{aligned}
 \mathfrak W_{\rm bulk}
   &:=(h,P(S\dot A-\dot S A)F),\\
 \mathfrak W_{\rm ext}
   &:=(\dot q^{0},z)-(q,\dot z^{0}),\\
 \mathfrak W_{\rm Tate}
   &:=(b,P\dot AF)-\rho(P\dot S^*Ph,b).
 \end{aligned}                                               \tag{2.5}
\]

Thus the residue of R170_853 is not an extra port: it is exactly the
exterior part of a single Green current whose bulk is the physical
curvature of R170_848--849.

## 3. The double sector producing the orientation sign

The operation above has a `Z/2`-graded realization. For the two
arithmetic legs define

\[
 \mathbb D_{L,S}:=
 \begin{pmatrix}0&L\\ S&0\end{pmatrix},\qquad
 \dot{\mathbb D}_{L,S}:=
 \begin{pmatrix}0&\dot L\\ \dot S&0\end{pmatrix},\qquad
 \Gamma:=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.            \tag{3.1}
\]

Since the causal operators commute on the line,

\[
 \boxed{
 [\dot{\mathbb D}_{L,S},\mathbb D_{L,S}]
 =\Gamma\,\mathcal A_{M,N}^{\rm raw},\qquad
 \mathcal A_{M,N}^{\rm raw}=\dot L S-L\dot S.}              \tag{3.2}
\]

The anticommutator, on the other hand, contains the synchronized jet
`dot L S+L dot S`. That is why the correct operation is the **ordinary
commutator of two odd operators**; the supercommutator of these same
operators would give the sum and would return to the synchronized
channel.

For the physical pair use

\[
 \mathbb D_{S,A}:=
 \begin{pmatrix}0&S^*\\ A&0\end{pmatrix}.                   \tag{3.3}
\]

The decomposition of its commutator current by
`P_gr=diag(P,P)` and `Q_gr=I-P_gr` is precisely (2.1):
the `P_gr` block is `W_Tate` and the `Q_gr` block is
`-W_ext`. This gives a pre-recombination construction and preserves
both orientations until the end.

Grading does not create positivity by itself. Indeed, for arbitrary
real vectors,

\[
 \begin{aligned}
 4\bigl((\dot q,z)-(q,\dot z)\bigr)
 ={}&\|\dot q+z\|^2-\|\dot q-z\|^2\\
    &-\|q+\dot z\|^2+\|q-\dot z\|^2.                       \tag{3.4}
 \end{aligned}

Every exact quadratic representation of the current therefore
preserves an indefinite metric. Replacing (3.4) by a sum of positive
squares loses the orientation one is trying to prove.

## 4. The second PC jet completes the prime virial

R170_847 proves

\[
 \partial_-K_N(r,q)=2K_N+K_N^{(2,\partial)},\qquad
 K_N^{(2,\partial)}
 =\sum_{n\le N}{(\log n)^2\over\sqrt n}
       \partial_t\tau_{\log n}.                             \tag{4.1}
\]

Let the causal Möbius comb be

\[
 M=\sum_{d\ge1}{\mu(d)\over\sqrt d}\tau_{\log d}.           \tag{4.2}
\]

On every complete fiber,

\[
 MK_N^{(2,\partial)}
 =\sum_k{W(k)\over\sqrt k}\partial_t\tau_{\log k},
 \qquad W=\mu*\log^2.                                      \tag{4.3}
\]

By R170_850,

\[
 M\mathcal A_\Lambda^{\rm raw}
 =-\sum_k{\gamma_\Lambda(k)\over\sqrt k}
        \partial_t\tau_{\log k},\qquad
 \gamma_\Lambda=\Lambda\log-\Lambda*\Lambda.              \tag{4.4}
\]

The Selberg identity gives

\[
 W=\Lambda\log+\Lambda*\Lambda.                            \tag{4.5}
\]

Consequently,

\[
 \boxed{
 -M\mathcal A_\Lambda^{\rm raw}+MK_N^{(2,\partial)}
 =2\sum_k{\Lambda(k)\log k\over\sqrt k}
        \partial_t\tau_{\log k}
 =-2\dot L.}                                                \tag{4.6}
\]

The signs in (4.6) are the signs that appear in the causal branch
of the differentiated PC: from `-H` is born
`-mathcal A_raw+2K+K2`. The zero-order term `2MK=2L` must
cancel against the jet of `X_r`; that cancellation and the routes
crossing the cut are not stated here.

R170_851 remains correct in asserting that the synchronized tail
`dot H` does not contain `W` for `k<=N`. What must be corrected is a
broader reading: the interior `W` is indeed present in PC, but in the
second antidiagonal jet `K2`, not in `dot H`. This avoids introducing
Selberg positivity as an auxiliary inequality. It still does not give
a sign to the physical pairing of (2.5).

The arithmetic specificity is literal. For a general weight `a`, if
`D a(n)=a(n)log n`, then

\[
 \mu*\beta_a=D a-(\mu*a)*D1.                                \tag{4.7}
\]

Only for `a=Lambda=mu*D1` does the Selberg identity turn (4.7)
together with (4.3) into `2D Lambda`. Thus this line uses unique
factorization, the comb of all integers, and the exact values of
`Lambda`.

## 5. What minimality contributes and what it does not

First contact is used in (0.2): the complete weak equation gives
`PAF=rho b`. This reduces the entire non-primitive interior part to
the scalar `rho` and makes (0.4) a finite, explicit identity.

The available dynamical minimality gives a sign for the diagonal
derivative of the form on the selected vector `F`. It does not imply

\[
 (b,P\dot AF)=\rho(P\dot S^*Ph,b),                           \tag{5.1}
\]

nor does it control

\[
 (h,P(S\dot A-\dot S A)F).                                  \tag{5.2}
\]

The test vectors `h` and `b` are not the minimizing vector `F`; `h`
is the causal dual fixed by the integer comb. Formally differentiating
`PAF=rho b` to obtain (5.1) would assume the existence of a vector
branch that remains in the radical, and would be exactly the
tangency that VIR--LB is trying to prove.

Thus (0.5) is a strict and falsifiable reduction of R170_853 (5.1),
but not an already-proved consequence of minimality.

## 6. Audit against the exhausted routes

### 6.1. Mixed `E--C`

R161_041 proves that the Poisson difference has the mean jet and that
the complementary sum has the critical jet. R161_057--064 show that
their mixed pairing leaves a support concomitant. Law (2.4) is a
concrete realization of that same class in the dual coordinates
`(h,F)`: it identifies the remaining concomitant exactly with
`W_ext`. It therefore does not evade the mixed `E--C` no-go; it
types it and reduces it to (0.5).

### 6.2. Selberg and deconvolution

Using `W>=0` after pairing returns to the R162_501 no-go. The only
admissible novelty is (4.6): `W` arrives with a fixed sign from `K2`
inside the same PC and algebraically cancels `Lambda*Lambda` before
pairing. This recovers the prime virial, but does not sign the
boundary.

### 6.3. Ratio-comb

The graded commutator (3.2) is linear and does not manufacture
Hermitian products `V*V`; hence it does not contain the ratio-comb of
R166_502. If one tries to obtain positivity by squaring the graded
sector, there are two possibilities:

1. with the positive Hilbert metric, the Hermitian squares reappear
   together with their ratio-comb;
2. with the supertrace the two squares cancel with opposite sign, but
   the form remains indefinite as in (3.4).

Thus grading avoids the ratio-comb only as long as it is kept as a
linear current; it does not by itself supply positive energy.

### 6.4. Two-prime complex

P122_028 constructs a positive Dirichlet--to--Neumann energy whose
vanishing is equivalent to equality of the traces of two primes, but
also proves that the known minimality does not force zero flow. Law
(2.4) is a symplectic current, not that energy. Turning it into a
positive energy would require precisely a zero-flow law; citing
P122_028 does not prove (0.5).

## 7. Remaining gate

After (0.4) and (4.6), a valid continuation must prove, in the full
PC expansion and at finite cutoff, the following three claims:

1. `2MK` cancels against the jet of `X_r`, preserving the boundary
   atoms;
2. the tails of (4.6), the polar continuum, and the reflected
   orientation group together with the Tate term of (2.4);
3. right minimality orients the dual pairing (5.2), or directly proves
   (0.5), without differentiating the radical equation as if a null
   branch already existed.

The third is now the only non-algebraic exterior law. Its form is no
longer an abstract cancellation of `z_F`: it is the scalar equality
(0.5) between the PC curvature observed by the causal dual and the
interior Tate Wronskian.

## 8. Status

```text
antidiagonal polarization of the exterior Wronskian            PROVED
bulk + exterior Green law = Tate, equation (0.4)                PROVED
Z/2-graded realization before recombination                     PROVED
indefinite character of every square completion                 PROVED
K2 extracted by Möbius = W                                      PROVED
gamma + W = 2 Lambda log inside PC                               PROVED
localization correction with respect to R170_851                PROVED
cancellation of the covariant term 2MK and of all tails          OPEN
minimality => dual equality (0.5)                                OPEN
exterior law R170_853 (5.1)                                     OPEN
VIR--LB / D                                                      OPEN
```
