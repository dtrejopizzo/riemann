# 107.71 -- Paper E1 audit coverage matrix

## 1. Purpose

Paper E1 combines two logically different burdens:

1. the applicability checklist of `107_12` for invoking an existing
   arithmetic Hodge theorem;
2. the terminal identity and equality-case transport of `107_13`.

Several exact finite shadows now exist on both sides, but the whole E1
bridge is still not geometrically closed.  This note records that
boundary explicitly.

## 2. Coverage matrix

| E1 component | Current evidence | Status |
| --- | --- | --- |
| Route A applicability checklist A1--A6 | `107_50` coverage matrix plus `107_51`--`107_55`, `107_80`, `107_81`, `107_82`, `107_83`, `107_91`, and the related Part III audits | partial shadow |
| Route exclusivity and failure logic | `107_67` exact audit of Route A / Route B exclusivity and failure conditions | exact-audited shadow |
| Kernel/equality-case shadow behind `107_11` | `107_48` exact kernel-shadow audit; `107_68` exactness audit against larger kernels; `107_92` exact assembled equality-case gate audit | exact-audited shadow |
| Bilinear pairing-transport shadow | `107_49` exact finite pairing-transport audit | exact-audited shadow |
| Primitive-quotient terminal identity shadow | `107_56` exact finite primitive-quotient quadratic audit | exact-audited shadow |
| Full target-side applicability on realized objects | theorem-level target in `107_12` only | formalized only |
| Full geometric terminal identity on realized objects | theorem-level target in `107_13` only | formalized only |
| RH closure once terminal identity and applicability are proved | logical closure theorem in `107_13`; `107_77` exact-audits one finite closure-readiness shadow, `107_84` exact-audits one assembled E1 bridge shadow, and `107_85` exact-audits one end-to-end pregeometric chain shadow | partial shadow |

## 3. What is genuinely secured

1. The applicability branch is no longer only a checklist:
   `107_50` records item-by-item coverage, and `107_67` exact-audits the
   exclusivity logic that forbids hybrid or analogy-based imports.
2. `107_91` now exact-audits one assembled IV-A governance shadow:
   the current finite assembled Route A state is certified as still
   pre-applicable rather than genuinely applicable, so finite assembly
   alone cannot trigger the E1 bridge.
3. The equality-case side is no longer only a verbal radical warning:
   `107_48` and `107_68` exact-audit both radical compatibility and the
   sharper exactness requirement \(\ker=\mathfrak R_W\).
4. `107_92` now exact-audits one assembled equality-case gate:
   kernel minimality, non-radical survival, and primitive-quotient
   identity coexist as one exact gate and reject enlarged kernels
   immediately.
5. The terminal comparison is no longer only bilinear prose:
   `107_49` exact-audits the finite pairing-transport shadow and
   `107_56` exact-audits the primitive-quotient quadratic shadow.
6. `107_77` now exact-audits one finite closure-readiness shadow:
   applicability, terminal identity, and exact kernel must all be
   present together before RH closure is allowed, and the current phase
   state is certified as still pre-closure.
7. `107_84` now exact-audits one assembled E1 bridge shadow:
   assembled Route A applicability, primitive-quotient terminal
   identity, exact equality case, and closure readiness can coexist in
   one finite bridge state, while removing any one ingredient breaks the
   bridge immediately.
8. `107_85` now exact-audits one end-to-end pregeometric chain shadow:
   the assembled candidate target, assembled Route A applicability,
   terminal identity, exact kernel, and closure logic coexist on one
   finite phase state, and any attempt to bypass the target assembly
   fails immediately.

## 4. What remains unaudited

1. actual Route A applicability on a realized arithmetic surface or
   precise adelic target;
2. the actual geometric terminal identity
   \(-\widehat{\deg}(\overline M_f^{\,2})=\mathcal Q_W(f)\);
3. the real RH closure, which still depends on the two missing
   geometric steps above despite the new finite closure-readiness,
   assembled-bridge, and end-to-end pregeometric-chain gates.

## 5. Status consequence

The correct reading of Paper E1 is:

\[
 \text{several exact finite shadows now exist},
 \qquad
 \text{but the classical/adelic Hodge bridge is still only partial}.
 \]

So later forward construction may not promote E1 beyond `partial`
without a new artifact that directly audits realized applicability or
the realized terminal identity itself.
