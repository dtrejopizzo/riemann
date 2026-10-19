# R183.008 — The white-light residue and the raw-Gram no-go

## 0. Verdict

R183.007's strategy cannot be closed by directly using the positive norm of the semilocal trace formula. Its residue does not have rank two: it is the identity on the whole test space, multiplied by the volume \(2\log\Lambda\). The two Tate conditions do not annihilate it.

Hence Weil's form is the **finite part after subtracting an infinite-rank positive operator**. Positivity before the subtraction does not pass to the finite part. This is the exact operator analogue of the full-rank residue found in R183.007(3.2).

The Connes--Consani route remains open, but its positive object cannot be the raw semilocal Gram matrix. It must be a relative defect in which the white light cancels algebraically within a single norm or a contraction before the limit is taken.

## 1. The dominant term is a full norm

Connes--Consani's semilocal trace theorem states, for compact \(f\),

\[
 \operatorname{Tr}(\vartheta(f)R_\Lambda)
 =2f(1)\log\Lambda+W_S(f)+o(1),                    \tag{1.1}
\]

where \(W_S(f)\) is the sum of local principal values. For the positive test

\[
 h=h_1*h_1^*,                                      \tag{1.2}
\]

the multiplicative convention gives

\[
 h(1)=\int_{C_{\mathbb Q,S}}|h_1(x)|^2d^*x
      =\|h_1\|_2^2.                                \tag{1.3}
\]

After normalization between \(f\) and \(h\), the dominant coefficient is still a positive constant times \(\|h_1\|_2^2\). Hence

\[
 \boxed{
 \operatorname*{Res}_{\Lambda=\infty}
 \operatorname{Tr}(\vartheta(f)R_\Lambda)
 =2\|h_1\|_2^2.}                                   \tag{1.4}
\]

It is an infinite-rank, positive-definite form.

## 2. The Tate moments do not remove the white light

The two moments are

\[
 T_\pm h_1=\int h_1(x)x^{\pm1/2}d^*x.              \tag{2.1}
\]

Their common kernel has codimension at most two and contains infinitely many nonzero vectors. For every \(h_1\ne0\) in that kernel,

\[
                 \|h_1\|_2^2>0.                   \tag{2.2}
\]

By (1.4), the trace's residue does not vanish on the primitive space. In particular, it cannot be

\[
 T_-^*T_-+T_+^*T_+.                                \tag{2.3}
\]

This refutes R183.007's (5.2) for the raw Gram matrix coming from \(R_\Lambda\).

## 3. The finite part does not inherit the sign

Write schematically

\[
 K_\Lambda=2\log\Lambda\,I+K_0+o(1),
 \qquad K_\Lambda\ge0.                              \tag{3.1}
\]

Positivity of \(K_\Lambda\) for large \(\Lambda\) imposes no restriction on \(K_0\): for any bounded Hermitian operator \(H\),

\[
                    2\log\Lambda\,I+H\ge0          \tag{3.2}
\]

once \(\Lambda\) is large enough. This is the operator version of R183.007's scalar example \(s^{-1}-1>0\).

The subtraction

\[
 K_0=\operatorname{FP}_{\Lambda\to\infty}
       (K_\Lambda-2\log\Lambda I)                  \tag{3.3}
\]

is precisely where the prespectral reason for the sign is lost.

## 4. Agreement with the greatest-common-divisor fiber

R183.007 finds, at finite cutoff,

\[
 K_{-1}=C_SD_rG_hD_r^*,                             \tag{4.1}
\]

generically of full rank. The trace formula shows that, after assembling every quotient and passing to the test space, that residue is the white light (1.4). It is not a spurious artifact of the \(\gcd\) reordering: it is the semilocal trace's volume term.

R183.006's coordinate \(\log p/(p+1)\) lives in the finite part and keeps agreeing with D.247's ports. But that agreement does not transmit positivity from the pole.

## 5. The only type of object that survives

The next object must cancel \(2\log\Lambda I\) **before** using positivity. There are two algebraically admissible forms:

1. a source contraction \({\cal R}_{q,h}^{[\Lambda]}\) with
   \[
   B_\Lambda^*B_\Lambda-C_\Lambda^*C_\Lambda
   =B_\Lambda^*(1-{\cal R}_{q,h}^{[\Lambda]*}
                     {\cal R}_{q,h}^{[\Lambda]})B_\Lambda\ge0; \tag{5.1}
   \]
2. a joint rectangular column \(Z_\Lambda\) such that
   \[
   K_\Lambda-2\log\Lambda I
   =Z_\Lambda^*Z_\Lambda+o(1),                     \tag{5.2}
   \]
   where the subtraction is realized by interference between
   components of \(Z_\Lambda\), not after forming \(Z_\Lambda^*Z_\Lambda\).

The second formulation requires an indefinite input metric or a conservative dilation; an orthogonal sum of positive squares cannot cancel an infinite-rank positive residue. The first formulation is exactly R183.003--004's return operator.

## 6. Logical status

* White-light residue (1.4): **PROVED/CITED** via the semilocal trace.
* Infinite rank on the Tate kernel: **PROVED**.
* Inheritance of positivity by the finite part: **REFUTED**.
* R183.007's raw Gram matrix with a rank-two Tate residue: **NO-GO**.
* R183.006's finite coordinate: **VALID**, with no inherited sign.
* Relative contraction with prior cancellation (5.1): **OPEN**.
* Row D: **OPEN**.
