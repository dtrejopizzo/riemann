# Row (d): a Lorentzian Szego theorem for all prime-power towers

## Status

This note proves a genuine Hodge-index theorem on a newly constructed mixed
prime-power coefficient space.  It uses the torsor grading and the
archimedean oscillator, and it has no spectral or zero input.  The theorem
includes all powers `p^k` and has a strict equality statement.  What remains
is a comparison morphism from the mixed test classes of rows (b)--(c) to
this space which preserves their already fixed intersection form.

## 1. Arithmetic Szego vectors

Let `H^2` be the Hardy space of the unit disk with orthonormal basis
`1,z,z^2,...`.  For a prime power `n=p^k>=2`, set `x_n=1/n` and define the
normalized Szego vector

\[
 h_n(z)=\frac{\sqrt{1-x_n^2}}{1-x_nz}.               \tag{1}
\]

Then `||h_n||=1` and

\[
 \langle h_m,h_n\rangle
 =\frac{\sqrt{(1-x_m^2)(1-x_n^2)}}{1-x_mx_n}.        \tag{2}
\]

The vector (1) is the normalized form of the Cauchy incidence produced by
the oscillator modes.  The basis vector indexed by `p^k` is metrically
distinguished by the `k`-th graded piece of the torsor filtration.

For a finite set `S` of distinct prime powers let `E_S=R[S]` with its
orthonormal torsor basis and define

\[
 J_S:E_S\longrightarrow H^2,\qquad J_Se_n=h_n,       \tag{3}
\]

\[
 q_S(v,w)=\langle J_Sv,J_Sw\rangle-\langle v,w\rangle.
                                                                    \tag{4}
\]

The degree is the constant Hardy coefficient

\[
 d_S(v)=\left\langle J_Sv,1\right\rangle
 =\sum_{n\in S}v_n\sqrt{1-n^{-2}}.                   \tag{5}
\]

Every nonzero vector in the positive coordinate cone has strictly positive
degree.

## 2. The global contraction constant

Write

\[
 h_n=a_n1+r_n,qquad a_n=\sqrt{1-n^{-2}},qquad r_n\perp1.
\]

Then

\[
 \|r_n\|^2=1-a_n^2=n^{-2}.                           \tag{6}
\]

Let `R_S:E_S->H^2_0` send `e_n` to `r_n`.

### Lemma 2.1

There is an unconditional uniform bound

\[
 \|R_S\|^2\le\|R_S\|_{\rm HS}^2
 =\sum_{n\in S}n^{-2}
 <\sum_p\sum_{k\ge1}p^{-2k}
 <\frac{1627}{2640}<1.                               \tag{7}
\]

### Proof

The first two assertions are the operator-norm/HS-norm inequality and (6).
Moreover

\[
 \sum_p\sum_{k\ge1}p^{-2k}=\sum_p\frac1{p^2-1}.
\]

For a fully elementary bound, separate `p=2,3,5,7` and dominate the
remaining primes by all integers `n>=11`:

\[
 \sum_p\frac1{p^2-1}
 \le \frac13+\frac18+\frac1{24}+\frac1{48}
       +\sum_{n\ge11}\frac1{n^2-1}.
\]

The last sum telescopes because

\[
 \frac1{n^2-1}=\frac12\left(\frac1{n-1}-\frac1{n+1}\right),
\]

and equals `(1/2)(1/10+1/11)`.  The resulting rational upper bound is

\[
 \frac13+\frac18+\frac1{24}+\frac1{48}
 +\frac12\left(\frac1{10}+\frac1{11}\right)
 =\frac{1627}{2640}<0.617.
\]

This gives the rigorous constant below one used in the theorem.  A direct
prime summation gives approximately `0.551694`, but that numerical
improvement is not used.

## 3. Hodge index and equality

### Theorem 3.1

For every finite `S` with at least two prime powers, the form `q_S` has
signature

\[
 (1,|S|-1).                                           \tag{8}
\]

More intrinsically,

\[
 q_S(v,v)<0
 \quad\text{for every nonzero }v\in\ker d_S.          \tag{9}
\]

Thus equality in the primitive Hodge inequality occurs only for `v=0`.

### Proof

The orthogonal decomposition `H^2=C1 direct-sum H^2_0` gives

\[
 \|J_Sv\|^2=|d_S(v)|^2+\|R_Sv\|^2.                  \tag{10}
\]

If `d_S(v)=0`, Lemma 2.1 gives

\[
 q_S(v,v)=\|R_Sv\|^2-\|v\|^2
 \le-(1-\|R_S\|^2)\|v\|^2<0.                       \tag{11}
\]

For the full inertia, write the matrix of (4) as

\[
 Q=aa^t-H,\qquad H=I-R_S^*R_S>0.                    \tag{12}
\]

On the codimension-one hyperplane
`{v:<Hv,H^{-1}a>=a^tv=0}`, the form is `-<Hv,v>`, so `Q` has at least
`|S|-1` strictly negative directions and at most one nonnegative
direction.  Its diagonal is zero because every `h_n` is normalized, hence
`tr Q=0`; and it is not the zero matrix because every off-diagonal entry in
(2) is positive.  Therefore the remaining eigenvalue is strictly positive.
There is no zero eigenvalue, and the signature is (8).  This also proves
(9) and its equality statement.

For `|S|=1`, the form is identically zero; the surface signature begins
when two mixed labels are present.

## 4. Compatibility under finite-support inclusions

If `S` is contained in `S'`, the maps (3), the torsor metric, the degree
and the form restrict exactly.  Therefore the finite spaces form a directed
system with a uniform primitive gap at least

\[
 1-\sum_p\frac1{p^2-1}>0.                            \tag{13}
\]

Only the tail operator extends boundedly to `ell^2({p^k})`.  The degree
functional is not represented by an `ell^2` vector because its coefficients
tend to one, so the rank-one term `|d(v)|^2` and the full form do **not**
extend to all of `ell^2`.  They are well defined on, for example,
`ell^1 intersect ell^2`, or on a weighted nuclear test space.  On the kernel
of `d` inside that domain the strict estimate is uniform.  Every
finite-support mixed class belongs to the domain.

## 5. Exact comparison obligation

Theorem 3.1 is an independent Hodge theorem, but it is not yet row (d).
To close row (d) one must construct, without using the sign of
`B_nuc`, a map

\[
 \mathcal J_{\rm mix}:\mathcal T\longrightarrow
 \varinjlim_SE_S                                      \tag{14}
\]

or an appropriate vector-valued enlargement, such that

\[
 d(\mathcal J_{\rm mix}f)
 \quad\text{is the pair of ruling degrees},           \tag{15}
\]

and

\[
 q(\mathcal J_{\rm mix}f,\mathcal J_{\rm mix}g)
 =B_{\rm nuc}(f,g).                                   \tag{16}
\]

The scalar degree in (5) supplies only one boundary coordinate; the second
must come from the Tate-conjugate copy.  The natural doubled target is
therefore the self-dual pair of Hardy modules at `n^{-1}` and its Tate
orientation.

Equation (16) is a theorem to be proved, not a definition of the image
metric.  The local data available for its construction are:

* the prime-power displacement `k log p` from the torsor;
* the contact mass `log p` from the derived complex;
* the oscillator vectors (1) from the Gamma boundary;
* Tate conjugation from row (b).

The next step is to build the doubled map on the dense algebraic
correspondence span and compare its kernel, term by term, with the finite
and archimedean character of row (c).
