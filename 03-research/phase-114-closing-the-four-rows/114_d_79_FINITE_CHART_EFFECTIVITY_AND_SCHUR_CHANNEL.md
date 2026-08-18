# D.79 — Primitive Koszul effectivity and the finite-chart Schur channel

## Status

D.75--D.76 put the two Tate moments, compact support, every finite
prime-power orbit and the complete Gamma oscillator in one source-defined
correspondence.  D.44 puts the same data in the two-chart Poisson--Koszul
complex.  This note tests whether their combination has an ordered,
non-Hilbertian effectivity law which proves the row-D sign without choosing
a spectral polarization.

The comparison is exact but negative.  The primitive potential turns the
two Tate equations into a compactly supported module and the adelic feature
map pulls the signed metric back to precisely `B_nuc`, including all `p^k`
and Gamma.  The two-chart Koszul construction pulls back the same form as an
Euler pairing.  An Euler pairing is virtual, however, and the global Poisson
relation supplies no order on it.

More decisively, every finite ordered chart realization has the same
zero-corner obstruction.  A negative sum of local squares whose auxiliary
`QQ` corner is zero must have zero cross corner.  If the cross corner is
nonzero, eliminating finitely many charts produces the positive Schur
channel of D.78; Clifford anticommutation removes cross terms in a square
but does not turn a supertrace into an effective trace.  Thus no finite
Koszul/Clifford correction proves the sign.  A possible continuation must be
an infinite, trace-compatible ordered resolution in which the Schur
channels converge at the boundary; its construction is a new theorem, not
a consequence of two-chart exactness.

No RH, zero divisor, or sign-dependent polarization is used.  The paper is
not modified.

## 1. The exact primitive pullback

Let

\[
 \mathfrak I_{\rm prim}
 =\{F:M_-(F)=M_+(F)=0\}.                                  \tag{1.1}
\]

On the logarithmic line put

\[
 L=D^2-\frac14,
 \qquad \mathcal WF=-e^{-|\cdot|/2}*F.                    \tag{1.2}
\]

D.75 proves, without a Fourier division, that

\[
 L\mathcal WF=F,
 \qquad
 \operatorname {supp}(\mathcal WF)
 \subseteq\operatorname {conv}(\operatorname {supp}F).    \tag{1.3}
\]

The two equations in (1.1) are exactly what cancels the two exponential
tails in (1.2).  They are also exactly the two characters killed by the
even Poisson quotient.  Thus the same two jets define both the compact
potential module and the primitive A--B--C source; there is no additional
boundary condition in this passage.

For a prime `p`, let

\[
 r_p=p^{-1/2},\qquad U_p=S_{\log p},\qquad
 A_p=\sqrt{1-r_p^2}(I-r_pU_p)^{-1}.                         \tag{1.4}
\]

For `u=\mathcal WF`, define

\[
 \begin{aligned}
 S_pu&=\sqrt{\log p}\,A_pLu,&
 B_pu&=\sqrt{\log p}\,Lu,\\
 S_\infty u&=\sqrt{m_0}\,Lu,&
 B_\infty u&=\partial_\infty Lu,
 \end{aligned}                                             \tag{1.5}
\]

where `m_0=log(pi)-psi(1/4)`.  The Neumann expansion of (1.4) gives

\[
 A_p^*A_p-I
 =\sum_{k\ne0}p^{-|k|/2}S_{k\log p}.                      \tag{1.6}
\]

Consequently, after the support stabilization of D.73,

\[
 \begin{aligned}
 &\sum_p\bigl(\langle S_pu,S_pv\rangle
                    -\langle B_pu,B_pv\rangle\bigr)\\
 &\quad+\langle S_\infty u,S_\infty v\rangle
                    -\langle B_\infty u,B_\infty v\rangle\\
 &=\sum_p\log p\sum_{k\ne0}p^{-|k|/2}
             \langle F,S_{k\log p}G\rangle
   +m_0\langle F,G\rangle
   -\langle\partial_\infty F,\partial_\infty G\rangle\\
 &=B_{\rm nuc}(F,G),                                       \tag{1.7}
 \end{aligned}
\]

where `u=W F` and `v=W G`.  The terms with `k` and `-k` in (1.7) are the two
Tate-symmetric appearances of every power `p^|k|`; the final two terms are
the full Gamma finite part.  Formula (1.7) is the exact pullback requested
from the primitive correspondence.  It precedes, and does not assume, any
sign.

## 2. What the two-chart Koszul complex adds

The strict Poisson presentation is

\[
 C_\zeta=[\mathcal L_\gamma^0\xrightarrow{\sigma_\zeta}\mathcal E],
 \qquad H^0(C_\zeta)=V.                                   \tag{2.1}
\]

Its mixed complex

\[
 K_\zeta=C_\zeta^\vee\widehat\otimes^{\mathbf L}C_\zeta \tag{2.2}
\]

has, under the row-C contraction, Euler pairing

\[
 \chi_{\rm nuc}(K_\zeta;F,G)=B_{\rm nuc}(F,G).             \tag{2.3}
\]

Together, (1.7) and (2.3) identify the two constructions exactly:

\[
 \boxed{
 \text{adelic signed Gram pullback}
 =\text{Poisson--Koszul Euler pairing}
 =B_{\rm nuc}.}                                           \tag{2.4}
\]

The equality is stronger than equality of determinants: it is the
polarized form on the common primitive source.  It is nevertheless an
equality of **virtual** metrics.  In an ordered Grothendieck group, exactness
gives additivity

\[
 [C_\zeta]=[\mathcal E]-[\mathcal L_\gamma^0],             \tag{2.5}
\]

not an inequality between its two terms.  The global Poisson relation
identifies the quotient and removes the two polar characters, but it does
not give a monomorphism of metric objects of norm at most one.  Such a
monomorphism would be precisely the missing comparison

\[
 \|\mathbf SF\|\le \|\mathbf BF\|.                        \tag{2.6}
\]

By (1.7), (2.6) is already the desired row-D inequality.  Therefore it
cannot be inferred from exactness alone.

## 3. The zero-corner lemma

The following elementary fact applies to Hilbert squares, Euclidean
fibers of ordered tensor categories, and any proposed categorical
effectivity law after evaluation by a positive real fiber functor.

> **Lemma 3.1 (zero-corner rigidity).**  Let `H=P direct-sum Q`, and let
> `L_j:H->K_j` be a finite or countable family such that
> `sum_j ||L_jx||^2` converges.  Put
> \[
>  q(x,y)=-\sum_j\langle L_jx,L_jy\rangle.                 \tag{3.1}
> \]
> If `q(q,q)=0` for every `q in Q`, then `L_jq=0` for every `j,q`, and
> hence `q(p,q)=0` for every `p in P,q in Q`.

Indeed, `q(q,q)=0` is the negative of a sum of nonnegative numbers, so
every summand vanishes.  Polarization then kills the cross corner.

Equivalently, if a Hermitian block

\[
 H_{\rm cor}=\begin{pmatrix}D&B\\B^*&0\end{pmatrix},
 \qquad D\le0,                                             \tag{3.2}
\]

has `B != 0`, it is not a negative Gram form.  This conclusion uses neither
completeness nor spectral theory; for a nonpositive Hermitian form, a null
vector is automatically orthogonal to every vector by Cauchy--Schwarz for
its negative.

The cross-window block in D.77--D.78 is precisely of the form (3.2), with

\[
 D=P\widehat PP-P\le0,
 \qquad B=\frac12P\widehat PQ,                              \tag{3.3}
\]

and `B` has infinite rank.  Thus no finite family of effective local
squares can reproduce the exact corner character while retaining the zero
`QQ` corner.

## 4. Finite auxiliary charts and the Schur channel

Adding finitely many auxiliary charts does not remove Lemma 3.1.  At a
fixed regularized window, eliminate the negative `P` block in (3.2).  If
`Ran(B) subset Ran(D)` and the Moore--Penrose expression is bounded, block
congruence gives

\[
 \begin{pmatrix}D&B\\B^*&0\end{pmatrix}
 \sim
 \begin{pmatrix}D&0\\0&S\end{pmatrix},
 \qquad
 \boxed{S=-B^*D^\dagger B\ge0.}                           \tag{4.1}
\]

If the range inclusion fails, no bounded chart elimination exists.  If it
holds and `B != 0` modulo `ker D`, then `S` is nonzero.  Hence the cross
corner is equivalent to a negative chart plus a positive Schur chart.

Suppose another finite effective chart is introduced to cancel `S` while
again leaving its final auxiliary diagonal equal to zero.  Applied to the
new last corner, Lemma 3.1 says that its cross map must vanish; if it does
not, eliminating it creates another positive Schur complement.  Induction
therefore gives:

> **Theorem 4.1 (finite-chart inheritance).**  A finite sequence of
> ordered square charts and exact eliminations cannot turn a Hermitian
> corner with zero auxiliary diagonal and nonzero cross block into a
> nonpositive form.  It either leaves a positive Schur channel, fails the
> bounded range condition, or changes the target pairing.  The statement
> remains true after a positive real fiber functor from an ordered
> non-Hilbertian category.

This is the categorical content of the triangular no-go in D.78.  It is
not tied to a particular graph map.  Sylvester inertia at every finite
cutoff records the same positive direction, so a different order of finite
Gaussian eliminations cannot delete it.

## 5. Clifford and super-Koszul audit

One may try to encode the places by anticommuting generators.  For maps
`T_v` and self-adjoint Clifford generators `gamma_v` with

\[
 \gamma_v\gamma_w+\gamma_w\gamma_v=2\delta_{vw},           \tag{5.1}
\]

the Dirac sum

\[
 \mathscr D=\sum_vT_v\otimes\gamma_v                       \tag{5.2}
\]

has no mixed-place terms when the `T_v` commute:

\[
 \mathscr D^*\mathscr D=\sum_vT_v^*T_v\otimes I.           \tag{5.3}
\]

This is useful for cancelling cross-prime monomials, but (5.3) is a
positive sum of squares.  The signs in (1.7) can only be recovered by a
grading and a supertrace.  A supertrace is again an Euler difference and
has no positivity property: on an even line minus an odd line it evaluates
`a-b`, with either sign.

The Gamma oscillator causes the same issue.  It fits (1.7) as

\[
 m_0\|F\|^2-\|\partial_\infty F\|^2,                       \tag{5.4}
\]

but a finite Clifford generator merely records the two terms in a graded
square.  Converting their supertrace into an ordinary negative square
requires a metric pairing from the positive summand into the negative one;
its contractivity is (2.6).  Clifford/Koszul structure therefore preserves
the exact A--B--C character but does not prove its sign.

## 6. Why the primitive potential does not kill the cross channel

The map `W` kills exactly two exponential tails.  It cannot annihilate the
semilocal cross block `Q P_hat P`, which has infinite rank.  D.75's
primitive approximate identity converges strongly to the identity; if the
cross block vanished on every primitive potential, this approximation
would force the full block to vanish, contrary to D.77.

There is also a local sign test.  A single prime fiber in (1.7) has
primitive positive directions.  Therefore the desired order cannot be a
placewise sum of negative local squares.  The Gamma term and the finite
places must interact before an order is taken.  The Poisson formula performs
that interaction at the level of the global trace, but an equality of
traces is not a sum-of-squares factorization.

Thus the following three statements must not be conflated:

\[
 \begin{array}{rcl}
 \text{primitive support}&:&\text{proved by }\mathcal W,\\
 \text{exact global character}&:&\text{proved by (1.7)--(2.4)},\\
 \text{effective global order}&:&\text{not supplied by finite charts}.
 \end{array}                                                \tag{6.1}
\]

## 7. The surviving route

The finite-chart theorem isolates a narrower possible mechanism.  One
would need an infinite ordered resolution

\[
 \cdots\longrightarrow E_2\longrightarrow E_1
 \longrightarrow E_0                                      \tag{7.1}
\]

constructed from the Poisson correspondence itself, with all of the
following properties:

1. its Euler pairing is the exact form (1.7), with every `p^k` and Gamma;
2. every finite truncation records its Schur boundary term rather than
   discarding it;
3. the boundary terms converge to zero in the nuclear trace topology;
4. the induced comparison on primitive cohomology is ordered, supported
   and compatible with the directed windows;
5. no inverse has the prolate angle blow-up of D.78.

An infinite nonclosed resolution can evade finite-dimensional inertia only
through a nontrivial boundary-at-infinity theorem.  Conditions 2--5 are
exactly the theorem that must be proved.  Two-chart exactness, determinant
multiplicativity and Clifford anticommutation do not imply it.

## 8. Conclusion

The decisive comparison is now complete:

\[
 \boxed{
 \mathfrak I_{\rm prim}\xrightarrow{\mathcal W}
 \text{adelic feature module}
 \quad\Longrightarrow\quad
 \text{pullback}=B_{\rm nuc}
 }
\]

with all prime powers and the full Gamma contribution, and the same
pullback is the Poisson--Koszul Euler pairing.  This gives a fully typed
common A--B--C source for row D.

The attempted finite non-Hilbertian effectivity law does not close the
inequality.  After any positive real realization it inherits zero-corner
rigidity; a nonzero cross term produces the positive Schur channel.  The
next mathematically distinct construction is therefore an infinite
Poisson resolution with a proved vanishing theorem for its Schur boundary,
not another finite graph, Koszul or Clifford correction.

