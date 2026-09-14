# P122 -- an affine integer carrier for Gamma and Euler

## Status

`IMPORTED INGREDIENTS + PROVED COMBINATION/APPLICATION`.  The `ax+b`
semigroup representation, Bost--Connes Hamiltonian, Lerch determinant and
Gauss multiplication formula are classical.  This note puts them on one
arithmetic Hilbert space and checks the particular quarter-Gamma/Euler
combination and `log p` anomaly needed by the programme.  It does not prove
Gates R or S and does not give row (d).

For the imported operator-algebra context see J. Cuntz, *C*-algebras
associated with the `ax+b`-semigroup over `N`,
<https://arxiv.org/abs/math/0611541>, and J.-B. Bost--A. Connes,
*Hecke algebras, type III factors and phase transitions with spontaneous
symmetry breaking in number theory*,
<https://cds.cern.ch/record/283504/>.

The construction combines two earlier ingredients without repeating their
failed claims: D.194 constructed the multiplicative Witt/Fock isometries
and proved that their ordinary Hilbert defects do not equal reduced contact;
106.195 constructed the Gamma Hurwitz determinant on a separate oscillator.
Here their common integer basis and additive successor are tested in the
repository for the first time as a transmission algebra.  No claim is made
that the underlying `ax+b` representation is new in the literature.

## 1. The affine arithmetic Hilbert space

Let

\[
 \mathcal H_{\rm aff}=\ell^2(\mathbb N_0),
 \qquad e_k\leftrightarrow n=k+1.                 \tag{1.1}
\]

Define the additive successor, multiplicative isometries and integer
Hamiltonian by

\[
 Se_k=e_{k+1},\qquad
 V_me_k=e_{m(k+1)-1},\qquad
 He_k=\log(k+1)e_k.                                \tag{1.2}
\]

### Proposition 1.1 -- affine semigroup relations

For positive integers `m,n`,

\[
 \begin{aligned}
 V_m^*V_m&=I,& V_mV_n&=V_{mn},\\
 V_mS&=S^mV_m,& V_m^*HV_m&=H+(\log m)I,\\
 e^{-\beta H}V_me^{\beta H}&=m^{-\beta}V_m
 \quad(\beta\in\mathbb R).                       \tag{1.3}
 \end{aligned}
\]

#### Proof

Every formula follows on the basis.  The affine relation, for example,
sends `e_k` on both sides to `e_(m(k+2)-1)`.  The last two formulas use
`log(m(k+1))=log m+log(k+1)`.  QED.

At `beta=1/2`, the last identity produces the physical half-density
`m^(-1/2)`.  Differentiating the modular covariance in `beta` produces
`log m`.  Thus the two scalar ingredients of
`(log p)p^(-j/2)` arise from the same source Hamiltonian before a Weil-form
comparison.

## 2. The Gamma oscillator is a function of the Euler Hamiltonian

For `a>0`, put

\[
 A_a e_k=(k+a)e_k.                                  \tag{2.1}
\]

At the central quarter twist,

\[
 \boxed{A_{1/4}=e^H-\frac34I.}                    \tag{2.2}
\]

Its spectral zeta and determinant are

\[
 \operatorname {Tr}A_a^{-w}=\zeta_H(w,a),
 \qquad
 \det_\zeta A_a={\sqrt{2\pi}\over\Gamma(a)}.     \tag{2.3}
\]

Thus the positive quarter-Gamma oscillator and the Euler energy `log n`
are not merely placed in an orthogonal direct sum: they are exact functions
of the same integer observable.

The additive successor does not commute with the Euler Hamiltonian,

\[
 [H,S]e_k=\log\left(1+{1\over k+1}\right)e_{k+1}, \tag{2.4}
\]

and the affine relation `V_mS=S^mV_m` mixes the additive Gamma ladder with
multiplicative Frobenius fibres before any trace is taken.

## 3. Residue-class transmission

For a prime `p` (indeed for every integer `p>=2`) and
`r=0,...,p-1`, define

\[
 W_{p,r}e_k=e_{pk+r}.                                \tag{3.1}
\]

These isometries have orthogonal ranges and

\[
 \sum_{r=0}^{p-1}W_{p,r}W_{p,r}^*=I,
 \qquad V_p=W_{p,p-1}.                              \tag{3.2}
\]

The exact Gamma transmission law is

\[
 \boxed{
 W_{p,r}^*A_aW_{p,r}
 =pA_{(r+a)/p}.}                                    \tag{3.3}
\]

Unlike an orthogonal prime direct sum, (3.2)--(3.3) use all residue classes
of the same additive oscillator.  Frobenius is one distinguished residue
range inside a complete Gamma decomposition.

## 4. Gauss determinant anomaly

### Theorem 4.1 -- exact zeta-determinant descent

For `a>0`,

\[
 \boxed{
 \det_\zeta A_a
 =\prod_{r=0}^{p-1}\det_\zeta
       \bigl(pA_{(r+a)/p}\bigr)
 =p^{1/2-a}
   \prod_{r=0}^{p-1}\det_\zeta A_{(r+a)/p}.}       \tag{4.1}
\]

#### Proof

The first equality is the orthogonal spectral partition (3.3).  Scaling a
zeta determinant gives

\[
 \det_\zeta(cA_b)=c^{\zeta_H(0,b)}\det_\zeta A_b,
 \qquad \zeta_H(0,b)=\frac12-b.                    \tag{4.2}
\]

Summing the exponents for `b=(r+a)/p` gives

\[
 \sum_{r=0}^{p-1}\left(\frac12-{r+a\over p}\right)
 =\frac12-a.                                       \tag{4.3}
\]

The remaining equality is also Gauss's multiplication formula

\[
 \prod_{r=0}^{p-1}\Gamma\left({r+a\over p}\right)
 =(2\pi)^{(p-1)/2}p^{1/2-a}\Gamma(a).              \tag{4.4}
\]

Substitution of (2.3) proves (4.1).  QED.

### Corollary 4.2 -- the local Frobenius connection coefficient

Taking the logarithm of the second equality in (4.1) and differentiating
in `a` gives

\[
 \boxed{
 {d\over da}\left[
  \log\det_\zeta A_a
  -\sum_{r=0}^{p-1}\log\det_\zeta A_{(r+a)/p}
 \right]
 =-\log p.}                                        \tag{4.5}
\]

Equivalently,

\[
 \psi(a)=\log p+{1\over p}
 \sum_{r=0}^{p-1}\psi\left({r+a\over p}\right). \tag{4.6}
\]

Thus `log p` is the normal-connection anomaly between one Gamma oscillator
and its `p` affine residue fibres.  It is not inserted as a trace weight.
Together with the modular half-density in (1.3), iteration of the
distinguished Frobenius range produces

\[
                         (\log p)p^{-j/2}.          \tag{4.7}
\]

This is precisely the local normalization demanded by A/B/C.

## 5. The candidate carrier added to D

Let `mathfrak A_aff` be the involutive operator algebra on the common core
of finite sequences generated by

\[
 S,S^*,\{V_p,V_p^*\}_p,H,\{A_a^{-1}\}_{a>0},
 \{W_{p,r},W_{p,r}^*\}_{p,r}.                     \tag{5.1}
\]

The new source object is

\[
 D^{\rm aff}
 =(\mathfrak A_{\rm aff},\mathcal H_{\rm aff},H,A_{1/4},
   S,\{W_{p,r}\},\text{Real conjugation}).         \tag{5.2}
\]

It has four properties absent from the direct tensor assembly:

1. Gamma and Euler live on one integer basis;
2. the additive and multiplicative dynamics do not commute;
3. unique factorization is retained by the `V_p`;
4. `log p` is a relative determinant anomaly of the Gamma ladder itself.

No zero of `zeta`, no target form and no positivity selection enters
(5.1)--(5.2).

## 6. Exact limitations

The old Fock no-go remains valid.  The ordinary range defect of `V_(p^j)`
has the wrong rank and does not equal reduced contact.  Equation (4.5) is a
determinant-connection anomaly, not a positive Hilbert defect.

For a composite modulus `m`, the same residue decomposition gives `log m`,
whereas `Lambda(m)` is zero when `m` has at least two distinct prime
factors.  The physical contact must therefore apply (4.5) to primitive
prime fibres and their iterates, using the row-B cyclotomic/torsion selector;
it may not sum the anomaly over arbitrary modulus objects.

Most importantly, (4.5) is local in the source parameter `a`.  It does not
yet prove that a compressed first-contact section has matching sharp-window
traces or equal `p` and `q` seam outputs.  Gates R and S remain open.

The immediate next calculation is forced and finite: construct the
two-prime compressed affine boundary complex generated by
`S,V_p,V_q,P_T`, compute its Green boundary form, and test whether its
horizontal kernel supplies Gate R or Gate S without using `Delta_T`.

```text
common Gamma--Euler integer carrier                 CONSTRUCTED
affine relation V_p S=S^p V_p                       PROVED
quarter oscillator A_(1/4)=exp(H)-3/4               PROVED
Gauss determinant anomaly d/da=-log p               PROVED
physical half-density from modular covariance       PROVED
reduced contact from ordinary V_p defect             REFUTED (D.194)
two-prime horizontal transmission                    OPEN
row (d)                                              OPEN
```
