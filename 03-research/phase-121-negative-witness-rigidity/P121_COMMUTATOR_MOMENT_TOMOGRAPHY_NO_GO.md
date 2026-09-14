# P121 -- commutator moment tomography no-go

## Proposal

For the position operator `QF(t)=tF(t)`, iterated commutators distinguish
translation lengths:

\[
 \operatorname{ad}_Q^k(S_a)=(-a)^kS_a.              \tag{1.1}
\]

At a fixed window the active prime-power lengths are finite.  It was
therefore tempting to use all commutator moments, invert their Vandermonde
matrix, and separate the atomic Euler shifts from the continuous Gamma jump
measure.

## Exact radical audit

Let `H=H^*>=0` be the primitive operator at first contact and let
`0\ne F\in\ker H`.  For every operator `X` preserving the required domains,

\[
 \langle F,[H,X]F\rangle=0.                          \tag{2.1}
\]

But (2.1) is only

\[
 \langle HF,XF\rangle-\langle X^*F,HF\rangle=0.     \tag{2.2}
\]

It contains no information beyond `HF=0`.  Taking `X=Q^k` and expanding
prime translations may re-coordinate the zero-mode equation, but it does
not create independent length moments.

The first genuinely new commutator is the double commutator.  Direct
expansion gives

\[
 \langle F,[Q,[H,Q]]F\rangle
 =2\langle QF,HQF\rangle\ge0.                       \tag{2.3}
\]

It vanishes if and only if `H^{1/2}QF=0`.  More generally, higher
commutators contain the Gram moments

\[
 \langle Q^iF,HQ^jF\rangle,                         \tag{2.4}
\]

which are not forced to vanish by `HF=0`.

## No-go theorem

An infinite sequence of zero commutator moments sufficient for Vandermonde
separation exists only after proving that the polynomial translation jet

\[
 F,QF,Q^2F,\ldots                                    \tag{3.1}
\]

lies in `ker H`, or after proving that every Gram moment (2.4) vanishes.
Either statement is the translation-jet/equality-state rigidity problem
already isolated in v94.  It is not a consequence of first contact.

If one retains only (2.3), the route becomes a sign estimate for a Mourre or
virial commutator.  That is explicitly outside the phase-121 admissible
architecture and, in the corpus, leaves the same boundary and moving-Tate
terms.

Therefore commutator moment tomography does not supply the independent
identities required to separate the Euler atoms.  The proposal is retired.
