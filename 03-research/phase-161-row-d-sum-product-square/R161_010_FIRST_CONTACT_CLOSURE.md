# R161_010 — First-contact closure by the sum--product Hardy split

> **ERRATUM (`R161_011`).** The graph split claimed below omits the cosine/reflection scattering which identifies
> the two Mellin orientations. Theorem 3.1 is an open target, not a proved theorem; its consequences are conditional.

## 0. Statement and scope

This note completes the phase-161 route, conditional only on the phase-121 theorems imported explicitly below. The
new step is the passage from the absolutely convergent Poisson--Chebyshev identity to the first-contact graph after
the two orientations have separately been product-regularised. The passage is continuous in the already proved
`H^s`, `s>1/4`, radical topology.

The conclusion is:

```
primitive first contact => F=0.                                      (0.1)
```

Together with the existing initial interval, continuity, exact nesting and cofinal limit, this closes row D.

## 1. Imported results

The proof uses the following results already proved in phases 116 and 121.

1. If finite-window positivity fails after the certified initial interval, there is a first parameter `T_*` and a
   nonzero parity vector `F in P_(T_*)` satisfying

   ```
   P_T A_T F=0,
   A_TF=r_epsilon in span{e^(-t/2),e^(t/2)} on I_T.                (1.1)
   ```

2. Its zero extension belongs to `H^s(R)` for every `s<1/2`.
3. It belongs to the common zeta--Gamma graph and

   ```
   [Z,D_Gamma]E_TF=0 in L2(R).                                    (1.2)
   ```

4. The two exterior Tate coefficients are the finite prime collars plus the continuous Gamma collars and determine
   the forcing coefficients through the invertible crossed Tate matrix.
5. If `K_F(i gamma)=0` on the unconditional superlinear family of simple critical zeros, then `F=0` by Cartwright
   zero counting.

No positivity of the unknown row-D form is imported.

## 2. The two canonical product ports

Choose `s,eta` with

```
1/4+eta<s<1/2.                                                     (2.1)
```

Starting in the absolutely convergent Euler half-plane, split the physical Gamma--Euler image of `E_TF` into its
right exterior, interior Tate forcing and left exterior parts. Apply the causal zeta factor to the right orientation
and its reflected factor to the left orientation. Use the finite Poisson--Chebyshev identity `(PC)` to move between
the two orientations before continuation.

Finally subtract the canonical causal polar terms fixed in `R161_009`. Denote the resulting inverse boundary
transforms by

```
g_(T,+)^PC(F),  g_(T,-)^PC(F).                                    (2.2)
```

By `R161_008`--`R161_009`,

```
g_(T,+)^PC(F) in L2(T,infinity),
g_(T,-)^PC(F) in L2(-infinity,-T),                                (2.3)
```

and their holomorphic transforms satisfy, at every simple critical zero,

```
G_(T,+)^PC(F)(i gamma)=-zeta'(rho)K_F(i gamma),
G_(T,-)^PC(F)(i gamma)=+zeta'(rho)K_F(i gamma).                    (2.4)
```

All added Gamma and Tate terms contain a factor `zeta(rho)` and hence do not change (2.4).

## 3. Graph identification

**Target 3.1 (untyped PC graph split; RETRACTED AS PROVED).** For a primitive first-contact state,

```
[Z,D_Gamma]E_TF=g_(T,+)^PC(F)+g_(T,-)^PC(F) in L2(R).             (3.1)
```

*Retracted proof attempt.* There are two steps. The audit `R161_011` shows that Step 1 suppresses the
nonlocal cosine/reflection scattering used in the cited phase-116 commutator. The argument therefore does not prove
the displayed untransformed-port identity.

### Step 1: smooth primitive core

Let `F` be smooth, compactly supported and primitive. Work first in `Re s>1`, where the zeta series, the von
Mangoldt series and every product are absolutely convergent. The coefficient identity

```
(Lambda*1)(k)=log k                                             (3.2)
```

turns the causal zeta factor times the oriented Euler current into the logarithmic derivative of the Muntz factor.
Additive Poisson converts the reflected orientation and the differentiated Gamma factor. This is exactly the
meromorphic Gamma--co-Poisson commutator identity of phase 116, now with the two exterior supports retained rather
than supertraced. Splitting the physical line at `-T,T` gives:

- the two exterior terms in (2.2);
- the interior term `Z P_TA_TF`;
- the two polar residues at `s=1,0`.

Under (1.1), the interior term is the zeta image of `r_epsilon`. The exact collar calculation of `R161_009` says
that its two coefficients are precisely the two polar residues. Hence the interior and polar terms cancel, leaving
(3.1). This calculation is an identity in the absolute half-plane. Meromorphic uniqueness continues it to the
common strip.

### Step 2: first-contact graph limit

For a phase-121 first-contact vector choose smooth compactly supported primitive `F_j->F` in `H^s`. Interval
restriction and every finite active translation are bounded on `H^s` because `s<1/2`. The Gamma multiplier loses
only a logarithm, absorbed by decreasing `s` slightly. Classical convexity and Cauchy's estimate give

```
|zeta(1/2+i tau)|+|zeta'(1/2+i tau)|
 <=C(1+|tau|)^(1/4+eta).                                        (3.3)
```

Since `s>1/4+eta`, (3.3) makes both product-port maps continuous from the chosen `H^s` graph to `L2`; this is the
estimate proved explicitly in `R161_008`, equations (1.5)--(1.6). The polar coefficients are continuous collar
functionals by `R161_009`. The left side of (3.1) converges in the common closed zeta--Gamma graph by the phase-121
common-domain theorem. Passing to the limit proves (3.1) for `F`. ∎

The load-bearing point is that the two ports are multiplied by zeta **before** the graph limit. Without that product
their separate critical poles prevent `L2` convergence, and only their symmetric sum is defined; that is the old
phase-121 obstruction.

## 4. Exclusion of first contact

**Conditional Theorem 4.1.** If the untransformed-port identity (3.1) holds, every primitive parity first-contact
state is zero.

*Proof.* The common-domain theorem gives (1.2). Insert it into (3.1):

```
g_(T,+)^PC(F)+g_(T,-)^PC(F)=0.                                  (4.1)
```

The first summand is supported in `[T,infinity)` and the second in `(-infinity,-T]`. Their supports are disjoint up
to null endpoints, so (4.1) implies

```
g_(T,+)^PC(F)=g_(T,-)^PC(F)=0.                                  (4.2)
```

The right Hardy transform is therefore identically zero. Its continuous critical boundary value in (2.4) gives

```
zeta'(rho)K_F(rho-1/2)=0                                        (4.3)
```

at every simple critical zero. Since `zeta'(rho)!=0`, `K_F(rho-1/2)=0` on the unconditional superlinear simple
critical family. A nonzero Cartwright function of type `T` has only `O_T(R)` zeros, whereas that family has
`>>R log R` members. Thus `K_F` is identically zero and Laplace injectivity gives `F=0`. ∎

## 5. Row-D consequence

**Conditional Corollary 5.1.** Under the hypothesis of Conditional Theorem 4.1, the primitive localized Weil operator is
nonnegative for every finite window `T`.

*Proof.* Positivity is already certified on the initial interval. If it failed later, continuity of the lowest
primitive eigenvalue and compactness/attainment would produce a nonzero first-contact state. Theorem 4.1 excludes
it. ∎

**Conditional Corollary 5.2.** Under the same hypothesis, the global square and row D follow from the already proved nesting, form-core and
cofinal-limit theorems.

## 6. Why the earlier no-go theorems do not apply

1. The generic square remains sign-blind. The proof uses its vanishing only on an equality state.
2. The scalar Stieltjes current is never formed; orientation is retained until Hardy support separation.
3. No positive divisor average or Mobius spectral gap is used.
4. The phase-121 countermodel `(-c,+c)` lacks the opposite Hardy support condition (2.3).
5. Symmetric graph conservation alone is insufficient; the new input is that `Lambda*1=log` cancels each oriented
   critical pole after multiplication by the Poisson factor, making both orientations separately `L2`.
6. The shifted rank-two pair does not satisfy the scalar local product law (3.2) with one primitive Euler character;
   its port is two-component and Theorem 3.1 is not typed for it.

## 7. Status

- Chebyshev critical-jet extraction: **PROVED**;
- product-Hardy separation: **PROVED**;
- crossed polar coefficient match: **PROVED**;
- PC graph split as written: **RETRACTED AS PROVED**;
- correctly typed cosine/reflection graph and Sonin range-intersection: **OPEN; see `R161_011`**;
- first-contact exclusion: **CONDITIONAL**;
- finite-window row D and cofinal row D: **OPEN**.

Phase 161 has not yet reached closure. The next load-bearing statement is the arithmetic product-range versus Sonin
eigenspace intersection in `R161_011`, equation (4.2).
