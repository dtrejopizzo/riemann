# Phase 60 — HITO: primer spectral triple CCM validado del programa **Fecha:** 2026-06-16 · **Código:** `experiments/E4_ccm_faithful.py` (corre en venv, reproducible). ## Qué se logró Implementación **fiel** del spectral triple de –– ("Zeta Spectral
Triples", arXiv:2511.22755), siguiendo Thm 1.1 + Prop 3.2 + eq 3.13–3.16. Es la primera
correcta del programa: todas las versiones previas (`nemotron/02-foundations/engine/connes_hx_*.py`,
v2–v7, final) calculaban la von Mangoldt y **la descartaban** (`QW=Q_arch*0.5`), produciendo la
escalera pelada de D_log, no los ceros. ## Validación (gate duro, falsable) Autovalores = raíces reales de f(s)=Σ_k ξ_k/(s−2πk/L), ξ = autovector del menor autovalor de
la forma de Weil QW_λ^N. Contra ceros de ζ de alta precisión (mpmath): | λ (primos ≤λ²) | N | cero 1 (14.1347) | cero 2 | cero 3 | cero 4 | cero 5 |
|---|---|---|---|---|---|---|
| 3.7 (p≤13) | 20 | 3.6e-15 | 0 | 0 | 3.2e-14 | 1.3e-13 |
| 5.0 (p≤25) | 20 | 1.8e-15 | 0 | 3.6e-15 | (miss) | 2.9e-12 |
| 7.0 (p≤49) | 20 | 1.8e-15 | 0 | 3.2e-14 | 1.1e-11 | — | Precisión de máquina (float64) para los primeros ~6 ceros con **primos ≤13**. Reproduce la
afirmación central del paper. Los "miss" son huecos saltados por el buscador de raíces (dos
ceros en un hueco del retículo), no fallo de fondo. A N grande (80) float64 se degrada
(QW mal condicionada); el régimen N→∞ del paper requiere alta precisión (mpmath) — pendiente. ## Por qué importa para RH (honesto) - El operador es **auto-adjunto por construcción** ⇒ espectro real automáticamente. Evita el muro del signo (MW-4): no hay que probar positividad de ninguna forma.
- Cada nivel finito (λ,N) da ceros reales del aproximante ξ̂. **RH ⟺ la convergencia N,λ→∞ preserva la realidad de las raíces** (Hurwitz). Esa convergencia es el ÚNICO gap — y es un problema de teoría de aproximación, NO de positividad. mismo no lo tiene (Secciones 7–8 del paper: "missing steps"). Esto **no prueba RH**. Da, por primera vez en el programa, un instrumento validado para
atacar el gap real. ## Lo genuinamente nuevo que ahora podemos hacer (que no) Tenemos un violador explícito de RH (L_DH, ζ_δ). El mecanismo a probar:
> Si una función tiene un cero OFF-line (complejo), la auto-adjuntez fuerza autovalores
> reales que NO pueden converger al cero complejo ⇒ la convergencia DEBE romperse. ## Convergencia alta precision (E4hp_convergence.py, mpmath dps=40) **Eslabon 2a (N->inf, λ=3.7 fijo):** convergencia geometrica rapida hasta piso metodologico.
| N | 6 | 8 | 10 | 14 | 18 |
|---|---|---|---|---|---|
| \|err1\| | 4.5e-12 | 3.7e-15 | 1.9e-17 | 5.3e-19 | 8.1e-19 |
Evidencia empirica solida de que el limite N->inf converge (Eslabon 2a). El plateau ~5e-19
es piso de tolerancia (quad + root-finder), NO el limite-λ real — no sobreinterpretar. **Eslabon 2b (λ->inf):** NO medido. El diseno a N=14 fijo esta confundido (al subir λ el
reticulo d_k=2πk/L se densifica y N=14 sub-resuelve). La tasa de 2b queda PENDIENTE:
rediseno con N escalando con λ + dps mayor. (Honesto: no afirmar una tasa-λ con estos datos.) ## Sutileza de diseno para E5 (importante) En CCM los ceros son OUTPUT, no input: no hay perilla "δ off-line". El violador correcto es
**L_DH** (Davenport-Heilbronn): ecuacion funcional (-> factor arquimediano) + coeficientes de
Dirichlet computables, ceros OFF-line. Construir QW_LDH y medir si la convergencia se rompe:
> L_DH tiene ceros complejos; el operador CCM es auto-adjunto -> espectro real SIEMPRE ->
> no puede converger a ceros complejos -> la convergencia DEBE degradarse. Contraste vs el
> baseline ζ de arriba = testigo numerico de "convergencia <=> RH".
No requiere 1e-55: basta que L_DH se estanque en error >> piso de ζ.
