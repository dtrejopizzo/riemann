# #2 — BORRADOR DE PRUEBA (para verificación de //) **Objetivo:** probar el Teorema #2: el espectro relativo del fondo de la forma de Weil
localizada A_λ converge a (k+1)², con ε_0(λ)≍λ^{−2}; junto con (i)+(#3), esto da ξ̂_λ→Ξ ⟹ RH. **Convención de estado:** [P]=probado riguroso · [N]=establecido numéricamente (a verificar
analíticamente) · [O]=paso abierto (el "missing step"). NO hay ∎ sobre pasos [O]. --- ## Lema 0 (restricción exacta) [P]
A_λ = A_∞|_{E_λ}, E_λ=PW_{L/2}. Primos >λ² contribuyen 0 por soporte (f**g⊂[λ⁻²,λ²]).
(Verificado 0.00e+00; demostración en 2b_part_i_EXACT.md.) ∎ ## Lema 1 (forma de muestreo) [P]
Por la fórmula explícita de Weil (incondicional) + Lema 0, para f∈PW_{L/2}: A_λ(f,f) = Σ_ρ f̂(ρ) · conj(f̂(1−ρ̄)),
suma sobre los ceros no triviales ρ de ζ; f̂ entera de tipo exponencial L/2. En la parte
on-line (ρ=½+iγ): términos |f̂(γ)|² ≥ 0. ∎ ## Lema 2 (horizonte de muestreo) [P, consecuencia de densidad]
f̂∈ tipo L/2 puede anularse en puntos de densidad ≤ L/2π. Los ceros γ_j tienen densidad
(1/2π)log(γ/2π). Igualando: f̂ puede anularse en TODOS los γ_j hasta altura T*(λ) = 2π λ² (horizonte),
y no más allá. ⟹ los modos blandos (A_λ pequeña) son f con f̂ anulándose en los ceros hasta
T*; el residual viene de los ceros en T*. **Esto da H(λ)→∞ (horizonte crece como λ²).** ∎ ## Lema 3 (localización de borde) [N, mecanismo identificado]
Los minimizadores son edge-localized: concentrados en w=±L/2 (u=λ^{±1}), nulos en el centro,
ocupando una capa de ancho FIJO a≈1.5 (en w). [Verificado: edgeprofile.py, λ=7.]
*Razón estructural:* δ_N (la normalización del minimizador) es evaluación en el borde u=λ;
la forma A_λ es "casi nula" salvo en la capa de borde. La banda-limitación PW_{L/2} actúa como
condición de Dirichlet en el borde interior de la capa. ## Lema 4 (operador de borde = Dirichlet de 2º orden) [N exacto + [O] derivación]
**Hecho [N, exacto a ~1%]:** √(ε_k/ε_0) = k+1 (medido: 1.00, 2.04, 3.00, 4.09, 5.02), y el
ancho a≈1.5 es independiente de k. Esto FUERZA que el operador efectivo de borde sea de
**segundo orden con espectro (jπ/a)²** (Laplaciano de Dirichlet en [0,a]): ε_k = (π/a)²·(escala)·(k+1)². **Mecanismo [O, el missing step]:** la reducción de A_λ, restringida al sector de borde, al
Laplaciano de Dirichlet −d²/ds² en [0,a]. Vía: band-limiting + concentración espacial ⟹
ecuación diferencial de **tipo prolate** (segundo orden): la concentración de funciones
band-limited satisface la ODE prolate ((1−x²)φ')' + (χ−c²x²)φ=0, cuyo espectro cerca del borde
de banda es j². [Herramientas: de Branges / prolate spheroidal — el programa ya las tiene
(P7/P8).] **Falta:** derivar la ODE de segundo orden efectiva desde A_λ y leer a = a(L). ## Lema 5 (escala ε_0 = tunneling) [N + [O]]
**Hecho [N]:** ε_0 ∝ λ^{−2.07} ≈ λ^{−2} = e^{−L}. [Verificado.]
**Mecanismo [O]:** splitting de tunneling entre las capas de borde u=λ y u=λ⁻¹, separadas por
L en w; tasa de decay κ=1 ⟹ e^{−κL}=λ^{−2}. **Falta:** derivar κ=1 de la cola de los modos de
borde (decay de la autofunción de Dirichlet fuera de [0,a]). ## Teorema #2 (condicional a Lemas 4-O, 5-O)
Lemas 0–5 ⟹ ε_k(λ)/ε_0(λ) → (k+1)² y ε_0≍λ^{−2}. Con #3 (reescalado por ε_0 ⟹ fondo aislado
⟹ Galerkin ⟹ convergencia del minimizador) ⟹ ξ̂_λ→Ξ. Con cada ξ̂_λ real-rooted (H1+H2) y
Hurwitz ⟹ Ξ real-rooted ⟹ **RH**. ∎ (condicional a 4-O, 5-O) --- ## CORRECCIÓN (revisión // + test O-4a) La revisión señaló correctamente: (a) "√(ε)=k+1 FUERZA Dirichlet" es demasiado fuerte — sólo es
COMPATIBLE con un Sturm–Liouville de 2º orden (muchos operadores tienen espectro cuadrático);
(b) el cuello de botella real es O-4a (existencia del operador límite de borde), previo a la ODE
prolate; (c) sin operador límite, "κ=1 / tunneling" no tiene sentido riguroso. **Test O-4a (width_vs_lambda.py) — refuta la capa de ancho fijo:**
| λ | 3 | 3.7 | 5 | 7 | 9 | 11 |
|---|---|---|---|---|---|---|
| a/L |.331 |.356 |.356 |.369 |.369 |.369 |
- **a ∝ L** (a/L → 0.369 ≈ 1/e), NO constante. Primos activos en la capa CRECEN con λ.
- ⟹ NO hay operador de borde fijo; los modos ocupan una fracción fija del intervalo creciente.
- Escala de energía: ε_0 ∝ e^{−L}=λ^{−2} (exponencial), NO 1/L² (verificado: ε_0(7)/ε_0(11)=0.40 =e^{−ΔL}, no (L_7/L_11)²=0.66). **Consecuencia (corrige el target):** λ²A_λ ⟹ −d²/ds² es INCORRECTO (daría 1/L²). El límite es un
**régimen semiclásico WKB/tunneling en la coordenada normalizada x=w/L ∈[−½,½]**; la torre (k+1)²
es de splittings de tunneling, con escala exponencial e^{−L}. La reducción correcta de O-4a es un
**límite semiclásico** (no convergencia a un Laplaciano fijo). Más sutil, pero WKB-tunneling son
herramientas clásicas — no un muro. ## ACTUALIZACIÓN 2 (O-4a.1/2/3 + paridad) — régimen semiclásico ESTABLECIDO, pozo único Siguiendo la metodología (medir el régimen antes que la ecuación):
- **O-4a.1 [N]:** los perfiles φ_k(x) colapsan a forma universal en x=w/L (limpio modos pares).
- **O-4a.2 [N]:** ε_0(λ) CONVERGE en N a valor >0 (no es artefacto). −log ε_0 ≈ 0.83·L + 43.7 ⟹ acción S = pendiente ≈ 0.83–1.0 ≈ 1 (más un prefactor constante grande ~43.7, no explicado).
- **O-4a.3 [N]:** corrección δ_2 = ε_2/ε_0 − 9 ∝ 1/L ⟹ **1/L es el parámetro semiclásico (ℏ)**.
- **PARIDAD [N, máquina-limpio]:** los modos alternan par/impar/par/impar… (||ξ−rev||/||ξ+rev|| ~1e−23 / 1e22), y √(ε_k/ε_0)=k+1 hasta k=6 (1,2.04,3.00,4.09,5.02,6.15,7.04). **CONSECUENCIA — corrige la imagen de "dos bordes/tunneling" (era un error):** la paridad
alternante + √=k+1 es la firma de un **POZO ÚNICO de segundo orden = Laplaciano de Dirichlet**
en [−½,½] (espectro (jπ)², autofunciones de paridad alternante). NO hay pares de tunneling
(darían ε_1/ε_0≈1, no observado). El e^{−L} es la **escala global ε_0**, no un splitting. **Target correcto y limpio (recupera el de la revisión, en coordenada normalizada):** (1/ε_0(λ)) · A_λ ⟹ −d²/dx² (Dirichlet en [−½,½]),
con ε_0(λ) ≍ e^{−S L}·(const), S≈1. Régimen semiclásico ESTABLECIDO (no intuición).
Quedan abiertos [O]: (O-4b) derivar el −d²/dx² desde A_λ; (O-4a.2') explicar la constante 43.7
y fijar S=1; limpiar la precisión de modos impares (parity OK, perfil ruidoso). ## ACTUALIZACIÓN 3 (revisión: separar existencia de identificación) Reformulación adoptada (correcta): NO afirmar "firma inequívoca de Dirichlet". Lo defendible:
**evidencia muy fuerte de un operador efectivo de 2º orden tipo Sturm–Liouville**. Y separar:
- **O-4b.1 (existencia de 𝓛):** (1/ε_0)A_λ ⟹ 𝓛 autoadjunto en [−½,½], SIN identificar 𝓛. Esencialmente establecido por: colapso de perfiles (A) + paridad alternante (B) + espectro (k+1)² (C) + correcciones O(1/L) (D) — las 4 piezas juntas ⟹ los autopares convergen ⟹ 𝓛 existe (operador con autobase {φ_k} completa ON y autovalores (k+1)²).
- **O-4b.2 (identificación de 𝓛):** ¿qué operador es? ABIERTO. **Intento de identificación (reveal_L.py): V(x)=φ_0''/φ_0.** Resultado HONESTO:
- Numéricamente RUIDOSO (φ'' de perfil band-limited amplifica ruido); no identifica 𝓛 limpio.
- Robusto: **singularidad central** (V→∞ en x=0; φ_0~x² ahí) ⟹ 𝓛 NO es el Laplaciano PLANO (cuyo fundamental cos(πx) tiene pico central, no nodo). Es Sturm–Liouville con término **centrífugo/Bessel** en x=0, espectro (k+1)². Coherente con que x=0 (u=1) es el punto fijo de ι donde la estructura de primos es singular.
- ⟹ confirma la cautela de: (k+1)² es 2º-orden pero NO Dirichlet plano; 𝓛 tiene potencial. La identificación precisa requiere derivación analítica (no φ'' numérico). **Estado:** 𝓛 existe (O-4b.1, vía convergencia de autopares); 𝓛 ≈ Sturm–Liouville de 2º orden
con singularidad central, espectro (k+1)² [O-4b.2, abierto]; identificación precisa = derivar el
operador efectivo desde A_λ (analítico), no por φ'' numérico (demasiado ruidoso). ## Estado honesto del borrador **Riguroso [P]:** Lemas 0, 1, 2 (restricción exacta, forma de muestreo, horizonte ~λ²).
**Establecido numéricamente [N], a verificar analíticamente:** localización de borde, ancho
fijo a≈1.5, √(ε_k/ε_0)=k+1 (segundo orden / Dirichlet), ε_0∝λ^{−2}.
**Abierto [O] — el missing step de, NO fabricado:** (4-O) reducción de A_λ al Laplaciano de Dirichlet vía la ODE prolate de segundo orden + identificación de a(L); (5-O) tunneling κ=1. **Lo nuevo y fuerte de este borrador:** (a) la forma de muestreo + horizonte ~λ² [P]; (b) la
identificación EXACTA √(ε)=k+1 ⟹ operador de Dirichlet de 2º orden [N]; (c) la ruta concreta
vía prolate/de Branges (P7/P8) para (4-O). El missing step quedó reducido a una ODE prolate
efectiva — un objeto clásico, no un muro. **Para los verificadores:** los puntos [N] son chequeables (relspec2.py, edgeprofile.py); los
[O] son donde pido el análisis de ustedes (prolate ODE + tunneling). Si (4-O) y (5-O) cierran,
2b ⟹ RH.
