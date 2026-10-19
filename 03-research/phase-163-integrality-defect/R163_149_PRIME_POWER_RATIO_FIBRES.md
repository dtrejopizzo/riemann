# R163_149 — Rational fibres of the moving graph: prime-power denominators

## Result

The discrete kernel of `R163_148`'s `S_N L_M^*` admits an exact classification by reduced ratios. If `a,b∈ℕ` are coprime and `R_{a,b}=min(⌊N/a⌋,⌊M/b⌋)`, the atom coefficient at `v=log(a/b)` is

```
c_{M,N}(a/b)=1/√(ab) Σ_{r≤R_{a,b}} Λ(br)/r.             (1)
```

For `b>1`:

* if `b` is not a prime power, `c_{M,N}(a/b)=0`;
* if `b=p^j`, `j≥1`, and `R_{a,b}≥1`, then

```
c_{M,N}(a/p^j)
 = (log p)/√(a p^j) Σ_{0≤h≤⌊log_p R_{a,p^j}⌋}p^(−h). (2)
```

In particular, for a **fixed** non-integer ratio and cutoffs `M,N→∞`, the fibre converges to the finite value

```
c_∞(a/p^j)=(log p)/[√(a p^j)(1−1/p)].                (3)
```

For `b=1`, instead,

```
c_{M,N}(a)=a^(−1/2) Σ_{r≤min(M,⌊N/a⌋)}Λ(r)/r,        (4)
```

which diverges as both cutoffs grow. So, among the **fixed rational fibres**, only the integer-ratio ones have unbounded weight. This does not imply convergence of the sum of all non-integer fibres: their supports become dense and `R163_148`'s absolutely continuous polar part must remain in the same distributional limit.

*Proof.* `k/n=a/b` reduced forces `k=ar`, `n=br`. The factor `1/√(kn)` becomes `1/(r√ab)`, giving (1). If `b>1` and `Λ(br)≠0`, `br` is a power of a single prime; hence `b=p^j` and `r=p^h`. This gives (2) and its geometric limit (3). For `b=1`, (4) results. The series `ΣΛ(r)/r` diverges: if it converged, by positivity `ΣΛ(r)r^(−s)` would be bounded as `s↓1`, contradicting `−ζ'(s)/ζ(s)∼1/(s−1)` from ζ's simple pole at 1. ∎

## Euler falsifier at the prime 2

In `R163_147`'s integer model `Z_K=ζ(s)(1−2^(−s))^(−K)`, the prime weight is `a_K(n)=Λ(n)+K log2·1_{n=2^j,j≥1}`. Formula (1) still holds with `a_K` in place of `Λ`. So every non-integer fibre with denominator `2^j` is multiplied exactly by `K+1`, while the fibres with an odd-prime-power denominator do not change. On an integer fibre `a`, the difference relative to ζ is

```
Δc_{M,N}(a)=K(log2)/√a Σ_{1≤h≤⌊log_2 R_{a,1}⌋}2^(−h)
             →K(log2)/√a.                              (5)
```

So the ratio ledger detects the local Euler modification with no recourse to zeros or a spectral sign. But it does **not** rule it out: the modified system also has non-negative fibres and a growing diagonal. The future closing law must pair these fibres with Poisson/Tate and the lattice equality `b_Λ(n)=1`; positivity of rational coefficients is not enough.

## Exact inversion of the Euler coefficients

Let `a(n)` be a weight supported on prime powers, and suppose `Σ_{h≥0}|a(p^{j+h})|p^(−h)<∞` for every `p,j`. Define the fixed exterior fibre amplitude

```
B_{p,j}:=p^(j/2) lim_{M,N→∞} c^a_{M,N}(1/p^j)
        =Σ_{h≥0}a(p^{j+h})p^(−h),                 j≥1.      (6)
```

Then

```
a(p^j)=B_{p,j}−p^(−1)B_{p,j+1}.                          (7)
```

*Proof.* Splitting off `h=0` in (6) leaves `a(p^j)+p^(−1)Σ_{h≥0}a(p^{j+1+h})p^(−h)`, which is (7). ∎

For ζ, every amplitude of a given prime is `B_{p,j}=log p/(1−1/p)` and (7) returns `Λ(p^j)=log p`. For `Z_K`, `p=2`'s amplitudes are multiplied by `K+1`. So the non-integer ledger, **before compressing**, determines the entire local Euler-weight sequence without loss.

This inversion does not resolve the gate: when paired with an autocorrelation `c_F` supported on `[-2T,2T]`, an isolated fibre `1/p^j` with `j log p>2T` is invisible. `AF`'s terms and the aggregated collisions can return information from outside, as in `R163_148`, but (7) alone does not turn it into a first-contact inequality. Moreover, recovering `Λ` from an operator built with `Λ` verifies arithmetic faithfulness; it does not prove a new property of its zeros.

## Limit of the result

Equations (1)–(7) are exact for finite cutoffs or limits of **a single fixed fibre**, as applicable. They do not license summing (3) over every fraction, nor exchanging cutoffs with compression. `R161_021`'s oriented defect is still not identified with a sign form on these fibres. Row D remains open.
