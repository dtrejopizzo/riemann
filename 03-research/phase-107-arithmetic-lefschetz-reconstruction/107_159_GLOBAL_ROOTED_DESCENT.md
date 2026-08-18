# 107.159 -- Canonical global descent of the finite rooted sectors

## 1. Transition theorem

For a support bound \(T\), let

\[
 L_T=\prod_{\log p\le T}p^{\lfloor T/\log p\rfloor},
 \qquad
 X_T^\vee=(1/L_T)\mathbb Z/\mathbb Z.
\]

If \(T\le T'\), then \(L_T\mid L_{T'}\).  Hence there is a canonical
inclusion

\[
 X_T^\vee\hookrightarrow X_{T'}^\vee
\]

and, after Pontryagin duality, a canonical surjection

\[
 X_{T'}\twoheadrightarrow X_T.
\]

These maps compose strictly for \(T\le T'\le T''\).

## 2. Gluing the prime sectors

The Chinese remainder theorem gives canonical finite-group
decompositions

\[
 X_T^\vee
 \simeq
 \bigoplus_{\log p\le T}
 \mathbb Z/p^{K_p(T)}\mathbb Z,
\]

\[
 X_T
 \simeq
 \prod_{\log p\le T}
 \mathbb Z/p^{K_p(T)}\mathbb Z.
\]

Thus the local \(p\)-primary rooted sectors of 107_158 glue uniquely
into one global finite rooted group.  No ordering of primes, choice of
generators, or post-hoc identification is needed.

## 3. Recovery of the full framing

Every positive integer \(n=\prod p^{e_p}\) divides \(L_T\) once

\[
 T\ge\max_{p\mid n}e_p\log p.
\]

Therefore

\[
 \varinjlim_T X_T^\vee=\mathbb Q/\mathbb Z.
\]

Pontryagin duality gives

\[
 \varprojlim_T X_T=\widehat{\mathbb Z}.
\]

This recovers exactly the rooted and framed coordinates of the 2026
Connes--Consani moduli from the finite support levels.

## 4. Compatibility with partial multiplication

At one fixed level, visible-order multiplication is partial as corrected
in 107_157.  For any \(m,n\), however, there is a larger \(T'\) with
\(mn\mid L_{T'}\).  Hence multiplication defines a strict operation on
the filtered system even though it is not internal to every level.

This is the same structural pattern as the Frobenius maps of 107_154:
finite levels remain finite, while unrestricted composition is restored
in the colimit.

## 5. Consequence and scope

The finite rooted charts now have:

1. finite local depth;
2. canonical transition maps;
3. canonical gluing of all prime-primary factors;
4. recovery of the full rooted/framed datum in the limit.

This closes global descent for the discrete framing coordinate.  It does
not construct an algebraic or analytic space representing those charts,
compactify that space, descend the Gamma--polar metric, or produce the
regular proper arithmetic variety required by row (a).

