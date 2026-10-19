# CA_A_008 — Pre-screen of the integer-invariant seed (spectral flow / Maslov / signed index): COLLAPSES

Phase 193. Pen and paper.

## 1. Structural point (PROVED, elementary)
Let (q_c)_{c∈[0,1]} be a continuous path of closed semibounded forms on P_T (or a path in T), with q_0≥0 PROVED. Let
SF be the spectral flow through 0 (or a Maslov index of the associated Lagrangian path).
**Lemma 1.** If SF is locally constant along the path, then n₋(q_1)=n₋(q_0)+SF[0,1]. In particular n₋(q_1)=0 ⟺
SF[0,1]=0 (given n₋(q_0)=0 and no eigenvalue resting at 0 at the endpoints).
*Proof.* Definition of spectral flow as the net count of eigenvalue crossings through 0, plus homotopy invariance with
fixed endpoints. ∎
So the statement "the invariant at c=1 equals its value at the PROVED endpoint" is exactly "no net crossing", which is
λ_A(T)≥0 (REF-D), unless the crossing count is forced to be zero by something independent of the path's spectrum.
Two candidate sources of such forcing:
(a) **a loop whose index is computed topologically** (degree or winding of a symbol). That is Fredholm-symbol data, and
P49-2 (NO-GO: the target enters through Fredholmness of the symbol) and P37-2 (winding wall = sieve wall) cover it;
(b) **an additive/semilocal decomposition** of the index over places. That is P35-3 (μ_A=2κ; additive form discarded; no
S→all-places mechanism) and NG-69 (gauge-robust signed index, forcer absent; the Cayley-invariant version, line 632,
is unbuilt but has the same forcer problem).
In addition, the record has the following fixed results:
- **thm:inertia-nogo**: n₋=∞ for T>½log2 for the bounded-remainder pencil. Any index computed through that splitting
  counts infinitely many crossings.
- **R186_028**: the full form has index one on L², and the scalar criterion is REF-D. The only finite index known is the
  one already carried by the polar pair (𝔊_T).
- **P54-2**: the κ balance law is deflationary (argument principle). An index read off zero counts falls under [zeros].
**Verdict: COLLAPSES (REF-D).** Local constancy holds on the open ball (CA_B_006), but the invariant's value at Λ is
λ_A≥0 itself. Neither known forcing mechanism (topological symbol index, additive place decomposition) survives the cited
NO-GOs. No construction undertaken. No sign contact.
