# 114.a.42 — I7 no-go: the standard reduced fixed cone has determinant one

```
+--------------------------------------------------------------------------+
| REDUCE      Remove the horizontal line Z phi_1 from W_{p^a}.             |
| OPERATOR    The induced F_p is nilpotent on the reduced free module.      |
| CONE        1-F_p is integrally invertible with determinant one.          |
| NO-GO       Its standard derived fixed-point determinant has degree 0,   |
|             not log p.                                                    |
| CORRECT MASS The factor p is Norm(1-zeta_{p^k}), the cyclotomic lambda   |
|             determinant already seen in a_36.                            |
| GATE        Realize this cyclotomic determinant as the geometric excess  |
|             normal complex (H7-WLEF-cyc).                                |
+--------------------------------------------------------------------------+
```

## 1. Removing the horizontal component

Use the notation of `a_41`:

\[
 A_a=\bigoplus_{j=0}^{a}\mathbb Z e_j,
 \qquad e_j=\phi_{p^j}.                                 \tag{1.1}
\]

The line `Z e_0` is stable under `F_p`. Put

\[
 \overline A_a=A_a/\mathbb Z e_0.                      \tag{1.2}
\]

Equation (12.20) induces

\[
 \overline F_p(\bar e_1)=0,
 \qquad
 \overline F_p(\bar e_j)=p\bar e_{j-1}\quad(j\ge2).  \tag{1.3}
\]

Thus `bar F_p^a=0`.

## 2. Standard derived-cone no-go

### Theorem 2.1

The endomorphism

\[
 1-\overline F_p:\overline A_a\longrightarrow\overline A_a              \tag{2.1}
\]

is an integral automorphism and

\[
 \det(1-\overline F_p)=1.                              \tag{2.2}
\]

### Proof

Nilpotence gives the integral inverse

\[
 (1-\overline F_p)^{-1}
 =1+\overline F_p+\cdots+\overline F_p^{a-1}.          \tag{2.3}
\]

In the ordered basis `(bar e_1,...,bar e_a)`, (2.1) is triangular with all
diagonal entries equal to `1`, proving (2.2). QED.

### Corollary 2.2

The two-term standard reduced fixed complex

\[
 [\overline A_a\xrightarrow{,1-\overline F_p,}\overline A_a]           \tag{2.4}
\]

is acyclic over `Z`, has trivial determinant line and arithmetic degree
zero. It cannot recover `Lambda(p)=log p`.

This remains true with any metric placed on the same source and target
lattice compatibly: the algebraic determinant is a unit. A nonzero mass
must come from a different normal object, not from renormalizing the length
of (2.4).

## 3. The cyclotomic determinant that has the right mass

Let `zeta_n` be a primitive `n`-th root of unity. The norm identity is

\[
 \left|N_{\mathbb Q(\zeta_n)/\mathbb Q}(1-\zeta_n)\right|
 =|\Phi_n(1)|
 =\begin{cases}
 p,&n=p^k,\\
 1,&n>1\text{ not a prime power}.
 \end{cases}                                           \tag{3.1}
\]

Hence

\[
 \log\left|N(1-\zeta_n)\right|=\Lambda(n).             \tag{3.2}
\]

This is exactly Haran's lambda-trace formula used in `a_36`:

\[
 \mathrm{tr}(\lambda_1(\phi_n))
 =\prod_{\zeta\in\mu_n^*}(1-\zeta)=\Phi_n(1).          \tag{3.3}
\]

The desired mass therefore lives in the primitive cyclotomic conormal
factor `1-[zeta]`, not in `1-F_p` on the reduced Witt lattice.

## 4. Refined surviving gate

H7-WLEF-red is sharpened to:

> **H7-WLEF-cyc.** Construct, after a non-total H7-WBASE transport, an
> excess normal/perfect complex `N_n` for the graph and diagonal whose
> determinant is canonically identified with
> \[
> \det N_n\simeq
> \bigotimes_{\zeta\in\mu_n^*}(1-\zeta),               \tag{4.1}
> \]
> and prove that its Arakelov norm/degree is (3.2), compatibly with
> correspondence composition.

Theorem 2.1 rules out taking `N_p` to be the standard cone of
`1-bar F_p`. Formula (4.1) specifies the replacement and fixes its required
determinant, but no such geometric perfect complex on Haran's square has yet
been constructed.

## 5. Verification scope

`114_a_42_i7_standard_cone_nogo_verify.py` checks nilpotence, integral
inverses, determinant one and the cyclotomic norm identity on broad finite
ranges. It does not assert H7-WLEF-cyc.
