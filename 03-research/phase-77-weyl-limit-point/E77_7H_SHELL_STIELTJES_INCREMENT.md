# E77.7h - Shell Stieltjes-increment identity

**Run:** 2026-07-18.

## 1. Purpose

E77.7h reduced the cofinal cyclic-tail problem to shell control of

```text
Sigma_{R,M}(eta)
= <h_{R,M},(K_{R,M}-mu_R+eta)^(-1)h_{R,M}>.
```

This note proves the exact finite shell identity for
`Sigma_{R,M+2}-Sigma_{R,M}` and measures whether the observed zeta
stability is a real shell-smallness effect or a cancellation artifact.

## 2. Exact shell Schur identity

At fixed `R`, embed the `M` complement into the `M+2` complement and write

```text
K_{M+2}-z =
[[A, C],
 [C^*, D]],

h_{M+2}=(h,g),
z=mu_R-eta.
```

Let

```text
x=A^{-1}h,
S=D-C^*A^{-1}C,
r=g-C^*x.
```

Then block inversion gives the exact identity

```text
Sigma_{M+2}(eta)-Sigma_M(eta)
= <r,S^{-1}r>.                                (S-1)
```

This is the right form for P76.061: the new shell source is paired and
shorted before any estimate is taken.  No ambient bordered inverse norm is
used.

If `eta` also changes from `eta_M` to `eta_{M+2}`, the total finite change is

```text
Sigma_{M+2}(eta_{M+2})-Sigma_M(eta_M)
 =
 [Sigma_{M+2}(eta_{M+2})-Sigma_M(eta_{M+2})]
 +[Sigma_M(eta_{M+2})-Sigma_M(eta_M)].        (S-2)
```

The first bracket is `(S-1)`.  The second is the `eta`-drift term.

## 3. Proof-facing target

The admissible next object is:

```text
SHELL-RESIDUAL-SUM:
For cofinal M(R), eta_R, prove

sum_{M>=M(R)}
 <r_{R,M}(eta_R), S_{R,M}(eta_R)^(-1) r_{R,M}(eta_R)>
 = o(eta_R),

with the eta-drift term in (S-2) also o(eta_R).
```

Then

```text
SHELL-RESIDUAL-SUM
=> SHELL-STIELTJES-INCREMENT
=> COFINAL-STIELTJES-TIGHTNESS
=> COFINAL-CYCLIC-TAIL
=> POSTERIORI-POLE-CAPTURE
=> CYCLIC-POLE-CAPTURE
=> KRYLOV-WINDOW-RESOLUTION
=> LANCZOS-RESOLUTION-ENVELOPE
=> CYCLIC-WINDOW-MASS
=> WFE-CYCLIC-TAIL
=> BRACKETED-LOW-MODE-BTG
=> BTG-DIV-L
=> corrected LP.                              (S-3)
```

This keeps the route as a convergence/identity theorem and does not invoke
Weil positivity, a zero filter, a pseudoinverse, or a raw inverse norm.

## 4. Probe

Companion:

```text
E77_7h_shell_stieltjes_increment_probe.py
E77_7h_shell_stieltjes_increment_results.json
```

Command:

```bash
python3 E77_7h_shell_stieltjes_increment_probe.py \
  --lambda 6 --max-modes 20 --pairs 16:18,18:20 \
  --ref-modes 14 --dps 60
```

The probe builds the `M=20` matrix once, embeds the smaller complements,
and verifies `(S-1)` directly against the full Stieltjes difference.

### Zeta

| shell | shell/eta | eta-drift/eta | total/eta | log10 defect |
|---:|---:|---:|---:|---:|
| 16 -> 18 | 9.0218e-5 | -4.3860e-8 | 9.0174e-5 | -73.75 |
| 18 -> 20 | 1.4807e-8 | -2.3165e-11 | 1.4784e-8 | -72.93 |

The zeta stability is not a large cancellation between shell and eta drift:
the shell increment itself collapses by about four orders of magnitude from
`16->18` to `18->20`.  The shell residual norms are:

```text
16 -> 18: 1.31e-30;
18 -> 20: 3.11e-33.
```

### Planted build

| shell | shell/eta | eta-drift/eta | total/eta | log10 defect |
|---:|---:|---:|---:|---:|
| 16 -> 18 | 0.229221 | -0.001705 | 0.227516 | -63.22 |
| 18 -> 20 | 0.187423 | -0.001716 | 0.185707 | -inf |

The plant also satisfies the algebraic identity, but does not show the same
short-window shell decay.  This is acceptable for the front-A audit: the
identity is neutral, while the cofinal quantitative behavior remains a real
proof obligation.

## 5. Autopsy

`SHELL-STIELTJES-INCREMENT` is not closed as an infinite estimate.

What is now proved is the exact shell formula `(S-1)`.  What remains is a
summability theorem for the shorted shell residual:

```text
r_{R,M}=g_{R,M}-C_{R,M}^*A_{R,M}^{-1}h_{R,M}.
```

The measured zeta decay suggests that this is the correct object.  The
proof cannot use `||A^{-1}||` or `||S^{-1}||` separately; that would re-enter
the inverse-gap/ambient norm wall.  The estimate must keep the scalar
pairing `<r,S^{-1}r>` intact.

The next strictly smaller live object is therefore:

```text
SHORTED-SHELL-ENERGY:
prove a direct bound for the scalar shell energy
<r_{R,M},S_{R,M}^{-1}r_{R,M}>,
summable over M in the cofinal regime.
```

Then

```text
SHORTED-SHELL-ENERGY
=> SHELL-RESIDUAL-SUM
=> ... => BTG-DIV-L => corrected LP.
```

## 6. Status

```text
proved:    exact finite shell Stieltjes identity (S-1);
proved:    SHELL-RESIDUAL-SUM implies the chain to BTG-DIV-L (S-3);
observed:  zeta shell/eta drops from 9.0e-5 to 1.5e-8;
observed:  zeta eta-drift is smaller than the shell increment;
observed:  plant satisfies the identity but not short-window shell decay;
open:      summable shorted-shell energy estimate;
open:      SHELL-STIELTJES-INCREMENT, COFINAL-CYCLIC-TAIL,
           CYCLIC-POLE-CAPTURE, KRYLOV-WINDOW-RESOLUTION,
           CYCLIC-WINDOW-MASS, WFE-CYCLIC-TAIL, RITZ-BRACKET,
           BRACKETED-LOW-MODE-BTG, BTG-DIV-L, corrected LP;
live:      SHORTED-SHELL-ENERGY.
```

