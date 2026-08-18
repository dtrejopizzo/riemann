# 114.a.04 — The Mahler scalar gauge on rational Witt vectors: corrected I7 status

> **Superseded status notice (114.a.05).** The scalar Tate-telescoping lemma in
> this file is valid only with a global uniform `O(1)` hypothesis, but it does
> not construct or determine a Green function.  Moreover, the kernel of
> `(r,m)` does contain an explicit infinite-rank free abelian lattice, while
> the resultant intersection provably does not descend to `(r,m)`.  See
> `114_a_05_I7_KERNEL_AND_HARAN_REAUDIT.md`.  Claims below that the Green metric
> is fixed, that kernel-lattice existence is undecided, or that Haran has no
> section/divisor formalism are retracted in favor of that audit.

```
+--------------------------------------------------------------------------+
| ROW (a), ITEM a4 — STAGE 3: THE GAUGE                                    |
|                                                                          |
| THE OBJECT   W_rat(Z) = { P/Q : P,Q in Z[T], P(0)=Q(0)=1 },              |
|              the rational Witt vectors, with Witt addition = series       |
|              multiplication.  Free abelian on the irreducible P with      |
|              P(0)=1: a genuine divisor group.  Frobenius F_N: a -> a^N,  |
|              Verschiebung V_N: f(T) -> f(T^N),  F_N V_N = N.             |
|                                                                          |
| THE BIDEGREE r(f) = deg P - deg Q          (finite / horizontal)         |
|              m(f) = int_0^1 log|f(e^{2 pi i t})| dt  = sum log+|alpha_i| |
|                                                (archimedean, = Weil ht)  |
|              Both are HOMOMORPHISMS (verified, D1/D2), so m is a degree.  |
|              r o F_N = r,  m o F_N = N m,  r o V_N = N r,  m o V_N = m,  |
|              and F_N V_N acts as (r,m) -> (Nr, Nm).                      |
|                                                                          |
| THE RESULT   m is the UNIQUE scalar function of Frobenius weight one     |
|  (Thm 4.1)   lying at globally bounded distance from Mahler measure.      |
|              This does NOT construct/fix a Green function and does NOT   |
|              answer the fifth stop test.                                 |
|                                                                          |
| THE WALL     I7.  In the rank-2 quotient (r,m) the cyclotomic classes    |
|  (sec.6)     are Gamma_n = (phi(n), 0), isotropic, and <Gamma_n, Delta>  |
|              = 0 — while the finite intersection is Lambda(n), nonzero  |
|              when n is a prime power.                                   |
|              The bidegree is ARITHMETICALLY BLIND.  All of Lambda lives  |
|              in the kernel of the projection to rank 2.  Whether that    |
|              kernel DOES carry an explicit infinite-rank lattice, but    |
|              no positive Frobenius-weight-one gauge can see it.          |
|                                                                          |
| VERDICT a04  a4-STRONG WAS OPEN HERE.  W_rat(Z) is infinite-rank and     |
|              (r,m) is a lossy quotient to the rank-two toric sector, not |
|              an identification with its Arakelov divisor group.          |
| LATER        a144 closes the metrized bivariant a1--a5 construction.     |
|                                                                          |
| WARNING      Nothing here is evidence for RH.  No zero of xi appears.    |
|              The identity Lambda(n) = log|Res(Phi_n, T-1)| is NOT new:   |
|              it is the n=1 case of 106_210 eq (1).  Credit is 106's.     |
|                                                                          |
| VERIFIER     114_a_04_lambda_gauge.py — 25 checks A-J, exit 0,           |
|              VERDICT: ALL CHECKS PASS (output in sec.8).                 |
|                                                                          |
| GAPS         Jensen/Mahler comparison computed.  I7 descent is closed    |
|              negatively. G-2 and R8 are resolved in a_08/a_137;         |
|              G-1 is closed; G-3 is fully delimited through a_60: every  |
|              meaningful branch is RH-equivalent. Haran G-7 remains open.|
| CIRCULARITY  CLEAN.  No zero, no sign(Q), no Weil positivity, no Li      |
|              coefficient enters any definition or proof.                 |
+--------------------------------------------------------------------------+
```

**Depends on:**

- `03-research/phase-114-closing-the-four-rows/114_a_02_AN_ARITHMETIC_SURFACE_OVER_SPEC_Z_WITH_QUADRATIC_H0.md`
  — Def 1.1, the form $\langle(k,a),(k',a')\rangle = ka'+k'a$, Thm 3.4, §7.3.
- `03-research/phase-114-closing-the-four-rows/114_a_03_THE_CANDIDATE_LEDGER.md`
  — §4 (Arakelov passes), §5 (Deninger / rational Witt vectors), **Gap G-4**, §6.2 **Gap G-7**.
- `03-research/phase-106-global-modular-star-audit/106_210_CYCLOTOMIC_DIAGONAL_STOP_TEST.md`
  — eq (1), eq (4), eq (10), eq (13), §4, §6, §7, §8. **Read in full.** This file is prior art
  for the resultant identities below and is credited as such throughout.
- `03-research/phase-107-arithmetic-lefschetz-reconstruction/107_242_*.md` — §5 ("a construction of
  the Frobenius graphs directly inside the row-(a) divisor group … is the candid route,
  and it is a row-(a) task").
- `03-research/phase-113-the-trace-on-schwartz-data/113_09_*.md` — §4 ($f_v^2=f_h^2=0$,
  $f_v\!\cdot\! f_h=1$, $H^2=2$, $(f_v-f_h)^2=-2$, measured from primes).

---

## 1. What is and is not claimed

Not claimed, and stated first so that nothing below can be read as more than it is:

1. **The identity $\Lambda(n) = \log|\operatorname{Res}(\Phi_n, T-1)|$ is not new.** It is the
   $n=1$ case of `106_210` eq (1), $\tfrac1{\varphi(n)}\log|\operatorname{Res}(\Phi_m,\Phi_n)| =
   \log p$ when $m/n = p^a$ and $0$ otherwise. I rederived it before finding `106_210`; the
   credit is `106_210`'s.
2. **No square is constructed here.** $(\operatorname{Spec}\mathbb Z[T], \psi^N : T\mapsto T^N)$
   is $\operatorname{Spec}\mathbb Z \times_{\mathbb F_1} \mathbb A^1_{\mathbb F_1}$, not
   $\operatorname{Spec}\mathbb Z \times_{\mathbb F_1} \operatorname{Spec}\mathbb Z$. The
   "second $\operatorname{Spec}\mathbb Z$" appearing below is $\mathbb N^\times$, the index set
   of the Frobenii, and that is a weaker object.
3. **At the stage of this file, a4-strong was not closed.** The later
   construction `a_144` supersedes that status and closes the metrized
   bivariant a1--a5 contract. See §7.

Claimed:

4. `$W_{\mathrm{rat}}(\mathbb Z)$` carries a canonical bidegree `(r,m)`, both
   components homomorphisms and compatible with the Witt operations (§3).
5. The scalar component $m$ is **uniquely determined within the globally
   bounded Frobenius-weight-one class**, by Tate telescoping (§4, Thm 4.1).
   This does not determine a Green function or answer `106_210`'s fifth stop test.
6. The rank-2 quotient generated by `(r,m)` cannot reproduce the arithmetic:
   `$\langle\Gamma_n,\Delta\rangle=0$` there, while the finite intersection is
   `$\Lambda(n)$`, nonzero for prime powers (§6). The exact collision
   `$n=3,6$` proves non-descent in `114_a_05`.

---

## 2. $W_{\mathrm{rat}}(\mathbb Z)$ maps to, but is not, the rank-two Arakelov sector

**Definition 2.1.** $W_{\mathrm{rat}}(\mathbb Z) = \{P/Q : P,Q\in\mathbb Z[T],\ P(0)=Q(0)=1\}
\subset 1+T\,\mathbb Z[[T]]$, an abelian group under multiplication of series ("Witt addition").

**Proposition 2.2.** $W_{\mathrm{rat}}(\mathbb Z)$ is free abelian on the irreducible
$P\in\mathbb Z[T]$ with $P(0)=1$. Writing $P = \prod_i(1-\alpha_i T)$, an element is the formal
$\mathbb Z$-combination of the algebraic numbers $\alpha_i$ — i.e. a $0$-cycle of algebraic
integers, i.e. a horizontal divisor on $\mathbb A^1_{\mathbb Z}$.

*Proof.* Unique factorisation in $\mathbb Z[T]$, restricted to the multiplicative subset with
constant term $1$ (which contains no units other than $1$). $\square$

**Remark 2.3 (corrected quotient relation).** `W_rat(Z)` and the rank-two toric
Arakelov divisor group are not the same object.  The former is free abelian of
infinite rank and contains the kernel constructed in `114_a_05`; the latter is
the quotient sector measured by `(r,m)`.  Their bounded-degree polynomial
section lattices agree, but their ambient divisor groups do not.

---

## 3. The canonical bidegree and its Witt-operation laws

**Definition 3.1.** For $f = P/Q \in W_{\mathrm{rat}}(\mathbb Z)$,
$$r(f) = \deg P - \deg Q, \qquad
  m(f) = \int_0^1 \log|f(e^{2\pi i t})|\,dt .$$

**Proposition 3.2 (Jensen).** $m(f) = \sum_i \log^+|\alpha_i|$, the sum over the inverse roots,
i.e. logarithmic Mahler measure, equivalently the unnormalised total Weil
height of the zero-cycle.

*Verified:* C1, eight polynomials, agreement to $10^{-40}$, including cases with roots **on**
the unit circle. The `114_a_03` Gap G-4 states that this comparison "is **not carried out
here**"; it is carried out here.

**Proposition 3.3.** $r$ and $m$ are group homomorphisms $W_{\mathrm{rat}}(\mathbb Z)\to\mathbb Z$,
$\mathbb R$. In particular **$m$ is a degree**, not merely a norm. *Verified:* D1, D2.

**Proposition 3.4 (the Witt operations act diagonally).** With $F_N:\{\alpha_i\}\mapsto
\{\alpha_i^N\}$ and $V_N: f(T)\mapsto f(T^N)$,
$$r\circ F_N = r,\quad m\circ F_N = N\,m,\quad r\circ V_N = N\,r,\quad m\circ V_N = m,$$
and consequently $F_NV_N$ acts on the bidegree as $(r,m)\mapsto (Nr,Nm)$, matching the Witt
identity $F_NV_N = N$. *Verified:* E1 (non-vacuously — see §8), F1.

**Proposition 3.5 (Kronecker).** For `$P\in\mathbb Z[T]$` with `P(0)=1`,
`m(P)=0` iff `P` is a product of cyclotomic polynomials. Equivalently, all
inverse roots are roots of unity. These elements are **not torsion** in the
additive group of `W_rat(Z)`, which is free abelian; they form the cyclotomic
kernel lattice studied in `114_a_05`. *Verified:* G1--G3 (the last against
Lehmer's number to 39 places).

---

## 4. Scalar uniqueness does not pass 106_210's fifth stop test

`106_210` §4, verbatim: *"The finite cyclotomic divisor does not determine it [the Green
metric]."* Its fifth stop test asks for a finite, **source-defined** self-intersection in the
same category, without importing an unrelated diagonal form or choosing its sign. It failed
because $\operatorname{Res}(\Phi_n,\Phi_n)=0$, the derived $\operatorname{Tor}$ is not finite,
and $\operatorname{div}(\Phi_n)$ is principal in the UFD $\mathbb Z[x]$.

The valid observation of this note is only a scalar rigidity statement for the
Mahler functional.  The missing Green diagonal is not supplied by it.

**Theorem 4.1 (Tate-style telescoping uniqueness).** Let
`$\lambda:W_{\mathrm{rat}}(\mathbb Z)\to\mathbb R$` satisfy
$$\lambda\circ F_N = N\,\lambda \quad (N\ge 2), \qquad \lambda = m + O(1).$$
Then $\lambda = m$.

*Proof.* Fix $f$ and $N=2$. Let $B$ bound $|\lambda - m|$. For every $k$,
$$|\lambda(f) - 2^{-k}m(F_2^k f)| = 2^{-k}\,|\lambda(F_2^kf) - m(F_2^kf)| \le 2^{-k}B .$$
But $m\circ F_2^k = 2^k m$, so $2^{-k}m(F_2^kf) = m(f)$ identically. Letting $k\to\infty$ gives
$\lambda(f)=m(f)$. $\square$

*Verified:* H1 (the bound $B/N^k\to0$), H2 ($m(F_2^kf)/2^k$ is **exactly** constant, spread
$0.00\mathrm{e}{+00}$ at 40 digits), H3 (its value is $\log 2$ for $f=1-2T$).

**Corollary 4.2 (corrected scope).** Within the class of real-valued
functionals satisfying the uniform bounded-distance hypothesis of Theorem 4.1,
Mahler measure is the unique Frobenius-weight-one functional.  No conclusion
about Green functions, diagonal regularisation, or intersection pairings
follows.  `114_a_09` further proves that every such functional vanishes on the
cyclotomic kernel.

---

## 5. The Frobenius graphs and $\Gamma_n\cdot\Delta$

**Definition 5.1.** $\Gamma_n := \operatorname{div}(\Phi_n)$, $\Delta := \operatorname{div}(T-1)$.

**Proposition 5.2.** For `n>1`, `$\Phi_n(1)=e^{\Lambda(n)}$`, hence
`$|\operatorname{Res}(\Phi_n,T-1)|=\Phi_n(1)$` and
`$\langle\Gamma_n,\Delta\rangle_{\mathrm{fin}}=\Lambda(n)$`. Separately,
the arithmetic identity `$\sum_{d\mid n}\Lambda(d)=\log n$` holds.

The latter sum is **not** asserted to be the intersection of
`$\operatorname{div}(T^n-1)$` with `Delta`: the factor `Phi_1=T-1` makes that
intersection improper and its ordinary resultant zero. A diagonal
regularisation would be precisely part of the still-open fifth stop test.

*Verified:* A1 ($2\le n\le 400$), A2, A3. *Prior art:* `106_210` eq (1), of which this is the
$n=1$ case. B1 re-verifies `106_210` eq (1) itself on 462 divisible pairs and B2 verifies
$\operatorname{Res}=\pm1$ on 708 non-divisible pairs.

---

## 6. Gap G-9: the rank-2 quotient is arithmetically blind

Give $\mathbb Z\oplus\mathbb R$ the hyperbolic form $\langle(k,a),(k',a')\rangle = ka'+k'a$ of
`114_a_02`. The rulings $f_v=(1,0)$, $f_h=(0,1)$ satisfy $f_v^2=f_h^2=0$, $f_v\cdot f_h=1$,
$H^2=2$, $(f_v-f_h)^2=-2$, reproducing `113_09` §4 — which was measured from primes, by a
different route. *Verified:* I1–I5.

But by Prop 3.5, $m(\Phi_n)=0$, so

$$\Gamma_n \longmapsto (\varphi(n),\,0), \qquad \Delta\longmapsto (1,0),$$

whence `$\langle\Gamma_n,\Gamma_n\rangle=0$` and
`$\langle\Gamma_n,\Delta\rangle=0$` in the quotient. For prime-power `n`
the finite intersection `$\Lambda(n)$` is nonzero; more strongly, `n=3` and
`n=6` have the same bidegree but intersections `log 3` and `0`. *Verified:*
I6--I7 and `114_a_05` B1--B2.

**G-9, corrected by `114_a_05` and `114_a_09`.** The bidegree `(r,m)`
annihilates the arithmetic.  Its kernel contains the explicit free lattice
`E_n=C_n-phi(n)C_1`.  Nevertheless no form on the rank-two quotient can recover
the resultants, no positive Frobenius-weight-one scalar gauge can see the
fixed `E_n`, and a global Picard pairing annihilates these principal classes.

The two readings originally proposed here are now decided for this route:

- **Historical analogy only.** On `$C\times C$`, Frobenius intersections split
  into trivial and Jacobian pieces. This does not define either piece here
  and is not used as evidence.
- **Actual obstruction.** Rank two is not all there is algebraically, but every
  weight-one scalar gauge is forced to vanish on the extra lattice. The
  separate phase-113 obstructions on the trace space are not automatically
  statements about `W_rat` and are not invoked here.

Thus the `W_rat/P1` route is closed negatively as a simultaneous solution of
principal invariance, raw resultant intersections and a weight-one kernel
gauge.  `114_a_17` constructs nonprincipal prime-incidence carriers on Haran's
square with `Delta cap V_p=Spec F_p`; a place-wise intersection complex and a
correspondence law extending those carriers remain open.  After the type
correction `a_66`, `114_a_18` supplies nontrivial external unit-torsor lifts
with diagonal degree `log p`; promotion to Section-11 completed bundles is
conditional on H7-PRIME-REG.

---

## 7. Status of row (a)

The long `G-7 (Haran)` entry below records the obstruction campaign only
through `a_103`; it is retained as provenance and is superseded by the
`G-7 current` entry plus the correction chain immediately after the table.

| item | status |
| --- | --- |
| a4-weak | **CLOSED** (`114_a_02`, unchanged) |
| Mahler scalar rigidity | **CLOSED HERE** (Thm 4.1, corrected scope) |
| `106_210` fifth stop test / Green diagonal | **OPEN** |
| G-4 (Witt gauge/pairing) | scalar degree exists, but a positive proper kernel gauge is **impossible in weight one** (`a_09`); pairing absent |
| **G-9** (rank-2 blindness) | **CLOSED NEGATIVELY for descent** (`a_05`, `a_09`) |
| G-7 (Haran) | **OPEN, refined through `a_103`.** Literal incidences, contact sheaves, scalar/tree constructions and abstract `Pic_tor` pullbacks exist; `a_61` gives faithful unit-torsor labels and `a_19` a discrete bigrade. Completed-lattice/gauge realization requires H7-PRIME-REG. `a_67`--`a_70` give typed contact, excess splitting and faithful decorated composition. `a_71`--`a_75` close all signed read-once trees. `a_76` identifies `(E_cancel:p)=E_cancel`; `a_77`--`a_79` close only the visible fixed-incidence subsystem. `a_81` retracts presentation-completeness using the contextual-zero `K2,2`. `a_82` proves all rectangular macro contexts saturated; `a_83` gives exact cycle-Laplacian Smith obstructions; `a_84` gives the conditional tame/scalar reduction. `a_85` closes H7-MACRO-PRESENT using Haran's sandwich-path theorem and splits saturation into p-CONVEX plus p-DIVPATH. `a_86` proves that p-CONVEX is exactly H7-p-ONE-BOUNDARY. `a_87` supplies the simultaneous characteristic-zero route H7-REAL-RES plus H7-TAME-PLANE; `a_88` proves its unary targets are blind to bilateral leaf matching; corrected `a_89` computes fixed-grid total-mass saturation; `a_90` closes laminar no-reuse cut systems; `a_91`--`a_98` audit and reject bare, positive and block-extractable scalar-invisible parity variants; `a_99` splits any remaining nonextractable rigidity into nontameness or failure of context retraction; `a_100` proves finite-set contraction/reuse itself always has coordinate retractions; `a_101` proves every correctly oriented split outer coefficient transmits all scalar sandwiches and shows nonsplitness alone is insufficient. The residual parity branch is H7-COEFF-ANN: a genuinely nonsplit context must annihilate an ambiently separable pair. `a_102` identifies scalar saturation exactly with torsion-freeness/ordinary `Z`-flatness of the off-diagonal augmentation ideal `K=ker(nabla)` and proves that the split fold alone does not imply it. `a_103` extracts Haran's first necessary tameness test: every centre-versus-Cartesian-grid cross defect is automatically invisible to all scalar sandwiches, so a surviving mixed generator defect H7-XDEF-12 would explicitly refute tameness. Its equality in the signed quotient is open. H7-AUG-FLAT plus H7-TAME-PLANE is the simultaneous all-prime route; alternatively p-CONVEX/p-DIVPATH remain. Geometric boundary transport, H7-DEN-TRANS and H7-SEL-MOM/RR/EXACT remain |
| G-1 | **CLOSED** (`a_11`: exact coupled constant `1/log 2`) |
| G-3 | **FULLY DELIMITED through `a_60`.** Pointwise non-additive domination is vacuous. Additive domination, non-additive two-point polarization/Kunneth, and the exact effectivity branch G3-EFF are each RH-equivalent. Constructing meaningful G-3 is the RH step, not a prior unconditional lemma |
| G-2 | **CLOSED** (`a_08`: unavoidable `-km log m`) |
| R8 acceptance test | **CLOSED** (`a_08`, scope fixed by `a_137`); the forced threshold is `h_theta(O_X)`. The full effectivity dictionary is a separate G3-EFF/G-7 gate |
| **a4-strong** | **CLOSED METRICALLY/BIVARIANTLY (`a_144`)** |
| G-7 current (`a_109`--`a_144`) | **ROW-A CLOSED.** `a_132` gives `Y^locreg`; `a_140` integrates faithful dynamics with geometric contact; `a_141` supplies the contact determinant; `a_142` constructs the normalized RR determinant from calibrated section images; `a_143` proves valued boundary faithfulness by a non-circular Picard norm; and `a_144` assembles one Div/Prin/product/pairing/gauge object satisfying a1--a5. Bare H7-RSPH-UNIT is an optional unmetrized strengthening |

**Current correction (`a104`--`a106`, superseding the `a103` end of the G-7 row):**
H7-XDEF-12 is closed negatively and H7-TAME-PLANE is false.  The
infinitesimal separator is valid for the full signed plane.  Therefore the
H7-AUG-FLAT-plus-tameness promotion is no longer live; direct
p-CONVEX/p-DIVPATH/componentwise prime regularity remains open.  Both
ordered first-jet targets are nevertheless prime-regular in every arity, so
any collision is confined to their common `N`-jet kernel; this need not be
purely higher-order.  `a_106` decides the source omission negatively:
`[1,1|1]` is an infinite-order entropy class killed by `C Omega -> N`.
The rationalized universal replacement
`F(Z) Pi (C Omega tensor Q)` is prime-regular in every arity, so every
possible collision lies in the common kernel of both ordered universal
rational jets.  That leaves integral torsion in `C Omega` and genuinely
nonlinear/higher-order differences.

**Decisive correction (`a107`--`a108`):** the integral scalar differential
has exactly one `Z/2` class `tau`, and it integrates to
`kappa=(1,-1)_1 o (1,1)_2^t` in the plane.  A middle-wire transposition gives
`kappa=-kappa`, hence `2kappa=0`, while the universal infinitesimal target
sends it to `tau!=0`.  Therefore H7-AUG-FLAT and H7-PRIME-REG are **false**
at `p=2`.  The conditional Section-11 completed-lattice route is closed
negatively; the literal square, prime rulings, contacts and `Pic_tor`
labels survive.  G-7 now requires a torsion-aware divisor/cycle repair that
retains the `Lambda(2)` contact.

`a_109` constructs that repair at the base: the universal simultaneous
Z-regular reflection `P^reg` kills `kappa`, retains both split arithmetic
axes and the `a104` non-total cross defect, and still has
`Delta^*V_p^reg=Spec F_p`.  `a_110` proves functorial affine gluing and
pro-transition compatibility on finite charts. After the type correction
`a_131`, `a_132` gives the actual modified pro-square `Y^locreg->Y` on
which every prime-generated completed lattice `L_n` exists faithfully.
This repairs the specific regular-denominator failure. `a_111` then realizes,
for every pair of distinct primes, a free rank-two subgroup of actual regular
Cartier-act data and completed Picard classes.  Its diagonal-contact degree
is the geometrically forced `m log p+n log q`.  This is a genuine
divisor/degree baseline, not yet a global bilinear intersection product;
`a_112` extends it to all primes on either axis, identifies every possible
two-axis relation as prime-by-prime anti-diagonal, and constructs the genuine
partial pairing `I(Delta,V_(p,i))=log p` from literal finite fiber products.
The mixed/self entries require H7-REG-MIXDEG; full intersection, section RR
and gauge on `Y^locreg` remain open. `a_113` nevertheless computes another
forced block: distinct primes on the same ruling have empty fiber product by
Bézout, hence intersection zero.  Only opposite-ruling products and
self-intersections remain uncomputed. `a_114` constructs the entire reduced
opposite-ruling block from canonical contact retracts:
`I_red(V_(p,1),V_(q,2))=delta_(p,q) log p`.  The full cross quotients may
carry generalized excess, so this does not yet supply the full product.
`a_115` proves that this excess is indispensable: the reduced contact differs
for every prime pair from the RR-forced global value
`(log p log q)/(2 log 3)`.  Lambda contact and global RR intersection must be
distinct compatible outputs, with H7-REG-EXCESS-RR constructing their
complement. `a_116` constructs the RR-forced hyperbolic form on the all-prime
presentation lattice and proves that it descends to completed Picard exactly
when the residual prime anti-diagonal map is faithful.  The correction `a122`
shows that bare H7-U3/LD on the literal square is not sufficient after
restriction to the repaired square: one also needs H7-REFL-PIC. Equivalently, the direct
geometric target is H7-RULING-PF, a separate product formula for the two
ruling degrees.

On the section side, `a_117` gives the first sharp selective construction on
the formerly obstructing saturated rays: projecting the `m`-moment block to
the first `floor((log2/(2log3))m)` coordinates is multiplicative, is hit
surjectively by genuine bounded sections, and has dimension
`d_1d_2/(2log3)+o(m^2)`.  This closes coefficient selection per block, not
DEN-TRANS, presentation-independent gluing or sheaf exactness.

`a_118` bypasses the `a_57` denominator collision for a degreewise invariant:
each standard divisor chooses a fresh canonical controlled prime, and
products are reevaluated directly in the fresh block of `D+E`.  This gives
definition, principal invariance and source multiplication without retaining
old characteristics.  It does not provide target transitions or restriction
control.  The former name H7-FRESH-EXACT is corrected by `a_125`: target
transitions are impossible, and only sourcewise H7-FRESH-RESTR is typed.

There is also a single-target algebraic repair: `a_119` uses an ultraproduct
of controlled finite fields to obtain a characteristic-zero pseudofinite
field in which every fixed odd power is bijective.  All rational denominators
and all odd-moment bios coexist, so algebraic DEN-TRANS is closed.  The target
is infinite, however; converting it into the required finite/height
dimension with genuine-section exactness is the new H7-PF-DIM gate.

`a_120` removes the remaining ray restriction from the finite degreewise
route.  On any positive effective ray, orient the coefficient vector along
the larger degree, use the odd powers `1,3,9,...` and the small nodes
`1,...,m`, and choose a fresh prime `p=2 mod 3` avoiding their generalized
Vandermonde determinant.  Genuine bounded sections then surject onto
`F_p^m`.  Retaining
`floor(t^2 deg(A)deg(B)/(2 log(3) log(p)))` coordinates gives the exact
asymptotic

\[
 h(tD)={t^2\deg(A)\deg(B)\over2\log3}+O(t)
\]

on every ray with both degrees positive.  Thus all-ray coefficient
calibration is closed; restriction/cohomology exactness and its geometric
identification with H7-REG-EXCESS-RR remain open.

The presentation qualifier is essential.  `a_121` proves that the `a_120`
section asymptotic descends to actual completed Picard classes if and only if
the prime anti-diagonal map is injective.  The proof compares two positive
rays separated by a hypothetical anti-relation: they represent the same
Picard classes at every scale but have different quadratic degree products.
This is exactly the same descent gate as the RR form in `a_116`; section
canonicity and intersection descent are no longer independent unknowns.

`a_122` identifies H7-RULING-PF as the exact direct route that would make the
two degrees descend separately.  `a_128` audits the only obvious
counterexample and rejects it: `p_2/p_1` cancels every finite valuation, but
its remaining factors `p` and `1/p` are not `O`-units on Haran's real unit
ball.  `a_129` consequently identifies the possible kernel exactly with the
kernel of the residual mixed archimedean boundary classes H7-ARCH-BDRY.

Finally `a_123` globalizes the complementary value of `a_115`.  On the
whole prime presentation lattice the reduced contact form is

\[
 C_\Lambda(x,y)=\sum_p\log p,(x_{p,1}y_{p,2}+x_{p,2}y_{p,1}),
\]

and the unique numerical Green correction is
`G_num=B_RR-C_Lambda`.  Hence

\[
 G_{\rm num}(D_{p,1},D_{q,2})
 ={\log p\log q\over2\log3}-\delta_{pq}\log p.
\]

The RR form, local contact, section asymptotic and numerical Green correction
all have exactly the same anti-diagonal descent gate.  That gate is now
H7-ARCH-BDRY: construct the two mixed-boundary norm maps and prove that their
values `log p` detect every finite integral combination.  The numerical
Green matrix cannot itself be used as that detector before geometric descent
without circularity.

`a_124` upgrades the matrix to a canonical metrized biextension.  For every
pair `(x,y)` of prime presentations, take the real line generated by
`1_(x,y)` with norm `exp(-G_num(x,y))`.  Bilinearity makes addition in either
variable an isometric tensor law, and

\[
 \mathcal E_{C_\Lambda}\otimes\mathcal E_{G_{\rm num}}
 \simeq\mathcal E_{B_{\rm RR}}
\]

isometrically.  Its quadratic gauge is `q_G(x)=G_num(x,x)/2`.  This closes
the normed-line Green object on the decorated presentation.  Descent to
completed Picard remains conditional on H7-ARCH-BDRY, followed by comparison
with actual Cartier data.

`a_125` corrects the last exactness formulation.  Distinct fresh finite
targets have different characteristics and admit no unital transition maps;
moreover Haran's completed section sheaves are right acts/sets, not the
abelian modules of Section 6.  Therefore target-sheaf transitions and a long
exact cohomology sequence are not a typed gate.  The correct replacement is
H7-FRESH-RESTR: form a restriction diagram in the source right acts,
reevaluate the whole diagram in one fresh target attached to its output, and
prove directly the fiber/cardinality identity needed by RR.

`a_126` closes the open-sheaf part of that replacement.  For every finite
diagram of open restrictions, choose one prime avoiding the union of its
denominators.  Localization and evaluation of the same rational operation
then commute literally, so evaluated global images include in evaluated
local images and multiplication remains natural.  The only restriction gate
left there appeared to be H7-FRESH-CARTIER.  `a_127` proves that its
common-target formulation is impossible: the inverse generic chart makes
the Cartier prime a unit, whereas its closed quotient kills that same prime.
The two evaluations cannot share a nonzero unital apex.  The corrected gate
is H7-TWO-TARGET-DELIGNE: compare the separate generic moment and residue
contact objects by determinant/norm lines, and prove descent, without a map
between their targets.

**Historical status at `a_127`: row (a) was not closed. The later
construction `a_144` closes it in the metrized bivariant category.**

---

## 8. Verifier

`114_a_04_lambda_gauge.py`, `mp.dps = 40`, 25 checks in blocks A–J, exit 0,
**VERDICT: ALL CHECKS PASS**.

Three errors were found and fixed during construction, all mine, and they are recorded because
two of them produced *passing* checks:

1. **Reciprocal reversal.** For $P(T)=\sum c_jT^j$ with $c_0=1$, the monic polynomial with roots
   $\alpha_i$ is $A(x)=x^dP(1/x)=\sum_j c_jx^{d-j}$, whose leading-first coefficient list is
   `coeffs` *verbatim, not reversed*. I had it reversed in both `mahler_roots` and `frob`.
   Consequence: $m$ returned $0$ almost everywhere, so **D2 and E1 passed vacuously** — the
   worst kind of false positive. Fixed; E1's printed table (§ output) now shows non-zero $m$.
2. **Quadrature partition.** Every cyclotomic has all roots *on* the unit circle, so
   $\log|P(e^{2\pi i t})|$ is logarithmically singular. mpmath's tanh-sinh rule handles
   **endpoint** singularities, so the cure is to place each singularity at a node:
   $P(z)=\prod(1-\alpha_iz)$ vanishes at $z=1/\alpha_i$, giving nodes $t=-\arg(\alpha_i)/2\pi$
   for $|\alpha_i|=1$. A blind uniform partition left $\Phi_5$ off by $8.8\times10^{-6}$; with
   the corrected partition the error is $1.35\times10^{-41}$.
3. **Lehmer.** Wrong coefficients *and* a wrong remembered reference constant, which did not
   cancel. The polynomial is $x^{10}+x^9-x^7-x^6-x^5-x^4-x^3+x+1$, palindromic. The check now
   compares against Lehmer's number $\lambda = 1.176280818259917506544070338474035050693$, an
   independently tabulated constant, rather than against a remembered value of $\log\lambda$.

Block J measures $\delta = 2.019$ and the leading constant $\to k\cdot a$; this reproduces
a4-weak's growth and is **not** independent evidence for anything beyond it.

---

## 9. Refutation conditions

Audit of the originally registered refutation conditions:

- **R30-a.** A $\lambda\neq m$ satisfying both hypotheses of Thm 4.1. (Then Cor 4.2 fails and
  `106_210` §4 stands.)
- **R30-b — RETIRED.** Its premise is false: `114_a_05` constructs an explicit
  infinite-rank kernel lattice. What fails is the desired gauge/pairing.
- **R30-c — FIRED against the original reading.** `114_a_05` proves by the
  `(3,6)` collision that the finite resultant pairing does not factor through
  `(r,m)`, and `114_a_09` adds the principal-invariance obstruction. Section
  5 above is now explicitly local and does not claim a diagonal completion.
- **R30-d — attribution condition only.** The finite resultant identity remains
  credited to `106_210`; it has no bearing on the corrected theorems here.

---

## Scope

**Proved here.** Prop 2.2; Remark 2.3 (the quotient relation between the Witt and toric sectors);
Prop 3.3 ($r,m$ homomorphisms); Prop 3.4 (the action of $F_N,V_N$ on the bidegree); **Thm 4.1**
(bounded Frobenius-weight-one scalar rigidity) and corrected Cor 4.2; rank-two blindness.

**Read from source.** Jensen's formula (Prop 3.2); Kronecker's theorem (Prop 3.5); `106_210`
eq (1), eq (4), eq (10), eq (13), §4, §7, §8; `114_a_02` Def 1.1 and the hyperbolic form;
`113_09` §4; `114_a_03` Gaps G-4 and G-7; `107_242` §5.

**Verified numerically.** All 25 checks A–J of `114_a_04_lambda_gauge.py` at 40 digits:
A1–A3 ($\Phi_n(1)=e^{\Lambda(n)}$ to $n=400$; $\sum_{d|n}\Lambda(d)=\log n$; the resultant
form); B1–B2 (`106_210` eq (1) on 462 pairs; $\operatorname{Res}=\pm1$ on 708); C1 (Jensen, 8
polynomials, $10^{-40}$); D1–D2 (homomorphism); E1 (the four equivariances, non-vacuously);
F1 ($F_NV_Nf=f^N$); G1–G3 (Kronecker, Lehmer); H1–H3 (Tate telescoping, exact constancy);
I1–I7 (the rulings, and the blindness); J1–J2 ($\delta=2.019$).

**Not established.** A proper kernel gauge and a finite diagonal compatible
with the place-wise resultant data.  The kernel lattice itself is constructed
in `114_a_05`, while `114_a_09` proves the weight-one/principal-invariant
versions impossible.  It is also not established that
$\operatorname{Spec}\mathbb Z\times_{\mathbb F_1}\operatorname{Spec}\mathbb Z$ is realised
by the present Witt construction. Haran's non-totally-commutative pro-square
is a separate literal construction. Files `a_17`--`a_20` construct its
prime-incidence, prime Picard and discrete-bigrade data; `a_24`--`a_29`
split the quadratic section gate into typed alternatives, and `a_30` closes
real boundedness on the Laurent route. `a_31` proves that full H7-DFLAT/LNF
would contradict H7-U through operadic leaf inflation. A selective quotient
H7-SEL, normalized dimension, complexity truncation or different gauge is
therefore required. `a_32` proves that the balanced quadratic code alone is
not multiplicatively closed; coefficient-additivity repairs closure only by
collapsing its entropy to the diagonal. `a_33` corrects the stronger-than-
necessary closure demand and constructs a finite-moment normalized dimension
with matching quadratic lower/upper size in the Laurent sector on positive
rays. `a_49` closes its descent H7-FMD. Its extension to all scalar trees
remains absent. `a_34` proves that the ternary rank is optimal,
derives the forced sectorial coefficient
`log(2)log(q)/(2log(3))`. `a_55` shows that the present complete-bounded
moment image cannot promote this coefficient: it contains bounded cross
interpolators with a strictly larger quadratic entropy. Promotion now
requires the replacement gate H7-SEL-RR/EXACT.
`a_35` extends the bounded construction to every fixed arity and arbitrary
effective second denominator, proving that this coefficient depends only on
the two idelic degrees, not on the selected primes or tree arity.
`a_36` audits Haran 2022 and closes the correspondence algebra at the exact
operator level: `V_mV_n=V_mn` is faithful and its lambda-trace diagonal mass
is `Lambda(n)`. The operators are not divisors of the pro-square; realizing
them with the same mass is the explicit gate H7-I7-REAL.
`a_37` realizes the Frobenius maps as compatible literal graphs on the
finite-stage Witt pro-scheme. It also proves that every stage and its
relative square are finite over `Spec Z`, hence one-dimensional. The graph
space cannot replace Haran's surface; transport and the trace/intersection
identity are the separate gates H7-WBASE and H7-WLEF.
`a_38` rules out the naive transport: every map to an ordinary Witt ring
identifies the two integral additions and factors through the diagonal fold.
Any surviving H7-WBASE must therefore be a genuinely non-totally-
commutative kernel/functor, not ordinary scalar base change.
`a_39` constructs the exact scalar shadow of such non-total targets by
multiplicatively conjugating real addition. The second integral embedding is
`n -> sgn(n)|n|^u`, so a full bio lift would give every power evaluation and
prove H7-LNF. Constructing its higher-arity operations, co-operations and
involution was the gate H7-TBIO left by `a_39`.
`a_40` constructs those higher operations universally by a coproduct and
unary coequalizer in commutative involutive bios. `a_49` represents this
quotient in the involutive double of the homogeneous endomorphism bio. Since
the common scalar `a` acts by `x -> ax`, evaluation at `1` proves H7-UEMB for
every parameter. Consequently H7-TBIO, H7-LNF and sectorial H7-FMD descent
are closed; H7-FMD-ALL and RR promotion are not.
`a_50` removes the moving-characteristic obstruction to degree functoriality
on fixed effective rays by accumulating separating primes in nested moduli.
Its transition maps are exact and retain quadratic target size. At the
`a_50` stage, all-tree cofinality and presentation independence remained.
`a_51` closes all-tree cofinality on fixed rays using finite twisted-field
bios and odd Vandermonde moments. The remaining dimension gate is now only
H7-FMD-GLOB: arbitrary-presentation and principal-divisor invariance.
`a_52` attempted arbitrary finite presentation by uniformizing intrinsic
norms, and `a_53` standardized Picard classes. `a_57` retracts their global
target: a retained characteristic eventually equals an allowed denominator.
Only the per-block/fixed-ray systems and the principal-invariant real-degree
**code coefficient** survive. `a_54` then shows that the unfiltered moment algebra
saturates the whole finite product by Lagrange interpolation, so its raw
cardinality cannot be the desired RR dimension. `a_55` strengthens this:
genuine bounded cross-contractions already surject onto a complete moment
block in linear bidegree, and their entropy exceeds the code coefficient by
a positive quadratic amount. Thus the existing `h_FM` sharp comparison is
false. H7-SEL-RR/EXACT must construct a different canonical measured object,
exclude the bounded interpolation family, and then prove multiplicativity,
sheaf exactness and the intersection identity.
For the quotient-based route, `a_56` proves that multiplicativity permits
only coordinate projections of each field-product block. The exact finite
gate is H7-SEL-MOM: the minimum coordinate hitting number `kappa` must satisfy
`kappa log p-log #I=o(t^2)`. Even if this asymptotic holds, compatible
cofinal choices and sheaf/intersection exactness still have to be proved.
`a_57` then finds a prior global obstruction: a finite-field coordinate
retained by the dyadic system eventually meets its own characteristic as an
allowed denominator. Hence `a_52` does not globalize the full effective cone
and the global `h_FM` of `a_53` is undefined. Per-height blocks, fixed-support
rays and the continuous code coefficient survive. H7-DEN-TRANS is the exact
new transition gate.
`a_58` further shows that this gate cannot be filled by an ordinary common
unital apex, since Bezout forces it to zero, nor by derived base change,
since `F_p tensor^L_Z F_q=0` for distinct primes. A Witt lift reduces mod
`p` only before `p` is inverted. Thus any surviving transition must abandon
transport by unital finite-ring maps and supply a new dimension formalism.
Independently, `a_59` closes the polarization branch of structured G-3 as
RH-equivalent without assuming additivity: two image vectors whose full Gram
form dominates a positive source plane contradict the Lorentzian index.
Thus only the effectivity-only branch G3-EFF survives.
`a_60` then proves that G3-EFF is RH-equivalent too: `D^o` has no strictly
effective classes, while a4-weak property (E) makes one sign of every
positive-square target effective. Under RH the spatial ray `(1,-1)` supplies
the converse map. Hence G-3 is now fully delimited.
`a_66` corrects the fraction-sheaf/type boundary: the unit torsors
`T_n=p_1^*T(tensor_p L_p^v_p(n))` exist and are faithfully monoidal without
H7-PRIME-REG. That condition is needed to promote them to completed
Section-11 lattices. It does **not** by itself yield Cartier/conormal modules:
the previous short-exact and `Tor` argument mixed operation sets with Haran's
abelian modules and is retracted. A typed Cartier comparison and the
principal ordinary-diagonal contact are supplied by `a_67`; a global
cotangent conormal is constructed by `a_68`, which reduces its derived
diagonal comparison to H7-LCI-DELTA. `a_69` then uses the projection/diagonal
retraction to split the desired `F_p[1]` contact canonically; LCI is only the
vanishing of the complementary excess. `a_70` promotes the torsor law to
literal composition in the category of Picard-decorated diagonal spans and
makes the contact a monoidal shadow. Only an undecorated Chow-type cycle lift
remains open at that point.
`a_64` rewrites H7-PRIME-REG as the exact tree statement
`pF~pG => F~G` for Haran's cancellation congruence in every arity and chart.
Jointly faithful finite twisted-field evaluations in auxiliary
characteristics would prove it (H7-RF-ALL); `a_51` supplies that faithfulness
only on the balanced code, not on the full tree presentation.
`a_71` uses the projection/diagonal retraction without treating operation
sets as abelian modules.  On every compatible chart, cancellation on the
curve forces a putative collision `pF=pG` into a single fold fiber; it is
therefore enough that the auxiliary evaluations be jointly faithful within
each fiber (H7-RF-FOLD).  Central localization preserves prime regularity.
The source gives tree representatives and relations but no unique confluent
normal form, so H7-RF-FOLD/H7-NF remains the exact open core.
`a_72` then retains the full finite bio, rather than its unary moment shadow,
and proves H7-RF-FOLD for the exponential arbitrary-arity block fibers of
`a_21` and their one-output scalarizations from `a_22`.  A cubic twist
distinguishes the two primitive additions by the values `2` and `8`, while
an auxiliary characteristic different from the tested prime permits
cancellation.  The remaining core is H7-RF-NEST for alternating nested trees
and cut-commutativity.
`a_73` extends the same cubic target to the complete depth-two read-once
family.  For each partition of the leaves, its Boolean pair table records
`8` exactly on same-block pairs (or on different-block pairs for the opposite
root color), recovering the partition.  Cross-color collisions reduce only
to deletion of unary vertices.  Hence any prime-torsion obstruction must now
involve depth at least three, repeated variables, contraction or a genuine
cut-commutativity ambiguity (H7-RF-DEEP).
`a_74` removes the depth bound.  In the real homogeneous bio, a color-`1`
root is recovered from the connected components of the mixed-Hessian graph
of `F`, while a color-`2` root is recovered from that of `F^(1/u)`; the
other graph is connected.  Restricting complementary variables to zero
recurses through the tree.  Therefore all reduced unsigned read-once trees
are prime-regular.  Any remaining collision must use signs, repeated
variables/contractions, two-sided graph data or cut-commutativity
(H7-RF-CUT).
`a_75` recovers each leaf sign by evaluating the represented function on the
corresponding unit vector.  On the orthant `x_i=epsilon_i y_i`, the signed
tree becomes precisely the positive tree of `a_74`, and diagonal sign changes
preserve Hessian support.  Hence signs also cannot cause prime torsion.  The
remaining gate H7-RF-BICUT concerns repeated/contracted leaves and genuinely
two-sided cut data.
`a_76` corrects the source audit: Section 13.2 does prove unique reductions
for each individual positive oriented tree.  This does not settle the
bilateral quotient.  On that presentation prime regularity is exactly the
colon-congruence identity `(E_cancel:p)=E_cancel`; neither the source nor the
read-once reconstruction proves it for repeated/contraction/cut data.
`a_77` removes the independent cut ambiguity.  Cuts of a fixed expanded
directed network are order ideals in its reachability poset, whose Hasse
graph is connected; adjacent cuts are Haran's consistent-commutativity move.
Cancellation in one fixed signed parallel bundle has the unique integer
normal form `#plus-#minus` and is prime-pure.  The remaining gate is therefore
H7-CORE-CONFLUENCE for overlaps where cancellation creates a unary/empty
branch and subsequent pruning or contraction changes the network core.
`a_78` proves that the two individual tree reductions are jointly confluent
and closes every isolated visible topology-changing site.  `a_79` classifies
the critical pairs and proves confluence only for the fixed-incidence local
rewrite.  `a_81` supplies the decisive scope correction: a binary
other-ruling context sends `x_0` to a `K2,2` grid with no visible local redex,
yet equivalence-ideal closure makes it zero.  Hence the earlier full-core
claim in `a_79` and base odd-prime claim in `a_80` are retracted.  The exact
remaining problem is the full macro-context relation system
H7-MACRO-CONTEXT-NF/SAT (equivalently a complete presentation and controlled
Smith factors), with boundary transport still separate.
`a_82` closes the full separable rectangular family: Cartesian corolla
contexts and vertex identifications give graph-incidence matrices with only
unit Smith factors.  `a_83` identifies the first exact danger from
nonseparable aggregation: cycle Laplacians have cokernel `Z plus Z/n`, so
even bipartite `C_6` carries an odd Smith factor unless individual fiber rows
are retained.  This isolates H7-FIBER-RETENTION.  Independently, `a_84`
proves that tameness plus scalar prime-regularity implies prime-regularity in
all arities; neither tameness of the plane nor scalar macro saturation is
currently established.
`a_85` uses Haran's general generator-path formula to close the set-theoretic
macro presentation: every elementary edge is one sandwich
`c o (x_epsilon plus id_V) o d`, and cancellation classes are connected
components of this graph.  Prime saturation is exactly injectivity of the
component map induced by `F -> pF`.  A structured sufficient proof splits
into H7-p-CONVEX (paths between divisible endpoints stay divisible) and
H7-p-DIVPATH (such paths divide after canceling `p`).  Neither is yet known
for the full macro graph.
`a_86` replaces the first path quantifier by an exact attachment test:
H7-p-CONVEX holds if and only if every connected component of nondivisible
macro vertices touches at most one component of the divisible induced graph.
Thus the first possible counterexample has a precise shape: one nondivisible
component with two gates to distinct divisible components.  The required
H7-p-ONE-BOUNDARY statement and H7-p-DIVPATH remain open for the plane.
`a_87` gives a second, prime-independent route.  Haran's first addition makes
the scalar plane an ordinary commutative ring, and the real homogeneous-bio
models give a product map to characteristic zero.  If this map is faithful
(H7-REAL-RES), scalar multiplication by every prime is injective at once;
H7-TAME-PLANE then promotes the result to every arity by `a_84`.  Faithfulness
and tameness are not yet proved, but the scalar saturation gate is now one
residual-embedding question rather than a separate colon calculation per prime.
`a_88` identifies the precise limitation of those existing targets.  A unary
regular bio duplicates the input at every leaf, so its two involutive
coordinates retain the signed left and right tree marginals but forget the
leaf-pairing correlation `sigma` inside equal-sign fibers.  Three leaves
already admit nonisomorphic incidence cores with identical marginals.  This
does not prove distinct quotient classes, but it makes H7-MARGINAL-COMPLETE
(or a new correlation-sensitive characteristic-zero target) an explicit
additional requirement of the residual route.
Corrected `a_89` resolves the full relation lattice on every fixed two-level
bilateral grid.  The first draft's row/column-margin formulation was false:
the contextual-zero `K2,2` of `a_81` has nonzero row margins.  Including both
ruling cancellations gives
`U_0 tensor Z^c + Z^r tensor V_0`; its quotient is the single total-mass
copy of `Z`, hence saturated at every prime.  The three-leaf ambiguity of
`a_88` vanishes, but the remaining theorem concerns cut-changing nested
contexts (H7-NESTED-CONTEXT-SAT), not compatibility of naive margins.
`a_90` closes the cut-changing theorem whenever the nested blocks are
laminar and no contraction reuses a strand in incomparable blocks.  Unique
fiber transport makes the gluing matrix a direct sum of oriented incidence
matrices, all of whose nonzero Smith factors are one.  Thus arbitrary-depth
bilateral laminar contexts are prime-saturated.  The first unresolved shape
must aggregate fibers through nonlaminar overlap or contraction/reuse
(H7-NONLAMINAR-FIBER).
`a_91` closes one more part of that residual shape.  A single binary mixing
interface is a regular bipartite multigraph and decomposes into perfect
matchings by Hall, so it admits copywise division.  Three simultaneous
overlaps are different: the even-parity `2x2x2` hypergraph is 2-regular but
has no perfect matching.  This is only a candidate ancestry shape, not a
Haran torsion class; its typed realization, contextual closure and
nonzeroness are the explicit H7-TERNARY-OVERLAP gates.
`a_92` closes only the typing part: `E=F_2^2` with maps `i`, `j`, `i+j`
has all pair projections bijective and joint image the four even triples,
and arbitrary finite-set maps are legitimate in Haran's fiberwise formulas.
`a_93` then finds the exact lattice signal: the six-vertex/four-edge incidence
matrix has Smith factors `1,1,1,2`, with a concrete mod-two functional; one
odd edge kills the factor two.  This is not yet a Haran torsion class because
ancestry incidence is not the complete macro relation matrix.  The remaining
tests are H7-PARITY-ENDPOINTS, H7-PARITY-PRESERVE and H7-PARITY-SEPARATE.
`a_94` verifies that the factor two is not merely caused by using nonzero-fold
incidence columns: the three fold-zero even differences have Smith
`1,1,2` and explicit witness `w=(-1,1;-1,1;-1,1)`.  But `a_95` then closes
the bare candidate negatively.  Each undecorated binary cut admits an
internal child swap under (10.14); adding any one swap column changes the
Smith factors to `1,1,1` and `omega` does not descend.  Only an intrinsically
rigidified parity diagram, or another nonlaminar shape, can survive.
`a_96` shows that same-fold rigidification is typable: a ternary color-1
corolla and a color-1 tree with a nested color-2 binary child have equal fold
and are intrinsically nonisomorphic.  However `a_97` rules out this whole
positive scalar-visible strategy.  If bit weights have ratios `r_i`, the
three even moves force `r_2r_3=r_1r_3=r_1r_2=1`; positive real weights give
all `r_i=1`.  The explicit `a_96` weights give `27` versus `75`, so no even
macro path exists.  A parity route would now require
H7-SCALAR-INVISIBLE-RIGID, not merely same-fold decorations.
`a_98` shows scalar invisibility alone is also insufficient.  The two
labelled pair partitions `12|34` and `13|24` have equal all-ones values for
every real parameter and equal fold, but Boolean pair probes distinguish
them.  Functorial block extraction therefore forbids every required even
move.  Any surviving parity construction must satisfy the stronger
H7-NONEXTRACTABLE-RIGID condition and hence use genuinely entangled
bilateral/repeated contraction data outside `a72`--`a75`.
`a_99` replaces that informal gate by an exhaustive dichotomy.  Distinct
bits invisible to every ambient scalar sandwich are a direct witness that
H7-TAME-PLANE fails; otherwise a separating sandwich exists and the outer
parity embedding must fail H7-CONTEXT-RETRACT.  `a_100` proves that arbitrary
finite-set maps and noninjective fiber contractions have coordinate
retractions using sections, zero insertions and units.  Hence any genuine
failure of context retraction must come from nonsplit outer operation
coefficients `c,d`, isolated as H7-COEFF-NORETRACT—not from the XOR ancestry
or set-theoretic reuse alone.
`a_101` closes the whole split-coefficient subcase.  If the left outer label
has a typed left inverse and the right label a typed right inverse, zero
extension of any scalar probes gives an exact sandwich retraction.  In an
ordinary matrix residual this is precisely the unit-ideal (unimodular)
criterion.  Nonsplitness by itself does not create a collision (`a -> 2a`
is injective over `Z`), so H7-COEFF-NORETRACT is sharpened to H7-COEFF-ANN:
one must construct an ambiently separable pair actually annihilated by a
genuinely nonsplit two-sided context, or prove that none exists in the
arithmetic plane.
`a_102` gives the corresponding scalar target without choosing a parity
model.  The first-ruling scalar ring splits additively as
`R=Z direct-sum K` under the fold, and scalar cancellation for every prime
is equivalent to torsion-freeness of `K`, equivalently ordinary `Z`-flatness.
The split fold is not enough: `Z -> Z x F_p -> Z` is a split ring extension
whose augmentation kernel has `p`-torsion.  Thus the exact simultaneous
scalar gate is H7-AUG-FLAT; with H7-TAME-PLANE it implies full H7-PRIME-REG.
`a_103` then sharpens the second hypothesis.  In any commutative Haran
`F`-ring, the centre `a o b` and the Cartesian grid
`(sum_Y b)o(sum_I a)` have identical values under every scalar sandwich.
If they differ, they are an explicit nontameness pair.  For the two plane
generators this gives H7-XDEF-12; neither Haran's non-diagonal theorem nor
the contextual-zero K2,2 calculation decides equality after signed
cancellation.
`a_104` decides that equality: Haran's commutative infinitesimal extension
`F(Z) Pi N` receives the full signed plane and sends centre minus grid to a
nonzero element with nine independent primitive-direction coordinates.
Hence H7-XDEF-12 survives and H7-TAME-PLANE is false.  The scalar gate
H7-AUG-FLAT remains meaningful, but it cannot be promoted by tameness; the
live all-arity route is the direct componentwise p-CONVEX/p-DIVPATH analysis.
`a_105` closes the first infinitesimal layer of that direct analysis.  The
two ordered maps to `F(Z) Pi N` are prime-regular in every arity because
Haran's module `N` is free abelian on primitive direction pairs.  Therefore
every possible prime collision lies in the common equality kernel of those
two jets; the `a_104` nontameness defect itself cannot be prime torsion.
`a_106` replaces `N` by the rationalized universal differential and
`a_107` computes its integral scalar group: two free prime copies plus one
`Z/2` anomaly.  `a_108` integrates that anomaly to the actual nonzero scalar
`kappa=(1,-1)_1 o (1,1)_2^t`; a wire swap gives `2kappa=0`.  Thus
H7-AUG-FLAT and H7-PRIME-REG are false at `p=2`, and the direct
p-CONVEX/p-DIVPATH conjunction must fail there.  The live G-7 question is
no longer how to prove regularity, but how to replace the completed
regular-denominator lattice while preserving the literal `Lambda(2)`
contact and all divisor/section/gauge axioms.
`a_41` computes the literal Witt graph/diagonal fixed ring at every
prime-power stage: it is exactly `Z`, with no torsion. Thus ordinary
intersection cannot have degree `log p`; H7-WLEF-red must remove the common
`F_0` horizontal component by a derived/excess construction and recover
`Lambda` from the remaining determinant.
`a_42` shows that the standard reduced cone still cannot work:
`1-F_p` is integrally invertible after removing `phi_1`, with determinant
one. The correct normal determinant is forced to be the primitive
cyclotomic factor `Norm(1-zeta_n)=Phi_n(1)`; geometrizing it is H7-WLEF-cyc.
`a_43` geometrizes this determinant for prime labels: the rank-two Witt
stage is exactly `Z x_{F_p} Z`, and its `F_0`/trace branches intersect in
`Spec F_p` with degree `log p`. This matches the literal Haran incidence
`Delta cap V_p` from `a_17`. A compatible transport and extension to
prime-power/operator composition is the remaining local gate H7-WNODE.
`a_44` extends the local calculation to every prime power: consecutive Witt
characters meet with thickness `Z/p^k`, and the new associated-graded layer
is `p^{k-1}Z/p^k ~= F_p`, hence has degree `Lambda(p^k)`. Functorial
transport under `V_{p^k}=V_p^k` and cancellation for multi-prime labels are
the remaining clauses H7-WNODE-COMP.
`a_45` closes those arithmetic composition/cancellation clauses in finite
modules: `P_n=tensor_{p^k||n}F_p`, so distinct-prime factors annihilate and
`log #P_n=Lambda(n)` for every `n`, while
`P_m tensor P_n ~= P_mn`. The remaining I7 step is geometric transport
H7-WCONTACT to actual correspondence/diagonal incidence modules on Haran's
square. `a_46` closes that transport at the incidence-sheaf level:
`M_n=tensor_{p|n}(i_p)_*F_p` is supported on the literal square and satisfies
both `M_m tensor M_n=M_mn` and `log #Gamma(Y,M_n)=Lambda(n)`. What remains is
the stronger H7-CYCLE-LIFT: construct distinct correspondence cycles
`Gamma_n`, their composition, and `LDelta^*Gamma_n=M_n`.
`a_47` proves that the shortcut `Gamma_n=M_n` cannot do this faithfully:
all powers of one prime have the same contact shadow, while every
multi-prime label has zero shadow. The missing cycle must retain precisely
the data that diagonal pullback is supposed to erase.
`a_48` also rules out taking the prime rulings themselves as generators under
ordinary span composition: for distinct primes the product either vanishes or
retains the oriented left endpoint and is noncommutative. The exact integer
composition law exists for Connes--Consani's arithmetic-site correspondences
`Psi(n)`, but in a different topos with no constructed bridge to this square.
Thus H7-CYCLE-LIFT is sharpened to H7-DYNAMIC-LIFT: a genuinely new
transverse/dynamic correspondence datum is required.
Structured G-3, G-7 and the full effectivity dictionary remain open; G-1 is settled
in `114_a_11`, while G-2 and the R8 basepoint predicate are settled in
`114_a_08`. **a4-strong and row (a) as a
whole remain open.** Nothing here proves anything about RH.
