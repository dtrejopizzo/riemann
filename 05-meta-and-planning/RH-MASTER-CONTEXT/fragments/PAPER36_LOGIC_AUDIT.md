# Logic audit of `36-obstruction-ledger`

## Verdict

The manuscript does not prove RH: its own Step 5, ARP-P, remains open and is equivalent to RH. The audit **does confirm**, with the classical interface caveats noted below, the formal architecture

\[
 \mathrm{ARP\!\!\text{-}P}\Longleftrightarrow\mathrm{RH}.
\]

This is a useful conditional equivalence: if ARP-P were established, the Pick–Nevanlinna bridge removes the non-real poles and gives RH; under RH, the channels are Cauchy transforms of positive measures. It does not turn arithmetic positivity into something weaker than RH.

The broader claim that "everything except Step 5" is proved in the sense suggested by the summary, the status map and the epilogue is not confirmed. There are auxiliary lemmas and theorems presented as closed that are only sketches, conditional consequences, finite computations, proposals, or uses of a realization constructed outside the manuscript. Some failures are of concrete logical typing, not merely missing detail.

Convention of this audit:

| Mark | Meaning |
|---|---|
| Confirmed | The conclusion follows from the stated hypotheses, with an identified classical input. |
| Conditional | Correct only after adding a hypothesis not proved here. |
| Partial | Covers a finite, separated, large-height, almost-everywhere regime, or a bounded class; not the global claim. |
| Not confirmed | A proof is missing, a result declared a sketch is used, the quantification is not formalized, or there is a type mismatch. |

In particular, "closed in the manuscript" is not equivalent to "confirmed by this audit".

## Scope and correct stratification

There are four levels that must not be interchanged.

1. **Step 1–15 chain.** Constructions and logical equivalences on the target function already defined via the zeros.
2. **H0–H8.** Exploratory decomposition of Step 5. Its subcases are not Steps and do not prove ARP-P unless they cover all the quantifiers.
3. **\(\Omega\) chain.** Re-expressions of the terminal difficulty. Several equivalences are obtained by passing through RH; they are not a direct arithmetic deduction.
4. **Tower/realization, sampling, cascade and closure routes.** Candidate certificates or auxiliary analyses. They must not be promoted to a proof of Step 5.

The first premise not derived from the central chain is exactly ARP-P. The first premise not derived from the operator narrative is even earlier: the existence of the self-adjoint operators \(A_P^\circ\), their compatibility with the arithmetic data, and the convergence of their compressions. The text expressly admits that this construction was done "elsewhere" and is not proved here (`main.tex:7675-7686`).

## Step 1–15: audited status

| Steps | Audited status | Reason and first non-derived point |
|---|---|---|
| 1 | Confirmed | The change \(s=\tfrac12+iz\), the symmetries of \(\Xi\) and the translation of RH into reality of zeros are correct (`2067-2131`). |
| 2–3 | Confirmed | For the stated core, horizontal decay and \(N(T)=O(T\log T)\) give normal convergence of the channel series and the indicated residues (`2133-2261`). It is a definition on the zero side, not an arithmetic realization. |
| 4 | Confirmed as a classical interface | Test admissibility is verified and the step uses the explicit formula on a strip-holomorphic test class (`2262-2399`). The first external input is precisely that version of the explicit formula; it is not a new proof of a tower identity. |
| 5 | Open, correctly labeled | ARP-P quantifies over **every** finite source plane and **every** finite set of nodes (`2400-2453`). This is the first unproved input of the chain. |
| 6–7 | Confirmed, conditional on the tower | The Cauchy identity for positive measures and the closure of the PSD cone are correct. Step 7 only states `tower-ARP => ARP-P`; it does not construct tower-ARP (`8032-8164`). |
| 8 | Confirmed with the matrix NP theorem | The Cayley reduction and the semidefinite treatment are adequate if the cited classical matrix NP is accepted (`8165-8303`). |
| 9–11 | Confirmed as a consequence of ARP-P | Pinning prevents a sequence of interpolants from escaping under the Cayley transform; analytic identity and residue detection give pole removal (`8188-8428`). It is a conditional consequence, not an independent proof of tower normality. |
| 12–13 | Confirmed | The symmetries translate the absence of poles of \(\Omega_-\) to the opposite half-plane and the final translation is Step 1 (`8429-8464`). |
| 14 | Confirmed | Under RH, the measure of each channel is finite and positive, so its Cauchy transform has a positive Pick kernel (`8465-8499`). |
| 15 | Confirmed as an assembly | Joins the two previous implications (`8500-8538`). |

Hence the prudent and exact statement would be: **the structural equivalence ARP-P–RH is closed, while ARP-P itself is not**. Steps 9 and 11 are not "closed unconditionally"; they are conditional theorems correctly stated as such in part of the text, but the count "fourteen closed" must keep that qualification.

## The realization and normality: what is and is not available

Layer `7676-8031` contains results valid **if** self-adjointness, a uniform source bound and tower convergence are granted. In particular:

- the mass bound of the source vectors is deduced from the absolutely convergent sum once the cell form and the shorting exist (`7785-7915`);
- compactness of spectral measures and the Cauchy bridge are correct under those hypotheses (`7922-8029`);
- tower-ARP is a convergence condition, not a proved consequence of \(\Lambda\ge0\) (`8129-8164`).

But the opening paragraph of the section presupposes the construction of \(A_P^\circ\), the canonical von Mangoldt form and source compatibility, and defers all of that outside the text (`7675-7686`). The claim "\(\Lambda\ge0\) makes the \(A_P\) self-adjoint" does not substitute for a construction with the limiting identity

\[
 (\Phi_P^F)^*(A_P^\circ-z)^{-1}\Phi_P^F\longrightarrow G_\Xi^F.
\]

That limit is tower-ARP and, by the chain itself, would imply RH. The audit confirms the theorems of the form "if such a tower exists, then…", but does not confirm that the program already has the tower. It also does not confirm "there is only one divergent direction": `rank-one pole isolation` proves summability of source masses, not a global operator bound on every primitive complement (`7715-7771`).

## H0–H8: reconstruction and first cut of each subchain

| Level | What actually remains | Audited status / first cut |
|---|---|---|
| H0 | Preservation of difficulty. | Confirmed, but it is modus ponens; it does not by itself locate a mathematical gap (`2941-2950`). |
| H1 | Scalar Pick positivity of one node for \(M_\Xi\) in \(\Re s>1\). | Confirmed with the symmetric Hadamard factorization. It is not ARP-P for a matrix node: the channel weights have phase, as the text itself acknowledges (`2951-2985`). |
| H2 | Sufficient Gershgorin criterion for separated nodes within a fixed band. | Partial and confirmed as a criterion. It does not cover arbitrary separated configurations nor accumulating nodes (`2986-3023`). |
| H3 | Infinitesimal two-node inequality in a logarithmic region and almost everywhere. | Partial. PDH is an open hypothesis, not a global closure (`3024-3316`). The "closed" label is correct only with the written regions and quantifiers. |
| H4 | Serialization via determinants along an accumulating sequence. | Confirmed as an equivalence with RH, via `prefix-extension` (`3657-3696`). It is a serialization, not a determinant bound nor a method that avoids RH. |
| H5 | Window positivity \(\Longleftrightarrow\) ARP-P. | Confirmed on the stated window class, if the dominated exchanges proved with the growth of \(\psi^F\) are accepted (`3347-3374`). It discharges no quantifier of Step 5. |
| H6 | Finite negative witness if RH fails. | Only the qualitative version is confirmed, since it is the contrapositive of ARP-P \(\Rightarrow\) RH. The "closed quantitative" version fails as explained below. |
| H7 | Andreief/Vandermonde SOS and two-node positivity. | The SOS remains a program. The band closure only handles \(N=2\), a compact band and common height large enough (`4039-4054`, `4605-4667`). It does not justify "all regimes". |
| H8 | Fixed-\(N\) patterns, jets and band closure; then the terminal defect. | Confirmed for fixed \(N\), band separated from the boundary, and common height translation large enough (`3809-4054`, `4605-4682`). The first uncovered point is uniformity in \(N\) for a sequence accumulating at fixed height: exactly the terminal condition. |

### H6: concrete normalization mismatch and lack of negativity

Proposition `H6 quantitative reduction` has as local term

\[
-\eta |\kappa|\,|r(w_0)|\,|r(\overline w_0)|,
\]

because the text declares that it does **not** normalize the channel (`3406-3464`). However, Theorem `H6 quantitative single-cluster witness` replaces that term with

\[
-2|r(w_0)|\,|r(\overline w_0)|
\]

without the \(|\kappa|\) factor (`3530-3555`). \(|\kappa|=1\) has not been imposed, and the source can be rescaled. The conclusion therefore has a type/normalization mismatch.

Moreover, even keeping \(|\kappa|\), the proofs only produce

\[
 \lambda_{\min}P\leq
 \frac{-2|\kappa|,|r(w_0)|,|r(\overline w_0)|+
 B_{\rm far}\|r\|_{\rm far}^2}{\|c\|^2}.
\]

It is not proved that the numerator is negative for every configuration. Phase control makes the local block negative, but does not dominate the tail. Hence what has been proved is a **reduction to an effective witness**: for given local data, poles and a tail bound, an upper Rayleigh bound can be computed. A **negative witness** — that this bound is less than zero for every non-real cluster — has not been proved. This is the first unjustified point of H6 and suffices to block the "quantitatively closed" status.

### H2: the bounded-heights addendum is invalid

The formal statement of H2 adds that "for bounded heights the Pick matrix is PSD by compactness and the strict positivity of \(\Re(\xi'/\xi)\)" (`2994-2998`). The following proof only handles large heights and the row-sum criterion. The additional inference is invalid: strictly positive diagonals do not imply that a Hermitian matrix is PSD, and compactness would only allow extracting continuous eigenvalue minima; it does not prove those minima are nonnegative. One would need to prove all principal minors, diagonal dominance, or the positivity itself on the compact set. None of those pieces appear.

Hence H2 is confirmed only as a large-height Gershgorin criterion under the explicit row-sum condition. The bounded-heights clause must be removed or turned into a hypothesis to be verified; it cannot be used to widen the regime of H2.

### Jets, band closure and the jump to \(N\to\infty\)

The paired Hadamard identity and the scalar jet serialization are strong, essentially confirmed pieces (`4175-4347`). In particular, positivity of all jets at **one** regular point is equivalent to RH: continuation via NP applies to a neighborhood and detects every pole. This makes the scalar defect a legitimate reformulation, but not an easier one.

The Band Closure Theorem (`4605-4667`) uses compactness after a Newton basis change. It proves positivity for fixed \(N\) and nodes of the form

\[
z_j=t+a_j-iy_j,\qquad |a_j|\le A,\quad y_j\in[\tfrac12+\epsilon_0,Y],
\]

when \(|t|\) is large enough **depending on \(N\)**. It does not prove positivity in a fixed box for any height, nor does it supply control of \(T^*(N)\) as \(N\) tends to infinity. The phrases "for all configurations" must be read with those three parameters fixed; without them they are stronger than the theorem.

## Terminal defect, sampling and saturation

Several status contradictions concentrate here.

1. There are two objects called \(\delta_N\). Definition `terminal-defect-fixed` uses
   \(\min c^*J_Nc/(c^*G_Nc)\) and is defined for all \(N\) because \(G_N\succ0\) (`4880-4927`). Definition `terminal-defect` uses \(1-\lambda_{\max}(T_N)\), whitened by \(J_N^\infty\), and only exists while \(J_N^\infty\succ0\), i.e. up to \(N_*(t_0)\) (`5109-5120`). They are not interchangeable outside that interval. In particular, a limiting claim \(N\to\infty\) written for \(T_N\) at fixed \(t_0\) is not well typed.

2. `whitened-terminal` is a correct congruence under the explicit hypothesis \(J_N^\infty\succ0\) (`4826-4861`). `pole-pair` denies precisely that positivity for all \(N\) (`4862-4879`). Hence \(\Omega_4\) cannot appear as a "for all \(N\)" closed equivalence with \(\mathcal W_A^{-1/2}\mathcal T_\Lambda\mathcal W_A^{-1/2}\). The reference-whitened form does serialize the sign; the operator whitened by the archimedean part does not do so globally.

3. `signed archimedean decomposition` is labeled **Proof sketch** (`5121-5176`). Its uniform bounds are used by the sampling theorems. Hence `leading sampling form` and, especially, the `audited weighted sampling form` are not fully proved results in the text. The second also invokes minimizer concentration and a factorial bound not yet established (`5227-5267`).

4. `conditional saturation` claims \(\limsup_N\lambda_{\max}(T_N)=1\) but the object on the left is not defined for all \(N\). Its proof says the tail can be made arbitrarily small and cites a conditional reduction and a theorem announced "closed modulo" pending accounting (`5268-5313`, `5495-5536`). Approximation by interpolation of a growing number of atoms is not, by itself, enough to make the tail ratio small. The first missing point is the uniform estimate of that tail.

5. `two-sided factorial saturation bounds` contains a **Proof sketch**, declares the upper bound "closed modulo" pending work, and acknowledges that the Turán–Remez step for \(c_1(y)\) is an audit point (`5519-5546`). It cannot be used as a closed theorem to prove saturation, `no fixed margin`, the cascade or a detection rate.

6. `root recovery` and `terminal wall as Weil positivity` are also given as sketches (`5555-5615`). The latter also switches to \(\mathsf d_N\), a symbol not defined compatibly with the two \(\delta_N\)'s, and its density/completeness is not proved. It is not a new proof of Weil nor a closure of Step 5.

The audited conclusion is: the equivalence of the reference-whitened sign with RH is valid as a serialization through the scalar jet theorem; the size laws, factorial saturation, lack of margin and root recovery are evidence or conditional reductions, not closed inputs.

## \(\Omega_1\)–\(\Omega_7\) chain

| Link | Status declared by the text | Audited status |
|---|---|---|
| \(\Omega_1\) | RH \(\Leftrightarrow\) real zeros of \(\Xi\). | Confirmed. |
| \(\Omega_2\) | Real zeros \(\Leftrightarrow\) ARP-P. | Confirmed as the Step 1–15 equivalence. It is not an arithmetic mechanism for proving ARP-P. |
| \(\Omega_3\) | ARP-P \(\Leftrightarrow\) \(\delta_N\ge0\) for all \(N\). | Confirmed only as a logical equivalence passing through RH: scalar jets \(\Leftrightarrow\) RH and ARP-P \(\Leftrightarrow\) RH. There is no direct derivation of all channels from a scalar jet. |
| \(\Omega_4\) | Defect \(\Leftrightarrow\) whitening domination. | Not confirmed for all \(N\): it conflates the reference-whitened form, valid globally, with the whitening by \(J_N^\infty\), valid only up to \(N_*\). |
| \(\Omega_5\) | Regular limit at the boundary. | Only **continuity** for each fixed \(N\) is confirmed (`5974-6004`). Unconditional interior positivity is not proved, nor is positivity of its limit; the step "if there is interior positivity, then the limit is PSD" is conditional. It also does not exchange \(y\downarrow\tfrac12\) with \(N\to\infty\). |
| \(\Omega_6\) | Boundary positivity \(\Leftrightarrow\) Li–Keiper. | Confirmed only as an equivalence of complete families, via both being equivalent to RH (`6005-6091`). The text itself correctly denies a level-by-level positive transformation. |
| \(\Omega_7\) | \(\lambda_n\ge0\) for all \(n\). | Open and equivalent to RH by Li. This remains the correct residue. It is not equivalent to \(|\lambda_n^{\rm prime}|<\lambda_n^{\rm arch}\) for all \(n\): that reformulation already fails at \(n=1\). |

The status table at `6130-6165` presents \(\Omega_4\) as closed while simultaneously limiting the \(J_N^\infty\) whitening to \(N\le N_*\). These are incompatible statements unless \(\Omega_4\) is rewritten exclusively in reference-whitened coordinates, without a global \(\mathcal W_A^{-1/2}\) operator. It also overstates \(\Omega_5\): its lemma proves continuity, not unconditional positivity. This does not undermine \(\Omega_3\) or \(\Omega_6\), which are complete equivalences obtained via RH; it does prevent reading \(\Omega_4\to\Omega_5\to\Omega_6\) as a proved chain that transports interior positivity through to Li.

### Li dictionary: what is confirmed and what is not

The Cayley identity

\[
w_{-i/2}(z_\rho)=1-\rho^{-1}
\]

is correct. It is also correct that positivity of all jets in the Li basis and positivity of all Li coefficients are equivalent because both characterize RH. It is not correct to present this as a finite transformation of one criterion into the other; the text acknowledges this at `6060-6091`.

The reformulation of \(\Omega_7\) by absolute value at `6255-6258` is not equivalent to Li and has an immediate internal counterexample. With the stated decomposition

\[
\log\xi(s)=\left[\log s-\frac{s}{2}\log\pi+\log\Gamma\!\left(\frac{s}{2}\right)\right]
+\log\bigl((s-1)\zeta(s)\bigr),
\]

Li's differential definition gives, for \(n=1\),

\[
\lambda_1^{\rm arch}
=1-\frac{\gamma}{2}-\log 2-\frac12\log\pi
\approx-0.55412,
\qquad
\lambda_1^{\rm prime}=\gamma\approx0.57722,
\]

since \(\psi(1/2)=-\gamma-2\log2\) and \((s-1)\zeta(s)=1+\gamma(s-1)+O((s-1)^2)\). Hence

\[
\lambda_1=\lambda_1^{\rm arch}+\lambda_1^{\rm prime}
\approx0.02310>0,
\]

while \(|\lambda_1^{\rm prime}|<\lambda_1^{\rm arch}\) is impossible because its right side is negative. In general, the exact identity implies

\[
\lambda_n\ge0
\quad\Longleftrightarrow\quad
\lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch},
\]

a one-sided inequality and not an absolute bound. If \(\lambda_n^{\rm arch}>0\), the stronger condition \(|\lambda_n^{\rm prime}|\le\lambda_n^{\rm arch}\) suffices for Li, but is neither necessary nor equivalent; with strict sign it also does not coincide with the non-strict criterion. Consequently, the formulations at `6122-6125`, `6255-6258`, `6298-6303` and `6333-6336` must replace the supposed equivalence with the one-sided inequality, or present the absolute envelope only as a sufficient strategy after separately checking the indices where the archimedean part is not positive.

The integration-by-parts identity at `6399-6401` also contains an independent error. With

\[
f_{n,\varepsilon}(y)=y^{-1-\varepsilon}L_{n-1}^{(1)}(\log y),
\qquad f_{n,\varepsilon}(1)=n,
\]

the earlier regularized representation gives

\[
\lambda_n^{\rm prime}
=-
\lim_{\varepsilon\downarrow0}
\int_{1^-}^{\infty}f_{n,\varepsilon}\,d(\psi-y).
\]

Integrating by parts and using \(\psi(1)=0\) produces

\[
\lambda_n^{\rm prime}
=
\lim_{\varepsilon\downarrow0}
\left[-n+
\int_1^\infty(\psi(y)-y)f'_{n,\varepsilon}(y)\,dy\right]
=
\lim_{\varepsilon\downarrow0}
\int_1^\infty(\psi(y)-y+1)f'_{n,\varepsilon}(y)\,dy.
\]

The manuscript writes the negative of the integral with \(\psi-y\), without the \(-n\) term. It therefore flips the sign and loses the lower boundary term. At \(n=1\) the printed formula cannot return \(\lambda_1^{\rm prime}=\gamma\). If \(A_n=\int|\psi-y|\,|f'_{n,0}|\), the correct lower bound is \(\lambda_n^{\rm prime}\ge-n-A_n\), not the one derived in the text. The magnitude no-go keeps its order deficit because the computation reports \(A_n\asymp n^2\log n\), but no signed conclusion can be inherited from `6399-6401`.

The later "envelope" route has a more severe problem: it defines

\[
O(n)=\sum_\rho(1-1/\rho)^n.
\]

Under RH the summands have modulus one and, after pairing, tend to \(2\), not zero. This sum does not converge, either absolutely or symmetrically, for fixed \(n\). The convergent combination is Li's, \(\sum_\rho[1-(1-1/\rho)^n]\), with the appropriate regularization; not \(O(n)\) in isolation. Consequently, the subsequent oscillatory integral, `exact reduction of the envelope bound` and the three routes R1–R3 (`7110-7185`) are not well defined as written. The first unjustified step is not the stationary-phase estimate: it is the separation of a divergent sum.

Moreover, the equivalence attributed to Bombieri–Lagarias between RH and the concrete bound
\(|\lambda_n^{\rm prime}|=O(\sqrt n\log n)\) is not proved in the manuscript. The bound suffices, together with a finite check, for positive Li; the converse requires an additional asymptotic result for Li and does not follow from Li by the logic shown. The formula written at `7079` also omits a linear term: with the manuscript's split,

\[
\lambda_n^{\rm arch}
=\frac n2\log\frac n{2\pi}
+\frac{\gamma-1}{2}n
+\frac34+O(n^{-1}).
\]

The term \(\frac{\gamma-1}{2}n\) does not fit inside \(O(\sqrt n\log n)\). The bound \(c\sqrt n\log n\) for the prime part should only be stated for \(n\ge2\), because its right side vanishes at \(n=1\). Until a reference and an exact proof of the converse are given, it should be labeled a sufficient conjecture, not "iff RH". The Laguerre representation in \(\Re s_0>1\) is an absolutely convergent identity; its boundary limit maintains a pole–prime cancellation and is not an absolute prime sum (`6339-6375`).

## The seven walls, the Weil umbrella and the no-gos

The text has an additional umbrella, Weil positivity, and seven walls numbered by the master quantifier. The umbrella should not be counted as an eighth wall.

| Obstruction | Declared classification | Audit |
|---|---|---|
| Weil umbrella | \(E(C)\): Weil positivity \(\Leftrightarrow\) RH. | Confirmed as a classical criterion, with the correct test class. |
| Arithmetic propagation | \(I(\mathcal I;C)\) for four method families. | The formal scope is only those families. Theorem `four-way` uses "every classical mechanism" and "no combination" without defining the class or supplying a complete proof (`655-693`); it does not confirm a general impossibility. |
| Wrong sign | \(I\) for lower/magnitude bounds. | A valid diagnosis of the enumerated paradigms; not a prohibition of every operator construction. |
| Infinite Hasse–Minkowski | \(I\) for local-global factorization. | Correct as a warning that there is no automatic principle. The non-existence of every useful factorization of the zero part is not formalized as a universal theorem. |
| Place-wise reflection | \(I\) for the chosen OS kernel. | The indefiniteness of the exhibited kernel is direct; it only closes that place-wise reconstruction, not any form of global positivity. |
| Cohomology/Frobenius | \(F(X;C)+S(C)\). | Only conditional: a polarization with a gap and Frobenius of the correct type would suffice. Computations in one window do not prove no global object exists. |
| Sign versus magnitude | \(I\) for functionals that see only \(|\Lambda|\). | The logical principle is reasonable within that class. Theorem `marginality` is stated without a formal proof and presupposes the positive realization not constructed in the text (`891-920`). |
| Uniform norm/rank one | \(F(X;C)+E(C)\). | Not confirmed as an internal equivalence: the direction "RH implies uniformly bounded primitive norm" and the identity with the Kreĭn–Langer kernel are not proved here; they also depend on objects from the external construction (`1375-1443`). |

The computational no-gos (p-values, exponent fits, DH tables, regressions or LP) only prove what was computed at finite precision and cutoff. They are not impossibility theorems. The labels `No-go`, `Wall` or `Theorem` do not add quantifiers nor substitute for a proof. This affects, among others, `phantom transition`, the DH detectors, the partition margins and the results called W4/W5.

W4 does not formalize a complete class of "recurrence arguments", so the statement "no proof can proceed" exceeds the estimates of one particular scheme (`6481-6586`). W5 does have a direct core: an \(L^1\) density cannot dominate a non-decaying periodic function at every resonance. But `per-prime cutoff feasibility` carries no proof; it follows a numerical table and asserts a uniform constant \(c_p\le6/5\) (`6956-7026`). It is evidence of finite feasibility, not a closed lemma until the density is constructed and the bound proved.

## Routes against \(\Omega_7\): status and cuts

| Route | Actual result | First unjustified point |
|---|---|---|
| Almost-periodic transport | The scale comparison shows a plausible imbalance between recurrence and detection. | `gauge transport` contains "[modulo Lemma signed-arch]", which is a sketch; `geometric detection` imports a rate that is only sketched. `ceiling rigidity` does not prove that for a fixed \(c\) the super-level occurs exactly in every gauge detecting a zero. Hence W4 is not a universal no-go. |
| Castelnuovo transplant | `conditional closure` claims X1–X4 imply positivity. | The argument takes \(c^*J_Nc<0\), produces \(\langle\alpha,\alpha\rangle<0\), but X3 only addresses classes with \(\langle\alpha,\alpha\rangle>0\) (`6629-6656`). X3 cannot be invoked on \(\alpha\); the written Hodge inequality does not give the contradiction. M2 and M2-closure inherit this failure. |
| Thermal construction X3-G | Conjecture and falsification plan. | \(e^D\), domains, regularization, twisted state, duality and the variance–Weil identity are hypothetical (`6746-6955`). "Twist positivity" does not produce the required moment identity. |
| Archimedean partition | Global \(L^1\) no-go for one prime; finite problems explored. | Missing is the feasibility proof with a uniform constant and the formal equivalence between global assignment, boundary symbol and \(\Omega_7\). |
| Li/stationary envelope | A sufficient RH-type condition and a numerical exploration. | The isolated sum \(O(n)\) diverges; hence the "lossless" reduction is not well defined. Using data up to \(n=170\) does not establish an envelope. |
| Pointwise bounds of \(\psi-x\) and term-by-term \(\Lambda\ge0\) | Numerical diagnosis of phase loss. | The tables rule out the absolute estimates tried, not every phase inequality nor every factorization. |

The "closure specification" and its conjectures are appropriate as proposals, but do not count as a seventh wall proof nor as deductive evidence for \(\Omega_7\).

## De Bruijn–Newman cascade

The cascade is not logically separated from the terminal defect. Its Theorem \(\alpha5\),

\[
\lim_N t_N^*=\Lambda_{\rm dBN},
\]

uses \(\alpha4\), which in turn uses L3 and L4. The cuts are:

- \(\alpha3\) is explicitly a `Proof sketch` and does not control the minimizing vector, collisions, or uniform constants (`7329-7347`). Although \(\alpha5\) does not cite it directly, it cannot be called a closed theorem.
- L3 appeals to "the upper part of `two-sided`" and to an unspecified regime; that factorial bound was not proved (`7457-7496`).
- L4 again uses a potential comparison and a denominator bound without proving sufficient uniformity (`7497-7528`).
- \(\alpha4\) and \(\alpha5\) inherit these gaps. The proof of \(\alpha5\) claims the factorial threshold ends up smaller than \(v^2\), precisely the conclusion that depends on L3/L4.

The confirmed part is that, if the detection and tail estimates are granted, the implication toward the characterization of \(\Lambda_{\rm dBN}\) has the correct form. Numerical validation does not replace those estimates. For this reason the cascade must appear as a conditional characterization/proposal, not as a proved result that could support H8.

## Internal status contradictions

1. The summary, the map and the epilogue say there is a single gap; H6 quantitative, sampling, saturation, factorial bound, cascade, partition feasibility and tower realization show additional gaps if presented as autonomous theorems.
2. H7 appears "partially closed", but the table states "scalar level-two band positivity closed for all configurations". The theorem only gives \(N=2\), fixed box, interior band and large height.
3. H8 is called "quantitatively closed" while the object used in the tables, \(1-\lambda_{\max}(T_N)\), ceases to be defined after \(N_*(t_0)\); the reference-whitened defect is a different object.
4. \(\Omega_4\) is labeled globally closed and in the same row limits the main coordinate to \(N\le N_*\).
5. `conditional saturation` and `no fixed margin` are stated as a theorem/corollary, but depend on bounds declared a sketch or "modulo" pending work.
6. The realization section admits that the operator and its compatibility were constructed outside the text, while the preface attributes to \(\Lambda\ge0\) the normality that would make the architecture work. The implication is conditional; the construction is not available in this manuscript.
7. The W4, M2, X3-G and W5 routes mix theorems, numerical propositions, conjectures and problems within paragraphs that then speak of "unconditional by-products". That label should be reserved for what has a complete proof.

## Operative conclusion

The defensible part of the manuscript is a formal reduction and an equivalence:

\[
\mathrm{ARP\!\!\text{-}P}\Longleftrightarrow\mathrm{RH}
\Longleftrightarrow
\bigl[J_N(z_0)\succeq0\ \forall N\bigr]
\Longleftrightarrow
\bigl[\lambda_n\ge0\ \forall n\bigr],
\]

where the equivalences at the ends must be read as complete characterizations, not as finite transformations nor as arithmetic proofs of positivity. The central open point remains \(\Omega_7\).

For the text to be able to claim that the auxiliary reductions are closed, it would need, at a minimum: to fix H6 and dominate its tail; to definitively separate the two defects \(\delta_N\); to restrict \(\Omega_4\) to the range where its whitening exists; to replace the sampling/saturation/cascade sketches with proofs free of circular dependency; to formalize or downgrade W4/W5; to repair the sign in the Castelnuovo closure; and to move the "elsewhere" realization to an explicit hypothesis or an included proof. Until that happens, the audit confirms the main equivalence and the Li residue, but does not confirm that the rest of the quantitative infrastructure is closed.
