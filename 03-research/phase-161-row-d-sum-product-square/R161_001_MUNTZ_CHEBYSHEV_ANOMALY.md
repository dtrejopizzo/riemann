# R161_001 — The finite Müntz–Chebyshev anomaly

## 0. Verdict

**PARTIAL_NEW / no sign claimed.** There is an exact finite operator identity in which the additive Fourier involution
and `Lambda*1=log` occur in the same line. It is not the linear kernel identity `(C')` of phase 160 and it is not a
Dirichlet-convolution identity applied to a test. It expresses the finite-contact Weil operator as the anomaly between:

- the truncated Müntz operator and additive Poisson summation; and
- the von Mangoldt operator and the completed divisor hyperbola.

The identity passes the falsifier test at the algebraic level. Its canonical norm square, however, is analysed in
`R161_002` and shown to lose the sign.

## 1. Operators and domains

Let `H=L^2(R,dt)`. On the Schwartz core `S(R)` put

`tau_a F(t)=F(t+a)`, `JF(t)=F(-t)`, `XF(t)=tF(t)`.

Let `Fcal=F_infty` be the ordinary additive Fourier transform transported to logarithmic coordinates. The imported
Tate–Beckner facts (`R160_C8_R1`, Lemmas 2.1–2.2 and Theorem 1) are

1. `Fcal=Fcal*=Fcal^{-1}`;
2. `J tau_a J=tau_{-a}`;
3. `X+Fcal X Fcal=M`, where `M=m(D)`.

All arithmetic operators below are finite sums of translations, hence bounded and preserve `S(R)`. The only unbounded
operator is `X`; every displayed identity is first an identity on `S(R)`.

For integers `N,M_0>=1` define

```
S_N       = sum_{n<=N} n^(-1/2) tau_(log n),
K_N       = sum_{n<=N} (log n)n^(-1/2) tau_(log n),
L_M0      = sum_{d<=M_0} Lambda(d)d^(-1/2) tau_(log d),
P_M0      = L_M0 + L_M0^*,
A_M0      = M - P_M0,
E_N       = S_N Fcal - J S_N,
H_M0,N    = L_M0 S_N - K_N.
```

`E_N` is the finite Poisson defect. For the full integer comb and primitive physical-space tests, Poisson summation
formally says `S_infty Fcal=J S_infty`. The raw `S_N` do **not** converge to that regularized operator at the critical
half-density; thus `E_N` is a finite defect, not a convergent approximation error. `H_M0,N` is the incomplete divisor-
hyperbola term. The required polar renormalization is developed in `R161_003`.

## 2. The arithmetic support theorem

**Theorem 2.1 (hyperbola support; PROVED).** If `M_0>=N`, then

```
H_M0,N = sum_{k>N} h_M0,N(k) k^(-1/2) tau_(log k),
h_M0,N(k) = sum_{dm=k, d<=M_0, m<=N} Lambda(d) >= 0.
```

In particular, `H_M0,N` has no coefficient at `k<=N`.

*Proof.* The coefficient of `k^(-1/2)tau_(log k)` in `L_M0 S_N` is

`sum_{dm=k,d<=M_0,m<=N}Lambda(d)`.

If `k<=N` and `M_0>=N`, all divisors satisfy `d<=k<=M_0` and `m=k/d<=k<=N`; hence the coefficient is
`sum_{d|k}Lambda(d)=log k`, exactly the coefficient of `K_N`. For `k>N`, `K_N` has coefficient zero and the displayed
coefficient is nonnegative. ∎

This is the finite operator form of `Lambda*1_N=log` on the completed hyperbola. Unlike `R160_D4_R2` Thm 3.4, it is
retained as an operator and will be combined with the Poisson defect before pairing with an autocorrelation.

## 3. The joint anomaly identity

**Theorem 3.1 (finite Poisson–Chebyshev anomaly; PROVED).** On `S(R)`, for every `M_0,N>=1`,

```
S_N A_M0 Fcal
  = {X,E_N} - L_M0^* E_N - J H_M0,N - H_M0,N Fcal,                 (PC)
```

where `{X,E}=XE+EX`.

*Proof.* First,

`[X,S_N]=-K_N`,

because `[X,tau_a]=-a tau_a`. From `E_N=S_NFcal-JS_N` and
`X Fcal + Fcal X=M Fcal`, calculate

```
[X,S_N]Fcal
 = X(JS_N+E_N)-S_N(MFcal-Fcal X)
 = -JXS_N+XE_N-S_NMFcal+(JS_N+E_N)X
 = -J[X,S_N]+{X,E_N}-S_NMFcal.
```

Insert `[X,S_N]=-K_N` and rearrange:

`S_N M Fcal = J K_N + K_N Fcal + {X,E_N}`.                 (3.1)

Now `K_N=L_M0S_N-H_M0,N`. Since `JL_M0=L_M0^*J` and
`JS_N=S_NFcal-E_N`,

```
J K_N + K_N Fcal
 = L_M0^* J S_N - JH_M0,N + L_M0S_NFcal-H_M0,NFcal
 = P_M0 S_NFcal - L_M0^*E_N - JH_M0,N-H_M0,NFcal.
```

Finite translation sums commute, so `P_M0S_N=S_NP_M0`. Subtract `S_NP_M0Fcal` from (3.1). ∎

**Reading.** `(PC)` is the requested joint line:

- additive Poisson/Fourier enters through `E_N` and `X+Fcal X Fcal=M`;
- multiplicative arithmetic enters through `H_M0,N`, whose lack of interior coefficients is exactly
  `Lambda*1=log`;
- the left side contains `A_M0=M-(L_M0+L_M0^*)`, the finite Weil symbol.

Neither ingredient can be removed without changing the identity. This is stronger than placing the two identities
next to one another.

## 4. Falsifier defect

Let `a:N->R`, `a(1)=0`, and define

`L^a_M0=sum_{d<=M_0}a(d)d^(-1/2)tau_(log d)` and
`delta_a(k)=sum_{d|k}a(d)-log k`.

Put `H^a_M0,N=L^a_M0S_N-K_N`.

**Theorem 4.1 (interior-defect theorem; PROVED).** If `M_0>=N`, the coefficient of
`k^(-1/2)tau_(log k)` in `H^a_M0,N` equals

```
delta_a(k),                    k<=N,
sum_{dm=k,d<=M_0,m<=N}a(d),   k>N.
```

Consequently `(PC)` for a general comb has an **interior** defect supported already at the first `k` for which
`delta_a(k)!=0`. For the falsifiers of phase 160:

- deletion `Lambda 1_(n>=N_0)`, `N_0>=3`: defect `-log 2` at `k=2`;
- amplification `Lambda+c 1_(n=n_0)`: defect `c` at `k=n_0`;
- `a_theta`: defect `-(1-theta)log 2` at `k=2`;
- `Lambda chi_2`: defect `-2log 2` at `k=2`;
- `Xi_a`: defect `log 2(2^a+2^(-a)-1)>0` at `k=2`;
- `zeta_K`: defect at the first inert or split rational prime;
- DH/Beurling: the standard integer-comb Poisson datum is absent or different.

*Proof.* For `k<=N<=M_0`, all divisors occur, so the coefficient of `L^a_M0S_N` is
`sum_{d|k}a(d)=log k+delta_a(k)`; subtract `K_N`. For `k>N`, `K_N` contributes zero. The listed values are
`R160_D4_R2`, Thm 2.2. ∎

Thus the new identity does not suffer the round-1 objection that it remains valid verbatim for the standard
falsifiers. What remains is to obtain a sign from it.

## 5. Relation to the full Weil form

For a fixed window `I_T`, choose `M_0>=exp(2T)`. When `(PC)` is paired against vectors whose autocorrelations are
supported in `[-2T,2T]`, the quadratic form of `A_M0` is exactly `a_T`; contacts beyond `exp(2T)` vanish. This does
**not** justify an operator limit `M_0,N->infty`: `S_infty` and `L_infty` do not define bounded operators at the
critical half-density. The divergent products are the anomaly, not a removable technicality.

Accordingly:

- `(PC)` is **PROVED** for finite `M_0,N`;
- its use inside a fixed supported quadratic form is legitimate after retaining all boundary terms;
- cancellation of `S_N` or passage to the untruncated operator is **FORBIDDEN** without a separate domain theorem.

The critical non-boundedness prevents the false formal conclusion `A=0` obtained by combining full Poisson and full
Chebyshev identities and cancelling `S_infty`.

## 6. What is new and what is not

New relative to the phase-160 record:

1. the operator `E_N` and the joint anomaly `(PC)`;
2. the support theorem saying ζ has only a positive hyperbola tail whereas every falsifier has an interior defect;
3. the identification of the critical half-density divergence as the location of the row-D anomaly.

Not new / not claimed:

- the identities `Lambda*1=log`, Poisson summation, or the Tate–Beckner formula separately;
- a sign for `a_T`;
- a bounded full Müntz operator;
- a proof that the hyperbola tail operator is positive (positive coefficients do not make a sum of translations
  positive).
