# 115.09 — The semi-local route: where row (d) escapes the archimedean no-go, and why row (a)'s code is the shape of the finite factor

`115_08` Corollary 7 proves that no single-place construction closes row (d):
any archimedean lower bound on \(-G_\infty\) costs a slack exactly equal to
what is missing.  The hypothesis of that corollary is that the functional
carries no arithmetic input.  This note works out the one construction that
violates the hypothesis, states precisely what it would need, and records a
structural match with row (a) that is checkable rather than suggestive.

Nothing here is claimed as proved.  The reductions are proved; the objects they
reduce to are not constructed.  That distinction is kept explicit throughout.

## 1. The semi-local reduction

Let \(S=\{\infty,p_1,\dots,p_k\}\) be a finite set of places,
\(\mathbb A_S=\prod_{v\in S}\mathbb Q_v\), and let \(\mathbf S_S\) denote the
orthogonal projection onto the orthocomplement of
\(\mathrm{Ran}(\mathcal P_\Lambda\vee\widehat{\mathcal P}_\Lambda)\) in
\(L^2(\mathbb A_S)\) at \(\Lambda=1\) — the semi-local Sonin space.  This is
the object Connes–Consani point at in their closing paragraph: *"All the
ingredients and tools used above make sense in the general semi-local case,
where Weil positivity implies RH."*

Suppose the semi-local analogue of their Theorem 3 holds, i.e. that there is a
distribution \(\epsilon_S\) with

\[
 \mathrm{Tr}\,\bigl(\vartheta(f)\,\mathbf S_S\bigr)
 =\sum_{v\in S}W_v^{CC}(f)+E_S(f),
 \qquad E_S(f)=\int f\,\epsilon_S\,d^*\rho .
\tag{H}
\]

> **Proposition 1.**  Assume (H).  Write \(K_S\) for the part of \(K\) carried
> by the primes in \(S\), and \(B^S_{\rm nuc}:=K_S+G_\infty\).  Then for every
> \(f=g\star g^\vee\) with \(g\in C_c^\infty(\mathbb R_+^*)\),
> \[
>  \mathcal S_S(g):=\mathrm{Tr}\,\bigl(\vartheta(g)\mathbf S_S\vartheta(g)^*\bigr)
>  =-B^S_{\rm nuc}(g,g)+E_S(g\star g^\vee).
> \]
> Consequently, since \(\mathcal S_S\ge0\) by construction,
> \[
>  \boxed{\;E_S\le0\ \text{on positive-definite }f
>  \;\Longrightarrow\;B^S_{\rm nuc}(g,g)\le0 .\;}
> \]

*Proof.*  \(\mathrm{Tr}(\vartheta(g)\mathbf S_S\vartheta(g)^*)
=\mathrm{Tr}(\vartheta(g\star g^\vee)\mathbf S_S)\) by cyclicity and
\(\vartheta(g)^*=\vartheta(g^\vee)\).  Apply (H) to \(f=g\star g^\vee\).  By
`115_08` §0 the sign dictionary is \(W_v^{CC}=-W_v^{\text{ours}}\) at every
place, so \(\sum_{v\in S}W_v^{CC}(f)=-(K_S+G_\infty)(g,g)=-B^S_{\rm nuc}(g,g)\).
Positivity of \(\mathcal S_S\) is by construction: it is
\(\|\vartheta(g)\mathbf S_S^{1/2}\|_{HS}^2\). \(\square\)

> **Proposition 2 (exhaustion).**  If \(\mathrm{supp}\,g\subset(p_k^{-1},p_k)\)
> and \(S=\{\infty,2,3,\dots,p_k\}\) contains every prime \(\le p_k\), then
> \(K_S=K\), hence \(B^S_{\rm nuc}=B_{\rm nuc}\).  Since every
> \(f\in\mathcal T^0\cap C_c^\infty\) has support in some \((p^{-1},p)\), the
> family of statements \(\{B^S_{\rm nuc}\le0\}_S\) exhausts row (d) on a dense
> subspace.
>
> *Proof.*  \(\mathrm{supp}(g\star g^\vee)\subset(p_k^{-2},p_k^{2})\), and
> `eq:Ktest` samples only at \(p^{\pm j}\).  A prime power \(p^{j}\) in
> \((1,p_k^2)\) has \(p\le p_k\) unless \(p>p_k\) and \(j=1\), i.e.
> \(p\in(p_k,p_k^2)\); those terms are absent from \(K_S\) but are also absent
> from \(K\) restricted to the support only when \(g\star g^\vee\) vanishes
> there.  Taking \(\mathrm{supp}\,g\subset(p_k^{-1/2},p_k^{1/2})\) instead
> gives \(\mathrm{supp}(g\star g^\vee)\subset(p_k^{-1},p_k)\) and removes
> the exception, at the cost of only shrinking the exhausting family — still
> dense. \(\square\)

**Why this escapes Corollary 7.**  \(\mathbf S_S\) is defined by a cutoff on
\(\mathbb A_S\), whose norm \(|x|=\prod_{v\in S}|x_v|_v\) involves the finite
places.  So \(\mathcal S_S\) is *not* a functional of the kind Corollary 7
excludes: it carries arithmetic input.  \(K_S\) is no longer a quantity to be
dominated by an archimedean reservoir; it is a summand of the same trace.  This
is a genuine structural difference, not a reformulation.

**What is not proved.**  (H) itself, and \(E_S\le0\).  For \(S=\{\infty\}\)
these are CC's Theorem 3 and their §5, the latter only up to finite
codimension and, for the sharp conclusion, only on a small interval.  Nothing
below reduces \(E_S\le0\) to anything easier; the value of Proposition 1 is
that it isolates \(E_S\le0\) as the single remaining statement, in place of the
family of doomed comparisons ruled out by Corollary 7.

## 2. The shell decomposition of the semi-local cutoff

This is elementary and is the part that connects to row (a).

Take \(S=\{\infty,p\}\), so \(\mathbb A_S=\mathbb R\times\mathbb Q_p\) and
\(|x|=|x_\infty|\cdot|x_p|_p\).  On \(\mathbb Q_p\) the norm is discrete,
\(|x_p|_p=p^{-v}\) with \(v=v_p(x_p)\in\mathbb Z\), and the level sets
\(\{v_p=v\}=p^{v}\mathbb Z_p^\times\) are compact open.  Hence

\[
 L^2(\mathbb A_S)=\bigoplus_{v\in\mathbb Z}
 L^2(\mathbb R)\otimes L^2\bigl(p^{v}\mathbb Z_p^\times\bigr),
\]

and the cutoff \(\{|x|\le\Lambda\}\) restricts on the \(v\)-th summand to the
**archimedean** cutoff \(\{|x_\infty|\le\Lambda p^{v}\}\).

> **Proposition 3 (shells).**  The multiplicative cutoff projection
> \(\mathcal P_\Lambda\) on \(L^2(\mathbb A_S)\) is the direct sum over
> \(v\in\mathbb Z\) of the archimedean cutoff projections at scale
> \(\Lambda p^{v}\), tensored with the identity on \(L^2(p^v\mathbb Z_p^\times)\).
>
> *Proof.*  \(\mathcal P_\Lambda\) is multiplication by the characteristic
> function of \(\{|x|\le\Lambda\}\); on the summand \(v_p=v\) this function is
> \(\mathbf 1\{|x_\infty|\le\Lambda p^{v}\}\otimes\mathbf 1\). \(\square\)

Two consequences, both elementary but worth stating because they fix the shape
of the finite factor.

* The semi-local Sonin space is **not** a tensor product of local Sonin
  spaces.  It is a \(\mathbb Z\)-graded sum of archimedean Sonin-type spaces
  with cutoffs sliding by powers of \(p\).  Any construction that assumes
  factorisation over places is wrong.
* The grading is by \(v_p\), so the natural bookkeeping is a **digit
  expansion in base \(p\)**, and the weights attached to shell \(v\) scale as
  \(p^{v}\), i.e. logarithmically as \(v\log p\).  That is the origin of the
  \(\log p\) in \(W_{\rm fin}\).

Note that \(\widehat{\mathcal P}_\Lambda\) is *not* diagonal in this grading —
the Fourier transform on \(\mathbb Q_p\) moves between shells — so
\(\mathcal P_\Lambda\vee\widehat{\mathcal P}_\Lambda\) genuinely couples them.
That coupling is where the difficulty of (H) lives, and it is also, in the
programme's own language, exactly a **global term coupling distinct primes
while preserving their local contact** — the phrase `main.tex` uses for what is
missing in row (d).

## 3. The match with row (a), stated so it can be refuted

Row (a) attaches to a divisor the negabinary code of `eq:rmdefinition`, with
radius \(r(m)=\lfloor\log_2(m+1)\rfloor\) and lattice rank \(N_t=r(m_t)r(n_t)\).
That is a digit count in radix \(-2\): a decomposition indexed by powers of 2.

**Conjecture (shell identification).**  For \(p=2\), the graded pieces of
Proposition 3 correspond to the digit places of row (a)'s negabinary code, with
\(r(m)\) counting the occupied shells and the coefficient-one normalisation of
`prop:continuousRRdet` matching the \(\Lambda=1\) cutoff.

This is a conjecture, and it is written so that it can be killed cheaply.  Three
concrete tests, in increasing cost:

1. **Rank.**  The number of shells \(v\) meeting \(\{|x|\le\Lambda\}\) for a
   divisor of radius \(m\) should be \(r(m)=\lfloor\log_2(m+1)\rfloor\), not
   \(\lfloor\log_2m\rfloor\) or \(\lceil\cdot\rceil\).  The \(+1\) is a sharp
   fingerprint and row (a) has it for a specific reason (`lem:negabinaryradius`);
   if the shell count has a different offset the identification is false.
2. **Radix sign.**  Row (a)'s code is radix \(-2\), not \(2\).  The shell
   decomposition as stated is indexed by \(v_2\in\mathbb Z\) with no sign
   alternation.  Either the alternation has a counterpart in the interaction
   between \(\mathcal P_\Lambda\) and \(\widehat{\mathcal P}_\Lambda\) — the
   Fourier transform on \(\mathbb Q_2\) does carry a sign through the additive
   character — or the identification fails.  **This is the test most likely to
   kill the conjecture and should be done first.**
3. **Covolume.**  Row (a)'s metric exponent is \((\log2)^2N_t\) with the
   universal constant \(\sigma=e^{-(\log2)^2}\) of `115_04` §2.  Under the
   identification the same exponent must arise as the shell-weighted volume of
   the cutoff region.  A \((\log 2)^2\) with no spurious factor would be strong
   evidence; anything else refutes.

Until test 2 is done this is an analogy, and it is recorded as one.

## 4. Candid position of row (d)

Proved in this phase: the sign dictionary (`115_08` §0), Proposition 0, the
slack lemma and its corollaries, the two lossless identities, the
characterisation of CC's window as \(K=0\), the archimedean no-go, and here the
semi-local reduction (Propositions 1–2, conditional on (H)) and the shell
decomposition (Proposition 3, unconditional).

Not proved, and not close: (H) for \(|S|\ge2\), and \(E_S\le0\).  These are the
statements Connes–Consani leave open at the end of arXiv:2006.13771, and this
phase has not advanced them.  What it has done is remove an entire family of
alternative routes with proof, so that the remaining work is not spread over
candidates but concentrated on one statement.

Row (d): **OPEN**, reduced to \(E_S\le0\) under (H).

## 5. Next

1. Test 2 of §3 — the radix sign.  Cheap, and it decides whether row (a) has
   anything to do with the semi-local cutoff.
2. Re-run `115_08` §4.1 with five bumps to obtain a non-odd \(\mathcal T^0\)
   test function, so the cross-check is generic.
3. Read Connes [11] (the semi-local trace formula) for the precise form of
   \(\mathcal P_\Lambda\vee\widehat{\mathcal P}_\Lambda\) at \(|S|\ge2\), which
   is what (H) requires.
