# R161_020 — Compressed scattering and the exact leakage square

## 0. Verdict

The physical scattering theorem can be weakened to a one-sided compressed equation. Let `P_+` be multiplication by
`1_[T,infinity)` and let `C_log` be the selfadjoint unitary logarithmic cosine transform. For the canonical product
port `g=P_+g`, it is enough to prove

```
P_+ C_log g=sigma g,       sigma in {+1,-1}.                       (0.1)
```

Unitarity then forces the missing exterior component to vanish and upgrades (0.1) to the full scattering equation
`C_log g=sigma g`. The Gamma-pole theorem `R161_019` consequently gives `F=0`.

The obstruction has an exact positive square:

```
L_T^sc(F):=||(I-P_+)C_log g||^2
          =||g||^2-||P_+C_log g||^2>=0.                          (0.2)
```

Thus phase 161 no longer needs an unspecified global port identity. It needs to identify the finite quadratic
Poisson--Chebyshev anomaly with the leakage square (0.2), or directly prove the compressed equation (0.1) on a
first-contact state.

## 1. Unit-modulus compression lemma

**Lemma 1.1 (unitary compression rigidity; PROVED).** Let `U` be unitary on a Hilbert space, `P` an orthogonal
projection and `g=Pg`. If

```
P U g=lambda g,       |lambda|=1,                                (1.1)
```

then

```
Ug=lambda g.                                                      (1.2)
```

*Proof.* Orthogonal decomposition gives

```
||g||^2=||Ug||^2=||PUg||^2+||(I-P)Ug||^2
       =||g||^2+||(I-P)Ug||^2.
```

Therefore `(I-P)Ug=0`, and (1.1) gives (1.2). ∎

Apply the lemma with `U=C_log`, `P=P_+` and `lambda=sigma`. This proves the verdict.

## 2. Two-port formulation

Let `g_+^0` and `g_-^0` be the corrected ports and suppose parity gives

```
R g_-^0=epsilon g_+^0.                                          (2.1)
```

The typed scattering equation is

```
g_+^0+C_log Rg_-^0=0.                                           (2.2)
```

Using (2.1), its right compression is

```
P_+C_log g_+^0=-epsilon g_+^0.                                  (2.3)
```

Conversely, Lemma 1.1 upgrades (2.3) to (2.2). Hence the full two-port boundary theorem is equivalent to its
right-exterior compression; no left-boundary convergence has to be proved separately.

## 3. The leakage square

For every right-supported `g`, define

```
L_T^sc(g):=||(I-P_+)C_log g||^2.                                 (3.1)
```

Since `C_log` is unitary,

```
L_T^sc(g)=||g||^2-||P_+C_log g||^2.                              (3.2)
```

If the compressed amplitude equation has an error `e`,

```
P_+C_log g=sigma g+e,                                           (3.3)
```

then

```
L_T^sc(g)
 =-2 sigma Re<g,e>-||e||^2.                                     (3.4)
```

The left side is nonnegative, so an independently proved orthogonality `Re<g,e>=0` already forces `e=0`. This is a
strictly weaker quadratic target than controlling an arbitrary port norm derivative.

In particular, the desired scattering is equivalent to either one of

```
P_+C_log g=sigma g,
L_T^sc(g)=0 and P_+C_log g has the correct sign.                  (3.5)
```

## 4. Mellin/Hardy expression of the projected defect

Let `H_T^+` denote the Hardy projection corresponding to support in `[T,infinity)`. On boundary transforms the
compressed scattering error is

```
E_T^sc(F)
 :=H_T^+[chi(s)G_-^0(s)]+G_+^0(s).                              (4.1)
```

Because `G_+^0` is already right Hardy, (4.1) is the Hardy projection of the exact meromorphic defect from
`R161_017`:

```
E_T^sc(F)=H_T^+[zeta(s)W_epsilon^0(s)].                          (4.2)
```

The full linear completed graph does not set (4.2) to zero: `R161_018` proves that recombining its complementary
Hardy component returns the tautology `[Z,D_Gamma]=0`. The novelty must therefore be a quadratic statement about
the complementary projection,

```
L_T^sc(F)
 =||H_T^-[chi(s)G_-^0(s)]||_2^2,                                (4.3)
```

where `H_T^-=I-H_T^+` after the endpoint shift.

## 5. Relation with the finite Poisson defect

The finite operator

```
E_N^ren=S_N^ren Fcal-JS_N^ren                                   (5.1)
```

is precisely the pre-limit failure of the additive Fourier/co-Poisson intertwining. Its unprojected strong limit
vanishes on smooth data, which is why the linear route contains no information. A possible nontrivial boundary
quantity is its **projected defect energy before the limit**.

The now sharply typed target is:

> **Leakage identification L161.4 (OPEN).** Construct an explicit normalization and first-contact input
> `V_(M,N,T)F`, using `(PC-ren)` before the two orientations are recombined, such that
> 
> ```
> lim ||H_T^- E_N^ren V_(M,N,T)F||^2=L_T^sc(F),                  (5.2)
> ```
> 
> and the finite first-contact identity makes the left side zero.

The normalization must be inherited from the existing zeta product and crossed Tate terms. Defining it from
`L_T^sc` would be circular. The convergence must be a projected graph convergence; ordinary convergence
`E_N^ren ->0` is too weak and simply kills both sides before the boundary layer is resolved.

## 6. Closure chain from the compressed equation

If L161.4 proves (0.1), then:

1. Lemma 1.1 gives `C_log g=sigma g`.
2. The Mellin equation is the exact physical scattering relation of `R161_017`.
3. `R161_019` forces the complete Gamma-pole moment lattice and hence `F=0`.
4. Consequently `g=0` and
   `E_T^PC(F)=0<=0`, proving the missing Sonin--Gamma upper balance.
5. First contact is impossible, so the existing nesting/cofinal argument closes row D.

## 7. Status

- reduction of full scattering to one compressed equation: **PROVED**;
- exact nonnegative leakage square: **PROVED**;
- Hardy expression of the scattering error: **PROVED**;
- Gamma-pole closure after zero leakage: **PROVED by `R161_019`**;
- identification of the finite `(PC-ren)` projected defect with leakage: **OPEN**;
- vanishing of that finite defect on first contact: **OPEN**;
- row D: **OPEN**.
