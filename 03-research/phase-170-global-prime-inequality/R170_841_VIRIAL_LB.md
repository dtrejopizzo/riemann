# R170_841 — VIR--LB: derivative of the finite hyperbola, first-order no-go and oriented residue

Continuation of R162_407--408, R162_501 and
R170_840. Paper 47 is not modified.

## 0. Verdict

It has not been proved that

\[
 \mathcal V_{\Lambda,T}(F)\le 0
 \qquad(F\in N_T^\varepsilon).
 \tag{0.1}
\]

The search does produce a new exact reduction at the level required by
R170_840: the finite hyperbola is differentiated **before** recombining it
into \(K_N\), the block \(k>N\) is retained, and the only first-order
channel that does not vanish by
\(\sum_{d\mid k}\Lambda(d)=\log k\) is identified. It is the antisymmetric
channel between the two legs of each factorization \(k=dm\):

\[
 \boxed{
 \mathcal A_{M,N}
 :=\dot L_M S_N-L_M\dot S_N.}
 \tag{0.2}
\]

On a complete fiber \(k\le N\le M\), its coefficient is

\[
 \boxed{
 \beta_\Lambda(k)
 =\sum_{d\mid k}\Lambda(d)\log{d\over k/d}
 =2\sum_{d\mid k}\Lambda(d)\log d-(\log k)^2.}
 \tag{0.3}
\]

The synchronized channel, on the other hand, telescopes exactly:

\[
 \dot L_MS_N+L_M\dot S_N-\dot K_N=\dot H_{M,N},
 \qquad
 \Pi_{\le N}\dot H_{M,N}=0.
 \tag{0.4}
\]

The second equality uses the factorization of the integers
irreversibly. For an altered weight \(a\), the right-hand side on the
lower fiber is \(\delta_a(k)\log k\), with
\(\delta_a(k)=\sum_{d\mid k}a(d)-\log k\); hence the line fails exactly
for modifications of \(\Lambda\) and for Davenport--Heilbronn when the
ordinary multiplicity-one comb is kept.

The attempt to obtain the sign of (0.1) from (0.3) fails for a
coefficient-by-coefficient reason, not from an insufficient estimate:
\(\beta_\Lambda(k)\) changes sign. The only canonical positive
completion is the second-order variance

\[
 \Sigma_\Lambda(k)
 =\sum_{d\mid k}\Lambda(d)
       \left(2\log d-\log k\right)^2\ge0,
 \qquad
 |\beta_\Lambda(k)|^2\le(\log k)\Sigma_\Lambda(k),
 \tag{0.5}
\]

but (0.5) controls the modulus of the antisymmetric channel, not its
orientation. The step from first to second order is precisely a square;
it cannot give VIR--LB without an additional saturation identity.

An exact no-go is proved below for the class of diagonal operations on
the fiber that uses \(\delta_\Lambda=0\), scale differentiation and sums
of squares. The operation still to be built is no longer another collar
identity: it is an **antisymmetric boundary Green law** orienting
\(\mathcal A_{M,N}\) at the contact state and literally including

1. \(\dot H_{M,N}\), with all \(k>N\);
2. the derivative of the polar continuum \(\dot C_N\);
3. the support defect upon compressing;
4. the Tate term \(2\operatorname{Re}\langle F,tr_F'\rangle\).

This reduction is strictly weaker than postulating VIR--LB: (0.2) is an
explicit finite operator with determined coefficients. What is missing is
a physical relation, specific to first contact, between that operator and
the three boundary blocks. No identity available in the corpus provides
that relation.

## 1. Quantifiers and dilation convention

Let \(T>0\) be a hypothetical first window and

\[
 N_T^\varepsilon
 =\{F\in\ker H_T:JF=\varepsilon F\},
 \qquad \varepsilon\in\{+1,-1\}.
 \tag{1.1}
\]

Whenever \(\mathcal V_{\Lambda,T}\) is mentioned, (REG) of R162_407 and
the threshold regularity needed for

\[
\begin{aligned}
 \mathcal V_{\Lambda,T}(F)
 ={}&{1\over2\pi}\int_{\mathbb R}
       \tau m'(\tau)|\widehat F(\tau)|^2\,d\tau\\
 &-\sum_{n<e^{2T}}{2\Lambda(n)\over\sqrt n}
       \log n\,c_F'(\log n)
 +2\operatorname{Re}\langle F,tr_F'\rangle
\end{aligned}
 \tag{1.2}
\]

to be defined are assumed. The coefficient identities of §§2--5 do not
need (REG): they hold in the Schwartz kernel and, by duality, on any
carrier where the pairings are defined.

Fix integers

\[
 N\ge\lceil e^{2T}\rceil,
 \qquad M\ge N.
 \tag{1.3}
\]

The following formulas hold for **every** \(T,M,N\) satisfying
(1.3), with no $T$-dependent constant. This is the uniformity that is
indeed obtained. No uniform bound is claimed for the missing boundary
law.

Let

\[
 (U_r f)(t)=r^{-1/2}f(t/r),\qquad r>0,
 \tag{1.4}
\]

and, for an operator \(B\), write

\[
 B(r)=U_r^{-1}BU_r,\qquad \dot B={d\over dr}B(r)\big|_{r=1}.
 \tag{1.5}
\]

Then

\[
 U_r^{-1}\tau_aU_r=\tau_{a/r},\qquad
 \dot\tau_a=-a\,\partial_t\tau_a.
 \tag{1.6}
\]

This is the pullback convention from the window \(rT\) to the fixed
window. With it, the derivative of the window form is
\(-\mathcal V\), including the Tate correction terms, as in
R162_407 Theorem 3.2.

## 2. No-duplication audit

Prior results on virial, Pohozaev, dilation and hyperbola identities that
might touch (0.1) were reviewed. The results restricting the construction
are:

| Source | Available result | Current restriction |
|---|---|---|
| R162_407 | derives (1.2) and proves the selected vector maximizes \(\mathcal V\), with maximum \(\ge0\) | VIR--LB is equivalent to exact tangency, not to a small bound |
| R162_408 | Feshbach orients the full collar energy; jets and Gamma moments are independent | a tail cannot be separated by norm |
| R162_501 | Selberg converts \(\Lambda\log+\Lambda*\Lambda\) into \(\mu*\log^2\), but leaves derived correlations without sign | mere positivity of \(W\) is not enough and does not fail for positive modifications |
| R106_124 | the dilation commutator contains \((\log n)(\delta'_{\log n}-\delta'_{-\log n})\) and is unbounded in both signs in the core | there is no source-independent sign of the prime virial |
| P124_007 | the projected virial doubles and cancels the Tate defect | a Pohozaev multiplier does not eliminate Tate |
| R161_030--039 | oriented variance and coherent square are positive; the physical saturation with polar/Tate is missing | fibers cannot be declared orthogonal nor saturation assumed |
| R161_057--065 | mixed Green leaves the support concomitant, of indefinite sign | moving the compression creates the block that must be preserved |
| R162_401, R162_502--503 | the log channel and Möbius conjugation recompose the equation; identities transport to DH only if the comb is also changed | the ordinary comb must remain fixed |
| R162_901 | at order two, \(\Lambda*\Lambda\) only appears in the sum channel; compression retains the difference channel too | a Selberg identity does not diagonalize the finite window |
| R163_139--140 | the Selberg jet has a positive Gamma tail but finite rational collisions without sign | non-divisible ratios cannot be discarded |
| R163_150--152 | there is a corner anomaly and an exact microscopic tomography of the weights | the polar continuum and the cutoff route are part of the physical datum |
| R163_159--160 | the truncated hyperbola preserves products and detects sub-principal modifications | recombining into a full convolution erases the boundary |
| R170_704 | interior dilation gives the opposite geometric sign and the identity \(\Lambda=\mu*\log\) leaves mixed summands | minimality alone only proves \(\mathcal V(G)\ge0\) |
| R170_837--840 | PC--collar leaves Tate, nonlocal residual and tail; R170_840 formulates VIR--EP | VIR--LB must be born before recombining PC |

The identity of §§3--4 is not the variance of R161_030: here the
hyperbola is first differentiated with respect to scale and its two legs
are separated. The result explains why that variance can only appear at
second order and locates the first moment that would have to orient a new
law.

## 3. Synchronized derivative of the finite hyperbola

For a real weight \(a(1)=0\), set

\[
\begin{aligned}
 S_N&=\sum_{m\le N}m^{-1/2}\tau_{\log m},\\
 L_M^a&=\sum_{d\le M}a(d)d^{-1/2}\tau_{\log d},\\
 K_N&=\sum_{k\le N}(\log k)k^{-1/2}\tau_{\log k},\\
 H_{M,N}^a&=L_M^aS_N-K_N.
\end{aligned}
 \tag{3.1}
\]

Define

\[
 q_{M,N}^a(k)
 =\sum_{\substack{dm=k\\d\le M,\ m\le N}}a(d)
  -1_{k\le N}\log k.
 \tag{3.2}
\]

Then, at finite cutoff,

\[
 H_{M,N}^a
 =\sum_{k\le MN}{q_{M,N}^a(k)\over\sqrt k}
       \tau_{\log k}.
 \tag{3.3}
\]

**Theorem 3.1 (scale Ward identity of the hyperbola).** For all \(M,N\),

\[
 \boxed{
 \dot H_{M,N}^a
 =-\sum_{k\le MN}{q_{M,N}^a(k)\log k\over\sqrt k}
       \partial_t\tau_{\log k}.}
 \tag{3.4}
\]

Moreover,

\[
 \boxed{
 \dot L_M^aS_N+L_M^a\dot S_N-\dot K_N
 =\dot H_{M,N}^a.}
 \tag{3.5}
\]

If \(M\ge N\), the projection onto \(k\le N\) is

\[
 \boxed{
 \Pi_{\le N}\dot H_{M,N}^a
 =-\sum_{k\le N}{\delta_a(k)\log k\over\sqrt k}
       \partial_t\tau_{\log k},
 \quad
 \delta_a(k)=\sum_{d\mid k}a(d)-\log k.}
 \tag{3.6}
\]

In particular,

\[
 \Pi_{\le N}\dot H_{M,N}^\Lambda=0,
 \tag{3.7}
\]

and the surviving block is exactly

\[
 \boxed{
 \dot H_{M,N}^\Lambda
 =-\sum_{N<k\le MN}{h_{M,N}(k)\log k\over\sqrt k}
       \partial_t\tau_{\log k},
 \quad
 h_{M,N}(k)=
 \sum_{\substack{dm=k\\d\le M,\ m\le N}}\Lambda(d)\ge0.}
 \tag{3.8}
\]

*Proof.* (3.3) follows from grouping \(L_M^aS_N\) by \(k=dm\).
Rule (1.6) gives (3.4). Differentiating the identity
\(H_{M,N}^a=L_M^aS_N-K_N\) gives (3.5). For \(k\le N\le M\)
all divisors appear, which gives (3.6). Finally
\(\delta_\Lambda(k)=0\) gives (3.7)--(3.8). \(\square\)

The logical order matters. In (3.7) the arithmetic was used **before**
recombining PC. \(H\) was not replaced by \(L S-K\) after the pairing, nor
was boundary term (3.8) eliminated.

### 3.1. Falsifiers on the exact line

If \(a=\Lambda+\eta\), then

\[
 \delta_a(k)=\sum_{d\mid k}\eta(d).
 \tag{3.9}
\]

A nonzero modification at \(q\) reappears at every multiple of
\(q\) contained in \([1,N]\). Thus (3.7), the load-bearing line, ceases
to hold.

For Davenport--Heilbronn, keeping \(S_N\) as the ordinary comb of the
integers, its logarithmic coefficients \(a_{DH}\) do not satisfy
\(a_{DH}*1=\log\), and (3.6) is again nonzero. If the comb \(1\) is also
changed to the DH series coefficients, the tautological cancellation
returns, as R162_503 proves. That change is not admissible here: it
destroys the specific input of \(\mathbb Z\), which is precisely the
multiplicity one of the comb \(S_N\).

## 4. Separating the two legs: the first-order residue

For a fiber \(k=dm\), define

\[
\begin{aligned}
 A_a(k)&=\sum_{d\mid k}a(d)\log d,\\
 B_a(k)&=\sum_{d\mid k}a(d)\log(k/d).
\end{aligned}
 \tag{4.1}
\]

On a complete fiber \(k\le N\le M\), \(\dot L_MS_N\) carries
\(-A_a(k)\partial_t\tau_{\log k}\) and
\(L_M\dot S_N\) carries
\(-B_a(k)\partial_t\tau_{\log k}\). For \(a=\Lambda\),

\[
 A_\Lambda(k)+B_\Lambda(k)=(\log k)^2.
 \tag{4.2}
\]

This is the coefficient-by-coefficient derivative of
\(\Lambda*1=\log\). The sum of the two legs cancels against
\(\dot K_N\), as in (3.7). Their difference does not cancel:

\[
 \mathcal A_{M,N}:=\dot L_MS_N-L_M\dot S_N,
 \tag{4.3}
\]

\[
 \Pi_{\le N}\mathcal A_{M,N}
 =-\sum_{k\le N}{\beta_\Lambda(k)\over\sqrt k}
       \partial_t\tau_{\log k},
 \tag{4.4}
\]

with \(\beta_\Lambda\) given by (0.3). From (3.5) and (4.3) one obtains
the exact decomposition

\[
 \boxed{
 2\dot L_MS_N
 =\dot H_{M,N}+\dot K_N+\mathcal A_{M,N}.}
 \tag{4.5}
\]

Hence the prime virial, which differentiates the \(L_M\) leg, is not
contained in the synchronized cancellation (3.7). To recover it one must
orient \(\mathcal A_{M,N}\) and undo the \(S_N\) leg. This last step does
not commute with compression and is where the boundary, the polar term
and Tate reappear.

### 4.1. The first moment changes sign

There is no coefficient-by-coefficient sign for (4.4). If \(k=p^j\),

\[
 \beta_\Lambda(p^j)=j(\log p)^2>0.
 \tag{4.6}
\]

But, for \(k=p^2q\),

\[
 \beta_\Lambda(p^2q)
 =2(\log p)^2+(\log q)^2-4\log p\log q.
 \tag{4.7}
\]

In particular \(\beta_\Lambda(12)<0\). Thus, neither the positivity of
\(\Lambda\), nor support on prime powers, nor the equality
\(\sum_{d\mid k}\Lambda(d)=\log k\) orients the antisymmetric first
moment.

### 4.2. The positive completion is of second order

The measure

\[
 {\Lambda(d)\over\log k},\qquad d\mid k,
 \tag{4.8}
\]

is an exact probability measure. Cauchy--Schwarz gives

\[
\begin{aligned}
 \Sigma_\Lambda(k)
 &:=\sum_{d\mid k}\Lambda(d)
      \left(2\log d-\log k\right)^2\ge0,\\
 |\beta_\Lambda(k)|^2
 &\le (\log k)\Sigma_\Lambda(k).
\end{aligned}
 \tag{4.9}
\]

More precisely, if
\(\bar\ell_k=(\log k)^{-1}\sum_{d\mid k}\Lambda(d)\log d\),

\[
 \Sigma_\Lambda(k)
 =4(\log k)\operatorname{Var}_k(\log d)
  +(\log k)(2\bar\ell_k-\log k)^2.
 \tag{4.10}
\]

(4.9)--(4.10) are sums of real squares and go through on the prime
fibers. However, they are even under
\(2\log d-\log k\mapsto-(2\log d-\log k)\), while
\(\beta_\Lambda\) is odd. An inequality built only from
\(\Sigma_\Lambda\) controls \(|\beta_\Lambda|\) and does not decide its
sign.

This is precisely the point where the search for a sum of squares stops:
the quantity required by the virial is a first moment; the positive
quantity available is its second moment.

### 4.3. Deconvolving returns exactly to the Selberg no-go

One can also try to remove the \(S_N\) leg via Möbius. In the compressed
causal algebra, where the semigroup is exact, this turns the first
moment into \(\Lambda\log\). The Selberg identity gives

\[
 \Lambda\log=\mu*\log^2-\Lambda*\Lambda
 =W-\Lambda*\Lambda.
 \tag{4.11}
\]

The term \(\Lambda*\Lambda\) is the square of the prime comb and \(W\ge0\),
but the virial pairs them with \(c_F'(\log k)\), not with a norm. This is
exactly the form audited in R162_501: it has no sign. On the full line,
(4.11) does not additionally eliminate the truncated hyperbola of (3.8);
in the window, multiplying by the compressed inverse creates the support
blocks of §5. Therefore Möbius does not orient (4.3): either it repeats
the Selberg no-go, or it transfers the problem to the physical boundary.

## 5. The boundary that cannot be lost

### 5.1. The tail \(k>N\)

On incomplete fibers set

\[
 \beta_{M,N}(k)
 =\sum_{\substack{dm=k\\d\le M,\ m\le N}}
     \Lambda(d)\log{d\over m}.
 \tag{5.1}
\]

Then

\[
 \mathcal A_{M,N}
 =-\sum_{k\le MN}{\beta_{M,N}(k)\over\sqrt k}
     \partial_t\tau_{\log k},
 \tag{5.2}
\]

where (0.3) only replaces (5.1) for \(k\le N\). The hyperbola has not
been completed near \(MN\). In PC, block (3.8)/(5.2) acts against
\(\mathscr F F\) and against exterior tests; the fact that \(\log k>2T\)
does not annihilate it. It would only annihilate the interior pairing
\(\langle F,\tau_{\log k}F\rangle\), which is not the PC carrier.

### 5.2. The polar derivative is explicit and has no sign

The R161_003 counterterm is

\[
 C_Nf(t)=e^{-t/2}\int_{-\infty}^{t+\log N}e^{u/2}f(u)\,du.
 \tag{5.3}
\]

With the convention (1.4)--(1.5),

\[
 C_N(r)f(t)
 =r e^{-rt/2}\int_{-\infty}^{t+(\log N)/r}
           e^{rv/2}f(v)\,dv,
 \tag{5.4}
\]

and therefore

\[
\boxed{
\begin{aligned}
 \dot C_Nf(t)={}&(1-t/2)C_Nf(t)
 +e^{-t/2}\int_{-\infty}^{t+\log N}
       {v\over2}e^{v/2}f(v)\,dv\\
 &-(\log N)\sqrt N\,f(t+\log N).
\end{aligned}}
 \tag{5.5}
\]

The last summand is the infinitesimal face of the corner anomaly of
R163_150--152. It can have any sign when paired with a test function.
The primitivity conditions annihilate full moments, not the truncated
integral nor the boundary value of (5.5).

In the renormalized identity

\[
 Z_N=S_N-C_N,
 \qquad
 \widetilde H_{M,N}=L_MZ_N-K_N^Z,
 \tag{5.6}
\]

\(\dot C_N\) must be kept inside
\(\dot Z_N=\dot S_N-\dot C_N\). Eliminating it turns (4.5) into an
identity of the raw comb that depends on the cutoff route and does not
represent the physical virial.

### 5.3. Tate does not disappear either

The correction from keeping the two primitive moments under dilation is

\[
 \boxed{
 \mathfrak T_T(F)
 =2\operatorname{Re}\langle F,tr_F'\rangle.}
 \tag{5.7}
\]

If
\(r_F=\alpha e^{t/2}+\beta e^{-t/2}\), (5.7) contains the moments
weighted by \(t\); it is not annihilated by
\(\langle F,e^{\pm t/2}\rangle=0\). P124_007 proves that inserting these
moments via a virial multiplier makes them appear twice in the
projection defect and cancel, without producing an inequality.

Consequently, a law derived from (4.5) must contain the ledger

\[
 \boxed{
 \text{interior }\beta_\Lambda(k)
 \;\oplus\;
 \text{incomplete hyperbola }k>N
 \;\oplus\;
 \dot C_N
 \;\oplus\;
 [P_T,Z_N]
 \;\oplus\;
 \mathfrak T_T.}
 \tag{5.8}
\]

There are no arithmetic ellipses in (5.8): these are exactly the blocks
generated when separating the two legs, renormalizing and compressing.

## 6. Exact no-go for first-order diagonal operations

We define \(\mathscr C_{\rm fib}^{(1)}\) as the class of arguments that,
before recombining PC,

1. group \(L_MS_N-K_N\) by the fiber \(k=dm\);
2. apply at most one scale derivative to each translation;
3. use \(\delta_\Lambda(k)=0\), \(\Lambda(d)\ge0\) and
   \(h_{M,N}(k)\ge0\) coefficient by coefficient;
4. may polarize or complete squares within the same fiber;
5. do not introduce a new physical identity between fibers, Fourier
   orientations and support blocks.

**Theorem 6.1.** No argument of
\(\mathscr C_{\rm fib}^{(1)}\) proves (0.1).

*Proof.* On a complete fiber, the synchronized part is zero by
(3.7). The only first-order part distinguishing the two legs is
\(\beta_\Lambda(k)\), by (4.2)--(4.4), and it changes sign by
(4.6)--(4.7). Every positive completion within the fiber is quadratic in
the difference of the legs; its canonical form is (4.9)--(4.10), which is
invariant under inverting that difference and does not orient
\(\beta_\Lambda(k)\).

On an incomplete fiber, the coefficients \(h_{M,N}(k)\) are positive, but
the derived carrier is
\(\partial_t\tau_{\log k}\). Its pairing is a correlation derivative and
has no sign. This already happens for a single translation. The sum
cannot recover a sign from positivity of the coefficients.

Finally, a diagonalization by \(k\) that declares the fibers orthogonal
changes the physical Gram matrix. R161_031--035 proves that PC contains
the coherent sum, with product and ratio interferences. Restoring those
interferences, the compression, or the second orientation violates
condition 5 and generates precisely the blocks of (5.8). Thus, within the
declared class, no first-order scalar with a sign remains. \(\square\)

### 6.1. Analytic indeterminacy, even with Gamma assembled

The obstruction is not only that (4.7) has a negative example. Let a
nonzero finite combination

\[
 Q(F)=\sum_j b_j c_F'(u_j),\qquad 0<u_j<2T.
 \tag{6.1}
\]

On the subspace of smooth primitive functions of fixed parity, \(Q\)
takes both signs with bounded \(L^2\) norm. Indeed, for a smooth envelope
of the correct parity and
\(F_\xi(t)=\phi(t)\cos(\xi t)\) or
\(\phi(t)\sin(\xi t)\),

\[
 c_{F_\xi}'(u)
 =-{\xi\over2}A_\phi(u)\sin(\xi u)+O(1).
 \tag{6.2}
\]

The two Tate moments of \(F_\xi\) are \(O_A(\xi^{-A})\); correcting them
within the same parity sector with fixed functions does not change the
leading term. The leading sum is a nonzero trigonometric polynomial of
mean zero, and by recurrence takes both signs at size
\(\asymp\xi\). The Archimedean term of (1.2) is
\(O(1)\), because \(\tau m'(\tau)\) is bounded, and any finite-rank Tate
correction is sub-principal in this family.

This is the window version of R106_124 Theorem 3. It does not contradict
a sign restricted to the unknown radical; it proves that such a sign
cannot come from positive coefficients or from the Gamma assembly alone.
It must use a new relation specific to \(N_T^\varepsilon\).

## 7. The piece still to be built

Reduction (4.5) identifies a smaller, concrete goal. What is needed is a
finite Green form

\[
 \mathfrak G_{M,N,T}^{\rm asym}(F),
 \tag{7.1}
\]

derived from renormalized PC and the first-contact equation, with the
following verifiable properties:

1. its interior block is literally the pairing of
   \(\mathcal A_{M,N}\) of (4.3), not recombined \(\dot H\);
2. its exterior block contains (3.8) and (5.1), without completing the
   hyperbola;
3. its polar block is the one obtained from (5.5);
4. its compression preserves the two blocks \(P_TZ_N(1-P_T)\) and
   \((1-P_T)Z_NP_T\);
5. its Tate block is exactly (5.7);
6. for \(F\in N_T^\varepsilon\), a minimality identity orients the total
   sum with the sign that, via (4.5), gives
   \(\mathcal V_{\Lambda,T}(F)\le0\).

Conditions 1--5 already determine all the algebraic terms. Condition 6 is
the new datum. It cannot be replaced by
\(\mathfrak G=0\) defined ad hoc: R161_039 proves that coherent saturation
of that type has the full strength of the closure.

The arithmetic filter for a candidate construction is immediate. For
\(a\ne\Lambda\), (3.6) adds

\[
 -\sum_{k\le N}{\delta_a(k)\log k\over\sqrt k}
       \partial_t\tau_{\log k},
 \tag{7.2}
\]

to the synchronized block. The sign proof must break on that line. For
DH the ordinary comb must be kept; allowing the comb to change transports
the whole identity again and the falsifier fails.

Thus the actual output of this document is:

\[
 \boxed{
 \text{VIR--LB}
 \quad\Longleftarrow\quad
 \text{antisymmetric Green law for }\mathcal A_{M,N}
 \text{ with ledger (5.8)}.}
 \tag{7.3}
\]

(7.3) is not a nominal equivalence with VIR--LB. It reduces the problem
to an explicit finite operator, fixes its coefficients, exhibits the
defect for every falsifying weight, and proves that no diagonal sum of
squares can orient its first moment.

## 8. Status

```text
synchronized derivative of the finite hyperbola               PROVED
exact support k>N after using delta_Lambda=0                  PROVED
defect under altered weight / DH with ordinary comb            PROVED

separation of the d and m legs                                PROVED
coefficient beta_Lambda(k) of the antisymmetric channel        PROVED
uniform sign of beta_Lambda(k)                                 FALSE
positive variance Sigma_Lambda and bound on |beta|             PROVED
the variance orients beta                                      FALSE

explicit derivative of the polar continuum C_N                 PROVED
retention of k>N, support and Tate in the ledger                DONE
source-independent sign of the virial                           FALSE
no-go of the class C_fib^(1)                                    PROVED

antisymmetric boundary Green law                                OPEN
REG and threshold regularity                                    OPEN
VIR--LB: V_Lambda,T|N <= 0                                      OPEN
VIR--DET                                                        OPEN
complete bilateral law                                          OPEN
D                                                                OPEN
```

The next construction must not re-derive the synchronized sum: that sum
is already zero for \(k\le N\) and leaves only (3.8). It must work with
the leg difference (4.3) and show, from a physical first-contact
identity, how the blocks of (5.8) orient that first moment.
