# D.43 — Paugam–OS–Krein dichotomy on the exact Meyer cokernel

## 1. Scope and result

Let

\[
 R=\sigma_\zeta(\mathcal L_\gamma^0)=Z\mathcal H_\cap,
 \qquad V=\mathcal H_-/R                                      \tag{1.1}
\]

with the Frechet quotient topology supplied by D.42.  This note audits the
remaining reflection-positive route on this **exact topological cokernel**.
No zero of zeta is used to define a scalar product, a quotient or a
subspace.

There are two canonical completions suggested by the two-chart construction:

1. the ordinary critical-boundary `L^2` completion;
2. the nuclear Frechet quotient equipped with the Tate--Paugam pairing.

They obey the following sharp dichotomy.

> **Theorem 1.1 (OS--Paugam dichotomy).**
> The ordinary critical-boundary completion is positive and centrally
> unitary, but its quotient is zero.  The Frechet quotient `V` is nonzero,
> faithful to Meyer's character and carries the unconditional nondegenerate
> Tate--Paugam pairing.  On `V`, however, a positive Hilbertizable reflected
> form which is simultaneously faithful, centrally unitary and
> trace-compatible exists if and only if the Weil form has the required
> sign, equivalently if and only if RH holds.
>
> Consequently the two charts, Tate reflection and Paugam's pairing do not
> by themselves construct row D.  They identify its missing assertion
> exactly: positivity of the reflected Paugam form (or, equivalently, a
> positive Weil polarization of the Meyer cokernel).

The theorem is not a no-go against a future source-defined polarization.
It is a no-go against claiming that the canonical boundary norm or the
unconditional symplectic pairing already supplies one.

## 2. Tate reflection and the weight-one pairing

Write `lambda_t` for the scaling action on `V`.  The functional equation
gives the antilinear Tate reflection

\[
 (\Theta u)(s)=\overline{u(1-\bar s)}.                         \tag{2.1}
\]

The two-chart gluing in D.42 makes (2.1) continuous on the source and on the
cokernel.  Its covariance is

\[
 \Theta\lambda_t=t\lambda_{t^{-1}}\Theta.                     \tag{2.2}
\]

The factor `t` is indispensable: this is weight-one Tate duality, not an
ordinary commuting reflection.

Paugam's trace construction supplies, on the same spectral realization, a
continuous nondegenerate antisymmetric pairing

\[
 \psi:V\widehat\otimes V\longrightarrow\mathbb C(1),
 \qquad
 \psi(\lambda_tv,\lambda_tw)=t\psi(v,w).                       \tag{2.3}
\]

At test-function level it is the antisymmetrized compact supertrace

\[
 \psi(F,G)=\mathrm{Tr}
   \bigl(F*JG-G*JF\mid H_+^1\bigr),                             \tag{2.4}
\]

with `J` the inversion operator.  Paugam proves that (2.4) is well defined,
antisymmetric, equivariant and nondegenerate.  These statements are
unconditional.  In particular, (2.3) is the symplectic Poincare pairing
already used in D.37.

Combining `psi` with the real/conjugate involution gives the natural
sesquilinear reflected form

\[
 H_P(v,w)=\psi(v,Cw),                                           \tag{2.5}
\]

where `C` denotes the conjugation on the real spectral realization (the
placement of `C` versus `Theta` is convention-dependent; the resulting
partner map is `rho -> 1-bar(rho)`).  Hermitian symmetry and
nondegeneracy follow from Paugam's symmetries.  **Positive definiteness does
not**: Paugam explicitly obtains positivity of (2.5) under RH, not before
it.

## 3. The boundary OS quotient is exactly zero

On the critical line, the two Gamma charts have a common positive norm
because `|gamma(1/2+i tau)|=1`.  It is tempting to use this norm as the OS
pre-Hilbert norm.  D.41 proves that this loses the cokernel completely:

\[
 \overline{\Xi E}^{L^2}=L^2,
 \qquad
 \Xi E\subseteq R,
 \qquad
 L^2/\overline R^{L^2}=0.                                    \tag{3.1}
\]

For completeness, the density in (3.1) has no spectral assumption.  The
critical traces of `E` contain translates of a Gaussian and are dense in
`L^2`; multiplication by `Xi(1/2+i tau)` has dense range because `Xi` is
bounded and nonzero almost everywhere.  Hence `Xi E` is already dense.

Thus the ordinary OS boundary construction satisfies positivity and the
central unitary covariance only vacuously on the quotient.  It fails both
faithfulness and trace compatibility, since Meyer's nonzero odd character
cannot be the character of the zero space.

## 4. Central unitarity plus trace faithfulness forces the critical line

Put

\[
 \rho_t=t^{-1/2}\lambda_t.                                    \tag{4.1}
\]

Suppose a positive Hilbert completion `H` of `V` has all of the following:

* the map `V -> H` is injective on the generalized spectral classes;
* every `rho_t` extends to a unitary operator;
* the integrated representation has Meyer's nuclear character, with
  multiplicities.

Let `ell_rho` be a nonzero generalized eigenfunctional corresponding to a
nontrivial zero `rho`.  The transpose scaling action has character

\[
 \rho_t'\ell_\rho=t^{\rho-1/2}\ell_\rho                 \tag{4.2}
\]

(with the inverse exponent under the opposite convention; the modulus
conclusion is identical).  A unitary representation has only unitary
characters on every finite-dimensional generalized eigenspace.  Therefore

\[
 |t^{\rho-1/2}|=1\quad\hbox{for all }t>0,
 \qquad\text{hence}\qquad \mathrm{Re}\,\rho=\tfrac12.     \tag{4.3}
\]

Trace compatibility prevents deleting an offending class: deleting it
would change the distribution character and its multiplicity.  Faithfulness
prevents putting it in the Hilbert nullspace.  Thus (4.3) applies to every
nontrivial zero seen by row C.  This proves

\[
 \boxed{
 \text{faithful positive central-unitary trace completion}
 \ \Longrightarrow\ \mathrm{RH}.}                              \tag{4.4}
\]

Conversely, under RH the partner of every spectral point is itself and
Paugam's formula reduces to a sum of squares (with the standard limiting
interpretation for multiplicities).  Completing after the radical gives a
positive centrally unitary spectral Hilbert space with the same character.
Hence the existence assertion in Theorem 1.1 is equivalent to RH.

This converse is an equivalence statement, not a source construction:
using the zero divisor to build the completion is forbidden as a proof of
row D.

## 5. Exact Krein block obstruction

The failure of automatic positivity is visible on a single possible
off-line partner pair.  Let

\[
 \sigma(\rho)=1-\bar\rho,
 \qquad
 \mathcal K_\rho=\mathbb C e_\rho\oplus\mathbb C e_{\sigma(\rho)}.
\]

The fundamental symmetry of the reflected Paugam/Weil form restricts to

\[
 J_\rho=
 \begin{pmatrix}0&1\\1&0\end{pmatrix}.                         \tag{5.1}
\]

Its normalized eigenvectors

\[
 e_+=2^{-1/2}(e_\rho+e_{\sigma(\rho)}),
 \qquad
 e_-=2^{-1/2}(e_\rho-e_{\sigma(\rho)})                         \tag{5.2}
\]

have signs `+1` and `-1`.  Thus every faithful subspace containing the full
pair is indefinite.  Keeping only the positive line is not a solution:

1. it kills the antisymmetric spectral class and is not faithful;
2. unless `rho=sigma(rho)`, the positive line is not invariant under the
   normalized scaling, because its two coordinates have distinct
   characters;
3. removing either character changes the trace distribution.

This is the exact operator obstruction requested by the OS/Krein audit.
It does **not** assert that an off-line zero exists.  It proves that, if one
exists, no positive-sector projection can retain simultaneously
faithfulness, central unitarity and the row-C trace.

Equivalently, on the unconditional Krein realization the sampling range is
the graph of an angular operator `K`, and

\[
 H_P\ge0
 \quad\Longleftrightarrow\quad
 \|K\|\le1
 \quad\Longleftrightarrow\quad
 \mathrm{RH}.                                                    \tag{5.3}
\]

## 6. Comparison with the nuclear Weil form

The comparison must be stated at the character level, not by declaring
the two forms equal.  Let `f` be primitive,

\[
 \widehat f(0)=\widehat f(1)=0,
 \qquad g(t)=t^{1/2}f(t),                                      \tag{6.1}
\]

and let

\[
 T_g=\int_0^\infty g(t)\rho_t\,d^*t.                           \tag{6.2}
\]

If `H_P` were positive and trace-compatible, central unitarity would give

\[
 T_g^*=T_{g^\sharp},
 \qquad T_gT_g^*\ge0.                                          \tag{6.3}
\]

The row-C supercharacter, together with the vanishing of the two even polar
characters in (6.1), then gives the exact pullback proved in D.37:

\[
 \boxed{
 B_{\rm nuc}(f,f)
   =-\mathrm{Tr}_{(V,H_P)}(T_gT_g^*)\le0.}                 \tag{6.4}
\]

Thus the diagonal reflected Paugam form and `B_nuc` are two realizations of
the same nuclear character with the conventional primitive minus sign.
D.32 already proves the term-by-term prime-power and Gamma comparison;
D.37 proves (6.4) from a hypothetical polarization.  No additional
chain-level equality is needed, and none is asserted here without the
positive completion.

Conversely, nonpositivity of `B_nuc` on all primitive tests is Weil's
criterion and supplies positivity of the spectral reflected form after
quotient by its radical.  Therefore

\[
 \boxed{
 H_P\text{ positive and trace-compatible}
 \ \Longleftrightarrow\
 B_{\rm nuc}|_{\rm primitive}\le0
 \ \Longleftrightarrow\
 \mathrm{RH}.}                                                   \tag{6.5}
\]

The first equivalence uses trace faithfulness.  Without it, one can make a
positive quotient merely by discarding negative blocks, but the result no
longer realizes row C.

## 7. Why local OS factorization cannot repair the sign

The finite-prime Weil density is

\[
 G_p(r)=\frac{2\log p}{p|1-z|^2}
       \bigl(\sqrt p\cos(r\log p)-1\bigr),
 \qquad z=p^{-1/2}e^{ir\log p}.                                \tag{7.1}
\]

It has both signs:

\[
 G_p(0)=\frac{2\log p}{\sqrt p-1}>0,
 \qquad
 G_p\!\left(\frac\pi{\log p}\right)
   =-\frac{2\log p}{\sqrt p+1}<0.                              \tag{7.2}
\]

Hence the reflected form cannot be obtained by tensoring positive local
prime OS forms.  Its sign is necessarily global: the Gamma contribution
and all finite places must be coupled before taking positivity.  This
agrees with the two-chart conclusion and rules out a hidden local repair.

## 8. Final audit table

| Candidate | Positive | central unitary | faithful | row-C trace | Verdict |
|---|---:|---:|---:|---:|---|
| critical-boundary `L^2` quotient | yes | yes | no | no | zero by (3.1) |
| full Paugam Frechet/Krein cokernel | indefinite a priori | Krein-isometric | yes | yes | unconditional object |
| positive spectral sector only | yes | generally no | no | no | deletes swap data |
| positive faithful Paugam completion | exactly the missing sign | yes | yes | yes | equivalent to RH |

## 9. Status

Closed in this note:

1. the two-chart/Tate/Paugam data yield an unconditional nondegenerate
   weight-one Krein pairing on the exact Frechet cokernel;
2. ordinary boundary OS completion has zero quotient;
3. the exact off-line obstruction is the swap block (5.1);
4. a positive-sector projection necessarily loses invariance, faithfulness
   or trace compatibility;
5. the reflected Paugam form compares with `B_nuc` through the exact row-C
   character identity (6.4);
6. existence of the requested positive completion is equivalent to RH.

Not closed: a source-defined proof that the form in (2.5) is positive.  That
assertion is row D itself; neither Paugam's unconditional symplectic theorem
nor the two-chart Gamma comparison proves it.

### References used

* F. Paugam, *Symetries spectrales des fonctions zeta*, J. Theorie des
  Nombres de Bordeaux **21** (2009), 713--720; arXiv:0803.0199.
* D.42 for the exact Frechet range--cokernel comparison.
* D.41 for the critical-boundary `L^2` collapse.
* D.37 for polarization, central unitarity and the trace-square identity.
* D.32 for the exact prime-power and Gamma pullback to `B_nuc`.
* Equation (7.1), obtained directly from the local phase derivative in
  D.33, for the local-prime indefiniteness calculation.
