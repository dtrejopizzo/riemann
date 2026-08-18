# 107.235 -- Direct divisor-sheaf to periodic-H0 comparison is impossible

## 1. The two published objects have different scalar size

The sheaf of arXiv:2602.15941v1 assigns to an arithmetic divisor
\(\mathcal D=(L,\|\cdot\|)\) the Gamma module

\[
 \mathcal O(\mathcal D)(U)=H\mathcal L(U)
 \tag{1.1}
\]

at finite opens, with an \(\ell^1\) unit-ball condition at infinity.  Every
\(L\) is a subgroup of \(\mathbb Q\), hence countable.  Evaluation on every
finite pointed set and every stalk or filtered colimit therefore remains a
countable set.

By contrast, the Scaling Site is explicitly obtained by extension of scalars
to \(\mathbb R_{\max}\).  On the periodic orbit

\[
 C_p=\mathbb R_+^*/p^{\mathbb Z},
\]

its rational functions are real-valued piecewise-affine functions, and
\(H^0(D)\) is an \(\mathbb R_{\max}\)-module.  For every positive-degree
divisor, the published RR theorem gives positive continuous dimension.  More
sharply, the extremal-generator theorem used in 107_232 gives a surjection

\[
 \mathbb R_{\max}^{d}\twoheadrightarrow H^0(N\{1\})^1,
 \qquad d=N-p+1>0,
 \tag{1.2}
\]

and its dominance cell embeds a nonempty open subset of \(\mathbb R^d\).
Thus this module has cardinality continuum and positive topological dimension.

## 2. Cardinality and dimension no-go

### Theorem 2.1

No restriction, pullback, tensor, sheafification, or filtered-colimit functor
formed in the unextended Gamma-module category from a finite family of the
modules \(\mathcal O(\mathcal D)\) of (1.1) can surject onto a positive-degree
periodic module \(H^0(D)^{p^n}\).  In particular there is no direct
isomorphism

\[
 \mathcal O(\mathcal D)|_{C_p}\simeq H^0(D)
 \tag{2.1}
\]

before extension of scalars.

### Proof

A finite product, quotient, tensor product, sheafification over a countable
basis, or filtered colimit over a countable category of countable sets is
countable.  The source of any proposed direct comparison is therefore
countable.  The target contains the real cell described above, so it is
uncountable.  No function from the former can be surjective onto the latter.

Independently, a countable metric source has covering dimension zero when it
is discrete in the Gamma-module topology used before scalar extension, while
the target contains an open \(d\)-cell.  Hence a dimension-preserving
comparison is impossible as well. \(\square\)

The theorem applies unchanged to the external tensor carrier of 107_234:
finite tensoring does not manufacture \(\mathbb R_{\max}\)-coefficients.

## 3. The unique surviving comparison architecture

The obstruction is not to 107_234 itself.  Its global arithmetic-divisor
module and monoidal descent remain valid.  What fails is the **direct** arrow
from that module to periodic tropical \(H^0\).

Any viable comparison must factor as

\[
 \mathcal O(\mathcal D)
 \longrightarrow
 \mathcal O(\mathcal D)\widehat\otimes_{\mathbb S[\pm1]}
 \mathbb R_{\max}
 \longrightarrow H^0(D),
 \tag{3.1}
\]

or pass through an analytic completion followed by tropicalization.  The
second route is not hypothetical vocabulary: arXiv:2606.06604v1 constructs
the absolute \(\mathbb F_1\)-curve with stalk
\(\mathbb F_1[T^{\mathbb Z[1/p]_+}]\) and a canonical tropicalization of
analytic valuation profiles into the Scaling-Site structure sheaf.

However, that paper explicitly leaves the descent of Frobenius eigenspaces to
\(C_p\) and their relation with the periodic geometry for future work.  It
therefore supplies the scalar/analytic bridge for structure functions, not
the divisor-module comparison required here.

## 4. Closed gate and next gate

\[
 \boxed{\texttt{DIRECT\_O(D)\_TO\_PERIODIC\_H0: CLOSED\_NO\_GO}.}
\]

The next gate is unique and constructive:

\[
 \boxed{
 \text{construct the base-changed divisor module and test whether its}
 \ C_p\text{-restriction equals the published periodic }H^0.}
 \tag{4.1}
\]

No new candidate surface, \(H^1\), or RR complex should be introduced before
this base-change comparison is resolved.  Row (a) remains `partial`.

## 5. Machine certificate

Run

```bash
/home/trabajo/miniforge3/bin/python \
  107_235_direct_divisor_sheaf_to_periodic_h0_no_go.py
```

The certificate reads all three real source files, checks the source and
target definitions, verifies that the 2026 tropical comparison stops at the
structure sheaf, and returns a binary verdict on the direct comparison.
