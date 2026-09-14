# P121 -- Bombieri, Suzuki and the shifted-pair falsifier

## Status

This note audits the proposed order

```text
construct a first-contact state for Xi_a
 -> test oriented divisibility
 -> read off whether the phase-121 terminal lemma is viable.
```

The literature comparison is useful, but the displayed test is not yet a
well-defined finite test of the zeta-specific lemma.  The distinctions below
are binding before any computation.

## 1. What the external comparison gets right

### 1.1 The negative-witness architecture is genuinely different

The retired positive-lift family asks for a contractive comparison on every
source and collapses to Douglas.  The phase-121 branch assumes one particular
first-contact state and seeks to annihilate it.  That additional hypothesis
is real information and the logical form is not Douglas by construction.

### 1.2 The terminal density argument is unconditional

For `F in L^2(-T,T)`,

\[
 K_F(z)=\int_{-T}^{T}F(t)e^{-zt}\,dt                 \tag{1.1}
\]

is an entire Cartwright function of exponential type at most `T`.  A nonzero
entire function of finite exponential type has only `O_T(R)` zeros in
`|z|<=R`, counted with multiplicity.  Riemann--von Mangoldt supplies
`asymp R log R` nontrivial zeta zeros.  Hence

\[
 K_F(\rho-1/2)=0\quad\hbox{for every nontrivial }\rho
 \quad\Longrightarrow\quad K_F\equiv0
 \quad\Longrightarrow\quad F=0.                    \tag{1.2}
\]

This uses the unconditional density of the zero divisor, not its horizontal
location.  It is the correct non-circular endgame after physical oriented
divisibility has been proved.

### 1.3 Bombieri and Suzuki are the correct variational context

Bombieri proves attainment of localized minima for Weil's quadratic
functional and derives the corresponding Euler--Lagrange operator.  Suzuki
constructs the localized self-adjoint operator, proves discreteness of its
spectrum and continuity of its lowest eigenvalue, and explicitly relates the
operator to Bombieri's variational problems through the screw kernel.

This confirms that first contact is a classical variational phenomenon.  It
does not supply the phase-121 oriented range theorem.

## 2. First correction: Bombieri's equation is adjacent, not identical

Bombieri's unconstrained unit-sphere problem gives an eigenvalue equation of
the form

\[
 L[f]=\lambda f.                                    \tag{2.1}
\]

The paper-42 first-contact problem is the compression to

\[
 \mathcal P_T=\ker M_+\cap\ker M_-.
\]

At a zero primitive eigenvalue its Euler--Lagrange equation is

\[
 \mathscr A_TF=\alpha e^{-t/2}+\beta e^{t/2}.       \tag{2.2}
\]

Thus the two equations share the variational template, but (2.2) has two
constraint multipliers and no `lambda F` term at first contact.  Calling
(2.2) "exactly Bombieri's equation" erases the primitive compression which
is load-bearing in row (d).

## 3. Second correction: the shifted-pair null state is not explicit

For `0<a<1/2`,

\[
 \Xi_a(s)=\xi(s+a)\xi(s-a)                          \tag{3.1}
\]

has a symmetric completed functional equation and off-central zeros.  Its
localized Weil form must therefore be negative on some compactly supported
source.  To obtain a *first-contact state* one still has to establish, for
the precise shifted-pair form and the precise primitive constraints:

1. positivity in an initial window;
2. continuity of the lowest constrained eigenvalue in the window;
3. attainment/compact resolvent on the constrained form domain.

These ingredients plausibly transfer from the Bombieri--Suzuki theory, but
their transfer is a theorem, not an explicit formula for the state.  Even
after it, the state is an abstract eigenvector.  Computing an approximation
does not evaluate an exact range statement such as (5.1) of the closure map.

## 4. Third correction: `(5.1) for Xi_a` is not yet a typed statement

For zeta the local Euler contact has one primitive character per place.  For
the shifted pair,

\[
 \Lambda_a(p^j)=\log p\,(p^{aj}+p^{-aj})             \tag{4.1}
\]

is a sum of two independent rank-one characters.  Accordingly the natural
causal observation has two local radii.  It is not the scalar rank-one
operator `Z_+` occurring in

\[
 [Q,Z_+]F=Z_+U_F.                                   \tag{4.2}
\]

There are at least two inequivalent ways to formulate a shifted-pair
analogue: multiply the two scalar Euler observations first, or retain a
two-component local port and descend later.  Their physical range spaces and
their defects are different.  Until the zeta theorem states exactly how
local rank one is consumed, “evaluate (4.2) on Xi_a” has no canonical
meaning.

The corpus already contains the correct conclusion: `Xi_a` is a **typing
falsifier** for any construction which claims to use indecomposable local
rank one.  It is not yet a numerical falsifier for an unconstructed terminal
law.

## 5. What a shifted-pair test could and could not prove

Assume a functorial terminal law has first been stated for Euler packages of
arbitrary local rank.

* If it applies to `Xi_a` and gives physical divisibility for its nonzero
  first-contact state, then the analogue of (1.2) forces that state to be
  zero.  The law is false.
* If it refuses `Xi_a` because its local source is rank two, the test only
  verifies the declared rank-one hypothesis.  It does not prove the theorem
  for zeta.
* If a numerical residual is nonzero on an approximate eigenstate, that is
  evidence about a discretized realization, not proof of failure of an exact
  graph-range inclusion.

Therefore the shifted pair is a necessary firewall after a candidate law is
written.  Running it before the candidate exists cannot reveal the missing
source identity.

## 6. The numerical Suzuki paper does not set a rigorous precision ceiling

The 2026 numerical paper reports positive finite-element values and a rapid
decay of the lowest eigenvalue in a tested range.  Its own scope statements
say that:

* Rayleigh--Ritz values are upper bounds on the true infimum;
* positive discrete values do not certify positivity;
* values beyond the resolved range are extrapolations;
* the work does not prove or advance RH.

Moreover its `A_a` is the uncompressed localized Weil operator in Suzuki's
normalization, whereas paper 42 uses the two-Tate primitive compression
`Delta_T`.  No theorem currently identifies the reported `lambda_1(a)` with
the primitive margins at `T=log 2` or `T=(1/2)log 5`.

Consequently the observed superexponential decay is useful numerical context,
but it does not prove that a certain `T` is the last endpoint certifiable by
all rigorous methods.  Such a claim would depend on the algorithm and the
precision model, not only on the operator.

## 7. Binding consequence

The external audit strengthens the phase-121 map in one place and does not
change its open theorem:

```text
physical oriented divisibility for the zeta first-contact state
 -> zero at every zeta zero
 -> Cartwright/Riemann--von Mangoldt overdetermination
 -> F=0.
```

The last two arrows are proved.  The first is still open.

The next pure-mathematics construction must therefore state a zeta-specific
source law which:

1. consumes indecomposable rank one at each prime explicitly;
2. couples distinct primes before the scalar trace;
3. descends to the physical scalar causal range;
4. does not request any critical-zero divisor as input;
5. ceases to be typed, or fails a stated clause, for the rank-two shifted
   pair.

Only after such a law is written does `Xi_a` become a decisive falsifier.

## 8. Semantic collision: flat descent of the Euler ideal is phase 91

A natural reaction to (4.2) is to work in the formal Euler algebra, use
`dZ=Z dlog Z`, and ask that the principal ideal `(Z)` descend faithfully to
the physical graph completion.  This is not a new mechanism in the corpus.

Phase 91 writes `A=Z^{-1}delta Z` and proves the exact identity

\[
 Av=Z^{-1}\delta[(Z-I)v]-(I-Z^{-1})\delta v.         \tag{8.1}
\]

The last summand is the Euler derivation defect.  It vanishes on an algebraic
ground vector with `delta v=0`, but in the physical interval representation
`delta=Q` and `Qv=0` forces `v=0`.  The accompanying no-bypass theorem proves
that absorbing (8.1) into a connection or coboundary leaves precisely the
safe reduced leakage which carries the original obstruction.

Thus "faithfully flat descent of the Euler principal ideal" is a new phrase
for the already audited phase-91 question.  In the current coordinate its
unremoved defect is part of the observed equation (3.1) in the closure map.
It is retired unless an additional source identity, not present in formal
Leibniz divisibility, is supplied.
