# R163_129 — Audit of the crossed lift: selector yes, orientation no

**Status:** audit of `R163_127`–`128`. The contact and tail identities are correct; they **do not** constitute the signed `(PC-ren)` bridge. Row D remains open.

## 1. What survives

For `A=M−C` extended to the line, `F` primitive and real, and `h_A` defined by `R163_127`, the following hold:

```
h_A(0)−∫h_A=2⟨F,H_TF⟩,                          (1)
−εĥ_A(k)=Σ_m K_m(F)²/[ζ(2m+1)k^(2m+1)]>0
                                  (k>e^(4T), F≠0). (2)
```

At a first contact, (1) annihilates the first order **without adjusting the test**, and (2) guarantees `h_A≠0`. These are genuine improvements over `R163_107`'s autocorrelation lift.

## 2. What does not survive as a closing argument

The `Φ_Λ` cocycle applied to `e^{h_A}` gives a strict negative sign on the radical. However, the cocycle identity is a distributional identity **for any test** (`R162_1101 §3.3`); it does not by itself impose a condition on `F`. If formally `A↦−A`, then `h_A↦−h_A`, and on the radical both quantities

```
1−∫e^{h_A},     1−∫e^{−h_A}
```

are strictly negative by Jensen. So the isolated entropic sign **does not orient Weil's sign**. The selective use of `λ=0` in (1) resolves F1, but not F2. A closure still needs the *other* half of the comparison to carry the Poisson–Tate orientation and to fail when `A`'s sign is flipped.

Nor does `h_A` contain a meromorphic family `g_{F,s}` with Gamma poles. Tail (2) exhibits the moments, but does not transfer `ζW^0`'s residue to a non-trivial torsional atom. The NO-GO of `R162_1101 Thm 2.2` localizes the residue of the standard torsional kernels at the identity atom. Identities (1)–(2) **do not** prove the crossed lift avoids that localization: they only show the fixed test contains Gamma data outside the window.

## 3. Exact reappearance of the extra factor `A`

The linear part of the torsional pairing is

```
⟨Φ_Λ,h_A⟩=2Σ_{n≥2}Λ(n)n^(−1/2)c_A(log n).     (3)
```

Since `c_A(v)=⟨F,τ_v AF⟩`, (3) is the Euler comb applied to **`AF`**, not to `F`. It is the same operator obstacle audited in `R161_068 §4`: `H_TF=0` does not annihilate an exterior observable of `AF`, and removing `A` would require inverting it on the kernel. Möbius inversion and the positive tail do not eliminate that factor.

## 4. The exact gate that remains

A valid continuation must build a signed identity from `(PC-ren)` with the polar/Tate collars and physical compression, relating the **non-linear test** `e^{h_A}` to a geometric energy of the opposite sign. It will have to explicitly show why that identity fails for deletion, `M_m`, `Λχ_2`, Epstein/DH and Beurling. The cocycle's tautology or the linear pairing (3) are not enough.

**Verdict:** `R163_127` is a faithful contact selector, not a partial closure of the sign. `R163_128` localizes a finite Fourier compensation, but `(G_K)` remains of RH strength and is unproved. The next action is not to iterate the cocycle: it is to find a non-separable physical family or a compression inequality supplying the missing orientation.
