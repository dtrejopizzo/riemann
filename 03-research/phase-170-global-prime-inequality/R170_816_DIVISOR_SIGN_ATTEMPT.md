# R170_816 — Divisor sign attempt for the corrected flux

This note attempts to prove the lower bound (G)(i) of
R170_814 while preserving the correct Tate port, the two collars, and
the domain of forms. The result is negative but precise: the divisor
identity localizes the tail that would need to be controlled, and gives
an explicit two-sided estimate; it does not give the proposed one-sided
bound. RH is not proved, nor is the known positivity range extended.

## 1. Data that are not modified

Let `U=𝓕`, let `g=S_LF`, and

    z=S_N U g,
    Φ(F)=Re[a_M(F,z)−<r_F,z>],

with `N=ceil(exp(2T))`, `M=N²`, and `F` a real, primitive vector of
definite parity in the radical of a hypothetical first contact. Every
pairing with `X` is understood as the joint extension of the form, as
in R170_813–814. In particular, distributions that are not individually
defined are not separated. The Tate term is

    Re<S_N* r_F,U g>=Re<r_F,S_N U g>.

It is not replaced by `S_N r_F`.

## 2. The exact reduction that does produce Λ*1=log

The Poisson–Chebyshev identity gives

    Φ(F)=Re<{X,E_N}F−L_M*E_NF−JH_{M,N}F−H_{M,N}UF,g>
          −Re<S_N* r_F,Ug>.                              (1)

Since `g` and `F` are supported on `I_T`, while every term of
`H_{M,N}` has shift `log k>log N≥2T`, we have exactly

    <JH_{M,N}F,g>=0.                                     (2)

Hence

    Φ(F)=B_{M,N,L}(F)−C_{M,N,L}(F),                       (3)

    B=Re<({X,E_N}−L_M*E_N)F,g>−Re<S_N*r_F,Ug>,
    C=Re<H_{M,N}UF,g>.

This (3), and not the sign of the coefficients separately, is the exact
output of the identity. For `M≥N`,

    H_{M,N}=Σ_{N<k≤MN} h_{M,N}(k) k^(−1/2) τ_{log k},      (4)
    h_{M,N}(k)=Σ_{dm=k,d≤M,m≤N} Λ(d)≥0.

The equality `Σ_{d|k}Λ(d)=log k` is used essentially to cancel every
coefficient with `k≤N`. The structural conclusion that comes from the
incidence is that the tail falls outside the support diagonal. It does
not eliminate (4) after applying `U`, because `UF` is not supported on
`I_T`.

## 3. Two-sided estimate of the surviving tail

Let us define the finite, explicit mass

    W_{M,N}=Σ_{N<k≤MN} h_{M,N}(k)/sqrt(k).                 (5)

Since the translations and `U` are unitary, (4) implies

    |C_{M,N,L}(F)|
      ≤ W_{M,N} ||F||₂ ||S_LF||₂.                         (6)

Equivalently, if

    K_{M,N,L}=
      (U H_{M,N}* S_L+S_L H_{M,N}U)/2,

then `K_{M,N,L}` is self-adjoint and

    C_{M,N,L}(F)=<F,K_{M,N,L}F>,
    −W_{M,N}||S_L|| I ≤ K_{M,N,L}≤W_{M,N}||S_L|| I.       (7)

This is the elementary norm bound for the term that remains after the
divisor cancellation; it is two-sided and does not constitute a new
arithmetic estimate. To obtain (G)(i) from (3) one would need, for
example,

    B_{M,N,L}(F)−<F,K_{M,N,L}F>
       ≥(1−q₀)||R_LF||²                                  (8)

on the radical of the first contact. Neither (6) nor (7) come close to
(8): their adverse side depends on `||F|| ||S_LF||`, while the reserve
depends on `||R_LF||²`; there is no uniform lower bound for
`||R_LF||/||F||` before fixing the radical, and even after that, such a
bound does not decide the sign of `K`. Moreover the mass (5) is not
small for the choice `M=N²`. Indeed, the subfamily `d=2`, `N/2<m≤N`, is
included in (4), and for `N≥2`, `M≥2`,

    W_{M,N} ≥ (log 2)/sqrt(2) Σ_{N/2<m≤N}m^(−1/2)
            ≥ (log 2)/(2sqrt(2)) sqrt(N).                 (8a)

Hence, keeping absolute values already produces, from a single divisor,
a loss growing like `sqrt(N)`, precisely where (8) would need an
oriented cancellation.

## 4. Why Eratosthenes does not repair the sign

In the notation of R170_814,

    Φ=Ω−Σ_{2≤d≤M} Λ(d) ξ_d/sqrt(d),                       (9)
    ξ_d=Re<F,(τ_{log d}+τ_{−log d})z>.

The exact inversion gives

    Σ_{d≤M} Λ(d)ξ_d/sqrt(d)
      =Σ_{km≤M} μ(k)log(m) ξ_{km}/sqrt(km).               (10)

Eratosthenes says that the numbers `Λ(d)` of (9) are determined by the
earlier divisors. It does not impose a positivity condition on the real
vector `(ξ_d)`. Even before using Möbius, a coefficient `Λ(d)>0`
multiplies a shifted correlation, whose sign can be positive or
negative. After (10), the signs of `μ` also appear.

This falsifies a concrete step that could have been used to prove (8):

    "h(k)≥0 (or Λ(d)≥0) ⇒ the corresponding pairing is ≥0".

Two functions `u` and `v=τ_a u` with small supports give
`Re<τ_a(u−v),u−v><0` for a suitable translation. Hence the inference
already fails on a single edge with a positive weight. This example is
not a first-contact vector and does not refute a possible specific law
for such vectors; it proves that the sign does not come from the
positivity of the coefficients or from the sieve alone.

## 5. The remaining arithmetic obligation, unrenamed

The sought bound is exactly equivalent to the positivity, on the
first-contact radical, of the quadratic form

    F ↦ Φ(F)−(1−q₀)||R_LF||².                             (11)

Equations (3)–(7) show where new information would have to enter: it
must correlate the Poisson–Tate defect `B` with the cross self-adjoint
form `K`, using the *first*-contact restriction. The oscillatory
example of §4 only invalidates the inference from positive coefficients
for general functions; it does not satisfy `H_TF=0` and does not rule
out an additional identity valid specifically on the radical.

That correlation was not obtained. In particular, (11) must not be
called a consequence of `Λ*1=log`: it would be exactly the missing new
arithmetic law. First minimality also does not appear in (1)–(10);
inserting it requires an oriented identity relating a window variation
to the same exterior test `S_NUS_LF`, including Tate and the Fourier
tail.

## 6. Oriented separation of the d=2 channel

It remains to check whether the loss of (8a) is merely an artifact of
taking norms. Set `a=(log 2)/sqrt(2)` and separate the `d=2` term before
estimating. Its contribution to `−L_M*E_N` is

    B₂=−a Re<τ_{−log2}E_NF,g>,                            (12)

and its contribution to the tail `−H_{M,N}UF` is

    −C₂=−a Σ_{N/2<m≤N}m^(−1/2)
                  Re<τ_{log(2m)}UF,g>.                   (13)

Using exactly `E_N=S_NU−JS_N`, without applying Cauchy–Schwarz,

    B₂−C₂ = a Σ_{m≤N}m^(−1/2)Re<τ_{−log(2m)}JF,g>
             −a Σ_{m≤N}m^(−1/2)Re<τ_{log(m/2)}UF,g>
             −a Σ_{N/2<m≤N}m^(−1/2)
                         Re<τ_{log(2m)}UF,g>.             (14)

Here `τ_{−log2}Jτ_{log m}=τ_{−log(2m)}J` and
`τ_{−log2}τ_{log m}=τ_{log(m/2)}` were used. The first sum of (14) is
the reflected orientation: by `JF=εF` and the supports of `F,g`, its
terms with `log(2m)≥2T` vanish. This is an exact support cancellation.

The other two sums do not cancel. In the second, shifts `log(m/2)` of
`UF` appear; in the third, shifts `log(2m)` of `UF` appear. The index
change that would formally align both scales would take `m` to `4m`,
but it changes the weights `m^(−1/2)` and, above all, the truncated
ranges. There are no opposite terms with the same operator, the same
index, and the same coefficient. The parity of `F` does not control
`UF` by support either.

Thus, separating `d=2` before taking norms recovers a genuine
cancellation in the `JF` orientation, but leaves two distinct Fourier
correlations with no sign. The `sqrt(N)` loss of (8a) does not prove
that the flux is large; it only proves that the absolute bound cannot
decide it. The exact expression (14) identifies the additional
cancellation that would still be needed.

## 7. Verdict of the attempt

The divisor identity performs two proved functions: it cancels the
`k≤N` zone and leaves the finite tail (4) with explicit weights. The
term with `JH_{M,N}F` vanishes by support, but the term with
`H_{M,N}UF` survives and satisfies only the two-sided estimate (6).
This is the concrete point where the attempt to prove

    (1−q₀)||R_LF||²≤Φ(F)

stops. No collars nor the Tate port were lost, and a coefficient
identity has not been turned into positivity of a form. The R170_814
bound remains open.
