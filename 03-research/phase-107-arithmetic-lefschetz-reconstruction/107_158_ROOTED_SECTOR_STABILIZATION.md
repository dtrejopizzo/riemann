# 107.158 -- Finite stabilization of the rooted cyclotomic sector

## 1. Corollary of 107_157

Fix \(T>0\), and define

\[
 K_p(T)=\left\lfloor\frac{T}{\log p}\right\rfloor,
 \qquad
 L_T=\prod_{\log p\le T}p^{K_p(T)}.
\]

After the correction of 107_157, the visible order set is

\[
 \mathcal N_T=\{n:n\mid L_T\}.
\]

The rooted dual introduced in 107_18 is therefore

\[
 X_T^\vee
 =
 \bigcup_{n\in\mathcal N_T}\frac1n\mathbb Z/\mathbb Z
 =
 \frac1{L_T}\mathbb Z/\mathbb Z.
\]

In particular, \(X_T^\vee\) is cyclic of order \(L_T\), and its
\(p\)-primary subgroup is cyclic of order \(p^{K_p(T)}\).  Thus the
maximum visible denominator/Frobenius depth at \(p\) is exactly
\(K_p(T)\).

## 2. Proof

Every \(n\in\mathcal N_T\) divides \(L_T\), so

\[
 \frac1n\mathbb Z/\mathbb Z
 \subseteq
 \frac1{L_T}\mathbb Z/\mathbb Z.
\]

Conversely \(L_T\in\mathcal N_T\), hence the right-hand group is one of
the terms in the union.  This proves equality.

The group \((1/L_T)\mathbb Z/\mathbb Z\) is canonically
\(\mathbb Z/L_T\mathbb Z\).  Its \(p\)-primary component has order equal
to the exact \(p\)-part of \(L_T\), namely \(p^{K_p(T)}\). \(\square\)

## 3. Stabilization consequence

The rooted framing labels used by a level-\(T\) divisor lie in the
finite set

\[
 \{(n,\chi):n\mid L_T,\ \chi\in X_T^\vee,\
 \mathrm{ord}(\chi)=n\}.
\]

Therefore their monomial-ray support is finite before any dimension is
computed.  The criterion of 107_155 applies: the rooted/cyclotomic
\(H^0\) sector stabilizes once a pro-level contains \(L_T\) and all
Frobenius depths \(|j|\le\max_pK_p(T)\).

Multiplication by a visible order remains a partial operation at level
\(T\).  If it raises a \(p\)-exponent above \(K_p(T)\), it maps to the
larger support level prescribed by 107_154 rather than creating a new
section at the old level.

## 4. Scope

This closes the local finite-support problem for the rooted framing
sector actually used in 107_18--107_22.  It does not make the full
absolute stalk finite, construct restriction maps between distinct
prime charts, or prove that the resulting chart space is a proper
arithmetic variety.  Those global gluing and representability problems
remain the row-(a) obstruction.

The verifier does not enumerate roots or divisors.  It uses only the
exponent vector \(\mathbf K(T)\), checks the order and primary depths
symbolically through \(T=8\), and records the explosive divisor count
only as a diagnostic.  All substantive content is the divisor-lattice
identification of 107_157; the present equality is its immediate
top-element corollary.
