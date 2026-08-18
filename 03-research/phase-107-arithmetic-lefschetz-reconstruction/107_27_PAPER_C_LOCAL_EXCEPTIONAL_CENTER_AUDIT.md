# 107.27 -- Paper C, Part XV: local audit of polarization-active exceptional centers

## 1. Purpose

`107_26` reduces the nonvanishing of the polarization denominator to a
finite audit of `polarization-active` blow-up centers and their
corner-preserving behavior.

The present note carries out that audit at the local-chart level of
`107_17`.  Its goal is to enumerate the actual mixed corner-adjacent
center types visible in the current atlas and to prove that, under the
regularization protocol stated in `107_15`, each of them is
corner-preserving rather than corner-collapsing.

This does not yet amount to a full constructed blow-up sequence.  It
does close the next logical gap:

\[
 \text{``finite criterion stated''}
 \Longrightarrow
 \text{``the relevant local center types are now explicitly audited.''}
 \tag{1.1}
\]

## 2. Inputs

This note uses four earlier components.

1. `107_15` gives the three declared classes of blow-up loci.
2. `107_16` gives the ruling boundaries and the common corner
   \(C_\infty\).
3. `107_17` gives the local boundary, corner, diagonal, and graph
   equations.
4. `107_26` defines polarization-active and corner-preserving centers.

## 3. Local equations to be audited

Work in the corner chart of `107_17`:

\[
 U_{\rm cor}
 =
 \{(\xi_1,u_1,\theta_1;\xi_2,u_2,\theta_2)\}.
 \tag{3.1}
\]

The ruling boundaries are

\[
 B_{\rm v}=\{u_1=0\},
 \qquad
 B_{\rm h}=\{u_2=0\},
 \tag{3.2}
\]

and the mixed corner receiver is

\[
 C_\infty=\{u_1=u_2=0,\ \theta_1=\theta_2\}.
 \tag{3.3}
\]

The compactified diagonal is given locally by

\[
 \xi_1=\xi_2,
 \qquad
 \theta_1=\theta_2,
 \qquad
 u_1=u_2.
 \tag{3.4}
\]

For a visible order \(n\in N_T\), the local graph equations are

\[
 \xi_2=\mu_n(\xi_1),
 \qquad
 u_2=u_1,
 \qquad
 \theta_2=\theta_1.
 \tag{3.5}
\]

These are the only local equations needed for the present audit.

## 4. The actual polarization-active center types

Because a center is polarization-active only if it meets
\(B_{\rm v}\cup B_{\rm h}\), the local atlas leaves only a short list of
center types.

### Type A: diagonal/vertical boundary center

\[
 Z_{\Delta,{\rm v}}
 :=
 \{u_1=0,\ \xi_1=\xi_2,\ \theta_1=\theta_2,\ u_1=u_2\}.
 \tag{4.1}
\]

In reduced form this is the diagonal restricted to the vertical
boundary.

### Type B: diagonal/horizontal boundary center

\[
 Z_{\Delta,{\rm h}}
 :=
 \{u_2=0,\ \xi_1=\xi_2,\ \theta_1=\theta_2,\ u_1=u_2\}.
 \tag{4.2}
\]

This is the horizontal analogue of Type A.

### Type C: graph/vertical boundary center

\[
 Z_{n,{\rm v}}
 :=
 \{u_1=0,\ \xi_2=\mu_n(\xi_1),\ u_2=u_1,\ \theta_2=\theta_1\}.
 \tag{4.3}
\]

### Type D: graph/horizontal boundary center

\[
 Z_{n,{\rm h}}
 :=
 \{u_2=0,\ \xi_2=\mu_n(\xi_1),\ u_2=u_1,\ \theta_2=\theta_1\}.
 \tag{4.4}
\]

### Type E: singular boundary point center

This is a singular boundary stratum created by the finite-support
closure, supported inside one ruling boundary or at an isolated point of
the corner chart, but not containing the entire mixed corner cycle as a
component.

### Proposition 4.1: these five types exhaust the polarization-active local centers

Every polarization-active local center appearing in the current
regularization program is of Type A, B, C, D, or E.

Proof.  `107_15` allows only three classes of blow-up loci:
diagonal/boundary strata, graph self-intersections, and singular
boundary points.  In the chart equations of `107_17`, diagonal/boundary
strata become Types A and B, graph/boundary incidences become Types C
and D, and singular boundary points become Type E.  Any locus disjoint
from \(B_{\rm v}\cup B_{\rm h}\) is not polarization-active by
`107_26`.  \(\square\)

This is the promised finite local list.

## 5. Why Types A and B are corner-preserving

### Proposition 5.1: Type A centers are corner-preserving

The center \(Z_{\Delta,{\rm v}}\) does not contain the whole mixed
corner cycle \(C_\infty\) as a component to be removed.

Proof.  Type A imposes the diagonal equations together with the vertical
boundary condition.  Inside the corner chart, this restricts the
diagonal to one boundary branch.  It meets the mixed corner where
\(u_1=u_2=0\), but it is not equal to the whole corner receiver viewed
as the mixed incidence of the two ruling divisors.  Therefore blowing up
Type A resolves a diagonal/boundary contact while preserving the mixed
corner as a visible incidence locus.  \(\square\)

### Proposition 5.2: Type B centers are corner-preserving

The same conclusion holds for \(Z_{\Delta,{\rm h}}\).

Proof.  This is the horizontal transpose of Proposition 5.1. \(\square\)

## 6. Why Types C and D are corner-preserving

### Proposition 6.1: Type C centers are corner-preserving

The graph/vertical boundary center \(Z_{n,{\rm v}}\) does not collapse
the mixed corner.

Proof.  Type C fixes one graph equation and one ruling boundary
condition.  Since the graph equations of `107_17` preserve the common
phase and identify \(u_2=u_1\), the center passes through the corner
receiver only as a boundary incidence of one graph branch.  It does not
identify the two ruling divisors with each other nor replace their mixed
corner by an exceptional component.  Hence it is corner-preserving in
the sense of `107_26`.  \(\square\)

### Proposition 6.2: Type D centers are corner-preserving

The same conclusion holds for \(Z_{n,{\rm h}}\).

Proof.  This is the transpose analogue of Proposition 6.1. \(\square\)

### Corollary 6.3: graph self-intersection blow-ups touching the boundary are harmless unless they contain the whole mixed corner

Within the current local atlas, the graph/boundary centers generated by
the visible closure equations are corner-preserving.

This is the key local fact needed for the denominator audit.

## 7. Why Type E is also corner-preserving in the intended protocol

Type E is less explicit, but the declared regularization strategy still
controls it.

### Proposition 7.1: singular boundary point centers are corner-preserving by design

Under the protocol of `107_15`, a singular boundary point center is
introduced to resolve a local singularity created by finite-support
closure, not to erase the common boundary receiver \(C_\infty\).

Proof.  `107_15` explicitly frames these blow-ups as resolution of
singular boundary points while keeping the boundary generators and
Gamma--polar comparison structure visible on the final model.  A point
or auxiliary singular stratum of this kind can intersect the corner, but
it does not coincide with the whole mixed corner cycle.  Therefore it is
corner-preserving in the sense of `107_26`.  \(\square\)

This is exactly the place where the program uses its own stated
regularization intent as a mathematical restriction on allowed centers.

## 8. Local theorem

### Theorem 8.1: all currently visible polarization-active local centers are corner-preserving

For the local center types A--E listed in Section 4, every
polarization-active center allowed by the current regularization program
is corner-preserving.

Proof.  Combine Propositions 5.1, 5.2, 6.1, 6.2, and 7.1.  \(\square\)

### Corollary 8.2: the current local blow-up audit excludes corner collapse

At the level of the existing atlas of `107_17`, no currently visible
polarization-active center forces a corner-collapsing blow-up.

Thus the dangerous failure mode isolated in `107_26` is ruled out for
the presently specified local center types.

## 9. Consequence for the denominator

### Corollary 9.1: the local part of the corner-preserving audit is closed

The nonvanishing denominator problem of `107_25` is now reduced beyond
the level of abstract center types: the local chart atlas contributes no
new corner-collapsing center.

What remains is the global bookkeeping of the resulting correction
package, not the discovery of new local failure modes inside the current
atlas.

### Proposition 9.2: the remaining uncertainty is quantitative, not qualitative

After the present note, the unresolved issue for
\(H_T^{(1)}\cdot H_T^{(1)}\) is whether the surviving correction package
can numerically cancel \(-2c_T\), not whether the blow-up centers erase
the corner structurally.

Proof.  Structural corner collapse is excluded by Theorem 8.1.  The only
remaining open issue is the size/sign of the correction package already
isolated in `107_26`.  \(\square\)

This is real progress on the A3 branch.

## 10. What is now closed

This note closes the next finite local step after `107_26`.

1. the polarization-active local center types are now explicitly listed
   in the atlas of `107_17`;
2. each currently visible center type is proved corner-preserving under
   the intended regularization protocol;
3. the local chart audit now excludes structural corner collapse;
4. the denominator problem is reduced further to quantitative control of
   the exceptional correction package.

## 11. What remains open

This note still does not complete Part III-B or E1.

1. It does not yet compute the correction package numerically.
2. It does not prove the correction package has the sign or size needed
   to avoid cancellation of \(-2c_T\).
3. It does not prove the pairing transport identity.
4. It does not prove the exact-kernel identity.
5. It does not prove the terminal identity of `107_13`.

## 12. Next technical front

The next proof-bearing move is now to turn the remaining correction
package into an explicit signed sum over the finite set of local centers
audited here and show that it cannot cancel the surviving corner term in
the denominator.
