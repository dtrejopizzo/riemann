# R163_133 — Exact Ward defect of the first chamber

**Status:** exact distributional identity for the `κ` models; it identifies the missing term in the two-ledger lift. It proves neither a `(PC-ren)` sign nor closes Row D.

## Computation

Take `R162_103`'s weight `a_κ`: `a_κ(n)=Λ(n)` except at `n=2,3,4`, where `a_κ(n)=κΛ(n)`. On the circle, `Φ_a=Σ_{n≥2}a(n)(ν_n−Leb)` is understood via its Fourier coefficients `Φ̂_a(k)=(a*1)(|k|)` for `k≠0`, with zero mean. Define the Ward defect

```
 D_{a,p}=ℒ_p Φ_a−Φ_a−(log p)(δ₀−Leb),
 D̂_{a,p}(k)=(a*1)(p|k|)−(a*1)(|k|)−log p.    (1)
```

Since `Λ*1=log`, for `k≠0` the perturbation is

```
 (a_κ*1)(k)−log|k|
  =(κ−1)[(log2)1_{2|k}+(log3)1_{3|k}
                         +(log2)1_{4|k}].              (2)
```

Substituting `p=2` and `p=3` in (1), we get the identities **as zero-mean distributions**:

```
 D_{a_κ,2}=(κ−1)(log2)(δ₀−ν₄),
 D_{a_κ,3}=(κ−1)(log3)(δ₀−ν₃).                 (3)
```

Indeed, for `p=2` the difference between the indicators of `2|k` and `4|k` is `1−1_{4|k}`; the `3|k` indicator cancels. For `p=3`, `1−1_{3|k}` remains and both indicators of powers of 2 cancel. The coefficients of `δ₀−ν_q` are precisely `1−1_{q|k}` for `k≠0`, and zero for `k=0`.

For any **finite** perturbation `η=a−Λ` there is a general formula. The map `×p` sends the uniform `n`-torsion measure to the `n/gcd(n,p)`-torsion measure; since `p` is prime, terms with `p∤n` cancel. Hence,

```
 D_{a,p}=Σ_{n:p|n} η(n)(ν_{n/p}−ν_n).           (3a)
```

The sum is finite and exact. In the `κ` case, for `p=2` the edges `2→1` and `4→2` telescope to `4→1`; for `p=3` only `3→1` remains. The edge presentation gives a check for any candidate identity on an arbitrary collar.

## Application to the non-linear test

Let `F` be a primitive vector in the kernel of the `κ` model, and `b=b_{a_κ,F}` from `R163_132`. The test `g=e^b` satisfies `g(0)=1`, `∫g>1`. The complete Ward identity is

```
 ⟨Φ_{a_κ},g(p·)−g⟩
   =(log p)[1−∫g]+⟨D_{a_κ,p},g⟩.                (4)
```

For the chamber's two primes, the missing correction is exactly

```
 p=2: (κ−1)(log2)[1−(g(0)+g(1/4)+g(1/2)+g(3/4))/4],
 p=3: (κ−1)(log3)[1−(g(0)+g(1/3)+g(2/3))/3].       (5)
```

No sign is assigned to those torsional averages: `g(0)=1` and `∫g>1` do **not** order the averages over `ν₃` or `ν₄`. So (5) neither automatically compensates Jensen's sign nor contradicts it.

There is an order difference that makes the coupling checkable. By Möbius inversion, for every integer `n≥1`,

```
 ⟨ν_n,b⟩−∫b=2Σ_{j≥1}b̂(nj)=−2ε w_{A_κ}(n).         (6)
```

More generally, combining (3a) with (6) gives the collar's linear identity, valid for every finite perturbation `η` and its own lift `b_{a,F}`:

```
 ⟨D_{a,p},b_{a,F}⟩
   =−2ε Σ_{n:p|n}η(n)[w_{A_a}(n/p)−w_{A_a}(n)].   (6a)
```

This formula keeps **the same weight `a`** in both the defect and the correlation. It imposes no sign, but it fixes the orientation and every edge endpoint that a computation from `(PC-ren)` should recover.

At contact, `∫b=0`. Applying (5) to `g_r=e^{r²b}` and using `b(0)=0` gives

```
 ⟨D_{a_κ,2},g_r⟩
   =2ε(κ−1)(log2)r² w_{A_κ}(4)+O_F(r⁴),
 ⟨D_{a_κ,3},g_r⟩
   =2ε(κ−1)(log3)r² w_{A_κ}(3)+O_F(r⁴).       (7)
```

By contrast, Jensen's universal term starts at `r⁴` (`R163_131`). So a modification `κ≠1` can introduce a **quadratic** Ward term that dominates the quartic entropy at small scale. The coefficients `w_{A_κ}(3)` and `w_{A_κ}(4)` have no known sign; (7) is a concrete port for comparison with `(PC-ren)`'s terminal jumps, not an inequality.

## What this changes in the gate

The defect `D_{a,p}` is the piece that detects that the compressed operator's weight is not the ordinary cocycle's weight. For ζ (`κ=1`) it vanishes, but a proof of D cannot declare its vanishing *before* deriving a physical identity using the same `a` on both sides: that would reproduce `R163_132`'s decoupling. Formulas (3)–(5) give a precise adversarial test for that future identity: it must produce the `ν₄` and `ν₃` corrections with those coefficients when the first chamber is modified. If it omits them, the identity does not preserve the arithmetic ledger.

This atom localization does not contradict `R162_1101 Thm 2.2`: there, the Gamma residues of a standard meromorphic kernel concentrate at the identity atom; here we only compute a regular cocycle defect for a fixed test, without moving a Gamma pole to `ν₃` or `ν₄`.
