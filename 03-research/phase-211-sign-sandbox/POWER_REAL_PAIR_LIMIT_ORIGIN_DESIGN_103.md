# POWER_REAL_PAIR_LIMIT_ORIGIN_DESIGN_103 — Single pointwise design of U_lim(0)

Status: **FIXED DESIGN audited and executed; result NEGATIVE with independent reproduction approved.** See `POWER_REAL_PAIR_DOUBLE_LIMIT_AUDIT_103.md` and section7 at the end of this source. The following parameters were fixed before data and did not change. Papers untouched.

## 1. Object, antecedent and exact test

The consultation of the project rules and of the three indexes, and the difference with respect to102, are recorded in POWER_REAL_PAIR_DOUBLE_LIMIT_103.md. Only the pointwise value of U_lim(0) for the limiting REAL pair (J,K) is studied; not a family of orders, parameters or windows. The analytic proof103 justifies the inference from a positive sign to a failure of the negative/positive crossing for FINITE p,q.

Only the seven full moments will be integrated

    I_r=int_0^infinito t^r Phi(t)dt, r=0,...,6.

Use the exact definitions

    a=I2/I0, K0=aI1-I3/2, Kmass=aI2/2-I4/6,
    b0=Kmass/I2,
    H0=(b0/2-a/6)I3+I5/24,
    Hmass=(b0/6-a/24)I4+I6/120.

103 proves I0,I2,Kmass,Hmass>0. The single main test will be the polynomial that clears all denominators:

    P=720 I0^2 (K0 Hmass-Kmass H0)
     =-3 I0^2 I3 I6+5 I0^2 I4 I5
       +6 I0 I1 I2 I6-20 I0 I1 I4^2
       -15 I0 I2^2 I5+25 I0 I2 I3 I4
       +30 I1 I2^2 I4-30 I2^3 I3.                 (TEST)

The equality is exactly algebraic, and sign(P)=sign(U_lim(0)). P is homogeneous of degree4 in the moments. The assert must accept P>0 OR P<0, without predetermining which. If the interval contains0, the result will be INCONCLUSIVE with these parameters, without adjusting precision, degree, panels or modes during the run. The previous quotients may be printed only as auxiliary readings after checking positive denominators; they do not replace TEST.

## 2. Parameters fixed before data

The geometry of093/098 is reused:

    compact interval [0,2], 128 panels,
    exact centres (2j+1)/128, j=0,...,127,
    half-width h=1/128, Cauchy radius R=1/32,
    ratio h/R=1/4,
    Arb arithmetic 512 bits, Taylor degree64, cap65,
    theta modes m=1,...,16.

ctx.prec=512 and ctx.cap=65 must be set explicitly. Check that the coefficients Phi[0],...,Phi[64] are finite at each centre and that the jet has sufficient precision. No mesh of another certificate is imported or run. No parameter search will be made.

## 3. Holomorphic bound and full tail of modes

The declared discs are contained in

    -1/32<=Re t<=65/32, |Im t|<=1/32, |t|<3.

The full bound093 gives |Phi(t)|<2^22 there; it comes from the full theta series and not from samples. Hence, for r=0,...,6,

    |t^r Phi(t)|<3^6*2^22<10^12=B.

The full tail of modes m>=17 is bounded by the same fixed quantity093/098

    EPS=2^25*17^4/8^289.

At each centre outward symmetric errors EPS*32^k are added to ALL coefficients Phi[k], k=0,...,64, BEFORE multiplying the jet by t^r. Thus the tail of modes is kept before forming each moment. Real derivatives of a remainder are not truncated nor is the prefactor of Phi omitted.

## 4. Exact Taylor integration and full remainder

For each r and panel, multiply the jet Phi by the exact polynomial t^r. Integrate the Taylor polynomial up to degree64 on the symmetric panel: only even k contribute, with exact factor 2 h^(k+1)/(k+1). Arb controls all roundings outward.

The bound B controls the whole series of each t^rPhi in the disc. The Taylor error at each point of the panel is at most B*(1/4)^65/(1-1/4). The total length of the panels is2. Hence to EACH compact moment one adds symmetrically

    REM=2*10^12*4^(-65)/(1-1/4)<10^(-24).

This cost pays all omitted terms, not only the next coefficient. Its exact rational expression will be kept in the verifier, without replacing it by the decimal bound.

## 5. Full time tail

For t>=2, the sources093/098 give the bound of the whole theta series

    Phi(t)<64 exp[9t/2-3exp(2t)].

The rational check exp4>54 fixes Phi(2)<2^(-140), and the logarithmic derivative of the majorant is less than -300. Thus for s>=0,

    Phi(2+s)<2^(-140)exp(-300s).

For all r<=6 one can use the bound already valid up to10:

    (2+s)^r<=1024 exp(5s).

Consequently

    0<int_2^infinito t^r Phi(t)dt
       <[1024/295]2^(-140)<2^(-138).

To each moment the POSITIVE interval [0,2^(-138)] is added. Not only a truncated density is integrated nor is this tail replaced by zero.

## 6. Conditions of execution, reading and audit

Before running, the script code and the proof of the two limits103 must be audited. After integrating, check I0,...,I6 strictly positive, and evaluate TEST by outward interval operations. The quantities Kmass and Hmass must have strictly positive enclosures if the quotients are printed; their analytic positivity is already proved103.

Allowed results:

- **P>0:** U_lim(0)>0, which by103 refutes the unique negative/positive crossing of U for some FINITE p,q of the REAL pair. It does not imply negative W.
- **P<0:** it only verifies the pointwise sign of the origin in this limit; it proves neither global crossing, preservation under Schur nor all orders.
- **P contains0:** INCONCLUSIVE, without changing the design during the run.

These seven moments will not be used to launch additional undesigned tests. No campaign will be made and no paper will be modified. The result and its audit will be recorded only after the authorised execution and its independent reproduction.

## 7. Final result of the single designed test

The analytic proof, this design and the code were audited BEFORE the run. Run68812 ended exit0/FULL PASS128 panels; run91737 independently reproduced exit0/FULL PASS128 and the same hash:

    P=[-3.1683047444094325e-13 +/- 2.16e-30],
    U_lim(0)=[-1.35855717857699839e-6 +/- 8.09e-24],
    hash=5090a71fd7dd4ae786a3f785ca8a4c32d6691cf92af912d4e5fffff9e583d080.

The main enclosure separates0 on the NEGATIVE side. Only the sign of the origin in the limit is proved and, by the sequential convergence103, that same sign for sufficiently small fixed q and then sufficiently large p. No quantitative threshold has been given, the global crossing has not been proved and no falsifier has been obtained. No other tests were run nor were parameters adjusted after observing the result. The global consequences and preservation under Schur remain OPEN.

Later chronological note: after this test a global analytic proof for U_lim was obtained, by means of (H/K)'<0; see section9 of POWER_REAL_PAIR_DOUBLE_LIMIT_103.md. That proof makes the test redundant for the sign of U_lim(0), but does not change its design or result. Nor does it by itself transfer the global crossing to the U of finite parameters.

A later analytic extension, section10 of the same source, also proves the global crossing of U_*(q) and Xi_q>0 for ALL q>0 of the limiting pair (J,K), without new tests. p->infinito is kept; the general case of finite p does not follow from that extension.
