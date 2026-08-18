# 106.163 — Derived residue symplectic form and the polarization gate

## 1. Purpose

The ordinary symplectic quotient of principal divisors collapses
(106.162), whereas the CCM cokernel retains the resonances in a
nonreduced topology.  This note constructs the alternating form directly
on a finite resonant derived quotient, without naming or assuming any
zero.  The construction is the one-dimensional Grothendieck residue
pairing for the completed arithmetic multiplier.

The result supplies the missing derived symplectic form and proves its
exact weight-one covariance.  It also gives a sharp descent test: a
positive compatible complex structure commuting with scaling can descend
to this quotient only if every enclosed zero is on the critical line.

## 2. The source-defined resonant quotient

Put
\[
 \Xi(z)=2\xi\!\left(\frac12+z\right).
 \tag{1}
\]
Then
\[
 \Xi(-z)=\Xi(z),
 \qquad
 \overline{\Xi(\bar z)}=\Xi(z),
 \qquad
 \Xi(0)\ne0.
 \tag{2}
\]

Let \(D\Subset\mathbb C\) be a bounded domain with smooth boundary,
invariant under \(z\mapsto-z\) and \(z\mapsto\bar z\), such that
\(\Xi\) has no zero on \(\partial D\).  Define the finite analytic
quotient
\[
 \mathcal H_D
 =\mathcal O(\overline D)\big/\Xi\mathcal O(\overline D).
 \tag{3}
\]
Equivalently, (3) is degree one of the two-term Koszul complex
\[
 \mathcal O(\overline D)
 \xrightarrow{\;M_\Xi\;}
 \mathcal O(\overline D).
 \tag{4}
\]
It is finite dimensional, with dimension equal to the number of zeros of
\(\Xi\) in \(D\), counted with multiplicity.  The definition uses only
the completed Euler--Gamma multiplier \(\Xi\), not a list of its zeros.

## 3. The alternating residue form

For classes represented by \(f,g\in\mathcal O(\overline D)\), set
\[
 \boxed{
 \Omega_D([f],[g])
 =\frac{1}{2\pi i}
   \int_{\partial D}
   \frac{f(z)g(-z)}{\Xi(z)}\,dz.}
 \tag{5}
\]

### Theorem 3.1 — Perfect derived symplectic pairing

The form (5) is well defined, complex bilinear, alternating, and
nondegenerate on \(\mathcal H_D\).

#### Proof

If \(f\) is replaced by \(f+\Xi a\), the change in (5) is
\[
 \frac{1}{2\pi i}\int_{\partial D}a(z)g(-z)\,dz=0.
\]
The same argument, using \(\Xi(-z)=\Xi(z)\), applies in the second
variable.  To interchange \(f\) and \(g\), substitute \(z=-w\).  The
domain and its boundary are invariant under this rotation, and
\[
 \Omega_D([g],[f])
 =-\frac{1}{2\pi i}
   \int_{\partial D}
   \frac{f(w)g(-w)}{\Xi(w)}\,dw
 =-\Omega_D([f],[g]).
 \tag{6}
\]

For nondegeneracy, decompose the Artin algebra (3) into its local factors
at the finite zero divisor of \(\Xi\) in \(D\).  On a local factor
\(\mathcal O_a/(\Xi)\), the ordinary Grothendieck residue
\[
 ([u],[v])\longmapsto
 \operatorname{Res}_{z=a}\frac{u(z)v(z)}{\Xi(z)}\,dz
 \tag{7}
\]
is perfect.  The involution \(z\mapsto-z\) identifies the factor at
\(-a\) with the dual factor in (7).  Summing these perfect local pairings
gives (5), so its radical is zero. \(\square\)

The real involution
\[
 \kappa[f](z)=\overline{f(\bar z)}
 \tag{8}
\]
preserves \(\mathcal H_D\).  On the fixed real form
\(\mathcal H_{D,\mathbb R}\), conjugate residues occur in pairs, so
\(\Omega_D\) is real valued.  Thus (5) is a genuine real symplectic form
on the finite resonant quotient.

## 3.1 The separated Rosati trace form

The perfect residue duality (5) retains nilpotent zero jets.  The CCM
trace pairing is a different, complementary Frobenius functional: the
trace of multiplication.  Define the holomorphic involution
\[
 f^\sharp(z)=\overline{f(-\bar z)}
 \tag{8a}
\]
and
\[
 \mathfrak h_D([f],[g])
 =\operatorname {Tr}_{\mathcal H_D}
     M_{\,f g^\sharp}.
 \tag{8b}
\]
Equivalently,
\[
 \boxed{
 \mathfrak h_D([f],[g])
 =\frac{1}{2\pi i}\int_{\partial D}
   \frac{\Xi'(z)}{\Xi(z)}f(z)g^\sharp(z)\,dz.}
 \tag{8c}
\]
The equality is the holomorphic functional-calculus trace formula.

The form (8b) is Hermitian.  Its radical is the nilradical of the Artin
algebra (3), so it is nondegenerate on the separated quotient
\[
 \mathcal H_D^{\rm sep}
 =\mathcal H_D/\operatorname {Nil}(\mathcal H_D).
 \tag{8d}
\]
On that quotient define
\[
 \Omega_D^{\rm Ros}=-\operatorname {Im}\mathfrak h_D,
 \qquad
 g_D^{\rm Ros}=\operatorname {Re}\mathfrak h_D.
 \tag{8e}
\]
This is the finite analytic model of the form in 106.157.  In evaluation
coordinates it pairs the point \(z\) with \(-\bar z\), exactly the
functional-equation involution
\(\rho\leftrightarrow1-\bar\rho\).  No derivative weight
\(1/\Xi'(z)\) occurs in (8b).

Both dualities are needed conceptually:

* (5) is the perfect shifted symplectic duality on the nonreduced derived
  zero scheme;
* (8b) is the separated Rosati trace form whose positivity is the Weil
  criterion.

## 4. Exact weight-one action

Define
\[
 T_t[f](z)=
 \left[e^{t(1/2+z)}f(z)\right],
 \qquad t\in\mathbb R.
 \tag{9}
\]
Multiplication by the nonvanishing entire exponential preserves the
ideal in (3), so (9) is well defined.

### Theorem 4.1 — Polarized similitude before positivity

For every \(u,v\in\mathcal H_D\),
\[
 \boxed{
 \Omega_D(T_tu,T_tv)=e^t\Omega_D(u,v).}
 \tag{10}
\]

#### Proof

The two factors in the numerator of (5) acquire the product
\[
 e^{t(1/2+z)}e^{t(1/2-z)}=e^t.
\]
It is independent of \(z\) and leaves the contour integral otherwise
unchanged. \(\square\)

Thus the functional equation supplies, without spectral input, precisely
the alternating weight-one pairing expected of degree one.

The same calculation gives
\[
 \boxed{
 \mathfrak h_D(T_tu,T_tv)=e^t\mathfrak h_D(u,v)}
 \tag{10a}
\]
on \(\mathcal H_D^{\rm sep}\), because
\((T_tg)^\sharp(z)=e^{t(1/2-z)}g^\sharp(z)\).  Consequently both
\(\Omega_D^{\rm Ros}\) and \(g_D^{\rm Ros}\) have weight one.

## 5. The exact positivity obstruction

Let \(A_D\) be multiplication by \(z\) on the separated quotient, so
\[
 T_t=e^{t/2}e^{tA_D}.
 \tag{11}
\]

### Theorem 5.1 — Positive descent forces criticality

Assume there is a real-linear operator
\[
 J_D:\mathcal H_{D,\mathbb R}^{\rm sep}
 \to\mathcal H_{D,\mathbb R}^{\rm sep}
 \tag{12}
\]
such that
\[
\begin{aligned}
 J_D^2&=-I,\\
 \Omega_D^{\rm Ros}(J_Du,J_Dv)&=\Omega_D^{\rm Ros}(u,v),\\
 g_D(u,v)&:=\Omega_D^{\rm Ros}(u,J_Dv)
     \quad\text{is positive definite},\\
 J_DT_t&=T_tJ_D\qquad(t\in\mathbb R).
\end{aligned}
\tag{13}
\]
Then every zero \(\rho\) of \(\xi\) represented in \(D\) satisfies
\[
 \boxed{\operatorname{Re}\rho=\frac12.}
 \tag{14}
\]

#### Proof

Let \(U_t=e^{-t/2}T_t=e^{tA_D}\).  From (10a), (13), and commutation,
\[
\begin{aligned}
 g_D(U_tu,U_tv)
 &=\Omega_D^{\rm Ros}(U_tu,J_DU_tv)\\
 &=e^{-t}\Omega_D^{\rm Ros}(T_tu,T_tJ_Dv)
 =g_D(u,v).
\end{aligned}
\tag{15}
\]
Hence \(U_t\) is a finite-dimensional orthogonal group for the positive
metric \(g_D\).  Its generator \(A_D\) is skew-adjoint.  Therefore
\(A_D\) is diagonalizable and
\[
 \operatorname{Spec}(A_D)\subset i\mathbb R.
\tag{16}
\]
The spectrum of multiplication by \(z\) on (8d) is the reduced zero
support of \(\Xi(z)\) in \(D\).  Since \(z=\rho-\tfrac12\), (16) gives
(14).  The separated quotient has already removed the nilpotent Jordan
directions, so no simplicity assertion is being made. \(\square\)

### Theorem 5.2 — Exact finite signature

Let \(Z_D\) be the reduced zero set of \(\Xi\) in \(D\), and let
\[
 j(a)=-\bar a.
 \tag{16a}
\]
Then evaluation identifies
\[
 \mathcal H_D^{\rm sep}\simeq\bigoplus_{a\in Z_D}\mathbb C,
 \tag{16b}
\]
and
\[
 \boxed{
 \mathfrak h_D(f,g)
 =\sum_{a\in Z_D}m_a f(a)\overline{g(j(a))},}
 \tag{16c}
\]
where \(m_a\) is the order of the zero at \(a\).
Each fixed point of \(j\) contributes one positive square.  Each
two-cycle \(\{a,j(a)\}\) contributes a Hermitian block
\[
 m_a\begin{pmatrix}0&1\\1&0\end{pmatrix}
 \tag{16d}
\]
of inertia \((1,1)\).  Consequently
\[
 \boxed{
 n_-(\mathfrak h_D)
 =\#\{\text{two-cycles of }j\text{ in }Z_D\}.}
 \tag{16e}
\]

#### Proof

The reduced finite algebra is the product of one copy of \(\mathbb C\)
for each point of \(Z_D\).  The trace inherited from the local Artin
factor has weight equal to its length \(m_a\).  Multiplication by
\(f g^\sharp\) is diagonal, and its trace is therefore (16c).  On a
fixed point \(a=j(a)\), the contribution to
\(\mathfrak h_D(f,f)\) is \(|f(a)|^2\).  On a two-cycle
\(\{a,b\}\), it is
\[
 f(a)\overline{f(b)}+f(b)\overline{f(a)},
\]
whose matrix is (16d) and whose eigenvalues are \(1,-1\).  Summing the
orthogonal orbit blocks proves (16e). \(\square\)

In the original variable, \(j(a)=a\) is exactly
\(\operatorname{Re}\rho=1/2\).  Thus the polarization problem has no
unseen finite-dimensional remainder: its negative index is literally the
number of off-line functional-equation pairs in the window.

## 6. Consequence for the Fourier--Poisson complex

The chain complex of 106.156 already has a positive complex structure
\(J_{\rm FW}\).  A faithful descent
\[
 H^1(\mathfrak C_{\rm FW,rel})
 \longrightarrow\mathcal H_D
 \tag{17}
\]
which intertwines scaling, the alternating forms, and \(J_{\rm FW}\)
would produce an operator \(J_D\) satisfying (13).  Theorem 5.1 then
proves the critical-line statement in \(D\).

Thus functoriality of Fourier, Poisson summation, and the local Tate
polarizations establish (5) and (10), but do not by themselves prove the
positive descent of \(J_{\rm FW}\).  That descent is not a missing
continuity lemma: on every spectral window it is exactly the assertion
that the normalized resonant flow is unitarizable.

### Theorem 6.1 — Finite \(C^*\)-descent criterion

For the separated algebra
\[
 A_D=\mathcal H_D^{\rm sep}
\tag{17a}
\]
with involution \(\sharp\), the following are equivalent:

1. \(\mathfrak h_D(f,f)\ge0\) for every \(f\in A_D\);
2. \((A_D,\sharp)\) admits a faithful representation
   \(\pi_D:A_D\to\mathcal B(\mathscr K_D)\) with
   \(\pi_D(f^\sharp)=\pi_D(f)^*\);
3. the involution \(j(a)=-\bar a\) fixes every point of \(Z_D\);
4. every zero represented in \(D\) lies on the critical line.

#### Proof

The equivalence of (1), (3), and (4) is Theorem 5.2.  If (3) holds, then
\(A_D\) is a product of copies of \(\mathbb C\) with ordinary complex
conjugation, and diagonal multiplication is the required faithful
\(*\)-representation, proving (2).

Conversely, suppose \(j\) has a two-cycle \(\{a,b\}\).  In its
\(\mathbb C^2\) factor choose \(x=(1,-1)\).  Since
\[
 x^\sharp=(-1,1),
 \qquad
 x^\sharp x=(-1,-1),
\tag{17b}
\]
a \(*\)-representation would give
\[
 \pi_D(x)^*\pi_D(x)
 =-\pi_D(1_{\{a,b\}}).
\tag{17c}
\]
The left side is positive and the right side is negative.  Faithfulness
excludes equality, so (2) implies (3). \(\square\)

Therefore “descent into the positive Cauchy/Fourier module” has a precise
meaning: it must be a faithful \(*\)-representation of the finite
resonant algebra.  Theorem 6.1 proves that constructing such a map is
already the complete finite-window critical-line theorem; positivity
cannot be inherited merely because the source chain complex was Hilbert.

In particular, if \(G^*=-G\) is the generator of the normalized positive
coefficient flow, a functional-calculus map
\[
 [f]\longmapsto f(G)
\tag{17d}
\]
can factor through (3) only on a subspace on which
\[
 \Xi(G)=0.
\tag{17e}
\]
Its spectral support is contained in \(i\mathbb R\).  It is faithful on
\(A_D\) exactly when the entire reduced zero support \(Z_D\) is contained
in \(i\mathbb R\).  Thus (17e) is not an auxiliary annihilation identity:
faithfulness of that identity is the same condition as Theorem 6.1.

## 7. What has been constructed

Without using zeros as input:

* a finite source-defined derived quotient of the completed arithmetic
  multiplier;
* a perfect alternating residue pairing on it;
* the exact weight-one scaling law;
* a rigorous comparison target for the chain-level positive
  Fourier--Poisson structure.

The sole unproved clause is now literal:
\[
 \boxed{
 J_{\rm FW}\text{ descends faithfully through the nonreduced adelic
 cone to }J_D\text{ with }g_D>0.}
 \tag{18}
\]
Theorem 5.1 proves that (18), in a cofinal exhaustion of \(D\), already
implies RH.  Hence (18) cannot be supplied by the reduced \(L^2\)
completion, the separable Hardy quotient, or ordinary principal-divisor
reduction; those three mechanisms were ruled out in 106.158,
106.161, and 106.162 respectively.
