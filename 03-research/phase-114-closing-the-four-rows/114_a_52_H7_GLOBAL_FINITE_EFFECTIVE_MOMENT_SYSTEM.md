# 114.a.52 — H7: global finite-effective full-tree moment system

```
+--------------------------------------------------------------------------+
| HEIGHT      tau(P,Q)=max(1,log P,log Q) uses only intrinsic norms.       |
| UNIFORM     One controlled prime at scale T handles every P,Q<=e^T.     |
| FULL TREE   Finite twisted bios of a_51 evaluate every scalar tree.      |
| CANONICAL   The quotient depends on the norms, not their prime/arity     |
|             presentation.                                                |
| TENSOR      log norms add and cofinal target projections are compatible.|
| SIZE        Uniform targets retain O(T^2) logarithmic cardinality.       |
| RETRACTED   a_57: old characteristic-p blocks cannot evaluate 1/p.      |
| SURVIVES    Each bounded-height block separately; fixed rays via a_51.  |
+--------------------------------------------------------------------------+
```

## 1. Intrinsic finite height

For an effective finite divisor `D=sum_p n_p[p]` on the arithmetic curve,
put

\[
 N(D)=\prod_p p^{n_p},qquad \deg_{fin}D=\log N(D).                       \tag{1.1}
\]

For a pair `(D_1,D_2)`, write `P=N(D_1)`, `Q=N(D_2)` and define

\[
 \tau(P,Q)=\max(1,\log P,\log Q).                                        \tag{1.2}
\]

These quantities depend only on the finite divisors, not on a selected
prime decomposition or contraction arity. Unique factorization makes (1.1)
intrinsic, and tensor product adds the logarithmic heights.

## 2. A uniform finite-bio block at height `T`

Let `T>=1`,

\[
 H_T=\lceil e^T\rceil,qquad
 R_T=\left\lceil\log_3(2H_T+1)\right\rceil.                              \tag{2.1}
\]

Apply the controlled-prime construction of `a_51` with `(r,Q)=(R_T,H_T)`,
using the least prime in its prescribed progression. This canonically
produces `p_T` such that

\[
 p_T>\max(2H_T,3^{R_T},2^{4R_T}),\qquad
 \gcd(s,p_T-1)=1quad(1\le s<4R_T, s\text{ odd}),                       \tag{2.2}
\]

and

\[
\log p_T=O(T).                                                          \tag{2.3}
\]

The third lower bound makes all nodes `2^s` in the block distinct already
as ordinary integers modulo `p_T`. It leaves (2.3) unchanged and is used by
the bounded-interpolation audit `a_55`.

For every odd `s<4R_T`, the finite twisted-bio map of `a_51` is defined on
the complete scalar bio. Their product gives the uniform block

\[
 \mathcal U_T:A_{full}(1)\longrightarrow
 \mathbb F_{p_T}^{,2R_T}.                                                \tag{2.4}

### Theorem 2.1 (uniform full-tree separation)

For every pair `P,Q<=H_T`, every balanced family of rank

\[
 r\le\lceil\log_3(2P+1)\rceil\le R_T                                   \tag{2.5}

and denominator `Q` is separated by the first `2r` coordinates of (2.4).

### Proof

The map is defined on every scalar tree by the finite-bio construction.
Since `p_T>2H_T>=2Q`, all labels `a/Q`, `1<=a<=Q`, are nonzero and distinct
up to sign modulo `p_T`. Since `p_T>3^{R_T}>=3^r`, grouped balanced
coefficients do not wrap. The odd-Vandermonde determinant (3.2) of `a_51`
is therefore nonzero and proves separation. QED.

## 3. Proposed global cofinal system (retracted by `a_57`)

Use dyadic heights `T_j=2^j` and define

\[
 \mathcal W_j=prod_{i=0}^j\mathbb F_{p_{T_i}}^{,2R_{T_i}}.              \tag{3.1}

The transition `W_{j+1}->W_j` is coordinate projection. For a finite
effective pair `(P,Q)`, choose the least `j` with `tau(P,Q)<=T_j` and measure
the image of its complete bounded scalar section set in `W_j`.

### Former Theorem 3.1 (global finite-effective compatibility)

The system (3.1) has the following properties.

1. It is independent of the prime and arity presentation of `(D_1,D_2)`.
2. If finite effective divisors are enlarged or tensored, passage to a later
   dyadic level and projection back commute with every scalar evaluation.
3. It separates the balanced lower family for every finite effective pair.
4. Its logarithmic size is quadratic:
   
   \[
   \log\#\mathcal W_j
    =\sum_{i=0}^j2R_{T_i}\log p_{T_i}
    =O\left(\sum_{i=0}^jT_i^2\right)=O(T_j^2).                           \tag{3.2}
   \]

### Proof

Only the intrinsic height bound enters (2.1)--(2.4), proving (1). Every
component is a bio map defined before imposing a degree bound; later targets
retain earlier components, proving (2). Theorem 2.1 proves (3). Finally
`R_T=Theta(T)` and (2.3) prove (4). QED.

The conclusion just stated is false. `a_57` observes that a retained old
factor `F_(p_i)` eventually meets the allowed divisor denominator `p_i`.
It cannot evaluate `1/p_i`, since reduction sends `p_i` to zero. Therefore
`W_j` is not defined on every later bounded section set. Items 1--2 above
hold only while all current denominators remain prime to every retained
characteristic; they do not globalize to the entire effective cone.

## 4. Exact remaining global gate

At the `a_52` stage Theorem 3.1 was claimed to close the finite-divisor
portion of H7-FMD-GLOB. `a_57` retracts that claim. Even ignoring this
denominator obstruction, the construction does not
identify finite divisors that become equivalent after adding a principal
arithmetic divisor with a compensating archimedean Green term. Nor does it
define continuity for arbitrary real archimedean coefficients.

The surviving gate is therefore:

> **H7-AR-PRIN.** Extend the normalized dimension to the archimedean metric
> parameter, prove invariance under principal arithmetic divisors, and prove
> compatibility with restriction/exact sequences.

At this stage H7-AR-PRIN was expected to precede promotion of the sectorial
coefficient to a global intersection/Riemann--Roch statement.

`a_53` later closes the principal-invariance and real-degree coefficient
parts by normalizing every effective Picard class to a standard
representative. `a_55` then refutes the sharp comparison for the complete
bounded image. A new selective object H7-SEL-RR/EXACT is required.

After `a_57`, only the continuous code coefficient and per-block
normalization parts of `a_53` survive. A global principal-invariant moment
dimension additionally requires H7-DEN-TRANS.

## 5. Verification scope

`114_a_52_h7_global_finite_effective_verify.py` checks uniform controlled
primes, denominators inside each individual height, intrinsic norms and
balanced-code separation. It does not prove global retention; `a_57`
supplies the explicit later-denominator collision.
