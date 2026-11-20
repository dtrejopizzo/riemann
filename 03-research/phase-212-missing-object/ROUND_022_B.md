# Ronda 22, memo B — la reformulación «blanda» con una norma fuerte

Postura asignada: objetivo blando, a_T(F) ≥ −ε(T)·N(F) con ε(T) → 0 y N una norma fija, independiente de T,
tan fuerte como se quiera. Conclusión anticipada: la reformulación es **exactamente** el objetivo para *toda*
N finita sobre un núcleo de forma. La causa es el congelamiento (P47 lem:wit-freeze): para F fija, a_T(F) no
depende de T, así que no hay ninguna cantidad que pueda tender a 0. No hay brecha en el lema ni condición
oculta sobre la fuerza de N. Es el caso (a) del encargo, en una forma más fuerte que la prevista, y el filtro
detecta repetición.

## Filtro de cuatro puntos (cotejo primero)

1. **Antecedente más cercano (leído en primaria).** P47 `thm:wit-Tc`(i),(iv) (main.tex l.6995–7027):
   la extensión por cero conserva a_T, y λ_A ≥ −ε(T) con ε → 0 equivale al objetivo. P47 `lem:wit-freeze`
   (l.7029–7043): para un F congelado, a_T, c_F, el término del peine y la pertenencia a P_T no dependen de T.
   P47 `thm:wit-asym` (l.7045–7060) y el comentario que le sigue: «any limit law … says nothing about frozen
   witnesses beyond what the corresponding statement at the window T_0 says». P47 prop. «no asymptotic slack»
   (e) (l.8848–8851). Índice maestro: l.109 (`λ_A ≥ −ε(T)` ya basta, R6), l.3953 y l.11663 (lem:wit-freeze,
   NO-GO: «frozen tests see nothing new as T grows»), l.4394 y l.12909 (R6, mitad inferior de la ley
   bilateral, OPEN). RULES_AVOID §F: la mitad inferior es el objetivo más un margen (211/ROUND_007_D Lema 4.6,
   l.193), y 211/LEDGER C20 da NO-GO para la ley exponencial simple.
2. **Lo nuevo.** El enunciado con N(F) en lugar de ‖F‖² o de 1 no figura textualmente en el corpus. El
   Lema 1 de abajo prueba que no aporta nada, ni siquiera de forma débil: para cualquier N la versión blanda
   equivale literalmente al objetivo, y la equivalencia vale punto por punto en cada F.
3. **¿Esquiva la dificultad del antecedente?** No. La dificultad de thm:wit-Tc(iv) es que la holgura ε(T) no
   puede actuar sobre tests congelados. Una norma fuerte no cambia eso, porque N(ιF) = N(F) también queda
   congelada.
4. **Conexión con la positividad global.** Es una identidad lógica (Lema 1), del tipo REF (filtro F5): no
   hay mecanismo de signo.

Hay repetición: la reformulación queda absorbida por lem:wit-freeze + thm:wit-asym. Abajo van el enunciado
exacto (que pide el encargo), las respuestas a las preguntas 1–2 y el diagnóstico del falsificador.

## §1 El lema blando exacto

Notación: a(F) := a_T(F) para cualquier T con supp F ⊂ [−T,T]. Por thm:wit-Tc(i) no depende de T.
Sea 𝒫 := ∪_T P_T (funciones reales con soporte compacto, ∫F e^{±t/2} = 0, en el dominio de forma).

**Lema 1 (PROVED).** Sea 𝒞 ⊂ 𝒫 tal que, para todo T_0, 𝒞 ∩ P_{T_0} es denso en P_{T_0} ∩ 𝒟_{T_0} para la
norma de forma. Sea N: 𝒞 → [0,∞) una función *cualquiera*: no hace falta que sea norma, seminorma ni que sea
continua; basta que sea finita y que dependa sólo de F, no de la ventana. Son equivalentes:
(i) existen T_1 y una ε(T) → 0 tales que a(F) ≥ −ε(T)N(F) para todo T ≥ T_1 y todo F ∈ 𝒞 ∩ P_T;
(ii) a(F) ≥ 0 para todo F ∈ 𝒞;
(iii) λ_A(T) ≥ 0 para todo T.

*Prueba.* (i)⇒(ii): dado F ∈ 𝒞 ∩ P_{T_0}, se tiene ιF ∈ 𝒞 ∩ P_T para todo T ≥ T_0, con a(ιF) = a(F) y
N(ιF) = N(F) (son el mismo objeto). Entonces a(F) ≥ −ε(T)N(F) para todo T grande, y como N(F) < ∞, haciendo
T → ∞ se obtiene a(F) ≥ 0.
(ii)⇒(iii): a_{T_0} es una forma cerrada y acotada inferiormente (P47 lem:compact), así que es continua en
la norma de forma, y la densidad lleva a ≥ 0 a P_{T_0} ∩ 𝒟_{T_0}.
(iii)⇒(i): se toma ε ≡ 0. ∎

**Densidad (PROVED).** Para 𝒞 = C_c^∞ ∩ 𝒫 la hipótesis se cumple. C_c^∞(I_T) es núcleo de forma (P47,
prueba en l.1832–1837, por dilatación y mollificación). Para conservar las dos ligaduras, se fijan
φ_±, χ ∈ C_c^∞(I_T) duales a los funcionales A, B (son L²-continuos y linealmente independientes) y se
corrige la aproximación con una combinación de φ_±; las correcciones tienden a 0. Por tanto N(F) puede ser
‖F‖²_{H^s} + ‖e^{α|t|}F‖², la energía arquimediana + ‖F‖², o cualquier cantidad finita sobre C_c^∞.

**Lo que fuerza el lema.** No obliga a que N sea débil. Obliga a que ε(T) actúe sobre una cantidad que no se
mueve. Toda estimación uniforme en P_T a ventana grande, restringida a los F de soporte ⊂ [−T_0,T_0], es una
cota del número fijo a(F) por −ε(T)N(F) con T libre: es decir, el signo exacto de a(F). Una N más fuerte sólo
achica la clase de F donde la cota tiene que ser exacta, sin vaciarla (contiene a C_c^∞ ∩ 𝒫, que es densa).
Por eso la respuesta es la variante más fuerte de (a): *toda* N admisible da un enunciado idéntico al
objetivo. No hay brecha (b) ni nada real (c).

## §2 Pregunta 1: qué barreras aplican

- **thm:shape (B′)/cor:shape(e)** (estimación con resto, ARGUED en general, PROVED en la precisión
  4·10⁹Te^{−15.449T}). (B′) mide el resto en la normalización del ínfimo sobre la esfera L². Con N fuerte,
  la cota −ε(T)N(F) en la esfera L² sólo es pequeña sobre F con N(F) ≲ ‖F‖², o sea en el «bulk». (B′) no
  excluye *literalmente* el formato −ε(T)N(F). Pero da igual, porque el Lema 1 lo reduce a (ii), que sí cae
  en cor:shape(a)–(e): es el objetivo sin holgura.
- **lem:wit-freeze / thm:wit-asym** (PROVED, clase: «argumentos asintóticos en T», cualquier ley límite).
  **Aplica de lleno.** Es exactamente el paso (i)⇒(ii).
- **cor:shape(c)** (ningún funcional acotado de los pesos decide). Aplica a la mitad (ii): un ε(T)N(F) que
  dependa de los pesos sólo a través de funcionales acotados no puede ser 0 en el límite para Λ y no para
  (1+δ)Λ.
- **Clase TV-robusta / cerrada bajo modificación finita (thm:shape(A), O_1–O_4).** Aplica a (ii): borrar un
  número finito de potencias de primo cambia a(F) en un F congelado con c_F(log n_0) ≠ 0, y la conclusión
  (ii) se vuelve falsa (ver §4).
- **R6 / «W-fam no excluye la mitad inferior»** (índice l.4394). Esto no contradice lo anterior. W-fam no
  excluye λ_A ≥ L(1−o(1)), y el Lema 1 muestra que con cualquier N ese enunciado *es* (ii). No excluido no
  quiere decir más fácil (RULES_AVOID §F).

**La pregunta decisiva: ¿da el error clásico del teorema del número primo un ε(T) → 0 para alguna N?**
(ARGUED, con un núcleo PROVED.) Para F ∈ C_c^∞ ∩ P_{T_0}, el término Σ_n v_n c_F(log n) es una suma
*finita* (n < e^{2T_0}). La fórmula explícita escribe a(F) como la suma de ceros Σ_ρ Φ_F(ρ)Φ_F(1−ρ) (P47,
lectura tras def:wit-model; la usamos sólo aquí, como contexto). P_T elimina exactamente los términos polares
(A = B = 0). Si se reemplaza ψ(x) por x + E(x), con |E(x)| ≪ x·exp(−c√log x), queda
a(F) = [término principal + arquimediano] − ∫ c_F(u) e^{−u/2} dE(e^u), con resto acotado por
R(F) ≍ ∫_0^{2T_0} |(c_F e^{−u/2})′(u)|·e^{u}exp(−c√u) du. Esta cota es **un número fijo** que depende de F,
no de T, y crece como e^{u/2}exp(−c√u) en la escala del soporte. Ninguna N tal que R(F) ≤ ε(T)N(F) puede
tener ε(T) → 0: R(F) no depende de T y en general es > 0. Para que las cuentas cierren con ε → 0 haría falta
R(F) = 0 o una cota con signo para el resto, que es (ii) sin modificar. Ninguna fuerza de N cambia esto: N
puede anular la contribución de F con soporte lejano (pesos e^{α|t|}) o con alta frecuencia (H^s), pero
cualquier F ∈ C_c^∞ ∩ P_{T_0} con c_F ≢ 0 en (0, 2T_0) sigue pidiendo signo exacto. El «bulk» suave no se
puede aislar: los F congelados de escala unidad ya son bulk.

## §3 Pregunta 2: cotejo de antecedentes

- P47 thm:wit-Tc(iv), lem:wit-freeze, thm:wit-asym, prop. (e) «no asymptotic slack». Ya contienen el Lema 1
  con N = ‖F‖² y con la observación sobre los tests congelados; el paso a N general es inmediato y no está
  escrito.
- 211/ROUND_007_D Lema 4.6 y LEDGER C20. La mitad inferior de la ley bilateral equivale a (N1′)
  μ₁ ≥ L + cota de Tate; no hay ninguna versión blanda más débil.
- Índice: l.109 (R6), l.3953/l.11663 (wit-freeze NO-GO), l.4394/l.12909 (R6 OPEN), l.4556 (fase 104:
  «límite profundo ⟺ Blaschke = 1 [REF-D]», puertas de parada). No releí en primaria la fase 160 (R160_*),
  la fase 164 (teorema de la cola), el «cierre de Cesàro» de la fase 62 ni las puertas 102–104; el
  cotejo de esas fuentes descansa en las entradas del índice citadas. Ninguna sugiere que una holgura
  asintótica se salve con normas fuertes. La regla «positivity data do not imply margin data» va en la
  dirección contraria y no afecta al Lema 1.

## §4 Falsificadores (R3-i)

El Lema 1 es una tautología y vale también para las controles: para 2Λ, para el borrado de una potencia de
primo y para un peso tipo Beurling. Lo que falla para cada una es la hipótesis (i), en el paso (i)⇒(ii):

- **2Λ.** Existe un F_⋆ ∈ C_c^∞ ∩ P_{T_0} con a^{2Λ}(F_⋆) < 0 (P47 thm:shape(A), O_4 con c = 1). Una vez
  congelado, a^{2Λ}(ιF_⋆) = a^{2Λ}(F_⋆) < 0 para todo T, así que ningún ε(T)N(F_⋆) → 0 lo acota: el resto
  queda fijo en un valor negativo y no decae.
- **Borrado de n_0.** a^{del}(F) = a(F) + v_{n_0}c_F(log n_0). Si se toma F de soporte < ½log n_0 junto a un
  testigo negativo, o un F_⋆ con c_{F_⋆}(log n_0) de signo adecuado (O_5, CONDITIONAL), la diferencia es
  constante en T y el mismo paso falla.
- **Beurling.** Igual, con el testigo de P47 en la ventana nombrada.

Lectura: el peso verdadero tiene que dar a(F) ≥ 0 *exactamente* en cada F congelado. El parámetro T no
aporta ninguna información. La «suavidad en T» no es un recurso: lo que el peso tiene que proporcionar es el
signo exacto en cada ventana finita.

## Veredicto

**REPETICIÓN / REF (F5).** El Lema 1 (PROVED) muestra que «a_T(F) ≥ −ε(T)N(F), ε → 0» es equivalente al
objetivo para *toda* N finita sobre un núcleo denso, porque a(F) y N(F) quedan congelados al ampliar la
ventana (lem:wit-freeze). La norma fuerte no debilita nada, el error clásico no produce ningún ε(T) → 0 y la
reformulación no tiene brecha. Lo nuevo frente al corpus es sólo el paso de ‖F‖² a una N arbitraria,
inmediato a partir de thm:wit-asym. No hay resultado intermedio que valga. Siguiente operación: ninguna
dentro de esta postura.
