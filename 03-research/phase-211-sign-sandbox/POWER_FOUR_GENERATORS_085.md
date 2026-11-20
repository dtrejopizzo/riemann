# POWER_FOUR_GENERATORS_085 — Positivity for four arbitrary admissible generators

Status: **PROVED, certificate of the main run exit0/FULL PASS and independent mathematical/code audit approved; independent reproduction run29132 exit0/FULL PASS16384 and matching hash.** See `POWER_FOUR_GENERATORS_AUDIT_085.md`. Four arbitrary generators, not all orders. Papers untouched.

## 1. Precise obligation and antecedents

Consulted the project rules, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; read080,083,084 and their reviews.083 factorizes exactly the determinant of the complete kernel.084 proves by Rolle that, for an increasing and strictly concave datum f, the condition2f'f'''−3(f'')²>0 implies the positive sign of the Pfaffian on ALL sets of four nodes, not only at confluence.

For the real Phi, put x=u², R(x)=u/M(u), S(x)=uM(u).073/080 already prove R',S'>0,R'',S''<0 for u>1/2.084 identifies exactly the two additional obligations N_R,N_S>0, with

    T_R=2R'R'''−3(R'')²=N_R/(16M⁴u⁶),
    T_S=2S'S'''−3(S'')²=N_S/(16u⁶).

Their exterior is proved for A=u+1/2>=128. Only the interval1/2<=u<=127+1/2 is missing. This source checks THAT continuous obligation with two complete scalar functions; it does not select matrices nor successively prove larger dimensions at isolated rates. The criterion, its inheritance falsifier and the exterior remainders are from084; these identities are not presented here again as an estimate.

## 2. Exact functions and regularization of the endpoint

Use c=M(u),d=M'(u),e=M''(u),f=M'''(u), and D=ud,E=u²e,F=u³f. Then

    N_R=3c²+c(−6D−6E−2F)+3D²+6DE+2DF−3E²,
    N_S=3c²+c(6D+6E+2F)−9D²−6DE+2DF−3E².          (NUMERATORS)

They are evaluated by the SAME entire arithmetic function of080,

    Z~ A[1+(A−1)zeta_deflate(A)]Gamma(A/2)pi^(−A/2),
    A=u+1/2,
    zeta_deflate(A)=zeta(A)−1/(A−1).

The positive constant relating this expression to∫Phi(t)e^(ut)dt does not change M=(logZ)'. The regularization is entire at A=1 and there the expression equals1; the pole of ζ is not evaluated. The endpoint u=1/2 serves only for the analytic enclosure: the exponents of the admissible conclusion are strictly greater than1.

The semantics of deflate and the interval exactness of the jets were verified against the installed API python-flint0.9.0 and official FLINT documentation, as080:

- https://arblib.org/arb_poly.html
- https://flintlib.org/doc/arb_poly/_arb_poly_zeta_series.html

The tests of the regularized value at A=1 and the ordinary identity at A=2 are implementation checks, not the proof of that mathematical identity. There is no truncation of the arithmetic without an error: rigorous evaluation of the complete function is used.

## 3. A bound on M independent of all panels

Fix r=1/32. For centres c0 in[1/2,127+1/2],

    c0+r+1<=128+17/32<129+1/2.

By monotonicity of M and the arithmetic formula at A=130,

    M(t)<=M(129+1/2)
      <1/130+1/129+(1/2)log[130/(2pi)]
      <2/129+(1/2)log27
      <2/129+33/20<2,                               (MEAN-BOUND)

for all the real parameters needed. pi>3, psi(y)<=logy and the negative sign of the arithmetic summand are used for this UPPER bound. The inequality log27<33/10 is obtained from exp(11/10)>3 via a positive rational Taylor sum. An anchor at a larger rate is evaluated first; 2/129 is not applied as a pointwise rational bound at small rates.

Then

    Z(c0+r+1)/Z(c0)<exp[2(r+1)]=exp(33/16)<8.        (RATIO)

The last constant uses log2>2[(1/3)+(1/3)^3/3]=56/81 and3·56/81>33/16. All those comparisons are rational in the verifier.

## 4. Cauchy disc and bound of the TWO numerators

For |z−c0|<=r, positivity and parity of Phi give, as080,

    |Z^(k)(z)|<=2k!Z(c0+r+1)<16k!Z(c0),
    |Z(z)−Z(c0)|<=2rZ(c0+r+1)<Z(c0)/2,
    |Z(z)|>Z(c0)/2.

Hence the quotients and logarithmic derivatives are analytic on the whole disc and

    |Z^(k)/Z|<32k!, k=1,2,3,4,
    |M|<32, |M'|<1100, |M''|<72000, |M'''|<8000000.

For the last derivative one uses exactly

    M'''=Z''''/Z−4Z'Z'''/Z²−3(Z''/Z)²
                        +12(Z'/Z)²Z''/Z−6(Z'/Z)^4.

With the ratios32,64,192,768, the absolute bound is7115520<8000000. The preceding derivatives cost1088<1100 and71872<72000.

Since |z|<128, put

    C*=32, D*=128·1100,
    E*=128²·72000, F*=128³·8000000.

The same bound serves for BOTH numerators of NUMERATORS:

    |N_R|,|N_S|
      <3C*²+C*(6D*+6E*+2F*)+9D*²+6D*E*+2D*F*+3E*²
      =8901242950707612672<10^20=:B.                 (DISK-BOUND)

This bound includes all cancellations as a safe absolute error; it is not an evaluation of the form on complex data nor an assumption of the sought sign.

## 5. Continuous certificate fixed before executing

The partition consists of16384equal intervals of[1/2,127+1/2]. Its radius is h=127/32768 and its exact centres are

    c_j=[16384+(2j+1)127]/32768, j=0,...,16383.

For EITHER of the two functions N(z), use the Taylor polynomial up to degree40 at the centre. Cauchy and DISK-BOUND give the complete error

    epsilon=B(h/r)^41/(1−h/r),
    h/r=127/1024,
    epsilon=10^20(127/1024)^41/(1−127/1024)<10^(−16). (TAIL)

This EXACT fraction is used, not the decimal upper bound10^(−16), in each assert. If N_k=N^(k)/k! are the normalized coefficients, the sign is certified on the WHOLE panel by verifying

    N_0.lower−Σ_(k=1)^40 |N_k|.upper h^k−epsilon>0.   (PANEL)

PANEL is required for N_R and for N_S on EACH interval. Positivity at centres is not used as if it sufficed to cover the compact set; the tail TAIL covers all points between them and the endpoints.

## 6. Implementation and status of the run

Code: tools/power_four_turan_compact_085_verify.py. Parameters fixed before executing:512bits, cap45,16384panels, r=1/32,B=10^20,degree40. cap45 keeps logZ up to degree44, M up to43 and M''' up to40; both numerators have series precision at least41. Finiteness of ALL coefficients0,...,40 and the value E0>0 before logE are required.

Jets are computed only at EXACT real centres. The interval-in-parameter representation that lost dependence near the pole in the attempts080 is not used again. The errors of the special functions are kept as rigorous balls; the rest of the interval is paid by the analytic TAIL, not by a jet over a wide ball. The parameters are not modified according to diagnostic values.

The fixed run61911 ended exit0/FULL PASS: analytic constants and regularization, and BOTH signs on ALL16384panels. The script was not modified during its run and no parameter was tuned. The SHA256 of the reproducible verifier is

    4916689a48baf3164b8e99ff8ff7973dbd505367cf9ee46b17b7efc9845abf46.

The common integer bound printed is8901242950707612672. The tail printed is exactly the fraction TAIL, not a floating estimate. The file.sha256 fixes the same version for independent reproduction.

## 7. Splicing and complete conclusion for four generators

The compact certificate FULL PASS combined with OUTER-TURAN084 proves T_R,T_S>0 on ALL u>=1/2. The global Rolle criterion084 gives Pf(A_R),Pf(A_S)>0 for any four distinct nodes ui>1/2. The factorization083 gives detK>0; the lower minors080 complete the positive definiteness of the COMPLETE kernel for FOUR distinct exponents A_i>1. Repeated exponents are grouped and give a redundant positive semidefinite matrix, with positive energy on the non-zero represented function.

Positivity includes ARCH, polar and ALL arithmetic contacts by the exact kernel identity of CONE001. The diagonal congruence of the exterior map keeps the conclusion for any real combination of four powers with exponents>1.

The result does NOT imply five generators, all orders, the complete linear envelope nor a new time window. No paper is modified. The global sign of Paper47 remains OPEN.
