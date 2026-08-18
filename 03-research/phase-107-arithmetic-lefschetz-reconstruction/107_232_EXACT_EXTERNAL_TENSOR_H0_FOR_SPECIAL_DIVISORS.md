# 107.232 -- Exact external-tensor H0 for special periodic divisors

## 1. The published generation theorem

For a prime \(p\) and integer \(N>p\), let

\[
 \mathcal E_{N,p}=H^0(N\{1\})^1.
\]

The appendix of Connes--Consani, *Geometry of the Scaling Site*, proves
that the functions

\[
 \phi_a(x)=max\left\{-a(x-1),
 \left\lfloor\frac{N-a}{p}\right\rfloor(x-p)\right\},
 \qquad 0\leq a\leq N-p,
 \tag{1.1}
\]

are exactly the extremal rays of \(\mathcal E_{N,p}\) and generate the
whole module. Equivalently, with \(d=N-p+1\), the map

\[
 \sigma_p:\mathbb R_{\max}^{d}\twoheadrightarrow\mathcal E_{N,p},
 \qquad
 (u_a)\longmapsto\max_a(\phi_a+u_a)
 \tag{1.2}
\]

is surjective. The same theorem for a prime \(q\), integer \(M>q\),
gives \(e=M-q+1\) extremal generators \(\psi_b\) of
\(\mathcal E_{M,q}\).

This is the missing input which 107_231 had not yet used: its dominance
frame is a frame of the complete one-ruling section module, not merely
an isolated submodule.

## 2. Intrinsic external tensor image

Define

\[
 \mathcal T_{N,M}^{p,q}
 =\left\{
 \max_{a,b}\bigl(\phi_a(x)+\psi_b(y)+c_{ab}\bigr):
 c_{ab}\in\mathbb R_{\max}
 \right\}.
 \tag{2.1}
\]

This is the image, in continuous max-plus functions on
\(C_p\times C_q\), of the algebraic external tensor product

\[
 \mathcal E_{N,p}\otimes_{\mathbb R_{\max}}\mathcal E_{M,q}.
 \tag{2.2}
\]

Indeed every pure external sum expands through (1.2) as

\[
 f(x)+g(y)
 =\max_{a,b}\bigl(\phi_a(x)+\psi_b(y)+u_a+v_b\bigr).
\]

Conversely, an arbitrary coefficient matrix \((c_{ab})\) is a maximum
of pure tropical rank-one matrices: isolate each entry \((a,b)\) by
taking all other coordinates equal to \(-\infty\). Thus finite maxima
of pure tensors give exactly (2.1).

Because (2.1) is defined as the intrinsic tensor image, it does not
depend on the chosen extremal enumeration or on the dominance points
used in 107_231.

## 3. Exact dimension theorem

### Theorem 3.1

With the uniform topology on \(C_p\times C_q\),

\[
 \mathrm{tdim}\,\mathcal T_{N,M}^{p,q}
 =(N-p+1)(M-q+1)=de.
 \tag{3.1}
\]

### Proof

The coefficient map

\[
 \Sigma:\mathbb R_{\max}^{de}\longrightarrow
 \mathcal T_{N,M}^{p,q}
 \tag{3.2}
\]

is surjective by definition. On every stratum where a fixed subset of
coefficients is finite, \(\Sigma\) is 1-Lipschitz from a Euclidean
space of dimension at most \(de\) to the uniform metric on continuous
functions: changing all coefficients by at most \(\epsilon\) changes
their finite maximum by at most \(\epsilon\). Exhaust each stratum by
compact cubes. A Lipschitz image of such a cube has Hausdorff dimension
at most \(de\), and its Lebesgue covering dimension is at most its
Hausdorff dimension. These compact images are closed in the metric
section module and form a countable cover. The countable closed-sum
theorem for covering dimension therefore gives

\[
 \mathrm{tdim}\,\mathcal T_{N,M}^{p,q}\leq de.
\]

For the reverse inequality, 107_231 constructs an open coefficient
cube on which \(\Sigma\) is a topological embedding, with every one of
the \(de\) coefficients recovered by evaluation on a strict dominance
rectangle. Hence the image contains a cell of dimension \(de\), so its
covering dimension is at least \(de\). \(\square\)

### Corollary 3.2

The lower-capacity construction of 107_231 is sharp: adding all
external tensors and closing under finite maximum introduces no hidden
higher-dimensional parameter channel.

## 4. Continuous two-ruling dimension

Let \(\alpha\in\mathbb Z[1/p]_{>0}\) and
\(\beta\in\mathbb Z[1/q]_{>0}\). For sufficiently large \(n,m\), use
Frobenius to put

\[
 N_n=\alpha p^n,
 \qquad M_m=\beta q^m.
\]

Define the special external continuous dimension by

\[
 \mathrm{cdim}^{(2)}
 \bigl(H^0(\alpha\{1\})\boxtimes H^0(\beta\{1\})\bigr)
 :=\lim_{n,m\to\infty}p^{-n}q^{-m}
 \mathrm{tdim}\,\mathcal T_{N_n,M_m}^{p,q}.
 \tag{4.1}
\]

The limit exists along every cofinal path and Theorem 3.1 gives

\[
 \mathrm{cdim}^{(2)}=\alpha\beta.
 \tag{4.2}
\]

Thus the external tensor has exactly the multiplicative dimension
needed for a mixed two-ruling coefficient. The Cartesian product no-go
of 107_230 is avoided by construction.

## 5. Finite-level functoriality

The construction is functorial for morphisms of the two factor modules.
In particular:

1. changing an extremal generating set does not change the intrinsic
   tensor image;
2. addition of a principal function in either factor translates every
   external section by its pullback and preserves dimension;
3. Frobenius in either ruling maps the corresponding tensor image to
   the transformed level;
4. restriction maps of one-variable section modules induce tensor
   restriction maps and the two rulings commute.

These statements give finite periodic descent. They do not yet prove
descent over the global prime atlas, whose cross-prime restriction
channel is absent from the published base sheaf by 107_161.

## 6. Scope

This closes \(H^0\) and its exact normalized dimension for **special
external divisors on a fixed periodic product**. It does not yet cover:

1. arbitrary divisors on either periodic orbit;
2. mixed divisors not linearly equivalent to an external sum;
3. cross-prime gluing into one global Scaling-Site square;
4. \(H^1\), Serre duality, RR, or intersection theory.

The next local gate is extension from special divisors to arbitrary
positive external divisors using the squeeze maps in the published
one-ruling RR proof. The next global gate remains an additional
cross-prime geometry, not another choice of tensor generators.

## 7. Exact verifier

107_232_exact_external_tensor_h0.py verifies on the fixed prime pairs
that all published extremal generators satisfy their divisor
inequality, arbitrary pure tensors expand to coefficient matrices,
arbitrary matrices decompose into isolated pure tensors, the exact
dimension formula has the required cofinal limit, and deleting one
mixed generator is detected.
