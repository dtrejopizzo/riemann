# R161_031 — Pathwise realization: the divisor seam collapses and the Poisson seam survives

## 0. Verdict

The abstract vectors of `R161_030` are not arbitrary. On the completed finite hyperbola they are supplied
canonically by the two terms `J L_M S_N` and `L_M S_N Fcal` in the derivation of `(PC)`. For every factorization
`de=k`, both translations compose to the same total displacement `log k`. Hence the conditional mean is independent
of `d`: the divisor-seam part of the two-level variance vanishes identically, while the two-orientation Poisson
square survives with coefficient `(log k)^2/k`.

Thus the path vectors required in `R161_030(4.1)` are identified on every completed fibre `k<=N<=M`. As audited in
`R161_033`, this does not yet realize their direct-sum second moment from the coherent physical `(PC-ren)` vector.
The remaining issue includes both that Gram completion and the polar/crossed-Tate first-contact pairing.

## 1. Two oriented paths over `de=k`

Use the phase-161 conventions

```
tau_a f(t)=f(t+a),          J tau_a=tau_(-a)J,
L_M=sum_(d<=M)Lambda(d)d^(-1/2)tau_(log d),
S_N=sum_(e<=N)e^(-1/2)tau_(log e).
```

The two unrecombined product terms in `(PC)` are

```
J L_M S_N,                 L_M S_N Fcal.             (1.1)
```

For a path `de=k` define, on any common-core input `f`,

```
x_(k,d)^-(f)=k^(-1/2) J tau_(log k)f,
x_(k,d)^+(f)=k^(-1/2) tau_(log k)Fcal f.             (1.2)
```

These are exactly the two path outputs in (1.1). Indeed,

```
J tau_(log d)tau_(log e)=J tau_(log k),
tau_(log d)tau_(log e)Fcal=tau_(log k)Fcal.           (1.3)
```

No commutation of `J` with a one-sided translation is being assumed: `J` remains on the left in the first line.

## 2. Exact completion by `Lambda*1=log`

Assume `k<=N<=M`. Then every factorization `de=k` occurs in `L_MS_N`, and

```
sum_(d|k)Lambda(d)=log k.                             (2.1)
```

Consequently

```
sum_(d|k)Lambda(d)x_(k,d)^-
 =k^(-1/2)(log k)Jtau_(log k)f,

sum_(d|k)Lambda(d)x_(k,d)^+
 =k^(-1/2)(log k)tau_(log k)Fcal f.                  (2.2)
```

Summing (2.2) over the completed fibres gives exactly the two orientations `J K_N f` and `K_N Fcal f`.

## 3. Collapse of the divisor seam

Put, as in `R161_030`,

```
m_(k,d)=(x_(k,d)^++x_(k,d)^-)/2,
r_(k,d)=(x_(k,d)^+-x_(k,d)^-)/2.
```

Equation (1.2) shows that both vectors are independent of `d` for fixed `k`. Therefore

```
m_(k,d)-m_(k,e)=0                                      (3.1)
```

for every pair of active divisors. Applying the gate identity `R161_030(1.1)` gives the exact fibre formula

```
 (log k)/2 sum_(d|k)Lambda(d)
       (||x_(k,d)^+||^2+||x_(k,d)^-||^2)
 -||sum_(d|k)Lambda(d)m_(k,d)||^2

 =(log k)^2/(4k)
   ||tau_(log k)Fcal f-Jtau_(log k)f||^2.             (3.2)
```

The right side is the square of the single-atom additive Poisson discrepancy at displacement `log k`, with the
Chebyshev weight supplied by the completed divisor fibre.

This is stronger than merely saying that the old divisor variance has no gap. Here its kernel is known exactly
and intentionally: multiplication is coherent along every path, so only the Fourier orientation can carry the
defect.

## 4. Operator form

Let

```
Delta_k=tau_(log k)Fcal-Jtau_(log k).                 (4.1)
```

For the completed interior `2<=k<=N<=M`, summing (3.2) yields the canonical nonnegative form

```
D_(M,N)^orient(f)
 =1/4 sum_(2<=k<=N) (log k)^2/k ||Delta_k f||^2
 >=0.                                                (4.2)
```

Every term is source-labelled before scalar synthesis. In particular, no absolute value has been inserted into a
von Mangoldt coefficient and no Mobius elimination is used. However, `(PC-ren)` contains the coherent synthesis of
these labels, not automatically their direct-sum norm; see `R161_033`.

The sum in (4.2) is not `||K_NFcal-JK_N||^2`: that latter norm contains interference between distinct `k` and can
lose the equality kernel. Formula (4.2) is the unsupertraced/direct-sum square. Keeping the fibre label is essential.

## 5. Polar renormalization and the remaining boundary term

For `S_N^ren=S_N-C_N`, the lattice part has exactly the realization above. The continuum part is not a discrete
divisor fibre and must not be hidden in (4.2). By `R161_028`, its derivative at
`log N=2(T+delta)` is the reflected exterior image. Hence the complete renormalized gate must have the form

```
finite lattice orientation square
+ continuum image/Gamma square
+ crossed Tate endpoint concomitant.                 (5.1)
```

The first two terms have now been identified as positive objects: (4.2) and `2D_(T,delta)^Gamma`. The remaining
calculation is to show that the crossed Tate endpoint term is exactly the coherent left side whose first-contact
value is zero, rather than an additional indefinite remainder.

Equivalently, the terminal identity sought in `R161_029(6.1)` is now coefficient-typed as

```
0=2D_(T,delta)^Gamma(F)+D_(M,N)^orient(F)+boundary_(M,N,T,delta)(F),  (5.2)
```

and closure requires the exact polar/Tate calculation

```
boundary_(M,N,T,delta)(F)=0                             (5.3)
```

on a primitive first-contact state (or absorption of that boundary into the two displayed squares with the same
sign). Equation (5.3) is not inferred here from primitive radicality.

## 6. Status

- canonical pathwise vectors `x_(k,d)^+/-`: **CONSTRUCTED**;
- completed-fibre use of `Lambda*1=log`: **PROVED**;
- exact collapse of the divisor seam: **PROVED**;
- surviving direct-sum Poisson square (4.2): **DEFINED AND POSITIVE; SOURCE-NORM REALIZATION OPEN**;
- continuum component identified with the polar image/Gamma coordinate: **PROVED by `R161_026`--`R161_028`**;
- crossed-Tate first-contact saturation: **OPEN / TERMINAL**;
- row D: **OPEN**.
