# R161_004 — Corpus collision and stop-gates for the polar boundary route

## 0. Verdict

The finite Poisson--Chebyshev identity `(PC)` of `R161_001` remains a valid new packaging. The proposed next step
`L161.2`, however, was too broad: two of its natural readings have already been exhausted in the corpus.

1. After scalarising the divisor fibre, the lattice-minus-continuum boundary is the common PNT Stieltjes primitive
   of Paper 41. Its local completion has a negative square and an explicit negative interval below the first prime.
2. Before scalarising, the positive divisor disintegration supplied by `Lambda*1=log` is the divisor--Markov/ANOVA
   lift of phases 104 and 106. It has zero spectral gap; the stronger unitriangular observability proposal was killed
   in phase 121 because logarithmic differentiation removes its identity diagonal.

Consequently phase 161 must not continue by seeking a positive scalar Euler--Maclaurin density, a positive average
over divisor fibres, or a unitriangular Mobius elimination. The only surviving use of `(PC)` is on a hypothetical
first-contact state while retaining the **oriented exterior Poisson port** before every scalar trace or norm.

No sign for row D is claimed here.

## 1. Exact finite-window identification of the Muntz operator

Let `P_T` denote multiplication by `1_(-T,T)` and extend its vectors by zero. Recall the convention of phase 161

`tau_a F(t)=F(t+a)`

and put

`S_N=sum_(n<=N)n^(-1/2)tau_(log n)`.

Phase 121 uses the two causal zeta observations

```
Z_(T,+)F(t)=F(t)+sum_(2<=n<e^(2T))n^(-1/2)F(t-log n),
Z_(T,-)=J Z_(T,+) J.
```

**Proposition 1.1 (stabilisation; PROVED).** If `N>=e^(2T)`, then, as compressed operators on `L2(-T,T)`,

```
P_T S_N P_T = Z_(T,-),
P_T J S_N J P_T = Z_(T,+).                                      (1.1)
```

Both operators are finite and invertible. Their nonidentity parts are nilpotent of order at most the least integer
`r` with `r log 2>2T`.

*Proof.* If `log n>=2T`, then `F(t+log n)=0` for almost every `t in (-T,T)`. The surviving terms in `S_N` are
exactly the negative causal port in the phase-121 convention. Reflection gives the other identity. Every
nonidentity summand advances by at least `log 2`, so a product of `r` such summands vanishes after compression. The
finite Neumann series gives the inverse. ∎

Thus, on a fixed window, phase 161 has not produced a new limiting observation operator: it has recovered the exact
causal observation already used in the phase-121 closure map. What is new in `(PC)` is its simultaneous relation to
the additive Fourier defect; any proposed consequence must come from that extra port, not from `S_N` alone.

## 2. The scalar polar boundary is the old PNT primitive

The polar continuum in `R161_003` satisfies

```
integral_1^x y^(-1/2)dy = 2(sqrt(x)-1).                         (2.1)
```

After the terminal von Mangoldt endpoint is read in logarithmic displacement `u=log x`, the resulting signed
cumulative is

```
D(u)=sum_(log n<=u) Lambda(n)/sqrt(n) - 2(e^(u/2)-1).            (2.2)
```

This is exactly the common primitive of Paper 41, equation (3.10). In distribution form,

```
dD = sum_(n>=2) Lambda(n)/sqrt(n) delta_(log n) - e^(u/2)du.     (2.3)
```

Paper 41 proves

```
dD = dk_D + (1/2)k_D du,
k_D(u)=e^(-u/2)(psi(e^u)-e^u+1),                                (2.4)
```

and rewrites the remaining physical term as the Stieltjes pairing against `dD`. Entry C5 then completes the local
centered path exactly and obtains

```
positive square - integral E_1(e^u)^2/a_theta(u) |Z_q'(u)|^2 du. (2.5)
```

The last term has the wrong sign. More sharply, the available scalar density is strictly negative on a nonempty
interval below `log 2`; high-frequency compactly supported tests make the separated derivative energies grow like
`N^2`, while the complete Gamma budget grows only like `log N`.

**Corollary 2.1 (scalar stop-gate; PROVED by the cited exact identities).** Any version of `L161.2` which first
collapses the divisor hyperbola to the scalar von Mangoldt endpoint and then seeks positivity from a displacement-
local square in the lattice-minus-continuum variable is precisely in the class excluded by Paper 41, C4--C5.

The conclusion is not that every use of `(PC-ren)` is impossible. It says that scalarisation **before** the Poisson
boundary coupling loses the only information which could still be new.

## 3. The divisor-fibre lift is also old

For `s>1`, phase `104_44` disintegrates `Lambda*1=log` exactly:

```
P(D=d | N)=Lambda(d)/log N * 1_(d|N).                            (3.1)
```

The associated conditional-expectation operator is contractive, but its norm on the mean-zero subspace is exactly
one. Prime parents give an explicit sequence approaching equality. Hence no positive divisor average supplies a
uniform coercive margin.

Phases 106 and Paper 41 go further: the divisor current and cross-divisor dispersion form an exact ANOVA lift, but
every positive radical-sharp routing forces endpoint preservation and contradicts the singular prime lines. Local
Hodge/Korn squares on the star fibres are likewise zero on all gradients once they are required to be sharp on the
complete radical.

Finally, `P121_CMO_SOURCE_MATRIX_NO_GO` tests the strongest finite Mobius version on

`D=(1,2,3,4,6,12)`.

The zeta-incidence matrix is unitriangular, but its logarithmic connection `Z partial Z^(-1)` is strictly lower
triangular. The derivation that creates `Lambda` annihilates the identity diagonal. Gamma commutators are also
strictly delayed, so the root diagonal remains the old observed transport equation. Mobius elimination cannot force
the root amplitude to vanish without assuming the desired uniqueness theorem.

**Corollary 3.1 (fibre stop-gate).** Replacing the scalar discrepancy by a positive divisor-fibre norm, conditional
variance, or unitriangular Mobius history does not repair `L161.2`. A surviving construction must mix the two causal
orientations through additive Fourier **before** a positive trace, and must remain globally signed until the
equality-state hypothesis is used.

## 4. Collision with the phase-121 terminal theorem

Let `QF(t)=tF(t)`. Since

`-[Q,S_N]=K_N`,

the Chebyshev half of `(PC)` is the finite logarithmic connection of the causal zeta observation. Proposition 1.1
identifies its compressed limit with `Z_(T,-)` (or, after reflection, `Z_(T,+)`). Phase 121 proves that the missing
statement in these coordinates is the equality-state oriented range certificate

```
[Q,Z_+]F = Z_+ U_F.                                               (4.1)
```

Meromorphically, (4.1) says that

```
-(zeta'/zeta)(s) K_F(s-1/2)                                     (4.2)
```

has no residues at the critical zeros. It therefore forces `K_F(rho-1/2)=0`; the already proved Cartwright density
argument then gives `F=0`. Equivalently, the missing assertion annihilates the critical conormal square

```
D_T^crit(F)=sup_J 8pi sum_(rho=1/2+i gamma in J, simple)
                         |K_F(i gamma)|^2.                         (4.3)
```

The phase-161 boundary problem is therefore not an independent positivity lemma after compression. If it is strong
enough to close D, it must produce (4.1), (4.3), or the equivalent vanishing of the causal observation on a
first-contact state. Merely deriving another scalar boundary energy renames the old gate.

## 5. Consequence for the region immediately above `T=0.8`

Nothing singular happens at `T=0.8` in this algebra. For

```
0.8 < T < (1/2)log 5 = 0.804718956...,
```

the only nontrivial integer contacts are `2,3,4`; the nilpotence order of either causal zeta port is three because
`3 log 2>2T`. Thus this first open strip is already a finite exact laboratory. It does not require an asymptotic
`N->infinity` or a raw critical-line Dirichlet series.

This observation does not prove its sign: the phase-121 source-matrix audit shows why finite triangularity alone is
insufficient. It does show that the next calculation should specialise `(PC)` to a first-contact vector in this
three-contact chamber and keep the exterior Fourier leakage as a vector port. That calculation is carried out in
`R161_005`.

## 6. Decision

`L161.2` is retired in its scalar-positive form. The replacement is:

> **L161.3 (oriented first-contact Poisson port; OPEN).** Apply `(PC)` or `(PC-ren)` to a primitive first-contact
> state before taking any norm or scalar divisor trace. Prove that its exterior additive-Fourier port annihilates
> the critical conormal class (4.3), using the equality equation and exact Tate cancellation. The statement must
> fail at a declared source clause for the shifted rank-two pair `Xi_a`.

This is narrower than the original `O-D4.1`: the joint identity exists, its generic square is sign-blind, and its
scalar and positive-fibre completions are both closed negatively. Only the equality-state oriented Poisson port
remains untested.
