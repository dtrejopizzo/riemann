# 108.19 — Route E (the radical): the constant's contribution is not
# invisible, by direct reduction to an already-proved witness

## 0. Result

Route E asks whether the constant's contribution to the assembled pairing —
an $a$-independent scalar $\sum_vC_v$ multiplying $c_g(a)$, integrated
against test data — lies in the radical of the corner-pairing form
$I_\partial$, so that it is invisible on the numerical quotient of 107_240
§5 without ever having to evaluate $\sum_vC_v$. The mission explicitly warns
that the naive version of this idea (a degree-zero combination
$\sum_i\lambda_if_{a_i}$, $\sum_i\lambda_i=0$) fails for the same reason
Route C failed, and asks that any version of Route E either avoid that trap
or say plainly that it cannot.

> **Route E, run without the combination trick, reduces to the exact
> statement 108_15 Theorem 3.1 already proved: the rank-one functional
> carrying the constant's contribution is nonzero on an explicit witness
> pair. Membership in the radical requires vanishing against every
> witness; one nonzero witness excludes it. Route E fails, and the proof is
> a direct corollary of already-established work, not a fresh construction
> — which is also the sense in which the trap is avoided: no combination of
> $f_{a_i}$'s is used anywhere below.**

No zero of $\xi$ is used anywhere. `ROW_A_STATUS` remains `partial`.

## 1. The functional in question

108_11–108_16 write the assembled pairing of the constant piece against test
data $(g,\varphi)$ — $g$ the test function of 108_06 Proposition 2.1,
$\varphi$ a smearing profile in $a$ — as

\[
 \Big(\textstyle\sum_vC_v\Big)\cdot\Phi(g,\varphi),
 \qquad
 \Phi(g,\varphi):=\int_0^1\varphi(a)\,c_g(a)\,da ,
\]

exactly the object 108_15 §5–6 constructs and evaluates: a scalar
($\sum_vC_v$, of unknown/divergent status) times a bilinear functional $\Phi$
of $(g,\varphi)$ built entirely from $c_g$ (108_06 Prop 2.1, entire in $a$)
and the smearing profile. This is precisely "a rank-one form factoring
through the constant function in $a$," as the mission states it: the
$a$-dependence of the whole contribution is carried by $c_g(a)$ alone, with
$\sum_vC_v$ a fixed multiplier out front.

> ### Definition 1.1 (radical membership, as the question actually posed)
> The constant's contribution is **invisible on the numerical quotient**
> exactly if $\Phi(g,\varphi)=0$ for **every** admissible pair $(g,\varphi)$
> — i.e. if $\Phi\equiv0$ as a functional, independently of the value (or
> divergence) of the scalar multiplier $\sum_vC_v$ in front of it. This is
> the radical-membership question stripped to what it needs: whether the
> *shape* of the constant's contribution ($\Phi$) is identically zero, not
> whether its *coefficient* ($\sum_vC_v$) is.

This framing already shows why the naive combination trick fails, and why
this note does not use it: $\Phi\equiv0$ is a global, one-time question about
the functional as a whole. Testing it by combinations $\sum_i\lambda_if_{a_i}$
introduces extra structure (the $\lambda_i$, the finitely many points $a_i$)
that is not needed and is exactly what the mission's warning targets: **a
combination is never used below.** Instead, Definition 1.1 is settled by
asking whether *any single* $(g,\varphi)$ makes $\Phi$ nonzero — the
logically minimal test, and the one 108_15 already performed for an
unrelated purpose.

## 2. The witness, already on record

> ### Theorem 2.1 (nonvanishing, cited)
> 108_15 Theorem 3.1 (Steps 1–4) proves: for every $g\ne0$, $c_g$ is entire
> and not identically zero on $\mathbb C$ (Mellin/Fourier injectivity), hence
> (identity theorem) not identically zero on the open interval $(0,1)$
> either; consequently a test profile $\varphi$ detecting a nonzero pairing
> always exists. 108_15 §6 exhibits this concretely: an explicit nonzero $g$
> satisfying the exact primitive condition $\hat g(0)=\hat g(1)=0$, and an
> explicit bump $\varphi$ supported on $[0.3,0.7]\subset(0,1)$, with
> \[
>  \Phi(g,\varphi)=\int_0^1\varphi(a)c_g(a)\,da\;\ne\;0
> \]
> verified numerically there to many orders of magnitude above the
> constraint-residual noise floor (108_15 §6, "pairing_nonzero" check), and
> cross-checked against a second, independent family $g'$ with the same
> constraints, ruling out an accidental universal cancellation.

**Proof.** This is 108_15 Theorem 3.1 and its §6 numerics, restated; no new
argument is supplied here — it is cited because it is exactly the fact
Definition 1.1 needs. $\square$

> ### Theorem 2.2 (Route E fails)
> $\Phi\not\equiv0$: by Theorem 2.1, there exists an admissible pair
> $(g,\varphi)$ with $\Phi(g,\varphi)\ne0$. By Definition 1.1, the
> constant's contribution is therefore **not** invisible on the numerical
> quotient: it does not lie in the radical of the pairing, whatever the
> precise value (finite or divergent) of the scalar $\sum_vC_v$ turns out to
> be. Route E fails.

**Proof.** Immediate: "$\Phi\equiv0$" and "$\exists$ a pair with
$\Phi\ne0$" are negations of each other; Theorem 2.1 supplies the latter.
$\square$

## 3. Why the trap is avoided, and why no combination could have helped
   anyway

The mission's warning is precise: taking $\sum_i\lambda_if_{a_i}$ with
$\sum_i\lambda_i=0$ does not help, because the constant's contribution
becomes $K\cdot\sum_i\lambda_ic_g(a_i)$, and Mellin evaluations at distinct
points $a_i$ are linearly independent functionals of $g$, forcing every
$\lambda_i=0$ — the same mechanism 108_15 Theorem 3.1 Step 1–2 already
proves (entire-function injectivity of the Mellin/Fourier transform). This
note's Theorem 2.1–2.2 sidesteps the trap **structurally**, not by luck:

* it never introduces a finite combination $\sum_i\lambda_if_{a_i}$ at all;
  the question (Definition 1.1) is posed directly about the functional
  $\Phi$ as a whole, evaluated against continuum test data $\varphi$, which
  is exactly the category $\Phi$ is already defined on (108_11's own
  construction);
* the witness that answers it (Theorem 2.1) is a single admissible pair, not
  a combination engineered to vanish at finitely many points and hence
  forced trivial by the same rigidity that would have killed the
  combination trick.

That said, candor requires flagging the following: **the *reason*
Theorem 2.1's witness is nonzero is the identical entire-function rigidity
that makes the combination trick vacuous.** 108_15 Theorem 3.1's Steps 1–2
(Mellin injectivity: $c_g\equiv0$ on an interval $\Rightarrow g=0$) is what
forces $\Phi\not\equiv0$ for nonzero $g$ in the first place. So Route E does
not fail by a *different* mechanism from Route C (108_16 §5's Theorem 5.1
already anticipates this: "the three failures... trace to one underlying
fact") — it fails by the **same** mechanism, viewed as a statement about the
functional $\Phi$ rather than about finite linear combinations of point
evaluations. This is stated plainly, per the mission's instruction, rather
than presented as an independent escape.

## 4. What this does, and does not, use from 107_240

108_00 §3 records, as inherited state (not re-derived here): "107_240 ...
Thm D: `rad I_∂` is zero-determined; §5: the numerical quotient is free."
This note does not need, and does not attempt, a precise unpacking of
"zero-determined" — Theorem 2.2 above settles the question that matters for
Stage 1 *directly*, via the explicit witness of §2, without needing the
abstract characterization of `rad I_∂` at all. The inherited fact is
recorded here only for consistency: a free numerical quotient is, at least,
not obviously hospitable to a nonzero functional accidentally lying in its
own radical, which is qualitatively consistent with (though not needed to
derive) Theorem 2.2's conclusion.

> ### Corollary 4.1 (scope of what is and is not settled)
> This note shows $\Phi\not\equiv0$, hence the constant's contribution is
> **detectable** — not invisible — on admissible test data. It does **not**
> show $\sum_vC_v$ itself is finite, nor compute it, nor say anything new
> about whether *some other* functional built from $\sum_vC_v$ differently
> might vanish; it settles exactly the one functional ($\Phi$, as defined by
> 108_11's own construction and used throughout 108_12–108_16) that the
> mission's Route E specifies.

## 5. Scope

Proved here:

* Definition 1.1's reduction of radical-membership to $\Phi\equiv0$ for the
  functional actually used in 108_11–108_16's construction;
* Theorem 2.2: $\Phi\not\equiv0$, by direct citation of 108_15 Theorem 3.1's
  witness — Route E fails;
* §3: the trap is avoided (no combination $\sum_i\lambda_if_{a_i}$ is used),
  while being explicit that the underlying rigidity mechanism is the same
  one that made the trap a trap in the first place, and the same one 108_16
  §5 already identified as common to routes A–C.

Not established, and explicitly not claimed:

* any unpacking of `rad I_∂`'s precise technical definition from 107_240
  (not re-derived; only the already-quoted headline facts of 108_00 §3 are
  used, for consistency, not as load-bearing steps);
* any value for $\sum_vC_v$;
* that no *other* notion of "invisibility" (not captured by
  $\Phi\equiv0$ against $(g,\varphi)$) could still apply — only the specific
  functional this program has used throughout is tested;
* anything about the zero side or about RH.

## 6. Verifier

`108_19_route_e_radical_membership_excluded.py` reconstructs, independently
(not by importing 108_15's code), the same class of $g$ satisfying the exact
primitive condition $\hat g(0)=\hat g(1)=0$ and a bump $\varphi$ supported
in $(0,1)$, evaluates $\Phi(g,\varphi)=\int\varphi(a)c_g(a)\,da$, and
confirms it is nonzero at a scale many orders of magnitude above the
constraint-residual noise floor — the exact witness Definition 1.1 needs —
together with a second, independently parametrized family confirming the
nonvanishing is not an accident of one specific choice.
