# P121 -- the universal orientation-Rees bridge

## Status and correction

The useful part of the former `central-jet` proposal is algebraic, but
its metric interpretation was too strong. Row-(b) contacts are indexed by
`(p,j)`, with length `j log p`, whereas the tame divisor is indexed by
Euler zeroes `(p,k)`. A displacement of the metric character acts on the
first indexing set and moves the divisor on the second; it does **not** give
a componentwise diagram between them. The moving-divisor derivative also
contains a Gauss--Manin term. We therefore remove that claim.

What survives without any identification of indices is a universal Rees
parameter for the two normal orientations. It gives an exact bridge from
the scalar sum to the oriented character, commutes with tame localization,
and is independent of row (d).

## 1. Universal orientation character

Let

\[
 R^{\leftrightarrow}=R\oplus R,
 \qquad
 \operatorname {str}(r_+,r_-)=r_++r_-,
 \qquad
 \operatorname {or}(r_+,r_-)=\frac{r_--r_+}{2}.
\tag{1.1}
\]

Put `A=C[z,z^(-1)]` and define

\[
 \chi_{\rm or}:R^{\leftrightarrow}\longrightarrow R\otimes A,
 \qquad
 \chi_{\rm or}(r_+,r_-)=z^{-1}r_+ +zr_- .
\tag{1.2}
\]

The variable `z` records the normal orientation only. It is not a metric
parameter and carries no prime or spectral label.

### Theorem 1.1 -- value/normal-jet reconstruction

The map

\[
 (r_+,r_-)\longmapsto
 \left(\chi_{\rm or}(r)|_{z=1},
       \frac12(z\partial_z\chi_{\rm or}(r))|_{z=1}\right)
\tag{1.3}
\]

is the isomorphism `(str,or)`. In particular

\[
 \chi_{\rm or}(r)|_{z=1}=\operatorname {str}(r),
 \qquad
 \frac12(z\partial_z\chi_{\rm or}(r))|_{z=1}
 =\operatorname {or}(r).
\tag{1.4}
\]

#### Proof

At `z=1`, (1.2) is `r_++r_-`; its logarithmic derivative is
`-r_++r_-`. The inverse is

\[
 r_+=\frac12\operatorname {str}(r)-\operatorname {or}(r),
 \qquad
 r_-=\frac12\operatorname {str}(r)+\operatorname {or}(r).
\]

QED.

Equivalently, over the dual numbers `D=C[delta]/(delta^2)`, the specialization
`z=1+delta/2` is

\[
 \chi_{\rm or}^{[1]}(r)
 =\operatorname {str}(r)+\delta\operatorname {or}(r).
\tag{1.5}
\]

Thus the first neighbourhood of the augmentation `z=1` remembers exactly
the coordinate erased by scalar supertrace.

## 2. Compatibility with oriented relative K2

For a finite Euler divisor `D`, use the already constructed localization

\[
 0\to\mathcal K_{2,D}^{\rm nr,\leftrightarrow}
 \to\mathcal K_{2,D}^{\rm Eul,\leftrightarrow}
 \xrightarrow{\ell\partial_D^{\leftrightarrow}}
 \mathcal R_D^{\leftrightarrow}\to0 .
\tag{2.1}
\]

Tensoring the target with `A` and applying (1.2) gives the universal
oriented tame regulator

\[
 \operatorname {Reg}_{D}^{\rm or}
 :=\chi_{\rm or}\circ\ell\partial_D^{\leftrightarrow}.
\tag{2.2}
\]

For the physical relative Euler pair

\[
 r_{p,k}(F)=
 \bigl(-K_F(\lambda_{p,k}),K_F(\lambda_{p,k})\bigr),
 \qquad
 \lambda_{p,k}=-\frac12+\frac{2\pi i k}{\log p},
\tag{2.3}
\]

one obtains

\[
 \operatorname {Reg}_{p,k}^{\rm or}(F)
 =(z-z^{-1})K_F(\lambda_{p,k}).
\tag{2.4}
\]

Consequently

\[
 \operatorname {Reg}_{p,k}^{\rm or}(F)|_{z=1}=0,
 \qquad
 \frac12z\partial_z
 \operatorname {Reg}_{p,k}^{\rm or}(F)|_{z=1}
 =K_F(\lambda_{p,k})=c^{(1)}_{p,k}(F).
\tag{2.5}
\]

### Theorem 2.1 -- Rees-localization exactness

The following diagram is well typed and commutes:

\[
\begin{array}{ccc}
 \mathcal K_{2,D}^{\rm Eul,\leftrightarrow}
 &\xrightarrow{\ell\partial_D^{\leftrightarrow}}&
 \mathcal R_D^{\leftrightarrow}\\[1mm]
 &&\downarrow\chi_{\rm or}\\[1mm]
 &&\mathcal R_D\otimes\mathbb C[z,z^{-1}].
\end{array}
\tag{2.6}
\]

Reduction at `z=1` is scalar supertrace. Its first normal jet is the
oriented boundary `c^(1)`. On the physical antidiagonal subspace the Rees
regulator is faithful.

#### Proof

Commutativity is the definition (2.2). Equations (1.4) give the two
specializations. On an antidiagonal vector `(-h,h)`, (1.2) equals
`(z-z^(-1))h`; the Laurent polynomial ring is a domain, so it vanishes
only for `h=0`. QED.

No contact label `(p,j)` has been identified with a divisor label `(p,k)`.
The tame/seam comparison remains the separate Fourier theorem already
proved in `P121_ORIENTED_K2_LOCALIZATION_EXACTNESS.md`.

## 3. The exact bridge condition

Let `N_T=ker Delta_T` be a first-contact radical. The missing implication
can now be stated without choosing a sign or a metric deformation:

> **ORL (orientation-Rees lift).** For `F in N_T`, the relative Euler
> class which gives (2.3) has zero universal oriented regulator,
> not merely zero augmentation at `z=1`:
> \[
>  \operatorname {Reg}_{D}^{\rm or}(F)=0
>  \quad\hbox{in }\mathcal R_D\otimes\mathbb C[z,z^{-1}]
>  \tag{3.1}
> \]
> for every finite Euler divisor `D`.

If ORL holds, Theorem 2.1 gives `c^(1)_(p,k)(F)=0` at every retained
label. The cofinal first-harmonic theorem then gives the full Tate-moment
tower, hence `K_F=0` and `F=0`. Thus ORL closes first contact, the global
square and row (d).

The point of (3.1) is not to rename scalar cancellation. The augmentation
map

\[
 \operatorname {ev}_1:\mathbb C[z,z^{-1}]\to\mathbb C
\tag{3.2}
\]

has the nonzero ideal `(z-1)` as kernel, and the physical class (2.4) lies
in that kernel for every source. Therefore row (c) at `z=1` alone cannot
imply ORL. A proof must construct the row-(c) equality **equivariantly in
the orientation variable before augmentation**.

## 4. Why the old central-metric argument is not ORL

For a row-(b) contact `(p,j)`, central displacement gives the weights
`exp(-u j log p)` and `exp(u j log p)`. On the Euler divisor, however,
the same displacement moves

\[
 e_{p,u}(s)=1-p^{-1/2-u-s}=0.
\]

Differentiating its tame symbol differentiates both the residue and the
point at which it is evaluated. This produces a Gauss--Manin/source-motion
term involving `K_F'`; it is not multiplication of every `(p,k)` residue
by `exp(+/-u log p)`. Hence the former componentwise central diagram was
invalid.

The Rees parameter avoids that error: it acts on the two copies of the
already localized normal fibre, leaving the divisor fixed. Phase 114's
central metric derivative and the present orientation-normal derivative
are different operations.

## 5. Precise progress ledger

```text
oriented relative K2 localization                     PROVED
scalar/oriented split                                  PROVED
universal Rees bridge sum -> normal jet                PROVED
compatibility with tame localization                   PROVED
faithfulness on the physical antidiagonal              PROVED
cofinal descent after oriented vanishing               PROVED
first-contact equivariant lift before augmentation     OPEN (ORL)
global square and row (d)                              OPEN
```

The bridge is now a genuine constructed object. The remaining work is no
longer to manufacture a map from sum to difference; it is to lift the
first-contact equality from the augmented scalar character to the
orientation-equivariant character. No paper-42 change follows before ORL
is proved.
