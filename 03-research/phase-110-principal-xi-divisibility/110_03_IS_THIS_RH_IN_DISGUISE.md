# 110.03 — Is ξ-divisibility RH in disguise? The candor check

## 0. Answer

**No.** The obstruction found in Task 2 (Theorem 110.2.4: ξ-divisibility
meets the admissible test class only at $0$) is **unconditional** — its
proof uses only $\xi$'s *growth rate* along the real axis (Theorem 110.2.2,
from Stirling's asymptotic for $\Gamma$) and an elementary
support/exponential-type correspondence (Fact 110.2.A). Neither ingredient
references the location of a single zero of $\xi$, nor any positivity
statement classically equivalent to RH. §2 makes this precise with a
**counterfactual test**: replacing $\zeta(\sigma)$ in $\xi$'s defining
product by an arbitrary bounded, zero-free dummy factor leaves the growth
constant governing Theorem 110.2.4 numerically unchanged, while replacing
the $\Gamma$-factor by a bounded dummy destroys the obstruction entirely.
This isolates the source of the impossibility to $\Gamma$'s classical
growth, which has nothing to do with where $\zeta$'s zeros are.

But the verdict is **not simply "clean, go ahead."** Per the pre-registered
criteria of 110\_00 §2, the outcome is **(N2, vacuous)**, which is a
*stronger* closure than either "RH in disguise" or the earlier programme
failure mode "(N1) circular": within the admissible (compactly supported)
test class there is nothing — zero, not even a badly-defined or
circularly-defined candidate — for $\mathcal P$ to be. Not even the
circular move of *defining* $\mathcal P$ to be "the ξ-divisible things" is
available as a face-saving trick, because that set is $\{0\}$ there. §3
explains precisely what a genuine fix would need to look like, and why it
is not attempted here.

## 1. Applying the pre-registered criteria of 110\_00 §2

Recall the three possible outcomes fixed in advance, before any Task 1/2
computation:

* **Refutation of the "empty/circular" concern:** an explicit $\mathcal
  P_0\subseteq(\text{ADM})$, defined independently of ξ-divisibility, proved
  (not defined) to satisfy $\hat f=\xi\hat g$. **Did not occur.** Task 1
  shows the one concrete candidate available from the permitted source
  material (the graded family) fails for an even more basic reason (it is
  not admissible at all — Theorem 110.1.4); Task 2 shows *no* nonzero
  element of the admissible class can be ξ-divisible, period (Theorem
  110.2.4), so no such $\mathcal P_0$ can exist, regardless of which
  admissible candidate one tries next.
* **(N1) circular:** every attempt to name a nonzero $\mathcal P_0$ forces
  the defining condition to *be* ξ-divisibility itself, with no independent
  handle. **Does not apply as stated**, and for a stronger reason than
  "avoided": by Theorem 110.2.4 there is no nonzero admissible $\mathcal
  P_0$ to name in the first place, circularly or otherwise. (N1) presupposes
  a nonempty target that can only be reached by definitional fiat; here the
  target set is empty, so there is nothing to reach even by fiat.
* **(N2) vacuous:** proved from classical, unconditional facts about $\xi$
  (order and type — not zero locations) that $\{\hat f=\xi\hat g\}\cap
  (\text{ADM})=\{0\}$. **This is what occurred** (Theorem 110.2.4).
* **"RH in disguise":** the containment can only be secured by using the
  location of the zeros, or a positivity statement equivalent to RH.
  **Tested directly in §2 below and found not to hold.**

So the phase lands on (N2), a distinct and — per 110\_00 §2 — *stronger*
outcome than either of the two the prompt anticipates as endpoints. It is
recorded candidly, without being reclassified as either of the other two.

## 2. The counterfactual test: does the obstruction know about zeros?

### Proposition 110.3.1 (the growth obstruction survives replacing $\zeta$ by any bounded zero-free dummy)

Let $\zeta^\ast$ be *any* function on $[2,\infty)$ with $c_1\le|\zeta^\ast(\sigma)|\le c_2$
for fixed $0<c_1\le c_2<\infty$ (in particular: bounded, and — trivially,
since it never gets near $0$ — zero-free; it need not resemble $\zeta$ at
all beyond this). Define $\xi^\ast(\sigma):=\tfrac12\sigma(\sigma-1)\pi^{-\sigma/2}\Gamma(\sigma/2)\zeta^\ast(\sigma)$.
Then
$$\log|\xi^\ast(\sigma)|=\frac\sigma2\log\sigma-C\sigma+O(\log\sigma),\qquad
\text{the same }C=\tfrac{\log2+1+\log\pi}2\text{ as in Theorem 110.2.2}. \tag{2.1}$$
Consequently Theorem 110.2.4's proof goes through **verbatim** with $\xi^\ast$
in place of $\xi$: the admissible class still meets $\{\hat f=\xi^\ast\hat g\}$
only at $0$.

**Proof.** $\log|\zeta^\ast(\sigma)|$ is bounded (between $\log c_1$ and
$\log c_2$), hence $O(1)=O(\log\sigma)$, exactly the same order as the true
term $\log\zeta(\sigma)\to0$ used in Theorem 110.2.2's proof. The rest of
that proof (Stirling's asymptotic for $\log\Gamma(\sigma/2)$, and the
elementary $\log\sigma,\log(\sigma-1)$ terms) is untouched, since it never
referenced $\zeta$ beyond this one bounded contribution. $\square$

**Reading.** The entire growth obstruction of Theorem 110.2.4 is produced by
the $\Gamma(\sigma/2)$ factor alone (via Stirling: $\log\Gamma(\sigma/2)\sim(\sigma/2)\log\sigma$,
the term that dominates and produces infinite type). Swapping out $\zeta$
for *anything* bounded and zero-free — in particular, for a function with
its zeros moved anywhere at all, or with no zeros whatsoever — changes
nothing about (2.1) or about Theorem 110.2.4's conclusion. If ξ-divisibility
secretly depended on RH, this substitution would necessarily break the
proof (since a bounded zero-free $\zeta^\ast$ trivially satisfies "RH" in
the empty sense — it has no zeros to be off the critical line). It does not
break. This is the operational meaning of "the obstruction does not know
where the zeros are."

### Proposition 110.3.2 (contrast: it *is* the $\Gamma$-factor, not $\zeta$, that produces infinite type)

Let $\Gamma^\ast$ be any bounded function on $[2,\infty)$ (in particular,
*not* resembling $\Gamma(\sigma/2)$'s growth at all), and define
$\xi^{\ast\ast}(\sigma):=\tfrac12\sigma(\sigma-1)\pi^{-\sigma/2}\Gamma^\ast(\sigma)\zeta(\sigma)$
(the true $\zeta$ restored, the $\Gamma$-factor replaced by a bounded
dummy). Then $\log|\xi^{\ast\ast}(\sigma)|/\sigma$ stays **bounded** as
$\sigma\to\infty$ (finite type) — Theorem 110.2.4's obstruction disappears.

**Proof/verification.** With $\Gamma^\ast$ bounded, $\log|\Gamma^\ast(\sigma)|=O(1)$,
so $\log|\xi^{\ast\ast}(\sigma)|=O(\log\sigma)$ (all remaining terms —
$\log\sigma,\log(\sigma-1),-\tfrac\sigma2\log\pi,\log\zeta(\sigma)$ — are
$O(\sigma)$ at worst, with the $-\tfrac\sigma2\log\pi$ term giving finite,
not infinite, type), hence $\log|\xi^{\ast\ast}(\sigma)|/\sigma\to
-\tfrac12\log\pi=O(1)$, bounded. **Status: verified numerically below**
(§4 verifier, Check 1): with $\Gamma^\ast(\sigma):=e^{\sin\sigma}$ (bounded,
oscillating, chosen only to be manifestly unlike $\Gamma$'s true growth),
$\log|\xi^{\ast\ast}(\sigma)|/\sigma$ converges to a finite constant
($\approx-0.572$) rather than diverging. $\square$

**Conclusion of §2.** The impossibility proved in Task 2 is a **structural
fact about the Gamma factor's classical growth rate**, entirely
insensitive to $\zeta$'s zero structure. It is unconditional in the
strongest available sense: it survives even the extreme counterfactual of
deleting $\zeta$'s zeros altogether (Proposition 110.3.1), and it
evaporates the moment the *actual* source of the growth (the $\Gamma$
factor) is removed (Proposition 110.3.2). This is the opposite of what "RH
in disguise" would look like: an RH-in-disguise result would break under
Proposition 110.3.1's substitution (since it would depend on the genuine
zero set), not survive it unchanged.

## 3. What a genuine fix would require, stated candidly

Theorem 110.2.4 leaves exactly one door open, already exhibited
constructively in 110\_02 §5 (Example 110.2.6): **relax the admissible test
class from compact support to Schwartz-class** (smooth, rapidly decaying at
both ends of $(0,\infty)$, not required to vanish identically anywhere).
Under that relaxation, ξ-divisibility is achievable explicitly and
nontrivially, by a genuine theorem (110\_02 Example 110.2.6: for
$g(r)=e^{-(\log r)^2}$, $\hat f:=\xi\hat g$ is nonzero, ξ-divisible by
construction, and decays superexponentially on every vertical line — ready
for the Weil-formula sum). This is an **algebraic/analytic condition on
$\mathcal P$ stated independently of ξ-divisibility** (namely: "$g$ ranges
over the Schwartz class on the multiplicative group, rather than $C_c^\infty$")
under which ξ-divisibility becomes a theorem about $g\mapsto\xi\hat g$,
not a definition of $\mathcal P$.

**What this fix would still owe, and does not receive here:** the corner
pairing $I_\partial$'s Weil-formula identity (110\_00 §1) is quoted from the
source material as a fact about *admissible* (compactly supported) data;
extending its domain of validity to Schwartz-class data is a **separate,
nontrivial analytic undertaking** — one would need to redo the derivation of
that identity (typically via contour-shifting arguments in the Weil explicit
formula, and a matching extension of whatever geometric object $D_f$/$U_f$
is on the correspondence side) for the larger class, and to check that the
"admissible" notion used throughout 108\_03/108\_31 (which this phase was
not permitted to re-examine beyond the two supplied files) is compatible
with such an extension. **This phase does not attempt that extension**; it
identifies precisely where it would have to occur, consistent with the
task's request to "say precisely what that condition would have to be" —
here, the condition is a *domain enlargement of the corner pairing itself*,
external to the definition of ξ-divisibility, and it is flagged as open,
not claimed.

## 4. Final verdict

* **Is ξ-divisibility RH in disguise? No.** Proposition 110.3.1/110.3.2
  isolate the obstruction to $\Gamma$'s classical growth, unconditionally,
  independent of $\zeta$'s zero set.
* **Is it circular (N1)?** No — and not merely "avoided": there is no
  nonzero candidate within (ADM) to define into existence by fiat in the
  first place (Theorem 110.2.4).
* **Is it vacuous (N2)?** **Yes**, within the admissible (compactly
  supported) test class: $\{\hat f=\xi\hat g\}\cap(\text{ADM})=\{0\}$.
* **Does this bear on RH?** No. Every claim in 110\_01–110\_03 is
  unconditional; RH is neither assumed nor established, nor is any
  statement here equivalent to it.
* **Complete closure, per the phase's own rules.** A proved no-go is a
  complete closure (governing instructions, "Rules that are not
  negotiable"). ξ-divisibility, tested candidly against the admissible test
  class the corner pairing actually accepts, is such a no-go. The one
  documented route past it (§3: enlarge the test class to Schwartz-class)
  is recorded as an open, unattempted, and substantial separate undertaking
  — not softened into a positive result, and not claimed as one.

## 5. Scope

**Proved here:** Proposition 110.3.1 (obstruction survives an arbitrary
bounded zero-free substitution for $\zeta$); Proposition 110.3.2 (removing
$\Gamma$'s growth removes the obstruction) — both direct corollaries of the
Stirling computation in Theorem 110.2.2, adapted here.

**Read from source, not re-derived:** Theorem 110.2.2/110.2.4 (110\_02);
Theorem 110.1.4 (110\_01); the pre-registered criteria (110\_00 §2).

**Verified numerically:** Proposition 110.3.1's claim that the growth
constant is unchanged under the $\zeta\to\zeta^\ast$ substitution (matches
to $4$–$5$ significant figures at three scales); Proposition 110.3.2's claim
that removing $\Gamma$'s growth yields a bounded (not diverging)
growth ratio.

**Not established, and explicitly not claimed:** any extension of the
corner pairing's domain to Schwartz-class test data (§3, flagged open); any
statement about RH's truth value; any claim that Example 110.2.6's $f$ is
itself a legitimate corner-pairing input under the *current*, unmodified
definition of admissibility.

## 6. Verifier

`110_03_is_this_rh_in_disguise.py`: (1) confirms Proposition 110.3.1 —
substituting a bounded, zero-free dummy for $\zeta(\sigma)$ leaves the
leading growth ratio $\log|\xi^\ast(\sigma)|/(\sigma\log\sigma)\to1/2$
numerically unchanged (matches the true-$\zeta$ value to high precision at
matched $\sigma$, refined across three scales); (2) confirms Proposition
110.3.2 — substituting a bounded dummy for $\Gamma(\sigma/2)$ makes
$\log|\xi^{\ast\ast}(\sigma)|/\sigma$ converge to a **finite** value
(bounded, not diverging) under refinement, with a control that would reject
an incorrectly-still-diverging trend; (3) a joint sanity check that the true
$\xi$ (neither factor replaced) reproduces the original divergent trend of
110\_02, so checks (1)–(2) are read against a correctly-behaving baseline,
not a vacuously-passing setup.
