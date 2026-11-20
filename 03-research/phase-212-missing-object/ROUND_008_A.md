# Ronda 8, encargo A — el concomitante de borde que convertiría el canal de producto en el de cocientes

Notación de la fase: a_T(F) = Arch(F) − Σ_n v_n c_F(log n), F real, sop F ⊂ [−T,T], F ∈ P_T.

## 0. Paso previo: ¿se intentó la exigencia de R161_034 §0 después de escrita?

Sí. Se llevó a cabo y se cerró dentro de la propia fase 161. Lectura en primaria:

- `phase-161-row-d-sum-product-square/R161_034_MELLIN_GRAM_AND_PRODUCT_RATIO_COLLISION.md` §§0–7. El símbolo de
  cada átomo es q_k(τ) = k^{−s}u_∞(τ) − k^{−(1−s)} (1.3). El Gram cruzado se parte en un canal de cocientes
  cos(τ log(k/l)) y un canal de productos Re{u_∞(τ)e^{−iτ log kl}} (3.2). En recta completa no hay cancelación
  (§4, ARGUED). El candidato que deja es la fuga coherente comprimida L_{N,T} = ‖(I−P)Σ(log k)d_kPF‖² (5.2), que
  envuelve el conmutador [P,d_k] (5.1). u_∞ es exactamente el intercambio de orientaciones ξ ↔ −ξ.
- `R161_035` construye el objeto pedido en su forma más fuerte. Con U_N = K_N𝓕 y V_N = JK_N (las dos
  orientaciones, sintetizadas previamente por Λ∗1 = log, (4.1)), la identidad del paralelogramo da
  D_N^coh = ¼‖(U_N − V_N)f‖² ≥ 0 (3.2), conservando todo el Gram k/l y kl. La componente de borde es
  ¼‖(I−P)(U_N−V_N)f‖² (5.1). Lo que falta es la saturación (5.2)–(5.3).
- `R161_037`: si hay saturación, entonces F = 0. `R161_038`: un contramodelo 2×2 exacto satisface (PC), la
  radicalidad y la paridad sin saturar. `R161_039`: equivalencia terminal; falta una identidad de Green física
  (3.1).
- `R161_057`–`R161_065`: la familia «concomitante de soporte / potencia hermítica / lagrangiana». R161_065 (1.2)
  prueba que el concomitante candidato es K_P(S;g,w) = ⟨g,[P,S]w⟩, es decir el conmutador de soporte ya
  auditado, que es indefinido. R161_064 (4.2), que lo expandía como suma de energías no negativas, queda retirada.
  Según R161_065 §4, lo que falta es un teorema aritmético exterior, por ejemplo Re⟨g, P_R C_log g + εg⟩ = 0.
- `R161_050`: un contramodelo de tres bloques muestra que la cancelación central, la unitariedad autoadjunta y la
  paridad de dispersión no transfieren el signo al exterior.
- `R161_075` y `R161_081` tratan el dominio del multiplicador y el test Q ≥ 0, que queda excluido en el espacio
  primitivo. Ninguno de los dos reabre lo anterior.
- Índice de rutas (`04_PHASES_100-189.md`, líneas 746, 763, 769): G1C-R161_061-065 DEAD (concomitante = conmutador
  de soporte); G4C-R161_035-038 PARTIAL; G8B-161 R161_037-039 DEAD (contramodelo 2×2). README l. 2457 registra los
  contramodelos 038/050. RULES_AVOID §Q3 y REVIEW_007 R7-c recogen la repetición de la ronda 7.
- 211 «Extensión factorial» y 106_109 (§2, (9)–(10)) ya figuran en la memoria de selecciones rechazadas. No
  contienen una versión comprimida del concomitante distinta de la anterior.

**Dictamen del paso 0: repetición.** La operación «canal de producto comprimido = canal de cocientes
comprimido + concomitante de borde con signo» se ejecutó en R161_035 (con signo, gracias al paralelogramo) y en
R161_057–065 (el concomitante se calcula y resulta ser [P,S], sin signo). Se cerró por dos vías: el contramodelo
R161_038/050 y la reducción R161_065 (1.2). Conforme a la regla, **la construcción se detiene aquí**. Las
secciones siguientes no derivan nada nuevo. Sólo fijan, con las fórmulas del encargo, dónde queda el signo y qué
hipótesis del cierre no está forzada.

## 1. Filtro de cuatro puntos (escrito después del paso 0)

1. **Antecedente:** R161_035 §§3–5 y R161_065 §§1–4, con los contramodelos R161_038 y R161_050.
2. **Objeto nuevo:** ninguno. El «canal de cocientes comprimido + concomitante» es D_N^coh de R161_035, y el
   concomitante es ⟨g,[P,S]w⟩ de R161_065.
3. **Esquiva de la dificultad:** no la esquiva. El signo queda en la saturación (R161_039 (2.1)), o bien en el
   conmutador indefinido.
4. **Conexión global:** la única existente es la de R161_037–039: saturación ⇒ ausencia de estado de primer
   contacto ⇒ a_T ≥ 0 en P_T para todo T, vía los teoremas de anidamiento. Esa implicación es CITED; la
   saturación sigue OPEN.

No pasa la puerta.

## 2. Precisión de (a)–(d) sin derivación nueva

**(a) Enunciado.** Con u_∞ como en R161_034 (1.1), el operador completo de una orientación es τ_{log k}𝓕 y el de
la otra es Jτ_{log k}. La reflexión entra por J: para F real, F̂(−ξ) = conj F̂(ξ). En Mellin, A(ξ)A(ξ) frente a
A(ξ)A(−ξ) es exactamente «orientaciones opuestas» frente a «iguales» ((3.1) de 034). u_∞ es el único factor que
liga ξ con −ξ en el peso completo. Comprimido a la ventana:

- canal de cocientes comprimido = ‖P(U_N+V_N)Pf‖² y ‖P U_N P f‖² + ‖P V_N P f‖²;
- canal de productos comprimido = Re⟨PU_NPf, PV_NPf⟩.

(PROVED como reescritura de R161_035 (3.1)–(3.2).)

**(b) Diferencia.** Producto menos cocientes es −¼‖(U_N−V_N)f‖² más el término de borde que separa la versión
comprimida de la versión completa. Ese término es exactamente ⟨f,[P,·]f⟩ (R161_065 (1.2)–(1.3)). La parte de bulk
es el cuadrado del paralelogramo. Ni para T → ∞ ni bajo las dos restricciones de momento (F ∈ P_T) el término de
borde pasa a tener signo: R161_064 (4.2) se retiró. (CITED.)

**(c) a_T de grado uno.** Los objetos de 035 son cuadráticos en el operador K_N, que es lineal en Λ ∗ 1 = log, y
por tanto de grado dos en la síntesis. a_T sólo aparece a través de la radicalidad lineal (PC-ren). El paso de la
afirmación de grado dos (saturación) a a_T ≥ 0 existe, pero es indirecto: por contradicción sobre un estado de
primer contacto y por R161_037 (CITED). Por R161_038, ningún enunciado que use sólo (PC) + radicalidad + paridad
fuerza el objeto de grado dos. (PROVED en la clase formal 2×2. Fuera de ella: OPEN.)

**(d) Término con signo y controles.** El único término con signo manifiesto es ¼‖(U_N−V_N)f‖². Ese término es
≥ 0 para todo peso, también con c = 2, con una potencia de primo borrada y con un peso de Beurling. Es ciego, y
no se rompe: es el patrón J2/L3. El término que debería romperse es la saturación, o el conmutador [P,S]. Ninguno
de los dos tiene signo en el corpus, de modo que no hay un signo nombrado que se pierda. (ARGUED.)

## 3. La hipótesis del cierre que no está forzada

Los contramodelos R161_038 (2×2) y R161_050 (3×3) refutan sólo la transferencia **puramente algebraica**. Lo dice
explícitamente R161_050: «does not reproduce the integer translation semigroup, the explicit zeta product port, or
the Gamma/Tate collars». La hipótesis no forzada del cierre es, por tanto, esta:

> que la saturación (o el signo del concomitante [P,S]) deba deducirse sin usar la ley de semigrupo
> τ_{log k}τ_{log l} = τ_{log kl} sobre ℕ acoplada a la compresión P_T.

En los modelos finitos S es nilpotente o una permutación, sin estructura multiplicativa de enteros. Para reabrir
haría falta un enunciado que use esa ley dentro del conmutador, de la forma [P,τ_{log kl}] = [P,τ_{log k}]τ_{log l}
+ τ_{log k}[P,τ_{log l}] (regla de Leibniz del conmutador, PROVED trivialmente). Además, tendría que sumarse con
pesos Λ∗Λ, y no sólo con Λ∗1. Ese enunciado tendría que producir un cuadrado y no una forma indefinida. No se
construye aquí. Antes habría que contrastarlo con R161_045 (Toeplitz–Hankel local) y con la familia de transporte
de la memoria de selecciones rechazadas.

## 4. Lista de afirmaciones

| # | Afirmación | Etiqueta |
|---|---|---|
| 1 | La exigencia de R161_034 §0 se ejecutó en R161_035 y R161_057–065 y se cerró | CITED (lectura en primaria) |
| 2 | Concomitante candidato = ⟨g,[P,S]w⟩, indefinido | CITED (R161_065 (1.2)) |
| 3 | La saturación no se sigue de (PC) + radicalidad + paridad | CITED (R161_038, R161_050) |
| 4 | Esta ronda: repetición; la construcción se detiene | NO-GO (repetición) |
| 5 | (a)–(b) como reescritura del paralelogramo de 035 | PROVED (reescritura) |
| 6 | El término con signo es ciego al peso (c = 2, borrado, Beurling) | ARGUED |
| 7 | Hipótesis no forzada: ausencia de la ley de semigrupo de ℕ en los contramodelos | ARGUED |
| 8 | Regla de Leibniz del conmutador sobre τ_{log kl} | PROVED (trivial) |
| 9 | Que esa regla dé un cuadrado | OPEN |
| 10 | Signo global | OPEN |
