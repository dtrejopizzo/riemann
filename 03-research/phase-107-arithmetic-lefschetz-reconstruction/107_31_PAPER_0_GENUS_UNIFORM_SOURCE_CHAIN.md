# 107.31 -- Paper 0 supplement: genus-uniform source chain on \(C\times C\)

## 1. Purpose

`107_30` proves that the primitive Gram package on \(C\times C\) is
genus-uniform at the exact point where the factor \(g\) enters.

The present note pushes one step further: it isolates the rest of the
Paper 0 source chain that is already genus-uniform for an arbitrary
smooth projective curve \(C/\mathbf F_q\), independently of the fixed
elliptic control.

Its output is the following source-level chain on \(C\times C\):

\[
 \Gamma_{F^n}
 \longrightarrow
 \Gamma_{F^n}\cdot\Delta
 \longrightarrow
 Z_C(u)
 \longrightarrow
 q^{-kd/2}
 \longrightarrow
 G_n^0.
 \tag{1.1}
\]

What remains special to the elliptic paper after this note is the exact
numerical anchor \(E/\mathbf F_5\), not the geometry of the source
operations themselves.

## 2. Setup

Let \(C/\mathbf F_q\) be a smooth projective geometrically connected
curve of genus \(g\), and fix \(x_0\in C(\mathbf F_q)\).

Set

\[
 S:=C\times C,
 \qquad
 F_{\rm v}:=\{x_0\}\times C,
 \qquad
 F_{\rm h}:=C\times\{x_0\},
 \qquad
 \Delta:=\{(P,P):P\in C\}.
 \tag{2.1}
\]

For geometric Frobenius \(F\), define

\[
 \Gamma_n:=\Gamma_{F^n}=\{(P,F^n(P)):P\in C\}\subset S.
 \tag{2.2}
\]

Write

\[
 N_n:=\#C(\mathbf F_{q^n}),
 \qquad
 a_n:=q^n+1-N_n.
 \tag{2.3}
\]

## 3. Composition and transpose

### Proposition 3.1: graph composition is genus-uniform

For all \(m,n\ge0\),

\[
 \Gamma_m\circ\Gamma_n=\Gamma_{m+n}.
 \tag{3.1}
\]

Proof.  Exactly as in the fixed elliptic case, the composition is the
image of the fiber product
\(\Gamma_n\times_C\Gamma_m\), whose points are triples
\((P,F^n(P),F^{m+n}(P))\).  Hence the resulting correspondence is the
graph of \(F^{m+n}\).  No genus input is used.  \(\square\)

### Proposition 3.2: transpose is genus-uniform

The transpose \(\Gamma_n^t\) is the graph of the Verschiebung \(V^n\),
with

\[
 V^n\circ F^n=F^n\circ V^n=[q^n].
 \tag{3.2}
\]

Proof.  This is the dual-isogeny relation for Frobenius on the Jacobian
side, transferred to the graph correspondence.  The statement depends on
Frobenius duality, not on \(g=1\).  \(\square\)

Thus the correspondence package itself is already genus-uniform.

## 4. Lefschetz fixed-point intersections

### Proposition 4.1: diagonal trace is genus-uniform

For every \(n\ge1\),

\[
 \Gamma_n\cdot\Delta=N_n=\#C(\mathbf F_{q^n}).
 \tag{4.1}
\]

Proof.  The intersection
\(\Gamma_n\cap\Delta\) is the fixed-point scheme of \(F^n\), equivalently
the kernel of \(F^n-\mathrm{id}_C\) interpreted on the graph side.  The
fixed points are exactly the \(\mathbf F_{q^n}\)-rational points of
\(C\), so the degree is \(N_n\).  This is the usual Lefschetz fixed-point
count on the graph of Frobenius, and it does not depend on genus.
\(\square\)

### Proposition 4.2: graph-versus-graph cross-check is genus-uniform

For \(m>n\),

\[
 \Gamma_m\cdot\Gamma_n=q^nN_{m-n}.
 \tag{4.2}
\]

Proof.  Exactly as in `107_02`, a point lies in the intersection iff
\(F^m(P)=F^n(P)\), equivalently
\(F^n(F^{m-n}(P)-P)=0\).  The composite has separable part
\(F^{m-n}-\mathrm{id}\) of degree \(N_{m-n}\) and purely inseparable
part \(F^n\) of degree \(q^n\).  Hence the intersection degree is
\(q^nN_{m-n}\).  \(\square\)

This gives the genus-uniform Lefschetz side of the chain.

## 5. Connected Euler extraction

Let \(B_d\) be the number of closed points of \(C\) of degree \(d\).

### Proposition 5.1: connected point-count decomposition is genus-uniform

For every \(n\ge1\),

\[
 N_n=\sum_{d\mid n} dB_d,
 \qquad
 B_n=\frac1n\left(N_n-\sum_{\substack{d\mid n\\ d<n}} dB_d\right).
 \tag{5.1}
\]

Proof.  A closed point of degree \(d\) contributes exactly \(d\)
geometric points to \(C(\mathbf F_{q^n})\) iff \(d\mid n\).  M\"obius
inversion gives the second formula.  \(\square\)

### Proposition 5.2: connected Euler projector is genus-uniform

\[
 Z_C(u)=\exp\left(\sum_{n\ge1}\frac{N_n}{n}u^n\right)
      =\prod_{d\ge1}(1-u^d)^{-B_d}.
 \tag{5.2}
\]

Proof.  As in `107_02`,

\[
 \log\prod_{d\ge1}(1-u^d)^{-B_d}
 =\sum_{d\ge1}B_d\sum_{k\ge1}\frac{u^{kd}}{k}
 =\sum_{n\ge1}\frac1n\left(\sum_{d\mid n}dB_d\right)u^n
 =\sum_{n\ge1}\frac{N_n}{n}u^n.
 \tag{5.3}
\]

\(\square\)

So the connected Euler extraction is also source-uniform in genus.

## 6. Critical balancing from bidegree

### Proposition 6.1: bidegree balancing is genus-uniform

The graph \(\Gamma_{kd}\) has bidegree \((1,q^{kd})\), hence the
symmetric half-density normalization
\((ab)^{-1/2}\) sends it to

\[
 (1\cdot q^{kd})^{-1/2}=q^{-kd/2}.
 \tag{6.1}
\]

Proof.  The first projection of \(\Gamma_{kd}\) has degree \(1\) and the
second has degree \(q^{kd}\).  Applying the same balancing rule used in
`107_02` gives the stated weight.  No genus input appears. \(\square\)

Thus the critical exponent is source-forced for all \(g\), not just for
the elliptic control.

## 7. Primitive package and Gram determinant

The genus-uniform primitive package itself is supplied by `107_30`:

\[
 (\Delta^0)^2=-2g,
 \qquad
 (\Gamma_n^0)^2=-2g\,q^n,
 \qquad
 \Gamma_n^0\cdot\Delta^0=-a_n.
 \tag{7.1}
\]

Hence

\[
 G_n^0=
 \begin{pmatrix}
 -2g & -a_n\\
 -a_n & -2g\,q^n
 \end{pmatrix},
 \qquad
 \det G_n^0=4g^2q^n-a_n^2.
 \tag{7.2}
\]

### Corollary 7.1: Hodge-sign output is genus-uniform once the classical Hodge theorem is invoked

Applying the Hodge-index theorem on \(C\times C\) yields

\[
 |a_n|\le 2g\,q^{n/2}.
 \tag{7.3}
\]

Thus the whole source chain (1.1) is now genus-uniform at the theorem
level.

## 8. What remains special to the elliptic control

What the fixed elliptic paper still uniquely provides:

1. one exact arithmetic anchor with all quantities computed explicitly;
2. one concrete preflight verifier already run in the workspace;
3. one fixed positive control curve to which the stop rule of `107_00`
   is pinned.

What is no longer special to it after the present note plus `107_30`:

1. composition of Frobenius graphs;
2. transpose/Verschiebung correspondence;
3. Lefschetz fixed-point trace;
4. connected Euler extraction;
5. balancing by graph bidegree;
6. primitive Gram package.

## 9. Status consequence

Paper 0 now splits cleanly into two layers.

1. The exact fixed elliptic control remains the audited positive anchor.
2. The source geometric chain behind it is now proved genus-uniformly at
   the \(C\times C\) level, up to the use of the classical Hodge-index
   theorem on that surface.

What still remains open is not the genus dependence of the source chain.
It is only a single fully integrated rewrite of `107_02` in genus-free
language, together with any additional exact verifiers one may want for
other concrete curves.
