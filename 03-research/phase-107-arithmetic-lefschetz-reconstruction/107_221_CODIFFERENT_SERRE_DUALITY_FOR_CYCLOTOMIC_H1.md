# 107.221 -- Codifferent Serre duality for the cyclotomic middle term

## 1. Why equal orders were not enough

For the component complex of 107_217--107_219, put

\[
 I=(a,b)\subset O_K.
\]

The untwisted calculation gives

\[
 H^0(C_{O_K})=O_K/I,
 \qquad H^1(C_{O_K})=I^{-1}/O_K.
 \tag{1.1}
\]

These groups have equal cardinality, but this does not make them
canonically Pontryagin dual.  The trace-dual lattice of \(O_K\) is the
codifferent

\[
 \mathfrak D_K^{-1}
 =\{y\in K:\operatorname{Tr}_{K/\mathbb Q}(yO_K)\subset\mathbb Z\},
\]

not \(O_K\) itself.

## 2. The dualizing twist

Tensor the same Koszul differential with
\(\mathfrak D_K^{-1}\):

\[
 C_{\mathfrak D^{-1}}:
 0\to\mathfrak D^{-1}
 \xrightarrow{(-b,a)}(\mathfrak D^{-1})^2
 \xrightarrow{(a,b)}\mathfrak D^{-1}\to0.
 \tag{2.1}
\]

The Dedekind-domain calculation gives

\[
 H^1(C_{\mathfrak D^{-1}})
 =I^{-1}\mathfrak D^{-1}/\mathfrak D^{-1}.
 \tag{2.2}
\]

### Theorem 2.1 (perfect componentwise duality)

The trace pairing

\[
 (O_K/I)\times
 (I^{-1}\mathfrak D^{-1}/\mathfrak D^{-1})
 \longrightarrow\mathbb Q/\mathbb Z,
 \qquad
 (\bar x,\bar y)\longmapsto
 \operatorname{Tr}_{K/\mathbb Q}(xy)\bmod\mathbb Z
 \tag{2.3}
\]

is well defined and perfect.

### Proof

Changing \(x\) by an element of \(I\) changes the trace by an integer
because \(yI\subset\mathfrak D^{-1}\).  Changing \(y\) by an element of
\(\mathfrak D^{-1}\) also changes it by an integer.

If \(y\in I^{-1}\mathfrak D^{-1}\) pairs integrally with every
\(x\in O_K\), the definition of the codifferent gives
\(y\in\mathfrak D^{-1}\).  Thus the right kernel is zero.  Finally,

\[
 [O_K:I]
 =[I^{-1}\mathfrak D^{-1}:\mathfrak D^{-1}]
 =N(I),
\]

so injectivity between finite groups of equal order proves perfection.
\(\square\)

## 3. Consequence for the Phase 107 H1 route

The direct adelic map rejected in 107_220 is replaced by a canonical
dual interface:

\[
 \boxed{
 H^0(C_{O_K})^\vee
 \cong H^1(C_{\mathfrak D^{-1}}).}
 \tag{3.1}
\]

The codifferent plays the local role of the dualizing sheaf.  Omitting
it would amount to choosing a noncanonical self-dualization of the
cyclotomic integer lattice.  For every nontrivial cyclotomic field that
lattice has discriminant greater than one, so the omission is genuine.

This supplies componentwise Serre duality and is compatible with the
open-and-closed level transitions of 107_219.  It still does not identify
the Connes--Consani canonical divisor \(K=-2\{2\}\) with the collection
of cyclotomic differents, nor construct a global dualizing object on a
two-dimensional square.  That comparison is the next required theorem.

## 4. Falsifier

`107_221_codifferent_serre_duality_for_cyclotomic_h1.sage` computes the
actual different, codifferent, augmentation ideal and trace lattices on
the three nontrivial mixed components of 107_219.  In bases of
\(I^{-1}\mathfrak D^{-1}\), it verifies that the codifferent inclusion
has index \(N(I)\) and that its trace matrix against \(O_K\) is integral
unimodular.  It separately rejects the false self-duality
\(O_K=O_K^\vee\) using the field discriminant.

