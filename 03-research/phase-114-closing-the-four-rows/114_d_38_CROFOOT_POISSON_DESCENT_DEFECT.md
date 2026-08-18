# D.38 — Exact Crofoot--Poisson descent defect

## Status

This note audits the descent claim isolated in D.37(6.1).  It does not use
the zero set of zeta, the Weil sign, or RH.  The conclusion is negative for
the finite Crofoot complex structure written in D.37(5.1): that complex
structure does not preserve the Poisson relations under the canonical
Crofoot identification.  The standard Gamma block does not cancel the
defect.

This rules out that particular descent mechanism.  It is not a
counterexample to row D or to the Hodge inequality.

## 1. A general graph-descent lemma

Let `H_1,H_2` be Hilbert spaces, let

\[
 C:H_1\longrightarrow H_2
\]

be unitary, and put

\[
 \mathbb J_C(x,y)=(-C^*y,Cx).                         \tag{1.1}
\]

Thus `mathbb J_C^2=-1`; this is exactly the finite Crofoot complex
structure of D.37.  Let a closed relation in `H_1 direct-sum H_2` be the
graph of a bounded map `L:H_1 -> H_2`,

\[
 R_L=\{(x,Lx):x\in H_1\}.                            \tag{1.2}
\]

Define the quotient coordinate

\[
 q_L(a,b)=b-La.                                      \tag{1.3}
\]

Then the exact descent defect is

\[
 \boxed{
 \Delta_{C,L}:=q_L\mathbb J_C\iota_L
       =C+LC^*L,}\qquad \iota_Lx=(x,Lx).             \tag{1.4}
\]

Consequently

\[
 \mathbb J_C(R_L)\subseteq R_L
 \quad\Longleftrightarrow\quad
 C+LC^*L=0.                                         \tag{1.5}
\]

### Proof

Direct substitution gives

\[
 \mathbb J_C\iota_Lx=(-C^*Lx,Cx).
\]

Applying (1.3),

\[
 q_L\mathbb J_C\iota_Lx
 =Cx-L(-C^*Lx)
 =(C+LC^*L)x.
\]

The kernel of `q_L` is precisely `R_L`, proving (1.5).

The formula is algebraic and remains valid on a common invariant core for
closed unbounded relations.  No trace or positivity argument enters it.

## 2. Application to the Meyer Poisson relation

Meyer's doubled map is

\[
 \iota_+f=(Zf,JZ\mathcal Ff).                        \tag{2.1}
\]

For `f in mathcal H_cap`, additive Poisson summation gives the exact
equality

\[
 Zf=JZ\mathcal Ff.                                  \tag{2.2}
\]

Hence the Poisson range is diagonal in the doubled realization:

\[
 \iota_+(\mathcal H_\cap)
 =\{(g,g):g\in Z\mathcal H_\cap\}.                  \tag{2.3}
\]

The two finite model spaces in D.37 are different spaces.  Therefore a
finite compression of (2.3) first requires a comparison map
`L_P:K_(Z_P)->K_(B_P)`.  D.37 does not construct such a compression of
(2.1).  Thus D.37(6.1), as written, is not yet a typed consequence of the
Meyer double.

There is nevertheless a canonical best-case test: use the Crofoot unitary
itself as the comparison,

\[
 L_P=\mathcal C_P.                                  \tag{2.4}
\]

This transports the second factor back by `mathcal C_P^*` and makes the
relation literally diagonal.  Formula (1.4) then yields

\[
 \boxed{
 \Delta_{\mathcal C_P,\mathcal C_P}
 =\mathcal C_P+
   \mathcal C_P\mathcal C_P^*\mathcal C_P
 =2\mathcal C_P.}                                   \tag{2.5}
\]

It is nonzero whenever the model space is nonzero.  Equivalently,

\[
 \mathbb J_P(x,\mathcal C_Px)
 =(-x,\mathcal C_Px),                               \tag{2.6}
\]

whereas membership in the same graph would require the second component
to be `mathcal C_P(-x)=-mathcal C_Px`.

After identifying both factors with one Hilbert space, (2.6) is the
elementary statement

\[
 (x,x)\longmapsto(-x,x):                            \tag{2.7}
\]

the standard positive complex structure sends the diagonal to the
anti-diagonal.  Thus it cannot descend through the diagonal Poisson
relation.

### Explicit one-dimensional witness

Take `H_1=H_2=C`, `C=1`, and the nonzero relation vector `(1,1)`.  Then

\[
 \mathbb J_C(1,1)=(-1,1),\qquad
 q_I(-1,1)=2.                                       \tag{2.8}
\]

This is the complete local block algebra of (2.5), not a numerical
approximation.

## 3. The Gamma block cannot cancel the defect

Let `C_infty:H_infty^+ -> H_infty^-` denote the unitary identification of
the two Gamma oscillator orientations, and give the two-copy oscillator the
same standard complex structure

\[
 \mathbb J_\infty(u,v)=(-C_\infty^*v,C_\infty u).    \tag{3.1}
\]

Under the canonical Gamma pairing, its Poisson relation is the graph of
`C_infty`.  Hence the same calculation gives

\[
 \Delta_{C_\infty,C_\infty}=2C_\infty.              \tag{3.2}
\]

For the orthogonal Crofoot--Gamma assembly of D.37 the total operators are
block diagonal.  Therefore

\[
 \Delta_{\rm tot}
 =2\mathcal C_P\oplus2C_\infty.                     \tag{3.3}
\]

In particular,

\[
 \|\Delta_{\rm tot}(x,u)\|^2
 =4\|x\|^2+4\|u\|^2.                               \tag{3.4}
\]

No cancellation between finite and archimedean components is possible in
an orthogonal direct sum.  This remains true if a global relation forces
`u=A x`: the right side becomes

\[
 4\|x\|^2+4\|Ax\|^2,
\]

which is positive for every nonzero `x`.

Changing the oscillator orientation merely changes the sign of the second
block in (3.3); it still cannot cancel a vector in the first orthogonal
summand.  A cancellation would require an additional non-block-diagonal
gluing operator and a proof that its range identifies the two defects.
No such operator is part of D.32--D.37.

## 4. Two different quarter-phase modifications

Equation (1.5) shows that, while keeping the complex structure
`mathbb J_C`, the graph of

\[
 L=iC                                                   \tag{4.1}
\]

is invariant, because

\[
 C+(iC)C^*(iC)=0.                                    \tag{4.2}
\]

But the Meyer relation is the equality (2.2), with phase `+1`, not `i`.
Replacing it by (4.1) changes the Poisson relation and, on the real form,
changes the real subspace being quotiented.

There is a distinct modification which keeps the relation `L=C` and
replaces the unit in (1.1) by

\[
 D=iC,\qquad \mathbb J_D(x,y)=(-D^*y,Dx).            \tag{4.3}
\]

Then

\[
 D+CD^*C=0,                                          \tag{4.4}
\]

so this second quarter-phase does preserve the graph.  It induces scalar
multiplication by `-i` in the quotient coordinate:

\[
 q_C\mathbb J_D(a,b)=-i\,q_C(a,b).                  \tag{4.5}
\]

This repairs graph invariance only.  With the fixed Crofoot--Tate form of
D.37, `mathbb J_D` is anti-symplectic and does not yield a positive Hodge
metric.  The complete proof, together with the audit of the global Meyer
operator `Fourier J`, is given in D.39.

## 5. Verdict for D.37

The finite Crofoot polarization is a valid positive polarization before
Poisson descent.  It does **not** preserve the canonical Crofoot-aligned
Poisson relations, and the Gamma direct-sum block does not repair this.
Consequently it does not induce the claimed operator on

\[
 \mathcal H_-^0=\mathcal H_-/Z\mathcal H_\cap.
\]

More generally, any proposed finite boundary comparison `L_P` must satisfy
the explicit Riccati-type identity

\[
 \boxed{\mathcal C_P+L_P\mathcal C_P^*L_P=0}         \tag{5.1}
\]

on the compressed Poisson range.  In addition one must construct `L_P`
from (2.1), prove compatibility with the finite compression, Gamma gluing,
transition maps and scaling, and only then take the cokernel.  D.37 does
not supply these data.

Thus the D.37 descent route is falsified in its canonical form.  Row D
remains open; no statement about RH follows from this audit.
