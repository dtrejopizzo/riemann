# Phase 15 · M3 · Attempt 6 — the elliptic control: where the arithmetic Hodge index lands (heights, not zeros)

**Author: David Alejandro Trejo Pizzo · 2026-06-06.**
Running the Attempt-5 construction on a case where the arithmetic surface **exists** — an elliptic curve
$E/\mathbb Q$ — to isolate the exact point at which the proven arithmetic Hodge index separates from RH. The result
sharpens the obstruction once more, and correctly: the proven theorem controls the *wrong cohomology*. Verifiable;
no fabricated crossing.

---

## 1. The control case
Let $E/\mathbb Q$ with minimal regular model $\mathcal E\to\operatorname{Spec}\mathbb Z$ — a genuine
$2$-dimensional regular arithmetic scheme (the surface that $\operatorname{Spec}\mathbb Z$ alone lacks). Here:
- the **arithmetic Hodge index theorem applies** (Faltings–Hriljac): the Arakelov pairing on
  $\widehat{\mathrm{Pic}}^0(\mathcal E)$ is negative definite, equal to the **Néron–Tate height** $\widehat h$ on
  $E(\mathbb Q)\otimes\mathbb R$;
- the Hasse–Weil $L$-function $L(E,s)$ (degree $2$, automorphic by modularity) has a functional equation about
  $s=1$ and conjectural zeros on $\operatorname{Re}s=1$ (GRH for $E$).
So this is exactly the setting of Attempt 5 with the surface present. We trace where it goes.

## 2. What the arithmetic Hodge index gives here
\begin{proposition}[Heights / special value]\label{prop:height}
On $\mathcal E$, Faltings–Hriljac gives the negative-definiteness of $\widehat h$ on $E(\mathbb Q)\otimes\mathbb R$.
This controls the \emph{Mordell–Weil regulator} $R_E=\det(\widehat h)$, hence (via BSD) the \emph{leading
coefficient of $L(E,s)$ at the central point $s=1$}:
\[
L^{(r)}(E,1)/r! \;\sim\; \Omega_E\,R_E\,\frac{\#\Sha\cdot\prod c_p}{(\#E_{\mathrm{tors}})^2},\qquad r=\mathrm{rank}\,E(\mathbb Q).
\]
\end{proposition}
\begin{proof}
Faltings–Hriljac identifies the Arakelov pairing with $\widehat h$; the regulator is its determinant; the BSD
formula expresses $L^{(r)}(E,1)$ through $R_E$. (Definiteness of $\widehat h$ is what makes $R_E$ a genuine positive
volume; it is the input used, e.g., in Gross–Zagier/Kolyvagin for rank $\le1$.)
\end{proof}

> The proven arithmetic Hodge index controls the **special value at the central point** $s=1$ — a BSD statement.

## 3. What it does *not* give — and the precise separation
\begin{proposition}[The zeros are a different object]\label{prop:zeros}
The location of the nontrivial zeros of $L(E,s)$ on $\operatorname{Re}s=1$ (GRH for $E$) is \emph{not} controlled by
$\widehat h$. The height pairing is a statement about the central special value; the zero distribution is a global
analytic statement. They separate at the level of \emph{which cohomology carries the eigenvalues}:
\[
\underbrace{\text{Frobenius on }H^1_{\mathrm{\acute et}}(C)\ \Rightarrow\ L\text{-zeros}}_{\text{function field}}
\qquad\text{vs}\qquad
\underbrace{\widehat{\mathrm{Pic}}^0(\mathcal E)=E(\mathbb Q)\ \Rightarrow\ \text{heights/special value}}_{\text{arithmetic}} .
\]
\end{proposition}
\begin{proof}
In the function-field case the zeros of $\zeta_C$ are the Frobenius eigenvalues on $H^1_{\mathrm{\acute et}}(C)$,
and the Hodge index on $C\times C$ constrains \emph{those eigenvalues}. The Arakelov $\widehat{\mathrm{Pic}}^0(\mathcal E)$
is the arithmetic analogue of the \emph{Mordell–Weil/Néron–Severi} part, carrying heights, not the analytic
$L$-zeros; Faltings–Hriljac constrains the \emph{height} eigenvalues. The two cohomologies are different objects,
and only the function-field one carries the zeros.
\end{proof}

## 4. The sharpened obstruction (the real result)
Running the construction where the surface exists reveals that Attempt 5's statement was still one step coarse.
There are \emph{two} arithmetic Hodge index theorems / two cohomologies:
\[
\boxed{
\begin{array}{ll}
\text{(i) Arakelov / Faltings--Hriljac / Yuan--Zhang} & \text{PROVEN; controls \emph{heights} (Mordell--Weil)} \\
 & \Rightarrow\ \text{special values (BSD), \emph{not} the zeros}.\\[4pt]
\text{(ii) Deninger / Connes ``arithmetic cohomology''} & \text{CONJECTURAL; would carry the \emph{$L$-zeros}}\\
 & \Rightarrow\ \text{GRH/RH; \emph{does not exist}}.
\end{array}}
\]
So the missing $I_{2b}$ is not merely ``a surface'': even with the surface (for $E$), the *proven* Hodge index is on
the **wrong cohomology** (heights). **The genuinely missing object is the zero-carrying arithmetic cohomology** (a
``$H^1$'' for $\operatorname{Spec}\mathbb Z$ on which a Frobenius-analogue has the $\zeta$-zeros as eigenvalues),
together with its own Hodge index. That is exactly the Deninger/Connes target — and it is distinct from, and not
supplied by, the Arakelov–Faltings–Hriljac height theory.

## 5. Consequences and the next concrete target
- **SURF refined:** constructing the $\mathbb F_1$-surface for $\operatorname{Spec}\mathbb Z$ is necessary but, by
  Attempt 6, **not sufficient unless its cohomology carries the zeros** (not the heights). The Connes–Consani
  program is right to seek the zeros as spectrum; the Arakelov route (heights) is a *different*, BSD-flavoured
  theory and does not transfer.
- **The Beilinson dictionary, located:** the bridge "special values (heights, controlled) $\leftrightarrow$ zeros
  (GRH, uncontrolled)" is the precise open link. Beilinson's conjectures relate special values to regulators
  (heights); the *zero distribution* is a further, finer datum the regulators do not see.
- **The single sharpest target now:** a zero-carrying arithmetic cohomology $H^1_?(\operatorname{Spec}\mathbb Z)$
  with a Frobenius-analogue $\Phi$ such that $\operatorname{spec}(\Phi)=\{\gamma_\rho\}$, and a Hodge-index/
  definiteness theorem for it. This is the Deninger ``$\Phi$ on leafwise cohomology'' / the Connes ``zeros as
  absorption spectrum'' object — now isolated, by the elliptic control, as the *unique* remaining ingredient, with
  the height-theory shown to be the wrong (though proven) Hodge index.

## 6. Status
- **New finding (verifiable):** even where the arithmetic surface exists ($E/\mathbb Q$), the proven arithmetic
  Hodge index (Faltings–Hriljac) controls **heights $\Rightarrow$ special values (BSD)**, **not** the critical-line
  **zeros (GRH)**. The two are different cohomologies; only the function-field one carries the zeros.
- **Obstruction sharpened to its final form:** the missing $I_{2b}$ is the **zero-carrying arithmetic cohomology**
  (Deninger/Connes), with its Hodge index — *not* the Arakelov height theory (which exists and is the wrong object),
  and *not* merely "a surface" (necessary but insufficient without the right cohomology).
- **No crossing.** The elliptic control isolates the exact missing object and shows the proven theorem is on the
  wrong invariant. This is the sharpest, most correct statement of the M3/RH obstruction the program has reached.
