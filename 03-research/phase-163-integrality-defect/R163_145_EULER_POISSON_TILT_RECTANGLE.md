# R163_145 — Euler–Poisson rectangle of the tilt: oriented identity and κ defect

**Status:** exact meromorphic identities and a computed falsifier. The functional equations used are classical; what is new here is their explicit coupling with `R163_143`'s two ports and `R163_144`'s tilt. There is no transfer of positivity to the compression, so Row D remains open.

## 1. Euler outward, Poisson back

On a safe half-plane, and then by meromorphic continuation, define for ζ

```
 T(s,u)=ζ(s+u)/ζ(s),
 Γ(s,u)=χ(s+u)/χ(s),
 χ(s)=2^sπ^(s−1)sin(πs/2)Γ(1−s).
```

The functional equation `ζ(s)=χ(s)ζ(1−s)` gives the **exact rectangle**

```
 T(s,u)=Γ(s,u) T(1−s,−u).                   (1)
```

The quotients are read meromorphically at the zeros; it is not claimed they are bounded operators on the critical line. (1)'s first edge is the Euler product's tilt; the second is the Poisson–Tate reflection with its Gamma factor. `T(s,u)`'s Dirichlet coefficients are `R163_144`'s `r_{Λ,u}`, and for ζ they coincide with `R163_143`'s lattice port's because `b_Λ(n)=1`.

## 2. First and second order: orientation preserves the cross terms

Let, where the expressions are meromorphic,

```
 L(s)=−ζ'(s)/ζ(s)=Σ_nΛ(n)n^(−s),
 W(s)=ζ''(s)/ζ(s)=Σ_n[Λ·log+Λ*Λ](n)n^(−s),
 g_1(s)=χ'(s)/χ(s),
 g_2(s)=χ''(s)/χ(s).
```

The expansion `T(s,u)=1−uL(s)+u²W(s)/2+O(u³)` in (1) gives the oriented equalities

```
 −L(s)=g_1(s)+L(1−s),
 W(s)=g_2(s)+2g_1(s)L(1−s)+W(1−s).         (2)
```

The cross term `2g_1L(1−s)` is mandatory: squaring only the first equality, or treating Euler and Gamma separately, does not reproduce the second order. (2) is the meromorphic form, **in a single step**, of the sum×product mixture that `R163_135` sees as the second jet. It does not by itself imply a sign, since `L` and `W` are already continued outside their positive half-plane.

## 3. κ falsifier on the same edge

For `R163_143`'s `Z_{a_κ}(s)=ζ(s)e^{δH(s)}`, `δ=κ−1` and `H(s)=2^(−s)+3^(−s)+½·4^(−s)`, define `T_κ(s,u)=Z_{a_κ}(s+u)/Z_{a_κ}(s)`. (1)'s **exact** failure is

```
 T_κ(s,u)/[Γ(s,u)T_κ(1−s,−u)]
   =exp{δ[H(s+u)−H(s)
             −H(1−s−u)+H(1−s)]}.           (3)
```

At `s=1/2`, the linear coefficient of its logarithm is

```
 2δH'(1/2)
 =−2δ[(log2)/√2+(log3)/√3+(log2)/2]≠0
                                                (δ≠0). (4)
```

This distinguishes the `κ` model **in the Poisson orientation**, in addition to `R163_143`'s multiplicity/pole defect and `R163_133`'s torsional Ward defect. `Φ_Λ` was not inserted externally into an operator `A_κ`: the same `Z_{a_κ}` appears on both sides of (3).

## 4. What is missing upon compression

For `x=2m+1>1`, `T(x,u)` is a Laplace transform of a probability and its curvature is positive (`R163_144`). Meromorphic identity (1) transports the **analytic value**, not the order of positivity, up to `s=1/2+iτ`. There, ζ has zeros, the Gamma factor changes the metric, and the compression `P_T` produces Tate and exterior ports (`R163_139`–`140`). The fact that (2) is exact for ζ does not prove that the first-contact state annihilates `R163_136`'s reflection defect `ℛ_F(−2m)`: (1)–(2) hold for every `F` and do not even contain `F`.

A closing construction must lift (1) **before compressing** into an identity of physical pairs over `F`, preserve `R163_137`–`138`'s Euler–Maclaurin corrections, `R163_140`'s rational collisions and defect (3) in modified models. Only then could one ask whether the equality `P_T A_Λ P_T F=0` forces a strict comparison of the Gamma energies. That oriented lift was not obtained.

## 5. Audit of the even channel on the critical line

At `s=1/2+iτ` away from the zeros, `1−s=conj(s)` and, by reality of the coefficients, `L(1−s)=conj(L(s))` and `W(1−s)=conj(W(s))`. (2)'s first equality fixes `Re L(s)`. The second has on the left `W(s)−conj(W(s))=2i Im W(s)`; **it does not fix `Re W(s)`**, the curvature component one would try to use as a sign. Consequently, the scalar rectangle transports the odd orientation of the reflection but does not create an inequality in the even channel.

An exact algebraic falsifier of any argument based solely on the functional equation is `Z_c(s)=ζ(s)exp(c(s−1/2)²)`, `c∈ℝ`: it satisfies the same reflection `Z_c(s)=χ(s)Z_c(1−s)` because the added factor is symmetric. However, at `s=1/2`, where `ζ(s)≠0`, its raw curvature satisfies

```
 Z_c''(1/2)/Z_c(1/2)
     =ζ''(1/2)/ζ(1/2)+2c.                      (5)
```

The sign can be changed arbitrarily without breaking the reflection. This `Z_c` does **not** have ζ's ordinary Euler product nor its Dirichlet normalization; so it does not refute an identity using both exact arithmetic and `(PC-ren)` together. It does prove that the sign piece must come from the additional physical-arithmetic coupling, not from (1)–(2) alone.
