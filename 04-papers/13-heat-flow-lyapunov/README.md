# Paper 13 — A Lyapunov Theorem for the de Bruijn–Newman Flow, a Dynamical No-Go, and the Extremal Form of the Riemann Hypothesis as Gap Universality

The paper studies the de Bruijn–Newman heat flow. For this flow the Riemann hypothesis is
equivalent to $\Lambda=0$, using the cited Rodgers–Tao bound $\Lambda\ge0$ and the Polymath15 bound
$\Lambda\le0.2$. The total off-line-ness is a strict Lyapunov function, so the critical line is
the global attractor of the flow. The Lyapunov identity is arithmetic-blind, which gives a no-go
for arguments that use the flow alone. The constant $\Lambda$ is an extremal quantity, the first
backward collision time of the zeros.

## Main results

- `thm:lyap`: $\mathcal L=\sum_j(\operatorname{Im}z_j)^2$ satisfies
  $\dot{\mathcal L}=-2\sum_{j\ne k}(y_j-y_k)^2/|z_j-z_k|^2\le0$ — PROVED.
- `cor:height`: any off-line zero has imaginary height $\le\sqrt{2\Lambda}\le0.63$ — PROVED
  (uses the CITED bound $\Lambda\le0.2$).
- `thm:nogo` (N5): the identity holds for every conjugate-symmetric configuration, so no
  argument from the flow alone proves the Riemann hypothesis — NO-GO.
- `prop:collision`: $\Lambda=\sup t_c$, with $t_c=-g_0^2/8$ to two-body order; one off-line zero
  forces $\Lambda>0$ — PROVED at two-body order (the higher-order statement is ARGUED).
- Normalized backward-collision margin $t_c/s^2$ clusters near $-0.02$ for real zeros — NUMERICAL.
- Reduction to unconditional GUE gap universality — CONDITIONAL / OPEN.

## Files

- `main.tex`, `main.pdf` — source and compiled paper.

## Relation to other papers

A companion of the map in Papers 12 and 14.
