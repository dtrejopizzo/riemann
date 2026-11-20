# Ronda 3, opción 5 — el par virial: selección

Memo de selección, no de construcción. Notación de `../phase-211-sign-sandbox/STATEMENT_001.md`;
N = e^{2T}. Etiquetas: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMÉRICO.
Pregunta: ¿existe una identidad exacta de conmutador o virial sobre todo P_T,
a_T(F) = (forma de conmutador con el generador de dilataciones) + ρ_T(F), o una cantidad monótona en T,
en la que m′ y los pesos Λ(n) log n entren con orientación firmada y cuya exactitud use
Σ_{d|k}Λ(d) = log k?

## Cotejo

### Qué se buscó y dónde

Grep sin distinguir mayúsculas de «virial», «pohozaev», «morawetz», «mourre», «positive commutator»,
«conmutador», «hellmann», «dilat», «monoton», «Grönwall», «Hadamard» en todo `03-research/`, en
`04-papers/47*` y `48*`, en el índice de rutas (README y catálogos 01–06), en el grid y en el
crucigrama, y lectura de `RULES_AVOID.md` §§B4, C1, D9, I3–I5, I8. Hubo más de cuarenta archivos con
coincidencias. Se leyeron en primaria: R170_840 (§0 y §§8–9 enteros); R162_501 (entero);
106_124 §§1–2; P121_COMMUTATOR_MOMENT_TOMOGRAPHY_NO_GO (entero); P124_007 (veredicto y §1);
R165_202 (tabla 1.4–1.9); 211/ROUND_008_C (§§0–2 y enunciados de las Prop. 3–6); IDX README, fase 193,
frente I. No se leyeron línea por línea: 106_105, 106_119, 106_41, R162_407, R162_408 ni los G2_* de la
fase 159. Que no se hayan leído no prueba que no contengan la idea.

### (1) Antecedentes más cercanos, leídos en primaria

- **R162_501, Teorema 2.2 (Selberg–virial), PROVED bajo (REG) sobre el radical.** Es justamente la
  pregunta de esta zona. El peso Λ(n) log n del peine derivado se reescribe con
  Λ·log + Λ∗Λ = W := μ∗log². Esa identidad sale de multiplicar Λ∗1 = log por la derivación log, así
  que usa Σ_{d|k}Λ(d) = log k. La ecuación del núcleo absorbe el cuadrado Λ∗Λ. Prop. 3.1: ningún
  término tiene signo determinado, y la reformulación (S-W) es equivalente a 𝒱|_N ≤ 0, es decir a
  VIR–LB. Falsificadores: el argumento cae para Davenport–Heilbronn sólo en la línea W ≥ 0, y **no
  cae** para modificaciones finitas Λ + η con η ≥ 0.
- **106_124 §1.** Con el generador completo, el conmutador de dilatación tiene paridad par. Cada
  potencia de primo aporta la distribución aislada log n·{δ′_{log n} − δ′_{−log n}}, y el conmutador
  es no acotado en ambos signos sobre el núcleo liso par. Proyectar la dilatación da un conjugado no
  local. Bajo el umbral, una estimación de Mourre estricta para él equivale a la ausencia de los
  estados que se querían excluir.
- **R170_840 §8, Prop. 8.1 (PROVED).** VIR–LB y VIR–DET juntas fuerzan R_LG = 0 en una primera
  ventana supuesta. Ambas quedan OPEN, igual que (REG) y la uniformidad en T. El propio memo dice que
  el par «tiene exactamente la fuerza necesaria» para el cierre (§8, tras (8.6)).
- **Monotonía y derivada en T.** R165_202 1.4 da la fórmula de Hellmann–Feynman
  D⁺λ ≤ −𝒱_T(F_T)/T ≤ D₋λ (PROVED bajo (REG)), y su 1.5 da el principio de Hadamard (ARGUED).
  En 211/ROUND_008_C, el Teorema 1 es la versión con multiplicadores de Tate y la Prop. 5 prueba que
  Grönwall en T y (EB_C) son reformulaciones de (★) más una tasa (PROVED). R186_038 α.3 está
  registrado como NO-GO (vacío). PROOF_L_SHARP_H_001 define la clase 𝒦_H, NO-GO ARGUED.
- **Conmutadores con la posición.** En P121 se tiene ad_Q(S_a) = −aS_a. Sobre el radical, los
  conmutadores simples no dan información; el doble conmutador da ⟨QF, HQF⟩ ≥ 0 y la ruta queda
  retirada. P124_007: el conmutador con el multiplicador de Tate se cancela con el defecto de
  proyección.
- **IDX README, fase 193, frente I:** «Virial/Pohozaev (holds for every comb, DH included) … dead».

### (2) Objeto realmente nuevo

**No hay ninguno que pueda escribir con mecanismo de signo.** La pregunta pide una forma
exacta en todo P_T y no sólo en el radical. En esa forma sólo es nuevo, respecto de los antecedentes,
lo que delimitan los dos lemas de §1: una forma de conmutador con multiplicadores traslación
invariantes es una tautología (Lema 1), y la identidad a_T = κ·𝒱 + ρ con ρ acotada inferiormente es
falsa (Lema 2). La identidad de Selberg–virial en todo P_T es la de R162_501 sin el paso 5, o sea
sin la ecuación del núcleo. En su lugar aparece un apareamiento cruzado −⟨τ Im z_c F, S_T F⟩ sin
signo, del mismo tipo que el residuo de I4 (§2). No se escribe ℋ_T, V_T ni ρ_T.

### (3) Por qué el cambio no evita la dificultad del antecedente

En el radical, la ecuación del núcleo es lo que convierte Λ∗Λ en datos arquimedianos (R162_501,
paso 5). Fuera del radical ese paso no existe, y el cuadrado del peine vuelve como un cruce sin signo
con S_T. Pasar del radical a todo P_T empeora la dificultad: el término comb del virial no es
relativamente acotado por a_T (Lema 2). Ninguna identidad de la forma pedida puede tener resto
acotado inferiormente.

### (4) Identidad o desigualdad que conectaría con la positividad global

Las únicas identidades exactas que conectan el virial con λ_A son la fórmula de variación en T
(R165_202 1.4; 211/ROUND_008_C Teor. 1) y la suficiencia VIR–EP ⟹ R_LG = 0 (R170_840 Prop. 8.1).
Ambas viven sobre minimizantes o vectores del radical. Sobre todo P_T, la desigualdad
«a_T ≥ κ𝒱 − C‖·‖²» es falsa para todo κ ≠ 0 y todo C cuando T > ½ log 2 (Lema 2). La versión
Grönwall está demostrada como reformulación de (★) más una tasa (211/ROUND_008_C Prop. 5).

¿Más débil o equivalente? VIR–EP está cuantificada sobre ventanas de primer contacto supuestas.
Cuando no hay contacto es vacía, así que no da un enunciado intermedio que se pueda probar por
separado. Su contenido, junto con (REG), es el del cierre (R170_840 §8; CITED). La forma global
a_T = κ𝒱 + ρ, ρ ≥ 0, no es ni más débil ni equivalente: es **falsa** (Lema 2).

### (5) Líneas que se rompen para cΛ y a_P

En la identidad de Selberg–virial, la única línea que distingue los pesos es W_a := a·log + a∗a = μ∗log².

- **cΛ, c ≠ 1:** W_{cΛ}(p) = c log²p ≠ log²p, y W_{cΛ}(pq) = 2c² log p log q. La identidad
  W_a = μ∗log² falla en n = p para todo c ≠ 1 (PROVED, por cálculo directo).
- **a_P:** W_{a_P}(n) = W(n)·1[todos los factores primos de n son ≥ P] (Lema 3). La identidad falla
  exactamente en n = p < P y en los n con algún primo pequeño. Las propiedades estructurales
  (W1)–(W3) de R162_501 se conservan en el soporte. La separación es «conocer Λ en [2,N)», o sea
  identificación lineal, ya registrada (RULES_AVOID I2, K4).

Lo que no se rompe: el signo. Ninguna orientación firmada del virial sale de estas líneas
(R162_501 Prop. 3.1), y el falsificador Λ + η, η ≥ 0, ya hace fallar cualquier signo basado en W ≥ 0.

**Veredicto del cotejo: repetición.** Por regla 3 del brief, la memo terminaría aquí. Se añaden sólo
los tres lemas cortos y completos que delimitan la clase, porque responden a la pregunta «en todo P_T».

## 1. Dos lemas de formato

Sea D el generador unitario de dilataciones, (U_rF)(t) = r^{−1/2}F(t/r). En Fourier,
(U_rF)^(τ) = r^{1/2}F̂(rτ). Para F real con c_F ∈ C¹ (por ejemplo F ∈ C_c^∞(I_T)) se define

    𝒱_T(F) := (1/2π)∫ τ s_T′(τ)|F̂(τ)|² dτ
            = (1/2π)∫ τ m′(τ)|F̂|² dτ − Σ_{log n<2T} v_n log n · c_F′(log n).

La igualdad se debe a que 2π c_F(u) = ∫ cos(τu)|F̂|², de donde ∫ τ sin(τu)|F̂|² = −2π c_F′(u). Es el
virial de R170_840 (8.1) sin el término de Tate del radical. Además
𝒱_T(F) = −(d/dr)|_{r=1} (1/2π)∫ s_T(τ)|(U_rF)^(τ)|² dτ: es la forma ⟨F, i[D, S_T]F⟩ con la
convención de signo de R162_407.

**Lema 1 (tautología en la clase de multiplicadores; PROVED).** Sea s una función real, par y
continua. Sea x(τ) := ∫_1^{|τ|} s(σ)σ^{−1} dσ para τ ≠ 0. Entonces τ x′(τ) = s(τ) para todo τ ≠ 0 y
⟨F, i[D, X]F⟩ = (1/2π)∫ s|F̂|² para todo F con ∫ |s||F̂|² < ∞, donde X es el multiplicador de símbolo
x y el conmutador se entiende en sentido de formas. En particular, para cualquier sucesión de pesos
a se tiene a_T^{(a)}(F) = ⟨F, i[D, X_a]F⟩ con ρ = 0.

*Demostración.* Para un multiplicador X de símbolo x, U_r X U_r^{−1} es el multiplicador de símbolo
x(τ/r). Derivando en r = 1 se obtiene el símbolo −τx′(τ) para i[D,X], salvo la convención de signo
fijada arriba. Por construcción τx′ = s, y la forma es (1/2π)∫ s|F̂|². ∎

Consecuencia. En la clase de conmutadores de D con multiplicadores traslación invariantes, toda
identidad «a_T = conmutador + ρ» es un reparto del símbolo s_T = σ₁ + σ₂. Vale para todo peine, de modo
que no se rompe para cΛ ni para a_P (patrón B1), y el signo del conmutador es literalmente (★).

**Lema 2 (el virial no es relativamente acotado por a_T en P_T; PROVED).** Sea T > ½ log 2. Para
todo κ ∈ ℝ∖{0} y todo C ≥ 0 existe G ∈ P_T ∩ C_c^∞(I_T) con a_T(G) − κ𝒱_T(G) < −C‖G‖². Por tanto
no existe identidad exacta a_T = κ𝒱_T + ρ_T sobre P_T ∩ C_c^∞ con ρ_T ≥ −C‖·‖².

*Demostración.* Sea ℓ = log 2. Sea φ ∈ C_c^∞(−1, 1) real con ‖φ‖ = 1. Entonces c_φ es par, de clase
C¹ y no constante, de modo que existe θ con c_φ′(−θ) ≠ 0. Como c_φ′ es impar, el signo de c_φ′(−θ)
se elige cambiando θ por −θ. Sea φ_ε := ε^{−1/2}φ(·/ε). Para ε pequeño se toma

    F_ε(t) = φ_ε(t − t₀) + φ_ε(t − t₀ − ℓ − εθ),

con t₀ tal que el soporte quede en I_T; esto es posible porque ℓ < 2T. Se tiene
c_{F_ε}(u) = 2c_φ(u/ε) + c_φ((u − ℓ − εθ)/ε) + c_φ((u + ℓ + εθ)/ε). Los log n con n ≥ 2 están
separados entre sí y de 0. Para ε pequeño, el único que cae en un soporte es log 2, por el segundo
sumando. Así c_{F_ε}′(log n) = 0 para n ≠ 2, c_{F_ε}′(ℓ) = ε^{−1}c_φ′(−θ) y c_{F_ε}(ℓ) = c_φ(−θ).

Corrección primitiva. Se fijan ψ₁, ψ₂ ∈ C_c^∞(I_T) con det[(A,B)(ψ_i)] ≠ 0; existen porque A y B son
linealmente independientes sobre C_c^∞(I_T). Se tiene |A(F_ε)|, |B(F_ε)| ≤ 2e^{T/2}‖φ‖₁ε^{1/2}.
Entonces G_ε = F_ε − α_εψ₁ − β_εψ₂ ∈ P_T con α_ε, β_ε = O(ε^{1/2}).

Estimaciones:
- s_T′ = m′ + Σ v_n log n sin(τ log n) está acotada (m′(τ) = O(1/(1+|τ|)), CITED de
  211/ROUND_008_C Lema 1.2). Luego |𝒱_T(F,ψ)| ≤ C‖F‖‖τψ̂‖ = O(1), y
  𝒱_T(G_ε) = −v_2 ℓ c_φ′(−θ)/ε + O(1).
- m(τ) ≤ C₁ + log(1 + |τ|) y (1/2π)∫ log(1+|τ|)|F̂_ε|² = O(log(1/ε)), mientras los términos del
  peine están acotados. Luego a_T(G_ε) = O(log(1/ε)), y ‖G_ε‖² → 2.

Se elige el signo de c_φ′(−θ) de modo que κ𝒱_T(G_ε) → +∞ como 1/ε. Entonces
a_T(G_ε) − κ𝒱_T(G_ε) → −∞, más rápido que cualquier −C‖G_ε‖². ∎

Alcance. El Lema 2 usa sólo v_2 ≠ 0. Es una obstrucción de formato, genérica en el peine y sin signo,
como el lema de K1′. Coincide en contenido con la frase de 106_124 §1 («unbounded in both signs on
the even smooth core»), pero aquí se enuncia para a_T sobre P_T y con demostración escrita. **No
excluye:** generadores distintos de D (por ejemplo dilataciones con peso aritmético, o el generador
multiplicativo log x · x d/dx en otras coordenadas); conmutadores con operadores no traslación
invariantes que no sean dilatación pura (la ventana, el defecto de Tate, U_n); restos ρ_T no acotados
inferiormente pero con signo sobre P_T; combinaciones κ(T)𝒱_T con κ dependiente de F o no lineales;
identidades sólo sobre subespacios propios; y la versión del radical (VIR–LB/VIR–DET), que sigue OPEN.

## 2. Selberg–virial en todo P_T (ARGUED, pasos 1–4 de R162_501 sin el paso 5)

Para F ∈ P_T real con c_F ∈ C¹, y z_c, Y, W como en R162_501, los pasos 1–4 no usan la ecuación del
núcleo. Dan

    𝒱_T(F) = (1/2π)∫ τ m′|F̂|² − (1/π)∫ τ Im Y |F̂|² + (1/π)∫ τ Im z_c · m |F̂|²
             − (1/π)∫ τ Im z_c · s_T |F̂|²                     (+ término de umbral si 2T = log n₀).

El último término es el apareamiento cruzado −(1/π)Re⟨M_{τ Im z_c}F, S_T F⟩. En el radical, S_T F
cae en el espacio de Tate y en la fuga exterior; aquí no tiene signo. Es el mismo formato
«−Re⟨X F, S_T F⟩ sin signo y con cota sólo bilateral» de RULES_AVOID I4. Vale para todo peine a con
W_a en lugar de W (R162_501 §3, línea DH), así que no es nuevo y no lleva signo.

**Lema 3 (W de a_P; PROVED).** Para a_P := Λ·1[p ≥ P] (potencias de primos p < P borradas),
W_{a_P} := a_P·log + a_P∗a_P = W·1[todo factor primo de n es ≥ P].

*Demostración.* Si p ≥ P, entonces a_P·log(p^k) = k log²p y a_P∗a_P(p^k) = Σ_{i=1}^{k−1}(log p)² =
(k−1)log²p; la suma es (2k−1)log²p = W(p^k). Si p, q ≥ P son distintos, a_P∗a_P(p^iq^j) =
2 log p log q = W(p^iq^j), y a_P·log se anula allí. Si ω(n) ≥ 3, ambos sumandos son 0. Si n tiene un
factor primo menor que P, a_P(n) = 0 o n no es potencia de primo, y todo par d·(n/d) con a_P(d)a_P(n/d)
≠ 0 tiene ambos factores sin primos pequeños; luego ambos sumandos son 0. ∎

Lectura. Para a_P, la identidad de Selberg falla sólo por soporte, nunca por estructura. El virial de
Selberg distingue Λ de a_P sólo por los valores en los n con primos pequeños, que es identificación
lineal. Para cΛ falla en el valor y en el grado (c frente a c²), pero sigue sin signo.

## Resultado

Sin mecanismo nuevo; repetición de R162_501, 106_124, R170_840 §8, R165_202, 211/ROUND_008_C y
P121. Se agregan dos lemas cortos que delimitan la pregunta «en todo P_T»: un NO-GO de clase (Lema 2)
y una tautología de clase (Lema 1). No hay candidata lista para construcción.

## Qué se probó

- Lema 1 (PROVED): en la clase de conmutadores de D con multiplicadores, la identidad
  a_T = conmutador es tautológica y genérica en el peine, y su signo es (★) literalmente.
- Lema 2 (PROVED, NO-GO con clase): para T > ½ log 2 no existe a_T = κ𝒱_T + ρ_T con κ ≠ 0 y
  ρ_T ≥ −C‖·‖² sobre P_T ∩ C_c^∞. El virial del peine es no acotado en ambos signos relativo a a_T.
- Lema 3 (PROVED): W_{a_P} = W·1[primos ≥ P]. La línea de a_P en el virial de Selberg es sólo soporte.

## Qué falló y por qué

Fuera del radical, el cuadrado Λ∗Λ que produce Σ_{d|k}Λ(d) = log k no se puede absorber: vuelve como
un cruce con S_T sin signo. El virial tiene crecimiento |τ| en el peine frente a log|τ| en a_T, lo que
impide toda identidad con resto acotado inferiormente. En el radical, el par VIR–LB/VIR–DET tiene la
fuerza del cierre y sigue OPEN, sin objeto que lo oriente.

## Siguiente paso concreto

No relanzar el virial de dilatación pura sobre P_T. Queda una sola reapertura que el Lema 2 no
excluye y que tiene operación explícita: sustituir D por un generador cuyo conmutador con el peine
sea relativamente acotado por a_T. Eso exige que el término δ′ en log n quede compensado dentro del
propio generador, por ejemplo un generador con amortiguación aritmética en cada log n. Antes de
derivar nada, una candidata así tiene que escribir el generador y mostrar la cota relativa. El cotejo
de esa idea contra 106_124 §§3–8 (generador completo, conjugado proyectado) queda pendiente y no se
ha hecho aquí.
