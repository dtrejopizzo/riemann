# 115.11 — Three refutations: the Künneth reading, the radix identification, and the duality repair

Points 0, 1 and 2 of the attack order.  One verification passes; three claimed
routes die, each by proof rather than by failure to find an argument.

Scripts: `scripts/115_11_p0_fivebump_crosscheck.py` (+`.out`),
`scripts/115_11_p1_radix_sign_test.py` (+`.out`).

## 0. The window cross-check is now generic — PASSES

`115_08` §4.1 used four bumps; with three constraints the null space was
one-dimensional and the solution came out **odd** in \(t\), for which the two
conditions at \(\pm i/2\) collapse to one.  The check was therefore not
generic.

Redone with five bumps at \(\mu\in\{-0.24,-0.12,0,0.12,0.24\}\), \(w=0.08\),
null space two-dimensional, selecting the least odd element:

\[
 c=(-1,\;3.00360108,\;-3.00360108,\;1,\;0),
\]

oddness measure \(2.0\) (zero would mean perfectly odd), constraints satisfied
to \(3\times10^{-31}\).  Support \(\subset[-0.32,0.32]\subset(-\log\sqrt2,\log\sqrt2)\),
so \(K=0\) by `115_08` Proposition 5.

\(\Psi(\tau)\) is now evaluated in closed form rather than by nested
quadrature.  Expanding \(\cos^8\),

\[
 \Psi(\tau)=\frac1{128}\sum_{m=0}^{4}a_m(-1)^{m+1}
 \frac{2\tau\sin(\tau w)}{(m\pi/w)^2-\tau^2},
 \qquad a=(35,56,28,8,1),
\]

with removable singularities at \(\tau=m\pi/w\).

| quantity | value |
|---|---|
| \(-G_\infty(f,f)\) | \(0.988062653184160993\) |
| \(\sum_\gamma\|\widehat{\mathcal G}(\gamma)\|^2\), 250 zeros, \(\gamma\le470.8\) | \(0.988062654959792408\) |
| relative difference | \(1.797\times10^{-9}\) |

Converged: stable in the 15th digit from 150 zeros on, tail
\(|\widehat H(470.8)|=7.4\times10^{-28}\).  Four orders of magnitude better than
the four-bump run, the improvement coming entirely from the closed form.

**Proposition 0 and the sign dictionary of `115_08` §0 are confirmed on a
generic (non-odd) element of \(\mathcal T^0\).**

## 1. The radix-sign test — REFUTES the shell identification

`115_09` §3 conjectured that the graded pieces of the semi-local cutoff
(Proposition 3 there) correspond to the digit places of row (a)'s negabinary
code, and named the radix sign as the test most likely to kill it.

Row (a)'s code is radix \(-2\): place value \((-2)^j=(-1)^j2^j\), so the sign
**alternates with the digit index**.  The shell grading by \(v_p\) carries no
alternation, so the conjecture survives only if the alternation is produced by
the one thing that is not diagonal in that grading — the Fourier transform on
\(\mathbb Q_2\).

Compute the coupling.  Normalise Haar measure so \(\mathbb Z_2\) has measure 1;
write \(B_v=2^v\mathbb Z_2\) (measure \(2^{-v}\)) and
\(e_v=\mathbf 1_{2^v\mathbb Z_2^\times}=\mathbf 1_{B_v}-\mathbf 1_{B_{v+1}}\)
(measure \(2^{-v-1}\)).  From
\(\widehat{\mathbf 1_{B_v}}=2^{-v}\mathbf 1_{B_{-v}}\),

\[
 \widehat{e_v}=2^{-v}\mathbf 1_{B_{-v}}-2^{-v-1}\mathbf 1_{B_{-v-1}},
\]

whose value on the shell of valuation \(u\) is \(2^{-v-1}\) if \(u\ge-v\),
\(-2^{-v-1}\) if \(u=-v-1\), and \(0\) if \(u<-v-1\).  Hence
\(\langle\widehat{e_v},e_u\rangle=2^{-u-1}\times\) that value, giving the sign
pattern

```
   v\u   -6  -5  -4  -3  -2  -1   0   1   2   3   4   5   6
     -2    .   .   .   .   .   .   .   -   +   +   +   +   +
     -1    .   .   .   .   .   .   -   +   +   +   +   +   +
      0    .   .   .   .   .   -   +   +   +   +   +   +   +
      1    .   .   .   .   -   +   +   +   +   +   +   +   +
      2    .   .   .   -   +   +   +   +   +   +   +   +   +
```

> **Proposition 1.**  The Fourier coupling between shells has exactly one
> negative band, the antidiagonal \(u+v=-1\), with \(+\) strictly above it and
> \(0\) strictly below.

That is a **single sign flip at a fixed offset**, not a sign alternating with
the digit index.  Radix \(-2\) requires a flip at every step.  The two patterns
do not agree.

> **The conjecture of `115_09` §3 is REFUTED.  Row (a)'s negabinary code is not
> the finite factor of the semi-local Sonin cutoff.**

Consequence, by the decision point stated in `115_09` §5: rows (a)–(b) do not
connect to the semi-local construction, so hypothesis (H) and \(E_S\le0\) remain
Connes–Consani's open problem and are not advanced by anything in this
programme.  What remains ours is the direct route, \(A(f)\prec0\).

## 2. The duality repair is impossible — the theta route to the axioms closes

`115_10`/the preceding analysis exposed an inconsistency in §9.9: with
\(L^\vee=\mathcal L(-D,-E)\) (`prop:divisorlines`), the chain

\[
 h^\vee_t \overset{\text{`cor:thetaomega`(2)}}{=} h^0(L^\vee)=h^0(-D,-E)
 \overset{\text{`cor:thetaomega`(1)}}{=}h^2=0
\]

contradicts \(h^\vee_t=N_t\log\vartheta(\sigma^{-1})\ne0\).  The repair would be
a lattice functor that is simultaneously

* **(A) dual-compatible:** \(V(-D)=V(D)^{*}\);
* **(B) vanishing off the cone:** \(V(D)=\{0\}\) for \(D\) non-effective.

> **Proposition 2 (no repair).**  No lattice functor satisfies both (A) and
> (B), unless \(V\equiv\{0\}\).
>
> *Proof.*  Let \(D\) be effective of positive degree with \(V(D)\ne\{0\}\), of
> rank \(\rho>0\).  Then \(-D\) is not effective, so (B) gives
> \(\mathrm{rk}\,V(-D)=0\); while (A) gives \(V(-D)=V(D)^{*}\), of rank
> \(\rho>0\).  \(\square\)

There is no room to weaken (A): `thm:thetaRR` is proved by Poisson summation,
which requires the **full** dual lattice.  A truncated dual does not satisfy
Poisson and the Riemann–Roch identity fails with it.

**This fires the kill criterion set for point 2.**  The two options are forced
apart and neither is free:

| | \(h^0(-D)\) | axiom 1 | Serre / \(h^1\) |
|---|---|---|---|
| **A** dual-compatible | \(=h^\vee\ne0\) | **fails** — \(h^0>0\) off the effective cone | \(h^1=h^\vee\) derived |
| **B** code (what §9.9 does) | \(=0\) | holds | \(h^0(L^\vee)\ne h^\vee\); `cor:thetaomega`(2) invalid, \(h^1=h^\vee\) is a fit |

Nor is option A rescued by a threshold reading of axiom 1.  With the canonical
metric \(V(-D,-E)=V(D,E)^{*}\) has full rank \(N_t\), so

\[
 \widehat h^0(-D,-E)=(c-1)\,ab>0,\qquad c-1=1.129\times10^{-3},
\]

strictly positive off the effective cone.  The separation from the effective
side is one of scale, not of vanishing:
\(\log\vartheta(\sigma)/\log\vartheta(\sigma^{-1})=886.7\).  A threshold
\(\kappa\) separating them would have to satisfy \((c-1)ab<\kappa<c\,ab\) for
every \(D,E\), impossible as \(ab\to0\).

> **The theta-on-lattices route to the four axioms is closed.**  It cannot
> supply both effectivity and duality, and `thm:mixedsectionforcing` needs both.

## 3. What this leaves

Of the six items in the attack order: 0 passes, 1 and 2 are refuted, 4 and 5
are Connes–Consani's open problem and are now known not to be reachable through
rows (a)–(b), and 3 is reading that only serves 4–5.

**Item 6 is the only live line that is ours**: construct \(A(f)\prec0\) on
\(\mathcal T^0\) from a realization that is not single-place.  Current state:
by `eq:muDef`, \(d\mu=\frac1{2\pi}\sigma(\tau)|\widehat F(\tau)|^2d\tau\) with
\(\sigma\) the symbol of \(\mathcal Q\), whose archimedean part is \(-m_\infty\)
— negative on \(|\tau|<\tau^*\approx6.29\) and positive outside.  So the
**negative** part of \(\mu\) is supported on a bounded interval, and by Slepian
concentration against \(\log n\in[0,2T]\) the corresponding \(Q_-\) has
effective rank \(O(T)\) against ambient \(N\sim e^{2T}/2T\): \(Q(f)\) is
positive semidefinite modulo a rank-\(O(T)\) correction.  Whether that yields
\(A\prec0\) is unresolved, and the sign is the opposite of what was hoped.

## 4. Status

* Window cross-check, generic non-odd \(\mathcal T^0\) element: **PASSES**,
  \(1.80\times10^{-9}\).
* `115_09` §3 shell/negabinary identification: **REFUTED** (Proposition 1).
* Dual-compatible-and-vanishing lattice functor: **PROVED IMPOSSIBLE**
  (Proposition 2).
* Theta route to the four axioms: **CLOSED**.
* `cor:thetaomega`(2) and `rem:kunnethtension` in `main.tex`: **require
  correction**; not touched, per the standing instruction.
* Row (d): **OPEN**.
