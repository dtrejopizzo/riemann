# 107.241 -- Infinite Weil quotient and finite-target no-go

## 1. Decision

This note stops the finite-rank realization branch of rows (a) and (d).
It does not construct the missing arithmetic surface and it does not prove
RH.  Its conclusion is narrower and unconditional:

> A realization faithful modulo the polarized Weil radical cannot factor
> through any finite-dimensional real target.

In particular, a Neron--Severi group of finite rank, a finite-dimensional
Picard shadow, or a finite collection of Chern classes cannot be the full
target required by the equality-case gate of `107_00`.

## 2. Test space and radical

Let

\[
 \mathcal V=C_c^\infty(\mathbb R;\mathbb C)
\]

in additive logarithmic coordinates, and let \(B_W\) be the polarized
completed Weil form.  Write

\[
 \mathfrak R_W=\{f\in\mathcal V:B_W(f,g)=0
                 \text{ for every }g\in\mathcal V\}.
 \tag{2.1}
\]

The balanced source used by Phase 107 is

\[
 \mathcal V_0=\{f\in\mathcal V:
 \widehat f(i/2)=\widehat f(-i/2)=0\}.
 \tag{2.2}
\]

Thus \(\mathcal V_0\) has codimension at most two in \(\mathcal V\).
The same argument works over the real even core after pairing conjugate
frequencies.

## 3. Infinite-rank lemma

### Theorem 3.1

The bilinear map

\[
 T_W:\mathcal V\longrightarrow\mathcal V',\qquad
 T_W(f)=B_W(f,\mathord\cdot)
 \tag{3.1}
\]

has infinite algebraic rank.  Its restriction to \(\mathcal V_0\) also
has infinite rank.

### Proof

In logarithmic coordinates the polarized explicit formula is a convolution
form

\[
 B_W(f,g)=W(f*\widetilde g),
 \tag{3.2}
\]

where the Fourier--Laplace transform of the completed distribution \(W\)
contains the spectral divisor of the completed zeta function, with
multiplicity, together with the two polar terms.  This is the usual
distributional Weil explicit formula; it is also the spectral side of the
semilocal trace formula used in `107_239`.

Assume that (3.1) has finite rank.  Then the convolution operator generated
by \(W\) has finite rank.  Convolving with a compactly supported approximate
identity and using that a finite-dimensional subspace of distributions is
closed shows that \(W\), and hence every additive translate of \(W\), lies
in that finite-dimensional range.  Call their span \(E\).

For completeness, the finite-translate argument needed here is short.
The space \(E\) is translation invariant and finite-dimensional, hence it
is also invariant under the infinitesimal generator \(D=d/dx\) (difference
quotients converge distributionally and finite-dimensional subspaces are
closed).  By Cayley--Hamilton there is a nonzero polynomial \(p\) such that

\[
 p(D)W=0.
 \tag{3.3}
\]

After Fourier transformation, (3.3) becomes
\(p(i\xi)\widehat W=0\).  Therefore \(\widehat W\) is supported on the
finite zero set of \(p(i\xi)\); derivatives of point masses may occur, but
only at those finitely many frequencies.  This is precisely the
exponential-polynomial conclusion, proved here without an additional
classification theorem.

That conclusion contradicts the spectral side of the explicit formula.
Hardy's theorem supplies infinitely many distinct zeros
\(1/2+i\gamma\) of \(\zeta\), so the transform of \(W\) has infinitely
many distinct spectral points.  Therefore \(T_W\) has infinite rank.

Finally, if \(T_W|_{\mathcal V_0}\) had finite rank, adjoining a complement
of dimension at most two to \(\mathcal V_0\) would make \(T_W\) finite
rank on all of \(\mathcal V\), a contradiction.  This proves both claims.
\(\square\)

The proof uses only the existence of infinitely many critical-line zeros,
not RH and not positivity of the Weil form.

## 4. Exact quotient

### Corollary 4.1

The quotient

\[
 \mathcal V_0/(\mathfrak R_W\cap\mathcal V_0)
 \tag{4.1}
\]

is infinite-dimensional.

### Proof

For every bilinear form, the map induced by \(T_W\) identifies the quotient
by its left radical with \(\mathrm{im}\,T_W\).  Theorem 3.1 says that
this image has infinite dimension. \(\square\)

### Corollary 4.2 -- finite-target no-go

Let \(A:\mathcal V_0\to E\) be linear and suppose

\[
 \ker A=\mathfrak R_W\cap\mathcal V_0.
 \tag{4.2}
\]

Then \(E\) contains an infinite-dimensional linear subspace.  In
particular, (4.2) is impossible when \(E\) is finite-dimensional or is the
realification of a finitely generated abelian group.

This is immediate because (4.2) induces an injection of (4.1) into \(E\).

## 5. Design consequence

The conclusion sharpens the prediction in `107_00`, Section 20, into a
theorem.  The missing realization cannot be encoded by:

1. a finite-rank Neron--Severi lattice;
2. an additive first Chern class in such a lattice;
3. finitely many intersection coordinates;
4. any other finite-dimensional equivariant shadow with exact Weil kernel.

The surviving target must retain an infinite-dimensional Green,
distributional, or cohomological component.  Together with `107_224`, this
also explains why the Connes--Consani integer dimension is structurally
relevant: the real archimedean direction cannot be carried faithfully by a
finitely generated additive target.

This does **not** prove that every infinite-dimensional target works.  It
does not establish DC Picard descent, an intersection theory, \(H^1\), RR
on the square, or the Hodge sign.  It only removes the entire finite-target
branch before further candidates are built.

## 6. Certificate

`107_241_infinite_weil_quotient_no_go.py` reads actual critical zeros with
`mpmath` and checks that their translation characters have full
Vandermonde rank at every tested size.  The program may return `NO`; it is
a finite witness to the mechanism, not the proof of Theorem 3.1.

## 7. Status

```text
WEIL_FORM_RANK: INFINITE
BALANCED_WEIL_QUOTIENT: INFINITE_DIMENSIONAL
FINITE_RANK_EXACT_TARGET: CLOSED_NO_GO
CLASSICAL_NS_ONLY_BRANCH: CLOSED_NO_GO
ROW_A: PARTIAL
ROW_D: OPEN_IN_INFINITE_CATEGORY
VERDICT: YES
```
