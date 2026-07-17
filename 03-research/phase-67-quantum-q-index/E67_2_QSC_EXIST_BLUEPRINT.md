# E67.2 — QSC-exist blueprint for the prime current

**Date:** 2026-07-06.
**Role:** first non-circular mathematical specification of the prime-current problem after the
archimedean carrier was identified as Gamma_q / Plancherel.
**Status update:** the original group-like Euler ansatz is now marked **NO-GO**. It preserves Euler
multiplicativity, but collapses the CQG structure to the Bost-Connes/Pontryagin-dual case and cannot
provide a new Haar contractivity mechanism.

## Starting point

The archimedean side is now structurally asymmetric with the prime side:

- `A_N` comes from the canonical Gamma factor and its q-deformation `Gamma_q`; no free coefficients.
- `P_lambda` comes from the von Mangoldt/log-Euler side; defining a current by forcing its Gram to be
  `P_lambda` is circular.

So `QSC-exist` must build the prime current first, then recover `P_lambda` as a theorem.

## E67.2a no-go: group-like Euler generators

The first ansatz was:

```text
Delta(U_p) = U_p tensor U_p,
epsilon(U_p) = 1,
S(U_p) = U_p^*.
```

This is insufficient by construction.

Group-like elements of a Hopf algebra form a group under multiplication. With one independent
group-like generator per prime, the generated object is the group algebra of the free abelian group on
the primes:

```text
< U_p group-like : p prime >
    ~= C[ direct_sum_p Z ]
    ~= C[ Q_{>0}^x ].
```

Equivalently, on the commutative dual side this is the character torus of the rational positive
multiplicative group. This is exactly the arithmetic group skeleton underlying Bost-Connes. It keeps the
Euler product but loses the noncommutative matrix-corepresentation structure needed by
`QSC-contract`.

In any unitary *-representation, a group-like unitary contributes only a unitary character/shift. Thus
the formal Euler current

```text
E(s) = product_p (1 - p^{-s} U_p)^(-1)
J(s) = - d/ds log E(s)
     = sum_{p,k>=1} (log p) p^{-ks} U_p^k
```

does reproduce the classical von Mangoldt coefficients, but the norm question is then controlled by
the same scalar weights `p^{-k/2}` and the same Pick matrix `A_N^{-1/2} P_lambda A_N^{-1/2}`. The
group-like algebra adds no independent contraction.

This is the prime-side analogue of the Sz.-Nagy warning:

```text
corner of a unitary        <=>  abstract contraction, no new force;
group-like prime generator <=>  Euler character, no new Haar force.
```

Therefore the original ansatz is a useful falsifier, not a candidate.

## Corrected requirement: Euler in fusion, not in group-likes

The prime generators must be **matrix coefficients of non-trivial irreducible corepresentations** of a
genuinely noncommutative compact quantum group. For each prime `p`, replace the scalar group-like
`U_p` by an irreducible unitary corepresentation

```text
u^(p) = (u^(p)_{ab})_{a,b=1}^{d_p},
d_q(u^(p)) > 1,
Delta(u^(p)_{ab}) = sum_c u^(p)_{ac} tensor u^(p)_{cb}.
```

The Euler multiplicativity is not the statement that each prime generator is group-like. It must live in
the tensor category:

```text
p^k        <->  (u^(p))^{tensor k},
mn         <->  u^(m) tensor u^(n),
Euler law  <->  fusion / tensor-product bookkeeping.
```

The von Mangoldt coefficient must come from a categorical logarithmic derivative on this fusion
semiring. Formally, define an Euler object in the completed representation ring:

```text
E_C(s) = product_p Exp_cyc( p^{-s} u^(p) )
       := product_p exp( sum_{k>=1} p^{-ks} Tr_cyc((u^(p))^{tensor k}) / k ).
```

Then

```text
J_C(s) := -D_s log E_C(s)
        = sum_{p,k>=1} (log p) p^{-ks} Tr_cyc((u^(p))^{tensor k}).
```

The `1/k` in the cyclic logarithm is essential: differentiating `p^{-ks}` produces `k log p`, and the
cyclic log cancels the `k`, leaving `Lambda(p^k)=log p`.

This keeps the Euler discriminant against Davenport-Heilbronn, while leaving room for a noncommutative
Haar/Peter-Weyl mechanism.

## Haar mechanism required by QSC-contract

For a compact quantum group, matrix coefficients of irreducible unitary corepresentations satisfy
Peter-Weyl orthogonality of the form

```text
h((u^alpha_ij)^* u^beta_kl)
  = 0, alpha != beta,
  = q-dimension/F_alpha weighted constants, alpha = beta.
```

This is the only acceptable source of a new contraction. The Schur bound must depend on the Haar
weights and quantum dimensions of the non-trivial corepresentations, not merely on the classical decay
`p^{-k/2}`.

So `QSC-contract` becomes:

```text
B_lambda is a specified coefficient/projection of J_C(s)
and
B_lambda^* B_lambda <= I
```

because of Haar/Peter-Weyl/q-dimension orthogonality.

If the computed bound is numerically identical to the group-like/counit case, the candidate has
collapsed back to Phase 51.

## Coupling to the archimedean module

The corrected current must still act on the q-archimedean module through Mellin shifts:

```text
pi_z0(Tr_cyc((u^(p))^{tensor k}))  ~  W_{k log p}
```

with covariance

```text
K W_u K^{-1} = e^{-u/2} W_u,
W_u^* = W_{-u},
W_u W_v = sigma_q(u,v) W_{u+v}.
```

Then the candidate prime current is

```text
B_lambda(z0,q) =
  sum_{p^k <= e^lambda}
    (log p) p^{-k/2}
    pi_z0(Tr_cyc((u^(p))^{tensor k}))
    * arch_q(k log p; z0),
```

where `arch_q` is fixed by the Gamma_q/Plancherel carrier, not by `P_lambda`.

## QSC-exist target

Prove, without using `P_lambda` as input:

```text
(P_lambda)_{ij}
= lim_{q->1} < B_lambda v_j^(q)(z0), B_lambda v_i^(q)(z0) >_{H_q}
```

where the right side is computed from:

- the non-group-like Euler fusion current;
- the Mellin covariance;
- the Gamma_q/Plancherel archimedean carrier;
- Haar/Peter-Weyl/q-dimension weights;
- the finite truncation `p^k <= e^lambda`.

## Immediate danger: false K2 positives

Reproducing `P_lambda` is necessary but not discriminating. The group-like/counit construction can
already reproduce the classical Euler current:

```text
J(s) = -zeta'(s)/zeta(s)
```

So the next numerical test must be split:

- `K2-repro`: does the construction reproduce the prime Pick jet? Necessary, but group-like also passes.
- `K2-mech`: does the Schur bound change because of non-trivial Haar/q-dimension weights? This is the
  discriminating test.

### K1 — coefficient source

Can `Lambda(p^k)=log p` be obtained from the cyclic categorical logarithmic derivative with no
reference to `P_lambda`?

Expected: yes, formally.

### K2-repro — jet matching

Does the Mellin action of `Tr_cyc((u^(p))^{tensor k})` on Gamma_q coherent/Plancherel jets produce the
exact P52 prime Pick entries?

Expected: unknown. This is necessary for `QSC-exist`, but not evidence of `QSC-contract`.

### K2-mech — non-group-like contraction

Does the same construction yield a Schur bound whose mechanism visibly uses Haar orthogonality and
quantum dimension `d_q>1`?

Expected: this is the real separator. If the finite-prime number equals the group-like baseline, the
construction has not escaped Phase 51.

### K3 — DH falsifier

Can Davenport-Heilbronn be represented by the same non-group-like Euler fusion current and same Haar
relations?

Expected: no. If yes, the structure is too weak and cannot force RH.

The anticipated failure mode is precise: DH has a functional equation but no honest Euler product. It
may mimic the archimedean/Gamma carrier, but it should fail the prime-local tensor factorization, the
cyclic Euler logarithm, or the Haar/fusion orthogonality relations.

### K4 — pole cell

The polar factor `s(s-1)` must be the rank-one distinguished vector `H`, not a hidden scalar correction.
This must match Phase 66's pole/degree direction.

## Current status

`E67.2` is a blueprint, not a theorem. The important correction is that von Mangoldt may come from an
Euler logarithm, but the contractivity cannot come from group-like prime generators. The live version is:

```text
von Mangoldt = cyclic logarithmic derivative in a noncommutative fusion category;
contractivity = Haar/Peter-Weyl/q-dimension bound for non-trivial corepresentations.
```

The next task is not yet a finite-prime numeric. First choose the CQG family and the irreducible
corepresentation type. Then build a finite-prime `K2-mech` experiment with the group-like construction
as explicit baseline and DH as falsifier.
