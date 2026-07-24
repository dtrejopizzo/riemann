# Phase 78 - Build-neutral LP and the IDENT discriminant

**Opened:** 2026-07-18.  Continues `phase-77-weyl-limit-point/`
(see `PHASE_77_CLOSURE.md` and `E77_7AZ_ATTRIBUTION_GATE.md`).

## Why this phase exists

Phase 77 decided the attribution question and, in doing so, discovered that the
LP front had drifted into a **detector spiral**: ~80 documents (E77.5d-5ah,
E77.7aa-ay) measuring a build-discriminating shell scalar that the attribution
gate (E77.7az) shows is a *detector*, not a forcing mechanism.

The governing conclusion this phase inherits:

```text
Attribution = Outcome A (E77.1b): operational LP holds for BOTH the zeta and
the planted builds. Therefore the object required for LP -- BTG-DIV-L, equal
sectionwise to fixed-mu canonical-energy divergence (E77.7f) -- is
FALSIFIER-NEUTRAL. The arithmetic discriminant lives ENTIRELY in IDENT.
```

**Binding rule for this phase (E77.7az / E72.16 gate).**
Any proposed LP step that separates the zeta build from the planted build by
order one is, by that fact, carrying surplus zero-location information beyond
what LP requires, and is inadmissible as a forcing mechanism. It may be recorded
as a detector but never pursued as a proof target. Only build-neutral LP
arguments, and finite-CCM symmetries that force cancellation without using zero
locations (E72.16 option 2), are admissible.

## The exact conditional chain (unchanged, proved down to the open items)

```text
LP + IDENT + RDP-SHELL + (PROLATE + WEIL-TAIL)
=> SAFE-LIMIT-POINT => SAFE-PROLATE-BRIDGE => SR-SAFE
=> Omega7 (Li-Keiper lambda_n >= 0) => RH.
```

## Open objects handed over (Fable-5 pending list, updated by Phase 77)

### Front A1 - LP, BTG side  [RE-ROUTED by E77.7az]
```text
Live object: BTG-DIV-L, proved BUILD-NEUTRALLY.
  For lower-semibounded H_L = D_L + B_L with compact resolvent (E77.7d):
  fixed-mu canonical energy S_N(mu_L) -> infinity and bordered Weyl disks
  contract. No build-discriminating shell scalar may enter the proof.
  The SIGNED-ACTIVE-BRANCH-DEFECT / RELATIVE-MISMATCH-LAW route is ARCHIVED.
  CAUTION: audit E77.7ak's SHELL-RESIDUAL-CANCELLATION under the same gate --
  only a build-neutral form is admissible.
```

### Front A2 - LP, interface side  [CORRECTED by E78.1/E78.2: NOT all build-neutral]
```text
Live object: SAFE-DISK-IDENT / BORDERED-WEYL-COMPLETENESS.
  (a) separation of safe Cauchy rows            -- PROVED (E77.7aj), build-neutral;
  (b) singular-section Schur regularization      -- LOCALIZED (E77.7x-7ai);
  (c) pencil compatibility, PROJECTIVE-MU-TRANSFER at true mu_L
      -- DETECTOR (E78.2): defect plateaus at ~0.84 for the plant, driven by the
         M-6 prefactor (mu_L - 0); NOT build-neutral;
  (d) existence of normalized l2 class            -- OPEN;
  (e) simplicity + nonvanishing at mu_L
      -- DETECTOR (E78.1): plant ground state isolated+simple (gap ~0.14 robust),
         zeta ground gap collapses geometrically to 0; build-discriminating;
         Perron-Frobenius route DEAD (B_L not gauge-single-signed for either
         build). NOT build-neutral.
  (f) assembly into the disk-intersection theorem -- OPEN, must be re-derived
         from the mu-FREE remnant (a) + NEUTRAL-GROUND-CAUCHY (E78.1 s.7), NOT
         from any subclause evaluated at mu_L.

Phase-78 scalar audits:
  anchor scalar r(z0)v0                           -- NEUTRAL but not forcing
                                                     (E78.4b);
  source scalar v0^* g_right                      -- DETECTOR, build-discriminating
                                                     (E78.4c);
  corrected live remnant                          -- NORMALIZED-CLASS-ASSEMBLY
                                                     inside SAFE-DISK-IDENT
                                                     (E78.4d).

KEY CORRECTION (E78.1/E78.2): subclauses (c) and (e) both reduce to the
mu_L-location/gap discriminant (mu_L ~ 0 for zeta, ~ -1.74 for the plant). Any
interface quantity pinned to mu_L inherits this discriminant and is a DETECTOR by
the E77.7az / E72.16 gate. The "front A2 build-neutral by nature" claim is
therefore WRONG for the mu_L-pinned subclauses; only the mu-free part is neutral.
```

### Front B - IDENT  [home of the discriminant]
```text
Cofinal diagonal lemma  -- PROVED (E77.6).
  FIXED-L-WEYL (with intrinsic RFL-2 identification) -- OPEN;
  SAFE-GAMMA-IDENT                                    -- OPEN;
  OUTER-LIMIT                                          -- OPEN;
  then E77.6 diagonal => IDENT.
The plant must pass the finite algebra and fail SAFE-GAMMA-IDENT / OUTER-LIMIT
(verified pattern: E77.6 mismatch 10.98-50.47 at the arithmetic target).

Phase-78 correction:
  absolute Euler tail                                 -- ALREADY theorem-grade
                                                         (P76.039);
  hard Euler finite proxy                             -- DEAD (P76.040);
  corrected live arithmetic object                    -- CELL-SMOOTHED-EULER-COMPARISON
                                                         for the exact fixed-L
                                                         symbol G_L versus the
                                                         safe truncation H_L
                                                         (E78.5).
  smaller fixed-L finite object                       -- COUPLED-GENERATOR-LIMIT
                                                         for the exact package
                                                         W_{L,N}=a_b(U+U_b)+b_b(V+V_b),
                                                         W'_{L,N}=a_bU'+b_bV'
                                                         (E78.6).
  invariant quotient form                             -- W-QUOTIENT-DELTA
                                                         i.e. consecutive
                                                         differences of
                                                         W'_{L,N}/(1+W_{L,N}),
                                                         exactly equal to the
                                                         Phase-77 LOGT-CELL
                                                         invariant (E78.7).
  denominator side condition                          -- HEALTHY on the tested
                                                         safe ladder in both
                                                         builds; not the active
                                                         obstruction (E78.8).
  finer anatomy of the quotient                       -- strong zeta-side
                                                         cancellation between a
                                                         linear term and a mixed
                                                         term; planted build
                                                         lacks that anatomy
                                                         (E78.9).
  numerator repackaging                               -- exact and useful, but
                                                         not itself a smaller
                                                         smallness target:
                                                         zeta has huge numerator
                                                         defect divided by an
                                                         even larger denominator
                                                         (E78.10).
  denominator geometry                                -- exact factorization
                                                         1+W=(z-d_b)t0(1-theta);
                                                         in zeta the huge
                                                         denominator is driven
                                                         mainly by huge transfer
                                                         scale |T|, not by large
                                                         |1-theta| (E78.11).
  dynamic driver of that geometry                     -- on the audited step,
                                                         zeta grows through |T|
                                                         while plant shrinks in
                                                         |T| and compensates via
                                                         |1-theta| growth
                                                         (E78.12).
  finer reduction of the driver                       -- t0 is the main growth
                                                         driver; 1-theta is a
                                                         correction/modulator,
                                                         not the principal scale
                                                         (E78.13).
  important no-go                                     -- t0 explains transfer
                                                         scale but not the signed
                                                         IDENT defect; the active
                                                         signed profile still
                                                         lives in theta-logderiv
                                                         coupling (E78.14).
  signed active ingredient                            -- after separating t0,
                                                         the admissible IDENT
                                                         front is the exact
                                                         theta-logderivative
                                                         object u=-theta'/(1-theta),
                                                         now re-imported on the
                                                         IDENT side only
                                                         (E78.15).
  current exact endpoint                              -- the only remaining
                                                         theorem-grade residual
                                                         in this tranche is the
                                                         signed coupling defect
                                                         Q_N = Q_ext - Q_t0 -
                                                         Q_theta (E78.16).
  sharper residual target                             -- control the relative
                                                         coupling defect
                                                         |Q_N|/(|Q_ext|+|Q_t0|+|Q_theta|)
                                                         rather than an absolute
                                                         Q_N bound from scratch
                                                         (E78.17).
  exact factorization of that target                  -- RELCOUP factors as
                                                         LOGT-CANCEL times
                                                         SCHUR-COMPRESSION;
                                                         on zeta rows the
                                                         compression factor is
                                                         stable (0.82-0.90), so
                                                         the live content moves
                                                         to the two-term signed
                                                         mismatch `Q_ext -
                                                         Q_logT` on a cofinal
                                                         envelope (E78.18).
  intrinsic residual reformulation                    -- `Q_ext-Q_logT` is
                                                         exactly the weighted
                                                         discrete curvature
                                                         `N^2(C_N-C_{N+2})` of
                                                         the signed section-lag
                                                         residual `C_N=N R_N`;
                                                         this reduces the live
                                                         arithmetic object to a
                                                         regularity/cofinal
                                                         statement for `C_N`,
                                                         with denominator
                                                         normalization still
                                                         present (E78.19).
  exact denominator side condition                    -- that normalization is
                                                         equivalent to a
                                                         two-sided cofinal bound
                                                         on `|Q_logT|/|Q_ext|`;
                                                         on audited zeta rows
                                                         this ratio already
                                                         lives in a tight band
                                                         near `1`, while the
                                                         plant does not sustain
                                                         that regime (E78.20).
  sharper same-sign reduction                         -- when `Q_ext` and
                                                         `Q_logT` have the same
                                                         sign, the normalized
                                                         defect is exactly
                                                         `|1-|Q_logT|/|Q_ext||`;
                                                         all audited zeta rows
                                                         satisfy this sign
                                                         coherence, while the
                                                         plant loses it on part
                                                         of the ladder
                                                         (E78.21).
  structural source of that coherence                 -- inside the exact Schur
                                                         split `Q_logT=Q_t0+
                                                         Q_theta`, sign
                                                         coherence reduces to
                                                         THETA-DOMINANCE:
                                                         fixed sign of
                                                         `Q_theta` plus
                                                         `|Q_theta|>|Q_t0|`;
                                                         this holds strongly on
                                                         audited zeta rows and
                                                         fails exactly where
                                                         the plant loses sign
                                                         coherence (E78.22).
  honest split of that target                         -- `THETA-DOMINANCE`
                                                         itself splits into
                                                         `THETA-SIGN-STABILITY`
                                                         (apparently governed by
                                                         the `u`-sector) plus
                                                         `T0-SMALLNESS`
                                                         (remaining quantitative
                                                         burden); plant loses
                                                         dominance more often
                                                         than sign compatibility
                                                         (E78.23).
  exact sign endpoint                                  -- `THETA-SIGN-STABILITY`
                                                         is exactly the sign of
                                                         the weighted second
                                                         drift of
                                                         `safe_u = 2 Re(iu)`,
                                                         i.e. `Q_theta`
                                                         itself; this reduces
                                                         the sign problem to
                                                         `SAFE-U-CURVATURE-SIGN`
                                                         (E78.24).
  sharper one-step sign target                         -- because
                                                         `Q_theta,N/N^2 =
                                                         N Delta safe_u_N -
                                                         (N+2) Delta safe_u_{N+2}`,
                                                         the sign problem
                                                         reduces further to
                                                         `SAFE-U-WEIGHTED-
                                                         MONOTONICITY`, a
                                                         weighted decay law for
                                                         consecutive
                                                         `Delta safe_u`
                                                         (E78.25).
  simplest sign-side endpoint                          -- equivalently, if
                                                         `A_N := N Delta
                                                         safe_u_N`, the sign
                                                         problem is strict
                                                         decay `A_N>A_{N+2}`;
                                                         zeta satisfies this on
                                                         the audited ladder and
                                                         the plant fails exactly
                                                         where the sign front
                                                         breaks (E78.26).
  quantitative refinement of that endpoint             -- with
                                                         `rho_N=A_{N+2}/A_N`,
                                                         the sign target
                                                         sharpens to
                                                         `SAFE-U-CONTRACTION:
                                                         rho_N<=rho_*<1`;
                                                         on audited zeta rows
                                                         rho stays in
                                                         `0.80898-0.88279`,
                                                         while the plant has
                                                         unstable, sign-changing
                                                         ratios (E78.27).
  strongest one-dimensional sign target                -- equivalently, one can
                                                         ask for the geometric
                                                         envelope
                                                         `0<A_{N+2}<=rho_*A_N`
                                                         for `A_N=N Delta
                                                         safe_u_N`; audited
                                                         zeta rows satisfy this
                                                         with observed
                                                         `rho_*=0.91223`, while
                                                         the plant fails by sign
                                                         loss (E78.28).
  payoff of that target                                -- the same geometric
                                                         envelope immediately
                                                         implies a geometric
                                                         tail and absolute
                                                         summability for
                                                         `Delta safe_u` on each
                                                         parity branch, so it
                                                         is directly useful for
                                                         cofinal assembly
                                                         (E78.29).
  primitive ratio form                                 -- the contraction ratio
                                                         `rho_N` factors exactly
                                                         as `((N+2)/N) *
                                                         (Delta safe_u_{N+2}/
                                                         Delta safe_u_N)`, so
                                                         the nontrivial target
                                                         is the raw one-step
                                                         ratio of consecutive
                                                         `Delta safe_u`; zeta
                                                         keeps it positive and
                                                         stable, plant loses it
                                                         by sign changes
                                                         (E78.30).
  most primitive geometric form                        -- one can ask directly
                                                         for
                                                         `0<Delta safe_u_{N+2}
                                                         <= eta_* Delta
                                                         safe_u_N`; audited
                                                         zeta rows satisfy this
                                                         with observed
                                                         `eta_*=0.82101`, while
                                                         the plant fails by raw
                                                         sign changes
                                                         (E78.31).
  exact polar anatomy of that form                     -- `Delta safe_u`
                                                         splits exactly into
                                                         modulus gain plus
                                                         angular correction for
                                                         `u`; on audited zeta
                                                         rows at least about
                                                         `85%` of the shell
                                                         increment comes from
                                                         modulus growth,
                                                         whereas the plant is
                                                         often driven or even
                                                         sign-flipped by the
                                                         angular term
                                                         (E78.32).
  exact scalarization of the angular term              -- the angular
                                                         correction is exactly
                                                         `2|u_N|(eps_N-eps_N+2)`
                                                         for the real vertical
                                                         defect
                                                         `eps_N=1-Im(u_N)/|u_N|`;
                                                         on audited zeta rows
                                                         this stays below about
                                                         `17.4%` of the modulus
                                                         term, while the plant
                                                         often exceeds it by
                                                         large factors
                                                         (E78.33).
  algebraic formula for that defect                    -- `eps_N` is exactly
                                                         `1-det_norm_N`, where
                                                         `det_norm_N` is the
                                                         normalized determinant
                                                         of `(theta'_N,
                                                         1-theta_N)`; on the
                                                         audited zeta ladder
                                                         `det_norm_N` stays
                                                         positive and close to
                                                         `1`, while the plant
                                                         can make it small or
                                                         negative
                                                         (E78.34).
  positive quadratic form of the same defect           -- equivalently,
                                                         `eps_N` is exactly
                                                         half the squared
                                                         distance between
                                                         normalized `theta'_N`
                                                         and the `+pi/2`
                                                         rotation of
                                                         normalized
                                                         `(1-theta_N)`; this
                                                         turns the angular
                                                         front into the drift
                                                         of a positive
                                                         quadratic
                                                         misalignment energy
                                                         (E78.35).
  exact drift split of that energy                     -- the shell drift of
                                                         the quadratic defect
                                                         polarizes exactly
                                                         into a
                                                         numerator-direction
                                                         term for normalized
                                                         `theta'_N` plus a
                                                         denominator-direction
                                                         term for normalized
                                                         `(1-theta_N)`; on the
                                                         audited zeta ladder
                                                         the denominator piece
                                                         is already secondary,
                                                         while it can dominate
                                                         in the planted build
                                                         (E78.36).
  exact control of the denominator piece               -- the
                                                         denominator-direction
                                                         term is bounded by the
                                                         averaged quadratic
                                                         misalignment size
                                                         times the chord of the
                                                         normalized
                                                         `(1-theta_N)`
                                                         direction, reducing
                                                         that correction to a
                                                         tiny nonnegative shell
                                                         scalar `DIRDEF_b,N`
                                                         (E78.37).
  phase form of the same scalar                        -- `DIRDEF_b,N` is
                                                         exactly the phase
                                                         defect
                                                         `1-cos(Delta phi_b,N)
                                                         = 2 sin^2(Delta
                                                         phi_b,N/2)` for the
                                                         unit-circle step of
                                                         normalized
                                                         `(1-theta_N)`, so the
                                                         denominator front
                                                         reduces to
                                                         DEN-PHASE-RIGIDITY
                                                         (E78.38).
  raw quotient form of that phase                      -- the phase step is
                                                         exactly the argument
                                                         of the raw shell
                                                         quotient
                                                         `(1-theta_N+2)/
                                                         (1-theta_N)`, hence
                                                         denominator rigidity
                                                         reduces to small
                                                         quotient skew
                                                         `Im(q_b,N)/Re(q_b,N)`
                                                         (E78.39).
  real-imag split of that quotient                     -- on the audited zeta
                                                         ladder `Re(q_b,N)` is
                                                         bounded away from `0`,
                                                         so denominator
                                                         rigidity reduces
                                                         further to small
                                                         `Im(q_b,N)` at a fixed
                                                         real scale
                                                         (E78.40).
  bilinear form of that imaginary part                 -- `Im(q_b,N)` is
                                                         exactly the
                                                         symplectic shell
                                                         numerator
                                                         `det(1-theta_N+2,
                                                         1-theta_N)` divided
                                                         by `|1-theta_N|^2`,
                                                         so the denominator
                                                         front reduces to a
                                                         finite oriented-area
                                                         target
                                                         (E78.41).
  increment form of that numerator                     -- the same symplectic
                                                         numerator is exactly
                                                         `det(Delta d_N,d_N)`
                                                         with
                                                         `Delta d_N =
                                                         (1-theta_N+2) -
                                                         (1-theta_N)`, so the
                                                         denominator front
                                                         reduces further to a
                                                         shell increment-area
                                                         target
                                                         (E78.42).
  directional normalization of that target             -- the increment area
                                                         factors as
                                                         `|Delta d_N| |d_N|`
                                                         times a pure
                                                         directional defect
                                                         `DIRINC_N`, reducing
                                                         the denominator front
                                                         to a shell direction
                                                         law for `Delta d_N`
                                                         relative to `d_N`
                                                         (E78.43).
  centered quotient form of that law                  -- the same direction
                                                         law is exactly the
                                                         normalized imaginary
                                                         part of the centered
                                                         quotient
                                                         `Delta d_N / d_N`;
                                                         on audited zeta rows
                                                         this quotient stays in
                                                         the left half-plane
                                                         and within about
                                                         `1.21e-2` relative
                                                         skew of the negative
                                                         real axis, while the
                                                         planted build already
                                                         fails there
                                                         (E78.44).
  honest new scalar in that centered picture          -- the only genuinely
                                                         new content of the
                                                         centered quotient is
                                                         the subunit real gap
                                                         `1-Re(q_N)=-Re(Delta
                                                         d_N/d_N)`; under that
                                                         barrier the directional
                                                         defect is controlled
                                                         by `|Im(q_N)|/(1-
                                                         Re(q_N))`, and the
                                                         planted build fails the
                                                         barrier already at the
                                                         early breaking steps
                                                         (E78.45).
  polar split of that new scalar                      -- the subunit gap
                                                         itself is exactly
                                                         `(1-|q_N|) +
                                                         |q_N|(1-cos(arg
                                                         q_N))`; on audited
                                                         zeta rows the angular
                                                         penalty is negligible
                                                         (max share about
                                                         `4.49e-5`), so the
                                                         real new burden is a
                                                         modulus-subunit law
                                                         `|q_N|<1`, while the
                                                         planted build can fail
                                                         already through
                                                         `|q_N|>1`
                                                         (E78.46).
  exact radial form of the modulus burden             -- the modulus condition
                                                         `|q_N|<1` is exactly
                                                         the shell contraction
                                                         law
                                                         `|1-theta_N+2| /
                                                         |1-theta_N| < 1`; on
                                                         audited zeta rows the
                                                         denominator norm
                                                         contracts strongly
                                                         step to step, while
                                                         the planted build
                                                         fails already by
                                                         violent early radial
                                                         expansion
                                                         (E78.47).
  squared-norm reformulation autopsied                -- the normalized squared
                                                         drop
                                                         `(|d_N|^2-|d_N+2|^2)/
                                                         |d_N|^2` equals
                                                         `(1-|q_N|)(1+|q_N|)`
                                                         exactly, so it is
                                                         equivalent to the same
                                                         radial contraction law
                                                         and not a smaller
                                                         theorem-grade target
                                                         (E78.48).
  logarithmic reformulation autopsied                 -- the multiplicative
                                                         contraction law is
                                                         equivalently the
                                                         additive drift
                                                         `log|d_N| -
                                                         log|d_N+2| =
                                                         -log|q_N|`, but this
                                                         is again equivalent to
                                                         the same radial target
                                                         rather than a smaller
                                                         one; its value is as
                                                         future telescoping
                                                         language, not as a new
                                                         endpoint
                                                         (E78.49).
  local quadratic increment law                       -- combining the radial
                                                         contraction with the
                                                         centered increment
                                                         `w_N = Delta d_N/d_N`
                                                         gives the exact local
                                                         inequality
                                                         `2 Re(w_N)+|w_N|^2<0`,
                                                         equivalently
                                                         `-2Re(w_N)>|w_N|^2`;
                                                         this moves the modulus
                                                         burden from a ratio
                                                         law on `|d_N|` to a
                                                         one-step quadratic
                                                         dominance law in the
                                                         shell increment itself
                                                         (E78.50).
  linear drift is the real live burden                -- on audited zeta rows
                                                         the whole quadratic
                                                         penalty `|w_N|^2` is
                                                         only about 15% of the
                                                         inward linear drift
                                                         `-2Re(w_N)` in median,
                                                         and the angular slice
                                                         `Im(w_N)^2` inside
                                                         that penalty is tiny;
                                                         the planted build
                                                         fails exactly when the
                                                         linear drift itself
                                                         turns outward, so the
                                                         next honest target is
                                                         a shell law for
                                                         `Re(w_N)`
                                                         (E78.51).
  normalization fully removed                         -- the same modulus
                                                         burden is exactly the
                                                         Euclidean shell
                                                         inequality
                                                         `-2<Delta d_N,d_N> >
                                                         |Delta d_N|^2`, i.e.
                                                         inward projection of
                                                         the raw increment
                                                         beats its own squared
                                                         size; this is the most
                                                         local denominator
                                                         modulus endpoint named
                                                         so far
                                                         (E78.52).
  projection polarization autopsied                   -- the inward projection
                                                         itself is exactly half
                                                         the signed radial
                                                         square change minus
                                                         half the increment
                                                         square, but this
                                                         collapses right back
                                                         to the same squared
                                                         radial drop law; so it
                                                         is structurally useful
                                                         but not a smaller
                                                         theorem-grade target
                                                         by itself
                                                         (E78.53).
  exact cone form of the same lock                    -- the Euclidean lock is
                                                         equivalently the cone
                                                         inequality
                                                         `|Delta d_N|/|d_N| +
                                                         2 cos(angle(Delta
                                                         d_N,d_N)) < 0`; on
                                                         audited zeta rows the
                                                         increment lies deep
                                                         inside that inward
                                                         cone with cosine
                                                         nearly `-1`, while the
                                                         planted build fails
                                                         exactly when the
                                                         increment points
                                                         outward and is too
                                                         large
                                                         (E78.54).
  size and direction fully merged                     -- on the inward branch,
                                                         the same cone lock is
                                                         exactly
                                                         `|Delta d_N|/|d_N| <
                                                         2 sqrt(1-DIRINC_N^2)`;
                                                         this merges the
                                                         denominator size-ratio
                                                         front with the
                                                         directional-defect
                                                         front into a single
                                                         exact criterion, and
                                                         audited zeta rows
                                                         satisfy it with very
                                                         large margin
                                                         (E78.55).
  final scalar gap factorization                      -- on the inward branch,
                                                         the full Euclidean
                                                         margin is exactly
                                                         `|Delta d_N||d_N|`
                                                         times the scalar gap
                                                         `2 sqrt(1-DIRINC_N^2)
                                                         - |Delta d_N|/|d_N|`;
                                                         so once the branch is
                                                         fixed, the whole
                                                         denominator front
                                                         collapses to the sign
                                                         of that one gap
                                                         (E78.56).
  branch condition fully scalarized                   -- the inward-branch
                                                         condition itself is
                                                         exactly `Re(Delta
                                                         d_N/d_N) < 0`, i.e.
                                                         the sign of the
                                                         centered shell
                                                         increment's real part;
                                                         audited zeta rows
                                                         satisfy this on every
                                                         tested step, and the
                                                         planted build fails
                                                         exactly when this real
                                                         part turns positive
                                                         (E78.57).
  denominator descent reaches a fixed point           -- E78.52-E78.57 do not
                                                         create a smaller
                                                         theorem-grade target
                                                         beyond the centered
                                                         quadratic core of
                                                         E78.50:
                                                         `2 Re(w_N)+|w_N|^2<0`;
                                                         from here on, further
                                                         progress must come
                                                         from a shell law for
                                                         `w_N` or `Re(w_N)`,
                                                         not from more
                                                         reparameterizations
                                                         (E78.58).
  exact bridge back to the theta cocycle              -- the centered core
                                                         variable itself is
                                                         exactly
                                                         `w_N = -Delta
                                                         theta_N/(1-theta_N)`,
                                                         so any further
                                                         denominator progress
                                                         must pass through the
                                                         Phase-77 ternary
                                                         `Delta theta` front
                                                         rather than through a
                                                         denominator-only
                                                         mechanism
                                                         (E78.59).
  ternarity survives normalization                    -- substituting the
                                                         Phase-77 cocycle
                                                         `Delta theta = A+B+C`
                                                         into the exact bridge
                                                         gives
                                                         `w_N = -(A+B+C)/
                                                         (1-theta_N)`, and on
                                                         the common audited
                                                         ladder the normalized
                                                         parts and normalized
                                                         pairs are still huge
                                                         compared with `|w_N|`
                                                         for zeta; so the live
                                                         target is now a
                                                         genuinely coupled
                                                         NORMALIZED-TERNARY-
                                                         CANCEL, not a safer
                                                         pairwise variant
                                                         (E78.60).
  taking real parts does not help either             -- the actual E78.50 core
                                                         uses `Re(w_N)`, but
                                                         on the same common
                                                         ladder the individual
                                                         real normalized parts
                                                         and the best real
                                                         normalized pairs are
                                                         still huge compared
                                                         with `|Re(w_N)|` for
                                                         zeta; hence the live
                                                         target sharpens to
                                                         `REAL-NORMALIZED-
                                                         TERNARY-CANCEL`
                                                         (E78.61).
  quotient removed from the real sign problem        -- the exact scalar
                                                         `Re(w_N)` equals
                                                         `-Re((A+B+C) conj(1-
                                                         theta_N)) / |1-
                                                         theta_N|^2`, so the
                                                         denominator is now a
                                                         harmless positive
                                                         factor and the live
                                                         target sharpens again
                                                         to the single coupled
                                                         numerator
                                                         `PAIRNUM-SIGN`
                                                         (E78.62).
  ternarity survives in the numerator itself         -- decomposing
                                                         `PAIRNUM_N =
                                                         -Re((A+B+C) conj(1-
                                                         theta_N))` into the
                                                         three real paired
                                                         pieces
                                                         `-Re(A conj d)`,
                                                         `-Re(B conj d)`,
                                                         `-Re(C conj d)` still
                                                         shows giant zeta-side
                                                         cancellation; neither
                                                         one part nor the best
                                                         pair is close to the
                                                         final scale, so the
                                                         live target sharpens
                                                         to the irreducibly
                                                         coupled
                                                         `PAIRNUM-TERNARY-
                                                         CANCEL`
                                                         (E78.63).
  no shortcut through `Q_theta` or `safe_u`          -- `PAIRNUM_N` is a
                                                         shell-direction real
                                                         pairing, while
                                                         `Q_theta` is the
                                                         sigma-derivative
                                                         second drift of
                                                         `safe_u`; on the
                                                         certified common
                                                         ladder the ratios
                                                         `PAIRNUM/Delta safe_u`
                                                         and `PAIRNUM/Q_theta`
                                                         vary substantially,
                                                         so the admissible next
                                                         target is the mixed
                                                         shell law
                                                         `MIXED-THETA-SHELL-
                                                         LAW`, not a reroute
                                                         through `Q_theta`
                                                         (E78.64).
  naive transfer-ratio reanchoring fails             -- the direct attempt to
                                                         rewrite `PAIRNUM_N`
                                                         as the quadratic
                                                         polarization of the
                                                         stored shell ratio
                                                         `q_N=1-theta_N=
                                                         T_N/t0_N` does not
                                                         match the current
                                                         certified artifacts;
                                                         therefore the next
                                                         honest target is an
                                                         explicit
                                                         `TRANSFER-RATIO-
                                                         ALIGNMENT` theorem
                                                         between the E77.5i
                                                         cocycle normalization
                                                         and the E77.5ac/E77.5g
                                                         shell rows
                                                         (E78.65).
  corrected transfer-ratio bridge                    -- the missing convention
                                                         is that the E77.5i
                                                         cocycle aligns with
                                                         the `old-old` shell
                                                         chain
                                                         `theta_old(N)-
                                                         theta_old(N+2)`, not
                                                         the mixed `old-new`
                                                         chain; on that
                                                         correct chain,
                                                         `PAIRNUM_N` is
                                                         exactly the quadratic
                                                         polarization of
                                                         `q_old(N)=1-theta_old
                                                         (N)=T_N/t0_N`, so the
                                                         live target sharpens
                                                         to
                                                         `OLD-OLD-TRANSFER-
                                                         CONTRACTION`
                                                         (E78.66).
  logarithmic bridge on the correct chain            -- because
                                                         `Delta ell_N =
                                                         log q_old(N) - log
                                                         q_old(N+2)`, the same
                                                         shell numerator is
                                                         exactly
                                                         `|q_old(N)|^2
                                                         Re(1-exp(-Delta
                                                         ell_N))`; this places
                                                         the live object
                                                         directly on the
                                                         old-old logarithmic
                                                         update already native
                                                         to E77.5g/E77.5l and
                                                         sharpens the target
                                                         to
                                                         `OLD-OLD-LOGQ-
                                                         CONTRACTION`
                                                         (E78.67).
  exact scalarization of the old-old log update      -- writing
                                                         `Delta ell_N =
                                                         a_N + i b_N`, the
                                                         same shell numerator
                                                         is exactly
                                                         `|q_N|^2 [1-exp(-
                                                         a_N) cos b_N]`; on
                                                         the audited zeta
                                                         ladder one sees
                                                         positive `a_N`,
                                                         extremely small
                                                         wrapped phase, and
                                                         positive scalar gain,
                                                         while the plant loses
                                                         this regime, so the
                                                         live target sharpens
                                                         again to
                                                         `LOGQ-GAIN-SIGN`
                                                         (E78.68).
  exact radial-vs-angular barrier                    -- on the admissible
                                                         sector
                                                         `|wrap Im Delta
                                                         ell_N| < pi/2`, the
                                                         sign of the same
                                                         scalar gain is
                                                         equivalent to
                                                         `Re Delta ell_N >
                                                         -log cos(|wrap Im
                                                         Delta ell_N|)`; on
                                                         the audited zeta
                                                         ladder the angular
                                                         barrier is tiny and
                                                         the radial margin is
                                                         uniformly positive,
                                                         while the plant fails
                                                         by letting the radial
                                                         drift fall below that
                                                         exact barrier, so the
                                                         live target sharpens
                                                         to `LOGQ-BARRIER`
                                                         (E78.69).
  quadratic sufficient barrier                       -- on `|wrap Im Delta
                                                         ell_N| <= 1`, the
                                                         exact angular barrier
                                                         obeys
                                                         `-log cos(beta) <=
                                                         beta^2`, so it is
                                                         enough to prove
                                                         `Re Delta ell_N >
                                                         |wrap Im Delta
                                                         ell_N|^2`; the
                                                         audited zeta ladder
                                                         satisfies this with
                                                         large margin, while
                                                         the plant does not,
                                                         so the live target
                                                         sharpens again to
                                                         `LOGQ-QUADRATIC-
                                                         BARRIER`
                                                         (E78.70).
  radial drift is an exact integral law              -- the radial part
                                                         `Re Delta ell_N` is
                                                         not a fresh scalar:
                                                         along the safe axis,
                                                         `d/dsigma Re Delta
                                                         ell_N = SAFEDELTA_N/2`
                                                         exactly, so the
                                                         radial barrier burden
                                                         reduces to a
                                                         left-endpoint lower
                                                         bound plus signed
                                                         integral control of
                                                         the already certified
                                                         shell safe
                                                         derivative; on the
                                                         audited zeta ladder
                                                         this derivative is
                                                         strictly negative
                                                         throughout, while the
                                                         plant loses that
                                                         sign regime
                                                         (E78.71).
  operational basepoint-tail split                   -- fixing a left endpoint
                                                         `sigma_0`, the exact
                                                         identity
                                                         `Re Delta ell_N(i
                                                         sigma)=BASE_N(
                                                         sigma_0)-TAIL_N(
                                                         sigma_0,sigma)`
                                                         turns the shell sign
                                                         into a three-piece
                                                         task: positive
                                                         basepoint,
                                                         controlled signed
                                                         tail loss, and
                                                         wrapped-phase square
                                                         below the remaining
                                                         reserve; on the
                                                         audited zeta ladder
                                                         the basepoint at
                                                         `sigma_0=0.55`
                                                         dominates the full
                                                         loss to `sigma=3` by
                                                         a wide margin
                                                         (E78.72).
  exact basepoint = old-old radial contraction       -- the basepoint reserve
                                                         itself is exactly
                                                         `log(|1-theta_old(
                                                         N)|/|1-theta_old(
                                                         N+2)|)`, so the
                                                         first ingredient of
                                                         the shell sign is
                                                         not an unnamed
                                                         constant but a
                                                         one-step radial
                                                         contraction law for
                                                         the old-old anchor;
                                                         on the audited zeta
                                                         ladder at
                                                         `sigma_0=0.55`
                                                         every step is
                                                         contractive, while
                                                         the planted build
                                                         alternates between
                                                         contraction and
                                                         expansion
                                                         (E78.73).
  exact reserve budget                               -- combining the
                                                         basepoint-tail split,
                                                         the old-old
                                                         contraction identity,
                                                         and the quadratic
                                                         barrier gives the
                                                         exact shell margin
                                                         identity
                                                         `Re Delta ell_N -
                                                         |wrap Im Delta
                                                         ell_N|^2 = BASE -
                                                         TAIL - phase^2`,
                                                         so the live shell
                                                         target sharpens to a
                                                         concrete three-term
                                                         budget inequality;
                                                         on the audited zeta
                                                         ladder this budget
                                                         stays uniformly
                                                         positive, while the
                                                         planted build does
                                                         not preserve that
                                                         regime (E78.74).
  fractional reserve criterion                       -- after dividing by the
                                                         positive basepoint
                                                         reserve, the shell
                                                         sign becomes the
                                                         dimensionless
                                                         inequality
                                                         `tail/base +
                                                         phase^2/base < 1`,
                                                         equivalently
                                                         `slack = 1 -
                                                         consumption`; on the
                                                         audited zeta ladder
                                                         total consumption
                                                         stays below about
                                                         `9.62e-2`, leaving
                                                         normalized slack
                                                         above about
                                                         `9.03e-1`
                                                         throughout
                                                         (E78.75).
  safe-u ratio shortcut dies                          -- the geometric
                                                         contraction ratio
                                                         `rho_N=A_{N+2}/A_N`
                                                         from the `safe_u`
                                                         front does not by
                                                         itself control the
                                                         normalized radial
                                                         tail `TAIL/BASE`;
                                                         on the common zeta
                                                         ladder the
                                                         correlation is weak
                                                         and wrong-signed,
                                                         while the amplitude
                                                         `A_N` itself
                                                         correlates strongly
                                                         with `TAIL/BASE`,
                                                         so the next honest
                                                         object is a
                                                         scale-coupled law
                                                         `SAFEU-BASE-
                                                         COUPLING`
                                                         (E78.76).
  scale-coupled tail candidate                        -- the radial budget
                                                         factorizes as
                                                         `TAIL/BASE =
                                                         (TAIL/A)*(A/BASE)`,
                                                         so the next honest
                                                         targets are
                                                         `SAFEU-TAIL-
                                                         COUPLING` and
                                                         `SAFEU-BASE-
                                                         COMPARISON`; on the
                                                         common zeta ladder
                                                         `TAIL/A` stays in the
                                                         small band
                                                         `0.00123-0.02908`
                                                         while `A/BASE`
                                                         stays in the band
                                                         `0.95145-4.42479`
                                                         (E78.77).
  exact normalized derivative target                  -- dividing the exact
                                                         tail integral by
                                                         `A_N` shows that
                                                         `TAIL/[A_N(σ-σ0)]`
                                                         is the radial average
                                                         of the normalized
                                                         derivative
                                                         `(-SAFEDELTA_N)/A_N`;
                                                         on the common zeta
                                                         ladder this average
                                                         correlates strongly
                                                         (`≈ 0.976`) with the
                                                         pointwise proxy, so
                                                         `SAFEU-TAIL-
                                                         COUPLING` sharpens to
                                                         `NORMALIZED-
                                                         SAFEDELTA-AVERAGE`
                                                         (E78.78).
  weighted normalized derivative                      -- on the common zeta
                                                         ladder the quantity
                                                         `(-SAFEDELTA_N)/A_N`
                                                         is organized much
                                                         better by the weight
                                                         `N` than by
                                                         sigma-based
                                                         normalizations,
                                                         suggesting the next
                                                         honest pointwise
                                                         target
                                                         `N*(-SAFEDELTA_N)/A_N
                                                         <= M(sigma)` and a
                                                         resulting `O(1/N)`
                                                         radial tail law
                                                         (E78.79).
  constant weighted envelope candidate                -- on the audited zeta
                                                         window one does not
                                                         yet need a nontrivial
                                                         sigma profile:
                                                         every certified row
                                                         already satisfies
                                                         `N*(-SAFEDELTA_N)/A_N
                                                         <= 0.321`, and at
                                                         fixed `N` the
                                                         `sigma=3.0` slice is
                                                         uniformly below the
                                                         `sigma=1.0` slice;
                                                         so the simplest
                                                         viable next target is
                                                         a constant envelope
                                                         `N*(-SAFEDELTA_N)/A_N
                                                         <= M_*`
                                                         (E78.80).
  sigma-monotone weighted derivative                  -- reconstructing
                                                         `A_N` directly from
                                                         the `E77.5ac` points
                                                         table extends the
                                                         common audit to
                                                         `N=20` and preserves
                                                         the pattern
                                                         `Y_N(3.0) < Y_N(1.0)`
                                                         for every available
                                                         row, so the next
                                                         honest sharpening is
                                                         a sigma-monotone
                                                         target for
                                                         `Y_N(sigma)=
                                                         N*(-SAFEDELTA_N)/A_N`
                                                         on the safe compact
                                                         (E78.81).
  left-endpoint reduction                             -- once sigma
                                                         monotonicity is
                                                         proved, the whole
                                                         weighted-safe-delta
                                                         front collapses to
                                                         the left endpoint
                                                         slice; on the current
                                                         audited slice
                                                         `sigma=1.0`, the
                                                         whole ladder lies in
                                                         `Y<=0.321` with worst
                                                         case
                                                         `Y_8(1.0)=
                                                         0.32033520392027215`
                                                         (E78.82).
  exact weighted quotient law                         -- the weighted object
                                                         `Y_N(sigma)=
                                                         N*(-SAFEDELTA_N)/A_N`
                                                         simplifies exactly to
                                                         the one-step quotient
                                                         `(-SAFEDELTA_N)/
                                                         Delta safe_u_N`,
                                                         so the radial front
                                                         is a direct
                                                         comparison between
                                                         the safe radial
                                                         derivative and the
                                                         shell `safe_u` drift
                                                         (E78.83).
  endpoint quotient leaves curvature branch           -- on the left endpoint
                                                         slice the exact
                                                         quotient
                                                         `(-SAFEDELTA_N)/
                                                         Delta safe_u_N`
                                                         correlates strongly
                                                         with `|u_N|` and the
                                                         sector margin, but
                                                         not with the
                                                         curvature scale
                                                         `Q_theta/(N^2 Delta
                                                         safe_u)`, so the
                                                         next honest object is
                                                         a `SECTOR-SIZE-
                                                         QUOTIENT`, not a
                                                         curvature-first
                                                         transfer
                                                         (E78.84).
  exact modulus quotient split                        -- the endpoint quotient
                                                         itself factors
                                                         exactly as
                                                         `(-SAFEDELTA_N)/
                                                         modulus_term_N`
                                                         times an angular
                                                         denominator factor
                                                         `modulus_share`;
                                                         on the certified
                                                         zeta ladder that
                                                         factor stays in
                                                         `[0.8520, 1.0038]`,
                                                         so the quotient front
                                                         reduces to
                                                         `MODULUS-QUOTIENT`
                                                         plus
                                                         `ANGULAR-
                                                         DENOMINATOR-
                                                         SMALLNESS`
                                                         (E78.85).
  angular denominator becomes one scalar alpha law    -- writing
                                                         `alpha_N :=
                                                         angular_term_N /
                                                         modulus_term_N =
                                                         2|u_N|
                                                         (eps_N-eps_N+2)/
                                                         modulus_term_N`
                                                         gives the exact law
                                                         `modulus_share =
                                                         1/(1+alpha_N)`,
                                                         so the entire
                                                         denominator branch
                                                         reduces to the single
                                                         target
                                                         `ALPHA-SMALLNESS`
                                                         (E78.86).
  modulus quotient also collapses to the endpoint      -- if
                                                         `(-SAFEDELTA_N(i
                                                         sigma))/
                                                         modulus_term_N`
                                                         is proved
                                                         sigma-decreasing on
                                                         the safe compact,
                                                         then the whole
                                                         modulus side reduces
                                                         exactly to its left
                                                         endpoint slice; the
                                                         current audited
                                                         ladder is fully
                                                         compatible, with
                                                         worst row
                                                         `M_8(1.0)=
                                                         0.3200997163`
                                                         (E78.87).
  exact 1/N source of the modulus quotient             -- writing
                                                         `modulus_term_N =
                                                         2(|u_N+2|-|u_N|)
                                                         s_N+2` gives an
                                                         exact split of the
                                                         modulus quotient into
                                                         an `O(1)` growth
                                                         quotient times the
                                                         explicit sector
                                                         factor `1/(N s_N+2)`;
                                                         this explains the
                                                         scale but also
                                                         autopsies the next
                                                         bad shortcut, because
                                                         the sector factor is
                                                         the old
                                                         build-separating
                                                         detector and should
                                                         remain subordinate
                                                         bookkeeping
                                                         (E78.88).
  growth-quotient monotonicity is a false trail        -- the isolated
                                                         `GROWTH-QUOTIENT`
                                                         from E78.88 is not
                                                         sigma-decreasing on
                                                         the certified ladder
                                                         (`N=16,18` already
                                                         violate it), so the
                                                         honest monotonicity
                                                         object remains the
                                                         weighted modulus
                                                         quotient
                                                         `W_N=N*MODULUS-
                                                         QUOTIENT_N`
                                                         rather than the raw
                                                         growth quotient
                                                         (E78.89).
  endpoint weighted modulus is the honest burden       -- on the left endpoint
                                                         slice `sigma=1.0`,
                                                         the weighted modulus
                                                         quotient
                                                         `W_N=N*MODULUS-
                                                         QUOTIENT_N` stays in
                                                         the audited band
                                                         `[2.152695,
                                                         2.586236]` through
                                                         `N=20`, with worst row
                                                         `W_12(1.0)=
                                                         2.5862363964`;
                                                         meanwhile the obvious
                                                         transfers to the
                                                         radial reserve scales
                                                         `A_N`, `BASE_N`,
                                                         `TAIL_N/BASE_N` are
                                                         too weak to justify a
                                                         theorem, so the live
                                                         endpoint target is the
                                                         constant-envelope law
                                                         `W_N(1.0) <= C_*`
                                                         itself (E78.90).
  u-growth comes from a radial gap, not a mystery      -- because
                                                         `u_N+2/u_N =
                                                         q_a,N/q_b,N` with
                                                         `q_a,N=
                                                         theta'_N+2/theta'_N`
                                                         and
                                                         `q_b,N=
                                                         (1-theta_N+2)/
                                                         (1-theta_N)`, the
                                                         shell growth of `|u|`
                                                         is driven exactly by
                                                         the explicit radial
                                                         gap `|q_a,N|-|q_b,N|`;
                                                         this gap stays
                                                         strictly positive on
                                                         the audited zeta
                                                         ladder and already
                                                         fails on the planted
                                                         falsifier, so the
                                                         modulus-growth front
                                                         reduces to
                                                         `U-RADIAL-GAP`
                                                         plus the safe
                                                         derivative numerator
                                                         (E78.91).
  endpoint weighted modulus is a gap quotient          -- substituting the
                                                         exact radial-gap law
                                                         into the weighted
                                                         modulus quotient
                                                         gives
                                                         `W_N = PREF_N /
                                                         U-RADIAL-GAP_N`,
                                                         so the left-endpoint
                                                         burden reduces
                                                         admissibly to
                                                         `PREF-CONTROL +
                                                         U-RADIAL-GAP-
                                                         LOWER-BOUND` rather
                                                         than a black-box
                                                         envelope for `W_N`
                                                         (E78.92).
  the rigid half is the radial gap                     -- in the exact split
                                                         `W_N=PREF_N/
                                                         U-RADIAL-GAP_N`, the
                                                         gap is the organized
                                                         side: it stays
                                                         strictly positive and
                                                         sigma-slice monotone
                                                         on the certified zeta
                                                         ladder, while the
                                                         prefactor still
                                                         oscillates and the
                                                         planted falsifier
                                                         already breaks the gap
                                                         by sign loss; so the
                                                         primary live target is
                                                         `U-RADIAL-GAP-
                                                         LOWER-BOUND`, with
                                                         `PREF-CONTROL`
                                                         downgraded to
                                                         bookkeeping
                                                         (E78.93).
  the gap itself polarizes toward the denominator      -- the primary gap
                                                         `|q_a,N|-|q_b,N|`
                                                         splits exactly as
                                                         `(|q_a,N|-1) +
                                                         (1-|q_b,N|)`;
                                                         on the certified zeta
                                                         ladder the coherent
                                                         monotone piece is the
                                                         denominator radial
                                                         deficit `1-|q_b,N|`,
                                                         while the numerator
                                                         gain changes sign
                                                         after the first
                                                         steps, and the planted
                                                         falsifier breaks the
                                                         law exactly by losing
                                                         denominator
                                                         contraction, so the
                                                         sharpened primary
                                                         target is the
                                                         denominator radial
                                                         deficit with the
                                                         numerator gain treated
                                                         as correction
                                                         (E78.94).
  the exact one-sided forcing law is now visible       -- writing the
                                                         numerator side as the
                                                         nonnegative loss
                                                         `max(0,-(|q_a,N|-1))`
                                                         turns the primary gap
                                                         into an exact
                                                         denominator margin:
                                                         `U-RADIAL-GAP_N =
                                                         DENOMINATOR-RADIAL-
                                                         DEFICIT_N -
                                                         NUMERATOR-LOSS_N`
                                                         in the late regime,
                                                         so the sharpest live
                                                         target is the
                                                         one-sided dominance
                                                         law
                                                         `DENOMINATOR-RADIAL-
                                                         DEFICIT >
                                                         NUMERATOR-LOSS`,
                                                         which the planted
                                                         falsifier already
                                                         fails by sign
                                                         (E78.95).
  the denominator deficit is fully local now           -- the denominator
                                                         deficit itself equals
                                                         the negative
                                                         quadratic residual of
                                                         the centered quotient
                                                         `w_N=Delta d_N/d_N`,
                                                         divided by the benign
                                                         factor `1+|q_b,N|`;
                                                         so the healthy half
                                                         of the front is
                                                         completely reduced to
                                                         a local shell
                                                         quadratic margin, and
                                                         the real live burden
                                                         has shifted to
                                                         bounding
                                                         `NUMERATOR-LOSS`
                                                         sharply enough to
                                                         dominate it
                                                         (E78.96).
  the shell-gap route is now autopsied                 -- the exact current
                                                         endpoint of the route
                                                         is
                                                         `NEGATIVE-QUADRATIC-
                                                         MARGIN >
                                                         (1+|q_b|) NUMERATOR-
                                                         LOSS`; the
                                                         denominator side is
                                                         completely local, but
                                                         the unresolved
                                                         numerator side still
                                                         runs through the
                                                         invariant Schur/log
                                                         residual with moving
                                                         `1/N` profile drift
                                                         from `E77.5m/E77.5n`,
                                                         so no cofinal scalar
                                                         theorem is presently
                                                         available. By mission
                                                         budget this route is
                                                         closed by autopsy and
                                                         the next valid front
                                                         is
                                                         `SAFE-GAMMA-IDENT`
                                                         direct
                                                         (E78.97).
  the tail side of the arithmetic front is already
  closed                                               -- absolute Euler tail
                                                         (`P76.039`) and high
                                                         Xi tail (`P76.038`)
                                                         already give the
                                                         needed uniform
                                                         compact control, so
                                                         `SAFE-GAMMA-IDENT /
                                                         OUTER-LIMIT` reduce
                                                         to the exact fixed-L
                                                         holomorphic core
                                                         `CELL-TRACE-WINDOW /
                                                         SAFE-GAMMA-IDENT-
                                                         CORE`
                                                         (E78.98).
  the fixed-L core splits into shell plus directional
  mu motion                                            -- the intrinsic moving
                                                         family
                                                         `J_{L,N}(mu_N)` is
                                                         exactly
                                                         `SHELL-LOG + MU-DIR`,
                                                         with the directional
                                                         piece isolated as the
                                                         integral
                                                         `int_0^{mu_N}
                                                         partial_mu J`
                                                         (E78.99).
  the current shell route is exhausted                 -- the cocycle chain
                                                         down to
                                                         `Q_N = N^2(C_N-
                                                         C_{N+2})` hits the
                                                         unresolved
                                                         `N=2 mod 4` spike, so
                                                         the present route to
                                                         `SHELL-LOG` is closed
                                                         by theorem-grade
                                                         autopsy; the live
                                                         front-B effort moves
                                                         to the directional
                                                         term / direct
                                                         holomorphic
                                                         identification
                                                         (E78.100).
  the directional term is now smaller and exact       -- `MU-DIR` itself
                                                         reduces to
                                                         `MU-BASEPOINT
                                                         (mu_N -> 0)` plus a
                                                         local paired
                                                         derivative bound
                                                         `PAIRED-DMU-LOCAL`
                                                         for `partial_mu J`.
                                                         The zeta audited
                                                         ladder is consistent
                                                         with tiny path length
                                                         and finite local
                                                         derivative, while the
                                                         planted falsifier
                                                         breaks exactly at the
                                                         basepoint condition,
                                                         as front B predicts
                                                         (E78.101).
  the low-mode spectral route to the local derivative
  is now closed by autopsy                            -- the exact ground-mode
                                                         term in
                                                         `r_z A_N(0)^(-2)b_N`
                                                         carries a squared
                                                         inner-gap denominator,
                                                         while the available
                                                         paired overlaps
                                                         suppress at most one
                                                         gap power.  On the
                                                         audited zeta ladder
                                                         the quantity
                                                         `|<r,v0><v0,b>|/
                                                         nu0^2` blows up
                                                         violently, so the
                                                         ground-localization
                                                         mechanism cannot
                                                         prove
                                                         `PAIRED-DMU-LOCAL`.
                                                         The next admissible
                                                         route is the coupled-
                                                         generator derivative
                                                         package, not spectral
                                                         projection
                                                         (E78.102).
  the local mu derivative now has an exact finite
  generator package                                   -- `partial_mu(F_b'/F_b)`
                                                         is generated exactly
                                                         by the four coupled
                                                         solutions
                                                         `u,v,c_b,y_b` and the
                                                         scalar coefficients
                                                         `a_b,b_b,alpha_b,
                                                         beta_b`, with
                                                         `A y_b = h_b +
                                                         alpha_b s + beta_b 1`.
                                                         The implementation
                                                         checks against the
                                                         exact `A^{-2}b`
                                                         derivative at
                                                         `~1e-48` in zeta and
                                                         `~1e-52` in the
                                                         planted build, so the
                                                         next live burden is
                                                         no longer existence of
                                                         the derivative
                                                         formula but the
                                                         cofinal control of the
                                                         package
                                                         `(F_b,c_b,y_b)`
                                                         itself
                                                         (E78.103).
  the exact burden is now localized inside the
  auxiliary source branch                              -- on the audited safe
                                                         ladder `|F_b|` stays
                                                         large and `|F_b'|`
                                                         remains secondary,
                                                         while the auxiliary
                                                         branch
                                                         `c_b -> (alpha_b,
                                                         beta_b) -> y_b`
                                                         blows up rapidly in
                                                         both builds.  Thus the
                                                         next live object is
                                                         `AUX-DMU-SOURCE`,
                                                         not a putative zero of
                                                         `F_b`
                                                         (E78.104).
  the auxiliary source itself now splits cleanly      -- writing
                                                         `y_b = y_b^(h) +
                                                         y_b^(ab)` with
                                                         `A y_b^(h)=h_b` and
                                                         `A y_b^(ab)=alpha_b s
                                                         + beta_b 1` shows on
                                                         the audited ladder
                                                         that the scalar
                                                         `alpha_b,beta_b`
                                                         branch is secondary
                                                         (`||y_ab||/||y||`
                                                         drops from ~0.18 to
                                                         ~0.10).  The next live
                                                         object is therefore
                                                         `H-DMU-SOURCE`,
                                                         i.e. the intrinsic
                                                         branch `A^{-1}h_b`
                                                         (E78.105).
  the intrinsic source is itself v-dominated         -- splitting
                                                         `h_b = a_b u + b_b v`
                                                         and therefore
                                                         `A^{-1}h_b =
                                                         y_b^(u)+y_b^(v)`
                                                         shows on the audited
                                                         ladder that
                                                         `y_b^(v)=A^{-1}(b_b v)`
                                                         already equals the
                                                         whole source to the
                                                         displayed scale in
                                                         both builds.  The next
                                                         live object is
                                                         `V-DMU-SOURCE`
                                                         (E78.106).
  the v-source is resolvent-dominated                -- writing
                                                         `y_b^(v)=b_b A^{-1}v`
                                                         shows on the audited
                                                         ladder that the
                                                         coefficient `b_b`
                                                         fluctuates and is
                                                         often tiny, while the
                                                         violent growth tracks
                                                         `A^{-1}v` itself.
                                                         The next live object
                                                         is therefore
                                                         `V-RESOLVENT-SOURCE`
                                                         (E78.107).
  the zeta resolvent source is ground-mode
  dominated on the audited ladder                     -- for zeta,
                                                         `A^{-1}v=A^{-2}1`
                                                         coincides with its
                                                         ground-mode
                                                         projection to the
                                                         displayed scale,
                                                         while the planted
                                                         build does not.  On
                                                         the zeta side, the
                                                         next live object is
                                                         the scalar ground
                                                         coefficient plus a
                                                         negligible-tail
                                                         statement
                                                         `G0-RESOLVENT-
                                                         SOURCE`
                                                         (E78.108).
  the crude ground-tail certificate is now closed
  by autopsy                                          -- the exact inequality
                                                         `||tail||/||ground||
                                                         <= (sqrt(N)/
                                                         |<v0,1>|) *
                                                         (nu0/nu1)^2` is
                                                         correct, but useless
                                                         on the audited zeta
                                                         ladder because the
                                                         bad factor is the raw
                                                         overlap
                                                         `|<v0,1>|^{-1}`.
                                                         So the route "gap
                                                         ratio + raw overlap
                                                         with 1" is dead, and
                                                         the next admissible
                                                         object must retain
                                                         the resolvent-weighted
                                                         off-ground piece
                                                         `(I-P0)A^{-1}1`
                                                         instead of collapsing
                                                         to `||1||`
                                                         (E78.109).
  the second-resolvent tail now has a sharp
  first-resolvent gate                               -- the exact inequality
                                                         `||tail(A^-2 1)|| /
                                                         ||ground(A^-2 1)||
                                                         <= |nu0/nu1| *
                                                         ||off(A^-1 1)|| /
                                                         ||ground(A^-1 1)||`
                                                         reduces the
                                                         negligible-tail
                                                         problem to the
                                                         off-ground ratio of
                                                         the first resolvent.
                                                         On the audited zeta
                                                         ladder this
                                                         certificate is
                                                         genuinely small
                                                         (`~1e-6`), while the
                                                         planted falsifier
                                                         breaks there as front
                                                         B allows.  The next
                                                         live object is
                                                         `G0-FIRST-
                                                         RESOLVENT`
                                                         (E78.110).
  the derivative-relevant second-resolvent tail is
  now purely paired                                   -- for every safe Cauchy
                                                         row `r_z`,
                                                         `<r_z,(I-P0)A^-2 1>`
                                                         equals exactly
                                                         `<(I-P0)A^-1 r_z,
                                                         (I-P0)A^-1 1>`.
                                                         This removes the free
                                                         vector tail from the
                                                         front and replaces it
                                                         by the paired first-
                                                         resolvent package.
                                                         On the audited safe
                                                         row family the zeta
                                                         Cauchy-side
                                                         off-ground ratio is
                                                         `10^-4 - 10^-3`,
                                                         while the planted
                                                         falsifier breaks by
                                                         huge factors exactly
                                                         on front B.  The next
                                                         live object is
                                                         `PAIRED-FIRST-
                                                         RESOLVENT`
                                                         (E78.111).
  the Cauchy half of that package is now reduced
  to raw geometry                                      -- the exact bound
                                                         `||(I-P0)A^-1 b|| /
                                                         ||P0 A^-1 b||
                                                         <= |nu0/nu1| *
                                                         ||(I-P0)b|| /
                                                         |<v0,b>|` reduces the
                                                         safe-row side
                                                         `b=r_z` to the raw
                                                         geometric ratio of
                                                         the Cauchy row.
                                                         Across the audited
                                                         zeta ladder the
                                                         resulting certificate
                                                         stays small
                                                         (`~1e-3 - 1e-2`),
                                                         while the planted
                                                         falsifier fails there
                                                         as front B allows.
                                                         The only remaining
                                                         live part of the pair
                                                         is now
                                                         `SOURCE-FIRST-
                                                         RESOLVENT`
                                                         (E78.112).
  the source side is now reduced to a safe scalar
  family                                              -- after reducing the
                                                         Cauchy side and
                                                         autopsying the raw
                                                         source geometry, the
                                                         only source data still
                                                         used by the
                                                         derivative-relevant
                                                         tail are the scalar
                                                         pairings
                                                         `S_N(z)=< (I-P0)A^-1
                                                         r_z, A^-1 1 >`.
                                                         This shrinks the live
                                                         burden from a full
                                                         off-ground vector to
                                                         the safe source-
                                                         pairing functional
                                                         `SAFE-SOURCE-PAIR`
                                                         (E78.114).
  that safe source family is now reduced to one
  scalar per section                                   -- by writing
                                                         `S_N(z)=<g_z,off_1>`
                                                         and applying
                                                         Cauchy-Schwarz after
                                                         the safe pairing,
                                                         the entire source
                                                         dependence collapses
                                                         to
                                                         `SOURCE-OFFGROUND-
                                                         NORM(N)=||(I-P0)A^-1
                                                         1||`.
                                                         The `z` dependence
                                                         stays only on the
                                                         already-reduced
                                                         Cauchy side.
                                                         So the only remaining
                                                         live source object is
                                                         now this single scalar
                                                         sequence
                                                         (E78.115).
  that source-norm route is now closed by autopsy      -- the exact
                                                         factorization
                                                         `|S_N(z)|=||g_z||
                                                         ||off_1|| cos_N(z)`
                                                         shows that the norm
                                                         route loses the
                                                         normalized
                                                         off-ground
                                                         correlation angle
                                                         `cos_N(z)`.
                                                         On the audited zeta
                                                         ladder this angle is
                                                         only
                                                         `~3e-3 - 9e-3`,
                                                         while on the planted
                                                         falsifier it is
                                                         essentially `1`.
                                                         So the only honest
                                                         remaining source
                                                         object is now
                                                         `SOURCE-PAIR-ANGLE`
                                                         (E78.116).
  the first off-ground mode is also dead as an
  explanation of that angle                            -- on the audited zeta
                                                         ladder the safe Cauchy
                                                         vector `g_z` is almost
                                                         entirely in the first
                                                         off-ground mode, but
                                                         the source vector
                                                         `off_1` has
                                                         essentially zero mass
                                                         there.  So the mode-1
                                                         contribution to the
                                                         pairing is negligible,
                                                         and the same mode is
                                                         also negligible on the
                                                         planted side.  The
                                                         remaining live object
                                                         must therefore be
                                                         distributed across
                                                         many off-ground modes
                                                         or encoded by a finite
                                                         coupled coefficient
                                                         mixing them
                                                         (E78.117).
  that distributed picture now collapses to two
  modes on the audited safe frontier                   -- the first off-ground
                                                         mode contributes
                                                         essentially nothing,
                                                         but the first two
                                                         off-ground
                                                         coordinates together
                                                         already saturate the
                                                         full source pairing to
                                                         displayed precision on
                                                         both builds.  So the
                                                         live angular object is
                                                         no longer an arbitrary
                                                         profile; it reduces to
                                                         the finite coefficient
                                                         `gamma_1(z)omega_1 +
                                                         gamma_2(z)omega_2`
                                                         (E78.118).
  that two-mode coefficient now collapses to the
  second mode alone                                     -- on the audited safe
                                                         frontier the first
                                                         off-ground term is
                                                         negligible and the
                                                         full pairing is
                                                         saturated to displayed
                                                         precision by
                                                         `gamma_2(z)omega_2`.
                                                         So the remaining live
                                                         object on this route
                                                         is now a single finite
                                                         modal coefficient
                                                         (E78.119).
  that modal coefficient is now carried by the
  Cauchy side alone                                     -- the source vector
                                                         `off_1` is already
                                                         essentially pure mode
                                                         2 on the audited safe
                                                         frontier, so the
                                                         remaining variation of
                                                         the angle is governed
                                                         by the mode-2
                                                         amplitude of `g_z`.
                                                         The live object is now
                                                         `MODE2-CAUCHY-
                                                         AMPLITUDE(z)`
                                                         (E78.120).
  that modal amplitude is now reduced to a raw
  spectral overlap                                      -- the mode-2
                                                         coefficient of `g_z`
                                                         is exactly
                                                         `gamma_2(z)=<v_2,r_z>/
                                                         nu_2`, so the
                                                         remaining live object
                                                         is the single overlap
                                                         `<v_2,r_z>` against
                                                         the safe Cauchy row,
                                                         up to the explicit
                                                         eigenvalue factor
                                                         `nu_2`
                                                         (E78.121).
  on the safe axis that overlap is now reduced to a
  real scalar amplitude                                 -- the mode `v_2` is
                                                         even to roundoff on
                                                         the audited sections,
                                                         and the overlap
                                                         `<v_2,r_{it}>` is
                                                         purely imaginary to
                                                         roundoff.  So on the
                                                         safe family the live
                                                         object is now the real
                                                         scalar
                                                         `MODE2-SAFE-
                                                         AMPLITUDE(t)=Im
                                                         <v_2,r_{it}>`
                                                         (E78.123).
  that safe scalar is now reduced to a real
  half-axis transform                                   -- by pairing the
                                                         symmetric interior
                                                         mesh and using the
                                                         evenness of `v_2`,
                                                         the amplitude becomes
                                                         exactly
                                                         `-v_2(0)/t - 2t
                                                         sum_{n>0}
                                                         v_2(n)/(t^2+d_n^2)`.
                                                         So the remaining live
                                                         object on this route
                                                         is now the explicit
                                                         half-axis kernel
                                                         transform
                                                         `HALF-AXIS-MODE2(t)`
                                                         (E78.124).
  that half-axis transform is not one-shell, but it
  already closes on a short signed profile             -- the zero mode and
                                                         first one/two shells
                                                         do not close it
                                                         monotonically, but the
                                                         signed profile using
                                                         the first five
                                                         positive shells already
                                                         reproduces the audited
                                                         safe transform closely.
                                                         So the explicit
                                                         exploratory endpoint on
                                                         this route is now
                                                         `FIVE-SHELL-MODE2(t)`
                                                         (E78.126).
  that five-shell profile does not obey a simple
  universal sign-ratio law                             -- the planted build
                                                         has a clean
                                                         alternating-decay
                                                         signature, but the
                                                         zeta five-shell vector
                                                         has the different sign
                                                         pattern `+ - - + - +`
                                                         with non-monotone,
                                                         non-geometric ratios.
                                                         So the honest finite
                                                         live object is the
                                                         full signed five-shell
                                                         vector itself, not a
                                                         one-parameter shell
                                                         law
                                                         (E78.127).
  that five-shell vector is already captured by a
  three-dimensional coupled span                       -- on the audited safe
                                                         frontier the full
                                                         signed five-shell
                                                         vector is strongly
                                                         captured by
                                                         `span(u,v,c)`, with
                                                         zeta scores about
                                                         `0.92` and `0.95` and
                                                         planted scores
                                                         `0.9998+`.  So the
                                                         exploratory live
                                                         object is now the
                                                         finite projection
                                                         `THREE-DIM-PACKAGE-
                                                         MODE2`
  that package does not collapse to one coordinate
  or any two-coordinate subpackage                    -- on the zeta side the
                                                         orthogonal package
                                                         mass splits stably as
                                                         about `0.30 / 0.53 /
                                                         0.16` across
                                                         `(u,v,c)`, and the
                                                         best audited 2D
                                                         capture stays around
                                                         `0.70-0.74`.  So
                                                         dimension three is
                                                         the minimal honest
                                                         finite package on
                                                         this route
                                                         (E78.129).
  that whole mode2/package branch is exploratory
  only                                                -- every step from
                                                         `MODE2-SAFE-
                                                         AMPLITUDE` down to
                                                         `THREE-DIM-PACKAGE-
                                                         MODE2` is restricted
                                                         to the audited safe
                                                         frontier and does not
                                                         prove any cofinal
                                                         `N>=N_0` statement or
                                                         any implication to
                                                         `PAIRED-DMU-LOCAL` /
                                                         `SAFE-GAMMA-IDENT-
                                                         CORE`.  So the exact
                                                         failed quantifier is
                                                         cofinality in `N`,
                                                         and the branch is now
                                                         archived as
                                                         exploratory rather
                                                         than live for closure
                                                         (E78.130).
  after archiving that branch, the front-B return
  point is above the safe-axis portrait                -- the next live
                                                         cofinal burden is not
                                                         `MODE2-SAFE-
                                                         AMPLITUDE` or
                                                         `THREE-DIM-PACKAGE-
                                                         MODE2`, but the
                                                         derivative-side core
                                                         `PAIRED-DMU-LOCAL`
                                                         and, inside its exact
                                                         coupled package, the
                                                         unresolved source
                                                         control branch named
                                                         in E78.104-E78.105.
  the loss of cofinality actually happens earlier
  than the mode2 split                                 -- from E78.106 onward
                                                         the chain
                                                         `H-DMU-SOURCE ->
                                                         V-DMU-SOURCE ->
                                                         V-RESOLVENT-SOURCE ->
                                                         ...` is justified
                                                         only on the audited
                                                         ladder / audited zeta
                                                         side, so it does not
                                                         prove `SAFE-Y-BOUND`
                                                         or any smaller
                                                         cofinal predecessor.
                                                         The true return point
                                                         is therefore the last
                                                         source-level objects
                                                         with cofinal
                                                         formulation:
                                                         `SAFE-Y-BOUND /
                                                         AUX-DMU-SOURCE /
                                                         H-DMU-SOURCE`
                                                         (E78.131).
  the loss of cofinality actually starts already at
  the split to H-DMU-SOURCE                            -- E78.105 proves only
                                                         that `y_b^(h)`
                                                         dominates
                                                         `y_b^(ab)` on the
                                                         audited ladder, with
                                                         ratios around
                                                         `0.10-0.18`, but no
                                                         `N>=N_0` theorem and
                                                         no separate cofinal
                                                         control of the scalar
                                                         branch.  So even
                                                         `H-DMU-SOURCE` is not
                                                         yet a legal cofinal
                                                         predecessor of
                                                         `SAFE-Y-BOUND`, and
                                                         the true return point
                                                         rises to
                                                         `SAFE-Y-BOUND /
                                                         AUX-DMU-SOURCE`
                                                         (E78.132).
  the loss of cofinality starts even before the
  source-only localization                             -- E78.104 proves the
                                                         exact three-part
                                                         implication
                                                         `SAFE-F-
                                                         NONVANISHING +
                                                         SAFE-H-BOUND +
                                                         SAFE-Y-BOUND =>
                                                         DMU-COUPLED-
                                                         GENERATOR`, but the
                                                         further claim that
                                                         the burden "really
                                                         lives in y_b" is only
                                                         supported by audited
                                                         values of `min|F_b|`
                                                         and `||y_b||`.  So
                                                         `AUX-DMU-SOURCE` is
                                                         not yet a legal
                                                         cofinal predecessor,
                                                         and the true return
                                                         point rises once more
                                                         to the exact triple
                                                         burden itself
                                                         (E78.133).
  one part of that triple burden is inherited rather
  than new                                              -- `SAFE-F-
                                                         NONVANISHING` is
                                                         exactly the same
                                                         denominator clause
                                                         `F_b = 1 + W_{L,N}`
                                                         already present in
                                                         the fixed-`L`
                                                         two-generator front
                                                         E78.6-E78.8. So,
                                                         relative to the
                                                         standing front-B
                                                         work, the genuinely
                                                         new derivative burden
                                                         is only
                                                         `SAFE-H-BOUND +
                                                         SAFE-Y-BOUND`
                                                         (E78.134).
  the remaining derivative-side transport of F_b' is
  also inherited up to the source term                  -- by
                                                         `partial_mu F_b'=
                                                         Y_b'` and
                                                         `F_b'(z;0)=W'_{L,N}`,
                                                         the clause
                                                         `SAFE-H-BOUND` follows
                                                         from a shared
                                                         basepoint bound for
                                                         `W'_{L,N}` together
                                                         with `SAFE-Y-BOUND`.
                                                         So the only
                                                         genuinely new
                                                         derivative-specific
                                                         clause left under
                                                         `DMU-COUPLED-
                                                         GENERATOR` is now
                                                         `SAFE-Y-BOUND`
                                                         (E78.135).
  that last derivative clause is itself only one
  source norm                                           -- on a fixed safe
                                                         compact, the three
                                                         transforms
                                                         `Y_b(i sigma)`,
                                                         `Y_b^bd`, and
                                                         `Y_b'(i sigma)` are
                                                         uniformly controlled
                                                         by `||y_b||_2`
                                                         through the l2 norms
                                                         of the Cauchy and
                                                         boundary coefficient
                                                         vectors on the mesh.
                                                         So the genuinely new
                                                         derivative burden
                                                         reduces further to a
                                                         single cofinal source
                                                         norm
                                                         `SOURCE-L2-BOUND`
                                                         (E78.136).
  the mu_N -> 0 gate: does the inner-block tower have
  an isolated ground state (Branch A) or does the
  whole low tower collapse together (Branch B)?        -- settled for zeta at
                                                         L=4,6,8, N=6..16:
                                                         nu_0^{(N)} and
                                                         nu_1^{(N)} of
                                                         A_N=H[1:-1,1:-1]
                                                         collapse to 0
                                                         together,
                                                         geometrically; the
                                                         planted falsifier
                                                         instead settles at a
                                                         stable order-one gap.
                                                         BRANCH B. Kills the
                                                         planned rank-one
                                                         quasimode-deflation
                                                         lemma (no isolated
                                                         target eigenvalue);
                                                         does not itself
                                                         close mu_N -> 0
                                                         (E78.137).
  first quasimode attempt on the correct inner-block
  operator: does the naive von Mangoldt vector
  u_N(n) = Lambda(|n|) drive eps_N = ||A_N u_N||/||u_N||
  to 0?                                                -- NO, for both builds,
                                                         at every L in
                                                         {4,6,8}: eps_N grows
                                                         or stabilizes at
                                                         order one (zeta,
                                                         L=4: 0.44 -> 0.40 ->
                                                         1.60 -> 2.23 -> 2.63
                                                         -> 2.72 over
                                                         N=6..16). Diagnosed
                                                         cause: the operator's
                                                         own arithmetic kernel
                                                         weights Lambda(p^k)
                                                         and evaluates it at
                                                         y=k log(p) inside the
                                                         q_value integral
                                                         transform, not as a
                                                         bare sequence indexed
                                                         by mesh position n;
                                                         a viable quasimode
                                                         must be built from
                                                         that same integral
                                                         kernel, not from
                                                         pointwise sampling of
                                                         Lambda(n). Autopsy,
                                                         not closure; mu_N ->
                                                         0 remains OPEN
                                                         (E78.139).
  three kernel-derived quasimode variants (C1/C2/C3:
  log(p)-weighted cosine, unweighted cosine, linear
  taper) built from the same prime-power sum the
  operator's kernel actually evaluates: does any
  variant drive eps_N -> 0, at L in {4,6,8}?          -- NO, for all three
                                                         variants, both
                                                         builds, every L.
                                                         L=4/L=6 show a sharp
                                                         construction-
                                                         breakdown blowup
                                                         after N=8 (likely
                                                         maxn/prime-cutoff
                                                         artifact, unproven).
                                                         One weak signal
                                                         survives at L=8/C3:
                                                         zeta's eps_N stays
                                                         flat near 0.002-0.006
                                                         while planted's grows
                                                         0.020 -> 0.096 over
                                                         N=6..16 -- a genuine
                                                         zeta/plant
                                                         separation, but
                                                         bounded-not-vanishing
                                                         residual does not
                                                         feed the min-max
                                                         argument. Autopsy,
                                                         not closure; mu_N ->
                                                         0 remains OPEN
                                                         (E78.141).
```

### Front C + closure
```text
SHELL-CAUCHY-GROWTH => RDP-SHELL          -- OPEN;
PROLATE + WEIL-TAIL radical pairings       -- OPEN;
E77.8 falsifier-location audit             -- OPEN;
E77.9 non-circularity audit                -- OPEN;
E77.10 final assembly => Omega7            -- OPEN.
```

## Suggested order of attack

1. **Front B first** (SAFE-GAMMA-IDENT / OUTER-LIMIT). This is where the
   discriminant provably lives and where the plant provably breaks; it is the
   most tractable genuine target and it uses only absolute Euler convergence in
   `Re(s)>1` (no wall). E77.6 already supplies the derivative identity and the
   cofinal diagonal; the open work is the `N->infinity` holomorphic-identity
   step and the outer `L->infinity` limit.
2. **Front A2** (interface subclauses c/d/e). Build-neutral, well-localized,
   and the cleanest remaining LP work.
3. **Front A1** (BTG-DIV-L abstract) only via a build-neutral compact-resolvent
   + disk-contraction argument. Treat any build-separating step as a red flag.

## Inherited discipline

```text
English only; documents in the E77 style (numbered sections, ```text``` blocks,
Status block with proved/observed/refuted/open/live labels); companion .py probe
at dps>=60; companion _results.json; every reduced target carries a proved
implication to its predecessor (else it is an archived detector).
Falsifier discipline: test every candidate against zeta AND the standard plant
  planted=("14.134725141734693790","0.30","5.0") in build_mp.
NO-GO walls MW-1..MW-6; kill-tests K1-K5; zero-filter gate E72.16; no ambient
  bordered-inverse norm (P76.061); arithmetic only through Re(s)>1.
Never claim Omega7 or RH proved. Autopsy every wall; name the next finite object.
Phase-size: ~100-150 documents, then close. Do NOT restart a detector spiral.
```
