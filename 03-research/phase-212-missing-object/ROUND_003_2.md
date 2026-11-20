# Ronda 3, opción 2 — Funcionales y factores que dependen de Λ (memo de selección)

Objetivo (★): λ_A(T) ≥ 0 para todo T, con las definiciones de `../phase-211-sign-sandbox/STATEMENT_001.md`.
Pregunta: ¿existe una factorización explícita a_T(F) = ‖V_T F‖² + ρ_T(F) sobre P_T (o sobre una reducción
PROVED) con V_T escrito con los valores exactos Λ(n), n < N = e^{2T}, ρ_T manifiestamente ≥ 0, y que se rompa
para cΛ y a_P? Notación: Arch(F) = (1/2π)∫ m|F̂|²; para un peso a, Comb_a(F) = Σ_{log n<2T} (2a(n)/√n) Re c_F(log n),
de modo que a_T^{(a)} = Arch − Comb_a y a_T = a_T^{(Λ)}. Etiquetas: PROVED / CITED / CONDITIONAL / ARGUED / OPEN /
NO-GO / NUMÉRICO.

## Cotejo

### Qué se buscó y dónde

Grep en `03-research/` (todas las fases), `04-papers/47` y `48`, grid, crucigrama y anexos de la fase 212 por:
Fejér–Riesz, Cholesky, LDL, pivote, Wiener–Hopf, outer function / función exterior, Szegő, square root / raíz
cuadrada, spectral factorization, B*B, V*V, ratio comb, Schur complement. Hay coincidencias en unas cuarenta
fases; las de más densidad son 114, 116, 72, 162, 186, 155, 211, 204, 200. Primarias abiertas: fase 200
`A_MU_FACTORIZATION_001.md` §1(a)–(e) y su tabla; fase 186 `R186_043_WH_SIGN_ROUTE.md` §§0, 2–3; 211
`ROUND_005_A.md` Prop. 3.3 y §5.3; 211 `LEDGER.md` C33b, C43; fase 170 `R170_861` §§0–7 (encabezados y
estado); P47 lem:shape-scale y cor:Tarch. Las coincidencias «LDL/pivote» de la fase 211 (POWER_*_007, 050,
052, 053, AUDIT_002/005) son certificados racionales de bloques fijos (W-fam, `RULES_AVOID.md` D12), no
factorizaciones de la forma completa. No abrí en primaria las coincidencias de las fases 72, 114 y 116 por
«square root»: por los títulos y por `REVIEW_002_BC.md` B.1(6) (fase 116) son operadores de Feshbach o Gram
ortonormalizados, no un V_T con Λ en el núcleo; queda como límite de este cotejo. Ninguna búsqueda encontró un
V_T afín o racional en Λ cuyo cuadrado se compare con a_T y cuyo resto se examine como tal; eso no prueba que
no exista en otra fase.

### (1) Antecedente más cercano

- **Factorización canónica de la forma o del símbolo:** fase 200 `A_MU_FACTORIZATION_001.md` §1(a)
  (Fejér–Riesz / factorización espectral del símbolo: NO-GO, el símbolo es nulo fuera de un conjunto
  discreto por la ecuación funcional) y §1(b) (Cholesky de la matriz agrupada: inercia mixta, clase C8,
  existe igual para a_P y c = 2). `RULES_AVOID.md` C1 lista «Fejér–Riesz, Cholesky» y «Wiener–Hopf como
  fuente de signo» como cerradas. R186_043 §2: Wiener–Hopf truncado es reformulación del autovalor extremo.
- **Cuadrado del peine comprimido:** 211 `ROUND_005_A.md` Prop. 3.3: Π² = Qσ_v²Q − 𝔏*𝔏, con Λ∗Λ, forma de
  cocientes ≥ 0 y fuga. Es exactamente ‖V_1F‖² para el V_1 lineal en Λ del encargo.
- **Completar el cuadrado:** R170_861 (D*G⁻¹D con D aritmético es congruencia pura, PROVED allí); R170_201/301
  (D_p*D_p = C_pI − (V_p + V_p*), cuadrados menos constante divergente); R166_502 §5.2 y fase 204
  `P1_BBSTAR_001` (V*V da cocientes con coeficiente ≥ 0).
- `REVIEW_002_BC.md` B.2(3), B.4: deja no excluidas las ℓ_i dependientes de Λ (R170_868 no las cubre).

### (2) Objeto realmente nuevo

Ninguna candidata escrita pasa. Lo nuevo de esta memo son tres lemas cortos que delimitan la zona; los
demuestro enteros abajo (§1). En resumen:

- **Lema 1 (PROVED).** «V_T depende de Λ» no es una restricción ni una ayuda algebraica: toda identidad
  polinómica en los pesos válida en a = Λ está en el ideal generado por los átomos Σ_{d|n}a(d) − log n. La
  pregunta de O2 «qué absorbe la parte cuadrática en Λ y con qué identidad» tiene siempre una respuesta
  formal, y esa respuesta no tiene contenido de signo.
- **Lema 2 (PROVED).** Las factorizaciones canónicas (raíz cuadrada de la forma, Cholesky/LDL en cualquier
  orden, factorización de Wiener–Hopf o exterior del símbolo) existen con resto nulo si y sólo si la forma
  es ≥ 0 en el dominio correspondiente: escribirlas exige ya el signo. Circularidad probada en esa clase.
- **Lema 3 (NO-GO con clase, PROVED usando P47 cor:Tarch).** La candidata natural del encargo, V_T afín en
  los pesos, V_T(a) = V_0 + V_1(a) con V_0 y los coeficientes de V_1 independientes del peso, y con el término
  cruzado del cuadrado reproduciendo el peine (2Re⟨V_0F, V_1(Λ)F⟩ = −Comb_Λ(F)), nunca tiene resto ≥ 0 sobre
  P_T para T ≥ 0.60.

Queda por escribir, y no sé escribir: un V_T no afín en Λ (resolvente, Cayley) con fórmula no canónica, o uno
afín cuyo término cruzado no reproduzca el peine y cuyo resto lleve el resto del peine con signo manifiesto.

### (3) Por qué el cambio evitaría la dificultad del antecedente

No la evita en las clases examinadas. Lema 3: con V afín y cruce emparejado, el resto es
ρ = Arch − ‖V_0F‖² − ‖V_1F‖² ≤ Arch, y Arch toma valores negativos en P_T desde T ≥ 0.60; la parte cuadrática
en Λ (Λ∗Λ, cocientes, fuga de Prop. 3.3) entra en ρ con signo menos y ninguna reescritura por
Σ_{d|k}Λ(d) = log k cambia su valor. Es la misma deuda «cuadrados menos constante» de R170_201/301, ahora
probada para toda V_0 y toda V_1 de la clase, no sólo para dilataciones unitarias. Lema 2: lo que sí
factoriza (raíz, Cholesky, Wiener–Hopf) lo hace sólo si ya se sabe el signo, como dice A_MU §1(b) para un
caso. Lema 1: añadir dependencia polinómica en Λ no da estructura que usar.

### (4) Identidad que conectaría con la positividad global

Sólo la trivial: a_T = ‖a_T^{1/2}F‖² sobre P_T (Lema 2), equivalente a (★). Para la clase afín no hay
identidad útil (Lema 3). No tengo identidad para las clases no excluidas.

### (5) Línea que se rompe para cΛ y a_P

- Clase canónica (Lema 2): la línea que falla es «pivote d_k ≥ 0» (o «a_T^{1/2} existe»): para c pequeño
  (P47 lem:shape-scale, PROVED para T ≥ 0.60) y para a_P donde λ_A(T; a_P) < 0. Pero es la propia conclusión,
  no un paso intermedio: la ruptura es circular.
- Clase afín emparejada (Lema 3): no hay línea que señalar, porque la identidad falla ya para Λ.
- Lema 1: toda identidad en un punto se «rompe» en otro punto de forma genérica; por eso O4, leído sólo
  como «la identidad deja de valer para cΛ», no separa por sí solo un paso de signo de una identidad
  arbitraria. Precisión posterior de O4: se exige la igualdad completa y la no negatividad demostradas
  para Λ; bajo el falsificador puede fallar únicamente la igualdad, sin que pierda positividad el
  resto auxiliar. El veto anterior excedía el Lema 1; véase la auditoría de O4/O17 en el índice maestro.

### Veredicto del cotejo

Repetición en la parte canónica (fase 200 §1(a)–(b); C1; R186_043). La parte afín es la candidata natural
del encargo y queda cerrada con clase por el Lema 3. Sin candidata lista para construcción.

## 1. Los tres lemas

### Lema 1 (los átomos generan el ideal del punto Λ; PROVED)

Sea R = ℝ[a_2, …, a_{N−1}] y ℓ_n(a) = Σ_{d|n, d≥2} a(d) − log n, 2 ≤ n < N. Entonces el ideal de R de los
polinomios que se anulan en a = Λ es (ℓ_2, …, ℓ_{N−1}). Lo mismo vale con coeficientes en un espacio de
formas hermíticas sobre un espacio fijo (tensorizando).

*Demostración.* ℓ_n(a) = a_n + Σ_{d|n, 2≤d<n} a_d − log n: el cambio a ↦ (ℓ_n(a))_n es afín y unitriangular
en el orden natural, luego invertible con inversa polinómica (afín). Por tanto R = ℝ[ℓ_2, …, ℓ_{N−1}], el punto
Λ es ℓ = 0 (pues Σ_{d|n}Λ(d) = log n), y el ideal de polinomios que se anulan en el origen de un anillo de
polinomios en las variables ℓ es (ℓ_2, …, ℓ_{N−1}). Para coeficientes en un espacio vectorial E se aplica
coordenada a coordenada a R ⊗ E. ∎

Consecuencia (PROVED). Si V_T(a) es polinómico en los pesos con coeficientes operadores fijos y (G) vale en
a = Λ, la diferencia a_T^{(a)} − ‖V_T(a)·‖² − ρ_T(a) se escribe Σ_n ℓ_n(a) Q_n con Q_n formas: la parte
cuadrática en Λ queda siempre «cancelada contra log k» en sentido formal. Es el análogo para polinomios de
la tautología de R170_868 señalada en `REVIEW_002_BC.md` B.2(3); no aporta signo ni restringe V_T. Con
dependencia racional (resolventes) vale lo mismo en la localización en Λ.

### Lema 2 (circularidad de las factorizaciones canónicas; PROVED)

(a) Existen ℋ, V lineal sobre P_T ∩ 𝒟_T (dominio de forma) y ρ ≥ 0 con a_T = ‖V·‖² + ρ si y sólo si
a_T ≥ 0 sobre P_T. (b) Una matriz hermítica 𝔸 (por ejemplo 𝔸_M de (S)) con menores principales directores
no nulos tiene factorización LDL* con D ≥ 0 si y sólo si 𝔸 ⪰ 0, y d_k = det 𝔸_k / det 𝔸_{k−1}; lo mismo en
cualquier orden de eliminación (permutación). (c) Si V conmuta con traslaciones (multiplicador h), entonces
‖VF‖² = (1/2π)∫|h|²|F̂|² y ρ = a_T − ‖V·‖² tiene símbolo s_T − |h|² ≤ s_T (`REVIEW_002_BC.md` Lema B-2).

*Demostración.* (a) ⇐: a_T es una forma cerrada semiacotada (P47 lem:contA y la forma de Lévy de
STATEMENT §1); si es ≥ 0 en P_T su operador asociado A ≥ 0 tiene raíz A^{1/2} y a_T(F) = ‖A^{1/2}F‖²,
ρ = 0. ⇒: ‖VF‖² + ρ(F) ≥ 0. (b) Eliminación gaussiana sin pivoteo: d_k es el complemento de Schur del bloque
director, igual al cociente de determinantes; 𝔸 = LDL* con L unitriangular es congruencia, y por Sylvester
𝔸 ⪰ 0 ⟺ D ⪰ 0. Un orden distinto es la misma afirmación para P𝔸Pᵀ. (c) Plancherel. ∎

Lectura. En (a) y (b) el factor está determinado por la forma; escribirlo «con Λ exacta» es inmediato
(la forma ya contiene Λ), y su existencia con resto ≥ 0 es (★) en ese dominio. La «ruptura para cΛ» es que
el pivote o la raíz dejan de existir, es decir la conclusión. Esto cierra como circular la clase «factor
determinado canónicamente por la forma». No cierra factores con fórmula propia (no derivada de a_T) cuya
igualdad con una factorización se demuestre después: eso queda en la lista de no excluidos. Para el símbolo en
la recta (Wiener–Hopf, Szegő, función exterior) ρ = 0 exigiría s_T = |h|² y s_T toma valores negativos; ver
además fase 200 §1(a). ARGUED que la variante «por ventana» (Wiener–Hopf truncado) es el caso (a) con A el
operador de Toeplitz truncado (R186_043 §2 lo trata como reformulación del autovalor extremo).

### Lema 3 (NO-GO para V afín con cruce emparejado; PROVED, con P47 cor:Tarch)

Clase 𝒱_aff. Para cada T: V_0 : P_T ∩ 𝒟_T → ℋ_T lineal y V_1(a) = Σ_{n<N} a(n) W_n con W_n lineales, todos
independientes del peso; V_T(a) = V_0 + V_1(a). Condición de emparejamiento:

    2 Re⟨V_0F, V_1(Λ)F⟩_{ℋ_T} = −Comb_Λ(F)   para todo F ∈ P_T ∩ 𝒟_T.          (E)

Enunciado. Si T ≥ 0.60, ninguna V_T ∈ 𝒱_aff que cumpla (E) admite (G) con ρ_T ≥ 0 sobre P_T. Además, para
todo T y todo c real, ρ_T^{(c)} := a_T^{(cΛ)} − ‖V_T(cΛ)·‖² = ρ_T^{(0)} − c²‖V_1(Λ)·‖², par en c y no creciente
en |c|.

*Demostración.* Desarrollando el cuadrado,
‖V_T(cΛ)F‖² = ‖V_0F‖² + 2c Re⟨V_0F, V_1(Λ)F⟩ + c²‖V_1(Λ)F‖² = ‖V_0F‖² − c Comb_Λ(F) + c²‖V_1(Λ)F‖² por (E)
(homogénea de grado uno en el peso, luego válida en cΛ si lo es en Λ). Como a_T^{(cΛ)} = Arch − c Comb_Λ,
ρ_T^{(c)}(F) = Arch(F) − ‖V_0F‖² − c²‖V_1(Λ)F‖². En particular ρ_T = ρ_T^{(1)} ≤ Arch sobre P_T. Por P47
cor:Tarch (PROVED allí, con verificación en aritmética de intervalos), inf{Arch(F) : F ∈ P_T, ‖F‖ = 1} < 0
para T ≥ 0.60; en un F así, ρ_T(F) < 0. ∎

Consecuencias.
- Respuesta a O2 en esta clase: la parte cuadrática en Λ de ‖V_TF‖², ‖V_1(Λ)F‖² (por ejemplo Λ∗Λ +
  cocientes − fuga de 211/ROUND_005_A Prop. 3.3 cuando V_1 es el peine comprimido), sólo puede absorberla ρ_T,
  y entra con signo menos. Reescribirla con Σ_{d|k}Λ(d) = log k (Lema 1) cambia su presentación, no su valor.
- Aun para T < 0.60, ρ_T ≥ 0 implicaría a_T^{(cΛ)} ≥ ‖V_T(cΛ)·‖² ≥ 0 para todo |c| ≤ 1: la identidad no
  podría romperse en c < 1, contra la exigencia O4 (y contra P47 lem:shape-scale para c pequeño, T ≥ 0.60).
- Cubre la candidata del encargo «operador arquimediano de primer orden − peine de dilataciones Λ(n)/√n
  comprimido a la ventana» en cuanto su término cruzado sea el peine, y cubre completar el cuadrado
  V = K − ½K⁻¹Π′ con K > 0 fijo (allí ρ = Arch − K² − ¼Π′K⁻²Π′, y K² + ¼Π′K⁻²Π′ ⪰ ±Π′, de modo que
  ρ ≤ min(a_T^{(Λ)}, a_T^{(−Λ)})); es una prueba directa, en esta clase, del fenómeno de R170_861.

Lo que el Lema 3 no cubre (NO excluido):
- (i) V afín sin (E): 2Re⟨V_0F, V_1(Λ)F⟩ = −Comb_Λ(F) + L(F) con L ≠ 0. Entonces
  ρ_T = Arch − ‖V_0F‖² − ‖V_1F‖² − L(F), y el signo tendría que salir de −L, un término lineal en Λ que queda
  fuera del cuadrado. El cuadrado no aporta el mecanismo; se vuelve a un uso lineal del peine en ρ. ARGUED que
  esto reproduce la situación de K1/I2; no probado.
- (ii) V_0 dependiente del peso, o V_T no afín en Λ (resolvente (1 − zΠ)⁻¹, transformada de Cayley,
  parámetros de Schur con fórmula propia). La prueba usa que c ↦ ‖V_T(cΛ)F‖² es un polinomio de grado dos con
  término lineal fijado por (E); con dependencia no polinómica la concavidad en c se pierde.
- (iii) Identidades sobre reducciones PROVED ((L2), (S), perfil, escalera) donde el término arquimediano
  reducido sea ≥ 0: el Lema 3 usa la negatividad de Arch sobre P_T; sobre 𝔸_M con 2T_0 < log 2 hay que
  rehacer la cuenta con Arch_M (no hecho aquí).

## Resultado

**Sin mecanismo nuevo, con una pieza NO-GO de clase PROVED (Lema 3) y dos lemas de delimitación PROVED
(Lemas 1 y 2).** La zona «funcionales que dependen de Λ» queda así: la dependencia polinómica en Λ es
formalmente vacía (Lema 1); las factorizaciones canónicas son circulares (Lema 2; repetición de fase 200
§1(a)–(b)); la clase afín con cruce emparejado está excluida (Lema 3). No hay candidata lista.

## Qué se probó

- Lema 1: el ideal del punto Λ está generado por los átomos Σ_{d|n}a(d) − log n (cambio de variables
  unitriangular). Toda absorción de Λ∗Λ «por log k» es formal.
- Lema 2: raíz, LDL en cualquier orden y factorización de símbolo existen con resto ≥ 0 sii la forma es ≥ 0.
- Lema 3: para V_T = V_0 + V_1(Λ) con coeficientes fijos y cruce igual al peine, ρ_T = Arch − ‖V_0F‖² −
  ‖V_1F‖² ≤ Arch, negativo en P_T para T ≥ 0.60 (P47 cor:Tarch); y ρ^{(c)} es par y no creciente en |c|.

## Qué falló y por qué

- En la clase afín el cuadrado sólo puede producir el peine en el término cruzado; entonces la parte
  cuadrática en Λ se paga en el resto con signo menos, y el arquimediano solo no la paga (es negativo en P_T).
- Las factorizaciones que sí existen están definidas por la forma y requieren el signo para existir.
- La dependencia en Λ no añade información algebraica explotable.

## Siguiente paso concreto

1. Anotar el Lema 3 como NO-GO de clase (𝒱_aff con (E)) en el índice de rutas, el grid y el ledger, con su
   alcance exacto (no cubre (i)–(iii)); los Lemas 1–2 como delimitación, no como clausura de la zona.
2. Si se reabre la zona, sólo con un V_T no afín en Λ con fórmula escrita no derivada de a_T (por ejemplo la
   resolvente del peine comprimido restringida a P_T) y con ρ_T escrito; antes de derivar, comprobar que
   ρ_T^{(c)} no es monótono en |c| (si lo es, el argumento del Lema 3 se adapta y lo cierra).
3. Revisar la variante (iii) sobre 𝔸_M: decidir si Arch_M es ≥ 0 en el portador reducido; si lo es, el Lema 3
   no aplica y la clase afín sobre (S) queda abierta en sentido estricto.
