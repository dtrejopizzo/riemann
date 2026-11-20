# POWER_PEANO_MONOTONICITY_OBSTRUCTION_091 — The Peano kernel is not monotone

Status: **PROVED; source and independent review approved.** See `POWER_PEANO_MONOTONICITY_AUDIT_091.md`. A very specific sufficient criterion for the anchored minor is refuted: global monotonicity of Pi(s)/s for all sets of four nodes. The failure occurs for the SAME real Phi and nodes sufficiently close to any t0>0. The sign of the final integral, the new determinant, an alternative implication from R4 and W are not refuted. Papers untouched; no campaigns.

## 1. Consultation and precise difference

Consulted the project rules, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; cross-checked065 and086–090. The search for Peano, cofactor prefixes and monotonicity of this kernel did not find this object in the corpus nor in the three records.

The new proposal used the single crossing of zeta=v−cw and its vanishing moment to pay for the determinant with a positive primitive K. The aim was to deduce its sign from a monotonicity of Pi/s. Here it is proved that this monotonicity fails locally for the real data, even though the previous four-density system is ECT. It is a NO-GO for the declared monotonicity criterion; not for the integration-by-parts strategy nor for every compensation estimate.

## 2. Real data and exact integral representation

Set w(t)=tPhi(t), v(t)=−Phi'(t), a=M'(0)>0 and c=1/a. In this source K denotes the positive ODD primitive

    zeta=v−cw,
    K(t)=int_t^infinito(s−t)zeta(s)ds, t>=0,
    K''=zeta, K(0)=0.

It is not the EVEN K of078. All relevant tails decay faster than any exponential. The real moment identities give

    int_0^infinito s zeta(s)ds=0.

Indeed int s v=int Phi and int s w=int s²Phi=a int Phi, on the half-line. By077, B=v/w=p/t is strictly increasing, so zeta has a single crossing from negative to positive; call it b. This representation and that crossing are not presented as a new result.

Fix four positive nodes t1<t2<t3<t4. Define the cofactors of the last column

    ell_i=(−1)^(i+4)det[(w(t_j),v(t_j),w''(t_j))]_(j≠i),
    Pi(s)=sum_(i=1)^4 ell_i(s−t_i)_+.

Expansion along that column and Fubini give exactly

    det[w,v,w'',K]_(t1,t2,t3,t4)
       =sum_i ell_i K(t_i)=int_0^infinito zeta(s)Pi(s)ds.

Interchanging the finite sum and the integral is legitimate: Pi grows at most linearly and zeta has the declared tails. Using the vanishing moment,

    det[w,v,w'',K]
       =int_0^infinito s zeta(s)
                   [Pi(s)/s−Pi(b)/b]ds.             (PEANO)

A decreasing function Pi(s)/s would give a nonpositive sign in PEANO; an increasing one would give a nonnegative sign. The proposal examined needed one of those global monotonicities, for ALL sets of nodes. It is shown below that neither holds.

## 3. The real Wronskian of three functions is positive

The identities of086 are

    v/w=B=p/t,
    w''/w=A=p²−q−2p/t,
    k=B'>0, J=(A'/B')'>0.

Hence, in the column order used here,

    W3(t)=W(w,v,w'')(t)
          =w(t)³ W(1,B,A)(t)
          =w(t)³ B'(t)²J(t)>0, ALL t>0.           (REAL-W3)

The order(1,A,B), whose sign would be the opposite, is not used. This check fixes the signs of the cofactors and presupposes no new five-column datum.

## 4. Taylor lemma for four equally spaced nodes

Fix ANY t0>0 and take

    t_i=t0+(i−1)epsilon, i=1,2,3,4, epsilon>0.

For three fixed offsets r1<r2<r3, the Taylor expansion of the rows gives

    det[(w,v,w'')(t0+r_j epsilon)]_(j=1)^3
      =epsilon³ W3(t0)
          ·Vandermonde(r1,r2,r3)/(0!1!2!)+O(epsilon^4).

Real smoothness allows the indicated remainder. The first nonzero orders use derivatives of orders0,1,2, whose sum is3. The determinant of their coefficients is the Vandermonde of the offsets and the derivative columns produce precisely W3. Repeated lower-order terms vanish.

Omitting respectively the offsets0,1,2,3 from the set(0,1,2,3), the Vandermondes are

    2, 6, 6, 2.

Dividing by0!1!2!=2 and adding the cofactor signs gives

    (ell_1,ell_2,ell_3,ell_4)
      =epsilon³ W3(t0)(−1,3,−3,1)+O(epsilon^4).      (COFACTORS)

The factor is not epsilon³W3/2: the2 of the adjacent offsets already cancels the factorial. The cofactors were not normalized by a global Vandermonde.

## 5. Two intervals with derivatives of opposite signs

Outside the nodes, differentiating the expression of Pi gives

    (Pi(s)/s)'=[sum_(t_i<s)ell_i t_i]/s².          (PREFIX)

On(t1,t2) the numerator is

    ell_1t_1=−t0W3(t0)epsilon³+O(epsilon^4)<0

for epsilon sufficiently small. On(t2,t3) the numerator is

    ell_1t_1+ell_2t_2
       =2t0W3(t0)epsilon³+O(epsilon^4)>0.

Both signs are strict by t0>0 and REAL-W3. Thus, for ALL t0>0, there exists epsilon0(t0)>0 such that for0<epsilon<epsilon0,

    Pi(s)/s decreases strictly on(t1,t2),
    Pi(s)/s increases strictly on(t2,t3).

In particular it is not globally monotone, in either direction. It is an analytic existence proof of families of nodes; numerical nodes were neither chosen nor searched for.

## 6. Exact scope and live residue

The result uses the REAL Phi, not just an auxiliary class: REAL-W3 is already proved in086. Nor does it need to refute the real ECT R4 of089, which remains valid. The cancellation ∫s zeta=0 and the single crossing remain correct tools; what fails is replacing the problem by global monotonicity of Pi/s for all nodes.

The PEANO integral could still have the required sign via compensation between the intervals where Pi/s rises and falls, a comparison with the position and mass of the crossing b, or a different kernel. Nothing proved decides that sign. It is not claimed that the datum R4 is insufficient for ALL possible arguments nor that the five-column datum is impossible. The anchored minor and T_h of the real Phi remain OPEN.

It does not change the already proved W positivity085 nor the real step S_G''<0 of090. No new W counterexample, global closure nor certificate campaign is obtained.
