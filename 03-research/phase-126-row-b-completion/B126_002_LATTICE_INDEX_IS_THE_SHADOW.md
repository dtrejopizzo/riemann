# B126.002 — the lattice index is the ramified half of the shadow

Status: `PROVED`. Full statement: Paper 44 §6.1, Thm. 6.1.

P123.038 §5 and P123.039 §5 both close on the same missing arrow: "the
lattice-index operation must be realized as the admissible diagonal shadow",
and "`T_n` is the finite translation, not the external dilation `E_n`".

With B126.001 the arrow is two lines.  For `S ⊇ {∞} ∪ P(n)` and
`Q_{S,n}=[L_S→n→L_S]`:

    − 2 log w_ram(Γ_n) = log [L_S : nL_S] = log n = deg_det C_ram(n).

Left side: analytic, the half-density of the external dilation.  Right side:
integral, the determinant of the ramification contact.  The identity is the
statement that the modulus of an automorphism of a locally compact group is
the inverse index of its invariant lattice, read through (8.1) of Paper 43.

`T_n` is never identified with `E_n`.  What is proved is that both determine
the same finite quotient `L_S/nL_S ≅ Z/n`: `E_n` as the map defining it, `T_n`
as its canonical order-`n` translation.  The cyclotomic factor is
`det(1−T|V_n)=Φ_n(1)` — a **deck** determinant, which is why it carries `n`
and not `n−1`.

Over `C` the torsion vanishes and the shadow of `Γ_n` at `p|n` is the rank-one
origin class (Paper 43 Thm. 7.1(c)).  No information is lost: a two-term
complex `[Z→m→Z]` with `m>0` is determined by `m`, and `m` is determined by
the half-density.
