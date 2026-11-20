# POWER_SHIFTED_WRONSKIAN_092 — Real zero of the elimination determinant

Status: **PROVED; final reading and independent audit passed.** See `POWER_SHIFTED_WRONSKIAN_AUDIT_092.md`. The single pointwise certificate087 is reused without modification. No new theta truncation, mesh, precision or explored parameter. Papers untouched. The result only limits an invertible elimination chart: it does not contradict the sign of W nor prove an unavoidable pole of the solution or of all coefficients of an alternative ODE.

## 1. Difference and consultation of antecedents

Consulted the project rules, ROUTES-TRIED-INDEX/README, R162_2300_MASTER_GRID and CROSSWORD-TO-D, and the sources077,087–090.087 decided the original four-density Wronskian at the origin;089 proved its global sign.090 does not allow inheriting the next sign only from a Turán inequality. The new object here is the determinant **of the elimination of two unknowns**, with its exact identity as a shifted Wronskian. A concrete premise of that elimination is checked using already certified jets, not another case of the form W.

## 2. Object and exact determinant

All derivatives in this section are in t>0. Fix

    w=t Phi, v=−Phi', L=D_t²,
    p=V', V=−logPhi, A=w''/w, B=v/w,
    k=B'>0, J=(A'/k)'>0,
    b=k'/k, j=J'/J, m=2w'/w.

077 controls k,J strictly positive. Let a=M'(0)>0,c=1/a and K''=v−cw, with K(0)=K(infinity)=0. For F=K/w,

    F''+m F'+AF=s, s=B−c.

The monic operator annihilating(1,B,A) is

    D3=D³−(2b+j)D²+(b²+bj−b')D.

Write H=m+2b+j. Substituting the ODE gives exactly

    Y=D3F=T0+UF'+Vc F,
    T0=k−Hs,
    U=Hm+b²+bj−b'−m'−A,
    Vc=HA−A'.

Then Y'−T0'−Us=(U'−mU+Vc)F'+(Vc'−AU)F. Inverting this2×2 system requires

    Delta=U(Vc'−AU)−Vc(U'−mU+Vc) != 0.

The relevant exact identity is

    Delta=−W_t(w'',v'',w'''')/[w³ k² J].          (SHIFT)

Proof: the homogeneous solutions of f''+mf'+Af=0 are h1=1/w,h2=t/w and W(h1,h2)=w^−2. The transformation(h,h')→(D3h,(D3h)') has determinant−Delta. By row elimination of the Wronskian,

    W(D3h1,D3h2)=W(1,B,A,h1,h2)/W(1,B,A).

Here W(1,B,A)=k²J. Multiplying the five columns by w contributes w^−5; moving the columns(1,t) to the front requires six transpositions, positive sign. Expanding along its first two rows leaves W(w'',v'',w''''). Thus W(D3h1,D3h2)=W(w'',v'',w'''')/(w^5 k²J)=−Delta/w², which proves SHIFT.

## 3. Origin: only the already certified intervals087

Write Phi(t)=Phi(0) sum a_r t^(2r), a0=1. By parity and the change lambda=t²,

    Wshift(t)=W_t(w'',v'',w'''')
             =8 Phi(0)³ t^6 [D0+O(t²)],

    D0=det [[6a1,−24a2,120a2],
            [20a2,−120a3,840a3],
            [84a3,−672a4,6048a4]]
       =−161280(6a1a3a4−8a2²a4+3a2a3²).

The row factors are correctly normalized derivatives: for three odd functions t f_i(t²), W_t=8t^6 W_lambda(f_i). Only even derivatives of Phi up to order8 are needed;087 already certified up to10 with the WHOLE theta tail and the prefactor pi exp(5t/2).

The verifier092 imports via runpy the verifier087 **without editing it** and evaluates only the preceding polynomial with the same outward rational arithmetic. It obtains and verifies exactly

    −56488961026 < D0 < −56488961025.

By analytic continuity, Wshift(t)<0 for all sufficiently small t>0. No uncertified radius is assigned to that neighbourhood.

## 4. Exterior with controlled remainder, not only a formal leading term

Set y=pi exp(2t). The full bounds of088, valid for t>=1,y>=21, give

    |V^(r)(t)−2^r y| <=65, r=1,...,6.            (JET)

Indeed the first mode is a product of exp(−y+9t/2) by(1−3/(2y)). The derivatives of the logarithm of the latter factor are bounded by 2^r sum n^(r−1)/14^n<2^r, and088 bounds by2E<1 the derivatives up to6 of the logarithm of the correction of ALL remaining modes. The linear term9t/2 only affects r=1, where65 is also more than enough.

After factoring Phi out of the three columns, Wshift/Phi³ is a polynomial P(t,p1,...,p6), with p_r=V^(r). It is defined explicitly as the determinant of rows0,1,2 of derivatives of

    g1=t(p1²−p2)−2p1,
    g2=p1³−3p1p2+p3,
    g3=t(p1^4−6p1²p2+3p2²+4p1p3−p4)−4g2,

where the formal derivation is Dt=1,Dp_r=p_(r+1). The degree in t is<=2 and the total degree in the p_r is<=9. Its homogeneous part of degree9 is W(t p1²,p1³,t p1^4), exactly

    −2p1^6(2p1²p2+t p1²p3−t p1p2²−t²p2³).

Substituting p_r=2^r y+e_r one concludes

    P=4096(2t²−1)y^9+Q(t,y,e1,...,e6),

where each monomial of Q has degree in y<=8 and degree in t<=2. This is a polynomial identity, not a numerical approximation. Define the explicit finite constant

    Cstar=sum |coefficient of Q| ·65^(total degree in e).

By JET, for t>=1,y>=21,

    |Q| <= Cstar t² y^8.

Since 2t²−1>=t², if y>Cstar/4096 then P>0. There is therefore a full tail on which **Wshift>0**. There is no need to compute an optimal threshold or examine points; Cstar is defined by an exact finite polynomial and the remainder includes all theta modes via JET.

## 5. Precise consequence and limits

Wshift is continuous, negative near0 and eventually positive. It has at least one zero t*>0. Since w,k,J are strictly positive there, SHIFT implies Delta(t*)=0.

Consequently, the elimination formulas that divide by Delta are not globally defined as an invertible chart. **This does not prove that their coefficients have non-removable poles**: their numerators may also vanish. The real function K remains smooth, and other charts, operators, partitions or arguments without that division remain available. A sign proof by those means is not excluded. No new sign of W, number of generators, T or all orders.

Additional approved qualification: the two images Y1=D3(1/w),Y2=D3(t/w) are smooth and satisfy W(Y1,Y2)=−Delta/w². This Wronskian is not identically zero, but it has an interior zero. There cannot exist a monic homogeneous ODE of order2, with coefficients continuous on the WHOLE half-line, containing both images simultaneously: if Y''=beta Y'+alpha Y, the elementary identity W'=beta W prevents an isolated or partial zero of a Wronskian that is not identically zero. This excludes globally removing all coefficients of the common universal equation while keeping those two solutions; it does not exclude cancellations for the particular solution K, a different inhomogeneous equation, another order or representation.

Reproducible verification: `python3 tools/power_shifted_wronskian_092_verify.py` from phase211. The script prints the rational endpoints and runs the asserts above; it does not alter087.
