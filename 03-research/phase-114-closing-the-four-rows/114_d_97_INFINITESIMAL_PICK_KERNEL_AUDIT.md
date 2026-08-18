# D.97 — Infinitesimal Pick kernel of the determinant flow

## Status

The infinitesimal Pick kernel of the scattering chain in D.96 can be
computed exactly from the normal prime--Gamma connection of D.94.  Since
the displacement moves the two reflected determinant lines apart with
relative speed two, the divisor-normalized infinitesimal kernel is one
half of the `a`-derivative.  Its pullback by the A--B--C Mellin transform is
the completed Weil form

\[
 QW(f,g)=\langle M f,C M g\rangle-B_{\rm nuc}(f,g).        \tag{0.1}
\]

The rank-two term is precisely the pair of Tate moments.  On the primitive
kernel it vanishes, leaving `-B_nuc`.  Thus infinitesimal Pick positivity
at the central endpoint is exactly row D.

At finite support the same kernel decomposes as a positive jump energy,
minus its full mass, plus the crossed Tate block.  In round-trip
coordinates it is the difference of two exact squares from D.86.  Neither
decomposition supplies the missing order.  Differentiating the transfer
function in the displacement parameter `a`, or integrating from the safe
edge, adds no monotonicity: propagation of the Schur cone requires
positivity of this same infinitesimal kernel at every intermediate `a`.

This note therefore rules out radial/Loewner differentiation as an
independent proof of D.  It remains valuable because it identifies the
precise source estimate a successful construction must establish.

No RH statement or desired sign is assumed.  The paper is not modified.

## 1. Infinitesimal transfer kernel

Retain

\[
 \Theta_a(z)={\Xi(1/2-a-iz)\over\Xi(1/2+a-iz)}            \tag{1.1}
\]

from D.96 and set

\[
 G_a(z)=-\partial_a\log\Theta_a(z)
 ={\Xi'\over\Xi}(1/2-a-iz)
  +{\Xi'\over\Xi}(1/2+a-iz).                             \tag{1.2}
\]

The Schur kernel on the upper half-plane is

\[
 K_a(z,w)={1-\Theta_a(z)\overline{\Theta_a(w)}
            \over-i(z-\overline w)}.                      \tag{1.3}
\]

Since `partial_a Theta_a=-G_a Theta_a`, differentiation gives

\[
 \partial_aK_a(z,w)
 ={\Theta_a(z)\overline{\Theta_a(w)}
    [G_a(z)+\overline{G_a(w)}]
   \over-i(z-\overline w)}.                               \tag{1.4}
\]

At `a=0`, `Theta_0=1`; hence

\[
 \boxed{
 \partial_aK_a(z,w)|_{a=0}
 ={G_0(z)+\overline{G_0(w)}
   \over-i(z-\overline w)},
 \quad
 G_0(z)=2{\Xi'\over\Xi}(1/2-iz).}                        \tag{1.5}
\]

Thus the endpoint infinitesimal Pick kernel is the Caratheodory kernel of
twice the completed logarithmic derivative.  Define the
divisor-normalized kernel

\[
 \mathcal H_0(z,w):={1\over2}\partial_aK_a(z,w)|_{a=0}.
                                                                    \tag{1.6}
\]

The factor `1/2` is forced: for the model fixed divisor
`Theta_a(z)=(z-lambda-ia)/(z-lambda+ia)`, the derivative in (1.5) is
`2/((z-lambda)(conj(w)-lambda))`, whereas one divisor point has trace
`1/((z-lambda)(conj(w)-lambda))`.  Positivity is unchanged by this positive
normalization.

## 2. Prime--Gamma source expansion

In the absolute-convergence region, logarithmic differentiation of the
completed determinant gives

\[
 {\Xi'\over\Xi}(s)
 ={1\over s}+{1\over s-1}
 -{1\over2}\log\pi+{1\over2}\psi(s/2)
 -\sum_{n\ge2}{\Lambda(n)\over n^s}.                      \tag{2.1}
\]

The first two fractions are the two polar/Tate factors.  The remaining
terms are exactly the Gamma oscillator connection and all prime-power
connections of D.94.  Consequently the boundary distribution of (1.6),
paired with Mellin transforms, is defined by the same nuclear completion
as row C; no zero expansion is needed to define its arithmetic side.

Let

\[
 M(f)=(M_-(f),M_+(f)),
 \qquad C=\begin{pmatrix}0&1\\1&0\end{pmatrix}.            \tag{2.2}
\]

The completed explicit formula and polarization give the exact pullback

\[
 \boxed{
 \mathfrak P_0(f,g)
 :=\langle\mathcal Ff,\mathcal H_0\mathcal Fg\rangle
 =\langle M(f),C M(g)\rangle-B_{\rm nuc}(f,g).}           \tag{2.3}
\]

Here `mathcal F` denotes the centered Mellin--Laplace transform and the
pairing is distributional.  Formula (2.3) contains every `p^k`, the full
Gamma factor, and both polar residues.

On the primitive space

\[
 \mathcal P=\ker M_-\cap\ker M_+                          \tag{2.4}
\]

it reduces to

\[
 \boxed{\mathfrak P_0(f,g)=-B_{\rm nuc}(f,g),
 \qquad f,g\in\mathcal P.}                               \tag{2.5}
\]

Therefore endpoint Pick positivity is not merely related to row D; its
pullback is row D exactly.

## 3. Positive energy, mass and rank two

On a support window `I_T`, D.49 gives

\[
 \mathfrak P_{0,T}(f,f)
 =\langle f,(L_T-m_TI)f\rangle
  +\langle M_Tf,C M_Tf\rangle,                            \tag{3.1}
\]

where

\[
\begin{aligned}
 \langle f,L_Tf\rangle={}&
 \sum_{2\le n\le e^{2T}}{\Lambda(n)\over\sqrt n}
       \|f-S_{\log n}f\|_2^2\\
 &+\int_0^\infty {e^{-r/2}\over1-e^{-2r}}
       \|f-S_rf\|_2^2dr\ge0,                              \tag{3.2}
\end{aligned}
\]

and

\[
 m_T=2\sum_{2\le n\le e^{2T}}{\Lambda(n)\over\sqrt n}+m_0.
                                                                    \tag{3.3}
\]

Thus the desired Pick form is not the positive Dirichlet energy `L_T`.
It is that energy minus the complete local mass, with only a rank-two
boundary correction.  On `ker M_T`, positivity is the sharp spectral-gap
estimate

\[
 \langle f,L_Tf\rangle\ge m_T\|f\|^2.                    \tag{3.4}
\]

No Markov or Dirichlet-form axiom yields (3.4): ordinary Poincare
inequalities remove the constant ground state, whereas (3.4) removes the
two non-`L^2` Tate boundary jets and asks for the exact arithmetic mass.

## 4. Round-trip comparison

The preparation complex of D.86 supplies source-defined maps `r_0` and
`z` and a positive contraction operator `C_T` such that

\[
 4\mathfrak P_{0,T}(f,f)
 =\|r_0(f)\|^2-\|C_T^{1/2}z(f)\|^2                       \tag{4.1}
\]

on the primitive realization.  Equivalently, with

\[
 \mathcal Qf=(r_0(f),C_T^{1/2}z(f)),
 \qquad J=\mathrm{diag}(I,-I),                       \tag{4.2}
\]

\[
 4\mathfrak P_{0,T}(f,g)=\langle\mathcal Qf,J\mathcal Qg\rangle.
                                                                    \tag{4.3}
\]

The ambient block has negative determinant at every nontrivial principal
angle.  Therefore (4.1) is positive exactly when the actual primitive
image satisfies

\[
 \|C_T^{1/2}z(f)\|\le\|r_0(f)\|.                         \tag{4.4}
\]

By Douglas factorization, (4.4) is equivalent to a contractive factor of
the boundary channel through the residual channel.  This is the same gate
found by the Pick kernel, now in source-side Hilbert coordinates.

## 5. Why the safe edge does not propagate automatically

Suppose `Theta_a` is Schur at a safe value.  Formula (1.4) shows that an
infinitesimal change preserves the positive-kernel order only if the
Caratheodory kernel

\[
 H_a(z,w)={G_a(z)+\overline{G_a(w)}
             \over-i(z-\overline w)}                      \tag{5.1}
\]

has the required sign.  Multiplication by
`Theta_a(z)overline(Theta_a(w))` is a congruence on finite Gram matrices;
it cannot create the missing sign.

Integrating (1.4) from the safe edge therefore expresses the difference of
two Schur kernels as an integral of the kernels (5.1).  It proves
monotonicity only after positivity of every `H_a` has been established.
When an off-line zero crosses the line `Re(s)=1/2+a`, `G_a` develops the
pole described in D.96 and its kernel acquires the free-orbit negative
square.

Hence neither differentiation in `a` nor integration from `a=1/2` supplies
an inequality absent from row D.

## 6. Outcome

The Loewner route has produced the exact commutative diagram

\[
 \begin{array}{ccc}
 \text{prime--Gamma normal connection}
 &\longrightarrow&\text{infinitesimal Pick kernel}\\
 \downarrow&&\downarrow\\
 B_{\rm nuc}\text{ plus two Tate jets}
 &\longrightarrow&QW\\
 \end{array}                                               \tag{6.1}
\]

and every arrow is an equality.  The desired sign is not introduced by
any arrow.

A genuinely new step must prove the sharp source estimate (3.4) or the
equivalent contraction (4.4) using an order structure not already defined
by `Xi`, `B_nuc`, or their Pick kernel.  The next admissible audit is the
canonical Markov/ground-state transform of `L_T`: determine whether the
two Tate moment constraints can be converted into an actual two-node
Dirichlet boundary condition whose first eigenvalue is exactly `m_T`.
That would be a source-side theorem; if the required ground state is built
from `Xi`, it is circular.
