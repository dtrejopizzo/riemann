# 114.a.137 — R8 is closed; the full effectivity dictionary is a different gate

~~~
+------------------------------------------------------------------------+
| SOURCE R8   No nonzero radical representative may become effective.     |
| RAW THETA   h_theta(O_X)>0, so the raw positivity predicate fails R8.    |
| REPAIR      L is strictly effective iff h_theta(L)>h_theta(O_X).         |
| FORCED      Requiring O_X to lie exactly on the boundary fixes the       |
|             constant threshold uniquely.                                |
| SEPARATION  A source/target effectivity biconditional is G3-EFF/G-7,     |
|             not an additional clause of the R8 acceptance test.          |
| VERDICT     R8 is closed without assuming RH.                            |
+------------------------------------------------------------------------+
~~~

## 1. The exact requirement

The phase-113 requirement R8 says that a nonzero element of the radical
cannot be declared effective after passing to divisor classes. If a
realisation \(\iota\) has

\[
 \ker\iota=\mathrm{rad} I_d,
\]

then every radical element has target class \(\mathcal O_X\). Thus R8 tests
the target predicate at one distinguished basepoint; it does not by itself
assert a biconditional on every source class.

For the imported theta invariant,

\[
 h_\theta(\mathcal O_X)=
 \log\sum_{n\in\mathbb Z}e^{-\pi n^2}>0.                              \tag{1.1}
\]

Consequently the raw rule \(h_\theta(L)>0\) declares the basepoint effective
and fails R8.

## 2. Forced repair

Define strict target effectivity by

\[
 L\in\mathrm{Eff}_{\rm thr}
 \quad\Longleftrightarrow\quad
 h_\theta(L)>h_\theta(\mathcal O_X).                                  \tag{2.1}
\]

Every radical element maps to \(\mathcal O_X\), where equality rather than
strict inequality holds. Hence no nonzero radical representative is
strictly effective.

Among predicates of the form \(h_\theta(L)>t\), requiring the trivial class
to lie exactly on the boundary gives

\[
 t=h_\theta(\mathcal O_X).                                           \tag{2.2}
\]

Therefore the repair is canonical within the constant-threshold class. It
does not replace the cohomological invariant inside Riemann--Roch; it only
normalises the sign predicate.

### Theorem 2.1

R8 is satisfied by (2.1), unconditionally and independently of RH.

This is exactly the repair proved in a08 and in 114_d3_03; the present note
settles its scope in the row-A ledger.

## 3. What is not part of R8

The stronger statement

\[
 c\in\mathrm{Eff}_{\rm source}
 \quad\Longleftrightarrow\quad
 h_\theta(\iota(c))>h_\theta(\mathcal O_X)                            \tag{3.1}
\]

for every source class requires construction of \(\iota\) and comparison of
two cones. It is the full effectivity dictionary. On \(D^\circ\), adding
quadratic domination turns (3.1) into G3-EFF, proved RH-equivalent in a60.
Outside \(D^\circ\), the extension remains a separate G-7 compatibility
problem.

Failure to prove (3.1) therefore does not reopen R8. Conversely, passing R8
does not prove (3.1), G-3, row A or RH.

## 4. Updated non-H7 status

| item | rigorous status |
|---|---|
| G-1 | closed by a11 |
| G-2 | closed by a08 |
| G-3 | fully delimited: meaningful branches are RH-equivalent |
| R8 acceptance test | closed by the forced threshold |
| full effectivity dictionary | separate G3-EFF/G-7 gate |

After this scope correction, the unconditional construction still missing
from row A lies in I7/G-7, not in G-1, G-2 or R8.

The verifier 114_a_137_r8_scope_verify.py checks the positive theta
basepoint, exact threshold cancellation, uniqueness and scope separation.
