# 106.46 — The nonlocal Green flux and the Evans boundary channel

## Purpose

The one-tail residue matrix of 106.45 supplies stable and unstable
asymptotic polarizations, but it does not impose the global matching
condition. This note constructs the exact conserved flux for the complete
ordinary-prime--Gamma generator. It determines the boundary space on which
a global Evans object must act.

The result is an exact Green identity. It also shows that the matching
object is not a scalar two-by-two Wronskian: the continuous Gamma jumps and
the infinitely many prime-power jumps crossing a spatial cut produce an
infinite-dimensional boundary channel.

## 1. Symmetric edge measure

Let

\[
 d\nu_\zeta(u)=
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}(du)
 \frac{e^{-u/2}}{1-e^{-2u}}\,du,\qquad u>0.           \tag{1}
\]

Define a symmetric measure \(\mathfrak j\) on
\(\mathbb R^2\setminus\{x=y\}\) by

\[
\begin{aligned}
 \iint\Phi(x,y)\,d\mathfrak j(x,y)
 :=\frac12\int_0^\infty\int_{\mathbb R}
 &K(x)K(x-u)\\
 &\times\{\Phi(x,x-u)+\Phi(x-u,x)\}\,dx\,d\nu_\zeta(u).
                                                               \tag{2}
\end{aligned}
\]

Then \(\mathfrak j\) is positive and invariant under
\((x,y)\mapsto(y,x)\). Moreover,

\[
 \mathscr E_K(f,g)
 =\iint(\overline{f(x)}-\overline{f(y)})
       (g(x)-g(y))\,d\mathfrak j(x,y).                \tag{3}
\]

The diagonal singularity from Gamma is harmless in (3), because the
difference product is \(O(|x-y|^2)\), while its density is
\(O(|x-y|^{-1})\).

## 2. Generator and local Green identity

Recall

\[
 d\mu_K(x)=\frac{h(x)K(x)}{c_K}\,dx,\qquad c_K=\frac12. \tag{4}
\]

On the smooth form core, the generator is characterized by

\[
 \langle f,Lg\rangle_{\mu_K}=\mathscr E_K(f,g).       \tag{5}
\]

Symmetry of \(\mathfrak j\) gives the pointwise weak formula

\[
 (Lg)(x)\,d\mu_K(x)
 =2\int_{\mathbb R}(g(x)-g(y))\,d\mathfrak j(x,y).   \tag{6}
\]

For \(X\in\mathbb R\), put

\[
 \Omega_X=(-\infty,X],\qquad \Omega_X^c=(X,\infty).  \tag{7}
\]

### Theorem 1 — Nonlocal Green formula

For all smooth form-core functions \(f,g\),

\[
\boxed{
\begin{aligned}
 &\int_{\Omega_X}
 \left((Lf)(x)\overline{g(x)}
       -f(x)\overline{(Lg)(x)}\right)d\mu_K(x)\\
 &\qquad =
 2\iint_{\Omega_X\times\Omega_X^c}
 \left(f(x)\overline{g(y)}
       -f(y)\overline{g(x)}\right)d\mathfrak j(x,y).
                                                               \tag{8}
\end{aligned}}
\]

#### Proof

Insert (6) in the left side. The contribution from
\(\Omega_X\times\Omega_X\) is antisymmetric under exchange of \(x\) and
\(y\), hence vanishes. The two remaining orientations are equal after the
same exchange and give the factor two in (8). All integrals are absolutely
convergent after a common small-jump cutoff; the difference cancels the
Gamma singularity, and monotone/dominated convergence removes the cutoff.
\(\square\)

Define the flux

\[
 \boxed{
 W_X(f,g)=
 2\iint_{\Omega_X\times\Omega_X^c}
 \left(f(x)\overline{g(y)}
       -f(y)\overline{g(x)}\right)d\mathfrak j(x,y).} \tag{9}
\]

If \(Lf=\lambda f\) and \(Lg=\eta g\), then

\[
 \boxed{
 W_X(f,g)=(\lambda-\overline\eta)
 \int_{\Omega_X}f(x)\overline{g(x)}\,d\mu_K(x).}      \tag{10}
\]

In particular, the flux of two solutions at the same real spectral
parameter is independent of the cut and equals zero whenever both are
global form-domain solutions.

## 3. The actual boundary channel

Let

\[
 d\mathfrak j_X
 =\mathbf1_{\Omega_X\times\Omega_X^c}\,d\mathfrak j. \tag{11}
\]

The natural boundary Hilbert space is

\[
 \mathscr B_X=L^2(\Omega_X\times\Omega_X^c,\mathfrak j_X). \tag{12}
\]

The trace of a function on crossing edges is the ordered pair

\[
 \Gamma_Xf=(f(x),f(y))_{x\le X<y}.                    \tag{13}
\]

The flux (9) is the canonical skew form on these traces. For each prime
power \(n\), \(\mathscr B_X\) contains the interval of edges

\[
 \{(x,x+\log n):X-\log n<x\le X\},                   \tag{14}
\]

and Gamma contributes all crossing displacements \(u>0\). Thus
\(\mathscr B_X\) is infinite-dimensional.

The Gamma mass crossing a cut is locally finite. Indeed, for \(0<u<1\),
the set of starting points whose \(u\)-edge crosses \(X\) has length \(u\),
while the Gamma density is \(1/(2u)+O(1)\). Hence

\[
 \int_0^1 u\frac{e^{-u/2}}{1-e^{-2u}}\,du<\infty.    \tag{15}
\]

The large-displacement crossing mass is finite because one of the two
theta factors is double-exponentially small. Therefore (9) is a genuine
boundary pairing, not a formal divergent Wronskian.

## 4. Evans operator rather than scalar Evans function

Fix \(0<\lambda<1/2\). Let \(\mathscr S_X^-(\lambda)\) denote the boundary
traces of solutions of \((L-\lambda)f=0\) on \(\Omega_X\) satisfying the
left form-domain condition, and let \(\mathscr S_X^+(\lambda)\) denote the
corresponding right traces. A global subthreshold state exists exactly when

\[
 \mathscr S_X^-(\lambda)\cap\mathscr S_X^+(\lambda)\ne\{0\}. \tag{16}
\]

Consequently the correct matching object is a pair of closed subspaces, or
equivalently the difference of their Calderón projections,

\[
 \boxed{\mathcal E_X(\lambda)
 =P_{\mathscr S_X^-(\lambda)}
  -P_{\mathscr S_X^+(\lambda)}.}                     \tag{17}
\]

A scalar Fredholm determinant can be attached to (17) only after proving
that the two projections form a Fredholm pair, for example

\[
 P_{\mathscr S_X^-(\lambda)}
 -P_{\mathscr S_X^+(\lambda)}\in\mathfrak S_2
 \quad\text{relative to a fixed reference polarization}.       \tag{18}
\]

Neither (18) nor an equivalent compactness statement follows merely from
the finite crossing mass (15). It requires a resolvent estimate for the
half-line nonlocal problem.

## 5. Consequences for the global program

The old finite Euler perturbation determinants are not used here. The
operator (17) is built from the already completed ordinary-prime--Gamma
generator, and the prime lattices remain edge channels rather than
off-real eigenvalues of a finite self-adjoint system.

The next required theorem is now analytic and precise:

> **Half-line Fredholm theorem.** For every compact
> \(J\Subset(0,1/2)\), the left and right Cauchy-data spaces form a
> Fredholm pair in \(\mathscr B_X\), locally uniformly for
> \(\lambda\in J\), after the exact threshold radical is shorted out.

Once this theorem is proved, one may define a regularized Evans determinant
whose zeros, with multiplicity, are exactly the global subthreshold
eigenvalues. Proving its nonvanishing remains the arithmetic matching step.

