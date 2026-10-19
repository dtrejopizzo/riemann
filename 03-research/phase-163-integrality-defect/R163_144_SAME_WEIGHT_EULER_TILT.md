# R163_144 — Single-weight Euler tilt: positive variance in Gamma, factor `A` in physics

**Status:** exact deformation family and curvature computation for `R163_143`. The positive result lives at the Gamma points; its pullback to the physical kernel remains open. Does not close Row D.

## 1. Family of quotients of the same product

Under `R163_143`'s hypotheses, for a parameter `u` near zero, define

```
 r_{a,u}(n)=Σ_{d|n}μ_a(d)b_a(n/d)(n/d)^(−u).
```

For `Re z>1` and `Re(z+u)>1`, the Dirichlet convolution gives exactly

```
 Σ_{n≥1}r_{a,u}(n)n^(−z)=Z_a(z+u)/Z_a(z).       (1)
```

Differentiating at `u=0`,

```
 r_{a,0}=δ_1,
 r'_{a,0}=−a,
 r''_{a,0}=W_a:=a·log+a*a.                    (2)
```

The first identity is `μ_a*b_a=δ_1`; the second is `μ_a*(b_a·log)=a`; the third follows from `Z_a''/Z_a=(Z_a'/Z_a)' +(Z_a'/Z_a)²` and keeps all of `a*a`'s cross terms. For `a=Λ`, `W_a` is `R163_135`'s Selberg weight.

`R163_143`'s physical port is now written unambiguously as

```
 B_a^Eul(u)=−εΣ_{n≥1}r_{a,u}(n)w_{a,F}(n),       (3)
```

so that (2) reproduces its selector, first jet and second jet. By contrast, the lattice port replaces `b_a(n/d)` with `1`; both are identical for ζ and differ for `κ`.

## 2. Probabilistic positivity exactly where Euler converges

If `b_a(n)≥0` and `Z_a(x)>0` for `x>1`, the measure

```
 P_{a,x}(n)=b_a(n)n^(−x)/Z_a(x)
```

is a probability. For `u≥0` and `x>1`, (1) is its Laplace transform in `L(n)=log n`:

```
 Z_a(x+u)/Z_a(x)=E_{P_{a,x}}[e^(−uL)]∈(0,1]. (4)
```

The second logarithmic derivative at zero is the variance

```
 d²/du² log[Z_a(x+u)/Z_a(x)]|_{u=0}
   =Var_{P_{a,x}}(L)
   =Σ_{n≥2}a(n)(log n)n^(−x)≥0.             (5)
```

The raw second moment is

```
 E_{P_{a,x}}[L²]=Σ_nW_a(n)n^(−x)≥0.        (6)
```

These identities hold in particular at `x=s_m=2m+1`, where `R163_143`'s Gamma tail sees the factors `Z_a(s_m+u)/Z_a(s_m)`. For ζ, (5) simultaneously uses the Euler product, `Λ*1=log` and the positivity of the exact measure `n^{-x}/ζ(x)` on the ordinary integers.

## 3. Why the sign does not reach contact

The positivity of (4)–(6) is a **scalar statement for `x>1`**. The physical object (3) is not `Σ_mK_m(F)² Z_a(s_m+u)/Z_a(s_m)`; it is the cross pairing of `F` with `A_aF` sampled at displacements `log n`. At a contact `P A_aF=0`, the primitive interior part vanishes, but `R163_139`'s Tate and exterior ports survive; `R163_140` explicitly computes the second jet's rational collisions. Removing `A_a` or replacing the physical port with (6)'s positive energy would be exactly the unjustified pullback of `R161_068 §4` and `R161_016`.

The `κ` models likewise have `b_{a_κ}(n)>0` and satisfy (4)–(6) in their Euler region, while having non-trivial kernel contacts. Their failure against ζ lies in `R163_143`'s lattice–Euler coincidence, not in positive variance. So a closing proof must use that coincidence **inside an oriented, compression Poisson–Tate identity**, not merely assert that the tilt is contractive at each Gamma point.
