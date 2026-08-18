# 114.a.53 — H7: Picard-normalized principal-invariant scalar dimension

```
+--------------------------------------------------------------------------+
| PICARD      Pic(X)=R_{>0}; write d(lambda)=log lambda.                  |
| STANDARD    Replace every effective representative by one determined    |
|             only by lambda: finite floor(lambda) plus residual metric.   |
| RETRACTED   a_57: the accumulated global quotient of a_52 is undefined. |
| CHOICE      Two transports differ by a global unit +/-1.                 |
| ODD         Odd moments turn +/-1 into a coordinatewise bijection.       |
| SURVIVES    Standard representatives, sign invariance and code coefficient.|
| LIMIT       Its code coefficient extends continuously to real degrees.   |
| LATER       a_55 refutes sharp RR for the complete-bounded h_FM image.   |
+--------------------------------------------------------------------------+
```

## 1. Standard representatives of effective Picard classes

Haran's computation gives

\[
 \operatorname{Pic}(X)\simeq\mathbb R_{>0},qquad
 d(\lambda)=\log\lambda.                                                   \tag{1.1}
\]

For `lambda>=1`, put

\[
 Q(\lambda)=\lfloor\lambda\rfloor,qquad
 \rho(\lambda)=\lambda/Q(\lambda)\in[1,1+1/Q(\lambda)).                  \tag{1.2}
\]

Let `S(lambda)` be the representative whose finite denominator/norm is
`Q(lambda)` and whose residual archimedean metric factor is `rho(lambda)`.
Its Picard class is

\[
 Q(\lambda)\rho(\lambda)=\lambda.                                        \tag{1.3}

Thus `S(lambda)` depends only on the class. For a pair of external classes
`(lambda,mu)`, use `S(lambda) boxtimes S(mu)` on the literal square.

Every effective arithmetic divisor representing `lambda` gives an
isomorphic line bundle. Transport its complete bounded scalar section set to
`S(lambda)` and then apply the global finite-effective moment system of
`a_52` at the intrinsic height of `Q(lambda)`.

## 2. Independence of transport and principal invariance

### Former Theorem 2.1 (global quotient retracted by `a_57`)

Conditionally on the global target claimed in `a_52`, the logarithmic
cardinality of the finite-moment image obtained above would be
independent of the chosen isomorphism to `S(lambda)` and is invariant under
adding a principal arithmetic divisor.

### Proof

Two isomorphisms from the same arithmetic line bundle to `S(lambda)` differ
by an automorphism of `S(lambda)`. The global units of the compactified
integer curve are `+/-1` (the global scalar bio is `F{+/-1}`). Hence the two
transported section sets differ by a common sign.

Every exponent used in `a_51`--`a_52` is odd. Multiplication of all scalar
sections by `-1` therefore multiplies every moment coordinate by `-1`, a
bijection of the finite target. Image cardinality is unchanged.

Adding a principal arithmetic divisor does not change the Picard class
`lambda`, so both representatives are transported to the same `S(lambda)`.
The preceding choice-independence proves the assertion. QED.

### Definition 2.2

For effective external classes `(lambda,mu)`, define

\[
 h_{\rm FM}^{\rm Pic}(\lambda,\mu)
 :=\log\#\operatorname{im}
 \left(H^0_{\rm scal}(S(\lambda)\boxtimes S(\mu))
       \longrightarrow\mathcal W_j\right),                              \tag{2.1}

where `W_j` is the least global target of `a_52` covering both finite norms.
At the `a_53` stage Theorem 2.1 was claimed to make (2.1) a function of
Picard classes. `a_57` shows that `W_j` is not defined on all allowed
denominators, so this global definition is retracted.

The standard-representative transport and its residual sign invariance
remain valid per-block statements, but they do not by themselves define a
global `h_FM^Pic` or a coherent-sheaf cohomology theory.

## 3. Real-degree extension of the optimal code

Let `lambda_1,lambda_2>1` and `d_i=log(lambda_i)`. At scale `t`, set

\[
 a_t=\left\lfloor\frac{t d_1}{2\log2}\right\rfloor,qquad
 N_t=2^{a_t},qquad
 r_t=\lfloor\log_3(2N_t+1)\rfloor,qquad
 Q_t=\lfloor e^{t d_2}\rfloor.                                          \tag{3.1}

The binary contraction of depth `a_t` costs finite degree
`2a_t log2<=td_1`; the residual positive metric absorbs the bounded
difference. Likewise `log Q_t<=td_2`, with the residual second metric
positive. Hence the bounded construction of `a_35`, transported through the
standard representatives, gives the complete code `I_{r_t}(Q_t)` in the
class `(lambda_1^t,lambda_2^t)`.

Since

\[
 r_t=\frac{td_1}{2\log3}+O(1),qquad
 \log Q_t=td_2+o(1),                                                       \tag{3.2}
\]

the cross-polytope estimate gives:

### Theorem 3.1 (continuous principal-invariant code coefficient)

\[
 \boxed{
 \log\#I_{r_t}(Q_t)
 =\frac{d_1d_2}{2\log3}t^2+O(t\log t).
 }                                                                        \tag{3.3}

The coefficient is continuous in the real degrees and invariant under all
principal changes of representative. It agrees with `a_34`--`a_35` when the
degrees come from finite prime divisors.

## 4. Exact remaining RR gate

At the `a_53` stage the scalar normalized dimension (2.1) was claimed on
effective external Picard classes. `a_57` retracts that global definition.
The code still has the continuous coefficient (3.3). Even conditionally on
a replacement global target, the proposed sharp upper comparison was

\[
 h_{\rm FM}^{\rm Pic}(\lambda_1^t,\lambda_2^t)
 -\log\#I_{r_t}(Q_t)=o(t^2).                                              \tag{4.1}

Nor is additivity under short exact sequences/restrictions available. At
the `a_53` stage the proposed surviving gate was:

> **H7-RR-FILT/EXACT.** In light of `a_54`, impose a geometric complexity
> filtration and prove the filtered version of (4.1), with the required sheaf/exactness
> formalism, and identify the polarized coefficient with a global
> intersection product.

Principal/sign invariance and real-degree continuity of the **code
coefficient** are no longer part of the gap; global target existence is.

**Later no-go (`a_55`).** Equation (4.1) is false for the `h_FM` defined
from the complete bounded scalar section set: bounded cross-interpolation
surjects onto a full moment block in linear bidegree and produces a positive
quadratic excess. The code coefficient (3.3) remains correct, but its
promotion requires a new selective object H7-SEL-RR/EXACT, not a proof of
(4.1) for the present `h_FM`.

**Global denominator no-go (`a_57`).** Independently, the `h_FM` in (2.1)
is not globally defined because a retained characteristic-`p` coordinate
cannot evaluate the later denominator `p`. The surviving positive result of
this note is the principal/sign invariance and continuity of the **code
coefficient**, not a global moment dimension.

## 5. Verification scope

`114_a_53_h7_picard_normalization_verify.py` checks standard representatives,
principal rescalings, sign-invariance of odd moment images, residual metric
budgets and convergence to (3.3) for many real degree pairs.
