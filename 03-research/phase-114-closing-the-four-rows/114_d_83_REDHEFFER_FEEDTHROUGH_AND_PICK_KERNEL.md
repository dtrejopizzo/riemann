# D.83 — Redheffer feedthrough and the exact primitive Pick kernel

## Status

D.82 proposes a two-symbol correction of the Toeplitz edge.  This note
solves its coefficient equations.  The proposed pure Hankel correction does
not exist: for the negative Hardy shift, every displacement
`Y W_+ - W_- Y` has zero `(0,0)` entry, while the prescribed Toeplitz edge
has `(0,0)=-T_(0,0)`.  Already for the single-prime symbol `v_r=b_r/z`,
`T_(0,0)=1-r^2` is nonzero.

The strictly causal tail determines negative Fourier coefficients of a
candidate second symbol, but creates an equal opposite first-column tail.
The two terms in the natural unitary-Hankel commutator are therefore an
inseparable compatible pair.  A full Redheffer colligation supplies the
missing zero-time feedthrough and is contractive as an input-output system,
but its canonical output has not been identified with the Schur landing of
the primitive A--B--C source.

The exact interpolation criterion for that identification is computed.
For primitive tests `F_i`, its Pick matrix is

\[
 \bigl(\langle J_-F_i,J_-F_j\rangle
       -\langle K_+F_i,K_+F_j\rangle\bigr)_{i,j}
 =\bigl(-B_{\rm nuc}(F_i,F_j)\bigr)_{i,j}.
\]

Hence positivity of every required Pick matrix is exactly row D, with all
prime powers and Gamma visible in its entries.  Boundary unitarity proves
positivity of the Redheffer transfer kernel, but the Toeplitz edge prevents
identifying that kernel with the primitive Pick kernel.  The remaining
noncircular target is a causal landing theorem for the actual primitive
data, including the feedthrough channel.

No RH or sign-defined interpolation is used.  The paper is not modified.

## 1. The constrained displacement equation

Retain the Hardy decomposition and unitary multiplier of D.82:

\[
 U=M_\Theta=\begin{pmatrix}T&G\\H&R\end{pmatrix},
 \qquad T=PUP.                                             \tag{1.1}
\]

For a window shift `W`, the canonical Hankel block satisfies

\[
 HW_+-W_-H=-QUQWP+QWPT.                                   \tag{1.2}
\]

D.82 asks for a second Hankel operator `Y=H_Psi` solving

\[
 YW_+-W_-Y=-QWPT.                                         \tag{1.3}
\]

If (1.3) existed, adding it to (1.2) would remove the Toeplitz edge while
retaining the transported annulus.  We now solve (1.3) at one Hardy
boundary.

## 2. Exact coefficient obstruction

Use the bases

\[
 e_n=z^n\quad(n\ge0),
 \qquad f_m=z^{-m-1}\quad(m\ge0),                          \tag{2.1}
\]

and take `W=M_(z^-1)`.  Then

\[
 W_+e_0=0,
 \quad W_+e_n=e_{n-1}\ (n\ge1),
 \quad W_-f_m=f_{m+1},                                    \tag{2.2}
\]

while

\[
 E:=QWP,
 \qquad Ee_0=f_0,
 \qquad Ee_n=0\ (n\ge1).                                 \tag{2.3}
\]

Let `Y=(y_(m,n))` be any operator from `H^2_+` to `H^2_-`.  Directly from
(2.2),

\[
 (YW_+-W_-Y)_{0,0}=0.                                     \tag{2.4}
\]

On the other hand,

\[
 (-ET)_{0,0}=-T_{0,0}.                                    \tag{2.5}
\]

Therefore:

> **Theorem 2.1 (feedthrough obstruction).**  Equation (1.3) has no
> solution, bounded or unbounded on the algebraic Hardy core, whenever
> `T_(0,0) != 0`.  The obstruction is the zero-time Toeplitz coefficient,
> which is outside the range of the shift derivation
> `Y mapsto YW_+-W_-Y`.

For a Hankel matrix

\[
 y_{m,n}=\widehat\Psi(-m-n-1),                              \tag{2.6}
\]

the remaining boundary equations are even more restrictive:

\[
 \begin{aligned}
 (YW_+-W_-Y)_{0,n}&=\widehat\Psi(-n) &&(n\ge1),\\
 (YW_+-W_-Y)_{m,0}&=-\widehat\Psi(-m)&&(m\ge1).            \tag{2.7}
 \end{aligned}
\]

Matching the first row of `-ET` would impose

\[
 \widehat\Psi(-n)=-T_{0,n},                               \tag{2.8}
\]

whereas its zero first column would impose

\[
 \widehat\Psi(-m)=0.                                      \tag{2.9}
\]

Thus even after deleting the `(0,0)` coefficient, the same tail is required
both to be `-T_(0,n)` and zero.  A scalar Hankel symbol cannot cancel one
edge of the compatible pair (1.2) independently of the other.

## 3. Application to one prime

For

\[
 v_r(z)={1-rz^{-1}\over1-rz}
 =-rz^{-1}+(1-r^2)\sum_{n\ge0}r^nz^n,                     \tag{3.1}
\]

the Toeplitz block has

\[
 T_{0,0}=\widehat v_r(0)=1-r^2\ne0.                        \tag{3.2}
\]

Therefore Theorem 2.1 applies before taking a product over primes.  The
first strictly causal coefficient would be

\[
 \widehat\Psi(-1)=-T_{0,1}
 =-\widehat v_r(-1)=r,                                    \tag{3.3}
\]

but (2.7) would then create the unwanted first-column coefficient `-r`.

The obstruction is not caused by Gamma, convergence of the Euler product,
or a choice of cutoff.  It is the zero-time coefficient of the local
Frobenius/torsor colligation.

## 4. Full unitary Redheffer colligation

The missing zero-time channel is normally handled by the feedthrough block
of a conservative system.  For the unitary colligation (1.1), define state,
input and output sequences by

\[
 \begin{aligned}
 x_{n+1}&=Tx_n+Gu_n,\\
 y_n&=Hx_n+Ru_n.                                           \tag{4.1}
 \end{aligned}
\]

Unitarity gives the exact energy identity

\[
 \|x_n\|^2+\|u_n\|^2
 =\|x_{n+1}\|^2+\|y_n\|^2.                               \tag{4.2}
\]

For zero initial state, summation gives

\[
 \sum_{n=0}^N\|y_n\|^2
 \le\sum_{n=0}^N\|u_n\|^2.                               \tag{4.3}
\]

The transfer function

\[
 \Phi(z)=R+zH(I-zT)^{-1}G                                 \tag{4.4}
\]

is therefore Schur.  Its de Branges--Rovnyak kernel

\[
 K_\Phi(z,w)
 ={I-\Phi(z)\Phi(w)^*\over1-z\overline w}                 \tag{4.5}
\]

is positive.  This is a genuine norm-one result obtained from the full
Poisson unitary, not from row D.

It concerns the canonical output in (4.1).  To prove row D one must also
show that, for the input determined by the negative primitive frame,

\[
 u(F)=\mathcal J_-(F),                                     \tag{4.6}
\]

the output of (4.1) is exactly

\[
 y(F)=\mathcal K_+(F).                                     \tag{4.7}
\]

The failed equation (1.3) is precisely the attempted zero-state proof of
this landing.

## 5. Energy defect for a forced landing

Suppose a proposed state sequence has residual

\[
 r_n=x_{n+1}-Tx_n-Gu_n.                                   \tag{5.1}
\]

Keeping the colligation output `y_n=Hx_n+Ru_n`, (4.2) becomes

\[
 \begin{aligned}
 \|y_n\|^2-\|u_n\|^2
 ={}&\|x_n\|^2-\|x_{n+1}\|^2\\
 &+2\operatorname {Re}\langle x_{n+1},r_n\rangle
   -\|r_n\|^2.                                            \tag{5.2}
 \end{aligned}
\]

Thus a nonzero landing cocycle is not harmless: after telescoping the state
energy it leaves the exact forcing term

\[
 \boxed{
 \sum_n\left(2\operatorname {Re}\langle x_{n+1},r_n\rangle
              -\|r_n\|^2\right).}                         \tag{5.3}
\]

For the Hardy window, `r_n` contains the feedthrough and first-column
defects (2.5)--(2.9).  Setting it to zero is the causal landing theorem
which has not followed from primitivity.

## 6. Exact primitive Pick matrix

Let

\[
 x_F=\mathcal J_-(F),
 \qquad y_F=\mathcal K_+(F).                               \tag{6.1}
\]

For finitely many primitive tests `F_1,...,F_N`, a contraction sending
`x_(F_i)` to `y_(F_i)` exists on their span if and only if the Gram/Pick
matrix

\[
 \mathfrak P(F_1,\ldots,F_N)
 =\left(
 \langle x_{F_i},x_{F_j}\rangle
 -\langle y_{F_i},y_{F_j}\rangle
 \right)_{i,j}                                             \tag{6.2}
\]

is positive semidefinite.  D.80 gives the exact polarized identity

\[
 \boxed{
 \mathfrak P(F_1,\ldots,F_N)
 =\bigl(-B_{\rm nuc}(F_i,F_j)\bigr)_{i,j}.}                \tag{6.3}
\]

Its entries are

\[
 \begin{aligned}
 -B_{\rm nuc}(F_i,F_j)
 ={}&-\sum_p\log p\sum_{k\ne0}p^{-|k|/2}
       \langle F_i,S_{k\log p}F_j\rangle\\
 &-m_0\langle F_i,F_j\rangle
 +\langle\partial_\infty F_i,
          \partial_\infty F_j\rangle.                    \tag{6.4}
 \end{aligned}
\]

Thus every prime power and the full Gamma oscillator occur in the Pick
kernel itself.

Positivity of (6.3) for every finite family is equivalent to

\[
 B_{\rm nuc}(F,F)\le0
 \quad\text{for every primitive }F.                        \tag{6.5}
\]

Indeed, matrix positivity implies the diagonal case; conversely (6.5)
applied to every linear combination of the `F_i` gives (6.3).  Therefore
the complete Pick criterion is exactly row D.

## 7. Why the automatic Redheffer kernel is not the primitive kernel

The kernel (4.5) is positive unconditionally.  If there were source maps
`z_F` such that

\[
 -B_{\rm nuc}(F,G)
 =\langle K_\Phi(\cdot,\cdot)z_F,z_G\rangle,               \tag{7.1}
\]

then row D would follow.  The natural attempt to construct `z_F` is the
causal state recursion (4.1).  The coefficient calculation in Sections
2--3 shows exactly why it fails: its windowed displacement misses the
feedthrough `T_(0,0)` and ties the first-row and first-column tails with
opposite signs.

Equivalently, the primitive Pick kernel (6.3) differs from the pullback of
the automatic Redheffer kernel by the forcing form (5.3).  Retaining that
form preserves (6.4); discarding it produces a positive kernel but changes
`B_nuc`.

## 8. Nehari audit

If one ignores the zero-time obstruction and prescribes only the first-row
tail (2.8), the negative Fourier coefficients of `Psi` are fixed.  Nehari's
theorem gives

\[
 \inf_{a\in H^\infty}\|\Psi+a\|_\infty
 =\|H_\Psi\|.                                              \tag{8.1}
\]

For the single-prime tail (3.3), the minimal Hankel has rank one and norm
`r<1`.  Nevertheless it does not solve (1.3), because it creates the
opposite first-column coefficient and leaves `T_(0,0)=1-r^2` untouched.

Thus the scalar Nehari bound is not the missing estimate.  The constrained
problem is a feedthrough interpolation problem.  Its exact finite-data
criterion is the Pick matrix (6.3), whose positivity is row D.

## 9. Surviving noncircular target

The full unitary colligation suggests one precise theorem which would close
the gap without defining a contraction from (6.3):

> **Causal primitive landing theorem.**  Construct, functorially from the
> semilocal Poisson relation, a zero-initial-state solution of (4.1) whose
> input is `J_-F` and whose output is `K_+F` for every primitive `F`, with
> the directed window and nuclear trace limits compatible.

If this theorem holds, (4.3) gives row D and (6.4) proves that the result is
the exact A--B--C form.  The theorem cannot be replaced by the pure Hankel
equation (1.3); Theorem 2.1 proves that equation inconsistent.

## 10. Conclusion

The constrained two-symbol equation of D.82 has been resolved: it has no
solution because the Toeplitz edge contains a nonzero zero-time
feedthrough, and its causal tail violates the row/column compatibility of a
Hankel displacement.

The complete Redheffer colligation is unitary and has a positive transfer
kernel, but identifying its canonical input-output map with the primitive
Schur landing is an additional theorem.  The exact Pick matrix for that
theorem is `(-B_nuc(F_i,F_j))`; its entries contain all `p^k` and Gamma, and
its positivity is exactly row D.  The next route must therefore construct
the causal primitive landing from Poisson geometry, not invoke abstract
Nehari or Pick existence.

