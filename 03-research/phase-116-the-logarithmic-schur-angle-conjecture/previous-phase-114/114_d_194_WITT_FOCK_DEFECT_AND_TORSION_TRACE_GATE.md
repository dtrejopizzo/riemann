# D.194 — Witt/Fock defect indices, reduced contact, and the torsion trace gate

## Verdict

The source Witt module has a canonical positive Fock Hilbertization:

\[
 \mathscr F_W=\ell^2(\mathbb N^\times),\qquad
 V_n\phi_r=\phi_{nr}.                                      \tag{0.1}
\]

Every \(V_n\) is an isometry and \(V_mV_n=V_{mn}\).  This is genuine
positivity before Meyer.  However its Hilbert defect does **not** reproduce
the B contact:

* for \(n=p^k\), the one-prime defect has rank \(k\), whereas
  \(\Lambda(p^k)=\log p\) is independent of \(k\);
* for \(n\) with two distinct prime factors, the Fock defect is nonzero,
  whereas \(\Lambda(n)=0\);
* on the full Fock tensor product every such defect has infinite ordinary
  rank;
* the perfect contact
  \([\mathbb Z\xrightarrow{\Phi_n(1)}\mathbb Z]\) becomes acyclic over
  \(\mathbb C\), so its Hilbert cohomological supertrace is zero even though
  its Arakelov torsion determinant has mass \(\Lambda(n)\).

Thus the first failed axiom is already local: **ordinary positive
Hilbert/Fock defect index is not the reduced arithmetic contact**.  The
perfect torsion determinant repairs the arithmetic mass, but it is not a
positive Hilbert trace.  Adding the Gamma oscillator then recovers the
complete row-C supercharacter only as a signed relative trace, not as a
negative square.

There is nevertheless a useful positive contact GNS algebra which realizes
the kernel \(\Lambda(mn)\) exactly.  It confirms that local contact
positivity is not the global obstacle; the missing step remains its
trace-exact Poisson gluing to the Witt translations and Gamma boundary.
No paper file is modified.

## 1. Prime Fock factorization

Unique factorization gives a canonical Hilbert tensor factorization

\[
 \ell^2(\mathbb N^\times)
 \cong\bigotimes_{p}'\ell^2(\mathbb N_0),
 \qquad
 \phi_r\longleftrightarrow
 \bigotimes_p|v_p(r)\rangle.                               \tag{1.1}
\]

Let \(S_p|j\rangle=|j+1\rangle\) on the \(p\)-factor.  Then

\[
 V_n=\prod_pS_p^{v_p(n)},qquad
 V_n^*\phi_r=
 \begin{cases}
 \phi_{r/n},&n\mid r,\\0,&n\nmid r.
 \end{cases}                                               \tag{1.2}
\]

Consequently

\[
 V_n^*V_n=I,qquad
 D_n:=I-V_nV_n^*\ge0.                                      \tag{1.3}
\]

Equations (1.1)--(1.3) are a bona fide source-side Hilbert representation
of the multiplicative semigroup.

## 2. The defect has the wrong prime-power law

On a single prime factor,

\[
 I-S_p^kS_p^{*k}=\sum_{j=0}^{k-1}|j\rangle\langle j|,       \tag{2.1}
\]

so

\[
 \mathrm{rank}(I-S_p^kS_p^{*k})=k.                 \tag{2.2}
\]

Let \(\omega\) be any faithful positive diagonal weight on this factor,
with \(\omega(|j\rangle\langle j|)=c_j>0\).  Then

\[
 \omega(I-S_p^kS_p^{*k})=\sum_{j=0}^{k-1}c_j              \tag{2.3}
\]

is strictly increasing in \(k\).  It cannot equal \(\log p\) for every
\(k\ge1\).

A vacuum state makes (2.3) equal to one for every \(k\), but it fails on
mixed integers.  If \(n=p^kq^\ell\), the global vacuum lies in
\(\mathrm{Ran}\,D_n\), so

\[
 \langle\Omega,D_{p^kq^\ell}\Omega\rangle=1,              \tag{2.4}
\]

whereas

\[
 \Lambda(p^kq^\ell)=0.                                    \tag{2.5}
\]

On the full tensor product the complement of multiples of \(n\) contains
infinitely many basis vectors, hence \(D_n\) has infinite rank.  Therefore
neither rank, ordinary trace, nor a faithful positive Fock state gives the
reduced contact law.

The central torsor does not repair this.  Replacing \(V_n\) by

\[
 \widetilde V_n=n^{-1/2}V_n                                \tag{2.6}
\]

gives

\[
 I-\widetilde V_n^*\widetilde V_n=(1-n^{-1})I,             \tag{2.7}
\]

again of infinite rank and now depending on the full exponent.  The
half-Tate factor is the correct metric character, but it is not a
finite-contact defect index.

## 3. Regularized Fock traces still give \(\log n\), not \(\Lambda(n)\)

For \(\sigma>1\), let

\[
 R_\sigma\phi_r=r^{-\sigma}\phi_r.                         \tag{3.1}
\]

Then \(R_\sigma\) is trace class and

\[
 \mathrm{Tr}\,R_\sigma=\zeta(\sigma),
 \qquad
 \mathrm{Tr}(R_\sigma V_nV_n^*)
 =n^{-\sigma}\zeta(\sigma).                               \tag{3.2}
\]

Thus

\[
 \mathrm{Tr}(R_\sigma D_n)
 =(1-n^{-\sigma})\zeta(\sigma).                            \tag{3.3}
\]

Logarithmic differentiation of the scalar \(n^{-\sigma}\) yields
\((\log n)n^{-\sigma}\), which remembers all prime exponents.  It does not
yield the reduced law \(\Lambda(n)\), supported only on prime powers and
independent of their exponent.

On one prime factor the Gibbs trace is equally explicit:

\[
 \mathrm{Tr}\,\left(q^{N_p}
 (I-S_p^kS_p^{*k})\right)
 ={1-q^k\over1-q}.                                        \tag{3.4}
\]

No positive limit of (3.4) is both faithful and constant in \(k\).

## 4. Why the perfect contact succeeds arithmetically but vanishes in Hilbert cohomology

Row B does not define contact as the Fock defect.  It derives

\[
 K_n^W=\mathbb Z[T,T^{-1}]/(\Phi_n(T))
 \otimes_{\mathbb Z[T,T^{-1}]}^{\mathbf L}\mathbb Z[T,T^{-1}]/(T-1)
 \simeq[\mathbb Z\xrightarrow{\Phi_n(1)}\mathbb Z].       \tag{4.1}
\]

For \(n>1\),

\[
 H^0(K_n^W)=
 \begin{cases}
 \mathbb F_p,&n=p^k,\\0,&n\text{ has two distinct primes},
 \end{cases}                                               \tag{4.2}
\]

and

\[
 -\log|\det_{\rm tor}K_n^W|=\log\Phi_n(1)=\Lambda(n).     \tag{4.3}
\]

After complexification, multiplication by the nonzero integer
\(\Phi_n(1)\) is an isomorphism:

\[
 K_n^W\otimes\mathbb C
 \simeq[\mathbb C\xrightarrow{\Phi_n(1)}\mathbb C]
 \simeq0.                                                   \tag{4.4}
\]

Hence its Hilbert cohomology, Fredholm index and cohomological supertrace
are all zero.  The nonzero number in (4.3) is analytic/Arakelov torsion: it
is retained by the metric determinant line, not by a positive Hilbert
cohomology class.

This is the first exact axiom failure in the proposed Fock proof:

\[
 \boxed{\text{Hilbert isometry defect}\ne
 \text{derived reduced contact determinant}.}             \tag{4.5}
\]

## 5. A positive GNS realization of reduced contact

The failure of Fock defects does not mean the local contact kernel is
indefinite.  Define the commutative nonunital algebra

\[
 \mathcal A_\Lambda=c_{00}(\mathbb P),qquad
 e_pe_q=\delta_{pq}e_p,qquad e_p^*=e_p,                   \tag{5.1}
\]

with positive semifinite trace

\[
 \tau_\Lambda(e_p)=\log p.                                \tag{5.2}
\]

For \(n>1\), put

\[
 \eta_n=
 \begin{cases}
 e_p,&n=p^k,\\0,&n\text{ is not a prime power}.
 \end{cases}                                               \tag{5.3}
\]

Then

\[
 \eta_m\eta_n=\eta_{mn}\qquad(m,n>1),                    \tag{5.4}
\]

with both sides zero when incompatible prime supports occur, and

\[
 \boxed{\tau_\Lambda(\eta_n)=\Lambda(n),qquad
 \tau_\Lambda(\eta_m^*\eta_n)=\Lambda(mn).}               \tag{5.5}
\]

The GNS Hilbert space is

\[
 L^2(\mathcal A_\Lambda,\tau_\Lambda)
 \cong\ell^2(\mathbb P,\log p).                            \tag{5.6}
\]

This is an exact positive realization of the **reduced contact algebra**.
It is nonunital at infinite prime level: the formal unit has infinite
trace.  That is compatible with the relative/cofinal nature of row C.

The construction (5.1)--(5.6) is useful new source data, but it realizes
only the scalar contact.  It does not yet identify the translation
correlations \(S_{k\log p}\) or the Gamma boundary with a single positive
square.

## 6. Reintroducing the translation dynamics

On the physical logarithmic Hilbert space, each finite prime contribution
is

\[
 \log p\sum_{k\ne0}p^{-|k|/2}S_{k\log p}
 =\log p\,(A_p^*A_p-I),                                   \tag{6.1}
\]

where

\[
 A_p=\sqrt{1-p^{-1}}
 (I-p^{-1/2}S_{\log p})^{-1}.                             \tag{6.2}
\]

The trace (5.2) supplies the coefficient \(\log p\), and the central torsor
supplies \(p^{-|k|/2}\).  Thus A--B source data recover all local
coefficients in (6.1).  But (6.1) is a **difference** of positive norms:

\[
 \log p\,\langle F,(A_p^*A_p-I)F\rangle
 =\log p\,(\|A_pF\|^2-\|F\|^2).                           \tag{6.3}
\]

The two terms diverge after summing over all primes and only their relative
combination with the complete Gamma oscillator stabilizes.  This is exactly
the relative object of D.73, not a positive Fock norm.

Moreover an exact intertwiner \(q\) satisfying

\[
 qS_{\log n}=V_nq                                         \tag{6.4}
\]

for the full translation group cannot land faithfully in the unilateral
Fock module: \(S_{\log n}\) is unitary while \(V_n\) has proper range.  A
bilateral dilation on \(\ell^2(\mathbb Q_+^\times)\) makes the shifts unitary,
but then every defect in Section 2 vanishes and contact is again lost.

D.189 gives the corresponding compressed statement: the exact old-core
return is not the raw Witt word Gram after Green shorting.  Thus (6.4) is not
recovered indirectly by compression.

## 7. Gamma and the full supertrace

One may adjoin the positive Gamma screw oscillator

\[
 H_{5/4}=D_\infty^*D_\infty                              \tag{7.1}
\]

to the contact GNS/Fock system.  Its character supplies the complete
archimedean term.  Together with (6.1), row C proves the exact signed
supertrace

\[
 B_{\rm nuc}(F,G)
 =\chi_{\rm Meyer}(F*G^\vee).                              \tag{7.2}
\]

But the source decomposition remains

\[
 -B_{\rm nuc}^{\rm prim}
 =\mathcal R_T-\mathcal W_T^*\mathcal W_T,                 \tag{7.3}
\]

not one positive square.  The Gamma oscillator repairs the complete
character; it does not change the local failure (4.5) or prove the global
comparison \(\mathcal W_T^*\mathcal W_T\le\mathcal R_T\).

## 8. Exact outcome of the Fock pivot

The source construction now separates three levels:

\[
\begin{array}{c|c|c}
\text{datum}&\text{positive source realization}&\text{outcome}\\ \hline
\text{Witt semigroup}&V_n\text{ isometries}&V_mV_n=V_{mn}\\
\text{reduced contact}&(\mathcal A_\Lambda,\tau_\Lambda)&\Lambda(n)\\
\text{Gamma}&D_\infty^*D_\infty&\text{full archimedean character}\\
\text{global gluing}&\text{relative supertrace}&B_{\rm nuc}
\end{array}                                                \tag{8.1}
\]

The first three rows are constructed without zeros.  The fourth is exact as
a signed trace but is not positive.  Therefore the Fock pivot does not close
D, but it identifies the first failure and supplies the maximal positive
local contact GNS object for the next gluing attempt.

## 9. Reproducible certificate

The companion script `114_d_194_witt_fock_defect_verify.py` checks:

1. single-prime defect ranks \(k\);
2. strict growth under every faithful positive diagonal weight;
3. nonzero mixed-prime vacuum defect;
4. the regularized trace formula (3.3);
5. acyclicity over \(\mathbb C\) versus nonzero log determinant;
6. positivity and the exact multiplication/trace law of the contact GNS
   algebra.
