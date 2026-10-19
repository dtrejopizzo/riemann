# R161_069 — A faithful observation cannot be factored formally through the zero-mode operator

**Correction (R161_070).** Section 1 is a conditional kernel lemma, not an impossibility theorem for deriving a factorization. Its application to first contact in Section 2 is invalid as written: first contact concerns ker H_T of the primitive compression, not ker A_infinity. The global adjoint representation of C_delta also needs the observation-domain correction of R161_070. Equivalence in strength to D does not make a proof circular. Independence from the full physical hypotheses has not been established.

## 1. Abstract lemma

Let `A=A*` on a common core and let `C>=0` be a faithful quadratic observation:

    <f,Cf>=0  iff  f=0.                                      (1.1)

Suppose there were an operator `K` such that

    C=AK                                                     (1.2)

as a quadratic-form identity on that core.  If `Af=0`, then

    <f,Cf>=<f,AKf>=<Af,Kf>=0,                                (1.3)

and faithfulness gives `f=0`.

Therefore a proof of (1.2) already proves injectivity of `A`; it cannot be obtained from formal commutation and
compression identities which admit a nonzero kernel countermodel.

## 2. Application to the Gamma--Euler observation

For R161_068 put

    C_delta=L*R_delta*R_delta.                                (2.1)

Its real quadratic form is

    Re<f,C_delta f>
      =sum_(m>=1)[-zeta'(2m+1)/zeta(2m+1)]
        a_me^(-2a_m(T+delta))|K_f(a_m)|^2,                    (2.2)

which is nonnegative and faithful.  Hence any division-free identity of the form

    C_delta=A_infinity K_delta                                (2.3)

would itself exclude every nonzero first-contact zero mode.  Adding Tate/exterior terms does not weaken this
conclusion unless their vanishing or favorable sign is independently proved; that independent assertion is again
the missing arithmetic input.

## 3. Consequence

R161_068 supplies a genuinely arithmetic faithful detector absent from the three-block countermodel, but not a
law forcing its value to vanish on a radical.  The following implication is invalid:

    `C_delta` is built from Gamma and Lambda
       => `<F,C_delta F>=0` on `ker A_infinity`.               (3.1)

What is required is precisely an independent equality-state theorem establishing the orthogonality or sign of
this detector.  Neither `(PC-ren)`, its adjoint, the support commutator, local Mobius inversion, nor finite Laurent
holomorphy supplies it, by R161_060--R161_068.

## 4. Status

- faithful Gamma--Euler detector: **proved in R161_068**;
- formal factorization through the zero-mode operator: **cannot be used without already proving injectivity**;
- equality-state annihilation/sign law: **missing**;
- D: **open**.
