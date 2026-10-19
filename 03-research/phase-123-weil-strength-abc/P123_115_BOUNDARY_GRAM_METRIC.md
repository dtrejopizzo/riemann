# P123.115 — An operator-defined boundary Gram metric and its Levi form

Status: PROVED-IN-REPOSITORY on each fixed external
Bruhat test domain of the induced representation. This is a boundary
metric, not an identification with the intrinsic arithmetic RR metric.

## 1. A positive Fredholm Gram determinant

Put X_L(F)=(1-E_L)R(F)E_L. It depends complex linearly on F. By
P123.111, X_L(F) is Hilbert--Schmidt and

    X_L(F)*X_L(F)=E_L R(F)^*(1-E_L)R(F)E_L.

For sufficiently large L this is the endpoint defect of P123.110
for the pair (F^*,F). Hence it has the form

    X_L(F)*X_L(F)=W_L d(F^*,F) W_L*,                        (1)

where d is a positive trace-class operator on a fixed finite sum of
tangential Hilbert spaces, independent of large L. Define

    h(F)=det(1+d(F^*,F))=det(1+X_L(F)*X_L(F)).              (2)

Every factor in this positive Fredholm determinant is at least one,
so h(F)>=1. Equation (1) gives exact eventual independence of the
normal cutoff, not merely convergence of its first derivative. The
construction remains defined for all amplitudes in the fixed test
domain; unlike the logarithmic relative determinant germ, it has no
smallness restriction. It obeys

    0<=log h(F)<=Tr d(F^*,F)=B(F^*,F).                     (3)

This follows from log(1+t)<=t on nonnegative eigenvalues. The trace
is the stabilized energy from P123.111.

One concrete Hermitian metric on the trivial line over this test domain
is ||1||_F^2=h(F)^-1. This is specified by an operator Gram determinant,
not by declaring the desired intersection form to be positive. Nothing
here identifies this trivial line with the arithmetic determinant line.

## 2. Exact infinitesimal Hermitian comparison

For finitely many directions F_i put F(z)=sum_i z_i F_i. On this
finite-dimensional parameter space h is smooth and real analytic near
zero: d(F(z)^*,F(z)) is quadratic in z,bar z in trace norm, and the
Fredholm logarithm has its convergent trace series near zero. Its
quadratic term is Tr(X_L(F(z))^*X_L(F(z))). Therefore

    partial_z partial_bar_w log h(zF+wG)|_(0,0)
       =Tr(X_L(G)^*X_L(F))=B(G^*,F)=B(F,G^*).              (4)

Thus the Levi form of log h at zero is exactly the Hermitian boundary
energy, with its existing normalization. Equivalently, under the
convention that the metric potential is -log ||1||^2, its Levi form
is (4). In particular no sign convention for a Chern curvature form
is hidden in the assertion.

## 3. The relative determinant modulus is a different metric

Let lambda(F)=log Delta_F(1) be the holomorphic germ of P123.114.
The logarithm of |Delta_F(1)|^2 is 2 Re lambda(F). On every such
finite-dimensional parameter space it is pluriharmonic:

    partial_z partial_bar_w [2 Re lambda(zF+wG)]=0.         (5)

This follows directly from holomorphicity and nonvanishing near zero.
Consequently its holomorphic Hessian in P123.114 is not the Levi form
of its modulus. A modulus-only metric obtained from that holomorphic
germ cannot reproduce a nonzero energy (4) without additional metric
data. This distinguishes two valid constructions rather than retracting
the analytic second-variation identity of P123.114.

## 4. Prescribed semilocal compatibility

For normalized scalar test pullback F_T, the isometry J_ST in P123.043
satisfies R_T(F_T)=J_ST R_S(F)J_ST* and E_T J_ST=J_ST E_S. Hence

    X_T(F_T)=J_ST X_S(F)J_ST*,
    det(1+X_T(F_T)^*X_T(F_T))
       =det(1+X_S(F)^*X_S(F)).                             (6)

These hold before stabilization and give equality of h and of its
metric/Levi pullbacks afterwards. The same proof applies to unitary
section changes with the cutoffs transported. Triple compatibility
follows from the original isometries; no additional scalar factors
are introduced.

## 5. Remaining burden

This constructs a boundary metric with exact cutoff independence,
semilocal compatibility and the specified energy as its Levi form at
zero. It does not supply a multiplicative isometry law under the
convolution-unitization product, identify the underlying line with the
mixed diagonal determinant, or match the periodic ruling metric.

Moreover P123.112 shows that the analogous local anomaly energy cannot
simply be the numerical intersection form: its radical fails ideal
stability. Thus (2) is additional controlled metric data, not a shortcut
to A.6, mixed RR or global positivity. Those identifications remain open.
