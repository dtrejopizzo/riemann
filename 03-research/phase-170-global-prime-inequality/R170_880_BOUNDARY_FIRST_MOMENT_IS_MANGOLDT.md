# R170_880 — The first moment of the divisor boundary is Mangoldt

> **Cutoff audit R170_884.** The theorem of this record is correct
> for the full incidence. The physical predictor uses the finite
> incidence `m_N;T,t` of R170_879. Its first moment contains the
> truncated convolution and needs the explicit tail (2.6)--(2.8) below. Hence the
> physical application of §3 cannot omit the routes `n>N`.

## 0. Theorem

For `T>0` and `k>=1`, define the moving incidence

\[
 \mathfrak m_{T,t}(k)
 :=\sum_{n\mid k}\mu(k/n)
       1_{[\log n-T,\,\log n+T]}(t).                       \tag{0.1}
\]

Then

\[
\boxed{
 \int_{\mathbb R}\mathfrak m_{T,t}(k)\,dt
 =2T\,1_{\{k=1\}},}                                      \tag{0.2}
\]

and

\[
\boxed{
 \int_{\mathbb R}t\,\mathfrak m_{T,t}(k)\,dt
 =2T\,\Lambda(k).}                                      \tag{0.3}
\]

Thus the mass of the incidence vanishes for `k>1`, but its first moment
is exactly von Mangoldt. The identity is term by term, uniform
in `T`, and uses every integer divisor with its exact Möbius values.

## 1. Proof

Each interval of (0.1) has length `2T`. Hence

\[
 \int_{\mathbb R}\mathfrak m_{T,t}(k)\,dt
 =2T\sum_{n\mid k}\mu(k/n)
 =2T(\mu*1)(k),                                           \tag{1.1}
\]

which is (0.2).

The first moment of an interval centered at `log n` is

\[
 \int_{\log n-T}^{\log n+T}t\,dt=2T\log n.                \tag{1.2}
\]

Hence

\[
 \int_{\mathbb R}t\,\mathfrak m_{T,t}(k)\,dt
 =2T\sum_{n\mid k}\mu(k/n)\log n
 =2T(\mu*\log)(k).                                        \tag{1.3}
\]

The exact identity `mu*log=Lambda` proves (0.3). No PNT,
Selberg, positivity of `Lambda`, nor a spectral explicit formula is used.

## 2. Interior--exterior separation

Set

\[
 \mathfrak I_T(k)
 :=\int_{-T}^{T}t\,\mathfrak m_{T,t}(k)\,dt,
 \qquad
 \mathfrak E_T(k)
 :=\int_{|t|>T}t\,\mathfrak m_{T,t}(k)\,dt.                \tag{2.1}
\]

Since all centers `log n` are nonnegative, (0.1) has no support
at `t<-T` except at null endpoints. Hence `mathfrak E_T` is the right
boundary, and (0.3) gives the exact oriented law

\[
\boxed{
 \mathfrak E_T(k)=2T\Lambda(k)-\mathfrak I_T(k).}          \tag{2.2}
\]

For `t>T`, the integrand is precisely the route coefficient of
R170_879. The left orientation is obtained by applying reflection to the whole
identity; it is not counted twice in (2.2).

The interior contribution is computed without an infinite sum. For each divisor
`n|k`, let `a_n=log n`. The intersection

\[
 [-T,T]\cap[a_n-T,a_n+T]                                  \tag{2.3}
\]

is empty if `a_n>=2T`, and is `[a_n-T,T]` if `0<=a_n<2T`.
Consequently,

\[
\boxed{
 \mathfrak I_T(k)
 ={1\over2}\sum_{\substack{n\mid k\\n<e^{2T}}}
 \mu(k/n)\bigl(T^2-(\log n-T)^2\bigr).}                  \tag{2.4}
\]

Equivalently,

\[
 \mathfrak I_T(k)
 =\sum_{\substack{n\mid k\\n<e^{2T}}}
 \mu(k/n)\left(T\log n-{(\log n)^2\over2}\right).       \tag{2.5}
\]

Thus (2.2) expresses the exterior moment via `Lambda(k)` minus a
finite polynomial over the divisors visible in the window.

### 2.1. Correction for the cutoff `N`

For the physical incidence `mathfrak m_N;T,t` of R170_879,

\[
 \int\mathfrak m_{N;T,t}(k)\,dt
 =2T\sum_{\substack{n\mid k\\n\le N}}\mu(k/n),             \tag{2.6}
\]

\[
 \int t\mathfrak m_{N;T,t}(k)\,dt
 =2T\sum_{\substack{n\mid k\\n\le N}}
      \mu(k/n)\log n.                                     \tag{2.7}
\]

In particular, (0.2)--(0.3) are automatically recovered for `k<=N`.
For `k>N`, the physical first moment is

\[
\boxed{
 2T\Lambda(k)
 -2T\sum_{\substack{n\mid k\\n>N}}\mu(k/n)\log n.}       \tag{2.8}
\]

The last term is the hyperbolic tail of the integer cutoff and must
be kept together with `R_M=L-L_M`.

## 3. Ward coefficient identity

Multiply (2.2) by any family of scalars `w(k)` for which
the sum is finite or absolutely convergent. One obtains

\[
\boxed{
 \sum_k w(k)\mathfrak E_T(k)
 +\sum_k w(k)\mathfrak I_T(k)
 =2T\sum_k\Lambda(k)w(k).}                                \tag{3.1}
\]

For the physical weights

\[
 w_F(k)={1\over\sqrt k}\,\mathcal R_F(\log k),             \tag{3.2}
\]

where `R_F` is any of the linear collars appearing before the
diagonal, (3.1) turns the first moment of the factorization
boundary into the exact prime coefficient. The specific choice of
`R_F` must respect the order of R170_856; (3.1) does not authorize substituting it
with `c_F` after recombining.

This is a Ward law at the coefficient level:

```text
exterior moment + interior moment = Mangoldt force.
```

## 4. Relation to the Wronskian

The antidiagonal derivation marks each translation by its length
`log n`. R170_879 shows that the amplitude of each exterior route is
`m_T,t(k)`. Hence (0.3) identifies the weight that must appear when summing
the exterior flow with the interior concomitant: it is not a postulated
coefficient, but `Lambda(k)` produced by the first moment of the cut.

To close R170_853 one still needs to prove that the physical pairing

\[
 (\dot q^{\,0},z_F)-(q,\dot z_F^{\,0})                    \tag{4.1}
\]

disintegrates with the same weight `w_F(k)` in both members of (3.1), and
that the polar continuum contributes exactly the endpoints of (2.4). This is
a statement about typing and operator order; (0.3) alone gives it no sign.

The new acceptance criterion is concrete: expand (4.1) and the polar term
in routes `(n,m)`, group by `k=nm`, and check that the coefficient of
each collar is the left-hand side of (3.1). If this holds, the right-hand side is
the exact prime virial force and no free exterior residue remains.

## 5. Status

```text
mass of the incidence = 2T delta_1                         PROVED
first moment = 2T Lambda(k)                                PROVED
oriented interior/exterior separation                      PROVED
finite formula for the interior moment                     PROVED
Ward coefficient identity, equation (3.1)                  PROVED
identification of the physical Wronskian weight with (3.2) OPEN
exact cancellation of the polar continuum                   OPEN
VIR--LB / D                                                 OPEN
```
