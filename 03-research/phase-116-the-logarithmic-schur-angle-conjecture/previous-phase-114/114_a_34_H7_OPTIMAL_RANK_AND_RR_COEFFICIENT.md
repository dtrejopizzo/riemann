# 114.a.34 — Optimal signed rank and the candidate RR coefficient

```
+--------------------------------------------------------------------------+
| OPTIMALITY  Any injective r-coordinate signed leaf code with N leaves    |
|             satisfies 3^r <= 2N+1.                                      |
| SHARPNESS   Ternary multiplicities 1,3,...,3^(r-1) attain the bound.     |
| CONSEQUENCE The log(3) in a_30 is forced by maximal signed rank, not an  |
|             arbitrary coding base.                                      |
| COEFFICIENT h_code(M,n) ~ [log(2)log(q)/(2log(3))] Mn.                  |
| RR GATE     Promote this sectorial coefficient to the global normalized  |
|             H^0 up to o(t^2), then prove its intersection functoriality. |
+--------------------------------------------------------------------------+
```

## 1. Exact capacity theorem

A depth-`d` dyadic tree from `114_a_30` has

\[
 N=2^d                                                        \tag{1.1}
\]

leaves. Consider any positive integer multiplicities
`w_0,...,w_{r-1}` with total `S<=N`. To recover independently the zero,
positive and negative choice at every coordinate, the signed digit map

\[
 \{-1,0,1\}^r\longrightarrow\mathbb Z,
 \qquad \varepsilon\longmapsto\sum_j\varepsilon_jw_j          \tag{1.2}
\]

must be injective.

### Theorem 1.1 (optimal signed leaf rank)

Every family satisfying (1.2) obeys

\[
 3^r\le2S+1\le2N+1,
 \qquad r\le\lfloor\log_3(2N+1)\rfloor.              \tag{1.3}
\]

Conversely, for

\[
 r=\lfloor\log_3(2N+1)\rfloor                         \tag{1.4}
\]

the weights `w_j=3^j` satisfy

\[
 \sum_{j<r}w_j=(3^r-1)/2\le N                         \tag{1.5}
\]

and make (1.2) injective. Thus (1.3) is sharp.

### Proof

The `3^r` signed words in (1.2) are distinct integers in `[-S,S]`, an
interval containing exactly `2S+1` integers. This proves (1.3).

For `w_j=3^j`, suppose a signed sum vanishes and choose its largest nonzero
digit `j`. Its absolute contribution is `3^j`, while all lower terms total
at most `(3^j-1)/2`; cancellation is impossible. Equations (1.4)--(1.5)
finish the converse. QED.

For `N=2^d`, Theorem 1.1 gives exactly

\[
 r_d=\lfloor\log_3(2^{d+1}+1)\rfloor,                 \tag{1.6}
\]

the rank used in `a_30`. Hence no other integer leaf multiplicities can
increase the number of independently signed coefficient slots at fixed
dyadic divisor cost.

## 2. Exact ray asymptotic of the optimal code

For even first bidegree `M=2d`, define the code entropy

\[
 h_{\rm code}(M,n)=\log\#I_{r_d}(q^n).                 \tag{2.1}
\]

Fix positive integers `M_0,n_0` with `M_0` even and put
`(M,n)=t(M_0,n_0)`. The cross-polytope estimate from `a_24` gives

\[
 \log\#I_r(Q)=r\log Q-r\log r+O(r)                    \tag{2.2}
\]

when `r=O(t)` and `Q` grows exponentially in `t`. Since

\[
 r_{tM_0/2}=\frac{\log2}{2\log3}M_0t+O(1),            \tag{2.3}
\]

we obtain:

### Theorem 2.1

\[
 h_{\rm code}(tM_0,tn_0)
 =\frac{\log2\,\log q}{2\log3}M_0n_0t^2
   +O(t\log t).                                        \tag{2.4}
\]

The leading constant is optimal among all signed integer-multiplicity
encodings admitted by the same dyadic tree gauge, by Theorem 1.1.

## 3. Polarization and degree units

Write

\[
 \deg_1(L_2^M)=M\log2,
 \qquad \deg_2(L_q^n)=n\log q.                         \tag{3.1}
\]

Then (2.4) reads

\[
 h_{\rm code}(M,n)
 =\frac{1}{2\log3}\deg_1(L_2^M)\deg_2(L_q^n)
   +o(Mn)                                               \tag{3.2}
\]

on positive rays. If a normalized Riemann--Roch formula has

\[
 h^0_{\rm norm}(tD)=\frac12(D\cdot D)t^2+o(t^2),       \tag{3.3}
\]

and the two rulings have square zero, (3.2) forces the mixed candidate

\[
 (L_2^M\cdot L_q^n)_{\rm code}
 =\frac{1}{2\log3}\deg_1(L_2^M)\deg_2(L_q^n).          \tag{3.4}
\]

Indeed `D=MH_1+nH_2` has
`D^2=2Mn(H_1 dot H_2)`, so the factor `1/2` in RR cancels the two mixed
terms. Formula (3.4) is a **forced candidate**, not yet an intersection
product on Haran's pro-square.

## 4. The precise promotion gate

Let `h_FM` denote the full-tree finite-moment dimension constructed on fixed
rays in `a_51`. The sectorial coefficient becomes a genuine Hilbert--Samuel
coefficient if one proves:

> **H7-RR0.** For every fixed positive two-prime divisor `D=(M_0,n_0)`,
> the global normalized dimension is defined functorially and
> \[
> h_{\rm FM}(tD)-h_{\rm code}(tD)=o(t^2),               \tag{4.1}
> \]
> while its polarized leading term is invariant under change of prime
> presentation and compatible with pullback, tensor product and principal
> divisors.

Under H7-RR0, (2.4) determines the mixed intersection coefficient rather
than merely bounding it. A complete RR theorem additionally requires the
linear/canonical correction and a cohomological or exact-sequence
interpretation; H7-RR0 deliberately records only the quadratic statement
needed before those later clauses can be formulated.

The current work proves the optimal sectorial coefficient and isolates
H7-RR0. `a_49` proves Laurent descent and `a_51` proves full-tree extension
on fixed rays; `a_52` makes the finite effective system presentation
independent. This does not prove archimedean/principal invariance, H7-RR0 or
any assertion about RH.

`a_53` later closes principal invariance and real-degree continuity of the
candidate coefficient. It does not prove the comparison (4.1) or sheaf
exactness.

## 5. Verification scope

`114_a_34_h7_optimal_rank_rr_verify.py` checks the sharp leaf-capacity bound,
balanced-ternary injectivity, exact cross-polytope counts and convergence to
the coefficient in (2.4).
