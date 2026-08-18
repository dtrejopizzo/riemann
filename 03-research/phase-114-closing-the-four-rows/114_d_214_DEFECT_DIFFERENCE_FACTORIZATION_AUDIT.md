# D.214 — The defect-difference factorization is exactly the output gate

## Verdict

The identity \(q=Dh-u\) of D.175 removes the reference harmonic lift from
the non-telescoping return, but attempting to factor \(u\) through
\(D^{1/2}\) does not create a new proof of the sharp Douglas condition.  It
is equivalent to the original output-defect range condition.

Let \(A:H\to K\) be a contraction and put

\[
 D=I-A^*A,
 \qquad D_{\rm out}=I-AA^*.                         \tag{0.1}
\]

For \(y:E\to K\), set \(u=A^*y\).  Then

\[
 \boxed{
 y^*D_{\rm out}^\dagger y
 =y^*y+u^*D^\dagger u
 }                                                     \tag{0.2}
\]

as an equality of extended positive forms.  In particular,

\[
 \boxed{
 yE\subset\mathrm{Dom}\,D_{\rm out}^{\dagger/2}
 \quad\Longleftrightarrow\quad
 uE\subset\mathrm{Dom}\,D^{\dagger/2}.
 }                                                     \tag{0.3}
\]

If \(q=Dh-u\), then

\[
 \boxed{
 u^*D^\dagger u
 =(D^{1/2}h-D^{\dagger/2}q)^*
  (D^{1/2}h-D^{\dagger/2}q).
 }                                                     \tag{0.4}
\]

Thus the harmonic term is completely paid, while the only unresolved
range datum is \(q\in\mathrm{Dom}\,D^{\dagger/2}\).  Factoring \(u\)
instead would merely restate that datum and the original output capacity.

Equations (0.2)--(0.4) are **PROVED OPERATOR IDENTITIES**.  They eliminate
the proposed \(u\)-factor route as a structurally distinct strategy.

## 1. Push-through identity

For \(0<r<1\), the bounded resolvent identity gives

\[
 (I-rAA^*)^{-1}=I+rA(I-rA^*A)^{-1}A^*.              \tag{1.1}
\]

Indeed multiplication by \(I-rAA^*\) on either side reduces (1.1) to the
intertwining relation

\[
 (I-rAA^*)A=A(I-rA^*A).                             \tag{1.2}
\]

Apply (1.1) to \(y\):

\[
 y^*(I-rAA^*)^{-1}y
 =y^*y+r\,u^*(I-rA^*A)^{-1}u.                       \tag{1.3}
\]

Both sides increase as \(r\uparrow1\).  Spectral monotone convergence
proves (0.2), including the value \(+\infty\) when a kernel/range
condition fails.  Finiteness on one side is therefore equivalent to
finiteness on the other, proving (0.3).

The same argument yields the supported-range identity often written

\[
 D_{\rm out}^\dagger=I+AD^\dagger A^*.              \tag{1.4}
\]

Formula (1.4) must be read as a quadratic-form identity with the kernel
conditions supplied by the monotone limit; no unbounded pseudoinverse is
being multiplied outside its domain.

## 2. Exact harmonic cancellation

Assume the D.175 identity

\[
 u=Dh-q.                                             \tag{2.1}
\]

On the supported form domain,

\[
 D^{\dagger/2}u
 =D^{1/2}h-D^{\dagger/2}q.                           \tag{2.2}
\]

Taking the Gram proves (0.4).  Expanded,

\[
 u^*D^\dagger u
 =h^*Dh-2\mathrm{Re}(h^*q)+q^*D^\dagger q.   \tag{2.3}
\]

This is exactly the telescoping identity of D.175.  The first two terms
are finite whenever the harmonic lift is in the reference form domain.
Consequently

\[
 u\in\mathrm{Dom}\,D^{\dagger/2}
 \quad\Longleftrightarrow\quad
 q\in\mathrm{Dom}\,D^{\dagger/2}.              \tag{2.4}
\]

Combining (0.3) and (2.4) proves that all three range statements are
equivalent:

\[
 y\in\mathrm{Dom}\,D_{\rm out}^{\dagger/2}
 \Longleftrightarrow
 u\in\mathrm{Dom}\,D^{\dagger/2}
 \Longleftrightarrow
 q\in\mathrm{Dom}\,D^{\dagger/2}.              \tag{2.5}
\]

## 3. Budget identity

Substitution of (2.3) into (0.2) gives the complete output capacity

\[
 \boxed{
 y^*D_{\rm out}^\dagger y
 =y^*y+h^*Dh-2\mathrm{Re}(h^*q)
   +q^*D^\dagger q.
 }                                                     \tag{3.1}
\]

Therefore the remaining born budget after the direct and harmonic terms
is not an informal margin.  It is the finite form

\[
 \mathcal M_N
 :=I-y^*y-h^*Dh+2\mathrm{Re}(h^*q),          \tag{3.2}
\]

with the identity operator replaced by the normalized born reference if
that reference has not yet been scaled to one.  The cell is accepted
exactly when

\[
 \boxed{
 q^*D^\dagger q\leq\mathcal M_N
 }                                                     \tag{3.3}
\]

and the range condition in (2.5) holds.  This is the correctly normalized
version of the return target in D.213.

## 4. Equality

If (3.3) holds, equality in the enlarged-cell capacity occurs precisely
on vectors \(e\) satisfying

\[
 \langle e,(\mathcal M_N-q^*D^\dagger q)e\rangle=0. \tag{4.1}
\]

The corresponding old-source harmonic component is

\[
 D^{\dagger/2}u e
 =D^{1/2}he-D^{\dagger/2}qe.                         \tag{4.2}
\]

Thus the equality classification is finite after the reference-spectral
shorting of D.211 and contains no independent infinite-tail kernel.  The
actual claim that only the known polar/radical modes occur still depends
on proving (3.3) sharply.

## 5. Classification

* Push-through identity (0.2): **PROVED OPERATOR IDENTITY**.
* Equivalence of the three range conditions (2.5): **PROVED**.
* Harmonic cancellation (0.4): **PROVED**, using D.175.
* Exact remaining budget (3.2)--(3.3): **PROVED EQUIVALENCE**.
* A source-derived estimate proving (3.3): **OPEN**.
* Equality classification beyond (4.1): **OPEN**, dependent on the sharp
  estimate.

