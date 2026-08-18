# 114.a.123 — H7: the global numerical Green excess on the prime lattice

```
+------------------------------------------------------------------------+
| LOCAL       C_Lambda pairs opposite equal-prime rulings by log p.       |
| GLOBAL      B_RR=c(d_1d'_2+d'_1d_2), c=1/(2 log 3).                    |
| GREEN       G_num=B_RR-C_Lambda is the unique bilinear correction.      |
| FORMULA     G(D_p1,D_q2)=c log p log q-delta_pq log p.                  |
| DESCENT     B_RR, C_Lambda and G_num all require anti-diagonal fidelity.|
| LIMIT       Numerical counterterm, not yet a Green complex or metric.   |
+------------------------------------------------------------------------+
```

## 1. The reduced contact form

On the all-prime presentation lattice `mathfrak D_pr` of `a112`, write
`x=(x_(p,1),x_(p,2))`.  The reduced opposite-ruling contacts of `a114`
extend uniquely to the symmetric bilinear form

\[
 C_\Lambda(x,y)=\sum_p\log p\,
 \bigl(x_{p,1}y_{p,2}+x_{p,2}y_{p,1}\bigr).                           \tag{1.1}
\]

Thus

\[
 C_\Lambda(e_{p,i},e_{q,i})=0,
 \qquad
 C_\Lambda(e_{p,1},e_{q,2})=\delta_{pq}\log p.                        \tag{1.2}
\]

The zero same-ruling entries for distinct primes are the empty intersections
of `a113`; the diagonal same-ruling entries are set to zero here because
`C_Lambda` records only the **reduced opposite-ruling contact block**.  It is
not asserted to be the full geometric intersection.

## 2. The unique numerical Green correction

Recall the RR form of `a116`:

\[
 B_{\rm RR}(x,y)=c\bigl(d_1(x)d_2(y)+d_1(y)d_2(x)\bigr),
 \qquad c={1\over2\log3}.                                              \tag{2.1}
\]

Define

\[
 G_{\rm num}:=B_{\rm RR}-C_\Lambda.                                  \tag{2.2}
\]

### Theorem 2.1 (global numerical excess)

`G_num` is symmetric and bilinear, vanishes on pairs in the same ruling,
and on prime generators satisfies

\[
 G_{\rm num}(e_{p,1},e_{q,2})
 ={\log p\log q\over2\log3}-\delta_{pq}\log p.                       \tag{2.3}
\]

Moreover it is the unique bilinear form satisfying

\[
 B_{\rm RR}=C_\Lambda+G                                                \tag{2.4}
\]

on `mathfrak D_pr`.

### Proof

Symmetry, bilinearity and (2.3) follow by subtraction from (1.1)--(2.1).
Both terms vanish on a same-ruling pair.  Equation (2.4) forces
`G=B_RR-C_Lambda`, proving uniqueness.  QED.

The associated quadratic counterterm is

\[
 {1\over2}G_{\rm num}(x,x)
 =c\,d_1(x)d_2(x)-\sum_px_{p,1}x_{p,2}\log p.                          \tag{2.5}
\]

Adding the reduced local term recovers exactly the all-ray section
coefficient of `a120`.

## 3. All three forms have the same descent gate

Let `0!=z` be a possible kernel vector.  By `a112`,

\[
 z=\sum_pa_p(e_{p,1}-e_{p,2}),
 \qquad A=\sum_pa_p\log p\ne0.                                       \tag{3.1}
\]

The form `C_Lambda` is not radical on `z`: choose `r` with `a_r!=0`; then

\[
 C_\Lambda(z,e_{r,1})=-a_r\log r\ne0.                                \tag{3.2}
\]

The form `G_num` is also not radical on `z`.  Choose any prime `s` outside
the finite support of `a`.  Then

\[
 C_\Lambda(z,e_{s,1})=0,
 \qquad
 G_{\rm num}(z,e_{s,1})=-cA\log s\ne0.                               \tag{3.3}
\]

Together with `a116`, this proves:

### Theorem 3.1 (common descent obstruction)

Each of `B_RR`, `C_Lambda` and `G_num` descends from the presentation lattice
to its completed Picard image if and only if `rho` is injective, equivalently
if and only if the prime anti-diagonal map is faithful.

### Proof

Injectivity makes every descent tautological.  Conversely, every nonzero
kernel vector has form (3.1).  Equations (3.2)--(3.3), and Theorem 2.1 of
`a116` for `B_RR`, show that it is outside the radical of each form.  QED.

Thus local contact, the RR form, the section asymptotic and the numerical
Green correction now share one and the same H7-RULING-PF/anti-diagonal gate.

## 4. What remains geometric

`G_num` determines every required prime-sector value and is principal
invariant once it descends.  It does not construct a Green function, a
Hermitian/adelic metric, a cotangent excess complex with Euler degree (2.3),
or a proof of the two-coordinate product formula.  Those are precisely the
remaining geometric content of H7-REG-EXCESS-RR and H7-RULING-PF.  Dynamic
undecorated cycles, row A and RH remain open.

## 5. Verification scope

`114_a_123_h7_global_numerical_green_verify.py` checks symmetry,
bilinearity, the prime matrix, the quadratic decomposition, and the two
non-radicality arguments on finite-support samples.  It does not promote the
numerical counterterm to a geometric Green object.

**Later boundary reduction (`a128`--`a129`).**  The apparent principalization
by `p_2/p_1` fails at infinity.  Theorem 3.1 remains undecided, with its
kernel now localized exactly at H7-ARCH-BDRY.  The numerical matrix cannot be
used to prove that boundary theorem without circularity.
