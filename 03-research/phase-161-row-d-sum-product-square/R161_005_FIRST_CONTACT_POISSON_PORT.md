# R161_005 — Exact first-contact specialisation of the Poisson--Chebyshev anomaly

## 0. Verdict

The joint identity `(PC)` has one non-redundant place left to act: the exterior port of a hypothetical first-contact
state. After window compression, its interior Muntz factor is the already invertible causal zeta observation, and
the first-contact equation fixes the interior of the Weil operator. What is not fixed is the part of the Weil image
outside the window, subsequently shifted back through the causal comb.

This note isolates that term exactly. It proves no estimate and no sign. It replaces the vague request for a
"positive Poisson boundary energy" by a typed vector identity whose missing implication is explicit.

## 1. Abstract compressed identity

Let `P=P_T`, let `A=A_M` with `M>=e^(2T)`, and let `F in P_T L2(R)` be in the common core. Assume the primitive
first-contact equation

```
P A P F = r,                                                       (1.1)
```

where `r=alpha e^(-t/2)+beta e^(t/2)` on `(-T,T)` and is extended by zero. Define the exterior Weil port

```
ell_T(F)=(1-P) A F.                                                (1.2)
```

Since `PF=F`, equations (1.1)--(1.2) give the exact decomposition

```
A F = r + ell_T(F).                                                (1.3)
```

For the phase-161 remainder

```
R_(M,N)={Q,E_N}-L_M^*E_N-JH_(M,N)-H_(M,N)Fcal,
```

identity `(PC)` says `R_(M,N)=S_N A Fcal`. Apply it to `Fcal F` and use `Fcal^2=I`:

**Theorem 1.1 (first-contact Poisson-port identity; PROVED).**

```
P R_(M,N) Fcal F
 = P S_N r + B_(N,T)(F),

B_(N,T)(F):=P S_N (1-P)A F.                                      (1.4)
```

*Proof.* The left side is `P S_N A F`; insert (1.3). ∎

Every term on the left of (1.4) is source-defined from the additive Fourier defect, the von Mangoldt comb and the
divisor hyperbola. The first term on the right is explicit from the two Tate multipliers. The only unknown is the
incoming exterior port `B_(N,T)(F)`.

## 2. Why the port cannot be discarded

Even when `N>=e^(2T)`, only the double compression stabilises:

`P S_N P=Z_(T,-)`.

The operator `P S_N(1-P)` does not stabilise at that cutoff. A large translation can bring a remote part of
`ell_T(F)` back into `(-T,T)`. Thus replacing (1.4) by

`P R_(M,N)Fcal F = Z_(T,-)r`

would silently assume that the exterior Weil port vanishes. That is precisely the missing boundary theorem, not a
support consequence.

Likewise, taking `||B_(N,T)(F)||^2` loses orientation. It is unchanged when the exterior Weil port changes sign and
therefore cannot by itself determine the sign of `A` or kill the antisymmetric critical residue.

## 3. Renormalised form

With the notation of `R161_003`, the same proof gives

```
P R_(M,N)^ren Fcal F
 = P S_N^ren r + B_(N,T)^ren(F),

B_(N,T)^ren(F):=P S_N^ren(1-P)A F.                                (3.1)
```

The benefit is analytic: `E_N^ren` tends to zero on Schwartz data. The cost is that the polar operator must remain
inside both terms on the right. On primitive data it is a finite-width translated boundary layer, but it does not
vanish operatorially. Its cancellation must occur in the oriented pairing, using both Tate moments, before a norm
is taken.

## 4. The first chamber above `0.8`

If

`0.8<T<(1/2)log 5`,

then

```
Z_(T,-)=I+2^(-1/2)tau_(log 2)
          +3^(-1/2)tau_(log 3)
          +4^(-1/2)tau_(log 4),                                  (4.1)
```

after compression. Its nonidentity part `K` satisfies `K^3=0`, so

```
Z_(T,-)^(-1)=I-K+K^2.                                             (4.2)
```

Equations (1.4), (4.1) and (4.2) make the interior algebra completely finite. They do **not** finite-rank the
exterior port: additive Fourier produces a noncompact tail before the returning translations act.

This sharply locates the possible gain over the retired phase-121 Mobius lift. The divisor incidence is still
finite and triangular, but the Poisson exterior port is not a divisor-depth history. Therefore the root-diagonal
no-go of `P121_CMO_SOURCE_MATRIX_NO_GO` does not automatically eliminate it. Conversely, unless this nonlocal port
is used, phase 161 reduces exactly to that no-go.

## 5. Required terminal implication

Let

```
nu_T(F)=(K_F(i gamma))_(rho=1/2+i gamma simple)
```

be the critical conormal observation of phase 121. The exact missing statement is now:

> **PC-port theorem (OPEN).** For a primitive first-contact vector, the oriented limit of (3.1), taken before any
> scalar trace, has critical normal symbol `c nu_T(F)` with `c!=0`, while the equality equation and the exact polar
> Tate cancellation force that symbol to vanish.

If proved, faithfulness of the conormal observation gives `F=0`, excludes first contact, and closes D by the existing
nesting and cofinal theorems.

The theorem has four binding tests:

1. **Orientation:** it must use `B^ren`, not only `||B^ren||` or the sum of the two reflected ports.
2. **Rank-one source:** the local Euler step must consume the single primitive character at each prime; the shifted
   rank-two pair must fail this typing clause.
3. **No scalar Stieltjes collapse:** tracing to `D(u)` before extracting the normal symbol returns to Paper 41 C5.
4. **No Mobius diagonal:** eliminating the exterior port into a finite divisor history returns to the phase-121 CMO
   no-go.

## 6. Status

- first-contact specialisation (1.4): **PROVED**;
- renormalised specialisation (3.1): **PROVED on the common core**;
- exact finite interior algebra immediately above `T=0.8`: **PROVED**;
- identification of the exterior-port critical normal symbol: **OPEN**;
- its equality-state vanishing: **OPEN / terminal row-D theorem**.

The next calculation is not another positivity search. It is the Mellin boundary-value calculation of
`B_(N,T)^ren(F)` at a simple critical zero, with the two causal orientations kept separate.
