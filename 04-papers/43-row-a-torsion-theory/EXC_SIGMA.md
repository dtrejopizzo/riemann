# (Exc_σ) for Paper 43, Thm 5.4 Step 3: verdict and proof

**Verdict: PROVED** in the generality that Step 3 uses, and in fact for any continuous
unital endomorphism σ with σ(I) ⊆ I. The proof is self-contained (Wodzicki's
two-filtration argument, redone with twisted coefficients). It needs one hypothesis
slightly stronger than "B'(I) contractible": a **right-A-linear** splitting
h : I → I ⊗̂ I of multiplication. The splitting that Lemma 5.(hunital)/Lemma
(partition) already builds, h(a)=Σ e_i ⊗ ρ_i a with ρ_i ∈ I, has this property
automatically. No literature citation is needed.

Literature status, not used: Wodzicki 1989, Thm 3.1, and Brodzki–Lykova 2001 are
stated for the coefficients A, I, A/I. I did not verify a published twisted or
general-bimodule statement exactly, so I cite none; the lemma below makes the question
moot. (Plausible sources, not checked: Guccione–Guccione, JPAA 1996; Meyer 2010.)

## Hypotheses (H)
- A is a unital complete locally convex (e.g. Fréchet) algebra, and I ⊆ A is a closed two-sided ideal
  with a closed complement L ∋ 1 (A = L ⊕ I topologically; L need not be a subalgebra).
- σ: A → A is continuous, with σ(1)=1 and σ(I) ⊆ I.
- h: I → I ⊗̂ I is continuous linear with μ∘h = id_I and h(ab) = h(a)b for a ∈ I, b ∈ A
  (right A-linearity, where I ⊗̂ I is a right A-module through the second factor).

**Check that (H) holds in Step 3.** Case (i) is K = E_P ⊂ T = E_v^+ ⊗̂ E_{S∖v}^+ with σ = σ_v ⊗ σ'.
Case (ii) is I = E_v ⊂ Q' = C ⊕ E_v ⊕ J. In both cases the complement is the sum of the other
support summands (Step 2), and σ preserves each support summand.
The map h is h(a)=Σ_i e_i ⊗ ρ_i a, with e_i, ρ_i in the ideal (proof of Lemma hunital, "verbatim for E_V").
It converges absolutely by (summable) and satisfies μh = id. Because ρ_i(ab) = (ρ_i a)b, it is right
linear for every b in the ambient algebra, and the identity passes to the sum by continuity.
**Caveat for the editor:** the paper says that (summable) holds "verbatim" for E_V. This proof relies on that claim; Lemma hunital needs it in any case.

## LaTeX, ready to insert (replaces the hypothesis after Thm excision-input)

```latex
\begin{lemma}[Twisted excision]\label{lem:Excsigma}
Let $A$ be a unital complete locally convex algebra, $I\subseteq A$ a closed
two-sided ideal with a closed complement $L\ni1$, and $\sigma$ a continuous
unital endomorphism of $A$ with $\sigma(I)\subseteq I$.  Suppose there is a
continuous linear $h:I\to I\widehat\otimes I$ with $\mu\circ h=\id_I$ and
$h(ab)=h(a)b$ for $a\in I$, $b\in A$.  Then the inclusions
\[
C(I,I_\sigma)\ \hookrightarrow\ C(A,I_\sigma)\ \hookrightarrow\
\mathcal K:=\ker\bigl(C(A,A_\sigma)\to C(A/I,(A/I)_\sigma)\bigr)
\]
are quasi-isomorphisms; in particular $(\mathrm{Exc}_\sigma)$ holds.  The
hypothesis holds for every ideal $E_V$ used in Step~3 of
Theorem~\ref{thm:kunneth}, with $h(a)=\sum_ie_i\otimes\rho_ia$ as in
Lemma~\ref{lem:hunital}.
\end{lemma}

\begin{proof}
Write each letter of $A^{\widehat\otimes(n+1)}$ according to $A=L\oplus I$;
then $A^{\widehat\otimes(n+1)}$ is the finite topological direct sum of the
$2^{n+1}$ \emph{patterns} $X_0\widehat\otimes\cdots\widehat\otimes X_n$,
$X_j\in\{L,I\}$.  The map to $C_n(A/I,(A/I)_\sigma)\cong L^{\widehat\otimes(n+1)}$ is
the projection onto the pattern $L\cdots L$, so $\mathcal K_n$ is the sum of all
the other patterns.  $C_n(A,I_\sigma)$ is the sum of the patterns with
$X_0=I$, and $C_n(I,I_\sigma)$ is the pattern $I\cdots I$.  All three are
subcomplexes because $I$ is an ideal and $\sigma(I)\subseteq I$; the twisted
boundary is $b=\sum_{j<n}(-1)^jd_j+(-1)^nd_n$, with $d_j$ multiplying
$a_ja_{j+1}$ and $d_n(a_0\otimes\cdots\otimes a_n)=\sigma(a_n)a_0\otimes
a_1\otimes\cdots\otimes a_{n-1}$.  Each quotient complex below has a
filtration that is finite in each degree, so it is acyclic as soon as
each graded piece is acyclic.

\emph{Bar contraction.}  Put $s=h\otimes\id$ on
$B'_n(I)=I^{\widehat\otimes n}$.  Write $b'_{n+1}=\mu\otimes\id-\id_I\otimes
b'_n$ on $I\widehat\otimes I^{\widehat\otimes n}$, and note that
$(\id\otimes\mu)(h\otimes\id_I)=h\circ\mu$ by right linearity.  Then
$b's+sb'=\id$ in every degree $n\ge1$ (in degree $1$, $b's=\mu h=\id$).  The
same identity holds for $s\otimes\id_Y$ on $B'(I)\widehat\otimes Y$, for any
complete space $Y$.

\emph{Step 1: $C(I,I_\sigma)\to C(A,I_\sigma)$.}  The quotient $R$ is spanned
by patterns with $X_0=I$ in which some $X_j=L$, $j\ge1$.  Let $m\ge1$ be the
first such $j$ and put $q:=n-m+1$.  The face $d_j$ with $j<m-1$ preserves
$q$.  The faces $d_{m-1}$ (an $I$ letter times an $L$ letter lies in $I$) and
$d_j$ with $j\ge m$ lower $q$, or send the word to $C(I,I_\sigma)$.  The twisted face
lowers $q$ by one if $m<n$; if $m=n$ it sends the word into $C(I,I_\sigma)$.  Hence
$G_s=\{q\le s\}$ is a filtration by subcomplexes, and
$G_s/G_{s-1}\cong B'(I)\widehat\otimes Y_s$ with
$Y_s=L\widehat\otimes A^{\widehat\otimes(s-1)}$.  Its differential is $\pm b'$ on
the head $a_0\otimes\cdots\otimes a_{m-1}$; no face acts on $Y_s$.  By the bar
contraction, each graded piece is contractible.

\emph{Step 2: $C(A,I_\sigma)\to\mathcal K$.}  The quotient $Q$ is spanned by
patterns with $X_0=L$ and some $X_j=I$, $j\ge1$.  Let $m$ be the first such
$j$ and put $r:=m-1$.  The faces $d_j$ with $j\le m-1$ lower $r$, or send the word
to $C(A,I_\sigma)$.  The faces $d_j$ with $j\ge m$ and the twisted face (when
$m<n$) preserve $m$; when $m=n$ the twisted face lands in $C(A,I_\sigma)$.  So
$F_r=\{m-1\le r\}$ is a filtration.  The piece $F_r/F_{r-1}$ has terms
$L\widehat\otimes L^{\widehat\otimes r}\widehat\otimes I\widehat\otimes
A^{\widehat\otimes k}$.  Rotating the head
$X:=L\widehat\otimes L^{\widehat\otimes r}$ to the right identifies it, up to
the global sign $(-1)^m$, with the complex
$\mathcal B_k=I\widehat\otimes A^{\widehat\otimes k}\widehat\otimes X$ with
\[
\partial(a\otimes b_1\otimes\cdots\otimes b_k\otimes x)=ab_1\otimes\cdots
+\sum_{j=1}^{k-1}(-1)^j\cdots\otimes b_jb_{j+1}\otimes\cdots
+(-1)^ka\otimes b_1\otimes\cdots\otimes b_{k-1}\otimes b_k\cdot x ,
\]
where $X$ is the left $A$-module $b\cdot(l_0\otimes y)=\pi_L(\sigma(b)l_0)\otimes y$.  This is a module because $\sigma(b)\pi_I(\cdot)\in I$, and
$I\cdot X=0$ because $\sigma(I)\subseteq I$.  Let
$\mathrm{Bar}_k=A\widehat\otimes A^{\widehat\otimes k}\widehat\otimes X$ be the
bar resolution of $X$; its continuous contraction
$t(c)=1\otimes c$ shows that $H(I\widehat\otimes\mathrm{Bar})=I\widehat\otimes X$
in degree $0$, through $\id\otimes\varepsilon$.  The maps
$\Phi=h\otimes\id:\mathcal B\to I\widehat\otimes\mathrm{Bar}$ (viewing
$h:I\to I\widehat\otimes A$) and $\Psi(a\otimes b_0\otimes c)=ab_0\otimes c$
are chain maps (for $\Phi$ this is exactly right linearity) with
$\Psi\Phi=\mu h\otimes\id=\id$; hence $H_k(\mathcal B)=0$ for $k\ge1$.  In
degree $0$, $\partial_1=\mu\otimes\id_X-\id_I\otimes\mathrm{act}$ on
$I\widehat\otimes A\widehat\otimes X$, and since $h$ takes values in
$I\widehat\otimes I$ and $I\cdot X=0$,
$\partial_1\circ(h\otimes\id_X)=\mu h\otimes\id-
(\id\otimes\mathrm{act})(h\otimes\id)=\id_{I\widehat\otimes X}-0$.  So
$\partial_1$ is onto and $H_0(\mathcal B)=0$.  Thus each graded piece is
acyclic.
\end{proof}
```

## Adversarial check (self-audit)
1. *Coefficient trap.* Wodzicki's theorem is for coefficients A, I, A/I. The argument above never invokes
   it. Step 1 needs only the contraction of B'(I), because the twisted face lowers the
   filtration. Step 2 needs the right-linear splitting, which is why (H) is stated explicitly. Plain
   algebraic H-unitality would also suffice there, through Wodzicki's Tor-vanishing, but that is not needed.
2. *Filtration directions.* Both directions were checked face by face, including the products L·L that
   create I-components: these only move the first-I position to the left (Step 2) or send the word to the
   subcomplex. In Step 1 they can only move the first-L position to the right, which lowers q. Both
   filtrations are finite in each degree (0 ≤ r ≤ n−1, 1 ≤ s ≤ n).
3. *Degree 0 / degree 1.* In Step 1, B'_1 = I has b'=0 and b's = μh = id. In Step 2, H_0 needs I·X=0, which
   holds because σ(I) ⊆ I. Without that condition the argument fails, as it should.
4. *Topology.* Every map is a finite composite of multiplications, σ, π_L, h, and unit insertions, so
   all are continuous. The pattern decomposition is a finite topological direct sum. The conclusion is a
   quasi-isomorphism of algebraic homology, which is what eq. (25) asserts. No closed-range claim is made.
5. *Signs.* The rotation multiplies the whole graded differential by (−1)^m, which leaves homology
   unchanged.
6. *The H_0 step* uses only that h takes values in I ⊗̂ I and that I·X = 0. Then ∂_1∘(h⊗id) = id on
   I ⊗̂ X, so ∂_1 is surjective. An earlier draft of this step went through ρ_i explicitly; it was
   replaced by this argument, which uses neither the form of h nor right linearity.

## Consequences (for the editor, not applied)
If the lemma is inserted, Thm 5.4, Thm 5.12(b), and the global part of Cor 5.14 become unconditional,
provided Lemma hunital holds for E_V. Remark 5.5 and the README/REPAIRS status lines would then need
updating. main.tex has NOT been edited.
