# E101.055 - Two-transport holonomy autopsy

## 1. Abstract setting

Let `D_N(t,z)` be a nonvanishing finite bordered determinant, continuously
differentiable in `t`, and let `G(t,z)` be an independent arithmetic target
which does not depend on the Fourier cutoff `N`.  Work on a simply connected
safe domain where logarithms are fixed and put

```text
Phi_N(t,z)=log D_N(t,z)-G(t,z).                      (1.1)
```

Define the arithmetic and spectral connections

```text
A_N(t,z)=partial_t Phi_N(t,z),
B_N(t,z)=Phi_(N+1)(t,z)-Phi_N(t,z).                  (1.2)
```

The proposal in E101.054 was to extract new information from their mixed
closed-loop defect.

## 2. Exact flatness theorem

### Theorem 2.1

For every family satisfying the hypotheses above,

```text
Delta_N A_N=partial_t B_N.                           (2.1)
```

Consequently the holonomy around every finite rectangle in `(N,t)` is zero.

### Proof

Direct calculation gives

```text
Delta_N A_N
=partial_t Phi_(N+1)-partial_t Phi_N
=partial_t[Phi_(N+1)-Phi_N]
=partial_t B_N.                                     (2.2)
```

Summation in `N` and integration in `t` prove the rectangle statement.
`QED`

No matrix identity, Euler product, zero location, or positivity enters this
proof.  The flatness is the commutation of two differences of one scalar.

## 3. The arithmetic target cancels from the spectral edge

Because `G` is independent of `N`,

```text
B_N=log D_(N+1)-log D_N.                             (3.1)
```

Thus the independent arithmetic target is invisible on the two spectral
edges of the rectangle.  Integrating (2.1) from `t=0` to `t=1` gives

```text
[Phi_(N+1)(1)-Phi_N(1)]
-[Phi_(N+1)(0)-Phi_N(0)]
=integral_0^1 Delta_N A_N(t)dt.                     (3.2)
```

After summation from `N_0` to `N_1-1`, equation (3.2) is only the telescoping
identity

```text
Phi_(N_1)(1)-Phi_(N_0)(1)
-Phi_(N_1)(0)+Phi_(N_0)(0)
=the same four boundary values.                     (3.3)
```

The desired identification `Phi_N(1)->0` remains one of those boundary
values.  It has not been estimated or determined.

## 4. Falsifier test

Replace `D_N` by the determinant of the controlled off-line build while
keeping the independent Euler target `G`.  Definitions (1.1)--(1.2) remain
valid, so Theorem 2.1 still gives zero holonomy.

```text
HOL(P)=0 and HOL(Z)=0.                               (4.1)
```

The proposed curvature therefore fails `N3` of E101.054: it does not
distinguish the builds.

The nonzero planted discrepancy survives only in the terminal value

```text
Phi_N^P(1,z),                                        (4.2)
```

which is the original identification defect.

## 5. Two independent connections do not repair the argument

One may instead introduce a spectral connection `A^S` and an independently
defined Euler connection `A^E`, then call

```text
K=Delta_N(A^S-A^E)-partial_t(B^S-B^E)               (5.1)
```

their relative curvature.  There are two possibilities.

```text
1. Both pairs are gradients of known finite scalar potentials.
   Then K=0 identically and the preceding autopsy applies.

2. The Euler pair has no finite scalar potential already identified with
   the determinant pair.
   Then proving K=0 is exactly the missing compatibility theorem.        (5.2)
```

In the second case the word `curvature` does not supply a new mechanism.  It
renames the obligation that the Euler and spectral currents agree.

## 6. Novelty-gate verdict

```text
N1  finite statement:                                      pass;
N2  permitted inputs:                                      pass;
N3  controlled build must fail:                            fail;
N4  avoids forbidden tools:                                pass;
N5  one-way implication rather than restatement:           fail.        (6.1)
```

The two-transport holonomy is rejected as a main route.

## 7. What survives

The calculation does identify one useful requirement.  A successful new
object cannot be obtained by taking two derivatives of the same determinant.
It must use an additional finite structure which

```text
is present for the arithmetic build;
is absent for the controlled off-line build;
acts before the cofinal limit;
is not equivalent by definition to the terminal current.               (7.1)
```

The unconditional radical identity

```text
Q_W(k,phi)=0                                            (7.2)
```

has exactly this separation property when `k=E(h)` is kept fixed: the
arithmetic Weil distribution annihilates it, while insertion of an extra
off-line quartet contributes a nonzero evaluation unless that quartet lies
in the divisor of the transform of `k`.

The next admissible direction is therefore not a second determinant
connection.  It is a finite dual-test completion theorem transporting (7.2)
to the matched current without splitting the Fourier collar.

## 8. Status

```text
proved:
  exact flatness of two transports derived from one scalar determinant;
  zero rectangle holonomy for both arithmetic and controlled builds;

rejected:
  ARITHMETIC-HOLONOMY of E101.054 as a discriminating mechanism;

retained:
  the requirement of an additional finite arithmetic structure;
  the global radical identity as the only current source with the required
  model separation;

next:
  formulate and test RADICAL-DUAL-COMPLETION;
  Omega7 remains open.
```
