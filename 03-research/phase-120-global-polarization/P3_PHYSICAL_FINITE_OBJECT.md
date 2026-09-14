# The physical finite P3 object with the row-(c) weights

Status: exact finite construction and calibration specification. Positivity of
its primitive defect beyond the certified range remains open.

## 1. Central Hodge amplitude

For `q=p^j`, put

    ell_q=j log p,
    w_q=log(p)/sqrt(q).

On the Connes–Consani Tate curve

    E_p=C_p x S^1,

the integral harmonic basis has Hodge norm

    c_p=2pi/log p.

Therefore the unique positive boundary amplitude whose *quadratic* Hodge
mass is the row-(c) coefficient is

    beta_q=sqrt(w_q/c_p)
          =log(p)/sqrt(2pi) p^(-j/4),

and

    c_p beta_q^2=w_q.

This distinguishes a half-density coefficient from a Hilbert amplitude. The
phase-106 choice `p^(-j/2)` used the former as the latter and consequently
squared it twice.

## 2. Dagger return edge

Let `V_ell F(t)=F(t+ell)` on the zero-extended logarithmic profile. Before
compression, retain the two oriented sheets of a return as

    E_q F=(V_(ell_q)F,F).

The normalized Hadamard matrix

    H=(1/sqrt(2)) [[1,-1],[1,1]]

is unitary and sends the oriented edge to its antisymmetric and symmetric
channels. Define

    B_q^- F=sqrt(w_q/2)(V_(ell_q)-I)F,
    B_q^+ F=sqrt(w_q/2)(V_(ell_q)+I)F.

Then, after zero-extension compression,

    (B_q^-)^*B_q^-=w_q(I-Re S_(ell_q)),
    (B_q^+)^*B_q^+=w_q(I+Re S_(ell_q)).

The construction is entirely before `B_nuc`: `w_q` comes from the Witt
contact determinant and central metric, while `H` comes from the two
orientations and the dagger.

## 3. Archimedean and Tate pages

The positive Gamma reservoir is the map `W_Gamma` of paper 42,
Lemma `positiveGammaReservoir`, and

    W_Gamma^*W_Gamma=G_Gamma.

The constant polar load is the positive line of squared norm

    m_0=log(pi)-psi(1/4)
       =log(pi)+gamma+pi/2+3log 2.

This constant is fixed by the centered Gamma determinant and the two polar
directions; it is not the phase-106 finite-part constant `kappa_infty`.

For a finite active set `S`, define

    X_S F=(W_Gamma F,(B_q^-F)_(q in S)),
    Y_S F=(sqrt(m_0)F,(B_q^+F)_(q in S)).

Their Grams are

    R_S=X_S^*X_S
       =G_Gamma+sum_q w_q(I-Re S_(ell_q)),

    L_S=Y_S^*Y_S
       =m_0 I+sum_q w_q(I+Re S_(ell_q)).

Thus

    A_S=R_S-L_S

is exactly the localized operator representing `-B_nuc`. This comparison
uses row (c) only after every positive source map has been constructed.

## 4. Primitive attachment and exact remaining theorem

Before forming the primitive attachment, the iterate channels admit a
strictly stronger place-coherent packaging. For each prime define

    C_p=p^(-1/2)V_(log p),
    O_p=sqrt(1-p^(-1))(I-C_p)^(-1).

Then

    O_p^*O_p-I
      =sum_(j>=1)p^(-j/2)(V_(j log p)+V_(-j log p)).

Hence the whole `p`-power tower, with the correct physical weights, is the
Poisson Gram of one strict contraction. The preferred finite maps can be
taken as

    X_T^pl F=(W_Gamma F,(sqrt(log p)F)_(p<exp(2T))),
    Y_T^pl F=(sqrt(m_0)F,(sqrt(log p)O_pE_TF)_(p<exp(2T))).

Their Gram difference is again exactly `A_T`. Unlike the iterate form, this
version is invariant by places and has a canonical Sz.-Nagy unitary dilation
before comparison with row (c).

Let

    P_T=ker M_- intersect ker M_+

be the two-Tate primitive space. The geometric attachment problem is now
typed exactly:

    find Theta_S : closure(X_S P_T) -> closure(Y_S P_T)

such that

    Y_S P_T=Theta_S X_S P_T

and derive `||Theta_S||<=1` from a unitary/partial-isometry construction on
the Tate/phase geometry.

If this is done, Douglas factorization gives

    A_S|P_T
      =(X_SP_T)^*(I-Theta_S^*Theta_S)(X_SP_T)>=0.

Defining `Theta_S=Y_SP_T(X_SP_T)^dagger` is allowed for calibration, but
asserting its norm is at most one is exactly the target sign. The new theorem
must realize it as a compression of an independently constructed unitary.

## 5. Gates

- At `T=log 2`, `S={2,3}`. Paper 42 already certifies the contraction on the
  full primitive Hilbert space. Phase 120 must reproduce the same `X_S,Y_S`
  from the Tate/phase construction and then compare any geometric
  `Theta_S` with the analytic one.
- At `T=(1/2)log 5`, `S={2,3,4}`. The iterate `4` tests Frobenius coherence
  inside the `p=2` place. A geometric unitary compression here would prove
  the first currently open endpoint. The full-residual calculation in
  `P3_LOG5_FULL_RESIDUAL_AUDIT.md` shows that the old scalar-gap proof misses
  ten boundary-dominated coupling directions at `V_200`; consequently the
  geometric attachment must retain the direction-dependent Green response,
  not merely a uniform complement coercivity constant.

## 6. Global warning

Because

    sum_(p^j<=X) w_(p^j)

grows at leading square-root scale, the raw boundary row is not uniformly
bounded in an ordinary Hilbert direct limit. Moreover phase 106.205 proves
that the absolutely continuous Cauchy completion cannot receive the discrete
CCM resonant classes faithfully. The cofinal target must therefore be a
renormalized nuclear, reproducing-kernel or derived cyclic completion which
retains evaluation jets before Hilbert reduction.
