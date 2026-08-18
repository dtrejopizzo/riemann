# 107.32 -- Paper 0 integrated supplement: genus-free source calibration on \(C\times C\)

## 1. Purpose

The Paper 0 situation after `107_30` and `107_31` is mathematically much
better, but still documentarily split:

1. `107_02` gives one fully written fixed elliptic control;
2. `107_30` gives the genus-uniform primitive Gram package;
3. `107_31` gives the genus-uniform source chain outside that primitive
   package.

The present note integrates those two source-uniform supplements into
one single genus-free calibration statement on \(C\times C\).  Its role
is not to replace the exact anchor \(E/\mathbf F_5\), but to eliminate
the remaining ambiguity about what is already proved source-uniformly.

## 2. Setup

Let \(C/\mathbf F_q\) be a smooth projective geometrically connected
curve of genus \(g\), with chosen rational point \(x_0\in C(\mathbf F_q)\).

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

For geometric Frobenius \(F\), let

\[
 \Gamma_n:=\Gamma_{F^n}=\{(P,F^n(P)):P\in C\}.
 \tag{2.2}
\]

Write

\[
 N_n:=\#C(\mathbf F_{q^n}),
 \qquad
 a_n:=q^n+1-N_n.
 \tag{2.3}
\]

## 3. Source correspondence package

### Theorem 3.1: genus-free graph package

For all \(m,n\ge0\),

\[
 \Gamma_m\circ\Gamma_n=\Gamma_{m+n},
 \qquad
 \Gamma_n^t=\Gamma_{V^n},
 \qquad
 V^n\circ F^n=F^n\circ V^n=[q^n].
 \tag{3.1}
\]

Also,

\[
 \Gamma_n\cdot F_{\rm v}=1,
 \qquad
 \Gamma_n\cdot F_{\rm h}=q^n.
 \tag{3.2}
\]

Proof.  This is the combined content of `107_31` §3 together with the
same fiber-product and bidegree arguments already used in `107_02`.
\(\square\)

So the categorical source package already specializes genus-freely on
\(C\times C\).

## 4. Lefschetz and Euler side

### Theorem 4.1: genus-free Lefschetz and Euler chain

For every \(n\ge1\),

\[
 \Gamma_n\cdot\Delta=N_n,
 \tag{4.1}
\]

and for \(m>n\),

\[
 \Gamma_m\cdot\Gamma_n=q^nN_{m-n}.
 \tag{4.2}
\]

If \(B_d\) denotes the number of closed points of degree \(d\), then

\[
 N_n=\sum_{d\mid n} dB_d,
 \qquad
 Z_C(u)=\exp\left(\sum_{n\ge1}\frac{N_n}{n}u^n\right)
      =\prod_{d\ge1}(1-u^d)^{-B_d}.
 \tag{4.3}
\]

Proof.  This is exactly `107_31` §§4--5.  \(\square\)

Thus the Lefschetz trace and connected Euler extraction are already
genus-free source operations.

## 5. Critical balancing

### Theorem 5.1: genus-free balancing

A primitive closed orbit of degree \(d\), iterated \(k\) times, receives
the source half-density weight

\[
 q^{-kd/2}.
 \tag{5.1}
\]

Proof.  The graph \(\Gamma_{kd}\) has bidegree \((1,q^{kd})\), so the
symmetric half-density rule gives
\((1\cdot q^{kd})^{-1/2}=q^{-kd/2}\).  This is `107_31` §6.  \(\square\)

So the critical exponent is source-forced for every genus.

## 6. Primitive package

Define

\[
 \Delta^0:=\Delta-F_{\rm v}-F_{\rm h},
 \qquad
 \Gamma_n^0:=\Gamma_n-q^nF_{\rm v}-F_{\rm h}.
 \tag{6.1}
\]

### Theorem 6.1: genus-free primitive intersection package

For every \(n\ge1\),

\[
 (\Delta^0)^2=-2g,
 \qquad
 (\Gamma_n^0)^2=-2g\,q^n,
 \qquad
 \Gamma_n^0\cdot\Delta^0=-a_n.
 \tag{6.2}
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
 \tag{6.3}
\]

Proof.  This is exactly `107_30` §§4--7.  \(\square\)

## 7. Hodge-sign output

### Corollary 7.1: genus-free calibrated Weil bound

Applying the classical Hodge-index theorem on \(C\times C\) gives

\[
 |a_n|\le 2g\,q^{n/2}.
 \tag{7.1}
\]

Thus the entire source chain

\[
 \Gamma_{F^n}
 \longrightarrow
 \Gamma_{F^n}\cdot\Delta
 \longrightarrow
 Z_C(u)
 \longrightarrow
 q^{-kd/2}
 \longrightarrow
 G_n^0
 \longrightarrow
 |a_n|\le 2g\,q^{n/2}
 \tag{7.2}
\]

is now proved in genus-free source form on \(C\times C\).

## 8. Role of the fixed elliptic control

The fixed elliptic control of `107_02` still matters.

1. It is the audited exact positive anchor required by the phase stop
   rule.
2. It is the only place in the current tree where all quantities are
   pinned to one concrete curve and exact preflight values are carried
   through by hand.
3. It provides the fixed operational model against which later
   arithmetic analogues are first compared.

But it is no longer the only place where the source geometry is proved.

## 9. Status consequence

After the present note, the correct Paper 0 reading is:

1. the fixed control \(E/\mathbf F_5\) remains the exact audited anchor;
2. the source correspondence--Lefschetz--Euler--balance--primitive chain
   is now proved genus-freely on \(C\times C\);
3. what remains open is only editorial/integration work if one wants to
   replace `107_02` itself by one single genus-free master paper.
