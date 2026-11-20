# Ronda 7, B — predicado de etapa para la inducción por primos

Notación del brief común: a_T(F) = Arch(F) − Σ_n v_n c_F(log n) sobre P_T; Π_{T,n}(F) := v_n c_F(log n);
𝔪_T := Arch. Una «etapa» es un conjunto S de contactos ya incorporados; Q_S := 𝔪_T − Σ_{n∈S} Π_{T,n}.

## 0. Filtro de cuatro puntos

**(1) Antecedente más cercano, leído en primaria.**
- `ROUND_005_G2.md` §3 «Teorema de cierre que habría que probar»: predicado I(Q, S) con (i)–(iv); (iv) abierto;
  el predicado trivial I(Q,S) := «Q + Σ_{p∉S}Π_{T,p} ⪰ 0» es (★)_T (patrón J3). Lema 2: semigrupos aditivos con
  índice acotado, NO-GO para T > ½ log 2.
- `phase-122-.../P122_018_...COCYCLE_PARITY_NO_GO.md` §§1–4: etapas Γ_ℝ∏_{p∈S}Z_p con ecuación funcional torcida;
  acoplamiento simétrico nulo; el causal es la historia entrante.
- `phase-197-barrier-theorem/BARRIER_W_001_...md` §§1–6: W1 (n₋ monótono en T, cruces de una sola signatura),
  W2 (segmentos en el peso), §6 (el único dato propio de Λ en un cruce es c_{h*}(log n)).
- `REVIEW_005.md` R5-d y `ROUND_005_G4.md` Lemas 1–3 (en el cruce el peso entrante no influye).
- `RULES_AVOID.md` §O y `ROUND_006_WINDOW_SPLIT_NUMERIC.md` §10 (reparto DIR existe hasta T ≈ 0.695; en 0.70
  falta un cuadrado).

**(2) Objeto o afirmación nueva.** No encontré un predicado candidato. Lo nuevo es un lema de reducción
(§1, PROVED): todo predicado de etapa cuyo paso sea *uniforme en la historia* (dependa sólo del contacto
entrante) y que sea de tipo cono convexo trasladado o de inercia acotada equivale a un reparto local con
incrementos en el cono; es decir, cae en la clase O / `G2_B8` o en L6. Más una observación (§3, NUMÉRICO
+ ARGUED) sobre dónde aparece el primer cuadrado faltante: inmediatamente después de la entrada de la
potencia 4 = 2², no de un primo.

**(3) Por qué evitaría la dificultad.** No la evita: el lema dice exactamente qué tendría que tener un
candidato para escapar (paso dependiente de la historia mediante un objeto transportado no cuadrático con
fórmula propia, que no sea el minimizador). No construyo nada sin esa pieza.

**(4) Conexión con la positividad global.** Para un predicado de cono, (c) sería
a_T + R_∞ ∈ 𝒦 ⟹ a_T ⪰ 0 en P_T para todo T; el lema muestra que, con paso uniforme, esto es la
identidad a_T = 𝔪_T + R_∅ − R_∞ + Σ_n q_n, q_n ∈ 𝒦, es decir el reparto. No hay conexión nueva.

**Veredicto de la puerta:** sin candidato que pase. El resto de la memo justifica el descarte y registra
la operación de reapertura.

## 1. Lema de reducción para pasos uniformes

Sea H := P_T (real, Hilbert). Los Π_{T,n} son formas acotadas en L²(I): |c_F(u)| ≤ ‖F‖².

**Lema 1 (cono convexo; PROVED).** Sea 𝒦 un cono convexo de formas acotadas en H y R_k formas acotadas.
Pongamos 𝒫_k(Q) :⟺ Q + R_k ∈ 𝒦. Son equivalentes:
(a) para toda Q acotada, 𝒫_k(Q) ⟹ 𝒫_{k+1}(Q − Π_{T,n_{k+1}});
(b) q_{k+1} := R_{k+1} − R_k − Π_{T,n_{k+1}} ∈ 𝒦.
*Demostración.* (b)⟹(a): Q − Π + R_{k+1} = (Q + R_k) + q_{k+1}, suma de dos elementos del cono.
(a)⟹(b): Q := −R_k cumple 𝒫_k (0 ∈ 𝒦 por ser cono cerrado bajo escalares ≥ 0, tomando 0·x); (a) da
q_{k+1} ∈ 𝒦. ∎
Consecuencia: la cadena completa es a_T + R_∞ = (𝔪_T + R_0) + Σ_k q_k con q_k ∈ 𝒦. Con 𝒦 = formas ⪰ 0 en H
es el reparto local por contacto de §O (con potencias de primo como contactos separados). Con 𝒦 ⊋ PSD,
(c) exige un argumento final aparte que use Λ, y ese argumento es el objetivo.

**Lema 2 (inercia acotada; PROVED en dimensión finita, ARGUED a nivel de forma).** Sea 𝒫_k(Q) :⟺
n₋(Q + R_k) ≤ r en H, con dim H ≥ r + 2. Si D := R_{k+1} − R_k − Π_{T,n_{k+1}} no es ⪰ 0, existe Q con
𝒫_k(Q) y no 𝒫_{k+1}(Q − Π).
*Demostración (dimensión finita).* Sea v unitario con ⟨Dv,v⟩ = −δ < 0. Tomemos E ⊥ v de dimensión r,
V := (E ⊕ ℝv)^⊥ y X := N P_V − N P_E (con P proyecciones ortogonales), X v = 0; n₋(X) = r. Sea Q := X − R_k.
En E ⊕ ℝv, X + D tiene bloque −N + O(‖D‖) en E y ⟨Dv,v⟩ = −δ en v; los acoplamientos con V se eliminan por
Schur con error O(‖D‖²/N). Para N grande la restricción a E ⊕ ℝv es definida negativa y n₋(X + D) ≥ r + 1. ∎
A nivel de forma (H de dimensión infinita) el mismo argumento con E, v en un subespacio finito y N P_V en
el complemento vale porque D es acotada; lo dejo ARGUED por no escribir los detalles de dominio de Arch.
Consecuencia: predicados de inercia con paso uniforme también exigen incrementos ⪰ 0; caen en L6/W1 o en §O.

**Lectura.** (b) del encargo, leído como «enunciado sobre un contacto», sólo tiene contenido si el paso no
es uniforme en Q; pero entonces 𝒫_k debe transportar un dato de la etapa (no sólo pertenencia), y ese dato
es el que tiene que llevar el signo.

## 2. Direcciones examinadas, una por una

| Dirección | Entrada cerrada en la que cae | Operación que la reabriría |
|---|---|---|
| Par (forma, medida o núcleo auxiliar positivo) con parte negativa consumida por el siguiente contacto, regla fija | Lema 1 ⟹ reparto con q_n ⪰ 0: §O (O1, O3), `G2_B8_R4` §1, `G2_B8_R5` Teor. D; datos §10.2: falla desde T ≈ 0.70 en la clase DIR | Fórmula cerrada de la parte negativa transferida (un cuadrado λℓ⊗ℓ en T ∈ (0.695, 0.72)) como término nombrado de otro contacto (reapertura de §O) |
| Inercia + subespacio negativo de descripción fija | Lema 2; L6, BARRIER_W_001 W1 (n₋ monótono, comb-genérico) | Una condición independiente de la ecuación de Euler–Lagrange sobre el núcleo (W3(b)): ninguna conocida |
| Comparación con Arch en un subespacio que se achica con k | Si el subespacio es {c_F(log n) = 0 para contactos posteriores}, son condiciones cuadráticas, no lineales: P47 lem:degen, §P (P1). Si es lineal y de descripción previa, §P exige dimensión creciente e identidad en todo P_T | Un S_T lineal escrito sin resolver el problema (reapertura de §P) |
| Ventana móvil: etapa k = T ∈ [T_k, T_{k+1}), T_k = ½ log n_k | R162_802 §§4–5, R162_2701, BARRIER_W_001 §6, R5-d. En T_k el peso entrante es invisible (Lema 1 de G4); entre contactos el peine está congelado y sólo actúa el crecimiento de la ventana, que lleva a negativo todo peine finito | Ver §2.1 |
| Etapas con ecuación funcional torcida (Γ_ℝ∏_{p∈S}Z_p) | P122_018 (acoplamiento simétrico nulo, el causal es la historia entrante 𝓛_{T,−}), G2 Lema 3 | Leer el cociclo de forma no simétrica con un término de signo nuevo: no encontrado |
| Intervalo admisible del peso entrante, J_{k+1}(T) ∋ v_{n_{k+1}} | R5-d Lema 2: es el objetivo (J3) | — |

### 2.1 Qué tendría que añadir un predicado acoplado ventana–primo

Un predicado acoplado natural es con margen: 𝒫_k :⟺ λ_A(T) ≥ m_k(T) en [T_k, T_{k+1}) con m_k explícito.
El paso exige: (i) que el déficit causado por el crecimiento de la ventana en el hueco congelado
[T_{k+1}, T_{k+2}) quede por debajo de la ganancia del contacto n_{k+1}; (ii) ésta, por Hellmann–Feynman,
es v_{n_{k+1}} c_{h*}(log n_{k+1}) sobre el minimizador (BARRIER_W_001 §6, Teorema X, W-fam). El predicado
debería añadir una cota inferior de c_{h*_T}(log n) que no pase por h* — exactamente el muro registrado.

Restricción adicional de los datos (NUMÉRICO, ROUND_006 §10.3): en T = 0.70 la forma es positiva sólo para
c en un intervalo de anchura ≲ 10⁻³ alrededor de 1, y el fondo en c = 1 es 7·10⁻⁸ (0.70) y 10⁻⁹ (0.75) en esa
discretización. ARGUED: ningún predicado con holgura abierta en el peso (estable por perturbación cΛ de
orden 10⁻³) puede servir en T ≥ 0.70; el paso tendría que ser una identidad o una desigualdad sin holgura
uniforme, lo que reafirma que la regla fija de un cono (Lema 1) no basta y que la reabertura debe ser exacta.

## 3. Observación sobre el primer cuadrado faltante (NUMÉRICO + ARGUED)

½ log 4 = log 2 = 0.6931 y el umbral DIR está en (0.695, 0.70): el primer cuadrado faltante aparece justo
tras la entrada del contacto n = 4. En el óptimo q₂ (que contiene Π_{T,2} + Π_{T,4}) lleva el único autovalor
negativo y ℓ se parece a la proyección de cos(2πt/log 2) sobre P_T (solapamiento 0.91–0.93). Lectura (ARGUED,
no verificada con 4 separado): la etapa debe indexarse por potencias de primo, y la transferencia necesaria
es entre la «familia de 2» y el arquimediano/3 justo cuando el término 2² entra. Esto fija el **primer caso
no trivial** que cualquier futura candidata tendrá que resolver: T ∈ (½ log 4, ½ log 5), contactos {2, 3, 4},
con un cuadrado explícito ℓ_T. Falsificadores en ese caso: borrar 4 (cambia q₂ y, en esos datos, el fondo);
c = 2 (forma negativa); Beurling: la frecuencia de ℓ ≈ 1/log 2 debería moverse con la retícula.
No tengo fórmula para ℓ_T, así que esto no es una candidata, sólo el blanco de prueba.

## 4. Resultado

Sin candidata que pase la puerta. Las direcciones del encargo caen en §O, §P, L6/BARRIER_W_001, P122_018 o
R5-d, y los Lemas 1–2 explican por qué: un paso que dependa sólo del contacto entrante es un reparto local
con incrementos en el cono. Reapertura precisa: un predicado de paso no uniforme que transporte un dato
de la etapa con fórmula propia (no el minimizador, no la pertenencia a un cono), cuya primera instancia
escriba ℓ_T en T ∈ (½ log 4, ½ log 5) como cuadrado compensado por un término nombrado, con la línea que
se rompe en c = 2 y al borrar 4.

## 5. Lista de afirmaciones

- Lema 1 (predicado de cono con paso uniforme ⟺ incrementos en el cono; cadena = reparto): PROVED.
- Lema 2 (inercia acotada con paso uniforme exige incremento ⪰ 0): PROVED en dimensión finita; ARGUED a
  nivel de forma.
- Clasificación de las seis direcciones en entradas cerradas (§2): ARGUED (cotejo en primaria de los
  antecedentes citados; no exhaustivo).
- §2.1, el predicado acoplado con margen necesita una cota de c_{h*}(log n): ARGUED (reducción a BARRIER_W_001 §6).
- Ventana en c de anchura ≲ 10⁻³ y fondo 10⁻⁸–10⁻⁹: NUMÉRICO (citado de ROUND_006 §10.3); consecuencia
  «sin holgura abierta en el peso»: ARGUED.
- Coincidencia del umbral DIR con la entrada de n = 4: NUMÉRICO (umbral) + aritmética; lectura «etapas
  por potencias de primo»: ARGUED.
- Existencia de un predicado de etapa con fórmula propia: OPEN.
