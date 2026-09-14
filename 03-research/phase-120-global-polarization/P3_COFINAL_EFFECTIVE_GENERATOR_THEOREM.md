# Cofinal effective-generator theorem

Status: exact cofinal algebra and local stabilization proved.  Passage of a
positive square is reduced to functoriality of the finite-horizon storage,
not to a new convergence estimate.

## 1. The renormalized variable

For a finite prime set `S`, let

    theta_S=sum_(p in S)log p

and let `C_eff,S` be the strict contraction of the coherent parallel-sum
theorem.  Define

    L_S=theta_S C_eff,S(I-C_eff,S)^(-1).             (1)

Using

    (I-C_eff,S)^(-1)
      =(1/theta_S)sum_p(log p)(I-C_p)^(-1),

one obtains the exact identity

    boxed[
    L_S=sum_(p in S)(log p)C_p(I-C_p)^(-1).
    ]                                               (2)

Thus `L_S`, not `C_eff,S`, is the additive arithmetic generator retained
by the cofinal limit.

## 2. Exact additivity

For disjoint finite prime sets `S_1,S_2`, equation (2) gives

    L_(S_1 union S_2)=L_(S_1)+L_(S_2).              (3)

The effective contractions themselves satisfy the nonlinear reconstruction

    C_eff,S=L_S(theta_S I+L_S)^(-1).                (4)

Consequently every inclusion of finite place sets has a canonical
lossless state extension at the additive-generator level.  No choice of a
unitary complement is required in the cofinal system.

## 3. Euler limit in the half-plane

In the right half-plane realization,

    L_S(s)=sum_(p in S)(log p)
       p^(-1/2-s)/(1-p^(-1/2-s)).                   (5)

For `Re(s)>1/2`, the series converges locally uniformly as `S` exhausts the
primes, and the Euler logarithmic derivative gives

    L_infty(s)=-zeta'(s+1/2)/zeta(s+1/2).           (6)

Hence

    C_eff,S(s)=L_S(s)/(theta_S+L_S(s)) -> 0         (7)

locally uniformly in that half-plane, whereas the scaled generator (1)
converges to the nontrivial limit (6).  Passing directly with
`C_eff,S -> 0` would therefore erase the arithmetic; (1) is the forced
renormalization.

## 4. Cofinal determinant

The one-port determinant of the finite system is

    D_S(s)=pi^(-s)Gamma(1/4+s/2)^2
              product_(p in S)(1-p^(-1/2-s))^(-2). (8)

For `Re(s)>1/2`, local uniform convergence gives

    D_S(s) -> D_infty(s)
      =pi^(-s)Gamma(1/4+s/2)^2 zeta(s+1/2)^2,       (9)

and

    partial_s log D_infty(s)
      =psi(1/4+s/2)-log pi
         +2 zeta'(s+1/2)/zeta(s+1/2).              (10)

The polar factor `1/4-s^2` is exactly the transform of the compact-potential
operator `L_0`.  Thus the two Tate conditions are the correct cofinal
removal of the poles at `s=+-1/2`; no additional finite-place moment may be
introduced in the limit.

## 5. Exact stabilization on compact support

Let `F` be supported in `[-T_0,T_0]`.  If `a=log p>=2T_0`, then for every
`j>=1` the supports of `F` and `V_(ja)F` are disjoint up to a null endpoint.
The place-Poisson identity therefore gives

    <F,(O_p^*O_p-I)F>=0.                            (11)

By polarization the compressed operator vanishes:

    E_(T_0)^*(O_p^*O_p-I)E_(T_0)=0.                (12)

Consequently the finite global forms stabilize exactly:

    E_(T_0)^* A_S E_(T_0)
      =E_(T_0)^* A_(S union S_new) E_(T_0)          (13)

whenever every prime in `S_new` has `log p>=2T_0`.  The same statement
includes all powers of those primes automatically.

Thus the cofinal quadratic form on the compact primitive core needs no
dominated-convergence argument: every test vector is evaluated at a finite
stage and never changes afterward.

## 6. Reverse-engineered requirement on the square

Suppose a finite-stage storage construction produces

    <A_S L_0G,L_0G>=||D_S^bulk G||^2.               (14)

The cofinal theorem shows exactly what functoriality is required.  On adding
an inactive prime with `log p>=2T_0`, its seam cylinder must enter as a
lossless summand whose incoming and outgoing boundary norms agree on
`C_c^infinity((-T_0,T_0))`.  Then there is a canonical isometry

    H_bulk,S -> H_bulk,S union {p}                  (15)

intertwining `D_S^bulk`, and the positive energies stabilize exactly as in
(13).

Therefore the cofinal limit is not an independent positivity gate.  Once
the finite one-port storage is constructed with lossless-place
functoriality, define

    ||D_infty G||^2:=||D_S^bulk G||^2               (16)

at any stabilized stage.  Equation (13) makes (16) well defined, positive,
and equal to the global row-(d) form on the compact primitive core.

The reverse-engineered finite requirement is consequently sharp:

    storage must be a functor of the additive generator L_S,             (17)

not a spectral square root of the compressed `A_S`.  Additivity (3) then
forces the correct lossless extension and closes the cofinal passage.

## 7. Classification

- effective generator identity (2): **PROVED**;
- cofinal additivity (3)--(4): **PROVED**;
- Euler/determinant limit (6)--(10): **PROVED IN `Re(s)>1/2`**;
- exact compact-support stabilization (11)--(13): **PROVED**;
- cofinal passage for a functorial finite storage (14)--(16):
  **PROVED CONDITIONALLY ON THE FINITE STORAGE**;
- finite one-port storage functor (17): **OPEN**;
- global square and row (d): **OPEN**.
