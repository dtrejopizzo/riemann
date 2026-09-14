# P122 -- the critical Sobolev gate detects the Tate boundary

## Status

`PROVED-IN-REPOSITORY` as an analytic statement, and `CONDITIONAL` as a
property of the still unconstructed relative determinant correspondence.

This note identifies exactly what would be gained if the completed incoming
current of a first-contact state were a boundary vector in the critical
determinant class `H^(1/2)`.  It kills the finite-dimensional Tate forcing,
but it does not kill the remaining homogeneous first-contact state.

## 1. The forced current has literal activation jumps

Fix `T>log 2`, put `I_T=(-T,T)`, and let

\[
 r_\varepsilon(t)
 =c\bigl(e^{t/2}+\varepsilon e^{-t/2}\bigr),
 \qquad \varepsilon\in\{+1,-1\}.                  \tag{1.1}
\]

Extend `r_epsilon` by zero outside `I_T` and define the finite-window causal
Euler observation

\[
 k_\varepsilon(t)=\mathcal Z_{T,+}r_\varepsilon(t)
 =\sum_{n\geq1}n^{-1/2}E_Tr_\varepsilon(t-\log n),
 \qquad t\in I_T.                                 \tag{1.2}
\]

For every integer `n` with

\[
                  2\leq n<e^{2T},                 \tag{1.3}
\]

there is an interior activation point

\[
                  t_n=-T+\log n\in I_T.           \tag{1.4}
\]

### Proposition 1.1 -- exact jump size

The one-sided limits of `k_epsilon` at `t_n` exist and

\[
 \boxed{
 k_\varepsilon(t_n+)-k_\varepsilon(t_n-)
 =n^{-1/2}r_\varepsilon(-T+).}                    \tag{1.5}
\]

In particular, if `c` is nonzero then every active integer produces a
nonzero jump.

#### Proof

Near `t_n`, all summands in (1.2) except the `n`-th one have unchanged
support status and are smooth.  The `n`-th summand is zero to the left and
tends from the right to `n^(-1/2)r_epsilon(-T+)`, proving (1.5).

Moreover

\[
 r_\varepsilon(-T+)
 =c\bigl(e^{-T/2}+\varepsilon e^{T/2}\bigr).       \tag{1.6}
\]

For `epsilon=+1` the bracket is positive.  For `epsilon=-1` it can vanish
only when `T=0`, excluded by `T>log 2`.  Thus it is nonzero whenever `c` is
nonzero.  QED.

There is no cancellation hidden in (1.5): distinct positive integers have
distinct activation points.

## 2. The exponent `1/2` is exact

### Lemma 2.1 -- a jump is not in `H^(1/2)`

Let `f` be piecewise `C^1` near `x_0` and suppose

\[
                 f(x_0+)-f(x_0-)=a\ne0.           \tag{2.1}
\]

Then `f` does not belong locally to `H^(1/2)` near `x_0`.

#### Proof

After shrinking the neighborhood, values on opposite sides of `x_0`
differ by at least `|a|/2`.  The cross-boundary portion of the Gagliardo
seminorm is therefore bounded below by a positive constant times

\[
 \int_0^\delta\int_0^\delta{dx\,dy\over(x+y)^2}=+\infty. \tag{2.2}
\]

QED.

Conversely, a compactly supported function with finitely many jumps and
piecewise Lipschitz pieces lies in `H^s(R)` for every `s<1/2`.  This follows
by applying the same cross-boundary integral with denominator
`|x-y|^(1+2s)`, which is finite precisely for `s<1/2`, while the same-side
Lipschitz contributions are harmless.

### Theorem 2.2 -- critical regularity kills exactly the Tate multiplier

For `T>log 2`,

\[
 \boxed{
 \mathcal Z_{T,+}r_\varepsilon\in H^{1/2}(I_T)
 \quad\Longrightarrow\quad c=0.}                 \tag{2.3}
\]

For arbitrary `c`, the same vector belongs to `H^s(I_T)` for every
`s<1/2`.  Thus the phase-121 subcritical regularity is exactly compatible
with a nonzero Tate forcing and cannot prove (2.3).

#### Proof

The integer `n=2` satisfies (1.3).  If `c` were nonzero, Proposition 1.1
would give a nonzero interior jump at `t_2`, contradicting Lemma 2.1.  The
subcritical assertion follows from the finite number of active summands
and the converse observation above.  QED.

## 3. Consequence for a first-contact current

Phase 121 proves, on the common closed zeta--Gamma graph,

\[
 \mathcal L^{\rm gr}_{T,-}(F)
 =-\mathcal Z_{T,+}r_\varepsilon.                 \tag{3.1}
\]

Hence Theorem 2.2 gives the unconditional implication

\[
 \boxed{
 \mathcal L^{\rm gr}_{T,-}(F)\in H^{1/2}(I_T)
 \quad\Longrightarrow\quad
 r_\varepsilon=0,
 \quad \mathcal L^{\rm gr}_{T,-}(F)=0.}          \tag{3.2}
\]

The hypothesis in (3.2) is not presently proved.  Its exponent matches the
restricted determinant boundary exponent: in the finite Bohr carrier of
P122.016 the commutator Hilbert--Schmidt energy is the critical flow
seminorm

\[
 \tau_S([P_+,\pi(f)]^*[P_+,\pi(f)])
 =\sum_n|\omega_n||f_n|^2.                        \tag{3.3}
\]

This matching of exponents is not a trace theorem.  P122.021 proves that
sharp-window translation fails to preserve `H^(1/2)`.  To use (3.3), the
missing relative Gamma--Euler correspondence must prove
that its Calderon trace sends the physical incoming current (3.1) into the
ordinary time-boundary `H^(1/2)` class.  Identifying these two spaces by
notation would be a type error; the trace theorem is part of the missing
construction.

## 4. Exact limitation

After (3.2), the first-contact equation becomes homogeneous:

\[
 F\in\mathcal P_T,
 \qquad P_T\mathcal A_\infty F=0,
 \qquad \mathcal L^{\rm gr}_{T,-}(F)=0.           \tag{4.1}
\]

Nothing proved here implies `F=0` from (4.1).  In particular, zero current
substituted into the strong commutator identity gives a conservation
identity, not annular vanishing of `mathcal Z_(T,+)F`.  A second,
Euler-specific equality law is still required.

The smallest already proved detector for that second law is one transverse
prime seam: phase 121 proves that

\[
 (E_{p,T}-E_{q,T})\mathfrak h_F=0
 \quad(p\ne q)\quad\Longrightarrow\quad F=0       \tag{4.2}
\]

at first contact.  P122.020 packages (3.2) and (4.2) as the minimal
two-gate completion theorem for `D_candidate`.

```text
activation jump formula                           PROVED-IN-REPOSITORY
H^(1/2) excludes nonzero Tate forcing             PROVED-IN-REPOSITORY
subcritical H^s, s<1/2, permits the forcing        PROVED-IN-REPOSITORY
relative determinant trace lands in H^(1/2)       OPEN CONSTRUCTION AXIOM
zero Tate current implies F=0                      FALSE AS AN INFERENCE HERE
```
