# Phase 15 · M3 · Attempt 8 — can the flow generate the Kähler form? (the deepest structural form of the capstone)

**Author: David Alejandro Trejo Pizzo · 2026-06-06.**
Attempt 7 reduced RH to a single missing object: a compatible $(1,1)$-Kähler form $\omega$ on the constructed
arithmetic cohomology $\mathcal H_W^{\mathrm{prim}}$, with $J$ (the spectral complex structure from the flow
$\mathcal T$) and $Q$ (the Weil pairing) in hand. We attack $\omega$ directly. The result is the deepest structural
statement of the capstone, executed honestly; it routes to the missing geometric Lefschetz/Kähler structure. No
crossing.

---

## 1. The form is determined; its positivity is RH
\begin{proposition}[$\omega$ is not independent]\label{prop:omega}
The only $(1,1)$-form compatible with $J$ and $Q$ in the standard way is $\omega(x,y)=Q(Jx,y)$. Its positivity
$\omega(x,Jx)=Q(Jx,Jx)>0$ (equivalently the Riemann relation $Q(x,Jx)>0$, Attempt 7, Thm) is exactly RH.
\end{proposition}
\begin{proof}
Compatibility of a $(1,1)$-form $\omega$ with $(J,Q)$ means $\omega(x,y)=g(Jx,y)$ for the metric $g=Q$ adapted to
$J$; this fixes $\omega=Q(J\cdot,\cdot)$. Positivity of $\omega$ is $Q(Jx,Jx)>0$, the second Riemann bilinear
relation, $=$ RH by Attempt 7.
\end{proof}

So $\omega$ built from the spectral data $(\mathcal T,J,Q)$ alone is *not* an independent object — it is $Q(J\cdot,
\cdot)$, and asserting its positivity is asserting RH. An $\omega$ that *forces* positivity must come from
**outside** the triple $(\mathcal T,J,Q)$ — from an independent geometric structure. We test the two natural
sources.

## 2. Source 1 — can $\mathcal T$ be the Lefschetz operator? (No: spectrum mismatch)
A Kähler positivity is delivered structurally by a **hard Lefschetz $\mathfrak{sl}_2$-action** $(L,\Lambda,H)$ with
$L=\omega\wedge\,\cdot$ the raising operator and $H$ the integer grading; the Hodge–Riemann signs then follow from
$\mathfrak{sl}_2$ representation theory (the primitive decomposition). The candidate raising operator would be
related to the flow $\mathcal T$.
\begin{proposition}[$\mathcal T$ is not the Lefschetz grading]\label{prop:sl2}
$\mathcal T$ cannot be the $\mathfrak{sl}_2$-grading operator $H$: the eigenvalues of $H$ are integers (Lefschetz
weights), while $\operatorname{spec}(\mathcal T)=\{\gamma_\rho\}$ is a real, irrational, asymptotically dense set
(density $\sim\tfrac1{2\pi}\log\tfrac{\gamma}{2\pi}$). $\mathcal T$ is the Frobenius/eigenvalue datum *within* a
weight, not the weight grading.
\end{proposition}
\begin{proof}
$\mathfrak{sl}_2$-grading eigenvalues are integers; the zero ordinates are not (and accumulate with growing
density), so no rescaling makes $\mathcal T$ an integer-graded operator.
\end{proof}
Thus the hard-Lefschetz structure is a *separate* operator (the integer Lefschetz grading $H$) commuting with the
Frobenius $\mathcal T$, with $\omega=L$ its raising part. The flow alone does not supply it.

## 3. Source 2 — does a contraction give a positive form? (No: self-adjoint $=$ unitary)
A dissipative/contraction semigroup yields a positive (Lyapunov) form. But:
\begin{proposition}[No contraction structure under RH]\label{prop:contr}
If RH holds, $\mathcal T$ is self-adjoint with real spectrum, generating a \emph{unitary} group $e^{it\mathcal T}$
--- not a contraction. A genuine contraction (positive imaginary part) would place all zeros on one side of the
line, contradicting the functional-equation symmetry. So the positivity of $\omega$ cannot come from a contraction
structure of $\mathcal T$.
\end{proposition}
\begin{proof}
Self-adjoint $\mathcal T\Rightarrow e^{it\mathcal T}$ unitary; a strict contraction needs $\operatorname{Im}\mathcal T
\succ0$, i.e.\ $\operatorname{Im}\gamma_\rho>0$ for all $\rho$, impossible under $\rho\mapsto1-\rho$. $\square$
\end{proof}

## 4. The deepest structural form of the capstone
Both natural sources fail to supply an *independent* $\omega$ from the spectral data: $\mathcal T$ is the Frobenius
(its spectrum is the zeros), not the Lefschetz grading (Prop.~\ref{prop:sl2}); and it is unitary, not a contraction
(Prop.~\ref{prop:contr}). Therefore:
\[
\boxed{\ \text{The missing }\omega\ =\ \text{an independent hard-Lefschetz }\mathfrak{sl}_2\text{ structure (the
Kähler class), commuting with the Frobenius }\mathcal T.\ }
\]
This is precisely what a **surface** supplies: on $C\times C$ the ample class $\omega$ gives the hard Lefschetz, the
Frobenius $\mathcal T$ acts on $H^1$, and Hodge–Riemann (the Kähler positivity) gives RH. For $\operatorname{Spec}
\mathbb Z$ we have built the Frobenius $\mathcal T$ and the cohomology (Attempt 7), but the **Lefschetz/Kähler
class $\omega$** — the ample geometry of the surface — is the lone missing structure. It cannot be generated from
$\mathcal T$ alone (Props.~\ref{prop:sl2}–\ref{prop:contr}); it is the geometric input SURF, in its sharpest form: a
single hard-Lefschetz $\mathfrak{sl}_2$-action.

## 5. Status — the honest terminus of the spectral construction
- **Established:** $\omega=Q(J\cdot,\cdot)$ is determined by the spectral triple, with positivity $=$ RH
  (Prop.~\ref{prop:omega}); the flow $\mathcal T$ is the Frobenius (zeros as spectrum), \emph{not} the Lefschetz
  grading (Prop.~\ref{prop:sl2}); and it is unitary, \emph{not} a contraction (Prop.~\ref{prop:contr}). So no
  independent $\omega$ arises from $\mathcal T$.
- **The capstone, deepest form:** RH $=$ the existence of an independent hard-Lefschetz $\mathfrak{sl}_2$ (Kähler
  class $\omega$) on $\mathcal H_W^{\mathrm{prim}}$ commuting with $\mathcal T$. This is the ample geometry of the
  arithmetic surface --- SURF --- reduced to a single $\mathfrak{sl}_2$-action.
- **Honest terminus.** Through eight attempts the program has built the zero-carrying cohomology and the Frobenius
  explicitly, and reduced RH to one missing structure: a hard-Lefschetz/Kähler $\mathfrak{sl}_2$-action — the ample
  class of the (missing) arithmetic surface. The spectral tools of this program supply everything *except* this one
  geometric input, and Props.~\ref{prop:sl2}–\ref{prop:contr} show it cannot be manufactured from the flow alone.
  This is the sharpest, most structural, and final form of the capstone the spectral construction reaches.

> The eight-attempt arc terminates here, honestly: $\mathcal H_W$, $\mathcal T$, $J$, $Q$, the trace formula, the
> anatomy/Frobenius, and the ample cone are built; RH is the existence of one independent Kähler/Lefschetz class
> $\omega$ (an $\mathfrak{sl}_2$), the ample geometry of $\operatorname{Spec}\mathbb Z\times\operatorname{Spec}
> \mathbb Z$. That object is the Connes–Consani/Deninger target, now reduced to a single hard-Lefschetz action and
> proven not generable from the flow — the most precise statement of what a proof must still supply.
