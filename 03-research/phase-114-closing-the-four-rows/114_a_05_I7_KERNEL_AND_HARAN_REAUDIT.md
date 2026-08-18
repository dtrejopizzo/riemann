# 114.a.05 — I7 resolved at the algebraic level; the missing object is a pairing, not a lattice

```
+--------------------------------------------------------------------------+
| ROW (a), ITEM a4 — CORRECTION AND NEXT GATE                              |
|                                                                          |
| I7-A        CLOSED POSITIVELY.  ker(r,m) contains an explicit free       |
|             abelian group of countably infinite rank:                    |
|             E_n = [Phi_n] - phi(n)[Phi_1], n >= 2.                       |
|                                                                          |
| I7-B        CLOSED NEGATIVELY.  The finite resultant intersection does   |
|             not factor through (r,m).  Phi_3 and Phi_6 have the same     |
|             bidegree (2,0), but their intersections with Delta are       |
|             log 3 and 0.  No form on Z (+) R can recover Lambda.         |
|                                                                          |
| I7-C        OPEN.  Construct a finite diagonal and a positive/proper      |
|             gauge on the explicit kernel lattice, compatible with the    |
|             off-diagonal resultants.  Mahler measure cannot do this: it  |
|             vanishes on the whole cyclotomic lattice.                    |
|                                                                          |
| TATE CLAIM  NARROWED.  Tate telescoping proves uniqueness of a scalar     |
|             F_N-homogeneous functional within a globally bounded         |
|             distance of Mahler measure.  It does not construct or        |
|             uniquely determine a Green function or an intersection      |
|             pairing.                                                     |
|                                                                          |
| HARAN G-7   PARTIALLY DISCHARGED FROM THE SOURCE.  Section 11 defines     |
|             completed bundles D_d, their section sheaves O_X(D), and     |
|             rank-one isomorphism classes for arbitrary pro-CFR schemes.  |
|             What remains is their computation on the square, plus a      |
|             degree, proper gauge, and intersection pairing.              |
|                                                                          |
| R8          ONLY A DICTIONARY REPAIR IS AVAILABLE.  Thresholding at       |
|             h^0(O_X) can define a strict target-effectivity predicate;   |
|             it does not alter the raw cohomological h^0 and by itself    |
|             does not prove compatibility with source effectivity.        |
|                                                                          |
| VERDICT     a4-weak remains available as a lattice-growth model.          |
|             a4-strong and row (a) remain OPEN at I7-C/Haran-degree.       |
+--------------------------------------------------------------------------+
```

This note supersedes the statements in `114_a_04` that (i) it was unknown
whether the bidegree kernel carries a lattice, (ii) Tate telescoping fixed a
Green metric, and (iii) Haran supplied no section/divisor formalism at all.
None of the corrections uses RH or any zero of `xi`.

It also corrects `114_a_04` Remark 2.3: `W_rat(Z)` is **not** the Arakelov
divisor group `Z (+) R` of `114_a_02`.  The former contains the infinite-rank
kernel constructed below, whereas the latter has rank two as an abstract
additive object.  The map `(r,m)` is a lossy quotient/invariant, not an
identification.  The polynomial section lattices used by the two models can be
isomorphic in each bounded degree without their ambient divisor groups being
isomorphic.

## 1. The exact cyclotomic kernel

Let

```
W_rat(Z) = Frac {P in Z[T] : P(0)=1}
```

under multiplication, and write `[P]` for the corresponding element of its
additive Witt group.  Unique factorisation makes this a free abelian group on
the normalized irreducible polynomials with constant term one.  Put

```
beta = (r,m) : W_rat(Z) -> Z (+) R,
r(P/Q) = deg P - deg Q,
m(P/Q) = log M(P) - log M(Q).
```

For `n >= 1`, let `C_n=[Phi_n]`, using `1-T` for the normalized `n=1`
generator.  Kronecker's theorem gives

```
beta(C_n) = (phi(n),0).
```

### Theorem 1.1 (an explicit infinite-rank lattice in the kernel)

For every `n >= 2` define

```
E_n = C_n - phi(n) C_1.
```

Then `beta(E_n)=0`, and `{E_n : n>=2}` is Z-linearly independent.  Therefore
`ker beta` contains a free abelian group of countably infinite rank.

*Proof.* The bidegree identity is immediate.  If a finite sum
`sum_{n>=2} a_n E_n` is zero, compare coefficients in the free abelian basis
of normalized irreducible polynomials.  The coefficient of `C_n` is `a_n`, so
every `a_n` is zero. `[]`

Thus the undecided sentence in `114_a_04` section 6 has a precise answer if
"lattice" means an integral free module: **yes, and explicitly**.  This does
not yet give a Euclidean/Arakelov lattice: no proper norm or finite covolume is
being claimed.

### Corollary 1.2 (Mahler blindness is total on the cyclotomic lattice)

`m(E_n)=0` for every `n`, and in fact `m` vanishes on the free group generated
by all `C_n`.  Consequently Mahler measure cannot be the norm required on the
I7 kernel: its unit ball contains nonzero integer multiples of every `E_n`.

This distinguishes two notions that `114_a_04` conflated:

- `m` is an additive height/degree on the ambient Witt group;
- a lattice gauge must be proper on the degree-zero kernel (finite balls on
  every finite-rank slice, at minimum).

Mahler measure has the first property and fails the second.

## 2. The quotient obstruction is exact

Let `Delta=div(T-1)`.  The finite local intersection supplied by the
cyclotomic resultant is

```
I_fin(C_n,Delta) = log |Res(Phi_n,T-1)| = Lambda(n).
```

### Theorem 2.1 (I7 no-factorisation theorem)

There is no function `L : Z (+) R -> R`, hence no bilinear form on
`Z (+) R`, such that

```
L(beta(C_n)) = I_fin(C_n,Delta)
```

for all `n`.

*Proof.* `phi(3)=phi(6)=2` and both cyclotomic Mahler measures vanish, so
`beta(C_3)=beta(C_6)=(2,0)`.  But

```
I_fin(C_3,Delta)=Lambda(3)=log 3,
I_fin(C_6,Delta)=Lambda(6)=0.
```

The same input to `L` would have to have two different outputs. `[]`

This is stronger than the single computation `<Gamma_n,Delta>=0` made in
`114_a_04`: it proves that **no modification of the form on the same rank-two
quotient can work**.  The arithmetic information is not merely assigned the
wrong form; it has been lost by the quotient map.

### Corollary 2.2 (what I7 actually asks for)

Any successful intersection theory must retain at least part of `ker beta`.
On the explicit generators it must distinguish

```
E_3 = C_3 - 2 C_1   from   E_6 = C_6 - 2 C_1.
```

The next problem is therefore not existence of an integral kernel.  It is:

> **I7-C.** Construct a symmetric pairing on a completion of the cyclotomic
> kernel whose off-diagonal finite-place terms agree with resultants and whose
> diagonal is finite and source-defined.

**Sharpening (114.a.09).** A positive kernel gauge cannot have Frobenius weight
one because coprime Frobenius maps fix every `E_n`; and a global pairing
descending to Picard annihilates these principal divisors.  The surviving
problem must retain the resultants place-wise or realise nonprincipal cycles on
the Haran square.  See `114_a_09_I7_FROBENIUS_AND_PRINCIPAL_NO_GO.md`.

The old fifth stop test of `106_210` remains exactly here.  For `m != n` the
resultant supplies local intersections, but `Res(Phi_n,Phi_n)=0`, and neither
the discriminant nor Mahler measure is a bilinear diagonal compatible with
those off-diagonal values.

## 3. What Tate telescoping does and does not prove

The following scalar statement in `114_a_04` is correct after making the
boundedness quantifier explicit.

### Proposition 3.1 (bounded homogeneous rigidity)

Suppose `lambda : W_rat(Z)->R` satisfies, for one fixed `N>=2`,

```
lambda(F_N f)=N lambda(f)
```

and there is one constant `B`, independent of `f`, with
`|lambda(f)-m(f)|<=B` for all `f`.  Then `lambda=m`.

*Proof.* For every `k`, equivariance and `m(F_N^k f)=N^k m(f)` give

```
|lambda(f)-m(f)|
 = N^(-k) |lambda(F_N^k f)-m(F_N^k f)|
 <= B N^(-k).
```

Let `k` tend to infinity. `[]`

This proposition is a rigidity lemma about one real-valued functional.  It
does **not** imply the previous `114_a_04` Corollary 4.2:

1. no map from Green functions to such `lambda` was constructed;
2. no reason was given that two admissible Green functions differ by a
   globally bounded scalar functional on all of `W_rat(Z)`;
3. a Green function is a two-variable/singular object and determines diagonal
   regularisations and pairings, while `m` is only a one-variable additive
   degree;
4. Corollary 1.2 shows that `m` is identically zero on the very lattice where
   the missing arithmetic must live.

Accordingly the correct status is: **Mahler degree rigid under the stated
hypotheses; Green metric not constructed and not proved unique.**

## 4. Haran G-7 re-read through section 11

`114_a_03` read Haran section 10 and correctly found the literal pro-object

```
X = overline(Spec Z) x_{Spec F{+-1}} overline(Spec Z).
```

It then stated that the source had no divisor group or section functor.  That
conclusion missed the immediately following section 11, which is written for
an arbitrary pro-`CF R^t` scheme `X={X_N}` and therefore applies formally to
the square.

The source defines:

- `D_d(X_N)=Gamma(X_N, GL_d(K_N)/GL_d(O_XN))` (equation (11.3));
- the sheaf `O_XN(D)` and its sections (equations (11.7), (11.13));
- completed bounded bundles `B_d^*(X)/~` (equations (11.11)--(11.16));
- rank-one isomorphism classes, called `Pic` in the number-field example
  (equation (11.19)).

### Proposition 4.1 (corrected Haran gate)

Haran supplies an intrinsic candidate category of rank-one divisors/line
bundles and an intrinsic section functor on the literal square.  Hence the old
G-7 items (i) "define a divisor group" and (ii) "define H0" are not absent at
the formal level.

What is **not** supplied in the read source is:

1. a computation of `Pic(X)` or of the section sets for this particular
   two-factor pro-object;
2. a degree on `Pic(X)` charging both projections;
3. an archimedean gauge making the section balls finite;
4. an intersection product and a Riemann--Roch theorem on `X`.

Thus G-7 is reduced, not closed.  The next candid construction was to compute
the external-product sector

```
p_1^* L_1 tensor p_2^* L_2  in Pic(X)
```

This sector is now constructed in `114_a_12`: both rulings are individually
injective and the only possible kernel is the anti-diagonal
`(lambda,lambda^{-1})`.  External multiplication of sections also exists.
What remains is to kill that anti-diagonal kernel and prove (rather than
assume) a Kunneth-type statement for its Haran sections.
If the two ranks and two radii multiply as expected, this sector is the first
place where the quadratic growth test can be run on the literal square.

## 5. R8: cohomology versus strict effectivity

For theta cohomology on an arithmetic surface,

```
h^0_X(O_X)=log theta(1)>0.
```

The threshold appearing in `114_d3_03` is useful, but two different operations
must not be conflated:

```
strictly_effective(L)  <=>  h^0_X(L)>h^0_X(O_X),
h^0_thr(L) = h^0_X(L)-h^0_X(O_X).
```

The first is a new **dictionary predicate**.  It sends `O_X` to the boundary
and can therefore satisfy the class-level R8 test.  The second is not the raw
theta cohomology: if only `h^0` is shifted while `h^1,h^2,chi` are unchanged,
the imported Riemann--Roch identity changes by a constant and is no longer the
quoted theorem.

Moreover 113_10 Corollary 2.3 concerns nonzero *functions in the radical*, not
the ordinary fact that the zero divisor has a section.  To finish the repair
one still needs a realisation map and a proof of the biconditional

```
source class effective  <=>  target line bundle strictly_effective.
```

Thresholding is therefore a consistent proposed dictionary, not a proof of
that dictionary.

## 6. Updated row-(a) status

| item | status after this note |
|---|---|
| quadratic lattice-growth model on `P^1_Z` | HAVE (`a4-weak`), subject to its stated model scope |
| Mahler measure as an additive Witt degree | HAVE |
| Mahler/Green uniqueness | **RETRACTED AS STATED**; only Proposition 3.1 survives |
| algebraic lattice in `ker(r,m)` | **HAVE**, Theorem 1.1 |
| pairing descending to `(r,m)` | **IMPOSSIBLE**, Theorem 2.1 |
| proper gauge and finite diagonal on the kernel | **OPEN (I7-C)** |
| Haran divisor/section formalism | **HAVE FORMALLY**, section 11 |
| Haran degree, gauge, intersection, RR | **OPEN** |
| R8 threshold predicate | HAVE as a proposed dictionary; compatibility OPEN |
| `a4-strong` / row (a) | **OPEN** |

## 7. Refutation conditions

- **R35.** Theorem 1.1 fails if a nontrivial finite Z-linear relation among the
  normalized distinct cyclotomic irreducibles is exhibited in `W_rat(Z)`.
- **R36.** Theorem 2.1 fails if either `beta(C_3)!=beta(C_6)` or the exact
  resultant values against `Delta` agree.
- **R37.** Proposition 4.1 fails if Haran's definitions (11.3), (11.7), and
  (11.11)--(11.16) do not apply to the pro-object (10.1).
- **R38.** Any future claim that Mahler measure supplies the I7 kernel norm
  must give a positive value on some `E_n`; otherwise Corollary 1.2 fires.

## 8. Verifier

`114_a_05_i7_kernel_verify.py` checks exact cyclotomic irreducibility,
`beta(E_n)=0`, independence in finite truncations, the `(3,6)` collision, the
resultant values, and Mahler blindness.  It uses exact SymPy arithmetic and no
numerical zero data.
