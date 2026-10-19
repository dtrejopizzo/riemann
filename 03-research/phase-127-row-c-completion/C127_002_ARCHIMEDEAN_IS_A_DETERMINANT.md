# C127.002 — the archimedean term is a determinant, not a fixed point

Status: `PROVED`. Full statement: Paper 45 §7.

No note in the corpus proves an archimedean dilation trace on the A-carrier, and
none can: the real coordinate is `R_{>0}`, the **modulus group**, with no zero
and no `|1−σ_∞|` Jacobian.  This was read as a deferred obligation in a dozen
notes (P123.032, 033, 034, 039, 043, 045, 046, 058, 059, 112).  It is not an
omission — it is correct Arakelov structure: finite places contribute torsion
lengths, the archimedean place contributes a Green/determinant term.

Two identities make this exact.  Let `N_Γ` have spectrum `{2m+1/2}_{m≥0}`
(`106_195`).  Then the kernel of P123.035's archimedean distribution is its heat
trace,

    K(t) = e^{−t/2}/(1−e^{−2t}) = Σ_{m≥0} e^{−(2m+1/2)t} = Tr e^{−tN_Γ},

and, by Lerch's formula `ζ'_H(0,a) = log Γ(a) − ½log 2π` applied to
`ζ_{N_Γ,s}(w) = 2^{−w}ζ_H(w,s/2)`,

    det_ζ(N_Γ + s − 1/2) = √(2π)·2^{1/2−s/2}/Γ(s/2).

So the archimedean Gamma factor **is** the zeta determinant of `N_Γ`, and the
archimedean Weil distribution **is** its regularized heat integral, the
subtraction `2h(0)e^{−t/2}` removing exactly the lowest eigenvalue's heat
factor.  One operator produces both.

Consequence: row C no longer cites Meyer.  P123.035 proves `W_∞` outright,
constant `γ + log 4π` computed and not assumed, symbol `log π − Re ψ(1/4+iτ/2)`.
That also settles the conflict P123.035 §1 had recorded: the literal Meyer
off-origin coefficient fails a Gaussian test (`−1/2`, not `−1`).  With the
citation removed, no external constant can be wrong.
