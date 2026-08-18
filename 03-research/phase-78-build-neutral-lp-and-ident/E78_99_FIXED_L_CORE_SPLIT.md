# E78.99 - The fixed-`L` core reduces to `SHELL-LOG + MU-DIR`

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` front.  
**Class:** REDUCCION GENUINA.  
**What we know after this doc that we did not know before:** after removing the
already-closed arithmetic tails, the live fixed-`L` core does not require a new
holomorphic package beyond the exact two-generator symbol; it reduces to one
nested-shell Cauchy criterion at `mu=0` plus one directional `mu`-freezing
criterion.

## 0. Wall checklist

```text
MW-1:  respected.  No positivity of a Weil form.
MW-2:  respected.  This is still inside the absolute region / fixed-L core and
       does not propagate arithmetic outside Re(s)>1.
MW-3:  respected.  No local-global assembly.
MW-4:  respected.  No wrong-sign lower-bound mechanism is used.
MW-5:  respected.  No site/cohomology input.
MW-6:  respected.  No uniform spectral-gap hypothesis.
K1-K5: respected.  No ambient inverse norm, no absolute pre-cancellation bound,
       no Christoffel evaluator, no scalar determinant closure.
P76.061: respected.  The split keeps the paired transfer/Cauchy object before
         inversion and isolates only a directional `mu` derivative.
E72.16/E77.7az: respected.  No build-separating LP detector is promoted; this
                is a front-B reduction only.
```

## 1. The exact core object after tail removal

E78.98 reduced `SAFE-GAMMA-IDENT / OUTER-LIMIT` to the fixed-`L` core object

```text
J_{L,N}(sigma)
 := L coth(sigma L/2)
  + 2 Re(i T'_{L,N}(i sigma)/T_{L,N}(i sigma))
  - B_ext,L,N(sigma),                                    (C-1)
```

with the arithmetic tails outside the window already closed.

By P76.041 `(TG-4)`--`(TG-8)`,

```text
T_{L,N}(z) = F_{L,N}(z)/(z-d_b),                         (C-2)

F_{L,N}(z) = 1 + a_{b,L,N}[U_{L,N}(z)+U_{b,L,N}]
               + b_{b,L,N}[V_{L,N}(z)+V_{b,L,N}],       (C-3)
```

so the exact finite core is the coupled two-generator logarithmic symbol

```text
J_{L,N}(sigma)
 = L coth(sigma L/2)
  + 2 Re( i F'_{L,N}(i sigma)/F_{L,N}(i sigma)
         -i/(i sigma-d_b) )
  - B_ext,L,N(sigma).                                    (C-4)
```

No further arithmetic simplification is permitted after P76.040.

## 2. The exact `mu`-split

P76.046-P76.047 introduces the same object with explicit `mu` dependence:

```text
J_{L,N}(sigma;mu)                                         (C-5)
```

obtained by using `(H_{N-1}-mu I)^(-1)` in the transfer.  Then the fundamental
identity is

```text
J_{L,N}(sigma;mu_N) - J_{L,N}(sigma;0)
 = int_0^{mu_N} partial_mu J_{L,N}(sigma;t) dt.          (C-6)
```

This is exact.

Therefore every convergence statement for the intrinsic finite-section core
splits into:

```text
J_{L,N}(sigma;mu_N) - J_{L,M}(sigma;mu_M)
 = [J_{L,N}(sigma;0)-J_{L,M}(sigma;0)]
   + int_0^{mu_N} partial_mu J_{L,N}(sigma;t)dt
   - int_0^{mu_M} partial_mu J_{L,M}(sigma;t)dt.         (C-7)
```

So if the `mu=0` branch is Cauchy and the directional `mu`-freezing terms vanish,
then the intrinsic branch is Cauchy as well.

## 3. Reduced subtargets

For one fixed `L` and one safe compact `K`, define:

```text
SHELL-LOG(L,K):
  for N<M sufficiently large,
  sup_K |J_{L,N}(0)-J_{L,M}(0)| -> 0;                    (C-8)

MU-DIR(L,K):
  sup_K int_0^{mu_N} |partial_mu J_{L,N}(sigma;t)| dt -> 0.  (C-9)
```

Then `(C-7)` gives the exact implication

```text
SHELL-LOG(L,K) + MU-DIR(L,K)
=> intrinsic fixed-L Cauchy convergence of J_{L,N}(mu_N).  (C-10)
```

This is strictly smaller than the old target because:

```text
old target:
  direct convergence of the full intrinsic family J_{L,N}(mu_N);

new target:
  one nested-shell statement at the fixed algebraic basepoint mu=0
  plus one directional mu-freezing term.                 (C-11)
```

The new pair uses fewer moving ingredients: `mu_N` is removed from the shell
part and appears only through the single directional integral.

## 4. Why this is genuine and not a reparametrization

This is not the same condition in different coordinates.

The previous live object quantified directly over the moving intrinsic family
`J_{L,N}(mu_N)`.  The new split replaces that by:

```text
1. a shell-nesting Cauchy problem at one fixed parameter mu=0;
2. a separate one-parameter directional correction.      (C-12)
```

That is strictly less information than controlling the full moving family at
once.  In particular, the shell part can now exploit nested-section algebra at
`mu=0` without carrying the spectral drift simultaneously.

## 5. Relation to the existing phase ledger

This reduction packages, in the exact front-B language, what P76.046-P76.047
already isolated heuristically:

```text
SHELL-LOG:
  nested shell cocycle at mu=0;                          (C-13)

MU-DIR:
  directional freezing along the true mu_N path.        (C-14)
```

It also subsumes the coordinate observations of E78.6/E78.7:

```text
the W-package and LOGT-CELL do not create a third front;
they live entirely inside SHELL-LOG at mu=0.             (C-15)
```

So the candid next front-B objects are no longer:

```text
raw W, raw W', or raw J_{L,N} convergence,
```

but precisely the pair `(C-8)` and `(C-9)`.

## 6. Consequence for SAFE-GAMMA-IDENT-CORE

Combining E78.98 with `(C-10)`:

```text
SHELL-LOG(L,K) + MU-DIR(L,K)
=> SAFE-GAMMA-IDENT-CORE on K
```

provided the fixed-`L` limit is then identified with the correct holomorphic
cell/Gamma-prime window functional.

Thus the next admissible front-B attack is:

```text
either prove SHELL-LOG cofinally from the exact nested-section cocycle,
or autopsy the exact coefficient that prevents it;
then handle MU-DIR separately.                           (C-16)
```

## 7. Status

```text
candidate closure - pending review

proved:
  the fixed-L intrinsic core reduces exactly to a shell part at mu=0 plus a
  directional mu-freezing correction;

proved:
  SHELL-LOG + MU-DIR imply intrinsic fixed-L Cauchy convergence of the core;

reduced:
  SAFE-GAMMA-IDENT-CORE to the pair of operational subtargets SHELL-LOG and
  MU-DIR;

clarified:
  the E78.6/E78.7 W-package does not define a new front; it is contained in
  SHELL-LOG at mu=0;

next:
  attack SHELL-LOG directly from the exact nested-shell cocycle, or autopsy
  that route if it again stalls before a cofinal theorem.
```
