# 106.152 — Poisson-holonomy heat lift and the global completion gate

## 1. Purpose and result

The arithmetic heat source of E101.036 is

\[
 P(t)=\frac1{\sqrt{\pi t}}
 \sum_{p}\log p\sum_{k\geq1}p^{-k/2}
 \exp\!\left(-\frac{(k\log p)^2}{4t}\right),
 \qquad t>0.                                      \tag{1}
\]

The scalar factor \(p^{-k/2}\) looks like the \(k\)-fold return amplitude
of a dissipative prime loop.  The first result below shows that no
nonunitary holonomy is needed: the whole prime tower is the sequence of
moments of one positive probability measure on unitary holonomies.

Consequently every individual prime tower in (1) has an exact realization
as the nonzero-winding part of a positive direct integral of self-adjoint
circle heat kernels.  This supplies an off-diagonal heat kernel and an exact
composition law before the winding-zero term is removed.  The associated
trace is the canonical semifinite trace of the decomposable von Neumann
algebra; it is not the ordinary Hilbert-space trace.

The construction does **not** yet produce the required arithmetic heat
semigroup.  The sum over primes of the winding-zero terms diverges, so the
ordinary trace exists only after a global completion.  Removing the
winding-zero term prime by prime gives the correct scalar \(P(t)\), but it
is a relative trace, and relative traces do not satisfy a semigroup law.
Thus the remaining problem is now a precise global completion problem,
not the local realization of the prime damping.

## 2. The positive holonomy measure

For \(0<r<1\), define the Poisson probability measure on the circle by

\[
 d\mu_r(\theta)
 =\frac{1-r^2}{1-2r\cos\theta+r^2}\,
   \frac{d\theta}{2\pi},
 \qquad -\pi\leq\theta<\pi .                     \tag{2}
\]

### Lemma 2.1 — Exact unitary moments

For every integer \(k\),

\[
 \boxed{
 \int_{-\pi}^{\pi}e^{ik\theta}\,d\mu_r(\theta)
 =r^{|k|}.}                                       \tag{3}
\]

#### Proof

The Poisson kernel has the absolutely convergent Fourier expansion

\[
 \frac{1-r^2}{1-2r\cos\theta+r^2}
 =\sum_{j\in\mathbb Z}r^{|j|}e^{ij\theta}.
\]

Integration against \(e^{ik\theta}d\theta/(2\pi)\) extracts the
coefficient with index \(-k\), which is \(r^{|k|}\).  \(\square\)

Equivalently, multiplication by \(e^{i\theta}\) on
\(L^2(\mathbb T,\mu_r)\) is a unitary \(U_r\) with cyclic vector
\(\mathbf1\) satisfying

\[
 \langle\mathbf1,U_r^k\mathbf1\rangle=r^k,
 \qquad k\geq0.                                  \tag{4}
\]

For a prime \(p\), taking \(r_p=p^{-1/2}\) gives every literal tower weight
\(p^{-k/2}\) without analytic continuation.

## 3. Twisted circle heat kernels

Put \(\ell_p=\log p\).  For a holonomy angle \(\theta\), let
\(A_{p,\theta}\) be the nonnegative self-adjoint Laplacian on the circle of
length \(\ell_p\) with boundary condition

\[
 f(x+\ell_p)=e^{i\theta}f(x).
\]

Its eigenvalues are

\[
 \left(\frac{2\pi m+\theta}{\ell_p}\right)^2,
 \qquad m\in\mathbb Z.                            \tag{5}
\]

The heat kernel before taking the diagonal is

\[
 K_{p,\theta,t}(x,y)
 =\frac1{\sqrt{4\pi t}}
  \sum_{k\in\mathbb Z}
  \exp\!\left(-\frac{(x-y+k\ell_p)^2}{4t}\right)e^{ik\theta}.
                                                        \tag{6}
\]

It satisfies

\[
 K_{p,\theta,t+u}(x,y)
 =\int_0^{\ell_p}K_{p,\theta,t}(x,z)
                     K_{p,\theta,u}(z,y)\,dz           \tag{7}
\]

and is the kernel of the positive contraction
\(e^{-tA_{p,\theta}}\).

### Theorem 3.1 — Exact positive semifinite lift of one prime tower

Let

\[
 \mathcal H_p
 =\int_{\mathbb T}^{\oplus}L^2(\mathbb R/\ell_p\mathbb Z)
   \,d\mu_{p^{-1/2}}(\theta),
 \qquad
 A_p=\int_{\mathbb T}^{\oplus}A_{p,\theta}
   \,d\mu_{p^{-1/2}}(\theta).
                                                        \tag{8}
\]

Let

\[
 \mathcal M_p
 =\int_{\mathbb T}^{\oplus}
 B\!\left(L^2(\mathbb R/\ell_p\mathbb Z)\right)
 d\mu_{p^{-1/2}}(\theta)
\]

and equip it with its canonical semifinite normal trace

\[
 \tau_p(T)=\int_{\mathbb T}
 \operatorname{Tr}(T_\theta)\,d\mu_{p^{-1/2}}(\theta)
\]

for positive decomposable \(T\).  Then \(A_p=A_p^*\geq0\),
\(e^{-tA_p}\) is a positive contraction and is \(\tau_p\)-trace-class for
\(t>0\), with

\[
 \boxed{
 \tau_p(e^{-tA_p})
 =\frac{\ell_p}{\sqrt{4\pi t}}
  \left[1+2\sum_{k\geq1}p^{-k/2}
  e^{-(k\ell_p)^2/(4t)}\right].}                  \tag{9}
\]

#### Proof

The direct integral preserves self-adjointness and nonnegativity.  Taking
the diagonal in (6), integrating over one circle, and then integrating over
\(\theta\) gives

\[
 \frac{\ell_p}{\sqrt{4\pi t}}
 \sum_{k\in\mathbb Z}e^{-(k\ell_p)^2/(4t)}
 \int e^{ik\theta}\,d\mu_{p^{-1/2}}(\theta).
\]

Lemma 2.1 turns the last integral into \(p^{-|k|/2}\), yielding (9).
All exchanges are justified by Gaussian absolute convergence.  \(\square\)

The distinction between \(\tau_p\) and the ordinary trace is essential.
Because the base measure in (8) is non-atomic, a nonzero decomposable
operator is not compact merely because its fibers are trace class.  In
particular \(e^{-tA_p}\) is not an ordinary trace-class operator on
\(\mathcal H_p\).  Formula (9) is a von Neumann trace formula.

Define the winding-zero contribution

\[
 W_p(t)=\frac{\ell_p}{\sqrt{4\pi t}}.              \tag{10}
\]

Equation (9) gives the exact identity

\[
 \boxed{
 \tau_p(e^{-tA_p})-W_p(t)
 =\frac{\log p}{\sqrt{\pi t}}
   \sum_{k\geq1}p^{-k/2}
   e^{-(k\log p)^2/(4t)}.}                        \tag{11}
\]

Summing (11) over primes gives precisely (1).

## 4. Outer factor and the normal-weight obstruction

The Poisson density has the exact outer factor

\[
 a_r(e^{i\theta})
 =\frac{\sqrt{1-r^2}}{1-re^{i\theta}},
 \qquad
 |a_r(e^{i\theta})|^2
 =\frac{1-r^2}{1-2r\cos\theta+r^2}.                \tag{11a}
\]

Let \(m=d\theta/(2\pi)\), and define

\[
 V_r:L^2(\mathbb T,\mu_r)\longrightarrow L^2(\mathbb T,m),
 \qquad V_rf=a_rf.                                  \tag{11b}
\]

### Lemma 4.1 — The local lift changes the normal weight, not the operator

The map \(V_r\) is unitary.  Moreover it commutes fiberwise with every
decomposable operator \(T(\theta)\).  In particular, after identifying the
two direct integrals by \(V_r\),

\[
 V_r A_p^{(\mu_r)}V_r^{-1}=A_p^{(m)}.               \tag{11c}
\]

#### Proof

Equation (11a) gives

\[
 \|V_rf\|_{L^2(m)}^2
 =\int |f|^2|a_r|^2dm
 =\int |f|^2d\mu_r.
\]

The function \(a_r\) and its reciprocal are bounded for fixed \(r<1\), so
\(V_r\) is onto.  Since \(V_r\) is scalar multiplication in the base
variable, it commutes with every fiber operator, proving (11c).  \(\square\)

Consequently the prime contribution is

\[
 \tau_m\!\left((M_{|a_r|^2}-I)e^{-tA_p^{(m)}}\right), \tag{11d}
\]

not a spectral difference between two local self-adjoint generators.  The
operator is the same on both sides of (11c); only the normal weight used to
read its diagonal has changed.

This is a sharp restriction on the global completion.  A direct sum or
unitary identification of the local prime lifts cannot leave a discrete
spectral defect, because each weighted lift is already unitarily equivalent
to the free holonomy lift.  The factors \(a_{p^{-1/2}}\) must enter a
nondecomposable Gamma--prime coupling **before** the trace is taken.

## 5. Why the prime-wise direct sum is only virtual

For every fixed \(t>0\), the right side of (1) converges absolutely.  In
contrast,

\[
 \sum_p W_p(t)
 =\frac1{\sqrt{4\pi t}}\sum_p\log p
 =+\infty.                                        \tag{12}
\]

Hence

\[
 \bigoplus_p e^{-tA_p}
\]

is not trace class.  The finite arithmetic quantity is the relative trace

\[
 \boxed{
 P(t)=\sum_p\bigl(\tau_p(e^{-tA_p})-W_p(t)\bigr),} \tag{13}
\]

not the ordinary trace of the direct-sum semigroup.  Even before summing
over primes, (13) uses a semifinite trace over a continuous holonomy
variable.

The subtraction in (13) is harmless as a scalar identity but fatal to the
naive Mercer argument.  The winding-zero paths are part of every circle
semigroup and cannot be deleted independently while preserving (7): winding
numbers add under path concatenation, and two nonzero windings may concatenate
to winding zero.  Therefore the nonzero-winding sector is not a reducing
subspace of \(A_p\).

This gives the exact local/global division:

\[
 \begin{array}{c|c}
 \text{local prime tower}&\text{positive self-adjoint heat kernel, proved}\\
 \text{sum of nonzero windings}&\text{finite relative trace, proved}\\
 \text{global ordinary trace}&\text{requires joint completion}
 \end{array}                                           \tag{14}
\]

## 6. The completion equation

Let \(H_A(t)\) be the pole--Gamma heat term of E101.036, so that

\[
 H_\Xi(t)=H_A(t)-P(t).                              \tag{15}
\]

An arithmetic heat-kernel realization must now provide one Hilbert space
\(\mathcal H\) and one strongly continuous semigroup \(K_t\) such that

\[
 \boxed{
 \begin{aligned}
 K_0&=I,\\
 K_{t+u}&=K_tK_u,\\
 K_t&=K_t^*\succeq0,\\
 \|K_t\|&\leq1,\\
 K_t&\in\mathcal S_1\quad(t>0),\\
 \operatorname{Tr}K_t&=H_A(t)-P(t).
 \end{aligned}}                                      \tag{16}
\]

The prime part in (16) is no longer an unspecified scalar source: it is the
relative semifinite trace of the explicit kernels (6), averaged by the
positive measures (2).  Thus the remaining construction has two precise
tasks: a joint pole--Gamma completion of the winding-zero channels, and a
cohomological compression of the continuous holonomy fibers to an ordinary
trace-class heat operator.  Both operations must occur without destroying
the circle composition law.

If (16) is achieved, the spectral theorem gives

\[
 K_t=e^{-t\mathcal A},\qquad\mathcal A=\mathcal A^*\geq0.
                                                        \tag{17}
\]

The Laplace identity of E101.036 then gives

\[
 \operatorname{Tr}(\mathcal A+x)^{-1}=g_\Xi(x),
\]

and the trace-class determinant in the variable
\(\lambda=s(1-s)\) is \(2\xi(s)\).  Since \(\xi\) has no real zeros,
this proves RH.

## 7. Nonduplication and the surviving issue

This lift is different from three earlier constructions.

1. E101.036 constructs the scalar arithmetic heat source and proves its
   complete-monotonicity equivalence.  It does not construct the
   off-diagonal kernels (6).
2. Document 106.01 uses translation generators on prime circles to obtain
   the local Euler determinant.  The present construction instead uses a
   positive distribution of unitary holonomies and obtains the exact
   Gaussian heat tower with self-adjoint fibers.
3. Document 106.131 realizes each displacement as a delay line in the Weil
   energy variable.  The present realization is in the heat-time variable
   and keeps the full winding composition law.

The construction also explains why an autocorrelation of scalar prime
coefficients is insufficient.  The quadratic and higher prime interactions
are already encoded as path concatenations inside (7).  Taking the relative
trace before composing deletes the winding-zero returns and loses those
interactions.  The missing operation is therefore not another cumulant or
another prime-wise square.  It is a global completion performed before the
trace.

## 8. Status

Proved:

* the positive Poisson-holonomy representation (2)--(4);
* the self-adjoint twisted-circle kernel and its semigroup law;
* the exact semifinite heat trace formula (9);
* the exact recovery of every ordinary prime-power term in (11);
* the outer-factor unitary equivalence (11a)--(11d);
* absolute convergence of the relative prime sum;
* divergence of the unrenormalized direct-sum trace;
* failure of the nonzero-winding sector to be reducing.

Open:

* construct a nondecomposable Gamma--prime coupling carrying all outer
  factors \(a_{p^{-1/2}}\);
* convert the resulting semifinite relative lift into the ordinary
  trace-class semigroup (16).

The remaining theorem is narrower than the original kernel request: local
prime positivity and local composition are now explicit.  Only the global
conversion of the relative semifinite trace into one ordinary trace remains.
