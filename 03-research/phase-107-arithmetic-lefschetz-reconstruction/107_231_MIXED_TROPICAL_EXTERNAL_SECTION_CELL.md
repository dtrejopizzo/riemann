# 107.231 -- A mixed tropical external section cell with product dimension

## 1. One-ruling generators from the published proof

Fix a prime \(p\) and an integer \(N>p\). Connes--Consani define

\[
 \phi_a(x)=\max\{-a(x-1),b_a(x-p)\},
 \qquad
 b_a=\left\lfloor\frac{N-a}{p}\right\rfloor,
 \tag{1.1}
\]

for \(1\leq a\leq N-p\), with \(\phi_0=0\). These functions belong
to the filtered section module

\[
 \mathcal E_{N,p}=H^0(N\{1\})^1.
\]

Put \(d=N-p+1\). Lemma 6.19 of *Geometry of the Scaling Site*
constructs constants \(c_i\) such that the functions

\[
 g_i=\phi_{N-p-i}+c_i,
 \qquad 0\leq i<d,
 \tag{1.2}
\]

have ordered intervals of strict dominance inside \([1,p]\). More
precisely, there are points \(x_i\) and gaps \(\gamma_i>0\) with

\[
 g_i(x_i)-g_k(x_i)\geq\gamma_i
 \qquad(k\ne i).
 \tag{1.3}
\]

The exact choice used here is the one in their proof: choose
\(0<t_1<\cdots<t_{d-1}<\epsilon\), set
\(c_i=-\sum_{j=0}^i t_j\), and take \(x_i\) in the interior of the
corresponding dominance interval.

Repeat this construction for a prime \(q\), integer \(M>q\), and

\[
 e=M-q+1,
 \]

obtaining sections \(h_j\), witness points \(y_j\), and positive gaps.

## 2. Mixed external family

On the periodic product \(C_p\times C_q\), define the external sums

\[
 B_{ij}(x,y)=g_i(x)+h_j(y),
 \qquad 0\leq i<d,\quad0\leq j<e.
 \tag{2.1}
\]

They are sections of the external divisor

\[
 \pi_1^*(N\{1\})+\pi_2^*(M\{1\})
 \tag{2.2}
\]

in the external max-plus section presheaf: sums add the two principal
divisor inequalities, and finite maxima preserve them.

Let

\[
 \Gamma=min_{i,j}\min_{(k,l)\ne(i,j)}
 \bigl(B_{ij}(x_i,y_j)-B_{kl}(x_i,y_j)\bigr)>0.
 \tag{2.3}
\]

For a coefficient matrix \(u=(u_{ij})\) with
\(|u_{ij}|<\Gamma/4\), put

\[
 F_u(x,y)=\max_{i,j}\{B_{ij}(x,y)+u_{ij}\}.
 \tag{2.4}
\]

## 3. Product-cell theorem

### Theorem 3.1

The map

\[
 \Theta:(-\Gamma/4,\Gamma/4)^{de}longrightarrow
 C(C_p\times C_q,\mathbb R),
 \qquad u\longmapsto F_u,
 \tag{3.1}
\]

is a topological embedding for the uniform topology. Its image is a
mixed section cell of covering dimension exactly \(de\).

### Proof

At \((x_i,y_j)\), (1.3) in the two factors implies that \(B_{ij}\)
strictly dominates every \(B_{kl}\), with gap at least \(\Gamma\).
A perturbation in the stated cube changes the difference between two
coefficients by less than \(\Gamma/2\), so \((i,j)\) remains the unique
maximizer. Therefore

\[
 F_u(x_i,y_j)=B_{ij}(x_i,y_j)+u_{ij}.
 \tag{3.2}
\]

Every coefficient is recovered by the continuous evaluation formula

\[
 u_{ij}=F_u(x_i,y_j)-B_{ij}(x_i,y_j).
 \tag{3.3}
\]

Thus \(\Theta\) is injective and has a continuous inverse on its image.
It is continuous because finite maximum is 1-Lipschitz in the
coefficient sup norm. Hence it is a topological embedding, and its
image has dimension \(de\). \(\square\)

This is genuinely mixed: there is one independently recoverable real
parameter for every pair \((i,j)\), rather than one parameter for each
row plus one for each column.

## 4. Correct normalized growth

Let \(\alpha\in\mathbb Z[1/p]_{>0}\) and
\(\beta\in\mathbb Z[1/q]_{>0}\). At sufficiently large depths set

\[
 N_n=\alpha p^n,
 \qquad M_m=\beta q^m.
\]

The mixed cell has exact dimension

\[
 d_ne_m=(\alpha p^n-p+1)(\beta q^m-q+1).
 \tag{4.1}
\]

Therefore, along every cofinal path,

\[
 \lim_{n,m\to\infty}p^{-n}q^{-m}d_ne_m
 =\alpha\beta.
 \tag{4.2}
\]

This is the nonzero product density which the Cartesian construction
of 107_230 necessarily loses. It also agrees with the norm-adapted
mixed ray density of 107_229.

## 5. What this constructs

The result supplies an actual family of bivariate continuous max-plus
sections, not a formal table of dimensions. It has:

1. explicit one-variable sections from the published RR proof;
2. an external divisor condition preserved by sum and maximum;
3. \(de\) independently recoverable mixed parameters;
4. the required cofinal product limit \(\alpha\beta\).

Thus the local finite-level square has enough genuine section capacity
for a nonzero bidegree-two RR term.

## 6. Scope and remaining \(H^0\) gate

This does not prove that the entire section module of the sought square
has dimension \(de\). The theorem is a lower-bound cell. The remaining
tasks are:

1. define the complete external tensor section sheaf on the chosen
   Scaling-Site square;
2. prove an upper bound of order \(de+o(p^nq^m)\);
3. prove restriction/descent compatibility and independence of the
   chosen CC dominance frame;
4. extend from the special external divisor (2.2) to arbitrary
   finite-support divisors.

No \(H^1\), RR identity, intersection product, or global proper model is
claimed here.

## 7. Exact verifier

107_231_mixed_tropical_external_section_cell.py constructs the exact
rational functions (1.1), dominance intervals, gaps, mixed basis, and
perturbed coefficient matrices for all fixed prime pairs. It recovers
every coefficient by (3.3), checks the dimension formula along balanced
and unbalanced cofinal paths, and returns NO if a mixed parameter is
deleted or forced to split as a row-plus-column coefficient.

