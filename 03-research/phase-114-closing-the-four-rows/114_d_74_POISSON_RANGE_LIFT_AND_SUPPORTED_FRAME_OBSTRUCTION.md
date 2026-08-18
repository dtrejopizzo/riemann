# D.74 — The Poisson range lift, its exact cokernel, and the supported-frame obstruction

## Status

This note carries out the range/lift comparison left open in D.73.  It
constructs a canonical lift on the **actual Poisson relation space**, proves
that its two boundary jets are exactly the two Tate moments used by A--B--C,
and computes the pullback of Meyer's nuclear character.  The pullback is the
full form `B_nuc`, term by term for every `p^k` and for the complete Gamma
factor.

The construction also gives a sharp negative result.  The range lift is a
topological Frechet lift, not a supported Hilbert lift.  Its cokernel is
exactly Meyer's odd object.  On the critical `L^2` boundary the same range is
dense and nonclosed, so its Moore--Penrose inverse is unbounded and the
cokernel collapses.  Passing instead through finite periodic frames does not
repair this: a nonzero translation-covariant convolution realization cannot
be simultaneously exact, `L^2`, and compactly supported.

Thus the two jets and the exact `B_nuc` pullback are now completely
identified.  What is not proved is the further equality with the supported
compression form of D.73(6.4).  That equality would supply the missing sign
and is not asserted here.  No RH, zero location, Weil positivity, or spectral
polarization is used.  The paper is not modified.

## 1. The two quotient jets are the two Tate moments

Let `H_+` be Meyer's even Schwartz source and

\[
 \mathcal H_\cap
 =\{\varphi\in\mathcal H_+:\varphi(0)=\mathcal F\varphi(0)=0\}.
                                                               \tag{1.1}
\]

The quotient map is

\[
 q_+:\mathcal H_+\longrightarrow\mathbb C(0)\oplus\mathbb C(1),
 \qquad q_+(\varphi)=(\varphi(0),\mathcal F\varphi(0)).          \tag{1.2}
\]

Its kernel is (1.1).  It is onto: two even Hermite functions with distinct
Fourier eigenvalues have linearly independent pairs in (1.2).  Hence

\[
 0\longrightarrow\mathcal H_\cap\longrightarrow\mathcal H_+
 \xrightarrow{q_+}\mathbb C(0)\oplus\mathbb C(1)
 \longrightarrow0                                             \tag{1.3}
\]

is an exact sequence of Frechet scaling modules.  The two one-dimensional
quotients have scaling characters `x^0` and `x^1`.  Therefore an integrated
multiplicative test `a` acts on them by

\[
 \rho_+^0(a)=
 \begin{pmatrix}\widehat a(0)&0\\0&\widehat a(1)\end{pmatrix}.
                                                               \tag{1.4}
\]

Under the central logarithmic change

\[
 F(t)=e^{t/2}a(e^t),                                          \tag{1.5}
\]

D.32 gives

\[
 M_-(F)=\widehat a(0),\qquad M_+(F)=\widehat a(1),             \tag{1.6}
\]

and, equivalently,

\[
 M_-(F)=\widehat F(-i/2),\qquad M_+(F)=\widehat F(i/2).        \tag{1.7}
\]

> **Theorem 1.1 (jet identification).**  The two boundary coordinates of
> Meyer's even Poisson quotient are exactly the two ruling/Tate moments of
> A--B--C.  In particular
> \[
> a\in\mathcal T^0
> \quad\Longleftrightarrow\quad
> \rho_+^0(a)=0
> \quad\Longleftrightarrow\quad M_-(F)=M_+(F)=0.               \tag{1.8}
> \]

This is an equality of scaling characters, not a choice of two linear
functionals after the fact.

## 2. The canonical Frechet range lift

Let `H_-` be Meyer's weighted Schwartz target and let

\[
 Z\varphi(x)=\sum_{n\ge1}\varphi(nx).                         \tag{2.1}
\]

Meyer's closed-range theorem gives a topological isomorphism

\[
 Z:\mathcal H_\cap\xrightarrow{\sim}Z\mathcal H_\cap
 \subset\mathcal H_-.                                        \tag{2.2}
\]

D.42 constructs the intrinsic two-chart Gamma line
`L_gamma^0` and the characteristic isomorphism

\[
 \sigma_\zeta:\mathcal L_\gamma^0
 \xrightarrow{\sim}Z\mathcal H_\cap,\qquad
 (u_+,u_-)\longmapsto \zeta(s)u_+(s)=\zeta(1-s)u_-(s).        \tag{2.3}
\]

Consequently there is a canonical continuous range lift

\[
 \boxed{
 \mathscr L_{\rm ran}:=Z^{-1}\sigma_\zeta:
 \mathcal L_\gamma^0\xrightarrow{\sim}\mathcal H_\cap.}     \tag{2.4}
\]

It is canonical because both arrows are inverse maps in source-defined
closed-range theorems; no complement of `Z H_cap` is chosen.  It commutes
with scaling and with every finite residue projection.  Multiplying (2.4)
by `Z` recovers the prescribed two-chart Poisson relation exactly.

The range and cokernel are therefore not unknown:

\[
 \boxed{
 0\longrightarrow\mathcal L_\gamma^0
 \xrightarrow{\sigma_\zeta}\mathcal H_-
 \longrightarrow V\longrightarrow0,
 \qquad V=\mathcal H_-/(Z\mathcal H_\cap).}                   \tag{2.5}
\]

> **Theorem 2.1 (range--cokernel theorem).**  The maximal Poisson lift
> supplied by the present A--B--C data is the Frechet isomorphism (2.4).
> Its obstruction to being a lift onto all of `H_-` is exactly the odd
> nuclear object `V`; there is no additional algebraic cokernel hidden in
> the Gamma gluing.

In particular a right inverse on all of `H_-` would split (2.5), while the
construction needed in D.73 must retain `V`, since row C takes its odd trace
on this very quotient.

## 3. Exact pullback of the nuclear character

Let `rho_+^0` denote the even quotient representation (1.4), and let `rho_-^0`
be the induced scaling representation on `V`.  Meyer's character theorem is

\[
 \chi_M(h)=\operatorname {Tr}_{\rm nuc}\rho_+^0(h)
            -\operatorname {Tr}_{\rm nuc}\rho_-^0(h).          \tag{3.1}
\]

For `h=a\star b^\vee`, the A--B--C realization theorem identifies (3.1)
with the diagonal nuclear form

\[
 \boxed{B_{\rm nuc}(a,b)=\chi_M(a\star b^\vee).}              \tag{3.2}
\]

If `a,b` are primitive, Theorem 1.1 kills the even term, so

\[
 B_{\rm nuc}(a,b)
 =-\operatorname {Tr}_{\rm nuc}\rho_-^0(a\star b^\vee).       \tag{3.3}
\]

This is the exact trace pullback through the range--cokernel triangle.  To
see that no local term is hidden, put `U_p=S_(log p)` and

\[
 A_p=\sqrt{1-p^{-1}}(I-p^{-1/2}U_p)^{-1}.                    \tag{3.4}
\]

The norm-convergent Poisson-kernel expansion gives

\[
 A_p^*A_p-I=\sum_{k\ne0}p^{-|k|/2}U_p^k.                     \tag{3.5}
\]

Thus, under (1.5), polarization of (3.2) is

\[
 \begin{aligned}
 B_{\rm nuc}(F,G)={}&
 \sum_p\log p\sum_{k\ne0}p^{-|k|/2}
       \langle F,S_{k\log p}G\rangle\\
 &+m_0\langle F,G\rangle
   -\langle\partial_\infty F,\partial_\infty G\rangle,
 \end{aligned}                                               \tag{3.6}
\]

where

\[
 m_0=\log\pi-\psi(1/4),                                     \tag{3.7}
\]

and

\[
 \langle\partial_\infty F,\partial_\infty G\rangle
 =\int_0^\infty{e^{-r/2}\over1-e^{-2r}}
  \langle F-S_rF,G-S_rG\rangle\,dr.                          \tag{3.8}
\]

For compact support, (3.6) is the stabilized paired difference.  For a
fixed window only primes `p<=e^(2T)` and powers with `k log p<=2T` meet the
window; all other correlations vanish by support, not by truncation.

> **Theorem 3.1 (complete trace comparison).**  The Meyer range--cokernel
> character pulls back to `B_nuc` with:
>
> 1. both primitive jets equal to the two A--B--C moments;
> 2. every power `p^k` carrying the coefficient
>    `Lambda(p^k)/sqrt(p^k)`;
> 3. the entire Gamma oscillator, including its finite-part constant.
>
> No asymptotic or scalar normalization remains in this comparison.

The theorem is a trace identity.  A nuclear supertrace on a Frechet
cokernel is not a positive Hilbert trace, so (3.3) alone has no sign.

## 4. Why Moore--Penrose cannot turn the range lift into D.73(6.4)

There are two available topologies, and they fail in complementary ways.

### 4.1. Intrinsic Frechet topology

In the intrinsic topology the range `Z H_cap` is closed and (2.4) is a
continuous inverse on it.  But a Frechet space has no canonical orthogonal
complement, adjoint, or minimum-norm section.  Choosing a Hilbert seminorm
and completing it changes the category and must be shown compatible with
scaling, the nuclear trace, and the directed support system.  None of these
properties follows from the open mapping theorem.

### 4.2. Critical-boundary `L^2` topology

In the ordinary critical-boundary Hilbert completion, multiplication by the
characteristic section has dense, nonclosed range.  The quotient in (2.5)
therefore collapses to zero after Hausdorff completion, although the Frechet
cokernel `V` is nonzero.  For a bounded operator between Hilbert spaces the
Moore--Penrose inverse is bounded exactly when the range is closed.  Hence

\[
 \boxed{(Z|_{\mathcal H_\cap})^\dagger
 \text{ is unbounded in the critical }L^2\text{ completion}.} \tag{4.1}
\]

This is not repaired by restricting to the two primitive jets: those jets
define `H_cap`, the domain already present in (4.1).

For completeness, density is D.41's multiplication-range theorem: the
critical traces of `E` contain all Gaussian translates densely, while the
completed characteristic `Xi(1/2+i tau)` is bounded and nonzero almost
everywhere.  Properness is independent: every actual element of
`Z H_cap subset E` has a smooth real-analytic critical trace, whereas, for
example, the characteristic function of a bounded interval is an `L^2`
class with no such representative.  Thus the range is proper and dense,
and hence is not closed.

The elementary model `De_n=n^{-1}e_n` on `ell^2` displays the same topology:
`Ran(D)` is dense and nonclosed, while `D^dagger e_n=ne_n` is unbounded.
The companion verifier checks this finite-section growth.

Therefore the formal expression

\[
 P A^*(APA^*)^\dagger                                      \tag{4.2}
\]

from D.73 cannot be a bounded, trace-compatible lift merely by taking `A`
to be Poisson summation.  In the topology where the cokernel is faithful
there is no Moore--Penrose structure; in the topology with an orthogonal
projection the range is not closed and the faithful cokernel disappears.

## 5. The periodic-frame minimum extension also fails the support contract

At finite periodic depth the A--B frames are finite free with an ordered
basis.  Declaring that basis orthonormal certainly produces a least-norm
extension at each finite level.  The common A--B--C realization, however,
sends the Dirichlet basis to point masses:

\[
 \phi_n\longmapsto\delta_n
 \longmapsto\delta_{n^{-1}}.                                \tag{5.1}
\]

These are distributions, not vectors of the physical `L^2` Poisson space.
One could try to smooth all point masses by a translation-covariant kernel
`kappa` and put

\[
 \delta_{e^t}\longmapsto\tau_t\kappa.                       \tag{5.2}
\]

Exact compatibility with Dirichlet composition/convolution and the unit
requires

\[
 \kappa*\kappa=\kappa.                                      \tag{5.3}
\]

If the desired lift is supported in a compact physical window, `kappa` is
compactly supported.  Its Fourier transform is then entire.  Transforming
(5.3) gives

\[
 \widehat\kappa(z)^2=\widehat\kappa(z)\qquad(z\in\mathbb C). \tag{5.4}
\]

An entire function with values in the discrete set `{0,1}` is constant.
The constant `1` is the Fourier transform of the Dirac distribution, not of
an `L^2` function; the constant `0` gives `kappa=0`.  Hence:

> **Theorem 5.1 (supported convolution-frame no-go).**  There is no nonzero
> translation-covariant realization of the exact periodic convolution frame
> by compactly supported `L^2` vectors which preserves the unit and
> multiplication.  Consequently finite-frame least-norm extension cannot,
> by itself, produce the supported trace-exact lift of D.73.

Dropping compact support permits band-limited convolution idempotents, but
then `P mathcal M=mathcal M` is lost.  Dropping exact multiplication changes
the `p^k` contacts and hence changes (3.6).

## 6. Exact comparison with the supported phase form

Let `P` be the semilocal support projection and `U` the unitary additive
Fourier--Poisson transform.  The desired D.73 lift would satisfy

\[
 P\mathcal M_T=\mathcal M_T                                \tag{6.1}
\]

and

\[
 B_{{\rm nuc},T}-M_T^*CM_T
 =\mathcal M_T^*(U^*PU-P)\mathcal M_T.                       \tag{6.2}
\]

For a supported lift the right side is automatically

\[
 -((I-P)U\mathcal M_T)^*((I-P)U\mathcal M_T)\le0.           \tag{6.3}
\]

The range lift (2.4) proves the trace identity (3.6), but it does not satisfy
(6.1).  Substituting Meyer's actual maps gives, before the final trace, the
three exact defects audited in D.45:

\[
 D_+=FJMJF-M,                                                \tag{6.4}
\]

\[
 \operatorname {Tr}(A[P,A^*])
 =\|QAP\|_{\rm HS}^2-\|PAQ\|_{\rm HS}^2,                   \tag{6.5}
\]

and

\[
 \mathfrak d_Z=Z-(Z^{-1})^\sharp.                            \tag{6.6}
\]

Their complete prime--Gamma recombination is exactly (3.6), but (6.4)--(6.6)
do not combine into the single supported square (6.3).  Equality (6.2) is
therefore a genuinely stronger operator theorem than the now-established
trace pullback.

> **Corollary 6.1.**  The decisive comparison splits into two statements:
>
> * the jet and trace comparison, including every `p^k` and Gamma, is proved
>   by Theorems 1.1 and 3.1;
> * the supported Hilbert pullback (6.2) is not furnished by Poisson range
>   inversion, Moore--Penrose inversion, or finite-frame least-norm
>   extension.

## 7. The remaining independent datum

The search is now narrower than D.73.  A successful construction must be a
**rigged supported comparison functor**, not a right inverse of `Z`.  It must
map the distributional periodic frame into a rigged Hilbert triple

\[
 \mathscr S\subset H\subset\mathscr S'                      \tag{7.1}
\]

while satisfying simultaneously:

1. exact Dirichlet convolution on `S'` and a supported `H`-valued image on
   primitive combinations;
2. preservation of the two quotient characters (1.4);
3. equality of its phase pullback with (3.6), including the Gamma finite
   part;
4. compatibility with support enlargement;
5. retention, rather than Hilbert annihilation, of the cokernel `V`.

Theorem 5.1 shows why the support can only emerge **after primitive
cancellation among distributional frame vectors**, not from smoothing each
basis vector separately.  This is the surviving construction pivot.

## 8. Verdict

The requested A--B--C comparison is complete at the nuclear trace level:
the two jets are the moments `widehat a(0),widehat a(1)`, and the pullback is
exactly `B_nuc` with all prime powers and Gamma.

The canonical Poisson range lift is (2.4), and its exact cokernel is `V`.
It cannot be promoted to the supported Hilbert lift by Moore--Penrose
inversion: the faithful topology is Frechet, while the Hilbert boundary
range is dense and nonclosed.  Finite periodic frames likewise admit no
nonzero basiswise supported exact convolution realization.

Accordingly row D is not declared closed.  The remaining construction is
the rigged primitive-cancellation functor of Section 7, whose operator
pullback must be (6.2) without defining it from the sign of `B_nuc`.
