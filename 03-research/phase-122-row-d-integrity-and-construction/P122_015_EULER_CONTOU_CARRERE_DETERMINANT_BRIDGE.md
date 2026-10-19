# P122 -- Euler analytic determinant bridge (and the Contou--Carrere type boundary)

## Status

`IMPORTED COCYCLE + PROVED EULER EVALUATION` on each local analytic loop,
with a correction to the first version of this note.  The analytic
loop-group determinant extension is classical Segal--Wilson/
Pressley--Segal material; the evaluation and its distinction from the
algebraic Contou--Carrere symbol are checked here.  The half-density
normalization, the logarithmic connection and the oriented determinant
curvature of P122.013 arise from one degree-one Euler loop pair.  This
removes an apparent choice in the local D block.

The factor `1-r^2` below is the analytic Hardy/Toeplitz determinant cocycle.
It is **not** the algebraic tame or Contou--Carrere symbol of the two Laurent
series in `C((z))`; that formal symbol is `1`.  Consequently no algebraic
reciprocity theorem may be invoked from the analytic calculation.

The global product/trivialization remains `OPEN`; Section 5 states why the
local symbol does not imply it.

## 1. The two oriented Euler loops

Fix `0<r<1` and on an annulus containing the unit circle put

\[
 e_r^+(z)=1-rz,
 \qquad e_r^-(z)=1-rz^{-1}.                        \tag{1.1}
\]

They are exchanged by circle reflection/conjugation.  Their logarithms
converge absolutely on the appropriate sides of the circle:

\[
 \log e_r^+=-\sum_{n\ge1}{r^nz^n\over n},
 \qquad
 \log e_r^-=-\sum_{n\ge1}{r^nz^{-n}\over n}.      \tag{1.2}
\]

For this inside/outside analytic factorization, define the Hardy
determinant cocycle

\[
 \langle f,g\rangle_{\rm Hdet}
 =\exp\operatorname {Res}_{z=0}(\log f\,d\log g). \tag{1.3}
\]

Here the logarithms mean their convergent positive and negative Fourier
expansions on the annulus.  In particular, `log e_r^-` has infinitely many
negative powers.  Formula (1.3) is an analytic loop-group determinant
cocycle; it is not an elementwise formula in the formal Laurent field.
No choice of the Weil form enters it.

## 2. Exact central-extension normalization

### Theorem 2.1

The oriented pair (1.1) satisfies

\[
 \boxed{\langle e_r^+,e_r^-\rangle_{\rm Hdet}=1-r^2.} \tag{2.1}
\]

Reversing the ports inverts the symbol.

#### Proof

From (1.2),

\[
 d\log e_r^-=\sum_{m\ge1}r^mz^{-m-1}dz.
\]

Only equal indices contribute to the residue, hence

\[
 \operatorname {Res}(\log e_r^+d\log e_r^-)
 =-\sum_{n\ge1}{r^{2n}\over n}
 =\log(1-r^2).
\]

Exponentiation proves (2.1).  Since the residue pairing is antisymmetric
up to an exact differential,
`<e_r^-,e_r^+>_(Hdet)=<e_r^+,e_r^->_(Hdet)^(-1)`.  QED.

At `r=p^(-1/2)`, (2.1) is exactly

\[
                         1-r^2=1-p^{-1}.           \tag{2.2}
\]

This is the normalization under the square root in the phase-120 Poisson
state and the bulk coefficient in the causal delay balance.  It is thus a
central-extension invariant of the two oriented local factors, not a fitted
Hilbert-space coefficient.

### Proposition 2.2 -- algebraic CC/tame comparison

Viewed instead as elements of `C((z))`,

\[
 v_z(e_r^+)=0,\qquad v_z(e_r^-)=-1,\qquad e_r^+(0)=1.
\]

The field-valued Contou--Carrere symbol specializes to the tame symbol, so

\[
 (e_r^+,e_r^-)_{\rm tame}
 =(-1)^{0\cdot(-1)}
   \left.{(e_r^+)^{-1}\over(e_r^-)^0}\right|_{z=0}
 =1.                                                       \tag{2.3}
\]

There is no contradiction with (2.1): the negative Fourier logarithm used
there is not a formal Laurent series in `C((z))`.  The value `1-r^2`
records the inside/outside Hardy polarization and the zero enclosed by the
circle; the formal tame symbol records only the puncture at `z=0`.

## 3. The same loop gives the logarithmic connection

Taking the grading derivative of the positive loop gives

\[
 -z{d\over dz}\log e_r^+(z)
 ={rz\over1-rz}
 =\sum_{n\ge1}r^nz^n=\phi_r(z).                   \tag{3.1}
\]

Hardy compression of multiplication by (3.1) is exactly

\[
 T_{\phi_r}=rS(1-rS)^{-1}=A_r.                    \tag{3.2}
\]

The reflected loop gives the adjoint orientation.  Its failure to preserve
the Hardy polarization is the Hankel block
`H_(bar phi_r)`, and

\[
 A_r^*A_r-A_rA_r^*
 =H_{\bar\phi_r}^*H_{\bar\phi_r}.                 \tag{3.3}
\]

Therefore (2.1), (3.1) and (3.3) form one chain:

```text
oriented Euler loop pair
  -> analytic Hardy determinant cocycle 1-r^2
  -> grading logarithmic connection A_r
  -> Hardy off-diagonal block
  -> rank-one determinant curvature.
```

For a prime, multiplying (3.1) by `log p` is the grading/length derivative
and yields the exact coefficients `(log p)p^(-n/2)`.

## 4. Consequences for the local D block

P122.013 introduced its determinant chart through the rank-one map built
from `H_(bar phi_r)`.  The present theorem proves that all its local inputs
have one source:

| datum | source operation on `(e_r^+,e_r^-)` |
|---|---|
| causal orientation | choice of inside/outside loop |
| half-density normalization | square root of the analytic determinant cocycle `1-r^2` |
| prime-power connection | grading derivative of `log e_r^+` |
| positive root curvature | determinant curvature of its off-diagonal Hardy block |
| port reversal | swap the loops, dualize the central line |

Thus the local line is not merely the graph determinant of an operator
selected after seeing its rank-one square.  Both the operator and its
normalization are forced by the central extension of the degree-one Euler
factor.

For several distinct roots the logarithmic derivative is a sum of
geometric sequences and its Hankel rank increases.  This retains the
shifted-degree falsifier before scalar augmentation.

## 5. The precise global obstruction

The local equality (2.1) is an analytic scalar central commutator.
Multiplying it
over primes gives local normalization factors; it does not provide:

1. an archimedean loop whose determinant line includes the exact quarter
   Gamma and both Tate conditions;
2. a convergent global central extension/trivialization of the Euler
   product at the critical boundary;
3. a metric anomaly theorem identifying the two causal histories; or
4. a first-contact flatness theorem.

Taking logarithms of a product of (2.1) returns an additive scalar law and
falls under P122.009--P122.010.  Tensoring the associated Hermitian lines
and asserting semipositivity falls under P122.014.  Hence neither operation
closes D.

The genuinely new remaining target is narrower:

> Lift the completed Euler--Gamma functional equation to a metrized
> determinant central extension on the common causal/Calderon carrier, and
> prove its anomaly/trivialization formula before taking scalar curvature.

P122.016 refines the type of this sentence: on the physical continuous
carrier the Euler factors are not ordinarily restricted.  The lift must use
the canonical semifinite Bohr determinant density and an archimedean
correspondence module, not an ordinary `GL_res(L^2(R))` determinant line.

If such a lift exists, P122.015 fixes every finite-place local restriction
it must have.  If its Gamma--Tate anomaly leaves an extra boundary line, the
determinant route fails rather than allowing that line to be tuned away.

Proposition 2.2 is a hard type boundary: this lift cannot be obtained by
suspending (2.1) into the published two-dimensional Contou--Carrere
reciprocity theorem.  It needs an analytic Hardy/Toeplitz or relative
semifinite determinant theory on the actual causal carrier.
