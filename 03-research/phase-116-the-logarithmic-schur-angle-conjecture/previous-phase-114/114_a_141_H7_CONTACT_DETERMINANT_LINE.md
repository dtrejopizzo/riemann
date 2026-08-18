# 114.a.141 — H7: the numerical contact biextension is a torsion determinant

~~~
+------------------------------------------------------------------------+
| CONTACT     Equal opposite prime rulings contribute the module F_p.      |
| PERFECT     F_p is represented by [Z --p--> Z].                         |
| NORM        Its torsion determinant generator has norm p^{-1}.           |
| VIRTUAL     Signed intersection multiplicities use tensor powers/duals.  |
| RESULT      The resulting determinant biextension is exactly E_C of a124.|
| REMAINING   Geometrize E_RR from generic section complexes; E_G is then  |
|             their metric quotient.                                       |
+------------------------------------------------------------------------+
~~~

## 1. Torsion determinant of a finite module

For a finite abelian group \(M\), choose a finite free resolution and take
its Knudsen--Mumford determinant line over \(\mathbb R\). Equip its
distinguished rational torsion generator with norm

\[
 \|\mathbf 1_M\|_{\rm tor}=(\#M)^{-1}.                               \tag{1.1}
\]

This is independent of the resolution: for a short exact sequence
\(0\to M'\to M\to M''\to0\), determinant lines tensor and
\(\#M=\#M'\#M''\). For a virtual negative class use the dual normed line.

For the prime contact,

\[
 \mathbb F_p\simeq[\mathbb Z\xrightarrow{p}\mathbb Z],\qquad
 -\log\|\mathbf1_{\mathbb F_p}\|_{\rm tor}=\log p.                    \tag{1.2}
\]

Thus the norm records the arithmetic length, not merely the dimension over
\(\mathbb F_p\).

## 2. The virtual contact complex

For prime-presentation vectors \(x,y\), put

\[
 m_p(x,y)=x_{p,1}y_{p,2}+x_{p,2}y_{p,1}.                             \tag{2.1}
\]

The contact-framed kernels of a140 and the opposite-ruling incidence of
a114 define the virtual finite contact class

\[
 [K_C(x,y)]=\sum_p m_p(x,y)[\mathbb F_p]
 \quad\text{in }K_0(\mathrm{FinAb}).                                 \tag{2.2}
\]

Positive coefficients mean direct sums and negative coefficients mean
formal negatives, realised on determinant lines by duals. Define

\[
 \lambda_C(x,y)=
 \bigotimes_p\det_{\rm tor}(\mathbb F_p)^{\otimes m_p(x,y)}.          \tag{2.3}
\]

Only finitely many factors are nontrivial.

## 3. Identification with the contact biextension

By (1.2),

\[
 -\log\|\mathbf1_{x,y}\|_{\lambda_C}
 =\sum_pm_p(x,y)\log p=C_\Lambda(x,y).                               \tag{3.1}
\]

### Theorem 3.1

The distinguished-generator map

\[
 \lambda_C(x,y)\xrightarrow{\sim}\mathcal E_C(x,y)                   \tag{3.2}
\]

is an isometry, natural and biexact in \(x,y\). Hence the contact
biextension of a124 is the torsion determinant of the geometric reduced
contact classes (2.2).

### Proof

Equation (3.1) gives the isometry. Bilinearity of \(m_p\) identifies direct
sum of virtual contact classes with tensor product of determinant lines in
either variable. The determinant associativity, symmetry and duality
coherences send distinguished generators to distinguished generators, the
same coherence laws used for \(\mathcal E_C\). QED.

This identification is valid on the presentation lattice independently of
anti-diagonal descent. If H7-RSPH-UNIT holds, both sides descend together.

## 4. Sharpened two-target gate

The contact side of H7-TWO-TARGET-DELIGNE is now constructed rather than
numerical. What remains is:

> **H7-RR-DET.** Construct a determinant/Deligne line
> \(\lambda_{RR}(x,y)\) from the generic calibrated section complexes,
> prove its logarithmic norm is \(B_{RR}(x,y)\), and prove compatibility
> with restriction and principal equivalence.

Once H7-RR-DET holds, define

\[
 \lambda_G=\lambda_{RR}\otimes\lambda_C^{-1}.                         \tag{4.1}
\]

The isometry of a124 then identifies its metric with \(G_{\rm num}\), so
the Green line is no longer an independently chosen numerical object.

The all-ray estimate in a120 gives the correct leading coefficient but only
an \(O(t)\) remainder. It does not by itself construct the biexact
determinant line required by H7-RR-DET.

## 5. Status

The residue/contact half of H7-TWO-TARGET-DELIGNE is closed. The generic RR
determinant, H7-RSPH-UNIT and their descent remain open; therefore row A and
RH remain open.

The verifier 114_a_141_h7_contact_determinant_verify.py checks torsion
cardinalities, virtual duals, bilinearity and the exact metric comparison.
