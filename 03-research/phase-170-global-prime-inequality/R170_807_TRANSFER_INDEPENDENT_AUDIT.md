# R170_807 — Independent audit of the archimedean transport

R170_805, its matrix diagnostics, and R170_806 are
audited here. The conclusion does not use the induction or
certificates of *The Three Gates*. It is not a proof of RH.

## Verdict

The capacity bound of R170_805 and the exact transport of R170_806 are
correct, with the normalizations made precise below. The new result
that is established is an identity of forms: the archimedean block of
Paper 47 contains, with coefficient one, the form `b` of R170_805, and
the rest is a scalar shift plus an explicit bounded integral operator.
The primes and the polar term transport exactly within the same
equality.

This removes a pending identification, but does not force the sign.
The capacity bound only controls a positive part of `b`. The residual
still contains the shift, the regular kernel, all the prime
translations, and the rank-two polar term; minimizing it separately
would be invalid. A concrete counterexample to that relaxation is
given below.

## 1. Analytic check of R170_805

Let

    r[u]=¼∬(1/|x−y|−1)|u(x)−u(y)|²
         +∫[−½log(x(1−x))−log2]|u(x)|².

For an interval `I=(a,a+eps)` and `V=||u_I−avg_I u||²`, the three loads
used in R170_805 are:

    interior:   ½(1−eps)V,
    complement: ½[log((a+eps)(1−a)/eps²)−(1−eps)]V,
    potential:  max(0,−½log((a+eps)(1−a))−log2)V.

If the last constant is nonnegative, the sum equals exactly
`log(1/(2eps))V`. If it is negative, then
`(a+eps)(1−a)>1/4`, and the first two loads alone are already strictly
greater than that same value. This case split justifies the potential
step; a negative bound is not being multiplied by `||u_I||²≥V`.

For two ordered intervals whose left endpoints are `D eps` apart, the
pair's actual contribution is at least

    ½[1/(D+1)−eps](V_mu+V_nu).

The two loads that the isolated-interval argument would have counted
add up to

    ½[log(1+1/D)−eps](V_mu+V_nu).

The per-pair subtraction is therefore exactly

    ½ d(D)(V_mu+V_nu),
    d(D)=log(1+1/D)−1/(D+1).

Moreover `d'(D)=−1/[D(D+1)^2]`. After ordering the intervals, their
separation gives `D_{mu,nu}≥|mu−nu|`, and

    sum_{j=1}^N d(j)=1+log(N+1)−H_{N+1} -> 1−gamma_E.

There is at most one interval on each side for each index distance; the
factor `1/2` of `Delta_nu` cancels that multiplicity of two. This
confirms `Delta_nu≤1−gamma_E`.

Minimizing

    l0[u]=(log2+½)||u||²−½|∫u|²

over a single complement of measure `1−ell`, with datum `f` fixed on
`S`, gives

    (log2+½)||f||²
      −(log2+½)/(2log2+ell) |∫_S f|².

The denominator and the direction of the infimum from R170_805 are
correct. The bound on `r` depends only on the datum on `S`, so it can
be added before taking that same infimum. This does not authorize
separately minimizing other forms that also depend on the complement.

## 2. `verify_common_complement.py` diagnostic

The script correctly assembles the compression of

    b[u]=¼∬|u(x)−u(y)|²/|x−y|
         +∫−½log(x(1−x))|u(x)|²

on normalized cell indicators. For cells at integer distance `d`, the
off-diagonal entry is

    −½[(d+1)log(d+1)+(d−1)log(d−1)−2d log d],

which correctly includes the cell normalization factor. The diagonal
`−sum(offdiag)+potential_average` and the Schur complement over the
complement are also correct. The lower matrix uses `ell=#selected/n`,
not the number of windows, and matches the continuous formula.

The three published values were reproduced:

    1.0398844780972514,
    1.0222310994169843,
    0.8916274345214998.

These are floating-point consistency checks, not interval certificates
nor approximations of the Paper 47 margin.

## 3. Independent derivation of the transport

Let `L=2T` and

    f(x)=sqrt(L) F(L(x−1/2)).

This transformation is unitary. With the Paper 47 density

    K(v)=1/(2sinh(v/2))+1/(2cosh(v/2))

we define

    q_L(s)=L K(Ls)−1/s,       q_L(0)=L/2.

If the R170_806 convention

    k=K/2,  h_L=q_L/2,

is used, then `h_L(0)=L/4`, exactly as stated there. For the
autocorrelation `C_f(s)=∫f(x+s)conj(f(x))dx`, the Lévy energy is

    Lev(F)=∫_0^1 [||f||²−Re C_f(s)] L K(Ls) ds
           +||f||²∫_L^infty K(v)dv.

The singular identity

    ∫_0^1 [||f||²−Re C_f(s)] ds/s = b[f]

is checked directly by separating interior pairs and the two boundary
loads. On the other hand,

    lim_{z->0}(∫_z^infty K(v)dv+log z)=log4+pi/2.

Hence

    C0+log4+pi/2−log L = −gamma_E−log(2pi L),

since `C0=−gamma_E−pi/2−3log2−log pi`. We obtain

    Arch_T(F)=b[f]−[gamma_E+log(2pi L)]||f||²
              −∫_0^1 q_L(s) Re C_f(s)ds,

equivalent to (1) of R170_806 because

    ∫q_L Re C_f = ⟨H_L f,f⟩

with `H_L` of kernel `h_L=q_L/2` and the double-integral convention used
there. `h_L` is continuous on `[0,1]`; the residual is Hilbert–Schmidt.
The difference between the forms is bounded and their domains coincide.

The script `verify_archimedean_transfer.py` compares this formula with
the original integral for real and complex step functions, at
`L=0.5, log(5), 4, 12`. Absolute errors between zero and `8.5e−44` were
reproduced with 45 digits of working precision. This checks factors
and constants, but remains a diagnostic, not an interval proof; the
derivation above is the proof.

## 4. Primes and polar term

The autocorrelation scales with no extra factor:

    c_F(log n)=C_f(log(n)/L).

Thus, if `V_d f(x)=f(x−d)` with extension by zero,

    J_L=sum_{n<exp(L)} Lambda(n)/sqrt(n)
             (V_{log(n)/L}+V_{log(n)/L}^*)

satisfies

    ⟨J_Lf,f⟩=sum 2Lambda(n)/sqrt(n) Re c_F(log n).

Also

    A(F)=⟨f,c_L+s_L⟩,   B(F)=⟨f,c_L−s_L⟩,

where `c_L=sqrt(L)cosh(L(x−1/2)/2)` and similarly for `s_L`. Then

    2 Re(A(F)conj(B(F)))
       =2|⟨f,c_L⟩|²−2|⟨f,s_L⟩|².

This confirms every sign and factor of (2). The identity preserves the
exact values of `Lambda`, the positions `log n`, their couplings with
the complement, and both polar channels.

## 5. Counterexample against discarding the reserve

The R170_806 warning is necessary, not merely formal. Suppose `S^c`
contains an interval `J` of width less than `log(2)/L`. Take as `f_j`
the normalized sines of `J`, extended by zero. They are orthonormal,
supported on `J`, and belong to the energy domain (their linear
vanishing at the endpoints avoids a jump). Then:

* `P_S[f_j]=0`;
* `J_L[f_j]=0`, because no prime translation can overlap `J` with
  itself;
* `f_j` converges weakly to zero, so the mean and polar terms tend to
  zero;
* `H_L` is compact, so `⟨H_Lf_j,f_j⟩->0`.

If `R_S` is discarded, the relaxed form tends to

    beta−a_L,
    beta=log2+1/2,  a_L=gamma_E+log(2pi L).

This is negative when

    L>exp(beta−gamma_E)/(2pi) ≈ 0.2946563400.

Scaling one of those vectors with negative value, the relaxed infimum
is `−infinity` already for zero source datum. This is not a
counterexample to the complete form: it shows that the reserve `R_S`
contains precisely high-frequency energy that cannot be discarded
before the joint Schur step.

## 6. What remains proved and what remains open

Proved:

1. the uniform capacity `Delta_nu≤1−gamma_E` with a common complement;
2. the exact formula for the minimum of `l0` over that complement;
3. the exact unitary transport of the archimedean term, the primes, and
   the polar term;
4. the formal equivalence of the problem with `b−K_L≥0`, or with the
   contraction of `b^(−1/2)K_Lb^(−1/2)`.

Not proved:

1. a sign bound for the residual `K_L` in the metric of `b`;
2. a Schur estimate that preserves `R_S` and is uniform in `L`;
3. the arithmetic annihilation at the first contact;
4. the global inequality of Paper 47 or RH.

The next bottleneck is now well localized: the positive reserve `R_S`
must be assigned to the joint residual, in the exact inverse metric of
the complement, without replacing the `log n` translations by a bound
that forgets the factorization of the integers.
