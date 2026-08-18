# E78.98 - The tail side of `SAFE-GAMMA-IDENT / OUTER-LIMIT` is already closed

**Run:** 2026-07-19.  
**Scope:** IDENT, `Re(s)>1` arithmetic front.  
**Class:** REDUCCION GENUINA.  
**What we know after this doc that we did not know before:** in front B the
only genuinely open load-bearing object is the exact cell-smoothed holomorphic
comparison, because the hard Euler tail and the high completed-zeta tail are
already theorem-grade and uniform on compact subsets of `Re(s)>1`.

## 0. Wall checklist

```text
MW-1:  respected.  No positivity/Weil form is used.
MW-2:  respected.  Arithmetic is used only in the absolutely convergent region
       Re(s)>1.
MW-3:  respected.  No local-global infinite-dimensional assembly.
MW-4:  respected.  No wrong-sign lower-bound mechanism is used; only explicit
       uniform tail estimates.
MW-5:  respected.  No site/cohomology input.
MW-6:  respected.  No uniform spectral-gap hypothesis.
K1-K5: respected.  No ambient inverse norm, no absolute pre-cancellation
       closure, no scalar determinant endpoint identification.
P76.061: respected.  The live core remains a paired Schur/Cauchy object before
         inversion; this note only closes the arithmetic tails around it.
E72.16/E77.7az: respected.  The plant break is used only on the IDENT front,
                where it is supposed to occur.
```

## 1. The current front-B obligations

E77.6 reduces IDENT to

```text
FIXED-L-WEYL
+ SAFE-GAMMA-IDENT
+ OUTER-LIMIT
+ cofinal diagonal
=> SR-LOG-2SCALE => IDENT.                              (B-1)
```

On the derivative side the finite object is

```text
J_{L,N}(sigma)
 := L coth(sigma L/2)
  + 2 Re(i T'_{L,N}(i sigma)/T_{L,N}(i sigma))
  - B_ext,L,N(sigma).                                   (B-2)
```

The exact finite calculus identity in E77.6 says that `(B-2)` is the right
partition-invariant safe derivative quantity.  The open question is not
whether its surrounding arithmetic tails converge absolutely; it is whether the
core Schur/cell quantity matches the correct holomorphic fixed-L target.

## 2. Two tail theorems already closed

Two theorem-grade inputs are already available.

### 2.1 Absolute Euler tail (P76.039)

Let

```text
x = lambda^2 = e^L.                                     (B-3)
```

Then for every compact `K subset {Re(s)>1}`,

```text
sum_{n>x} Lambda(n)n^(-s) -> 0
```

locally uniformly on `K` as `L->infinity` (P76.039).  Using only Chebyshev's
bound and partial summation, one gets the explicit estimate

```text
|sum_{n>x} Lambda(n)n^(-s)|
 <= x^(-sigma) psi(x)
   + |s| int_x^infinity psi(t)t^(-sigma-1)dt
 = O_K(x^(1-sigma)),   sigma=Re(s)>1.                   (B-4)
```

Hence the hard prime-power tail is already closed in the exact region allowed
by MW-2.

### 2.2 High completed-zeta tail (P76.038)

Let

```text
R_{L,N} = 2 pi N / L.                                   (B-5)
```

Then the completed-zeta zero contribution above `R_{L,N}` is

```text
O_K(log R_{L,N} / R_{L,N})                              (B-6)
```

uniformly on compact safe sets, unconditionally (P76.038).  Therefore under
`N/L -> infinity` this high target tail is `o_K(1)`.

So both tails surrounding the core comparison are already closed:

```text
prime-power tail beyond x=e^L      -> 0 uniformly on K,
high Xi tail beyond R_{L,N}        -> 0 uniformly on K.  (B-7)
```

## 3. The forbidden shortcut remains forbidden

P76.040 autopsies the invalid hard-truncation identity

```text
J_{L,N}(s) ?= arch_gamma(s)
          - 2 sum_{n<=e^L} Lambda(n)n^(-s)
          + small finite-section error.                 (B-8)
```

This is false at finite scale.  Therefore the closed tail theorems from §2 may
**not** be attached directly to a raw truncated Euler sum.

The valid core object remains the exact cell-smoothed Schur quantity `(B-2)`.

## 4. Genuine reduction of front B

Because §2 closes the tails and §3 rules out the hard truncation shortcut, the
front-B burden reduces to the exact window comparison already named in P76.038:

```text
CELL-TRACE-WINDOW:
core Schur quotient trace below R_{L,N}
 - completed-zeta trace below R_{L,N}
 -> 0                                                   (B-9)
```

locally uniformly on compact subsets of `Re(s)>1`.

In E77.6 language, this means:

```text
SAFE-GAMMA-IDENT / OUTER-LIMIT
reduce to proving that the exact holomorphic fixed-L core behind J_{L,N}
matches the corresponding completed-zeta finite window, because every tail
outside that window is already theorem-grade.           (B-10)
```

This is a genuine reduction, not a reparametrization:

```text
old front B:
  coupled core + low prime powers + high prime powers + high Xi tail;

new front B:
  exact cell-smoothed finite window only.              (B-11)
```

Less information is required: the arithmetic outside the window is already
eliminated by theorem-grade uniform tails.

## 5. Immediate consequence for the next admissible document

The next admissible front-B theorem is no longer a statement about raw Euler
convergence.  It must act directly on the exact holomorphic core:

```text
SAFE-GAMMA-IDENT-CORE:
identify the fixed-L limit of J_{L,N} as the exact cell-smoothed
Gamma-prime / Schur window functional, uniformly on compact subsets of
Re(s)>1.                                                (B-12)
```

Then:

```text
SAFE-GAMMA-IDENT-CORE
+ absolute Euler tail (P76.039)
+ high Xi tail (P76.038)
=> SAFE-GAMMA-IDENT / OUTER-LIMIT.                      (B-13)
```

This isolates the only front-B load-bearing object that is still open.

## 6. Probe audit

Companion:

```text
E78_98_safe_gamma_ident_tail_probe.py
E78_98_safe_gamma_ident_tail_results.json
```

The probe evaluates the explicit bound from `(B-4)` against direct prime-power
tails truncated at `2e6`, for several `lambda` and safe `sigma`.

Representative outcome:

```text
actual tail / explicit bound < 1
```

throughout the tested grid, with comfortable slack.  This does not prove
P76.039, which is already proved, but it audits that the bound is numerically
consistent on the current safe window.

## 7. Status

```text
candidate closure - pending review

proved:
  the absolute Euler tail and the high completed-zeta tail are already closed
  uniformly on compact subsets of Re(s)>1;

proved:
  the hard truncated Euler shortcut is inadmissible and remains autopsied;

reduced:
  front B to the exact cell-smoothed finite-window core comparison
  CELL-TRACE-WINDOW / SAFE-GAMMA-IDENT-CORE;

next:
  attack SAFE-GAMMA-IDENT-CORE directly, i.e. the holomorphic fixed-L core
  identity for J_{L,N}, with the tails removed from the problem.
```
