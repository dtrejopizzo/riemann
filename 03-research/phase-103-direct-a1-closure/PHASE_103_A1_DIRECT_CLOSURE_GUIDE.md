# Phase 103: direct A1 closure guide

## Purpose

This phase begins at the narrowest exact direct formulation reached in
phase 102.  Its sole mathematical objective is to prove
\[
  \boxed{C_n(T_n)\ge 0\qquad(n\ge 8).}
  \tag{1}
\]

The index \(n=8\) already has a certified positive margin.  Therefore the
infinite task starts at \(n=9\).

No new reformulation counts as closure.  Phase 103 closes A1 only after a
proof of (1) for every \(n\ge8\), with every endpoint convention and every
uniform constant stated explicitly.

## Starting point inherited from phase 102

Put
\[
  N=n-1,
  \qquad
  G_N(u)=e^{-u}L_N^{(1)}(u),
  \qquad
  \omega_n(u)=G_N(T_n)-G_N(u).
  \tag{2}
\]

After the low interval, pole term, and archimedean terms are collected in
\(B_n^{\rm base}\), the direct certificate is
\[
  \boxed{
  B_n^{\rm base}
  +
  \sum_{T_8\le \log m\le T_n}
    \Lambda(m)\omega_n(\log m)
  \ge0.
  }
  \tag{3}
\]

The high-block coefficient is exact:
\[
  \Omega_n(m)
  =
  e^{-T_n}L_{n-1}^{(1)}(T_n)
  -e^{-\log m}L_{n-1}^{(1)}(\log m).
  \tag{4}
\]

The coefficient profile changes sign.  Thus neither
\(\Lambda(m)\ge0\), nor monotonicity of \(\psi\), nor coefficientwise
positivity proves (3).  The remaining theorem is an oriented compensation
theorem for the actual prime-power measure.

## First task: replace the lobe sum by one global correlation

Define
\[
  E(u)=\psi(e^u)-e^u.
  \tag{5}
\]

The lobe partition is useful for sign geometry, but it must not be used to
create independent local errors.  Sum all lobe partial-summation identities
before estimating anything.  Since
\[
  \omega_n'(u)=e^{-u}L_{n-1}^{(2)}(u),
  \qquad
  \omega_n(T_n)=0,
  \tag{6}
\]
global Stieltjes summation gives, with a fixed left/right endpoint
convention,
\[
\begin{aligned}
  &\sum_{T_8\le\log m<T_n}
    \Lambda(m)\omega_n(\log m)\\
  &\qquad=
  \int_{T_8}^{T_n}\omega_n(u)e^u\,du
  -E(T_8-)\omega_n(T_8)
  -\int_{T_8}^{T_n}
       E(u)e^{-u}L_{n-1}^{(2)}(u)\,du.
\end{aligned}
\tag{7}
\]

If a prime power lies at an endpoint, its jump must be assigned according
to the convention used in (3); the corresponding finite correction must be
written explicitly.  This bookkeeping is the first formal verification of
the phase.

Define the explicit reserve
\[
  Q_n
  =
  B_n^{\rm base}
  +\int_{T_8}^{T_n}\omega_n(u)e^u\,du
  -E(T_8-)\omega_n(T_8),
  \tag{8}
\]
and the oriented correlation
\[
  \mathcal R_n
  =
  \int_{T_8}^{T_n}
       E(u)e^{-u}L_{n-1}^{(2)}(u)\,du.
  \tag{9}
\]

Then the minimal direct theorem becomes
\[
  \boxed{\mathcal R_n\le Q_n\qquad(n\ge9).}
  \tag{10}
\]

The first deliverable of phase 103 is a complete algebraic derivation of
(7)--(10), including an endpoint table and a closed formula for \(Q_n\).
It must also prove directly that (10) is identical to (3), rather than a
stronger sufficient condition.

## Second task: determine the available reserve

Before bounding \(\mathcal R_n\), compute the size and sign of \(Q_n\).
The required output is a theorem of the form
\[
  Q_n=q(n,T_n)+q_8(n,T_7,T_8),
  \tag{11}
\]
where every term is an endpoint expression in Laguerre polynomials and the
already fixed finite arithmetic data below \(e^{T_8}\).

The analysis must establish:

1. an exact formula for \(Q_n\);
2. a rigorous lower bound for \(Q_n\), uniform in \(n\ge9\);
3. its true asymptotic scale under the chosen admissible cutoff \(T_n\);
4. a finite threshold separating direct verification from the uniform
   argument.

An estimate for the correlation is useful only after its scale is compared
with this reserve.  Any proposed bound whose leading cost exceeds the
leading reserve is to be rejected immediately.

## Third task: expose the oriented lobe geometry

Let
\[
  T_8=a_{n,0}<a_{n,1}<\cdots<a_{n,J_n}=T_n
  \tag{12}
\]
be obtained by inserting the zeros of \(\omega_n\), and let the zeros of
\(L_{n-1}^{(2)}\) provide the derivative-lobe partition for (9).

The required Laguerre analysis is:

1. locate all relevant zeros relative to \(T_8\) and \(T_n\);
2. determine the sign on every lobe;
3. give uniform bounds for lobe widths, extrema, and signed areas;
4. pair adjacent positive and negative lobes whenever the pairing preserves
   orientation;
5. isolate the initial and terminal unpaired pieces explicitly.

The target is not an absolute estimate involving
\(\int |E(u)L_{n-1}^{(2)}(u)|e^{-u}\,du\).  It is a signed comparison that
retains the alternating Laguerre geometry.

## Fourth task: prove an arithmetic transport theorem

The new mathematical step must control how the actual Chebyshev discrepancy
is sampled by consecutive Laguerre lobes.  A useful theorem would have one
of the following forms.

### Adjacent-lobe transport

Construct maps
\[
  \tau_{n,j}:J_{n,j}^{-}\longrightarrow J_{n,j}^{+}
  \tag{13}
\]
between a negative-cost lobe and a compensating positive lobe, together
with a Jacobian/kernel comparison, and prove a signed inequality for the
actual Stieltjes prime-power mass.  Summing the paired inequalities must
give
\[
  \mathcal R_n^{\rm paired}
  \le Q_n-\mathcal R_n^{\rm edge}.
  \tag{14}
\]

### Cumulative oriented discrepancy

Alternatively, construct a primitive \(W_n\) of the Laguerre kernel whose
sign at successive extrema is controlled, then perform a second summation
by parts.  The desired theorem has the shape
\[
  \int_{T_8}^{T_n}E(u)K_n(u)\,du
  \le
  \mathcal C_n(E,W_n),
  \qquad
  K_n(u)=e^{-u}L_{n-1}^{(2)}(u),
  \tag{15}
\]
where \(\mathcal C_n\) uses one-sided increments of \(E\), not
\(|E|\).  Its final upper bound must be at most \(Q_n\).

### Dirichlet-series positivity

A third possibility is to transform (3) into a finite Dirichlet-polynomial
identity and exhibit a positive quadratic or sum-of-squares structure that
is valid before any assertion about zero locations.  The transformation
must reproduce the precise cutoff and the coefficient (4); positivity of a
different extension does not suffice.

These are alternative constructions.  Only one complete theorem is
needed.

## Mandatory no-go audit

Every attempted proof must be tested against the following failures before
it is developed further.

1. **Termwise sign:** \(G_N(T_n)-G_N(u)\) changes sign.  Positivity of
   \(\Lambda\) is insufficient.
2. **Symmetric Chebyshev envelope:** replacing \(E\) by \(|E|\) discards the
   orientation and returns to the failed absolute-load route.
3. **Independent lobe estimates:** bounding every lobe separately loses
   the cancellations which define the problem.
4. **Zero-free regions or density alone:** any input compatible with one
   off-line zero cannot prove the full theorem.
5. **Finite verification without a uniform tail theorem:** computation of
   arbitrarily many indices does not establish (10) for all \(n\).
6. **Circular zero-side positivity:** a sum-of-squares representation
   obtained only after putting every zero on the critical line assumes the
   desired conclusion.
7. **Abstract extension theorems:** existence of some positive extension is
   irrelevant unless the extension is the arithmetic kernel occurring in
   (3).
8. **Equivalent restatement presented as progress:** equations (3), (10),
   the lobe balance, and \(s_n\ge d_n\) are coordinatizations of the same
   open theorem.  Moving among them does not close a subproblem.

## Work order

The phase should proceed in this order.

1. Prove the global telescoping identity (7) with exact endpoints.
2. Expand and simplify \(Q_n\) completely.
3. Determine the reserve scale and a rigorous lower bound.
4. Establish uniform Laguerre lobe geometry on \([T_8,T_n]\).
5. Formulate one precise oriented arithmetic transport lemma.
6. Test the lemma against explicit prime-power sums for a substantial finite
   range, using interval arithmetic only as diagnosis.
7. Prove the transport lemma uniformly.
8. Combine it with the reserve theorem to prove (10) beyond an explicit
   threshold.
9. Certify the remaining finite range exactly.
10. Substitute the result into the compact chain and state the resulting A1
    and Omega7 theorem.

Steps 1--4 are infrastructure.  Step 7 is expected to contain the genuine
RH-strength mathematics.  It must not be hidden inside an unproved
regularity, positivity, or uniformity assumption.

## Acceptance criteria for closure

A direct A1 proof is complete only if the final document contains all of
the following:

1. the exact definition and admissibility proof for every \(T_n\);
2. the exact identity connecting \(C_n(T_n)\) to (3);
3. the proof of the oriented theorem (10) for every \(n\ge9\);
4. explicit treatment of all boundary prime powers and cutoff jumps;
5. uniform constants and a proved threshold;
6. an exact finite certificate below that threshold;
7. a non-circularity audit showing where the prime number theorem, explicit
   formula, or zero information enters;
8. the already certified \(n=8\) base case;
9. the final deduction
   \[
     C_n(T_n)\ge0\ (n\ge8)
     \Longrightarrow
     \lambda_n\ge0\ (n\ge1)
     \Longrightarrow
     \mathrm{RH}.
   \]

## Source map

The phase 102 documents that define the starting point are:

- `196_A1_REMAINING_THEOREMS_CANONICAL_FORM.md` for the canonical A1 target;
- `217_N8_BASE_MARGIN_CERTIFICATE.md` for the base index;
- `219_MIXED_LAGUERRE_TELESCOPING_COLLAPSE.md` for the collapsed kernel;
- `226_DIRECT_TELESCOPED_PRIME_COEFFICIENT_CERTIFICATE.md` for the exact
  prime-power coefficients;
- `298_LAGUERRE_LOBE_BLOCK_COMPENSATION_GATE.md` for oriented lobe balance;
- `299_LOBE_BLOCK_PARTIAL_SUMMATION_GATE.md` for local summation by parts;
- `313_DIRECT_A1_TERMWISE_SIGN_OBSTRUCTION.md` for the coefficientwise
  no-go;
- `320_TAIL_LOBE_ONE_SIDED_ENVELOPE_CRITERION.md` for the equivalent
  tail-lobe orientation;
- `329_DIRECT_A1_ORIENTED_CHEBYSHEV_MINIMAL_THEOREM.md` for the minimal
  remaining direct theorem.

## Status at the opening of phase 103

The direct route is alive and has been reduced to one exact inequality:
\[
  \boxed{\mathcal R_n\le Q_n\qquad(n\ge9).}
\]

The algebraic reductions, the base index, and the termwise-sign audit are
closed.  The oriented arithmetic transport theorem is open.  Proving it
with sufficient uniform margin closes direct A1; completing the already
established compact chain then closes Omega7.
