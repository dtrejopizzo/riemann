# 107.110 -- Same bad-prime profile global no-go

## 1. Purpose

`107_108` and `107_109` already isolate a local obstruction:
if a putative local comparison still factors through a source signature
that is too coarse, then distinct pinned real local target states must
collapse.

This note records the corresponding finite global obstruction.
Even if one moves from a single local row to the whole finite set of bad
primes of an actual elliptic curve over \(\mathbf Q\), a source package
that sees only the bad-prime profile still cannot recover the real local
target atlas.

## 2. Real curves used here

The verifier `107_110_same_bad_prime_profile_global_no_go.py` uses the
following two genuine elliptic curves over \(\mathbf Q\):

1. `14.a1`, whose conductor is \(14=2\cdot7\), with pinned local row
   at \(p=2\) of type \(I_9\), \(c_2=1\), nonsplit multiplicative;
2. `14.a5`, whose conductor is also \(14=2\cdot7\), with pinned local
   row at \(p=2\) of type \(I_2\), \(c_2=2\), nonsplit multiplicative.

So the two curves have the same finite bad-prime support

\[
 \{2,7\},
 \]

but already differ on the visible local target state at one bad prime.

## 3. Exact no-go statement

The verifier defines the coarse finite global source profile

\[
 G(E)=\{\text{bad primes of }E\}.
 \]

On the pinned pair it checks exactly:

1. both curves have the same conductor \(14\), hence the same bad-prime
   profile \(G(E)=\{2,7\}\);
2. the pinned visible local target signatures at \(p=2\) are distinct;
3. therefore any finite global comparison map that factors only through
   the bad-prime profile \(G(E)\) cannot recover even the pinned
   \(p=2\) local target state faithfully on this pair.

So the exact obstruction is:

\[
 \text{same finite bad-prime profile}
 \centernot\Longrightarrow
 \text{same real local target atlas}.
 \]

## 4. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All same bad-prime profile global no-go checks passed.
```

So the workspace now contains a finite global obstruction, not only a
pointwise local one.

## 5. What this proves and what it does not

This witness proves a narrow but useful point:

1. even knowing the full finite set of bad primes of an actual elliptic
   curve is still far coarser than knowing its real local target atlas;
2. the local obstructions already isolated in `107_108` and `107_109`
   do not disappear when one passes to a coarse finite global profile;
3. any future global finite-support realization claim in Phase 107 must
   carry more than the mere list of bad primes if it aims to recover
   actual local target data.

It does **not** prove:

1. that every global source package built in Phase 107 factors only
   through the bad-prime profile;
2. that no richer finite global package could distinguish this pair;
3. any global realization theorem, the terminal identity, or RH.

So the correct reading is:

\[
 \text{same bad-prime profile global no-go exact-checked},
 \qquad
 \text{full refined global realization problem still open}.
 \]
