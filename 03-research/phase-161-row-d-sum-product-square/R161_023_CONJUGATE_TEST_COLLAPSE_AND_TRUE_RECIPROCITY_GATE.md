# R161_023 — The canonical conjugate test collapses to `(PC-ren)`; the reciprocity must be independent

## 0. Verdict

The canonical test `Pi_TP_TZ*g` of `R161_022` is well typed, but radicality against that test supplies no new
boundary law. At every finite level its Tate term and its exterior-Weil term recombine exactly into the left side
of `(PC-ren)`. Adding the exterior functional-equation defect then reconstructs the extremal correlation itself.

Therefore the proposed pullback test is a useful coordinate decomposition but not the terminal trick. The crossed
Tate matrix determines the coefficients; it must not be mistaken for the orthogonal Tate Gram and does not cancel
the Tate contribution on its own.

## 1. The Tate projection disappears against a Tate vector

Let `P=P_T`, let `Pi=Pi_T` be the orthogonal primitive projection in `PL2`, and put `Tau=I-Pi` on `PL2`. If
`r` belongs to the two-dimensional Tate space and `y` is any vector for which the pairings are defined, then

```
<r,Tau P y>=<r,P y>=<r,y>.                                      (1.1)
```

The first equality holds because `r` is orthogonal to the primitive range of `Pi`; the second because `r=Pr`.

Now take a finite causal synthesis `S=S_N^ren`, a separated right test port `g_N`, and

```
y_N=S* g_N.                                                      (1.2)
```

Then

```
boxed: <r,Tau P y_N>=<Sr,g_N>.                                  (1.3)
```

This is the explicit first-contact Tate term in `R161_005`, not an additional correction.

## 2. Recombination with the exterior Weil leakage

Write as before

```
AF=r+ell,       r=PAF,       ell=(I-P)AF.                        (2.1)
```

At first contact, radicality gives

```
<AF,Pi P y_N>=0.                                                 (2.2)
```

By support orthogonality and (1.3),

```
<r,Tau P y_N>+<ell,(I-P)y_N>
 =<AF,y_N>
 =<S AF,g_N>.                                                    (2.3)
```

The finite Poisson--Chebyshev identity says

```
S_N^ren A_M Fcal=R_(M,N)^ren.                                   (2.4)
```

After applying it to `Fcal F`, equation (2.3) is therefore just the mixed pairing

```
<R_(M,N)^ren Fcal F,g_N>.                                       (2.5)
```

No sign or vanishing has been gained.

## 3. Addition of the functional-equation exterior

Let `w=(W_epsilon^0)^vee` and `d=w-AF`, so `Pd=0`. The three-term formula of `R161_022` becomes, at the finite
regularized level,

```
X_(M,N)(F)
 =Re[<S_N^ren AF,g_N>+<S_N^ren d_N,g_N>]
 =Re<g_N,S_N^ren w_N>.                                          (3.1)
```

In the asserted graph limit this is exactly

```
X_T(F)=Re<G_+^0,zeta W_epsilon^0>.                               (3.2)
```

Thus the construction returns the definition of `X_T`; it does not prove `X_T=0`.

## 4. Why the crossed Tate matrix cannot repair the collapse

In the ordered Tate basis `(phi_-,phi_+)`, phase 121 proves that the genuine positive Gram is

```
G_T=2 [[sinh T,T],[T,sinh T]],                                   (4.1)
```

whereas the collar system uses the crossed matrix

```
G_T C=2 [[T,sinh T],[sinh T,T]].                                 (4.2)
```

The latter is indefinite. It determines `(alpha,beta)` from the collar currents but is not the matrix of `Tau`.
Substituting (4.2) into (1.1) as though it were an orthogonal Gram would create a false sign and a false
cancellation. Equation (1.3) is the correct projection calculation.

## 5. Consequence for the terminal strategy

The extremal-correlation reduction of `R161_021` remains valid and useful:

```
X_T(F)=0  <=>  C_log g=-epsilon g  ->  F=0.                       (5.1)
```

What fails is deriving `X_T=0` from radicality by the direct pullback `Pi PZ*g`. A successful proof must add a law
not contained in

```
a_T(F,H)=0       for every primitive H.                          (5.2)
```

In the current coordinates the exact admissible target is:

> **L161.6 (independent exterior reciprocity; OPEN).** Derive from the two-orientation finite `(PC-ren)` identity,
> before scalar recombination, an antisymmetric boundary law which makes
> `Re<g_N,S_N^ren w_N>` tend to zero. The law must not follow merely by choosing a primitive test in (5.2).

Equivalently, the new input must distinguish the two orderings in the mixed product

```
<g_N,S_N^ren w_N>       and       <S_N^ren* g_N,w_N>,             (5.3)
```

through their moving support boundary. Ordinary adjointness makes them equal on the full graph; the only possible
new term is the oriented boundary concomitant created before the finite window is removed.

## 6. Status

- Tate projection identity (1.3): **PROVED**;
- recombination with the exterior Weil port into `(PC-ren)`: **PROVED**;
- direct conjugate-test closure: **REJECTED AS TAUTOLOGICAL**;
- crossed-matrix-as-Gram shortcut: **REJECTED / WRONG SIGN**;
- extremal scalar criterion `X_T=0`: **STILL PROVED AND LIVE**;
- independent exterior boundary reciprocity L161.6: **OPEN / TERMINAL**;
- row D: **OPEN**.
