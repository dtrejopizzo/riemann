# 108.21 — Stage 1, final status: the constant term is a genuine, terminal
# obstruction, proved by one unifying mechanism

## 0. Terminal verdict

\[
 \boxed{\text{Stage 1 does not close. Outcome (ii): the obstruction is
 genuine and terminal. The }a\text{-dependent part is closed (108_06,
 108_07, 108_11); }\sum_pC_p\text{'s presence in }\mathfrak
 T_S(f_a\star\tilde g)\text{ is forced, not repairable, by a single proved
 mechanism (Theorem 1.1 below), of which every one of six independently
 attempted repairs is now shown to be an instance.}}
\]

This note closes the "settle the constant term" mandate under outcome (ii)
of the mission: not by exhausting patience across an open-ended list of
repairs, but by proving one theorem general enough to explain why routes
A–E (108_13–108_16, 108_17–108_19) all fail, and precise enough to state
exactly what a successful disposal would have had to supply.

No zero of $\xi$ is used anywhere in this note or anywhere in Phase 108.
`ROW_A_STATUS` remains `partial`. Nothing here bears on RH.

## 1. The unifying theorem

> ### Theorem 1.1 (the identity obstruction — terminal form)
> Let $v$ be a place and let $\Delta_v(u):=1/|1-u|_v$ be the finite- or
> archimedean-place trace-formula kernel appearing in
> $\mathfrak T_S(h)=\sum_{v\in S}\int'_{\mathbb Q_v^\times}h(u^{-1})\Delta_v(u)\,d^\times u$
> (107_239 (2.1)). For $v=p$ finite, write $\varphi(u):=h(u^{-1})$ and let
> $\varphi_0$ be its value on the shell $|u|_p=1$ (assumed locally
> constant there). Then:
>
> **(a)** $W_p(\varphi)$ is finite under Tate's principal value **iff**
> $\varphi_0=0$ (108_17 Theorem 2.2), and when $\varphi_0\ne0$ the
> divergence rate is exactly $\varphi_0$ per unit of the regularization
> cutoff (108_17 Theorem 2.2, second clause) — not merely an unevaluated
> limit, but a literal, unbounded, $\varphi_0$-proportional growth.
>
> **(b)** Every element of the graded family $\mathcal G=\{f_a\}$ has
> $\varphi_0=f_a(1)=1$ for **every** $a\in\mathbb C$ for which $f_a$ is
> defined (108_17 Theorem 3.1), because $u\mapsto|u|_p^{a}$ is a
> quasi-character and every quasi-character sends the group identity to
> $1$. This is not a property of a particular $a$: it is a property of
> $\mathcal G$ being a family of characters at all.
>
> **(c)** Any construction that avoids the divergence by discarding the
> kernel $\Delta_v$ (replacing it with a non-singular kernel, e.g. Tate's
> $|u|_p^{s}$ alone, 108_18 §2) is finite for every input, including at
> $\varphi_0\ne0$ — but is thereby a *different* object, provably not
> satisfying $\mathfrak T_S(h)=N(h)$'s founding identity, since that
> identity's validity was never claimed, or claimable, beyond compactly
> supported $h$ (108_06 §1, 108_18 Theorem 3.1–3.2). Removing $\Delta_v$
> removes the divergence and the trace-formula content in the same stroke.
>
> **(d)** Any attempt to make the constant's contribution invisible without
> resolving (a)–(c) — by absorbing it into a counterterm (Route A, 108_13),
> regularizing it via $\zeta$ (Route B, 108_14), restricting the test class
> by finitely many linear conditions (Route C, 108_15), or asking whether
> its pairing lies in the radical of the global form (Route E, 108_19) —
> fails, and in each case the failure is traceable to (a)–(b): the
> counterterm's scale (linear in a cutoff $T$) cannot match a divergence
> whose *rate itself* is fixed at $\varphi_0=1$ shell-by-shell and summed
> over primes (108_13); the regulator leaves the elementary $\varphi_0=1$
> obstruction $B_0=\sum_p\frac{p-2}{p-1}$ untouched (108_14); no
> finite-codimension linear condition on $g$ can force $c_g\equiv0$ on an
> open interval, by entire-function rigidity (108_15, and 108_19's direct
> reduction to the same rigidity for the radical question).

**Proof.** (a) is 108_17 Theorem 2.2. (b) is 108_17 Theorem 3.1. (c) is
108_18 Theorem 3.1–3.2, using 108_06 §1's own statement of $\mathfrak
T_S(h)=N(h)$'s domain and 108_05 Proposition 2.1's proof that $f_a$ has no
Mellin transform (hence lies outside the domain on which $\mathfrak
T_S(h)=N(h)$ could ever have been asserted to hold with $h=f_a$). (d) is
108_13 Theorem 3.1, 108_14 Theorem 2.2–2.4, 108_15 Theorem 3.1, and 108_19
Theorem 2.2 respectively, each cited for its own proved conclusion, with the
common thread ((a)–(b)) made explicit for the first time in this note.
$\square$

## 2. Why this is stronger than 108_16 Theorem 5.1

108_16 Theorem 5.1 proved that three specific, concretely attempted repairs
(A, B, C) fail, each for its own reason, and observed (without a unifying
proof beyond "all trace to one underlying fact") that this looked
structural. Theorem 1.1 above supplies the missing unification, in a form
sharp enough to also cover three further repairs attempted only in this
note's own investigation (G, D, E — 108_17–108_19), and sharp enough to be
**predictive**: clause (a)'s criterion ($\varphi_0=0$) determines, for any
future proposed repair, in one line, whether it can possibly work — a
repair works only if it can be phrased as supplying a test-function argument
to $\Delta_v$ that vanishes at $u=1$, and clause (b) shows the graded family
can never supply one.

## 3. What a disposal would have had to supply (stated precisely, per the
   mission's closing instruction)

A successful outcome-(i) disposal of $\sum_pC_p$ in $\mathfrak
T_S(f_a\star\tilde g)$ would have had to supply **one** of the following,
and Theorem 1.1 shows why none is available within this program's
definitions:

1. **A test-function argument to $\mathfrak T_S$'s kernel $\Delta_v$ that
   vanishes at the group identity $u=1$ of every place in $S$, while still
   representing the graded family's grading.** Impossible: every element of
   $\mathcal G$ is (built from) a quasi-character, and $\chi(1)=1$ is forced
   by the group-homomorphism property alone, not by any freedom left
   unexploited (Theorem 1.1(b)).
2. **A redefinition of the arithmetic-side extension of the corner trace to
   $\mathcal G$ that does not route through $\Delta_v=1/|1-u|_v$, while
   still satisfying $\mathfrak T_S(h)=N(h)$'s intended content on the
   relevant class.** The natural candidate (Tate's local zeta integral,
   Route D) is available and finite, but demonstrably fails the second
   requirement: it computes ordinary local Euler factors / $\zeta(s)$
   itself, not a trace-formula object tied to $N(h)$ (108_18 Theorem 3.1).
   No other candidate redefinition is proposed or known to this program.
3. **A proof that the constant's rank-one contribution pairs to zero
   against every admissible test datum**, making it invisible regardless of
   its own value. Refuted by an explicit, independently reconstructed
   nonzero witness (108_15 §6, 108_19 §2), itself forced nonzero by the same
   entire-function rigidity that blocks item 1's escape route by
   finite-codimension restriction.

None of the three is available. This is what "the obstruction is genuine
and terminal" means here, made as concrete as the program's own definitions
allow.

## 4. Updated status table

| component | status |
|---|---|
| finite local terms $W_p(f_a)$ | closed (108_06) |
| archimedean local term | closed, $\pi\cot(\pi a/2)$ (108_07) |
| global, $a$-dependent part, distributional | **closed** (108_11) |
| global, the constant $\sum_pC_p$ inside $\mathfrak T_S(f_a\star\tilde g)$ | **open, and now proved terminal** (Theorem 1.1, this note) |
| Route A — 107_239 counterterm | fails (108_13) |
| Route B — $\zeta$-regularization | fails as an identification (108_14) |
| Route C — primitive restriction | fails except vacuously (108_15) |
| Route G — PV re-derivation / normalization artifact | fails for $\mathcal G$, exact criterion identified (108_17) |
| Route D — twist slot (Tate zeta integral) | finite but a different, non-rescuing object (108_18) |
| Route E — radical membership | excluded by explicit witness (108_19) |
| Stage 1 overall | **not closed; terminal (outcome (ii))** |

## 5. Scope — final, unsparing accounting

**Proved (this note, synthesizing 108_13–108_19):**

* Theorem 1.1, the unifying identity-obstruction mechanism, in the precise
  four-clause form above;
* §3's exact statement of the three logically possible disposal routes and
  the specific already-proved fact excluding each.

**Proved in the cited notes (not re-proved here, only assembled):**

* 108_17 Theorems 1.2, 2.1–2.2, 3.1: the exact finiteness criterion
  $\varphi_0=0$ for the PV local term, derived from scratch, and its
  permanent violation on $\mathcal G$;
* 108_18 Theorems 2.2, 3.1–3.2: Tate's local zeta integral is finite with no
  leftover constant for any test function, but is a provably different
  construction from $\mathfrak T_S$;
* 108_19 Theorem 2.2: the constant's rank-one functional is nonzero on an
  explicit witness, hence not in the radical of the pairing;
* 108_13 Theorem 3.1, 108_14 Theorems 2.2–2.4, 108_15 Theorem 3.1 (cited,
  not re-derived): routes A, B, C fail.

**Verified numerically only, clearly labeled in each source file:** all the
closed-form-vs-quadrature and closed-form-vs-direct-summation checks listed
in 108_17–108_19's own Verifier sections, plus the pre-existing checks of
108_11–108_16.

**Read from source / classical, not proved anywhere in this phase:** Tate's
local zeta integral and its meromorphic continuation (Tate's thesis, 1950,
used in 108_18 without re-derivation beyond its elementary geometric-series
evaluation); Chebyshev's theorem (108_12); the Euler–Maclaurin continuation
of $\zeta$ (108_14).

**Not established, and explicitly still open — stated plainly, not
minimized:**

1. **The value of $\sum_pC_p$ under any regularization whatsoever.** Six
   concrete repair attempts (A, B, C, G, D, E) all fail, and Theorem 1.1
   explains why each of the first five and the sixth trace to one
   mechanism — but this is not, and cannot be, a proof that *every
   conceivable* repair fails; it is a proof that every repair of the three
   *types* enumerated in §3 fails, and an argument (not a theorem) that
   these three types exhaust the natural candidates this program's own
   definitions make available.
2. **Whether $\mathfrak T_S(f_a\star\tilde g)$, as literally defined by
   substituting $f_a$ into 107_239 (2.1), was ever the right object for
   Stage 1's mandate.** 108_05 Proposition 2.1 and 108_18 §1 show $f_a$ sits
   outside the domain where $\mathfrak T_S(h)=N(h)$ is asserted to hold; this
   note documents that fact and its consequences (Theorem 1.1(c)) but does
   not resolve, and this program is not positioned to resolve without
   returning to 107_239's original source material, whether Stage 1 should
   instead have been posed with a different starting formula.
3. Complex $a$ outside the results explicitly extended here: Theorem 1.1(b)
   holds for all $a\in\mathbb C$ (an improvement over 108_08's real-axis
   confinement), but the singular-set analysis of 108_08 and 108_11 for the
   $a$-dependent part remains, as those notes state, confined to the real
   segment for the global-sum question.
4. The comparison with the zero side of the explicit formula: untouched,
   and forbidden as a *definition* by 108_00 §2 in any case.
5. Whether the distributional object 108_11 Theorem 3.1 constructs (the
   $a$-dependent part alone, without the constant) is "the right one" for
   the rest of the program (107_239–107_241): not established anywhere in
   Phase 108, including here.

`ROW_A_STATUS` remains `partial`. This note promotes no status, resolves no
row, and bears on RH nowhere.

## 6. Verifier

`108_21_stage_1_final.py` re-runs, as subprocesses, the verifiers of 108_11
through 108_19 (nine scripts) and confirms each exits $0$, printing a
consolidated pass/fail table; it then independently re-checks, standalone,
the two headline facts Theorem 1.1 depends on most directly: the exact
finiteness criterion $\varphi_0=0$ (108_17's dichotomy, re-derived here in a
compressed form) and $f_a(1)=1$ for a fresh grid of complex $a$ not used in
108_17's own verifier, as a final independent consistency pass.
