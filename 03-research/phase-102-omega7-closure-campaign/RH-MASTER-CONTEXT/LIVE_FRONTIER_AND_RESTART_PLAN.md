# Live frontier and restart plan

## Corrected governing rule

No statement will be discarded, downgraded or avoided for being RH-strength. If a true statement is
equivalent to RH and appears as a necessary obligation, then that is precisely the theorem the
program must prove. The **RH-STRENGTH** label is a marker of priority and mathematical load, not a
veto.

The only distinction that is kept is logical:

- a false statement must be corrected or replaced;
- an RH-strength statement must be attacked until a proof is obtained;
- an equivalence with RH can be used as a conclusion or as a change of coordinates, but not as a
  hypothesis without an independent proof;
- an independent proof may establish a criterion equivalent to RH from Euler–Gamma, geometric or
  operator data: doing so counts as proving RH and is the project's goal.

Therefore, expressions such as "this contains the full force of RH" do not close a route. They
identify the point where new mathematics must be created.

## Canonical list of obligations to close \(\Omega_7\)

### Closure criterion

\(\Omega_7\) will be closed only when there exists a complete proof of

\[
   \lambda_n=\lambda_n^{\rm arch}+\lambda_n^{\rm prime}\ge0
   \qquad\text{for all }n\ge1,
\]

with the prime part defined via its paired continuation, and when Li's theorem allows concluding
RH without any intermediate open hypothesis. A finite verification, a conditional identity, a
numerical estimate, or a chain that still contains an unproved obligation is not enough.

The list is split into a **mandatory trunk**, which every proof must close, and two **construction
lanes**. It suffices to fully complete one of the lanes; it is not necessary to close LP+IDENT if the
direct Li attack produces the global inequality.

### Mandatory trunk

1. **Fix the exact target. — CLOSED.**

   Prove and use exclusively
   \[
      \Omega_7
      \Longleftrightarrow
      \lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch}
      \quad(n\ge1).
   \]
   The absolute bound on the prime part is only a sufficient strategy for certain indices, not the
   logical target.

2. **Fix the arithmetic continuation. — CLOSED.**

   Keep the pole and the prime sum joined:
   \[
   \lambda_n^{\rm prime}
   =\lim_{\varepsilon\downarrow0}
   \left[
   \sum_{k=1}^n\binom nk\frac{(-1)^{k-1}}{\varepsilon^k}
   -\sum_{m\ge2}\frac{\Lambda(m)}{m^{1+\varepsilon}}
    L_{n-1}^{(1)}(\log m)
   \right].
   \]
   No proof may split two divergent series at the boundary and estimate them separately.

3. **Close the integration-by-parts identity together with its boundary. — CLOSED.**

   With
   \(f_{n,\varepsilon}(y)=y^{-1-\varepsilon}L_{n-1}^{(1)}(\log y)\), use
   \[
   \lambda_n^{\rm prime}
   =\lim_{\varepsilon\downarrow0}
   \left[-n+\int_1^\infty(\psi(y)-y)f'_{n,\varepsilon}(y)\,dy\right]
   =\lim_{\varepsilon\downarrow0}
   \int_1^\infty(\psi(y)-y+1)f'_{n,\varepsilon}(y)\,dy.
   \]

4. **Rigorously separate the exceptional finite range. — CLOSED.**

   It is already proved that
   \[
      \lambda_n^{\rm arch}<0\iff1\le n\le7.
   \]
   Moreover, the finite certificate
   `fragments/OMEGA7_POINT4_FINITE_CERTIFICATE.md` proves with rational intervals that
   \[
      \lambda_n>0,\qquad 1\le n\le7,
   \]
   using only the Laurent expansion of \(\zeta\) at \(1\), the Euler–Gamma part, and rational interval
   arithmetic. This block is finite and does not contain the asymptotic problem.

5. **Prove the global signed inequality. — OPEN / RH-STRENGTH.**

   For all \(n\ge8\), prove
   \[
      \boxed{
      \lim_{\varepsilon\downarrow0}
      \int_1^\infty(\psi(y)-y+1)f'_{n,\varepsilon}(y)\,dy
      \ge-\lambda_n^{\rm arch}}
   \]
   from arithmetic data. This is the central core. Its RH-strength does not authorize suspending it:
   it requires finding an identity, one-sided inequality, variational principle or geometric
   structure that proves it.

6. **Uniformly justify the boundary limit. — OPEN.**

   The estimate proving point 5 must be uniform in \(\varepsilon\downarrow0\). One must exhibit an
   integrable quantity or an exact cancellation that allows passing to the limit without replacing the
   integrand by its absolute value and without losing the term \(-n\).

7. **Control all scales of \(n\). — OPEN.**

   The proof must simultaneously cover:

   - the finite range after \(I_-\);
   - the transition zone of the Laguerre kernel;
   - the oscillatory regime \(\log m\lesssim4n\);
   - the tail \(\log m\gtrsim4n\);
   - the limit \(n\to\infty\).

   It may do so via a global theorem that avoids this partition, but it cannot leave constants
   dependent on \(n\) that destroy the final inequality.

8. **Preserve the sign before estimating. — OPEN.**

   A pairing or decomposition must be constructed for which the negative excursion is visible
   without applying
   \[
      \left|\int gh\right|\le\int|g||h|.
   \]
   The sought object must jointly retain pole, Gamma, primes, conjugation and boundary. Loss of sign
   via shells or individual primes cannot be recovered afterward.

9. **Prove the discriminating mechanism from arithmetic data. — OPEN / RH-STRENGTH.**

   Whatever form is chosen in points 5–8, its hypotheses must be proved for \(\zeta\) from an
   independent construction. It is not enough to define a metric, measure, current or factorization
   that exists exactly when \(\lambda_n\ge0\). If the mechanism itself is equivalent to RH, it must be
   proved: it will not be discarded for that equivalence.

10. **Prove off-line sensitivity within a typed class. — VALIDITY CONTROL OPEN.**

    Construct a class \(\mathcal C_{\rm Euler}\) with shared Dirichlet data, Gamma factor, functional
    equation and continuation. The new mechanism must:

    - work for \(\zeta\)'s data;
    - be compatible with an on-line control;
    - fail structurally for an off-line arithmetic member.

    This point is not a logical premise of Li's criterion and must not be artificially inserted into
    the proof. It is a validity control of the mechanism: it prevents inverting the program into an
    identity unable to distinguish the sought phenomenon.

11. **Close the Li assembly. — OPEN, dependent on 4–9.**

    Combine the certificates for \(1\le n\le7\) with the uniform theorem for \(n\ge8\), conclude
    \(\lambda_n\ge0\) for all \(n\), verify the hypotheses of the version of Li's criterion used, and
    deduce RH. This last step is short, but it is only closed when it carries no pending hypothesis.

### Lane A — direct Euler–Gamma/Laguerre construction

This is the priority lane. To complete point 5 it must close, in this order:

12. **Find an elementary signed unit. — OPEN.**

    Identify blocks of primes or intervals of \(\log m\) whose combined contribution with the pole and
    Gamma has a lower bound, even if each term separately changes sign.

    The updated triage is in `fragments/OMEGA7_CARRIL_A_FIRST_TARGET.md`: no sound local unit was
    found; the minimal canonical unit is global, a continuous pole against all prime powers.
    That is why the first technical target is separated into A0, an unconditional uniform tail, and
    A1, the RH-strength signed core.

13. **Prove a global compensation law. — OPEN / RH-STRENGTH.**

    Construct an involution, coboundary, functional identity, energy inequality or variational
    principle that sums these units before taking magnitudes and yields exactly the bound of point 5.

14. **Close the signed truncation error. — OPEN.**

    For every truncation used, prove that the omitted contribution preserves the one-sided inequality
    or converges with a controllable signed remainder. A norm bound on the tail is not enough if it is
    larger than the archimedean margin.

15. **Close the \((n,\varepsilon,X)\) uniformity. — OPEN.**

    Declare the order of limits and prove the uniform estimates needed for
    \(X\to\infty\), \(\varepsilon\downarrow0\) and \(n\to\infty\). Swapping these limits by pointwise
    convergence is not accepted.

16. **Turn the mechanism into the global theorem of point 5. — OPEN.**

    The lane's final result must not be a new coordinate: it must literally deliver
    \(\lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch}\) for all \(n\ge8\).

### Lane B — LP+IDENT/RDI, only if it produces Li's sign

This lane is alternative. To complete it, all the following points must be closed and, at the end,
its explicit link to point 5 must be proved:

17. **BTG-DIV in the true measure \(\mu_L\). — OPEN.**
18. **LP interface free of a circular choice of \(\mu_L\). — OPEN.**
19. **GAP-Z, including the ZERO contribution with signed cancellation. — OPEN.**
20. **RDI-ANCHOR or a single fully written equivalent formulation. — OPEN / RH-STRENGTH.**
21. **RDP-SHELL with directional tails after the signed pairing. — OPEN.**
22. **SAFE-PROLATE-BRIDGE without assuming Weil positivity. — OPEN / possible RH-STRENGTH.**
23. **SAFE-LIMIT-POINT. — OPEN.**
24. **SR-SAFE. — OPEN.**
25. **RDI link theorem \(\Rightarrow\lambda_n\ge0\). — OPEN / RH-STRENGTH.**

    It is not enough to reach a "safe" object: one must prove, with full normalizations and limits,
    that its safety implies Li's one-sided inequality for each index.

    The short triage is recorded in `fragments/OMEGA7_CARRIL_B_TRIAGE.md`. The current conclusion is
    to suspend this lane as a priority: there is not yet a literal bridge RDI \(\Rightarrow\lambda_n\ge0\)
    nor RDI \(\Rightarrow\) reality of zeros; BTG and GAP-Z remain open infrastructure, not a
    sign mechanism.

### Cross-cutting controls that must accompany any lane

26. **No-go audit by class, not as a universal veto.** Each no-go only eliminates the class it
    actually covers. No no-go can be used to abandon a statement for being equivalent to RH.
27. **Bibliographic comparison by mechanism.** Determine which part is known and isolate exactly
    the new identity or inequality that must be proved.
28. **Symbolic proof before numerical inference.** Computations serve to discover and falsify; closure
    requires a uniform proof.
29. **Explicit order of limits.** Every theorem must declare dependencies on \(n,N,L,X,\varepsilon\)
    and the order in which regulators are removed.
30. **Dependency ledger.** Every closed obligation must point to the exact lemma that proves it and
    cannot depend directly or indirectly on the same conclusion except within a declared equivalence
    whose useful direction has an independent proof.

## Main decision

It is not advisable to keep accumulating formulas around LP+IDENT. The review also discovers that the
prime target used to organize part of paper 36 was unnecessarily strong. From the exact split

\[
\lambda_n=\lambda_n^{\rm arch}+\lambda_n^{\rm prime}
\]

one obtains

\[
\Omega_7
\quad\Longleftrightarrow\quad
\lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch}
\quad\text{for all }n,
\]

not a domination in absolute value. The restart must prioritize the **one-sided, signed** lower
bound of the prime part. When \(\lambda_n^{\rm arch}\ge0\), this means controlling its negative
excursion; when \(\lambda_n^{\rm arch}<0\), it requires preserving a sufficient positive prime
contribution. Walls based on summing magnitudes or dominating \(|\lambda_n^{\rm prime}|\) do not close
this class.

RDI-ANCHOR remains the clearest candidate within the LP+IDENT route to carry the arithmetic
identification that must fail off line. It is not proved to be the only RH-strength step, because
LP/BTG and GAP-Z are also not closed in the correct control. That route remains a second lane, not a
prerequisite for every attack on \(\Omega_7\).

The claim "GAP-Z is neutral infrastructure" would be conclusive if proved for a class that includes a
construction with an off-line divisor. Today there is only finite evidence, and part uses
\(\mu_{\rm ref}\) instead of the true \(\mu_L\). For this reason a long campaign should not be invested
in GAP-Z, but it should not be declared irrelevant either.

The restart must first attack Li's minimal target and, in limited parallel, decide whether LP/GAP-Z
are provable infrastructure or additional burdens. Only if a genuine mechanism appears in the RDI
route should its downstream chain be resumed.

## Minimal state of the current route

The sufficient chain is

\[
\begin{aligned}
&\mathrm{LP}+\mathrm{IDENT}+\mathrm{RDP\!-\!SHELL}
+(\mathrm{PROLATE}+\mathrm{WEIL\!-\!TAIL})\\
&\Longrightarrow
\mathrm{SAFE\!-\!LIMIT\!-\!POINT}
\Longrightarrow
\mathrm{SR\!-\!SAFE}
\Longrightarrow
\Omega_7.
\end{aligned}
\]

Its corrected ledger is:

| Obligation | Status | Risk |
|---|---|---|
| BTG-DIV in the true \(\mu_L\) | **OPEN** | Outcome A evidence uses a finite approximation; neutral LP is not certified. |
| mu-free LP interface | **OPEN** | The clauses fixed in \(\mu_L\) were declared inadmissible, but the replacement was not built. |
| GAP-Z | **OPEN** | MESH and BND are bounded; ZERO is not. The absolute sum of layers is blocked. |
| RDI-ANCHOR | **OPEN / RH-STRENGTH candidate** | Convergence and coherence do not identify the Euler–Gamma limit. |
| RDP-SHELL and directional tails | **OPEN** | Cannot be estimated before the signed pairing. |
| SAFE-PROLATE-BRIDGE | **OPEN** | High risk of reintroducing Weil positivity. |
| \(\Omega_7\) | **OPEN / RH-STRENGTH** | It is RH via Li. |

The original candidate E79.6 — single-signedness of a finite cloud — is not the canonical target. It
was weakened by retractions and later phases. The current version must be formulated in just one of
these equivalent coordinates:

\[
\mathrm{RDI\!-\!ANCHOR}
\sim
\mathrm{DIRECT\!-\!BORDERED\!-\!ANCHOR}
\sim
\mathrm{LOCAL\!-\!COVARIANT\!-\!IDENT}
\sim
\mathrm{STIELTJES\!-\!IDENT}.
\]

TRUE-DIVISOR-IDENT is stronger and should not be chosen if a safe identification of smaller scope
suffices.

## Stage I — repair the map to attack RH

This stage does not need a new phase.

### I.1 Canonical register of objects

Fix a single definition for:

\[
\delta_N^{\rm ref},\quad
\delta_N^{\rm arch},\quad
\mu_L,\quad
\mu_{\rm ref},\quad
\mathrm{ZERO},\quad
C_{\rm core},\quad
\mathrm{RDI\!-\!ANCHOR},\quad
\mathcal C_{\rm Euler}.
\]

Each definition must contain domain, normalization, order of limits and dependence on \(L,N,z\). No
theorem may use \(\delta_N\) or \(\mu\) without a superscript or domain.

### I.2 Mathematical errata of paper 36 — COMPLETED

Separate the repairs from the proof frontier:

- withdraw H2's compact extension;
- correct H6, keep \(|\kappa|\) and label tail domination as open;
- rewrite \(\Omega_4\) with the two whitenings;
- downgrade \(\Omega_5\) to continuity for fixed \(N\);
- withdraw the envelope that isolates \(\sum_\rho(1-1/\rho)^n\);
- correct the sign and boundary term of the Laguerre integration by parts;
- restore \(\frac{\gamma-1}{2}n\) in the envelope asymptotics and restrict the \(\log n\) bound to \(n\ge2\);
- downgrade sampling, saturation and cascade to conditional results;
- correct the application of X3 to a negative-norm class.

These repairs are already incorporated in paper 36. They do not close \(\Omega_7\), but they leave its
frontier correctly typed and avoid supporting the new proof on false lemmas.

### I.3 Precedence register

Create a table claim \(\to\) status \(\to\) proof \(\to\) correction \(\to\) dependencies. The closure
label will never be the source of truth. This prevents a later phase from inheriting the withdrawn
QED from phase 65, E78.154, the proxy of insufficient precision, or the incorrect definition of
mean(d).

## Stage II — direct attack on Li's one-sided target

### II.1 Unambiguous definition

Fix the arithmetic continuation via the paired limit

\[
\lambda_n^{\rm prime}
=
\lim_{\varepsilon\downarrow0}
\left[
\sum_{k=1}^n
\binom nk\frac{(-1)^{k-1}}{\varepsilon^k}
-
\sum_{m\ge2}\frac{\Lambda(m)}{m^{1+\varepsilon}}
L_{n-1}^{(1)}(\log m)
\right]
\]

or with a finite-part symbol that declares exactly the same procedure. The bare boundary sum cannot
be manipulated as absolutely convergent. Every integration by parts must keep together the
cancellation that defines the continued value.

With \(f_{n,\varepsilon}(y)=y^{-1-\varepsilon}L_{n-1}^{(1)}(\log y)\), the polar term is not a formal
abbreviation: it satisfies

\[
\sum_{k=1}^n\binom nk\frac{(-1)^{k-1}}{\varepsilon^k}
=
\int_0^\infty L_{n-1}^{(1)}(x)e^{-\varepsilon x}\,dx
=
\int_1^\infty f_{n,\varepsilon}(y)\,dy.
\]

This identity is what must be preserved when passing to Stieltjes form and integrating by parts.

The exact goal will be

\[
\boxed{
\lambda_n^{\rm prime}+\lambda_n^{\rm arch}\ge0
\quad(n\ge1)
}
\]

This is the only global target. For indices with \(\lambda_n^{\rm arch}\ge0\), it can be rewritten as

\[
(\lambda_n^{\rm prime})_-
\le\lambda_n^{\rm arch}.
\]

For this split, the sign of the archimedean part can be closed:

\[
I_-:=\{n\ge1:\lambda_n^{\rm arch}<0\}=\{1,2,\ldots,7\}.
\]

Indeed,

\[
\lambda_n^{\rm arch}
=1-\frac n2(\gamma+\log(4\pi))
+\sum_{\substack{r\ge1\\r\ {\rm odd}}}
\left[\left(1-\frac1r\right)^n-1+\frac nr\right].
\]

If \(d_n=\lambda_{n+1}^{\rm arch}-\lambda_n^{\rm arch}\), then

\[
d_{n+1}-d_n
=\sum_{r\ {\rm odd}}\frac{(1-1/r)^n}{r^2}>0.
\]

An interval evaluation of the exact formula gives \(d_3\in(0.0062,0.0063)\), \(\lambda_1^{\rm arch}\in(-0.555,-0.554)\), \(\lambda_2^{\rm arch}\in(-0.875,-0.874)\), \(\lambda_7^{\rm arch}\in(-0.356,-0.355)\) and \(\lambda_8^{\rm arch}\in(0.020,0.022)\). By discrete convexity, the sequence increases from \(n=3\) on and does not become negative again after \(n=8\). For \(n=1,\ldots,7\) the original lower bound must be certified; there a positive prime contribution is necessary.

### II.2 Decomposition by negative excursion

Use the representation that preserves the sign of the Laguerre kernel before estimating. With

\[
f_{n,\varepsilon}(y)
=y^{-1-\varepsilon}L_{n-1}^{(1)}(\log y),
\]

the corrected identity, with the lower boundary included, is

\[
\lambda_n^{\rm prime}
=
\lim_{\varepsilon\downarrow0}
\int_1^\infty
(\psi(y)-y+1)f'_{n,\varepsilon}(y)\,dy
=
\lim_{\varepsilon\downarrow0}
\left[-n+
\int_1^\infty(\psi(y)-y)f'_{n,\varepsilon}(y)\,dy\right].
\]

The target is

\[
\lim_{\varepsilon\downarrow0}
\int_1^\infty
(\psi(y)-y+1)f'_{n,\varepsilon}(y)\,dy
\ge-\lambda_n^{\rm arch}.
\]

On the complement of \(I_-\), the same inequality only controls the negative part. The integral of
\(|\psi-y+1|\,|f'_{n,\varepsilon}|\), the sum of shell norms, and symmetric majorants are not the
minimal target and the known estimates do not reach it. However, they are not forbidden: if an
absolute bound of sufficient RH-strength is proved, that too will close \(\Omega_7\). The one-sided
priority only avoids imposing unnecessary additional difficulty.

### II.3 Mandatory falsifiers

Before requiring an arithmetic falsifier, a class \(\mathcal C_{\rm Euler}\) of completed objects \(F\)
must be defined, each with Dirichlet coefficients, Gamma factor, functional equation, continuation,
and a common rule that produces

\[
F\longmapsto
(\lambda_{n,F}^{\rm arch},\lambda_{n,F}^{\rm prime}).
\]

Only within that class does it make sense to claim that the same lemma holds for \(\zeta\) and fails
off line. A quartet planted without compatible arithmetic data proves sensitivity on the zero side,
but does not deductively falsify a Euler–Gamma inequality.

Once the class is built, a candidate lemma must distinguish three situations without reading zero
positions:

1. \(\zeta\)'s arithmetic data, where it delivers the lower bound;
2. a member of \(\mathcal C_{\rm Euler}\) with an off-line quartet, where the negative excursion grows
   geometrically and the lemma fails;
3. an on-line control, where it forbids neither the positive oscillations nor the sum of squares.

If the lemma also holds for the off-line control, it cannot close \(\Omega_7\). If its hypothesis is
equivalent to real-rootedness, that hypothesis becomes a new RH-strength obligation: it must be proved
independently from the arithmetic structure and cannot be assumed.

### II.4 Exit gate

This lane continues only if it produces one of these objects:

- a new signed identity that delivers the exact lower bound without absolute values;
- a one-sided inequality stable under the boundary limit;
- an arithmetic variational principle whose hypothesis is verifiable from Euler–Gamma and fails
  structurally off line.

A numerical envelope bound, an adjusted exponent, or positivity for finite indices do not justify a
new phase.

## Stage III — H0 attribution proof for LP+IDENT

Before attacking the discriminant, one must decide which parts are really neutral.

### III.1 Neutrality of LP

Formulate an abstract class \(\mathcal C_{\rm LP}\) that contains both the zeta construction and an
off-line control and that uses only:

\[
H_L=D_L+B_L,\qquad
D_L(n)=\log(1+|n|)+O_L(1),\qquad
B_L\ \text{bounded},
\]

plus explicit hypotheses of compactness and source.

The goal is not to measure disks, but to prove or refute:

\[
\mathcal C_{\rm LP}
\Longrightarrow
\|A_N(\mu_L)^{-1}b_N\|\longrightarrow\infty.
\]

There are three possible outcomes:

1. it is proved for every \(\mathcal C_{\rm LP}\): LP is neutral;
2. a counterexample appears within \(\mathcal C_{\rm LP}\): the formulation is false;
3. the proof needs an arithmetic property that separates the control: LP also carries difficulty and
   exclusive attribution to IDENT is refuted.

Substituting \(\mu_L\) by \(\mu_{\rm ref}\) in the conclusion is not accepted.

### III.2 Neutrality of GAP-Z

Start only from the proved identity

\[
g_{N+2}-g_N
=
\mathrm{ZERO}+\mathrm{MESH}+\mathrm{BND},
\]

with the known bounds for MESH and BND. The exact problem is a signed, locally uniform bound for
ZERO.

A dichotomy must first be proved:

\[
\begin{cases}
\mathrm{ZERO}\text{ is controlled from axioms shared by both builds},&
\text{GAP-Z neutral};\\
\mathrm{ZERO}\text{ requires a specific Euler identity},&
\text{GAP-Z carries part of the discrimination}.
\end{cases}
\]

Forbidden:

- summing shell magnitudes before canceling;
- using a signature that separates the builds as a convergence assumption;
- inferring a law from an adjusted exponent;
- carrying over to the limit a mesh of finite \(N\)'s.

This stage must be a triage: if no short abstract theorem or counterexample appears, GAP-Z stays open
and is suspended. No further cascade of proxies is opened.

### III.3 Attribution result

Only after III.1–III.2, via a build-neutral theorem or a counterexample in the declared classes, can
one of these statements be asserted:

\[
\boxed{\text{all the force is in IDENT}}
\qquad\text{or}\qquad
\boxed{\text{the force is distributed or the route contains an error}}.
\]

H0 guarantees at least one RH-strength or false step. It does not guarantee exactly one while the other
steps are not proved.

## Stage IV — fix the single RDI target, if it survives attribution

If attribution leaves IDENT as the separator, freeze all its coordinates but one. The recommendation
is to use the covariant core defect because:

- it preserves the correct outer factor;
- it avoids dividing on the singular curve;
- it keeps the full Gamma–Euler source;
- it is formulated in \(\Re s>1\), where the prime side converges absolutely;
- it admits an off-line falsifier within a typed arithmetic class.

This stage does not authorize a new reformulation of the anchor. It only continues if there is
already an identity or inequality that supplies an estimate missing in the previous coordinates. In
that case, the minimal statement must have this logical form:

\[
\textbf{ARITHMETIC-CORE-IDENT:}\qquad
C_{{\rm core},L,N}(s)
\longrightarrow
0
\]

locally on a safe set, with a written order of limits and a derivative if propagation needs it. The
name is provisional; the final document must write the full formula, not hide it behind an acronym.

The theorem must satisfy five conditions:

1. the left-hand side is computed from finite CCM data without zero positions;
2. its vanishing is derived from a Euler–Gamma identity in absolute convergence, not postulated;
3. the identity preserves conjugation, transversal support and linear multiplicity;
4. the off-line arithmetic control of the declared class fails by a structural computation, not an
   adjusted threshold;
5. the proof does not use Weil positivity, real-rootedness, a metric adapted to roots, or an absolute
   sum of prime contributions.

Proving this statement will have RH-strength. The goal is not to make it "technical", but to find a
new arithmetic reason why it is true.

## Stage V — search for mechanism, not coordinate

Three candidate classes currently identified, with no claim of exhaustiveness, justify new work.

### V.A Global cancellation identity

Look for an involution, coboundary or functional relation over the full set of prime cells that makes
the defect vanish after the correct pairing:

\[
\sum_{p^k}\mathcal J_{p^k}(s)
\quad\text{is globally reorganized before taking}\quad |\cdot|.
\]

Per-prime positivity or cell-by-cell matching does not work. The mechanism must be non-local and
retain the archimedean and boundary terms.

### V.B Signed phase→current transport

Construct a theorem that transforms arithmetic phase information into the covariant current without
going through an average:

\[
\text{Euler data}
\Longrightarrow
\text{signed cancellation of the core}
\Longrightarrow
\text{safe identification}.
\]

It must exceed the already-closed Tauberian/local classes and distinguish \(\zeta\) from the off-line
control within a typed class.

### V.C External geometry

Only reopen the geometric route if an independent object with diagonal, polarization and spectral
reader is built first. Defining the star, metric or correspondence from \(\Xi\)'s divisor is not
allowed. Without a new object, returning to Hodge/Lefschetz would repeat RH9 and phases 39–45.

The recommended priority is V.A, starting from its direct one-sided version from Stage II. It is the
currently specified direct route that uses the already-isolated Euler–Gamma structure without
requiring a nonexistent geometry or an average.

## Stage VI — bibliographic novelty gate

Before developing a candidate lemma:

1. write the statement without internal terminology;
2. identify its classical ingredients;
3. search primary sources by formula and mechanism;
4. compare hypothesis and conclusion, not just keywords;
5. record whether it is known, a known combination, a real variant, or new.

Until this gate is passed, every "new mathematics" label remains **UNCERTIFIED NOVELTY**.

## Stage VII — falsification before a phase

No new phase is opened until there is a candidate that passes:

| Test | Requirement |
|---|---|
| Off-line | Must fail on an off-line arithmetic control within a typed class; an isolated planted quartet only gives heuristic falsification. |
| On-line | Must be compatible with the on-line control without using its zeros. |
| Information | Must preserve conjugation and linear multiplicity. |
| Limits | Must declare and justify the order \(N\), \(L\), boundary. |
| No-go | Cannot be tautological Gram, finite positivity, single gap, smoothing, pseudoinverse, a moment level, or a product of traces. |
| Independence | May prove and use a condition equivalent to RH, but not assume it: must derive it independently from the allowed data. |
| Novelty | Must pass the bibliographic comparison by mechanism. |

If a gate fails, it is recorded in this dossier; no new phase directory is opened. A new phase is only
justified when a new mathematical degree of freedom appears, not another name for the anchor.

## Recommended order of effort

1. **Completed:** correct the ledger, the prime target, paper 36 and the separation of objects.
2. **Completed:** fix the one-sided arithmetic formula with all its continuation and boundary terms.
3. **Completed:** close with rational intervals the seven indices of the exceptional archimedean
   range.
4. Pass the bibliographic gate for the formula and for each proposed signed mechanism.
5. Attack A0, the uniform Mellin–Laguerre tail, and then A1, the global signed core of points
   12–13.
6. Simultaneously prove the boundary limit, the signed tail, and the uniformity in \(n\).
7. If a provable absolute bound of RH-strength appears, pursue it: even if it is stronger than the
   minimal target, it would equally close \(\Omega_7\).
8. **Completed:** carry out a short triage of LP/GAP-Z. Result: lane B does not yet supply a literal
   sign mechanism; it remains suspended unless an RDI-to-Li or RDI-to-reality bridge appears.
9. Fix a single RDI-ANCHOR/core formula if lane B produces an explicit link to Li.
10. Return to downstream tails and bridges only as part of a complete chain up to point 25.
11. Assemble the finite and infinite ranges and apply Li's criterion.

This sequence concentrates effort on the first still-open statement that can deliver the global sign.
It does not exclude a route for being stronger than or equivalent to RH; it requires that every route
arrive, via a proof, at the final inequality.
