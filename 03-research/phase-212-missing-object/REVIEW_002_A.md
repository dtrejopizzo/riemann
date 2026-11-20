# REVIEW_002_A — Revisión hostil de ROUND_002_A (cola exterior de la hipérbola como suma de cuadrados)

Alcance: lectura línea a línea de la memo; derivación propia de la identidad (1), del Lema y de la
Observación (2) contra P47 §sec:firstcontact (`04-papers/47-row-d-dual-certificates/main.tex`,
l. 6625–6946: operadores en la recta, thm:PCfinite, eq:Gammaenergy, eq:collar, eq:Qbalance,
eq:Qrecombine, eq:Qspectral, prop:GEgap, eq:equivgate, rem:returnremarks); apertura de los
antecedentes citados (`R170_816`, `819`–`821`, `835`, `837`, `841`, `870`; `R161_030`–`039`, `071`,
`072`, `081`; catálogo 04 del índice, filas G4C-R161_030-032, 033-034, 035-038, 039-045, G8B-161);
búsqueda de contraejemplos; delimitación de lo no excluido. Ningún archivo existente fue modificado.
Etiquetas: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMÉRICO.

## 0. Resumen de veredictos

| Afirmación de la memo | Veredicto | Corrección |
|---|---|---|
| Identidad (1) | ACEPTADO CON CORRECCIONES | identidad PROVED; «los únicos funcionales», «la única suma», «exactamente tres maneras» no están probados (ARGUED); descripción de ℓ_k imprecisa (§1.1) |
| Lema (indefinición de C^w − ⟨α,Bα⟩ sobre P_T, L finito) | ACEPTADO, PROVED; enunciado a corregir | las hipótesis w ≥ 0 y k > N no se usan: vale para todo peso complejo no nulo de soporte finito en k ≥ 1; no ve h ni Λ. Falta la versión por sector de paridad (se prueba aquí, §2.4). Clase exacta en §2.5 |
| «ni siquiera para un solo k» | ACEPTADO, PROVED | — |
| Observación (2) | ACEPTADO, PROVED (un punto validado, NUMÉRICO) | sólo con M finito; la matriz no es canónica (sistema de momentos sobrecompleto) y su norma es exponencial en MN e^{2T}; «alternada» es la serie de Taylor del coseno (§3) |
| Cotejo | ACEPTADO CON CORRECCIONES | citas correctas salvo una sección; «misma dificultad que R161_033» inexacto: C es lineal en k y no tiene cruces entre k distintos (§4) |
| Resultado «sin mecanismo nuevo» | ACEPTADO | — |
| «No relanzar … en ninguna variante de … test de rango finito» | RECHAZADO en esa redacción | contraejemplo explícito con test de rango uno (§5.1); sustituir por la clase de §2.5 |
| «Lo único que queda sin excluir es la matriz (2)» | RECHAZADO | lista de lo no excluido en §5.2 |
| «Fila K1 cerrada en la formulación de L finito» | ACEPTADO CON CORRECCIONES | cerrada sólo para la cola aislada, módulo formas en finitos momentos Gamma, con resto no negativo sobre P_T o sobre un sector de paridad (§6) |

No se halló error matemático en ninguna demostración etiquetada PROVED. Los defectos son de alcance:
el Lema es más general de lo que dice (y por eso mismo dice menos sobre la cola), y el cierre que la
memo pide anotar es más ancho que lo que el Lema sostiene.

## 1. Identidad (1)

### 1.1 Verificación

Por thm:PCfinite, para M ≥ N el operador H_{M,N} = L_MS_N − S′_N tiene coeficiente h(k) en k > N y
cero en k ≤ N. Evaluando la serie de Dirichlet de coeficientes en s = s_m = a_m + ½:

    Σ_{N<k≤MN} h(k) k^{−s_m} = (Σ_{d≤M} Λ(d) d^{−s_m})(Σ_{n≤N} n^{−s_m}) − Σ_{n≤N} (log n) n^{−s_m}
                             = d_{m,M} Z_N(s_m) − Z_N^{log}(s_m),

con d_{m,M} el de P47 (l. 6765). Multiplicando por b_m²|μ_m^+(F)|² = |(𝒪_LF)_m|² y sumando en m ≤ L
sale (1). Correcto, PROVED. La matriz diagonal D_{M,L}Z_{N,L} − Z^{log}_{N,L} es no negativa entrada a
entrada (es Σ_{k>N} h(k)k^{−s_m}). La comparación con c_{N,L} = Σ_n Λ(n)‖ℓ_n‖² de eq:Qbalance es
correcta: mismos ℓ_n, otro peso.

### 1.2 Correcciones

- La glosa «el vector 𝒪_L del trasladado de F por log k, con el factor k^{−1/2}» no describe ℓ_k:
  ese vector tiene componentes b_m k^{−s_m}μ_m^+(F), no b_m k^{−s_m/2}μ_m^+(F). Lo exacto es
  ‖ℓ_k(F)‖² = ⟨𝒪_LF, 𝒪_L(k^{−1/2}V_{log k}F)⟩ con el momento del trasladado tomado sin truncar a la
  ventana (el momento truncado es el que produce el collar eq:collar). ℓ_k es una raíz cuadrada
  diagonal de ese apareamiento, elegida.
- «Los únicos funcionales … que la estructura ofrece», «la única suma … con ℓ_k explícitos» y «hay
  exactamente tres maneras» son afirmaciones de exhaustividad sin demostración. Etiqueta: ARGUED. En
  «Qué se probó» debe quedar sólo la identidad.
- §(5), cΛ: lo que cambia es la forma de la identidad (aparece el bloque interior
  (c − 1)Σ_{k≤N}(log k)‖ℓ_k‖²), no su validez. La conclusión de la memo (no es paso de signo; reproduce
  la restricción R1 de REVIEW_001_ABD §4.3) es correcta.

## 2. El Lema

### 2.1 Convenciones comprobadas

P47 l. 6649–6661: V_{−log k}F(t) = F(t + log k), H_{M,N} = Σ h(k)k^{−1/2}V_{−log k}; las fases 161 y 170
escriben τ_aF(t) = F(t + a) (`R161_031` §1). Con F(t) = e^{t/2}f(e^t), 𝓕F(t) = e^{t/2}f̂(e^t) y
(k^{−1/2}τ_{log k}𝓕F)(t) = e^{t/2}f̂(ke^t). El adjunto de τ_{log k} es F ↦ F(· − log k), de modo que

    (H^w)* e_m^±(t) = e^{t/2} g(e^t),   g(x) = x^{∓a_m−1/2} Σ_k w(k) k^{−1/2±a_m} 1_{(ke^{−T}, ke^{T})}(x),

como en la memo. 𝓕* = 𝓕 (P47 l. 6640) da ⟨H^w𝓕F, e_m^±⟩ = ⟨F, φ_m^±⟩ con φ_m^± = 1_{I_T}𝓕(H^w)*e_m^±
= e^{t/2}ĝ(e^t) en I_T, ĝ(ξ) = 2∫_0^∞ g(x)cos(2πxξ)dx. Correcto.

### 2.2 Paso (i)

q(F) = Re⟨α(F), β′(F)⟩ es la forma cuadrática de la forma hermítica
s(G, F) = ½(⟨α(G), β′(F)⟩ + ⟨β′(G), α(F)⟩). Si q es semidefinida sobre V y α(F) = 0, entonces q(F) = 0 y,
por Cauchy–Schwarz para formas semidefinidas, s(G, F) = 0 para todo G ∈ V; como α(F) = 0 queda
⟨α(G), β′(F)⟩ = 0 para todo G ∈ V, y la sobreyectividad de α sobre V da β′(F) = 0. Luego
ker α ∩ V ⊂ ker β′ ∩ V y β′ = B′α sobre V. La sobreyectividad sobre P_T equivale a que ninguna
combinación no trivial de e_m^± (m ≤ L) esté en el espacio generado por e^{±t/2}, cierto por
independencia lineal de exponenciales de exponentes distintos. Correcto. El paso vale igual para F
reales (la forma real simétrica y su extensión hermítica son semidefinidas a la vez).

### 2.3 Paso (ii)

β − Bα = B′α sobre P_T significa que cada φ_m^±, como función en I_T, está en el espacio generado por
e_j^± (j ≤ L) y e^{±t/2} (un funcional acotado que se anula sobre P_T está representado por un vector
de Tate). Dividiendo por e^{t/2} y con ξ = e^t: ĝ(ξ) = Σ_j (c_j^+ ξ^{−2j−1} + c_j^− ξ^{2j}) + d_+ + d_−ξ^{−1}
en (e^{−T}, e^{T}). ĝ es entera (g acotada de soporte compacto en (0,∞)); la igualdad se propaga a
ℂ∖{0}; una función entera no tiene parte principal en 0, luego ĝ es un polinomio; acotada en ℝ, es
constante; tiende a 0 (Riemann–Lebesgue), es nula; g = 0. Correcto.

g ≠ 0: los indicadores de los intervalos (ke^{−T}, ke^{T}) son linealmente independientes (en el
tramo (k_0e^{−T}, (k_0+1)e^{−T}), con k_0 el menor índice del soporte de w, sólo contribuye k_0). Por
tanto g ≠ 0 **para todo w no nulo, real o complejo, sin condición de signo**.

Conclusión: la demostración es completa y sostiene los cuantificadores «todo L finito», «toda B
hermítica 2L × 2L», «un solo k». El corolario sobre ±C = Σ_k h(k)|ℓ_k|² + ρ es correcto: una suma
(finita o convergente) de módulos al cuadrado de funcionales que factorizan por α es ⟨α, Bα⟩ con
B ≥ 0, y el caso −C se obtiene con −B.

Búsqueda de contraejemplos: se intentó (a) w con signos, (b) k ≤ N, incluido k = 1, (c) intervalos
solapados, (d) F reales. En los cuatro la demostración sigue valiendo; no hay contraejemplo.

### 2.4 Lo que el enunciado dice de más y de menos

**De más en las hipótesis.** Ni w ≥ 0, ni k > N, ni M ≥ N ≥ e^{2T}, ni el valor de b_m (basta b_m ≠ 0
para algún m) intervienen. El enunciado correcto es: para todo peso complejo w ≠ 0 de soporte finito
en k ≥ 1. Consecuencia para la lectura: el Lema no es un hecho sobre la cola k > N ni sobre h; es el
hecho de que el espacio generado por finitas exponenciales de Gamma, módulo Tate, no es invariante
por la compresión de H^w𝓕 a la ventana. Vale igual para el bloque interior, para cΛ, para a_P y
para cualquier peine: sobrevive a toda la batería, como la memo reconoce. Es una obstrucción de
formato, no aritmética.

**Extensiones que la misma prueba da (PROVED, mismas líneas).**
(a) ℓ_k y B pueden usar momentos hasta cualquier L′ ≥ L finito con el test Σ_L: se aplica el paso (i)
con α de orden L′ y β completado con ceros.
(b) El test puede ser 𝒪_L*G𝒪_L + J𝒪_L*G′𝒪_LJ con G, G′ hermíticas invertibles cualesquiera, o
cualquier forma hermítica invertible sobre los 2L momentos: se sustituye β por Gβ.
(c) Las exponenciales del test pueden ser finitas e^{ct} con c real cualquiera: si ĝ coincide en un
intervalo con Σ_p c_p ξ^p (exponentes reales distintos), coincide en (0,∞) por analiticidad real; el
término de mayor exponente obliga, con ĝ → 0 en +∞, a que no haya exponentes ≥ 0, y el de menor
exponente obliga, con ĝ acotada en 0+, a que no haya exponentes < 0.

**De menos: el sector de paridad.** Los vectores sobre los que se necesita el signo tienen paridad
definida, Σ_L conmuta con J, pero C no es invariante por J (J𝓕J = J u_∞(D) ≠ 𝓕). La indefinición
sobre P_T no implica la indefinición sobre P_T^ε = {F ∈ P_T : JF = εF}, y la memo no la prueba.
Vale, con la demostración siguiente (escrita en esta revisión; pendiente de la verificación
independiente habitual antes de citarse como parte del NO-GO).

*Complemento (PROVED).* Para w ≠ 0 de soporte finito, ε = ±1, L finito y B hermítica L × L, la forma
F ↦ C^w(F) − ⟨α^+(F), Bα^+(F)⟩ no es semidefinida sobre P_T^ε.
*Demostración.* Sobre P_T^ε, α_m^− = εα_m^+, luego C^w = Re⟨α^+, β^+ + εβ^−⟩, y α^+ es sobreyectiva
sobre ℂ^L (las funciones e^{−a_mt} + εe^{a_mt} y e^{t/2} + εe^{−t/2} son independientes). Por el paso
(i), si la forma fuese semidefinida, la parte de paridad ε de ψ_m = φ_m^+ + εφ_m^− estaría en el
espacio generado por e^{−a_jt} + εe^{a_jt} (j ≤ L) y e^{t/2} + εe^{−t/2}. Con ψ_m = e^{t/2}G(e^t),
G = ĝ_+ + εĝ_− entera, acotada en ℝ y con G(ξ) → 0 cuando ξ → ±∞, y multiplicando por ξ^{1/2}:

    ξG(ξ) + εG(1/ξ) = Σ_{j≤L} c_j (ξ^{−2j} + εξ^{2j+1}) + d(ξ + ε)   en (e^{−T}, e^{T}),

y por analiticidad en ℂ∖{0}. Para ξ → +∞ el lado izquierdo es o(ξ), luego c_j = 0 y d = 0. Queda
G(1/ξ) = −εξG(ξ) en ℂ∖{0}; cuando ξ → 0 el lado derecho tiende a 0, es decir G(z) → 0 cuando
|z| → ∞ en todo ℂ, y G ≡ 0 por Liouville. Entonces g_+ + εg_− = 0, donde

    (g_+ + εg_−)(x) = x^{−1/2} Σ_k w(k) k^{−1/2} [ (k/x)^{a_m} + ε (x/k)^{a_m} ] 1_{(ke^{−T}, ke^{T})}(x).

En (k_0e^{−T}, min(k_0, (k_0+1)e^{−T})) sólo contribuye k_0 y el corchete es no nulo (x < k_0).
Contradicción. ∎

### 2.5 Clase exacta del NO-GO

Clase 𝒞_fin: identidades exactas, sobre todo P_T o sobre todo un sector de paridad P_T^ε, de la forma

    ± Re⟨H^w𝓕F, ΣF⟩ = ⟨α_{L′}(F), Bα_{L′}(F)⟩ + ρ(F),   ρ ≥ 0,

con Σ un test hermítico invertible sobre finitos momentos de exponenciales reales (en particular
Σ_L), α_{L′} finitos momentos Gamma, B hermítica cualquiera (en particular B ≥ 0, que cubre
Σ_k h(k)|ℓ_k|² con ℓ_k factorizando por α_{L′}) y w cualquier peso no nulo de soporte finito. Ningún
miembro de 𝒞_fin existe. El NO-GO es exacto, no cuantitativo: las exponenciales de Gamma son
completas en L²(I_T) y siguen siéndolo al quitar finitas (CITED: teorema de Müntz en un intervalo
[a,b] con a > 0; es el argumento de densidad de P47 tras eq:Gammaenergy), de modo que cada φ_m^± se
aproxima en norma por combinaciones de e_j^±, j ≤ L′, con error tan pequeño como se quiera al crecer
L′. El Lema excluye la igualdad, que es lo que la holgura cero exige, y nada más.

## 3. La Observación (2)

### 3.1 Verificación

ĝ(ξ) = 2∫_0^∞ g(x)cos(2πxξ)dx = Σ_{j≥0} γ_j ξ^{2j}∫_0^∞ g(x)x^{2j}dx con γ_j = 2(−1)^j(2π)^{2j}/(2j)!
(la integral de la memo debe leerse sobre (0,∞)). Para φ_m^+ con peso h:

    ∫_0^∞ g x^{2j} dx = Σ_k h(k) k^{a_m−1/2} ∫_{ke^{−T}}^{ke^{T}} x^{2j−a_m−1/2} dx
                      = Σ_k h(k) k^{2j} ∫_{e^{−T}}^{e^{T}} y^{2(j−m)−1} dy = Θ_j σ_{j−m}(T),

y para φ_m^−, Θ_j · 2 sinh((2m+2j+1)T)/(2m+2j+1). Como e^{t/2}ξ^{2j} = e^{a_jt}, sale (2); el término
j = 0 es A(F) = 0. Todos los σ son positivos, luego el signo de la columna j es (−1)^j. Correcto.

Convergencia: Θ_j es una suma finita (N < k ≤ MN), Θ_j ≤ (MN)^{2j}Σh(k); |μ_j^−(F)| ≤ ‖F‖√(2T)e^{a_jT};
σ_{j−m} ≤ e^{2jT}/max(1, j−m) para j grande. El término general está dominado por
C(2πMNe^{2T})^{2j}/(2j)!: convergencia absoluta. Correcto.

Validación de un punto (NUMÉRICO; T = 0.3, w = δ_2, m = 1, F polinomio cúbico proyectado a P_T,
80 términos, 40 dígitos): ambos lados de (2) dan −3.005922708983058…·10⁻⁴, con acuerdo en 33 cifras.

### 3.2 Correcciones de alcance

- **Sólo M finito.** Con el rango k > N sin tope, Θ_j diverge para todo j ≥ 0; (2) no tiene versión
  límite en M. Debe decirse.
- **Cancelación.** Los términos de (2) crecen hasta j ≈ πMNe^{2T} antes de decaer; su tamaño máximo
  es del orden de exp(2πMNe^{2T}), mientras que |⟨F, φ_m^+⟩| ≤ ‖F‖‖φ_m^+‖ está acotado por la masa
  W_{M,N}. Con N ≥ e^{2T} y M ≥ N la cancelación entre columnas es de exp(2πe^{6T}) como mínimo. La
  alternancia (−1)^j es la serie de Taylor del coseno en un argumento grande; no es una estructura
  de signo y ningún argumento columna a columna puede usarla.
- **No canónica.** El sistema {e^{a_jt}}_{j≥1} es sobrecompleto en L²(I_T) (§2.5), de modo que los
  coeficientes de un funcional en los momentos μ_j^− no son únicos. (2) es un desarrollo, el de
  Taylor; hay otros. «La factorización» debe decir «un desarrollo en todos los momentos».
- **Forma sin cancelación (PROVED, cuenta directa).** De 𝓕τ_a = τ_{−a}𝓕 y 𝓕* = 𝓕 resulta que H^w𝓕
  es autoadjunto para w real, con núcleo de Hankel explícito sobre la ventana:

      (H^w𝓕F)(t) = ∫ κ_w(t + s) F(s) ds,    κ_w(v) = 2 e^{v/2} Σ_k w(k) cos(2πk e^{v}).

  Σ_L es también suma de dos formas de Hankel (núcleos Σ b_m² e^{∓a_m(t+u)}). Así
  C(F) = ½⟨F, (K_hΣ_L + Σ_LK_h)F⟩ es el producto de Jordan de dos operadores autoadjuntos explícitos,
  K_h compacto sin signo y Σ_L ≥ 0 de rango 2L. Ésta es la expresión exacta de la que (2) es el
  desarrollo en serie; el Lema dice que Ran Σ_L no es invariante por K_h módulo Tate. No se ha
  cotejado si esta escritura figura ya en el corpus; no se afirma novedad y no lleva signo.

Veredicto: (2) PROVED como desarrollo exacto, sin signo, con las cuatro precisiones.

## 4. Cotejo

Citas abiertas y comprobadas:

- `R170_816` §§2–7: (3) Φ = B − C, (2) anulación por soporte, (6)–(7) cota bilateral, §4 falsación de
  «h(k) ≥ 0 ⟹ apareamiento ≥ 0», §6 canal d = 2 con dos correlaciones sin signo. Coincide.
  En 816, g = S_LF con S_L = R_L*R_L + JR_L*R_LJ (`R170_811`), que es Σ_L. Coincide.
- `R170_820` (ΔH con los mismos h_{M,N}, sin signo), `821`. Coincide. `819` sólo se leyó en su
  planteamiento y en la línea 287.
- `R170_837` §4 (casillas distintas), Teor. 5.1 (residuo común literal ⟹ radical nulo; «construirlo
  es construir el cierre»), (6.7) (independencia del peso tras recombinar). Coincide.
- `R170_835` Prop. 4.1 y §4.2. Coincide en contenido; el ledger es el §8, no el §9. La proposición
  trata otro funcional (el germen producto) y su prueba usa un objeto ajeno a las definiciones de
  STATEMENT_001; la memo hace bien en no usarla. El Lema de la memo es un enunciado distinto, con
  prueba propia dentro del sandbox.
- `R170_841` §4.2, `R170_870` §8: coinciden.
- P47 eq:Qbalance, eq:Qrecombine, eq:Qspectral, eq:equivgate, rem:returnremarks: coinciden
  literalmente con lo citado. `R161_072` §2 (pesos no negativos arbitrarios), `R161_081`: coinciden.

Sobre R161_030–039, dos correcciones.

1. **Estado en el índice.** Las filas G4C-R161_030-032 y G4C-R161_035-038 figuran PARTIAL; las filas
   G4C-R161_033-034 y G8B-161 (037–039) figuran DEAD. `R161_033` retira la afirmación de
   `R161_031` de que la realización discreta estaba completa y deja dos salidas OPEN: una dilatación
   de fuente isométrica (§5 A) y la compensación exacta del Gram cruzado por los términos polar y
   de Tate (§5 B). `R161_034` identifica el Gram cruzado con el canal producto–cociente de la fase
   106 (fila DEAD: no cancela con el Tate de rango dos en el álgebra invariante por traslación).
   `R161_037`–`039`: la saturación coherente fuerza F = 0 pero no se sigue de (PC) y radicalidad
   (contramodelo 2 × 2); equivalencia terminal. La memo resume «ruta cerrada en el índice»; lo
   exacto es «realización retirada, salidas A y B sin objeto, saturación terminal».
2. **No es la misma dificultad.** El obstáculo de `R161_033` es la diferencia entre ‖Σ_k u_k‖² y
   Σ_k‖u_k‖², es decir los términos de Gram entre k distintos en la **norma** de una suma coherente.
   C no es una norma: es lineal en H, de modo que C = Σ_k h(k)k^{−1/2}Re⟨τ_{log k}𝓕F, Σ_LF⟩
   exactamente, sin cruces entre k distintos. La suma directa en k es automática para C; lo que
   falta es que cada sumando sea un cuadrado, y eso es lo que el Lema niega en 𝒞_fin. La frase «el
   obstáculo registrado (coherencia en k …) no depende de ninguna de las dos cosas» mezcla dos
   obstáculos. El antecedente que sí registra la dificultad real es `R170_816` §4 (apareamiento de
   dos vectores distintos con coeficiente positivo) y P47 eq:Qspectral. El veredicto de repetición
   se sostiene por éstos, no por R161_033. La nota del LEDGER («conversión literal no intentada en
   ninguna memo») sigue siendo cierta; el Lema es el primer enunciado probado sobre ella.

Sandbox: la memo no nombra ni usa equivalencias externas. Conforme.

## 5. Lo que la memo descarta de más

### 5.1 «Test de rango finito»: contraejemplo

Sea K la compresión de H^w𝓕 a P_T (w real, no nulo, soporte finito). K es autoadjunto (§3.2),
compacto y no nulo: un operador de Hankel de rango finito tiene núcleo polinomio-exponencial
(Kronecker), lo que obligaría a que Σ_k w(k)cos(2πkx) fuese en (0,∞) una suma finita de términos
x^p(log x)^q; la extensión entera del lado izquierdo fuerza un polinomio, acotado, constante: imposible.
Sea u ∈ P_T, ‖u‖ = 1, Ku = λu, λ ≠ 0 real, y Σ_u = |u⟩⟨u|. Para F ∈ P_T,

    Re⟨H^w𝓕F, Σ_uF⟩ = Re ⟨F, Ku⟩⟨u, F⟩ = λ |⟨F, u⟩|².

Es un cuadrado con signo fijo sobre todo P_T, con test positivo de rango uno, para cualquier w y en
particular para w = δ_k con un solo k > N. Luego «no relanzar con ningún test de rango finito» no es
consecuencia del Lema y, como afirmación de imposibilidad, es falsa. (PROVED.)

Esto no reabre nada: el cuadrado es genérico en el peso, sobrevive a toda la batería, pierde la
casilla de momentos que produce D_Δ (`R170_837` §4) y no tiene relación escrita con a_T; es la
variante de rango finito de (D2) de la propia memo. Pero el cierre debe redactarse con la clase
𝒞_fin de §2.5 y no con «test de rango finito».

### 5.2 Lo que queda NO excluido (delimitación)

El Lema y el Complemento no dicen nada sobre:

1. **L = ∞.** Con Σ_∞ = 𝒪*𝒪 + J𝒪*𝒪J (núcleo de Hankel −(k_Γ^+)′ de eq:Gammaenergy) o con ℓ_k y B
   sobre toda la sucesión de momentos, la prueba no se aplica (el espacio generado es denso). La
   semidefinición de C_∞ − ⟨α, Bα⟩ con B acotada en ℓ² está OPEN, sin objeto.
2. **B y C juntas.** El Lema trata la cola aislada módulo formas en momentos. La obligación real de
   `R170_816` (8), (11) es B − C − (1 − q_0)‖𝒪_LF‖² con B = Re⟨({X,E_N} − L_M*E_N)F, Σ_LF⟩ menos el
   término de Tate. Los funcionales de B no factorizan por momentos y no se ha probado nada sobre la
   suma. Una identidad en que la parte no factorizable de la cola se cancele contra la de E_N no
   está en 𝒞_fin.
3. **ℓ_k que no factorizan por finitos momentos.** Funcionales de los valores exteriores de 𝓕F, de
   las colas del collar, o cualquier ℓ_k continuo en L²(I_T) fuera del espacio de finitas
   exponenciales.
4. **Tests fuera de finitas exponenciales reales**, incluidos los adaptados al operador (§5.1) y
   los de rango infinito.
5. **Dominios que no sean P_T ni un sector de paridad completo.** Sobre un subespacio de dimensión
   finita donde α es inyectiva toda forma factoriza por α (es la factorización a posteriori de
   `R170_835` §4.2); el Lema no restringe conos ni subespacios propios.
6. **Operaciones no lineales en F.** La memo dice no haber encontrado ninguna y que las disponibles
   dan (D2) o enunciados por vector; es un informe de búsqueda (ARGUED), no un cierre. No se
   examinó: la envolvente en los parámetros libres de la familia de identidades (thm:PCfinite vale
   para todo M ≥ N ≥ e^{2T}, todo L y todo δ > 0; ínfimo o promedio en (M, N, L, δ) dependiente de F);
   la elección de Σ dependiente de F fuera del radical; composiciones de C consigo misma.
   Ninguna tiene objeto escrito; ninguna queda excluida.
7. **Restos sin signo manifiesto por separado** que sólo sean no negativos al sumarse con los
   bloques de E_N y de Tate.

La frase «lo único que queda sin excluir es la matriz (2) completa» debe sustituirse por esta lista.
La exigencia final de la memo (bloque interior con signo opuesto al exterior) es una indicación de
diseño coherente con la restricción R1 de REVIEW_001_ABD; no es una necesidad probada (ARGUED).

## 6. Correcciones exactas a ROUND_002_A

1. Lema, enunciado: sustituir «w(k) ≥ 0, no todos nulos, con soporte finito en k > N» por «w complejo,
   no nulo, de soporte finito en k ≥ 1», y añadir que el Lema no usa h, Λ ni el rango k > N.
2. Añadir el Complemento de paridad (§2.4) o declarar que el Lema está probado sólo sobre P_T.
3. Clase: la de §2.5 (finitas exponenciales reales en el test, finitos momentos en ℓ_k y B, resto no
   negativo sobre P_T o P_T^ε, identidad exacta).
4. (D1): retirar «los únicos», «la única», «exactamente tres maneras», o etiquetarlos ARGUED;
   corregir la glosa de ℓ_k (§1.2).
5. Observación: añadir «M finito; Θ_j diverge sin tope en k», la nota de cancelación exponencial, la
   no unicidad del desarrollo, y la forma de Hankel κ_w.
6. Cotejo (1)a: «R170_835 Prop. 4.1 y §8». Cotejo (1)b y (3): reescribir según §4, puntos 1–2.
7. «Siguiente paso»: sustituir «en ninguna variante de rango de k, peso o test de rango finito» por
   «en ninguna variante de rango de k o de peso con test de finitas exponenciales reales y ℓ_k en
   finitos momentos Gamma»; sustituir «lo único que queda sin excluir» por la lista de §5.2.
8. LEDGER K1: no «cerrada en la formulación de L finito», sino «la conversión de la cola aislada en
   Σ_k h(k)|ℓ_k|² con ℓ_k en finitos momentos Gamma más resto no negativo es NO-GO (𝒞_fin); la
   conversión conjunta de los apareamientos de H_{M,N} y E_N, que es como la fila enuncia el
   residuo, sigue sin objeto y sin exclusión».

## 7. Texto de anotación para el índice y el grid

> **Fase 212, cola exterior de la hipérbola como suma de cuadrados en momentos Gamma — NO-GO con
> clase, PROVED (`ROUND_002_A.md`, Lema; revisión `REVIEW_002_A.md` §§2.4–2.5).** Clase: identidades
> exactas ±Re⟨H^w𝓕F, ΣF⟩ = ⟨α, Bα⟩ + ρ(F), ρ ≥ 0, sobre todo P_T o sobre un sector de paridad, con Σ
> un test invertible sobre finitas exponenciales reales (en particular Σ_L), α finitos momentos
> Gamma, B hermítica cualquiera y w cualquier peso no nulo de soporte finito (en particular h(k),
> k > N, o un solo k). Ninguna existe: los funcionales F ↦ ⟨τ_{log k}𝓕F, e_m^±⟩ no factorizan por
> finitos momentos (transformada coseno entera de una función de soporte compacto). El Lema no usa
> h, Λ ni k > N: es genérico en el peine, sobrevive a toda la batería y no lleva signo. NO excluye:
> L = ∞; la suma de la cola con los bloques de E_N y de Tate; ℓ_k o tests fuera de finitas
> exponenciales (con un test de rango uno adaptado al operador la cola sí es un cuadrado, genérico
> y sin relación con a_T); dominios propios de P_T; operaciones no lineales en F. Antecedentes:
> `R170_816` §4, P47 eq:Qbalance–eq:Qspectral, `R161_033`. Signo global OPEN.

## 8. Qué se comprobó y qué no

Comprobado con derivación propia: (1); pasos (i) y (ii) del Lema; g ≠ 0 para w arbitrario; (2) con su
convergencia; autoadjunción y núcleo de H^w𝓕; contraejemplo de §5.1; Complemento de paridad.
Comprobado por lectura: las citas de §4. No comprobado: `R170_819` y `R170_821` más allá de las
líneas citadas; las filas del grid distintas de la sección de la fase 212; si la escritura de
Hankel de §3.2 tiene antecedente en el corpus. El Complemento de §2.4 y el contraejemplo de §5.1
son demostraciones de esta revisión y no han pasado por un segundo lector.
