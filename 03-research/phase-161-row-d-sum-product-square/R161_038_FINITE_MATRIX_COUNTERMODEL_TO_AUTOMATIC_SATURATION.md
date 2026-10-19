# R161_038 — Exact matrix countermodel: `(PC)` plus radicality does not imply coherent saturation

## 0. Verdict

There is a two-dimensional exact model satisfying every algebraic identity used in the derivation of `(PC)`, with
`A=0`, but whose coherent orientation square is strictly positive on every nonzero vector. Therefore the terminal
saturation in `R161_035` cannot follow from the linear `(PC)` identity and first-contact radicality alone.

Any successful proof must use a property absent from the formal algebra: the actual additive-Fourier kernel,
physical support compression, and the polar/Tate boundary geometry. This countermodel prevents the coherent
parallelogram from being mistaken for the missing proof.

## 1. The model

Work on `H=C^2` with the standard inner product. Put

```
X = [[ 1, 0],
     [ 0,-1]],

J=Fcal=[[0,1],
        [1,0]],

S = [[0,1],
     [0,0]],

L=0.                                                     (1.1)
```

Then

```
J=J*=J^(-1),       Fcal=Fcal*=Fcal^(-1),
JXJ=-X,
M:=X+Fcal X Fcal=0.                                    (1.2)
```

Consequently

```
A=M-(L+L*)=0.                                           (1.3)
```

Thus every vector is an exact radical/equality vector for `A`.

## 2. The finite Poisson--Chebyshev identity holds

Define exactly as in phase 161

```
K=-[X,S],
E=SFcal-JS,
H=LS-K.                                                 (2.1)
```

Direct multiplication gives

```
K=-2S,
E=X,
H=2S.                                                   (2.2)
```

Since `X^2=I`,

```
{X,E}=2I.                                               (2.3)
```

Moreover

```
JH+HFcal=2JS+2SJ=2I.                                   (2.4)
```

The `L*E` term is zero. Hence the complete anomaly is

```
{X,E}-L*E-JH-HFcal=0=SAFcal.                           (2.5)
```

This is `(PC)` exactly, not approximately.

The earlier mean identity also holds:

```
SMFcal=0=JK+KFcal+{X,E}.                               (2.6)
```

Indeed `JK+KFcal=-2(JS+SJ)=-2I` and `{X,E}=2I`.

## 3. Coherent saturation fails maximally

The two orientations are

```
U=KFcal=-2SJ=-2[[1,0],[0,0]],
V=JK=-2JS=-2[[0,0],[0,1]].                            (3.1)
```

Therefore

```
U-V=-2X.                                                (3.2)
```

For every `f in C^2`,

```
D^coh(f)=1/4||(U-V)f||^2=||f||^2.                     (3.3)
```

In particular

```
Af=0
```

does not imply `D^coh(f)=0` unless `f=0`.

The model also contains both parity lines: `J(1,epsilon)=epsilon(1,epsilon)`. Equation (3.3) remains strictly
positive on either parity line, so parity alone does not repair the implication.

## 4. What the countermodel does and does not reject

It rejects every proof whose inputs are only:

1. the involution identities for `J,Fcal`;
2. `X+Fcal X Fcal=M`;
3. the definitions of `K,E,H,A`;
4. the linear `(PC)` identity;
5. radicality `Af=0` or its polarized linear consequences;
6. parity.

It does not model:

- the genuine logarithmic cosine kernel;
- support on a finite physical interval;
- the integer-translation semigroup and its Euler--Maclaurin continuum;
- the crossed Tate collar law;
- the Gamma pole lattice.

At least one of these physical properties must enter load-bearingly in the saturation proof.

## 5. Consequence for the terminal gate

`R161_037` remains valid:

```
coherent saturation => F=0.
```

What fails is any assertion that saturation is automatic from `(PC)` and radicality. The remaining theorem must
be a genuine **physical compression theorem**, for example

```
first contact + exact polar/Tate collar geometry
 -> ||(K_N^renFcal-JK_N^ren)F||_2 ->0.                (5.1)
```

Proving (5.1) is already a uniqueness theorem strong enough to close D; the matrix model shows why it cannot be
obtained by rearranging the formal anomaly once more.

## 6. Status

- exact matrix realization of all formal `(PC)` identities: **PROVED**;
- exact radical `A=0`: **PROVED**;
- failure of coherent saturation on both parity lines: **PROVED**;
- automatic algebraic saturation: **REFUTED**;
- physical compression/polar/Tate saturation: **OPEN / SOLE TERMINAL INPUT**;
- row D: **OPEN**.
