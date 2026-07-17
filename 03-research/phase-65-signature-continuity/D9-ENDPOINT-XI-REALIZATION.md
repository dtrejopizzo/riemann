# D9 — Endpoint realization: the limit kernel is the fixed $\mathsf K_\Xi^{\mathrm{G5}}$ (axiom A3)

> **R3 update.** Carry the change-of-variable factor `M_Ξ(z) = −Ξ'(z)/Ξ(z) = i·M_ξ(s)`, `M_ξ = −ξ'/ξ`,
> `s = ½ + iz`. Keep the **one-variable** Weyl coordinate `M_Ξ` distinct from the **two-variable** Pick
> kernel `K_Ξ` built from it: Vitali acts on `M_Ξ`; the index `sq₋` is read off `K_Ξ` at the end. See
> [`CORRECTIONS-CONNES-R3.md`](CORRECTIONS-CONNES-R3.md).

**Phase 65 / Signature-Continuity Package, deliverable D9.** Pure mathematics, full proofs (conditional
on D8). This is the decisive *audit* point. D6 proved that a $\tau_\kappa$-limit of positive shorted
kernels is positive; D9 proves that the limit is not *some* positive kernel attached to $\Xi$ but the
**fixed** Kreĭn–Langer kernel $\mathsf K_\Xi^{\mathrm{G5}}$ of D0 — obtained by differentiating the
sourced limit (D8), never assigned. Conflating "a positive limit kernel" with "the $\Xi$ kernel" is the
forbidden endpoint reassignment (D0); D9 is precisely the proof that they coincide.

> `ASSUMED` ledger (D9): inherits D8.5 (via D8). No new assumption.

---

## §1. The two halves that must meet

\begin{definition}
Let $\mathsf K_\infty^\circ:=\lim_P\mathsf K_P^\circ$ (the $\tau_\kappa$-limit, existing by D8.7). Let
$\mathsf K_\Xi^{\mathrm{G5}}$ be the *fixed* endpoint kernel of D0 (Def. KG5), $\mathsf K_\Xi^{\mathrm{G5}}
=\mathsf N_{M_\Xi}$, $M_\Xi=-\Xi'/\Xi$ (Herglotz; D0 sign-corrected, Connes R1.A / R3.E).
\end{definition}

\begin{redflag}
D6 gives $\operatorname{sq}_-(\mathsf K_\infty^\circ)=0$. By itself this says nothing about RH: it is the
index of *the limit kernel*, which is not yet known to be $\mathsf K_\Xi^{\mathrm{G5}}$. The package is
RH \textbf{only if} $\mathsf K_\infty^\circ=\mathsf K_\Xi^{\mathrm{G5}}$ — equality with the pre-fixed
object. Asserting this without proof is the forbidden reassignment.
\end{redflag}

---

## §2. The identification theorem

\begin{theorem}[A3: endpoint identification]\label{thm:a3}
Conditional on D8 (in particular D8.5), the limit kernel equals the fixed endpoint kernel:
\[
   \boxed{\ \mathsf K_\infty^\circ(z,w)=\mathsf K_\Xi^{\mathrm{G5}}(z,w)\ \ \text{for all }z,w.\ }
\]
Consequently $\kappa(A_\infty)=\operatorname{sq}_-(\mathsf K_\infty^\circ)=\operatorname{sq}_-(\mathsf
K_\Xi^{\mathrm{G5}})=\kappa(\Xi)$.
\end{theorem}
\emph{Proof (corrected, Connes R1.F — now rests on D8.5b, not on the scalar slice).} By D8.7, $\mathsf
K_\infty^\circ=\operatorname{Pol}(d_V^2\log\mathcal D_\Xi^{\mathrm{src}}(0))$, the polarized second
\emph{source} variation of the limit germ. \textbf{Caution:} $D_\infty^\circ=\Xi$ (G3) does \emph{not}
by itself give the first source variation — \emph{derivative in $V$ is not derivative in $z$}. The
identification of the limit's marked source Hessian with the fixed kernel must come from the
endpoint-identification input \textbf{D8.5b} (the marked Green matrix converges to the genuine
$\Xi$-resolvent matrix $G_\Xi^{\mathrm{G5}}$, D8.5$'$, not merely to some Green matrix whose scalar
determinant is $\Xi$). Given D8.5b, the first source variation of the limit germ is $\langle R_\Xi^{
\mathrm{G5}}(z)u,v\rangle$, so the polarized second variation is the Nevanlinna kernel of the Herglotz
coordinate $M_\Xi=-\Xi'/\Xi$ (D0, sign-corrected), i.e. $\mathsf N_{M_\Xi}=\mathsf K_\Xi^{\mathrm{G5}}$.
$\square$

\begin{remark}[why this is identification, not assignment — and where the RH-strength sits]
The kernel $\mathsf K_\infty^\circ$ is *computed* from the limit germ's source derivatives (D8.7); the
endpoint $\mathsf K_\Xi^{\mathrm{G5}}$ was *fixed in D0*. They coincide *iff* the marked Green matrices
converge to the genuine $\Xi$-resolvent — which is exactly \textbf{D8.5b}. So D9 is \emph{not} free from
G3: it is D8.5b cashed out, and D8.5b is the load-bearing, RH-strength step (Connes R1 §1; matches the
M3 "endpoint identification" worry). The forbidden move (D0) — *assigning* $\mathsf K_\Xi:=\lim\mathsf
K_\infty^\circ$ — is avoided precisely because the limit must be shown to equal the *independently fixed*
object, and that showing is D8.5b, not a definition.
\end{remark}

---

## §3. The role of D8.5 in the identification

\begin{remark}[honest dependency]
Theorem~\ref{thm:a3} rests on D8.5: the *first variation* of the limit germ must be the $\Xi$-system's
primitive resolvent response $\langle R_\Xi u,v\rangle$ (so that its Weyl function is $-\Xi'/\Xi$). D8.5 is
exactly what supplies this (the source-level local factors assemble to the $\Xi$-resolvent, not to some
other operator with determinant $\Xi$). Without D8.5, one would know only $\mathsf K_\infty^\circ\succeq0$
(D6) and $D_\infty^\circ=\Xi$ (G3) — the two halves that the M3 audit showed do *not* meet at the scalar
level. D8.5 is the bridge; D9 is its consequence. The package's validity is therefore exactly the
validity of D8.5.
\end{remark}

---

## §4. What D9 establishes

- **A3** (Thm~\ref{thm:a3}, conditional on D8.5): the limit kernel *is* the fixed $\mathsf K_\Xi^{\mathrm{G5}}$,
  by differentiation of the identified limit germ — not by assignment.
- Hence $\kappa(A_\infty)=\kappa(\Xi)$, connecting the *constructed* limit index to the *given* G5 index.
- The honest dependency: D9 = D8.5 cashed out; the endpoint identification is the second face of the one
  load-bearing input. D6 (positivity closed) + D9 (limit is the $\Xi$ kernel) together give
  $\operatorname{sq}_-(\mathsf K_\Xi^{\mathrm{G5}})=0$, i.e. $\kappa(\Xi)=0$ — assembled in D11.

Next: D10 (the DH falsifier — DH must break D8.5 or finite positivity, forcing $\deg\mathfrak b_{\mathrm
{DH}}>0$), then D11 (assembly), D12 (audit).
