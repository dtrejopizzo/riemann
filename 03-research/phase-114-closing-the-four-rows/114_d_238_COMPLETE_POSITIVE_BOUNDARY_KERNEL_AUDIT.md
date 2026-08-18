# D.238 — The raw boundary coupling is a negative completely positive kernel

## Verdict

Combining D.190 with the Euler--Poisson resummation of D.236 shows that the
uncompressed old/shell coupling has one sign and one common-target
factorization.  For disjoint support projections (P_O P_E=0),

\[
 \boxed{
 P_OQ_TP_E=-P_O\mathcal K_TP_E,
 }                                                     \tag{0.1}
\]

where

\[
 \mathcal K_T=K_{\Gamma,T}+R_{1/2,T}
 +\sum_{p<e^{2T}}(\log p)V_p^*V_p\ge0.              \tag{0.2}
\]

Here (K_{\Gamma,T}) is the positive Gamma integral kernel between
disjoint sets, (R_{1/2,T}) has kernel (e^{-|t-s|/2}), and

\[
 V_p=\sqrt{1-p^{-1}}(I-p^{-1/2}S_{\log p})^{-1}.
\]

The identity term in D.236(0.2) has no old/shell block, which is why the
whole tower contributes (-(log p)P_OV_p^*V_pP_E).  Thus the
infinite-rank coupling is the negative of a completely positive common
feature Gram.  The two Tate projections add a perturbation of rank at most
four, as in D.190.

This is a genuine sharpening of the raw shift expansion, but it does not
imply the sharp Douglas inequality.  A symmetric operator with nonpositive
off-diagonal kernel can have arbitrarily many negative eigenvalues after a
diagonal potential is subtracted.  To close row D through this structure
one needs an independent oscillation/ground-state theorem proving that the
Morse index of the uncompressed form is at most two and that its negative
subspace is detected by the two Tate functionals.  That assertion is
equivalent to primitive positivity and therefore cannot be inferred from
the sign of (0.1) alone.

## 1. Common-target factorization

On disjoint old and shell sets the Gamma difference form polarizes as

\[
 H_{5/4,T}(f,e)
 =-\langle K_{\Gamma,T}^{1/2}f,
          K_{\Gamma,T}^{1/2}e\rangle,               \tag{1.1}
\]

in the standard common-feature interpretation of its positive kernel.
The resolvent term satisfies the analogous identity with the positive
kernel (e^{-|t-s|/2}).

For one prime, D.236 gives

\[
 -\sum_{k\ge1}{\log p\over p^{k/2}}
 (S_{k\log p}+S_{-k\log p})
 =(\log p)(I-V_p^*V_p).                             \tag{1.2}
\]

Multiplying (1.2) on the left by (P_O) and on the right by (P_E)
removes the identity term.  Summing (1.1)--(1.2) and observing that the
scalar term (-\beta I) also has zero cross block proves (0.1)--(0.2).

Equivalently, introduce the common target

\[
 \mathscr H_{OE}=mathscr H_\Gamma\oplus
 \mathscr H_{1/2}\oplus\bigoplus_{p<e^{2T}}L^2(\mathbb R)
\]

and the feature

\[
 \mathcal VF=
 \left(K_{\Gamma,T}^{1/2}F,
       R_{1/2,T}^{1/2}F,
       (\sqrt{\log p}\,V_pF)_p\right).              \tag{1.3}
\]

Then

\[
 P_OQ_TP_E=-(\mathcal VP_O)^*(\mathcal VP_E).       \tag{1.4}
\]

Formula (1.4) is source-defined, contains the full Gamma place and every
prime power, and uses no zero or sign assumption.

## 2. Tate compression

Let (Pi_T=I-F_T) be the projection onto the two-Tate primitive space,
with (operatorname {rank}F_T\le2).  Expanding

\[
 P_O\Pi_TQ_T\Pi_TP_E
\]

around (P_OQ_TP_E) produces

\[
 -P_OF_TQ_TP_E-P_OQ_TF_TP_E+P_OF_TQ_TF_TP_E,       \tag{2.1}
\]

which has rank at most four on every finite-energy regularization and is a
finite-rank form perturbation on the closed domain.  Therefore the
primitive cross is a negative completely positive boundary kernel plus a
known finite-rank correction.  The correction cannot transport the
infinite-rank range by itself.

## 3. Exact obstruction to an M-matrix shortcut

There is a sharper obstruction on an integer birth cell.  Let (E) be a
born shell whose length is smaller than every active translation
(k\log p).  Then

\[
 P_EU_p^kP_E=0\qquad(k\ge1),                         \tag{3.1}
\]

and D.236(0.1) gives

\[
 \boxed{P_EV_p^*V_pP_E=P_E.}                        \tag{3.2}
\]

Therefore the two terms in the local prime defect cancel exactly on the
born diagonal:

\[
 P_E(\log p)(I-V_p^*V_p)P_E=0.                      \tag{3.3}
\]

After summing over active primes, separating the positive identity and
Poisson pieces would introduce two artificial diagonal masses of size

\[
 \sum_{p\le N}\log p=\vartheta(N)\sim N,            \tag{3.4}
\]

which cancel before the actual Schur problem is formed.  The real
prime-power birth contribution is an off-diagonal bridge, not either of
these positive masses.  Hence a dilation which treats (I) and
(V_p^*V_p) as independent budgets is necessarily too coarse by order
(N); it cannot recover the sharp constant-one capacity whose natural
scale is logarithmic.

This proves that the common feature (1.3) must be used in a conservative
colligation retaining the cancellation (3.3), not through a triangle or
Cauchy--Schwarz estimate on its two positive pieces.

### Off-diagonal sign is still insufficient

Nonpositive off-diagonal entries do not control the number of negative
eigenvalues.  For any (m\ge1), the finite matrix

\[
 A_m=\varepsilon I_m-\mathbf1_m\mathbf1_m^t
       -cI_m                                        \tag{3.5}
\]

has nonpositive off-diagonal entries, while choosing (c>\varepsilon)
makes all (m) eigenvalues negative.  The same phenomenon occurs for a
Dirichlet form minus an uncontrolled local potential.  Hence (0.1) alone
cannot prove that only the two polar directions are negative.

In the present operator the diagonal and local terms are fixed, so (3.1)
is not a counterexample to row D.  It proves the logical point: a theorem
deducing primitive positivity must use more than positivity of the common
boundary kernel.  It must use the exact Gamma/prime diagonal balance,
support geometry and the two Tate characters.

## 4. Admissible next theorem

The common feature (1.3) suggests a precise alternative form of the
D.190 target.  Construct a source-defined map

\[
 \Theta_T:\overline{\mathcal VP_E\mathcal P_T}
 \longrightarrow\overline{\mathcal VP_O\mathcal P_T}              \tag{4.1}
\]

whose graph incorporates the finite Tate correction (2.1), and prove the
exact defect identity

\[
 B_E-C_{OE}^*C_{OE}=Z_T^*Z_T,                       \tag{4.2}
\]

with (C_{OE}) induced by (Theta_T).  Defining (Theta_T) by the
old-core pseudoinverse is forbidden: it would restate D.190(0.3).  A valid
construction must come from the Euler resolvents in (1.3), the Gamma
L\'evy state and support restriction.

## 5. Classification

* Positive common-kernel identity (0.1)--(0.2): **PROVED OPERATOR
  IDENTITY**.
* One common feature realization (1.3)--(1.4): **PROVED**.
* Exact cancellation of the order-(N) prime diagonal on a born shell:
  **PROVED**.
* Finite-rank Tate correction: **PROVED**, using D.190.
* Deduction of a two-dimensional negative index from off-diagonal sign:
  **IMPOSSIBLE WITHOUT ADDITIONAL STRUCTURE**.
* Source-defined contraction (4.1)--(4.2): **OPEN**.
* Row D: **OPEN**.
