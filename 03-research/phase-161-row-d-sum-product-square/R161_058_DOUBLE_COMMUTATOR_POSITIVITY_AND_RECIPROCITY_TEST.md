# R161_058 — Double-commutator positivity and the reciprocity test

## 1. Radical double-commutator lemma

Let H=H*>=0, let f belong to ker H, and let B be bounded and preserve the relevant form domain. With [H,B]=HB-BH,

    <f,[B*,[H,B]]f>
      =<Bf,HBf>+<B*f,HB*f>>=0.                         (1.1)

Proof. Expand

    [B*,[H,B]]=B*HB-B*BH-HBB*+BHB*.

The middle two terms have zero pairing with f because Hf=0. The first and last terms are the two displayed quadratic forms.

If the left side of (1.1) vanishes, both H^(1/2)Bf and H^(1/2)B*f vanish. Thus B and B* carry f back into the radical. This is a strong equality-state transport law.

## 2. Causal/reflected symmetry does not force vanishing

Suppose JHJ=H, Jf=epsilon f, and JBJ=B*. Reflection exchanges the two terms on the right of (1.1). Hence

    <Bf,HBf>=<B*f,HB*f>,                                (2.1)

and

    <f,[B*,[H,B]]f>=2<Bf,HBf>.                         (2.2)

The scalar is parity-even and nonnegative. Reflection does not change its sign. Therefore it cannot be set to zero by pairing a parity vector with an odd operator.

Nor may cyclicity of trace be used: (1.1) is a vector state, not a finite trace of a commutator. In general it is strictly positive.

## 3. Relation to the phase-161 boundary terms

Take H to be the nonnegative primitive compression at first contact and B to be a bounded, Tate-corrected finite causal synthesis. Expanding B through P_0 and Q=I-P_0 converts (1.1) into:

1. interior primitive energies of Bf and B*f;
2. the off-diagonal compression blocks P_0BQ and QBP_0;
3. finite Tate normal components.

The off-diagonal blocks are the same one-sided integer-minus-continuum discrepancies isolated in R161_006 and R161_057. Thus the desired quadratic reciprocity would follow from

    <f,[B*,[H,B]]f>=0.                                  (3.1)

But (3.1) is not a formal consequence of Hf=0; (1.1) shows that it is exactly the assertion that both causal orientations preserve the first-contact radical.

The Tate projection does not change this conclusion. It can remove the two finite normal coordinates, but the primitive energies on the right of (1.1) remain nonnegative and unconstrained.

## 4. Consequence for PC-ren

For (PC-ren) to close through the double-commutator route, its mixed Green expansion must prove (3.1), or prove that the left side equals the negative of another nonnegative Gamma/polar energy. Merely rewriting the linear PC identity inside the commutator returns Hf=0 and supplies no vanishing of the two terms in (1.1).

This gives a sharp acceptance test for the remaining calculation:

    finite PC mixed pairing
      =-<f,[B*,[H,B]]f>-D_N^Gamma(F),                 (4.1)

with the left side zero by a source identity and D_N^Gamma>=0. If (4.1) is derived with all projections and Tate terms, then every term vanishes and D closes. Defining the mixed pairing by the right side would be circular.

## 5. Status

- radical double-commutator identity and positivity: proved;
- reflection equality of the two causal energies: proved;
- vanishing from parity or formal commutator cyclicity: rejected;
- identification of reciprocity with radical invariance under both causal orientations: proved;
- derivation of the negative balance (4.1) from PC-ren: open;
- D: open.
