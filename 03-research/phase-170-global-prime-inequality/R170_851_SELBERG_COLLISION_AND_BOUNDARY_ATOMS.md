# R170_851 — Selberg collision of the Möbius law and boundary atoms of the extracted port

## 0. Verdict

The law of R170_850 is exact, but its possible completion with the
synchronized channel was a mistaken identification. Algebraically,

\[
 \boxed{
 \gamma_\Lambda
 =\Lambda\log-\Lambda*\Lambda.}                              \tag{0.1}
\]

The Selberg identity is

\[
 \boxed{
 W:=\mu*\log^2
 =\Lambda\log+\Lambda*\Lambda.}                              \tag{0.2}
\]

Thus

\[
 \gamma_\Lambda+W=2\Lambda\log.                              \tag{0.3}
\]

But the synchronized channel of R170_841 vanishes on `k<=N` and
retains only the incomplete hyperbola `k>N`; it does not supply `W` in
the interior. Using (0.2) separately reproduces exactly R162_501:
`W>=0` gives no sign to the pairing with `c_F'`.

Moreover, the separation of the ports in R170_849 must be understood
distributionally. `dot S_N` applied separately to `P A F` and `Q A F`
creates atoms at the moving endpoints; only the sum has the type of the
original jet.

## 1. Direct proof of the difference identity

Set

\[
 \mathcal L(s)=-{\zeta'(s)\over\zeta(s)}
 =\sum_{n\ge2}{\Lambda(n)\over n^s}.
\]

From R170_843,

\[
 {B_\Lambda(s)\over\zeta(s)}
 ={\zeta''\over\zeta}-2\left({\zeta'\over\zeta}\right)^2.
\]

Since `zeta'/zeta=-mathcal L`,

\[
 {\zeta''\over\zeta}=\mathcal L^2-\mathcal L',
\]

and therefore

\[
 {B_\Lambda\over\zeta}=-\mathcal L'-\mathcal L^2.           \tag{1.1}
\]

Now

\[
 -\mathcal L'(s)
 =\sum_n{\Lambda(n)\log n\over n^s},
 \qquad
 \mathcal L(s)^2
 =\sum_n{(\Lambda*\Lambda)(n)\over n^s}.
\]

Uniqueness of Dirichlet series proves (0.1). This agrees with the
values by `omega(n)` of R170_850.

## 2. The synchronized channel does not complete Selberg

R170_841 Theorem 3.1 gives

\[
 \dot H_{M,N}^\Lambda
 =-\sum_{N<k\le MN}{h_{M,N}(k)\log k\over\sqrt k}
       \partial_t\tau_{\log k}.                              \tag{2.1}
\]

In particular, its coefficient is zero for every `k<=N`. By contrast,
`W(k)>0` already at each prime power `k<=N`. Hence (2.1) cannot be
identified with the missing channel `W` of (0.3).

Introducing (0.2) as a second identity does reconstruct the prime
virial, but gives

\[
 -2\sum_{n<e^{2T}}{W(n)\over\sqrt n}c_F'(\log n),             \tag{2.2}
\]

whose sign is not determined. This is literally R162_501
Proposition 3.1(a) and R170_841 §4.3. So the Möbius law reduces the
arithmetic carrier, but does not by itself overcome the Selberg no-go.

## 3. Differentiating after cutting creates atoms

Let `P=P_T`, viewed as multiplication by `1_(-T,T)`, and let `g` be
smooth near the endpoints. Distributionally,

\[
 \partial_t(Pg)
 =P g'+g(-T+)\delta_{-T}-g(T-)\delta_T.                       \tag{3.1}
\]

For `Q=I-P`,

\[
 \partial_t(Qg)
 =Q g'-g(-T+)\delta_{-T}+g(T-)\delta_T.                       \tag{3.2}
\]

The atoms cancel only in the sum of (3.1)--(3.2). After a translation
`tau_a`, they appear at `-T-a` and `T-a` with the corresponding causal
convention.

Since

\[
 \dot S_N=-\sum_{n\le N}{\log n\over\sqrt n}
                 \partial_t\tau_{\log n},                    \tag{3.3}
\]

the two pieces of R170_849 (2.2)

\[
 P\dot S_NP A_MF,
 \qquad P\dot S_NQ A_MF                                    \tag{3.4}
\]

are not, separately, trace-condition-free `L^2` ports. Their internal
atoms cancel in

\[
 \boxed{P\dot S_N(P+Q)A_MF=P\dot S_NA_MF.}                  \tag{3.5}
\]

This does not invalidate the R170_849 (2.2) extraction as an identity
in the distributional core, but it forbids assigning a sign or Tate
coordinate to the first piece before combining it with the second.

## 4. Correct combined port

The extraction formula must be written as

\[
\boxed{
 P\dot A_MF
 =B_{N,T}P\mathcal C_{M,N}F
  +B_{N,T}P\dot S_NA_MF
  -B_{N,T}PS_NQ\dot A_MF.}                                  \tag{4.1}
\]

Here the second term jointly contains Tate and exterior content; it is
not separated until the sum of atoms has cancelled. On first contact
one may use `PA_MF=r_F`, but `QA_MF` must simultaneously be kept
inside the same `dot S_N`.

The moving connection of R170_845 must be compared with the Tate
projection of the whole combined port

\[
 \mathcal P_{N,T}^{\rm comb}(F)
 :=B_{N,T}P\dot S_NA_MF-B_{N,T}PS_NQ\dot A_MF,               \tag{4.2}
\]

not with the isolated `B P dot S r_F`.

## 5. Status and next gate

```text
gamma = Lambda log-Lambda*Lambda                           PROVED
gamma+W=2 Lambda log                                       PROVED
identification of the synchronized tail with W              REJECTED
collision with the Selberg no-go                            PROVED
boundary atoms of dotS P and dotS Q                         PROVED
distributional cancellation in the combined port            PROVED
correct combined port (4.2)                                 DEFINED
its Tate projection and cancellation with dotPi              OPEN
VIR--LB / D                                                  OPEN
```

The next legitimate step is to apply the Tate projection to (4.2) as a
whole, using the residues of R161_009 only after the atom
cancellation. Any computation that projects only `dot S r_F` would
repeat a domain error.
