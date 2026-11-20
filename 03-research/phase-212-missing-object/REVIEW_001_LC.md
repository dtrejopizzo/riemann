# REVIEW_001_LC — Revisión hostil de ROUND_001_L y ROUND_001_C

Alcance: lectura línea a línea de las dos memos, derivación propia de cada paso, cotejo de las citas
contra `../phase-211-sign-sandbox/` (STATEMENT_001, POWER_CONE_001, POWER_BRIDGE_002,
POWER_GRAM_SLICES_OBSTRUCTION §§17.2–17.5, 18.1–18.4, 18.7; POWER_GLOBAL_ROUTE_REVIEW «Comparador
asinh», «Comparaciones primitivas», «Comparación hiperbólica pequeña», «Cierre…», «Filtro general
reutilizable», «Extensión factorial…», «Escalas libres de cuadrados…»; POWER_HYPERBOLIC_MODEL_GRAM §4),
búsqueda en el índice de rutas, el grid y `RULES_AVOID.md`, y caza de contraejemplos. Ningún archivo
existente fue modificado. Etiquetas: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMÉRICO.

Resumen de veredictos.

| Memo | Veredicto | Error matemático en el núcleo | Corrección necesaria |
|---|---|---|---|
| ROUND_001_L | ACCEPT with corrections | ninguno hallado | etiquetas de §6.3(a) y §9; alcance real del corolario asinh; no efectividad; redacción de sandbox |
| ROUND_001_C | ACCEPT with corrections | ninguno en Lema 1, (R0), (R1), (R2) nodos | laguna en la versión de modos; tres sobre-enunciados; novedad menor que la declarada |

---

## Parte I — ROUND_001_L

### I.1 Verificación paso a paso (derivaciones propias)

- **F2.** H par y real en ℝ ⟹ H(iτ) real ⟹ H′(iτ) ∈ iℝ ⟹ Re M(iτ) = 0 fuera de los polos. Correcto.
- **F4.** Rehecha: para Re z ≥ 1, |k+z| ≥ k+1 da |ψ(z)+γ| ≤ (π²/6)|z−1|; con Re a ≥ 2,
  |1/a|+|1/(a−1)| ≤ 3/2. (b) correcto; (a) correcto.
- **C1.** Normalización comprobada: Re 1/(σ+i(τ−s)) = σ/(σ²+(τ−s)²), integral π; un átomo de masa m en
  τ da m/(u−iτ), es decir residuo = masa. Coherente con el Paso 2 (masa r_k) y con 2u/(u²+τ²) por par.
- **C2.** Teorema de Pick en Π, nodos arbitrarios de Π (los reales incluidos). La identidad de
  transporte al disco fue recomputada:
  1 − S(u)conj S(v) = 2(F(u)+conj F(v))/[(F(u)+1)conj(F(v)+1)] y análoga para z; el cociente es el
  escrito. Re w_i ≥ 0 garantiza w_i ≠ −1. El caso S unimodular constante (F constante imaginaria) no
  rompe nada. Correcto.
- **C3 y Lema 1.2.** Condición de Blaschke de Π para ceros de una función de tipo acotado:
  Σ Re u_n/(1+|u_n|²) < ∞. Para la escalera, Σ (31.5+n)/(1+(31.5+n)²) = ∞; trasladada al semiplano
  Re u > 3/2 sigue divergiendo. Correcto. La clase en juego es la correcta: F y M0 son real-positivas
  (luego de tipo acotado), y M es de tipo acotado en Re u > 3/2 porque M = [M/(u+1)]/[1/(u+1)] con
  ambos factores acotados (F4(b)). No se necesita que M sea real-positiva para la unicidad: bien.
- **Lema 1.3.** Montel + C2; el límite S cumple S(x_j) ≠ 1. Correcto. Caso no numerable: correcto.
- **Teorema 2.1.** Correcto (requiere sólo que M sea finita en X; lo es, F1).
- **Teorema 3.1, Paso 1.** G = M − εM0 − F es de tipo acotado en Re u > 3/2 y se anula en un conjunto
  que viola Blaschke ⟹ G ≡ 0 allí ⟹ identidad meromorfa en Π. Correcto. **Paso 2.** Inversión de
  Stieltjes con F2: fuera de los polos la densidad límite es 0; en un polo
  (1/π)∫φ·r_kσ/(σ²+(τ−τ_k)²)dτ → r_kφ(τ_k). Correcto; c_M = 0 por F4(a). **Paso 3.** Unicidad de la
  terna de Herglotz ⟹ c_0 = c_F = 0, εμ_0 ≤ μ_M. Correcto.
- **Corolario 4.1.** Contrarrecíproco exacto del Teorema 3.1; lógicamente incondicional. Correcto.
- **Proposición 4.2.** Correcta; CONDITIONAL bien puesta.
- **§6.2.** REP de 211/HYP §4 dice exactamente M_a(u)/u = ½Tr(H_a+u²/4)^{-1}, con Tr R_x ≤ 1/(2a);
  de ahí M_a = Σ_k 2u/(u²+ω_k²), ω_k = 2√λ_k. Correcto.
- **§6.3.** El Gram real de los resolventes (u − 2i√H)^{-1} es Σ_k[1/((u−iω_k)(v+iω_k)) + c.c.], que es
  el Lema 1.1 para μ_a; U_Phi = Σ_k G(ω_k)·(proyector k). La condición «U_Phi = 0» y «todo iω_k es polo
  de M» coinciden. Correcto. **NUMÉRICO** (comprobación puntual, mpmath 30 dígitos): primer cero en ν
  de K_{iν}(2π) en ν₁ = 9.768770…, ω₁ = 19.53754… ∈ [17, 41/2], coherente con la localización de 211.
- **§6.4.** sinh aplica {Re w > 0, |Im w| < π/2} biyectivamente sobre Π; M_0 = ½asinh(u/4π) es
  real-positiva, c_0 = 0, y en el borde Re M_0(iτ) = ½arccosh(|τ|/4π) > 0 para |τ| > 4π: densidad
  (1/2π)arccosh. (E2) se cumple. Correcto.
- **§7.1.** Complemento de Schur: K − g⊗g/K(w,w) ⪰ 0 si K ⪰ 0. Correcto.
- **Circularidad.** No hay: ni el Teorema 3.1 ni el Cor. 4.1 suponen el signo de K_M. Lo que sí ocurre
  (y la memo lo dice) es que la hipótesis del Teorema 3.1 contiene ese signo.

### I.2 Caza de contraejemplos (NUMÉRICO, juguete)

Juguete: M_toy(u) = π coth(πu) − 1/u = Σ_{k≥1} 2u/(u²+k²) (medida de borde atómica, masas 1 en ±k),
nodos 1.5 + n, n < N, mínimo autovalor de K_{M_toy − εM0}, aritmética de 150–260 dígitos.

| comparador M0 | ε | N = 4 | 8 | 16 | 32 | 48 |
|---|---|---|---|---|---|---|
| 1/(u+1) (borde continuo) | 0.9 | 2.6e−5 | 1.9e−11 | −2.8e−16 | −1.0e−15 | −1.2e−15 |
| 1/(u+1) | 0.3 | 3.1e−5 | 2.5e−11 | 1.5e−23 | −6.6e−30 | −2.3e−29 |
| 2u/(u²+1.5²) (átomo ajeno) | 0.5 | 2.9e−5 | 2.5e−11 | 1.6e−23 | −2.0e−36 | −2.3e−35 |
| u (término lineal) | 0.05 | 3.0e−5 | 2.1e−11 | −2.3e−9 | −2.3e−4 | −1.1e−2 |
| 2u/(u²+1) (átomo propio), tamaños 3–24 | 0.5 | positivo en todos | | | | |
| 2u/(u²+1) (átomo propio), tamaños 3–24 | 1.2 | negativo desde N = 6 (≈ −7e−6) | | | | |
| ninguno (control) | — | 3.2e−5 | 2.6e−11 | 1.8e−23 | 7.0e−48 | 2.5e−72 |

No se halló contraejemplo; todos los casos se comportan como predicen (E1)–(E4) y la Prop. 4.2. Dato
que la memo no dice: la violación aparece tarde y con tamaño 10⁻¹⁶–10⁻³⁶ (con ε = 0.05 no aparece
hasta N = 24). El Cor. 4.1 **no es efectivo**: no sirve como filtro numérico en doble precisión ni da
el tamaño del bloque.

### I.3 Errores y lagunas (con ubicación)

L-1. **§6.3, punto (a) — etiqueta inflada.** «Vale para todo a > 0 y para las variantes Robin y las
sumas w·b·M_{a,β}(bu)» figura bajo un encabezado PROVED sin que la memo demuestre que cada variante
es real-positiva en Π con medida de borde atómica (para Robin hace falta la REP con operador positivo
de resolvente de traza; para las sumas, la convergencia en el sentido de C1). Etiqueta correcta:
**ARGUED** para Robin y sumas; **PROVED** sólo para Dirichlet y todo a > 0 (REP vale para todo a).

L-2. **§9, primer punto, y «Qué se probó» 7 — dependencia de certificado omitida.** «Ningún modelo
exterior… con un átomo fuera de los polos de M (hiperbólico a = 2π) sirve, para ningún ε» es PROVED
sólo relativo al certificado de intervalos de 211 (G < −10⁻⁸ en [17, 41/2]). La memo lo reconoce en
§6.3 pero lo omite en §9. Etiqueta correcta: **PROVED asistido (rel. certificado de 211, CITED)**.

L-3. **Cotejo (2) y §6.4 — alcance real de la novedad del corolario asinh.** Para ε > 1 la exclusión
es trivial y no necesita la memo: M(u) − (ε/2)asinh(u/4π) ~ ((1−ε)/2)·log u → −∞, de modo que ya un
bloque 1×1 de la escalera es negativo. Para ε = 1 ya estaba en el corpus (certificado de jets).
El contenido nuevo es exactamente **0 < ε < 1**. Cotejado: `RULES_AVOID.md` B4, índice README
(entradas «comparador asinh») y grid sólo registran ε = 1; el «Filtro general reutilizable» no aplica
(D no es o(1/u)); la no positividad con ε = 1 no implica la de ε < 1. La novedad se sostiene en ese
rango.

L-4. **Cor. 4.1 — falta declarar la no efectividad** (I.2) y que, como herramienta, sólo informa en
la rama en que K_M es PSD (en la otra rama el enunciado es cierto por razones triviales:
K_M − εK_{M0} ⪯ K_M). Es lógicamente incondicional; no es información independiente del objetivo.
No es un error, es alcance que debe constar en el registro.

L-5. **Resumen de §4, segundo punto.** «Existe uno si y sólo si M es real-positiva en Π y tiene al
menos un polo en el eje»: la segunda cláusula es redundante. Si M es real-positiva, c_M = 0 y
M ≢ 0 obligan μ_M ≠ 0. Enunciado correcto: existe un comparador real-positivo no nulo admisible
⟺ M es real-positiva en Π. Menor.

L-6. **Lema 1.2, frase final** («la condición es también necesaria»). (i)/(ii) no son necesarias:
un X que sólo se acumula en 0 con Σu = ∞ también viola Blaschke en Π y da unicidad del interpolante
F (ambas funciones son de tipo acotado en Π). Lo único que falta en ese caso es identificar M con F
(§7.5). La frase debe decir: la condición exacta para la unicidad del interpolante es
Σ_{u∈X} u/(1+u²) = ∞. Menor.

L-7. **Redacción de sandbox (Teorema 3.1 punto 1, Cor. 2.2, F3).** El punto 1 y el Cor. 2.2 son
reformulaciones del objetivo en términos de la localización de los polos de M; la regla 1 del brief
prohíbe razonar por reducción de ese tipo y B3 prohíbe registrar reformulaciones como resultado. La
demostración no lo necesita: basta «M − εM0 se extiende a una real-positiva» y la medida de borde.
El Cor. 2.2 no debe anotarse en el índice ni en el grid; en el registro, la conclusión se enuncia por
la medida de borde, no por la localización de polos.

L-8. **§7.4.** Depende del lema «Comparaciones primitivas» de 211 (CITED); cotejado: el lema pide D
impar y real-analítica en todo ℝ y todos los bloques primitivos de un intervalo abierto de (c,∞),
c = ½, y concluye PSD completa. La memo lo usa dentro de ese alcance (M0 con hueco de la medida
alrededor de 0). Correcto; etiqueta CITED + PROVED adecuada.

No se encontró error en el Teorema 2.1, el Teorema 3.1 ni el Cor. 4.1. El reparto
incondicional/condicional es correcto con la precisión L-4 y la corrección L-5.

### I.4 Enunciado corregido, etiqueta y alcance

**Lema de rigidez (PROVED relativo a C1–C3, CITED).** Sea X ⊂ (0,∞) con punto de acumulación en
(0,∞) o con Σ_{u∈X,u≥2} 1/u = ∞ (p. ej. la escalera 31.5 + n), ε > 0, y M0 real-positiva en Π, real
en (0,∞), con datos de Herglotz (c_0, μ_0). Si K_M − εK_{M0} es PSD en todo subconjunto finito de X,
entonces M − εM0 se extiende a una función real-positiva en Π, la medida de borde de M es
Σ_k r_k(δ_{τ_k}+δ_{−τ_k}), c_0 = 0 y εμ_0 ≤ μ_M. Contrarrecíproco (lógicamente incondicional, no
efectivo): si c_0 > 0, o μ_0 tiene parte continua, o un átomo fuera de {±τ_k}, o μ_0({τ_k}) > r_k/ε,
existe un bloque finito de X con energía negativa para K_M − εK_{M0}; no se da ni el tamaño ni el
vector.

**Corolario asinh (PROVED rel. C1–C3).** K_M − ε·K_{½asinh(u/4π)} no es PSD en la escalera para
ningún ε > 0. Contenido nuevo: 0 < ε < 1 (ε = 1 ya certificado en 211; ε > 1 trivial por bloques 1×1).

**Instancia hiperbólica (PROVED asistido, rel. certificado de 211).** Para a = 2π Dirichlet, la
condición necesaria del lema coincide con U_Phi = 0; el cierre de 211 es la verificación de un átomo
ajeno. Para otros a > 0 Dirichlet el lema da la condición necesaria (PROVED) pero no la exclusión sin
un certificado por átomo. Robin y sumas: ARGUED.

Alcance: sólo comparadores real-positivos en el mismo portador (o tras congruencia común), dominación
en todos los tamaños. No cubre núcleos PSD generales, congruencias no comunes, compensaciones
conjuntas, bloques de tamaño acotado, ventana fija ni la escalera discreta primitiva (OPEN, §7.4).
No es paso de signo.

### I.5 Qué puede anotarse en el índice y en el grid

Puede anotarse, con este texto:

> **Fase 212, comparadores real-positivos en la escalera de potencias — NO-GO con clase, PROVED
> relativo a tres teoremas clásicos citados (representación integral de funciones real-positivas,
> interpolación de Pick, condición de Blaschke).** `ROUND_001_L.md`, Teorema 3.1 y Cor. 4.1; revisión
> `REVIEW_001_LC.md`. Clase: núcleos [M0(u)+M0(v)]/(u+v) con M0 real-positiva en Re u > 0 y real en
> (0,∞), comparados con el núcleo de la escalera en el mismo portador o tras congruencia común, con
> dominación K_M − εK_{M0} ⪰ 0 en todos los tamaños sobre la escalera 31.5 + n (o cualquier conjunto
> de nodos con Σ1/u = ∞ o con acumulación interior). Conclusión: M0 no tiene término lineal y su
> medida de borde está dominada por (1/ε) veces la de M, que bajo esa hipótesis es puramente atómica;
> quedan excluidos, para el ε correspondiente, todo término lineal, toda parte continua, todo átomo
> ajeno y toda masa mayor que r_k/ε. Consecuencia nueva: ½asinh(u/4π) queda excluido para todo
> 0 < ε < 1 sin certificado (ε = 1 ya registrado; ε > 1 trivial). La comparación hiperbólica pequeña
> a = 2π de 211 es una instancia (misma condición necesaria; su cierre sigue dependiendo del
> certificado de intervalos). Exclusión no efectiva: no da bloque ni vector. No cubre núcleos PSD
> generales, congruencias no comunes, compensaciones conjuntas, tamaños acotados, ventana fija ni la
> escalera primitiva discreta. No aporta signo.

No puede anotarse: (a) el Cor. 2.2 ni el punto 1 del Teorema 3.1 como resultado (reformulación, B3;
y redacción fuera del sandbox); (b) «la medida de borde de M es puramente atómica» sin la hipótesis;
(c) las variantes Robin y sumas como PROVED; (d) la exclusión de a = 2π como «sin certificado»;
(e) cualquier lectura de la memo como restricción sobre espacios ℋ que no provengan de un comparador
de esta clase (§7.1 de la memo prueba que fuera de la clase no hay restricción).

---

## Parte II — ROUND_001_C

### II.1 Cotejo de (M1)–(M5) contra la fase 211

- **(M1)** GRAM §18.1: (GRAPH) y (A-GRAPH) coinciden con lo citado (T, Lg, C, F, G). Correcto.
- **(M2)** GRAM §18.2: el texto fija una lista finita de κ_i, 0 < a < π·min(1, min κ_i), 0 < γ < 2a, y
  prueba continuidad B_a² → H_γ × H_γ de P ↦ (F,G) y de la forma de (A-GRAPH), «sin presuponer PSD».
  Para escalas enteras la condición es 0 < a < π, como dice la memo. La constante depende de (a,γ).
  Rehecho aquí el único ingrediente remitido a §17.7: ‖F(m²·)‖_{H_γ} ≤ e^{−γ(m²−1)/2}‖F‖_{H_γ}, luego C
  es acotado en H_γ para todo γ > 0. (M2) dice exactamente lo que la memo usa. Correcto.
- **(M3)** GLOBAL, «Escalas libres de cuadrados»: holomorfía de z ↦ P_z en Re z > a/π con valores en
  B_a² y cota C_δ(1+|z|)^{13/4} en Re z ≥ δ: literal. La afirmación sobre E_z es añadida por la memo;
  verificada: sup_{t≥1} e^{at}|∂_t^j e^{−πzt}| ≤ (π|z|)^j e^{a−π Re z}.
- **(M4)** (MOB-P) literal en GRAM §18.3, absoluta en B_a²; la expansión modal y b_λ = q^{−1/2}f_{d,q}
  recomputadas (λ = kn², k^{5/4}n² = λ^{5/4}n^{−1/2}). Correcto.
- **(M5)** GRAM §17.2–17.3: (RES-SOS) y D_q > 0 literales, válidos en y = 0. La cota D_q ≥ c_*I_q
  (§17.5) se enuncia allí para una familia con parámetro 0 < ε ≤ 1; no se comprobó aquí que cubra
  y = 0. No importa: la memo sólo usa D_q > 0.

### II.2 Verificación de los pasos

- **Lema 1.** ‖Vc‖² = A_0 − ρ ≤ A_0 ≤ |A_0| ≤ C_a‖P(c)‖². Correcto; no supone signo. Un cuadrado
  acotado por una forma continua en una norma es continuo en esa norma: inmediato, sin laguna.
- **(R0).** El funcional está bien definido en el cociente (se anula donde P(c) = 0), Hahn–Banach en
  el espacio de Banach complejo B_a², composición con una aplicación holomorfa: correcto. Los valores
  N_g(k) no dependen de la extensión elegida.
- **(R1), clase de crecimiento.** H = N/(z+1)⁴ es holomorfa y acotada en Re z ≥ δ; el cociente por
  factores de Blaschke finitos del semiplano Re z > δ es acotado y continuo hasta el borde, con
  módulo ≤ ‖H‖_∞ en el borde; el principio de Phragmén–Lindelöf para funciones acotadas da la cota
  interior. Producto: Π(1 − 2(z₀−δ)/(k+z₀−2δ)) → 0 ⟺ Σ1/k = ∞. Correcto. El crecimiento polinómico
  en un semiplano **es suficiente** (tras dividir por un polinomio la función es acotada; la
  condición de Blaschke de la clase acotada se aplica). No hace falta un teorema de tipo exponencial.
- **(R2), nodos.** Correcto: N_g − αN′_g se anula en {θ = α}, luego N_g = αN′_g; entonces N′_g se
  anula en {θ ≠ α}.
- **Proposición 3.** Correcta; no supone signo. Para RES-SOS coincide con (TAIL-ZERO) +
  (NO-FIN-MARGIN) de GRAM §18.7 (f_{d,q} es de soporte finito): no es nueva.
- **Proposición 4.** Trivial y correcta.
- **Observación 5.** Recomputada contra STATEMENT_001 §2: x = δ_m − δ_k da x*𝔸x = 2B(0) − 2B(log(m/k));
  para |d| < log 2 − 2T_0 la parte aritmética de B(d) es nula; F̂_0 = (τ²+¼)|ĝ|⁴ = O(τ^{−2}), de modo
  que τ²m(τ)F̂_0² es integrable y B es C² par cerca de 0. Correcta relativa a STATEMENT_001 §2 (no
  cotejada contra el texto del paper, como la propia memo advierte).
- **Circularidad.** Ninguna.

### II.3 Caza de contraejemplos

Juguete exacto de la misma estructura: A_toy[c] = ∫_1^∞ |Σ_k c_k e^{−πkt}|² dt (forma continua en la
norma del grafo, PSD, con sistema exacto V c = Σ c_k e^{−πk·} y ρ = 0). ¿Admite un cuadrado
dependiente sólo del coeficiente c_1? La distancia relativa de e^{−πt} al span de {e^{−πkt}}_{2≤k≤K}
en L² es exactamente Π_{k=2}^K (k−1)/(k+1) = 2/(K(K+1)) → 0 (fórmula de Müntz, que es el mismo
producto de Blaschke de (R1)). Luego inf{A_toy[c] : c_1 = 1} = 0 y ningún cuadrado w|c_1|², w > 0,
cabe en una identidad exacta: el juguete confirma el teorema y no lo refuta. Con nodos lacunares
(k = 2^j) el producto no tiende a 0 y el cuadrado sí cabe: la hipótesis de divergencia es necesaria.
**PROVED** (cálculo cerrado). No se halló contraejemplo al Lema 1, (R0), (R1) ni (R2).

Lo que sí existe, y limita el título de la memo: funcionales continuos cuyo ÍNDICE o cuyos PESOS son
aritméticos, por ejemplo ℓ_{m,t₀}(c) = (TP(c))(t₀) − m^{−1/2}(TP(c))(m²t₀) con peso Λ(m). Sus
coeficientes en k son valores de una función holomorfa de k, como exige (R0), y no caen en la clase 𝒜.
La memo lo reconoce en §7(i); el título y §4 deben ser coherentes con ello (C-2).

### II.4 Errores y lagunas (con ubicación)

C-1. **Versión de modos de (R1), (R2), clase 𝒜 «en el índice de modos», instancia 5 — laguna.**
Los «coeficientes en modos» de un funcional no están definidos unívocamente sobre vectores c finitos:
ningún c finito aísla un modo (b = δ_λ exige c_{λn²} = μ(n)n^{−1/2}, de soporte infinito). La memo
aplica (R1) a un operador dado como «selección 1_S(λ) de un operador continuo» identificando sus
coeficientes formales x_λ con n_g(λ) sin demostrarlo. Lema que falta (PROVED aquí): si
ℓ(c) = Σ_λ b_λ(c)x_λ para todo c finito, ℓ es continuo en la norma del grafo y
Σ_N d(N)N^{−1/2}|x_{λN²}| < ∞ para cada λ, entonces n_g(λ) = x_λ. Prueba: por (MOB-P) y continuidad,
ℓ̃(E_λ) = λ^{−5/4}Σ_n μ(n)n^{−1/2}ℓ(δ_{λn²}) = λ^{−5/4}Σ_{n,n′} μ(n)(nn′)^{−1/2}x_{λn²n′²}
= λ^{−5/4}Σ_N N^{−1/2}x_{λN²}Σ_{n|N}μ(n) = λ^{−5/4}x_λ, con reordenación justificada por la
convergencia absoluta. En la instancia 5, x_λ = 1_{m²|λ}⟨h_λ, g⟩ decae exponencialmente y la
hipótesis se cumple. Con este lema la versión de modos y la instancia 5 quedan PROVED; sin él son
ARGUED.

C-2. **§4, instancia 2, última frase — falsa como está escrita.** «El índice “clase libre de
cuadrados” no puede ser parte del índice de ningún sistema exacto.» Lo probado es que ningún cuadrado
puede DEPENDER sólo de coeficientes de un conjunto de nodos de complemento divergente (en particular
de un número finito de clases). Un sistema exacto puede estar indexado por d, por m o por cualquier
etiqueta aritmética, siempre que cada funcional sea continuo en el grafo (ejemplo de II.3). Debe
sustituirse por: «ningún cuadrado de un sistema exacto puede depender sólo de los coeficientes de
una familia de clases cuyo complemento sea divergente».

C-3. **§4, párrafo final — afirmación no demostrada y falsa en su literalidad.** «La única función
aritmética clásica que pasa el filtro (R0) como torsión es log k.» Toda restricción a los enteros de
una función holomorfa de crecimiento polinómico en el semiplano pasa la condición necesaria (k^s,
k^{it}, polinomios en log k); y (R2) no dice nada de torsiones sin conjunto de nivel divergente
(φ(k)/k, σ(k)/k, e(αk) con α irracional): ni excluidas ni admitidas. Debe eliminarse o quedar como
observación sin etiqueta. Para e(αk) irracional una exclusión por un argumento de tipo exponencial
más integrabilidad logarítmica en el borde es plausible (ARGUED, no escrita en la memo).

C-4. **Respuesta corta, §9 y título — alcance de «torsión aritmética».** (R2) cubre sólo torsiones θ
con un valor α tal que {θ = α} y {θ ≠ α} son ambos divergentes (caracteres de módulo q ≥ 2, sumas de
Ramanujan no constantes, μ, μ², Λ, indicadoras). La frase «ningún cuadrado puede depender de índices
aritméticos» no está probada y no es cierta (C-2, II.3). El enunciado debe llevar la clase exacta.

C-5. **Novedad sobrestimada en el cotejo.** El argumento de (R1) (holomorfía de z ↦ ℓ(P_z), división
por (z+1)⁴, producto finito de factores de Schwarz del semiplano, divergencia de Σ1/d) es literalmente
el de GLOBAL «Escalas libres de cuadrados» con «libres de cuadrados» sustituido por «conjunto de suma
recíproca divergente»; las instancias 1, 2 y 6 son GRAM §18.7; la instancia 5 es la «Consecuencia
para el resto conjunto» de GLOBAL. Lo nuevo respecto del corpus es: el Lema 1 como enunciado
(exactitud con resto no negativo ⟹ continuidad de cada cuadrado), (R2), y las instancias 3–4
(clases de residuos, caracteres, Ramanujan, μ, Λ, gcd). La memo lo dice a medias («generalización
común»); el registro debe decirlo sin ambigüedad. No hay herramienta nueva.

C-6. **§8 — etiqueta.** «(M2) vale para la forma análoga de cualquier peine con C_a acotado en H_γ,
en particular cΛ, a_P…» no está demostrado en la memo ni en la cita (la identidad (GRAPH) usa
Σ_{m|n}Λ(m) = log n; para otro peine la forma análoga no está escrita). Etiqueta: **ARGUED**.

C-7. **Proposición 3, «Lectura».** «Off cancela a R_res por completo» es (TAIL-ZERO) reescrito:
A_0 → 0 a lo largo de la sucesión con R_res ≥ √d·D_q. No añade nada a GRAM §18.7 y no debe figurar
como resultado nuevo.

C-8. **Alcance respecto de la identidad (G) de OBJECT_SPEC.** El teorema restringe una identidad
ÚNICA sobre el portador de escalas enteras en y = 0, en las coordenadas c. No restringe objetos
escritos por ventana (a_T, P_T) ni sobre 𝔸_M (la memo lo dice en §7(ii)); el punto (4) del cotejo
(«condición necesaria sobre el operador V de (G)») debe llevar esa restricción.

### II.5 Enunciado corregido, etiqueta y alcance

**Teorema R (PROVED, relativo a (M2)–(M4) de la fase 211, CITED y recomprobados aquí).** Sea
0 < a < π. Si un sistema de cuadrados (ℋ, V) sobre coeficientes finitos en escalas enteras cumple
‖Vc‖² ≤ M·A_0[c] para todo c (en particular si A_0 = ‖Vc‖² + ρ con ρ ≥ 0 para todo c), entonces para
cada g ∈ ℋ:
(i) c ↦ ⟨Vc, g⟩ es continuo en la norma ‖P(c)‖_{a,2};
(ii) ⟨Vδ_k, g⟩ = N_g(k) con N_g holomorfa en Re z > a/π y |N_g(z)| ≤ C(1+|z|)^{13/4} en Re z ≥ δ;
(iii) si ⟨Vδ_k, g⟩ = 0 para todo k de un conjunto con Σ1/k = ∞, entonces ⟨Vc, g⟩ = 0 para todo c;
(iv) si V′ cumple la misma cota y Vδ_k = θ(k)V′δ_k con {θ = α} y {θ ≠ α} ambos de suma recíproca
divergente para algún α, entonces V = V′ = 0;
(v) lo mismo en el índice de modos para funcionales ℓ(c) = Σ_λ b_λ(c)x_λ con
Σ_N d(N)N^{−1/2}|x_{λN²}| < ∞ (lema de C-1).

**Corolario (NO-GO con clase, PROVED).** En una identidad única A_0 = Σ cuadrados + ρ, ρ ≥ 0, sobre
todo el portador de escalas enteras en y = 0, ningún cuadrado no nulo puede: depender sólo de un
conjunto de nodos de complemento divergente (soporte finito, un número finito de clases libres de
cuadrados, una clase de residuos, múltiplos de g ≥ 2, gcd(k,q) fijo); ser la torsión de un funcional
continuo por un carácter aditivo o multiplicativo de módulo q ≥ 2, una suma de Ramanujan no
constante, μ, μ² o Λ; ser la selección de un conjunto de modos de complemento divergente aplicada a
un operador continuo, sola o sumada a un término continuo. Lo mismo vale con «‖Vc‖² ≤ M·A_0» en lugar
de la identidad.

No queda excluido: cuadrados continuos en el grafo con etiquetas o pesos aritméticos (índice de
dilatación m, pesos Λ(m)); torsiones sin conjunto de nivel divergente; identidades con resto sin signo
manifiesto o no negativo sólo en un subespacio; cualquier objeto escrito por ventana o sobre 𝔸_M
(allí sólo la Observación 5, PROVED relativa a STATEMENT_001 §2). No es paso de signo.

### II.6 Qué puede anotarse en el índice y en el grid

Puede anotarse (índice 06, residuo R9, subrutas muertas; grid), con este texto:

> **Fase 212, sistema ampliado de cuadrados con selección o torsión aritmética en nodos o modos —
> NO-GO con clase, PROVED (relativo a GRAM §18.2 y a la holomorfía de z ↦ P_z de GLOBAL «Escalas
> libres de cuadrados»).** `ROUND_001_C.md`, Lema 1, Teorema R, Corolario 2; revisión
> `REVIEW_001_LC.md` (lema de unicidad de coeficientes modales incluido allí). En una identidad única
> A_0 = Σ cuadrados + resto no negativo sobre el portador de escalas enteras (y = 0), cada cuadrado
> es continuo en la norma del grafo y sus coeficientes en k son los valores enteros de una función
> holomorfa de crecimiento polinómico en un semiplano; por tanto ningún cuadrado no nulo puede
> anularse sobre un conjunto de nodos o de modos de suma recíproca divergente, ni ser la torsión de
> un funcional continuo por una función con un conjunto de nivel divergente de complemento divergente
> (caracteres de módulo q ≥ 2, sumas de Ramanujan no constantes, μ, μ², Λ, indicadoras de clases de
> residuos, de múltiplos o de gcd fijo). Generaliza con el mismo instrumento GRAM §18.7 (soporte
> finito) y GLOBAL «Escalas libres de cuadrados» (cola libre de cuadrados, discontinuidad de S_sq); lo
> nuevo es la clase, no la herramienta. No excluye cuadrados continuos con índice o pesos aritméticos
> en la dilatación, torsiones sin conjunto de nivel divergente, restos sin signo manifiesto, ni
> objetos por ventana o sobre 𝔸_M. No aporta signo. La dirección de R9 en la formulación (S) queda
> abierta con una única restricción de módulo de continuidad (Observación 5).

No puede anotarse: (a) «ningún cuadrado puede depender de índices aritméticos» ni «el índice clase
libre de cuadrados no puede formar parte de un sistema exacto» (C-2, C-4); (b) «log k es la única
torsión aritmética admisible» (C-3); (c) la genericidad en el peine de §8 como PROVED (C-6);
(d) la Proposición 3 como resultado nuevo (C-7); (e) el cierre de R9: la memo no lo cierra.

---

## Parte III — Veredicto

- **ROUND_001_L: ACCEPT with corrections.** Núcleo matemático correcto y completo relativo a tres
  teoremas clásicos bien enunciados y con hipótesis satisfechas. Correcciones: L-1, L-2 (etiquetas),
  L-3 (rango nuevo 0 < ε < 1), L-4 (no efectividad), L-5, L-6 (menores), L-7 (redacción de sandbox y
  no registro del Cor. 2.2).
- **ROUND_001_C: ACCEPT with corrections.** Lema 1 y Teorema R (nodos) correctos. Correcciones: C-1
  (lema que falta en la versión de modos; suplido arriba), C-2 a C-4 (sobre-enunciados que deben
  retirarse), C-5 y C-7 (novedad), C-6 (etiqueta), C-8 (alcance).

Ninguna de las dos memos aporta positividad de la forma; ambas son herramientas de descarte y así
deben figurar.
