# D.253 — The relative Euler factor has a one-negative-square kernel

## Verdict

Although the relative Euler factor \(c_r=b_r/z\) is not Schur (D.252),
its de Branges--Rovnyak kernel has an exact rank-two Krein factorization
with one positive and one negative square.  Thus the correct local system
class is generalized Schur/Pontryagin, not ordinary Schur.

The negative feature is precisely the removed free-delay channel.  This
gives a rigorous system-theoretic meaning to the degree/contact completion
of D.247 and selects the Potapov--Ginzburg transform as the next wiring
operation.  It does not yet prove the D.190 comparison.

## 1. Exact kernel calculation

Let \(0<r<1\),

\[
 b_r(z)={z-r\over1-rz},\qquad c_r(z)={b_r(z)\over z}.
\]

For a scalar function \(s\), write

\[
 K_s(w,z)={1-s(w)^*s(z)\over1-\bar wz}.             \tag{1.1}
\]

The degree-one Blaschke kernel is

\[
 K_{b_r}(w,z)
 ={1-r^2\over(1-r\bar w)(1-rz)}.                   \tag{1.2}
\]

Since \(c_r=b_r/z\), direct algebra gives

\[
 \begin{aligned}
 K_{c_r}(w,z)
 &= {\bar wz-b_r(w)^*b_r(z)
       \over \bar wz(1-\bar wz)}\\
 &= {K_{b_r}(w,z)-1\over\bar wz}.                  \tag{1.3}
 \end{aligned}
\]

Define

\[
 u_r(z)={\sqrt{1-r^2}\over z(1-rz)},\qquad
 v(z)={1\over z}.                                  \tag{1.4}
\]

Then

\[
 \boxed{
 K_{c_r}(w,z)=u_r(w)^*u_r(z)-v(w)^*v(z).
 }                                                   \tag{1.5}
\]

This identity holds for nonzero \(w,z\in\mathbb D\), which is the natural
domain of the meromorphic relative factor.

## 2. The negative index is exactly one

Formula (1.5) shows that every finite Gram matrix of \(K_{c_r}\) has at
most one negative eigenvalue.  It has one negative eigenvalue for a
suitable two-point set because \(u_r\) and \(v\) are linearly independent:
their ratio

\[
 {u_r(z)\over v(z)}={\sqrt{1-r^2}\over1-rz}
\]

is nonconstant.  Choose two distinct points for which the two evaluation
vectors are independent.  In that two-dimensional span, (1.5) is the
pullback of \(\mathrm{diag}(1,-1)\), so its inertia is \((1,1)\).
Consequently \(K_{c_r}\) has exactly one negative square.

Thus \(c_r\) belongs to the generalized Schur class of index one on its
punctured-disk domain.  This conclusion uses only the explicit Euler
factor.

## 3. Interpretation of the two features

The positive feature \(u_r\) is the Julia/Poisson state divided by the
free delay.  The negative feature \(v=z^{-1}\) is exactly the anticausal
unit-delay state introduced when \(b_r\) is divided by \(z\).  Therefore

\[
 \text{positive Poisson delay}
 -\text{free delay}
\]

is represented by a conservative Krein colligation with one negative
state, rather than by a contractive Hilbert colligation.

For several primes the orthogonal sum has one such negative port per
prime.  D.247(4.1) performs a nonlocal port rearrangement: the coherent
linear combination becomes the global degree port and the orthogonal
local information becomes the reduced-contact output.  That rearrangement
must be implemented before the primitive degree port is shorted.

## 4. Potapov--Ginzburg target

Let the local Krein input/output signature be written schematically as

\[
 J_S=I_{\rm Poisson}\oplus(-I_{\rm free}).
\]

After adjoining the D.247 degree/contact completion, seek an explicit
\(J_S\)-unitary system matrix \(\mathcal V_S\).  The
Potapov--Ginzburg transform exchanges the selected negative input and
output ports and, whenever the corresponding pivot is invertible, produces
an ordinary unitary colligation.

The next calculation is therefore finite and algebraic:

1. write the direct sum of (1.5) in the prime basis;
2. apply the exact degree/contact port change from D.247(4.1);
3. compute its Potapov--Ginzburg transform;
4. determine the pivot and its inverse without using row-D positivity;
5. compare the transformed positive kernel with the balanced prime part
   of D.137.

If the pivot fails exactly on the global degree port, keep that port
external and let the two Tate equations short it only after Gamma is
adjoined.  This is the only ordering compatible with D.252.

## 5. Classification

* Kernel formula (1.3)--(1.5): **PROVED ALGEBRAIC IDENTITY**.
* Exactly one negative square for one relative prime factor: **PROVED**.
* Ordinary local Schur realization: **IMPOSSIBLE**, D.252.
* Local generalized-Schur/Pontryagin realization: **CONSTRUCTED AT THE
  KERNEL LEVEL**.
* Degree/contact Potapov--Ginzburg transform: **OPEN**.
* Comparison with D.137/D.190 after Gamma, Tate and support shorting:
  **OPEN**.
* Row D: **OPEN**.

