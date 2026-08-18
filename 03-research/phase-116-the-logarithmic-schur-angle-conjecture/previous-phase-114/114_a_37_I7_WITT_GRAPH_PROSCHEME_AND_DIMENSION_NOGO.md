# 114.a.37 — Witt graph pro-scheme and the dimension no-go

```
+--------------------------------------------------------------------------+
| STAGES      W_N=sum_{d|N} Z phi_d is finite free over Z and preserved    |
|             by every Frobenius F_m.                                      |
| GRAPHS      F_m gives a literal graph on Spec(W_N), compatible in N,     |
|             with graph composition Gamma_m Gamma_n=Gamma_mn.             |
| PRO-OBJECT  The inverse system Spec(W_N) is a genuine Witt pro-scheme.   |
| NO-GO       Every stage and its relative square are finite over Spec Z,  |
|             hence one-dimensional: this is not Haran's arithmetic       |
|             surface and cannot supply its quadratic intersection theory. |
| OPEN        Transport the graphs to the Haran square and prove a trace-  |
|             intersection formula for the Lambda mass.                    |
+--------------------------------------------------------------------------+
```

## 1. Frobenius-stable finite stages

Haran 2022, equation (12.17), writes

\[
 \mathcal W=\bigcup_{N\ge1}\mathcal W_N,
 \qquad
 \mathcal W_N=\bigoplus_{d\mid N}\mathbb Z\phi_d.     \tag{1.1}
\]

Each `W_N` is a finite-rank commutative `Z`-algebra. Equation (12.21) gives

\[
 F_m\phi_d=c(m,d)\phi_{d/(m,d)},                       \tag{1.2}
\]

with an integer coefficient `c(m,d)`. Since `d/(m,d)` divides `d`, it also
divides `N`. Therefore:

### Proposition 1.1

Every `F_m` preserves every finite stage `W_N`, and the restrictions commute
with the inclusions `W_N subset W_M` for `N|M`.

This is stronger than merely having an endomorphism of the direct limit.

## 2. Literal graphs and composition

Put

\[
 Z_N=\operatorname{Spec}\mathcal W_N.                 \tag{2.1}
\]

The ring endomorphism `F_m|W_N` induces a scheme endomorphism

\[
 f_{m,N}:Z_N\longrightarrow Z_N.                       \tag{2.2}
\]

Its graph is the closed subscheme

\[
 G_{m,N}=\Gamma(f_{m,N})
 \hookrightarrow Z_N\times_{\operatorname{Spec}\mathbb Z}Z_N,             \tag{2.3}
\]

defined affinely by the multiplication map

\[
 \mathcal W_N\otimes_{\mathbb Z}\mathcal W_N
 \longrightarrow\mathcal W_N,
 \qquad a\otimes b\longmapsto aF_m(b)                 \tag{2.4}
\]

for the chosen graph orientation.

### Theorem 2.1 (literal graph composition)

The graphs satisfy

\[
 G_{m,N}\circ G_{n,N}=G_{mn,N},                        \tag{2.5}
\]

and are compatible under `N|M`.

### Proof

Haran's equation (12.19) gives `F_m F_n=F_mn`. Composition of graphs of
morphisms is the graph of the composite. Proposition 1.1 supplies stage
compatibility. QED.

Consequently

\[
 Z_{\mathcal W}:=\{Z_N\}_{N\ge1}                       \tag{2.6}
\]

is a genuine pro-scheme carrying compatible Frobenius graphs. Their
transpose action on the Witt Hilbert completion is the Verschiebung algebra
of `a_36`.

## 3. Exact dimension obstruction

As a `Z`-module, `W_N` is free of rank

\[
 \operatorname{rank}_{\mathbb Z}\mathcal W_N=\tau(N), 
                                                               \tag{3.1}
\]

the number of divisors of `N`. Hence `Z_N -> Spec Z` is finite. In
particular,

\[
 \dim Z_N=1.                                            \tag{3.2}
\]

Moreover

\[
 Z_N\times_{\operatorname{Spec}\mathbb Z}Z_N
 =\operatorname{Spec}(\mathcal W_N\otimes_{\mathbb Z}\mathcal W_N)         \tag{3.3}
\]

is again finite over `Spec Z`, so

\[
 \dim(Z_N\times_{\mathbb Z}Z_N)=1.                    \tag{3.4}
\]

### Theorem 3.1 (Witt graph space is not the arithmetic surface)

The pro-system (2.6) gives literal Frobenius graphs, but neither its stages
nor their relative squares have surface dimension. It cannot replace

\[
 X\times_{\operatorname{Spec}\mathbb F\{\pm1\}}X,      \tag{3.5}
\]

whose two independent rulings are essential for the quadratic coefficient
constructed in `a_35`.

This is a dimension theorem, not merely a missing comparison map.

## 4. The two remaining realization clauses

The operatorial gate H7-I7-REAL now splits sharply:

1. **H7-WBASE:** construct a functor/kernel from the Witt graph pro-scheme
   to correspondences on Haran's square, carrying `G_m compose G_n` to
   geometric composition and the Witt cyclic vector to the diagonal;
2. **H7-WLEF:** prove a Lefschetz/intersection identity
   \[
   \langle\rho(G_n),\Delta\rangle_Y
   =\log|\operatorname{tr}(\lambda_1(V_n\phi_1))|
   =\Lambda(n).                                        \tag{4.1}
   \]

The graphs (2.3) solve neither clause by themselves. In particular, their
ordinary fixed-point scheme has no degree calculation in the source that
equals (4.1).

Thus `a_36`--`a_37` construct composition first as faithful operators and
then as literal graphs, while proving that the graph space has the wrong
dimension for row A. The only admissible next step is transport to the
two-ruling Haran square, not relabeling `Z_W` as that surface.

## 5. Verification scope

`114_a_37_i7_witt_graph_verify.py` checks formula (12.21), stability of every
finite stage, Frobenius composition and finite-stage ranks. The Krull
dimension conclusion uses the standard theorem that a finite integral
algebra has the same dimension as its base; the verifier does not simulate
scheme intersection.
