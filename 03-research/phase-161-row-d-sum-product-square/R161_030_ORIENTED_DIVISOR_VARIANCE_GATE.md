# R161_030 — The algebraic gate: oriented divisor variance before scalar synthesis

## 0. Verdict

There is an exact positive square which uses the two ingredients in the required order. First retain the two
Poisson/Fourier orientations over every factorization path `de=k`; only then average the paths with the Chebyshev
weights `Lambda(d)`. The result is a two-level Hilbert-space variance identity.

Unlike the divisor variance of phases 104--121, it does not vanish identically on a prime fibre. A prime fibre has
only one nonzero divisor path, but it still has two Fourier orientations. Its surviving term is the orientation-
difference square. This removes the root-diagonal obstruction algebraically.

The identity proves the gate implication: saturation of one coherent quadratic equality forces both the Poisson
orientation defect and every transverse divisor seam to vanish. What remains to close D is the source
identification that the finite first-contact `(PC-ren)` pairing is exactly this saturated equality.

## 1. The two-level square

Let `H` be a complex Hilbert space. Fix `k>=2`, put

```
w_d=Lambda(d),                  d|k,
W_k=sum_(d|k)w_d=log k,
```

and attach two vectors `x_d^+,x_d^- in H` to every divisor path with `w_d>0`. Define

```
m_d=(x_d^+ + x_d^-)/2,
r_d=(x_d^+ - x_d^-)/2.
```

### Theorem 1.1 (oriented Chebyshev variance)

One has the exact identity

```
 W_k/2 sum_(d|k) w_d (||x_d^+||^2+||x_d^-||^2)
       - ||sum_(d|k)w_d m_d||^2

 = W_k sum_(d|k)w_d ||r_d||^2
   + 1/2 sum_(d,e|k)w_dw_e ||m_d-m_e||^2.             (1.1)
```

The left side is nonnegative, and it is zero if and only if

```
x_d^+=x_d^-                    for every active d,
m_d=m_e                        for every active d,e.              (1.2)
```

*Proof.* The parallelogram identity gives

```
(||x_d^+||^2+||x_d^-||^2)/2=||m_d||^2+||r_d||^2.     (1.3)
```

The weighted Hilbert variance identity gives

```
W_k sum_d w_d||m_d||^2-||sum_dw_dm_d||^2
 =1/2 sum_(d,e)w_dw_e||m_d-m_e||^2.                 (1.4)
```

Multiply (1.3) by `W_kw_d`, sum over `d`, and use (1.4). All weights are nonnegative and `W_k>0`, so equality is
equivalent to (1.2). QED.

## 2. The prime-root obstruction is removed

If `k=p` is prime, the only active divisor is `d=p`. The second term on the right of (1.1) is zero, exactly as in
the phase-104 conditional variance. But the first term remains:

```
left side=(log p)^2 ||x_p^+-x_p^-||^2/4.             (2.1)
```

Thus the additive orientation supplies the missing second state on the one-point multiplicative fibre. This is
the minimal algebraic way in which simultaneous Poisson/Fourier and `Lambda*1=log` evade the unitriangular
root-diagonal obstruction of `P121_CMO_SOURCE_MATRIX_NO_GO`.

Either ordering separately loses this fact: averaging orientations first deletes `r_d`; summing divisor paths
first retains only one global Poisson defect and deletes transverse seams; taking a scalar trace before (1.1)
deletes both equality conditions.

## 3. Total-variance interpretation

Give `D` the conditional probability

```
P(D=d|k)=Lambda(d)/log k
```

and give the orientation `Sigma` the values `+,-` with probability `1/2`. For `X=x_D^Sigma`, (1.1) divided by
`W_k^2` is exactly

```
Var(X)=E_D Var(X|D)+Var_D(E[X|D]).                    (3.1)
```

The first term is the additive Poisson seam; the second is the multiplicative divisor seam. The order of
conditioning is structural.

## 4. The precise finite `(PC-ren)` gate

The remaining construction must produce, before `J` and `Fcal` are recombined, source-defined vectors

```
x_(k,d)^+(F), x_(k,d)^-(F),       de=k,              (4.1)
```

such that their difference is the projected finite Poisson/Fourier defect on that path, their weighted mean is
the coherent Chebyshev port, and the crossed-Tate/polar first-contact identity is the saturation

```
 sum_k [
   (log k)/2 sum_(d|k)Lambda(d)
       (||x_(k,d)^+||^2+||x_(k,d)^-||^2)
   -||sum_(d|k)Lambda(d)m_(k,d)||^2
 ]=0.                                                        (4.2)
```

If (4.1)--(4.2) are obtained, (1.1) forces every orientation defect and divisor seam to vanish termwise. In
particular prime fibres force the projected Poisson defect to vanish. Under the phase-161 boundary identification
this is the leakage square of `R161_020`; unitary compression rigidity gives full physical scattering, and
`R161_019` forces `F=0`.

## 5. Noncircularity boundary

Equation (4.2) has not been proved merely by (1.1). It must be derived from the finite `(PC-ren)` source law.
Asserting that radicality makes it zero would repeat `R161_023`: radicality annihilates a primitive linear test,
not an arbitrary source second moment.

The terminal problem is therefore the coefficient-by-coefficient verification of (4.1)--(4.2), including the
polar/Tate boundary. No estimate is needed after that verification; the rest is the exact algebra (1.1).

## 6. Status

- oriented divisor variance identity (1.1): **PROVED**;
- equality kernel and survival on prime fibres: **PROVED**;
- escape from the old scalar divisor-fibre root diagonal: **PROVED ALGEBRAICALLY**;
- realization by finite `(PC-ren)` source vectors: **OPEN**;
- first-contact saturation (4.2): **OPEN / TERMINAL SOURCE MATCH**;
- row D: **OPEN**.
