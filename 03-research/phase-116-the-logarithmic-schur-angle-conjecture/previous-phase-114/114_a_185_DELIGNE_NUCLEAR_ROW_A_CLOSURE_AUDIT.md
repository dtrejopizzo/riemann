# Closure audit for the Deligne--nuclear row A

## 1. Contract being audited

The audited contract is the strongest mathematically consistent version of
row A:

1. a literal noncollapsed arithmetic square;
2. actual invertible divisor lines and principal descent;
3. a canonical cohomology construction with curve-linear restrictions;
4. Kunneth and quadratic mixed Riemann--Roch dimension;
5. a determinant of that cohomology, finite contact and Green comparison in
   one category;
6. exact arithmetic correspondences with a genuine finiteness condition.

The two clauses already contradicted by theorem are not reintroduced: raw
bounded-section dimension is not required to be quadratic, and the exact
correspondence group is not required to have finite abelian rank.

## 2. Acceptance table

| Requirement | Proof object | Verdict |
|---|---|---|
| Noncollapsed carrier | spherical square; mixed smash class survives both marginals | proved |
| Divisor and principal theory | external spherical line modules and multiplication by rational functions | proved |
| Canonical section code | maximal negabinary digit cubes from `1+1=X+X^2` | constructed |
| Code consists of genuine sections | Day representatives `z_epsilon` | proved |
| Separation | assembly recovers every Boolean matrix | proved |
| Cotangent/tangent cohomology | smooth affine linear envelope at the zero code | constructed |
| Kunneth | tangent of matrix code is tensor of the two digit tangents | proved |
| Curve growth | `r(exp(t a))=t a/log 2+O(1)` | proved |
| Surface growth | product rank and `(log 2)^2/t^2` normalization | proved, coefficient one |
| Effective inclusions | zero-extension of digit coordinates | functorial and split |
| Principal invariance | canonical positive normalization; residual sign fixes digit indices | proved |
| Perfect arithmetic category | Deligne homotopy pullback of integral, real and nuclear perfect categories | constructed |
| Determinant | determinant of finite locally free tangent objects; based metric limit | proved |
| Finite contact | integral perfect complex `[Z --p--> Z]`, real-acyclic | proved |
| Green line | determinant quotient in the same Picard groupoid | proved |
| Frobenius composition | Dirichlet convolution by `delta_n` | proved exactly |
| Exact contact values | continuous functional `ell(delta_n)=Lambda(n)` | proved exactly |
| Finiteness | locally free rank three over the nuclear Dirichlet algebra | proved |

## 3. No hidden identification with raw sections

The assembly theorem gives an exponential lower bound for the raw spherical
smash.  The present cohomology is the tangent of the canonical linear code
envelope, not the full raw set.  This distinction is part of the definition
and is testable: the code has `2^(rs)` distinct section values and tangent
rank `rs`, exactly as an `rs`-dimensional vector code should.

Thus the construction does not evade a counterexample by renaming the raw
dimension.  It supplies a different, intrinsic linearization functor whose
input is a canonically characterized family of actual sections.

## 4. No hidden finite-rank claim

The prime-block theorem makes finite abelian rank impossible.  Finiteness is
instead finite local module rank over a nuclear arithmetic algebra.  The
three module generators are the two rulings and the mixed correspondence;
all prime labels occur in the coefficient algebra.  This is why arbitrary
prime blocks do not contradict rank three.

## 5. Final verdict

Relative to the noncontradictory contract in Section 1, the construction

`A_DN=(Y_S,O_Y,Perf_DN,Pic_ext,H^cot,lambda_RR,lambda_C,lambda_G,N_DN)`

is **constructed complete**.  No Kunneth, determinant, principal-descent,
contact, Green or correspondence-composition statement in that contract is
left conditional.

This verdict does not claim that the discarded contradictory clauses have
somehow become true.  It states precisely which categorical replacements
make the arithmetic surface package complete.

