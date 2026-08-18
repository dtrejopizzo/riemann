# 107.239 -- The renormalized corner trace realizes the Weil pairing

## 1. Geometric input, fixed before the value

Let \(S\) be a finite set of places containing \(\infty\), let

\[
 X_S=\mathbb Z_S^\times\backslash\mathbb A_S,
 \qquad
 \mathcal H_S=L^2(X_S),
 \tag{1.1}
\]

and let \(\theta\) be the scaling representation of the semilocal idele class
group:

\[
 (\theta(u)\xi)(a)=\xi(u^{-1}a).
 \tag{1.2}
\]

These are geometric data of the adelic covering, not data extracted from the
zeros.  Let \(P_\Lambda\) be the position cutoff and
\(\widehat P_\Lambda\) its Fourier conjugate.  Put

\[
 R_\Lambda=\widehat P_\Lambda P_\Lambda.
 \tag{1.3}
\]

For a compactly supported test \(h\), define the finite-part trace

\[
 \mathfrak T_S(h)=
 \lim_{\Lambda\to\infty}
 \left(
 \mathrm{Tr}_{\mathcal H_S}(\theta(h)R_\Lambda)
 -2h(1)\log\Lambda
 \right).
 \tag{1.4}
\]

The subtracted term is fixed by the regular representation.  In the 2026
Picard interpretation it is the contribution of the generic point.  Formula
(1.4) therefore defines a relative trace for the pair consisting of the
rooted arithmetic Picard monoid and its generic orbit.  It does not mention
the explicit-formula distribution \(N\).

## 2. Published semilocal trace theorem

The semilocal trace formula quoted and geometrically interpreted in
arXiv:2602.15941v1 proves

\[
 \boxed{
 \mathfrak T_S(h)=
 \sum_{v\in S}\int_{\mathbb Q_v^\times}'
 \frac{h(u^{-1})}{|1-u|_v}\,d^*u.}
 \tag{2.1}
\]

The prime denotes Tate's fixed local normalization.  The same paper identifies
the local term intrinsically: \(\mathbb Q_v^\times\) is the isotropy group of
the closed fiber, its transverse space is \(\mathbb Q_v\), and the kernel
trace on the diagonal is

\[
 \int_{\mathbb Q_v}\delta((u-1)x)\,dx=|1-u|_v^{-1}.
 \tag{2.2}
\]

Thus (2.1) is a fixed-point/corner trace theorem.  It is not a declaration
that intersection means the right-hand side.

## 3. Stabilization in the set of places

Embed a compactly supported test on \(\mathbb R_+^*\) into the idele class
group through the module, \(h(u)=h(|u|)\).  If
\(\mathrm{supp}\,h\subset[e^{-T},e^T]\), a finite prime can contribute
only if

\[
 p^k\leq e^T
 \tag{3.1}
\]

for some positive integer \(k\).  Hence all contributing primes satisfy
\(p\leq e^T\).  Once

\[
 S\supset S(h):=\{\infty\}\cup\{p:p\leq e^T\},
 \tag{3.2}
\]

the finite remainder stabilizes.  Define

\[
 \mathfrak T(h):=\mathfrak T_{S(h)}(h).
 \tag{3.3}
\]

Enlarging \(S\) further adds zero local terms.  This is the same finite-place
support mechanism that makes the prime sum in the explicit formula finite
for compact support.

## 4. From correspondence composition to convolution

The scaling representation satisfies

\[
 \theta(f)\theta(g)=\theta(f\star g),
 \qquad
 \theta(f)^*=\theta(\widetilde f),
 \tag{4.1}
\]

with the involution and modular normalization fixed in Phase 107.  Under the
Frobenius-ray realization of 107_237 this is exactly

\[
 D_f\star\widetilde D_g\longmapsto
 \theta(f\star\widetilde g).
 \tag{4.2}
\]

### Definition 4.1 (numerical corner pairing)

For the DC correspondence currents with their adelic representation, set

\[
 \boxed{
 I_\partial(D_f,D_g):=
 \mathfrak T(f\star\widetilde g).}
 \tag{4.3}
\]

This definition uses only composition, the geometric representation, the
phase-space cutoff, and removal of the generic regular orbit. At this stage it
is a numerical pairing on represented correspondences; descent to a pairing
on DC Cartier/Picard classes is not asserted.

### Theorem 4.2

With Tate's local normalization,

\[
 \boxed{
 I_\partial(D_f,D_g)
 =N(f\star\widetilde g)
 =\langle D_f\star\widetilde D_g,\Delta\rangle.}
 \tag{4.4}
\]

### Proof

Apply (2.1) to \(h=f\star\widetilde g\), enlarge \(S\) to the canonical
finite set (3.2), and use stabilization.  The sum of Tate-normalized local
terms is Weil's explicit-formula distribution by the published global
identity.  Compatibility (4.2) identifies the operator product with the
composed correspondence. \(\square\)

The local interior contribution proved zero in 107_238.  Formula (4.4)
therefore identifies the entire nonzero intersection with the renormalized
corner trace, exactly as forced there.

## 5. Non-circularity and scope

The construction would be circular if (4.3) were defined as \(N\).  It is
not: (1.4) is defined before (2.1), from a representation and two geometric
cutoffs.  Equality with \(N\) is the semilocal trace theorem plus Tate's
global explicit formula.

The resulting status is

\[
 \boxed{\texttt{DC\_CORNER\_PAIRING: CONSTRUCTED}},
 \qquad
 \boxed{\texttt{PAIRING\_VALUE: WEIL\_N}}.
\]

This supplies a new adelic-trace channel beyond the finite
prime/Euler/valuative package closed by the earlier row-(c) no-go.  It does
not retract that no-go and does not promote its papers: the new channel uses
the full semilocal Schwartz algebra, Fourier cutoff, and rooted Picard
isotropy.

Still open:

- prove that \(I_\partial\) is the intersection product entering a RR theorem
  for the DC completion, rather than only a numerical correspondence pairing;
- construct the nonprincipal line-bundle/descent class whose local equations
  are the potentials of 107_237, and prove principal invariance;
- construct \(H^1\) or an existence theorem for positive self-intersection;
- prove a Hodge-index/effectivity statement in this category.

Thus row (a) remains `partial`.  The numerical identity required from row (c)
is realized on the DC correspondence image through a genuinely new source
channel, but no paper status changes automatically.

## 6. Machine certificate

Run

```bash
/home/trabajo/miniforge3/bin/python \
  107_239_renormalized_corner_trace_pairing.py
```

The certificate reads the operator, cutoff, semilocal asymptotic, isotropy
and global explicit-formula statements from the real 2026 source.  It then
checks convolution/composition exactly on five finite multiplicative
quotients, verifies support stabilization for five compact windows, and
tests the local fixed-point Jacobian at real and p-adic places.
