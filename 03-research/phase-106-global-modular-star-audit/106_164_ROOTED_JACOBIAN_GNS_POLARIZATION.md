# 106.164 — Rooted-Jacobian GNS polarization and the critical white-light boundary

## 1. Purpose

The arithmetic Jacobian identifies its finite root datum with the character
group of \(\widehat{\mathbb Z}\), and its tensor product with multiplication
of roots. This note constructs the corresponding global Hilbert module
directly. It is not a direct sum of independent prime fibres: every prime
acts on the same compact root space and the actions multiply exactly.

The construction gives, without using a zero of \(\zeta\),

* a positive global polarization;
* the full multiplicative semigroup action;
* the exact midpoint coefficients \(p^{-k/2}\);
* the local Euler resolvents as matrix coefficients;
* an exact calculation of the critical infinite-product overlap.

The last calculation identifies the remaining descent problem. At the
critical exponent the polarized product representation becomes the regular
``white-light'' sector. Passing from that sector to the CCM resonant
cokernel is therefore a relative-cohomology operation, not a Hilbert-space
completion of the root module.

## 2. The common root Hilbert space

Let
\[
 X=\widehat{\mathbb Z}=\prod_p\mathbb Z_p
\]
with normalized Haar probability measure \(\mu\), and put
\[
 \mathscr H_{\rm rt}=L^2(X,\mu).
\tag{1}
\]
All complex inner products below are conjugate-linear in the first
variable and linear in the second.
The Pontryagin dual of \(X\) is \(\mathbb Q/\mathbb Z\). Thus (1) is the
Hilbert realization of the universal system of roots used in the rooted
description of the arithmetic Jacobian.

For \(n\geq1\), define
\[
 (V_nf)(x)
 =\sqrt n\,\mathbf 1_{nX}(x)f(x/n).
 \tag{2}
\]
Here \(x/n\) is the unique element of \(X\) whose product by \(n\) is
\(x\), when \(x\in nX\).

### Theorem 2.1 — Multiplicative isometric representation

The operators (2) satisfy
\[
 \boxed{
 V_n^*V_n=I,
 \qquad V_mV_n=V_{mn},
 \qquad (V_n^*f)(y)=n^{-1/2}f(ny).}
 \tag{3}
\]

#### Proof

Multiplication by \(n\) maps \(X\) bijectively onto \(nX\), and
\(\mu(nX)=n^{-1}\). Hence
\[
 \begin{aligned}
 \|V_nf\|_2^2
 &=n\int_{nX}|f(x/n)|^2\,d\mu(x)\\
 &=\int_X|f(y)|^2\,d\mu(y).
 \end{aligned}
\]
The same change of variables gives
\[
 \langle V_nf,g\rangle
 =\left\langle f,n^{-1/2}g(n\,\cdot)\right\rangle,
\]
which proves the adjoint formula and \(V_n^*V_n=I\). Applying (2) twice
gives \(V_mV_n=V_{mn}\). \(\square\)

The range projection is
\[
 V_nV_n^*=M_{\mathbf1_{nX}}.
 \tag{4}
\]
Thus nonunits act by genuine unilateral isometries. This is the operator
form of the singular strata of the arithmetic Picard monoid.

## 3. The generic vector and the Euler coefficients

Let \(\Omega=\mathbf1_X\). It is a unit vector.

### Theorem 3.1 — Exact midpoint coefficient

For every \(n\ge1\),
\[
 \boxed{
 V_n^*\Omega=n^{-1/2}\Omega,
 \qquad
 \langle\Omega,V_n\Omega\rangle=n^{-1/2}.}
 \tag{5}
\]
In particular,
\[
 \langle\Omega,V_p^k\Omega\rangle=p^{-k/2}.
 \tag{6}
\]

#### Proof

The adjoint formula in (3), applied to the constant function, gives the
first equality. The second follows by adjunction, and (6) follows from
\(V_p^k=V_{p^k}\). \(\square\)

Consequently, for \(|z|<1\),
\[
 \boxed{
 \left\langle\Omega,(I-zV_p)^{-1}\Omega\right\rangle
 =\frac1{1-zp^{-1/2}}.}
 \tag{7}
\]
The ordinary-prime tower is therefore a matrix coefficient of one
positive global representation. The radial boundary value of the scalar
matrix coefficient in (7), at \(z=e^{-it\log p}\), is the local critical
Euler factor.  The operator inverse itself is asserted only for
\(|z|<1\); no boundary resolvent of the unilateral shift is being used.

For every test sequence for which the following sum is legitimate,
\[
 \left\langle\Omega,
  \sum_{p}\sum_{k\ge1}\log p\,c(k\log p)V_p^k\Omega
 \right\rangle
 =\sum_p\sum_{k\ge1}
   \frac{\log p}{p^{k/2}}c(k\log p).
 \tag{8}
\]
Equation (8) realizes all ordinary von Mangoldt atoms before taking a
trace or an absolute square. It also keeps the multiplicative relations
between distinct primes because \(V_mV_n=V_{mn}\).

## 4. The global root polarization

Regard \(\mathscr H_{\rm rt}\) as a real Hilbert space and set
\[
 \mathscr V_{\rm rt}
 =\mathscr H_{\rm rt,\mathbb R}\oplus
  \mathscr H_{\rm rt,\mathbb R}.
 \tag{9}
\]
Define
\[
 J(f,g)=(-g,f),
 \qquad
 g((f,g),(u,v))
 =\operatorname{Re}\langle f,u\rangle
  +\operatorname{Re}\langle g,v\rangle,
 \tag{10}
\]
and
\[
 \Omega_{\rm rt}(x,y)=g(Jx,y).
 \tag{11}
\]

### Theorem 4.1 — Source-defined positive polarization

The triple \((\Omega_{\rm rt},J,g)\) is a positive Kähler polarization:
\[
 \boxed{
 J^2=-I,
 \quad
 \Omega_{\rm rt}(y,x)=-\Omega_{\rm rt}(x,y),
 \quad
 \Omega_{\rm rt}(x,Jy)=g(x,y),
 \quad g(x,x)>0\ (x\ne0).}
 \tag{12}
\]
Moreover every \(V_n\oplus V_n\) commutes with \(J\) and preserves
\(g\) and \(\Omega_{\rm rt}\).

#### Proof

The first four assertions are the standard real double of a Hilbert
space. The last assertion follows from Theorem 2.1 because \(V_n\) is an
isometry and acts identically in the two components. \(\square\)

This is a global polarization on the root side of the arithmetic
Jacobian. It is defined before analytic continuation, uses one common
root space for all primes, and is not obtained by shifting an indefinite
Weil matrix.

## 5. Local coherent vectors and the Euler product

The restricted product decomposition of \(X\) gives the standard tensor
product relative to the local constant vectors,
\[
 \mathscr H_{\rm rt}
 \cong\widehat\bigotimes_p L^2(\mathbb Z_p).
 \tag{13}
\]
Let \(\mathscr H_{\rm val}\) be the closed subspace of functions invariant
under the local unit groups.  Its local factor has the orthonormal shell
basis
\[
 e_{p,j}
 =\mu(p^j\mathbb Z_p^\times)^{-1/2}
   \mathbf1_{p^j\mathbb Z_p^\times},
 \qquad j\ge0.
 \tag{13a}
\]
On this radial subspace, \(V_p e_{p,j}=e_{p,j+1}\) in the \(p\)-factor;
its unit actions in the other local factors fix the radial vectors.  Thus
the commuting family \((V_p)_p\) is the tensor product of unilateral
shifts on \(\mathscr H_{\rm val}\).

The local Haar vector is
\[
 \Omega_p
 =\sqrt{1-p^{-1}}
   \sum_{j\ge0}p^{-j/2}e_{p,j}.
 \tag{13b}
\]
Consequently \(\Omega=\widehat\otimes_p\Omega_p\) in the standard Haar
representation. For \(\operatorname{Re}s>0\), let
\[
 k_{p,s}
 =\sqrt{1-p^{-2\operatorname{Re}s}}
   \sum_{j\ge0}p^{-js}e_{p,j}.
 \tag{14}
\]
Then \(\|k_{p,s}\|=1\) and
\[
 V_p^*k_{p,s}=p^{-s}k_{p,s}.
 \tag{15}
\]

For \(s=\sigma+it\) and \(w=\sigma+iu\),
\[
 \boxed{
 \langle k_{p,s},k_{p,w}\rangle
 =\frac{1-p^{-2\sigma}}
        {1-p^{-2\sigma-i(u-t)}}.}
 \tag{16}
\]

### Theorem 5.1 — Global coherent overlap

For \(\sigma>1/2\), the product coherent vectors exist in the incomplete
tensor product whose reference vectors are \(e_{p,0}\), and satisfy
\[
 \boxed{
 \left\langle k_{\sigma+it},k_{\sigma+iu}\right\rangle
 =\prod_p
  \frac{1-p^{-2\sigma}}
       {1-p^{-2\sigma-i(u-t)}}
 =\frac{\zeta(2\sigma+i(u-t))}{\zeta(2\sigma)}.}
 \tag{17}
\]

#### Proof

The criterion relative to \(\widehat\otimes_pe_{p,0}\) is
\(\sum_p\|k_{p,s}-e_{p,0}\|^2<\infty\), which is equivalent to
\(\sum_p p^{-2\sigma}<\infty\), hence to \(\sigma>1/2\). Multiplying
(16) and using the absolutely convergent Euler product gives (17).
\(\square\)

The normalized overlap is thus an arithmetic covariance kernel. Its
positive definiteness is automatic in that product representation, while
its logarithmic derivatives contain the complete prime-power tower.

The representation in Theorem 5.1 is not the Haar representation (13).
Indeed, (13b) and \(\sum_p p^{-1}=\infty\) show that
\(\widehat\otimes_p\Omega_p\) and
\(\widehat\otimes_pe_{p,0}\) are inequivalent incomplete tensor products.
Both are GNS representations of the same quasilocal root algebra. This is
the first, representation-theoretic form of the critical transition, not
an identification to be suppressed.

## 6. Critical collapse to white light

### Theorem 6.1 — Orthogonality at the critical boundary

For fixed \(t\ne u\),
\[
 \boxed{
 \lim_{\sigma\downarrow1/2}
 \left\langle k_{\sigma+it},k_{\sigma+iu}\right\rangle=0,}
 \tag{18}
\]
whereas the overlap equals \(1\) for \(t=u\).

#### Proof

By (17), the numerator \(\zeta(2\sigma+i(u-t))\) has a finite limit when
\(u-t\ne0\), while \(\zeta(2\sigma)\to+\infty\). The diagonal overlap
is identically one. \(\square\)

Thus the boundary limit of the coherent-state covariance is
\[
 \langle k_t,k_u\rangle=\mathbf1_{t=u}.
 \tag{19}
\]
The direct-sum GNS representation of these mutually disjoint boundary
states is the regular, nonseparable white-light sector. The continuous
scaling orbit has lost strong continuity: distinct times are orthogonal.
The Haar vector \(\Omega\) is the \(t=0\) boundary state in its own GNS
sector, by (13b).

This is exactly the divergent generic contribution in the semilocal trace
formula. Removing it is not an orthogonal subspace operation inside the
critical product Hilbert space. It is a relative/renormalized operation
whose finite remainder is the Weil distribution.

## 7. The descent theorem and its obstruction

Let \(E\) denote the CCM restriction/summation morphism and let
\(H^1_{\rm CCM}\) denote its Schwartz/Meyer cokernel. The construction
above gives a positive source module and realizes all finite-place
coefficients. It does not yet put a positive metric on the resonant
cokernel.

The reason is topological and can be stated independently of \(\zeta\).

### Proposition 7.1 — Dense-range descent obstruction

Let \(D:E\to F\) be a continuous map of pre-Hilbert spaces with dense
range. If a seminorm \(q\) on the algebraic cokernel \(F/D(E)\) has the
property that \(q\circ\pi\) is continuous for the Hilbert norm of \(F\),
then \(q=0\).

#### Proof

The continuous seminorm \(q\circ\pi\) vanishes on \(D(E)\). It therefore
vanishes on its closure, which is all of \(F\). Since \(\pi\) is
surjective, \(q=0\). \(\square\)

The resonant CCM classes are retained precisely by using a nonreduced
nuclear topology; the corresponding reduced Hilbert cokernel is zero.
Proposition 7.1 proves that the positive metric (12) cannot be transferred
to those classes by a continuous Hilbert quotient. A successful global
polarization must instead be an intersection or residue pairing on the
derived relative object, followed by a positivity theorem. The
alternating residue pairing of 106.163 supplies the first part. Its
Rosati positivity is the remaining part.

## 8. What is now constructed

The following data are unconditional and source-defined:

1. the common root Hilbert space \(L^2(\widehat{\mathbb Z})\);
2. the multiplicative isometries \(V_n\);
3. the exact coefficients \(p^{-k/2}\) as matrix coefficients;
4. the local Euler resolvents and the full von Mangoldt distribution;
5. a positive global Kähler polarization commuting with every \(V_n\);
6. the coherent Euler-product kernel \(\zeta(2\sigma+i\tau)/\zeta(2\sigma)\);
7. the exact critical white-light limit;
8. the theorem excluding continuous Hilbert descent to nonreduced CCM
   degree one.

The remaining construction is therefore not a polarization of the root
module—it has now been built. It is a **polarized relative cohomology of
the pair consisting of the arithmetic Picard monoid and its generic
white-light orbit**, whose intersection form on the torsion/resonant
quotient agrees with the CCM Rosati trace. Positivity of that relative
intersection form is not proved here.

## 9. Primary geometric input

The identification of \(\widehat{\mathbb Z}\) with the universal finite
root system, the tensor product of roots, the arithmetic Picard/Jacobian
monoids, and the interpretation of the divergent semilocal trace as the
generic orbit are taken from Connes and Consani, *On the Jacobian of the
arithmetic curve*. Equations (2)–(19) are the operator realization of
those data.
