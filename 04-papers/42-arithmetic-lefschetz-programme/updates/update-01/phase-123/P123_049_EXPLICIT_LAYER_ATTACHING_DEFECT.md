# P123.049 — Explicit multiplication defect attaching the double-zero layer

Status: PROVED for the continuous attaching defect,
its associativity identity and its two-prime shell formula. This supplies
chain-level input for descent, not an established excision theorem for
the desired shadow.

## 1. Attaching data from the actual source extension

Write the strict extension of P123.045 as

    0 -> I -> A --pi--> B -> 0,
    I=A(U), A=A(X^+), B=A(F).

Let s:B -> A be its explicit coefficientwise linear section. Define

    omega(b,c)=s(b)s(c)-s(bc).                    (1.1)

Since pi is multiplicative and pi s=id, omega takes values in I. If
p_k(s b)<=C p_k(b), the multiplication estimates give

    p_k(omega(b,c)) <= (C²+C)p_k(b)p_k(c).        (1.2)

The source multiplication can therefore be written exactly on I plus B:

    (i,b)(j,c)=(ij+i s(c)+s(b)j+omega(b,c),bc).

Associativity in A gives the identity

    s(a)omega(b,c)-omega(ab,c)+omega(a,bc)
                         -omega(a,b)s(c)=0.      (1.3)

This follows by expanding the four terms and canceling; it is valid
without assuming that s is multiplicative. Calling omega an ordinary
Hochschild cocycle for a B-bimodule would require care: multiplication
by s does not necessarily define a B-action on I. Equation (1.3), with
its actual A multipliers, is the precise assertion used here.

## 2. Two-prime formula in the repaired rapid algebra

Take S_f={p,q}, t=log x_infinity, and

    chi(x_p,x_q)=1_(Z_p)(x_p)1_(Z_q)(x_q).

For coefficients g,h in C_0(R), a label gamma=p^m q^n and any label eta,
the section is s(g U_gamma)=chi g U_gamma. Crossed multiplication gives

    omega(g U_gamma,h U_eta)
      =(chi alpha_gamma(chi)-chi)
           g(t)h(t-log gamma) U_(gamma eta).     (2.1)

At the double-zero set, both chi and alpha_gamma(chi) equal one, so this
coefficient vanishes there, as required. Formula (2.1) displays the
attaching term before any trace is taken.

Because the other prime factors are local units,

    chi alpha_gamma(chi)
       =1_(p^max(m,0) Z_p) 1_(q^max(n,0) Z_q).   (2.2)

Put A_m=1_(p^max(m,0) Z_p), B_n=1_(q^max(n,0) Z_q),
P=1_(Z_p), Q=1_(Z_q). Then

    A_m B_n-PQ=(A_m-P)Q+A_m(B_n-Q).              (2.3)

The first term is supported where x_p!=0, so belongs to C_0(U_q)
after multiplication by g(t)h(t-log gamma). The second is supported
where x_q!=0, so belongs to C_0(U_p). This is an explicit decomposition
of the attaching defect into the two single-zero charts.

For gamma=p, it reduces to

    omega(g U_p,h U_eta)
       =-1_(Z_p^*) 1_(Z_q)
                g(t)h(t-log p) U_(p eta).        (2.4)

For gamma=p^-1 the defect is zero with this section. This asymmetry
reflects the chosen integral lattice section; it is not an assertion
of asymmetry of the final Weil distribution. Taking h(t)=g(t+log p)
with a nonzero real compactly supported g makes (2.4) nonzero and
exhibits an actual attaching correction.

## 3. Changing the chart decomposition gives exactly a generic overlap

The alternative order is

    A_m B_n-PQ=(A_m-P)B_n+P(B_n-Q).              (3.1)

The U_q components of (2.3) and (3.1) differ by

    -(A_m-P)(B_n-Q),

and the U_p components differ by its negative. This product is supported
where both coordinates are nonzero, namely O. Thus the difference of
the two chart decompositions is precisely in the image of the overlap
map d of P123.044–045, with the sign determined by the component order.
The equality is pointwise and remains valid for the completed rapid
coefficients by continuity.

Hence the generic-overlap relation is already needed when multiplying
lifted double-zero elements. It is not merely an optional correction
to a later sum of scalar traces.

## 4. An explicit relative Hochschild boundary in degree one

For a finite Hochschild 1-cycle z=sum_i b_i tensor c_i in B, its cycle
condition is sum_i [b_i,c_i]=0. Lift it by s in both tensor factors.
Its Hochschild boundary in A is

    w=sum_i [s(b_i),s(c_i)]
      =sum_i (omega(b_i,c_i)-omega(c_i,b_i)) in I. (4.1)

Thus (2.1) computes this relative boundary by actual lattice shells.
If the lifts of b_i,c_i are changed by u_i,v_i in I, the change in w
is a sum of [u_i,s(c_i)], [s(b_i),v_i] and [u_i,v_i]. Its class modulo
the span of mixed commutators [A,I] is therefore independent of those
lift choices.

Equation (4.1) is a calculation for lifted chains and the relative
complex. It is not a claim that relative Hochschild homology has already
been identified with the homology of I in all degrees or completions.
Such an identification is part of the remaining excision requirement.

If a continuous trace tau_I on the relevant ideal domain satisfies
tau_I([A,I])=0, its value on (4.1) is correspondingly lift-independent.
The local external-test characters W_p have not yet been constructed as
such a tau_I on this source domain; substituting them here without that
map would skip the remaining comparison.

## 5. What the next shadow construction must preserve

There is now an explicit nonzero multiplication correction from the
double-zero quotient into the single-zero ideal, with a concrete overlap
identity and a relative chain boundary. The intended shadow must evaluate
these source terms compatibly with the normal cutoff realization and
the generic-overlap relation. Setting the quotient contribution to zero
without handling (2.1)–(4.1) is not justified by the filtration alone.

The same definition (1.1) applies to every explicit section in P123.048,
with its seminorm bound and associativity identity. This note computes
the first nontrivial layer completely at the coefficient/label level;
it does not assert the full mixed RR, integral contact transport or D sign.
