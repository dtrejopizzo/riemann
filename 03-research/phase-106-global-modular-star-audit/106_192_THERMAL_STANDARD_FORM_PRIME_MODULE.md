# 106.192 — The thermal standard-form prime module

## 1. Purpose

The pure rooted vector of 106.164 has the correct coefficient
\(p^{-k/2}\), but its critical real orbit becomes white light: distinct
times lie in disjoint incomplete tensor-product sectors.  The nuclear
Euler module of 106.188 restores a single coefficient space, but its
natural continuous action is parameter translation rather than the CCM
scale action.

This note tests the standard Hilbert-space form of the critical geometric
state.  It has three exact properties:

1. it reproduces \(p^{-k/2}\) as an exact left--right matrix coefficient,
   but the two vectors are collinear by the KMS relation;
2. its infinite-prime real gauge action is strongly continuous because
   every local reference vector is fixed;
3. its charge spectrum is the full dense group
   \(\log\mathbb Q_+^\times\), with the Poisson kernel retained inside
   each charge sector.

No zero of \(\zeta\) and no analytic continuation is used.  The
collinearity is the decisive outcome: ordinary thermal doubling does not
create a second arithmetic direction carrying the missing sign.

## 2. One prime in standard form

Fix a prime \(p\), put \(r=p^{-1}\), and let

\[
 H_p=\ell^2(\mathbb N_0),\qquad
 Ne_j=je_j,\qquad Se_j=e_{j+1}.                             \tag{1}
\]

Define the trace-one geometric density

\[
 \rho_p=(1-r)r^N                                           \tag{2}
\]

and its standard-form Hilbert space

\[
 \mathcal K_p=\mathfrak S_2(H_p),\qquad
 \langle X,Y\rangle_2=\operatorname {Tr}(X^*Y),\qquad
 \Omega_p=\rho_p^{1/2}.                                    \tag{3}
\]

Then \(\|\Omega_p\|_2=1\).  Left and right multiplication will be
denoted by

\[
 L_p(A)X=AX,\qquad R_p(A)X=XA.                              \tag{4}
\]

### Theorem 2.1 — Exact critical coefficient

For every \(k\ge0\),

\[
 \boxed{
 \left\langle L_p(S^k)\Omega_p,
                 R_p(S^k)\Omega_p\right\rangle_2
 =p^{-k/2}.}                                                \tag{5}
\]

More precisely,

\[
 \boxed{
 R_p(S^k)\Omega_p
 =p^{-k/2}L_p(S^k)\Omega_p,\qquad
 \|L_p(S^k)\Omega_p\|_2=1,\quad
 \|R_p(S^k)\Omega_p\|_2=p^{-k/2}.}                         \tag{5a}
\]

#### Proof

Using

\[
 \rho_p^{1/2}
 =\sqrt{1-r}\sum_{j\ge0}r^{j/2}|e_j\rangle\langle e_j|,    \tag{6}
\]

one obtains

\[
 \begin{aligned}
 \left\langle S^k\rho_p^{1/2},\rho_p^{1/2}S^k\right\rangle_2
 &=\operatorname {Tr}\left(
    \rho_p^{1/2}S^{*k}\rho_p^{1/2}S^k\right)\\
 &=(1-r)\sum_{j\ge0}r^{j/2}r^{(j+k)/2}
 =r^{k/2}.
 \end{aligned}                                             \tag{7}
\]

The diagonal commutation relation

\[
 \rho_p^{1/2}S^k=r^{k/2}S^k\rho_p^{1/2}                   \tag{7a}
\]

proves (5a), and then (5) follows immediately. \(\square\)

The coefficient in (5) is therefore a modular eigenvalue, not an
interference amplitude between independent charged vectors.  The
standard form packages the KMS boundary relation exactly, but does not
by itself add a polarization direction.

## 3. The complete local charge module

For \(a,b\ge0\), set

\[
 E_{a,b}^{(p)}=S^a\rho_p^{1/2}S^{*b}.                       \tag{8}
\]

### Theorem 3.1 — Charge orthogonality and the Poisson overlap

The vectors (8) have norm one and

\[
 \boxed{
 \left\langle E_{a,b}^{(p)},E_{c,d}^{(p)}\right\rangle_2
 =\begin{cases}
 p^{-|c-a|/2},&a-b=c-d,\\
 0,&a-b\ne c-d.
 \end{cases}}                                              \tag{9}
\]

#### Proof

Expanding (8) gives

\[
 E_{a,b}^{(p)}
 =\sqrt{1-r}\sum_{j\ge0}r^{j/2}
   |e_{j+a}\rangle\langle e_{j+b}|.                        \tag{10}
\]

Two matrix units in the expansions have nonzero Hilbert--Schmidt inner
product precisely when

\[
 j+a=k+c,qquad j+b=k+d,                                   \tag{11}
\]

which requires \(a-b=c-d\).  If, for example,
\(c=a+h,d=b+h\) with \(h\ge0\), then \(j=k+h\), and (10) gives

\[
 (1-r)\sum_{k\ge0}r^{(k+h)/2}r^{k/2}=r^{h/2}.              \tag{12}
\]

The case \(h<0\) follows by conjugation. \(\square\)

Thus different multiplicative charges are orthogonal, while the common
valuation direction inside one charge retains exactly the local Poisson
kernel.

## 4. Strong real scaling before any descent

Put

\[
 u_{p,t}=p^{itN},\qquad
 \mathcal U_{p,t}X=u_{p,t}Xu_{p,t}^*.                      \tag{13}
\]

Then \(\mathcal U_{p,t}\Omega_p=\Omega_p\), and

\[
 \boxed{
 \mathcal U_{p,t}E_{a,b}^{(p)}
 =p^{it(a-b)}E_{a,b}^{(p)}.}                               \tag{14}
\]

Let

\[
 \mathcal K_{\rm th}
 =\widehat\bigotimes_p(\mathcal K_p,\Omega_p).             \tag{15}
\]

Because every local reference vector is fixed, the finite tensor-product
actions extend to a strongly continuous unitary group

\[
 \mathcal U_t=\widehat\bigotimes_p\mathcal U_{p,t}          \tag{16}
\]

on (15).  Finite excitations form a dense invariant core, and their
charges are

\[
 \sum_p(a_p-b_p)\log p=\log q,qquad
 q\in\mathbb Q_+^\times.                                  \tag{17}
\]

Therefore

\[
 \boxed{
 \mathcal U_tE_{\mathbf a,\mathbf b}
 =q^{it}E_{\mathbf a,\mathbf b}.}                          \tag{18}
\]

Unlike the pure critical product of 106.164, (16) is a single strongly
continuous representation.  The price is doubling: the midpoint
coefficient is now the left--right overlap (5).

## 5. Global arithmetic coefficients

For \(n=\prod_pp^{k_p}\), define

\[
 \ell_n=\bigotimes_p S_p^{k_p}\rho_p^{1/2},
 \qquad
 r_n=\bigotimes_p\rho_p^{1/2}S_p^{k_p}.                    \tag{19}
\]

Theorem 2.1 gives

\[
 \boxed{
 \langle\ell_m,\ell_n\rangle=\delta_{m,n},\qquad
 r_n=n^{-1/2}\ell_n,\qquad
 \langle r_m,r_n\rangle=\delta_{m,n}n^{-1},\qquad
 \langle\ell_m,r_n\rangle=\delta_{m,n}n^{-1/2}.}          \tag{20}
\]

Hence every von Mangoldt atom is an exact matrix coefficient:

\[
 \boxed{
 \sum_{p,k\ge1}(\log p)c(k\log p)
 \langle\ell_{p^k},r_{p^k}\rangle
 =\sum_{p,k\ge1}\frac{\log p}{p^{k/2}}c(k\log p).}        \tag{21}
\]

The apparent two-dimensional Gram block at \(n\ge2\) is

\[
 G_n=\begin{pmatrix}1&n^{-1/2}\\n^{-1/2}&n^{-1}\end{pmatrix},
 \qquad \det G_n=0.                                        \tag{22}
\]

Thus the complete prime tower is carried by a positive standard-form
module with a strongly continuous real action, but its left--right line
has rank one.  Thermal purification alone cannot be the missing odd
polarization.

## 6. Why the construction is not yet the CCM polarization

The action (16) is the gauge action on arithmetic charges.  Under the
Fourier synthesis

\[
 (\mathcal Fa)(\xi)=\sum_qa_qe^{i\xi\log q},               \tag{23}
\]

it becomes translation of \(\xi\), whereas CCM scaling on the spectral
target is multiplication by \(e^{it\xi}\).  Passing from one to the other
requires continuous induction.

If continuous induction is performed freely, the total-energy
coordinate turns (23) into a fiberwise row.  The coisometry theorem of
106.189 then applies: the degree-one range defect is lost.  Consequently
the doubled module solves the white-light and coefficient problems, but
not by itself the relative descent problem.

The complete charge sectors of Theorem 3.1 still contain nontrivial
multiplicity in the common-valuation direction.  A viable non-free
coupling would have to act on that multiplicity before charge collapse;
the rank-one line (20) is insufficient.  In total-energy coordinates an
archimedean multiplier acting before collapse necessarily depends on the
internal charge:

\[
 \boxed{
 \Gamma_{\rm nf}(E)_{q,q}
 =\Gamma_\infty(E-\log q),}                                \tag{24}
\]

or, more generally, be an operator-valued matrix
\(B_\infty(E)_{q,r}\) on the charge multiplicity space.  A scalar
multiplier \(\Gamma_\infty(E)I\) after collapse is Euler-blind by
106.189.

Equation (24) is forced by total-energy bookkeeping, but it is only a
necessary form.  Because of the rank-one identity (22), a diagonal
operator of the form (24) is not sufficient: the polar boundary must mix
the common-valuation multiplicities or introduce a genuinely relative
off-diagonal connection.

## 7. Status

Proved without RH or zero input:

* a standard-form prime module carrying the full real gauge action;
* exact realization of every coefficient \(p^{-k/2}\) as a modular
  left--right coefficient;
* the local Poisson overlap inside every charge sector;
* a single strongly continuous infinite-prime representation, avoiding
  the pure-state white-light split;
* exact realization of the complete ordinary von Mangoldt tower;
* the rank-one collapse of the apparent thermal double;
* the charge-dependent form (24), and proof that diagonal dependence
  alone cannot supply the missing direction.

Still required:

* construct an off-diagonal relative differential on the
  common-valuation multiplicities, using (24), the polar boundary, and
  the CCM restriction row;
* prove that its torsion degree one is the CCM cokernel rather than a free
  coisometric collapse;
* show that the induced Hilbert norm satisfies the three hypotheses of
  106.191.
