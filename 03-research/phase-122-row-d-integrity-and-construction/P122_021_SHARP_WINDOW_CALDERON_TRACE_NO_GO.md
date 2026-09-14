# P122 -- sharp windows do not transport the determinant `H^(1/2)` class

## Status

`PROVED-IN-REPOSITORY`.  This note corrects a possible overinterpretation of
P122.019: equality of the critical exponents does not identify the Bohr
determinant domain with the physical finite-window trace domain.

## 1. Truncated translation creates the forbidden jump

Let `I_T=(-T,T)`, let `0<a<2T`, and define, initially on smooth functions
on the closed interval,

\[
 (C_{a,T}f)(t)
 =\mathbf1_{I_T}(t-a)f(t-a),\qquad t\in I_T.       \tag{1.1}
\]

### Proposition 1.1

If `f(-T)` is nonzero, then `C_(a,T)f` has a jump of size `f(-T)` at
`-T+a` and does not belong to `H^(1/2)(I_T)`.  Consequently truncated
translation is not a map

\[
                  H^{1/2}(I_T)\longrightarrow H^{1/2}(I_T). \tag{1.2}
\]

#### Proof

To the left of `-T+a`, the indicator in (1.1) is zero.  From the right the
function tends to `f(-T)`.  The cross-boundary Gagliardo integral diverges
as in P122.019, Lemma 2.1.  Taking `f=1` gives a smooth input whose output is
not in `H^(1/2)`, proving the last assertion.  QED.

For `s<1/2`, the same operation is bounded on the relevant zero-extension
class.  This is the familiar sharp-cutoff threshold and exactly matches the
phase-121 regularity ceiling.

## 2. Application to the causal Euler observation

Every nontrivial summand of

\[
 \mathcal Z_{T,+}f
 =f+\sum_{2\leq n<e^{2T}}n^{-1/2}C_{\log n,T}f     \tag{2.1}
\]

contains the operation in Proposition 1.1.  Thus even a smooth `f` produces
interior activation jumps unless its left boundary trace vanishes.  On the
Tate line that trace is

\[
 c(e^{-T/2}+\varepsilon e^{T/2}),                 \tag{2.2}
\]

which vanishes, for `T>log 2`, exactly when `c=0`.

Therefore Gate R of P122.020 cannot be justified by either of the bare
statements

```text
the source is smooth in the Gamma bulk;
the Euler loop lies in the semifinite restricted determinant group.
```

The sharp finite-window trace sits between them and loses the endpoint
regularity.

## 3. The Bohr and physical seminorms are different types

For a trigonometric polynomial on the finite Bohr torus, P122.016 proves

\[
 \tau_S([P_+,\pi(f)]^*[P_+,\pi(f)])
 =\sum_n|\omega_n||f_n|^2.                         \tag{3.1}
\]

This is a homogeneous half-derivative in the Kronecker-flow frequency.  The
seminorm in P122.019 is the inhomogeneous time-boundary norm on the bounded
interval after zero extension and causal truncation.  Proposition 1.1
shows there is no automatic bounded intertwiner from (3.1) to that physical
norm.

The earlier slit-disk construction makes the same distinction geometrically.
Its Gamma field is holomorphic off an exterior cut, while the Frobenius
states are discontinuities between the two banks of that cut.  Holomorphy
on the slit domain gives separate regular traces; it does not identify the
two traces across the slit and therefore does not remove their jump.

## 4. Corrected meaning of Gate R

Gate R is not a generic regularity theorem for all determinant sections.
That statement is false by Proposition 1.1.  The admissible target is a
transmission theorem for a source-defined horizontal/null family:

\[
 \text{horizontal source equation plus the two Tate conditions}
 \quad\Longrightarrow\quad
 \text{matching of the two sharp-window traces}.         \tag{4.1}
\]

When specialized to a first-contact state, (4.1) places its completed
incoming current in `H^(1/2)` and P122.019 then forces the Tate multiplier
to vanish.  The transmission law must be defined for a larger source family
and proved by a Green or gluing theorem; defining horizontality as the
absence of the jump would be circular.

This is a stricter construction requirement than the wording “determinant
regularity” alone suggests.

```text
Bohr determinant half-derivative                     PROVED
physical sharp-window half-derivative                DIFFERENT SPACE
truncated translation preserves H^(1/2)              FALSE
slit-domain holomorphy glues its two banks            FALSE
horizontal transmission cancels the activation jump  OPEN
```
