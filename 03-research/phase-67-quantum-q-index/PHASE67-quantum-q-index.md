# Phase 67 — Quantum q-Pick algebra for Omega_7: algebraic contraction or disguised zeta?

**Program:** Riemann Hypothesis — Phase 67: quantum algebra / q-deformation for the whitened
terminal defect.
**Role of the document:** AUDITABLE PROPOSITION, not a proof. Mandate: ground the intuition
"Omega_7 can be modeled from both sides by quantum algebra" without repeating Phase 51
(Bost-Connes/KMS: partition function = zeta), Phase 53 (Stone/CCR: inner product = RH) or Phase 66
(wrong scalar whitening).

**Honesty contract.** This document does not prove RH. It defines an algebra, the relations that should
force terminal positivity, and the exact place where the idea lives or dies. If the prime operator
ends up contractive only because a norm/metric was chosen that already contains zeta, it falls into
Phase 51/MW-5. If the contractivity comes from q-unitary algebraic relations independent of zeros, it is
a new node.

---

## 0. Advance verdict

> **PROVISIONAL VERDICT: CAND-67, alive only as a gate.** The quantum route that is not already
> destroyed is a **quantum group / q-deformation** route, not KMS nor Weyl-CCR. The correct
> candidate is a **q-Pick algebra** in which:
>
> 1. the archimedean jet `A_N` is the positive contravariant form of a q-unitary representation
>    of type `U_q(su(1,1))`;
> 2. the **prime current** `B_lambda` is built canonically from Hopf-* / Mellin /
>    Euler relations, before looking at the prime Pick jet;
> 3. the prime jet `P_lambda` appears afterward as the jet of that current, not as its definition;
> 4. Omega_7 is exactly the statement that `B_lambda` is a contractive Schur multiplier:
>    `B_lambda^* B_lambda <= I`;
> 5. the index `m` is half the negative index of `I - B_lambda^* B_lambda`, equivalent to the
>    Jantzen/spectral-flow index of the representation when crossing a wall of unitarity.
>
> The new piece would be that the positivity would not come from a zeta-weighted metric, but from
> the q-algebraic unitarizability of the module. The missing piece splits in two:
>
> **QSC-exist.** There exists a canonical Mellin-q cocycle and a compact quantum group `(A_G,Delta,h)`
> with Haar state such that the von Mangoldt current is a coefficient of a
> fundamental corepresentation, and its jet `q->1` gives `P_lambda` as output.
>
> **QSC-contract.** The Hopf-* / Peter-Weyl / Haar relations of that CQG force
> `B_lambda^*B_lambda <= I`.
>
> **Correction E67.2/E67.3.** The prime generators **cannot be group-like**. That preserves Euler,
> but collapses to the Bost-Connes/`\mathbb Q_{>0}^\times` skeleton and contributes no contractivity. Euler
> multiplicativity must live in the tensor/fusion category of non-trivial corepresentations.
>
> **Correction E67.4/E67.7.** The strict free product over primes is not enough either: Haar orthogonalizes
> too much and destroys the interference that keeps `P_lambda` marginal. Woronowicz `F` alone
> does not fix this; it only weights the orthogonality. The living route requires a coherent modular state
> `omega_{z0,q}` that preserves the arithmetic off-diagonal and a canonical Haar-dominant density `D_{z0,q}`.

If both gates are proved, Omega_7 falls: `delta_N >= 0` for all `N`. If they fail, this phase leaves
a frank detector: the negative eigenvalues of `I - B_lambda^*B_lambda` read `m`, but do not annul it.

---

## 1. The object to be modeled

The P52/P53 input is:

$$
\delta_N =
\lambda_{\min}\!\left(A_N^{-1/2}(A_N-P_\lambda)A_N^{-1/2}\right)
= 1-\lambda_{\max}\!\left(A_N^{-1/2}P_\lambda A_N^{-1/2}\right).
$$

Then

$$
\Omega_7:\quad \delta_N\ge 0\ \forall N
\quad\Longleftrightarrow\quad
A_N\succeq P_\lambda\ \forall N
\quad\Longleftrightarrow\quad
\left\|A_N^{-1/2}P_\lambda A_N^{-1/2}\right\|\le 1\ \forall N.
$$

The quantum form of this must not be "look for another positive form". It must be:

$$
A_N^{-1/2}P_\lambda A_N^{-1/2} = B_{\lambda,N}^* B_{\lambda,N}
\quad\text{and}\quad
\|B_{\lambda,N}\|\le 1
$$

for a structural reason. Thus:

$$
\delta_N\ge0
\quad\Longleftrightarrow\quad
I-B_{\lambda,N}^*B_{\lambda,N}\succeq0.
$$

The quantum algebra has to produce `B_lambda` as a **matrix coefficient of a
fundamental corepresentation of a CQG with Haar state** or as a **contractive multiplier of a quantum
Schur ball with explicit Hopf-* relations**. That is the difference between a reformulation and a
lever.

**Anti-tautology warning 1.** The equality

$$
A_N^{-1/2}P_\lambda A_N^{-1/2}=B_{\lambda,N}^*B_{\lambda,N}
$$

has no content by itself. Since `P_lambda` is positive semidefinite, a
canonical/Cholesky root always exists; it exists for zeta, for Davenport-Heilbronn and for any
positive control. With that `B`, the statement

$$
\Omega_7\iff I-B^*B\succeq0
$$

is just a renaming of `delta_N`. Therefore `B_lambda` cannot be defined as a root of `P_lambda`.
It must come beforehand: from Hopf-* / Mellin / Euler relations. The matching with `P_lambda` is a later
gate (`QSC-exist`), not a definition.

**Anti-tautology warning 2.** "Being the corner of a unitary" is not enough either. By Sz.-Nagy, every
contraction has a unitary dilation, and every corner of a unitary is a contraction. Therefore

$$
B\ \text{is the corner of a unitary}\quad\Longleftrightarrow\quad \|B\|\le1
$$

adds no strength. The lever can only be more rigid: `B_lambda` must be a coefficient of a
fundamental corepresentation of a **compact quantum group** with coproduct, counit, antipode and Haar
state; the Haar/Peter-Weyl orthogonality relations are indeed extra structure that a generic Sz.-Nagy
dilation does not possess.

---

## 2. The proposed algebra

### 2.1 Archimedean sector: `U_q(su(1,1))` + Plancherel/q-Gamma

Take `0<q<1`, with `q` as a deformation/regularization parameter, not as KMS temperature. Define the
*-algebra

$$
\mathcal U_q=\langle K,K^{-1},E,F\rangle
$$

with relations

$$
K E K^{-1}=qE,\qquad
K F K^{-1}=q^{-1}F,\qquad
[E,F]=\frac{K^2-K^{-2}}{q-q^{-1}},
$$

and involution structure

$$
K^*=K,\qquad E^*=F.
$$

Use the positive discrete series `D_y^+`, `y>=1/2`, on the basis `e_0,e_1,...`:

$$
K e_n=q^{n+y}e_n,
$$

$$
E e_n=\sqrt{[n+1]_q[n+2y]_q}\,e_{n+1},\qquad
F e_n=\sqrt{[n]_q[n+2y-1]_q}\,e_{n-1}.
$$

The contravariant form `H_q` determined by `E^*=F` is positive on `D_y^+`, but a single coherent
kernel of this representation only gives the Szego term:

$$
A_N \sim \log(t_0/2\pi)\,G_{\mathrm{exact}}(N,y).
$$

This was measured in `E67.1`: the best fit is `alpha=1`, `tau=1`, `c=log(t0/2pi)`, with residual of
order `1/(t0 log t0)`. Hence the single coherent kernel is **leading only** and does not close E67.1.

The correct object for the full archimedean sector is the **q-deformed Plancherel c-function**
(equivalently the Haar/Plancherel weight) whose scalar factor is `Gamma_q`. In the limit `q->1`,

$$
\Gamma_q(x)\longrightarrow \Gamma(x),\qquad
\psi_q(x):=\frac{d}{dx}\log\Gamma_q(x)\longrightarrow \psi(x).
$$

Inserting `x=s/2`, `s=1/2+iz`, gives the exact archimedean input of the harness:

$$
h_{A,q}(z)
= i\left[-\left(\frac1s+\frac1{s-1}\right)+\frac12\log\pi-\frac12\psi_q(s/2)\right]
\longrightarrow
h_A(z).
$$

The polar factor `s(s-1)` is included because P52/h8lab includes it in `h_A`; this remains
archimedean and zeta-free.

The archimedean jet is obtained from the coherent/Plancherel vectors at the point `z_0`. Define

$$
v_i^{(q)}(z_0):=\left.\nabla_z^i v_z^{(q)}\right|_{z=z_0},\qquad i=0,\dots,N-1,
$$

where `v_z^(q)` is the coherent vector of the positive discrete series and `\nabla_z` is the Mellin-q
covariant derivative compatible with `K`. In the renormalized limit `q->1`, this form must reproduce
the archimedean jet P52:

$$
G_N^{(q)}=(\langle v_i^{(q)}(z_0),v_j^{(q)}(z_0)\rangle_{H_q})_{i,j<N}
\longrightarrow A_N.
$$

**Gate A (archimedean matching).** One must prove, with the polygamma entries of
`prop:laguerre-entries`, that the finite block of the q-renormalized contravariant form gives exactly
`A_N`, not just its leading scalar. This protects against the Phase 66 failure: here the whitening is
matricial.

**Current status.** `E67.1b` passes this gate at the Gamma_q level: the jets of `h_{A,q}` converge to the
exact jets `A_N`. `E67.1c` anchors the Plancherel/Haar terminology in the literature on Fourier transforms
on quantum `SU(1,1)` and spherical Plancherel transforms. Hence the living archimedean sector of
CAND-67 is Gamma_q / Haar-Plancherel q-special-function data, not the single coherent kernel. The only
remaining bookkeeping is to give an explicit q-home to the polar cell `s(s-1)` as the rank-one
direction `H`.

### 2.2 Prime sector: the current `B_lambda`

Add a family of arithmetic shift operators `W_u`, `u in log N`, acting on the same
representation via q-coherent translations. Formally:

$$
K W_u K^{-1}=e^{-u/2}W_u,
\qquad
W_u^*=W_{-u}
$$

in the multiplier completion.

The naive scheme would be to take a prime-local group-like generator `U_p` and form

$$
J(s)=\sum_{p,k\ge1}(\log p)p^{-ks}U_p^k.
$$

But this is a **NO-GO**. The group-like elements generate the free abelian group over the primes, i.e.
`\mathbb Q_{>0}^\times`; in any unitary representation they only give unitary characters/shifts.
That reproduces the scalar Euler product, but leaves the contractivity entirely in the classical
coefficients `p^{-k/2}`. It is Phase 51/Bost-Connes in Hopf form, not a new CQG mechanism.

The living version replaces `U_p` with a non-trivial irreducible corepresentation:

$$
u^{(p)}=(u^{(p)}_{ab})_{a,b=1}^{d_p},
\qquad
\Delta(u^{(p)}_{ab})=\sum_c u^{(p)}_{ac}\otimes u^{(p)}_{cb},
\qquad
d_q(u^{(p)})>1.
$$

The prime powers are read as tensor words `(u^(p))^{\otimes k}`, not as powers of a
character. The von Mangoldt coefficient must come from the cyclic logarithm:

$$
J_C(s)=
\sum_{p,k\ge1}
(\log p)p^{-ks}\,
X_{p,k},
\qquad
X_{p,k}:=
d_q((u^{(p)})^{\otimes k})^{-1/2}
\mathrm{Tr}_{q,\mathrm{cyc}}((u^{(p)})^{\otimes k}).
$$

The `1/k` factor of the cyclic logarithm is implicit before differentiating: it cancels the `k` produced
by `d(p^{-ks})/ds`, leaving `\Lambda(p^k)=\log p`.

The candidate truncated prime current is

$$
B_\lambda
= \sum_{p^k\le e^\lambda}
(\log p)\,p^{-k/2}\,X_{p,k}\,a_{k,p}^{(q)}\,W_{k\log p}.
$$

**Anti-circular correction.** The coefficients `a_{k,p}^{(q)}` are not fixed by requiring that the Gram be
`P_lambda`. That would be reverse engineering: it would make `QSC == Omega_7`. In the living version, the
`a_{k,p}^{(q)}` must come from one of these sources, in this order of preference:

- the Mellin-q covariance of `W_{log n}` with `U_q(su(1,1))`;
- Euler multiplicativity as a fusion/tensor law over prime-local corepresentations, not
  as group-like;
- the Haar orthogonality of an auxiliary compact quantum group `G_lambda`;
- a local archimedean normalization depending on `y,z_0`, but not on the zeros.

Only afterward is the matching required:

$$
(P_\lambda)_{ij}
=\lim_{q\to1}\langle B_\lambda v_j^{(q)}(z_0),\ B_\lambda v_i^{(q)}(z_0)\rangle_{H_q}.
$$

This is **QSC-exist**, not a definition. Arithmetic enters through `Lambda(n)`, the shifts
`log n` and the coproduct structure; the zeros must not enter.

### 2.3 The complete q-Pick algebra

Define

$$
\mathcal Q_{\Omega_7}
= \mathcal U_q\ \widehat\ltimes\ \mathcal W_{\Lambda}\ \widehat\rtimes\ \mathcal O(G_\lambda)
$$

where `\mathcal W_\Lambda` is the *-algebra generated by the `W_{log n}` with:

$$
W_uW_v=\sigma_q(u,v)W_{u+v},\qquad
W_u^*=W_{-u},
$$

and `\sigma_q` is a 2-cocycle q-Mellin chosen so that the representation is covariant with
`U_q(su(1,1))`. The auditable datum is whether there exists a **canonical** choice of `\sigma_q` from
the archimedean Mellin side, not from zeta.

The new ingredient is not a generic unitary dilation but a **compact quantum group**

$$
G_\lambda=(\mathcal O(G_\lambda),\Delta,\varepsilon,S,h)
$$

with coproduct `Delta`, counit `epsilon`, antipode `S` and Haar state `h`. There must exist a
fundamental corepresentation

$$
U_\lambda\in M_d(\mathcal O(G_\lambda))
$$

such that the prime current is a matrix coefficient or an algebraically specified compression:

$$
B_\lambda=(\omega_{\mathrm{out},\mathrm{in}}\otimes \pi)(U_\lambda)
$$

for a representation `pi` of `\mathcal O(G_lambda)` on the q-archimedean module. This condition is
much stronger than "B is the corner of some unitary": it imposes the Hopf-* identities

$$
\Delta(U_{ij})=\sum_k U_{ik}\otimes U_{kj},\qquad
S(U)=U^*,\qquad
(\mathrm{id}\otimes h)(U^*(I\otimes X)U)=\text{Peter-Weyl projection}.
$$

The crucial relation needed is a Schur ball relation, but now as a consequence of Haar/Peter-Weyl:

$$
B_\lambda^*B_\lambda \le I
\quad\text{in the q-unitary representation}.
$$

This inequality must not be proved via Sz.-Nagy. It must follow from the fact that the coefficients of a
unitary corepresentation of a CQG are contractive in every C* representation compatible with `h`, and
that `B_lambda` is exactly one of those arithmetic coefficients. Then:

$$
\|B_{\lambda,N}\|\le1
\quad\Rightarrow\quad
A_N-P_\lambda\succeq0.
$$

This is the clean quantum version of Omega_7, now without the dilation tautology.

---

## 3. How `m` is read

Let

$$
D_N := I - A_N^{-1/2}P_\lambda A_N^{-1/2}
= I-B_{\lambda,N}^*B_{\lambda,N}.
$$

Then:

$$
\delta_N=\lambda_{\min}(D_N).
$$

In the window limit,

$$
\kappa = \mathrm{ind}_-(D_\infty)
$$

is the negative index of the Weil/Pontryagin form already identified in the program, and

$$
m=\frac{\kappa}{2}.
$$

The q-algebraic reading is:

$$
m
=\frac12\,\mathrm{ind}_-\!\left(I-B_\lambda^*B_\lambda\right)
=\frac12\,\ell_{\mathrm{Jantzen}}(D_y^+,B_\lambda),
$$

where `\ell_Jantzen` is the sum of the dimensions of the negative layers of the Jantzen filtration of
the contravariant form deformed by `B_lambda`.

The intuition: the off-line zeros are not "mysterious eigenvalues" but **failures of
unitarizability**. Each off-line quadruplet contributes a hyperbolic layer in the total form; it cancels
Witt-trivially (Phase 52), but the absolute negative index does not cancel. In q-representational
language, that layer is a wall-crossing of the Shapovalov/Jantzen form:

$$
\det H_q(\mu)=0
\quad\leadsto\quad
\text{signature jump}.
$$

This is how `m` is read without introducing a new metric: `m` is the number of unitarizability
failures of the prime current within the q-unitary category. But annulling `m` requires proving that the
current is inside the Schur ball, not merely measuring that it left it.

---

## 4. Why this is neither Bost-Connes nor Berry-Keating

### 4.1 Difference from Bost-Connes/KMS

Here no thermal state `phi_beta` is taken, nor a trace `Tr(e^{-beta H})`, nor a Hamiltonian with
spectrum `{log n}` used to define the metric. If

$$
Z(\beta)=\sum n^{-\beta}=\zeta(\beta),
$$

appears in the definition of the positive form, the route dies by Phase 51. The allowed positive form is
the standard contravariant one of `U_q(su(1,1))`, fixed by `E^*=F`, and its archimedean limit `A_N`.

Arithmetic enters only through the operator `B_lambda`, not through the metric that decides positivity.

### 4.2 Difference from Weyl/CCR and Berry-Keating

No self-adjoint `H=xp` with spectrum `{gamma_rho}` is required. Stone's theorem is not invoked to
conclude reality. The central operator is a contraction:

$$
B_\lambda:\mathcal H_A\to\mathcal H_A.
$$

The problem is one of **Schur/contractivity**, not of self-adjointness. This avoids the inverted-Stone
wall of Phase 53. If the only way to obtain the contraction is to choose an extension/boundary with a
zeta phase, the route dies by the same wall; but the formulation does not presuppose it.

---

## 5. The exact test against the NO-GO-LIST

| Test | Question | Expected result |
|---|---|---|
| T0 | `A_N` comes from the exact q-contravariant form, not from scalar whitening | Must pass before any claim |
| T1 | The positivity of the form does not use KMS, a partition function nor `Tr(e^{-beta H})` | If it fails, Phase 51/MW-5 |
| T2 | `B_lambda` is not defined by Cholesky/root of `P_lambda` | If it fails, QSC-exist is Omega_7 rewritten |
| T3 | `B_lambda` is a coefficient of a CQG corepresentation with Haar, not merely a Sz.-Nagy corner | If it fails, QSC-contract is tautological |
| T4 | The DH falsifier violates some identifiable Hopf-* / Haar relation | If DH also satisfies the relations, the route would prove something false |
| T5 | The relations do not encode the zeros in `sigma_q`, `h` or in a boundary condition | If they do encode them, Phase 52/53 |
| T6 | The limit `q->1`, `N->infty` preserves the index without primitive leakage | If it fails, Phase 66/rank-one escape |

The most important test is T4. A structure that accepts both zeta and Davenport-Heilbronn and still
forces `B^*B<=I` cannot be correct. Hence the new relation must be a fine
arithmetic relation that DH does not have: not "smoothness of `Lambda`", not an envelope, not
magnitudes, but a corepresentation identity tied to the Euler product.

---

## 6. The two QSC gates

**QSC-exist — non-circular existence of the current.** There exists a canonical cocycle `sigma_q`, built
from the archimedean Mellin covariance and Euler multiplicativity in the fusion category, and
there exists a CQG
`G_lambda=(O(G_lambda),Delta,h)` such that:

1. `B_lambda` is a matrix coefficient of a fundamental corepresentation of `G_lambda`;
2. the prime generators are not group-like; they are blocks of non-trivial corepresentations with
   `d_q>1`;
3. their coefficients `a_{k,p}^{(q)}` are not chosen to reproduce `P_lambda`;
4. the archimedean coherent jet satisfies, as a matching theorem,

$$
(P_\lambda)_{ij}
=\lim_{q\to1}\langle B_\lambda v_j^{(q)}(z_0),B_\lambda v_i^{(q)}(z_0)\rangle_{H_q}.
$$

This is the gate where Phase 51 can reappear: if identifying `B_lambda` as a Haar coefficient
requires introducing the full Euler product as a partition function, or the zeros as boundary
data, the route dies.

**QSC-contract — contractivity via Haar/Peter-Weyl.** In every C* representation compatible with the
Haar state and with the q-archimedean module, the coefficient `B_lambda` satisfies:

$$
B_\lambda^*B_\lambda\le I
$$

for every `lambda`, with a strong limit compatible with the exact whitening `A_N^{-1/2}`. This inequality
must follow from the Hopf-* / Peter-Weyl / Haar relations of the CQG, not from Sz.-Nagy nor from assuming
that `B` is already a contraction.

**Consequence if QSC-exist and QSC-contract are true.**

For every `N`,

$$
A_N^{-1/2}P_\lambda A_N^{-1/2}
=B_{\lambda,N}^*B_{\lambda,N}\le I,
$$

hence

$$
\delta_N\ge0.
$$

By P52/P53:

$$
\Omega_7\quad\Longleftrightarrow\quad\mathrm{RH}.
$$

**But neither gate may be assumed.** If they are proved using only:

- the relations of `U_q(su(1,1))`;
- the Mellin covariance of the `W_{log n}`;
- Euler multiplicativity as fusion/tensor, not as group-like;
- the Hopf-* relations and the Haar/Peter-Weyl/q-dimension orthogonality;

then the idea opens a new node. If QSC is proved using:

- a norm defined by `-zeta'/zeta`;
- a boundary condition with zeta phase;
- a KMS state whose partition function is zeta;
- an index convergence equivalent to RH;
- a Sz.-Nagy dilation without Hopf-* relations;

then it opened nothing.

---

## 7. Proposed experiments and falsifiers

### E67.1 — Exact archimedean matching

Build `G_N^(q)` from the contravariant form of the representation `D_y^+`, take the
renormalized limit `q->1`, and compare entry by entry against the polygamma `A_N`. The tolerance is not
a coarse asymptotic one: it must reproduce the matrix whitening of P52.

**Go:** `G_N^(q)->A_N` for `N<=24` in the exact harness.
**No-go:** it only reproduces `1/log(t0)` or a leading Toeplitz symbol. That would be Phase 66 again.

### E67.2 — QSC-exist: current before the Pick jet

Build `sigma_q`, `O(G_lambda)` and the coefficients `a_{k,p}^{(q)}` from the Mellin/Euler relations,
without using `P_lambda`. The group-like version of this point is marked NO-GO: it reproduces Euler but
collapses to Bost-Connes. The living version requires a non-commutative fusion current as in `E67.3`.
Only afterward compute

$$
\widehat P_{\lambda,ij}^{(q)}
=\langle B_\lambda v_j^{(q)}(z_0),B_\lambda v_i^{(q)}(z_0)\rangle_{H_q}
$$

and compare `lim_{q->1} \widehat P_\lambda^{(q)}` against the exact `P_lambda`.

**Go:** the matching appears entry by entry without adjusting coefficients from `P_lambda`.
**No-go:** Cholesky, a canonical root, or a later adjustment is needed. Then QSC-exist is circular.

### E67.2b — K2-mech: separating reproduction from mechanism

`K2-repro` asks whether the current reproduces `P_lambda`. This is necessary, but not enough: the
group-like case can also reproduce classical Euler.

`K2-mech` asks whether the Schur bound changes because Haar/q-dimension weights of a non-trivial
corepresentation appear.

**Go:** the CQG number explicitly uses the `d_q^{-1/2}` / Peter-Weyl normalization and does not coincide
with the group-like baseline.
**No-go:** the result is identical to the counit/group-like case; there is no new mechanism.

### E67.3 — QSC-contract: Haar/Peter-Weyl relations

$$
\Delta(U_{ij})=\sum_k U_{ik}\otimes U_{kj},\qquad
(\mathrm{id}\otimes h)(U_{ij}^*U_{kl})=\text{orthogonality constants}
$$

Verify that those relations force `||B_lambda||<=1` as a corepresentation coefficient, not via an
abstract dilation.

**Go:** contractivity is deduced from the CQG structure and survives the exact whitening.
**No-go:** only an ad hoc dilated unitary is obtained. That is Sz.-Nagy and adds no content.

### E67.4 — Interference no-go for strict free products

The model `*_{p<=e^lambda} U_N^+(F_p)` is now a baseline/falsifier, not a final candidate. Its Haar state
orthogonalizes the blocks `X_{p,k}`:

$$
h(X_{p,k}^*X_{q,l})=0\quad((p,k)\ne(q,l)),
$$

and therefore turns the Gram of the current into an absolute/diagonal sum. But `P_lambda` is a
linear oscillatory sum with phases `n^{\pm it_0}`; the interference between prime powers is part of the
operator, not noise.

The existing measurement `omega7_operator_interference.py` gives, at `t0=10,y=1`:

```text
N=4  ||S P S|| = 0.99999993423   S_abs =   219.4407   I =   219.441
N=8  ||S P S|| = 1.0             S_abs = 18683.3261   I = 18683.326
```

So killing interference inflates the norm by huge factors. Any living CQG must preserve that
interference.

### E67.5 — Modular/Woronowicz route, weakened by E67.7

The Woronowicz route replaced "pure Haar" with two channels:

```text
f_z  = Woronowicz modular characters  -> Mellin/Euler evaluation, phases e^{-it log p};
h,F  = Haar with matrix F             -> Peter-Weyl/q-dimension, bound.
```

The same modular datum `F_p` must produce:

```text
f_{-s}(u^(p)) ~ p^{-s},
d_q(p) = Tr(F_p),
h((u_ij^(p))^*u_kl^(p)) = F_p-weighted / d_q(p).
```

But E67.7 shows that this is still not enough. The simple modular inequality

```text
|Phi_{t0,y,q}(X)|^2 <= C(t0,y,q) * h(X^* F_p X) / d_q(p),
```

summed term by term returns to the incoherent ceiling `S_abs`. To escape, an off-diagonal source is
needed:

```text
omega_{z0,q}(X_a^*X_b) != 0
```

that reproduces the arithmetic phases, together with a non-circular domination:

```text
|omega_{z0,q}(Y)|^2 <= h(Y^* D_{z0,q} Y).
```

The datum `D_{z0,q}` cannot be `P_lambda`, `-zeta'/zeta`, nor a KMS density with partition function `zeta`.

### E67.6 — Woronowicz normalization

Before the DH falsifier there remains a normalization gate: the Woronowicz channel cannot double-count
the factor `p^{-k/2}` nor hide it outside the CQG. One must decide whether `f_z` carries the full
Dirichlet weight or only the Mellin phase, and in both cases verify:

```text
N1: f_z exactly reproduces the p,z dependence;
N2: Haar measures the same X_{p,k} with weights F_p/d_q;
N3: replacing X_{p,k} with the counit changes the bound.
```

This is `E67.6` in the auxiliary documents.

### E67.7 — Woronowicz off-diagonal audit

The decisive test is no longer `mech != 0`, but:

```text
offdiag_error =
  ||offdiag(G_mod)-offdiag(G_exact)|| / ||offdiag(G_exact)||.
```

If the modular Gram is diagonal between prime powers, it is E67.4 again. If it reproduces the off-diagonal
but the dominant density is KMS-zeta, it is Phase 51 again. It only remains alive if the off-diagonal comes
from a canonical `omega_{z0,q}` and the bound comes from a zeta-free `D_{z0,q}`.

### E67.8 — DH falsifier

Repeat E67.2/E67.3 with DH or with a planted off-line zero. The proof of life of the idea is that DH must
break some Hopf-* / Haar relation before merely breaking positivity.

**Go:** DH violates the corepresentation/cocycle relation or the quantum unitarity.
**No-go:** DH satisfies the same relations and only has `||B||>1`. Then the algebra only detects
RH, it does not explain it.

---

## 8. Final diagnosis

The idea stands as:

$$
\boxed{
\Omega_7
\iff
I-B_\lambda^*B_\lambda\succeq0
\iff
B_\lambda\ \text{is Schur-contractive}
}
$$

with

$$
\boxed{
m=\frac12\mathrm{ind}_-(I-B_\lambda^*B_\lambda).
}
$$

The legitimate quantum route is not "make a positive metric for zeta"; that is already dead. It is
sharper:

> first build a non-group-like modular CQG corepresentation that produces the **prime operator** without
> looking at `P_lambda`, using a coherent state `omega_{z0,q}` to preserve the Mellin interference, and
> then prove that this state is dominated by Haar via a canonical density `D_{z0,q}`; not via
> dilation, group-like characters nor KMS-zeta.

This does model "both sides":

- archimedean side: contravariant form `U_q(su(1,1))` = `A_N`;
- prime side: von Mangoldt current = tensorial cyclic logarithm evaluated by a coherent modular
  state;
- Hopf side: `Delta,h,S,epsilon` force constraints that a Cholesky root does not have;
- RH side: negative index of the Schur defect = `2m`;
- Omega_7 side: finite contractivity of all jets = `delta_N>=0`.

**Exact audit points:**

1. `E67.1`: prove the exact archimedean matching `G_N^(q)->A_N` with matrix whitening, not a
   leading symbol.
2. `QSC-exist`: build `sigma_q`, `G_lambda` and `B_lambda` without Cholesky or adjustment to `P_lambda`; then
   obtain `P_lambda` as output.
3. `E67.4`: rule out the strict free-product Haar model as the final candidate due to loss of
   interference.
4. `E67.5`: use Woronowicz `f_z/F_p` only as modular vocabulary, not as sufficient proof.
5. `E67.6`: fix the normalization without double counting the factor `p^{-k/2}` nor collapsing to counit.
6. `E67.7`: build or refute an off-diagonal `omega_{z0,q}` and a Haar-dominant `D_{z0,q}`.
7. `QSC-contract`: derive `B_lambda^*B_lambda<=I` from that modular domination, not from
   Sz.-Nagy nor from group-like.
8. `DH`: show that Davenport-Heilbronn breaks some specific Hopf-* / Haar relation.

Up to here, Phase 67 is a good language and a detector. Crossing `QSC-exist + QSC-contract` would be
new mathematics.
