# E77.7ak - BTG frontier reset

**Run:** 2026-07-18.

## 1. Purpose

After E77.7f--j and the later singular-section cleanup, the LP front was
reduced to two global theorem targets:

```text
LP-BTG side:       FESHBACH-RITZ-ENVELOPE;
LP-interface side: SAFE-DISK-IDENT / BORDERED-WEYL-COMPLETENESS.
```

This note refines the **BTG side** one level further.  The goal is to record
which parts of the Ritz/Feshbach chain are merely reformulations and which
part is the actual smallest unresolved analytic cancellation.

## 2. What the current BTG chain proves exactly

From E77.7g:

```text
LOW-MODE-BTG(K) => BTG-DIV-L.                          (AK-1)
```

From E77.7h (Ritz/Feshbach):

```text
WEIGHTED-FESHBACH-ENVELOPE
+ bracketed low-mode divergence
=> BRACKETED-LOW-MODE-BTG
=> BTG-DIV-L.                                         (AK-2)
```

From E77.7h (cyclic tail):

```text
COFINAL-STIELTJES-TIGHTNESS
=> COFINAL-CYCLIC-TAIL
=> WFE-CYCLIC-TAIL
=> WEIGHTED-FESHBACH-ENVELOPE.                        (AK-3)
```

From E77.7h (shorted shell energy):

```text
SHELL-RESIDUAL-CANCELLATION
=> SHORTED-SHELL-ENERGY
=> SHELL-STIELTJES-INCREMENT
=> COFINAL-STIELTJES-TIGHTNESS.                       (AK-4)
```

So the full proven implication chain already present in the ledger is

```text
SHELL-RESIDUAL-CANCELLATION
=> SHORTED-SHELL-ENERGY
=> SHELL-STIELTJES-INCREMENT
=> COFINAL-STIELTJES-TIGHTNESS
=> COFINAL-CYCLIC-TAIL
=> WFE-CYCLIC-TAIL
=> WEIGHTED-FESHBACH-ENVELOPE
=> BRACKETED-LOW-MODE-BTG
=> BTG-DIV-L.                                         (AK-5)
```

This is crucial: the Feshbach/Ritz object is not isolated.  It already sits
downstream of a more primitive shell/Stieltjes cancellation target.

## 3. What the autopsies killed

The sequence of autopsies removed several tempting but non-admissible
shortcuts:

```text
1. fixed overlap with one ground vector            [E77.7f];
2. Ritz convergence alone as true-mu certificate   [E77.7g];
3. coarse tail bracket on BTG scale                [E77.7h];
4. fixed low-order Lanczos moments                 [E77.7h];
5. tracking named dominant cyclic poles            [E77.7h];
6. separate ||g|| / ||C^*A^{-1}h|| estimates       [E77.7h].
```

Each failure points in the same direction:

```text
the proof must control the paired scalar shell/Stieltjes quantity before
coarse spectral bracketing.
```

That is exactly the P76.061 lesson in BTG form.

## 4. Smallest live BTG object

Therefore the smallest currently admissible unresolved BTG object is not
`FESHBACH-RITZ-ENVELOPE` itself, but the shell-level cancellation underneath
it:

```text
SHELL-RESIDUAL-CANCELLATION:
prove directly that the shell residual

  r_{R,M} = g_{R,M} - C_{R,M}^* A_{R,M}^{-1} h_{R,M}

is small in the shorted pairing

  sum_M <r_{R,M}, S_{R,M}^{-1} r_{R,M}> = o(eta_R)

along a cofinal relation.
```

If this is closed, the downstream Feshbach and BTG statements are already
hooked up by explicit implications `(AK-4)`--`(AK-5)`.

So the candid BTG frontier is:

```text
minimal live object: SHELL-RESIDUAL-CANCELLATION;
downstream reformulations: COFINAL-STIELTJES-TIGHTNESS,
                           WFE-CYCLIC-TAIL,
                           WEIGHTED-FESHBACH-ENVELOPE,
                           BRACKETED-LOW-MODE-BTG.
```

## 5. Why this is better than pushing Ritz directly

Pursuing `FESHBACH-RITZ-ENVELOPE` directly is still legitimate, but it risks
rephrasing the same unresolved cancellation in progressively more spectral
language.

By contrast, `SHELL-RESIDUAL-CANCELLATION`:

```text
1. stays closest to the exact cell/Hilbert/Gamma-prime algebra already
   established in phases 72--77;
2. is paired before any ambient or determinant loss;
3. already explains the observed zeta/planted separation in the measured
   shell windows;
4. has an explicit proven chain to BTG-DIV-L.
```

So if the question is “what is the smallest theorem we still actually need on
the BTG side?”, this is it.

## 6. Consequence for the Omega7 roadmap

The LP segment should now be read as:

```text
SHELL-RESIDUAL-CANCELLATION
=> ... => BTG-DIV-L
```

and independently

```text
SAFE-DISK-IDENT / BORDERED-WEYL-COMPLETENESS
=> SAFE-LIMIT-POINT.
```

Thus the next natural BTG work should target shell residual cancellation
directly, and any future reduced target must imply it or lie below it with an
explicit proof of implication.

## 7. Status

```text
reset:     the smallest live BTG object is SHELL-RESIDUAL-CANCELLATION;
clarified: FESHBACH-RITZ-ENVELOPE is downstream and no longer the minimal
           unresolved theorem;
live:      SHELL-RESIDUAL-CANCELLATION;
downstream: COFINAL-STIELTJES-TIGHTNESS, WFE-CYCLIC-TAIL,
            WEIGHTED-FESHBACH-ENVELOPE, BRACKETED-LOW-MODE-BTG, BTG-DIV-L;
next:      return to the exact shell Schur/cell/Hilbert identities and try to
           prove the residual cancellation theorem-grade.
```
