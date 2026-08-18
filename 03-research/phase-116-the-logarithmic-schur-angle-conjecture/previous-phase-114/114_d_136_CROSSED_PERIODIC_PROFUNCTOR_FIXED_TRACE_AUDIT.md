# D.136 — Crossed periodic profunctors and the fixed-contact obstruction

## Verdict

The periodic section categories admit a canonical crossed/profunctorial
action of \(\mathbb N^\times\).  Translation by \(\log n\) on every
periodic curve induces enriched strong monoidal autoequivalences
\(\tau_n\), graph profunctors \(\mathbb P_n\), and coherent products

\[
 \mathbb P_m\otimes_{\mathsf{Sec}_{\rm per}}\mathbb P_n
 \simeq\mathbb P_{mn}.                                  \tag{0.1}
\]

Their formal derived trace is the twisted Hochschild shadow

\[
 \operatorname {Tr}(\mathbb P_n)
 =\mathsf{Sec}_{\rm per}
   \otimes^{\mathbf L}_{\mathsf{Sec}_{\rm per}^{e}}\mathbb P_n. \tag{0.2}
\]

Thus composition of \(\Gamma_n\) can be internalized at the level of
periodic coefficient profunctors without using \(B_{\rm nuc}\) or any zero.

The fixed-point trace does **not** derive the arithmetic contact \(P_n\).
On \(C_p=\mathbb R/(\log p)\mathbb Z\), translation by \(\log n\) has a
fixed point exactly when \(n=p^k\).  Hence the periodic geometry recovers
the correct support predicate.  But when \(n=p^k\) the translation is the
identity and its fixed locus is the whole circle; its derived self-contact
is the loop/Hochschild object with degree-zero and degree-one tangent
pieces and Euler characteristic zero.  It is not

\[
 P_{p^k}=\mathbb F_p
 \quad\text{or}\quad
 K_{p^k}^W=[\mathbb Z\xrightarrow p\mathbb Z].          \tag{0.3}
\]

The circumference \(\log p\) is a metric, not a differential equal to
multiplication by \(p\).  No topological or enriched fixed-point
construction turns one into the other canonically.

There is a second obstruction to a mixed Riemann--Roch complex.  The
periodic determinant is quadratic in the two ruling degrees, but every
\(\tau_n\) preserves those degrees.  Its mixed second cross-effect on the
correspondence directions is therefore zero.  The local fixed traces, even
if decorated by \(P_n\), recover only the finite contact kernel
\(\Lambda(mn)\); they do not contain the Gamma/Poisson term forced by row C.
Moreover the full tropical section modules are not perfect dualizable
objects, so the formal profunctor shadow does not automatically yield a
numerical determinant trace.

The minimum additional datum is precise:

1. the Witt lambda-characteristic orientation
   \(R/(\Phi_n)\otimes_R^{\mathbf L}R/(T-1)\), mapping the periodic fixed
   component to \(K_n^W\);
2. a compatible archimedean Poisson/Gamma trace object; and
3. a bivariant perfect/nuclear mixed determinant whose cross-effect agrees
   with the row-C character.

With (1) adjoined, the crossed periodic trace can be *decorated* to have
contact \(P_n\), but this is exactly the already constructed Witt input of
row B, not a derivation from translations.  With (1)--(3), the desired
mixed theory can be stated; its primitive positivity remains row D.

No paper file is modified.

## 1. Translation action on the periodic section categories

Write

\[
 C_p=\mathbb R/(\log p)\mathbb Z.                       \tag{1.1}
\]

For \(n\geq1\), let

\[
 r_{n,p}:C_p\longrightarrow C_p,
 \qquad t\longmapsto t+\log n.                         \tag{1.2}
\]

The relations

\[
 r_{m,p}r_{n,p}=r_{mn,p},\qquad r_{1,p}=\operatorname{id} \tag{1.3}
\]

are literal.  On the product component \((p,q)\), use
\(r_{n,p,q}=r_{n,p}\times r_{n,q}\).

An object of \(\mathsf{Sec}_{p,q}\) is a pair of divisor degrees
\((d,e)\).  Translation preserves both degrees.  Pullback of periodic
sections along (1.2) therefore gives an enriched strong symmetric monoidal
autoequivalence

\[
 \tau_n^{p,q}:\mathsf{Sec}_{p,q}\longrightarrow
                    \mathsf{Sec}_{p,q},                \tag{1.4}
\]

which is the identity on objects and acts on a section by

\[
 (\tau_n f)(t,u)=f(t-\log n,u-\log n).                 \tag{1.5}
\]

The sign in (1.5) is the pullback convention and has no effect on the
fixed-locus calculation.  Equations (1.3) give coherent isomorphisms

\[
 \tau_m\tau_n\simeq\tau_{mn}.                          \tag{1.6}
\]

Taking the finite-support coproduct over \((p,q)\) defines the action on
\(\mathsf{Sec}_{\rm per}\).  Enriched Yoneda and Day convolution extend it
to the periodic coefficient category \(\mathsf A_{\rm per}\).

## 2. Crossed category and graph profunctors

The semidirect enriched category

\[
 \mathsf{Sec}_{\rm per}\rtimes\mathbb N^\times         \tag{2.1}
\]

has the same objects as \(\mathsf{Sec}_{\rm per}\) and morphism object

\[
 \underline{\operatorname {Hom}}_{\rtimes}(x,y)
 =\bigoplus_{n\geq1}'
   \underline{\operatorname {Hom}}_{\mathsf{Sec}_{\rm per}}
       (x,\tau_n y).                                    \tag{2.2}
\]

The prime denotes finite support in the crossing label.  If
\(f:x\to\tau_n y\) and \(g:y\to\tau_m z\), composition is

\[
 x\xrightarrow{f}\tau_n y
 \xrightarrow{\tau_n(g)}\tau_n\tau_mz
 \simeq\tau_{mn}z.                                     \tag{2.3}
\]

Associativity follows from (1.6) and associativity in
\(\mathsf{Sec}_{\rm per}\).

Equivalently, define the graph profunctor

\[
 \mathbb P_n(x,y)=
 \underline{\operatorname {Hom}}_{\mathsf{Sec}_{\rm per}}
        (x,\tau_n y).                                   \tag{2.4}
\]

The enriched co-Yoneda lemma gives

\[
\begin{aligned}
 (\mathbb P_m\otimes_{\mathsf{Sec}}\mathbb P_n)(x,z)
 &=\int^{y}\mathbb P_m(x,y)\otimes\mathbb P_n(y,z)\\
 &\simeq\mathbb P_{mn}(x,z),                            \tag{2.5}
\end{aligned}
\]

proving (0.1).  Thus \(n\mapsto\mathbb P_n\) is a genuine monoidal
profunctorial realization of the composition law of \(\Gamma_n\).

## 3. Formal trace and the required finiteness distinction

In the bicategory of enriched profunctors, the shadow of (2.4) is the
coend

\[
 \operatorname {Tr}_{\rm form}(\mathbb P_n)
 =\int^x\mathbb P_n(x,x).                              \tag{3.1}
\]

After stabilization/linearization, its derived form is the twisted
Hochschild object (0.2).  This formal trace exists whenever the indicated
derived coend exists; it does not require a sign on \(B_{\rm nuc}\).

One must distinguish this from a numerical categorical trace.  A trace in
the Morita category of perfect stable categories requires the relevant
objects and kernels to be perfect, and a two-dimensional TFT-type trace
requires smoothness/properness (saturation).  Here

* the object set contains a real degree plane on every \((p,q)\);
* the periodic section Hom objects are filtered tropical modules with
  continuum strata; and
* the arithmetic object is an infinite prime-pair coproduct.

They are not finite perfect modules in the Deligne--nuclear category.  The
Yoneda representables are projective in the presheaf category, which is
enough for internal global sections, but projectivity is not
dualizability/perfectness for a numerical Hochschild trace.

Finite periodic-depth coordinate models are dualizable.  Their traces are
finite approximants, but passing to continuous dimension uses the special
normalized determinant limit of row A.  It is not supplied by the formal
coend (3.1).

## 4. Exact spatial fixed loci

The fixed-point equation on \(C_p\) is

\[
 t+\log n\equiv t\pmod{\log p}.                        \tag{4.1}
\]

It has a solution if and only if

\[
 \log n=k\log p\quad(k\in\mathbb Z),                  \tag{4.2}
\]

and, for an integer \(n>1\), this is equivalent to \(n=p^k\), \(k\geq1\).
When (4.2) holds, \(r_{n,p}\) is the identity and every point is fixed.
Otherwise the fixed locus is empty.  Thus

\[
 \operatorname {Fix}(r_{n,p})=
 \begin{cases}
 C_p,&n=p^k,\\
 \varnothing,&\text{otherwise}.
 \end{cases}                                           \tag{4.3}
\]

On \(C_p\times C_q\), simultaneous translation has a fixed point only if
\(n\) is both a power of \(p\) and a power of \(q\).  For \(n>1\) this
forces \(p=q\), after which the fixed locus is the complete product
\(C_p\times C_p\).  Restriction to the geometric diagonal gives the circle
in (4.3).

Equation (4.3) is a real success: periodic geometry detects exactly the
prime-power support of the von Mangoldt contact.

## 5. Why the fixed trace is not \(P_n\)

For \(n=p^k\), the graph of \(r_{n,p}\) equals the diagonal.  Its derived
intersection with the diagonal is therefore the derived self-intersection

\[
 C_p\times^{\mathbf R}_{C_p\times C_p}C_p,             \tag{5.1}
\]

the derived loop/fixed-point object.  In a one-dimensional smooth model,
HKR identifies its local tangent complex with

\[
 \mathcal O_{C_p}\oplus\Omega^1_{C_p}[1].              \tag{5.2}
\]

The two terms have equal rank and alternating Euler characteristic zero.
Topologically this is the ordinary Lefschetz number of an
orientation-preserving circle rotation:

\[
 \operatorname {tr}(r_n^*|H^0(C_p))
 -\operatorname {tr}(r_n^*|H^1(C_p))=1-1=0.           \tag{5.3}
\]

For a nontrivial rotation the geometric fixed locus is empty; for the
identity it is an excess one-dimensional locus.  Neither case produces a
finite torsion module.

By contrast, row B gives

\[
\begin{aligned}
 K_n^W
 &=\mathbb Z[T,T^{-1}]/(\Phi_n(T))
   \otimes_{\mathbb Z[T,T^{-1}]}^{\mathbf L}
   \mathbb Z[T,T^{-1}]/(T-1)\\
 &\simeq[\mathbb Z\xrightarrow{\Phi_n(1)}\mathbb Z],  \tag{5.4}
\end{aligned}
\]

and

\[
 H^0(K_n^W)=P_n\simeq
 \begin{cases}
 \mathbb F_p,&n=p^k,\\
 0,&n\text{ has at least two prime factors}.
 \end{cases}                                           \tag{5.5}
\]

The equality \(\Phi_{p^k}(1)=p\) is arithmetic lambda-characteristic data.
It cannot be recovered from the equation
\(k\log p=0\) in the quotient circle: that equation says the rotation is
the identity and has zero normal differential.  In particular, its
derived normal map is \(1-dr_{p^k}=0\), not multiplication by \(p\).

Hence the periodic fixed trace internalizes the support condition in
(5.5), but not the object \(P_n\), its determinant, or its metric mass
\(\log p\).

## 6. The enriched degree category loses even the spatial localization

There is a further warning.  The autoequivalence (1.4) is the identity on
the object plane \(\mathbb R^2\); only the section Hom objects remember the
rotation.  If one takes the trace solely in
\(\mathsf{Sec}_{p,q}\), without the spatial sheaf factor on
\(C_p\times C_q\), the coend (3.1) has no object-level fixed-point equation
capable of distinguishing a free rotation from the identity.

Therefore a correct Lefschetz localization must retain the spatial factor

\[
 \operatorname {Sh}(C_p\times C_q)\widehat\boxtimes
 \mathsf A_{p,q},                                      \tag{6.1}
\]

not only the degree-enriched category.  Retaining (6.1) restores (4.3),
but Section 5 shows that it still does not restore \(P_n\).

## 7. Obstruction to a mixed RR complex

The intrinsic periodic determinant of row A depends on an object through
its two ruling degrees:

\[
 \log\|\lambda_{RR}(d,e)\|=-de.                       \tag{7.1}
\]

Every \(\tau_n\) preserves \((d,e)\).  Consequently the second cross-effect
of (7.1) in any pure correspondence direction is zero.  Passing to the
semidirect category (2.1) changes morphisms but does not create new line
objects with mixed degrees.

The Witt decoration (5.4) would add the local bilinear contact

\[
 K(e_m,e_n)=\Lambda(mn).                               \tag{7.2}
\]

For powers of \(r\) distinct primes, its matrix is the orthogonal sum of
\(r\) rank-one positive all-ones blocks.  Hence its rank and positive index
are unbounded.  It cannot be the cross-effect of the rank-two ruling form.

More decisively, (7.2) is only the finite-place contact.  The row-C identity
forces the complementary Gamma/Poisson distribution

\[
 B_{\rm nuc}=K+G_\infty.                               \tag{7.3}
\]

Translations on the compact periodic circles contain no real-place
oscillator, Poisson quotient or digamma multiplier.  An Euler trace of
their fixed loci cannot manufacture \(G_\infty\).  Thus there is no complex
constructed solely from (2.1) whose RR cross-effect is the full
\(B_{\rm nuc}\).

This is not a sign obstruction.  It is a typing and rank obstruction
established before asking whether \(B_{\rm nuc}\) is nonpositive.

## 8. Minimum additional datum

The minimal extension has three independent pieces.

### 8.1 Cyclotomic fixed orientation

For every \(n\), supply a natural transformation from the periodic fixed
shadow to the perfect complex

\[
 \mathfrak o_n:\operatorname {Tr}(\mathbb P_n)
 \longrightarrow K_n^W,                               \tag{8.1}
\]

compatible with the reduced \(\star\)-composition.  Concretely its normal
orientation is the Witt lambda-characteristic \(\Phi_n(T)\) evaluated at
\(T=1\).  This is precisely the additional datum already constructed in
row B.  Without it the differential \(p\) in (0.3) is absent.

### 8.2 Archimedean trace object

Adjoin the real periodic/Poisson object whose character is
\(G_\infty\), with the Tate involution identifying the two boundary jets.
This is the Meyer nuclear realization of row C.  It is not a finite-place
fixed locus.

### 8.3 Mixed determinant orientation

Construct a dualizable bivariant object \(\mathbb M\) over the combined
periodic--Witt--Poisson category and an isomorphism

\[
 \delta^2\log\operatorname {Det}(\mathbb M)(f,g)
 \simeq B_{\rm nuc}(f,g).                              \tag{8.2}
\]

Compatibility must include Day composition, the cyclotomic orientations
(8.1), the Gamma trace and principal/Tate shorting.  Equation (8.2) is the
minimum datum that would turn the already proved character identity into a
mixed RR theorem.  Its existence does not by itself prove the Hodge sign;
that would require a positive metric/effectivity theorem on its primitive
part.

## 9. Conclusion

The non-circular geometric audit separates three levels:

\[
 \begin{array}{c|c|c}
 \text{level}&\text{constructed from periodic translations}&\text{result}\\ \hline
 \text{composition}&\mathbb P_m\otimes\mathbb P_n&\mathbb P_{mn}\\
 \text{fixed support}&\operatorname {Fix}(r_{n,p})&n=p^k\\
 \text{fixed contact}&\text{derived loop of }C_p&
      \mathcal O\oplus\Omega^1[1],\ \chi=0\\
 \text{arithmetic contact}&\text{requires }\Phi_n(1)&P_n\\
 \text{ruling RR}&\text{periodic determinant}&d_1d_2\\
 \text{mixed RR}&\text{requires Witt+Poisson orientation}&B_{\rm nuc}
 \end{array}
\]

Thus the crossed periodic category is a valid geometric enhancement of the
composition law and it detects prime-power fixed support.  It does not
derive the torsion contact or the mixed nuclear RR form.  The exact missing
bridge is the cyclotomic normal orientation together with an archimedean
trace and a dualizable mixed determinant object.
