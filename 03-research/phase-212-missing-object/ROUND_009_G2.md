# Ronda 9, G2: recursión con dato de etapa dependiente de la historia

Notación del brief común: a_T(F) = Arch(F) − Σ_n v_n c_F(log n) sobre P_T, v_n = 2Λ(n)/√n, Π_{T,n}(F) = v_n c_F(log n),
T_n = ½ log n. Encargo: buscar una recursión cuyo paso dependa de la historia mediante un dato de etapa con
fórmula propia. Según REVIEW_007 R7-b, el dato no puede ser la pertenencia a un cono ni el minimizador.

## 0. Cotejo en primaria (se hace primero)

| Familia | Antecedente (archivo, sección) | Qué se construyó | Dónde y por qué se detuvo |
|---|---|---|---|
| Schur / Verblunsky / Szegő (retícula) | `phase-159-.../G2_B9_R1.md` §§1–3 (l. 82–87) | Positividad ∀N ⟺ \|α_N\| < 1, pero sólo si los contactos están en una retícula hℤ | log 2/log 3 ∉ ℚ: no hay retícula. El muestreo en retícula es thm:AL (RETRACTED → AL′, déficit Θ(1/M)); el cálculo de saltos discreto es la reformulación Kreĭn/KEP, EQUIVALENT |
| Schur / Verblunsky como hipótesis de un teorema puente | `phase-201-.../CPOS_CLASS_001.md` §§1–4; `FAMILIES_C_001.md` C5 | «\|α_n\| < 1 ⟹ P ≥ 0» con α_n construidos de (g, a) | Teorema de clase: o el puente es afín en el peine (α: convexidad ⟹ C-E′), o es no lineal con verificación REF-D (β). \|α_n\| < 1 es la positividad de la medida (rama 2). NO-GO de clase (PROVED en (i), (ii), (γ); tricotomía ARGUED) |
| Cholesky causal / sistema de Kreĭn en la ventana | `G2_B4_R1.md` Obs. S2.4 | Factorización triangular de Gohberg–Kreĭn a lo largo de L²(−T, −T+s); es el análogo continuo de Szegő | Existe ∀T ⟺ la recursión no se rompe ⟺ λ_T > 0. EQUIV (R157_002 filas 38–39). Para este símbolo no acotado, la existencia está OPEN incluso en una sola ventana |
| Sistemas canónicos / de Branges | índice 04 l. 410, 457, 467 (G1_B8, G2_B5); 03 ES-16, P0-3, P64 | Núcleo de Suzuki, normas de Nehari, sistema de de Branges en tiempo de ventana | REF-D (reformulación de D, no cerrada). Problema del germen H_∞, sin dλ/dT utilizable. P64: puente falso |
| Matriz de transferencia por primos | `R162_2701` (índice 04 l. 817); `ROUND_005_G4.md` §0 | T_p = E_{log p} C_p E_{log p}^{-1}, boost con tanh θ_p = p^{−1/2} | Es J-unitario para todo coeficiente de reflexión y no detecta ningún falsificador (borrado, Beurling, Λχ₂). NO-GO [W12] |
| Inducción en la ventana / Riccati de Kreĭn–Bellman–Siegert | `R162_802` §§4–5; `BARRIER_W_001` §§1–6; `ROUND_005_G4` Lemas 1–3; README l. 141 (SPEC_A) | Flujo en T. La identidad Λ∗1 = log actúa como desplazamiento de ventana | Lineal en el peso. En el cruce el peso entrante no influye (lem:contA). El único dato de Λ en un cruce es c_{h*}(log n). SPEC_A: el paso hereda λ_A ≈ exp(−13e^{2T}) |
| Jacobi inverso / momentos / OPUC | índice 01 R5-06, F-06; 03 P33-6, P34-3, P61 | Jacobi T_N reconstruido desde el lado espectral; e_k ≥ 0 | DEAD: ciego a los falsificadores; 2N momentos sólo dan N coeficientes |
| Sturm / nodal / Courant | README l. 36, 559, 561; 04 l. 264, 395, 672 | Conteos de oscilación, arena | DEAD (arena ≥ 12 modos, no PF₂; Courant–Sturm NO-GO de clase) |
| Darboux / conmutación / Riccati SUSY | RULES_AVOID J8 (fase 70); FAMILIES_C (Riccati/SUSY, rama β); P1_BBSTAR_001 | A = B*B (+ desplazamiento) con el peine como superpotencial | BB* NO-GO PROVED en la clase convolutiva y término a término. «∃B» ⟺ 𝒲 ⪰ 0 |
| Cadena de Sonin semilocal | índice 04 l. 123 (R186_010–015); fases 183–186 | Cadena F_S, A_S, Π_S PROVED para todo S finito | PARTIAL, sin signo: la inercia del resto en P_T sigue OPEN |
| Transferencia recursiva | `phase-210-.../RECURSIVE_TRANSFER_001.md` §1 | Serie geométrica exacta de A_{p⁶} en función de A_1 a escalas D/N(p)^j | Otro problema (densidad de ceros en cuerpos cúbicos). No aporta signo a a_T |
| Descenso por escalas, recurrencia de frontera | `phase-211/POWER_DESCENT_016` §§2–4, `POWER_RECURRENCE_BOUNDARY_036` §§5–7 | Diferencias finitas positivas a orden fijo; energía de frontera → 0 | Figura en la memoria de selecciones rechazadas: el resto conserva la obligación de signo |
| Predicado de etapa con paso uniforme | `ROUND_007_B` Lemas 1–2 | — | Equivale a un reparto local (§Q2) |
| Determinantes de Szegő–Widom | índice 04 l. 39 (W-det), l. 924 (R164_502c) | — | NO-GO: todo determinante que decida el signo factoriza λ_A·R; el símbolo nunca es positivo |

**Conclusión del cotejo (CITED, en primaria).** Las siete familias clásicas del encargo están en el corpus. Cada
una terminó de una de dos maneras:

- (a) **Reparametrización exacta.** Los parámetros de etapa (α_k de Schur, pivotes de Cholesky/LDL, factor
  causal de Kreĭn, hamiltoniano canónico) son una biyección del Gram. Que permanezcan en la región equivale a
  la positividad, y calcularlos exige invertir el Gram de la etapa anterior. Ése es el patrón J3 / REF-D.
- (b) **Factores ciegos al peso.** El boost de R162_2701 y la matriz de Jacobi de RH5 no detectan ningún
  falsificador.

## 1. Búsqueda de una recursión fuera de esas entradas

Exigencias del encargo: (i) indexación por orden de entrada; (ii) actualización que use la aritmética de n;
(iii) región nombrada; (iv) ruptura nombrada bajo los tres controles.

### 1.1 Dos restricciones estructurales (aplican a toda candidata)

**Lema A (la identidad de divisores es ciega a Beurling; CITED + PROVED trivial).** Sea (𝒩, Λ_𝒩) un sistema de
enteros generalizados de Beurling con log como norma. Entonces Σ_{d|ν} Λ_𝒩(d) = log ν para todo ν ∈ 𝒩, por la
definición de Λ_𝒩 como −(ζ_𝒩'/ζ_𝒩). Por tanto, una actualización que sólo use (ii) en la forma
Σ_{d|n} Λ(d) = log n, junto con la estructura de monoide libre, se ejecuta sin cambios sobre el peine de
Beurling. Por FAMILIES_A_001 G1 (PROVED, CITED), el monoide libre ℕ^× no distingue ζ de Beurling. En
consecuencia, el control (iv)-Beurling sólo puede fallar si el paso usa además la estructura aditiva de ℕ: qué
entero entra después de cuál, o la relación de log n con log(n−1). ∎

**Lema B (el instante de entrada está vacío; CITED).** Si la cadena se indexa por la ventana que crece pasando
por T_n, el contacto n aporta 0 a todo orden en el cruce (Paper 47 lem:contA; 211 ROUND_008_C Prop. 2.3;
ROUND_005_G4 Lema 1). Entre cruces el peine está congelado. Todo dato de etapa que se actualice «en la entrada
de n» se actualiza, por tanto, con un incremento que no depende de v_n en el cruce. Su dependencia de v_n sólo
puede aparecer a lo largo de [T_n, T_{n+1}), es decir, por transporte. Por BARRIER_W_001 §6, la derivada en ese
tramo es v_n c_{h*_T}(log n), que se lee sobre el minimizador (J3).

Consecuencia (ARGUED): con la indexación por ventana, la «fórmula propia» del dato no puede ser una regla de
salto en T_n. Tiene que ser una ley de transporte en T, no lineal en el peso, que no pase por h*. Es exactamente
el residuo que R162_802 §5 dejó sin objeto. Con la indexación por n a T fijo (añadir Π_{T,n} en orden de n), el
Lema 1 de ROUND_007_B obliga a que el dato no sea de cono.

### 1.2 Candidata 1: cadena de Schur sobre el grupo ordenado ℚ_{>0}^×

**Idea.** Los log p son linealmente independientes sobre ℚ (factorización única, PROVED). Por tanto, el orden
de ℝ restringido a log ℚ_{>0}^× ≅ ℤ^{(∞)} es un orden total de grupo, y en él entran los contactos log n en el
orden de n. Por Helson–Lowdenslager (CITED: predicción en grupos ordenados), las formas de Toeplitz sobre un
grupo con orden total admiten una recursión de Schur/Szegő a lo largo del orden, con un parámetro por cada
elemento que entra.

**Filtro de cuatro puntos.**
1. *Antecedente:* G2_B9_R1 §3 (la retícula es necesaria para Verblunsky) y AUDIT_PHASE193 fila 26 / CA_C_002
   Prop. 2 (Helson H²(𝔻^∞), toro frente a recta, RD + CIRC). También CPOS_CLASS_001 (rama β).
2. *Nuevo:* sustituir la retícula hℤ por el orden total de ℚ_{>0}^× inducido por la recta. Esto evita la
   objeción «log 2/log 3 ∉ ℚ» de G2_B9_R1.
3. *Por qué evitaría la dificultad:* no la evita. La forma a_T no es de Toeplitz sobre ℚ_{>0}^×, porque Arch
   tiene núcleo continuo en ℝ y no está soportado en log ℚ^×. Su compresión a log ℚ^× es el levantamiento
   toro/recta de CA_C_002 Prop. 2, que ya se clasificó como RD + CIRC. Además, aunque existiera, los parámetros
   de Helson–Lowdenslager se calculan proyectando sobre el pasado, es decir, invirtiendo el Gram (§0 (a)). Es
   REF-D y J3.
4. *Conexión global:* sería «|α_r| < 1 para todo r ∈ ℚ^×, r < e^{2T}». Esto equivale a la positividad sólo para
   la forma discreta, no para a_T.

**Veredicto:** no pasa. Es repetición de CA_C_002 Prop. 2 más CPOS rama β.

### 1.3 Candidata 2: parámetro de Schur multiplicativo (la mejor de la búsqueda; sin objeto)

**Enunciado deseado.** Ventana fija T. Cadena por n creciente, Q_N := Arch − Σ_{n≤N} Π_{T,n} sobre P_T. El dato
de etapa es un parámetro escalar o de rango finito ρ_N(T), con una regla

  ρ_n = Φ_T(ρ_d : d | n, d < n ; ρ_{n−1} ; log n),

que cumpla:
- (iii) Q_N ⪰ 0 para todo N ⟸ ρ_n ∈ 𝔇 (región fija) para todo n;
- (ii) Φ usa los divisores (Σ_{d|n}Λ(d) = log n) **y** el predecesor aditivo n − 1. Por el Lema A, sin el
  predecesor aditivo el paso no puede fallar bajo Beurling.

**Filtro de cuatro puntos.**
1. *Antecedente:* ROUND_005_G4 §0 (dato de puerto con actualización exacta por cruce, R162_2701); R162_802 §5;
   ROUND_007_B §1 (lectura final: el dato tiene que llevar el signo).
2. *Nuevo:* sólo la exigencia combinada «divisores + predecesor aditivo» en la regla de paso. No tengo Φ.
3. *Evitaría la dificultad* de R162_2701, cuyos factores dependen de un solo primo y son J-unitarios para
   cualquier peso, porque haría depender el paso de n de la historia multiplicativa (los ρ_d) y de la aditiva
   (ρ_{n−1}). Pero no tengo una fórmula, así que no puedo comprobar que el dato no sea el pivote de Cholesky
   del Gram en la base ordenada. Si lo fuera, estaríamos en el caso (a) de §0.
4. *Conexión global:* (iii) para todo T. Sin Φ no hay identidad.

**Primer caso no trivial (blanco, no resultado).** T ∈ (½ log 4, ½ log 5), contactos {2, 3, 4}, donde
ROUND_007_B §3 sitúa el primer cuadrado faltante. La entrada de 4 = 2·2 es la primera en la que la regla tiene
un divisor propio no trivial: Λ(4) = log 4 − Λ(2) − Λ(1) = log 2, y su predecesor aditivo es 3. Falsificadores
de la regla de divisores en ese caso (PROVED, aritmética):
- c = 2: Σ_{d|4} 2Λ(d) = 4 log 2 ≠ log 4. La regla, que recibe log 4 y ρ_2, asigna a 4 el peso log 2, mientras
  el peine tiene 2 log 2. El paso 3 → 4 debería dejar ρ_4 fuera de 𝔇.
- Borrado de 4: Σ = log 2 ≠ log 4. Mismo paso.
- Borrado de 2 (con 4 conservado): falla la entrada de 2 y, a través de ρ_2, la de 4.
- Beurling: la regla de divisores se conserva (Lema A). Sólo el término en ρ_{n−1}, es decir 3 → 4, con
  log 4 − log 3, puede romperse. **Ésa es la línea que Φ tiene que contener.**

Que la ruptura bajo c = 2 deje el resto con signo negativo, y no sólo «rompa la identidad», requiere conocer
Φ y 𝔇 (disciplina R3-i). No lo afirmo.

**Veredicto:** no pasa la puerta: no hay objeto. Queda registrada la operación que falta (§2).

### 1.4 Candidata descartada sin desarrollo

Una cadena de Sturm/Jacobi en la base de Dirichlet de la ventana, con un salto por cada contacto: se descarta
por arena ≥ 12 modos (thm:arena), por RFIN_TRACT_001 (n₋(𝔄_N) = 1, REF-D) y por CS0_COMMUTE_001.

## 2. Resultado

Ninguna candidata sobrevive. Las recursiones clásicas del encargo se clasifican así: reparametrizaciones exactas
del Gram (REF-D/J3), factores ciegos al peso, o teoremas puente de la clase CPOS. La mejor dirección es la
candidata 2.

**La operación que falta**, precisa: una regla explícita ρ_n = Φ_T(ρ_d (d|n), ρ_{n−1}, log n) que no se obtenga
invirtiendo ni factorizando el Gram de la etapa. Debe cumplir dos condiciones:
- en la ventana fija T ∈ (½ log 4, ½ log 5), Q_4 ⪰ 0 ⟸ ρ_2, ρ_3, ρ_4 ∈ 𝔇;
- el paso 3 → 4 debe sacar ρ_4 de 𝔇 con c = 2, al borrar 4, y bajo un peso de Beurling. En este último caso
  la causa debe ser el término aditivo log 4 − log 3, porque la parte de divisores es ciega a Beurling (Lema A).

Por el Lema B, si la cadena se indexa por ventana en lugar de por n, Φ tiene que ser una ley de transporte en T,
no un salto en T_n.

## 3. Lista de afirmaciones

| # | Afirmación | Etiqueta |
|---|---|---|
| 1 | Las siete familias del encargo figuran en el corpus con el desenlace de la tabla de §0 | CITED (lectura en primaria; no exhaustiva) |
| 2 | Dicotomía «reparametrización del Gram / factor ciego» como resumen de esos desenlaces | ARGUED |
| 3 | Lema A: Σ_{d\|ν}Λ_𝒩(d) = log ν en todo sistema de Beurling; una regla que sólo use divisores y el monoide es ciega a Beurling | PROVED (trivial) + CITED (FAMILIES_A G1) |
| 4 | Lema B: el contacto n aporta 0 en el cruce; un salto en T_n no lee v_n | CITED (lem:contA, 211 ROUND_008_C, G4) |
| 5 | Con indexación por ventana, el dato debe ser una ley de transporte no lineal sin h* | ARGUED |
| 6 | Independencia lineal de los log p y orden total de ℚ_{>0}^× | PROVED |
| 7 | Candidata 1 (Helson–Lowdenslager en ℚ_{>0}^×): repetición de CA_C_002 Prop. 2 + CPOS β | NO-GO (repetición), ARGUED |
| 8 | Candidata 2: sin objeto; queda registrada la operación que falta | OPEN |
| 9 | Desajustes de la regla de divisores en n = 4 bajo c = 2 y bajo el borrado de 4 | PROVED (aritmética) |
| 10 | Que esos desajustes produzcan un resto negativo | OPEN (requiere Φ, 𝔇) |
| 11 | Candidata Sturm/Jacobi en la base de Dirichlet: descartada por thm:arena, RFIN_TRACT_001, CS0_COMMUTE_001 | CITED |
| 12 | Signo global | OPEN |
