# Analytic dagger completion and a rejected source Gram

Status: the dagger construction is exact. The cyclic Gram is an independently
positive phase-106 source object but is **rejected** as the physical P3 Gram
by the central-weight calibration below.

## 1. The charge dagger groupoid

Let

    K_C = L^2(R,w_C(gamma)dgamma),
    w_C(gamma)=1/(2pi(gamma^2+1/4)),

and let `A` be multiplication by `gamma`. For every real charge `ell`, define

    (S_ell F)(gamma)
      =sqrt(w_C(gamma+ell)/w_C(gamma)) F(gamma+ell).

Change of variables proves

    S_ell S_m=S_(ell+m),   S_ell^*=S_(-ell),
    S_ell(A-ell)=A S_ell.

Therefore the objects `H_ell=(K_C,A-ell)` for
`ell in log Q_+^x`, with the unitary arrows `S_(ell-m):H_ell->H_m`, form a
dagger groupoid. The Witt correspondence `Gamma_n` maps to charge
`ell_n=log n`; multiplication of labels becomes addition of charges. This is
an RH-independent analytic dagger completion of the positive correspondence
semigroup.

It does not yet lift the adjoint back to an algebraic Witt correspondence:
that would require a geometric opposite orientation. Hence it proves
`P3_dag` on the common analytic coefficient module, not in the original
graph-image category.

## 2. Corrected Gamma compliance

Let

    k_Gamma(gamma)=kappa_infty+g_Gamma(gamma),
    kappa_infty=gamma_Euler+sum_p log(p)/(p(p-1)),

where `g_Gamma` is the forced positive multiplier constructed in paper 42.
Then `K_Gamma=k_Gamma(A)>0`, and

    S_ell^* K_Gamma^-1 S_ell
      = (kappa_infty+g_Gamma(A-ell))^-1.

For distinct charges the same common regression produces the operator

    C_(ell,m)=S_ell^* K_Gamma^-1 S_m.

This retains cross-place phase and is defined without `B_nuc`.

## 3. Canonical cyclic-vector source Gram

The constant function `b(gamma)=1` is a unit cyclic vector of `K_C`. Define

    c(ell,m)=<S_ell b,K_Gamma^-1 S_m b>.

It has the explicit integral

    c(ell,m)=integral_R
      sqrt(w_C(gamma+ell)w_C(gamma+m)) /
      k_Gamma(gamma) dgamma.

This kernel is positive definite because it is the Gram of the vectors
`K_Gamma^-1/2 S_ell b`. For a place-iterate `q=p^j`, the corrected
phase-106 boundary amplitude is

    alpha_q = log(p)/sqrt(2pi) * p^(-j/2).

Consequently

    G_S(q,r)=alpha_q alpha_r c(log q,log r)

is an explicit positive cross-place matrix which can be evaluated before the
nuclear form. The script `scripts/p3_charge_compliance.py` evaluates it on
`{2,3}` and `{2,3,4}`.

With the prime sum in `kappa_infty` truncated at `10^6` (so a small positive
tail is omitted), the reproducible reconnaissance values are

    G_{2,3} = [[0.010634277004, 0.012138447328],
               [0.012138447328, 0.015018196818]],

with eigenvalues `0.000491465256, 0.025161008565`, and

    G_{2,3,4} =
      [[0.010634277004, 0.012138447328, 0.005961605147],
       [0.012138447328, 0.015018196818, 0.007711316789],
       [0.005961605147, 0.007711316789, 0.004122520381]],

with eigenvalues approximately
`0.000041719858, 0.000754801584, 0.028978472760`. These signs are not the
gate: positivity is formal from the Gram representation. Their purpose is to
freeze the candidate before comparison with row (c).

## 4. Exact scope

This is operationally non-circular, but calibration rejects it as the desired
Gram. It proves neither of the following:

1. that this cyclic vector is the image of the finite mixed divisor `D_f`;
2. that its Schur defect equals the forced compression of `-B_nuc`.

The calibration gate is now a precise comparison problem: construct the map
from the row-(a) finite mixed class to the charge vectors above and compare
the resulting full matrix—not merely this cyclic submatrix—with the
`T=log 2` output-defect matrix. No parameter remains available after the
sign-quotient normalization.

## 5. Calibration verdict: wrong central mass

For `q=p^j`, row (c) fixes the quadratic contact coefficient

    w_q=log(p)/sqrt(q)=log(p)p^(-j/2).

If a Tate plane has `g(a,a)=c_p`, its boundary amplitude must therefore be

    beta_q=sqrt(w_q/c_p)
          =log(p)/sqrt(2pi) p^(-j/4),

so that `c_p beta_q^2=w_q`. Phase 106 instead used
`alpha_q=log(p)/sqrt(2pi)p^(-j/2)`, whose squared mass is
`log(p)/p^j`. It also used `kappa_infty` where the balanced physical load
requires

    m_0=log(pi)-psi(1/4).

Hence the numerical matrices in §3 are frozen diagnostics of the rejected
source model, not evidence for the physical gate. The unitary charge groupoid
of §1 survives; the attachment must be rebuilt with `beta_q`, `m_0`, the
Gamma gradient and the symmetric/antisymmetric return channels.
