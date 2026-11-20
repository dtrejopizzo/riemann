# POWER_CONFLUENT_FOUR_005 — Four confluent poles: the polar rescues the sign

Status: PROVED exact certificate; independently reviewed. It does not prove four arbitrary rates. Papers untouched.

Antecedents: POWER_CONFLUENT_004, POWER_POLYNOMIAL_003, pole motion and weighted control of POWER_AUDIT_004. New reason: in dimension four isolated archimedean positivity fails; the polar matrix is kept explicitly before comparing. The dimension-three proof is not extrapolated while ignoring that sign change.

## 1. Exact matrices

Fix u=63/2 and phi_j(y)=sqrt(63)e^-uy L_j(63y), 0≤j≤3, an orthonormal Laguerre basis. The archimedean matrix is Toeplitz with first row (d,b,c,e), where

    d=psi(16)−log pi,
    b=(63/4)psi'(16),
    c=b+(3969/16)psi''(16),
    e=b+(3969/8)psi''(16)+(250047/96)psi'''(16).

The general formula of the fourth coefficient is 2up'+4u²p''+(4/3)u³p''', with p=[psi((u+.5)/2)−log pi]/2. It is derived by differentiating the same kernel [p(u)+p(v)]/(u+v) and conjugating by Laguerre.

The exact polar moments are

    A_j=sqrt(63)(−32)^j/31^(j+1),
    B_j=sqrt(63)(−31)^j/32^(j+1),
    Polar_jk=A_j B_k+B_j A_k.

Thus the whole polar matrix is rational, without roots after multiplying the moments.

## 2. Rational intervals

Use J,E and H defined in POWER_CONFLUENT_004, all with 24 terms. The bounds 223/71<pi<22/7, H256−log256−1/256<gamma<H256−log256 give

    dlo=H15−H256+8J(1/3)−J(15/29)−E(15/29),
    dhi=H15−H256+8[J(1/3)+E(1/3)]+1/256−J(76/147).

For r=2,3,4 define

    Sr=Σ(k=16..255)k^-r,
    lo_r=Sr+1/[(r−1)256^(r−1)],
    hi_r=Sr+1/[(r−1)255^(r−1)].

Then b lies between (u/2)lo_2 and (u/2)hi_2; c between blo−(u²/2)hi_3 and bhi−(u²/2)lo_3; e between blo−u²hi_3+(u³/2)lo_4 and bhi−u²lo_3+(u³/2)hi_4. These are exact rational intervals.

Take the rational center r=(1596/1000,1016/1000,−16/1000,349/1000) and T(r) the Toeplitz of order four. Applying the previous intervals proves that the error between the true archimedean matrix and T(r) has maximal absolute row sum less than 1/200. By symmetry its norm is less than 1/200.

The exact LDL of T(r)+Polar−(1/4)I has four positive pivots; the attached verifier checks it exclusively with Fraction. Alternatively, the polar is also Toeplitz: if (a,b0,c0,e0) is the first row of T(r)+Polar, the rational congruence by the vectors (1,0,0,1),(0,1,1,0),(1,0,0,−1),(0,1,−1,0) separates the two blocks

    [[a+e0−1/4,b0+c0],[b0+c0,a+b0−1/4]],
    [[a−e0−1/4,b0−c0],[b0−c0,a−b0−1/4]].

Both have positive rational first pivot and determinant, also checked in the verifier. Hence

    Arch+Polar > (1/4−1/200)I = (49/200)I.                  (AP4)

## 3. Comb control and complete result

The previously audited weighted control of four poles gives ∫e^(uy)|h(y)|²dy≤32552||h||² for this confluence. By Cauchy–Schwarz, |c_h(log n)|≤sqrt(32552)n^(-u/2)||h||². Using Lambda(n)≤n, 2sqrt(32552)<362, (u−1)/2>15, and integral comparison,

    |Comb|≤362 Σ(n>=2)n^-15 ||h||²
           ≤362[2^-15+2^-14/14]||h||²
           =362/28672 ||h||² <(13/1000)||h||².

Together with AP4 this gives

    W[h] > (49/200−13/1000)||h||² > (1/5)||h||².

This theorem holds on span{e^-31.5y,ye^-31.5y,y²e^-31.5y,y³e^-31.5y}. By continuity in a basis of divided differences it persists in some neighborhood of confluent rates; no explicit radius is obtained here. It does not prove positivity of all quadruples a>=32: the monotonicity used for ARCH does not automatically include the polar term.

## 4. Exact falsifier of positive ARCH at order four

For the Laguerre vector v=(1,−1,1,−1),

    Arch[v]/||v||² = d−(3/2)b+c−(1/2)e <−1/10,

by the same rational intervals. Thus the method «ARCH positive for any number of poles with rates >=31.5 and small remainder» is refuted already in dimension four. It is not negativity of the complete form: AP4 explicitly shows the polar compensation.
