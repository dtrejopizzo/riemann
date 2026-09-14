# P123.004 — semilocal crossed-product source audit

## Status

`IMPORTED` for the algebraic sheaf theorem of Connes--Consani.

`IMPORTED` for Connes's semilocal distributional trace formula in its
published analytic setting.

`OPEN` for the nuclear-completed sheaf, its comparison with `C_Q`, and its
comparison with the periodic Deligne determinant.

## 1. Primary sources and version check

The current arXiv record checked on 2026-09-04 is:

* A. Connes and C. Consani, *On the Jacobian of the completed spectrum of
  Z*, arXiv:2602.15941v1, submitted 2026-02-17.  The arXiv record presently
  lists only v1: <https://arxiv.org/abs/2602.15941>.

Its local TeX source is

```text
00-references/papers-nuevos/A/arXiv-2602.15941v1/Jacobian.tex
SHA-256 8b18c5b22a0e98a52f2b8cd22c4f89be70995ba5f02e5eab5da2f77d6fa693d7
```

The sheaf theorem invoked there is proved in:

* A. Connes and C. Consani, *Knots, primes and class field theory*,
  arXiv:2501.06560v1, Theorem `structure1`:
  <https://arxiv.org/abs/2501.06560>.

The repository source is

```text
00-references/papers-ref-phase-60/arXiv-2501.06560v1/arXiv-2501.06560v1.tex
SHA-256 249fed347469cfaf6da97915d547c2ca704a4ba21cc339613713e570f14d5cea
```

The distributional trace formula is traced back by both papers to:

* A. Connes, *Trace formula in noncommutative geometry and the zeros of the
  Riemann zeta function*, Selecta Math. 5 (1999), 29--106;
  arXiv:math/9811068.

## 2. Exact imported sheaf theorem

For a finite set of places `S` containing infinity, put

```text
A_S=product_(v in S) Q_v,
Gamma_S=Z_S^x=G_m(S^c).
```

The primary theorem constructs the algebraic crossed product

```text
K_alg(S^c)=S(A_S) rtimes Gamma_S.                    (2.1)
```

The transition from `S` to `S'` tensors a Bruhat--Schwartz function with
the characteristic function of the maximal compact rings at the new
places and includes the group of units.  The theorem proves:

1. (2.1) is a sheaf of algebras on `Spec Z`;
2. its generic stalk is `S(A_Q) rtimes Q^x`;
3. its global sections are `S(R) rtimes {+1,-1}`.

The proof is not merely asserted in the 2026 paper.  The 2025 source first
proves that the Bruhat--Schwartz algebras form a subsheaf of the constant
global adelic Schwartz algebra, then repeats the membership argument for
the uniquely expanded finite crossed-product sums.

## 3. Hypothesis map for row A

| imported datum | repository target | verdict |
|---|---|---|
| Zariski base `Spec Z` | arithmetic curve underlying row A | exact on the finite-place base; compactified infinity is encoded semilocally, not as a new closed stalk |
| `S(A_S)` | trace-class/test-function coefficient ideal | exact |
| `Gamma_S=G_m(S^c)` | source-defined scaling correspondences | exact |
| crossed-product multiplication | mixed correspondence composition | exact algebraically |
| algebraic sheaf descent | localization of finite sums | exact |
| generic stalk | global adelic correspondence algebra | exact |
| multiplier elements `U_q` | individual correspondence graphs | present as multipliers/actions, not as Schwartz elements |
| involution and C-star completion | dagger/analytic completion | natural but not part of Theorem `structure1`; must be constructed in our declared category |
| nuclear rapid completion in the group label | `C_Q` of P123.003 | not supplied |
| periodic determinant/RR comparison | existing `lambda_int` | not supplied |

Therefore the imported theorem closes the algebraic sheaf part of A1 for
finite crossed-product sums.  It does not close A1 for the nuclear
completion and does not close A5--A8.

## 4. Exact imported trace scope

**Normalization audit, 2026-09-05:**
[P123.035](P123_035_REAL_FOURIER_GAMMA_NORMALIZATION.md) detects a
factor-two discrepancy in the literal real Fourier-log calculation of
the separately cited Meyer source. Its real coefficient cannot be
imported without reconciling full-line Haar and even-function conventions.
The schematic semilocal formula below does not settle that normalization
or identify the repaired common-carrier shadow. Finite-place Fourier
normalization is treated explicitly in P123.034.

For a compactly supported test function `h` on the semilocal idele class
group and the phase-space cutoff `R_lambda`, the semilocal trace formula has
the form

```text
Tr(theta(h)R_lambda)
 =2h(1)log(lambda)
  +sum_(v in S) integral'_Q_v^x h(u^-1)/|1-u|_v d^*u
  +o(1).                                             (4.1)
```

This is an analytic operator trace after cutoff and renormalization.  Its
local distribution is interpreted by the kernel
`delta(ux-y)` restricted to the diagonal, producing `|1-u|_v^-1`.

Equation (4.1) is not an intersection product on the spherical square, a
mixed Riemann--Roch theorem, or a Hodge-index statement.  The 2026 paper
describes it as a geometric reinterpretation on the adelic Picard monoid;
the trace theorem itself is the earlier noncommutative-geometric result.

## 5. New A1 architecture forced by the audit

The strongest nonconflated carrier now available is two-tiered:

```text
algebraic localized trace ideal:
    K_alg = S(A_-) rtimes G_m                  [IMPORTED]

dagger-complete label/kernel algebra:
    C_Q with K_c(x,y)=sum c_q delta(y-qx)      [P123.003]

required bridge:
    completed crossed-product sheaf K_nuc
    containing K_alg as trace ideal and C_Q as multipliers.
```

The bridge must prove strict topological descent, continuity of the module
actions, compatibility of dagger, and agreement of composition.  Only
after that construction may the distributional diagonal trace be compared
with `Tr_coef` from P123.002.

## 6. Stop rule

It is inadmissible to cite the algebraic sheaf theorem as if it already
proved descent of infinite rapidly decreasing sums, or to cite (4.1) as if
it were the mixed Riemann--Roch determinant.  Those are precisely the next
two construction gates.
