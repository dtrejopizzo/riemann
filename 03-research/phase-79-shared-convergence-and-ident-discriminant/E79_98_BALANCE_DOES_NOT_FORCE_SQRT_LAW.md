# E79.98 - Balance alone does not force the zeta-side square-root law

**Scope:** `DISCRIMINANT`, post-E79.97 audit of the balance route.  
**Class:** AUTOPSIA HONESTA.  
**What we know after this document that we did not know before:** the new
square-root coupling from E79.97 is **not** a consequence of balance alone on
the audited ladder.  So the burden cannot be pushed back onto `BAL` by itself.

## 0. Why this check is necessary

E79.97 left the live coupled law as

```text
escape_ratio * sqrt(D_N) ~ const_zeta,                                 (98-1)
```

with the natural next question:

```text
does this already follow from CLOSE + BAL,
or at least from BAL on the rows where geometry is improving?          (98-2)
```

This has to be checked before promoting the square-root law to a new primitive
finite invariant.

## 1. Evidence used

No new build is needed.  This note reads off the already certified long-ladder
data from

```text
E79_89_closure_balance_to_geom_results.json,
E79_90_escape_balance_split_results.json,
E79_91_escape_denominator_results.json.                                (98-3)
```

The relevant comparison is:

```text
sqrtlaw_N := escape_ratio_N * sqrt(D_N).                               (98-4)
```

against the balance diagnostics

```text
R_net,
balance_log_ratio.                                                     (98-5)
```

## 2. Counterpattern from the planted main control

The planted main control is the key witness.

From `N=10` to `N=18`, its balance steadily improves:

```text
R_net:              0.5407, 0.2113, 0.1505, 0.1408, 0.1328,
balance_log_ratio:  1.2104, 0.4291, 0.3033, 0.2834, 0.2672.           (98-6)
```

At the same time the geometric defect also improves:

```text
D_N:  0.01441, 0.01025, 0.00906, 0.00727, 0.00506.                    (98-7)
```

But the square-root law quantity does **not** move toward the zeta regime:

```text
sqrtlaw_N = escape_ratio * sqrt(D_N)
          = 0.198, 0.129, 0.104, 0.112, 0.101,                        (98-8)
```

while zeta sits at

```text
4.818, 4.599, 4.490, 4.656, 4.714, 4.611.                             (98-9)
```

So even on rows where balance is getting much better and `D_N` is shrinking,
the planted build stays smaller than zeta by a factor around

```text
~ 20x to 45x.                                                          (98-10)
```

That is already enough to refute the hoped-for route

```text
BAL  =>  zeta-side square-root coupling.                               (98-11)
```

## 3. Reading

This is exactly parallel to E79.92.

There we learned:

```text
BAL => LOW_DEFECT
```

is too strong and the balance half alone is too permissive.

Now we learn the same thing one level deeper:

```text
BAL
```

also does not force the stronger coupled law

```text
escape_ratio * sqrt(D_N) ~ const_zeta.                                 (98-12)
```

So the zeta-side square-root regime is not just "good balance plus shrinking
defect".  It needs the escape mechanism in an essential way.

## 4. Consequence

After E79.98, the honest picture is:

```text
- BAL helps describe the clean zeta rows;
- but BAL alone does not force either LOW_DEFECT (E79.92)
  or the square-root coupling (here);
- the load-bearing arithmetic content still sits on the escape / closure side. (98-13)
```

So the next admissible target is not

```text
derive the square-root law from BAL.                                   (98-14)
```

It is either:

```text
(a) derive it from CLOSE + the rank-one escape mechanism,
or
(b) name it honestly as the next primitive finite invariant.           (98-15)
```

## 5. Status

```text
proved by audit:
  the planted main control exhibits improving balance and improving D_N while
  remaining far outside the zeta-side square-root regime;

refuted:
  BAL by itself as a forcing route to the E79.97 square-root law;

reduced:
  the live burden to the escape/closure side, not the balance side;

open:
  determine whether CLOSE plus rank-one escape forces the square-root law, or
  whether the law must be promoted to a new primitive invariant.
```
