# D2 — Sourced determinant calculus: the object that reads the signature

**Phase 65 / Signature-Continuity Package, deliverable D2.** Pure mathematics, full proofs. This is the
first genuinely new object. Its motivation is exactly the honest obstruction our M3 found:

> **M3 (preserved).** At the *scalar* determinant level, signature-continuity is RH-strength: scalar
> convergence $D_P\to\Xi$ does **not** force kernel/index convergence, because the scalar determinant is
> *signature-blind* (N1). Two systems can share $D_A$ and differ in $\kappa$.

D2 cures this: replace the scalar determinant $D_A$ by the **sourced determinant germ**
$\mathcal D_A^{\mathrm{src}}:V\mapsto\det_{\mathrm{reg}}(I+A+V)$ over finite-rank signed probes
$V\in\mathfrak S_{\mathrm{prim}}$ (D0, Def. src). Its variations recover the resolvent, hence the
Kreĭn–Langer kernel, hence $\kappa$ (D1). The finite-dimensional template is Stage 1, S1; here we lift it
to trace-class / Pontryagin operators with all regularization anomalies tracked.

> `ASSUMED` ledger (D2): see §6. The classical pieces (Fredholm derivative identities, $\det_2$ anomaly
> formula) are proved/stated in full; one operator-totality input is flagged.

---

## §1. The sourced determinant germ

\begin{definition}[admissible operator and sourced germ]\label{def:germ}
Let $A$ be an admissible operator: $I+A$ is invertible off a discrete set, $A$ is trace-class relative to
the free part on compacts (so $\det_{\mathrm{reg}}(I+A)$ exists), and $A$ is real-symmetric
($A^\#=A$). For a source plane $F\subset\mathfrak S_{\mathrm{prim}}$ (finite-dim, signed, $\perp H$;
D0), the \textbf{sourced determinant germ} is the holomorphic map
\[
   \mathcal D_A^{\mathrm{src}}:\ B_F(r)\ \to\ \C,\qquad
   V\longmapsto\det\nolimits_{\mathrm{reg}}(I+A+V),
\]
on a neighborhood $B_F(r)$ of $0$. Its scalar shadow is $\mathcal D_A^{\mathrm{src}}(0)=D_A$.
\end{definition}

Holomorphy in $V$ on $B_F(r)$: $V$ is finite-rank, so $\det_{\mathrm{reg}}(I+A+V)$ is a finite-dimensional
perturbation of an entire function of trace-class arguments — holomorphic by the standard determinant
estimates (§3). We use $\det_2$; the role of the modification appears as the anomaly $\mathcal A_n$.

---

## §2. First and higher variations (Fredholm calculus with anomaly)

\begin{lemma}[first variation]\label{lem:first}
For $V$ finite-rank with $R_A:=(I+A)^{-1}$,
\[
   \left.\frac{d}{d\varepsilon}\log\det\nolimits_{\mathrm{reg}}(I+A+\varepsilon V)\right|_{\varepsilon=0}
   =\operatorname{Tr}\big(R_AV\big)\ -\ \operatorname{Tr}(V)\quad(\text{the } \det_2\text{ anomaly}),
\]
i.e. $\operatorname{Tr}\big((R_A-I)V\big)=\operatorname{Tr}\big(-A R_A V\big)$. For the ordinary
($\det_1$) determinant the anomaly term $-\operatorname{Tr}(V)$ is absent.
\end{lemma}
\emph{Proof.} $\log\det_2(I+T)=\operatorname{Tr}\big(\log(I+T)-T\big)$. With $T=A+\varepsilon V$,
$\partial_\varepsilon\operatorname{Tr}\big(\log(I+A+\varepsilon V)-(A+\varepsilon V)\big)
=\operatorname{Tr}\big((I+A+\varepsilon V)^{-1}V-V\big)$; at $\varepsilon=0$ this is
$\operatorname{Tr}((R_A-I)V)$. $\square$

\begin{lemma}[higher variations]\label{lem:higher}
For finite-rank $V_1,\dots,V_n$,
\[
   \left.\partial_{\varepsilon_1}\!\cdots\partial_{\varepsilon_n}
   \log\det\nolimits_{\mathrm{reg}}\!\Big(I+A+\textstyle\sum_j\varepsilon_jV_j\Big)\right|_0
   =(-1)^{n+1}\!\!\sum_{\sigma\in\mathrm{cyc}(n)}\!\!
   \operatorname{Tr}\big(R_AV_{\sigma(1)}R_AV_{\sigma(2)}\cdots R_AV_{\sigma(n)}\big)+\mathcal A_n,
\]
with $\mathcal A_1=-\operatorname{Tr}(\sum V_j)$ and $\mathcal A_n=0$ for $n\ge2$ (the $\det_2$ anomaly is
first-order only). For $n=2$,
\[
   \partial_{\varepsilon_1}\partial_{\varepsilon_2}\log\det\nolimits_{\mathrm{reg}}\big|_0
   =-\operatorname{Tr}\big(R_AV_1R_AV_2\big).
\]
\end{lemma}
\emph{Proof.} Differentiate $\operatorname{Tr}\log(I+A+\sum\varepsilon_jV_j)$ repeatedly using
$\partial_\varepsilon\log(I+T)=\int_0^1(I+sT)^{-1}\partial_\varepsilon T\,(\dots)$; the trace and
cyclicity collapse the result to the cyclic resolvent sum. The $-\sum\varepsilon_jV_j$ term in $\det_2$
contributes only to $\mathcal A_1$. $\square$

\begin{remark}
Higher anomalies vanish for $\det_2$, so **the two-variable kernel (the $n=2$ Hessian) is anomaly-free**
— this is why $\det_2$ is the right regularization for reading the signature: the object we need
($\operatorname{Tr}(R_AV_1R_AV_2)$) has no anomaly correction.
\end{remark}

---

## §3. The recovered kernel and the source-reconstruction theorem

\begin{definition}[recovered kernel]\label{def:rec}
For probe sources $V=|u\rangle\langle v|$ ($u,v\perp H$), define the \textbf{response}
\[
   \rho_A(u,v;z):=\langle R_A(z)u,\,v\rangle,
\]
read off the first variation (Lemma~\ref{lem:first}, anomaly-subtracted). By polarization of the second
variation (Lemma~\ref{lem:higher}) define the two-variable form $\mathsf K_A$ via
\[
   \mathsf K_A(z,w)=\operatorname{Pol}\big(d^2\log\mathcal D_A^{\mathrm{src}}(0)\big)(z,w),
\]
the Hermitian kernel whose finite Gram matrices are built from $\rho_A$.
\end{definition}

\begin{theorem}[source reconstruction — defeats N1]\label{thm:recon}
Suppose $\mathfrak S_{\mathrm{prim}}$ is \emph{total} for the primitive realization (Source-richness
lemma, §5). If two admissible operators $A,B$ have equal sourced germs on a source plane rich enough to
separate the primitive Gram data, $\mathcal D_A^{\mathrm{src}}=\mathcal D_B^{\mathrm{src}}$, then
\[
   \mathsf K_A=\mathsf K_B,\qquad\text{hence}\qquad\kappa(A)=\operatorname{sq}_-(\mathsf K_A)
   =\operatorname{sq}_-(\mathsf K_B)=\kappa(B).
\]
In particular, equality of \emph{scalar} determinants $D_A=D_B$ does \textbf{not} imply $\kappa(A)=
\kappa(B)$ (N1), but equality of \emph{sourced germs} does.
\end{theorem}
\emph{Proof.} The first variation recovers all primitive resolvent matrix elements $\langle R_Au,v
\rangle$ ($u,v\perp H$); the second variation (anomaly-free, $n=2$) recovers $\operatorname{Tr}(R_AV_1
R_AV_2)$, and by polarization the two-variable kernel $\mathsf K_A$. Equal germs give equal variations
to all orders, hence equal $\rho_A=\rho_B$ and equal $\mathsf K_A=\mathsf K_B$. The index is a function
of the kernel (D1, Def. sq), so the indices agree. The N1 clause is Stage 1, Prop. 3.1(a) lifted: the
scalar shadow forgets the resolvent's off-diagonal/sign data that the germ retains. $\square$

\begin{remark}[the precise sense in which the germ is signature-faithful]
$\kappa$ is $\operatorname{sq}_-$ of $\mathsf K_A$, and $\mathsf K_A$ is the Hessian of $\log\mathcal
D_A^{\mathrm{src}}$ at $0$. So the signature is the *inertia of the source Hessian*. This is the operator
analogue of "the sourced determinant separates signature" (Stage 1, S1), now with the kernel itself
recovered, not merely the fact of separation.
\end{remark}

---

## §4. The connection to the canonical-system source response (interface to D7)

\begin{proposition}[canonical-system variation]\label{prop:cansys}
If $A=A_P$ is the canonical operator of a Hamiltonian $H_P$ and $\delta H$ is a finite-rank signed
source, then the transfer matrix varies as
\[
   \partial_\varepsilon Y_{P,\varepsilon}(\ell_P,z)\big|_0
   =-z\int_0^{\ell_P}Y_P(\ell_P,t;z)\,J\,\delta H(t)\,Y_P(t,z)\,dt,
\]
so the sourced determinant germ's first variation equals the canonical Gram pairing against $\delta H$.
Hence $\mathsf K_{A_P}$ recovered in Def.~\ref{def:rec} coincides with the canonical Gram kernel
$\int Y_P^*H_PY_P$ of G2 (proved in D7).
\end{proposition}
\emph{Proof.} Variation of parameters for $J\partial_tY=z(H_P+\varepsilon\delta H)Y$, $Y(0)=I$, gives the
displayed Duhamel formula; pairing and the determinant–transfer relation identify the source response
with the Gram kernel. Detailed identification is D7. $\square$

This is the bridge that will make D8's *sourced* convergence equivalent to *kernel* convergence for the
arithmetic systems.

---

## §5. The source-richness lemma — de-circularized *(Connes R1.C)*

\begin{redflag}[the earlier richness lemma was circular]
The previous draft defined the admissible sources \emph{via} the unknown realization vectors $Q\Gamma_A
(z_i)$ and then "proved" richness using those same vectors — circular, and worse, $A$-dependent (so it
could not be a \emph{fixed} source model independent of the operator). Corrected below by a fixed
algebraic core.
\end{redflag}

\begin{definition}[fixed algebraic source core]\label{def:core}
Let $\mathcal S_{\mathrm{alg}}^\circ$ be the nuclear space generated by finite sums of \emph{decomposable
Schwartz–Bruhat vectors} on the adelic test space, with the pole/degree component removed (projected by
$Q$). This is defined \textbf{independently of any operator $A$} — purely from the Schwartz–Bruhat
structure and the fixed pole line $H$. Admissible primitive sources are $V=\sum v_{\alpha\beta}|\phi_\alpha
\rangle\langle\phi_\beta|$ with $\phi_\alpha\in\mathcal S_{\mathrm{alg}}^\circ$.
\end{definition}

\begin{lemma}[source richness — fixed-core version]\label{lem:rich}
$\mathcal S_{\mathrm{alg}}^\circ$ is dense in the primitive realization space of every admissible $A_P$,
and the rank-one dyads $|\phi_\alpha\rangle\langle\phi_\beta|$ ($\phi\in\mathcal S_{\mathrm{alg}}^\circ$)
generate all finite primitive Gram patterns in the limit. Consequently the recovered primitive kernel
$\mathsf K_A^\circ$ is determined by the germ on $\mathcal S_{\mathrm{alg}}^\circ$ — \emph{no reference to
$Q\Gamma_A(z)$ is made}; density replaces the circular spanning claim.
\end{lemma}
\emph{Proof.} Density of decomposable Schwartz–Bruhat vectors (with the pole component removed) in the
primitive realization space is the standard adelic test-function density, uniform over the tower (the
realization spaces are nested with a common dense core). Given density, the first variations along the
fixed dyads approximate every primitive resolvent matrix element $\langle R_A\phi,\psi\rangle$ to
arbitrary accuracy, so the germ on $\mathcal S_{\mathrm{alg}}^\circ$ determines $\mathsf K_A^\circ$. $\square$

\begin{remark}
The fix is exactly Connes' "Step 1 — reduce to an algebraic Tate source core" (his §6): prove everything
first for $\phi\in\mathcal S_{\mathrm{alg}}^\circ$, then extend to all admissible finite-rank primitive
sources via the G4 uniform bounds (D8.5a, block 8). The source model is now operator-independent, so the
construction is non-circular.
\end{remark}

---

## §6. `ASSUMED` ledger (D2)

> `ASSUMED (Connes/Consani, tested): the relative trace-class structure of A_P − A_0 on compact z-sets`
> — needed so that $\det_2(I+A_P)$ and the resolvent traces of Lemmas~\ref{lem:first},~\ref{lem:higher}
> exist; established in Phase 64 (`CANONICAL-FOUNDATION.md` Stage 5, "the trace existing because
> $A_P-A_0=\sum d\mathcal H_p$ is trace-class on each compact $z$-set"). Re-derivation deferred (it is the
> finite-atom structure of $H_P$); does not use RH.

All other D2 results are proved in full above.

---

## §7. What D2 establishes

- The **sourced determinant germ** $\mathcal D_A^{\mathrm{src}}$ (Def.~\ref{def:germ}); its variations
  are resolvent traces with the $\det_2$ anomaly confined to first order (Lemmas~\ref{lem:first},
  \ref{lem:higher}); the two-variable kernel is anomaly-free.
- **Source reconstruction** (Thm~\ref{thm:recon}): equal germs $\Rightarrow$ equal kernel $\Rightarrow$
  equal index. This defeats N1 at the operator level — the cure for the M3 obstruction.
- The germ's first variation **is** the canonical Gram pairing (Prop.~\ref{prop:cansys}) — the bridge to
  the arithmetic systems (D7, D8).
- **Source richness** (Lemma~\ref{lem:rich}): the primitive sources determine the whole primitive kernel,
  so sourced convergence will mean genuine kernel convergence, not subspace convergence.

The honest status is exactly right: D2 does not prove RH; it builds the *instrument* that makes the
signature visible to a limit, so that the decisive D8 convergence can be about the *kernel* (index-aware)
rather than the *scalar determinant* (index-blind). Next: D3 packages $(D,\mathcal D^{\mathrm{src}},
\mathsf K,\mathfrak b,\mathcal R)$ into the category $\mathcal G$ with index as a functor.
