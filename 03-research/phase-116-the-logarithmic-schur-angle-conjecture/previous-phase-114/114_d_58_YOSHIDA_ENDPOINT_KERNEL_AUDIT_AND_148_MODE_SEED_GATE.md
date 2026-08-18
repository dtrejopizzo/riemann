# D.58 — Yoshida endpoint-kernel audit and the 148-mode seed gate

## 1. Purpose

D.57 shows that a rigorous post-`2` interval follows from one coercive
full-primitive seed.  This note audits whether that seed is already supplied
by the truncated archimedean positivity of Yoshida or by the stronger Sonin
estimate of Connes--Consani.

The two theorems have different domains and must not be conflated:

* Yoshida's truncated statement uses only the polar vanishing conditions
  required by the primitive class;
* the strong Sonin square uses an additional central Mellin zero.

The audit finds no published equality classification or explicit coercive
constant for the full primitive form at the endpoint `T=(log 2)/2` in the
source available here.  Therefore the post-`2` interval cannot yet be
started from that theorem alone.

The improved monotone Gamma cutoff of D.55 makes the remaining computation
far smaller than before: with margin one it is a parity core of total
dimension at most `148` at the endpoint.  This is the precise finite seed
gate.

No paper file is changed, and no RH, screw positivity or zero location is
used.

## 2. The two distinct positivity statements

Let `f` be a positive-definite multiplicative test supported in `(1/2,2)`.
The truncated Yoshida statement, as quoted and used by Connes--Consani, is

\[
 \widehat f(i/2)=\widehat f(-i/2)=0
 \quad\Longrightarrow\quad W_\infty(f)\geq0.              \tag{2.1}
\]

Writing

\[
 f=g*g^*,qquad
 \operatorname{supp}g\subset[2^{-1/2},2^{1/2}],           \tag{2.2}
\]

the two conjugate zeros of `f` come from the single polar zero of the
convolution root `g`.  Thus (2.1) is equivalent to

\[
 QW_{T_2}(g,g)=W_\infty(g*g^*)\geq0,
 \qquad \widehat g(i/2)=0,                                \tag{2.3}
\]

with

\[
 T_2={\log2\over2}.                                       \tag{2.4}
\]

Under the logarithmic normalization of D.32, this is the full two-polar
primitive condition.  There is no central zero in (2.1)--(2.3).

By contrast, Connes--Consani, arXiv:2006.13771, Theorem 1, assumes

\[
 \widehat g(i/2)=0,qquad\widehat g(0)=0                   \tag{2.5}
\]

and proves

\[
 W_\infty(g*g^*)
 \geq\operatorname{Tr}
 \bigl(\vartheta(g)\mathfrak S\vartheta(g)^*\bigr)
 =\|\vartheta(g)\mathfrak S\|_{HS}^2\geq0.               \tag{2.6}
\]

Theorem 6.11 removes the central zero only at the cost of a negative defect:

\[
 W_\infty(g*g^*)
 \geq\|\vartheta(g)\mathfrak S\|_{HS}^2
       -c|\widehat g(0)|^2.                               \tag{2.7}
\]

Therefore (2.6) cannot be cited as a coercive estimate on the full space in
(2.3).

## 3. Equality audit

### 3.1 Extra-central Sonin class

On the class (2.5), equality in the right side of (2.6) implies

\[
 \vartheta(g)\mathfrak S=0.                               \tag{3.1}
\]

Choose a nonzero Sonin vector `xi`.  In the Mellin representation,
`vartheta(g)` is multiplication by the entire function `hat g`; the Mellin
transform of `xi` is nonzero on a positive-measure set.  Hence (3.1) forces
`hat g` to vanish on a set with an accumulation point, so `g=0`.  Thus the
Sonin square is strict for nonzero tests satisfying the extra central zero.

This does not settle equality in the larger space (2.3), because the defect
in (2.7) may cancel the positive Sonin trace.

### 3.2 Full Yoshida primitive class

The endpoint result quoted in the accessible sources is the nonnegative
inequality (2.1).  It does not give, in the quoted theorem statement,

1. a description of `ker QW_(T_2)`;
2. a proof that the kernel is zero;
3. a lower bound `gamma_2>0` in the graph norm of the canonical endpoint
   operator.

Suzuki's audit of Yoshida distinguishes two results.  Yoshida proves
unconditionally that the Hermitian form is positive definite for
*sufficiently small* support, and proves that nondegeneracy for every support
is equivalent to RH.  The first statement does exclude equality on an
unspecified initial interval, but the quoted result does not provide an
explicit endpoint reaching `T_2`, nor a quantitative graph-norm constant.
Later computations quote a small positive lowest eigenvalue at
`lambda=sqrt 2`.  Those numerical computations are not a directed enclosure
of the infinite-dimensional operator and cannot be used as the missing
`gamma_2`.

Accordingly, strictness of the full endpoint form is not imported here.

## 4. The improved exact Gamma cutoff

Let

\[
 A_T=\sum_{p^k\leq e^{2T}}{\log p\over p^{k/2}},
 \qquad
 m_\infty(\tau)=\log\pi-
 \operatorname{Re}\psi(1/4+i\tau/2).                     \tag{4.1}
\]

D.55 now uses the monotone exact cutoff `R_T^sharp` defined by

\[
 \operatorname{Re}\psi(1/4+iR_T^\sharp/2)-\log\pi
 =2A_T+\eta.                                               \tag{4.2}
\]

Then the complete multiplier, including every active prime power, satisfies

\[
 b_T(\tau)\leq-\eta
 \qquad(|\tau|\geq R_T^\sharp).                            \tag{4.3}
\]

At `T=T_2`, including the endpoint `p=2` harmlessly in the upper bound,

\[
 A_{T_2}={\log2\over\sqrt2}.                              \tag{4.4}
\]

For `eta=1`, (4.2) has the unique positive solution

\[
 R_{T_2}^\sharp=45.5201607008\ldots.                      \tag{4.5}
\]

The prolate trace bound of D.55 becomes

\[
 d_{T_2}leq
 {4T_2R_{T_2}^\sharp(M_{T_2}+1)\over\pi}
 =147.6865\ldots,                                         \tag{4.6}
\]

where `M_T=m_0+2A_T`.  Hence

\[
 \boxed{d_{T_2}\leq148.}                                 \tag{4.7}
\]

This replaces the earlier multi-million-dimensional coarse bound.  The
number in (4.5) is diagnostic; the rigorous definition is the monotone root
(4.2), which can be enclosed by directed digamma-series bounds.

## 5. The exact endpoint seed theorem needed

Let `S_(2,e)` and `S_(2,o)` be the parity Feshbach matrices obtained from the
common cutoff (4.2), and let the two effective jets be those of D.56.  A
rigorous interval computation of at most 148 modes must establish

\[
 \begin{aligned}
 S_{2,o}&\leq-\gamma_2 I,\\
 Q_vS_{2,e}Q_v&\leq-\gamma_2 Q_v,\\
 \sigma_{2,e}&\geq\gamma_2,\\
 g_{2,e}&\geq\gamma_2,qquad g_{2,o}\leq-\gamma_2
 \end{aligned}                                             \tag{5.1}
\]

for one directed rational `gamma_2>0`, with the D.55 high residual included.
These inequalities simultaneously prove the absence of an equality mode
and furnish the propagation margin required in D.57.

The full Yoshida nonnegativity says that no negative primitive direction is
present at the endpoint; it does not by itself imply the quantitative
system (5.1).

## 6. Combination with the first hinge

Suppose (5.1) has been certified.  On a rational interval

\[
 [T_2,T_2+h]\subset
 [T_2,\log3/2),                                             \tag{6.1}
\]

the only new finite-place term is

\[
 g_2(t)={\log2\over\sqrt2}(|t|-\log2)_+.                  \tag{6.2}
\]

The D.57 interval engine gives a directed derivative bound `L_2` for the
three parity/jet certificates, including the one-sided hinge subdivision.
Then

\[
 \boxed{0<h<{\gamma_2\over L_2}}                          \tag{6.3}
\]

closes a rigorous nontrivial interval posterior to `T_2`.

The form of (6.3) is unconditional, but no numerical `h` is asserted because
`gamma_2` has not yet been certified.  Substituting a plotted or ordinary
floating smallest eigenvalue for `gamma_2` would not be a proof.

## 7. Why compact resolvent alone does not finish the audit

If one first proved that the full endpoint operator is strictly positive,
its compact resolvent would indeed turn strictness into a positive lowest
eigenvalue.  The logical missing step is exactly the triviality of the
kernel.  Compact resolvent cannot convert a merely nonnegative theorem into
a positive gap: the finite matrix `diag(0,1)` already shows this.

Likewise, strictness on the extra-central codimension-one subspace does not
exclude a zero mode with nonzero central Mellin value.  The defect term in
(2.7) is precisely the uncontrolled scalar channel.

## 8. Result and next computation

The equality audit does not justify a full-primitive coercive seed from the
currently quoted Yoshida/Connes--Consani statements.  Therefore D.58 does
not claim a post-`2` interval.

It does, however, reduce the missing seed to a practical and exact task:

1. construct the at-most-148-dimensional parity core using the monotone
   cutoff (4.2);
2. enclose its Gamma entries by the positive series and analytic tail;
3. enclose the `p=2` threshold contribution one-sidedly;
4. perform directed `LDL^*` and jet Schur arithmetic;
5. obtain `gamma_2` in (5.1), then apply (6.3).

This computation would prove the endpoint kernel trivial rather than assume
it.  Invoking global screw positivity or the zeta zero representation to
exclude the kernel would be circular.
