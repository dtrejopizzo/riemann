# 107.157 -- Correction of the visible-order algebra at finite support

## 1. Correction

The finite visible order set used in 107_15 and 107_18 was called a
"finite multiplicative monoid."  That is false: the only finite
submonoid of \(\mathbb N^\times\) is \(\{1\}\).

For

\[
 S_T=\{(p,k):k\log p\le T\},
\qquad
 K_p(T)=\left\lfloor\frac{T}{\log p}\right\rfloor,
\]

the correct object is

\[
 L_T=\prod_{\log p\le T}p^{K_p(T)},
\qquad
 \mathcal N_T=\{n:n\mid L_T\}.
\]

It is finite and closed under gcd and lcm.  Multiplication is a partial
operation:

\[
 (m,n)\longmapsto mn
\quad\text{is defined at level }T
\quad\Longleftrightarrow\quad mn\mid L_T.
\]

## 2. Proof

If \(n=\prod p^{e_p}\), then every prime-power divisor \(p^k\mid n\)
is visible exactly when \(e_p\le K_p(T)\).  This is equivalent to
\(n\mid L_T\), proving the formula.

The divisor set of one integer is finite and is closed under gcd and
lcm.  It is generally not closed under products: if
\(\log2\le T<2\log2\), then \(2\mid L_T\) but \(4\nmid L_T\).

Finally, if a finite subset \(M\subset\mathbb N^\times\) is a monoid and
contains \(n>1\), it contains all distinct powers \(n^r\), contradicting
finiteness.  Thus no nontrivial finite multiplicative monoid was
available.

## 3. Consequence

The partial action written in 107_18,
\(\mu_m(n,\chi)\) only when \(mn\in\mathcal N_T\), was the correct
operation despite the incorrect terminology.  The correction aligns
those charts with 107_154: Frobenius composition that leaves the finite
divisor lattice maps to a larger level rather than being forced back
into the same finite object.

## 4. Non-enumerative representation

The correct computational object is the exponent vector

\[
 \mathbf K(T)=(K_p(T))_{p\le e^T},
\]

not the list of divisors of \(L_T\).  Gcd and lcm are coordinatewise
minimum and maximum, and the partial product is coordinatewise addition
subject to \(e_p+f_p\le K_p(T)\).  Moreover

\[
 \log L_T=\sum_{p\le e^T}K_p(T)\log p,
 \qquad
 \tau(L_T)=\prod_{p\le e^T}(K_p(T)+1).
\]

Since \(L_T=\mathrm{lcm}(1,\ldots,\lfloor e^T\rfloor)\), the
prime number theorem gives \(\log L_T\sim e^T\).  Enumeration is already
infeasible at \(T=5\), where \(\tau(L_T)=773094113280\).  The verifier
therefore works only with \(\mathbf K(T)\), through \(T=8\), and never
enumerates \(\mathcal N_T\).
