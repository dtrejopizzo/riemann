# 106.63 — The all-atoms flag and the radical-shorting gate

## Purpose and verdict

Document 106.62 reduces a finite-head assertion on elementary
mean-periodic modes to positivity of an explicit Hermitian Gram matrix.  A
natural successor is to order the prime powers, add one literal von
Mangoldt atom at a time, and look for a Cholesky or Schur-complement
telescoping identity.  This note carries out that calculation before any
sign is asserted.

There is an exact flag, and every arithmetic increment is positive.  The
theta scaling further splits each increment into the divisible,
nondivisible-fractional and central-crossing features of 106.38.  However,
the flag does not commute with exact Riemann-radical shorting.  At every
proper finite head the signed curvature is strictly negative on every
nonconstant exact radical direction; only the complete infinite joint sum
restores the radical to zero.  Consequently the signed Schur short of a
finite head over the radical is unbounded below.  At the zero-mode matrix
level, the determinant update contains the inverse of the preceding
*signed* Gram matrix and therefore has no fixed sign.

Thus atomwise positivity supplies monotone bookkeeping, but not a
radical-compatible determinant telescope.  Any closing factorization has
to be formed after the complete prime--Gamma--polar limit is assembled.

## 1. Exact feature maps on the zero divisor

Retain the notation

\[
 h(x)=\cosh(x/2),\qquad c_K=\frac12,
 \qquad \chi_z(x)=\frac{\cos(zx)}{h(x)}.             \tag{1}
\]

Let \(z_1,\ldots,z_d\) be zeros of \(\Xi\), with the usual derivative
jets when a zero is multiple, and define the synthesis map

\[
 Z_d a=\sum_{j=1}^d a_j\chi_{z_j}.                  \tag{2}
\]

The identities in 106.43 give

\[
 \operatorname {ran}Z_d\subset(1\oplus\mathcal R)^\perp. \tag{3}
\]

For a prime power \(m\), put \(u_m=\log m\),
\(a_m=\Lambda(m)/\sqrt m\), and define

\[
 (V_m a)(x)
 =\sqrt{a_mK(x)K(x-u_m)}\,
   \Delta_{u_m}(Z_da)(x).                            \tag{4}
\]

The Gamma and polar feature maps are

\[
\begin{aligned}
 (V_\Gamma a)(u,x)
 &=\sqrt{\frac{e^{-u/2}}{1-e^{-2u}}K(x)K(x-u)}\,
   \Delta_u(Z_da)(x),\\
 D_da&=D_\mu Z_da .                                  \tag{5}
\end{aligned}
\]

Their target spaces carry Lebesgue measure in the displayed variables.
For a finite set \(S\) of prime powers, set

\[
 V_S=V_\Gamma\oplus\bigoplus_{m\in S}V_m,
 \qquad H_S=V_S^*V_S-D_d^*D_d.                      \tag{6}
\]

Because \(\|D_\mu q\|^2=\frac12\|q\|^2\) for centered \(q\), (6) is
exactly the kernel \(\mathcal H_S\) of 106.62:

\[
 a^*H_Sa
 =\mathscr E_S(Z_da)-\frac12\|Z_da\|_{L^2(\mu_K)}^2. \tag{7}
\]

### Theorem 1 — Literal all-atoms Loewner flag

If \(S\subset S'\), then

\[
 \boxed{H_{S'}-H_S
 =\sum_{m\in S'\setminus S}V_m^*V_m\succeq0.}       \tag{8}
\]

In particular, for any enumeration \(m_1,m_2,\ldots\) of the prime
powers, \(H_N:=H_{\{m_1,\ldots,m_N\}}\) is an increasing sequence of
Hermitian matrices and

\[
 H_N=H_\Gamma+\sum_{k=1}^NV_{m_k}^*V_{m_k}.         \tag{9}
\]

#### Proof

Equation (8) follows by subtracting the orthogonal direct sums in (6).
It is also the polarization of the atomwise identity 106.32(6).  No
location statement about the zeros is used. \(\square\)

## 2. The complete theta feature of one increment

The identity 106.38(7) polarizes.  Therefore every feature in (4) is
unitarily equivalent to the orthogonal sum

\[
 V_m\simeq V_m^{\rm div}\oplus V_m^{\rm frac}
                 \oplus V_m^{\rm ctr},              \tag{10}
\]

where, writing \(u=\log m\),

\[
\begin{aligned}
 (V_m^{\rm div}a)(x)
 &=\sqrt{\frac{2\Lambda(m)}m}\,K(x)
   \Delta_u(Z_da)(x),&&x\ge u,\\
 (V_m^{\rm frac}a)(x)
 &=\sqrt{\frac{2\Lambda(m)}{\sqrt m}K(x)R_m(x)}\,
   \Delta_u(Z_da)(x),&&x\ge u,\\
 (V_m^{\rm ctr}a)(x)
 &=\sqrt{\frac{\Lambda(m)}{\sqrt m}K(x)K(u-x)}\,
   \{(Z_da)(x)-(Z_da)(u-x)\},&&0<x<u .              \tag{11}
\end{aligned}
\]

Consequently the flag increment itself has the exact three-square form

\[
 \boxed{V_m^*V_m
 =(V_m^{\rm div})^*V_m^{\rm div}
 +(V_m^{\rm frac})^*V_m^{\rm frac}
 +(V_m^{\rm ctr})^*V_m^{\rm ctr}.}                 \tag{12}
\]

This is the strongest atomwise statement supplied by the theta dilation.
It retains rather than discards the nondivisible indices and the crossing
interval.

## 3. Why the determinant increment has no sign

Fix the zero-mode dimension \(d\).  If \(H_N\) is invertible, the matrix
determinant lemma gives

\[
 \boxed{
 \frac{\det H_{N+1}}{\det H_N}
 =\det_{\mathbb C^d}\!\left(
 I+H_N^{-1}V_{m_{N+1}}^*V_{m_{N+1}}\right).}       \tag{13}
\]

The right side of (13) is not a Gram determinant: before positivity has
been proved, \(H_N^{-1}\) is indefinite.  Hence (8) does not imply that
the ratio in (13) is positive.  Equivalently, if a new zero mode is added
and the preceding principal block \(A\) is invertible, its pivot is

\[
 \sigma=d-b^*A^{-1}b,                               \tag{14}
\]

which is a signed Schur complement, not a squared Hilbert-space distance
unless \(A\succ0\) is already known.  Declaring (13) or (14) positive
would assume the assertion that the flag was intended to prove.

This also explains the moving finite-head diagnostics of 106.62.  Adding
an atom raises every fixed Rayleigh quotient by (8), but enlarging the
zero-mode synthesis space introduces a new signed Schur pivot.  These are
different monotonicities and do not telescope against one another.

## 4. Exact incompatibility with radical shorting at finite head

Let

\[
 r_j=K^{(2j)}/K,\qquad j\ge1.                        \tag{15}
\]

For the complete ordinary-prime--Gamma energy the radical identity is

\[
 \mathscr E_K(r_j)-\frac12\operatorname {Var}_{\mu_K}(r_j)=0. \tag{16}
\]

Let \(S\) be any proper set of prime powers whose omitted energy is
nonzero.  Atomwise subtraction gives

\[
\begin{aligned}
 \mathscr E_S(r_j)-\frac12\operatorname {Var}_{\mu_K}(r_j)
 &=-\sum_{m\notin S}\frac{\Lambda(m)}{\sqrt m}
       \mathcal J_{\log m}(r_j)\\
 &<0.                                                  \tag{17}
\end{aligned}
\]

The strict sign follows because \(r_j\) is analytic and nonconstant.  If
\(\mathcal J_u(r_j)=0\), positivity of \(K(x)K(x-u)\) would make \(r_j\)
\(u\)-periodic; the theta asymptotic makes \(K^{(2j)}/K\) unbounded at
infinity, so this is impossible.

### Theorem 2 — No finite-head signed radical short

Let \(\mathcal A_S\) denote the signed quadratic form on its extended
form domain

\[
 \mathcal A_S(q)=\mathscr E_S(q)
 -\frac12\operatorname {Var}_{\mu_K}(q).             \tag{18}
\]

For every proper finite head \(S\), every \(q\) for which \(q,r_j\) lie
in that extended form domain, and every nonconstant radical direction
\(r_j\),

\[
 \inf_{t\in\mathbb R}\mathcal A_S(q+tr_j)=-\infty. \tag{19}
\]

Therefore the form-theoretic short of \(\mathcal A_S\) over \(\mathcal
R\) does not exist as a lower-semibounded quadratic form.  Radical
shorting becomes legitimate only after all prime powers have been summed,
when (16) and its polarization make \(\mathcal R\) a genuine null space.

#### Proof

By (17), the coefficient of \(t^2\) in
\(\mathcal A_S(q+tr_j)\) is strictly negative.  The remaining terms are
at most affine in \(t\), proving (19). \(\square\)

This is stronger than saying that a finite head has not yet accumulated
enough mass.  It says that the natural operation required by the proposed
telescope—short first, then add atoms—is undefined at every proper finite
stage.  The two operations have to occur in the opposite order:

\[
 \boxed{\text{assemble the complete joint limit first, then short the
 radical.}}                                           \tag{20}
\]

## 5. Consequence for Pick and sum-of-squares proposals

On the zero divisor, an identity of the form

\[
 \mathcal H_\infty(z,w)
 =\sum_\ell\overline{F_\ell(z)}F_\ell(w)
 +\overline{\Xi(z)}A(z,w)+\Xi(w)\overline{A(w,z)}    \tag{21}
\]

would prove every finite Gram matrix positive.  Thus (21) remains a
logically valid target.  The calculation above proves that it cannot be
obtained by a finite-head Cholesky telescope whose partial remainders are
nonnegative and radical-compatible: (17) gives the opposite sign at every
proper stage, and (13) gives no signed determinant increment.

Likewise, the strict reverse minor of the Gamma kernel in 106.42 rules out
deriving (21) from total positivity or a variation-diminishing ordering.
A surviving identity must be a *global* modulo-\(\Xi\) factorization of
the already-renormalized infinite prime--Gamma--polar form.  Proving such
a factorization is precisely the unresolved complementary contraction; it
is not furnished by the atom flag itself.

## 6. Status

The following facts are now exact.

1. Every literal prime-power addition is a positive Gram increment.
2. Every increment has the complete divisor/fractional/central theta
   three-square decomposition.
3. Determinant and zero-mode Schur updates have no sign before the desired
   positivity is known.
4. Every proper finite head is strictly negative on all nonconstant exact
   radical directions, so finite-head signed shorting is unbounded below.

The all-atoms flag is therefore useful bookkeeping but not a proof of the
sharp floor.  The remaining theorem is still the positivity of the
complete, jointly assembled curvature on
\((1\oplus\mathcal R)^\perp\), with no separation of the infinite Euler
tail, Gamma channel or polar subtraction.
