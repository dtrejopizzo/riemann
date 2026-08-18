# 114.a.140 — I7: contact-framed arithmetic kernels integrate dynamics and incidence

~~~
+------------------------------------------------------------------------+
| KERNEL      Gamma_n has diagonal carrier and faithful torsor T_n.        |
| PRIME FRAME Its p-contact F_p is the canonical H_1 cotangent retract.    |
| COMPOSITE   Tensor reduced H_1 modules over the prime support of n.       |
| CONTACT     The resulting reduced object is M_n and has mass Lambda(n).  |
| MONOID      Torsors and contact frames both compose under mn.             |
| REMAINING   Extend the G-7 principal/RR/Green pairing to these kernels.   |
+------------------------------------------------------------------------+
~~~

## 1. Canonical prime data

On a cofinal supportwise level of \(Y^{locreg}\), fix a prime \(p\). The
prime ruling quotient gives the cotangent complex \(C_p\) pulled to the
diagonal. By a69, projection and diagonal functoriality give a canonical
split pair

\[
 \mathbb F_p[1]\xrightarrow{s_p}C_p
 \xrightarrow{\rho_p}\mathbb F_p[1],
 \qquad \rho_p s_p=\operatorname{id}.                                \tag{1.1}
\]

Passing to homology gives a canonical split retract
\(\mathbb F_p\leftrightarrows H_1(C_p)\). Independently, a61/a66 give the
faithful unit torsor \(T_p\), and a111/a132 realise its prime lattice on the
repaired square. Thus the prime arithmetic kernel carries both pieces of data

\[
 \mathbf K_p=(X\xleftarrow{\rm id}X\xrightarrow{\rm id}X;
              T_p;\mathbb F_p\leftrightarrows H_1(C_p)).              \tag{1.2}
\]

The contact frame in (1.2) is derived from the ruling quotient and
cotangent functoriality; it is not chosen from its cardinality.

## 2. All arithmetic labels

For \(n=\prod p^{v_p(n)}>1\), put

\[
 T_n=\bigotimes_pT_p^{\otimes v_p(n)},\qquad
 M_n^{red}=\bigotimes_{p\mid n}^{\mathbb Z}\mathbb F_p,               \tag{2.1}
\]

using one reduced contact factor per distinct prime. Prime powers retain
\(\mathbb F_p\); two distinct primes tensor to zero. The corresponding
contact sheaf is exactly \(\mathcal M_n\) from a46.

Define

\[
 \mathbf K_n=(X\xleftarrow{\rm id}X\xrightarrow{\rm id}X;
              T_n;\mathcal M_n;
              \{\mathbb F_p\leftrightarrows H_1(C_p)\}_{p\mid n}).    \tag{2.2}
\]

The last entry records the cotangent provenance of every nonzero prime
factor. We do **not** tensor the shifted ambient complexes:
\(\mathbb F_p[1]\otimes\mathbb F_p[1]\) changes degree. Composition is
instead performed on the canonical \(H_1\)-retracts, exactly where a45/a46
prove the idempotent prime-power law.

## 3. Contact-framed composition

Compose carriers by fiber product, torsors by tensor product and contact
sheaves by tensor product. Retain the union of the prime cotangent
provenance frames. Associativity and symmetry are the coherence maps of
these tensor products.

### Theorem 3.1

There are coherent canonical isomorphisms

\[
 \mathbf K_m\circ\mathbf K_n\simeq\mathbf K_{mn}.                     \tag{3.1}
\]

The torsor component is \(T_m\otimes T_n\simeq T_{mn}\) from a70. The
contact component is

\[
 \mathcal M_m\otimes\mathcal M_n\simeq\mathcal M_{mn}                 \tag{3.2}
\]

from a45/a46. For every surviving prime factor, a69 supplies its canonical
split \(H_1\)-projector; repeated powers use
\(\mathbb F_p\otimes\mathbb F_p\simeq\mathbb F_p\), and mixed primes give
the zero sheaf. This proves (3.1) without identifying shifted ambient
complexes.

### Corollary 3.2

The reduced diagonal-contact functor on the arithmetic submonoid satisfies

\[
 \operatorname{Cont}^{red}(\mathbf K_n)=\mathcal M_n,\qquad
 \log\#\Gamma(Y,\mathcal M_n)=\Lambda(n).                             \tag{3.3}
\]

Thus faithful dynamics, actual prime incidence, derived contact extraction,
prime-power stability and mixed-prime cancellation now belong to one
contact-framed kernel object.

## 4. Exact remaining integration

This closes the first four clauses of the corrected, reduced-contact
H7-DYN-INTEGRATE from a139 on the arithmetic kernel submonoid. The fifth
clause remains:

> **H7-FRAMED-RR.** Extend the principal equivalence, boundary descent and
> RR/Green intersection of G-7 to the contact-framed kernels
> \(\mathbf K_n\), compatibly with composition and with the already
> constructed reduced contact projector.

H7-FRAMED-RR contains no new dynamic or finite-contact problem. Its Picard
faithfulness part is H7-RSPH-UNIT; its global comparison part is the
two-target Deligne/Green gate already present in a127/a124.

No assertion is made that the prime ambient excess \(E_p\) vanishes or that
ambient cotangent complexes compose idempotently. The \(H_1\)-retract is
canonical precisely so that these assertions are unnecessary for the
\(\Lambda\) contact.

## 5. Status

I7 dynamic-contact integration is closed positively in a typed bivariant
subcategory. Row A remains open at H7-FRAMED-RR and the G-7 boundary/RR
comparison. No RH statement is used.

The verifier 114_a_140_i7_contact_framed_verify.py checks contact-module
tensor algebra, torsor exponent composition, contact cancellation and scope.
