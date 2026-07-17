# Phase 16 · The de Branges chain criterion in clean form: $\Re\,\xi'/\xi>0$ for $\sigma>\tfrac12$ (Herglotz)

**Author: David Alejandro Trejo Pizzo · 2026-06-06.**
Pushing the de Branges / Conrey--Li frontier to its sharpest computable form. Result: RH $\iff
\Re\,\xi'/\xi(\sigma+i\tau)>0$ for all $\sigma>\tfrac12$ (i.e. $\xi'/\xi$ is a **Herglotz/Nevanlinna function** in the
right half-plane), with the **unconditional boundary fact** $\Re\,\xi'/\xi=0$ on $\sigma=\tfrac12$ (functional
equation alone). The obstruction is precisely the harmonic minimum principle in the presence of possible interior
poles (off-line zeros). This is a clean criterion — a genuine reformulation — but it is RH-equivalent (no crossing):
it equals Hilbert--P\'olya. Logged as the cleanest statement the program has reached on this front.

---

## The criterion and the unconditional boundary fact
The de Branges chain $E_a(z)=\xi(\tfrac12+a-iz)$ is Hermite--Biehler at level $a$ iff its phase is monotone, i.e.
$\theta_a'(t)=\Re\,\xi'/\xi(\tfrac12+a-it)>0$. As $a\downarrow0$ this is:
$$
\boxed{\ \mathrm{RH}\iff \Re\,\frac{\xi'}{\xi}(\sigma+i\tau)>0\ \text{ for all }\sigma>\tfrac12,\ \text{all }\tau.\ }
$$

\begin{proposition}[Unconditional boundary value]
$\Re\,\dfrac{\xi'}{\xi}\!\left(\tfrac12+i\tau\right)=0$ for all real $\tau$ — \emph{no RH used}.
\end{proposition}
\begin{proof}
$\xi(s)=\xi(1-s)\Rightarrow \xi'/\xi(s)=-\xi'/\xi(1-s)$. On $s=\tfrac12+i\tau$, $1-s=\bar s$, and $\xi$ has real
coefficients so $\xi'/\xi(\bar s)=\overline{\xi'/\xi(s)}$. Hence $\xi'/\xi(s)=-\overline{\xi'/\xi(s)}$, so its real
part vanishes. (Verified to machine precision, `debranges_boundary_value.py`.)
\end{proof}

## The structure (harmonic / Herglotz) and the precise obstruction
$\Re\,\xi'/\xi$ is **harmonic** in $\sigma>\tfrac12$ away from the zeros of $\xi$, equals $0$ on the boundary
$\sigma=\tfrac12$ (Prop.), and $\to+\infty$ as $\sigma\to\infty$ (the $\Gamma$-factor). Two consequences:
- **RH $\Rightarrow$ positivity:** if no zeros lie in $\sigma>\tfrac12$, $\Re\,\xi'/\xi$ is harmonic there with
  boundary value $0$ and positive growth at infinity, so $\Re\,\xi'/\xi>0$ by the **minimum principle**.
- **An off-line zero kills it:** a zero $\rho_0$ with $\beta_0>\tfrac12$ is an **interior pole** of $\xi'/\xi$
  (residue $+1$); near it $\Re\,\xi'/\xi\sim(\sigma-\beta_0)/|s-\rho_0|^2$ takes **both signs**, so positivity fails.

Hence RH $\iff$ positivity $\iff$ $\xi'/\xi$ has no interior poles $\iff$ $\xi'/\xi$ is a **Herglotz/Nevanlinna
function** on $\{\sigma>\tfrac12\}$ (positive real part). Equivalently (Herglotz $=$ resolvent/Weyl function of a
self-adjoint operator): $\xi'/\xi$ Herglotz $\iff$ its poles (the $\zeta$-zeros) are real eigenvalues on the line
$=$ **Hilbert--P\'olya**.

> **The new-tool target, precisely:** prove $\Re\,\xi'/\xi>0$ on $\tfrac12<\sigma<1$ using only the unconditional
> boundary value ($=0$ on $\sigma=\tfrac12$) and the growth at infinity, surviving the *possible* interior poles — a
> Phragm\'en--Lindel\"of / harmonic-measure argument that does not assume the poles are absent. Equivalently,
> construct the self-adjoint operator whose Weyl function is $\xi'/\xi$ (Hilbert--P\'olya). This is the open core, in
> harmonic-function / Nevanlinna form.

## Why it does not cross (honest)
The minimum-principle argument needs *no interior poles*, which is RH; the Herglotz/Weyl realization is
Hilbert--P\'olya. So this clean criterion is **RH-equivalent**: it reformulates, it does not cross. It is the
wrong-sign capstone (CAP) once more — the unconditional input (boundary value $0$, growth at infinity) is a
two-sided/boundary constraint, and the missing piece is the *exclusion of interior negative singularities*, the same
one-sided/upper constraint the program has shown is the irreducible difficulty.

## Status
- **Genuine, clean output (a real reformulation, not a crossing):** RH $\iff\Re\,\xi'/\xi>0$ on $\sigma>\tfrac12$
  $\iff\xi'/\xi$ Herglotz $\iff$ Hilbert--P\'olya, with the **unconditional** boundary identity $\Re\,\xi'/\xi=0$ on
  the critical line. The cleanest form of the de Branges chain criterion the program has reached, with the obstruction
  named in harmonic-function terms (interior poles vs minimum principle).
- **No new crossing:** the de Branges/Conrey--Li wall stands, now phrased as: rule out interior poles of a Herglotz
  candidate from boundary data alone. That is RH.
- This consolidates the Phase-16 frontier: the indefinite object is $H(E_\xi)$ (P16/de Branges), its positivity is
  $\xi'/\xi$ Herglotz $=$ Hilbert--P\'olya $=$ CAP, and the unconditional boundary structure ($\Re\,\xi'/\xi=0$ on the
  line) is the one clean handle — necessary, not sufficient.
