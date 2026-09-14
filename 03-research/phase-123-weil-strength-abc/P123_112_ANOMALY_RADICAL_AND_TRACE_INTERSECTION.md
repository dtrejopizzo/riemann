# P123.112 — The anomaly radical fails composition stability on local normal tests

Date: 2026-09-07. Status: PROVED-IN-REPOSITORY on the compact
multiplicative Bruhat test algebra of Q_q^*. This distinguishes the
local anomaly energy from a trace-of-product intersection. It does
not assert that every normal test has already been lifted to a scalar
external test in the induced representation.

## 1. Two pairings that must not be identified

Use probability unit Haar and counting valuation measure. Let D(f)
be the normal convolution representation and E the cutoff of P123.042.
The local normal anomaly of P123.108 has mixed derivative

    B_loc(f,g)=eventual Tr(E D(f)(1-E)D(g) E).               (1)

Exact stabilization follows from the endpoint matrices in P123.108,
just as in the coupled argument of P123.111. Its Hermitian specialization
is a nonnegative cutoff-escape energy. We show that its radical is not
an ideal of the local convolution algebra.

Choose a nontrivial unit character chi of conductor c>=1. Define the
actual locally constant compact tests

    e_chi(u)=chi(u) on U, zero off U,
    v_chi(q u)=chi(u) on qU, zero elsewhere.

Unit character orthogonality gives

    D(e_chi)=P_chi,    D(v_chi)=D_q P_chi,
    e_chi*e_chi=e_chi, e_chi*v_chi=v_chi,
    e_chi^*=e_chi,     v_chi*v_chi^*=e_chi.                 (2)

Here * between tests means convolution, and the superscript means its
involution. P_chi is the unit-isotypic projection; these formulas agree
with the character convention of P123.106.

## 2. Explicit failure of ideal stability

The normal cutoff commutes with every unit projection P_chi. Hence

    E P_chi(1-E)=0,
    B_loc(e_chi,g)=0 for every compact Bruhat test g.         (3)

Thus e_chi belongs to the full bilinear radical of this local anomaly
pairing, not merely to its zero-norm set. But on the retained chi block
of length n=L-c+1, D(v_chi) compresses to the truncated shift T_n.
Using D(v_chi)D(v_chi)^*=P_chi gives

    B_loc(v_chi,v_chi^*)=Tr(I_n-T_n T_n^*)=1                (4)

for every L>=c. Therefore v_chi is not in that radical, even though
it is the convolution product e_chi*v_chi of a radical element with
another test. This is a concrete failure of composition stability.
It remains true after multiplying the pairing by any nonzero Haar
normalization constant.

Consequently the positive local anomaly pairing cannot, with this
unchanged product and test domain, itself supply the numerical
equivalence required by A.6. This does not invalidate its determinant
composition law, endpoint interpretation or semilocal properties.

## 3. The trace-of-product pairing has a different radical and sign

Let W_loc be the probability-normalized local relative trace, namely
the expression in P123.107 before multiplication by log q. Define

    I_loc(f,g)=W_loc(f*g).                                  (5)

Associativity gives I_loc(f*g,h)=I_loc(f,g*h). Since the compact
Bruhat test algebra is closed under convolution, its radical against
all such tests is an ideal. More explicitly, if I_loc(f,h)=0 for all h,
then I_loc(f*g,h)=I_loc(f,g*h)=0 for every g,h. Its radical is closed
in any specified locally convex test topology in which these functionals
are continuous, as an intersection of closed kernels. These are formal
consequences for this particular pairing; they do not construct the
full mixed numerical quotient or its required nonzero sectors.

The two pairings differ on the same explicit tests. The conductor
formula of P123.105 yields

    W_loc(e_chi)=-c,
    I_loc(e_chi,e_chi)=-c,
    I_loc(v_chi,v_chi^*)=-c,                                (6)

whereas the anomaly values are zero and one respectively in (3)–(4).
With the prescribed multiplicative Haar normalization, (6) is multiplied
by log q. Thus the positive endpoint energy is not the local
trace-of-product form, even up to a single nonzero overall scale.

## 4. Consequence for the geometric comparison

This supplies a necessary distinction for the next A construction:
the determinant anomaly is a correction to composition, not automatically
the intersection form itself. Its local radical demonstrably fails the
ideal condition, while a trace-of-product pairing has that formal
condition but a different value and sign on actual source tests.

Neither local conclusion proves or refutes the global Weil sign, which
involves the full source and all local/archimedean contributions. The
required RR identity must explain how the anomaly, the trace-of-product
term and the ruling determinant fit together. Equating the positive
anomaly energy to the arithmetic intersection would omit necessary data.
That geometric identity and full row A remain open.
