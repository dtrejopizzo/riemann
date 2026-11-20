# Ronda 002 C — El canal de dos bases primas: memo de selección

Notación de `../phase-211-sign-sandbox/STATEMENT_001.md`; N = e^{2T}; ℓ_p = log p. Objetivo (★):
λ_A(T) ≥ 0 para todo T, como signo de la forma a_T sobre P_T. Esta memo es de selección: no deriva
más allá de lo necesario para enunciar los cinco puntos del cotejo.

Candidata. En γ_Λ = μ∗β_Λ = Λ·log − Λ∗Λ (valores: ℓ_p² en p^k; −2ℓ_pℓ_q en p^a q^b, p ≠ q; 0 si
ω(n) ≥ 3) el canal −2ℓ_pℓ_q «sugiere un cuadrado en la red de bases primas» (R170_850 §5). Pregunta:
¿existe un cuadrado explícito en F, indexado por pares (p,q) o por la red de exponentes, cuyo
desarrollo dé ese término cruzado con la orientación correcta y diagonales que a_T contiene, y que
no sea ninguno de los cinco casos ya cerrados?

**Veredicto del cotejo: repetición. Sin mecanismo nuevo.** La memo termina en el cotejo.

## Cotejo

### (1) Antecedentes más cercanos (fuentes primarias leídas)

a. `phase-170-global-prime-inequality/R170_850` §§0, 4, 5 (ley (0.2), forma extraída (4.2),
   completación «no afirmada»); `R170_851` §§0–2 (γ = Λ·log − Λ∗Λ; con W = μ∗log² vuelve al
   apareamiento sin signo); `R170_841` §§4.1–4.3 (β_Λ(12) < 0; Cauchy–Schwarz par frente a primer
   momento impar; la deconvolución de Möbius vuelve al mismo punto); `R170_854` §3 ecuación (3.4) y
   §6.3 (toda completación por cuadrados de la corriente graduada conserva métrica indefinida;
   cuadrar el sector da ratio-comb o supertraza indefinida); `R170_855`–`R170_856` §§3–4 (γ + W =
   2Λ·log es subidentidad de ramas; en la identidad completa de Poisson–Chebyshev el W se cancela
   término a término con el −W del bloque de Poisson). Todo CITED.
b. `phase-162-row-d-first-contact-closure/R162_501` Prop. 3.1(a) (PROVED allí): la positividad de
   coeficientes sobre log ℕ no da signo al apareamiento con c_F′(log n).
c. `phase-70-lee-yang-dbn/E70_10` (cuadrado de Dirichlet (I−V)*(I−V) = I − T_Λ + V*V; V*V vive en
   el peine de cocientes log(n/m) con coeficientes ≥ 0 y masa divergente) y `E70_11`–`E70_12`
   (Selberg = Riccati de V = Z⁻¹δZ). `phase-166-omega-closure/R166_502` §5.2 (PROVED allí): el cuadrado
   hermítico V*V y el cuadrado de convolución V² difieren, par de primos por par de primos, en
   S_{log q^l} ↦ S*_{log q^l}, es decir productos p^k q^l ↦ cocientes p^k/q^l; la parte no entera de
   V*V es exactamente Σ_{p≠q} V_p*V_q; Selberg reescribe V², no V*V; «la cancelación tendría que venir
   de un segundo sector con signo». **Éste es el antecedente literal de la candidata**: el «cuadrado
   en la red de bases primas» es la suma cruzada Σ_{p≠q}, y ya está escrito qué produce.
d. `phase-204-refd-tractability/P1_BBSTAR_001`: Teorema P1.A (PROVED allí: P47 thm:sos vale para
   polinomios de Dirichlet con frecuencias reales arbitrarias, incluidas dilataciones con pesos Λ,
   Λ₂, μ, log; no hay B convolutivo para T ≥ ½log3), Lema 2.7 (toda descomposición 𝒲 = α𝒞*𝒞 + R
   fuerza en R átomos −αℓ_pℓ_q/√(pq) en ±log(p/q)) y §2.8 («Selberg entra en 𝒞², no en 𝒞*𝒞»).
e. `phase-211-sign-sandbox/ROUND_005_A` Lema 3.2 y Prop. 3.3 (PROVED allí): en la ventana,
   ⟨F,Π²F⟩ = [peine de productos con Λ∗Λ, indefinido] + [media del polinomio de Dirichlet, ≥ 0,
   cocientes] − ‖𝔏F‖² [fuga]; §5.3: (R) y (L) son genéricas en el peine y casi se cancelan; el
   contenido Λ∗Λ es la parte menor y sin signo. `ROUND_023_A` Lema 2.1 (Selberg en forma de
   operadores, Φ(Λ·log) = [M,P] = 𝔇⁻¹[M,[M,𝔇]] − P²) con el «no reintentar» de P211-23A.
f. `phase-186-toolbox/R186_005` Lema S0 y Teor. TB3-neg (PROVED allí): la identidad de grado dos
   vale para todo peso b con su propio sistema; lo único específico es N_b ≡ 1.
g. Índice: `ROUTES-TRIED-INDEX/04_PHASES_100-189.md` filas G6C-R162_501, G6C-R162_2301,
   G6C-R166_502, G4C fase-36/107 («el bloque primo×primo entra con signo más»), G4C fase-70/E70_10;
   README l.541 (R11_2_ORIGIN: «Selberg Λ∗Λ orden 2 NO-GO»), l.596 (P1_BBSTAR), l.651 (nodo:
   Selberg = reintento sin razón nueva), l.1087 (P211-5A). Grid: celda 6C (R162_501 herramienta;
   R162_2301, R166_502 cerradas). Crucigrama: l.516, l.622, l.1594–1598 (Potencias067). Paper 48:
   fila «Selberg difference channel» de la tabla de rutas (no-go). `RULES_AVOID.md` B1, D17b, I2, I8.
   Fase 212: `ROUND_001_A` Lema B, `ROUND_001_D` Lema A.

### (2) El objeto: qué puede escribirse y qué falta

No hay (ℋ_T, V_T, ρ_T) que escribir. Las tres lecturas posibles de «cuadrado indexado por pares»
caen cada una en un caso ya cerrado:

- **Lectura de coeficientes** (la matriz de la red de bases primas leída de la ley (0.2):
  Γ_pp = ℓ_p², Γ_pq = −ℓ_pℓ_q). Con y_p = ℓ_p x_p,
  Σ_p y_p² − 2Σ_{p<q} y_p y_q = 2Σ_p y_p² − (Σ_p y_p)².
  Para dos primos es (y_p − y_q)²; para r ≥ 3 primos tiene autovalores 2 (multiplicidad r − 1) y
  2 − r < 0. PROVED (cálculo de una línea; afirma sólo esto sobre la matriz de coeficientes). La
  sugerencia de R170_850 §5 es, pues, un hecho de dos primos: la red completa lleva una dirección
  negativa. Además γ se aparea con c_F′(log n) en nodos distintos (p, q, pq), así que ni siquiera el
  caso de dos primos es un cuadrado en F: es un uso lineal en la autocorrelación. Caso (ii) y
  cláusula O2 (certificado). CITED: R162_501 Prop. 3.1(a).
- **Lectura hermítica convolutiva** (V_T F = combinación de traslaciones por ±k ℓ_p con pesos
  ℓ_p p^{−k/2}; el término cruzado en log p^a + log q^b sale de emparejar una traslación hacia
  adelante con una hacia atrás). La diagonal de todo cuadrado de este tipo es masa ‖F‖² y no un
  término de traslación; las traslaciones del mismo sentido producen los cocientes log(p^a/q^b), que
  a_T no contiene. Es literalmente E70_10 / R166_502 §5.2 / P1_BBSTAR Lema 2.7, y la clase entera
  (sumas de cuadrados con frecuencias en log ℚ y pesos Λ, Λ₂, μ, log) está cerrada para T ≥ ½log3
  por P1.A. Caso (iv), O8. CITED.
- **Lectura comprimida a la ventana** (traslaciones truncadas). Es ROUND_005_A Prop. 3.3: producto
  (Λ∗Λ, sin signo) + cocientes (≥ 0, genérico) − fuga (≤ 0, genérico). CITED. No hay cuarta pieza.

Lo que falta, con precisión: una familia de operadores X_p sobre un espacio de Hilbert tal que
(a) X_q*X_p sea, para **todos** los pares p ≠ q a la vez, el desplazamiento por log p + log q con
coeficiente de signo fijo; (b) no aparezca ningún átomo en log(p/q); (c) Σ_p ℓ_p² X_p*X_p sea una
parte exacta de la forma arquimediana, uniformemente en T. Ningún archivo del corpus la contiene y
esta memo no la tiene. OPEN, sin objeto.

### (3) Por qué el cambio no evita la dificultad del antecedente

No hay cambio. La dificultad registrada en R170_851 §2 y R170_841 §4.3 es que el contenido de grado
dos entra apareado con una derivada de correlación, no con una norma; la registrada en R166_502 §5.2
es que el paso a una norma cambia productos por cocientes. Indexar por pares (p,q) no altera ninguna
de las dos: el índice de pares **es** la suma Σ_{p≠q} de R166_502. La orientación «correcta» del
término cruzado se obtiene sólo en el cuadrado de convolución (lineal en c_F), no en el hermítico.
La variante «con ambas diagonales en el mismo collar» es la completación que R170_854 (3.4) y §6.3
ya declaran indefinida o productora de ratio-comb. NO-GO en esas clases, CITED.

### (4) Identidad que la conectaría con la positividad global

Ninguna. Tres hechos lo impiden:

- a_T no contiene ningún desplazamiento en log(pq), p ≠ q: su parte aritmética es
  −Σ_{n<N} v_n Re c_F(log n) con soporte en potencias de primos (STATEMENT §1). Un término cruzado
  −2ℓ_pℓ_q en log p + log q sólo puede entrar en (G) cancelándose o vía Λ∗Λ = μ∗log² − Λ·log; el
  μ∗log² así introducido es el segundo jet del peine entero, y R170_856 §§3–4 prueba que se cancela
  en la identidad completa. CITED.
- γ vive en la derivada de escala (virial), apareada con c_F′. Unirla a (★) exige la arquitectura de
  primer contacto de la fase 170 (dependiente de (REG), no probada) o el signo de una pendiente,
  ambas registradas sin signo (R162_501 Prop. 3.1; P211-23A, P211-24A). No se reabre.
- Por ROUND_001_D Lema A la forma es afín en el peine: una identidad que sólo reescribe el peso
  (aquí por la regla de Leibniz, ROUND_001_A Lema B) no cambia la forma. CITED.

### (5) cΛ y a_P: la línea que se rompe

No hay línea que romper porque no hay (G). Sobre el canal mismo: por R170_854 (4.7), para un peso
general a, μ∗β_a = a·log − (μ∗a)∗log, luego γ_{cΛ} = c·γ_Λ. PROVED (sustitución directa, usando
μ∗log = Λ). El canal de dos bases primas es **lineal y homogéneo en el peso**: uno de los dos
factores ℓ_p, ℓ_q viene del peine entero fijo, no del peso. No distingue c = 1 (incumple O4 y O10)
y es compatible con ROUND_001_D Lema A. Para a_P: γ_{a_P} = a_P·log − a_P∗Λ sigue siendo una ley
exacta explícita (el cruce vale −2ℓ_pℓ_q si p, q ≥ P y −ℓ_pℓ_q si sólo uno lo es); nada falla. Los
demás falsificadores de `RULES_AVOID.md` §E no se recorren por la misma razón; para sistemas de
Beurling, R186_005 Lema S0 (CITED) da la ley análoga con su propio sistema.

### Respuesta a las cinco exclusiones de la pregunta

(i) Selberg: la candidata **es** ese descarte (R170_851; R166_502). (ii) Uso lineal: sí, por c_F′ y
por la homogeneidad en el peso; R170_869 clasifica toda fila lineal sobre el espacio de coeficientes.
(iii) Genérica en el peso: sí, por (5). (iv) Suma de cuadrados aritmética: la lectura hermítica cae
en P1.A. (v) Selección aritmética en el nodo: no se llega a este punto; un índice de pares en la
dilatación no está excluido por R-cont, pero no hay cuadrado que indexar.

## Resultado

**Sin mecanismo nuevo.** Repetición de R170_850–856, R166_502 §5.2, E70_10–12, P1_BBSTAR (P1.A, Lema
2.7, §2.8) y 211/ROUND_005_A Prop. 3.3. No es un teorema de imposibilidad nuevo: no se excluye un
segundo sector con signo ni un objeto no convolutivo con las propiedades (a)–(c) de (2); se registra
que la candidata, tal como está formulada, no aporta ninguno. No procede construcción.

## Qué se probó

- La matriz de coeficientes de la red de bases primas leída de la ley (0.2) es
  2·diag − (rango uno): cuadrado perfecto sólo con dos primos, con una dirección negativa 2 − r
  desde r = 3. PROVED (elemental; alcance: sólo la matriz de coeficientes).
- γ_{cΛ} = c·γ_Λ: el canal es lineal y homogéneo en el peso. PROVED (a partir de R170_854 (4.7)).
- Lo demás es CITED de las fuentes de (1).

## Qué falló y por qué

- El término cruzado con orientación negativa en desplazamientos de producto sólo aparece en el
  cuadrado de convolución, que es lineal en la autocorrelación de F; al pasar a una norma en F los
  productos se convierten en cocientes con coeficiente ≥ 0 y la diagonal en masa, no en los términos
  ℓ_p² c_F′(k ℓ_p) de la ley. Falla la identidad «cuadrado hermítico = canal γ»: la diferencia es
  exactamente Σ_{p≠q} V_p*V_q − Σ_{p≠q} V_pV_q (R166_502 §5.2).
- a_T no tiene términos en log(pq); el único puente (Selberg) introduce μ∗log², que se cancela en la
  identidad completa (R170_856).
- El canal no rompe bajo cΛ ni bajo a_P.

## Siguiente paso concreto

No relanzar el canal de dos bases primas ni otra lectura de Λ·log ± Λ∗Λ. Reabrir exige escribir
antes los operadores X_p de (2)(a)–(c), en particular el mecanismo que elimina los átomos en
log(p/q) sin pagar masa, que es el «segundo sector con signo» de E70_10 y R166_502, nunca
construido. Anotar en `RULES_AVOID.md` I8 que el residuo «canal −2 log p log q (850 §5, no
construido)» queda cotejado como repetición, con las dos observaciones PROVED de arriba, y registrar
la fila correspondiente en el índice de rutas y en el grid (no hecho aquí: esta memo no edita otros
archivos).
