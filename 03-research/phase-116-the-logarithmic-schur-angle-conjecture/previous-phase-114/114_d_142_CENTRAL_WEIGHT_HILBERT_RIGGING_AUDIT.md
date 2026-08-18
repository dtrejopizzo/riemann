# D.142 — Central-weight Hilbert realization and the rigged pivot

## Verdict

The common Dirichlet action of A--B--C has a canonical positive Hilbert
realization at central weight:

\[
 H_{-1/2}=\ell^2(\mathbb N,n^{-1}),\qquad
 L_m\delta_n=\delta_{mn},\qquad \|L_m\|=m^{-1/2}.       \tag{0.1}
\]

It is faithful, multiplicative and retains every label \(p^k\).  It does
not, however, construct the comparison \(C_TX_T=Y_T\).  Three exact
obstructions occur before any question about the sign of
\(B_{\rm nuc}\):

1. the contact functional \(\ell(\delta_n)=\Lambda(n)\) is unbounded on
   \(H_{-1/2}\);
2. the two Tate boundary characters are not both continuous on this
   Hilbert completion, so their common kernel does not give the required
   closed codimension-two primitive space; and
3. every bounded intertwiner from (0.1) to the unitary logarithmic
   translation representation carrying the Gamma screw is zero.

Thus the central metric character cannot simultaneously be used as the
Hilbert norm, the finite-contact functional and the Gamma covariance.
The minimum non-circular pivot is a rigged Hilbert system in which the
unweighted Dirichlet shifts are isometries, while \(n^{-1/2}\),
\(\Lambda(n)\), the two Tate moments and Gamma are retained as separate
metric-line or distributional data:

\[
 \Phi_{\rm ABC}\subset H_0\subset\Phi_{\rm ABC}',
 \qquad H_0=\ell^2(\mathbb N)\widehat\otimes L^2(\mathbb R).          \tag{0.2}
\]

This pivot types every ingredient and removes the scaling argument that
forces every equivariant map to vanish; existence of a useful nonzero map
is still a separate theorem.
It still does not prove that the resulting mixed comparison is a
contraction; that assertion remains exactly row D.

No zero of zeta and no sign of \(B_{\rm nuc}\) is used.  The paper is not
modified.

## 1. The positive central-weight representation

Let \(c_{00}(\mathbb N)\) have basis \(\delta_n\) and Dirichlet product
\(\delta_m*\delta_n=\delta_{mn}\).  Define

\[
 \langle a,b\rangle_{-1/2}
 =\sum_{n\geq1}{a_n\overline{b_n}\over n}.             \tag{1.1}
\]

Then

\[
\begin{aligned}
 \|L_ma\|_{-1/2}^2
 &=\sum_{n\geq1}{|a_n|^2\over mn}
 ={1\over m}\|a\|_{-1/2}^2,\\
 L_mL_n&=L_{mn}.                                      \tag{1.2}
\end{aligned}
\]

Consequently (0.1) extends to the completion.  In the orthonormal basis
\(e_n=\sqrt n\,\delta_n\),

\[
 L_me_n=m^{-1/2}e_{mn}.                               \tag{1.3}
\]

This is the unique diagonal Hilbert weight, up to one scalar, with exact
central scaling.  Indeed, if
\(\|\delta_n\|^2=w_n\) and
\(\|L_m\delta_n\|^2=m^{-1}\|\delta_n\|^2\) for all
\(m,n\), then

\[
 w_{mn}=m^{-1}w_n,\qquad w_n=w_1/n.                   \tag{1.4}
\]

Thus changing the diagonal measure while retaining exact central weight
cannot repair the obstructions below.

## 2. The finite contact is not Hilbert-continuous

On the algebraic cyclic orbit row C has

\[
 \ell(\delta_n)=\Lambda(n).                           \tag{2.1}
\]

If \(\ell\) extended continuously to \(H_{-1/2}\), then for a constant
\(C\)

\[
 \Lambda(n)\leq C\|\delta_n\|_{-1/2}=C n^{-1/2}.     \tag{2.2}
\]

Taking \(n=p^k\) contradicts (2.2), since its two sides are
\(\log p\) and \(Cp^{-k/2}\).  Equivalently, the formal Riesz vector has
coordinates \(n\Lambda(n)\), whose squared norm would be

\[
 \sum_{n\geq1}{|n\Lambda(n)|^2\over n}
 =\sum_{n\geq1}n\Lambda(n)^2=\infty.                 \tag{2.3}
\]

This obstruction already uses a single prime-power tower.  It is not a
failure caused by mixing primes or by the archimedean place.

More generally, suppose a Hilbert realization has a cyclic vector
\(\Omega\) with

\[
 v_n=\pi(\delta_n)\Omega,\qquad
 \|v_n\|=n^{-1/2}\|\Omega\|.                         \tag{2.4}
\]

No bounded functional can take the values \(\Lambda(n)\) on all \(v_n\),
by the same one-vector estimate.  Hence the no-go is not restricted to the
orthogonal model (1.1).

## 3. The two Tate characters are boundary distributions

On Dirichlet labels the two central characters are

\[
 \chi_-(\delta_n)=n^{-1/2},\qquad
 \chi_+(\delta_n)=n^{1/2}.                            \tag{3.1}
\]

The second is immediately unbounded on \(H_{-1/2}\), because

\[
 { |\chi_+(\delta_n)|\over\|\delta_n\|_{-1/2}}=n.    \tag{3.2}
\]

The first has bounded values on individual normalized rays but is still
not continuous: on

\[
 a_N={1\over\sqrt N}\sum_{n=1}^N e_n
\]

one has \(\|a_N\|=1\) and \(\chi_-(a_N)=\sqrt N\).
Thus neither the pair
\((\chi_-,\chi_+)\) nor its common kernel is a Hilbert boundary map on
\(H_{-1/2}\).

On the nuclear Dirichlet test algebra

\[
 \mathcal C_{\mathbb R}
 =\{a:\sum_n|a_n|n^r<\infty\text{ for every }r\},     \tag{3.3}
\]

both characters and \(\ell\) are continuous.  They do not define kernels
of continuous boundary maps in the middle Hilbert topology.  This is
precisely the role of a rigging: the Tate moments live in the strong dual, not as Riesz
vectors of the central Hilbert completion.

## 4. Exact incompatibility with the Gamma channel

Let \(U_m=S_{\log m}\) be logarithmic translation on the full-line Gamma
space.  It is unitary.  Suppose a bounded map

\[
 T:H_{-1/2}\longrightarrow H_\infty                 \tag{4.1}
\]

intertwines the common labels:

\[
 TL_m=U_mT.                                           \tag{4.2}
\]

For every \(a\in H_{-1/2}\), (1.2) and unitarity give

\[
 \|Ta\|=\|U_m^kTa\|=\|TL_{m^k}a\|
 \leq\|T\|m^{-k/2}\|a\|.                            \tag{4.3}
\]

Letting \(k\to\infty\) proves \(Ta=0\).  Therefore

\[
 \boxed{T=0.}                                         \tag{4.4}
\]

The complete Gamma feature is nonzero:

\[
 (D_\infty F)(r,t)=
 \sqrt{{e^{-5r/2}\over1-e^{-2r}}}
 (F(t)-F(t-r)),                                       \tag{4.5}
\]

and commutes with full-line translations in \(t\).  Hence it cannot be
coupled to (0.1) by a nonzero bounded equivariant map.  Adjoining it as an
orthogonal direct summand does not repair the problem: that gives no
source-defined off-diagonal covariance and therefore no candidate for
\(C_TX_T=Y_T\).

This is an action-level obstruction, independent of summability.  It also
shows why retaining the factor \(n^{-1/2}\) as a metric character is
different from putting it into the norm of the correspondence orbit.

## 5. Why the positive Hilbert action does not imply the contraction

On a support window D.137 gives

\[
 B_{\rm nuc}(F,G)
 =\langle Y_TF,Y_TG\rangle-\langle X_TF,X_TG\rangle, \tag{5.1}
\]

where \(X_T\) contains the full Gamma screw and every antisymmetric
\(p^k\)-channel, while \(Y_T\) contains the \(\beta\)-line, the Poisson
resolvent and every symmetric \(p^k\)-channel.  A desired comparison would
be

\[
 C_TX_TF=Y_TF,\qquad\|C_T\|\leq1.                    \tag{5.2}
\]

The representation (0.1) only proves positivity of its own norm.  It does
not compare the symmetric and antisymmetric translation channels, and by
Section 4 it cannot supply the Gamma component equivariantly.  Moreover
(5.2) is equivalent to

\[
 \|Y_TF\|\leq\|X_TF\|\quad(F\in\mathcal P_T),         \tag{5.3}
\]

which, by (5.1), is exactly the row-D inequality.  Therefore defining
\(C_T\) by \(X_TF\mapsto Y_TF\) and citing positivity of (0.1) would be a
change of Hilbert space, not a proof of contractivity.

## 6. The minimum rigged-Hilbert pivot

The obstruction (4.4) disappears if the Hilbert correspondence action is
unweighted and the central character is kept as separate line data.  Put

\[
 H_{\rm lab}=\ell^2(\mathbb N),\qquad
 \widetilde L_m e_n=e_{mn}.                           \tag{6.1}
\]

Each \(\widetilde L_m\) is an isometry and
\(\widetilde L_m\widetilde L_n=\widetilde L_{mn}\).  The old action is

\[
 L_m=m^{-1/2}\widetilde L_m.                         \tag{6.2}
\]

Thus the exact central normalization survives as the positive metric
character \(m^{-1/2}\), but no longer destroys unitary covariance at the
Hilbert level.

Use the Gelfand triple

\[
 \Phi_{\rm lab}=\mathcal C_{\mathbb R}
 \subset H_{\rm lab}\subset\Phi_{\rm lab}',           \tag{6.3}
\]

and on logarithmic tests

\[
 \mathcal S(\mathbb R)\subset L^2(\mathbb R)
 \subset\mathcal S'(\mathbb R).                       \tag{6.4}
\]

The minimum joint source is their completed projective tensor product,
with the Gamma screw space adjoined:

\[
 \Phi_{\rm ABC}
 =\Phi_{\rm lab}\widehat\otimes\mathcal S(\mathbb R)
 \subset
 H_{\rm lab}\widehat\otimes L^2(\mathbb R)
 \subset\Phi_{\rm ABC}'.                             \tag{6.5}
\]

In (6.5):

* all \(\delta_{p^k}\) remain distinct vectors;
* \(\widetilde L_m\) and \(S_{\log m}\) are isometric actions;
* \(m^{-1/2}\) is the half-Tate metric line, not a Hilbert weight;
* \(\ell,\chi_-,\chi_+\) are continuous boundary distributions on the
  nuclear test space; and
* \(D_\infty\) is a closed Gamma boundary map on the logarithmic factor.

For compact support one then uses the graph completion of the exact
reference feature,

\[
 \|F\|_{X,T}^2=\|X_TF\|^2,                            \tag{6.6}
\]

and regards \(Y_T\) as a bounded map from that completion to its load
space.  Coercivity of the Gamma form proves boundedness for each \(T\).
The remaining sharp assertion is
\(\|Y_T\|_{X,T\to\mathcal Y_T}\leq1\).

This is the minimum useful pivot: it repairs domains, label covariance and
Gamma typing without selecting a spectral sign.  Any further declaration
that the graph map is contractive is precisely D and must come from an
independent positive-monodromy, capacity or Hodge theorem.

## 7. Conclusion

The central-weight Hilbert representation exists and is exact, but it is
too small for the A--B--C contact geometry:

\[
\begin{array}{c|c}
\text{requirement}&\ell^2(\mathbb N,n^{-1})\\ \hline
\delta_m\delta_n=\delta_{mn}&\text{yes}\\
\text{all }p^k\text{ labels}&\text{yes}\\
\text{positive Hilbert norm}&\text{yes}\\
\ell(\delta_n)=\Lambda(n)\text{ continuous}&\text{no}\\
\text{two Tate jets continuous}&\text{no}\\
\text{nonzero bounded Gamma intertwiner}&\text{no}\\
C_TX_T=Y_T\text{ contractive}&\text{not implied}
\end{array}
\]

The rigged pivot (6.5), with the half-Tate line separated from the
isometric label action, is necessary to formulate the comparison without
domain errors.  It does not close row D; it isolates the remaining
non-circular contraction theorem.
