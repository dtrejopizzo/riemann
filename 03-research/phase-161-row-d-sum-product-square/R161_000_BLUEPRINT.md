# R161_000 — Blueprint: the sum×product square


## 0. Objective

Develop `R160_D4_R2`, open problem `O-D4.1`:

> Construct a quadratic object in which `Lambda * 1_N = log` and additive Poisson/Fourier are used in the same
> load-bearing analytic step, rather than separately through a Dirichlet-convolution identity or a translated test.

The mathematical objective is row D:

`a_T(F) >= 0` for every `T` and every primitive `F in P_T`.

No identity, detector, finite-window computation or RH-equivalent reformulation counts as closure.

## 1. Premises of record

1. Primitive positivity is proved for `T <= log 2`; complete positivity is cited to `T <= 0.8`; nothing is proved
   for `T > 0.8`.
2. The margin has no positive uniform lower bound and satisfies the unconditional upper bound
   `lambda_T <= exp(-exp((2-epsilon)T))` for large `T`.
3. A convolution identity acting only on dilated tests is a window shift (`R160_D4_R2`, Thm 5.1).
4. A separated arithmetic/archimedean square is excluded beyond the recorded threshold (`G2_B3_R5`).
5. A finite number of exact values or instances of `Lambda*1=log` cannot decide the uniform problem.
6. The additive square by itself is zero-blind: its exponents add and its top pole is the known pole at `2`
   (Paper 46, Thms 26.15–26.17).

## 2. Required novelty test

A phase-161 candidate must have all four properties:

1. **Jointness:** Poisson and `Lambda*1=log` occur in one operator identity before taking a sign.
2. **Quadraticity:** the proposed positive object is an honest norm square or a proved positive block form.
3. **Orientation:** the construction retains `A_T`, not merely `A_T^2` or `|A_T|`.
4. **Separation:** the joint identity acquires an explicit interior defect for `Lambda chi_2`, `Xi_a`, finite deletion,
   finite amplification, Dedekind zeta and Beurling data.

Failure of item 3 is a negative result, not a mechanism.

## 3. Normalisation

Work on `H=L^2(R,dt)`. Put:

- `tau_a F(t)=F(t+a)`;
- `J F(t)=F(-t)`;
- `X F(t)=tF(t)`;
- `F_infty` = the additive Fourier transform transported to log scale, a self-adjoint unitary involution;
- `M=m(D)`, with `m(tau)=Re psi(1/4+i tau/2)-log pi`.

From `R160_C8_R1`, Theorem 1,

`X + F_infty X F_infty = M`.

For `N>=1` define the finite Müntz operator

`S_N = sum_{n<=N} n^(-1/2) tau_(log n)`

and its finite Poisson defect

`E_N = S_N F_infty - J S_N`.

For `M_0>=1` define

`L_M0 = sum_{d<=M_0} Lambda(d)d^(-1/2)tau_(log d)`,

`P_M0=L_M0+L_M0^*`, and `A_M0=M-P_M0`.

`A_M0` is the finite-contact Weil multiplier.

## 4. Work plan

1. Derive an exact finite identity relating `S_N A_M0 F_infty` to `E_N` and to the hyperbola remainder.
2. Check its coefficient support using `Lambda*1=log`.
3. Repeat with a general comb and exhibit the falsifier defect inside `k<=N`.
4. Form the canonical norm square and determine whether it retains the sign of `A_M0`.
5. If the norm square is sterile, isolate the weakest oriented boundary inequality which would recover the sign.

## 5. Success levels

- **COMPLETE:** a proved nonnegative expression implies `a_T>=0` for every `T` and passes all falsifiers.
- **PARTIAL_NEW:** a new joint identity plus a nontrivial sign-bearing lemma not equivalent to row D.
- **STRUCTURAL_NEGATIVE:** a theorem showing that the natural joint squares lose orientation, with a precise residual.
- **RESTATEMENT:** the candidate is `||A_TF||^2`, a window shift, Li/Weil positivity, or Douglas factorisation.

