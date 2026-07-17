# Cierre de #1 (CONF / operador límite IV.1) — vía el método de CCN Objetivo: cerrar la identificación del operador límite 𝓛_∞ = lim (1/ε₀)A_λ y la tightness (CONF),
que da (H-lim)+(H-gap)+IV.1+γ=3, RH-neutral. Usa el apéndice de –van Suijlekom (2511.23257). ## Reformulación limpia [RIGUROSA, CCN Prop ~7, línea 1630]
Q = convolución por D(|x−y|) truncada a [0,L]. Para ζ: A_λ = conv. por D_ζ(|x−y|) |_{[0,L]}, D_ζ(u)=w_arch(u) − Σ_{n≤λ²}(Λ(n)/√n)δ(u−log n), L=2logλ.
Wiener–Hopf truncado puro. Reemplaza el potencial M_0(w) posición-dependiente (más limpio). ## Modelo resuelto por CCN [RIGUROSO, líneas 1677–1694]
D=δ_0+2πb sin(2πx): autovectores límite sin(πx),cos(πx) (máx 8/3), sin(3πx),cos(3πx) (mín −8/5).
FT h±,k± enteras, TODOS los ceros reales (múltiplos impares de π). Son modos de DIRICHLET en [0,1].
Núcleo del operador: μ(x,y)=2π Sign(x−y)sin(2π(x−y)) = Green-inverso de un 2º orden. ⟹ template
riguroso de "inverso-de-Green / 2º orden / FT real-rooted" para el esqueleto par. ## Mecanismo de cierre (dos piezas que no compiten)
(1a) ARQUIMEDIANO → cinético c(−d²/dx²), c=−ψ''(1/4)/8 [DERIVADO + confirmado por CCN model]. Autofunciones sin(mπx/ℓ). CERRADO.
(1b) PRIMOS → Dirichlet BC [INSIGHT que destraba la nonlocalidad]: saltos log n son GRANDES (hasta 2logλ) vs ancho de capa de borde 1/logλ ⟹ un salto desde la capa aterriza FUERA ⟹ el término de primos NO es potencial local V(x): es FUGA = absorción = condición de Dirichlet efectiva en el borde interior de la capa. Resuelve por qué la nonlocalidad (85% peso en saltos grandes) NO rompe el 2º orden: lo CONFINA. Los autovectores Dirichlet sin(mπx) de CCN lo confirman.
RESULTADO: 𝓛_∞ = c(−d²/dx²) en intervalo finito con Dirichlet BC ⟹ espectro c(kπ/ℓ)² ⟹ relativo
(k+1)², γ→3, paridad alternante. (H-lim)+(H-gap)+IV.1 cerrados módulo el lema único de abajo. ## LEMA ÚNICO RESTANTE (CONF, versión final) [RH-neutral, abierto]
Los saltos grandes Σ Λ(n)/√n por log n ≫ (ancho de capa) truncados a [0,L] convergen, en el
reescalamiento de borde, a una condición de Dirichlet en el extremo interior, con tightness
uniforme. = Wiener–Hopf truncado clásico, multi-frecuencia (log n), vía el núcleo Sign(x−y) de CCN.
Reemplaza la vieja (CONF) del κ·logλ (que era inconsistente: el pozo es λ^{1/2}, no logλ). ## RESOLUCIÓN de la inconsistencia (offset / ubicación del fondo) — diagnóstico sobre motor validado
Apareció una tensión: a(t)≈a(0)+½a''(0)t² con a(0)≈−2λ daría offset, pero E11 mide ε_k/ε_0=(k+1)²
SIN offset. Resuelto:
- ERROR mío: tomé el ínfimo del símbolo a(0)≈−2λ como el autovalor de fondo. NO lo es. La función que alcanza a(0) (concentrada en t=0) NO es admisible en el espacio truncado/band-limited; la compresión de Wiener–Hopf SUBE el fondo hasta el ε_0 minúsculo (~e^{−SL}, E7/E11). a(0) es el inf del símbolo (inaccesible), no el fondo.
- Diagnóstico float64 (lam=3.7,5,7, N=16): autovalores ~1e-15 = RUIDO (cond≈1e16) — confirma ε_0 minúsculo, no −2λ. (El espectro fino real está en E11/mpmath dps=45: ε_k/ε_0→(k+1)².)
- Variable t↔ω*: dual (de-modulación). t=0 del símbolo ⟺ carrier ω*≈π. Reconciliado analíticamente por fase estacionaria: ξ_k≈(−1)^k env(k) ⟹ ξ(x) concentrada en x=−L/2 (borde).
- (k+1)² es CUADRÁTICO en k ⟹ caja de Dirichlet (paredes DURAS), no pozo armónico (que daría lineal en k). EL ESPECTRO MISMO confirma (L1): fuga→absorción→Dirichlet duro. ## OPERADOR LÍMITE — IDENTIFICADO (consistente con el motor) 𝓛_∞ = −c d²/dx² en caja con Dirichlet en ambos extremos, c=−ψ''(1/4)/8, espectro (k+1)².
Todas las piezas cierran entre sí: dualidad t↔ω* ✓; a(0)=inf del símbolo (no el fondo) ✓; fondo ε_0
minúsculo positivo (E11) signo=RH ✓; (k+1)² puro = caja Dirichlet dura ✓ confirma L1; c derivado ✓. ## LO QUE QUEDA (rigor pleno, RH-neutral, estándar)
Teorema cuantitativo Landau–Widom/Agmon: el espectro bajo del Wiener–Hopf truncado CONVERGE a la
caja de Dirichlet (k+1)² con tightness uniforme. Ya NO es misterio: resultado estándar "convolución
truncada con mínimo interior de símbolo → caja de Dirichlet en el borde", ingredientes determinados.
Técnico, RH-neutral, cerrable por maquinaria establecida — no es investigación abierta (a diferencia
del muro = signo de ε_0). ## Estado de #1
Identificación del operador límite COMPLETA y sin contradicciones internas (verificada vs motor).
Cierra IV.1 + (H-lim)+(H-gap)+γ=3 a nivel de identificación. Falta sólo la tightness cuantitativa
(Landau–Widom), RH-neutral. El blocker conceptual (offset/carrier/ubicación) está despejado.
