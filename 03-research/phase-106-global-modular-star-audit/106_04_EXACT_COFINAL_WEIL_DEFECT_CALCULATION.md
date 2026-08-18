# 106.04 — Exact cofinal Weil-defect calculation

## Result

At a fixed physical cutoff \(L=2\log\lambda\), the canonical connection of
106.03 has an explicit intertwining defect. It is not a generic dense matrix.
It is the sum of

1. two rank-one ground-state transport channels of opposite parity; and
2. a double-operator-integral transform of another rank-two displacement.

No zero of \(\Xi\) enters the formula. Every quantity is obtained from two
consecutive finite Weil matrices and hence from the polar, Gamma and Euler
entries of E101.093.

The calculation reduces fixed-\(L\) trace-resolvent convergence to two
quantitative source estimates:

\[
\left\|S_{N+1}^{1/2}D_{0,N+1}
       (I_N\xi_N-\xi_{N+1})\right\|,
\qquad
\frac{\Delta_N}{m_N^2}
\quad\text{with}\quad
m_N=\min\operatorname{Spec}S_N.
\tag{1}
\]

The first is graph-norm convergence of consecutive ground states. The second
measures whether the decrease of the ground energy is small relative to the
first positive quotient gap. Neither estimate has yet been proved uniformly.
A further \(L\to\infty\) or diagonal \((L,N(L))\) theorem is also required to
identify the limiting divisor with that of \(\Xi\).

## 1. Source data and quotient coordinates

Fix \(L\) and let

\[
V_N=\operatorname{span}\{U_k:|k|\leq N\},
\qquad
D_{0,N}U_k=kU_k.
\tag{2}
\]

Let \(I_N:V_N\to V_{N+1}\) be the standard Fourier inclusion. The exact finite
Weil matrices satisfy

\[
W_N=I_N^*W_{N+1}I_N.
\tag{3}
\]

Their entries are E101.093(2.6)--(2.9): the complete coupled polar,
archimedean and prime-power formula.

Assume the lowest eigenvalue is simple and its ground state is even. Write

\[
\varepsilon_N=\min\operatorname{Spec}W_N,
\qquad
T_N=W_N-\varepsilon_NI,
\qquad
\langle\eta_N,\xi_N\rangle=1,
\tag{4}
\]

where \(\eta_N=\sum_{|k|\leq N}U_k\). Put

\[
K_N=(\mathbb C\xi_N)^\perp,
\qquad
P_N=P_{K_N},
\qquad
S_N=T_N|_{K_N},
\qquad
a_N=D_{0,N}\xi_N,
\qquad
b_N=P_N\eta_N.
\tag{5}
\]

The dimensionless source operator is

\[
A'_N=D_{0,N}-|a_N\rangle\langle\eta_N|,
\qquad
A'_N\xi_N=0.
\tag{6}
\]

With \(c_L=2\pi/L\), the physical quotient operator represented on \(K_N\)
is

\[
D_N=c_LP_NA'_N|_{K_N}
   =c_L\bigl(P_ND_{0,N}P_N-|a_N\rangle\langle b_N|\bigr).
\tag{7}
\]

It is self-adjoint in the positive metric \(S_N\):

\[
S_ND_N=D_N^*S_N.
\tag{8}
\]

## 2. Canonical connection

Set

\[
\Delta_N=\varepsilon_N-\varepsilon_{N+1}\geq0,
\qquad
C_N=P_{N+1}I_N|_{K_N},
\tag{9}
\]

and

\[
B_N=(S_N+\Delta_NI)^{-1/2}S_N^{1/2},
\qquad
j_N=C_NB_N.
\tag{10}
\]

The compression identity of 106.03 gives

\[
C_N^*S_{N+1}C_N=S_N+\Delta_NI,
\qquad
j_N^*S_{N+1}j_N=S_N.
\tag{11}
\]

Thus \(j_N\) is the canonical isometry between the shifted-Weil quotient
metrics.

## 3. Exact rank-two cross-level defect

Define the ground-state difference and its two projections

\[
e_N=I_N\xi_N-\xi_{N+1},
\qquad
u_N=D_{0,N+1}e_N,
\qquad
v_N=P_{N+1}I_N\xi_N=P_{N+1}e_N.
\tag{12}
\]

### Theorem 1 — Uncorrected transport is rank two

On \(K_N\),

\[
\boxed{
X_N:=D_{N+1}C_N-C_ND_N
=c_L|u_N\rangle\langle b_N|
 +\frac{c_L}{\|\xi_N\|^2}|v_N\rangle\langle a_N|.
}
\tag{13}
\]

The first channel maps the even sector to the odd sector, and the second
maps the odd sector to the even sector. Consequently the two nonzero
singular values of \(X_N\) are exactly

\[
c_L\|u_N\|\,\|b_N\|,
\qquad
\frac{c_L\|v_N\|\,\|a_N\|}{\|\xi_N\|^2}.
\tag{14}
\]

### Proof

For \(x\in K_N\), use \(A'_{N+1}\xi_{N+1}=0\) to remove the projection in
the argument of \(A'_{N+1}\). Then

\[
\begin{aligned}
X_Nx
&=c_LP_{N+1}
   \left(A'_{N+1}I_N-I_NP_NA'_N\right)x\\
&=c_LP_{N+1}
   \left(A'_{N+1}I_N-I_NA'_N\right)x
  +c_LP_{N+1}I_N(I-P_N)A'_Nx.
\end{aligned}
\tag{15}
\]

Because \(D_{0,N+1}I_N=I_ND_{0,N}\) and
\(\langle\eta_{N+1},I_Nx\rangle=\langle\eta_N,x\rangle\), the first term in
(15) is

\[
c_L|u_N\rangle\langle b_N|x.
\tag{16}
\]

The second is

\[
\frac{c_L}{\|\xi_N\|^2}
P_{N+1}I_N|\xi_N\rangle\langle(A'_N)^*\xi_N|x.
\tag{17}
\]

Evenness of \(\xi_N\) makes \(a_N=D_{0,N}\xi_N\) odd, so
\(\langle a_N,\xi_N\rangle=0\) and
\((A'_N)^*\xi_N=a_N\). Equations (16)--(17) prove (13). The parity sectors
in the domain and range are orthogonal, which proves (14). \(\square\)

The ordinary ground-line rotation already has the exact energy identity

\[
\boxed{
\|S_{N+1}^{1/2}v_N\|^2
=\Delta_N\|\xi_N\|^2.
}
\tag{18}
\]

Indeed, apply (35) of 106.03 to \(\xi_N\) and use that replacing
\(I_N\xi_N\) by \(v_N\) changes it only by the new radical vector.

## 4. The metric correction is a rank-two Loewner transform

From (7)--(8),

\[
D_N-D_N^*
=c_L\bigl(|b_N\rangle\langle a_N|
          -|a_N\rangle\langle b_N|\bigr)
\tag{19}
\]

and hence

\[
\boxed{
[D_N,S_N]
=c_L\bigl(|b_N\rangle\langle S_Na_N|
          -|a_N\rangle\langle S_Nb_N|\bigr).
}
\tag{20}
\]

In particular, this displacement also has rank at most two.

Let

\[
f_\Delta(t)=\sqrt{\frac{t}{t+\Delta}},
\qquad
B_N=f_{\Delta_N}(S_N).
\tag{21}
\]

If \(S_N=\sum_p\sigma_pE_p\), functional calculus gives the exact
divided-difference identity

\[
\boxed{
[D_N,B_N]
=\sum_{p,q}f_{\Delta_N}^{[1]}(\sigma_p,\sigma_q)
  E_p[D_N,S_N]E_q,
}
\tag{22}
\]

where

\[
f^{[1]}(x,y)=
\begin{cases}
\dfrac{f(y)-f(x)}{y-x},&x\ne y,\\[6pt]
f'(x),&x=y.
\end{cases}
\tag{23}
\]

An equivalent source formula, useful because every integrand has rank at
most two, is

\[
\boxed{
\begin{aligned}
[D_N,B_N]
=\frac{c_L\Delta_N}{\pi}
\int_0^1\sqrt{\frac r{1-r}}
\bigl(&|R_r b_N\rangle\langle S_NR_r a_N|\\
      &-|R_r a_N\rangle\langle S_NR_r b_N|\bigr)\,dr,
\end{aligned}}
\tag{24}
\]

with \(R_r=(S_N+r\Delta_NI)^{-1}\). It follows from

\[
f_\Delta(t)=\frac1\pi\int_0^1
\frac{t}{t+r\Delta}\frac{dr}{\sqrt{r(1-r)}}.
\tag{25}
\]

Since \(f_\Delta\) is operator-monotone, its Loewner matrix is positive.
Writing \(m_N=\min\operatorname{Spec}S_N\), the corresponding completely
positive Schur multiplier yields

\[
\boxed{
\|[D_N,B_N]\|_{\mathcal S_1}
\leq
\frac{\Delta_N}
 {2\sqrt{m_N}(m_N+\Delta_N)^{3/2}}
\|[D_N,S_N]\|_{\mathcal S_1}.
}
\tag{26}
\]

The analogous inequality holds for every Schatten norm
\(\mathcal S_p\), \(1\leq p\leq\infty\).

## 5. Complete formula for the intertwining defect

### Theorem 2 — Exact source formula

The arithmetic intertwining defect of 106.03 is

\[
\boxed{
\mathcal R_N=X_NB_N+C_N[D_N,B_N].
}
\tag{27}
\]

Equations (13) and (24) therefore give the completely explicit expression

\[
\boxed{
\begin{aligned}
\mathcal R_N={}&
c_L|u_N\rangle\langle B_Nb_N|
+\frac{c_L}{\|\xi_N\|^2}|v_N\rangle\langle B_Na_N|\\
&+\frac{c_L\Delta_N}{\pi}C_N
\int_0^1\sqrt{\frac r{1-r}}
\bigl(|R_rb_N\rangle\langle S_NR_ra_N|
      -|R_ra_N\rangle\langle S_NR_rb_N|\bigr)\,dr.
\end{aligned}}
\tag{28}
\]

### Proof

Insert \(j_N=C_NB_N\) and add and subtract \(C_ND_NB_N\):

\[
\begin{aligned}
D_{N+1}j_N-j_ND_N
&=(D_{N+1}C_N-C_ND_N)B_N\\
&\quad+C_N(D_NB_N-B_ND_N).
\end{aligned}
\tag{29}
\]

Now use Theorem 1 and (24). \(\square\)

## 6. Correct Schatten coordinate

Raw Euclidean norms of (28) are not the cofinal norms, because \(j_N\) is
isometric in the \(S_N\)-metrics. Define

\[
\mathsf A_N=S_N^{1/2}D_NS_N^{-1/2},
\qquad
\mathsf U_N=S_{N+1}^{1/2}j_NS_N^{-1/2}
=S_{N+1}^{1/2}C_N(S_N+\Delta_NI)^{-1/2}.
\tag{30}
\]

Then \(\mathsf A_N\) is Euclidean self-adjoint and \(\mathsf U_N\) is an
isometry. The relevant defect is

\[
\widehat{\mathcal R}_N
=S_{N+1}^{1/2}\mathcal R_NS_N^{-1/2}
=\mathsf A_{N+1}\mathsf U_N-\mathsf U_N\mathsf A_N.
\tag{31}
\]

Put \(H_N=S_N+\Delta_NI\). Equations (27) and (30) give

\[
\boxed{
\widehat{\mathcal R}_N
=S_{N+1}^{1/2}X_NH_N^{-1/2}+\mathsf U_NY_N,
}
\tag{32}
\]

where

\[
Y_N=H_N^{1/2}[D_N,B_N]S_N^{-1/2}.
\tag{33}
\]

The two exact singular values of the first term in (32) are

\[
\alpha_N
=c_L\|S_{N+1}^{1/2}u_N\|\,\|H_N^{-1/2}b_N\|,
\tag{34}
\]

\[
\boxed{
\beta_N
=\frac{c_L\sqrt{\Delta_N}}{\|\xi_N\|}
 \|H_N^{-1/2}a_N\|,
}
\tag{35}
\]

where (18) was used in (35). Moreover, (24) gives the dimension-free formula

\[
\boxed{
\begin{aligned}
Y_N=\frac{c_L\Delta_N}{\pi}
\int_0^1\sqrt{\frac r{1-r}}
\bigl(&|H_N^{1/2}R_rb_N\rangle
       \langle S_N^{1/2}R_ra_N|\\
      -&|H_N^{1/2}R_ra_N\rangle
       \langle S_N^{1/2}R_rb_N|\bigr)\,dr.
\end{aligned}}
\tag{36}
\]

Equations (34)--(36), rather than the raw norm of \(\mathcal R_N\), are the
correct quantitative target.

## 7. Resolvent consequence and the new-mode shell

For \(z\notin\mathbb R\), put

\[
G_N(z)=(\mathsf A_N-z)^{-1}.
\tag{37}
\]

Then

\[
G_{N+1}(z)\mathsf U_N-\mathsf U_NG_N(z)
=-G_{N+1}(z)\widehat{\mathcal R}_NG_N(z).
\tag{38}
\]

Consequently, with \(d=|\operatorname{Im}z|\),

\[
\|G_{N+1}\mathsf U_N-\mathsf U_NG_N\|_{\mathcal S_1}
\leq d^{-2}\|\widehat{\mathcal R}_N\|_{\mathcal S_1}.
\tag{39}
\]

Let

\[
Q_N^{\mathrm{new}}=I-\mathsf U_N\mathsf U_N^*.
\tag{40}
\]

The exact second-resolvent increment is

\[
\boxed{
\begin{aligned}
\operatorname{Tr}G_{N+1}(z)^2-\operatorname{Tr}G_N(z)^2
={}&\operatorname{Tr}\mathsf U_N^*
\bigl(G_{N+1}E_N+E_NG_N\bigr)\\
&+\operatorname{Tr}Q_N^{\mathrm{new}}
G_{N+1}(z)^2Q_N^{\mathrm{new}},
\end{aligned}}
\tag{41}
\]

where \(E_N=G_{N+1}\mathsf U_N-\mathsf U_NG_N\).

Thus a sufficient fixed-\(L\) trace-Cauchy package is

\[
\sum_N\|G_{N+1}\widehat{\mathcal R}_NG_N\|_{\mathcal S_1}<\infty,
\qquad
\sum_N\|G_{N+1}Q_N^{\mathrm{new}}\|_{\mathcal S_2}^2<\infty.
\tag{42}
\]

At this stage the second series appears independent of the intertwining
defect. Document 106.05, Theorem 7 and Corollary 8, subsequently prove a
uniform fixed-\(L\) Hilbert--Schmidt resolvent bound and show that summability
of the first series implies summability of the second. Thus the shell does
not remain an independent obligation.

## 8. Scalar boundary equation

Use the parity boundary vectors

\[
e_{N+1}^{\pm}
=\frac{U_{N+1}\pm U_{-(N+1)}}{\sqrt2}.
\tag{43}
\]

The extension \(W_N\subset W_{N+1}\) becomes one scalar arrowhead in each
parity sector. Only the even arrowhead moves the ground energy. If \(y_N^+\)
is its old-to-new column and \(z_N^+\) its new diagonal, then

\[
\boxed{
z_N^+-\varepsilon_N+\Delta_N
-\left\langle y_N^+,
(T_{N,+}+\Delta_NI)^{-1}y_N^+\right\rangle=0.
}
\tag{44}
\]

If \(T_{N,+}e_j=\mu_je_j\), \(\mu_0=0\), and
\(y_N^+=\sum_j\gamma_je_j\), this is

\[
z_N^+-\varepsilon_N+\Delta_N
-\frac{|\gamma_0|^2}{\Delta_N}
-\sum_{j\geq1}\frac{|\gamma_j|^2}{\mu_j+\Delta_N}=0.
\tag{45}
\]

Every coefficient in (44)--(45) is an explicit polar--Gamma--Euler matrix
entry. The old component of the new ground vector is the corresponding
resolvent vector

\[
x_N=-(T_{N,+}+\Delta_NI)^{-1}y_N^+t_N,
\tag{46}
\]

where \(t_N\) is fixed by the normalization in (4). Therefore the two open
quantities in (1) have been reduced to a scalar arrowhead equation and one
explicit source resolvent vector.

## 9. Reproducible diagnostic

The NumPy-only script 106_04_cofinal_weil_defect_probe.py builds one largest
exact Weil matrix and obtains every lower level by principal compression. It
evaluates (11), (13), (27), (31), (38) and (41), as well as the transported
Schatten and shell quantities.

For example:

~~~bash
python3 106_04_cofinal_weil_defect_probe.py \
  --lambda 2.2 --n-min 1 --n-max 7 --quadrature 512
~~~

In the float64-stable window, the rank-two formula (13) is reproduced with
relative residual between \(5\times10^{-16}\) and \(2\times10^{-15}\). The
raw defect is dominated by its rank-two ground-transport part, while the
sandwiched resolvent and new-shell quantities decrease over the measured
range. These observations are diagnostic only. The quotient gap rapidly
falls below float64 resolution, so no asymptotic rate or summability claim is
made.

## 10. Binding conclusion

The abstract open symbol \(\mathcal R_N\) has now been eliminated. At fixed
\(L\), the remaining analytic theorem is precisely:

\[
\boxed{
\begin{gathered}
\text{control the graph-energy drift }
\|S_{N+1}^{1/2}D_0(I_N\xi_N-\xi_{N+1})\|,\\
\text{and control the gap-weighted Loewner correction in (36),}
\end{gathered}}
\tag{47}
\]

strongly enough to prove (42). Ordinary Hilbert-space convergence of the
ground lines is insufficient; (18) already supplies that weaker control.

Even (42) constructs only a fixed-\(L\) trace limit. The RH-bearing second
step remains a source-canonical diagonal theorem as

\[
L\to\infty,
\qquad
N=N(L),
\qquad
N(L)/L^2\to\infty,
\tag{48}
\]

which identifies the limiting second-resolvent trace with
\(-(\xi'/\xi)'\) on a safe half-plane. The stronger mesh rate in (48) is
the correction proved in 106.06 for the raw determinant: its exterior
curvature is \(O_K(L^2/N)\). If that known exterior factor is divided out
exactly, no mesh rate is needed for this term. No global source
identification is claimed here.

## Status

Proved: the rank-two cross-level formula, the rank-two displacement behind
the functional-calculus commutator, the exact Loewner integral, the
metric-conjugated defect, the ground-rotation energy identity, the scalar
arrowhead equation, and the exact trace-shell increment.

Implemented: a NumPy-only finite-level diagnostic checking all algebraic
identities.

Superseded by 106.05: scalar trace summability is proved on a cofinal
subsequence, and new-mode shell summability follows from transported-defect
summability. Open: the consecutive Gamma--Euler rate, the canonical
transported Schatten series, and the cofinal \(L\to\infty\) Gamma--Euler
identification.
