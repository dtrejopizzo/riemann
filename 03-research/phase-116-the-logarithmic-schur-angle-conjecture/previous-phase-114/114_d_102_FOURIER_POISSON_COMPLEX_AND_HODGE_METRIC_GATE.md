# D.102 — Fourier--Poisson complex, contraction and Hodge-metric gate

## Status

The additive Fourier--Poisson construction gives an explicit complex whose
contractible range pair and cohomology can be calculated before any
spectral description.  The map

\[
 Z:\mathcal H_\cap\longrightarrow Z\mathcal H_\cap
\]

is a topological isomorphism of nuclear Frechet spaces, so that range pair
has a continuous Real contracting homotopy.  Its quotient cohomology is
not just the two Tate classes: the even cohomology is the Tate plane and
the odd cohomology is Meyer's nontrivial quotient
`V=H_-/(Z H_cap)`.

The Fourier involution makes the range contraction compatible with
Poisson summation, but it does not contract `V`.  In the critical Hilbert
topology the range is dense and nonclosed, so the inverse homotopy is
unbounded and the Hausdorff cokernel disappears.  Thus there is no
simultaneously faithful, Hilbert-isometric contraction in the presently
constructed topology.

The induced nuclear Green form on `V` pulls back to `-B_nuc` on primitive
tests.  Giving `V` a positive Hilbert metric compatible with scaling would
prove row D; for a free Real zero orbit its Gram is the hyperbolic swap
block of D.95.  Hence positivity of the odd Poisson cohomology is strictly
equivalent to D/RH, not a consequence of algebraic contractibility.

The exact additional datum is a Hodge Hilbertization of the Frechet
Poisson complex: a rigged Hilbert metric retaining `V`, making the range
closed, the Fourier--Real structure unitary and the induced cohomology
metric positive.  Constructing that metric from A--B--C energy before the
zero divisor would close D.

No RH statement or desired positivity is assumed.  The paper is not
modified.

## 1. The source-defined two-step complex

Let

\[
 \mathcal H_\cap
 =\{f\in\mathcal H_+:f(0)=\mathcal Ff(0)=0\}.             \tag{1.1}
\]

The two exact sequences constructed in row C are

\[
 0\to\mathcal H_\cap\to\mathcal H_+
 \xrightarrow{q_+}\mathbb C(0)\oplus\mathbb C(1)\to0     \tag{1.2}
\]

and

\[
 0\to Z\mathcal H_\cap\to\mathcal H_-
 \xrightarrow{q_-}V\to0,
 \qquad V=\mathcal H_-/(Z\mathcal H_\cap).                \tag{1.3}
\]

Meyer's closed-range theorem gives a topological isomorphism

\[
 Z:\mathcal H_\cap\xrightarrow{\sim}Z\mathcal H_\cap.    \tag{1.4}
\]

Place the source/range pair in consecutive degrees.  Its mapping cone is
contractible, while adjoining the two ambient quotients gives the
cohomology superobject

\[
 H^{\bar0}=\mathbb C(0)\oplus\mathbb C(1),
 \qquad H^{\bar1}=V.                                      \tag{1.5}
\]

This is exactly the row-C object `L_comp`; (1.5) is obtained from closed
subquotients, not from the zeros.

## 2. The Frechet contracting homotopy

On the range pair define

\[
 h_Z:Z\mathcal H_\cap\to\mathcal H_\cap,
 \qquad h_Z=Z^{-1}.                                      \tag{2.1}
\]

It is continuous in the intrinsic Frechet topologies and satisfies

\[
 h_ZZ=I_{\mathcal H_\cap},
 \qquad Zh_Z=I_{Z\mathcal H_\cap}.                        \tag{2.2}
\]

Thus the range pair is genuinely and continuously contractible.  It
contributes zero to every additive Euler/supertrace character.

On even functions `F^2=I`, and `F` preserves `H_cap`.  Poisson summation is

\[
 Zf=\mathscr JZ\mathcal Ff,qquad f\in\mathcal H_\cap.     \tag{2.3}
\]

Consequently the range involution

\[
 R_Z=Z\mathcal FZ^{-1}=\mathscr J|_{Z\mathcal H_\cap}     \tag{2.4}
\]

is source-defined and makes (2.1) Real/Fourier covariant.

But (2.1) is defined only on the subspace `Z H_cap`.  It induces no map
`V->H_cap`, because every representative of a nonzero quotient class lies
outside the range.  Extending `h_Z` to all of `H_-` would split (1.3); even
an algebraic splitting would leave a copy of `V`, not make it
contractible, unless a new differential out of `V` were added.

## 3. Why an isometric Hilbert contraction is unavailable

In the critical boundary `L^2` completion, multiplication by the completed
characteristic section is nonzero almost everywhere.  Hence its range is
dense.  It is proper, and therefore nonclosed.  Equivalently, the model
diagonal map

\[
 De_n=n^{-1}e_n                                           \tag{3.1}
\]

has dense nonclosed range and inverse `D^dagger e_n=ne_n`.

For a bounded Hilbert-space operator, a bounded Moore--Penrose inverse and
a Hodge decomposition exist only when the range is closed.  Therefore

\[
 (Z|_{\mathcal H_\cap})^\dagger
 \text{ is unbounded in the critical }L^2\text{ topology}.\tag{3.2}
\]

In that topology the Hausdorff quotient by the dense range is zero, so it
does not retain `V`.  In the faithful Frechet topology, `V` is a closed
nuclear quotient, but there is no canonical adjoint, orthogonal complement
or positive minimum-norm homotopy.

Thus the two desirable properties occur in incompatible present
completions:

\[
 \begin{array}{c|c|c}
 &\text{continuous range inverse}&\text{faithful orthogonal }V\\ \hline
 \text{intrinsic Frechet}&\checkmark&\text{no canonical Hilbert metric}\\
 \text{critical }L^2&\text{unbounded}&\text{Hausdorff quotient }0
 \end{array}.                                             \tag{3.3}
\]

## 4. Form induced on the odd cohomology

Let `rho_-^0` be the scaling representation on `V`.  For a completed test
`h=f star g^vee`, row C gives

\[
 \chi_{\mathbb L_{\rm comp}}(h)
 =\operatorname{Tr}_{\mathbb C(0)\oplus\mathbb C(1)}\rho_+^0(h)
 -\operatorname{Tr}_V\rho_-^0(h).                         \tag{4.1}
\]

Under the central Mellin identification, the even trace is

\[
 \langle M(f),CM(g)\rangle.                               \tag{4.2}
\]

The full character is `B_nuc(f,g)`.  Hence

\[
 \boxed{
 \operatorname{Tr}_V\rho_-^0(f\star g^\vee)
 =\langle M(f),CM(g)\rangle-B_{\rm nuc}(f,g).}            \tag{4.3}
\]

On primitive tests,

\[
 \boxed{
 \operatorname{Tr}_V\rho_-^0(f\star g^\vee)
 =-B_{\rm nuc}(f,g).}                                     \tag{4.4}
\]

This is an equality of nuclear characters, not yet a Hilbert Gram.  If `V`
carried a positive Hilbert metric for which the involutive scaling action
were a `star`-representation and the nuclear trace agreed with the Hilbert
trace, then (4.4) would imply row D immediately.

Conversely, the Real divisor realization of `V` has, for each fixed zero,
a positive square and for each free orbit the block

\[
 m_\rho\begin{pmatrix}0&1\\1&0\end{pmatrix}.              \tag{4.5}
\]

Thus a positive compatible metric with character (4.4) exists exactly
when those free blocks are absent, in the sense of the Weil positivity
criterion.  Positivity of odd Poisson cohomology is therefore equivalent
to D/RH.

## 5. Why Fourier involution does not pair away `V`

The identity (2.3) identifies the two presentations of the **range**.  It
does not say that every element of `H_-` is in that range.  Passing to the
quotient, the range class is zero and the Poisson identity becomes
`0=0`; it supplies no contracting map on `V`.

An involution on a vector space, even a unitary one, only decomposes it into
`plus-or-minus` eigenspaces.  It makes the space acyclic only after a new
odd differential is supplied which is invertible between those
eigenspaces.  No such differential on `V` is part of the Poisson triangle.

Moreover a contraction of `V` inside the superobject would delete its
nuclear character.  Since the character of `V` is the nontrivial term in
(4.1), this would change the row-C Lefschetz identity rather than prove a
sign for it.

## 6. Exact Hodge-Hilbertization contract

The missing datum can now be stated without reference to zeros.  Construct
a rigged Hilbert triple

\[
 \mathscr S_Z\subset\mathscr H_Z\subset\mathscr S_Z'      \tag{6.1}
\]

and a closed extension of the Poisson differential satisfying:

1. `H_cap` and `Z H_cap` are dense nuclear cores and the latter is closed
   in the graph/Hodge topology;
2. `Z` has a bounded Real contracting homotopy on its range;
3. the cohomology embeds faithfully as the same Frechet quotient `V`;
4. scaling is an involutive `star`-representation and Fourier--Poisson is
   unitary;
5. the Hodge cohomology metric is positive and its trace character is
   (4.3), including all prime powers and Gamma.

Then Hodge decomposition would give

\[
 \mathscr H_Z=\overline{\operatorname{Ran}d}
 \oplus\overline{\operatorname{Ran}d^*}
 \oplus\mathcal H_{\rm harm},                             \tag{6.2}
\]

with `H_harm` a positive realization of `Tate direct-sum Pi V`.  Equation
(4.4) would prove D.

This contract is noncircular only if the metric and closed-range estimate
are constructed from additive Fourier energy, periodic section norms and
the Euler--Gamma correspondence before invoking `Xi`'s divisor or the sign
of (4.4).  Defining the norm of a class by the right side of (4.4) assumes
the desired positivity.

## 7. Next energy identity to test

The natural source candidate is the graph energy

\[
 \|f\|_{\rm graph}^2
 =\|f\|_{\rm per}^2+\|Zf\|_{\rm Fourier}^2                \tag{7.1}
\]

on `H_cap`, with the two summands furnished respectively by periodic
A-cohomology and additive Fourier--Poisson energy.  It is positive and
makes `Z` bounded below on its graph completion by construction.

However, to retain `V` one must extend (7.1) to `H_-` and compute the
orthogonal quotient.  The decisive test is whether the induced quotient
norm has polarization (4.4) **without defining it that way**.  A generic
graph norm yields a positive quotient but an unrelated trace; matching all
prime powers and Gamma is the new theorem required.

The next audit therefore computes this graph-norm quotient at finite
periodic/Dirichlet cutoff and compares its Schur complement term by term
with the D.32 feature form.

