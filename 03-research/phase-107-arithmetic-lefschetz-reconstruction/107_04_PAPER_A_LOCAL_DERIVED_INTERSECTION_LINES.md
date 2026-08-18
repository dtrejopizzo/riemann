# 107.04 -- Paper A, Part II: local derived intersection lines

## 1. Purpose

This note executes Work Package I-B of 107.00.  Its goal is to replace
naive scalar intersection guesses by finite-place determinant lines whose
canonical sections recover the exact cyclotomic resultant support.

The scope is deliberately local and finite.  This paper does **not**
define the global diagonal number.  Its output is a line with section,
not yet a signed real scalar.  The missing diagonal metric is reserved
for Work Package I-C.

## 2. Input from previous steps

Two ingredients are already fixed:

1. `107_03` supplies the finite-support divisor module
   \(\mathrm{Div}_{\mathrm{EF}}\), together with connected prime
   returns \(Z_{p,k}\), the diagonal symbol \(\Delta\), the archimedean
   symbol \(Z_\infty\), and the transpose-compatible raw package.
2. `106.210` identifies the correct finite cyclotomic local support:
   distinct cyclotomic strata are measured by Apostol's resultant
   formula, while the diagonal has no finite scalar value in the same
   standalone theory.

The present note packages exactly that finite information into a
determinant-line formalism.

## 3. Cyclotomic finite models

For \(n\ge1\), write

\[
 A=\mathbf Z[x],
 \qquad
 B_n=A/(\Phi_n),
 \qquad
 Z_n=\mathrm{Spec}(B_n)=V(\Phi_n)\subset\mathrm{Spec}\,A.
 \tag{3.1}
\]

For two indices \(m,n\ge1\), the finite derived intersection object is

\[
 Z_m\cap^{\mathbf L} Z_n
 :=
 B_m\otimes_A^{\mathbf L}B_n.
 \tag{3.2}
\]

When \(m\neq n\), this derived tensor product is perfect of finite
support over \(\mathrm{Spec}\,\mathbf Z\).  When \(m=n\), it becomes
the excess self-intersection complex discussed in `106.210`.

The finite-place determinant line attached to a perfect complex \(C\) of
finite support is denoted

\[
 \det_{\mathbf Z}(C)
 :=\bigotimes_i \det_{\mathbf Z} H^i(C)^{(-1)^i}.
 \tag{3.3}
\]

## 4. Local line functor on distinct cyclotomic strata

### Definition 4.1: finite determinant line

For distinct indices \(m\neq n\), define the finite determinant line

\[
 \langle Z_m,Z_n\rangle_{\mathrm{fin}}
 :=\det_{\mathbf Z}\!\left(B_m\otimes_A^{\mathbf L}B_n\right).
 \tag{4.1}
\]

Its canonical section is the determinant of multiplication by the pair
\((\Phi_m,\Phi_n)\), equivalently the principal section induced by the
Koszul complex of the regular sequence \((\Phi_m,\Phi_n)\).

### Proposition 4.1: resultant norm

For \(m\neq n\), the norm of the canonical section of
\(\langle Z_m,Z_n\rangle_{\mathrm{fin}}\) is

\[
 \left\|s_{m,n}\right\|_{\mathrm{fin}}
 =\left|\mathrm{Res}(\Phi_m,\Phi_n)\right|.
 \tag{4.2}
\]

Proof.  For distinct principal divisors on the regular surface
\(\mathrm{Spec}\,\mathbf Z[x]\), the determinant of the Koszul
complex computing the derived intersection is the classical Deligne
pairing section.  Its norm is the resultant of the defining equations.
\(\square\)

Thus the local line remembers finite intersection multiplicity without
prematurely converting it into a global numerical pairing.

## 5. Apostol normalization and prime-power support

The cyclotomic support theorem required by 107.00 is the following
normalization of Apostol's formula.

### Proposition 5.1: normalized finite order

For \(m>n>1\),

\[
 \frac1{\varphi(n)}
 \log\left\|s_{m,n}\right\|_{\mathrm{fin}}
 =
 \frac1{\varphi(n)}
 \log\left|\mathrm{Res}(\Phi_m,\Phi_n)\right|
 =
 \begin{cases}
 \log p,&m/n=p^a,\\
 0,&\text{otherwise}.
 \end{cases}
 \tag{5.1}
\]

Proof.  The first equality is Proposition 4.1.  The second is Apostol's
cyclotomic resultant formula, already isolated in `106.210`.  \(\square\)

This is the precise finite-place support required for Phase 107:

1. mixed ratios have trivial finite order;
2. prime-power transitions contribute exactly \(\log p\);
3. no appeal to zeros or to a global sign is used.

## 6. Extension to the source divisor module

The connected symbols \(Z_{p,k}\in\mathrm{Div}_{\mathrm{EF}}\) of
`107_03` are source-level placeholders for primitive \(k\)-fold
prime-power returns.  Their finite local interaction is modeled by the
cyclotomic indices underlying the same prime tower.

### Definition 6.1: finite-place line on generators

For connected generators \(Z_{p,k}\) and \(Z_{q,\ell}\), define a finite
line \(\langle Z_{p,k},Z_{q,\ell}\rangle_{\mathrm{fin}}\) by choosing the
corresponding cyclotomic strata whose ratio encodes the transition from
\((q,\ell)\) to \((p,k)\), and requiring its canonical section to obey
the normalized order law

\[
 \mathrm{ord}_{\mathrm{fin}}
 \langle Z_{p,k},Z_{q,\ell}\rangle_{\mathrm{fin}}
 =
 \begin{cases}
 \log p,&p=q,\ k>\ell,\\
 0,&p\neq q.
 \end{cases}
 \tag{6.1}
\]

This definition records only the support rule that survives into the
future arithmetic surface.  It deliberately suppresses any attempt to
assign a finite diagonal scalar.

### Definition 6.2: bilinear extension away from the diagonal

Extend \(\langle\cdot,\cdot\rangle_{\mathrm{fin}}\) biadditively from
off-diagonal generator pairs in \(\mathrm{Div}_{\mathrm{EF}}\),
with

\[
 \langle F_{\mathrm v},-\rangle_{\mathrm{fin}}
 =\langle F_{\mathrm h},-\rangle_{\mathrm{fin}}
 =\langle Z_\infty,-\rangle_{\mathrm{fin}}
 =0
 \tag{6.2}
\]

at the purely finite stage.

The polar rulings and the archimedean fiber contribute later through the
global metrized pairing of I-C; no finite-place numerical content is
assigned to them here.

## 7. The diagonal remains an excess-intersection line

The key structural point of `106.210` must be carried forward exactly.

### Proposition 7.1: no finite scalar diagonal

For any \(n\ge1\),

\[
 \mathrm{Res}(\Phi_n,\Phi_n)=0,
 \tag{7.1}
\]

and

\[
 B_n\otimes_A^{\mathbf L}B_n
 \simeq [B_n\xrightarrow{0}B_n].
 \tag{7.2}
\]

Hence the self-intersection of \(Z_n\) at the finite cyclotomic level is
an excess-intersection object, not a finite scalar.

Proof.  This is exactly Sections 2 and 3 of `106.210`.  \(\square\)

### Corollary 7.2: diagonal placeholder

The source diagonal symbol \(\Delta\in\mathrm{Div}_{\mathrm{EF}}\)
must be sent at the finite stage to an excess-intersection line object
\(\mathcal E_\Delta\), not to a number \(n\), \(\varphi(n)\), or
\(\log|\mathrm{Disc}(\Phi_n)|\).

Proof.  Any of those scalar substitutes would import extra information
not furnished by the same finite determinant theory.  In particular, the
discriminant arises from \(\mathrm{Res}(\Phi_n,\Phi_n')\), which is
a normal-torsion invariant rather than a bilinear self-pairing.
\(\square\)

This is exactly stop test 2 of I-B.

## 8. Symmetry, base change and projection

The determinant-line package inherits the formal properties required by
107.00 on the off-diagonal sector.

### Proposition 8.1: symmetry

For \(m\neq n\),

\[
 \langle Z_m,Z_n\rangle_{\mathrm{fin}}
 \cong
 \langle Z_n,Z_m\rangle_{\mathrm{fin}}.
 \tag{8.1}
\]

Proof.  The derived tensor product
\(B_m\otimes_A^{\mathbf L}B_n\) is symmetric in \(m,n\), and the
resultant is symmetric up to the standard sign, which disappears after
absolute value in the norm.  \(\square\)

### Proposition 8.2: finite base change

The construction of \(\langle Z_m,Z_n\rangle_{\mathrm{fin}}\) commutes
with restriction to any finite set of primes containing the support of
\(\mathrm{Res}(\Phi_m,\Phi_n)\).

Proof.  Off the support of the resultant the intersection is empty, hence
the localized complex is acyclic.  Therefore the determinant line
localizes to the finite set of bad primes without changing the norm.
\(\square\)

### Proposition 8.3: projection formula

If a decorated correspondence pulls back cyclotomic strata by a genuine
derived fiber square, then the determinant line of the pullback
intersection is the pullback of the determinant line.

Proof.  Determinant of cohomology is functorial for perfect complexes and
compatible with derived base change.  This is exactly the abstract reason
for insisting in Phase 107 that composition squares be genuine derived
fiber products.  \(\square\)

## 9. Compatibility with transpose and composition

Work Package I-B must already fit the source algebra of `107_03`.

### Proposition 9.1: transpose compatibility

The finite determinant line is invariant under exchanging the two factors
of the decorated pair:

\[
 \langle \tau_{\mathrm{raw}}(C_1),\tau_{\mathrm{raw}}(C_2)\rangle_{\mathrm{fin}}
 \cong
 \langle C_1,C_2\rangle_{\mathrm{fin}}
 \tag{9.1}
\]

whenever both sides are defined off the diagonal.

Proof.  Transpose exchanges the two orientations but does not alter the
underlying finite cyclotomic support.  At the derived level this is just
the symmetry of the tensor product.  \(\square\)

### Proposition 9.2: composition compatibility

If \(C_{12}\) and \(C_{23}\) compose through a genuine derived fiber
product, then the local finite determinant line of the composite is the
determinant line of the corresponding iterated derived intersection.

Proof.  Derived fiber products compose associatively up to canonical
equivalence, and determinant of cohomology respects those equivalences.
The statement is structural: I-B does not yet compute the full composite
matrix, but it fixes the functorial rule that later computations must
obey.  \(\square\)

This is enough for I-B; the explicit composite category itself belongs to
Paper B.

## 10. Stop-test audit

Work Package I-B passes its three stop tests.

### Stop test 1

Mixed ratios have trivial local line and prime-power ratios have order
exactly \(\log p\).

Reason.  Proposition 5.1 is precisely the normalized Apostol formula.

### Stop test 2

The diagonal remains an excess-intersection line and is not filled by a
cardinality scalar.

Reason.  Proposition 7.1 and Corollary 7.2 preserve the diagonal as an
unresolved excess object.

### Stop test 3

The functor is compatible with transpose and composition on the
decorated category.

Reason.  Propositions 9.1 and 9.2 give the required structural
compatibility.

## 11. Status inside Paper A

Work Package I-B is now fixed at the finite-place level:

1. the correct off-diagonal support is the cyclotomic resultant;
2. the right object is a determinant line with canonical section;
3. the diagonal is postponed rather than fabricated.

What remains open is exactly what 107.00 predicted:

* the Gamma contribution;
* the pole and the polar rulings;
* the diagonal self-intersection as part of the same metrized line;
* the product-formula cancellation joining the finite and archimedean
  sectors.

Those belong to Work Package I-C and are the next step if Paper A is to
become a coherent arithmetic intersection theory rather than a collection
of local finite identities.

### A5 branch note

At the current Phase 107 state, the determinant-line package above is
still the legacy finite-place theory of Paper A.
The live `A5` branch now adds a first refined local object on top of it:

\[
G_{A5}(row)=\bigl(\mathcal S_{\mathrm{legacy}}(row),\rho_{32}(row)\bigr),
\]

with corresponding refined local line labels
\(\mathcal L_{A5}(row_1,row_2)\).
The exact real tests now show:

1. forgetting \(\rho_{32}\) recovers the same legacy local support
   class;
2. adjoining \(\rho_{32}\) splits a real family on which the legacy
   finite row is blind;
3. so the current A5 work should be read as a refinement **over** the
   local determinant-line viewpoint of `107_04`, not yet as a
   replacement theorem for it.
4. the first decorated determinant-line candidate of that branch is now
   the object
   \[
   \mathcal D_{A5}(row)=
   \bigl(\mathcal D_{\mathrm{legacy}}(row),\rho_{32}(row)\bigr),
   \]
   whose real-data verifier keeps the legacy scalar projection fixed
   while splitting the blind \(IV^\ast\) class.
5. the first compatibility law on that decoration is now the difference
   cocycle
   \[
   \delta_{32}(row_1,row_2)=
   \rho_{32}(row_1)-\rho_{32}(row_2)\pmod{32},
   \]
   whose real-data verifier satisfies transpose symmetry and a first
   cocycle law on sampled triples.
6. the same decoration now admits a first transport/composition reading:
   local arrows
   \[
   \mathsf A_{A5}(row_1,row_2)=\delta_{32}(row_1,row_2)
   \]
   compose additively on sampled real triples and reverse by additive
   inverse on sampled real pairs.
