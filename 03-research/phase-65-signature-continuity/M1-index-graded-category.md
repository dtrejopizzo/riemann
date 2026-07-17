# M1 — The index-graded category $\mathcal G$: language for signature-continuity

**Phase 65, milestone M1.** Pure mathematics. Goal: define the category in which the Signature-Continuity
Theorem (`PROBLEM-STATEMENT.md` §4) is even a statement — objects that are entire functions *carrying* a
Kreĭn–Langer index, morphisms that *track* the index, and the index realized as a functor. We prove the
structural lemmas that are provable at the language level and state precisely the two interfaces M2
(topology/limit) and M3 (closedness) must fill. Nothing here uses RH; nothing here is claimed to prove
RH. M1 succeeds if the category is well-defined, $E_P$ and $\Xi$ are objects, the index is functorial,
and Davenport–Heilbronn is distinguished from $\zeta$ at the language level.

---

## §1. Substrate: generalized Nevanlinna functions and Pontryagin spaces (recollection)

We build on the classical Kreĭn–Langer theory; we recall only what we need, then add the new grading.

\begin{definition}[generalized Nevanlinna class $\mathcal N_\kappa$]
For $\kappa\in\Z_{\ge0}$, a function $q$ meromorphic on $\C\setminus\R$ with $q(\bar z)=\overline{q(z)}$
belongs to $\mathcal N_\kappa$ iff the Nevanlinna kernel
\[
   \mathsf N_q(z,w)=\frac{q(z)-\overline{q(w)}}{z-\bar w}
\]
has \textbf{exactly $\kappa$ negative squares}: every finite Hermitian matrix
$\big(\mathsf N_q(z_i,z_j)\big)_{i,j}$ has at most $\kappa$ negative eigenvalues, and $\kappa$ is
attained. We write $\kappa(q)=\mathrm{ind}_-\mathsf N_q$.
\end{definition}

$\mathcal N_0$ is the classical Nevanlinna (Herglotz/Pick) class. By Kreĭn–Langer, $q\in\mathcal N_\kappa$
has an essentially unique representation via a self-adjoint relation in a \textbf{Pontryagin space}
$\Pi_\kappa$ (Hilbert space with a $\kappa$-dimensional negative part), and $\kappa$ is the negative
index of that space.

\begin{definition}[Hermite–Biehler / de Branges side]
An entire $E$ is \textbf{Hermite–Biehler} (HB) if $|E(z)|>|E^\#(z)|$ for $\Im z>0$, where
$E^\#(z)=\overline{E(\bar z)}$. Then $q_E=E^\#/E$ (or the associated Weyl function) lies in
$\mathcal N_0$. The de Branges space $\mathcal H(E)$ is a Hilbert space. The
\textbf{generalized} (Pontryagin) de Branges spaces $\mathcal H_\kappa(E)$ attach to $E$ with
$q_E\in\mathcal N_\kappa$; then $\mathcal H_\kappa(E)$ is a Pontryagin space of negative index $\kappa$.
\end{definition}

\textbf{Dictionary with Phase 64.} $E_P=$ structure function of the positive von Mangoldt system; $G2$
gives $q_{E_P}\in\mathcal N_0$, $\kappa(E_P)=0$. $G5$ gives $\kappa(\Xi$-companion$)=\#\{$off-line
zeros$\}$. So "the index of $\Xi$" is literally the negative index of the Pontryagin space
$\mathcal H_\kappa(E_\Xi)$. \emph{The category below makes the assignment $E\mapsto\kappa(E)$ a functor,
so that a limit statement about $\kappa$ becomes meaningful.}

---

## §2. The objects of $\mathcal G$

\begin{definition}[index-graded analytic object]\label{def:obj}
An \textbf{object} of $\mathcal G$ is a pair $\mathsf E=(E,\Pi)$ where
\begin{itemize}
\item $E$ is an entire function, real ($E^\#=\pm E$) on $\R$ up to the de Branges normalization, of
finite exponential type, with $q_E\in\mathcal N_{\kappa}$ for some $\kappa<\infty$;
\item $\Pi=\mathcal H_\kappa(E)$ is its (Pontryagin) model space, carrying the indefinite inner product
$[\cdot,\cdot]_\Pi$ of negative index $\kappa$.
\end{itemize}
We write $\kappa(\mathsf E)=\kappa=\mathrm{ind}_-\Pi$. The objects with $\kappa=0$ form the full
subcategory $\mathcal N_0\subset\mathcal G$ (the Hilbert / Hermite–Biehler objects).
\end{definition}

\begin{remark}[why a pair, not just $E$]
The grading datum is \emph{not} recoverable from $E$ as a bare entire function up to the information that
already failed us (N1: determinants are signature-blind). Carrying the model space $\Pi$ \emph{with} $E$
is the categorical device that defeats signature-blindness: morphisms will see $\Pi$, hence see
$\kappa$. This is the one structural decision of M1.
\end{remark}

\textbf{Two distinguished objects (the endpoints of the renormalization).}
\[
   \mathsf E_P=(E_P,\ \mathcal H(E_P)),\ \ \kappa=0;\qquad
   \mathsf E_\Xi=(E_\Xi,\ \mathcal H_\kappa(E_\Xi)),\ \ \kappa=\kappa(\Xi).
\]
By G2 and G5 these are objects of $\mathcal G$; M4 will pin $E_P,E_\Xi$ to $\zeta$.

---

## §3. The morphisms of $\mathcal G$

We need morphisms that (i) include the elementary moves of de Branges theory (isometric inclusions of
model spaces) and (ii) \emph{record} index change, so that the index becomes functorial and a definite-
signed perturbation is visible as a one-sided move.

\begin{definition}[morphism]\label{def:mor}
A \textbf{morphism} $\Phi:\mathsf E\to\mathsf E'$ is a pair $\Phi=(\iota,\,\sigma)$ where
\begin{itemize}
\item $\iota:\Pi\hookrightarrow\Pi'$ is a (possibly partial) \textbf{contractive} map of Pontryagin
spaces that is isometric on a subspace of finite codimension/corank (a de Branges-type inclusion,
allowing a finite-rank defect);
\item $\sigma\in\Z$ is the \textbf{signature defect} of $\iota$: $\sigma=\mathrm{ind}_-\Pi'-
\mathrm{ind}_-\iota(\Pi)$, the number of negative squares created on the complement of the image.
\end{itemize}
Composition $(\iota',\sigma')\circ(\iota,\sigma)=(\iota'\iota,\ \sigma+\sigma')$. The identity is
$(\mathrm{id},0)$.
\end{definition}

\begin{definition}[the index functor]\label{def:functor}
Let $\kappa:\mathcal G\to(\Z_{\ge0},\le)$ send $\mathsf E\mapsto\mathrm{ind}_-\Pi$ on objects and
$\Phi=(\iota,\sigma)\mapsto\sigma$ on morphisms, recording the index change. Then for $\Phi:\mathsf E\to
\mathsf E'$,
\[
   \kappa(\mathsf E')=\kappa(\mathsf E)+\sigma_\Phi-d_\Phi,
\]
where $d_\Phi\ge0$ is the corank of $\iota$ on the negative part (negative squares lost to the defect).
On \textbf{exact} morphisms ($\iota$ isometric, $d_\Phi=0$) this reads $\kappa(\mathsf E')=
\kappa(\mathsf E)+\sigma_\Phi$.
\end{definition}

\begin{lemma}[functoriality of the index]\label{lem:functor}
$\kappa$ is a functor to the poset $(\Z_{\ge0},\le)$ along the subcategory $\mathcal G^{+}$ of
\textbf{monotone} morphisms (those with $\iota$ isometric, $d_\Phi=0$, $\sigma\ge0$): along $\mathcal
G^+$, $\kappa$ is non-decreasing, and $\sigma_\Phi=0\Rightarrow\kappa$ preserved.
\end{lemma}
\emph{Proof.} Composition adds $\sigma$ (Def.~\ref{def:mor}); on $\mathcal G^+$, $d_\Phi=0$ so
$\kappa(\mathsf E')=\kappa(\mathsf E)+\sigma_\Phi$ (Def.~\ref{def:functor}), and $\sigma_\Phi\ge0$ gives
monotonicity; identities give $\sigma=0$. $\square$

\begin{remark}[what Lemma~\ref{lem:functor} buys]
The index is now a \emph{functor}, not a bare number: index change is carried by morphisms and is
\emph{additive}. This is exactly the structure needed to phrase "the index does not jump" as "the
renormalization morphism has $\sigma=0$." M3's task becomes: \emph{show the renormalization is a
monotone morphism with $\sigma=0$}, i.e. lives in $\mathcal G^+$ and creates no negative square.
\end{remark}

---

## §4. The renormalization as a morphism-limit (interface to M2)

The renormalization $A_P\to A_\infty$ (G3–G4) should be a morphism $\Phi_\infty:\mathsf E_\infty\to
\mathsf E_\Xi$ obtained as a limit of the finite inclusions. At the language level we can only *type* it;
M2 must *construct* the limit.

\begin{definition}[renormalization tower]\label{def:tower}
The finite systems give exact monotone inclusions $\mathsf E_P\to\mathsf E_{P'}$ ($P<P'$) of the model
spaces (adding prime cells; de Branges nesting). All lie in $\mathcal N_0$ ($\sigma=0$, G2). The
renormalization is the formal colimit/limit $\mathsf E_\infty=\text{``}\lim_P\text{''}\,\mathsf E_P$
together with a comparison morphism $c:\mathsf E_\infty\to\mathsf E_\Xi$ (G3: $\widetilde D(A_\infty)=
\Xi$).
\end{definition}

\begin{openinterface}{M2 must supply}
A topology/uniformity $\tau_\kappa$ on $\mathcal G$ (or on a subcategory containing the tower) in which
(T2) the tower $\{\mathsf E_P\}$ \textbf{converges} to $\mathsf E_\infty$ and the comparison $c$ is an
\textbf{isomorphism} $\mathsf E_\infty\cong\mathsf E_\Xi$ (so the renormalized limit really is the
$\Xi$-object, not merely sharing a determinant). Equivalently: realize $\text{``}\lim\text{''}$ of
Def.~\ref{def:tower} as an actual colimit in a $\tau_\kappa$-complete enrichment of $\mathcal G$.
\end{openinterface}

\begin{openinterface}{M3 must supply}
That the limit morphism $\Phi_\infty=c\circ(\lim_P\!\text{incl}):\mathsf E_P\to\mathsf E_\Xi$ is
\textbf{monotone with $\sigma=0$} — no negative square is created in the limit — using G4 (the only
divergence is rank-one and \textbf{definite-signed}). Then by Lemma~\ref{lem:functor}
$\kappa(\mathsf E_\Xi)=\kappa(\mathsf E_P)=0$.
\end{openinterface}

With both interfaces filled, the assembly (M5) is Lemma~\ref{lem:functor}: $\kappa(\Xi)=0$, RH.

---

## §5. The Davenport–Heilbronn falsifier at the language level

\begin{proposition}[DH is distinguished in $\mathcal G$]\label{prop:dh}
Let $H^\chi_P$ be the \emph{signed} Davenport–Heilbronn Hamiltonian (twisted local masses
$\mu_p^\chi$ of mixed sign). Then the associated kernel $K_P^\chi$ is indefinite already at finite $P$
(Phase 64, G2-analogue fails), so $q_{E_P^\chi}\in\mathcal N_{\kappa_P}$ with $\kappa_P>0$ for some
finite $P$; the finite DH objects are \textbf{not} in $\mathcal N_0$.
\end{proposition}
\emph{Proof.} The Gram identity gives $K_P=\int Y^*H_PY$; for $H_P\ge0$ this is $\succeq0$ (G2), but for
the signed $H^\chi_P$ the integrand is indefinite and the negative index of $K_P^\chi$ is $>0$ once a
sign change occurs in the local masses, which happens at finite $P$ for the DH twist. Hence
$\kappa(\mathsf E^\chi_P)>0$. $\square$

\begin{resultbox}
\textbf{Built-in falsifier confirmed at M1.} For $\zeta$, every finite object is in $\mathcal N_0$
($\kappa=0$), so "index continuity" can possibly give $\kappa(\Xi)=0$. For DH, the finite objects are
\emph{already} outside $\mathcal N_0$, so no continuity argument can or should give index $0$ — exactly
as required (DH has off-line zeros). The category therefore separates $\zeta$ from DH \emph{at the level
of objects}, before any topology is built. Any later step that fails to use $H_P\ge0$ (and would thus
apply to DH) is wrong by this Proposition.
\end{resultbox}

---

## §6. What M1 has established, and what it has not

\textbf{Established (definitions + language-level lemmas, no RH used):}
\begin{itemize}
\item $\mathcal G$: objects $(E,\Pi)$ graded by Kreĭn–Langer index (Def.~\ref{def:obj}); morphisms
$(\iota,\sigma)$ recording signature defect (Def.~\ref{def:mor}); the index \textbf{functor} $\kappa$
(Def.~\ref{def:functor}).
\item \textbf{Functoriality} (Lemma~\ref{lem:functor}): along monotone morphisms $\mathcal G^+$, index is
additive in $\sigma$ and non-decreasing; $\sigma=0\Rightarrow$ index preserved. \emph{This is the precise
sense in which "index does not jump" $=$ "$\sigma=0$."}
\item Endpoints $\mathsf E_P\ (\kappa=0)$ and $\mathsf E_\Xi\ (\kappa=\kappa(\Xi))$ are objects;
renormalization typed as a morphism-limit (Def.~\ref{def:tower}).
\item \textbf{DH separated at the object level} (Prop.~\ref{prop:dh}): the falsifier is structural, not
incidental.
\end{itemize}

\textbf{Not established (the two interfaces — the real theorems, M2 and M3):}
\begin{itemize}
\item \emph{(M2)} the $\tau_\kappa$-completion in which the tower converges and $c$ is an isomorphism —
the analytic content (N3 must be defeated: the renormalized limit is not classical).
\item \emph{(M3)} that $\Phi_\infty$ is monotone with $\sigma=0$ — the conceptual content (G4's definite
sign $\Rightarrow$ no negative square created). This is where RH actually lives.
\end{itemize}

\textbf{Honest status.} M1 is \emph{definitional scaffolding with two genuine lemmas}
(functoriality; DH separation). It does not approach RH; it makes "index-continuity" a precise
categorical statement ($\sigma_{\Phi_\infty}=0$) and hands M2/M3 well-posed targets. The decisive
reduction achieved: \textbf{RH $=$ the renormalization morphism $\Phi_\infty$ lies in $\mathcal G^+$ with
signature defect $\sigma=0$}, to be proved from $H_{\mathrm{vM}}\ge0$ and the definite-signed rank-one
divergence. No false victory; M1 is language, and it is now in place.

Next document: `M2-pole-relative-completion.md` (construct $\tau_\kappa$ and the limit), or
`M3-signature-closedness.md` if attacking the conceptual heart first.
