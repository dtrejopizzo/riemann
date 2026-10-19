# R183.007 — Positive Gram family and the polar kernel test

## 0. Result

R183.006's fiber matrix is not merely Eulerian: for \(s>0\) it is an explicit Gram matrix and hence positive. This provides a rigorous criterion for inheriting a sign in the Laurent finite part. The criterion requires the vector to lie in the kernel of the polar residue.

The computation also reveals a limitation: the polar residue of the isolated Möbius family does not have rank two; it contains the full Gram matrix of translations of the test. Hence the two Tate moments do not automatically annihilate it. Positivity of the finite part cannot be deduced before combining this family with its Poisson image and the Gamma channel. The object that must have rank-two residue is the **completed difference**, not the isolated Möbius fiber.

## 1. Gram realization

Fix a finite set \(A\subset M_S\) of indices and \(h\in L^2(-T,T)\). For \(s>0\), define

\[
 K_{S,h}^{(s)}(a,b)
 ={1\over\sqrt{ab}}
  \sum_{\substack{d\in M_S\\(d,ab)=1}}
  {\mu(da)\mu(db)\over d^{1+s}}
  c_h\!\left(\log{b\over a}\right).                \tag{1.1}
\]

The condition \((d,ab)=1\) can be dropped if \(\mu(n)=0\) is adopted for non-squarefree \(n\). For \(z=(z_a)_{a\in A}\), rearranging absolutely convergent sums gives

\[
 \boxed{
 \sum_{a,b\in A}z_a\overline{z_b}K_{S,h}^{(s)}(a,b)
 =\sum_{d\in M_S}{1\over d^{1+s}}
   \left\|\sum_{a\in A}{z_a\mu(da)\over\sqrt a}D_ah
   \right\|_2^2\ge0.}                               \tag{1.2}
\]

Hence \(K_{S,h}^{(s)}\ge0\) for every \(s>0\), for a reason prior to the spectrum.

## 2. Positive Laurent lemma

### Lemma 2. `PROVED`

Let, in finite dimension,

\[
 K(s)={K_{-1}\over s}+K_0+O(s),\qquad s\downarrow0, \tag{2.1}
\]

be a Hermitian family that is positive for every \(s>0\). Then

\[
 K_{-1}\ge0,
 \qquad
 \langle v,K_0v\rangle\ge0
 \quad(v\in\ker K_{-1}).                            \tag{2.2}
\]

**Proof.** Multiplying \(\langle v,K(s)v\rangle\ge0\) by \(s\) and taking the limit proves \(K_{-1}\ge0\). If \(K_{-1}v=0\), taking the limit directly in (2.1) proves the second statement. \(\square\)

The kernel condition is necessary. The scalar family \(K(s)=s^{-1}-1\) is positive for \(0<s<1\), but its finite part is \(-1\).

## 3. Residue of the Möbius family

By R183.006, for coprime squarefree indices the residue is

\[
 K_{-1}(a,b)
 =C_S r_a\overline{r_b}\,
       c_h\!\left(\log{b\over a}\right),
 \qquad r_a={\mu(a)\rho(a)\over\sqrt a}.           \tag{3.1}
\]

Let \(G_h(a,b)=c_h(\log(b/a))\). Then

\[
                  K_{-1}=C_S D_rG_hD_r^*.           \tag{3.2}
\]

In particular,

\[
 \langle z,K_{-1}z\rangle
 =C_S\left\|\sum_a z_ar_aD_ah\right\|_2^2.         \tag{3.3}
\]

Hence

\[
 \boxed{
 z\in\ker K_{-1}
 \Longleftrightarrow
 \sum_a z_ar_aD_ah=0.}                              \tag{3.4}
\]

This is a full functional condition, not two scalar equations. For a finite family of distinct translations of a compact \(h\ne0\), the functions \(D_ah\) are linearly independent: Fourier transforming,

\[
 \widehat h(\tau)\sum_a z_ar_ae^{i\tau\log a}=0,    \tag{3.5}
\]

and \(\widehat h\) does not vanish identically; independence of exponentials forces \(z_ar_a=0\) for every \(a\). Hence, in generic truncations,

\[
                         \ker K_{-1}=\{0\}.         \tag{3.6}
\]

The two Tate moments alone cannot turn (3.4) into a codimension-two condition.

## 4. Consequence for the bridge

R183.006's provisional statement (5.1) cannot be obtained simply by taking the finite part of the positive family (1.2). First a completed combination must be formed:

\[
 \mathcal K_{S,h}^{\rm comp}(s)
 =\mathcal K_{S,h}^{\rm Euler}(s)
  +\mathcal K_{S,h}^{\rm Poisson}(s)
  +\mathcal K_{h}^{\Gamma}(s),                     \tag{4.1}
\]

keeping the two Tate terms. The checkable requirement is

\[
 \operatorname*{Res}_{s=0}\mathcal K_{S,h}^{\rm comp}(s)
 =T_-^*T_-+T_+^*T_+,                               \tag{4.2}
\]

with \(T_\pm h=\int h(x)x^{\pm1/2}d^*x\). Only then is the primitive space \(\ker T_-\cap\ker T_+\) contained in the residue's kernel, and only then can Lemma 2 transfer positivity to the finite part.

But Lemma 2 also requires

\[
             \mathcal K_{S,h}^{\rm comp}(s)\ge0
             \quad(s>0).                            \tag{4.3}
\]

Form (4.1) must therefore be built as a single adelic Gram matrix; separately summing a positive Euler family and signed Poisson/Gamma terms is not enough.

## 5. New precise target

**Completed Gram theorem (NO-GO for the raw Gram matrix; OPEN only for a prior relative cancellation).** Build, for \(s>0\), a source operator \(\mathcal A_{S,h}(s)\) on the semilocal Schwartz--Bruhat space such that

\[
 \mathcal K_{S,h}^{\rm comp}(s)
 =\mathcal A_{S,h}(s)^*\mathcal A_{S,h}(s),         \tag{5.1}
\]

\[
 \operatorname*{Res}_{s=0}\mathcal K_{S,h}^{\rm comp}(s)
 =T_-^*T_-+T_+^*T_+,                               \tag{5.2}
\]

and

\[
 \operatorname{FP}_{s=0}\mathcal K_{S,h}^{\rm comp}(s)
 =-M_h^*A_SM_h                                      \tag{5.3}
\]

with the semilocal trace's normalizations. Then Lemma 2 proves Weil's inequality on the two vanishing moments.

This theorem is prior to the spectrum and combines Euler, Poisson, and Gamma into a single Gram matrix. It fails for a Beurling system lacking a self-dual additive Fourier transform, because there the Poisson summand of (4.1) does not exist.

## 6. Logical status

* Positive realization (1.2): **PROVED**.
* Laurent lemma on the polar kernel: **PROVED**.
* Residue of the isolated fiber (3.1)--(3.4): **PROVED**.
* Generic kernel trivial at finite cutoff: **PROVED**.
* "The two moments annihilate the isolated Möbius residue": **REFUTED**.
* Identity (5.2) for the raw Gram matrix: **REFUTED** by R183.008.
* Relative Gram matrix with prior white-light cancellation: **OPEN**.
* Row D: **OPEN**.
