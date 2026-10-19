# P123.002 — coefficient trace and the separated mixed corner

## Status

`PROVED-IN-REPOSITORY` on the finite locally free coefficient module and on
its distinguished global nuclear Frechet sector.

This is a coefficient-valued trace theorem.  A scalar intersection theorem,
kernel localization, mixed Riemann--Roch and geometric effectivity remain
open.

## 1. Source-defined trace target

Retain the row-A object

```text
N_DN = O_C e_1 direct-sum O_C e_2 direct-sum O_C e_Gamma.
```

It is finite locally free over the commutative coefficient algebra object
`O_C`.  Therefore its endomorphism algebra is locally the matrix algebra

```text
End_{O_C}(N_DN) ~= M_3(O_C).
```

Define the coefficient trace by the ordinary finite-projective module
trace

```text
Tr_coef : End_{O_C}(N_DN) -> O_C,
Tr_coef((a_ij)) = a_11+a_22+a_33.
```

This construction uses neither the von Mangoldt functional nor a selected
family of arithmetic labels.

## 2. Trace theorem

### Theorem 2.1

`Tr_coef` is independent of the chosen local free frame, additive and
cyclic:

```text
Tr_coef(U V)=Tr_coef(V U).
```

It commutes with restriction and base change of the coefficient algebra.
On finite matrices over the distinguished global nuclear Frechet algebra it
is continuous.  The determinant polynomial

```text
det_coef(1-TU) in O_C[T]
```

is likewise frame-independent, restriction-compatible and continuous in
every coefficient for fixed rank.

### Proof

The trace and determinant of an endomorphism of a finite locally free
module are obtained by descent from their matrix formulas.  On overlaps a
change of frame conjugates the matrix; trace and determinant are invariant
under conjugation over a commutative algebra.  The matrix identity
`Tr(UV)=Tr(VU)` proves cyclicity.  Restriction and scalar base change apply
entrywise and preserve the universal trace and determinant polynomials.
Finally, addition and Dirichlet convolution are continuous in every
defining seminorm of the global coefficient algebra, and only finitely many
entries and products occur.  This proves continuity.  QED.

## 3. Restriction to the mixed corner

Let `iota(a)` be multiplication by `a` on `O_C e_Gamma`, extended by zero
on the two ruling summands.  The corner theorem of P123.001 gives

```text
iota(a)iota(b)=iota(a*b).
```

The coefficient trace gives

```text
Tr_coef(iota(a))=a,
Tr_coef(iota(a)iota(b))=a*b.                 (3.1)
```

Thus

```text
I_coef(a,b):=Tr_coef(iota(a)iota(b))=a*b     (3.2)
```

is a continuous symmetric coefficient-valued pairing on the global mixed
nuclear corner.

### Corollary 3.1 — separatedness

The radical of `I_coef` is zero.

### Proof

If `I_coef(a,b)=0` for every `b`, take `b=delta_1`, the convolution unit.
Then `a*delta_1=a=0`.  QED.

Consequently the coefficient-valued numerical quotient of this corner is
the entire infinite-rank nuclear coefficient algebra.  This is compatible
with the finite-rank obstruction: no finite-dimensional quotient has been
asserted or produced.

## 4. Logical placement of B and C

Row B will select `a=delta_n` and prove that these coefficient
endomorphisms are the realization of its Witt/cyclotomic correspondences.
Equation (3.1) will then give, without any scalar arithmetic input,

```text
Tr_coef(rho_m rho_n)=delta_mn.
```

Row C must construct and justify a scalarization

```text
aug_C : trace target -> scalar nuclear character target
```

and prove its compatibility with diagonal contact.  On the finite Euler
sector the existing candidate is the continuous functional `ell`; only at
that later stage does

```text
ell(delta_mn)=Lambda(mn)
```

enter.  The archimedean and polar components require additional trace
targets and cannot be manufactured by `Tr_coef` alone.

## 5. Precise gain and remaining boundary

The construction supplies three pieces that were previously conflated with
the final scalar formula:

1. a trace defined before the arithmetic labels;
2. cyclicity and determinant compatibility from finite-projective algebra;
3. a separated infinite-rank mixed numerical corner before scalarization.

It still does not prove that `iota(a)` is a localized kernel on the
spherical square, that `Tr_coef` is diagonal pullback of such a kernel, or
that the periodic determinant extends to this corner.  Therefore A.2,
A.5, A.6 and A.8 of the acceptance specification remain only partially
discharged.

## 6. Next gate

The next gate remains `A1-KERNEL-LOCALIZATION`, now with a sharper required
commutative square:

```text
localized A-kernel K_a  --composition-->  K_(a*b)
        |                                  |
 diagonal trace                     diagonal trace
        v                                  v
       a                  --product-->     a*b.
```

The lower row is Theorem 2.1.  The missing theorem is the upper row and the
vertical comparison.  Constructing only the lower row again is no longer
progress on A1.

