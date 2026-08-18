# The backward map: what each of (a)–(d) needs from the next

## 0. Why this document

Every phase so far has worked **forwards**: build (a), then hope (b), (c),
(d) follow.  Four stages and two phases closed negatively that way.

This note works **backwards**.  (d) is the goal, so the question is what (d)
needs; that fixes what (c) must deliver; that fixes (b); that fixes (a).  The
result is a dependency graph with the missing objects named at each edge, and
it relocates the binding constraint.

Nothing here is a new theorem.  It is an audit of requirements against
inventory.  Every "have" entry cites a proved result; every "missing" entry
is a named object nobody has built.

## 1. (d) — what the target actually requires

Weil's row (d) is the Hodge index theorem in Castelnuovo–Severi form.  Its
role is to be an **input from geometry** which then *implies* the zeta bound.
The programme's analogue is 107_241 Corollary 3.4: the primitive form
\[
 Q(f)=-\sum_\rho m_\rho\,\widehat f(\rho)\,\overline{\widehat f(\rho')}
\]
satisfies $Q\le0$ if and only if RH.  So (d) is not "compute $Q$" — that is
done — but **prove $Q\le0$ from something other than RH**.

The classical proof of the Hodge index theorem is worth writing out, because
it names every ingredient (d) needs:

> Let $H$ be a polarization, $H^2>0$.  Let $D\ne0$ with $D\cdot H=0$, and
> suppose $D^2>0$.  Riemann–Roch gives
> $\chi(nD)=\chi(\mathcal O)+\tfrac{(nD)^2-(nD)\cdot K}2
> \sim \tfrac{n^2D^2}2\to\infty$.  Serre duality gives
> $h^2(nD)=h^0(K-nD)$, which vanishes for large $n$.  Hence
> $h^0(nD)\to\infty$, so $nD$ is effective for large $n$; and an effective
> divisor pairs positively with a polarization, so $nD\cdot H>0$,
> contradicting $D\cdot H=0$.  Therefore $D^2\le0$ on $H^\perp$.

**The engine is Riemann–Roch plus effectivity.**  Positivity is not assumed
anywhere; it is *produced*, by the quadratic growth of $\chi(nD)$ forcing
sections to exist, and by effective divisors meeting the polarization
positively.

So (d) requires, from (c):

| # | requirement | why |
|---|---|---|
| d0 | a degree map, $\mathbb Z$-valued on effective classes, killing the radical | isolated only in 113; implicit in the classical proof |
| d1 | an intersection form descending to **linear** equivalence | $h^0$ is a linear-equivalence invariant |
| d2 | a polarization $H$ with $H^2>0$ | the reference class for $H^\perp$ |
| d3 | Riemann–Roch with a **quadratic** $D^2$ term | the growth that forces sections |
| d4 | Serre duality (or a vanishing theorem for $h^2$) | to convert growth of $\chi$ into growth of $h^0$ |
| d5 | an effective cone, with $D$ effective $\Rightarrow D\cdot H>0$ | the contradiction step |

**Status update (phase 113 — this supersedes the 110/111/112 reading below).**
Phase 113 moved the pairing onto **Schwartz** data — the class
$\mathcal D=\bigcup_{\theta>3/2}\mathcal D_\theta$ defined by decay of the
balanced profile $F(x)=e^{x/2}f(e^x)$ (113\_07 Def 1.3) — where the
$\xi$-divisibility route 110 closed on compact support is alive.  On that class
the identity-value condition $h(1)=0$ turned out to be both impossible to
impose and **unnecessary** (113\_07 §3), and Assumption T was discharged on its
analytic half (113\_06 Thm 3.2).  The row-(c) object is now a commutative
**Frobenius $*$-algebra** $(\mathcal D/\mathrm{rad},\star,{}^*,\tau)$ with a
zero-free trace.  Requirement by requirement:

* **d0 BUILT** — 113\_10 Thm 1.2/1.3.
* **d1 BUILT, analytic half** — $\mathrm{rad}\,I_\partial$ is exactly the
  $\chi$-ideal, $\chi(s)=s(s-1)\xi(s)$ (113\_09 Thm 2.2).  The geometric half
  (a principal subspace on an actual space) is untouched, and is now a row-(a)
  problem, not a row-(c) one.
* **d2 HAVE** — $H^2=2$, and $H=2\Phi$ is *effective* (113\_10 Thm 3.2).
* **d3 IMPOSSIBLE inside $\mathcal D$** — 113\_11 Thm 3.1/3.3: divisor and
  values are doubly dissociated, so no $h^0$ growing like $n^2D^2/2$ can be a
  function of either.
* **d4 BUILT, unconditional** — 113\_12 §3 plus 113\_14 Thm 2.1 (the separating
  family $\chi(s)/(s-\rho)^{m_\rho}$, an candid element of $\mathcal D$).
* **d5 BUILT** — requirement (R) proved, not merely tested: 113\_10 Thm
  2.2/2.5.  This supersedes 112's "formal only".
* **$K=0$ BUILT** — 113\_12 Thm 3.4.

**And this is why the row does not close.**  113\_10 Thm 4.2/4.3 prove that
$(E^\circ)$ — the effectivity statement d3 was supposed to supply — is
**equivalent to RH**, both directions; 113\_12 Thm 4.1 proves the Hodge index
inequality on $H^\perp$ holds **iff** RH (measured: signature $(1,7)$ with the
zeros on the line, $(3,5)$ off it).  So row (d) is not a route to RH; row (d)
**is** RH.  Full audit in 113\_15; phase summary in 113\_99.

## 2. (c) — what the intersection row must deliver, and what it has

**Has.**  The identity, proved: $\sum_p\sum_{k\ge1}\Gamma^{\mathrm{Tate}}_{p,k}
(f_s)=\sum_n\Lambda(n)n^{-s}=-\zeta'/\zeta(s)$ (108_36 Thm 1.1).  This is the
$\Gamma_n\cdot\Delta=N_n$ shape.

**Has.**  A pairing $I_\partial$ that is **zero-free in its definition** (a
renormalized semilocal trace, 107_240 §1), nondegenerate on the quotient by
its radical (107_240 §5), with a computed signature $n_+=1+\#P$
(107_241 Thm 3.1).

**Has, and this is better than it has been credited.**  $H^2>0$ is
*available*.  107_241 Theorem 3.1(1) gives the polar block
$\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$ on the two
rulings, $F_v^2=F_h^2=0$, $F_v\cdot F_h=1$.  So $H:=F_v+F_h$ has $H^2=2>0$.
**Requirement d2 is met.**

**Missing — d1, and it is the binding constraint of the whole programme.**
$I_\partial$ descends to *numerical* equivalence for free (107_240 (5.1)),
but $h^0$ needs *linear* equivalence, which needs a principal subspace
$\mathcal P$ with $\mathcal P\subseteq\mathrm{rad}\,I_\partial$.  And
$\mathrm{rad}\,I_\partial=\{f:\widehat f(0)=\widehat f(1)=0,\
\widehat f(\rho)=0\ \forall\rho\}$ (107_240 Thm D).  So every principal $f$
must have transform vanishing at every zero of $\xi$.

> **Update (phase 110).**  The natural zero-free route to d1 — requiring
> $\widehat f=\xi\cdot\widehat g$, which makes the vanishing automatic and
> uses $\xi$ rather than any zero of $\xi$ — is **impossible inside the
> corner pairing's admissible class**.  By Stirling,
> $\log\xi(\sigma)=\tfrac\sigma2\log\sigma-C\sigma+o(\sigma)$ with
> $C=\tfrac{\log2+1+\log\pi}2$, so $\xi$ has *infinite* exponential type on
> the real axis; every compactly supported $f$ has $\log|\widehat f(\sigma)|
> \le\sigma\log B+O(1)$, finite type.  Dividing forces $\widehat g$ to decay
> faster than $e^{-M\sigma}$ for every $M$, which forces $g\equiv0$.  Hence
> $\{\widehat f=\xi\widehat g\}\cap\{\text{compact support}\}=\{0\}$
> (110_02).
>
> **This is not RH in disguise** (110_03), and the reason is stronger than
> an operational test: $\zeta(\sigma)\to1$ as $\sigma\to\infty$, so
> $\log\zeta(\sigma)\to0$ and contributes *nothing* to the growth.  The
> obstruction is carried entirely by $\Gamma$.  No zero of $\zeta$ enters it.
>
> **The door that remains.**  Enlarging the pairing's admissible class from
> compactly supported to Schwartz-class data.  There $\xi$-divisibility is
> populated — e.g. $g(r)=e^{-(\log r)^2}$, $\widehat g(w)=\sqrt\pi e^{w^2/4}$
> — but whether $I_\partial$ still converges on that class is unbuilt and
> substantial.  Note the shape: this is instance 9 of 108_90's
> rigidity-versus-finiteness condition, with $\xi$-divisibility as the
> rigidity and compact support as the finiteness.

This is exactly the fork 107_240 §5 tabulates:

| goal | needs principal invariance? | status |
|---|---|---|
| Hodge index / signature on the numerical quotient | no | available now |
| Riemann–Roch, $h^0$, $h^1$ | **yes** | **blocked by Theorem D** — *resolved analytically in 113* |

> **Update (phase 113).**  The radical is not an obstruction, it is an answer:
> $\mathrm{rad}\,I_\partial$ is exactly the ideal generated by
> $\chi(s)=s(s-1)\xi(s)$ (113\_09 Thm 2.2), and the quotient is a Frobenius
> algebra.  The principal subspace the fork asks for therefore *exists* on the
> analytic side.  What the fork does **not** supply — and what phase 113 also
> did not supply — is a space whose principal divisors are that ideal.  d1's
> geometric half is now a row-(a) requirement.

**Built in phase 113 — d0, d2, d4, d5, $K=0$; d3 proved impossible inside
$\mathcal D$.**  This paragraph previously read "no Riemann–Roch, no Serre
duality, no effective cone has been constructed or attempted anywhere in the
programme."  That is no longer true; see §1's status update.  What replaces it
is a harder statement: the assembled engine does not turn, because the one
missing input, $(E^\circ)$, is equivalent to RH (113\_10 Thm 4.2/4.3).

**The three obstructions.**  One fact — there is no lattice inside
$\mathcal D$ — proved three independent times, each killing a different escape
route.  **O1** (113\_10 §5): the divisor group is a complex vector space, so
the effective cone is scaling-stable and $h^0(nD)=h^0(D)$, measured exactly at
$n=2,5,100$; this kills every growth argument, which is the engine of the
classical proof quoted in §1.  **O2** (113\_13 Thm 4.1): the correspondences
$\delta_n$ have infinite mutual intersection, since
$|(n/m)^\rho|=(n/m)^{1/2}\not\to0$; this kills discretisation.  **O3**
(113\_13 Thm 3.1): the negative part has no spectral gap,
$\sup\mathfrak s(f,f)/\|f\|^2=0$ on $\mathcal D^\circ\setminus\mathrm{rad}$,
not attained; this kills every coercive or compactness proof.

**Also missing: (c) is an identity, not an intersection number.**  Phase 108
Stage 5 proved the two natural routes to promoting it are closed (108_50,
108_53); phase 109 proved that any pairing reading the prime-power
coefficients is blind to the zeros, for **every** kernel (109_04 Thm 1.1).

## 3. (b) — what the correspondence row must deliver

(c) needs $\Gamma_n$ to be **divisor classes on the square**, so that
$\Gamma_n\cdot\Delta$ is an intersection number; a diagonal $\Delta$ in the
same group; composability, so the chain $\Gamma_m\circ\Gamma_n$ behaves; and
a transpose.

**Has.**  The shell functionals $\Gamma_{p,k}$, with
$\Gamma^{\mathrm{Tate}}_{p,k}(f_{1/2})=\Lambda(p^k)/\sqrt{p^k}$ (108_34,
108_35) — the Weil coefficient, exactly, at the central weight.

**Missing.**  They are **functionals, not cycles**.  Nothing attaches them to
elements of a divisor group on a square.  And the natural import is closed:
the Deninger–Morishita bridge annihilates the $p$-adic transverse direction,
because at a point over $p$ the residue field is $\overline{\mathbb F}_p$
with $\mu_{(p)}$ of order prime to $p$ (107_242 Thm 4.1).

## 4. (a) — what the space must deliver, and the growth constraint

(b) needs a product $X\times X$ with a divisor group, two rulings, a
diagonal, and an endomorphism generating the $\Gamma_n$.  (d) needs, through
the chain, a canonical class $K$ and a finite $h^0$.

**Has.**  A graded family $\mathcal G$ with $\Div$ and a principal subgroup
$\Prin'$ (108_03, 108_31, 108_33); difference-of-convex correspondence
potentials on the square with vanishing mixed interior density (107_237,
107_238).

**Has, and it is the right shape — for the curve.**  107_146 Corollary C
proves the Connes–Consani absolute dimension satisfies
$\dim_{S\pm}M_r=\Theta(\deg D)$, **linear** in the degree, in every rank
$r\ge1$.

That linearity is worth reading carefully.  Riemann–Roch on a **curve** gives
$h^0-h^1=\deg D+1-g$: linear in the degree.  Riemann–Roch on a **surface**
gives $\chi(D)=\chi(\mathcal O)+\frac{D^2-D\cdot K}2$: **quadratic**.
Requirement d3 is the quadratic one, since it is the $n^2D^2/2$ growth that
forces sections to exist.

> **The growth constraint.**  $\Theta(\deg D)$ is curve-like.  It is
> therefore a candidate dimension for $X$, not for $X\times X$.  What is
> missing is the **product structure** under which the dimension on the
> square grows quadratically.  Nothing in the programme has built or tested
> that.

This is a concrete, checkable gap, and it is invisible from the forward
direction: it only appears once one asks what growth rate d3 requires.

## 5. The map

```
(d)  Q <= 0 from geometry .......................... IS RH (113_10 Thm 4.2/4.3,
      |                                                    113_12 Thm 4.1)
      +-- d0  degree map, Z-valued on eff. classes ....... BUILT (113_10)
      +-- d1  form descends to LINEAR equivalence ....... BUILT, analytic half
      |        rad = the chi-ideal, chi = s(s-1)xi ......... (113_09 Thm 2.2)
      |        xi-divisibility on Schwartz data .......... ALIVE, used (113_07)
      |        xi-divisibility on compact support ........ CLOSED (110_02)
      |        a space with those principal divisors ..... MISSING -> row (a)
      +-- d2  polarization H, H^2 > 0 .................... HAVE; H = 2Phi is
      |                                                    effective (113_10)
      +-- d3  RR with quadratic D^2 term ................. IMPOSSIBLE inside D
      |                                                    (113_11 Thm 3.1/3.3)
      +-- d4  Serre duality / h^2 vanishing .............. BUILT, unconditional
      |                                                    (113_12 + 113_14)
      +-- d5  effective cone, D eff => D.H > 0 ........... BUILT, (R) proved
      |                                                    (113_10 Thm 2.2/2.5)
      +-- K = 0 (canonical class) ........................ BUILT (113_12 Thm 3.4)
      +-- (E^o), the residue ............................. EQUIVALENT TO RH
                    ^
(c)  Gamma . Delta = N
      +-- identity, analytic ............................. HAVE (108_36)
      +-- pairing, zero-free definition .................. HAVE (107_240, 113_06)
      +-- on Schwartz data, domain D stated .............. HAVE (113_07)
      +-- radical computed exactly ....................... HAVE (113_09)
      +-- Frobenius *-algebra, zero-free trace tau ....... HAVE (113_12 Thm 1.3)
      +-- nondegeneracy, both blocks ..................... HAVE (113_14 Thm 2.1)
      +-- as an intersection number OF CYCLES ............ CLOSED both routes
                    ^
(b)  Gamma_n as cycles
      +-- Weil coefficient Lambda(p^k)/sqrt(p^k) ......... HAVE (108_34/35)
      +-- as divisor classes, not functionals ............ MISSING
      +-- importable from foliated dynamics .............. CLOSED (107_242)
      +-- a lattice with finite mutual intersection ...... CLOSED (O2, 113_13)
                    ^
(a)  the space
      +-- Div, Prin' .................................... HAVE (108_03/31/33)
      +-- curve-like dimension Theta(deg D) ............. HAVE (107_146)
      +-- product structure => quadratic growth ......... MISSING
      +-- a working pairing ............................. CLOSED both sides
      +-- a Z-structure carrying a finite pairing ....... MISSING (O1, O2, O3
                                                          say none is inside D)
```

## 6. What the map changes

*Points 1–5 below were written before phase 113; point 6 records which of them
survived it.*

**1.  The binding constraint is not in (a).**  It is d1, at the (c)→(d)
edge: $\mathcal P\subseteq\mathrm{rad}\,I_\partial$.  Phase 108 spent
five stages building (a); the blocker sits one link later, and no amount of
work on (a) reaches it.  This is the main strategic finding.

**2.  Three requirements have never been attempted.**  d3 (Riemann–Roch),
d4 (Serre duality), d5 (the effective cone).  They are not blocked, not
closed, not hard-in-a-known-way — they are simply unbuilt.  Any of them
could be attacked today without waiting on d1.

**3.  d2 is already met** and had not been recognised as met.  The two
rulings give $H^2=2>0$.

**4.  The growth constraint is new and testable.**  A curve-like dimension
in hand, a surface-like one required, and no product structure connecting
them.

**5.  Positivity is produced, not assumed.**  The classical engine derives
$Q\le0$ from RR and effectivity.  Every attempt in this programme to reach
(d) by computing a signature has been circular precisely because it skipped
the engine.  The engine is d3+d4+d5, and it is the part nobody has built.

**6.  What phase 113 did to points 1–5.**

* Point 1 is **superseded**.  d1's analytic half is closed (113\_09 Thm 2.2),
  and the binding constraint moved back into (a) and (b): the absence of any
  integral structure at all, i.e. a4, b4, and the O1/O2/O3 triple saying no
  lattice is hiding inside $\mathcal D$.
* Point 2 is **spent**.  All three were attempted.  d4 and d5 are built; d3 is
  proved impossible inside $\mathcal D$.
* Point 3 stands, and is now stronger: $H=2\Phi$ is not merely a class with
  $H^2=2$, it is an *effective* one.
* Point 4 stands, untouched.  It is now the sharpest open item on the (a) side.
* Point 5 is **confirmed, and it is the whole story**.  The engine was
  assembled and it does not turn: the only input it still needs, $(E^\circ)$,
  is equivalent to RH.  Positivity is still not produced — it is now provably
  not producible *from this side*, since anything producing it would be a proof
  of RH.

## 7. What to do, in order

*Rewritten after phase 113.  "Prove $(E^\circ)$" and "prove the Hodge index"
are no longer entries on this list, because each of them is RH.*

1. **a4 — the product with quadratic growth.**  The CC absolute dimension is
   $\Theta(\deg D)$, curve-like; a surface needs $D^2$.  Untested, bounded, and
   independent of everything phase 113 did.  This is the top item.
2. **a-new / b4 — a space with a $\mathbb Z$-structure.**  Exhibit a space
   whose principal divisors are the $\chi$-ideal (113\_09 §5 makes this the
   candid statement of d1) **and** whose divisor group is a lattice on which
   the row-(c) pairing is finite.  O1 and O2 are the two tests any candidate
   must pass, and both are cheap to run.
3. **R16 — can a *quadratic* $\chi$ exist over $\mathrm{Spec}\,\mathbb Z$
   at all?**  Every Riemann–Roch actually available there is one-dimensional
   with a linear $\chi$.  If none can be quadratic, Ansatz A (113\_12 §5) is
   dead and this route with it.  A negative answer is as valuable as a positive
   one and is the sharpest open test the programme has.
4. **(b) as cycles** — only after (c) has an intersection number of cycles,
   which c10 (108\_50, 108\_53, 109\_04 Thm 1.1) currently forbids.

Not on the list: any further work inside $\mathcal D$ aimed at row (d).  It is
now a theorem that such work would have to prove RH.

## 7B. Status update: phases 114–118

*Added 2026-08-17. Five phases have run since the map was written. None of them
changes §7's priority list; all of them strengthen §6 point 5. Recorded here so
the map is not read as stale.*

### What changed, phase by phase

**Phase 114 — rows (a)–(c) written up.** Paper 42 exists. Row (d) was reduced to
the sharp Douglas gate and then to one explicit joint residual. The
local-construction campaign inside that reduction re-proved two obstructions
already recorded in the paper — a first sign that work on this side had become
self-repeating.

**Phase 115 — the diagnosis that row (d) is missing an *object*, not an
inequality.** Row (a)'s Green term is a rank cut (`ll^T − diag l`), and row (a)
attains `B = 0` on its own primitive space, so row (a) **is** row (d)'s equality
case. Target named: the mixed class **M**_f. This is §7 item 2 in different
language, and it remains unbuilt.

**Phase 116 — the Logarithmic Schur Angle Conjecture,** `rho_N <= 1/(20 log N)`,
extracted after rejecting a proposed Cauchy–Schwarz/Gamma-gap closure. Carried
verbatim into paper 42, where row (d) was completed *conditionally* on it.

**Phase 117 — the source route dies, and the conjecture is falsified.**
The comparison carrying the Gamma–Tate *source model* to the exact threshold
condition has best constant `c_N < 1` at every threshold `3 <= N <= 37`, decaying
like `(log N)^{-0.6}`. Galerkin restriction bounds `c_N` from **above**, so this
is one-sided-robust: the source route does not reach the target, whatever the
status of the source estimate. Separately, `rho_N <= 1/(20 log N)` is contradicted
by paper 42's own audit table at 4 of its 5 points. **New no-go for the ledger.**

**Phase 118 — §6 point 5, proved again from the analytic side.** Verified against
real zeros of zeta, to relative `5e-11`–`2e-9`, that for `F` primitive and
supported in `I_T`

    <A_T F,F> = sum_rho h(gamma_rho),      h(tau) = Fhat(tau) Fhat(-tau).

So the row-(d) inequality **is** localized Weil positivity on the primitive
space, hence equivalent to RH (Weil 1952; Yoshida 1992; Bombieri 2000). This is
`113_10` Thm 4.2/4.3 and `113_12` Thm 4.1 again, reached independently and by a
different method — algebra of `D` there, explicit formula against actual zeros
here. Two independent derivations of the same wall.

Three collapses make the identity exact rather than approximate, and all three
*validate* the construction: the pole terms die **because** `F` is primitive
(that is what the two Tate moments are for); `psi(1/4) = -(gamma + pi/2 + 3 log 2)`
forces `m_0 = log pi + gamma + pi/2 + 3 log 2` exactly, so the constant was never
a normalization choice; and the prime sum terminates at `n < e^{2T}` exactly
because the autocorrelation is supported in `(-2T,2T)`. Also observed:
`g_Gamma(tau) - m_0 = 2 pi *(zero density at tau) + o(1)`.

Phase 118 also: re-verified the balanced factorization `X^*X = R`, `Y^*Y = L`,
`X^*X - Y^*Y = A` to `~1e-12` by a code path independent of the original
assembly; **refuted** Toeplitz-in-`log n` and Hankel-in-`log n` structure for the
scattering operator (`R^2 <= 0.16`) and found no explicit `Psi` with
`I - Phi^*Phi = Psi^*Psi`; reproduced the `T <= log 2` certificate with all five
SHA-256 pins and diagnosed its limit as **analytic, not numerical** (precision has
5x headroom, tail quadrature 10x; the binding quantity is a Feshbach gap
`h = 0.0012` around one near-null direction, and extending to `(1/2)log 5` needs
two cross-coupling terms phase 114 attempted and retracted); and measured
`lambda_min(A_0) -> 0` directly under refinement (to `5.4e-8`), a direct
confirmation of **O3**.

### What this does to §7

**Nothing is added to the list and nothing is removed.** Items 1 (a4, quadratic
growth), 2 (a-new/b4, a space with a `Z`-structure), 3 (R16, whether a quadratic
`chi` can exist over `Spec Z` at all) and 4 ((b) as cycles) stand exactly as
written.

The "not on the list" clause is now broader. It read: *no further work inside `D`
aimed at row (d)*. Phases 117 and 118 extend it to:

* no further work on the **Gamma–Tate source model** — `c_N < 1` and decaying
  means it does not reach the target however sharp it becomes (117);
* no further work on **operator-theoretic reformulations** of the threshold
  inequality — factorization, Schur complements, defect operators, scattering.
  They are exact and worth having, and none of them adds arithmetic input; by
  phase 118's identity, anything closing the inequality closes RH (118).

### One item carried forward unresolved

Phase 118 left a two-route discrepancy in the numerical assembly: two
computations of the same `<A_T F,F>` for piecewise-constant `F` differ by 2%–8%
with a nearly constant absolute offset. `psi_kernel` was checked against 30-digit
`mpmath` (machine precision) and the four-point Gamma formula re-derived as
algebraically exact, so the assembly should carry no approximation; the suspicion
is truncation in the newer cross-validation script, **unverified**. It bears on
phase 117's `c_N` numbers if the assembly is the faulty side. See
`phase-118-the-exact-threshold-inequality/PROOF_ARCHITECTURE.md` §2.

## 8. Scope

**Established elsewhere, cited here, not re-proved.** 107_146 Corollary C;
107_237 Theorem 2.1; 107_238; 107_240 Theorem D and §5; 107_241 Theorem 3.1
and Corollaries 3.3, 3.4; 107_242 Theorem 4.1; 108_03; 108_31; 108_33;
108_34; 108_35; 108_36 Theorem 1.1; 108_50; 108_53; 109_04 Theorem 1.1;
110_02; and from phase 113: 113_06 Def 2.1 and Thm 3.2, 113_07 Def 1.3 and §3,
113_09 Thm 2.2 and Thm 3.1, 113_10 Thms 1.2/1.3, 2.2/2.5, 3.2, 4.2/4.3 and §5,
113_11 Thms 3.1/3.3, 113_12 Thms 1.3, 3.4, 4.1 and §5, 113_13 Thms 3.1 and 4.1,
113_14 Thms 2.1 and 3.3.  The consolidated audit with mechanically-checked
citations is 113_15; the phase summary is 113_99.

**Classical, cited, not re-proved.** The Hodge index theorem and its standard
proof; Riemann–Roch on curves and surfaces; Serre duality.

**Asserted here as audit, not theorem.** The requirement lists d1–d5 are a
reading of the classical proof, not a theorem that these are necessary and
sufficient; a different route to $Q\le0$ might need a different list.  The
"HAVE / MISSING / CLOSED" statuses are bookkeeping against the cited results.

**Not established.** That $H=F_v+F_h$ is ample, or a polarization in any sense
beyond $H^2>0$ together with the positivity-against-the-cone that 113_10 Thm
2.2/2.5 does prove. That the growth constraint of §4 is an obstruction — it is
a mismatch between what exists and what is required, and may be resolved by a
product construction nobody has tried.  And, from phase 113: a4, b2, b4, c10,
d3 inside $\mathcal D$, $(E^\circ)$, Ansatz A, row (d), and **RH**.

Nothing here bears on RH.  No status is promoted.  In particular, the
"BUILT" entries added for phase 113 are built *inside the analytic class
$\mathcal D$* and do not close row (d), which 113_10 Thm 4.2/4.3 and 113_12
Thm 4.1 show is equivalent to RH.  **RH is not proved.**
