# E78.100 - Autopsy of the `SHELL-LOG` route

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` core.  
**Class:** AUTOPSIA theorem-grade.  
**What we know after this doc that we did not know before:** the exact reason
the fixed-`L` shell route has not produced a cofinal theorem is that its
invariant residual hierarchy does not stop at a stable `1/N` or `1/N^2`
coefficient; the currently certified obstruction is the unresolved `N=2 mod 4`
spike in the signed second-profile quantity `Q_N`, so the numerical heuristic
`|J_{L,N+1}-J_{L,N}| <= C_K L^2/N^2` has no theorem-grade support from the
closed cocycle chain presently available.

## 0. Wall checklist

```text
MW-1:  respected.  No positivity/Weil form is introduced.
MW-2:  respected.  This is a fixed-L shell autopsy; no arithmetic is pushed
       outside Re(s)>1.
MW-3:  respected.  No local-global infinite-dimensional assembly.
MW-4:  respected.  No wrong-sign lower-bound mechanism is used.
MW-5:  respected.  No site/cohomology input.
MW-6:  respected.  No uniform spectral-gap hypothesis.
K1-K5: respected.  No ambient inverse norm, no absolute pre-cancellation bound,
       no scalar determinant endpoint identification.
P76.061: respected.  Every cited live object is a paired transfer/Cauchy shell
         quantity before inversion.
E72.16/E77.7az: respected.  No LP detector is imported; this is an IDENT-front
                autopsy only.
```

## 1. The route that looked promising

P76.046-P76.047 recorded the numerical fixed-`L` heuristic

```text
|J_{L,N+1}(0)-J_{L,N}(0)| <= C_K L^2/N^2,                (S-1)
```

which would imply a fixed-`L` tail `O_K(L^2/N)` by summation.  In E78.99 the
front-B core was reduced to

```text
SHELL-LOG(L,K):
  sup_K |J_{L,N}(0)-J_{L,M}(0)| -> 0                    (S-2)
```

plus the separate `MU-DIR` term.  So `(S-1)` would indeed be enough to close the
shell part if it were proved.

The question is whether the exact invariant cocycle chain actually supports
`(S-1)`.

## 2. What the exact cocycle chain really proves

The exact fixed-`L` shell object is not a raw transfer increment; by E77.5l it
is the signed residual

```text
R_N(sigma)
 := Delta external_N(sigma) - Delta logT_N(sigma),      (S-3)
```

which is partition-invariant and exact.

The certified chain then proceeds:

```text
raw summability of R_N          -- refuted by E77.5m;
leading 1/N coefficient C_N     -- does not stabilize, E77.5n;
profile drift D_N=C_N-C_{N+2}   -- still visible, E77.5o;
single second coefficient Q_N   -- does not stabilize, E77.5p;
mod-4 split                     -- only the N=0 mod 4 branch is tame,
                                   E77.5q.                                (S-4)
```

More explicitly:

```text
C_N(sigma) := N R_N(sigma),                             (S-5)
D_N(sigma) := C_N(sigma)-C_{N+2}(sigma),               (S-6)
Q_N(sigma) := N^2 D_N(sigma).                          (S-7)
```

E77.5m shows that `R_N` still carries a visible `1/N` term.  
E77.5n shows that the coefficient profile `C_N(sigma)` drifts with `N`.  
E77.5o shows the drift itself is still of `N^-2` size.  
E77.5p shows the “second coefficient” `Q_N` does **not** stabilize.  
E77.5q shows only one mod-4 branch looks tame, while the `N=2 mod 4` branch
still develops a late spike.

So the invariant shell hierarchy does not close at the level needed for `(S-1)`.

## 3. The exact coefficient that fails

The currently named unresolved coefficient is:

```text
MOD2-SPIKE-CELL:
the N = 2 mod 4 spike in Q_N(sigma)
 = N^2 [ C_N(sigma)-C_{N+2}(sigma) ].                  (S-8)
```

This is not a vague “higher-order effect”; it is the exact quantity left alive
by the whole certified shell hierarchy.

E77.5q records the obstruction concretely:

```text
zeta, sigma=3.0, mod 2 branch:
Q = 0.3605, -0.4157, 3.5575.                            (S-9)
```

The theorem-grade reading is:

```text
there is currently no proved asymptotic statement forcing
Q_N(sigma) to remain uniformly bounded, let alone converge,
on the N = 2 mod 4 branch.                             (S-10)
```

Without `(S-10)`, the route to an `N^-2` shell bound `(S-1)` is not supported by
the exact cocycle chain.

## 4. Why the heuristic `|Delta J| <= C L^2/N^2` is not yet a theorem target

The numerical pattern in P76.046-P76.047 is compatible with `(S-1)`, but the
exact invariant reductions show that proving `(S-1)` requires more than the
observed size of a few shell increments.

The live obstruction is not “small noise” but the unresolved branch-sensitive
coefficient `(S-8)`.  Therefore the exact quantifier that fails is:

```text
there is no proved statement of the form
  exists C_K, N_0 such that
  |J_{L,N+1}(0)-J_{L,N}(0)| <= C_K L^2/N^2
for all N >= N_0 and sigma in K,                       (S-11)
```

because the current reductions never produce a stabilized second coefficient on
the full even ladder.

## 5. Consequence for the front-B program

By Rule 2 of the mission, `SHELL-LOG` has reached an autopsy point: the current
toolchain has not yielded a cofinal theorem, and the exact surviving
obstruction is already named.

So the honest conclusion is:

```text
the present shell-cocycle route to SHELL-LOG is exhausted.  (S-12)
```

This does **not** refute `SHELL-LOG` itself.  It refutes the current closure
mechanism:

```text
P76.046 heuristic
=> R_N hierarchy
=> coefficient stabilization
=> summable shell increments.                          (S-13)
```

The chain stops at `MOD2-SPIKE-CELL`.

## 6. What remains alive after this autopsy

E78.99 already split the fixed-`L` core into

```text
SHELL-LOG + MU-DIR.                                    (S-14)
```

The present document shows that the **current shell route** toward the first term
is stalled at `(S-8)`.  Therefore the next admissible front-B work should be:

```text
1. a new exact mechanism for SHELL-LOG that does not pass through the
   coefficient hierarchy R_N -> C_N -> D_N -> Q_N; or
2. move to MU-DIR / direct holomorphic core identification while leaving
   the shell hierarchy archived as an exhausted route.  (S-15)
```

Given the mission order and the fact that the goal is `SAFE-GAMMA-IDENT`
direct, option 2 is the honest next move.

## 7. Predecessor implication / closure status

This autopsy closes the current shell route, not the theorem itself.

If a future mechanism proved

```text
SHELL-LOG(L,K),                                         (S-16)
```

then E78.99 would still give

```text
SHELL-LOG + MU-DIR => SAFE-GAMMA-IDENT-CORE.            (S-17)
```

The present document proves only that the existing cocycle/coefficient route does
not currently supply `(S-16)` because it stops at the unresolved branch spike
`(S-8)`.

## 8. Status

```text
candidate closure - pending review

proved:
  the current shell hierarchy for the fixed-L core reduces exactly to the
  unresolved branch-sensitive coefficient Q_N on the N=2 mod 4 branch;

proved:
  the numerical heuristic |Delta J| <= C_K L^2/N^2 is not supported by a
  stabilized coefficient theorem in the closed cocycle chain presently
  available;

autopsied:
  the current SHELL-LOG route is exhausted at MOD2-SPIKE-CELL;

next:
  leave the shell coefficient hierarchy archived as an exhausted route and
  move the front-B effort to MU-DIR / direct holomorphic core identification.
```
