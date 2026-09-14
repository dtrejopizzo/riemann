# Coherent parallel-sum theorem for all active primes

Status: proved exact operator theorem.  It collapses the complete finite
place-Poisson load to one independently constructed Schur channel.  The
remaining global square is the attachment of this single channel to the
quarter-Gamma system.

## 1. The prime seam system

Let `S` be a nonempty finite set of active primes and put

    a_p=log p,
    r_p=p^(-1/2),
    C_p=r_pV_(a_p),
    theta=sum_(p in S)a_p.                          (1)

On `K=H tensor C^S`, with `H=L2(R)`, define

    C=direct-sum_p C_p,
    (WF)_p=sqrt(a_p)F.                              (2)

Then `||W F||^2=theta||F||^2`.  Let

    w_p=sqrt(a_p/theta),
    j:H -> K,  jF=(w_pF)_p,                         (3)

so that `j` is an isometry and `W=sqrt(theta)j`.  Write

    P_c=jj^*,  P_0=I-P_c.                           (4)

The coherent line in this theorem is fixed by the common source jump.  It
is generally different from the unweighted contact line used in D.256.

Define the incoming seam state

    alpha=(I-C)^(-1)WF                             (5)

and the outgoing seam state

    beta=C alpha.                                  (6)

The strict inequality `||C||<1` makes (5) unambiguous.  Equations (5)--(6)
give

    alpha-beta=WF=sqrt(theta)jF.                   (7)

## 2. Primitive seam cancellation is forced

Decompose

    alpha=j alpha_c+alpha_0,
    beta =j beta_c +beta_0,

with `alpha_0,beta_0 in P_0K`.  Applying `P_0` to (7) proves the vector
identity

    alpha_0=beta_0.                                (8)

This is not a feedback condition and not a chosen unitary extension.  It
is forced by the fact that every prime cylinder is driven by the same
profile `F`, with its determinant weight `sqrt(log p)`.

Consequently

    ||alpha||^2-||beta||^2
      =||alpha_c||^2-||beta_c||^2.                 (9)

But the seam-loss identity at every prime gives

    ||alpha||^2-||beta||^2
      =sum_p a_p||O_pF||^2.                        (10)

Thus the full place load is already a one-channel coherent defect.

## 3. Explicit effective contraction

Write `C` in blocks relative to `jH direct-sum P_0K`:

    A=j^*Cj,
    B=j^*CP_0,
    C_0=P_0Cj,
    D=P_0CP_0.                                     (11)

Since `||D||<=||C||<1`, `I-D` is invertible.  Equations (6) and (8) give

    alpha_0=(I-D)^(-1)C_0 alpha_c                  (12)

and

    beta_c=C_eff alpha_c,                          (13)

where the effective coherent return is the Redheffer parallel sum

    C_eff=A+B(I-D)^(-1)C_0.                        (14)

The contraction of `C_eff` is automatic and independent of row (d): from
`beta=C alpha`, (8), and `||C alpha||<=||alpha||`,

    ||C_eff alpha_c||=||beta_c||<=||alpha_c||.     (15)

In fact it is strict because `||C||<1`.

The coherent part of (7) is

    alpha_c-beta_c=sqrt(theta)F,                   (16)

and hence

    alpha_c=sqrt(theta)(I-C_eff)^(-1)F.            (17)

Combining (5) with `alpha_c=j^*alpha` also gives the closed formula

    (I-C_eff)^(-1)
      =(1/theta)sum_p a_p(I-C_p)^(-1),             (18)

or, equivalently,

    C_eff=I-theta[sum_p a_p(I-C_p)^(-1)]^(-1).     (19)

The parentheses in (18)--(19) are operator parentheses; all summands
commute here, but commutativity is not needed for the block proof.

## 4. Exact one-channel Poisson factorization

Let

    D_eff=(I-C_eff^*C_eff)^(1/2),
    O_eff=D_eff(I-C_eff)^(-1).                      (20)

This square root is admissible: it is the defect of the independently
constructed strict contraction (14), not a square root of the row-(d)
operator.  From (9), (10), and (17),

    boxed[
    sum_p (log p) O_p^*O_p
      =theta O_eff^*O_eff.                          (21)
    ]

Therefore the complete finite arithmetic term has the single-channel form

    theta I-sum_p(log p)O_p^*O_p
      =theta(I-O_eff^*O_eff).                       (22)

This is an operator identity on `H`, before support compression and before
row (c).  It is not the scalar Euler-product cascade excluded by D.252 and
D.255: the operation is a weighted parallel/Redheffer sum of the strict
return contractions, not multiplication of their relative factors.

## 5. New form of the global-square gate

The exact finite global operator is now

    A_T=W_Gamma^*W_Gamma-m_0I
          +theta_T(I-O_eff,T^*O_eff,T).             (23)

Equivalently, its two positive banks contain only one arithmetic channel:

    X_eff F=(W_Gamma F,sqrt(theta_T)F),
    Y_eff F=(sqrt(m_0)F,sqrt(theta_T)O_eff,T F),     (24)

and

    A_T=X_eff^*X_eff-Y_eff^*Y_eff.                 (25)

The global square is consequently reduced, without a Douglas definition,
to constructing the quarter-Gamma transmission for the explicit strict
contraction `C_eff,T` and proving

    Y_eff P_T=Theta_eff,T X_eff P_T.                (26)

All growing prime-index negative channels and all arbitrary D.247 defect
extensions have disappeared from (26).

## 6. Classification

- weighted coherent source line (3)--(7): **CONSTRUCTED**;
- forced primitive seam cancellation (8)--(10): **PROVED**;
- effective Redheffer contraction (11)--(19): **CONSTRUCTED AND PROVED
  STRICTLY CONTRACTIVE**;
- exact one-channel place-Poisson factorization (21)--(22): **PROVED**;
- one-channel global banks (23)--(25): **PROVED**;
- quarter-Gamma/effective-return transmission (26): **OPEN**;
- global square: **OPEN**.
