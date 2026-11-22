# POWER_BRIDGE_002 — Bridge from powers to PW_N in strong norm

Status: PROVED, independently reviewed in POWER_AUDIT_002.md and POWER_PACKET_SCOPE_AUDIT_009.md. It does not claim positivity of matrices of all orders. Papers untouched.

## Antecedents and difference

Read the project rules, POWER_CONE_001, the powers proposal, the README index (exterior/Pick family and P211 record), grid parts 3/5, crossword (exterior and gauge entries), and the ext/univ definitions of Paper 46. The concrete novelty with respect to the proposal is to settle its density requirement in the form norm via a weighted fractional Sobolev space, without assuming sufficient L² density. No new Pick principle is proposed and no identity is retried as a sign proof.

## 1. Bridge space

Fix s=3/4, t=1/4. For real data rho on X>1 write

    g(y)=exp(5y/4) rho(exp y), y>0,
    ||rho||B=||g||H^t(0,infinito).

The intrinsic Gagliardo norm is used. The standard zero-extension lemma for fractional Sobolev spaces is invoked here, not a new tool: extension by zero from H^t(0,infinito) to H^t(R) is bounded for 0<t<1/2; its boundary term is the fractional Hardy inequality ∫|g(y)|² y^(-2t)dy ≤ C||g||H^t². g(0)=0 is not required. The cross term of the seminorm of the extension is exactly (1/t)∫|g(y)|²y^(-2t)dy.

Let h(y)=Zrho(exp y) for y>0 and zero outside. Then

    exp(sy)h(y)=Σ(n>=1)n^(-5/4) g(y+log n).

Translations to the left on the half-line are contractions for the intrinsic H^t norm: both the simple integral and the double integral of differences are restricted. By summability of n^(-5/4),

    ||exp(s·)h||H^t(0,infinito) ≤ zeta(5/4)||rho||B.

Multiplication by exp(-sy) on the half-line is bounded in H^t; then extend by zero. One obtains simultaneously

    ||h||H^t(R)+||exp(s·)h||L²(0,infinito) ≤ C||rho||B.        (B1)

Via log(2+|tau|)≤C(1+|tau|²)^t, B1 controls the archimedean form norm. Moreover

    |c_h(log n)|≤n^(-s)||exp(s·)h||²L²,

by Cauchy–Schwarz after shifting. The comb sum converges and is bounded by 2ΣLambda(n)n^(-5/4)||exp(s·)h||². The two moments are continuous by Cauchy–Schwarz, since s>1/2. All these estimates admit a bilinear version. Consequently the complete exterior form Q is a continuous bilinear form on B:

    |Q(rho,sigma)| ≤ C ||rho||B ||sigma||B.                    (B2)

This norm separately controls all the terms of Paper 46; it depends neither on cancellations nor on an assumed sign.

## 2. Every PW_N datum belongs to B

If rho=Fourier(h)|_(1,infinito), with h in PW_N, integrating twice by parts gives

    |rho(X)|+|rho'(X)|≤C_h X^(-2), X>=1.

This also follows for rho' because xh(x) is C² inside [-N,N], vanishes at the endpoints, and its one-sided derivatives are finite. The possible boundary terms of the second integration are O(X^-2).

For g it follows that |g(y)|≤Ce^(-3y/4), |g'(y)|≤Ce^(y/4). If 0<delta<1, splitting at R=log(1/delta) shows

    ∫_0^infinito |g(y+delta)-g(y)|²dy ≤ C delta^(3/2).

On (0,R) the derivative bound is used; on (R,infinito) the amplitudes are used. By the characterization via differences, integrating against delta^(-1-2t) shows g∈H^t for t<3/4, in particular t=1/4. The zero extension only requires t<1/2 and adds O(delta), also integrable. Thus PW_N⊂B for each finite N.

## 3. Constructive density of powers with exponents >=32

First approximate g∈H^t(0,infinito) by smooth g_j on [0,infinito), of compact support. It is not necessary for them to vanish at 0. This is standard density obtained by extension, cutoff and convolution; each operation converges in H^t.

Fix B=32-5/4=123/4 and one such g_j. The function q(x)=x^(-B)g_j(-log x) for 0<x≤1 extends smoothly by zero near x=0. Choose polynomials P_k approximating q in C¹([0,1]). They are built by approximating q' uniformly by polynomials and integrating, adjusting the value at 0. Then

    g_jk(y)=e^(-By)P_k(e^(-y)) → g_j(y) in H¹(0,infinito),

because the error and its derivative are bounded by C epsilon_k e^(-By). Hence they converge in H^t. Restoring the weight,

    rho_jk(X)=Σ_n p_kn X^(-(B+5/4+n)).

All exponents are exactly 32+n, n a nonnegative integer. A diagonal selection gives rho_k→rho in B. By B1/B2, both the images Zrho_k in log-Fourier norm and moments and each term of Q converge; Q[rho_k]→Q[rho].

**Bridge theorem:** the finite real envelope of X^-a, a>=32, is dense for all PW_N data in a norm in which the complete exterior universal form is continuous. The approximants need not belong to PW_N: continuity is proved in the ambient space B and the limit does belong to PW_N.

Neither moments nor the edge of the datum rho are corrected: the paper's conditions are imposed on its compact preimage h, not on rho at X=1. Requiring each approximant to be the transform of a compactly supported function would be an additional requirement unnecessary for passing an inequality Q>=0. The correct property is to approximate all integrals, including the polar moments of Zrho; B1/B2 do this explicitly.

## 4. Precise conditional consequence and limit

If positivity of ALL finite sizes of the power kernel is proved, even restricting to the fixed ladder a=32+n, the above density implies Q>=0 on each PW_N. Positivity on each plane of two powers does not suffice: the polynomial approximations use a growing number of terms with arbitrary signs. Nor does this argument produce coercivity with respect to distance to the gauge or a polynomial constant; it only allows transferring nonnegativity.

## 5. Independent verification of polarization

For a,b>1, u=a-1/2,v=b-1/2, the bilinear polar part on e^-uy,e^-vy is exactly

    P_ab=1/[(a-1)b]+1/[a(b-1)].

The kernel proposed in POWER_CONE_001 uses instead

    R_ab=[1/a+1/(a-1)+1/b+1/(b-1)]/(a+b-1).

These expressions coincide exactly: multiplying by a(a-1)b(b-1)(a+b-1), both give (a+b-1)(2ab-a-b). For a=2,b=3, both are 7/12. Hence I find no error in the cross polar term of POWER_CONE_001. The archimedean and comb parts also polarize with the denominator u+v via the identity Re[(u-iτ)^(-1)(v+iτ)^(-1)]=[u/(u²+τ²)+v/(v²+τ²)]/(u+v). The density and continuity B1/B2 are independent of this scalar computation.

## 6. Simpler direct bridge to every compact test

The passage through PW_N is not necessary to transfer nonnegativity. Given a smooth compactly supported real test F, translate it to obtain h supported in (0,L). The complete form is translation invariant. Define for y>0

    u(y)=Σ(n>=1)mu(n)n^(-1/2)h(y+log n),
    rho(exp y)=exp(-y/2)u(y).

The sums are finite: n≤exp L, and each summand is smooth up to y=0 and vanishes for y≥L. Thus G(y)=exp(sy)u(y) is smooth with compact support on the half-line, belongs to B, and

    Zrho(exp y)=Σ(k,n>=1)mu(n)(kn)^(-1/2)h(y+log(kn))=h(y),

by Σ(n|m)mu(n)=1_(m=1). No arithmetic limit appears in this inversion. The density of §3 approximates this rho by combinations of X^(-(32+n)) in norm B; their images converge to h in all pieces of the form.

Therefore it suffices to prove that, for each m, the matrix K_ij=(L(32+i)+L(32+j))/(63+i+j), 0≤i,j≤m, is positive semidefinite. That gives nonnegativity of the complete form on all smooth compact tests, and by the usual density of the form on all window domains. In particular it gives the sign on the primitive subspaces. No gauge, coercivity, external equivalence or spectral reduction is used. The new concrete target is positivity of a single ladder of explicit finite matrices. That sign remains OPEN here.
