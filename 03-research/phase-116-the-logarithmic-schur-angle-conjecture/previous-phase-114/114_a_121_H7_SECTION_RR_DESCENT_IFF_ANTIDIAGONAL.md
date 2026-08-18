# 114.a.121 — H7: section RR descent is equivalent to anti-diagonal faithfulness

```
+------------------------------------------------------------------------+
| INPUT       a120 gives h(tD)=c d_1(D)d_2(D)t^2+o(t^2) on presentations. |
| KERNEL      a112 confines every Picard relation to (z,-z).              |
| NECESSARY   A nonzero such relation identifies two positive rays with   |
|             different quadratic coefficients.                           |
| SUFFICIENT  If the presentation map is injective, descent is tautological.|
| RESULT      Section-RR descent iff the prime anti-diagonal is faithful.  |
| LIMIT       Does not prove faithfulness, Green realization or RH.        |
+------------------------------------------------------------------------+
```

## 1. Presentation asymptotic

Use the finite-support prime presentation lattice

\[
 \mathfrak D_{\rm pr}=\mathfrak D_1\oplus\mathfrak D_2
 \xrightarrow{\rho}\mathrm{Pic}_{\rm cmp}(Y^{\rm reg})          \tag{1.1}
\]

of `a112`.  Put

\[
 d_i(x)=\sum_pm_{p,i}\log p,
 \qquad q(x)={d_1(x)d_2(x)\over2\log3}.                                \tag{1.2}
\]

For every integral presentation `x` in the strict positive cone, `a120`
constructs a canonical degreewise finite image invariant satisfying

\[
 h_{\rm pres}(nx)=n^2q(x)+o(n^2).                                     \tag{1.3}
\]

Factorwise principal changes and signs have already been removed by
`a53`, `a118` and `a120`.  What is not yet automatic is invariance under two
different presentations with the same image under (1.1).

## 2. A nonzero anti-relation changes the quadratic coefficient

Assume `0!=z in ker rho`.  By `a112`, it has the form

\[
 z=\sum_pa_p(e_{p,1}-e_{p,2}),\qquad
 A=\sum_pa_p\log p\ne0.                                                \tag{2.1}
\]

The last inequality is unique factorization.  Choose an integral
presentation `u` so deep in the positive cone that both `u` and `u+z` are
strictly positive.  We may additionally arrange

\[
 d_2(u)-d_1(u)\ne A                                                    \tag{2.2}
\]

by adding one prime generator to either ruling; only one real value is
forbidden.  Then

\[
 \begin{aligned}
 q(u+z)-q(u)
 &= { (d_1(u)+A)(d_2(u)-A)-d_1(u)d_2(u)\over2\log3}\\
 &= {A(d_2(u)-d_1(u)-A)\over2\log3}\ne0.                              \tag{2.3}
 \end{aligned}
\]

Nevertheless `rho(nu)=rho(n(u+z))` for every positive integer `n`.

### Theorem 2.1 (necessity)

If an invariant `h` on actual completed Picard classes pulls back to the
`a120` asymptotic (1.3) on every positive presentation ray, then `rho` is
injective.

### Proof

Class invariance gives

\[
 h(\rho(nu))=h(\rho(n(u+z))).                                          \tag{2.4}
\]

Apply (1.3) to the two fixed positive rays, subtract and divide by `n^2`.
The left side is zero for every `n`, while the limit of the right side is
the nonzero number (2.3), a contradiction.  Hence no nonzero `z` exists.
QED.

The argument needs only `o(n^2)` errors; the stronger `O(n)` error of `a120`
is more than sufficient.

## 3. Exact equivalence

### Corollary 3.1

The following are equivalent:

1. the all-positive-ray calibrated invariant of `a120` descends from
   `mathfrak D_pr` to `rho(mathfrak D_pr)` with its stated asymptotic;
2. `rho` is injective;
3. the prime anti-diagonal map `delta_pr` of `a112` is injective.

### Proof

Theorem 2.1 proves `(1)=>(2)`.  If `rho` is injective, every image class has
a unique presentation, so `(2)=>(1)` is tautological.  The equivalence
`(2)<=>(3)` is Proposition 3.1 of `a112`.  QED.

This is the section-theoretic analogue of `a116`: the intersection form and
the sharp section dimension have the **same** exact descent obstruction.
Consequently anti-diagonal descent and the geometric-canonicity clause of
H7-SEL are not two independent open problems.

## 4. Remaining scope

`a121` closes an equivalence, not the anti-diagonal theorem.  A direct unit
or boundary calculation is still required to prove `delta_pr` injective.
Even after that, H7-REG-EXCESS-RR must realize the numerical form
geometrically and H7-FRESH-EXACT must supply whatever restriction formalism
is actually needed.  Dynamic undecorated cycles, row A and RH remain open.

## 5. Verification scope

`114_a_121_h7_section_rr_descent_verify.py` checks the exact coefficient
difference, positivity shifts, the scaling contradiction and the scope
markers on exhaustive finite-support samples.  The unbounded theorem is the
two-ray limit argument above.

**Later boundary reduction (`a128`--`a129`).**  The explicit fraction
`p_2/p_1` cancels only finite valuations; it leaves nonunit real-boundary
data.  Therefore descent is still open rather than false.  By the boundary
kernel formula it is now equivalent to H7-ARCH-BDRY.
