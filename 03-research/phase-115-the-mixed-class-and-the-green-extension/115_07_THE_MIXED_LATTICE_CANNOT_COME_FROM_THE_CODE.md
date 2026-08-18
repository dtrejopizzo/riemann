# 115.07 — The mixed lattice cannot come from the code, and where its covolume must come from instead

## Verdict

The extension to the mixed classes reduces, by Poisson, to **one scalar
condition**: produce a lattice \(\mathcal V_t(f)\) with

\[
 -\log\mathrm{covol}\,\bigl(\mathcal V_t(f)\bigr)
 =\tfrac{t^2}{2}B_{\rm nuc}(f,f)+O(t).
\tag{$\ast$}
\]

Everything else — \(h^0,h^1,h^2\), all four axioms — follows by the mechanism
already proved in `115_04`–`115_06`.

Two results here, one negative and one positive, and the negative one is the
more useful:

1. **The row-(a) code construction cannot produce \((\ast)\).**  Its covolume
   is controlled by the two degrees, and both degrees vanish on
   \(\mathcal T^0\).  Extending the code is not merely unfinished — it is the
   wrong mechanism.
2. **The finite part of \(B_{\rm nuc}\) already has a lattice realization**, in
   rows (a) and (b), as tensor powers of explicit torsion determinant lines.
   That is where the covolume must come from instead.

## 1. The obstruction: degrees vanish on \(\mathcal T^0\)

In row (a) the covolume is
\(-\log\mathrm{covol}=(\log2)^2N_t\) with \(N_t=r(m_t)r(n_t)\), and by
`lem:negabinaryradius`

\[
 r(m_t)=\frac{t\,d_1(D)}{\log2}+O(1),
 \qquad
 r(n_t)=\frac{t\,d_2(E)}{\log2}+O(1).
\]

So the covolume is quadratic **because the rank is a product of two quantities
each linear in a degree**, and this is exactly why
\(B_{\rm int}(D,D)=2d_1d_2\) comes out.

Now take a mixed class \(D_f\) with \(f\in\mathcal T^0\).  By
`eq:requiredprimitiveclass` its ruling coordinates are
\(\bigl(\widehat f(1),\widehat f(0)\bigr)\), and \(\mathcal T^0\) is defined by
\(\widehat f(0)=\widehat f(1)=0\).  Both degrees are zero.  Hence the code
mechanism gives \(N_t=0\), covolume \(1\), and

\[
 -\log\mathrm{covol}=0\neq\tfrac{t^2}{2}B_{\rm nuc}(f,f).
\]

The right-hand side is not zero: by `eq:rowcspectral`, for \(f\in\mathcal T^0\)
one has \(\widehat h(0)=\widehat h(1)=0\), so \(B_{\rm nuc}(f,f)\) reduces to
the zero sum and is generically nonzero.

> **Conclusion.**  The mixed lattice cannot be obtained by extending the
> negabinary code to the mixed classes.  Its covolume must come from a source
> that survives on the degree-zero space.

This is the same fact `115_01` recorded on the form side — row (a) gives
\(B_{\rm int}\equiv0\) on the codimension-two space while row (d) needs
\(\le0\) — now seen at the level of the lattice, where it says something
sharper: not "the deformation must open the radical downwards" but "the
construction must not be a deformation of the code at all".

## 2. What does survive: the contact indices

Every metric exponent in rows (a) and (b) is a **lattice index**, and the
paper says so explicitly.

`eq:contactmass` and the surrounding text: with the standard torsion metric
the determinant generator of \([\Z\xrightarrow{p}\Z]\) has norm \(p^{-1}\),
*"indeed the image lattice has index \(p\) in the target lattice"*, so

\[
 \kappa_p:=\det\nolimits_{\rm tor}C_p,
 \qquad
 -\log\|\kappa_p\|=\log p .
\]

Row (b) `eq:contactdegreeagain`:
\(-\log\|\det_{\rm tor}\mathbb L_n\|=\log\Phi_n(1)=\Lambda(n)\).

Row (a)'s real metric power \(L^{\langle c\rangle}\) (norm \(\|1\|^{c}\)) and
row (b)'s self-dual normalization \(w_{1/2}(\Gamma_n)=n^{-1/2}\)
(`eq:centralLocalCoefficient`) then give

\[
 \boxed{\;
 -\log\bigl\|\mathbb L_n^{\langle n^{-1/2}\rangle}\bigr\|
 =\frac{\Lambda(n)}{\sqrt n}\;}
\]

which is exactly the weight appearing in the finite part \(K\) of
`thm:forcedgreen`, and in `eq:localizedprimitiveoperator`.  The assembly rule
is already in the paper too: `eq:Clambda` builds \(\lambda_C\) by *"tensoring
the appropriate powers of the determinant lines \(\kappa_p\)"*.

So the finite half of \((\ast)\) needs no new construction.  It needs the
correct **cross** assembly — `115_01` §3, not the self form of
`eq:finitecandidate`.

## 3. Where the archimedean half has to live

Not in the lattice.  In a theta invariant the places divide as

```text
finite places      ->  the lattice   (indices)
archimedean place  ->  the metric    (the Gaussian e^{-pi |x|^2})
```

which is the Arakelov division: finite contributions to \(\widehat\deg\) are
indices, the archimedean one is \(-\log\|s\|_\infty\), a norm.  Row (a)
already works this way — \(\sigma\) is a metric scale, not an index.

Quantitatively, deforming the metric by a positive operator \(M\), i.e.
\(\|x\|_M^2=\langle Mx,x\rangle\), multiplies the covolume by
\((\det M)^{1/2}\), so

\[
 -\log\mathrm{covol}_M
 =-\log\mathrm{covol}-\tfrac12\log\det M .
\]

The requirement is therefore explicit:

> **Archimedean requirement.**  Find a positive \(M_t(f)\) on the contact
> lattice with
> \[
>  -\tfrac12\log\det M_t(f)=\tfrac{t^2}{2}\,G_\infty(f,f)+O(t).
> \]

## 4. The obstacle inside that requirement

The natural candidate \(M=e^{-c\mathcal G_\infty}\), with \(\mathcal G_\infty\)
the multiplier operator of \(m_\infty\), gives
\(\log\det M=-c\mathrm{tr}\,\mathcal G_\infty\).  But
\(m_\infty(\tau)=\log(2\pi/|\tau|)+O(\tau^{-2})\to-\infty\), so the trace over
a window diverges logarithmically and the determinant is not defined without
regularization.

This is not a new difficulty: it is the same one `eq:greenline` sidesteps.
The Green line \(\lambda_G\) is **defined as a quotient**,
\(\lambda_G:=\delta\lambda_{\rm int}\otimes\lambda_C^{-1}\), and the paper is
explicit that this is *"a canonical factorization of the intrinsic section
determinant, not an independent construction of a Green current by a second
geometric process"*.  So the archimedean line has never been constructed
directly in this programme; it has only ever been the residue of a division.

The mixed extension is the point at which that debt comes due.

## 5. Status

* Reduction of the mixed extension to the single scalar \((\ast)\):
  **PROVED** (Poisson, as in `115_04`).
* The code construction cannot supply \((\ast)\), because both degrees vanish
  on \(\mathcal T^0\): **PROVED** (§1).
* The finite half of \((\ast)\) is realized by
  \(\mathbb L_n^{\langle n^{-1/2}\rangle}\), assembled as in `eq:Clambda`:
  **AVAILABLE**, no new construction needed; the assembly must be **cross**,
  not self.
* The archimedean half must be a metric, and the requirement is
  \(-\tfrac12\log\det M_t(f)=\tfrac{t^2}{2}G_\infty(f,f)+O(t)\): **STATED**.
* Regularizing \(\det M\) against \(m_\infty\to-\infty\): **OPEN**, and it is
  the same debt that `eq:greenline` defers by defining \(\lambda_G\) as a
  quotient.
* Row D: **OPEN**.

## 6. Next

The frontier is now one object: **a direct construction of the archimedean
line \(\lambda_G\)**, as a metric on the contact lattice rather than as a
determinant quotient.  Two things make this a smaller problem than it was an
hour ago — the finite half is already built, and the target is a
\(\log\det\), not an inequality.

Note also what this closes off: no amount of work on the code, the periodic
cohomology, or the effective cone will produce the mixed lattice, because
those are all controlled by the degrees.  §1 is a no-go for that whole
direction.
