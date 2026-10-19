# Phase 181 — complex polarization of the logarithmic prime current

## Verdict

A complex polarization keeps the affine commutator with its orientation. It
passes the information-loss test that killed Robertson in Phase 178. Its
positive square, however, necessarily contains the square of the prime-shift
operator. That square produces diagonal mass and all ratio frequencies
log(m/n). They are absent from the Weil form and cannot be removed while
retaining Hilbert positivity except by the previously excluded
Clifford/Schur mechanisms. The oriented current is PROVED; closure by this
complex square is NO-GO.

## 1. The oriented square identity

Let X=X* and B=B* preserve a common core. Then

\[
 \boxed{
 \|(X+iB)F\|^2
 =\|XF\|^2+\|BF\|^2+i\langle F,[X,B]F\rangle.}       \tag{1.1}
\]

The sign of the last term reverses for X-iB. Unlike Robertson's inequality,
(1.1) retains the commutator linearly. This follows by direct expansion.

## 2. Exact prime current

On L2(R), let tau_a F(t)=F(t-a), so

\[
 [X,\tau_a]=-a\tau_a.                                   \tag{2.1}
\]

For a finite real coefficient family c_n, put

\[
 B_c={1\over2i}\sum_n c_n(\tau_{\log n}-\tau_{-\log n}). \tag{2.2}
\]

This is self-adjoint, and (2.1) gives

\[
 \boxed{
 i[X,B_c]
 =-{1\over2}\sum_n c_n\log n,
       (\tau_{\log n}+\tau_{-\log n}).}                \tag{2.3}
\]

Thus the Euler-logarithm coefficients

\[
 c_{p^k}={2\over k}p^{-k/2},\qquad c_n=0\quad(n\ne p^k),
\]

give `c_{p^k} log(p^k)=2(log p)p^{-k/2}` and therefore produce exactly the
oriented Hermitian von Mangoldt current, up to the fixed global sign. This is
the bounded sine-shift form of [H,V_p]=(log p)V_p.

## 3. The unavoidable ratio comb

The other arithmetic term in (1.1) is

\[
 B_c^2=-{1\over4}\sum_{m,n}c_mc_n
 (\tau_{\log(mn)}-\tau_{\log(m/n)}
  -\tau_{\log(n/m)}+\tau_{-\log(mn)}).                 \tag{3.1}
\]

For m different from n, this contains ratio frequencies
plus-or-minus log(m/n), including cross-prime pairs. For m=n it contains a
nonzero identity component.

### Theorem 1 (support obstruction). PROVED

Assume `c_n>=0`, as for the physical Euler-logarithm coefficients, and that
two multiplicatively independent integers m,n have nonzero coefficients. For
each positive rational r, the coefficient of `tau_{log r}` coming from the
ratio slots of (3.1) is

\[
 {1\over4}\sum_{u/v=r}c_uc_v\ge0.                       \tag{3.2}
\]

It is strictly positive when r=m/n. Thus ratio collisions reinforce one
another and cannot cancel. Removing every nonintegral ratio would require at
most one multiplicative ray to carry the coefficients, contrary to the
presence of two primes. Lambda*1=log controls product fibers dm=k and supplies
no relation that changes the positive sum (3.2).

This follows immediately from collecting equal translations in (3.1). It is
the ratio-collision obstruction of the finite PC calculations, now forced
directly by positivity of the complex square.

## 4. Why the standard repairs return to previous no-go theorems

1. Subtracting B_c^2 recovers the linear current but destroys positivity.
2. If an auxiliary positive block has Schur complement cancelling B_c^2,
   R170_861 makes the extension a triangular congruence of the physical
   operator and a positive block.
3. Anticommuting Clifford labels cancel cross-prime terms, but this is exactly
   114_d_18; its archimedean boundary is the Real-chirality defect audited in
   R179 section 7.
4. Treating one prime at a time loses the global sign and is shared by the
   prime-local falsifiers.
5. Projection away from ratio frequencies is not positive on the operator
   square; it is the diagonal-removed CP failure of D.195.

## 5. Contact with the logarithmic-channel audit

Equation (2.3) is the Hermitian sine/cosine form of

\[
 [X,S_N]=-K_N                                             \tag{5.1}
\]

from R162_401. There the log current occurs once on each side of the full
Poisson-cell identity and cancels term by term. Formula (1.1) avoids that
linear cancellation only by retaining B_c^2; Theorem 1 shows why the price is
the ratio comb. The complex polarization displays the two alternatives in one
identity.

## 6. Status

    complex square preserves oriented commutator             PROVED
    affine/logarithmic commutator gives exact prime current   PROVED
    positive square also produces B_c^2                       PROVED
    B_c^2 contains rational-ratio collision comb              PROVED
    Lambda*1=log cancels those ratio fibers                   FALSE
    Schur/Clifford/CP repairs are new                          FALSE
    complex polarization forces R_L F=0                       NO-GO
    row D                                                     OPEN
