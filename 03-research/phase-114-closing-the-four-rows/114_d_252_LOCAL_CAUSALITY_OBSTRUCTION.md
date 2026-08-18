# D.252 — The relative Euler score is not a local Schur defect

## Verdict

The direct-sum/cascade interpretation of D.248 cannot by itself produce
the D.190 Douglas contraction.  The positive Poisson delay of the prime
Blaschke factor is a Schur-system quantity, but the arithmetic score is
the **relative** delay

\[
 (\log p)(P_{p^{-1/2}}-I).
\]

Removing the free unit delay divides the Blaschke factor by the disk
coordinate.  The resulting boundary-unitary function has a pole at the
origin and is not the transfer function of a causal Schur colligation.
Equivalently, its time delay changes sign.  Thus the local prime score is
not a positive transfer-defect kernel.

The four-port degree/contact completion of D.247 remains conservative, but
the degree and contact ports cannot be eliminated prime by prime.  They
must be wired globally together with the two Tate ports and the Gamma
channel.  Proving that this global feedback is well posed and contractive
is substantive; it cannot be inferred from the orthogonal sum of the
local unitary components.

## 1. The relative factor has a pole

Put \(r=p^{-1/2}\) and

\[
 b_r(z)={z-r\over1-rz}.
\]

This is a scalar disk inner function.  The free unit delay has transfer
function \(z\).  The boundary phase whose derivative is the relative
Euler score is therefore represented by

\[
 c_r(z):={b_r(z)\over z}
 ={z-r\over z(1-rz)}.                               \tag{1.1}
\]

Since \(0<r<1\), (1.1) has a nonremovable simple pole at \(z=0\).  Hence
\(c_r\notin H^\infty(\mathbb D)\), and in particular it is not a Schur
function.  No causal unitary colligation with bounded state operator can
have \(c_r\) as its transfer function, because every such transfer
function is analytic and contractive on the disk.

On \(|z|=1\), both \(b_r\) and \(z\) have modulus one, so \(c_r\) is
boundary unitary.  Boundary unitarity therefore does not imply the causal
Schur realization needed for a positive transfer-defect kernel.

## 2. The relative delay changes sign

Writing \(z=e^{i\theta}\), D.248 gives

\[
 -i\partial_\theta\log c_r(e^{i\theta})
 =P_r(e^{i\theta})-1,
 \qquad
 P_r(e^{i\theta})={1-r^2\over1-2r\cos\theta+r^2}.
                                                               \tag{2.1}
\]

Now

\[
 P_r(e^{i\theta})-1
 ={2r(\cos\theta-r)\over1-2r\cos\theta+r^2}.        \tag{2.2}
\]

The denominator is positive and the numerator has the sign of
\(\cos\theta-r\).  It is positive near \(\theta=0\) and negative near
\(\theta=\pi\).  Therefore the relative score is indefinite on every
prime circle.  In particular it cannot equal a kernel diagonal
\(K(z,z)\) for a positive Schur defect kernel.

This is the analytic counterpart of the zero modes found in D.250: the
tangent filters lose precisely the boundary information carried by the
free-delay/contact ports.

## 3. What the orthogonal sum actually proves

The Julia colligation of \(b_r\) proves positivity of

\[
 {1-b_r(w)^*b_r(z)\over1-\bar wz}.
\]

Orthogonal sums over primes and oscillator levels preserve positivity of
the **unsubtracted** local kernels.  They do not implement the subtraction
of the unit delay in (2.1), nor the coherent rank-one degree completion in
D.247.  Consequently their transfer-defect kernel is not yet the balanced
row-D score and cannot be denoted by the \(K_S^{\rm tr}\) required in
D.251(4.2).

The conservation law D.247(4.1)

\[
 \|\widetilde{\mathcal E}_-z\|^2
 +\left|\sum_p\sqrt{\log p}\,z_p\right|^2
 =\|\widetilde{\mathcal E}_+z\|^2
 +\sum_p(\log p)|z_p|^2                            \tag{3.1}
\]

does retain the missing ports.  But (3.1) couples all primes through one
global degree channel.  Closing that channel locally destroys (3.1); on
the primitive kernel it is the source of the desired negative contact
defect.

## 4. The next admissible wiring theorem

Let \(\mathcal U_S^{(4)}\) be the four-port partial isometry of (3.1),
with input ports

\[
 (\text{odd tangent},\text{global degree})
\]

and output ports

\[
 (\text{even tangent},\text{reduced contact}).
\]

Adjoin the paired Gamma systems of D.249, without separating their
divergent free delays.  The next noncircular theorem must construct a
global Redheffer feedback \(\mathfrak F_T\), defined before the sign of
\(B_{\rm nuc}\) is known, such that:

1. its two scalar external ports are exactly the Tate maps \(M_-,M_+\);
2. its position-space external ports are the D.137 maps \(X_T,Y_T\);
3. feedback elimination is well posed on a common compact form core;
4. after imposing \(M_-=M_+=0\), its old/born short is the D.190 block;
5. the remaining transfer operator is contractive by the unitary system
   identity, not by assuming that the D.190 block is positive.

Writing the feedback equations explicitly and eliminating the internal
degree/contact/Gamma ports must either give

\[
 \mathscr R_E^{\rm D190}
 =P_E\Pi_TK_{\mathfrak F_T}^{\rm tr}\Pi_TP_E       \tag{4.1}
\]

or an exact residual.  Equality of boundary phase derivatives is not
enough to prove (4.1).

## 5. Classification

* Pole obstruction (1.1): **PROVED**.
* Sign change of the relative delay (2.2): **PROVED**.
* Local relative Euler score is not a causal Schur defect: **PROVED**.
* Naive orthogonal-sum/cascade closure of D.190: **IMPOSSIBLE**.
* Four-port degree/contact conservation: **PROVED IN D.247**.
* Global Tate--Gamma Redheffer feedback and comparison (4.1): **OPEN**.
* Row D: **OPEN**.

This is a strict reduction: it eliminates the local causal wiring and
leaves only a global four-port feedback construction as the transfer
route.
