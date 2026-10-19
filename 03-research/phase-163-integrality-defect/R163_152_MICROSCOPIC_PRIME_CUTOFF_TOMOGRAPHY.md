# R163_152 — Microscopic tomography of the Euler weights in `(PC-ren)`

## Motivation and scope

The proportional cutoff `M=αN` of `R163_150`–`151` averages `Λ` and keeps only Euler–Maclaurin's universal term. To retain the exact arithmetic, one must look at the **unit** step `M=n−1→n`. This note computes that step on the physical primitive space. It is an identity faithful to the Euler weight, not a proof of the Weil sign.

Let `a(m)` be a real weight on the integers (`a(1)=0`), `L_M^a=Σ_{m≤M}a(m)m^(−1/2)τ_{log m}` and `A_M^a=M_Γ−L_M^a−(L_M^a)^*`. The comb `S_N^ren` remains the **ordinary** one, with multiplicity one at each integer. Let `F∈C_c^∞([-T,T])` be non-zero and primitive, and `c_F(v)=∫overline{F(t)}F(t+v)dt`.

## Theorem — Exact jump of a weight

For `n>e^(2T)` define the known quadrature error

```
D_n(F)=Σ_{k≤n} k^(−1/2)c_F(log(k/n))
       −∫_0^n x^(−1/2)c_F(log(x/n))dx.                (1)
```

Then, at a **finite cutoff**,

```
⟨F,S_n^ren(A_n^a−A_{n−1}^a)F⟩
 =−a(n)n^(−1/2)D_n(F).                              (2)
```

Moreover,

```
D_n(F)=||F||²/(2√n)+O_F(n^(−3/2)).                  (3)
```

Consequently `D_n(F)>0` for every sufficiently large `n`, and the physical observable determines exactly the individual weight:

```
a(n)=−√n ⟨F,S_n^ren(A_n^a−A_{n−1}^a)F⟩/D_n(F).    (4)
```

*Proof.* `A_n^a−A_{n−1}^a=−a(n)n^(−1/2)(τ_{log n}+τ_{−log n})`. In the reflected channel, commuting translations with `S_n^ren` gives exactly `−a(n)n^(−1/2)D_n(F)`. In the forward channel, the discrete comb only produces translations `log(kn)>2T`, and its pairing with `F` is zero. The continuous part, with `v=log(xn)`, is `a(n)/n ∫e^(v/2)c_F(v)dv`, which vanishes by the two Tate moments, as in `R163_151 (4)`. This proves (2). For (3), apply second-order Euler–Maclaurin to `f_n(x)=x^(−1/2)c_F(log(x/n))`, supported below `x=n` only on `[ne^(−2T),n]`; its value at `n` is `||F||²/√n`, its first and second derivatives have uniform orders `n^(−3/2)` and `n^(−5/2)`, and the integrated remainder is `O_F(n^(−3/2))`. Eventual positivity and (4) follow. ∎

## Exact Euler and falsifiers

For ζ, `a(n)=Λ(n)`. By (4), the physical jumps recover `log p` at **every** sufficiently large `n=p^j` and zero at every other integer. The identity `Λ*1=log` becomes an exact relation among these observables once the finitely many indices below the threshold are included:

```
Σ_{d|m} a(d)=log m.                                  (5)
```

By Möbius inversion, (5) for every `m` characterizes `a=Λ`. Here (5) is a faithfulness check of the physical ledger, **not** a new proof of the arithmetic identity nor a law about zeros.

In `R163_147`'s `Z_K` model, the jump at every high power of 2 is `K+1` times ζ's, and the rest of the prime-power jumps are unchanged. Epstein/Davenport–Heilbronn offer no ordinary Euler weight `a` whose divisor sum is `log`; Beurling systems with non-integer primes do not share (1)'s ordinary comb. So the tomography distinguishes the falsifiers at the level of the **input datum**, but does not exclude them spectrally: formula (2) holds for any `a` and never uses the functional equation or first contact.

## Consequence for the gate

The cutoff analysis identifies two scales. With `M/N→α>1`, `R163_151` sees only the average density and returns `Q₀`; with a jump `M=n−1→n`, (2) preserves the individual Euler weight and the comb's multiplicity one. An identity closing D must **sum or couple these microscopic jumps before the limit**, together with the Poisson–Tate orientation and the polar collars, so that (5) enters the step fixing the sign. Summing (2) directly only reconstructs `A_M^a` and would be tautological. That additional oriented relation has not been obtained; D remains open.
