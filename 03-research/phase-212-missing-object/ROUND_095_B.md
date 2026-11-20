# No self-energy constant repairs the cyclotomic finite part

Status: **PROVED**, with independent review of the proof and of its scope. An auxiliary form is studied, not the sign of the complete form.

## Cross-check

1. Antecedents: `ROUND_095_A.md`, especially §§2–4, and the record "Index-dependent cyclotomic cutoff" in Part V of the master index. The first proves a negative value of J_sc; it does not prove that J_sc/A has no lower bound. The second admits the freedom to change the constant scale of the cutoff.
2. New claim: inf_(β∈K_Z, β≠0) J_sc(β)/A(β)=−infinity, where K_Z is the integer carrier. This excludes J_sc+cA PSD for every real constant c, not only for c=0.
3. Operation: weight the prime dilations by 1/p, stopping the sum when its reciprocal mass reaches one. Thus A stays bounded while the minimum scale of the crossings tends to infinity. The passage from rational to integer coefficients is justified. The independent gate approved only this class obstruction.
4. Connection: changing the cutoff ε to λε, with fixed λ>0, changes the finite part to J_sc−Alogλ. The result prevents using any of those finite parts as a universal PSD piece in a splitting of the complete form. It does not exclude other counterterms nor a joint compensation with the remainder.

## 1. Forms and data already proved

Use the test b=b_6 and the dilations D_p of `ROUND_095_A.md`. Denote by K_R the real kernel of the constraints Σ_jβ_j=0, Σ_jjβ_j=0 and Σ_jβ_jv_r(j)=0 for each prime r, always on finitely supported sequences; K_Z is its subset of integer sequences, the carrier K of 095-A. For finitely supported sequences, set

    G(u,v)=Σ_(i,j≥1)gcd(i,j)u_i v_j,    A(u)=G(u,u),
    B(u,v)=−Σ_(i,j≥1)gcd(i,j)u_i v_j log((i+j)/gcd(i,j)),
    J_sc(u)=B(u,u).

The identity gcd(i,j)=Σ_(d|i,d|j)φ(d) gives

    A(u)=Σ_d φ(d)(Σ_(d|i)u_i)²>0 for finitely supported u≠0.

Indeed, if L is the largest nonzero index, the summand d=L is positive. Hence the ratio J_sc/A is well defined.

The data of 095-A are

    A(b)=14,    J_sc(b)<3,
    A(D_p b)=14p,    J_sc(D_p b)=pJ_sc(b),
    G(D_p b,D_q b)=14 for distinct primes p,q>6,
    B(D_p b,D_q b)=−14log max(p,q)+E_pq,
    |E_pq|<1152 for those same primes.

The equality for G uses the same identity gcd(pi,qj)=gcd(i,j) already proved. All crossings and diagonals are of the complete forms A and J_sc; no terms are omitted.

## 2. Finite selection of primes with controlled reciprocal mass

Only the elementary divergence Σ_(p prime)1/p=infinity is needed. A sufficient proof is the following. If that sum were finite, for every N,

    Σ_(n≤N)1/n ≤ ∏_(p≤N)(1−1/p)^(−1)

would be uniformly bounded: the logarithm of the product is at most 2Σ_(p≤N)1/p, since −log(1−x)≤2x for 0≤x≤1/2. The product inequality is obtained by expanding finitely many positive geometric series; it includes all integers up to N. It contradicts the divergence of the harmonic sum. Removing finitely many primes preserves divergence.

Fix an integer Q>6. Take, in increasing order, primes p>Q until the sum of their reciprocals first reaches one; let S_Q be that finite set. Define

    s=Σ_(p∈S_Q)1/p,    r=Σ_(p∈S_Q)1/p²,
    u=s²−r=Σ_(p≠q in S_Q)1/(pq).

By the stopping rule,

    1≤s<1+1/Q<2,
    r≤s/Q<2/Q,
    1/2<u<4.

The lower bound uses Q>6 and s²≥1. The sum defining u counts ordered pairs.

## 3. Bounded self-energy and finite part without lower bound

Set

    γ_Q=Σ_(p∈S_Q)(1/p)D_p b.

It is a nonzero rational test of K_R; the supports of the dilations are disjoint. Expanding both forms, with all ordered pairs,

    A(γ_Q)=14(s+u),    0<A(γ_Q)<84,
    J_sc(γ_Q)≤J_sc(b)s+(1152−14log Q)u.

If log Q>100, the coefficient of u is negative. Using s<2 and u>1/2,

    J_sc(γ_Q)<6+(1152−14log Q)/2
               =582−7log Q<0.                         (NEG)

Since A(γ_Q)<84 and the bounded numerator in (NEG) is negative,

    J_sc(γ_Q)/A(γ_Q)<(582−7log Q)/84 → −infinity.

To obtain integer tests, multiply γ_Q by the integer M_Q=∏_(p∈S_Q)p. The vector β_Q=M_Qγ_Q is nonzero, integer and satisfies the same linear constraints. Both energies are multiplied by M_Q², so their ratio does not change. One concludes

    inf_(β∈K_Z, β≠0) J_sc(β)/A(β)=−infinity.

No dimension is fixed and no numerical sweep is used: each Q defines a finite test by an exact rule, whose termination has been proved.

## 4. Every correction cA and every constant scale of the cutoff

Let c be real and fixed and C=max(c,0). Choose an integer Q with log Q>100+12C. By (NEG) and A(γ_Q)<84,

    J_sc(γ_Q)+cA(γ_Q)
      ≤J_sc(γ_Q)+C A(γ_Q)
      <582−7log Q+84C<−118.

After multiplying by M_Q² one obtains a negative integer test of J_sc+cA. No real constant c produces PSD on the whole carrier.

The regularizer already recorded satisfies, for each fixed finite test,

    Q_ε(β)=−A(β)log ε+J_sc(β)+o(1).

For fixed λ>0, replacing ε by λε and keeping the subtraction A log ε gives

    lim_(ε↓0)[Q_(λε)(β)+A(β)log ε]
       =J_sc(β)−A(β)logλ.

These are exactly corrections cA with c=−logλ. Therefore no constant choice of the cutoff scale turns that finite part into a PSD form on the whole carrier.

## Result

**What was proved:** J_sc is not bounded below by any constant times A, even on integer tests annihilating the two moments and all valuation rows. The negativity of 095-A is not repaired by choosing another self-energy constant or a different fixed scale of the same cutoff.

**What failed and why:** with reciprocal mass approximately one, the diagonals and A remain bounded, but the crossings of J_sc contain a negative term proportional to the logarithm of the minimum scale. This is an obstruction to the class of cA repairs, not to every counterterm.

**Concrete next step:** a reopening must give a different compensation, dependent on the crossings and with an exact identity for the complete form. This proof does not provide it nor claim that it exists. The sign of a or of the remainder a−J_sc is not decided, J_sc≤a is not refuted and test-dependent scales are not excluded. No positive step on a has been taken to which the target's falsifier battery could be applied; an auxiliary repair has been refuted. The global sign remains open.
