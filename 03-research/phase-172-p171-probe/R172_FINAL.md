# R172 FINAL — \(P_{171}\) as a probe for row D


## 0. Verdict

The working hypothesis is **REFUTED in its literal reading**: there is no
single row `[F]`. Several global formulations of D reuse the same bridge,
and the finite chain of phases 166--170 further uses a second structure
not derivable from mere multiplicative integrality.

The correct result is the following.

> **Dependency classification theorem — PROVED.** When transporting
> \(P=P_{171}\) through this concrete chain for D, every purely
> harmonic, variational, or operator-theoretic piece survives under its
> hypotheses. Every observed transport failure belongs to one of these
> two families:
> \[
> \boxed{\text{analytic self-duality centered at }1/2}
> \qquad\text{or}\qquad
> \boxed{\text{exact additive geometry of }\mathbb N}.
> \]
> The first comprises the functional equation, the Gamma factor, the poles,
> the quartets, and the explicit formula. The second comprises the
> integer comb, \(n\mapsto n+1\), Poisson--Euler--Maclaurin, the
> ordinary hyperbola, and the PC--Tate identities. For \(\zeta\), both act on
> the same lattice and couple. Generalized Euler/integrality or the FE separately do not force
> the sign.

Thus, the statement "the only category `[F]` is FE" is false. The table
identifies as a **candidate minimal coupling — ARGUED**, without proving
sufficiency or logical minimality,

\[
 \boxed{\text{ordinary Euler over }\mathbb N
 \quad\wedge\quad
 \text{exact Poisson/FE for that same lattice}.}       \tag{0.1}
\]

Neither RH nor a new positivity window for \(\zeta\) is proved.

## 1. Audit convention

A row receives exactly one class:

- `[V]`: the full statement holds verbatim for the datum of \(P\), or it is
  an abstract theorem that does not claim to identify its measure with the zeros;
- `[F]`: the full statement does not transport; the individual
  hypothesis of \(\zeta\) that is missing is indicated;
- `[?]`: the corpus does not decide.

The table has zero `[?]` entries. When a theorem mixes an abstract
`[V]` part with an arithmetic `[F]` identification, it is split into two
rows. This avoids attributing a zero measure to \(P\) just because the
operator algebra survives.

The probe's datum is R171_FINAL §§3--6:

\[
 N_P(x)=cx+O(x^{83/208}),\qquad
 \zeta_P(s)=\zeta(w)F(w)G(w),\qquad
 w={s-3/8\over5/8},                                    \tag{1.1}
\]

with integer multiplicities and zeros at \(\Re s=11/16\). The symmetry
inherited from \(\zeta(w)\) is centered at \(11/16\), not at \(1/2\).
The system carries no Gamma factor, no self-dual poles, nor a Poisson
formula for its generalized integers.

## 2. Full table

| Link | Class | Label | Exact reason and source |
|---|:---:|---|---|
| E1: \(\forall T,\lambda_T^W\ge0\) as the Weil criterion | **[F]** | **PROVED** (diagnosis) | The full form of P47 uses \(m_\zeta\), the poles \(0,1\), and the explicit formula centered at \(1/2\). Substituting only \(P\)'s comb defines a different form, but not \(\zeta_P\)'s Weil criterion. ROW-D-REDUCED §1 E1; P47 `eq:W`. |
| E2: primitive form as a variational form | **[V]** | **PROVED** | The compression by the two Tate moments and the variational minimum are defined for any locally finite comb once the archimedean term is fixed. P47 §1. |
| E2: global equivalence with the system's RH | **[F]** | **PROVED** (diagnosis) | The Bombieri--Weil equivalence uses the explicit formula and symmetry about \(1/2\). ROW-D-REDUCED §1 E2. |
| E3 and Theorem Z: certificate \(\leftrightarrow\) smoothing of the zeros | **[F]** | **PROVED** | Identifying the certificate with the zero measure is \(\zeta\)'s explicit formula. \(P\) lacks that FE/completion. P47 `thm:Z`, `cor:RH`. |
| E4: finite weight vector in the convex set \(\mathcal V_T\) | **[V]** | **PROVED** | Local finiteness leaves only finitely many atoms below \(e^{2T}\); the convex reduction is finite and uses no zeros. P47 `prop:finite`, `prop:uniform`. |
| E5: \(\lim_{T\to\infty}\lambda_T^A\ge0\leftrightarrow\mathrm{RH}\) | **[F]** | **PROVED** (diagnosis) | The formal limit can be written, but identifying it with RH again uses Weil/FE. ROW-D-REDUCED §1 E5; P47 `cor:margin2`. |
| E6: adelic Hodge-index as a criterion | **[F]** | **PROVED** (diagnosis) | There is no adelic square for \(P\); any analogous detector is equivalent to its own RH. P46 Cor. 17.11 and Thm. 17.21; ROW-D-REDUCED §1 E6. |
| Parity and Schur form | **[V]** | **PROVED** | It is algebra of a closed even form plus two functionals and a rank-two perturbation. P47 `thm:parityschur`. |
| \(2\times2\) polar capacity | **[V]** | **PROVED** | The identity \(\mathfrak G_T=S_T^{Sch}+J\) is functional-analytic. P47 `prop:polarcap`. It does not identify \(\zeta_P\)'s poles. |
| Abstract skeleton of KEP1(i--ii), KEP2, and KEP3(a) | **[V]** | **PROVED** | Fourier--Bochner, duality, and extension hold for abstract data \(g\). P47's specialization uses \(g_\zeta\); identifying a natural \(g_P\) belongs to the following [F] row. P47 `thm:KEP1`--`thm:KEP3`. |
| KEP1(iii), KEP3(b): atomic solution = zeros and equivalence with RH | **[F]** | **PROVED** | The identification uses Theorem Z and \(\zeta\)'s explicit formula. P47 `thm:KEP1(iii)`, `thm:KEP3(b)`. |
| Abstract Theorem M: doubly exponential collapse | **[V]** | **PROVED** | It is a density/Nyquist phenomenon for completed multisets with the required symmetry. R162_2401b; Paper 48 `thm:M`. |
| Theorem M applied verbatim to \(P\) | **[F]** | **PROVED** (diagnosis) | \(P\)'s known zeros do not form the real multiset symmetric about \(1/2\). Recentering at \(11/16\) changes the polar term, Gamma, and the form. |
| Abstract `finZ` | **[V]** | **PROVED** | It is a harmonic theorem for every finite real symmetric multiset and a flat-top weight. P47 `thm:finZ`. It does not claim that \(P\)'s ordinates produce such a multiset. |
| Theorem R / identification R164 | **[V]** | **PROVED** | The conditional theorem holds: positivity outside \(\mathbb N\), the gap, FE, Gamma, and exact poles force \(f=\zeta\). R164_401 Theorem R; R164_190. \(P\) falls outside due to its hypotheses. |
| Cellular decomposition and \((\star_{\rm cell})\) | **[F]** | **PROVED** as a transport failure; **OPEN** as a sign for \(\zeta\) | The \(P_j,N_j\) use quartets about \(1/2\). In \(\zeta\)'s witness, \((\star_{\rm cell})\) is equivalent to RH. R163_401 §4.7--4.8 and Rem. 4.8a. |
| Tail condition (TC) | **[F]** | **PROVED** (diagnosis) | It is the tail of \(-\zeta'/\zeta\) recomposed with residues, Gamma, and the cutoff \(e^{2T_c}\). It does not exist verbatim for (1.1). R164_000 §§0--1. |
| Exact identity behind \((WS^*)\) | **[F]** | **PROVED** (diagnosis) | R167_101 Thm A applies Weil--Guinand to \(\zeta\), with Gamma, pole, and quartets. |
| Poisson majorant / amplification ceiling | **[V]** | **PROVED** | It is Cartwright for \(\Phi\ge0\), with no arithmetic. R167_101 Thm C. |
| Dualization, Parseval, Bernstein, and mean value | **[V]** | **PROVED** | They are identities for discrete exponential sums. R167_102 L0--L1, Prop. 1, and Thm A. |
| Sieve blindness | **[V]** | **PROVED** | It only uses class-level data; \(P\) precisely proves it cannot give the sign. R167_102 Thm B; R167_103 Thm S. |
| Ladder/Landau | **[V]** | **PROVED** | A uniform saving implies a zero-free region for the corresponding series; applying it remains circular. R167_102 Thm C. |
| Vaughan/Heath--Brown on the ordinary hyperbola | **[F]** | **PROVED** for the failure; general scope **ARGUED** | It uses congruences, \(mn\le X\), and the ordinary lattice. \(P\)'s factorization gives no additive order. R167_102 Thm D. |
| Jet hierarchy verbatim | **[F]** | **PROVED** | Requires quartets around \(1/2\). R166_201 Thms 1.1--1.4. |
| Recentered jets and \(k=1\) blindness/\(k=-1\) wall | **[V]** | **PROVED** | Recentered on any axis, it is a geometric identity that does not orient the sign. R166_201 Cor. 1.4. |
| Full arithmetic construction of the ledger \(Z_N=S_N-C_N\) | **[F]** | **PROVED** (diagnosis) | For P, \(S_{P,N}\) can be canonically defined from its counting measure and \(C_{P,N}\) from its density \(c\). What does not transport is its Poisson--Euler--Maclaurin identification with the ordinary lattice, nor the exterior coupling. R170_888 §§0--2; audit R172 round 3. |
| Minimality identity, given the operators | **[V]** | **PROVED** under REG/C1 | It is Hellmann--Feynman and operator algebra. R170_888 §§2--3. |
| Parity wall | **[V]** | **PROVED** | The minimal derivative is quadratic/even and the linear/odd EM residue does not inherit a sign. R170_888 §§3--5. |
| PC--Tate collision as an operator identity | **[V]** | **PROVED**, conditional on the assembly | The exact recombination preserves collars, ports, and the Tate factor, but gives no sign. R170_900 §§0--3. |
| Arithmetic realization PC--Tate | **[F]** | **PROVED** (diagnosis) | It uses the ordinary hyperbola, Poisson, Gamma, the exterior port, and Tate in a comparison. P admits a continuum \(C_{P,N}\), but not that full coupling nor a compatible contact. R170_900 §§1--3. |

## 3. Mandatory attempt to repair each `[F]`

The `[F]` rows belong to four groups; in each group a
\(P'\) was tried.

| Failure group | Candidate \(P'\) | Result |
|---|---|---|
| FE, Gamma, poles, Theorem Z, zero-KEP, TC, and quartets | Try to impose \(\zeta\)'s FE on P | **NO-GO only under the full Theorem R package:** exact agreement with \(\zeta\)'s comb on \([1,X)\), positivity outside \(\mathbb N\), Gamma, poles/residues, and finite order force \(P'=\zeta\). It is not claimed that every partial modification of P falls under the theorem. |
| FE only | Davenport--Heilbronn, Epstein, \(f_\chi\) | **NO-GO for downgrading to [V]:** they keep an FE and may have zeros off the line, but lack \(\zeta\)'s exact positive Euler product, or change Gamma/conductor. FE alone does not transport D's datum. |
| Symmetry axis only | Recenter \(P\) at \(11/16\) | **NO-GO:** it produces geometric identities, but changes the critical line, Gamma, the polar term, and the Tate moments. It is not the verbatim step. |
| Additive lattice, ledger, and hyperbola | Identify the generalized integers with \(\mathbb N\) and keep the exact Euler convolution | **NO-GO, PROVED:** the Eratosthenes induction identifies the system with the ordinary one; R169_101 §6. The repair removes the falsifier. |

No attempt downgrades an `[F]` row to `[V]`.

## 4. Proved scope of the classification

The `[V]` rows are proved in the corpus without identifying the datum with the
zeros of a completed function: finite convexity, Schur under its
hypotheses, abstract Bochner--Kreĭn, Cartwright, Parseval, Landau,
recentered jets, and the operator identities. The `[F]` rows split by
the missing hypothesis: some need the self-dual explicit formula centered
at \(1/2\); others need Poisson--Euler--Maclaurin on the ordinary
additive lattice.

This proves the taxonomy for the chain examined. It does not prove that the
two doors are sufficient to obtain the sign, that they are logically
minimal among all possible mathematics, nor that every `[F]` is a
formal consequence of a single identity. Those statements remain
**ARGUED**, not `PROVED`.

## 5. Exact candidate and status of the success criterion

The only candidate that preserves all the interaction located by the
table is the literal residue of R170_900 (1.2):

\[
\begin{aligned}
 \mathfrak R_{\rm rem}(M,N,T;F)={}&
 \operatorname{Re}(h,P[
   \mathcal D_{\rm PC}-\mathcal G_{A_M+L_M}(Z_N)]F)\\
 &-\rho\operatorname{Re}[(P\dot S_N^*Ph,b)-g],
 \qquad Z_N=S_N-C_N.                                   \tag{5.1}
\end{aligned}
\]

Here \(\mathcal D_{\rm PC}\), \(S_N,C_N,A_M,L_M,h,P,b,g,\rho\), and the order
of limits are exactly those of R170_888 and R170_900; none is redefined.
The concrete proposal is:

> **R172-candidate — OPEN.** Under REG/C1 and at a first contact, prove
> \[
> \liminf_{N\to\infty}\liminf_{M\to\infty}
> \mathfrak R_{\rm rem}(M,N,T;F)\ge0.                    \tag{R172-cand}
> \]

R170_900 proves identity (5.1), but declares its sign and vanishing
open and does not prove that (R172-cand) alone excludes first contact.
Hence an orientation proposition exactly connecting that sign to D is
still missing.

Audit of the three requested criteria:

1. For \(P\), the interior pair \((S_{P,N},C_{P,N})\) exists, but not
   the exterior/FE totalization nor the coupled ordinary hyperbola; for
   Davenport--Heilbronn the positive Euler comb is missing. This proves
   **inapplicability/separation by hypothesis**, not falsity of the
   inequality. The "failure" criterion in the counterexample sense is not
   satisfied.
2. (R172-cand) is not literally RH: it asks for a sign before
   recombining. This condition is indeed satisfied.
3. Paper 47 proves \(W_T\ge0\) after recombining for
   \(T\le\frac12\log5\); it does not prove the separate sign of (5.1). Hence
   there is not yet a proved case of (R172-cand).

**Phase verdict: PARTIAL.** The formal stopping condition "full table
with no `[?]`" was reached. The scientific success criterion of the goal was not:
a statement that is simultaneously false for both probes and has a
non-vacuous proved case is still missing. Presenting Paper 47's recombined
positivity as a case of (R172-cand) would be incorrect.

## 6. NO-GO for simultaneously repairing the three criteria

The second round tried two repairs: totalizing the probes via
Euler/FE defects and replacing the residue with a window statement using
the already-certified positivity. Both are closed within the class examined.

> **Proposition (window trilemma) — PROVED / NO-GO.** Let \(S_{T_0}\)
> be a statement whose value depends only on the Gamma/polar term and on
> the restriction to \((-2T_0,2T_0)\) of the explicit distribution. Then a
> positive case of \(S_{T_0}\) for \(\zeta\) cannot, by the mere
> existence of exterior zeros, be false for every off-line
> falsifier. If positivity is required on every window, Weil's criterion is
> recovered. If, in addition, exact positive Euler, FE, Gamma, poles, and
> local agreement are imposed, the identification theorem leaves only
> \(\zeta\).

**Proof.** R163_901 Theorem F builds, for each \(T_0\), an \(f_t\) with
\(\zeta\)'s FE, Gamma, and poles, zeros off the line, and
\(W_T^{f_t}=W_T^\zeta\) for every \(T\le T_0\). Hence a certified window
positivity does not by itself detect exterior zeros. Quantifying over all
\(T\), positivity of Weil's form is RH (R121_AT_CORPUS_ATLAS §3.1). Finally, under all
the precise hypotheses of R164_401 Theorem R — including comb agreement on
\([1,X)\), positivity outside \(\mathbb N\), Gamma, poles/residues, and
finite order — the object is identified with \(\zeta\). ∎

The additive repair via cancelling defects is also ruled out. If

\[
 Q_T(f;F)=W_T(f;F)+\Psi_T(F;E_f,P_f),
 \qquad E_\zeta=P_\zeta=0,\quad\Psi_T(F;0,0)=0,
\]

then \(Q_T(\zeta;F)=W_T(\zeta;F)\); requiring its sign for all \(T,F\)
is another way of writing RH. A sum of squares of \(E_f,P_f\) only measures
membership in the compatible domain and does not orient the PC--Tate
residue. This NO-GO does not prove that no future mathematics could
satisfy the three criteria; it proves that it is not obtained via local
data, cancelling defects, nor the corpus's current results.

The new input needed is located: a quantitative theorem that
builds and locates a negative witness from the Euler--Poisson decoupling,
or a sign law for (5.1) with a canonical totalization to both probes.
Neither is currently proved.

## 7. Round 3: localization and totalization

The last round examined the two outcomes §6 had not excluded.

**Localization.** Phase 106, `106_11_BILATERAL_PARITY_NEGATIVE_TEST_THEOREM.md`,
Theorem 1 and Corollary 2, prove that \(\neg\mathrm{RH}\) produces negative real
\(C_c^\infty\) tests in both parities. The support depends on the full divisor
and no universal window is given. R163_901 Theorem F shows that,
for every \(T_0\), there can be FE, Gamma, poles, and exterior zeros while
the data of every window \(T\le T_0\) agrees with that of \(\zeta\).
Hence the support theorem does not supply the required small case, nor does
it transport to P, which is not completed around \(1/2\).

**Totalization.** For a counting measure \(\nu\),
\(N_\nu(x)=cx+o(x)\), one does canonically define

\[
 S_{\nu,N}=\int_{[1,N]}x^{-1/2}\tau_{\log x}\,d\nu(x),
 \quad
 C_{\nu,N}=c\int_{[1,N]}x^{-1/2}\tau_{\log x}\,dx,
 \quad Z_{\nu,N}=S_{\nu,N}-C_{\nu,N}.                   \tag{7.1}
\]

This corrects the preliminary claim that P lacked a \(C_N\). However,
(7.1) does not determine the completion, the exterior port, nor the
Tate/contact coordinate of (5.1). R170_874 shows that, keeping the
interior data fixed, the exterior class can be varied; hence two
extensions agree on (7.1) and take different signs in the residue. Without
a new naturality axiom, the full totalization is not canonical.

**Round 3 verdict — NO-GO within the class examined.** No
non-vacuous case of the separate sign appeared. The parity wall of R170_888 also
prevents inheriting it from quadratic minimality. This result does not claim
universal impossibility; it identifies the new axiom or law that would need
to be built.

## 8. Consequence for D

\(P_{171}\) definitively closes routes based on counting regularity,
multiplicative semigroup structure, and integrality. Phase 172 locates two missing dependencies and leaves as an
**ARGUED** candidate their coupling over the same copy of \(\mathbb N\). Turning
that candidate into a validated inequality remains open.

## 9. Neutral audit

Two independent readings confirmed the table and rejected the first
closure attempt. A second round, with two builders and one auditor, proved the trilemma
of §6. A third round examined localization and totalization, corrected the
scope of \(C_N\), and confirmed the relative NO-GO of §7. Their objections were incorporated: Schur/capacity hypotheses,
the exact scope of Theorem R, the distinction between falsity and
inapplicability, and withdrawal of the assumed small case of (R172-cand). The `PARTIAL` verdict is
not editorial caution: it expresses that success criterion (i)/(iii)
remains unproved.
