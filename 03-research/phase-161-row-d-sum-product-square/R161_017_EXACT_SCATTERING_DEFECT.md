# R161_017 — Exact functional-equation defect of the product-port scattering

## 0. Verdict

The typed cosine relation left schematic in `R161_011` has an exact meromorphic defect. For a parity source it is
not an unspecified boundary term: before the canonical polar correction,

```
G_+(z)+chi(s)G_-(z)=zeta(s)W_epsilon(F)(z),   s=1/2+z,           (0.1)
```

where

```
W_epsilon(F)=d_Gamma K_F-Q_+-epsilon Q_+(-z),
d_Gamma(s)=-chi'(s)/chi(s).                                     (0.2)
```

The inverse distribution of `W_epsilon(F)` restricts on the physical window to the Tate forcing `r_epsilon`.
The canonical right/left polar corrections are exterior-supported, so they do not change that interior restriction.

Consequently, a proof of the exact product-port cosine eigenrelation would already force

```
r_epsilon=0.                                                     (0.3)
```

It first reduces the equation to the homogeneous defect. `R161_019` strengthens this observation: the positive odd
Gamma poles of that explicit defect force a complete lattice of exponential moments, hence `F=0`. Thus exact
physical scattering already closes the product-range rigidity problem.

## 1. Conventions and the reflected port

Use the functional equation in the convention

```
zeta(s)=chi(s)zeta(1-s),
chi(s)=pi^(s-1/2) Gamma((1-s)/2)/Gamma(s/2).                     (1.1)
```

Let `F(-t)=epsilon F(t)`, `epsilon in {+1,-1}`. Then

```
K_F(-z)=epsilon K_F(z).                                         (1.2)
```

The right product port is

```
G_+(z)=-zeta'(s)K_F(z)-zeta(s)Q_+(z).                           (1.3)
```

Define its physically reflected left port by

```
G_-(z):=epsilon G_+(-z)
       =-zeta'(1-s)K_F(z)-zeta(1-s)Q_-(z),                       (1.4)
Q_-(z):=epsilon Q_+(-z).                                        (1.5)
```

Thus no independent left amplitude has been inserted. Equation (1.4) is just parity and reflection of the causal
right construction.

For logarithmic reflection `R` and the normalized cosine transform `C_log`, the Mellin rule is

```
M(C_log u)(s)=chi(s)M(u)(1-s).                                  (1.6)
```

Hence the boundary transform of `C_log R g_-` is `chi(s)G_-(z)`. The desired typed graph relation is therefore

```
G_+(z)+chi(s)G_-(z)=0,                                         (1.7)
```

up to the fixed global sign convention already absorbed into `epsilon`.

## 2. Exact defect identity

Differentiate (1.1):

```
zeta'(s)=chi'(s)zeta(1-s)-chi(s)zeta'(1-s).                      (2.1)
```

It follows that

```
zeta'(s)+chi(s)zeta'(1-s)
 =(chi'(s)/chi(s))zeta(s).                                      (2.2)
```

Substitute (1.3)--(1.5) into the left side of (1.7). Since
`chi(s)zeta(1-s)=zeta(s)`, equation (2.2) gives:

**Theorem 2.1 (product scattering defect; PROVED).** As meromorphic Mellin germs,

```
G_+(z)+chi(s)G_-(z)
 =zeta(s)[d_Gamma(s)K_F(z)-Q_+(z)-Q_-(z)].                       (2.3)
```

*Proof.* Direct substitution gives

```
G_++chi G_-
 =-[zeta'(s)+chi(s)zeta'(1-s)]K_F
   -zeta(s)[Q_++Q_-].                                           (2.4)
```

Use (2.2) and `d_Gamma=-chi'/chi`. ∎

This calculation also checks the critical jets. At a critical zero the right side of (2.3) vanishes, while the
two terms on the left have opposite values by the differentiated functional equation. Thus scattering conservation
cancels the two jets; it does not annihilate either one separately.

## 3. Physical meaning of `W_epsilon`

Let `q_+` be the compact prehistory whose transform is `Q_+`; by construction

```
q_+(t)=Y_+(t),       -T<t<T.                                    (3.1)
```

Reflection and parity give a posthistory `q_-` with transform `Q_-` and

```
q_-(t)=Y_-(t),       -T<t<T.                                    (3.2)
```

The inverse Mellin distribution of `d_Gamma K_F` is `D_Gamma F`. Therefore, on the open physical window,

```
W_epsilon(F)^vee
 =D_Gamma F-B_+F-B_-F
 =r_epsilon.                                                     (3.3)
```

The last equality is exactly the primitive first-contact equation. No boundary trace at `+/-T` is used.

## 4. Canonical polar corrections

Write the corrected ports in the general typed form

```
G_+^0=G_+-zeta(s)Theta_+,
G_-^0=G_--zeta(1-s)Theta_-.                                     (4.1)
```

Here the scalar coefficients are included in `Theta_+/-`. The phase-161 construction chooses `Theta_+` with
inverse support in `[T,infinity)` and `Theta_-` with inverse support in `(-infinity,-T]`. Equation (2.3) becomes

```
G_+^0+chi G_-^0
 =zeta(s)W_epsilon^0,
W_epsilon^0:=W_epsilon-Theta_+-Theta_-.                          (4.2)
```

Because both corrections are exterior-supported,

```
(W_epsilon^0)^vee=r_epsilon       on (-T,T).                     (4.3)
```

This statement is independent of whether one uses the compact cutoff of `R161_008` or the canonical Hardy kernel
of `R161_015`.

## 5. Consequence of completing the physical scattering

Assume the desired physical boundary passage proves

```
G_+^0+chi G_-^0=0                                                (5.1)
```

as a common meromorphic germ (equivalently, first in any open zero-free half-plane and then by continuation).
For `Re s>1`, zeta has no zeros. Equations (4.2) and (5.1) imply

```
W_epsilon^0=0.                                                   (5.2)
```

Uniqueness of Mellin transforms and (4.3) give:

**Corollary 5.1 (scattering kills the Tate forcing; PROVED CONDITIONALLY).** Exact physical product-port
scattering implies `r_epsilon=0`.

This is a genuine strengthening of completed scalar conservation. The phase-121 common-graph identity fixes the
incoming current to `-Z_(T,+)r_epsilon` but allows nonzero `r_epsilon`; it does not prove (5.1).

At the level of the abstract phase-121 equation, a nonzero homogeneous mode could satisfy

```
(D_Gamma-B_+-B_-)F=0 on I_T.                                   (5.3)
```

Ruling that out is explicitly the remaining homogeneous zero-mode problem in phase 121. However, the product range
contains additional information not present in that abstract problem: `R161_019` uses the positive odd poles of
`d_Gamma` in (4.2) to prove that (5.1) forces `F=0`.

## 6. Relation with `(PC)` and the remaining theorem

The finite Poisson--Chebyshev identity constructs the right side of (2.3) before continuation. What it has not yet
proved is that its graph limit is the zero germ (5.1), rather than only the already known completed scalar
commutator. The missing assertion can now be stated without informal port language:

> **Physical scattering theorem (OPEN).** On a first-contact radical, the polar-renormalized `(PC)` limit equals
> `zeta(s)W_epsilon^0` in a graph topology retaining the two causal orientations, and the completed incoming/Tate
> system makes `W_epsilon^0` vanish.

The last phrase is load-bearing. The known incoming identity merely says that its compression cancels the local
zeta image of `r_epsilon`; it does not prove global vanishing of `W_epsilon^0`.

## 7. Status

- exact functional-equation defect (2.3): **PROVED**;
- interior identification with the first-contact forcing (3.3): **PROVED**;
- invariance of that interior value under the polar corrections: **PROVED**;
- exact physical scattering implies homogeneous forcing: **PROVED CONDITIONALLY**;
- physical scattering identity (5.1) from `(PC)`: **OPEN**;
- uniqueness of the resulting homogeneous mode in the explicit product range: **PROVED in `R161_019`**;
- row D: **OPEN**.

**Successor audit.** `R161_018` performs the graph-limit comparison. It proves that the linear `(PC-ren)` limit is
the zero completed commutator and that separating it into prehistory plus exterior product ports gives a tautology,
not (5.1). Thus the physical scattering theorem cannot be obtained from the linear limit alone; the finite
quadratic defect must be retained.
