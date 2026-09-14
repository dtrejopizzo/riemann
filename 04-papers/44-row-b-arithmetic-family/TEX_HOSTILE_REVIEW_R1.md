# Hostile referee report R1 — `04-papers/44-row-b-arithmetic-family/main.tex`

Reviewed: `main.tex` (3636 lines, 45 pp.), against `main.md`,
`TEX_CONVERSION_NOTES.md`, and the style reference
`04-papers/42-arithmetic-lefschetz-programme/main.tex`.
`main.tex` was **not** edited. Line numbers are those of `main.tex` as
reviewed.

Summary of the check order: (1) forbidden vocabulary, (2) completeness of
proofs, (3) fidelity to the Markdown, (4) compile, (5) style.

---

## A. Forbidden vocabulary and internal-programme prose

### A1. `\S 13` "Nine labels, as a check" and its announcement — BLOCKING
**Lines 269, 3476–3564.**

> l.269: `computation. \S\ref{sec:verification} tabulates nine labels as a check.`
> l.3476: `\section{Nine labels, as a check}\label{sec:verification}`
> l.3479: `are a check, not a source.`
> l.3504–3507: `The last three rows were chosen ... row $16$ has $V(15)=\{3,5\}$, row $9$ has ... One verifies $\Phi_9(1)=3$ ...`
> l.3537, 3542, 3550, 3554–3556: `rows $6,12,30,10$`, `rows $2,4,8,16$`, `because the rows are indexed by $n$`, `visible in the rows`.
> l.3563: `No statement in this paper is obtained by extrapolating from small labels or from the tables above.`

This is internal bookkeeping vocabulary in four distinct registers
("labels", "rows", "check", "verification"), plus a defensive
meta-proposition (`prop:bystructure`, l.3558–3564) whose content is
"our theorems are stated for all `n`" — a statement about the paper, not
about mathematics. `\label{sec:verification}` is itself the forbidden word.

**Decision on mathematical content: there is none that is not already
proved.** Both tables are pure evaluation of `\Lambda`, `\Phi_n(1)`,
`\log n`, `n^{3/2}/(n^2-1)` and `M(\Gamma_n^{\mathrm{rad}})` at nine
integers; `prop:bystructure` states outright that every entry is forced.
The only genuinely instructive items are (a) the disjointness
`V(n)\cap V(n-1)=\emptyset` made visible, and (b) the
`k`-independence `\Prim_4\cong\Prim_8\cong\Z/2` versus the `k`-dependent
half-density.

**Concrete fix.**
1. Delete `\S 13` entirely, including `prop:bystructure`, the second
   (carrier-side) table and the three "structural facts" list.
2. Replace it by a short unnumbered `Examples` subsection placed at the end
   of `\S 5` (`sec:integral`), of at most one table with the columns
   `n | P(n) | \Phi_n(1) | \Lambda(n) | \#H^0(C_{\mathrm{fix}}(n)) | V(n) | V(n-1)`
   for `n = 2,4,8,9,6,12,30`, prefaced by one sentence:
   "The following values illustrate Theorems~\ref{thm:separation}
   and~\ref{thm:degreelaw}." No "check", no "rows", no "labels", no
   "One verifies", no discussion of why the entries were chosen.
3. Delete the clause at l.269 and end that sentence at
   `computation.`; delete `sec:verification` from `\S 1.5`.

### A2. Systematic use of "label" as a technical word — MAJOR
Genuine (non-`\label{}`) occurrences at lines
**288, 599, 730, 869, 939, 1197, 1199, 1661, 1819, 1827, 1829, 1830, 1934,
1955, 2054, 2097, 2102, 2160, 2211, 2367, 2514, 2754, 3549, 3563**, including
the *named object* `\S 5.2 "The label category and its realization"` and
`Definition~\ref{def:labelcat}` "The *label category* `W`".

"Label" is not standard mathematical vocabulary for the index of a family;
in this corpus it is project vocabulary, and an outside reader meets it as a
tic. **Fix:** global substitution `label -> index` (and `label category ->
index category`, `\S 5.2 The index category and its realization`,
`integer label n -> integer n`, `rational label r -> rational index r`,
`real label -> real parameter`). `def:labelcat` must then read "The *index
category* `W`". Check that `\S 5.3`'s `divisor arrows of the index poset`
still reads correctly.

### A3. Meta / AI-flavoured prose — MAJOR
- **l.199–200:** `so no more than an identity of degrees is available, and we say so rather than hiding it.`
- **l.2412–2414** (`thm:additiveext`(ii)): `cyclic invariance of any trace on it is therefore automatic, and we say so rather than claiming it as a result.`
- **l.2186** (`rem:nomapsupplied`): `a collection of equal numerical values does not by itself produce one` — argumentative addressee-directed prose.
- **l.1780** (`rem:aboutthelift`): `and none is smuggled in` (also l.2051 `No information is lost in the passage, and none is smuggled in.`)
- **l.3463** (`rem:singlefreqscope`): `Note carefully what Lemma~\ref{lem:singlefreq} does and does not say.`
- **l.2712 ff.** `rem:nodiagonal`, **l.2440 ff.** `rem:shadowlimits`: `It is worth stating precisely what \S\ref{sec:shadow} does and does not achieve.`
- **l.1536 ff.**: `In particular $\Frob_6$ and $\Frob_4$ are distinguished by their supports before any trace is computed.` — rhetorical.

These are the residue of an internal adversarial process. A referee reads
them as the author arguing with a previous referee. **Fix:** in each case
delete the meta-clause and keep only the mathematical assertion. E.g.
l.199–200 -> `...so the identification is one of degrees only.`;
l.2413 -> `...so cyclic invariance is automatic.`; delete `rem:nomapsupplied`'s
last two sentences and `rem:shadowlimits`'s first sentence.

### A4. Clean hits
No occurrence of "Riemann hypothesis", `\RH`, "programme", "corpus",
"repository", "of record", "ledger", "withdrawn", "acceptance",
"contract", "status", "builder", "auditor", "honest", "candidly",
"PROVED", `P1[0-9][0-9]`, `106_1`. The word "round" does not occur.
"Phase" occurs only at l.3399, 3440, 3471 in the legitimate analytic sense
("non-stationary phase", "sign- or phase-changing amplitude") — acceptable.
"Critical line" occurs once, l.3363, descriptively (`every zero on the
critical line contributes a non-negative amount`), not as a conjecture —
acceptable, though see F2.

---

## B. Completeness of proofs — BLOCKING and MAJOR gaps

All 62 theorem-environment statements were enumerated. Every one is followed
by a proof or by a precise external citation, with the exceptions listed
below. Imports (`prop:splitting`, `prop:slices`, `prop:trace`, `prop:tate`,
`prop:completion`, `prop:shadow`) carry precise pointers to `\cite{Companion}`
and are correctly marked as stated-not-proved; `prop:noZp` is restated with a
correct two-line proof.

### B1. `\Prim_n` is never defined in a numbered environment, and the
### divisor-cube it names is inconsistent between statements — BLOCKING
**Lines 1915–1916 (only definition, in running prose), 1932, 1967–1971,
2061, 2199, 2301–2303, 2333–2340.**

> l.1915: `So the cube with vertices $C_{n/\prod_Jp}$, edges $i_{d,pd}$ and total cofiber $\Prim_n$ is a categorification of ...`

`\Prim_n` — the central object of `\S\S 5–7` — is introduced only in a
connecting sentence, with the cube indexed by subsets `J\subseteq P(n)`
(the *radical* cube, `2^{|P(n)|}` vertices). But
`thm:shstructure`(v), l.2301–2303, states:

> `The M\"obius total cofiber over the divisor poset of $d\mapsto\Sh_\Z(\Frob_d)$, $d\mid n$, is $\Prim_n$`

which is a different diagram (for `n=p^k` the divisor poset is a chain of
length `k`, not a cube), and the proof then concedes exactly this in a
parenthesis, l.2337–2341:

> `(For non-squarefree $n$ the divisor poset is not itself a cube --- for $n=p^k$ it is a chain of length $k$ --- and the cube in question is the one indexed by the radical divisors, of which the poset statement is the top layer; the identity $\sum_{d\mid n}\mu(n/d)\log d=\Lambda(n)$ is unaffected.)`

"of which the poset statement is the top layer" is not a definition and not
an argument; and the appeal to a *numerical* identity does not repair a
statement about a *complex*. **Fix:** add a numbered Definition immediately
after `lem:mobiuscube`:
`\begin{definition} For $n>1$ let $\Prim_n:=\mathrm{tot\,cofib}\bigl(J\mapsto C_{\mathrm{ram}}(n/\prod_{p\in J}p)\bigr)_{J\subseteq P(n)}$, the total cofiber of the $|P(n)|$-cube of radical divisors. \end{definition}`
Then restate `thm:shstructure`(v) with "the radical cube of
$d\mapsto\Sh_\Z(\Frob_d)$", not "the divisor poset", and delete the
parenthesis.

### B2. The structure of `\Prim_n` is asserted in two places, each citing the
### other; it is never proved — BLOCKING
**Lines 1932–1934 (`thm:degreelaw`), 1938–1951 (its proof), 2061–2062 and
2076–2079 (`thm:fourmodels`(a) and its proof).**

`thm:degreelaw` states:
> l.1932: `and $\Prim_n\cong\Z/p$ in degree $0$ when $n=p^k$, while $\Prim_n\cong0$ when $n$ has at least two prime divisors.`

Its proof computes only `\degdet`, i.e. an alternating sum of *numbers*:
> l.1941–1944: `The cone law applied along each cube direction gives that $\degdet$ of the total cofiber is the alternating sum of the vertex degrees; by Lemma~\ref{lem:mobiuscube} that alternating sum is $\sum_{d\mid n}\mu(d)\log(n/d)$.`

Nothing there establishes `H^{-1}(\Prim_n)=0`, nor that `H^0` is cyclic, nor
its order. Conversely `thm:fourmodels`(a) proves the structure by citing
`thm:degreelaw`:
> l.2076–2079: `For (a), apply Lemma~\ref{lem:mobiuscube} and Theorem~\ref{thm:degreelaw}: the total cofiber has $H^{-1}=0$ and $H^0$ cyclic of order $\prod_{d\mid n}d^{\mu(n/d)}=\Phi_n(1)$.`

This is a closed citation loop. Neither `lem:mobiuscube` (an identity of
sums of group elements) nor `thm:degreelaw` (an identity of real numbers)
can produce a statement about `H^{-1}` or about cyclicity. The conclusion is
in fact true, but it is never proved, and it is load-bearing for
`thm:notmonoidal` (l.1967–1978, which asserts `\Prim_2=\Z/2`,
`\Prim_4=\Z/2`), `thm:fourmodels`, `thm:discriminating`(ii),
`thm:degreematching`(iii), `thm:shstructure`(v) and `thm:shdegrees`
(eq. `\eqref{eq:shdeg1}`) — i.e. for the paper's headline identity
`\cfin(\Frob_n)=n^{-1/2}\degdet\Prim(\Sh_\Z)_n`.

**Concrete fix.** Insert a proof by induction on `|P(n)|` of the following
lemma, before `thm:degreelaw`:
> **Lemma.** For `n>1`, `\Prim_n` is quasi-isomorphic to `[\Z\xrightarrow{\Phi_n(1)}\Z]`; in particular `H^{-1}\Prim_n=0` and `H^0\Prim_n=\Z/\Phi_n(1)`.

Proof sketch to be written out: for `|P(n)|=1`, `n=p^k`, `\Prim_n` is the
cone of `i_{n/p,n}=(\mathrm{id},p):[\Z\xrightarrow{n/p}\Z]\to[\Z\xrightarrow{n}\Z]`;
the cone of an injective chain map of two-term free complexes with injective
differentials is quasi-isomorphic to the degree-`0` cokernel complex, here
`\Z/p` — which is `[\Z\xrightarrow{p}\Z]` up to quasi-isomorphism, and
`\Phi_{p^k}(1)=p`. For `|P(n)|\ge2` iterate one cube direction: the cube is
the cone of a map of `(|P(n)|-1)`-cubes, and the inductive hypothesis gives
`\Prim_n=\Cone([\Z\xrightarrow{a}\Z]\to[\Z\xrightarrow{b}\Z])` with
`b/a=\Phi_n(1)`; conclude by the same cokernel computation, noting
`\Phi_n(1)=1` forces a contractible cone. Only after this may
`thm:fourmodels`(a) cite it, and `thm:degreelaw`'s proof must then be reduced
to the degree statement alone, with the structural clause moved into the new
lemma.

### B3. `\degdet` is defined so that `\eqref{eq:degreelaw}` is a tautology,
### and then used as if it were a theorem — MAJOR
**Lines 1919–1925 (`def:degdet`), 1926–1951 (`thm:degreelaw`).**

> l.1921–1924: `set $\degdet K:=\log\#H^0(K)$ ... extend additively to finite direct sums, with a sign reversal on shifts, and by the cone law to total cofibers. For $m=0$ the invariant is $0$.`

Two defects. (i) "by the cone law to total cofibers" *stipulates* the first
equality of `\eqref{eq:degreelaw}`, so the theorem's first equality is a
definition, not a result; the reader is not told, and the sentence after
`thm:indexcomplex` (l.2034: "Part (iii) is a definitional identity") shows
the author is elsewhere careful about exactly this. (ii) `\log\#H^0` and the
cone law are *not* consistent extensions in general: for a triangle
`A\to B\to C` with `H^{-1}C\ne0` the cone law and `\log\#H^0` disagree, and
the definition gives no coherence proof. The stipulation "`For $m=0$ the
invariant is $0$`" is ad hoc and inconsistent with `\log\#H^0=\log\infty`.

**Fix.** Define `\degdet` on a bounded perfect complex `K` of finite-index
type by `\degdet K:=\sum_i(-1)^i\log\#H^i(K)` (finite when all `H^i` are
finite), prove in one line that it is additive on triangles whose terms all
have finite cohomology, and delete the `m=0` clause (or restrict the
definition to `m\ne0`). Then `\eqref{eq:degreelaw}`'s first equality is a
genuine consequence of B2's lemma rather than a convention.

### B4. `\eqref{eq:cfix}` is asserted without derivation — MAJOR
**Lines 1668–1680.**

> `On $X=\Spec R[z]$ with the dilation $d_n:z\mapsto nz$, the derived intersection of the graph of $d_n$ with the diagonal is the Koszul complex $K_{\mathrm{fix}}(n)=[R[z]\xrightarrow{(n-1)z} R[z]]$, and its transverse cotangent factor at the zero section is $C_{\mathrm{fix}}(n)=[R\xrightarrow{\ n-1\ }R]$`

The Koszul complex is correct. The passage to `C_{\mathrm{fix}}(n)` is not:
`H^0(K_{\mathrm{fix}}(n))=R[z]/((n-1)z)`, which is *not* `R/(n-1)`, and
"transverse cotangent factor at the zero section" is an undefined operation
performed once and never again. Likewise `\eqref{eq:cram}` (l.1681–1684):

> `For the power map $\pi_n:z\mapsto z^n$ on $\mathbb G_m$, the relative cotangent complex pulled back to the identity section is $C_{\mathrm{ram}}(n)=[\Z\xrightarrow{\ n\ }\Z]$`

is asserted with no proof and no citation, although the computation
(`\Omega_{\mathbb G_m}=\mathcal O\,dz/z`, `\pi_n^*(dz/z)=n\,dz/z`) is two
lines.

**Fix.** (a) Write the `\eqref{eq:cram}` computation out and cite Illusie,
*Complexe cotangent et déformations I*, or Stacks Project Tag 08UQ. (b) For
`\eqref{eq:cfix}`, either define "transverse cotangent factor" precisely
(the derived fibre at `z=0` of `K_{\mathrm{fix}}(n)` regarded as a complex of
`R[z]`-modules, i.e. `K_{\mathrm{fix}}(n)\otimes^L_{R[z]}R`, whose `H^0` is
`R\oplus\ldots` — check this, it is not obviously `R/(n-1)` either) or, more
safely, simply *define* `C_{\mathrm{fix}}(n):=[R\xrightarrow{n-1}R]` as the
Koszul complex of the fixed equation `w^{n-1}=1` linearised at `w=1`, which
is what `lem:deformation` actually supplies, and drop the `X=\Spec R[z]`
sentence entirely. Nothing downstream uses the `R[z]` complex.

### B5. `thm:gramoff`: the convolution constant is wrong whenever
### `P(m)\ne P(n)` — BLOCKING
**Lines 2528–2531 (statement), 2543–2550 (proof); propagated to l.2728–2740
(`cor:onlyfinite`, `V_N^{(m,n)}`).**

Statement:
> `Finally the convolution of the level-$N$ coset indicators contributes the constant $\prod_{s\in S_f\smallsetminus F}\vol(1+s^N\Z_s)$, which is $1$ in the flat convention.`

Proof:
> `the last because the convolution of the indicator of a coset of an open subgroup with itself is that volume times the indicator of the product coset.`

The cited fact is correct (`\mathbf 1_{aU}\star\mathbf 1_{bU}=\vol(U)\mathbf 1_{abU}`)
but it does not cover the places in the symmetric difference. By
`\eqref{eq:smearedfrob}`, `\Frob_m^{\mathrm{sm}}` carries an indicator at
every `s\notin P(m)` and `\Frob_n^{\mathrm{sm}}` at every `s\notin P(n)`.
Split `S_f` into three parts:

- `s\notin P(m)\cup P(n) = S_f\smallsetminus F`: both factors carry
  `\mathbf 1_{\cdot U_s}`, convolution gives `\vol(U_s)\mathbf 1_{(n/m)U_s}`.
  Contributes `\vol(U_s)`. **As stated.**
- `s\in P(n)\smallsetminus P(m)`: the first factor carries
  `\mathbf 1_{m^{-1}U_s}`, the second carries *no* condition, i.e. the
  constant `1` on `\Z_s^\times`. Then
  `\mathbf 1_{m^{-1}U_s}\star\mathbf 1_{\Z_s^\times}=\vol(U_s)\cdot\mathbf 1_{\Z_s^\times}`.
  Contributes a further `\vol(U_s)` **which the stated constant omits.**
- `s\in P(m)\smallsetminus P(n)`: symmetric, another omitted `\vol(U_s)`.
- `s\in P(m)\cap P(n)`: `\mathbf 1\star\mathbf 1=1` (probability Haar).
  Contributes `1`.

So the correct constant is
`\prod_{s\in S_f\smallsetminus(P(m)\cap P(n))}\vol(1+s^N\Z_s)`,
not `\prod_{s\in S_f\smallsetminus(P(m)\cup P(n))}`. Already for `m=2`,
`n=3`, `S_f=\{2,3,5\}`: the stated constant is `\vol(U_5)`; the true
constant is `\vol(U_2)\vol(U_3)\vol(U_5)`, off by a factor
`\bigl((2-1)2^{N-1}(3-1)3^{N-1}\bigr)^{-1}`, which is *not* `1` in the flat
convention either (the flat convention divides by
`\prod_{s\notin P(m)}\vol` and `\prod_{s\notin P(n)}\vol`, giving
`\prod_{s\in P(n)\triangle P(m)}\vol(U_s)^{-1}\cdot\ldots`; the arithmetic
must be redone).

The theorem is therefore **stated more generally than it is proved**: the
formula as written is correct only in the case `P(m)=P(n)`, which is exactly
the case verified in `cor:gramdiagconv` (l.2686–2711, `m=n`). This is the
converter's flagged item 1 of `TEX_CONVERSION_NOTES.md \S (c)`, and the
converter's own diagnosis there ("in that case the product coset is a
translate and the constant is as stated") is also wrong: the failure is at
the places of `P(m)\triangle P(n)`, not at shifted cosets.

**Fix.** (a) Replace the constant in the statement by
`\prod_{s\in S_f\smallsetminus(P(m)\cap P(n))}\vol(1+s^N\Z_s)`.
(b) In the proof, write out the three-case split above explicitly.
(c) Redefine `V_N^{(m,n)}:=\prod_{s\in S_f\smallsetminus(P(m)\cap P(n))}\vol(1+s^N\Z_s)`
in `cor:onlyfinite` (l.2733) and recheck the sentence at l.2752–2757
("in the flat convention `V_N^{(m,n)}=1`"), which is now false in general
and must either be dropped or replaced by the corrected value
`\prod_{s\in P(m)\triangle P(n)}\vol(1+s^N\Z_s)`.
(d) Note that `\eqref{eq:gramfinite}` and `\eqref{eq:gramarch}` are
**unaffected** — the index set `F=P(m)\cup P(n)` of the *form*
`\Frob_{r,F}^{\mathrm{sm}}` is correct — so the qualitative conclusion of
`thm:twohalves`(i) survives. Only the scalar is wrong.

### B6. `thm:qfinpositive` uses a phase normalisation of `\zeta_p` that the
### import does not supply — MAJOR
**Lines 2898–2991; the offending step is l.2903–2909.**

> `By \eqref{eq:symbol}, $\widehat W_p(\mathfrak c_0,\tau)=(\log p)\cdot2\Rel(\zeta_p/(1-\zeta_p))$ with $\zeta_p=p^{-1/2}e^{i(\tau\log p+\theta_p)}$. At $\tau=0$ on the principal component $\theta_p=0$, so $\zeta_p=p^{-1/2}\in(0,1)$ is real`

The imported `prop:tate`, `\eqref{eq:symbol}` (l.2390 region), states only
`|\zeta_p|=p^{-1/2}`. The parametrisation `\zeta_p=p^{-1/2}e^{i(\tau\log p+\theta_p)}`
and, crucially, `\theta_p=0` on `\mathfrak c_0`, are new data introduced
inside the proof. The whole of Step 1 — strict positivity
`\widehat\omega_{\mathrm{fin}}(0)>0`, and the sharp claim
`A_S=\widehat\omega_{\mathrm{fin}}(0)` exactly — rests on it. Since
`thm:qfinpositive` is one of the paper's four advertised conclusions
(abstract, l.229–231), the import must carry the phase.

**Fix.** Strengthen `prop:tate` `\eqref{eq:symbol}` to state
`\zeta_p=p^{-1/2-i\tau}` on the principal component, with the precise
pointer into `\cite{Companion}` that supplies it. (The monotonicity step is
otherwise correct: with `\zeta=\rho e^{i\theta}`, `\rho<1`,
`\partial_{\cos\theta}\,2\Rel(\zeta/(1-\zeta))=2\rho(1-\rho^2)/|1-\zeta|^4>0`,
so the maximum is at `\theta=0` and the minimum `-2\rho/(1+\rho)` at
`\theta=\pi`; hence both `A_S=\widehat\omega_{\mathrm{fin}}(0)` and
`|\widehat\omega_{\mathrm{fin}}|\le A_S` hold — but only given `\theta_p=0`.)
Steps 2–4 of the proof are correct as written and were verified
(primitivity of `\Pi g_{0,T}`, `\widehat g_T=(\tau^2+\frac14)T\widehat\varphi(T\tau)`,
`M_{\mathrm{bulk}}\asymp T`, `M_{\mathrm{tail}}=o(T^{-k})`).

### B7. `thm:tateresidue`(iv) is unproved and, as written, ill-posed — MAJOR
**Lines 3144–3150 (statement), 3168–3175 (proof).**

> `(iv) ... the residues at $\tau=i/2$ are $-i(c_p/\log p)$ at $p$ and $-i$ at $\infty$, and they agree if and only if $c_p=\log p$.`
> proof: `The local symbol on the principal component is $\sum_{k\ne0}\vol(p^k\Z_p^\times)p^{-|k|/2}\eta_p^{k}$, in which the volume enters as an overall factor; so replacing $\log p$ by $c_p$ multiplies the whole function, and every residue of its Mittag--Leffler expansion, by $c_p/\log p$. The archimedean residue is unchanged.`

Three defects. (a) `\eta_p` is never defined anywhere in the paper.
(b) No Mittag–Leffler expansion of either local symbol is exhibited, so
"every residue of its Mittag–Leffler expansion" has no referent, and the two
numbers `-i(c_p/\log p)` and `-i` are simply asserted. (c) The archimedean
symbol is given in `\eqref{eq:symbol}` as
`\log\pi-\Rel\psi(\frac14+\frac{i\tau}2)`, which is *not* a meromorphic
function of `\tau` (it is the real part of one), so "the residue at
`\tau=i/2`" of the displayed expression is undefined.

Note that `(iv)` is not needed: `(i)`–`(iii)` are correct, complete, and
already give `cor:uniquenorm`. Note also that `rem:notchartinv` (l.3177–3194)
depends on (iv) for `The \emph{total} Tate residue of the symbol at a chart
$S$ is $\mp i(|S_f|+1)$`, itself unproved.

**Fix.** Delete `thm:tateresidue`(iv) and the corresponding paragraph of its
proof; retitle the theorem accordingly. In `rem:notchartinv`, replace the
"total Tate residue is `\mp i(|S_f|+1)`" sentence by the residue statement of
(i)–(ii) ("each place of `S` carries one residue `c_p/\log p`, resp. `1`, and
their number is `|S_f|+1`, manifestly chart-dependent"), which is what the
remark's argument actually needs.

### B8. `lem:singlefreq`(ii): the Laplace-method sizes are both overstated
### and self-contradictory — MAJOR
**Lines 3373–3392.**

> `both factors being positive real numbers, of sizes $\widehat g_L(\rho_0)\asymp_\psi e^{\delta L}$, dominated by the right endpoint $t=L$, and $\widehat g_L(1-\bar\rho_0)\asymp_\psi e^{-\delta L/2}$, dominated by the left endpoint $t=L/2$, up to sub-exponential factors depending on $\psi$; for a smooth $\psi$ vanishing to infinite order at the endpoints, Laplace's method has a saddle at distance $\asymp(\delta L)^{-1/2}$ from the endpoint and contributes a factor $e^{-c\sqrt{\delta L}}$, which is sub-exponential but not polynomial.`

(a) `\asymp_\psi e^{\delta L}` and "up to sub-exponential factors" are
mutually exclusive: `\asymp` denotes two-sided bounds with constants, and the
subsequent sentence says the true size is `e^{\delta L}e^{-c\sqrt{\delta L}}`.
(b) The saddle scale `(\delta L)^{-1/2}` and the factor `e^{-c\sqrt{\delta L}}`
are correct for `\psi(u)\sim\exp(-1/(1-u))` near `u=1` but **false for a
general** `\psi\in C_c^\infty` vanishing to infinite order: for
`\psi(u)\sim\exp(-(1-u)^{-2})` the balance is at `(\delta L)^{-1/3}` with
factor `e^{-c(\delta L)^{1/3}}`, and by choosing the order of vanishing the
exponent `\sqrt{\ }` can be replaced by any `(\delta L)^{\alpha}`,
`0<\alpha<1`. The statement is made for all such `\psi`. (c) The saddle
computation is never carried out; `c` is never named.
(d) The proof (l.3430–3434) reduces to one sentence:
`The sizes are Laplace's method on $[L/2,L]$: for $\delta>0$ the weight $e^{\delta t}$ is maximal at $t=L$ and $e^{-\delta t}$ at $t=L/2$` — which establishes the location of the maximum, not any size.

The converter flagged this (`\S (c)` item 3) and reproduced it "with the
source's own hedge". A hedge is not a proof.

**Fix.** Replace the size clause by the only statement that is proved and
that (iii)–(v) use:
`with $e^{\delta L/2}\le \widehat g_L(\rho_0)\widehat g_L(1-\bar\rho_0)\cdot e^{?}$` — concretely, state and prove
`\lim_{L\to\infty}\frac1L\log\bigl(\widehat g_L(\rho_0)\widehat g_L(1-\bar\rho_0)\bigr)=\delta/2`
(exponential scale only, no sub-exponential claim), which follows from
`\int_{L/2}^{L}\psi(t/L)e^{\pm\delta t}dt` and Laplace's principle on a fixed
`\psi`. Delete the saddle sentence, or fix one explicit `\psi` in the
statement of the lemma and carry out the saddle computation.
Also: **(iii)** (l.3393–3402) asserts the mismatched pair is `of the same
order $e^{\delta L/2}$ as the resonant pair and no larger`; only the upper
bound is proved (modulus bound plus `\psi\ge0`). Change `of the same order
... and no larger` to `bounded by the resonant contribution`.
Also: **(v)** (l.3403–3419) is correct — I verified
`A=\frac14-\delta^2+\gamma_0^2-2i\delta\gamma_0`,
`\Rel(A^2)=X^2-Y^2` with `X-Y=(|\gamma_0|-\delta)^2+\frac14-2\delta^2>\frac14-\delta^2>0`
when `|\gamma_0|>2\delta` — but the statement should carry the hypothesis
`0<\delta<\frac12` explicitly (it is used, and is only implicit via
`\beta<1`).

### B9. `thm:infgenus`: `\eqref{eq:diagdivnorm}` claims more than the proof
### gives — MAJOR
**Lines 3011–3015 (statement), 3020–3086 (proof).**

> `I_A(G_\varepsilon,G_\varepsilon)=-\log\frac1\varepsilon+C_\varphi+o(1).`

The proof produces `\widehat T(\mathfrak c_0,\tau)=-\log|\tau|+O(1)` with a
bounded, *unidentified* `O(1)`, then
`I_A=\varepsilon^{-1}\|\varphi\|_2^2(\log\varepsilon+O(1))`. Dividing gives
`-\log(1/\varepsilon)+O(1)`, **not** `+C_\varphi+o(1)`: the existence of a
limiting constant would require the `O(1)` in the symbol to converge, which
is neither stated nor proved (and is false without an asymptotic expansion of
`\widehat W_\infty` beyond `\eqref{eq:symbolasym}`'s `O(|\tau|^{-1})` plus
control of `\sum_p\widehat W_p` as `\tau\to\infty`).

**Fix.** Replace `\eqref{eq:diagdivnorm}` by
`I_A(G_\varepsilon,G_\varepsilon)=-\log\frac1\varepsilon+O(1)`, and delete
the symbol `C_\varphi`. Everything downstream (`rem:infinitegenus`, the
abstract's "rate `\log(1/\varepsilon)` per unit of `L^2`-normalized test")
is unaffected.

The rest of the proof is correct as checked: `\|F_\varepsilon\|_{L^2}^2=\varepsilon^{-1}\|\varphi\|_2^2`,
`\widehat F_\varepsilon(\tau)=\widehat\varphi(\varepsilon\tau)`, the
bounded-region estimate `\eqref{eq:boundedregion}`, and the colimit remark at
the end.

### B10. `thm:fourmodels`(d) does not live in `D(\Z)` — MAJOR
**Lines 2053–2095.**

> `the following constructions agree in $D(\Z)$: ... (d) $K_{\mathrm{prim}}(n,t)=[\Z[t]\xrightarrow{\Phi_n(1)}\Z[t]]$`

`[\Z[t]\to\Z[t]]` is a complex of `\Z[t]`-modules of infinite rank over `\Z`;
it is *not* isomorphic in `D(\Z)` to `K_n=[\Z\xrightarrow{\Phi_n(1)}\Z]`
(its `H^0` is `\Z[t]/\Phi_n(1)`, not `\Z/\Phi_n(1)`). The statement's own
tail (`constant in $t$ and specializing to \eqref{eq:Kn} at every $t=c$`)
and the proof's last sentence (`All four have $H^{-1}=0$ and $H^0=\Z/\Phi_n(1)$`)
contradict each other.

**Fix.** Reword the preamble: "(a)–(c) agree in `D(\Z)`; (d) is a complex of
`\Z[t]`-modules whose specialisation at every `t=c\in\Z` is `K_n`, and which
equals `K_n\otimes_\Z\Z[t]`." Then the proof's last sentence applies to
(a)–(c) only.

Apart from this, `thm:fourmodels` (c) and (d) — the two proofs the converter
supplied himself — were verified from scratch and are **correct**:
`\Z[L_S/nL_S]\cong\Z[T]/(T^n-1)`, primitive part `V_n=\Z[T]/\Phi_n(T)`,
`\det(1-T\mid V_n)=\prod_{\zeta\ \mathrm{prim}}(1-\zeta)=\Phi_n(1)`,
`\mathrm{coker}(1-T\mid V_n)=\Z[T]/(\Phi_n(T),1-T)=\Z/\Phi_n(1)`, injectivity
from `\Phi_n(1)\ne0`; and `P_n=\Phi_n(1+tz)` a nonzerodivisor with
`P_n(t,0)=\Phi_n(1)`.

### B11. `\log|\Phi_n(1)|=\Lambda(n)` — the converter's third supplied proof
### is CORRECT
**Lines 1946–1951.** Verified from scratch: `\prod_{d\mid n}\Phi_d(x)=x^n-1`
with `\Phi_1(x)=x-1` gives `\prod_{d\mid n,d>1}\Phi_d(1)=\lim_{x\to1}(x^n-1)/(x-1)=n`;
setting `f(1):=1`, `f(d):=\Phi_d(1)` for `d>1`, one has `\prod_{d\mid n}f(d)=n`
for all `n\ge1` (including `n=1`, empty product), whence by multiplicative
Möbius inversion `f(n)=\prod_{d\mid n}d^{\mu(n/d)}` and
`\log f(n)=\sum_{d\mid n}\mu(n/d)\log d=\Lambda(n)`. No defect. Only note
that the paper should say explicitly that `\Phi_1(1)=0` is why `n>1` is
required.

### B12. `thm:frobincompletion`(ii): uniformity in `N` is asserted, not
### proved — MAJOR
**Lines 1611–1645; specifically l.1627–1642.**

> `Combining this with $|\widehat G|\le C''_B\min(1,\tau^{-2})$ and $|\widehat T|\le A_S+B_S\log(2+|\tau|)$ gives, for $R>0$, $\sup_{G\in B}|I_A(F_{\varepsilon,N},G)-\ell_n^F(G)|\le C_B\,\varepsilon\,R^2\log R+\eta(R)$ ... uniformly on $B$; choose $R$ first and then $\varepsilon$.`

`C_B` is never exhibited and, per the converter's flag (`\S(c)` item 2),
the absorption of the component count `d_{N_B}` and of the finitely many
non-principal components into `C_B` **uniformly in `N\ge N_B`** is not
verified. The claim is a joint limit `\varepsilon\to0`, `N\to\infty`; the
displayed bound has no `N` in it at all, which is precisely the point that
needs an argument (the `r`-factors of `\widehat F_{\varepsilon,N}` and
`\widehat{\Frob_n}` are shown to coincide *provided* `N\ge N_B`, but the
number of components on which they are compared is `d_{N_B}`, which is
`N`-free only because `B` is fixed first — this reasoning must be written).

**Fix.** Add two sentences: fix `B`, hence `N_B` and `d_{N_B}`; for every
`N\ge N_B` the `r`-factors agree exactly on the `d_{N_B}` components met by
`B`, so the difference is supported there and the component count enters as
the constant `C_B:=d_{N_B}C''_B\max(A_S,B_S)`, independent of `N`. Then the
bound holds for all `N\ge N_B` uniformly and the joint limit is legitimate.
(The analogous step in `thm:radincompletion`(ii), l.1029–1056, is fine, there
being no `N`.)

### B13. `lem:traceontinuity` cites `thm:radtrace` outside its hypothesis —
### MINOR
**Lines 3205–3233.** `thm:radtrace` requires `0\notin\supp h`; here
`\supp h\subseteq[-R,R]` contains `0`, and the counterterm is used. The
decomposition at l.3213–3215 is nevertheless correct, because the unit-packet
vanishing for radial sections proved inside `thm:radtrace`'s proof
(l.822–827) is *pointwise* and needs no support hypothesis — but the lemma
cites the theorem, not that step. **Fix:** cite "the pointwise vanishing of
the unit packets on radial sections, established in the proof of
Theorem~\ref{thm:radtrace}" instead of the theorem.

### B14. `thm:invsemigroup`(iii), minimality — MINOR
**Lines 1319–1321.** `minimality is (i) again` is not an argument.
**Fix:** one line: `\Delta^{(F)}=\star_{p\in F}(\Frob_p\star\Frob_p^\dagger)`
and `\Frob_{r,F}=\Frob_a\star\Frob_b^\dagger\star\Delta^{(F)}` for `r=a/b`,
so every element of `\mathfrak F_S` is a `\star`/`\dagger` word in the
`\Frob_n`.

### B15. `E_x` is used but never defined — MINOR
**Lines 371, 1095, 1120, 1155, 1182, 1849, 1867, 1880, 1891.**
`prop:trace` introduces `F\mapsto E_F` for `F\in\DA`; the paper then writes
`E_{j_p(p^ku)}`, `E_{c_n\cdot u}`, `E_1`, `E_{a_S(n)}` with a *point of
`C_S`* (or an idele) as subscript, and l.1867 uses `E_u\star E_v\cong E_{uv}`
without justification. **Fix:** add one sentence to `prop:trace`: "for
`x\in C_S` we also write `E_x` for the point mass `\delta_x`, a multiplier of
`\DA`, and `E_a:=E_{[a]}` for an idele `a`; `E_x\star E_y=E_{xy}`."

### B16. Statements verified correct (no action)
For the record, the following were checked line by line and contain no gap:
`lem:classunit`, `prop:noslice` (all three parts, including the
`|S_f|\ge2` hypothesis and `rem:minimalchart`'s honest exception),
`cor:liftnotcontact`, `lem:notideal`, `thm:radmonoidal` (i)–(iv),
`lem:smeared`, `thm:radtrace` (finite and archimedean places, colimit),
`thm:repmeasures` (including
`K(\log n)=n^{3/2}/(n^2-1)=\frac12[\tau_\infty(1/n)+\tau_\infty(-1/n)]`),
`thm:contactlocus`, `thm:radincompletion`, `lem:frobsupport`,
`thm:frobmonoidal`, `rem:nointerp`, `prop:avgtorad`,
`thm:frobdagger` (including `\Frob_n\star\Frob_n^\dagger=\Delta^{(n)}`, the
bidegree `(n^{1/2},n^{-1/2})`, and `\Delta^{(n)}\ne\Delta` by atomicity),
`thm:invsemigroup`(i),(ii),(iv) (the inverse-semigroup axioms check out:
regularity, commutativity, idempotents exactly `r=1`, and the `2/1=6/3`
counterexample is correct), `lem:smearedfrobinDA`, `thm:frobcontact`
(exactness at every `N`, unit packets, the `r^N\mid n-1` indicator),
`cor:frobnoarch`, `cor:frobinvariant`, `thm:compositedisjoint`,
`prop:archflow`, `thm:separation` (the product-formula computations
`w_{\mathrm{ram}}=n^{-1/2}`, `w_{\mathrm{unit}}=n-1` are right),
`lem:tauinv`, `lem:mobiuscube`, `thm:notmonoidal` (modulo B2),
`thm:indexcomplex`, `thm:discriminating`, `thm:carrierside`,
`lem:shwelldef`, `thm:shstructure`(i)–(iv), `lem:shfunctor` (the strict
functoriality `(f/e)(e/d)=f/d` is right), `thm:additiveext`,
`thm:gramdiag` (the stratification `\vol\{v_r(1-u)=j\}=r^{-j}`,
`\vol\{v_r(1-u)=0\}=(r-2)/(r-1)`, the total `(r-2)/(r-1)+(N-1)`, and the
archimedean `-\log(1/\varepsilon)+O(1)` are all correct, including the
`r=2` degeneration), `cor:gramdiagconv`, `thm:fullweil`, `thm:twohalves`,
`lem:complexprofiles` (the odd cross-term argument is right),
`prop:formsdiffer` (including `\widehat\omega_\infty(\tau)=-\log|\tau|+\log2\pi+O(|\tau|^{-1})`),
`thm:tateresidue`(i)–(iii), `cor:uniquenorm`, `lem:riemannsum`,
`lem:C1control` (the cancellation `\sum_n\rho'(x-n)\equiv0` is the right
mechanism and is correctly used).

---

## C. Fidelity to `main.md`

### C1. Nothing in the TeX is added beyond the Markdown's proved set.
Every numbered statement in `main.tex` maps to a `main.md` item graded
`PROVED`, `PROVED-IN-REPOSITORY`, `CLASSICAL` or imported-with-citation,
per the table of `TEX_CONVERSION_NOTES.md \S(a)`, which I spot-checked
against the source for `thm:gramoff` (md Thm 8bis.1, `PROVED`),
`thm:gramdiag` (8bis.1b), `thm:qfinpositive` (8bis.4a),
`thm:fourmodels` (6.3), `thm:shstructure` (6bis.3) and
`lem:singlefreq` (8bis.6b). No hypothesis was dropped and no claim
strengthened in transit; in particular the defect B5 is **inherited** from
md Thm 8bis.1 verbatim, not introduced by the conversion.

### C2. Exclusions are justified. — no defect.
`TEX_CONVERSION_NOTES.md \S(b)` excludes exactly the `OPEN`, `PARTIAL`,
`WITHDRAWN`, conditional and bookkeeping material (md Thm 8bis.4(ii)(iii)(v)(vi),
Thm 8bis.7 under the open hypothesis `(H_L)`, Thm 8.1, Thm 8.2, §9bis, §10,
the clause tables of §§5505–5546). I found no md item graded `PROVED` that is
omitted without reason. Note in passing that md Thm 8bis.7 is precisely the
conditional statement whose omission keeps the paper free of any
zero-location claim; its analytic lemmas (§12 here) are correctly retained.

### C3. `\S(c)` flags 1 and 3 understate the defects. — MAJOR
`TEX_CONVERSION_NOTES.md \S(c)` item 1 misdiagnoses B5 (see above) and
item 3 calls B8 a hedge rather than a gap. **Fix:** after the repairs, update
`\S(c)` to record that item 1 was a genuine error now corrected, and that
item 3 was resolved by weakening the claim to the exponential scale.

### C4. Imports from the companion paper. — one defect (B6), otherwise clean.
`prop:splitting`, `prop:slices`, `prop:trace`, `prop:tate`,
`prop:completion`, `prop:shadow` are stated as cited propositions with
precise references (`[Lemma 3.3]`, `[(9.5b)]`, `[\S8]`, `[\S9]`,
`[Thms. 7.1, 8A.9]`) and nothing is claimed for them beyond what the
reference is said to prove — **except** the phase normalisation of
`\zeta_p`, which is used but not imported (B6). One presentational point:
`\cite{Companion}` is a bare "companion paper" with no arXiv number, page
count or date; a referee cannot locate it. **Fix (MINOR):** give the
companion a resolvable identifier.

---

## D. Compile

`pdflatex -interaction=nonstopmode main.tex`, run twice from a clean state
(`.aux`, `.log`, `.out`, `.toc` removed first):

- **errors:** none
- **undefined references / citations:** none
- **LaTeX or package warnings:** none
- **Overfull / Underfull boxes:** zero
- **Output:** `main.pdf`, 45 pages.

No defect.

---

## E. Style

### E1. Preamble matches Paper 42. — no defect.
Same `amsart` 11pt, same geometry, same theorem environments and numbering
scheme, same `microtype`/`hyperref` settings, same `Y` column type, same
`\thanks` form. Paper 44 correctly *drops* `\RH` and `\QW` and adds
`\Frob`, `\Sh`, `\Prim`, `\degdet`, `\cfin`, `\Knat`, `\DA`, `\Drad`,
`\Doff`, `\Wfin`. **MINOR:** `\Div`, `\divv`, `\Gr`, `\GL`, `\rk`, `\Ch`
(3 uses, fine) — `\Div`, `\divv`, `\Gr`, `\GL`, `\rk` are each defined and
used zero times outside their own definition. Delete them.

### E2. Title. — acceptable.
> `An Arithmetic Frobenius Family and its Integral Shadow on a Correspondence Algebra of the Idele Class Group` + subtitle `Inverse semigroup structure, two Gram forms, and the von Mangoldt function as a shell volume`

The main title names what is constructed (a family and its shadow) and where;
the subtitle lists three results. This is the same two-deck shape as Paper
42 and is within normal `amsart` practice. The running head
`An arithmetic Frobenius family and its integral shadow` is correct. **No
change required.** (If shortened at all, drop only `on a Correspondence
Algebra of the Idele Class Group` — but the location is informative and I
would keep it.)

### E3. Section title `\S 13` — see A1. BLOCKING.

### E4. Meta-prose — see A3. MAJOR.

---

## F. Two further observations

### F1. `\S 12` is orphaned. — MINOR
**Lines 3195–3204.** The section opens
`The three are independent of everything in \S\S\ref{sec:radial}--\ref{sec:shadow} and are used by no statement there.`
Combined with the introduction's `it is used by the approximation apparatus
of \S\ref{sec:approx}` (l.247–248, about `lem:singlefreq`), this is a
self-contradiction: `lem:singlefreq` *is* in `\S 12`, and nothing in `\S 12`
uses it either. In fact `lem:traceontinuity`, `lem:riemannsum`,
`lem:C1control` and `lem:singlefreq` are mutually independent and used by
nothing in the paper. **Fix:** in `\S 1.4` say plainly that
`lem:singlefreq` is included as a self-contained computation and is used by
no other statement; delete the false claim that `\S 12` uses it. In `\S 12`,
delete "and are used by no statement there" (it is a claim about the paper,
not mathematics) and instead say the three lemmas are independent of one
another.

### F2. `lem:singlefreq` is conditional and should say so in its statement. — MINOR
**Line 3360:** `Suppose $\rho_0=\beta+i\gamma_0$ is a zero with $\delta:=\beta-\tfrac12>0$.`
Parts (ii)–(v) are vacuous unless such a zero exists. This is correct as
written and `rem:singlefreqscope` says it decides nothing — but the lemma
should open `Assume, for this lemma only, that ...` so no reader takes (ii)
as an unconditional assertion. Also add `0<\delta<\frac12` explicitly (B8).

---

## Summary of findings by severity

**BLOCKING (3)**
- A1 — `\S 13` "Nine labels, as a check" and l.269: internal bookkeeping
  vocabulary in a paper for outside mathematicians; no mathematical content
  beyond what is already proved. Delete; replace with a one-table
  `Examples` subsection in `\S 5`.
- B1 — `\Prim_n` has no definition and the diagram it names is inconsistent
  between `\S 5.3` (radical cube) and `thm:shstructure`(v) (divisor poset).
- B2 — the structure `\Prim_n\cong[\Z\xrightarrow{\Phi_n(1)}\Z]` is never
  proved: `thm:degreelaw` and `thm:fourmodels`(a) cite each other. This
  carries the paper's headline degree identity `\eqref{eq:shdeg1}`.
- B5 — `thm:gramoff`: the convolution constant
  `\prod_{s\in S_f\smallsetminus F}\vol(1+s^N\Z_s)` is wrong whenever
  `P(m)\ne P(n)`; the correct index set is `S_f\smallsetminus(P(m)\cap P(n))`.
  The theorem is stated more generally than it is proved; the verified case
  is the diagonal one. Propagates to `cor:onlyfinite`.

**MAJOR (11)**
A2 (systematic "label"); A3 (meta/AI prose, six sites); B3 (`\degdet`
stipulated, making `\eqref{eq:degreelaw}` partly tautological and partly
incoherent); B4 (`\eqref{eq:cfix}`/`\eqref{eq:cram}` asserted without
derivation or citation); B6 (`thm:qfinpositive` uses `\theta_p=0`, not
supplied by the import); B7 (`thm:tateresidue`(iv) unproved and ill-posed);
B8 (`lem:singlefreq`(ii) Laplace sizes overstated, self-contradictory, and
false for general `\psi`); B9 (`\eqref{eq:diagdivnorm}`'s `C_\varphi+o(1)`
not proved); B10 (`thm:fourmodels`(d) not an object of `D(\Z)`);
B12 (`thm:frobincompletion`(ii) uniformity in `N` asserted); C3 (conversion
notes understate two defects).

**MINOR (7)**
B11 note on `\Phi_1(1)=0`; B13 (`lem:traceontinuity` citation);
B14 (`thm:invsemigroup`(iii) minimality); B15 (`E_x` undefined);
C4 (unresolvable `\cite{Companion}`); E1 (five dead macros); F1 (`\S 12`
self-contradiction); F2 (`lem:singlefreq` conditionality).

---

# VERDICT: MAJOR REPAIRS NEEDED

The construction is sound and the paper is, for the most part, unusually
careful about what it does and does not prove — the type distinctions
(multiplier vs. element, atom vs. density, degree vs. object), the explicit
scope remarks, and the refusal to claim Weil's degree relation are all
correct and are the paper's strength. The compile is clean and the fidelity
to the source is good.

But it cannot be accepted as it stands. Three blocking defects: an entire
section written in internal project vocabulary (A1); a central object
(`\Prim_n`) that is undefined, diagram-ambiguous, and whose structure theorem
rests on a two-way citation loop (B1, B2) — this carries the advertised
identity `\cfin(\Frob_n)=n^{-1/2}\degdet\Prim(\Sh_\Z)_n`; and a Gram-form
constant that is simply wrong off the diagonal (B5), stated in the generality
the proof does not reach. Each has a concrete, bounded repair, specified
above. The eleven MAJOR items are repairs of statement or of one-paragraph
arguments, not of the mathematics.

I expect a revised version to be acceptable.

---
---

# Review R2 — confirmation round (2026-09-13)

Verified against the **current** `main.tex` (3817 lines, up from 3636),
`main.md` (5892 lines, up from 5716) and
`04-papers/43-row-a-torsion-theory/main.md`. Every finding of R1 was
re-checked at its site in the revised file; the two mathematical corrections
(B5, B2) were re-derived from scratch rather than read off the notes.

## 1. B5 — the Gram convolution constant: **RESOLVED, re-derived**

`thm:gramoff` now carries `\eqref{eq:gramconst}` (l.2732–2733)
`c_N(m,n):=\prod_{s\in S_f\smallsetminus(P(m)\cap P(n))}\vol(1+s^N\Z_s)`,
with the sentence "whose index set is the complement of the *intersection* of
the two prime sets, not of their union".

**Four-case computation re-derived independently (l.2745–2778).** The proof
first justifies the dagger step —
`\mathbf 1_{n^{-1}U_s}(x_s^{-1})=\mathbf 1_{nU_s}(x_s)`, using that `U_s` is
a group — which R1 did not require but which was needed. Then, with `\Z_s^\times`
carrying probability Haar measure:
- `s\notin P(m)\cup P(n)`: `\mathbf 1_{m^{-1}U_s}\star\mathbf 1_{nU_s}=\vol(U_s)\mathbf 1_{(n/m)U_s}` — contributes `\vol(U_s)`. ✔
- `s\in P(n)\smallsetminus P(m)`: `(\mathbf 1_{m^{-1}U_s}\star\mathbf 1_{\Z_s^\times})(x)=\int_{m^{-1}U_s}\mathbf 1(y^{-1}x)\,dy=\vol(m^{-1}U_s)=\vol(U_s)` for all `x\in\Z_s^\times` — contributes `\vol(U_s)`, previously omitted. ✔
- `s\in P(m)\smallsetminus P(n)`: symmetric. ✔
- `s\in P(m)\cap P(n)`: `\mathbf 1_{\Z_s^\times}\star\mathbf 1_{\Z_s^\times}=\mathbf 1_{\Z_s^\times}` — contributes `1`. ✔

Multiplicity check: an `s` contributes `\vol(U_s)` iff `s\notin P(m)\cap P(n)`.
This is exactly `\eqref{eq:gramconst}`. **Correct.**

**Flat-convention value verified.** The paper asserts
`V_N(m)V_N(n)=c_N(m,n)\cdot\prod_{s\in S_f\smallsetminus F}\vol(U_s)`.
Counting multiplicities of `s` on each side: `s\notin F` gives `2=1+1`;
`s` in exactly one of `P(m),P(n)` gives `1=1+0`; `s\in P(m)\cap P(n)` gives
`0=0+0`. ✔ Hence the flat entry constant is
`c_N(m,n)/(V_N(m)V_N(n))=\prod_{s\in S_f\smallsetminus F}\vol(1+s^N\Z_s)^{-1}`,
equal to `1` exactly when `F=S_f` — as stated (l.2736–2742), and as the
coordinator's message specifies. **Correct.**

**Propagation.** `cor:onlyfinite` (l.2973–2977) now sets
`V_N^{(m,n)}:=c_N(m,n)`, with the observation that at `m=n` this is exactly
the `V_N(n)` of `\eqref{eq:VN}` — verified: for `m=n`,
`S_f\smallsetminus(P(n)\cap P(n))=S_f\smallsetminus P(n)`. ✔ So one formula
now covers off-diagonal and diagonal, and `cor:gramdiagconv` (which verified
`m=n`) is untouched. The trailing note (l.2988–2995) correctly replaces the
old false "in the flat convention `V_N^{(m,n)}=1`" by the corrected value and
the condition `F=S_f`.

**`thm:fullweil` and `thm:twohalves` confirmed unaffected.** `thm:fullweil`
(l.2999 ff.) is proved through `\Gamma_{h_m}\star\Gamma_{h_n}^\dagger=\Gamma_{h_m\star h_n^\dagger}`
(`lem:smeared`) and `thm:radtrace`; no coset indicator and no level constant
enters — radial classes are `\Knat`-invariant, so `\eqref{eq:smearedfrob}`'s
finite factors are the constant `1`. `thm:twohalves`(i) cites only
`cor:onlyfinite`'s qualitative content (`\Wfin` off the diagonal, no
archimedean block), which depends on `\eqref{eq:gramfinite}` and
`\eqref{eq:gramarch}` — both unchanged, as is the index set `F=P(m)\cup P(n)`
of the composed object. ✔

**`main.md` matches.** Thm 8bis.1 carries `(8bis.2b)` with the same index set
(l.3351), the same flat-convention derivation (l.3360) and the four-case
proof (l.3384); Cor 8bis.1d carries `V_N^{(m,n)}:=c_N(m,n)` (l.3575) with the
correction marker (l.3591). ✔

## 2. B2 / B1 — `\Prim_n`: **RESOLVED, induction verified**

`def:prim` (l.1964–1978) is a numbered definition of the radical cube and of
`\Prim(N,P)`, `\Prim_n:=\Prim(n,P(n))`, followed by two remarks that state
explicitly that the cube is indexed by *radical* divisors and not by the
divisor poset (killing B1's ambiguity), and that the squares commute strictly.

`lem:primstructure` (l.1987–2050) — induction on `r=|P|`, checked line by line:
- **Base `r=1`, `P=\{q\}`:** the cube is the single edge `i=(\mathrm{id},q):C_{\mathrm{ram}}(N/q)\to C_{\mathrm{ram}}(N)`, degreewise injective (identity in degree `-1`, `\times q` in degree `0`), so `\Cone(i)` is quasi-isomorphic to the degreewise cokernel `[0\to\Z/q]`. ✔ Both `H^{-1}=0` and `H^0=\Z/q` follow, which is exactly what R1 said was missing.
- **Step `r\ge2`:** splitting along direction `q` identifies the face `\{J:q\notin J\}` with the radical cube of `(N,P')` and `\{J:q\in J\}` with that of `(N/q,P')`, the direction-`q` edges giving `\varphi`; total cofibers commute with iterated cones in any order, so `\Prim(N,P)=\Cone(\varphi_*)`. ✔
- **`r\ge3`:** `|P'|\ge2`, both ends acyclic by induction, cone acyclic. ✔
- **`|P|=2` identification:** `P=\{q,q'\}`; both `\Prim(N,\{q'\})` and `\Prim(N/q,\{q'\})` are `\Z/q'` in degree `0`, presented as the degree-`0` terms of `C_{\mathrm{ram}}(N)` resp. `C_{\mathrm{ram}}(N/q)` modulo `q'`; the direction-`q` edges are `(\mathrm{id},q)` in both, so `\varphi_*` is multiplication by `q` on `\Z/q'`, an isomorphism since `q\ne q'` are primes; the cone is acyclic. ✔ This is the one step R1 could not find anywhere in the old text.
- **Consequence:** `n=p^k` gives `\Z/p` with `\Phi_{p^k}(1)=\Phi_p(1)=p`; `|P(n)|\ge2` gives `0` with `\Phi_n(1)=1` (via the new independent `lem:cyclotomicvalue`), so `[\Z\xrightarrow{1}\Z]` is acyclic too. ✔

**Citation loop gone.** `lem:cyclotomicvalue` (l.2051–2065) is self-contained
and cites only `\cite[Ch.~1]{IK}`; `lem:primstructure` cites it, not
`thm:degreelaw`. `thm:degreelaw`'s proof (l.2110–2122) now derives its first
equality *from* `lem:primstructure`+`def:degdet` and is reduced to a degree
statement. `thm:fourmodels`(a) (l.2249) cites `lem:primstructure`;
`thm:notmonoidal` (l.2149) cites `lem:primstructure`; `thm:shstructure`(v)
(l.2533–2538) now says "on the whole radical cube of Definition~\ref{def:prim}"
and cites `def:prim`+`lem:primstructure`, with the old hand-waving parenthesis
deleted. No statement any longer cites `thm:degreelaw` for structure. ✔

`main.md` carries Definition 5.1a (l.2106) and Lemma 5.1b (l.2122–2147) with
the same induction, Thm 5.3 reduced (l.2176–2195) and Thm 6.3(a) re-cited
(l.2490). ✔

## 3. B6 — the phase `\theta_p`: **RESOLVED; the companion does prove it**

`prop:tate` now states `\eqref{eq:zetap}`
`\zeta_p=p^{-1/2}e^{i(\tau\log p+\theta_p)}` with
`\theta_p=\arg\prod_{q\in S_f,q\ne p}\kappa_q(p)`, and `\eqref{eq:nophase}`
`\theta_p=0` on `\mathfrak c_0` (l.394–404), and `thm:qfinpositive` cites
`\eqref{eq:nophase}` (l.3153).

**Checked against Paper 43** (`43-row-a-torsion-theory/main.md`):
Theorem 9.11(a), l.2566–2570, defines
`\eta_p(\chi):=p^{-i\tau}\prod_{q\ne p}\kappa_q(p)^{-1}` and
`\zeta_p(\chi):=p^{-1/2}\overline{\eta_p(\chi)}`, with
`\widehat W_p(\chi)=(\log p)\cdot2\Rel(\zeta_p/(1-\zeta_p))` when `\kappa_p=1`;
its proof, l.2636–2639, states verbatim
`\zeta_p=p^{-1/2}e^{i(\tau\log p+\theta_p)}` for
`\theta_p:=\arg\prod_{q\ne p}\kappa_q(p)`; and Theorem 9.7b(c), l.2770–2773,
states `\theta_p\equiv0\ (\mathrm{mod}\ 2\pi)` "in particular on the principal
component `\mathfrak c_0:=(\varepsilon=0,\kappa_q=1\ \forall q)`". Paper 43
also supplies the bound `2(\log p)p^{-1/2}/(1-p^{-1/2})` per component, which
is `\eqref{eq:AS}`. **The import is exactly what the companion proves.** ✔
(See R2/6 for one sign typo in the transcription.)

## 4. Remaining R1 findings — per-finding status

| # | Severity | Status | Evidence |
|---|---|---|---|
| A1 | BLOCKING | **RESOLVED** | `\S 13` deleted with `prop:bystructure` and the second table; replaced by `\subsection*{Examples}` at l.2406 with one 7-row table and the single sentence "The following values illustrate Theorems~\ref{thm:separation} and~\ref{thm:degreelaw}." The l.269 clause is gone. Table entries spot-checked (`\#H^0(C_{\mathrm{fix}}(2))=1`, `\Phi_9(1)=3`, `\Phi_{30}(1)=1`). |
| A2 | MAJOR | **RESOLVED** | 192 occurrences of the string `label` in `main.tex`, all 192 of them the LaTeX macro `\label{`. Zero prose uses. `def:labelcat` is now the *index category*; "integer label" → "integer", "rational label" → "rational index". |
| A3 | MAJOR | **RESOLVED** | All six sites gone: no "we say so rather than", "smuggled in", "does and does not say/achieve", "rather than hiding it", "does not by itself produce one", "before any trace is computed". |
| B1 | BLOCKING | **RESOLVED** | `def:prim`, l.1964; `thm:shstructure`(v) restated on the radical cube, l.2533. |
| B2 | BLOCKING | **RESOLVED** | See R2/2. |
| B3 | MAJOR | **RESOLVED** | `def:degdet` (l.2067–2075) is now `\degdet K:=\sum_i(-1)^i\log\#H^i(K)` on complexes of finite type; `lem:degdetadd` (l.2077–2098) proves additivity on direct sums, sign under shift, and additivity on exact triangles via `\prod_j\#G_j^{(-1)^j}=1` for a bounded exact sequence of finite groups. Verified: `\degdet[\Z\xrightarrow{m}\Z]=\log|m|`, and the ad hoc `m=0` clause is gone. `\eqref{eq:degreelaw}` is now a consequence, not a convention. |
| B4 | MAJOR | **RESOLVED** | `\eqref{eq:cram}` is now derived: `L_{\pi_n}=[\pi_n^*\Omega\to\Omega]` with `\cite[II.1.2]{Illusie}`, `\cite[Tag 08UQ]{Stacks}`, `\Omega_{\mathbb G_m}=\mathcal O\,dz/z`, `\pi_n^*(dz/z)=n\,dz/z`, pulled back along `e` (l.1704–1715). `\eqref{eq:cfix}` is now explicitly *a definition* — the Koszul complex of the linearised fixed equation `w^{n-1}=1` at `w=1` — with the sentence "This is a definition, not a computation: no complex on an ambient affine line is needed below, and none is used." The false `R[z]` passage is deleted. Two new bibliography entries (`Illusie`, `Stacks`). |
| B5 | BLOCKING | **RESOLVED** | See R2/1. |
| B6 | MAJOR | **RESOLVED** | See R2/3. |
| B7 | MAJOR | **RESOLVED** | `thm:tateresidue`(iv) and its proof paragraph deleted; the theorem now has (i)–(iii) only. `rem:notchartinv` rewritten: it now reasons from (i)–(ii) ("each place carries one local Tate residue — `c_p/\log p` at finite `p` and `1` at `\infty` — and there are `|S_f|+1` of them; that count changes when a place is added"), with no Mittag–Leffler claim and no undefined `\eta_p`. |
| B8 | MAJOR | **RESOLVED** | `\eqref{eq:laplacescales}` (l.3617–3620) now asserts only exponential scales, `\lim\frac1L\log\widehat g_L(\rho_0)=\delta b`, `\lim\frac1L\log\widehat g_L(1-\bar\rho_0)=-\delta a`, with `a=\inf\supp\psi`, `b=\sup\supp\psi`, product scale `\delta(b-a)\le\delta/2`, equality iff `\supp\psi` spans `[1/2,1]` — verified, since `1/2\le a<b\le1`. The proof (l.3682–3697) supplies both bounds: upper by `\le L\|\psi\|_\infty e^{\delta Lb}`, lower by an interval `I\subset(b-\eta,b)` of positive length on which `\psi\ge\psi(u_0)/2`. The saddle sentence and the `e^{-c\sqrt{\delta L}}` claim are deleted, replaced by "Only the exponential scale is asserted: sub-exponential factors depend on the order of vanishing of `\psi` … and are not claimed here." (iii) now says "bounded in modulus by the resonant contribution" rather than "of the same order". (v) carries `0<\delta<\frac12` explicitly. |
| B9 | MAJOR | **RESOLVED** | `\eqref{eq:diagdivnorm}` is `-\log\frac1\varepsilon+O(1)`; `C_\varphi` is gone from the file, and a following sentence (l.3262) states "No limiting constant is asserted in `\eqref{eq:diagdivnorm}`: the proof produces …". |
| B10 | MAJOR | **RESOLVED** | `thm:fourmodels` (l.2225–2233) now reads "The constructions (a)–(c) below agree with `K_n` in `D(\Z)`, while (d) is a complex of `\Z[t]`-modules, namely `K_n\otimes_\Z\Z[t]`, whose specialisation at every `t=c\in\Z` is `K_n`"; the proof's closing sentence (l.2257–2260) is restricted accordingly. |
| B11 | MINOR | **RESOLVED** | `lem:cyclotomicvalue` now records "(The restriction `n>1` is forced here and everywhere below by `\Phi_1(1)=0`.)" |
| B12 | MAJOR | **RESOLVED** | `thm:frobincompletion`(ii), l.1642–1647: the argument now fixes `B`, hence `N_B,d_{N_B},C''_B`; notes that for every `N\ge N_B` the difference is supported on the *same* `d_{N_B}` components for every `G\in B`; and names `C_B:=d_{N_B}C''_B\max(A_S,B_S)`, "which is independent of `N`". The joint limit is now legitimate. |
| B13 | MINOR | **RESOLVED** | `lem:traceontinuity`'s proof now says "Here `0` may lie in `\supp h`, so Theorem~\ref{thm:radtrace} does not apply as stated; what is used instead is the *pointwise* vanishing of the unit packets …". |
| B14 | MINOR | **RESOLVED** | `thm:invsemigroup`(iii)'s proof now gives the converse explicitly: `\Delta^{(F)}=\Frob_{p_1}\star\Frob_{p_1}^\dagger\star\cdots\star\Frob_{p_k}\star\Frob_{p_k}^\dagger` and `\Frob_{r,F}` as a word for `r=a/b`. |
| B15 | MINOR | **RESOLVED** | `prop:trace` now defines `E_x` for `x\in C_S` as the point mass `\delta_x`, a multiplier, with `E_x\star E_y=E_{xy}`, `E_1=\Delta` (l.350–353). |
| C3 | MAJOR | **RESOLVED** | `main.md \S 12` "Corrections of record (2026-09-13)" records K1 (B5) and K2 (B2) accurately: what was stated, why it is wrong (including the `m=2,n=3,S_f=\{2,3,5\}` instance), what replaces it, and what is unaffected. The `\S 12` header states "Nothing is relabelled: both statements remain `PROVED`, one after a change of its content and one after the supply of a missing proof" — and indeed no grading in `main.md` was altered. The in-place edits carry `[ADDED 2026-09-13; see §12.]` markers at each site. |
| C4 | MINOR | **RESOLVED** | `\bibitem{Companion}` now reads "manuscript, 2026; available from the author". |
| E1 | MINOR | **RESOLVED** | `\Div`, `\divv`, `\Gr`, `\GL`, `\rk` deleted from the preamble. (`\Tr` and `\dd` are now unused; see R2/6.) |
| E2 | — | no change needed | title unchanged, as recommended. |
| F1 | MINOR | **RESOLVED** | `\S 1.4` now says `lem:singlefreq` "is used by no other statement here, and decides nothing about the location of any zero"; the false claim that `\S 12` uses it is gone. |
| F2 | MINOR | **RESOLVED** | `lem:singlefreq` opens "Assume, for this lemma only, that `\rho_0=\beta+i\gamma_0` is a zero with `0<\delta:=\beta-\tfrac12<\tfrac12`; parts (ii)–(v) are vacuous if no such zero exists." |

**21 of 21 findings resolved.** Nothing was resolved by deletion of
mathematics except `\S 13` and `thm:tateresidue`(iv), both of which R1
specified should be deleted.

## 5. Forbidden vocabulary — regrep of the current file

`grep -n -i -E "riemann hypothesis|\bRH\b|builder|auditor|honest|candid|PROVED|P1[0-9][0-9]|106_1|programme|corpus|repositor|of record|ledger|withdrawn|acceptance|\bcontract\b|\bstatus\b|verificat|\brows?\b|\bround\b|\blead \b"` returns five lines, all innocuous: four are ordinary uses of the verb "proved" ("what is proved is …", l.237, 1833, 2360, 3348) and one is `The square with rows $L_S\xrightarrow{m}L_S$ and …` (l.2513), the standard word for the rows of a commutative square. `check`/`checked`: **zero** occurrences. `label` as a word: **zero**. "Phase" occurs only in the analytic sense (l.3577, 3618-region, 3652). "Critical line" once, descriptively.

## 6. Compile

Three runs of `pdflatex -interaction=nonstopmode main.tex` from a clean state:

- errors: **0**
- LaTeX warnings after the third run: **0** (after the *second* run the file still reports `Label(s) may have changed`, so three runs are now needed, where two sufficed before — a consequence of the added lemmas shifting page breaks)
- undefined references / citations: **0**
- Overfull / Underfull boxes: **0**
- Output: `main.pdf`, **47 pages** (was 45).

## 7. Two cosmetic points for the author (neither blocks acceptance)

**R2-a (typo, sign of the exponent).** `\eqref{eq:zetap}` gives
`\zeta_p=p^{-1/2}e^{i(\tau\log p+\theta_p)}`, so with `\theta_p=0` one has
`\zeta_p=p^{-1/2}e^{i\tau\log p}=p^{-1/2+i\tau}`; but `\eqref{eq:nophase}`
writes `\zeta_p=p^{-1/2-i\tau}`. Paper 43's `\zeta_p=p^{-1/2}\overline{\eta_p}`
with `\eta_p=p^{-i\tau}\prod\kappa_q(p)^{-1}` also gives `p^{-1/2+i\tau}` on
`\mathfrak c_0`. The two adjacent displays therefore disagree in one sign.
Nothing depends on it — `2\Rel(\zeta/(1-\zeta))` is invariant under
`\zeta\mapsto\bar\zeta`, so `\widehat W_p` and every use of it in
`thm:qfinpositive` are unchanged — but `\eqref{eq:nophase}` should read
`\zeta_p=p^{-1/2+i\tau}`.

**R2-b (dead macros, again).** After the B4 rewrite `\Tr` and `\dd` are each
used exactly once (their own `\newcommand`). Delete them, as `\Div` etc. were.

---

# VERDICT R2: ACCEPT

All three BLOCKING findings and all eleven MAJOR findings of R1 are resolved,
and the two mathematical corrections were re-derived here independently rather
than taken on report: the four-case convolution computation and the
flat-convention identity `V_N(m)V_N(n)=c_N(m,n)\prod_{s\notin F}\vol(U_s)`
check out, and the induction in `lem:primstructure` proves both `H^{-1}=0` and
the cyclicity of `H^0` at every step, including the `|P|=2` case that was the
actual missing link. The citation loop is gone; `\Prim_n` is defined; the
`\degdet` convention is now a theorem rather than a stipulation; the phase
import is exactly what Paper 43 proves; the Laplace claim has been reduced to
what is provable and proved; and `\S 13` is gone, with the surviving
mathematics kept as a seven-row `Examples` table in the language of the rest
of the paper. Forbidden vocabulary is clean, the compile is clean at 47 pages,
and `main.md \S 12` records both corrections faithfully without relabelling.

The two items in R2/7 are typographic and can be fixed at proof stage.

**ACCEPT.**
