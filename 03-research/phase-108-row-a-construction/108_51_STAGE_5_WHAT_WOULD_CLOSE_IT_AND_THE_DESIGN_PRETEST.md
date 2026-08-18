# 108.51 — Stage 5: what would have to be true, and the design pre-test on
the regularized route

## 0. Result

108_50 proved that no comparison map exists at the level of the natural
generators of the two quotients, in either direction. This note carries out
the two remaining deliverables of Stage 5 that survive that impossibility:
(3) it states precisely, with named objects, what would have to be true for
Stage 3's assembly to be an intersection number, via the one route 108_50
left open — a **regularized** comparison, smearing the graded family to
compact support and taking a limit; and (4) it applies 108_90's
rigidity-versus-finiteness design condition to that route as a pre-test, and
reports the result: **the route passes the pre-test architecturally, but a
toy computation below shows that passing the pre-test does not supply the
convergence the route needs, and that convergence is a genuine, unproved,
and (on the evidence of the toy model) not merely technical requirement.**

## 1. The regularized route

108_50 §2 showed $f_s$ cannot itself be compactly supported. The one
opening 108_90 §3 records — instance 8's escape — is to smear rather than
convert: replace $f_s$ by a family $f_{s,T}$, $T>0$, that **is** compactly
supported for every finite $T$ (e.g.\ $f_s$ windowed to $[1/T,T]$, or
convolved with a compactly supported approximate identity of width
shrinking as $T\to\infty$), and move the comparison into a **limit of the
pairing**, not a map of the objects themselves.

Concretely, this defines, for each finite $T$, a genuine Stage-0
correspondence divisor $D_{f_{s,T}}$, and a real number (or complex number)
$I_{\mathrm{partial}}(D_{f_{s,T}},D_{g_T})$. The candidate comparison map is
\[
 \delta_s\ \longmapsto\ \big[D_{f_{s,T}}\big]\in V,\qquad T\to\infty,
\]
in whatever sense the limit of $I_{\mathrm{partial}}(D_{f_{s,T}},D_{g_T})$
exists.

## 2. What would have to be true (deliverable 3)

Stage 3's identity (108_36 Theorem 1.1, 108_38 §1) is
\[
 L_g(s)=c_g(s)\Phi(s),\qquad
 \Phi(s)=\pi\cot\tfrac{\pi s}2-\tfrac{\zeta'}\zeta(s)-\tfrac{\zeta'}\zeta(1-s).
\]
For this to literally **be** an intersection number $I_{\mathrm
partial}([D],[D'])$ on $V$, three separate conditions are needed, none of
which is established anywhere in this programme to date.

> ### Condition I (regularizing family exists in Stage 0's category)
> For every $s$ in the index set and every admissible $g$, there exist
> compactly supported $f_{s,T}$, $g_T$ ($T>0$) such that
> $D_{f_{s,T}},D_{g_T}$ are correspondence divisors in Stage 0's sense for
> every finite $T$, and $f_{s,T}\to f_s$ in whatever topology makes
> $c_g(s)$ (108_06 (2.5)) the correct limiting pairing coefficient.

> ### Condition II (the regularized pairing converges to the Stage 3 value)
> \[
>  \lim_{T\to\infty} I_{\mathrm{partial}}\big(D_{f_{s,T}},D_{g_T}\big)
>  = c_g(s)\,\Phi(s)
> \]
> for every $s$ and every admissible $g$ — an identity between a limit of
> genuine intersection numbers and Stage 3's closed form. This is a
> nontrivial analytic theorem, not a formal consequence of Condition I: §3
> below exhibits a toy computation in which the analogous naive limit
> **diverges**, so Condition II cannot be assumed to hold merely because a
> regularizing family (Condition I) can be built.

> ### Condition III (the radicals correspond)
> The map $s\mapsto[D_{f_{s,T}}]$, $T\to\infty$, sends
> $\mathrm{rad}\,\Lambda^0$ (108_38 Theorem 3.3: spanned by point masses
> at the zeros of $\Phi$) into $\mathrm{rad}\,I_{\mathrm{partial}}$, so
> that it descends to a well-defined map on the quotients
> $\mathrm{Prin}'/\mathrm{rad}\,\Lambda^0\to V$ under which the two
> pairings agree — not merely at the level of individual values (Condition
> II) but as forms on the quotient spaces.

> ### Statement
> If Conditions I–III all hold, then Stage 3's assembly
> $L_g(s)=c_g(s)\Phi(s)$ **is** the image, under the regularized comparison
> map, of the corner pairing $I_{\mathrm{partial}}$ on $V$ — i.e.\ it is an
> intersection number, and Stage 5 closes completely, joining the two halves
> of the programme exactly as 108_38 §4 anticipated.

None of Conditions I, II, III is proved or disproved here. Condition I is
architecturally unproblematic (any reasonable cutoff produces compactly
supported data). Condition III cannot even be examined with the material
available to this note, because $\mathrm{rad}\,I_{\mathrm{partial}}$'s
generating description was not read here (108_50 §5, Scope). Condition II
is examined directly in §3, and found to fail in the naive form.

## 3. A toy model showing Condition II is not automatic

This section studies a **model** computation, not Stage 0's actual
$I_{\mathrm{partial}}$: the exact operator $T(\cdot)$ is unknown to this
note (108_50 §5, Scope). The model is offered only as evidence that formal
cutoff-and-limit constructions of this shape do not converge for free, and
that mass-zero alone does not repair this, contrary to what one might
optimistically hope by analogy with 108_33's removal of Stage 1's divergent
constant.

**The model.** Represent the cutoff of a pure dilation eigenfunction
$x\mapsto x^{s-1}$ to the "compact support window" $[1/T,T]$, and pair it
with itself under the model bilinear functional
$P(T;a)=\int_{1/T}^{T}x^{a-1}\,dx$ (a stand-in for a corner-type pairing
evaluated on the cutoff data, chosen only because it is the simplest
bilinear functional respecting scaling on an interval symmetric under
$x\mapsto1/x$, the shape common to Tate-style local integrals). In closed
form,
\[
 P(T;a)=\begin{cases}\dfrac{T^{a}-T^{-a}}{a}, & a\ne0,\\[4pt]
 2\log T, & a=0.\end{cases}
\]

> ### Proposition 3.1 (the toy regularized pairing diverges on a mass-zero
> pair)
> Let $s_1=0.3,\ s_2=0.7$, $\lambda_1=1,\ \lambda_2=-1$ (so
> $\lambda_1+\lambda_2=0$, matching the mass-zero condition of
> $\mathrm{Prin}'$), and set
> $Q(T)=\lambda_1P(T;s_1)+\lambda_2P(T;s_2)$. Then $Q(T)\to-\infty$ as
> $T\to\infty$.

**Proof.** $Q(T)=\dfrac{T^{0.3}-T^{-0.3}}{0.3}-\dfrac{T^{0.7}-T^{-0.7}}{0.7}$.
As $T\to\infty$, $T^{-0.3},T^{-0.7}\to0$, so
$Q(T)=\dfrac{T^{0.3}}{0.3}-\dfrac{T^{0.7}}{0.7}+o(1)$. Since $0.7>0.3$, the
second term dominates in absolute value, and it carries a minus sign, so
$Q(T)\to-\infty$. $\blacksquare$

**What this shows, and its limits.** In this model, the mass-zero condition
that made Stage 1's *constant* term drop out (108_33; the removed term in
108_38 §1 is $s$-independent) does **not** make the *leading, $T$-dependent*
divergence of a cutoff pairing drop out, because that divergence's exponent
depends on $s$ itself, not just on the mass-zero condition on the
$\lambda_i$. So Condition II, if true at all, needs either a different
regularization than a flat cutoff (e.g.\ one carrying its own
$s$-dependent counter-term, in the spirit of 108_36's removal of the
constant $(\log p)\sum_pC_p$, but now for a $T$-divergent rather than
constant term) or a fundamentally different route into $V$ than
"cutoff-then-limit." **This is illustrative, not a proof that Condition II
is false**: $I_{\mathrm{partial}}$ is not the toy $P(T;\cdot)$, and Stage 0's
actual construction may already build in exactly the renormalization the toy
model lacks. The claim is narrower and is exactly what is needed: the
convergence in Condition II is not a formality that comes for free once
Condition I is met, and asserting it without proof would be exactly the kind
of overclaim the task rules out.

## 4. The design-condition pre-test (deliverable 4)

108_90 §3's design condition: *never require one object to be both
$\Gamma$-equivariant and finitely supported; put equivariance on one side of
a duality, finiteness on the other, and regularize the pairing.*

Apply it to the regularized route of §1–§2.

* **Equivariance.** Carried entirely by the untruncated graded family $f_s$
  (and, in the limit, by $s$ itself as a continuous parameter) — never by
  the cutoff family $f_{s,T}$, which is not asked to be equivariant for any
  finite $T$.
* **Finiteness.** Carried entirely by $f_{s,T}$, compactly supported in
  Stage 0's exact sense, for every finite $T$ — never by $f_s$ itself.
* **What is regularized.** Not either object, but the **pairing**
  $I_{\mathrm{partial}}(D_{f_{s,T}},D_{g_T})$, via the limit $T\to\infty$ —
  exactly the role $\langle k_T,\varphi\rangle\to2\pi\varphi(0)$ played in
  108_05/108_90 §3 for the unrelated cutoff there.

> ### Verdict of the pre-test
> **Passes.** The construction of §1 does not, at any point, ask a single
> object to be both equivariant and finitely supported; the two properties
> sit on opposite sides ($f_s$ versus $f_{s,T}$) of exactly the kind of
> duality 108_90 prescribes, and what is regularized is the pairing
> (Condition II), not either object.

This verdict is architectural, not analytic, and 108_90 §0 is explicit that
the design condition itself is "a synthesis with retrodictive support, not a
theorem." Passing it certifies only that the construction avoids the *known*
dead end (the one that sank Stage 3 as originally posed, per 108_90 §5). It
does not certify that the limit in Condition II exists: §3's toy model gives
a concrete reason to expect that establishing it will require genuine new
analytic work — most plausibly an $s$-dependent renormalization on top of
the cutoff, not visible from the design condition alone.

## 5. Scope

**Read.** 108_38, 108_37, 108_90 (all in full, as in 108_50); 108_50 (this
note's own prerequisite, written earlier in this session).

**Proved here.** Proposition 3.1 (elementary calculus, complete proof).

**Stated, not proved.** Conditions I–III of §2 (these are exactly the
missing theorems, named as precisely as the available material allows;
proving any of them is future work, not attempted here).

**Read from source and applied, not re-derived.** 108_90's design condition
and its own self-description as retrodictive-not-theorem.

**Explicitly not attempted.** Any comparison of $\mathrm{rad}
I_{\mathrm{partial}}$'s generating data against the zeros of $\Phi$
(Condition III), for the reason given in 108_50 §5: this note does not have
Stage 0's internal definitions.

**No zero of $\xi$ enters any definition in this note.**

## 6. Verifier

`108_51_toy_regularized_pairing_divergence.py` computes $P(T;s_1),P(T;s_2)$
and $Q(T)$ from the closed forms of §3 for a range of $T$ from $10$ to
$10^{12}$, confirms the closed form against direct numerical quadrature at
moderate $T$, confirms $Q(T)\to-\infty$ monotonically for large $T$ (no
threshold beyond floating range: the test is that $Q$ is strictly
decreasing and unbounded below on the tested range, which is the actual
mathematical property of Proposition 3.1), and confirms the exponent of
divergence matches $s_2=0.7$ by a log-log slope fit.
