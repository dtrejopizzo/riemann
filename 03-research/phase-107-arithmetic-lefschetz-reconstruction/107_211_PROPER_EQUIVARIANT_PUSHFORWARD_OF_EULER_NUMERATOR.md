# 107.211 -- Proper equivariant pushforward preserves the Euler numerator, not the localized pole

## 1. Universal proper compactification

Let (T=mathbb G_m) act on

[
 overline Y=mathbb P^1_{mathbb C},qquad
 t[X:Y]=[tX:Y].
 	ag{1.1}
]

The affine chart (Y=mathbb A^1) is the archimedean-local moduli line
used in `107_207`, and its trivial point is
(i_0:Z={0}hookrightarrowoverline Y).  The conormal character at
zero is denoted by (chi).  The other fixed point is infinity, with
inverse normal character.

Unlike the coarse orbit quotient rejected in `107_208`, the structural
map

[
 pi:mathbb P^1longrightarrowoperatorname{Spec}mathbb C
 	ag{1.2}
]

is proper and supports the ordinary equivariant coherent pushforward.

## 2. Supported self-intersection class

On the proper square (overline Y	imesoverline Y), let (Delta) be
the diagonal and (Gamma_chi) the graph of scaling.  In affine
coordinates ((x,y)) at ((0,0)), use the ordered equations

[
 x-y=0,qquad y-chi x=0.
 	ag{2.1}
]

After eliminating (y), their graph--diagonal intersection has normal
equation

[
 (1-chi)x=0.
 	ag{2.2}
]

Thus the conormal determinant of this actual proper graph--diagonal
problem is the same (1-chi) obtained from the germ in `107_209`.
The point (0) is not selected from two target-dependent Galois
components: it is the canonical trivial point of the published
absolute Connes--Consani moduli space, before any elliptic-curve target
is supplied.  Hence the selector obstruction of `107_175` does not
apply.

`107_209` constructs on (Z) the derived self-intersection

[
 eta_0=i_0^*i_{0,*}1=lambda_{-1}(L_0)=1-chi,qquad
 L_0=mathfrak m_0/mathfrak m_0^2.
 	ag{2.3}
]

Push it into the proper compactification and then to a point:

[
 alpha_0=i_{0,*}eta_0in K_T(mathbb P^1),qquad
 pi_*alpha_0=(picirc i_0)_*eta_0=1-chi.
 	ag{2.4}
]

This is a genuine proper equivariant pushforward of a bounded virtual
coherent class.

## 3. Fixed-point localization check

The restriction of a closed-embedding pushforward satisfies the
self-intersection formula.  Therefore

[
 alpha_0|_0=(1-chi)^2,qquad
 alpha_0|_infty=0.
 	ag{3.1}
]

Thomason localization gives

[
 pi_*alpha_0
 ={(1-chi)^2over1-chi}
  +{0over1-chi^{-1}}
 =1-chi.
 	ag{3.2}
]

Thus the added fixed point at infinity contributes nothing to this
supported class.  Evaluating (chi=p^{-s}) recovers

[
 operatorname{ev}_{p,s}(pi_*alpha_0)=1-p^{-s}.
 	ag{3.3}
]

### Theorem 3.1 (proper numerator pushforward)

The local derived Euler numerator of Phase 107 admits a universal
proper equivariant compactification and pushforward.  Its character is
still (1-p^{-s}), with no infinity contamination.

## 4. Why this does not contradict the compactification no-go

For the structure sheaf, localization instead gives

[
 {1over1-chi}+{1over1-chi^{-1}}=1.
 	ag{4.1}
]

This is the denominator cancellation proved in `107_180`.  The two
statements concern different classes:

1. (mathcal O_{mathbb P^1}) produces two inverse-Euler fixed-point
   terms whose poles cancel;
2. (alpha_0) is already supported at zero and pushes the unlocalized
   Euler numerator.

The explicit Euler inverse appears only after taking the inverse global
Fredholm determinant in `107_210`.  It is not a coherent class
((1-chi)^{-1}) on (mathbb P^1).

At the ordinary augmentation (chimapsto1), the pushed class
(1-chi) becomes zero.  Hence this construction does not create an
ordinary nonzero Arakelov divisor and does not evade `107_179`.

## 5. Exact advance and remaining obstruction

There is now a complete finite-place chain on the Euler half-plane:

[
 	ext{CC fixed germ}	o
 	ext{derived self-intersection}	o
 	ext{proper equivariant local pushforward}	o
 	ext{nuclear prime sum}	o
 zeta^{-1}.
 	ag{5.1}
]

What remains for rows (a), (c), and (d) is not local properness.  It is
to realize the countable/nuclear assembly as one global arithmetic
square object and to equip its equivariant/relative class with a
primitive numerical pairing.  Ordinary augmentation kills every local
numerator, while localized inverse Euler classes cannot be forgotten;
therefore a renormalized equivariant arithmetic index theorem is still
required.

## 6. Falsifier

`107_211_proper_equivariant_pushforward_of_euler_numerator.py` verifies
the graph--diagonal Jacobian and localization identities symbolically,
evaluates five actual prime characters, rejects replacement by the
structure sheaf, and confirms that augmentation annihilates the
supported numerator.
