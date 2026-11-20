# SCOPE_P44_009 — Arbitrary interpolation is different from a semigroup flow

2026-10-19. Direct check of a citation encountered while testing the D link.
Source: Paper44 main.tex rem:nointerp, introduction and abstract. This note
does not modify the paper or affect its other theorems.

## Explicit counterexample to the unrestricted wording

Let nu_n=Frob_n be the compactly supported probability measures of Paper44.
For t in [log n,log(n+1)], put

    lambda(t)=(t-log n)/(log(n+1)-log n),
    nu(t)=(1-lambda(t))nu_n+lambda(t)nu_(n+1).

For t<=0 set nu(t)=nu_1. Each measure is compactly supported: its support
is contained in the union of two compact sets. For every continuous test
in the weak-* topology, its pairing with nu(t) is affine on each interval
and agrees at endpoints. The nodes log n have no finite accumulation point.
Thus this is a weak-* continuous family on R with nu(log n)=Frob_n.

Consequently the unrestricted sentence in rem:nointerp saying that NO
one-parameter family of compactly supported measures can interpolate these
values is false as written. A changing support invariant is not a continuous
invariant of arbitrary weak-* paths of measures. Convex mixtures need not
stay in the special class of single Frobenius shell measures.

## Scope of the correction needed

The definitions and the strong monoidal law at integer indices are not
refuted by this example. A claim about interpolation preserving a specified
shell class or a semigroup law is a different claim and needs its exact
hypotheses. This note does not supply that stronger theorem.

The safe editorial repair is to retain the integer, factorization-sensitive
nature of the canonical construction and remove the universal prohibition
of arbitrary continuous interpolation, unless an explicit restricted class
and a valid proof are supplied. The abstract, introduction and remark must
be aligned if this repair is integrated later.

LINK_009 is independent: it proves impossibility of a strongly continuous
UNIFORMLY BOUNDED SEMIGROUP or UNITARY COMPRESSION for the exact normalized
operators V_n in the new Hilbert module. It does not assert impossibility
of arbitrary continuous interpolation, which can likewise be made piecewise
affine in an operator space without respecting the semigroup law.

No conclusion about D follows from the counterexample. It prevents an
incorrect citation from being used as a premise in its proof.
