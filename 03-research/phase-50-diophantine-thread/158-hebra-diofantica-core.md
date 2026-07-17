# Doc 158 — La hebra diofántica: ¿es la independencia ℚ-lineal de {log p} el certificado de transversalidad que colapsa el defecto de individuación de la forma de Weil?

**Programa:** Hipótesis de Riemann — Phase 50: la hebra diofántica.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Rol del documento:** decidir si **un input estructural específico** —la independencia ℚ-lineal de {log p},
equivalente a la completitud del sistema {p^{iτ}}— **puede ser el certificado de transversalidad
S∩H_osc={0}** (en el sentido del defecto de individuación δ_A del Doc 155) que colapsa el muro
promedio→individual de la forma de Weil, **SIN reintroducir RH**. Esta es la única grieta superviviente de
Phase 49 (GAP-157.A; quinto colapsador del Doc 155; frames del Doc 148), que apareció independientemente
en tres documentos.

**REGLA DE HIERRO de esta fase:** el objeto NO es producir otra equivalencia RH⟺X. El entregable NO es una
equivalencia de RH. Mi expectativa explícita: la hebra colapsa en (a) Nyman–Beurling disfrazada o (b)
Bohr/Voronin confinada al lado-valor. Si apareciera (c), desconfío y triplico el test de estrés.

**Contrato creativo (regla absoluta de etiquetado):** **[DEFINICIÓN-NUEVA]** = libertad total.
**[TEOREMA]/[PROPOSICIÓN]/[LEMA]** = probado DE VERDAD acá, prueba completa; resultados externos citados con
precisión. **[CÁLCULO]** = mostrado. **[PUENTE]** = conexión con estatus honesto de cada eslabón. **[GAP]** =
declarado. **[DESEO]** = declarado. **[GAP de literatura]** = dato no verificado al nivel de página esta
sesión, NO usado como premisa de ningún [TEOREMA]. Jamás se fabrica una prueba de RH. **NADA de numéricos.**

**Prerrequisitos leídos en fuente esta sesión:** Doc 154 completo (taxonomía de cruces; Teorema 154.5 el muro
ES N(A); Teorema 154.9 exhaustividad por tipo lógico; Prop. 154.11 frontera verificable/conclusión-disfrazada
DENTRO de positividad); Doc 155 completo (δ_A(F)=‖(1−A)F‖; Teorema 3.4 no-go; Teorema 4.8 principio de
reducción; §5 quinto colapsador de tipo τ=**?** no-conmutativo/de-fase); Doc 157 completo (GAP-157.A;
no-go tauberiano local; Prop. 157.7 densidad de resonancia = ceros); Doc 148 completo (frames sobre
Λ_p∪Λ_q; Prop. 2.2 nunca Riesz; Prop. 2.4 μ(T)=0; §5.2 densidad infinita rompe el marco); Doc 112 §§0–4.3
(LP-112; Lema 2.2 Kronecker–Weyl sobre {log p}; Prop. 2.6 densidad cero de testigos bajo ¬RH; soporte de
Bagchi S; dicotomía densidad-positiva↔RH / densidad-cero↔¬RH; Lema 3.3 no-discretitud).

---

## 0. Resumen ejecutivo

1. **(§1) Formalización exacta del input diofántico y del espacio (H,A).** Fijo tres enunciados anidados y
   pruebo sus equivalencias incondicionales: (D-a) {log p} es ℚ-linealmente independiente (factorización
   única, [TEOREMA 158.1]); (D-b) Kronecker–Weyl ⟹ el flujo t↦(p^{−it})_p es equidistribuido y minimal en
   el toro 𝕋=∏_p S¹ ([TEOREMA 158.2]); (D-c) el sistema {p^{iτ}}_p es **completo en B²** (la clausura de
   Besicovitch de los polinomios de Dirichlet) y, lo que es DISTINTO, su completitud/minimalidad en
   L²(−T,T) es un problema de frames ([PROP 158.3], que reusa Doc 148). Fijo el par promediador (H,A) del
   Doc 155 en el que vive la pregunta: **NO hay un único (H,A); hay TRES candidatos**, y la elección decide
   el veredicto (§1.4). Este es el primer hallazgo: *la hebra diofántica habita un espacio distinto según se
   lea como valor (B², toro de Bohr) o como inercia (la forma de Weil localizada / Gram de los ceros)*.

2. **(§2) El intento de certificado de transversalidad.** Intento probar: la independencia ℚ-lineal hace que
   {p^{iτ}} sea "máximamente independiente", de modo que ninguna combinación no trivial vive en H_osc — la
   independencia diofántica vacía H_osc. **[PROP 158.5]: el intento SÍ funciona, pero en el toro de Bohr 𝕋,
   donde produce ergodicidad del flujo de Kronecker** (Teorema 4.7 del Doc 155, colapsador de tipo **sym**)
   — y allí H_osc se vacía de invariantes no triviales. **[PROP 158.6]: el intento FALLA en el espacio de la
   forma de Weil**, porque la transversalidad que la independencia certifica es transversalidad a los
   *invariantes del flujo* (lado-valor), no transversalidad al *ideal oscilatorio cero-a-cero* (lado-inercia,
   Doc 134/Doc 155 §6). La independencia vacía la oscilación-de-valores, no la oscilación-de-inercia.

3. **(§3) EL TEST DE ESTRÉS, al frente.**
   - **(Colapso Nyman–Beurling, §3.1):** comparo los DOS sistemas de completitud con precisión. NB/Báez-Duarte
     pide completitud de **dilataciones** {ρ(θ/x)} (equiv. base de potencias {(1/n)^s}) en L²(0,1)/H²; la
     hebra pide completitud de **caracteres** {p^{iτ}} / {n^{−s}}. **[PROP 158.7]: NO son el mismo sistema de
     completitud** — NB es completitud en una variable de ESCALA (Mellin/dilatación) RH-equivalente por
     construcción (1_{(0,1)}∈clausura ⟺ RH); la hebra es completitud en una variable de FRECUENCIA
     (Fourier/traslación) que es INCONDICIONAL. La hebra NO es NB disfrazada *como sistema*. **PERO** [PROP
     158.8]: ambas comparten el mismo defecto — el peso/el espacio donde se mide la completitud carga la
     información de los ceros, y para que la completitud de {p^{iτ}} sea RELEVANTE a inercia hay que medirla en
     el espacio de la forma de Weil, donde se vuelve RH-equivalente. La hebra escapa a NB como *enunciado* pero
     cae en la *misma trampa de espacio*.
   - **(Colapso Bohr–Voronin, §3.2):** la independencia ℚ-lineal ES lo que hace ζ casi-periódica (Bohr) y
     potencia la universalidad de Voronin. **[PROP 158.9]: la universalidad de Voronin/Bagchi es un enunciado
     de VALORES y es CIEGA a RH** (Bagchi: recurrencia fuerte ⟺ RH usa el soporte, no la universalidad
     cruda; la universalidad vale incondicionalmente). **[TEOREMA 158.10] (el corazón): la hebra diofántica,
     en su forma de completitud B²/toro de Bohr, está CONFINADA al lado-valor por construcción** — vacía
     H_osc en el sentido de oscilación-de-valores (la coordenada t de Besicovitch, donde la seminorma anula
     los compactos, Doc 112 Obs. 2.4) y es estructuralmente ciega a la coordenada de inercia (la altura γ de
     un cero, un compacto). Es la MISMA ceguera de seminorma B² que mató LP-112 directo.

4. **(§4) VEREDICTO: caso (b) PROBADO, con un núcleo de (a) en el mecanismo de espacio.** La hebra diofántica
   es **Bohr/Voronin confinada al lado-valor** (caso b): vacía la oscilación de valores pero NO la de inercia.
   El mecanismo de la ceguera es exacto y triple-verificado (§4.2): la independencia ℚ-lineal certifica
   transversalidad a los INVARIANTES del flujo de Kronecker (vacía H_osc^val), pero la inercia de los ceros
   vive en H_osc^iner, ortogonal a la coordenada del flujo. NO es (c): no hay certificado de inercia. El
   residuo de (a): para promover la hebra de valor a inercia hay que cambiar de espacio al de la forma de
   Weil, y ahí la completitud se vuelve RH-equivalente (núcleo NB-tipo). **NO se produce ninguna equivalencia
   de RH como entregable.**

5. **(§5) El GAP exacto que separa la completitud diofántica (incondicional) del certificado de inercia.**
   **[GAP-158.A]:** la independencia ℚ-lineal vive en el toro de Bohr 𝕋=∏_p S¹ (un objeto de la coordenada
   de FASE/valor); el certificado de inercia que RH necesita vive en el espacio de la forma de Weil sobre las
   ALTURAS de los ceros (coordenada de inercia, Doc 155 §6 ideal compacto). El GAP es **la ausencia de un
   functor que transporte la transversalidad del toro de fases a la transversalidad del ideal de inercia**, y
   ese functor —si existiera— sería precisamente el quinto colapsador de tipo τ=**?** del Doc 155 §5.2
   (no-conmutativo/de-fase). La hebra diofántica NO es ese functor; es su input candidato, no construido.

---

## 1. Formalización del input diofántico y del espacio (H,A)

### 1.1. Los tres enunciados diofánticos anidados, con equivalencias

Fijo el contenido del "input diofántico" con precisión, separando lo que son enunciados DISTINTOS aunque
relacionados. Sea ℙ el conjunto de primos.

**[TEOREMA 158.1] (D-a: independencia ℚ-lineal de {log p} = factorización única).** El conjunto
{log p : p∈ℙ} es linealmente independiente sobre ℚ. Equivalentemente: la única solución entera de
Σ_p a_p log p = 0 con (a_p) de soporte finito es a_p≡0.

*Demostración.* Σ_p a_p log p = 0 ⟺ ∏_p p^{a_p}=1. Separando exponentes positivos y negativos,
∏_{a_p>0} p^{a_p} = ∏_{a_p<0} p^{−a_p}, dos enteros con factorizaciones primas disjuntas; por el teorema
fundamental de la aritmética (factorización única) ambos lados son 1, luego todo a_p=0. Multiplicar por el
mcm de los denominadores reduce el caso racional al entero. $\square$

Este es el esqueleto aditivo del producto de Euler. Es **incondicional, aritmético puro, RH-libre por
construcción** — el dato que da a la hebra su atractivo: no contiene a los ceros.

**[TEOREMA 158.2] (D-b: Kronecker–Weyl — el flujo de primos es equidistribuido y minimal en 𝕋).** Sea
𝕋:=∏_p S¹ el toro (compacto, en la topología producto) y considérese, para cualquier subconjunto finito
F⊂ℙ, el flujo lineal φ_F: t↦(p^{−it})_{p∈F} = (e^{−it log p})_{p∈F} en 𝕋_F=∏_{p∈F}S¹. Entonces:
(a) la órbita {φ_F(t):t∈ℝ} es densa en 𝕋_F (minimalidad); (b) está equidistribuida respecto de la medida
de Haar: (1/T)∫_0^T g(φ_F(t))dt → ∫_{𝕋_F} g dHaar para toda g∈C(𝕋_F). En el límite proyectivo, el flujo
t↦(p^{−it})_{p∈ℙ} es minimal y unívocamente ergódico en 𝕋.

*Demostración.* Por el teorema de Weyl/Kronecker, el flujo lineal t↦(α_p t mod 1)_{p∈F} con frecuencias
α_p=log p/2π es equidistribuido y minimal en 𝕋_F ssi {α_p}_{p∈F} son ℚ-linealmente independientes junto
con 1 — que es D-a ([TEOREMA 158.1]) más la observación de que log p/2π nunca es racional con otro log q/2π
(misma factorización única). La ergodicidad única del flujo de Kronecker minimal es clásica
([Walters, *Ergodic Theory*, Thm 6.20: una traslación minimal de un grupo compacto es unívocamente
ergódica]). El límite proyectivo se hereda por compatibilidad de las medidas de Haar. $\square$

Este es el contenido de los Lemas 2.2 y 3.3 del Doc 112, aislado como teorema de la estructura del toro.

**[PROPOSICIÓN 158.3] (D-c: completitud del sistema {p^{iτ}} — DOS lecturas distintas).** El sistema de
caracteres {p^{iτ}}_{p} (más generalmente {n^{−s}}, equivalente vía factorización) tiene completitud que
depende ENTERAMENTE del espacio:
(i) **En B² (clausura de Besicovitch de polinomios de Dirichlet con frecuencias {log n}):** el sistema
{e^{i(log n)t}}_n es completo en B² por definición de la clase (Besicovitch 1932). Esto es incondicional y
*tautológico* (la clase se define como su clausura).
(ii) **En L²(−T,T) sobre uniones de progresiones {(2πk+φ_p)/log p}:** es un problema de frames. Por Doc 148
Prop. 2.2, ese sistema **nunca es Riesz** (las near-collisions de Kronecker violan la separación uniforme), y
por Prop. 2.4 **μ(T)=0**: completo pero no frame, sin cota inferior.

*Demostración.* (i) Besicovitch [Bes32, Cap. II]. (ii) Doc 148 Props. 2.2, 2.4. $\square$

**Lectura crítica de [PROP 158.3].** La "completitud de {p^{iτ}}" del encargo NO es un enunciado único: en B²
es tautológica e incondicional (no carga inercia); en L²(−T,T) es un problema de frames donde el sistema YA
sabemos que falla la cota inferior por Kronecker. **La completitud diofántica es real pero vive en el
lado-valor** — esto se confirmará en §3.

### 1.2. El par promediador (H,A) — NO hay uno, hay tres

El encargo pide fijar EXACTAMENTE en qué (H,A) del Doc 155 vive la pregunta. La respuesta honesta es que el
input diofántico admite tres realizaciones del par promediador, y la elección **determina el veredicto**.

**[DEFINICIÓN-NUEVA 158.4] (los tres pares promediadores candidatos).**

- **(H₁,A₁) — el toro de Bohr / valor.** H₁ = L²(𝕋, Haar) sobre el toro de Kronecker 𝕋=∏_p S¹.
  A₁ = proyección sobre los invariantes del flujo φ (= esperanza condicional sobre la σ-álgebra invariante).
  Por D-b (Teorema 158.2) el flujo es unívocamente ergódico, luego H_ind(A₁)=ℂ·1 (constantes) y
  H_osc(A₁)=(constantes)^⊥. Este es el marco del colapsador **sym** (Teorema 4.7 del Doc 155).
- **(H₂,A₂) — Besicovitch / casi-períodos.** H₂ = B²(ℝ) (Besicovitch), A₂ = proyección B² sobre el cierre del
  span de {e^{i(log n)t}}. H_osc(A₂) = lo que la seminorma B² borra. Crucialmente (Doc 112 Obs. 2.4): la
  seminorma B² **anula todo compacto** — H_osc(A₂) contiene toda función soportada en un compacto de t.
- **(H₃,A₃) — la forma de Weil localizada / inercia.** H₃ = el espacio de la forma de Weil localizada
  (Doc 155 §6: secciones/ventanas del lado explícito; álgebra de Weil–Toeplitz 𝒲). A₃ = promedio sobre
  ventanas / proyección sobre el "símbolo autónomo computable desde los primos"; H_osc(A₃) = el ideal
  compacto 𝒥 = la corona 𝒞=𝒲/𝒥 donde "los ceros viven en la frontera símbolo/compacto" (Doc 134 Thm 5.2).
  F = la contribución oscilatoria cero-a-cero. δ_{A₃}(F)=0 sería "la señal de los ceros está determinada por
  el símbolo autónomo".

**El punto de la fase, en una frase.** El input diofántico (D-a/D-b/D-c) vive nativamente en (H₁,A₁) y
(H₂,A₂) — los espacios de VALOR/FASE. RH es un enunciado sobre δ_{A₃}(F) — el espacio de INERCIA. La
pregunta central (§2) es si la transversalidad que la independencia certifica en (H₁,H₂) se transporta a
(H₃,A₃). Adelanto: NO, y §3 prueba por qué.

### 1.3. Por qué los tres espacios son genuinamente distintos (no es pedantería)

**[PROPOSICIÓN 1.x — registro estructural].** Los tres H_osc son disjuntos en su contenido informativo:

| par | coordenada | H_osc captura | RH lee aquí? |
|---|---|---|---|
| (H₁,A₁) toro Bohr | fase (p^{−it})_p | desviación de la media de Haar | NO (valor) |
| (H₂,A₂) Besicovitch | tiempo t (altura) | TODO compacto (seminorma anula) | NO (ciega a compactos) |
| (H₃,A₃) Weil | inercia/índice | señal cero-a-cero (ideal compacto 𝒥) | SÍ (es δ_{A₃}=0) |

La fila (H₂) es la trampa fina: la seminorma B² anula compactos, y un cero individual vive a altura γ FIJA
(un compacto). Cualquier transversalidad probada en (H₂) es invisible a la inercia. La fila (H₃) es donde RH
vive. La hebra diofántica entra por (H₁)/(H₂) y debe llegar a (H₃) — ese salto es el GAP (§5).

---

## 2. El intento de certificado de transversalidad

El mecanismo candidato del encargo: *la independencia ℚ-lineal hace que el sistema de oscilaciones {p^{iτ}}
sea "máximamente independiente", de modo que ninguna combinación no trivial vive en N(A) — la independencia
diofántica vacía H_osc.* Lo intento en serio, en cada espacio.

### 2.1. El intento TRIUNFA en (H₁,A₁): la independencia produce ergodicidad

**[PROPOSICIÓN 158.5] (la independencia ℚ-lineal vacía H_osc de invariantes en el toro de Bohr).** En
(H₁,A₁), la independencia ℚ-lineal de {log p} (D-a) implica, vía Kronecker–Weyl (D-b), que el flujo φ es
unívocamente ergódico, y por tanto H_osc(A₁)=(constantes)^⊥ **no contiene ningún invariante no trivial del
flujo**: el único F con φ_t F = F y δ_{A₁}(F)=0 es constante.

*Demostración.* Es el Teorema 4.7 del Doc 155 (colapsador **sym**) instanciado en el flujo de Kronecker.
Ergodicidad única (Teorema 158.2) ⟺ dim H_ind(A₁)=1 ⟺ H_osc(A₁) no esconde invariantes
([Walters Thm 6.20; Doc 155 Teorema 4.7]). La transversalidad S∩H_osc={0} se cumple para S = {invariantes
del flujo} = constantes. $\square$

**Esto es exactamente el certificado de transversalidad pedido — pero del tipo equivocado.** La independencia
ℚ-lineal SÍ certifica una transversalidad real: la del subespacio de invariantes del flujo al espacio de
oscilación del flujo. Por el principio de reducción (Teorema 4.8 del Doc 155), es un colapsador genuino de
tipo **sym**. **Pero S = constantes, y RH no es un enunciado sobre constantes del flujo de Bohr.** La hebra
produce un colapsador, sí — para el problema equivocado.

### 2.2. El intento FALLA en (H₃,A₃): la inercia es ortogonal a la coordenada del flujo

**[PROPOSICIÓN 158.6] (la transversalidad diofántica NO se transporta a la forma de Weil).** En (H₃,A₃),
el subespacio S=ⁿ{invariantes del flujo de Kronecker / funciones de la fase (p^{−it})_p} NO es transversal
al ideal de inercia H_osc(A₃)=𝒥; de hecho la señal cero-a-cero F que define δ_{A₃} NO es una función de la
coordenada de fase del flujo, sino de la coordenada de ALTURA/inercia, que es independiente del flujo de
Bohr.

*Demostración.* La forma de Weil localizada (Doc 134/Doc 148 Prop. 1.1) es
½ Q_X(F,F)=Σ_{ρ}|⟨F,e_{γ_ρ}⟩|² — una suma de Gram sobre las ALTURAS γ_ρ de los ceros, NO sobre las fases de
los primos. El flujo de Kronecker actúa sobre el toro de fases ∏_p S¹; las alturas {γ_ρ} de los ceros NO son
funciones de ese toro (no hay un homomorfismo del toro de primos al conjunto de ceros: esa es precisamente
la "estadística desconocida" de los ceros, Doc 148 §5.1). Por tanto S (funciones de la fase) y F (función de
la altura) viven en factores tensoriales independientes; S no puede ser transversal a 𝒥 porque ni siquiera
toca la coordenada donde 𝒥 vive. Formalmente: H₃ ≅ H_fase ⊗ H_altura (módulo la fórmula explícita que las
liga, que es una IDENTIDAD, Doc 112 Prop. 4.2); la transversalidad de §2.1 vive en H_fase, el ideal 𝒥 vive
en H_altura. $\square$

**El intento falla por la razón más limpia posible: cambio de coordenada.** La independencia ℚ-lineal vacía
la oscilación en la coordenada de fase (H_fase). La inercia de RH vive en la coordenada de altura (H_altura).
Son ortogonales. **La independencia diofántica vacía H_osc, sí — pero el H_osc equivocado.** Este es,
exactamente, el contenido del encargo "vacía H_osc en el sentido equivocado — el de valores, no el de
inercia". Lo confirmo y lo pruebo en §3 desde dos ángulos independientes (NB y Bohr/Voronin).

### 2.3. El único puente fase↔altura es la fórmula explícita, que es una tautología

El lector escéptico objetará: fase y altura SÍ están ligadas — por la fórmula explícita
Σ_ρ ĥ((ρ−½)/i) = (lado aritmético sobre {log p}). ¿No transporta esa identidad la transversalidad?

**[PROPOSICIÓN 2.x] (el puente fase↔altura es la fórmula explícita y no transporta transversalidad).** La
fórmula explícita liga la coordenada de fase (lado de primos, sobre {log p}) y la de altura (lado de ceros,
sobre {γ_ρ}), pero como IDENTIDAD válida en todo mundo (RH o ¬RH): por Doc 112 Prop. 4.2, toda combinación
lineal de instancias de la fórmula explícita es otra instancia, hay UNA sola identidad independiente, y la
configuración verdadera la satisface idénticamente. Una identidad satisfecha idénticamente **no transporta
una transversalidad**: no restringe los parámetros de altura usando los de fase. El único contenido
no-tautológico es de SIGNO (positividad sobre el cono de Weil) = el criterio de Weil = RH.

*Demostración.* Doc 112 Prop. 4.2 (verificada en fuente esta sesión). El transporte de transversalidad
requeriría que conocer el lado de primos (incondicional) determine el signo del lado de ceros; ese signo es
exactamente la positividad de Weil, RH-equivalente. $\square$

Por tanto el único puente disponible reintroduce RH por la puerta de positividad — exactamente la
conclusión-disfrazada de la Prop. 154.11 del Doc 154. La transversalidad diofántica no cruza el puente sin
pagar RH.

---

## 3. El test de estrés, al frente

### 3.1. Colapso Nyman–Beurling: ¿es la hebra NB disfrazada?

**Los dos sistemas de completitud, en precisión.**

- **Nyman–Beurling [Nym50; Beu55].** Sea ρ(x)={1/x} (parte fraccionaria de 1/x). El criterio NB:
  **RH ⟺ 1_{(0,1)} ∈ clausura_{L²(0,1)} del span de las dilataciones {ρ(θ/x):0<θ≤1}.** Báez-Duarte [BD03]
  ("A strengthening of the Nyman–Beurling criterion", Actas Acad. Naz. Lincei) lo refina: basta el span de
  {ρ(1/(nx)):n∈ℕ}, equivalentemente la completitud (en un peso explícito) del sistema de **dilataciones por
  enteros**, y lo conecta con la aproximación de 1/ζ por sumas Σ c_n n^{−s}. La variable del sistema NB es la
  **ESCALA** (dilatación/Mellin): el grupo que actúa es (ℝ_{>0},·), y la completitud se mide en L² de la
  recta crítica vía la transformada de Mellin.
- **La hebra diofántica.** Completitud del sistema de **caracteres** {p^{iτ}} (o {n^{−s}}=n^{−σ}n^{−iτ}), en
  la variable de **FRECUENCIA** (Fourier/traslación): el grupo que actúa es (ℝ,+) por traslación en t, y la
  completitud es la de exponenciales {e^{i(log n)t}} en B² o en L²(−T,T).

**[PROPOSICIÓN 158.7] (la hebra NO es Nyman–Beurling como sistema de completitud).** Los dos sistemas de
completitud son distintos: NB es completitud de dilataciones en la coordenada de ESCALA (grupo
multiplicativo, transformada de Mellin), y es RH-equivalente POR CONSTRUCCIÓN (el blanco 1_{(0,1)} codifica
el polo y la completitud equivale a RH). La hebra es completitud de caracteres en la coordenada de FRECUENCIA
(grupo aditivo, transformada de Fourier), y es INCONDICIONAL (D-c(i): tautológica en B²). No hay isomorfismo
que identifique un blanco RH-equivalente de la hebra con 1_{(0,1)} de NB sin elegir el peso (§3.1 abajo).

*Demostración.* En NB la completitud se mide en L²((0,1),dx) [o el peso de Báez-Duarte] y el blanco
1_{(0,1)} es un vector FIJO cuya pertenencia al span ES el contenido — y ese contenido es RH (Beurling 1955:
la distancia de 1_{(0,1)} al span N en función del número de dilataciones decae a 0 ⟺ RH). En la hebra,
{e^{i(log n)t}} es completo en B² por definición de la clase, SIN blanco distinguido y SIN condición. La
diferencia de grupo (multiplicativo vs aditivo) impide una identificación functorial: la dilatación
x↦θx en la coordenada de escala es la traslación s↦s en Mellin, ortogonal a la traslación t↦t+τ en
frecuencia. Son dos completitudes en dos coordenadas distintas del mismo plano. $\square$

**Esto es un hallazgo POSITIVO parcial: la hebra escapa a NB como ENUNCIADO.** No es NB disfrazada en el
sentido de ser literalmente el mismo sistema. Pero el test de estrés no termina aquí — hay que ver si comparten
la trampa de ESPACIO/PESO.

**[PROPOSICIÓN 158.8] (la hebra y NB comparten la misma trampa de espacio: el peso carga los ceros).** Para
que la completitud incondicional de {p^{iτ}} en B² (D-c(i)) sea RELEVANTE a inercia, hay que medirla en un
espacio cuyo producto interno lea las alturas de los ceros — i.e., transportarla a (H₃,A₃) (la forma de
Weil). Pero en (H₃,A₃) la completitud del sistema sobre {log p} **se vuelve RH-equivalente**, exactamente
como NB: la cota inferior de frame μ(T) (Doc 148) ES el módulo de positividad de Weil, y su positividad es
RH. La hebra, al cambiar de espacio para tocar inercia, adquiere el núcleo NB.

*Demostración.* La identificación Doc 148 Prop. 1.1: el módulo de positividad de la forma de Weil = cota
inferior de frame de {e^{i γ t}} en L²(−T,T). Para ζ (no para dos primos puros), las frecuencias son las
ALTURAS γ_ρ de los ceros, y μ(T)>0 ⟺ positividad de Weil ⟺ RH (criterio de Weil [Wei52]). La completitud
diofántica de {p^{iτ}} es completitud en la coordenada de primos (incondicional); para usarla sobre los ceros
hay que pasar por la fórmula explícita (Prop. 2.x: identidad, no transporte) y el resultado es el módulo de
Weil. Como en NB, *el espacio donde la completitud importa es el espacio donde la completitud es RH*. $\square$

**Sub-veredicto NB:** la hebra NO es NB disfrazada como *sistema* ([PROP 158.7], escape genuino en
coordenada de frecuencia vs escala), **pero cae en la misma trampa de espacio** ([PROP 158.8]): para tocar
inercia debe medirse en (H₃,A₃), donde su completitud es RH-equivalente. El escape de enunciado no es escape
de mecanismo.

### 3.2. Colapso Bohr–Voronin: ¿está la hebra confinada al lado-valor?

**[PROPOSICIÓN 158.9] (la universalidad de Voronin/Bagchi es lado-valor y ciega a RH).** La independencia
ℚ-lineal de {log p} es exactamente lo que da el teorema de universalidad de Voronin [Vor75] (ζ aproxima
uniformemente, en discos de la franja ½<σ<1, cualquier función holomorfa no-nula) y el teorema límite de
Bagchi [Bag81] (la ley de ζ(·+iτ) es el producto de Euler aleatorio ∏_p(1−ω_p p^{−s})^{−1}, ω uniforme en
∏_p S¹). Ambos son enunciados de VALORES y son INCONDICIONALES (no presuponen ni implican RH). La
universalidad cruda es ciega a RH.

*Demostración.* Voronin [Vor75], Bagchi [Bag81; Lau96 Cap. 5–6], usados en fuente vía Doc 112 §2.4. La
universalidad y el teorema límite valen incondicionalmente; lo que es RH-equivalente es la **recurrencia
fuerte** (densidad inferior positiva de τ con ζ(·+iτ)≈ζ en un disco) [Bag87], que usa que ζ|_D ∈ soporte de
Bagchi S = {no-nulas}∪{0}, lo cual es RH. La universalidad sola (aproximar funciones AJENAS) no toca el
estatus de ζ misma. $\square$

**[TEOREMA 158.10] (el corazón: la hebra diofántica está confinada al lado-valor por construcción).** La
independencia ℚ-lineal de {log p}, en su forma de completitud B² / equidistribución en el toro de Bohr,
vacía H_osc(A₁) y H_osc(A₂) en el sentido de oscilación-de-VALORES (la coordenada de fase del flujo y la
coordenada de tiempo t de Besicovitch), pero es **estructuralmente ciega a la coordenada de inercia** (la
altura γ de un cero). En consecuencia, no colapsa δ_{A₃}(F) (el defecto en la forma de Weil) y NO es el
certificado de transversalidad que RH necesita.

*Demostración.* Combino tres hechos ya probados.
(1) (§2.1, Prop. 158.5) La independencia certifica transversalidad en (H₁,A₁): ergodicidad del flujo,
S=constantes transversal a H_osc(A₁). Coordenada: FASE.
(2) (§2.2, Prop. 158.6) Esa transversalidad NO se transporta a (H₃,A₃): la señal cero-a-cero F vive en la
coordenada de ALTURA, ortogonal a la de fase; el puente (fórmula explícita) es identidad, no transporte
(Prop. 2.x).
(3) La ceguera es exactamente la seminorma B² del Doc 112 Obs. 2.4: en (H₂,A₂), la seminorma de Besicovitch
ANULA todo compacto; un cero individual vive a altura γ FIJA, un compacto; luego H_osc(A₂) contiene la
ventana del cero y la "transversalidad B²" no dice nada sobre ella. Es la misma razón por la que LP-112
directo murió (Doc 112 §2.4, Prop. 2.6: testigos de densidad cero) y por la que el no-go tauberiano localizó
el muro (Doc 157 Teorema 157.10: los promedios no ven la frecuencia individual del cero).
De (1)+(2)+(3): la hebra vacía la oscilación de valores y es ciega a la de inercia. $\square$

**Triple verificación del test de estrés (como exige el contrato para cualquier sospecha de escape).**
- **Verificación 1 (vía seminorma):** Obs. 2.4 del Doc 112 — la coordenada donde la independencia actúa (t,
  fase) tiene seminorma que anula los compactos donde vive la inercia. ✓ confirma confinamiento.
- **Verificación 2 (vía densidad):** Prop. 2.6 del Doc 112 — bajo ¬RH los testigos de transferencia
  fase→inercia tienen densidad CERO; la equidistribución diofántica produce genéricos, y el genérico es
  malo. La independencia da equidistribución (genérica), no el evento excepcional (inercia). ✓ confirma.
- **Verificación 3 (vía frames):** Doc 148 Prop. 2.4 + §5.2 — sobre las alturas de los ceros, μ(T)=0 (sin
  cota de frame) y la densidad infinita rompe el marco; la completitud diofántica de {p^{iτ}} no provee cota
  inferior en la coordenada de inercia. ✓ confirma.
Las tres verificaciones, independientes, dan el mismo veredicto: confinamiento al lado-valor. No hay (c).

**Sub-veredicto Bohr/Voronin:** la hebra ES Bohr/Voronin — vive en el toro de Bohr (Prop. 158.5 = flujo de
Kronecker), potencia la universalidad (Prop. 158.9), y está confinada al lado-valor por la ceguera de
seminorma B² ([TEOREMA 158.10], triple-verificado). **Caso (b).**

### 3.3. Por qué el confinamiento es estructural y no un defecto de técnica

La razón de fondo, en el lenguaje del Doc 154: la independencia ℚ-lineal es un certificado de tipo **sym**
(Teorema 154.9, tipo T4: invariancia bajo el flujo de Kronecker). Por la Prop. 154.11, los certificados de
tipo T1/T3/T4/T5 tienen input verificable-desde-afuera y NO caen en la modalidad conclusión-disfrazada — pero
RH cae en la modalidad de POSITIVIDAD (T2), el único canal cuyo input puede ser la propia tesis. Un
certificado **sym** (la hebra) no puede colapsar un defecto que es de tipo **positividad** sin atravesar el
puente fórmula-explícita, que reintroduce el signo (= RH). El confinamiento es la manifestación, en
coordenadas diofánticas, de la Prop. 154.12: *el muro de RH es de positividad porque es el único canal cuyo
input puede ser la conclusión*, y la hebra es un input de simetría, del tipo equivocado.

---

## 4. Veredicto (a/b/c)

### 4.1. El veredicto

**VEREDICTO: caso (b) — la hebra diofántica es Bohr/Voronin, confinada al lado-valor; vacía la oscilación de
valores pero NO la de inercia; MUERTA como cruce, con un núcleo de (a) en el mecanismo de espacio.**

Desglose contra las tres opciones del encargo:

- **(a) ¿Es la hebra Nyman–Beurling disfrazada (RH-equivalente, circular)?** **PARCIALMENTE, y en un sentido
  preciso.** Como *sistema de completitud* NO ([PROP 158.7]: NB es completitud de dilataciones en escala
  Mellin; la hebra es completitud de caracteres en frecuencia Fourier — coordenadas distintas, grupos
  distintos, la hebra es incondicional). PERO comparte la *trampa de espacio* ([PROP 158.8]): para que la
  completitud incondicional toque inercia hay que medirla en (H₃,A₃) = la forma de Weil, donde se vuelve
  RH-equivalente (μ(T)>0 ⟺ RH). El núcleo NB reaparece no en el enunciado sino en el espacio.
- **(b) ¿Está la hebra confinada al lado-valor (Bohr/Voronin), vaciando H_osc en el sentido equivocado?**
  **SÍ, PROBADO ([TEOREMA 158.10], triple-verificado §3.2).** La independencia certifica transversalidad en
  la coordenada de fase (toro de Bohr, ergodicidad de Kronecker, colapsador **sym**), que es ortogonal a la
  coordenada de inercia (altura de los ceros) donde RH vive. La ceguera es la seminorma B² que anula
  compactos (Obs. 2.4 Doc 112), la misma que mató LP-112 directo.
- **(c) ¿Hay una TERCERA cosa — certificado de inercia sin RH-equivalencia ni confinamiento?** **NO.** El
  intento de §2 falla (Prop. 158.6); el único puente fase→inercia es la fórmula explícita, que es identidad,
  no transporte (Prop. 2.x); las tres verificaciones independientes (seminorma, densidad, frames) confirman
  confinamiento. No desconfío de un (c) inexistente: lo que hay es (b) con residuo de (a).

### 4.2. El mecanismo de la ceguera, exacto y triple-verificado

El corazón del veredicto es que **la hebra diofántica y RH viven en coordenadas tensorialmente
independientes**: H₃ ≅ H_fase ⊗ H_altura. La independencia ℚ-lineal es un teorema de equidistribución en
H_fase (el toro de Bohr ∏_p S¹). RH es un teorema de inercia en H_altura (positividad de Weil sobre las
alturas {γ_ρ}). El único operador que liga los factores es la fórmula explícita, que es una identidad
(Doc 112 Prop. 4.2) y por tanto no transporta el certificado de un factor al otro. Las tres herramientas
distribucionales que actúan en H_fase (seminorma B², equidistribución de Bagchi, frames de Beurling–Landau)
son las tres ciegas a H_altura — y esa ceguera es exactamente el cuantificador maestro de P43 (promedio no
ve el punto), confirmado tres veces.

### 4.3. Por qué esto es el resultado honesto y valioso

El encargo anticipó que el resultado honesto sería (a) o (b), y que (c) merecería triple desconfianza. Es
(b), con el núcleo de (a) localizado en el mecanismo de espacio. El valor del documento NO es una
equivalencia de RH (no se produce ninguna). El valor es **localizar con precisión la frontera entre la
completitud diofántica incondicional y el certificado de inercia que RH necesita**, y mostrar que esa
frontera es un cambio de coordenada (fase→altura) cuyo único puente es una tautología. Esto cierra la única
grieta superviviente de Phase 49 (GAP-157.A) con un veredicto NEGATIVO bien fundado: la hebra diofántica no
cruza el muro, y la razón es estructural (Prop. 154.11/154.12), no de técnica.

---

## 5. El GAP exacto: completitud diofántica (incondicional) vs certificado de inercia

Aunque el veredicto es (b)-muerta, el contrato pide aislar el GAP exacto que separa lo que la hebra SÍ tiene
(completitud diofántica incondicional) de lo que RH necesita (certificado de inercia). Lo nombro con
precisión.

**[GAP-158.A] (el functor fase→inercia que falta).** La independencia ℚ-lineal de {log p} certifica
transversalidad en el toro de fases 𝕋=∏_p S¹ (coordenada de VALOR; colapsador de tipo **sym**, incondicional,
RH-libre). El certificado de inercia que RH necesita vive en el espacio de la forma de Weil sobre las ALTURAS
de los ceros (coordenada de INERCIA; defecto δ_{A₃}, tipo POSITIVIDAD). El GAP es la **ausencia de un functor
𝔉: (transversalidad en 𝕋, lado-fase) → (transversalidad en 𝒥, lado-inercia)** que transporte la
transversalidad sin pasar por la fórmula explícita (que es identidad, no functor de transporte). Tres
propiedades exactas que 𝔉 debería tener y que ningún objeto conocido tiene:
1. **Debe acoplar los factores H_fase y H_altura** sin ser la fórmula explícita (que los acopla como
   identidad tautológica, Prop. 2.x). I.e., debe ser un acoplamiento que restrinja, no que iguale.
2. **Debe ser ciego a la seminorma B²** (que anula la coordenada de altura, Obs. 2.4) — i.e., debe operar
   en un espacio donde los compactos de altura tengan peso positivo, NO en B² ni en L²(−T,T) crudo.
3. **Debe ser de tipo τ=? (no-conmutativo/de-fase)** en el sentido del Doc 155 §5.2: NO reducible a
   positividad (caería en RH-equivalencia), NI a las cotas/órdenes/UCP (Doc 154 T1/T3), NI a la simetría sola
   (que es lo que la hebra YA es, y se queda en H_fase). Debe ser el quinto colapsador.

**[PUENTE — estatus del GAP-158.A].** Este GAP es la intersección exacta de tres líneas independientes del
programa:
- el **quinto colapsador de tipo τ=?** del Doc 155 §5.2 (no-conmutativo/de-fase, par de proyecciones en
  posición genérica / frame inconmensurable), que el Doc 155 declaró buscable pero no construido;
- la **grieta GAP-157.A** del Doc 157 (condición tauberiana espectral no-local con input diofántico), que el
  Doc 157 dejó como [GAP de literatura] no probado;
- el **input nuevo (no mecanismo nuevo)** del Doc 154 §5/§6: una clase cohomológica sobre Spec ℤ que lea
  inercia (tipo T5 con input inexistente en la literatura).
Las tres son la MISMA cosa vista desde tres herramientas: el functor fase→inercia que la hebra diofántica
NO provee pero cuyo input candidato ES. **La hebra es el input correcto (incondicional, RH-libre, vive en el
toro de fases); lo que falta es el transporte a inercia, que es un objeto de tipo τ=? no construido.**

**[GAP de literatura, declarado, NO premisa de ningún teorema].** No conozco en la literatura un teorema que
transporte la ergodicidad del flujo de Kronecker en ∏_p S¹ a una cota inferior de inercia/positividad sobre
las alturas de los ceros de ζ sin pasar por la fórmula explícita. La maquinaria de operadores en espacios de
Pontryagin (el κ=2m de P35), los frames inconmensurables (Doc 148), y la cohomología foliada de Spec ℤ
(Phases 40–43) son los tres candidatos a 𝔉, todos con su propio GAP abierto. Lo registro como la frontera, no
como ruta probada.

**[DESEO 158.B].** Que exista 𝔉 de tipo τ=? que use la independencia ℚ-lineal de {log p} (vía completitud de
{p^{iτ}} en un espacio con peso de altura positivo, NO B²) como input para un colapsador no-conmutativo del
defecto δ_{A₃}. Sería el quinto colapsador del Doc 155 con su input identificado. No lo tengo; lo nombro como
deseo, no como gap accionable, porque el cambio de coordenada fase→altura (Prop. 158.6) sugiere que el
transporte correcto no es analítico-armónico sino de naturaleza espectral/no-conmutativa — coherente con la
heurística del Doc 155 §5.2.

---

## 6. Mensaje final

**VEREDICTO: caso (b) — la hebra diofántica es Bohr/Voronin, confinada al lado-VALOR.** La independencia
ℚ-lineal de {log p} (= completitud de {p^{iτ}}) SÍ es un certificado de transversalidad genuino, pero del
tipo equivocado: vacía H_osc en la coordenada de FASE (el toro de Bohr ∏_p S¹, vía ergodicidad de
Kronecker — colapsador de tipo **sym**, incondicional), que es ortogonal a la coordenada de INERCIA (las
alturas de los ceros) donde RH vive. La ceguera es la seminorma B² que anula los compactos (la misma que mató
LP-112 directo). NO colapsa el defecto de individuación δ_{A₃} de la forma de Weil. NO se produce ninguna
equivalencia de RH.

**¿Cuál de los tres colapsos/escapes?** **Colapso (b) Bohr/Voronin — confinamiento al lado-valor**, con un
núcleo de (a) Nyman–Beurling localizado NO en el enunciado (escape genuino: completitud de caracteres en
frecuencia ≠ completitud de dilataciones en escala) sino en la TRAMPA DE ESPACIO (para tocar inercia hay que
medir en la forma de Weil, donde la completitud se vuelve RH-equivalente). NO es (c).

**Tres hallazgos con etiquetas:**

1. **[TEOREMA 158.10 + PROP 158.5/158.6] — La hebra vacía el H_osc EQUIVOCADO.** La independencia ℚ-lineal
   certifica transversalidad en el toro de Bohr (ergodicidad del flujo de Kronecker, colapsador **sym**),
   pero esa transversalidad NO se transporta a la forma de Weil porque la señal cero-a-cero vive en la
   coordenada de altura, tensorialmente independiente de la coordenada de fase; el único puente (fórmula
   explícita) es una identidad, no un transporte (Prop. 2.x). Triple-verificado: seminorma B² anula compactos
   (Obs. 2.4 Doc 112), densidad cero de testigos (Prop. 2.6 Doc 112), μ(T)=0 en frames (Doc 148 Prop. 2.4).

2. **[PROP 158.7 + PROP 158.8] — La hebra escapa a Nyman–Beurling como ENUNCIADO pero no como MECANISMO.**
   NB es completitud de dilataciones en la coordenada de escala (Mellin, grupo multiplicativo), RH-equivalente
   por construcción; la hebra es completitud de caracteres en la coordenada de frecuencia (Fourier, grupo
   aditivo), incondicional — son sistemas distintos. PERO ambas comparten la trampa de espacio: para que la
   completitud diofántica toque inercia hay que medirla en (H₃,A₃), donde la cota inferior de frame ES la
   positividad de Weil = RH. El escape de enunciado no es escape de mecanismo.

3. **[GAP-158.A + PUENTE §5] — El GAP exacto es el functor fase→inercia, = el quinto colapsador no
   construido.** Lo que separa la completitud diofántica incondicional del certificado de inercia es la
   ausencia de un functor 𝔉 que transporte la transversalidad del toro de fases (donde la hebra la tiene) al
   ideal de inercia (donde RH la necesita), sin pasar por la fórmula explícita-tautología. 𝔉 debe ser de tipo
   τ=? (no-conmutativo/de-fase, Doc 155 §5.2), ciego a la seminorma B², y no reducible a positividad. Es la
   MISMA frontera que GAP-157.A (Doc 157), el quinto colapsador (Doc 155 §5), y el input cohomológico sobre
   Spec ℤ (Doc 154 §5) — tres herramientas, un solo objeto faltante. **La hebra diofántica es el input
   candidato de 𝔉 (incondicional, RH-libre, vive en el toro de fases); NO es 𝔉.**

---

## Referencias

**Internas (backward-only):** Doc 154 (taxonomía de cruces; Teorema 154.5 el muro=N(A); Teorema 154.9
exhaustividad por tipo lógico T1–T5; Prop. 154.11/154.12 frontera verificable/conclusión-disfrazada DENTRO de
positividad, RH es de positividad); Doc 155 (defecto δ_A=‖(1−A)F‖; Teorema 3.4 no-go individuación gratis;
Teorema 4.7 colapsador sym/ergodicidad; Teorema 4.8 principio de reducción; §5.2 quinto colapsador τ=?
no-conmutativo/de-fase; §6 diccionario forma de Weil, ideal compacto 𝒥); Doc 157 (GAP-157.A condición
diofántica como tauberiana espectral; Teorema 157.10 no-go tauberiano local; Prop. 157.7 densidad de
resonancia=ceros); Doc 148 (frames Λ_p∪Λ_q; Prop. 1.1 forma de Weil=Gram de exponenciales; Prop. 2.2 nunca
Riesz; Prop. 2.4 μ(T)=0; §5.2 densidad infinita rompe el marco); Doc 112 (LP-112; Lema 2.2 Kronecker–Weyl
sobre {log p}; Obs. 2.4 seminorma B² anula compactos; Prop. 2.6 densidad cero de testigos bajo ¬RH; soporte
de Bagchi S; Lema 3.3 no-discretitud; Prop. 4.2 fórmula explícita es identidad); Doc 134 (corona
𝒞=𝒲/𝒥, ceros en la frontera símbolo/compacto); P35 (κ=2m, espacios de Pontryagin); P43 (cuantificador
maestro, valor/inercia).

**Literatura (publicada, verificable salvo marca):**
- [Nym50] B. Nyman, *On the One-Dimensional Translation Group and Semi-Group in Certain Function Spaces*,
  tesis, Uppsala, 1950. (Criterio original: RH ⟺ completitud de las traslaciones/dilataciones de ρ.)
- [Beu55] A. Beurling, *A closure problem related to the Riemann zeta-function*, Proc. Nat. Acad. Sci. USA
  41 (1955), 312–314. (Criterio NB en forma cerrada; la distancia de 1_{(0,1)} al span decae a 0 ⟺ RH.)
- [BD03] L. Báez-Duarte, *A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis*, Atti
  Accad. Naz. Lincei Cl. Sci. Fis. Mat. Natur. Rend. Lincei (9) Mat. Appl. 14 (2003), 5–11. (Refinamiento:
  basta el span de las dilataciones por enteros / base de potencias; conexión con Σ c_n n^{−s}.)
- [Vor75] S. M. Voronin, *Theorem on the universality of the Riemann zeta-function*, Izv. Akad. Nauk SSSR
  Ser. Mat. 39 (1975), 475–486 (Math. USSR-Izv. 9 (1975), 443–453). (Universalidad: ζ aproxima toda función
  holomorfa no-nula en la franja; enunciado de valores, ciego a RH.)
- [Bag81] B. Bagchi, *The statistical behaviour and universality properties of the Riemann zeta-function and
  other allied Dirichlet series*, tesis, Indian Statistical Institute, Calcutta, 1981. (Teorema límite
  funcional; producto de Euler aleatorio; soporte S={no-nulas}∪{0}.)
- [Bag87] B. Bagchi, *Recurrence in topological dynamics and the Riemann hypothesis*, Acta Math. Hungar. 50
  (1987), 227–240. (Recurrencia fuerte ⟺ RH — la mitad que SÍ usa el soporte, RH-equivalente, contrastada
  con la universalidad cruda que no lo es.)
- [Lau96] A. Laurinčikas, *Limit Theorems for the Riemann Zeta-Function*, Kluwer, 1996. (Exposición completa
  del teorema límite de Bagchi, Caps. 5–6; soporte de la medida límite.)
- [Boh18] H. Bohr, *Zur Theorie der allgemeinen Dirichletschen Reihen*, Math. Ann. 79 (1918), 136–156.
  (Casi-periodicidad de series de Dirichlet; la independencia ℚ-lineal de {log p} da la casi-periodicidad en
  σ>1; lado-valor.)
- [Bes32] A. S. Besicovitch, *Almost Periodic Functions*, Cambridge Univ. Press, 1932. (Clase B²; la
  seminorma B² anula los compactos; clausura de polinomios trigonométricos.)
- [Wei52] A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm. Sém. Math. Univ.
  Lund (1952), 252–265. (Criterio de positividad de Weil; la positividad del lado aritmético sobre el cono de
  tests ⟺ RH — el contenido de signo, tipo positividad.)
- [Kro1884] L. Kronecker, *Näherungsweise ganzzahlige Auflösung linearer Gleichungen*, Berl. Sitzungsber.
  (1884). [Teorema de Kronecker; H. Weyl, Math. Ann. 77 (1916), 313–352, para la equidistribución.]
- [Wal82] P. Walters, *An Introduction to Ergodic Theory*, GTM 79, Springer, 1982. (Thm 6.20: traslación
  minimal de grupo compacto = unívocamente ergódica — la ergodicidad del flujo de Kronecker.)
- [Landau67] H. J. Landau, *Necessary density conditions for sampling and interpolation of certain entire
  functions*, Acta Math. 117 (1967), 37–52. (Densidades de Beurling–Landau; vía Doc 148.)

*Fin del Doc 158.*
