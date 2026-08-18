# 108.30 -- The component-triviality escape: not well posed for row (a)'s `D_f`, and already false on the fixed atlas for the only well-posed reading

## 1. The claim under test, and why it needs a reading before it can be tested

107_144 SS5 names, without attempting it, a possible target-retraction:

> "A future Phase 107 realization could attempt to prove that every
> realized \(D_f\) is component-trivial at every finite place... it would
> be a genuine target-retraction theorem."

108_00 SS8 elevates this to item 108.30: if true, \(c_p\) leaves the target
and 107_126's `TARGET_KODAIRA_ONLY: YES` already suffices, closing the
design fork that 107_126 left open.

Before testing anything, the claim needs a referent for "realized
\(D_f\)". This phase has, by this point, two constructions bearing that
name: 107_237's compactly-supported currents \(D_f\), \(f\in C_c\), and
108.03's graded family \(\mathcal G=\{U_s\}\). **Neither is a divisor on an
elliptic curve.** Both live on the universal positive chart of the Scaling
square \((0,\infty)\); nothing constructed anywhere in Phase 107 or 108 so
far maps them to points, or to horizontal divisors, on a Weierstrass model
over \(\mathbb Z\). So Reading A below is answered first, candidly, as not
yet posable; Reading B is the concrete question 107_144 SS5 was actually
gesturing at, using the only category in which "realized divisor" already
has a precise meaning: the horizontal degree-zero divisors of 107_144's own
local Neron-pairing computation.

### Reading A -- literal row-(a) `D_f` or `U_s`

**Status: not well posed.** There is no constructed map
\(\{D_f\}\cup\mathcal G\to\{\text{divisors on a fixed elliptic curve}\}\).
Component-triviality cannot be asked of an object that has not been placed
on a curve with a Neron model. This is the same shape of gap as 107_240
Theorem C and 108.04 SS2: a well-formedness gap, not a false statement.

### Reading B -- 107_144's horizontal divisors on the fixed atlas

**Status: well posed, and tested below.** 107_144 already works with
"realized" divisors \(D=(P)-(O)\) for \(\mathbb Q\)-rational points \(P\) on
fixed curves, computes their component-group membership via the explicit
Kodaira/Tamagawa data, and exhibits one such \(P\) that is *not*
component-trivial. This note extends that computation across the full
fixed atlas of 108_00 SS8 and draws the consequence for the escape.

## 2. Data, and where each fact comes from

All curve data below is either (a) proved in 107_144 (cited, not
re-derived, not modified), (b) an elementary consequence of the definition
of conductor (derived here, no computation needed), or (c) computed
directly in the verifier without Sage (the genus-2 control). No entry is
newly computed with Sage-dependent machinery, since Sage is unavailable in
this environment; this is stated candidly rather than worked around.

### 2.1 The forcing pair, `20a1@2` and `36a4@2` -- source: 107_144 SS3-4 (cited)

| curve | \(p\) | component group | realized point | order | component |
|---|---|---|---|---|---|
| `20a1` | 2 | \(\mathbb Z/3\mathbb Z\) (\(c_2=3\)) | \(P_+=(0,2)\) | 3 | **non-identity** |
| `36a4` | 2 | trivial (\(c_2=1\)) | \(T=(-6,0)\) | 2 | identity (forced: only one component exists) |

107_144 (3.2), SS3: \(P_\pm=(0,\pm2)\) on `20a1` have order \(3\) and do
**not** have smooth reduction at \(2\); the component group there has order
\(3\), so a nonidentity-order-3 point occupies one of the two nonidentity
classes. This is an explicit, already-published counterexample to
universal component-triviality: it is a \(\mathbb Q\)-rational point,
arithmetically as natural a "realized" divisor as exists, and it is not
component-trivial.

### 2.2 The controls, `14a1@5` and `11a1@5` -- elementary conductor argument (derived here)

The conductor of an elliptic curve \(E/\mathbb Q\) is, by definition,
divisible exactly by the primes of bad reduction. `14a1` has conductor
\(14=2\cdot7\); `11a1` has conductor \(11\). Neither is divisible by \(5\).
Hence both curves have **good reduction at \(5\)**: the special fiber of
the Neron model at \(5\) is already smooth, has a single component, and
*every* \(\mathbb Q_5\)-rational point (indeed every point) trivially meets
the identity component, because there is no other component to meet. This
requires no curve-specific computation, Sage or otherwise; it follows from
the definition of conductor alone (standard fact, e.g. Silverman AEC II
Ch. VII).

So `14a1@5` and `11a1@5` are **controls that pass trivially and cannot
falsify anything**: component-triviality can only fail at primes of bad
reduction, and \(5\) is not one for either curve. Any test restricted to
these two entries alone would vacuously "confirm" the escape; this is
exactly why the forcing pair (SS2.1) is the entry that carries the content.

### 2.3 Genus-2 control -- computed directly, no Sage

\(H:y^2=x^5+x+1\) over \(\mathbb F_5\) (107_144 SS7 item 4). Over
\(\mathbb F_5\), \(\tfrac{d}{dx}(x^5+x+1)=5x^4+1\equiv1\pmod5\), a nonzero
constant. Hence \(\gcd(f,f')=1\) automatically (a nonzero constant is a
unit), so \(f\) is squarefree mod \(5\) and \(H\) is smooth: a genuine
hyperelliptic curve of genus \(\lfloor(5-1)/2\rfloor=2\). This is verified
directly in the verifier by polynomial arithmetic over \(\mathrm{GF}(5)\),
with no Sage dependency. It confirms the formalism's genus computation is
correct; it is not, by itself, a component-triviality statement (a curve
given directly over \(\mathbb F_5\) has no Neron model over \(\mathbb Z\)
to speak of), and is not used as one.

## 3. Verdict on Reading B

### Theorem 3.1 (the escape fails)

Universal component-triviality of realized (\(\mathbb Q\)-rational,
horizontal, degree-zero) divisors on the fixed atlas is **false**: `20a1`
carries a rational point, of the same kind used throughout the legacy row's
own analysis, whose reduction at the curve's only bad prime in the atlas
misses the identity component.

**Proof.** SS2.1, citing 107_144 (3.2) and the component-group computation
of 107_144 SS2-3 (which gives the nonidentity correction \(4\log(2)/3\) for
exactly this point). \(\square\)

### What this does, and does not, decide

* It falsifies the *universal* escape on the fixed atlas: not every
  realized divisor is component-trivial.
* It does **not** show 107_126's `TARGET_KODAIRA_ONLY: YES` is wrong on the
  specific pair `20a1`/`36a4` -- that verdict compares *source packets*
  (whether the reduced target still distinguishes what the retained source
  data can distinguish), a different question from whether component data
  is *needed at all*. The escape hypothesis, had it held, would have argued
  the retained-\(c_p\) target (Target A) is never actually exercised because
  no realized divisor ever sees a nonidentity component. Theorem 3.1 shows
  a realized divisor does see one (on `20a1`), so this particular
  justification for discarding \(c_p\) does not exist. 107_144 Theorem 1
  (component data necessary for the full local target) stands
  un-retracted.
* It leaves Reading A exactly where SS1 put it: not yet well posed, because
  the row-(a) `D_f`/\(U_s\) objects have no constructed map to elliptic
  curves at all. A future construction of such a map is a prerequisite for
  ever testing Reading A, and nothing here builds one.

## 4. Scope

Proved/verified here:

* SS1: neither existing row-(a) divisor category is yet mapped to Neron
  models, so Reading A is not well posed;
* SS2.2: `14a1@5`, `11a1@5` pass only because \(5\) is a prime of good
  reduction for both -- an elementary, Sage-free conductor argument, not a
  substantive confirmation;
* SS2.3: the genus-2 control curve is smooth over \(\mathbb F_5\), computed
  directly (no Sage);
* Theorem 3.1: universal component-triviality on Reading B is false, using
  data already published in 107_144 SS3-4 (cited, not re-derived, not
  modified).

Not established:

* any component-triviality statement about literal row-(a) `D_f` or the
  graded family \(\mathcal G\) (Reading A remains open, and is not
  advanced by this note beyond stating why it cannot yet be posed);
* any retraction of 107_144 Theorem 1 or of 107_126's
  `TARGET_KODAIRA_ONLY: YES` verdict on its own specific pair;
* whether some *restricted* class of realized divisors (narrower than "all
  \(\mathbb Q\)-rational points") might still be uniformly component-trivial
  -- not investigated here, and would need a construction connecting row
  (a) to elliptic curves before it could even be framed precisely
  (Reading A's gap again).

This closes 108.30 as a no-go on the only currently well-posed reading of
the escape, consistent with 108_00 SS9.3 ("a failed gate is the
deliverable").

## 5. Verifier

`108_30_component_triviality_escape_test.py`:

1. reproduces, from the numbers published in 107_144 (not recomputed via
   Sage, which is unavailable here), the `20a1@2`/`36a4@2` component-group
   orders and the order/reduction status of \(P_+\) and \(T\);
2. derives the good-reduction-at-5 triviality for `14a1` and `11a1` from
   their conductors (\(14=2\cdot7\), \(11\)) alone, i.e. checks
   \(5\nmid14\) and \(5\nmid11\), and states the resulting component group
   is trivial by definition;
3. verifies the genus-2 control directly: builds \(f=x^5+x+1\) and
   \(f'=5x^4+1\) as polynomials over \(\mathrm{GF}(5)\), reduces
   coefficients mod \(5\), confirms \(f'\) is the nonzero constant
   polynomial \(1\), computes \(\gcd(f,f')\) by explicit polynomial
   Euclidean algorithm over \(\mathrm{GF}(5)\) and confirms it is a nonzero
   constant (squarefree), and reports genus \(\lfloor(5-1)/2\rfloor=2\);
4. prints the falsifying witness (`20a1`, \(P_+\), order 3, non-identity)
   and `VERDICT: NO` for universal component-triviality on Reading B, with
   `READING_A: NOT_WELL_POSED` recorded separately (not folded into the
   NO, since it is a different kind of gap).
