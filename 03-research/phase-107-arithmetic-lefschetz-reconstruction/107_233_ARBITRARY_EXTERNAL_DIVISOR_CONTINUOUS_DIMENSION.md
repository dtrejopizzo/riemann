# 107.233 -- Continuous H0 dimension for arbitrary external periodic divisors

## 1. External tensor filtration

Let \(D\in\mathrm{Div}(C_p)\) and
\(E\in\mathrm{Div}(C_q)\). At depths \(n,m\), define

\[
 \mathcal T_{D,E}^{n,m}
 =\mathrm{im}\,\left(
 H^0(D)^{p^n}\otimes_{\mathbb R_{\max}}H^0(E)^{q^m}
 \longrightarrow C(C_p\times C_q,\mathbb R_{\max})
 \right),
 \tag{1.1}
\]

where a pure tensor maps to the external sum
\((x,y)\mapsto f(x)+g(y)\), and finite tropical sums map to their
pointwise maximum.

When the limit exists, put

\[
 \mathrm{cdim}^{(2)}H^0(D\boxtimes E)
 =\lim_{n,m\to\infty}p^{-n}q^{-m}
 \mathrm{tdim}\,\mathcal T_{D,E}^{n,m}.
 \tag{1.2}
\]

## 2. Tensorization of the published squeeze maps

The proof of the one-ruling periodic RR theorem supplies the following.
If \(\delta=\deg D>0\), then for every \(\epsilon>0\) there are
\(\alpha_-,\alpha_+\in\mathbb Z[1/p]_{>0}\) such that

\[
 \delta-\epsilon<\alpha_-<\delta<\alpha_+<\delta+\epsilon
 \tag{2.1}
\]

and, at all sufficiently large depths, isometric embeddings

\[
 H^0(\alpha_-\{1\})^{p^n}hookrightarrow H^0(D)^{p^n}
 \hookrightarrow H^0(\alpha_+\{1\})^{p^n}.
 \tag{2.2}
\]

They are obtained only by adding an effective divisor and translating
sections by a fixed principal function. The congruence class
\(\chi(D)\in\mathbb Z/(p-1)\mathbb Z\) is retained when choosing the
approximants; the required class in \(\mathbb Z[1/p]\) is dense.

The same construction gives \(\beta_-,\beta_+\) and embeddings for
\(E\). These maps remain embeddings after external tensor:

1. inclusion after adding an effective divisor remains pointwise
   inclusion of section spaces;
2. translation by principal functions sends
   \(F(x,y)\) to \(F(x,y)+u(x)+v(y)\), an isometric homeomorphism;
3. composing the two operations in either ruling commutes.

Consequently, eventually in every cofinal pair \((n,m)\),

\[
 \mathcal T_{\alpha_-,\beta_-}^{n,m}hookrightarrow
 \mathcal T_{D,E}^{n,m}hookrightarrow
 \mathcal T_{\alpha_+,\beta_+}^{n,m}.
 \tag{2.3}
\]

## 3. Arbitrary-external-divisor theorem

### Theorem 3.1

For all divisors \(D\) on \(C_p\) and \(E\) on \(C_q\), the limit
(1.2) exists along every cofinal path and

\[
 \boxed{
 \mathrm{cdim}^{(2)}H^0(D\boxtimes E)
 =\max(\deg D,0)\max(\deg E,0).}
 \tag{3.1}
\]

### Proof for positive degrees

Assume \(\delta=\deg D>0\) and \(\eta=\deg E>0\). Monotonicity of
covering dimension under the embeddings (2.3), followed by the exact
special-divisor theorem 107_232, gives

\[
 \alpha_-\beta_-
 \leq\liminf p^{-n}q^{-m}\mathrm{tdim}\,\mathcal T_{D,E}^{n,m}
\]

and

\[
 \limsup p^{-n}q^{-m}\mathrm{tdim}\,\mathcal T_{D,E}^{n,m}
 \leq\alpha_+\beta_+.
\]

Letting the two approximation errors tend to zero forces both bounds
to \(\delta\eta\). The estimates do not impose a relation between
\(n\) and \(m\), so the limit is cofinal-path independent.

### Nonpositive degrees

If either degree is negative, the corresponding \(H^0\) is zero by the
published periodic theorem. If one degree is zero, its section module
is either zero or consists only of constants and has covering dimension
at most one at every depth. Tensoring with the other factor therefore
has growth at most \(O(p^n)+O(q^m)\), which vanishes after the product
normalization. This proves (3.1). \(\square\)

## 4. Consequences

The local periodic-product \(H^0\) problem is now closed for every
external divisor:

1. the filtration is intrinsic and norm-adapted;
2. the external tensor image is independent of extremal frames;
3. its continuous dimension exists cofinally;
4. the answer is the product of positive degrees;
5. the special-divisor calculation is not a calibration restricted to
   one class.

This gives the exact bidegree \((1,1)\) coefficient expected from two
rulings. It does not yet treat a divisor with an intrinsically mixed
component, such as a diagonal or Frobenius graph.

## 5. Scope and next gate

The theorem is local on one periodic product \(C_p\times C_q\). It does
not supply the cross-prime gluing absent in 107_161, a global proper
square, \(H^1\), Serre duality, or RR for mixed divisors.

The next row-(a) problem is no longer the dimension of external
sections. It is to construct the sheaf transition which embeds these
periodic tensor modules into one global square and to define the
additional section condition for diagonal/correspondence divisors.

## 6. Exact verifier

107_233_arbitrary_external_divisor_continuous_dimension.py constructs
lower and upper approximants in the prescribed component class for
five prime pairs and fixed real rational degrees not generally lying in
the local slope groups. It checks exact inequalities, shrinking product
squeeze intervals, cofinal special limits, and the zero-degree branch.
It returns NO if the component congruence is dropped or if the squeeze
fails to converge to the product of degrees.

