# R163_110 — Logical audit of the discrete BF threshold

**Status:** logical correction proved; excluding thresholds `>1/3` additionally uses the internal proof `R163_103`, pending external review. **Paper 48 was not edited.**

## 1. What threshold would actually imply RH

Problem 6 of paper 48 asks whether there exists `θ₀>0` such that every discrete Beurling system with

```
N(x)=ρx+O(x^θ),    θ<θ₀,
```

has all its zeros at `Re s>θ₀` on `Re s=1/2`. Since `N_ζ(x)=⌊x⌋=x+O(1)`, the system of ordinary integers belongs to the class for any `θ₀>0`.

However, **applying the conclusion only to ζ gives RH if `0<θ₀≤1/2`, not if `θ₀>1/2`**. In the first range, any off-line zero has, by symmetry, one with `Re ρ>1/2≥θ₀`, which the conclusion forbids. If `θ₀>1/2`, the conclusion allows zeros in `1/2<Re ρ≤θ₀` and their reflections: it does not imply RH. This is a correction to problem 6's phrase "a positive answer at any `θ₀>0` gives RH"; there could be an additional class reduction for `θ₀>1/2`, but it is neither formulated nor proved there.

## 2. Range already falsified by phase 163's discrete systems

The internal proof `R163_103`, if it survives the pending external review, supplies, for every `1/3<η<1/2`, a discrete system with error `O_ε(x^{η+ε})` and zeros at

```
β=(1+η)/2.
```

For every `1/3<θ₀≤1/2`, choosing `η∈(1/3,θ₀)` and `ε>0` with `η+ε<θ₀` gives `β>θ₀`; hence it refutes the universal BF statement for those thresholds. For `1/2<θ₀<3/4`, one can choose `η∈(max(1/3,2θ₀−1),1/2)` with `η+ε<θ₀`, which again gives `β>θ₀`. For `3/4≤θ₀<1`, Broucke's discrete construction for `η>1/2` supplies the falsifier, as detailed in `R163_103 §5`.

So, **conditional on `R163_103`'s validity**, any universal BF of the stated form with the power to imply RH would have to have

```
0<θ₀≤1/3.                                             (1)
```

The endpoint `θ₀=1/3` is not refuted by the bound `O_ε(x^{1/3+ε})`: it does not supply an exponent `θ<1/3`. The interval `0<θ₀<1/3` is likewise not decided here.

## 3. Scope for building D

The BF route is significantly more rigid than its initial statement suggests: it must prove a law for **all** of a discrete class with error strictly better than `x^{1/3}` (or at the exact endpoint), not only for ζ. The `Q(i)` example of `R163_104` shows that `θ₀=1/3` would also include the Dedekind zeta of the Gaussian integers and would give GRH for `L(s,χ_{−4})`.

None of this proves or refutes the specific law for ζ that would close D. It does avoid two invalid inferences: using a threshold `>1/2` as if it excluded all off-line zeros of ζ, and presenting `R163_103`'s examples as a refutation of the strict endpoint `θ₀=1/3`.

**Recommended correction for paper 48, once touching it is authorized:** replace "any `θ₀>0` gives RH" with "any `0<θ₀≤1/2` gives RH by direct application to ζ," and record that the plausible range after `R163_103` is `0<θ₀≤1/3`, subject to review of the new theorem.
