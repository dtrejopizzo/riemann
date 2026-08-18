# 107.160 -- Representability of the finite rooted chart

## 1. Label correction

The chart \(Z_n=V(\Phi_n)\) is the closure of primitive \(n\)-th roots.
Therefore a rooted label \((n,\chi)\) on that chart must satisfy

\[
 \mathrm{ord}(\chi)=n,
\]

not merely \(\mathrm{ord}(\chi)\mid n\).  The latter condition
duplicates a character on several cyclotomic charts and contradicts the
order-forgetting map to \(V(\Phi_n)\).

With exact order, the labels over all \(n\mid L_T\) form the \(L_T\)
elements of \(X_T^\vee\), each appearing once.

## 2. Representing scheme

Define

\[
 \mathcal R_T
 =
 \coprod_{n\mid L_T}
 \mathrm{Spec}\,\mathbb Z[x]/(\Phi_n(x))
 =
 \coprod_{n\mid L_T}
 \mathrm{Spec}\,\mathbb Z[\zeta_n].
\]

Then \(\mathcal R_T\to\mathrm{Spec}\,\mathbb Z\) is:

1. finite and flat, since every \(\Phi_n\) is monic and
   \(\mathbb Z[\zeta_n]\) is free of rank \(\varphi(n)\);
2. proper, because every finite morphism is proper;
3. regular and normal, because \(\mathbb Z[\zeta_n]\) is the full ring
   of integers of the cyclotomic field and hence a Dedekind domain
   (with the components \(n=1,2\) equal to \(\mathbb Z\)).

Its generic geometric points are exactly the primitive characters
\((n,\chi)\) with \(n\mid L_T\).

## 3. Relation with the full root scheme

The factorization

\[
 x^{L_T}-1=\prod_{n\mid L_T}\Phi_n(x)
\]

shows that \(\mathcal R_T\) is the normalization of the finite flat root
scheme \(\mu_{L_T}\).  The latter can have nonreduced ramified fibres;
normalization separates its cyclotomic closures while keeping a regular
total arithmetic scheme.

Moreover

\[
 \sum_{n\mid L_T}\varphi(n)=L_T,
\]

so the generic degree of \(\mathcal R_T\) is exactly the cardinality of
the finite rooted group in 107_158.

## 4. Level transitions

When \(L_T\mid L_{T'}\), every component indexed by \(n\mid L_T\)
appears unchanged in \(\mathcal R_{T'}\).  Their disjoint union gives a
canonical open-and-closed immersion

\[
 \mathcal R_T\hookrightarrow\mathcal R_{T'}.
\]

Thus the combinatorial descent of 107_159 is represented by actual
finite regular arithmetic schemes.

## 5. Scope

This proves representability of the discrete rooted coordinate that was
left symbolic in 107_17--107_22.  The scheme has relative dimension
zero.  It does not by itself provide the two-dimensional generic fibre
required by 107_149; the dynamical and archimedean coordinates must
still be represented and compactified around this finite regular
factor.

