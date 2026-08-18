# Source correspondence geometry: the two stop tests

## 1. Purpose

The objective is to construct an arithmetic correspondence algebra from
the prime-return towers and the archimedean Gamma--polar page, rather than
from the Weil operator or its spectrum. Before attempting a global
intersection product, two necessary tests must be passed.

1. **Hyperbolic-rulings test.** The source must contain two transverse
   isotropic classes \(F_{\mathrm v},F_{\mathrm h}\) with

   \[
   F_{\mathrm v}^2=F_{\mathrm h}^2=0,
   \qquad
   F_{\mathrm v}F_{\mathrm h}=1.
   \tag{1}
   \]

2. **Mixed-prime composition test.** The source correspondences for
   distinct primes must compose with a well-defined degree. The connected
   trace must nevertheless kill their disconnected product, because
   \(\Lambda(pq)=0\) for \(p\ne q\).

The stop rule is fixed in advance:

> If either test has no source-defined solution, the construction stops.
> No intersection form or Hodge-index conjecture is introduced afterward.

Both tests pass at the algebraic source level. The proofs below also show
why this construction does not repeat the earlier spectral-square model.

## 2. The excluded spectral-square construction

Let \(A\) be a finite Weil operator with eigenvalues
\(\varepsilon_0\leq\varepsilon_1\leq\cdots\). The earlier spectral square
used

\[
 \mathcal I_A=A\boxtimes I+I\boxtimes A-2\varepsilon_0I.
 \tag{2}
\]

Its eigenvalues are

\[
 \varepsilon_i+\varepsilon_j-2\varepsilon_0\geq0.
 \tag{3}
\]

Thus \(\mathcal I_A\succeq0\) for every zero configuration. Its
semidefiniteness is created by the ground-state shift and cannot carry the
off-line index. In particular, (2) contains no hyperbolic plane of the
form (1). The present construction starts instead from the graded polar
page and from finite root correspondences; neither is defined from \(A\).

## 3. Test A: the polar page supplies two rulings

### 3.1 The minimal polar Frobenius algebra

The polar determinant page already contains a degree-zero class and a
degree-two class. Write

\[
 \mathcal H_{\mathrm{pol}}=\mathbb R e_0\oplus\mathbb R e_2,
 \qquad
 |e_0|=0,\quad |e_2|=2.
 \tag{4}
\]

Give it the minimal graded Frobenius structure

\[
 e_0e_0=e_0,\qquad e_0e_2=e_2e_0=e_2,\qquad e_2^2=0,
 \tag{5}
\]

with trace

\[
 \mathrm{tr}_{\mathrm{pol}}(e_0)=0,\qquad
 \mathrm{tr}_{\mathrm{pol}}(e_2)=1.
 \tag{6}
\]

The normalization in (6) is the cohomological normalization of the polar
factor \(s(s-1)\): \(e_0\) is the unit and \(e_2\) is the normalized top
class. Once those two requirements are fixed, (5)--(6) are the unique
two-dimensional connected graded Frobenius algebra with no degree-four
class.

On the square, define

\[
 F_{\mathrm v}=e_2\otimes e_0,\qquad
 F_{\mathrm h}=e_0\otimes e_2,
 \tag{7}
\]

and use the product trace

\[
 \mathrm{Tr}_{\square}
 =\mathrm{tr}_{\mathrm{pol}}\otimes
  \mathrm{tr}_{\mathrm{pol}}.
 \tag{8}
\]

### Theorem 3.1 -- Exact hyperbolic plane

The two source classes in (7) satisfy

\[
 \boxed{
 F_{\mathrm v}^2=F_{\mathrm h}^2=0,\qquad
 \mathrm{Tr}_{\square}(F_{\mathrm v}F_{\mathrm h})=1.}
 \tag{9}
\]

Consequently their intersection matrix is

\[
 H_{\mathrm{pol}}
 =\begin{pmatrix}0&1\\1&0\end{pmatrix},
 \qquad
 \mathrm{sig}(H_{\mathrm{pol}})=(1,1).
 \tag{10}
\]

#### Proof

Equations (5) and (7) give

\[
 F_{\mathrm v}^2=e_2^2\otimes e_0=0,\qquad
 F_{\mathrm h}^2=e_0\otimes e_2^2=0.
\]

The cross product is \(e_2\otimes e_2\), whose product trace is one by
(6) and (8). The eigenvalues of (10) are \(1\) and \(-1\). \(\square\)

### 3.2 Interpretation and scope

This is the exact analogue of the vertical and horizontal rulings on the
square of a curve:

\[
 [C\times\mathrm{pt}]\leftrightarrow F_{\mathrm v},\qquad
 [\mathrm{pt}\times C]\leftrightarrow F_{\mathrm h}.
 \tag{11}
\]

The positive direction is not manufactured by shifting a Weil operator.
It is present before degree one is attached and comes from the graded
\(H^0/H^2\) polar page. Therefore Test A passes.

What is not yet proved is that the polar Frobenius multiplication descends
from a global arithmetic curve object or that its primitive complement has
the Hodge sign. Test A supplies the necessary hyperbolic page, not the
global index theorem.

## 4. Test B: mixed-prime root coverings compose

### 4.1 The root-cover category

Let \(R_M=\mathbb Z/M\mathbb Z\). For \(n\geq1\), reduction modulo \(M\)
defines

\[
 \pi_{Mn,M}:R_{Mn}\longrightarrow R_M.
 \tag{12}
\]

Use the unnormalized pullback

\[
 U_n^{(M)}:\ell^2(R_M)\longrightarrow\ell^2(R_{Mn}),
 \qquad
 U_n^{(M)}f=f\circ\pi_{Mn,M}.
 \tag{13}
\]

Every fiber has \(n\) elements, hence

\[
 (U_n^{(M)})^*U_n^{(M)}=nI.
 \tag{14}
\]

This defines the degree

\[
 \deg\Gamma_n=n
 \tag{15}
\]

of the corresponding root-cover correspondence. Its normalized pullback
is \(P_n^{(M)}=n^{-1/2}U_n^{(M)}\).

### Theorem 4.1 -- Mixed-prime composition and degree

For all \(m,n,M\),

\[
 \boxed{
 U_m^{(Mn)}U_n^{(M)}=U_{mn}^{(M)},\qquad
 P_m^{(Mn)}P_n^{(M)}=P_{mn}^{(M)}.}
 \tag{16}
\]

Consequently

\[
 \Gamma_m\circ\Gamma_n=\Gamma_{mn},\qquad
 \deg(\Gamma_m\circ\Gamma_n)=\deg\Gamma_m\,\deg\Gamma_n.
 \tag{17}
\]

For distinct primes \(p,q\) and an auxiliary level \(M\) coprime to
\(pq\), the square

\[
 \begin{CD}
 R_{Mpq}@>>>R_{Mp}\\
 @VVV       @VVV\\
 R_{Mq}@>>>R_M
 \end{CD}
 \tag{18}
\]

is a fiber product of finite cyclic root sets.

#### Proof

Both sides of the first identity in (16) pull a function on \(R_M\) back
along reduction \(R_{Mmn}\to R_M\). The normalization factors multiply,
giving the second identity. Equation (14) then proves multiplicativity of
the degree.

For (18), a compatible pair
\((a\bmod Mp,b\bmod Mq)\) with equal reduction modulo \(M\) has a unique
lift modulo \(Mpq\) by the Chinese remainder theorem applied after fixing
the common residue modulo \(M\). This proves the fiber-product claim.
\(\square\)

Thus distinct prime towers do compose before completion, and their degree
is source-defined. This answers the first half of Test B.

## 5. The connected projector removes the false mixed atom

Composition alone is not enough. The correspondence
\(\Gamma_p\Gamma_q=\Gamma_{pq}\) is a disconnected product of two prime
orbits, whereas the logarithmic derivative of an Euler product has no
von Mangoldt atom at \(pq\) when \(p\ne q\).

Let

\[
 \mathscr P=\bigoplus_p\bigoplus_{k\geq1}\mathbb R X_{p,k}
 \tag{19}
\]

be the space of connected return symbols. The symbol \(X_{p,k}\) labels
the \(k\)-fold return of one primitive \(p\)-orbit; it is not the algebra
product \(X_{p,1}^k\). Form the augmentation-completed symmetric Hopf
algebra

\[
 \widehat{\mathscr E}
 =\prod_{r\geq0}\mathrm{Sym}^r(\mathscr P),
 \qquad
 \Delta X=X\otimes1+1\otimes X.
 \tag{20}
\]

Let \(N=I-\eta\epsilon\) and define the first Eulerian idempotent

\[
 \mathfrak e_1=\log^\star I
 =\sum_{r\geq1}\frac{(-1)^{r-1}}rN^{\star r}.
 \tag{21}
\]

### Theorem 5.1 -- Exact connected extraction

The operator \(\mathfrak e_1\) is an idempotent with

\[
 \boxed{
 \mathrm{Ran}\,\mathfrak e_1=\mathscr P,\qquad
 \mathfrak e_1(X_{p,k})=X_{p,k},\qquad
 \mathfrak e_1(X_1\cdots X_r)=0\quad(r\geq2).}
 \tag{22}
\]

For the group-like Euler element

\[
 \mathcal Z
 =\exp\left(\sum_{p,k\geq1}\frac{X_{p,k}}k\right)
 \tag{23}
\]

and the length derivation

\[
 DX_{p,k}=k\log p\,X_{p,k},
 \tag{24}
\]

one has

\[
 \boxed{
 D\mathfrak e_1\mathcal Z
 =\sum_{p,k\geq1}\log p\,X_{p,k}.}
 \tag{25}
\]

Under the orbit character

\[
 X_{p,k}\longmapsto
 p^{-k/2}\widehat h(k\log p),
 \tag{26}
\]

(25) becomes the complete finite-place term

\[
 \sum_{p,k\geq1}\frac{\log p}{p^{k/2}}
 \widehat h(k\log p).
 \tag{27}
\]

#### Proof

For \(v\in\mathscr P\), the exponential \(\exp(v)\) is group-like.
Convolution of endomorphisms evaluated on a group-like element becomes
ordinary multiplication, so

\[
 \mathfrak e_1\exp(v)=\log\exp(v)=v.
\]

Comparison of homogeneous degrees proves (22). Applying this identity to
(23), followed by (24), gives (25), and (26) gives (27). \(\square\)

In particular,

\[
 \mathfrak e_1(X_{p,1}X_{q,1})=0\qquad(p\ne q),
 \tag{28}
\]

while every connected return \(X_{p,k}\) survives. The disappearance of
the mixed \(pq\) atom is therefore exact and precedes every norm, trace
estimate, or limiting argument. The second half of Test B passes.

## 6. The minimal source correspondence package

The tests identify the smallest algebraic object on which the geometric
program can continue.

### Definition 6.1 -- Source correspondence package

The package \(\mathfrak C_{\mathrm{src}}\) consists of:

1. the polar Frobenius page
   \((\mathcal H_{\mathrm{pol}},e_0,e_2,\mathrm{tr}_{\mathrm{pol}})\);
2. the root-cover category generated by the correspondences
   \(\Gamma_n\), their transposes, and the degree relation (14);
3. the connected orbit Hopf algebra
   \((\widehat{\mathscr E},\mathfrak e_1)\);
4. the finite-place coefficient functional

   \[
   \lambda_{\mathrm{fin}}(X_{p,k})
   =\frac{\log p}{p^{k/2}};
   \tag{29}
   \]

5. the positive Gamma degree-one page and the polar determinant fiber;
6. the common matched finite-part boundary joining the primitive Euler
   row to the Gamma and polar rows.

Every item is defined from prime-root coverings, the positive Gamma spin,
and the pole. No zero, Weil eigenvalue, or spectral ground-state shift is
used.

### Proposition 6.2 -- The package passes the two stop tests

The package \(\mathfrak C_{\mathrm{src}}\) contains a hyperbolic plane of
signature \((1,1)\), admits associative mixed-prime composition with
multiplicative degree, and its connected character is exactly supported
on the prime-power returns with coefficient
\(\Lambda(p^k)/\sqrt{p^k}\).

#### Proof

Theorem 3.1 gives the hyperbolic plane. Theorem 4.1 gives composition and
degree. Theorem 5.1 removes disconnected products and gives the stated
coefficient. \(\square\)

## 7. What may now be constructed

Because both stop tests pass, the geometric program may proceed to the
following source-level tasks:

1. define a global graded correspondence module whose degree-two page has
   the Kunneth form

   \[
   H^2_{\mathrm{src},\square}
   =\mathbb RF_{\mathrm v}
    \oplus(H^1_{\mathrm{src}}\widehat\otimes H^1_{\mathrm{src}})
    \oplus\mathbb RF_{\mathrm h};
   \tag{30}
   \]

2. define composition with transposes and a diagonal trace before any
   Hilbert completion;
3. attach the Gamma determinant fiber and the matched finite-part boundary;
4. prove that diagonal intersections reproduce the complete explicit
   formula;
5. identify the primitive quotient orthogonal to the hyperbolic plane.

Only after tasks 1--5 are complete is it meaningful to ask for a
Hodge-index inequality on the primitive quotient. No such inequality is
claimed here.

## 8. Status

Proved without RH or zero input:

* the earlier spectral-square model fails because its intersection form is
  positive by ground-state shifting;
* the existing polar \(H^0/H^2\) page supplies an exact hyperbolic pair of
  rulings;
* distinct prime root towers form genuine finite fiber-product squares and
  compose with multiplicative degree;
* the first Eulerian idempotent kills every disconnected mixed-prime
  product while retaining every connected prime-power return;
* the resulting primitive character is the literal von Mangoldt channel;
* the minimal source correspondence package passes both precommitted stop
  tests.

Still open:

* a global diagonal/intersection trace joining the finite and archimedean
  pages;
* comparison of the resulting degree one with the CCM resonant degree one;
* the primitive Hodge-index inequality.
