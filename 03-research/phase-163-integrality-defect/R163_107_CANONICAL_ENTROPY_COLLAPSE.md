# R163_107 — Audit of the canonical test: torsional entropy sees only the norm

**Status:** exact identity proved; **NO-GO for coupling `R163_106` to first contact via the canonical Möbius lift**. Row D remains open. Main entries: `R162_1001` Prop. 3.2 and paper 48, §torsion.

## 1. Calculation that decides the first gate

Let `F` be a window test, `c_F` its autocorrelation and `w_F(n)=n^{-1/2}c_F(log n)`; then `w_F(1)=c_F(0)=||F||²`. The trigonometric test of `R162_1001` has coefficients, for `k≠0`,

```
ĥ_F(k)=Σ_{j≥1} μ(j)w_F(|k|j),       ĥ_F(0)=0.
```

The sums are finite because of `c_F`'s support. By Möbius inversion,

```
Σ_{k≥1} ĥ_F(k)
 = Σ_{n≥1} w_F(n) Σ_{j|n} μ(j)
 = w_F(1)=||F||².
```

Since `h_F` is real and even,

```
h_F(0)−∫_T h_F = Σ_{k≠0}ĥ_F(k)=2||F||².              (1)
```

The factor `2` follows the symmetric `±k`-frequency convention; if `h_F` is rescaled to absorb it, the invariant conclusion is the same: the defect is a positive constant times `||F||²`, **not** `W_T(F)` nor `λ_A(T)`.

## 2. Consequence for the exponential

Plugging `g=e^{ηh_F}` into `R163_106`'s identity gives

```
E_p(ηh_F)=(log p)[e^{ηh_F(0)}−∫_T e^{ηh_F}]
          =2η(log p)||F||²+O_F(η²).                    (2)
```

For `F≠0`, the linear term does not vanish when `F` is a radical vector at first contact: it depends only on the norm. Its sign flips when `η` is replaced by `−η`, both for `λ=0` and for eigenvectors `λ>0`. So `R163_106 (2)`'s quadratic Jensen coercivity does **not** naturally appear at contact.

One could remove the first order by subtracting a first harmonic from the test, e.g. `h_F−2||F||² cos(2πx)`. Then the value at `0` and the mean coincide and Jensen gives a strict sign, but it does so for **every** `F≠0`. This correction uses no `PC-ren`, Poisson, Gamma poles, compression or first contact: it is an artificial normalization, not a closing mechanism.

If the `n=1` term is omitted before taking the lift, the same count gives `h(0)−∫h=0` for every `F`, again without using contact. So neither of these two canonical normalizations supplies the selective condition demanded in `R163_106 §3(1)`.

The same obstacle does not depend on choosing the exponential. For any function `φ` analytic near `0` and small `η`, the cocycle applied to `φ(ηh_F)` has the exact series

```
(log p) Σ_{r≥1} φ^{(r)}(0)η^r/r! ·[h_F(0)^r−∫h_F^r].
```

The linear coefficient is `2φ′(0)(log p)||F||²`; choosing `φ′(0)=0` makes it vanish **for every vector**, not only for `ker H_{T_*}`. So a pointwise analytic composition of the canonical lift, absent a new identity connecting the higher moments with `(PC-ren)` and contact, does not by itself introduce the `λ=0` selector.

## 3. Arithmetic reading and falsifiers

The map `w↦h_w` reads every prime when `h_w` is paired with `Φ_Λ`, but the `×p` cocycle applied to `h_w` collapses the first order to `w(1)`. In the autocorrelation lift, that datum is just `||F||²`. It is the analogue, for the torsional exponential, of the localization at the identity atom noted by `R162_1101` for the polar residue.

- Calculation (1) does not use ζ or the functional equation: it holds for the witnesses of `M_m`, `Λχ_2`, Epstein or the Type I curve when the same lift is formed. So it fails S1 (essential use of `λ=0`) and, as a bridge, S4.
- `R163_106`'s exact identity remains valid; what is ruled out is **this natural coupling** to contact, not every possible non-linear construction with a new kernel.
- Reopening the route would require an `h_{F,s}` with a meromorphic profile and Gamma/exterior corrections such that its functional `h(0)−∫h` reduces neither to `w_F(1)` nor to a hand-imposed harmonic adjustment. No such object is built here.

**Verdict:** do not use `R163_106`'s entropic coercivity as a proof of D. The canonical lift has a strictly positive first-order defect independent of first contact; removing it by hand produces a universal sign empty of content for RH.
