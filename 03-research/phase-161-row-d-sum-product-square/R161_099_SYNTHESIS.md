# R161_099 — Synthesis of phase 161, first construction


## 0. Verdict

**Row D remains OPEN. No sign beyond the record is claimed.** The assigned route was nevertheless developed far
enough to separate a real new identity from two sterile versions of it.

Claim level: **PARTIAL_NEW + STRUCTURAL_NEGATIVE**.

## 1. What was constructed

For the finite Müntz operator `S_N`, the finite von Mangoldt operator `L_M`, the log-scale additive Fourier involution
`Fcal`, and the finite Weil operator `A_M`, define:

```
E_N   = S_NFcal-JS_N                         (Poisson defect),
H_M,N = L_MS_N-K_N                           (divisor-hyperbola tail).
```

The main exact identity is

```
S_N A_M Fcal
 = {X,E_N}-L_M^*E_N-JH_M,N-H_M,NFcal.        (PC)
```

This is the first recorded operator identity in the corpus in which:

- additive Poisson/Fourier;
- the multiplicative identity `Lambda*1=log`; and
- the finite Weil operator

occur in the same analytic step.

For ζ, `H_M,N` has no coefficient inside `k<=N` and has a nonnegative coefficient tail. Every standard falsifier has
an explicit interior defect `delta_a(k)`.

## 2. What failed

The canonical square is

`||{X,E_N}F-L_M^*E_NF-JH_M,NF-H_M,NFcal F||^2=||S_NA_MFcal F||^2`.

It is invariant under `A_M -> -A_M`; hence it sees `A_M^2` and cannot orient the sign. Nonnegative combinations of
these squares remain sign-blind.

Likewise, nonnegative weights cannot telescope the arithmetic tail: at every prime `p`, `h_N(p)=log p` for `N<p`
and zero after `N=p`. The sign `-log p` occurs only in the terminal discrete jump.

## 3. The necessary repair

Raw Dirichlet partial sums are not a Poisson approximation on `Re s=1/2`; their defect is generically of size
`N^(1/2)` and oscillatory. The canonical repair is

```
S_N^ren = S_N-C_N(D),
C_N(s)=N^(1-s)/(1-s).
```

The polar operator is exactly the positive-continuum dilation integral

`C_N(D)=integral_0^N x^(-1/2)tau_(log x)dx`.

Thus `S_N^ren` is integer lattice minus continuum. Its Poisson defect tends to zero on Schwartz data. On primitive
window tests, `C_N(D)` becomes an explicit compact Volterra boundary layer rather than disappearing.

## 4. Corpus collision and corrected remaining lemma

The first formulation L161.2 was too broad. The corpus audit in `R161_004` gives three exact stop-gates:

- scalarising the endpoint gives the common PNT primitive `D(u)` and returns to Paper 41 C4--C5;
- a positive divisor-fibre lift returns to the phase-104 divisor--Markov transport and phase-106 ANOVA no-go;
- unitriangular Mobius elimination returns to `P121_CMO_SOURCE_MATRIX_NO_GO`, where logarithmic differentiation
  removes the identity diagonal.

On a fixed window, `P_T S_N P_T` stabilises exactly to one of the two phase-121 causal zeta observations. Therefore
the corrected target L161.3 is:

> Apply `(PC-ren)` to a hypothetical primitive first-contact state and retain the oriented exterior additive-Fourier
> port before every scalar trace. Prove that its critical normal symbol vanishes.

`R161_005` isolates that port exactly:

```
P_T R_(M,N)^ren Fcal F
 = P_T S_N^ren r + P_T S_N^ren(1-P_T)A_MF.
```

The last term is the only carrier not already covered by the stop-gates.

`R161_006` computes it pointwise. In the `S_N` orientation it is

```
Delta_(N,T)^R ell_T(F)-e^(-t/2)a_-(ell_T(F)),
ell_T(F)=(1-P_T)A_MF,
```

and reflection gives the left discrepancy plus an `e^(t/2)` Tate scalar. Thus all contamination from the opposite
exterior tail lies in the two Tate directions. After their exact crossed cancellation, the unresolved object is the
pair of one-sided moving-endpoint Euler--Maclaurin discrepancies, not a scalar positive measure.

`R161_007` identifies their critical jet. If

```
H_(+,T)F=-(zeta'/zeta)K_F-Q_(+,T),
```

then the sum--product regularisation

```
G_(+,T)F=zeta H_(+,T)F=-zeta'K_F-zeta Q_(+,T)
```

is holomorphic at every nontrivial zero and, at a simple critical zero,

```
G_(+,T)F(i gamma)=-zeta'(rho)K_F(i gamma).
```

Thus the critical normal symbol is now computed. What remains is to identify one separated PC port with this product
in a critical-jet-preserving graph topology and derive its vanishing from first contact. Symmetric graph
conservation alone cannot do this because it adds the two symbols `(-c,+c)`.

`R161_008` proves the required analytic separation short of one two-scalar match. The phase-121 radical belongs to
`H^s` for every `s<1/2`; choosing `s>1/4` and using convexity for `zeta,zeta'` makes the product-regularised boundary
`L2`. After a causal polar correction by `zeta(s)Theta_T`, which vanishes at every nontrivial zero, the right port is
in `H2(C_+)` and the reflected port is in `H2(C_-)`. If the strong zero commutator is their sum with the crossed Tate
coefficients, opposite support forces both ports to vanish and the critical jet theorem closes first contact.

The only unchecked line is now the equality of the two polar coefficients introduced by this Hardy correction with
the coefficients already fixed by the phase-121 crossed Tate boundary system.

`R161_009` closes that scalar match. The residue of the right product port at `s=1` is its exterior Tate moment; the
primitive condition kills every `n>=e^(2T)` contribution and leaves exactly the finite `Lambda(n)/n` collar of phase
121. Reflection gives the `Lambda(n)` collar, Gamma supplies the continuous collars, and the invertible crossed Tate
matrix fixes both corrections. Hence no scalar ambiguity remains. The sole open line is the vector identity that
decomposes the strong zero commutator as the sum of the two canonically corrected, oppositely supported Hardy ports.

`R161_010` attempted to prove that line by working first in the absolute Euler half-plane and then passing to the
first-contact `H^s` graph. The typed scattering audit `R161_011` rejects the literal untransformed-port sum: the
phase-116 commutator identifies the reflected Mellin orientation through the additive cosine transform. For a
parity source the corrected equation places the right product port in a cosine-eigen Sonin gap space. Such spaces
are nonzero, so support separation alone does not exclude first contact.

The remaining theorem is now sharper: the arithmetic range of the product-port map, whose critical jet is
`-zeta'(rho)K_F`, must intersect the relevant Sonin eigenspace trivially on the first-contact radical. In the first
chamber above `0.8`, its arithmetic interior data involve only `n=2,3,4`. A boundary equation specific to that
finite product range, combined with the phase-121 infinitesimal gap-enlargement theorem, is the next target.

`R161_012` makes that target physical.  It identifies the sufficient condition as membership of the `H2` numerator
in the actual causal co-Poisson range, not formal meromorphic divisibility by zeta.  It also computes, for
`0.8<T<(log 5)/2`, the literal first-collar germ

```
g_+(t)=(log2)/sqrt2 F(t-log2)
      +(log3)/sqrt3 F(t-log3)
      +(log2)/2 F(t-log4).
```

The next calculation must obtain a second, independent collar equation from the differentiated co-Poisson law and
the unsupertraced Gamma/Tate term.  If that equation is merely the cosine transform of the first, the route has
returned to the known Sonin equivalence; if independent, it can eliminate the finite translates and start the
boundary-gap propagation.

`R161_013` performs the local test.  The bare identity `[Q,Z_+]=Z_+B_+` gives no second row: on the first exterior
collar both sides are literally the same `2,3,4` delay field.  The first-contact equation nevertheless supplies the
exact transmission law

```
Y_3(F)=D_Gamma F-r_epsilon        just inside T,
Y_3(F)=g_+^0                     just outside T.
```

After `D_Gamma=Q+C Q C`, the only genuinely new cross-place datum is the nonlocal term `C Q C F`.  The next proof
must combine that unsupertraced Gamma transmission with the exterior Sonin eigenrelation; differentiating the
scalar co-Poisson identity again is now a closed dead end.

`R161_014` extracts the positive quadratic content of that combination.  On a cosine-parity port supported in
`[T,infinity)`, the exact identity `D_Gamma=Q+C Q C` gives

```
<D_Gamma g,g>-2T||g||^2
 =2 integral_T^infinity (t-T)|g(t)|^2dt >=0,
```

with equality only for `g=0`.  The product port has the required `Q`-domain by differentiating its explicit
`H2` numerator and using the same `H^s`, `s>1/4`, estimate.  Conditional on completing the typed physical scattering
passage isolated in `R161_011`, closure is reduced to the single oriented upper/null balance saying that first
contact makes this explicit excess energy nonpositive.  Scalar commutation cannot supply that balance; it must be
derived from the finite `(PC)` mixed pairing with the crossed Gamma/Tate boundary retained.

## 5. Research value

Before phase 161 the open instruction was “use sum and product jointly in a quadratic object”. The exact joint
identity now exists, its generic square is known to be insufficient, and its two natural positive completions have
been matched to old no-go results. Product regularisation supplies a separated causal Hardy port and a
critical-jet detector, but not yet a first-contact contradiction. Phase 161 remains a **partial new construction**.
The load-bearing statement is now the Sonin range-intersection lemma `R161_011` (4.2), not the retracted direct-sum
identity of `R161_010`.

`R161_015`--`R161_016` sharpen the metric content and its orientation.  For the canonical pole gauge the product-port
excess is

```
E_T^PC(F)=-N_T'(0+).
```

A direct pullback of the positive Euler--Gamma Markov defect gives
`N_T(0)-N_T(delta)>=0`, hence only `N_T'(0+)<=0`; this is the causal inequality already contained in the displayed
formula and cannot close first contact.  The missing Poisson/Fourier scattering must reverse the physical typing so
that its positive defect is `N_T(delta)-N_T(0)` to first order.  The renormalised finite Poisson defect tends to zero
and therefore cannot itself be that order-zero scattering.  Also, the orthogonal prime innovations must be Tate-
centred and coherently synthesized before taking the exterior norm; their unsynthesised global energy diverges.

The first chamber does **not** make the global norm problem finite: `n=2,3,4` describe only the endpoint collar,
whereas the product port at arbitrarily large exterior time contains infinitely many prime powers, and its norm
slope integrates the whole tail.  The construction therefore branches cleanly.  The local branch may use a finite
`2,3,4` plus Gamma/Tate matrix only to force a zero collar and then invoke gap enlargement.  The global branch must
construct the complete Tate-centred cross-prime synthesis and the reverse pullback.  That global identity remains
**OPEN** and is the same operator-level obstruction as phase-116 `(220j)/(223j)`, now with its sign fixed explicitly.

`R161_017` removes the schematic ambiguity in the cosine scattering. For a parity source, differentiation of the
zeta functional equation gives the exact germ

```
G_+(z)+chi(s)G_-(z)
 =zeta(s)[d_Gamma(s)K_F(z)-Q_+(z)-epsilon Q_+(-z)].
```

After the canonical exterior polar corrections the bracket changes only by exterior-supported Hardy kernels. Its
inverse distribution therefore still equals `r_epsilon` on `I_T`. Exact physical cosine scattering would make the
left side zero, hence make the bracket zero in `Re s>1`, and consequently force `r_epsilon=0`. This is stronger than
the phase-121 completed conservation law, which permits nonzero forcing and only fixes its incoming current.
However, phase 121 already records that uniqueness of the resulting homogeneous zero mode remains open. Thus the
scattering step and the Sonin range-intersection step are now cleanly separated; neither may be inferred from the
other.

`R161_018` then performs the promised comparison with `(PC-ren)`. If the full currents are split as
`B_+u=q_++h_+` and `B_-u=q_-+h_-`, then

```
w_epsilon=A_infinity u+h_++h_-.
```

Product regularisation gives `zeta W_epsilon=P_epsilon`, while applying zeta to the displayed split gives
`zeta W_epsilon=Z A_infinity u+P_epsilon`. Their comparison is only
`Z A_infinity u=[Z,D_Gamma]u=0`. The polar corrections change `w` and the exterior ports by the same terms and do
not alter this conclusion. Hence a linear `(PC-ren)` graph limit cannot prove separated-port vanishing; doing so
would silently delete the incoming/prehistory component. The only surviving use of `(PC)` must retain a normalized
finite quadratic or oriented mixed defect. Together with the arrow audit, this leaves the reverse Tate-centred
Markov pullback as the exact terminal construction.

`R161_019` closes the range-rigidity half of that construction. If physical scattering makes the corrected defect
`W_epsilon^0` vanish, its non-Gamma terms are holomorphic at every `s=3,5,7,...`, while `d_Gamma=-chi'/chi` has a
simple pole there. Hence

```
K_F(5/2)=K_F(9/2)=K_F(13/2)=...=0.
```

With `x=e^(-2t)`, these are the moments of a weighted copy of `F` against `x^m`, `m>=1`, on the compact interval
`[e^(-2T),e^(2T)]`. Positive powers are dense there because the interval is separated from zero, so `F=0`. This
proves the product-range/Sonin intersection and gives `E_T^PC(F)=0<=0` once physical scattering is established.
The former provisional homogeneous-mode ambiguity disappears after retaining the explicit Gamma quotient. The sole
terminal gate is now the construction of physical scattering from the finite quadratic `(PC)` defect; the linear
limit cannot supply it by `R161_018`.

`R161_020` and `R161_021` reduce that terminal gate substantially. It is unnecessary to prove bilateral scattering,
or even the compressed vector equation, directly. For the canonical right-supported product port it suffices to
prove the one scalar identity

```
X_T(F)=||g||^2+epsilon<g,C_log g>
      =Re<G_+^0,zeta W_epsilon^0>=0.
```

Selfadjoint unitarity gives
`X_T=(1/2)||(I+epsilon C_log)g||^2`, so equality forces the full physical scattering relation. The most economical
remaining construction is consequently a finite, crossed-Tate-corrected conjugate test `H_(M,N,T)F` satisfying

```
lim a_T(F,H_(M,N,T)F)=X_T(F).
```

The left side vanishes on a first-contact radical. Producing this identity from `(PC-ren)` before causal
recombination is L161.5; it remains open and is strictly weaker than projected defect-norm convergence.

`R161_022` removes the apparent freedom in the conjugate test. On the common product graph take
`H_F=Pi_TP_TZ*g`. If `w=(W_epsilon^0)^vee`, then first contact gives `P_Tw=P_TAF=r`, so
`d=w-AF` is exterior-supported. With `y=Z*g`, radicality and the primitive/Tate/exterior decomposition give exactly

```
X_T(F)=Re[<r,(I-Pi_T)P_Ty>
          +<(I-P_T)AF,(I-P_T)y>
          +<d,y>].
```

Thus L161.5 is no longer a search for a test vector. It is the concrete statement that the already fixed crossed
Tate polar term and the two displayed exterior terms obey the Green reciprocity inherited from finite `(PC-ren)`.
The canonical finite gauge is `Pi_TP_T(S_N^ren)*g_(M,N)`; proving its graph limit and the exterior cancellation is
the remaining terminal calculation.

`R161_023` corrects the optimistic reading of that test. Since `r` lies in the Tate range,

```
<r,(I-Pi_T)P_T(S_N^ren)*g_N>=<S_N^ren r,g_N>.
```

Adding the exterior Weil term reconstructs `<S_N^ren AF,g_N>`, hence exactly the mixed `(PC-ren)` pairing. Adding
`d=w-AF` then reconstructs `X_T=Re<G_+^0,zeta W_epsilon^0>`. Radicality has produced no new equality. The crossed
Tate matrix cannot change this conclusion: it is `G_TC`, indefinite, whereas the orthogonal Tate projection uses
the positive Gram `G_T`. The extremal scalar criterion remains valid, but its vanishing must come from an
independent antisymmetric boundary concomitant prior to causal recombination (L161.6), not from a primitive test
chosen after the fact.

`R161_024` then weakens the terminal theorem beyond scattering. The range-rigidity proof only uses the residues of
`W_epsilon^0` at `s=3,5,7,...`; it does not require that the defect vanish. Since all non-Gamma terms are holomorphic
there, mere removability gives

```
K_F(5/2)=K_F(9/2)=K_F(13/2)=...=0,
```

and the already proved compact-interval moment density forces `F=0`. Equivalently, the reflected product port must
vanish only at the trivial-zero lattice. This moves the minimal remaining calculation into the safe half-plane:
expand the two oriented finite `(PC-ren)` germs near each positive odd Gamma pole and prove annihilation of the
Gamma residue coefficient. There is no compensating non-Gamma residue: the continuum/Tate corrections are
holomorphic there. Global causality, compressed scattering, and the extremal correlation are sufficient but no
longer necessary if this discrete removability law L161.7 is obtained.

`R161_025` computes the Laurent coefficient exactly:

```
Res_(s=2m+1)[zeta(s)W_epsilon^0(s)]
 =zeta(2m+1)K_F(2m+1/2).
```

This exposes a necessary correction to L161.7. Finite holomorphy does not imply removability of the limit without
uniform control of that Laurent coefficient, and every linear `(PC-ren)` graph limit is already tautological by
`R161_018`. The surviving object is the positive faithful pole energy

```
D_T^pole(F)=sum_(m>=1)2^(-m)(2m+1/2)e^(-2(2m+1/2)T)
             |K_F(2m+1/2)|^2.
```

It is finite by Cauchy--Schwarz and vanishes exactly when `F=0`. L161.8 is the precise remaining quadratic target:
construct this energy as a limit of the separated finite `(PC-ren)` mixed defect and prove its annihilation on a
first-contact state before causal recombination.

`R161_026` identifies this pole energy with an intrinsic Gamma boundary object. Put
`k_Gamma^+(v)=c_Gamma(v)-e^(-v/2)=sum_(m>=1)e^{-(2m+1/2)v}`. Then, for `delta>0`,

```
B_(T,delta)^Gamma(F)
 =double_integral F(t)conj(F(u))
    k_Gamma^+(2T+2delta+t+u)dtdu,

D_(T,delta)^Gamma(F)
 =-(1/2)partial_delta B_(T,delta)^Gamma(F)
 =sum_(m>=1)(2m+1/2)e^(-2(2m+1/2)(T+delta))
    |K_F(2m+1/2)|^2.
```

Thus the residue detector is a positive Hankel square generated by the Gamma pole lattice; reflection, and hence
the additive Poisson/Fourier side of `(PC)`, is essential. The direct displacement sign is automatic. The new
terminal formulation L161.9 is to obtain the reverse sign on a first-contact state from the finite mixed identity,
with `J` and the continuum counterterm retained. Equality then kills the faithful Hankel observation and forces
`F=0`.

`R161_027` gives the Hankel form a method-of-images interpretation. If
`M_(T,delta)F(x)=F(-x-2(T+delta))`, the image lies beyond the left endpoint with gap `2delta`, and

```
B_(T,delta)^Gamma(F)=<F,C_(k_Gamma^+)M_(T,delta)F>.
```

Thus `D^Gamma` is the attractive force between the source and its reflected exterior copy. The corresponding raw
prime-power force is an autocorrelation derivative and has no fixed sign, despite `Lambda(n)>=0`. Consequently an
ordinary Gamma-minus-prime Green conservation law remains indefinite. The exact new acceptance test L161.10 is
that finite `(PC-ren)`, polarized between the source and its image before causal recombination, converts the full
prime force through `Lambda*1=log` and Poisson into a same-sign nonnegative boundary square. A first-contact zero
force would then annihilate the faithful Gamma square and force `F=0`.

`R161_028` proves that this image geometry is already present in the polar renormalization. Writing `a=log N`,

```
C_a=e^(a/2)tau_a V,
partial_a C_a=e^(a/2)tau_a.
```

For `a=2(T+delta)` and a parity source, `partial_aC_aF` is, up to the explicit scalar, precisely the reflected
exterior image, and `C_aF` has exactly its support interval. The discrepancy `S_a-C_a` therefore has a continuous
image velocity between integer births and the literal jumps `n^(-1/2)tau_(log n)` at births. The refined terminal
target L161.11 is to differentiate the finite quadratic `(PC-ren)` pairing in `a`, add those jumps, and use the
Chebyshev hyperbola identity to obtain `2D^Gamma+D^Poisson=0` with both terms nonnegative. This is now a calculation
inside the original sum--product construction rather than an externally imposed image deformation.

`R161_029` performs the sign audit. Between integer births,

```
partial_a||Z_af||^2=-2e^(a/2)Re<Z_af,tau_af>,
```

while a birth `a=log n` changes the norm by

```
2n^(-1/2)Re<Z_(a-)f,tau_(log n)f>+n^(-1)||f||^2.
```

Both contain an indefinite cross term; the raw probe confirms nonmonotonicity. Compressing `Z_a*Z_a` with the
primitive projection only evaluates the already known radical equation on a moving test. Therefore L161.11 does
not bypass the arrow audit: its same-sign completion is exactly the reverse Tate-centred Markov pullback of
`R161_016`, with `R161_028` providing a canonical Gamma-Hankel coordinate for the missing positive component.

`R161_030` isolates the algebraic completion missing from that audit. On every completed product fibre `de=k`,
retain two source vectors `x_d^+,x_d^-` before Fourier reflection is recombined, and put
`m_d=(x_d^++x_d^-)/2`, `r_d=(x_d^+-x_d^-)/2`. Then `sum_(d|k)Lambda(d)=log k` gives

```
(log k)/2 sum_d Lambda(d)(||x_d^+||^2+||x_d^-||^2)
 -||sum_d Lambda(d)m_d||^2
=(log k)sum_d Lambda(d)||r_d||^2
 +1/2 sum_(d,e)Lambda(d)Lambda(e)||m_d-m_e||^2.
```

This is total variance with divisor and orientation conditioned in the correct order. For `k=p` the divisor seam
vanishes but the orientation square `(log p)^2||x_p^+-x_p^-||^2/4` survives, removing the old prime-root diagonal
obstruction. The remaining terminal calculation is sharply defined: realize these pathwise oriented vectors from
finite `(PC-ren)` and prove that its crossed-Tate first-contact pairing is exactly the saturated left side above.
The identity then kills Poisson leakage without a further estimate. This source match is not yet proved and cannot
be replaced by linear radicality.

`R161_031` constructs the abstract path vectors directly from the two unrecombined product terms. For `de=k`,

```
x_(k,d)^-=k^(-1/2)Jtau_(log k)f,
x_(k,d)^+=k^(-1/2)tau_(log k)Fcal f.
```

They do not depend on `d`. Thus the transverse divisor variance vanishes identically, while the orientation part
of `R161_030` becomes

```
D_(M,N)^orient(f)
 =1/4 sum_(2<=k<=N)(log k)^2/k
      ||tau_(log k)Fcal f-Jtau_(log k)f||^2.
```

This is an unsupertraced direct-sum square; replacing it by the norm of the sum introduces cross-`k`
interference and loses its equality kernel. The path labels are complete, but `R161_033` corrects the claim that
their direct-sum norm has already been realized by the coherent source identity. Under polar
renormalization the continuum derivative is the Gamma image square already identified in `R161_026`--`R161_028`.
The terminal calculation has narrowed to the crossed-Tate endpoint concomitant: prove that it vanishes at first
contact, or that it is absorbed with the same sign into the two positive squares. Linear radicality alone does not
establish that statement.

`R161_032` proves the finite-dimensional sign conversion. Writing `C` for exchange of the Tate characters, the
positive Gram is `G_T`, while the collar matrix is `G_TC`. A parity first-contact forcing has coefficient vector
`v` with `Cv=epsilon v`; hence, if `j=G_TCv` is the exact collar current,

```
epsilon<v,j>=epsilon<v,G_TCv>=<v,G_Tv>=||r||^2.
```

The crossed block is therefore indefinite only before parity reduction. On the relevant parity line it becomes,
with precisely the sign occurring in `X_T=||g||^2+epsilon<g,C_log g>`, a positive endpoint square. The endpoint
need not vanish separately: a terminal finite Green identity could retain it and yield a sum of the scattering,
Tate, direct-sum Poisson and Gamma-image energies. The outstanding step is the exact source bookkeeping producing
that equality, including the sign/order of the concomitant and the cross-`k` Gram.

`R161_033` corrects an overstatement in the preceding two notes. The path vectors are canonically labelled, but
the physical `(PC-ren)` identity contains their coherent sum over `k`. Its squared norm contains the cross Gram

```
sum_(k!=l)(log k)(log l)/sqrt(kl)
 Re<Delta_kF,Delta_lF>,
```

whereas `D^orient` retains only the diagonal. Formal source labels do not provide an isometry from the physical
space into that direct sum. Thus the discrete second-moment realization and the claimed resolution of the complete
sign problem are withdrawn. The valid parity identity is conditional: a boundary term occurring as
`+epsilon<v,j>` equals `||r||^2`, but its occurrence and ordering must be derived. The legitimate terminal choices
are now an explicit Parseval/Naimark dilation supplied by Poisson, or a coherent Green completion in which the
polar/Gamma and parity-Tate boundary exactly compensate the cross-`k` interference. This audit prevents the
variance gate from becoming an assumed source square.

`R161_034` diagonalizes that missing Gram. If
`q_k(tau)=k^(-s)u_infty(tau)-k^(-(1-s))`, then the coherent source energy has symbol
`|sum_k(log k)q_k|^2`, while the labelled square has symbol `sum_k(log k)^2|q_k|^2`. For `k!=l`,

```
Re(q_k conjugate(q_l))
=2(kl)^(-1/2)[cos(tau log(k/l))
 -Re{u_infty(tau)exp(-i tau log(kl))}].
```

These are exactly the ratio and product channels of phase 106. Hence a full-line cancellation would merely return
to that exhausted triangle-current route. What remains genuinely phase-161 is boundary compression: retain the
positive coherent leakage

```
||(I-P_T)sum_(k<=N)(log k)d_kP_TF||^2
```

and its continuum polar analogue before expanding. This object keeps all cross-`k` interference with the correct
sign and belongs to the original `(PC-ren)` Hilbert space. The terminal task is its graph-limit identification with
the physical scattering leakage and proof of compression saturation at first contact.

`R161_035` gives the cleaner coherent formulation and removes the need for any labelled dilation. Before `(PC)` is
rearranged, its derivation supplies

```
U_N=K_N^ren Fcal,              V_N=JK_N^ren,
U_N+V_N=S_N^ren M Fcal-{X,E_N^ren}.
```

The two-vector parallelogram therefore gives on the physical Hilbert space

```
1/2(||U_Nf||^2+||V_Nf||^2)-1/4||(U_N+V_N)f||^2
 =1/4||(U_N-V_N)f||^2>=0.
```

All product/ratio interference remains inside the coherent norms. `Lambda*1=log` is used first to synthesize
`K_N=L_MS_N-H_M,N`; only then are the two Fourier orientations compared. The remaining statement is the
first-contact saturation of this exact two-state second moment, with the polar layer and the endpoint
`epsilon<v,G_TCv>=||r||^2` derived in their correct order from the finite Green pairing.

`R161_036` identifies the observed vector. With
`e_N(s)=Z_N(s)u_infty(s)-Z_N(1-s)`, the exact finite symbols satisfy

```
U_N+V_N=-e_N'(s)+Z_N(s)u_infty'(s),
U_N-V_N=-Z_N'(s)u_infty(s)+Z_N'(1-s).
```

After differentiated graph convergence and the functional equation, the second line becomes

```
-2zeta'(s)u_infty(s)-zeta(s)u_infty'(s).
```

At a simple critical zero this is `-2zeta'(rho)u_infty(rho)`, so vanishing of the coherent gate forces the existing
critical conormal samples `K_F(i gamma)` to vanish. Thus the gate can close through the phase-121 critical-jet
density theorem without an additional global scattering assertion. The two still-open statements are precisely
first-contact saturation of the coherent parallelogram and differentiated boundary-graph convergence; ordinary
pointwise convergence of `E_N^ren` is insufficient.

`R161_037` removes differentiated strong graph convergence as a separate hypothesis. If saturation gives
`||B_NF||_2->0` for `B_N=U_N^ren-V_N^ren`, Plancherel yields a subsequence
`b_(N_j)(tau)Fhat(-tau)->0` almost everywhere. Differentiated Euler--Maclaurin converges at every fixed frequency,
so the same subsequence converges pointwise to

```
b_infty(tau)Fhat(-tau)
=(-2zeta'(s)u_infty(s)-zeta(s)u_infty'(s))Fhat(-tau).
```

The multiplier `b_infty` is not identically zero: otherwise `(zeta^2u_infty)'=0`, contradicting the pole/zero
structure of zeta. Its critical-line zero set therefore has measure zero, and `Fhat=0` almost everywhere. Hence
coherent saturation alone forces `F=0`; the finite polar/crossed-Tate derivation of that saturation is the sole
remaining gate.

`R161_038` proves that this last gate is not automatic algebra. On `C^2`, take
`X=diag(1,-1)`, `J=Fcal=((0,1),(1,0))`, `S=((0,1),(0,0))`, and `L=0`. Then `M=0`, `A=0`, and the full finite
identity

```
SAFcal={X,E}-L*E-JH-HFcal=0
```

holds exactly. Nevertheless `U-V=-2X`, so `D^coh(f)=||f||^2` for every `f`; the failure persists on both parity
lines. Hence `(PC)`, radicality, polarization and parity cannot imply saturation without additional physical
input. The sole surviving theorem must use the actual support compression and polar/Tate collar law to exclude
this formal countermodel.

`R161_039` records the terminal equivalence. The coherent saturation
`||B_NF||_2->0` is sufficient for `F=0` by `R161_037`, but it is independent of the available formal source algebra
by `R161_038`. The same missing physical law has appeared successively as scattering leakage, reverse Gamma-Hankel
displacement, oriented-fibre saturation and coherent saturation. A valid continuation must add an explicit
compressed Green identity whose radical pairing is zero and whose expansion yields the coherent defect together
with the polar image and the literal parity-oriented Tate term. No such identity has been derived in phases
1--161; row D remains open.

After the retry, `R161_040` identifies a physical input which invalidates the formal countermodel as
a model of the terminal boundary. For `Z_N=S_N^ren`, reflection gives `JZ_NJ=Z_N*`, while Poisson gives

```
Z_NFcal=Z_N*J+E_N^ren.
```

Thus for a parity source and the physical support projection,

```
(I-P)Z_NFcal f-epsilon(I-P)Z_N*f=(I-P)E_N^renf.
```

This is an exact finite identification of the two exterior causal histories, modulo the explicit Poisson defect;
it is precisely the annular transport missing from the phase-121 local Hankel observable. Its norm is a positive
square before any scalar trace. Since `P_T` commutes with `X=t`, differentiating this history identity is now the
concrete candidate for producing `K_N^renFcal-JK_N^ren`, the polar-image Gamma square, and the parity-oriented Tate
endpoint in one line. That differentiated energy identity remains to be computed.

`R161_041` corrects the orientation of that last sentence. If
`E_N=Z_NFcal-JZ_N` and `C_N=Z_NFcal+JZ_N`, exact anticommutator algebra gives

```
K_NFcal+JK_N=Z_NM Fcal-{X,E_N},
K_NFcal-JK_N=Z_NM Fcal-{X,C_N}.
```

Thus differentiating the positive norm of the small Poisson defect observes the mean, not the critical jet. The
desired simultaneous construction must mix the compressed difference `E_N` with the covariant derivative of the
sum `C_N` before taking the real part, with the polar and Tate terms retained. The former squared-history target is
withdrawn rather than used with the wrong sign.

`R161_042` evaluates the infinite-dimensional part of that mixed pairing. For
`a=Z_NFcal f`, `d=JZ_Nf`, the elementary identity

```
Re<a-d,X(a+d)>=<a,Xa>-<d,Xd>
```

cancels both cross orientations. On the physical right/left exteriors, subtracting `T` times the two masses leaves

```
||(X-T)^(1/2)P_+a||^2
+||(-X-T)^(1/2)P_-d||^2>=0,
```

the two-sided Sonin--Gamma excess. In the full critical-jet pairing the only additional anticommutator term is
`Re<E_Nf,C_NXf>`. Decomposing `PXf` into its primitive projection and its two Tate coordinates shows where the
crossed endpoint concomitant can enter. The primitive component is an admissible test, but the mixed expression
must still be shown to equal its Weil pairing before radicality may annihilate it; the Tate component must be
computed against the collar vector. The exact typing and the signs of the residual wrong-side boundary pieces
remain open.

`R161_043` corrects the Tate expectation in this particular ordering. Because `JX=-XJ`, if `f` has parity
`epsilon`, then `Tau_TPXf` has parity `-epsilon`. The first-contact forcing `r` and its collar vector `j=G_TCv`
have parity `epsilon`; hence both the physical and coefficient pairings with the `Xf` Tate correction vanish.
Therefore the positive same-parity identity `epsilon<v,G_TCv>=||r||^2` cannot be inserted here. If the finite
`(PC-ren)` expansion reduces the source-derivative endpoint literally to this Tate pairing, it cancels exactly and
the remaining gate contains only the primitive test and the exterior wrong-side pieces.

`R161_044` audits the primitive piece against the phase-121 horizontal-modulation theorem. Since
`Pi_TP_TXf` is the derivative at zero of `Pi_T(e^(sigma t)f)`, its radical pairing is true but tautological. The
mixed Green term can be identified with that pairing only after moving the causal synthesis across the physical
projection, and the resulting Hankel commutator is exactly the exterior reciprocity left open in `R161_023`.
Therefore the interior analysis is complete: the Tate component is zero, the primitive component adds no law, and
all possible new information lies in the two exterior orderings. It is enough for their antisymmetric difference
to imply the scalar extremal relation `Re<g,P_+C_log g+epsilon g>=0`; `R161_021` then gives exact scattering.

`R161_045` checks the remaining Hardy/Toeplitz possibility against phase 122. Brown--Halmos supplies an exact
positive rank-one self-commutator for each degree-one Euler factor, and the local analytic determinant cocycle has
the forced normalization `1-p^(-1)`. But the physical equations place the two adjoint factors on different causal
histories. Poisson identifies those histories before differentiation, while the orientation audit shows that its
derivative produces the mean rather than the critical difference. Phase 122 proves that globalizing the local
curvatures would require a new metrized Euler--Gamma determinant anomaly including both Tate boundaries. Such a
trivialization is not in the corpus and is equivalent to the remaining exterior reciprocity, so the local Hankel
square cannot be promoted to a closure claim.
