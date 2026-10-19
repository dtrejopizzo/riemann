# R161_015 — Canonical Hardy gauge and the exact norm-slope form of the last inequality

## 0. Verdict

The compactly supported polar profile used to establish existence in `R161_008` is unsuitable for a metric
variation: its profile is arbitrary, while the derivative of a port norm depends on that profile.  There is a
canonical replacement.  In the `s` variable choose

```
Theta_T(s)=exp(-T(s-1))/s,             Theta_T(1)=1.               (0.1)
```

This is the shifted Hardy reproducing-kernel gauge at the zeta pole.  It is causal from the endpoint `T`, preserves
all nontrivial-zero critical values, and is fixed before moving the contour.

For the resulting corrected product port, the Sonin--Gamma excess of `R161_014` is exactly minus the right derivative
of its endpoint-normalized Hardy norm.  Thus the final upper balance is equivalent to a one-sided minimum theorem
for one explicit norm family.

## 1. Canonical polar subtraction

Write `z=s-1/2` and let

```
G_+(s)=-zeta'(s)K_F(s-1/2)-zeta(s)Q_(+,T)(s-1/2).                 (1.1)
```

Its only right-half-plane singularity is the simple pole at `s=1`.  If

```
c_+(F)=Res_(s=1)G_+(s),                                          (1.2)
```

define

```
G_+^can(s)=G_+(s)-c_+(F)zeta(s)Theta_T(s).                        (1.3)
```

Because `Res_(s=1)zeta(s)=1` and `Theta_T(1)=1`, (1.3) is holomorphic at `s=1`.  At every nontrivial zero `rho`,

```
G_+^can(rho)=G_+(rho)=-zeta'(rho)K_F(rho-1/2).                    (1.4)
```

In the `z` variable,

```
Theta_T(1/2+z)=exp(-T(z-1/2))/(z+1/2).                            (1.5)
```

The inverse Laplace transform of (1.5) is a scalar multiple of
`1_[T,infinity)(t)exp(-t/2)`.  Hence the correction preserves right support.  Its boundary product with zeta is
`L2`, since the factor `(z+1/2)^(-1)` gains one power while zeta has critical convexity growth strictly below
`|tau|^(1/2)`.

Among shifted right-Hardy functions with value one at `s=1`, (0.1) is the normalized reproducing kernel and has
minimal norm.  This fixes the vector correction, not only its residue coefficient.

## 2. Fixed function, moving contour

Keep the holomorphic function `G_+^can(s)` fixed and move its boundary from `Re s=1/2` to
`Re s=1/2+delta`.  Define the endpoint-normalized boundary

```
G_(T,delta)(tau)
 :=exp(T delta)G_+^can(1/2+delta+i tau),             delta>=0.    (2.1)
```

If `g` is the inverse boundary transform at `delta=0`, Paley--Wiener gives

```
g_delta(t)=exp(-delta(t-T))g(t),
supp g_delta subset [T,infinity).                                  (2.2)
```

No derivative of a chosen cutoff profile occurs: the same corrected holomorphic function is being observed on
parallel contours.

## 3. Exact slope identity

The one-derivative estimate of `R161_014` permits differentiation under the norm.

**Theorem 3.1 (endpoint-normalized norm slope; PROVED).** Put

```
N_T(delta)=||G_(T,delta)||_L2(iR)^2=||g_delta||_L2(T,infinity)^2. (3.1)
```

Then

```
N_T'(0+)
 =-2 integral_T^infinity (t-T)|g(t)|^2dt
 =-E_T^PC(F).                                                     (3.2)
```

In particular `N_T'(0+)<=0`, with equality if and only if `g=0`.

*Proof.* Insert (2.2) in (3.1):

```
N_T(delta)=integral_T^infinity exp(-2delta(t-T))|g(t)|^2dt.
```

Differentiate at zero.  The moment is finite by `Qg in L2`; comparison with (5.1) of `R161_014` proves (3.2).
If the integral is zero, `g` is supported at the null set `{T}` and hence is zero in `L2`. ∎

## 4. Exact final inequality

The upper balance of `R161_014`,

```
E_T^PC(F)<=0,                                                     (4.1)
```

is now equivalent to

```
N_T'(0+)>=0.                                                      (4.2)
```

But Theorem 3.1 gives the opposite inequality for every causal port.  Therefore either (4.1) or (4.2) forces

```
N_T'(0+)=0,
E_T^PC(F)=0,
g=0.                                                             (4.3)
```

The closure problem has consequently become:

> **Canonical port minimum theorem.** On a primitive first-contact state, the finite Poisson--Chebyshev mixed
> pairing and the crossed moving-Tate correction imply that the canonical endpoint-normalized product-port norm
> has a right minimum at the critical contour.

Unlike an abstract contractivity assertion, every object in this statement is fixed: the port is (1.3), its gauge
is (0.1), and its deformation is (2.1).

## 5. Collision with the old first-jet gauge obstruction

Phase 116, equations (752)--(753), showed that the derivative of a synthesized two-port amplitude does not determine
the derivative of separated port energy: one may add `delta h` to one port and `-delta h` to the other.

The canonical Hardy construction removes the arbitrary cutoff part of that gauge.  Any remaining admissible `h`
must simultaneously:

1. preserve the right/left Hardy support;
2. preserve the canonical pole interpolation (0.1);
3. preserve the crossed Tate coefficients;
4. lie in the physical cosine-scattering kernel.

The homogeneous remainder is precisely the Sonin component measured by `E_T^PC`.  Thus the old gauge obstruction is
no longer an unspecified Hilbert vector: its norm slope is the explicit nonnegative integral in (3.2).  Proving the
minimum theorem kills it.

## 6. What remains to calculate

It remains to differentiate the finite, safe-half-plane `(PC)` mixed pairing along the same contour displacement,
including the canonical moving primitive projection.  The already proved deformed one-sided identity of phase 116
shows that the bilateral amplitude tangent is purely Tate.  With the canonical gauge (0.1), the required conclusion
is that its two crossed Tate contributions are exactly the derivative of the normal correction, leaving
`N_T'(0+)>=0` on a first-contact radical.

No arbitrary Hardy profile, square root of `A_T`, or fitted port metric is allowed in that calculation.

## 7. Status

- canonical vector-valued polar gauge (0.1)--(1.3): **PROVED**;
- critical-jet preservation: **PROVED**;
- exact norm-slope formula (3.2): **PROVED**;
- equivalence of the last upper balance with the port minimum theorem: **PROVED**;
- first contact implies the port minimum theorem: **OPEN — final mixed-pairing calculation**;
- row D: **OPEN**.

