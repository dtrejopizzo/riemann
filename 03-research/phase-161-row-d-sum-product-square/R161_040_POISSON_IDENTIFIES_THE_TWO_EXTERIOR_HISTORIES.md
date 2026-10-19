# R161_040 — Poisson identifies the two exterior histories missing in phase 121

## 0. Verdict

The matrix countermodel of `R161_038` and the phase-121 local Hankel no-go omit one load-bearing physical fact.
For the actual renormalized Muntz synthesis, additive Poisson identifies the Fourier-oriented causal history with
the adjoint causal history, modulo the explicit finite defect `E_N^ren`. After exterior compression this is exactly
the annular-transport relation which phase 121 could not obtain from Real symmetry alone.

This does not yet prove the differentiated/coherent saturation: differentiating the relation produces the Gamma
connection and endpoint terms. It does, however, supply the missing structural input which the formal countermodel
shows is necessary.

## 1. Causal synthesis and its adjoint

Let

```
Z_N=S_N^ren,
E_N=Z_NFcal-JZ_N.                                       (1.1)
```

Every coefficient of `Z_N` is real and its translations all have the same orientation. Reflection reverses that
orientation, so on the common core

```
JZ_NJ=Z_N*.                                             (1.2)
```

Consequently (1.1) can be written

```
boxed: Z_NFcal=Z_N*J+E_N.                              (1.3)
```

## 2. Exact exterior-history identification

Let `P=P_T`, and let `f=Pf` have parity

```
Jf=epsilon f.                                          (2.1)
```

Apply (1.3) to `f` and then compress to the exterior:

### Theorem 2.1 (finite Poisson annular transport)

```
boxed:
(I-P)Z_NFcal f-epsilon(I-P)Z_N*f
 =(I-P)E_Nf.                                           (2.2)
```

The analogous interior identity is

```
PZ_NFcal f-epsilon PZ_N*f=PE_Nf.                       (2.3)
```

*Proof.* Equation (1.3), parity (2.1), and application of the orthogonal projections. QED.

No scalar trace, norm or limiting argument is used.

## 3. Toeplitz--Hankel interpretation

Define the two exterior history maps

```
H_N^+= (I-P)Z_NFcal P,
H_N^-= (I-P)Z_N*P.                                     (3.1)
```

Then on the parity-`epsilon` line, (2.2) says

```
H_N^+f-epsilon H_N^-f=(I-P)E_Nf.                       (3.2)
```

Thus

```
||H_N^+f-epsilon H_N^-f||^2
 =||(I-P)E_Nf||^2.                                     (3.3)
```

This is a genuine positive Poisson leakage square. It contains the cross term between the two causal histories
with its physical sign.

For comparison, phase 121 obtained two vectors `h_+,h_-` but no identity between them. Equation (3.2) is that
identity, with the exact finite error retained. It comes from additive Fourier, not from reflection alone.

## 4. Relation to the compressed self-commutator

For any normal full-line convolution `Z`, its compression `T=PZP` satisfies

```
T*T-TT*
 =PZ(I-P)Z*P-PZ*(I-P)ZP.                              (4.1)
```

Equivalently,

```
<f,(T*T-TT*)f>
 =||(I-P)Z*f||^2-||(I-P)Zf||^2.                       (4.2)
```

The right side is the difference of the two Hankel leakage squares. Equation (3.2) supplies the missing
orientation-sensitive comparison when the first input is Fourier-transported and `f` has fixed parity.

The `2x2` model in `R161_038` satisfies the formal `(PC)` identity but has no analogue of the small physical defect
in (3.2) tied to a convergent Euler--Maclaurin family and a fixed support projection.

## 5. Differentiating the transport

The multiplication operator `Xf(t)=tf(t)` commutes with `P_T`. Hence applying `X` to (2.2), or taking its graph
commutator before compression, introduces no derivative of the sharp window itself. With

```
K_N=-[X,Z_N],                                           (5.1)
```

the differentiated relation contains the desired coherent jet

```
K_NFcal-JK_N,                                          (5.2)
```

plus the derivative of the Fourier intertwiner. By `X+Fcal XFcal=M`, that derivative is exactly the Gamma
connection already appearing in `R161_035`--`R161_036`.

**Successor correction (`R161_041`).** Differentiating the difference history produces the orientation mean
`K_NFcal+JK_N`, not the critical difference `K_NFcal-JK_N`. The latter is the covariant derivative of the
complementary sum `Z_NFcal+JZ_N`. Thus the squared-history target below is withdrawn; the live target is a mixed
compressed pairing between the Poisson difference and the derivative of the complementary sum.

## 6. Required next identity

The admissible target is a differentiated version of (3.3) of the form

```
boundary derivative of ||(I-P)E_N^ren f||^2
 = ||(I-P)(K_N^renFcal-JK_N^ren)f||^2
   +2D_(T,delta)^Gamma(f)
   +epsilon<v,G_TCv>,                                  (6.1)
```

with all normalization and possible finite endpoint terms computed explicitly. The last term becomes `||r||^2`
by `R161_032`.

Equation (6.1) is **withdrawn by `R161_041` for wrong orientation**.

## 7. Status

- adjoint/reflection identity `JZ_NJ=Z_N*`: **PROVED**;
- exact finite exterior-history transport (2.2): **PROVED**;
- positive history-difference square (3.3): **PROVED**;
- identification of the missing phase-121 annular transport with Poisson defect: **PROVED**;
- differentiated polar/Tate energy identity (6.1): **WITHDRAWN / WRONG ORIENTATION**;
- row D: **OPEN**.
