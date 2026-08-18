# 114.a.142 — H7: the calibrated RR coefficient is an asymptotic determinant line

~~~
+------------------------------------------------------------------------+
| SECTIONS    a120 gives canonical finite images S_t(D)=F_{p_t}^{k_t}.    |
| DET         Their torsion determinant has norm p_t^{-k_t}.              |
| NORMALIZE   The t^{-2} real tensor power has a metric limit.            |
| LIMIT       -log ||1|| -> deg_1(D)deg_2(D)/(2 log 3).                   |
| POLARIZE    Its second difference is exactly the RR biextension E_RR.   |
| SCOPE       This closes RR determinants on the presentation; global     |
|             Cartier descent remains the same H7-RSPH-UNIT gate.         |
+------------------------------------------------------------------------+
~~~

## 1. Determinants of the calibrated section images

Let (D=p_1^*A+p_2^*B) be a primitive positive effective divisor in the
prime presentation, and put

\[
 a=\deg A,
 \qquad b=\deg B,
 \qquad F_{RR}(D)={ab\over2\log3}.                                  \tag{1.1}
\]

The canonical choices in a120 give, for every sufficiently large (t), a
fresh prime (p_t), an integer (k_t), and a surjective image of genuine
bounded sections

\[
 S_t(D)=\mathbb F_{p_t}^{,k_t},
 \qquad k_t\log p_t=t^2F_{RR}(D)+O(t).                              \tag{1.2}
\]

Give the torsion determinant line

\[
 L_t(D)=\det_{\rm tor}S_t(D)
\]

its distinguished generator and cardinality norm, as in a141:

\[
 \|\mathbf1_t\|=\#S_t(D)^{-1}=p_t^{-k_t}.                          \tag{1.3}
\]

## 2. The normalized metric limit

A real power of a distinguished normed line is unambiguous: it is the real
line with the same distinguished generator and with the norm raised to that
power.  Define

\[
 \widehat L_t(D)=L_t(D)^{\otimes 1/t^2}.                             \tag{2.1}
\]

Then (1.2) gives

\[
 -\log\|\mathbf1_t\|_{\widehat L_t}
 ={k_t\log p_t\over t^2}
 =F_{RR}(D)+O(t^{-1}).                                               \tag{2.2}
\]

Consequently the distinguished lines converge isometrically to

\[
 \lambda_{RR}(D)=\mathbb R\mathbf1_D,
 \qquad \|\mathbf1_D\|=e^{-F_{RR}(D)}.                             \tag{2.3}
\]

### Proposition 2.1

The limit (2.3) is independent of every admissible fresh-prime or floor
choice satisfying (1.2).

### Proof

After the distinguished generators are identified, a normed real line has
only one positive metric parameter.  Equation (2.2) forces that parameter
to converge to (e^{-F_{RR}(D)}) for every admissible choice.  QED.

Thus the (O(t)) term obstructs stabilization of the unnormalised finite
determinants, but it does **not** obstruct their normalized determinant
limit.

## 3. Polarization gives the RR biextension

On the full prime presentation lattice put

\[
 F_{RR}(x)={d_1(x)d_2(x)\over2\log3}.                               \tag{3.1}
\]

Equation (2.3) on the positive cone extends uniquely by this quadratic
formula to a distinguished metrized line \(\lambda_{RR}(x)\).  Its Deligne
second difference is

\[
 \begin{split}
 \delta\lambda_{RR}(x,y)
 &=\lambda_{RR}(x+y)\otimes\lambda_{RR}(x)^{-1}
   \otimes\lambda_{RR}(y)^{-1},\\
 -\log\|\mathbf1_{x,y}\|
 &=F_{RR}(x+y)-F_{RR}(x)-F_{RR}(y)\\
 &={d_1(x)d_2(y)+d_2(x)d_1(y)\over2\log3}
 =B_{RR}(x,y).                                                       \tag{3.2}
 \end{split}
\]

The generator map therefore gives a canonical isometry

\[
 \delta\lambda_{RR}(x,y)\simeq\mathcal E_{RR}(x,y)                 \tag{3.3}
\]

with the RR biextension of a124.  The tensor associativity, symmetry and
interchange laws hold because every map sends distinguished generator to
distinguished generator and (3.2) is bilinear.

Combining (3.3) with a141 gives, on the presentation,

\[
 \mathcal E_G\simeq
 \delta\lambda_{RR}\otimes\lambda_C^{-1}.                          \tag{3.4}
\]

Hence both targets in H7-TWO-TARGET-DELIGNE now have determinant origins.

## 4. Exact scope of the remaining gate

This proves **H7-RR-DET-PRES**: the generic calibrated section images have a
canonical normalized determinant limit, and its polarization is exactly
the previously numerical RR line.

It does not assert an unnormalised determinant stabilizes, nor a long exact
sequence between different fresh finite targets.  More importantly, it does
not make a nonzero anti-diagonal class disappear.  By a121 and a124, the
line, its polarization and the Green quotient descend to the repaired
Cartier/Picard object exactly when the prime anti-diagonal is faithful.
After a138 this is H7-RSPH-UNIT, including reflection invariance.

Thus the independent RR-determinant construction is closed on the
presentation.  The single common global obstruction is now
H7-RSPH-UNIT. Row A and RH remain open.

## 5. Verification

`114_a_142_h7_asymptotic_rr_determinant_verify.py` checks the normalized
floor error, choice independence, exact quadratic polarization, tensor laws
and the scope markers above.
