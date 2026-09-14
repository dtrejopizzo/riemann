# P123.093 — Explicit completed corner tensors for the orbit-decay domain

Date: 2026-09-06. Status: PROVED-IN-REPOSITORY for J=J_orb of
P123.092 on a single-zero two-prime boundary. This proves the tensor
comparison on that declared stronger domain, not on all of A_Z.

Let e be the cutoff projection of P123.090 and B=eJe. Since every
corner coefficient from P123.091 has compact support and finitely many
labels, that result gives B=C(B_q), topologically, also with the J
seminorms. The spaces Je and eJ carry their inherited Frechet topologies.
All balanced tensors below use completed projective tensor and closed
balancing relations. We prove

    Je tensorhat_B eJ  --multiplication--> J,
    eJ tensorhat_J Je  --multiplication--> B                 (1)

are topological bimodule isomorphisms.

## 1. A countable local frame

The free proper Gamma action on Z has a compact quotient B_q. Choose
a finite cover of B_q by evenly covered open sets, with continuous
sections and a subordinate continuous partition of unity theta_i whose
supports lie compactly inside those sets. Lift sqrt(theta_i) to the
chosen sheet and extend by zero; call the resulting compact continuous
function f_i on Z. Each orbit meets supp(f_i) at most once, and

    sum_(i,gamma) |f_i(gamma^-1 z)|^2=1.                     (2)

This sum is locally finite. Put f_(i,gamma)(z)=f_i(gamma^-1 z).
Define an element r_(i,gamma) by its label eta coefficient

    (r_(i,gamma))_eta(z)
       =f_(i,gamma)(z) sqrt(c(eta^-1 z)).                    (3)

Its orbit matrix is |f_(i,gamma),y><v_y|, where v_y is the normalized
cutoff vector of P123.091. Hence r_(i,gamma)e=r_(i,gamma). Properness
shows it has compact support and finitely many labels, so it lies in Je.
Because the support of f_i meets each orbit at most once,

    r_(i,gamma) r_(i,gamma)*
       =M_(|f_(i,gamma)|^2),                                (4)

an identity-label coefficient. This can also be checked directly using
Pc=1; every nonidentity output coefficient vanishes by the sheet property.

Finite partial sums of (4) are multipliers M_chi with 0<=chi<=1.
Along any exhaustion of the index set they tend to identity on J by
left multiplication in every seminorm: they equal one eventually on
each compact set, and compact coefficient approximations are dense by
P123.092. No assertion of convergence to a unit inside nonunital J is
needed.

## 2. Quantitative bounds ensuring projective-tensor convergence

For z in a fixed compact set K_i containing supp(f_i),

    w(gamma z)<=C H(gamma)^2,
    w(gamma z)>=c H(gamma)^(1/2).                            (5)

The upper estimate is P123.092. For the lower one write gamma=p^m q^n.
Then log H(gamma)<=|m|log p+|n|log q
<=|log gamma|+2|m|log p. Bounded coordinates on K_i imply this is at
most 2 log w(gamma z)+C, proving the assertion uniformly on K_i.

There is a finite set F_i, independent of gamma, such that the labels
in (3) lie in gamma F_i: nonzero coefficients require gamma K_i to
meet eta supp(c), so properness applied before translation gives this
finite set. Therefore for every k,l there is a constant with

    s_kl(r_(i,gamma))<=C_kl H(gamma)^(k+2l).                 (6)

For a in J, the product r_(i,gamma)* a is supported in supp(c) in its
output coordinate. Its finite first labels have height at most a
constant times H(gamma), and its a coefficients are evaluated in
gamma K_i. Using the lower estimate (5), for every k',l',N,

    s_(k',l')(r_(i,gamma)* a)
        <= C_(k',l',N) H(gamma)^(k'-N/2) s_(k',N)(a).        (7)

To see the label summation explicitly, put the output label zeta=eta mu
in the product. Then H(zeta)^k'<=H(eta)^k' H(mu)^k'; the sum over
eta has uniformly bounded cardinality, the output weight is bounded
on supp(c), and w(eta^-1 z)^(-N)<=C H(gamma)^(-N/2).
This gives (7) after summing mu.

Finally sum_gamma H(gamma)^(-epsilon)<infinity for every epsilon>0:
log H(p^m q^n)>= (|m|log p+|n|log q)/2, so two geometric series bound
the sum. Given any pair of module seminorms, choose N sufficiently
large in (7). Equations (6)–(7) then prove absolute convergence in the
corresponding projective seminorm of

    S(a)=sum_(i,gamma) r_(i,gamma) tensor r_(i,gamma)* a.      (8)

This defines a continuous linear map from J into Je tensorhat_B eJ.
The estimates construct it even in the unbalanced completed tensor
before passing to the quotient.

## 3. Both inverse identities

Multiplication of (8) is sum_(i,gamma) |f_(i,gamma)|^2 a=a, by (2)
and the strong multiplier convergence following (4). Thus mS=1.

For an elementary tensor u tensor v with u in Je and v in eJ,
r_(i,gamma)*u belongs to eJe=B. Balancing gives

    r_(i,gamma) tensor r_(i,gamma)*u v
       =r_(i,gamma)r_(i,gamma)*u tensor v.

Finite partial sums converge on the left by (8), and on the right to
u tensor v by (4). Therefore Sm(u tensor v)=u tensor v. Continuity
and density of elementary tensors give Sm=1 on the whole completed
balanced tensor. This proves the first topological isomorphism in (1).

For the second, the inverse is b->e tensor b. If u in eJ and v in Je,
balancing over J gives u tensor v=e u tensor v=e tensor uv. These
identities extend continuously and prove both inverse identities.

## 4. Scope of the resulting comparison

Equations (1) supply the exact completed bimodule tensor identities
missing after P123.091, on the orbit-decay ideal J. They use its explicit
weight estimates; the proof does not rely on density in the larger
algebra. The counterexample in P123.091 remains outside J, so the
non-surjectivity there is not contradicted.

The multiplication maps in (1) are canonical. The local frame only
constructs their inverse, whose uniqueness makes it independent of the
chosen frame. This is a strict topological Morita context for these
bimodules; equivalences for any chosen categories of complexes still
require their essentiality and exactness conditions to be stated.

Traces and external cutoff descent on J are those already compared in
P123.092 and P123.090. Transport of the designated full source, semilocal
gluing and its determinant-valued mixed RR remain separate requirements.
No full row A or global sign conclusion is asserted.
