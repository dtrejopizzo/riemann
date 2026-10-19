# R161_002 — The square, its loss of orientation, and the next lemma

## 0. Verdict

The finite anomaly identity `(PC)` gives a canonical sum×product square, but that square is **sign-blind**. It sees
`A_M^2`, not `A_M`. This is a structural negative result for the most natural construction, not a closure of D.

The phase nevertheless leaves a sharper residual than `O-D4.1`: the missing datum is an **orientation of the Poisson
boundary defect**. A norm cannot supply it; an oriented mixed pairing might.

## 1. The canonical square

Write

```
R_M,N := {X,E_N} - L_M^*E_N - JH_M,N - H_M,N Fcal.
```

By `R161_001`, Theorem 3.1,

`R_M,N=S_N A_M Fcal`.

Hence the most direct positive candidate is

```
Q_M,N(F) := ||R_M,N F||^2
          = ||S_N A_M Fcal F||^2 >= 0.                              (SQ)
```

It is a genuine square and its unexpanded expression contains Poisson and Chebyshev jointly.

**Theorem 1.1 (orientation loss; PROVED).** `(SQ)` is invariant under replacing `A_M` by `-A_M`. Therefore no
argument using only the nonnegativity, vanishing or size of `Q_M,N` can prove the sign of `A_M`.

*Proof.* The right side is the squared norm of `S_N A_M Fcal F`, unchanged when `A_M` is multiplied by `-1`. ∎

This is the exact analogue of replacing a self-adjoint operator by its square. It passes the separation gate but fails
the orientation gate of the blueprint.

**Corollary 1.2.** Every construction obtained from finite sums or nonnegative integrals of the squares
`||R_M,NF||^2`, with coefficients independent of the sign of `A_M`, is sign-blind.

## 2. The oriented pairing

The first expression retaining orientation is

```
B_M,N(F) := Re <R_M,N F, S_N Fcal F>
          = <A_M G, S_N^*S_N G>,       G=Fcal F.                    (OR)
```

The equality follows from `(PC)`, self-adjointness of `A_M`, and commutation of the translation multipliers
`A_M` and `S_N^*S_N`.

`S_N^*S_N` is positive, but this fact alone does **not** make `(OR)` nonnegative: two commuting self-adjoint operators
have a positive product only when their spectral signs agree, and the sign of `A_M` is the target.

On all of `L^2(R)`, positivity of `(OR)` for every `F` is equivalent to nonnegativity of the multiplier `A_M` wherever
the Dirichlet polynomial `D_N(1/2+i tau)` is nonzero. Its zero set has measure zero unless the polynomial vanishes
identically, so the range of `S_N` is dense. The unrestricted statement is therefore exactly the sign problem, and
is false for finite `M` on the full line because the sharp semilocal bottom is negative.

## 3. Why the uncompressed window version is not new

If `F` ranges over a window and arbitrary finite dilation coefficients are allowed, the ranges of the operators
`S_b` span a larger interval. `R160_D4_R2`, Thm 5.1 identifies positivity on that span with positivity at a shifted
window. Thus an oriented pairing based only on uncompressed dilations returns to the window-shift closure.

The only possible escape inside this architecture is to keep the **boundary compression** before taking the square or
the oriented pairing.

Let `P_T` be multiplication by `1_(-T,T)` and `Pi_T` the orthogonal projection onto the primitive subspace `P_T`.
Define the two boundary leakages

```
C_T       = (1-P_T) Fcal P_T,
C_T^(N)   = (1-P_T) S_N Fcal Pi_T,
```

and the compressed Poisson defect

`E_N,T=P_T(S_NFcal-JS_N)Pi_T`.

These operators contain information lost by the span argument: `P_T` does not commute with `Fcal`, and truncating a
translated vector at the boundary is not a mere enlargement of the window.

## 4. The phase-161 residual

**Later status.** The positive-weight branch below is killed by Theorem 8.1, and `R161_004` closes its scalar
Stieltjes and positive divisor-fibre successors against the existing corpus. The surviving target is `L161.3` in
`R161_005`--`R161_006`; the statements below are retained to record the route by which it was reached.

**Problem SP-161 (oriented boundary lemma; OPEN).** Find explicit nonnegative weights `w_N(T)` and a finite-contact
choice `M(T)>=exp(2T)` such that, for every real `F in P_T`, the compressed version of `(PC)` gives

```
a_T(F)
 = sum_N w_N(T) Re <R_M(T),N F, S_N Fcal F> + B_T(F),              (SP161)
```

where `B_T(F)` is a sum of proved nonnegative boundary-leakage squares built from `C_T`, `C_T^(N)` and where the
coefficient of `a_T` is strictly positive. The identity and positivity of `B_T` must be proved without assuming the
sign of `a_T`.

This formulation is deliberately strict:

- replacing `Re<.,.>` by a norm square fails by Theorem 1.1;
- dropping `P_T` returns to the window-shift theorem;
- choosing the weights by solving the spectral problem for `A_T` installs the answer;
- a Douglas factorisation of `A_T` is EQUIV and does not count;
- an estimate with a positive margin cannot be uniform in `T`.

## 5. A more falsable first lemma

Before `(SP161)`, prove or refute the following finite statement.

**Lemma target L161.1 (OPEN).** There exist canonical weights `w_N(T)>=0`, depending only on the integer lattice and
the support projection, for which the *interior* terms of the weighted sum of `(PC)` telescope and leave

```
sum_N w_N(T) B_M,N(F) = a_T(F) + boundary_T(F),
```

with `boundary_T(F)>=0` by Plancherel/Poisson.

The weights are required to be canonical before `Lambda` is inserted. Arithmetic may enter only through the support
theorem `H_M,N|_(k<=N)=0`. This ensures:

- for ζ, the hyperbola interior cancels;
- for every falsifier, Theorem 4.1 of `R161_001` leaves its explicit `delta_a(k)` term;
- positivity, if it exists, comes from the additive boundary rather than being imposed through `A_T`.

## 6. Immediate tests for L161.1

1. **Two-point test:** use a smooth approximation to two narrow packets separated by `log 2`. Any candidate must
   reproduce the exact coefficient `2log 2/sqrt 2` with the correct negative sign in `a_T`.
2. **Sign-flip test:** replace `Lambda(2)` by `-Lambda(2)`. The interior defect must change by `-2log 2`; if the proposed
   boundary square is unchanged, the identity cannot hold.
3. **Xi_a test:** the first defect must be `log 2(2^a+2^-a-1)` and must not be absorbable into a gauge constant.
4. **Deletion/amplification test:** a single coefficient change must survive; otherwise the construction is class-level.
5. **Large-T test:** no proof may divide by a spectral gap or use a fixed finite family of `N`.

## 7. Research decision

Phase 161 should continue only along one of these two branches:

1. construct the canonical telescoping weights and prove a positive boundary formula; or
2. prove a no-go theorem that every canonical positive weighting of the finite Poisson defects is even in `A_M` and
   therefore sign-blind.

Both outcomes add information. Replacing `(SQ)` by a more elaborate norm without demonstrating orientation does not.

## 8. Positive-weight tail no-go

The proposed positive telescoping has an arithmetic obstruction even before Poisson is estimated.

For simplicity take `M>=k` and write `h_N(k)` for the coefficient of the hyperbola tail `H_M,N` at `k>N`. If `p` is
prime, then

```
h_N(p)=log p,   N<p,
h_N(p)=0,       N>=p.
```

**Theorem 8.1 (no positive algebraic telescoping; PROVED).** Let `w_N>=0` and suppose some `w_N` is nonzero. Then the
coefficientwise sum `sum_N w_N H_M,N` is nonzero and has a strictly positive coefficient at every sufficiently large
prime `p` (with `M>=p`):

`[p](sum_N w_NH_M,N)=log p sum_(N<p)w_N>0`.

Therefore no nonnegative weighting of the hyperbola tails cancels them algebraically. Any cancellation in L161.1
must use the Poisson boundary term, or else use signed/discrete-derivative weights.

*Proof.* Choose `N_0` with `w_N0>0` and a prime `p>N_0`. For every `N<p`, the only factorisation `dm=p` with `m<=N`
is `d=p,m=1`, which contributes `Lambda(p)=log p`; for `N>=p`, Theorem 2.1 gives zero. Sum with the weights. ∎

**Corollary 8.2 (where orientation can enter).** At a prime `p`, the discrete jump is

`h_p(p)-h_(p-1)(p)=-log p`.

Thus the von Mangoldt sign appears as a **terminal boundary derivative** of the positive hyperbola tail, not as a
positive average of it. The next mechanism must orient this derivative. This is compatible with the first-contact
programme and incompatible with a plain sum of norm squares.
