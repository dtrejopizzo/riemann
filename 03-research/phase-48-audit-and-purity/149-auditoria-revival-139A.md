# Doc 149 — Auditoría adversarial del revival de 139.A: el Doc 147 NO revive el teorema

**Programa:** Hipótesis de Riemann — Phase 48, "auditoría y pureza"
**Fecha:** junio 2026
**Mandato:** destruir o certificar la reparación del Doc 147 (dominancia exponencial para la rama ¬RH del criterio logístico, Problema 139.A). Objeto auditado: Doc 147 completo ([Lema 2.1], [Prop. 3.1], `hyp:band` Def. 4.1, [Thm. 4.2], la verificación anti-falsa-victoria §5, y la afirmación §6.2 de incondicionalidad con eje de centro real).
**Insumos (leídos completos, citas solo hacia atrás):** D147; D139 (GAP-A, Lema 139.1, GAP-B, §4.4, Problema 139.A); D136 (Def. 3.1–3.2, Lemas 5.2–5.3, Teoremas 4.1–4.4, 5.4, lado espectral (1.1)–(1.2)); D107/D108 vía las citas de D136. Nada se fabrica; cada afirmación de error viene con el cálculo en forma cerrada.

---

## 0. Veredicto por pieza, en una línea cada una

| Pieza | Veredicto |
|---|---|
| **[Lema 2.1]** (dominancia exponencial-vs-polinomial) | **SOBREVIVE-CON-ERRATA** — la cota inferior (2.4) es genuina solo tras reparar el hueco de los ceros de Fourier con la modulación (que el doc relega a un paréntesis y que choca con la paridad de §3.4); las constantes dependen también de γ₀, no "solo de Φ y δ₀". El lema controla **módulos**; no contiene ni puede contener información de **signo** — y todo lo que viene después necesita signo. |
| **[Prop. 3.1]** (testigo sin constante divergente) | **MUERE** en tres pasos exactos: (i) la ecuación (3.4) contiene un **error de conjugación** — la paridad da ĝ(σ₀′) = conj(ĝ(σ₀)), luego el término objetivo es Re[ĝ(σ₀)²] (signo oscilante con a₀), no |ĝ(σ₀)|²; (ii) el mecanismo (†) usa una **cota superior sin signo** (valor medio) como término principal **con signo** — la "discrepancia contra el término autónomo" es un error de categoría: neg.ind exige Q₂(v,v) < 0, y en Q₂ no existe ningún término "lo que valdría si ρ⁰ estuviera on-line"; (iii) el presupuesto (3.6) asume tácitamente que el cuádruplo de ρ⁰ **agota** los ceros off ("4 ceros off" en la prueba): juguete presentado como general. El enunciado es plausiblemente verdadero **bajo defecto finito** con otra prueba (§5.4 abajo); bajo ¬RH general está abierto. |
| **[Thm. 4.2] (rama ¬RH bajo `hyp:band`)** | **MUERE**, independientemente de `hyp:band`: hereda el cadáver de la Prop. 3.1; el trasplante del testigo de dos jorobas al span {B·σᵃ} de la celda está afirmado, no derivado ((3.6) nunca se re-deriva para la celda); y la cola de la celda **a M fijo** (el doc fija M ≥ D+4) no es poly(a₀) bajo ¬RH general: porta factores de franja e^{βa₀} de los ceros off desconocidos — cerrarla exige M creciente con a₀, y entonces el Lema 139.1 **reabre GAP-A literalmente**. Además **SOBRE-RECLAMA**: enunciado para ¬RH general, demostrable (tras reparaciones) a lo sumo bajo "defecto finito + β* alcanzado". |
| **`hyp:band` como hipótesis** | **SOBREVIVE** (única pieza que sale mejor de lo que el mandato temía) — tras corregir un desliz de cuantificador (la (4.1) literal, con c libre, es contradictoria con el propio decaimiento de (∗)): no existe Lema 139.1-bis para cotas inferiores puntuales en dirección real con masa de signo definido; es satisfacible y de hecho demostrable para familias explícitas (§3.3). Pero `hyp:band` solo da **módulo**, y la rama ¬RH muere por **fase/signo**: la hipótesis sobrevive, la implicación "`hyp:band` ⟹ rama ¬RH" no. |
| **§5 (anti-falsa-victoria, b₀ = O(1), cero de parte real máxima)** | **SOBRE-RECLAMA** — el análisis de condicionamiento Vandermonde es correcto en su alcance, pero "verificado" es falso: presupone que β* = sup{β} se **alcanza** (no garantizado bajo ¬RH general: escenario de acumulación β_n ↗ β*, consistente con los teoremas de densidad), contradice la Prop. 3.1 (que usa el cero de **altura** mínima), y no toca ni el signo ni los pares de tasa igual. |
| **§6.2 (eje de centro real ⟹ ambas ramas incondicionales)** | **MUERE** en el punto (b) del protocolo — falacia *pars pro toto*: re-centrar el bump en ½+δ₀ hace trivial el **numerador** (|B(0)| = 1) y traslada todo el contenido al **denominador** (los valores del bump sobre la línea Re = ½, donde vive el mar): la cantidad load-bearing es el **cociente** off/on, y tras re-centrar el cociente exige una cota **superior** exponencialmente pequeña sobre la línea crítica — la misma asimetría direccional de `hyp:band` con otra ropa, no una identidad. Las partes (a) test-accesibilidad y (c) preservación de la rama RH y la canonicidad **sobreviven** (§4.3): el eje es una ampliación inocua y hasta recomendable — pero no trivializa nada. |
| **Estatus de 139.A** | **SIGUE ABIERTO.** El "CERRADO-PARCIAL" del Doc 147 no es sostenible; el abstract de P47 queda como lo dejó D139. |

---

## 1. Protocolo 1: re-derivación del [Lema 2.1] y el asunto cota-inferior-de-Fourier

### 1.1. La derivación, desde cero

Con la representación de banda crítica (D147 (2.1), = `rem:theta` de P47):
$$\hat f(s)=\int_{-a_0}^{a_0}F(u)\,e^{(s-\frac12)u}\,du,\qquad F=a_0^{-1/2}\,\Phi(\cdot-a_0/2),\ \Phi\in C_c^\infty([-1,1]).$$
En ρ⁰ = ½+δ₀+iγ₀:
$$\hat f(\rho^0)=a_0^{-1/2}\,e^{(\delta_0+i\gamma_0)a_0/2}\cdot c,\qquad
c:=\int_{-1}^{1}\Phi(t)\,e^{\delta_0 t}\,e^{i\gamma_0 t}\,dt \;=\; \widehat{\Phi e^{\delta_0\cdot}}(-\gamma_0).$$
El módulo del factor exponencial es exacto: e^{δ₀a₀/2}. Todo el contenido de la cota inferior (2.4) es la afirmación |c| ≥ c₁ > 0.

### 1.2. Dónde está el punto fino y cómo le va al doc

El número c es el valor de la transformada de Fourier de una función C_c^∞ en la frecuencia γ₀. Dos hechos, ambos contra el enunciado literal del lema:

1. **c depende de γ₀ y decae superpolinomialmente en γ₀** (Paley–Wiener para Φe^{δ₀·} ∈ C_c^∞; Hörmander I, Thm. 7.3.1). La frase del lema "constantes que dependen solo de Φ y de δ₀" es **falsa**: c₁ = c₁(Φ, δ₀, γ₀). Como γ₀ está fijo por la configuración, esto no es fatal — es errata, pero errata que importa porque la misma frase reaparece en la Prop. 3.1 ("NO de un parámetro que tienda a infinito": cierto, pero las constantes sí dependen de toda la configuración).
2. **c puede anularse exactamente.** $\widehat{\Phi e^{\delta_0\cdot}}$ es entera de tipo exponencial 1, no constante: tiene infinitos ceros (Hadamard; Boas, *Entire Functions*, Cap. 2), y nada impide que γ₀ — que es **del adversario** — caiga en uno. Para el bump plano Φ ≥ 0 la positividad solo protege el punto **real** (γ = 0): ∫Φe^{δ₀t}dt > 0 sin cancelación. Este es exactamente el fenómeno que el mandato señala: las cotas inferiores de transformadas en puntos complejos son delicadas porque los ceros de la transformada se mueven con el test.

**La reparación del doc (modulación Φ ↦ Φe^{−iγ₀t}) es correcta en sí**: traslada la evaluación al punto real, c = ∫Φe^{δ₀t}dt ≥ e^{−δ₀} > 0, y la clase es cerrada bajo modulación [D107]. Pero está relegada a un paréntesis dentro de la prueba, **cambia el test** (el lema tal como está enunciado, con F = bump plano, es falso para γ₀ en el conjunto de ceros), y — decisivo para §3.4 — **la modulación compleja destruye la realidad/paridad de F** que §3.4 necesita. La versión real-par compatible (jorobas en ±a₀/2 moduladas por cos(γ₀u)) sí existe y da
$$\hat f(\sigma_0)=\tfrac12\,a_0^{-1/2}e^{(\delta_0+i\gamma_0)a_0/2}\Big[\underbrace{\textstyle\int\Phi e^{\delta_0t}dt}_{>0}+\underbrace{e^{i\gamma_0a_0}\textstyle\int\Phi e^{\delta_0t}e^{2i\gamma_0t}dt}_{\text{oscila con }a_0}\Big]+O\big(e^{-\delta_0a_0/2}\big),$$
con cota inferior |ĝ(σ₀)| ≥ c₁e^{δ₀a₀/2}a₀^{−1/2} siempre que $|\widehat{\Phi e^{\delta_0\cdot}}(-2\gamma_0)|<\int\Phi e^{\delta_0t}dt$ — verificable para γ₀ grande por suavidad, ajustable para γ₀ pequeño. Nada de esto está en el doc.

### 1.3. Veredicto del protocolo 1

**[Lema 2.1] SOBREVIVE-CON-ERRATA**: (2.4) es verdadera para el test corregido (modulación compatible con paridad), la garantía de "≥ y no solo ≤" existe y proviene de la masa de signo definido evaluada en el punto real — el único lugar donde la cota inferior de Fourier es barata. (2.5) es correcta tal cual. **Pero el lema entero vive en el mundo de los módulos.** El cociente off/on → ∞ es verdad y no cierra nada: lo que la negatividad de Q₂(v,v) necesita es el **signo** de un término concreto, y el signo es una fase que el Lema 2.1 ni menciona. El lema es un ladrillo sano usado como piedra angular de un arco que no existe.

---

## 2. Protocolo 2: el término de perturbación (†), la conjugación de (3.4), y la caza de la constante escondida

### 2.1. El error de conjugación en (3.4) — el paso exacto donde muere la Prop. 3.1

§3.4 toma g_v real con F **par** y afirma: "ĝ_v(σ₀) = ĝ_v(σ₀′) (paridad ⟹ simetría σ ↔ 1−σ)", y de ahí (3.4):
$$\hat f(\sigma_0)\,\overline{\hat f(\sigma_0')}\;\overset{\text{D147}}{=}\;|\hat f(\sigma_0)|^2.$$
Re-derivemos. La paridad de F da la simetría funcional ĝ(1−s) = ĝ(s); la realidad de F da ĝ(s̄) = conj(ĝ(s)). Con σ₀ = ½+δ₀+iγ₀ y σ₀′ = 1−σ̄₀ = ½−δ₀+iγ₀:
$$\hat g(\sigma_0')=\hat g(1-\bar\sigma_0)\overset{\text{paridad}}{=}\hat g(\bar\sigma_0)\overset{\text{realidad}}{=}\overline{\hat g(\sigma_0)}
\qquad\Longrightarrow\qquad
\hat g(\sigma_0)\,\overline{\hat g(\sigma_0')}=\hat g(\sigma_0)^2,$$
**un cuadrado complejo, no un módulo al cuadrado**. Nótese que 1−σ₀ = ½−δ₀−iγ₀ ≠ σ₀′: la simetría de paridad NO lleva σ₀ a σ₀′; lo hace componiéndose con la conjugación, y la conjugación sobra exactamente una vez. La contribución de la órbita {P₀, ιP₀} con testigo real par es, en forma cerrada (usando §1.2):
$$2m_0^2\,\mathrm{Re}\big[\hat h(P_0)\overline{\hat h(\iota P_0)}\big]
=\tfrac{m_0^2}{2}\,\hat\varphi(0)^2\,\mathrm{Re}\big[\hat g(\sigma_0)^2\big]
=\tfrac{m_0^2}{2}\,\hat\varphi(0)^2\,a_0^{-1}e^{\delta_0a_0}\,|c_+|^2\cos\!\big(\gamma_0a_0+2\arg c_+\big)\,(1+o(1)),$$
con c₊ la constante de §1.2. **El signo oscila con a₀** a través de la fase γ₀a₀. Consecuencias exactas:

- La identidad (3.4) "= |f̂(σ₀)|² ≥ c₁²a₀^{−1}e^{δ₀a₀}" es **falsa**.
- El párrafo siguiente del propio doc ("ese producto es real y positivo (=|ĥ(P₀)|² ≥ 0)... parece matar la idea") comete **el mismo error con la conclusión opuesta**. El doc afirma, a tres líneas de distancia, que esencialmente la misma cantidad es positiva (+|ĥ|²) y negativa (−c_W|f̂|² en la prueba de la Prop. 3.1). La verdad es: ninguna de las dos — es Re[ĥ(P₀)²], de signo oscilante. Que un documento sostenga ambos signos para el mismo término es por sí solo motivo de retiro.
- Lo irónico: **la verdad es más útil que ambas afirmaciones del doc** — un signo oscilante es elegible: existen ventanas de a₀ (progresiones de paso 2π/γ₀) donde cos < −½ y el término objetivo es genuinamente −c·a₀^{−poly}e^{δ₀a₀}. Ese ajuste de fase (elegir a₀ módulo 2π/γ₀, legítimo: el testigo puede usar posiciones, Obs. 5.1 de D136) es el mecanismo real del criterio clásico de Weil — y **no está en ninguna parte del Doc 147**.

### 2.2. (†) re-derivado: cota de valor medio, sin signo, y con la tasa equivocada

Sea P(δ) := f̂(½+δ+iγ)·conj(f̂(½−δ+iγ)). Entonces P(0) = |f̂(½+iγ)|² y
$$P'(\delta)=\Big(\int uF\,e^{\delta u}e^{i\gamma u}du\Big)\overline{\hat f(\tfrac12-\delta+i\gamma)}
-\hat f(\tfrac12+\delta+i\gamma)\overline{\Big(\int uF\,e^{-\delta u}e^{i\gamma u}du\Big)},$$
de donde, con F de jorobas en ±a₀/2 (‖uFe^{δu}‖₁ ≤ C a₀^{1/2}e^{δa₀/2}, |f̂(½±δ+iγ)| ≤ C a₀^{−1/2}e^{δa₀/2}):
$$\big|P(\delta_0)-P(0)\big|\;\le\;C\,\delta_0\,e^{\delta_0 a_0}. \tag{2.A}$$
Tres conclusiones, en orden de gravedad creciente:

1. **Verificación estrecha a favor del doc:** en (2.A) no hay C_M, ni b₀(M)^{−1}, ni M. En ese sentido literal, la afirmación "no hay constante divergente en M" es cierta. La rigidez del Lema 139.1 no muerde aquí.
2. **La constante escondida está, pero no es M — es un exponencial declarado polinomio.** El coeficiente impreso en (†) es "δ a₀ e^{a₀/2}‖F‖₁ sup_band|f̂|" con la afirmación "‖F‖₁, sup|f̂| son O(poly(a₀))". Falso: el supremo sobre la banda |Re−½| ≤ δ₀ incluye Re = ½+δ₀, donde |f̂| ≍ a₀^{−1/2}e^{δ₀a₀/2} — **exponencial**. Es la lección de GAP-A en su forma nueva: en D136 era una "constante" que era función de M; aquí es un "polinomio" que es exponencial en a₀. Y con el factor e^{a₀/2} impreso, la tasa total del resto de (†) es (1+δ₀)/2 > δ₀ para todo δ₀ < 1: **el término de error de (†), leído como el doc lo escribe, engulle al término principal e^{δ₀a₀} que se pretende extraer de él.** Con la lectura reparada (2.A) la tasa del error es exactamente δ₀ — igual a la del principal: tampoco así se extrae nada.
3. **El error de categoría (el golpe fatal):** (†) es una cota de |desviación|, sin signo. El doc la usa así: "la discrepancia |ĥ(ρ⁰_off)|² − |ĥ(ρ⁰_on)|² es lo negativo cuando se compara contra el término autónomo... el término O(δa₀e^{a₀/2}) es el portador del signo del defecto". Pero **el certificado que neg.ind(Q₂|_{V_p}) ≥ 1 necesita es Q₂(v,v) < 0, punto** — la suma espectral real, (1.1) de D136. El lado aritmético/autónomo es **igual** al lado espectral (es la fórmula explícita): no existe en el formalismo ningún término "el valor que ĥ tendría si ρ⁰ estuviera on-line" que se reste de nada. La comparación contrafáctica no es un término de la forma; es narrativa. La cantidad real es la de §2.1: Re[ĝ(σ₀)²]·(...), computable directamente, con signo oscilante — y el doc nunca la computa, porque la computación directa contradice a la vez su "+|ĥ|²" y su "−c_W|f̂|²".

### 2.3. El presupuesto (3.6) y los términos omitidos de tasa máxima

Aun concediendo el signo del primer término de (3.6), el presupuesto está incompleto **a la misma tasa exponencial**:

- **Pares (z₁,z₂) del propio cuádruplo** (z₁ = ½+δ₀+iγ₀, z₂ = ½−δ₀+iγ₀): σ = ½+iγ₀, τ = ±δ₀. Con g, φ reales pares de soporte a₀ (el diseño declarado de la Prop. 3.1), φ̂(±δ₀) ∈ ℝ y la órbita {(z₁,z₂),(z₂,z₁)} aporta
$$\tfrac12\,|\hat g(\tfrac12+i\gamma_0)|^2\,\hat\varphi(\delta_0)^2\;\asymp\;+\,a_0^{-2}\,e^{\delta_0a_0}\;>\;0,$$
**positivo, de la misma tasa δ₀ y el mismo orden polinomial a₀^{−2} que el término "dominante" negativo**. No aparece en (3.6). (Es matable: o soporte de φ fijo — diseño asimétrico que el doc no usa —, o aniquilación Vandermonde en τ sobre ±δ₀, iγ₀ — el parche GAP-B usado con nodos que el doc no lista.)
- **La prueba de (3.6) declara "su número es finito (4 ceros off × ...)" y suma el mar solo sobre ρ on-line**: asume que el cuádruplo de ρ⁰ agota los ceros off. Bajo ¬RH general hay (posiblemente infinitos) ceros off adicionales ρ = ½+β+iγ con β hasta cerca de ½ y signo no controlado, que viven en la "cola" de (3.6) con factores de franja e^{βa₀} — **no poly(a₀)**. Si existe un solo cero off con β > δ₀ (la elección de ρ⁰ es por altura mínima, ¡no por β máxima!), su término no-signado e^{βa₀} derrota al principal e^{δ₀a₀}. Este es el mismo patrón que D139 documentó en GAP-B: "probado en el juguete, citado en general". Detalle completo en §5.

**Veredicto protocolo 2: la Prop. 3.1 MUERE en (3.4) (conjugación), en el mecanismo (†) (cota sin signo usada como término con signo; "polinomio" que es exponencial), y en (3.6) (presupuesto de juguete bajo hipótesis general).**

---

## 3. Protocolo 3: `hyp:band`, los ceros de B̂, y si existe un Lema 139.1-bis

### 3.1. El enunciado preciso y un desliz de cuantificador

La (4.1) literal pide |B^{(M)}_w(½+δ+ic)| ≥ c_δ e^{c′δa₀} con c sin acotar. **Así escrita es contradictoria con la propia (∗)**: a lo largo de la recta Re = ½+δ, la cota (∗) da |B(½+δ+ic)| ≤ C_M e^{δa₀}(1+|c−c_centro|/w)^{−M} → 0 cuando |c| → ∞ — ninguna función de la clase satisface una cota inferior uniforme en c. La lectura reparada (la única que la aplicación usa): la cota inferior se exige **en el punto desplazado que la celda evalúa**, ½+δ+iε con |ε| ≤ b (malla), tras elegir el centro c en la malla cerca de γ₀. Registro la corrección como E-149.1 (no fatal: la aplicación nunca usó el ∀c).

### 3.2. ¿Hay un Lema 139.1-bis? No — y este es el único punto donde el Doc 147 gana

El mecanismo del Lema 139.1 (D139) necesita una **familia de cotas a lo largo de todo el eje real, uniforme en M**: si C_M ≤ A^M para infinitos M, B se anula en |t| > Aw — contradicción con ceros reales discretos. Una cota **inferior puntual en un solo punto de dirección real** no tiene ese apalancamiento: no hay ningún límite M → ∞ que tomar, y el punto es uno. Más aún, es satisfacible de forma elemental:

**[CÁLCULO 149.2] (familia explícita que satisface `hyp:band` reparada).** Sea G_a ≥ 0, C_c^∞, soporte en [−a, a], par, con masa ≥ η > 0 en [a/2−1, a/2+1] y ‖G_a‖₁ = 1, y B_a(z) := ∫G_a(u)e^{(z−½)u}du. Entonces:
(i) |B_a(½+ic)| ≤ ‖G_a‖₁ = 1 para todo c (la segunda cláusula de (4.1), gratis);
(ii) B_a(½+δ) = ∫G_a e^{δu}du ≥ η·e^{δ(a/2−1)} — integrando positivo, **sin problema de ceros**: la cota inferior en el punto real es barata exactamente porque la masa tiene signo definido;
(iii) para el punto desplazado: Re B_a(½+δ+iε) ≥ cos(εa)·η e^{δ(a/2−1)} − (resto acotado), > 0 si |ε| ≤ π/(3a) — **la malla debe ser b ≲ 1/a₀**, disponible en la grilla dyádica de D136, con N₀ creciente. ∎

Los ceros de B̂ — la amenaza que el mandato pide rastrear — solo muerden en puntos de **ordenada desplazada** (γ₀ − c ≠ 0) o tras la combinación Vandermonde; el primero se controla con malla 1/a₀-fina o con la genericidad del centro (Lema 5.3 de D136: conjunto de ceros discreto, evitable); el segundo es (R2), tratado en §5. **Quién controla dónde caen los ceros de B̂ respecto de ρ⁰:** nadie necesita controlarlo si la evaluación decisiva es en el punto real con masa positiva; el adversario controla (β, γ₀), pero γ₀ se neutraliza con el centro de ordenada (eje que la grilla SÍ tiene) y β con... el factor de franja, que es la cláusula (ii). Conclusión: **no hay Lema 139.1-bis; `hyp:band` (reparada) es satisfacible, demostrable, y el residuo R1 del doc es incluso sobre-cauto.**

### 3.3. Por qué esto no salva nada

`hyp:band` entrega |ĝ(σ₀)| grande. La rama ¬RH necesita un término **negativo** grande. Entre el módulo y el signo está la fase arg ĝ(σ₀) ≈ γ₀a₀/2 + O(1), que rota con a₀ (§2.1) y que ninguna cota inferior de módulo fija. La cadena lógica del Doc 147 es: `hyp:band` ⟹ (2.4)-en-la-celda ⟹ (3.6) ⟹ Q₂(v,v) < 0; el eslabón (3.6) está roto por el signo y por los términos omitidos (§2), y `hyp:band` es irrelevante para ambos. **La hipótesis sobrevive; el teorema condicional no.**

Hay además una segunda dependencia no auditada por el doc: el paso celda-ideal → grilla (Teorema 4.4 de D136) usa b ≤ μ/(4√2 L) con μ = margen espectral y L = constante Lipschitz del Gram. En el régimen no-normalizado, μ ≍ e^{δ₀a₀} pero L ≍ a₀·(tamaño de entradas) ≍ e^{2a₀·(alcance)} — **ambos exponenciales en a₀**; la malla requerida es b ≲ e^{−ca₀}, disponible pero jamás re-cuantificada en D147. Errata E-149.3: todo el paquete de malla debe re-derivarse en el régimen exponencial antes de citarse "sin cambios" (D147, prueba del Thm. 4.2: "el Teorema 4.4 ... sin cambios" — no).

---

## 4. Protocolo 4: el eje de centro real (§6.2) — la afirmación incondicional

### 4.1. (a) Test-accesibilidad: SOBREVIVE

La grilla extendida barre c_Re ∈ ℚ∩[0,½] en malla dyádica: no menciona posiciones de ceros; la celda que "encuentra" a δ₀ existe en 𝒢_N para N grande sin que nadie conozca β (es el mismo argumento de existencia que para los centros de ordenada: el máximo sobre la grilla incluye la celda buena). No se necesita uniformidad sobre la malla: basta una celda negativa. La inclusión 𝒢_N ⊆ 𝒢_{N+1} se preserva con mallas anidadas. ✔

### 4.2. (b) El deslizamiento |B(0)| = 1: AQUÍ MUERE

La cantidad load-bearing del mecanismo entero es el **cociente** (D147 Lema 2.1: "el cociente off/on crece como e^{δ₀a₀/2}"):
$$\mathcal R \;:=\; \frac{|\hat g(\sigma_0)|}{\sup_{\rho\ \mathrm{on}}|\hat g(\tfrac12+i\gamma)|}\,.$$
Con el bump centrado en la línea crítica: numerador ≍ e^{δ₀a₀} (factor de franja, `hyp:band`), denominador ≍ poly — cociente exponencial. Con el bump re-centrado en ½+δ₀ (la propuesta §6.2): numerador = |B(0)| = 1 — **y el denominador son los valores de B sobre la recta re-centrada Re = −δ₀, que es donde ahora vive TODO el mar on-line**. Para que el cociente siga siendo exponencial se necesita
$$\sup_{y\,\in\,\text{ventana}}\big|B(-\delta_0+iy)\big|\;\le\;e^{-c\,\delta_0 a_0},$$
una cota **superior** exponencialmente pequeña a lo largo de un segmento de recta vertical. Eso: (i) **no es la identidad |B(0)| = 1** — es una segunda condición, independiente y no trivial; (ii) es exactamente la asimetría direccional del indicador de Phragmén–Lindelöf que `hyp:band` codificaba (h_B(π) ≪ h_B(0) en la coordenada re-centrada; Levin, *Lectures on Entire Functions*, Lecc. 8–9), **la misma hipótesis con otra ropa**; (iii) tiene su propio costo de rigidez: por el teorema de las tres rectas (Hadamard; cf. Boas §1.4), 1 = |B(0)| ≤ sup_{Re=−δ₀}|B|^{1/2}·sup_{Re=+δ₀}|B|^{1/2}, así que la pequeñez en la recta del mar fuerza |B| ≥ e^{+cδ₀a₀} en Re = +δ₀ — el crecimiento no desaparece, se muda al otro lado, donde habrá que volver a presupuestar los pares que caigan allí (ceros off con β > δ₀, si los hay: §5). El "se evalúa en su máximo" del doc ni siquiera es cierto: B(0) = 1 es la normalización, no el máximo; el máximo de un bump de tipo a₀ en la dirección real está en el borde de la franja.

**Conclusión (b):** "`hyp:band` se vuelve la identidad trivial |B(0)| = 1" es una falacia *pars pro toto*: verifica el numerador del cociente y olvida el denominador. La frase "ambas ramas son teorema incondicional" es **insostenible**; con el eje real, la rama ¬RH queda exactamente igual de condicional (y además sigue muerta por §2, que el eje real no toca: el signo del término objetivo es el mismo problema en cualquier centrado).

### 4.3. (c) Preservación de la rama RH, monotonía y canonicidad: SOBREVIVE

Re-centrar en Re es multiplicar g por x^{c_Re} con c_Re real: C_c^∞(ℝ₊*) es cerrada bajo ello, así que las celdas extendidas viven en la misma clase y el lado espectral (1.1) con convergencia absoluta [D107, Lema 2.2(b)] les aplica. Bajo RH la suma es diagonal y Q₂ ≥ 0 sobre **todo** el span de la clase [D108, Prop. 2.2]; toda compresión de PSD es PSD; el relleno es positivo: x₀(N) ≡ 0 también con el eje extendido — **la rama RH no se rompe**. Monotonía: mallas dyádicas anidadas en c_Re ⟹ 𝒢_N ⊆ 𝒢_{N+1} ⟹ Prop. 3.3(c) intacta; la cota x₀ ≤ ½ del relleno no cambia; el bug E-139.1 (radical) queda como estaba. **El eje de centro real es, como ampliación de diseño, inocuo y razonable** — solo que no demuestra lo que §6.2 dice. (Errata adicional E-149.4: la propia (3.1)/(∗) de D136 normaliza B(0) = 1 mientras mide la franja desde Re = ½ — el punto 0 está a distancia ½ del centro de franja; esa incoherencia de normalización es el terreno donde la confusión de §6.2 crece.)

---

## 5. Protocolo 5: GAP-B revisitado — el cero de parte real máxima y el escenario de acumulación

### 5.1. La contradicción interna

La Prop. 3.1 y el Thm. 4.2 se enuncian con ρ⁰ = el cero off de **altura mínima** (herencia de D136 §1.1). §5 del propio doc descubre que la construcción necesita el cero de **parte real máxima** β* ("la Prop. 3.1 debe usar ρ* = ½+β*+iγ*, no el de altura mínima") — y lo registra como "afinamiento" sin re-enunciar ni re-probar nada. Tal como están escritos, los dos resultados etiquetados usan el cero equivocado: con el de altura mínima, cualquier cero off con β > δ₀ (legítimo bajo ¬RH) aporta un término no-signado e^{βa₀} ≫ e^{δ₀a₀} que ninguna cláusula de (3.6) acota. Esto solo ya invalida los enunciados tal cual.

### 5.2. ¿Existe el máximo? El sup puede no alcanzarse

β* := sup{β : ζ(½+β+iγ) = 0, β > 0}. Bajo ¬RH general el conjunto de ceros off puede ser infinito (el escenario sub-resolución ya señalado en D144): β_n ↗ β* con γ_n → ∞ y **sup no alcanzado**. El doc lo concede a medias ("existe finito bajo ¬RH de defecto que toque la franja" — frase sin definición — "bajo ¬RH general β* ≤ ½") y procede como si se alcanzara. Veamos qué pasa si no:

**[CÁLCULO 149.5] (el escenario de acumulación derrota a todo testigo de soporte compacto con celdas de orden M fijo).** Sea la configuración β_n = β* − εₙ con εₙ ↓ 0 arbitrariamente rápido y ordenadas γ_n las mínimas compatibles con los teoremas de densidad (Ingham: N(σ,T) ≪ T^{4σ(1−σ)}log T para σ > ½, así que γ_n ≫ n^{1/θ} con θ = 4β*(1−β*) < 1 — los teoremas de densidad acotan el **conteo**, no la velocidad de acercamiento εₙ, que queda libre para el adversario). El testigo elige un cero realizado ρ_w con β_w = β* − ε_m fijo. Los ceros con β ∈ (β_w, β*) son infinitos; con bump de celda de decaimiento polinomial de orden M − D (M fijo, como el doc prescribe: "M queda fijado en M ≥ D+4"), el término no-signado del cero n vale hasta
$$e^{\beta_n a_0}\,\big(1+|\gamma_n-\gamma_w|/w\big)^{-(M-D)}\quad\text{frente al principal}\quad e^{\beta_w a_0}\,a_0^{-\mathrm{poly}}.$$
Maximizando sobre n con εₙ = e^{−n}: el cociente malo/principal contiene e^{(ε_m−e^{−n})a₀}·γ_n^{−(M−D)}; en n ≍ log a₀ el factor exponencial es ≍ e^{ε_m a₀} y el polinomial es solo (log a₀)^{−C}: **el cociente diverge**. La aniquilación Vandermonde no ayuda: el grado D de la celda está acotado y los ofensores son infinitos; aniquilar los D peores deja al (D+1)-ésimo, apenas más lejos. Subir M con a₀ para ganar decaimiento reintroduce C_M y el balance e^{2M} → ∞ del Lema 139.1: **GAP-A reabierto literalmente**. ∎

**Conclusión:** bajo ¬RH general, el argumento del Doc 147 (y cualquier reparación dentro de celdas de D, M acotados) **requiere tácitamente** que β* se alcance Y esté aislado (solo finitos ceros con β > β* − η para algún η > 0): un "cero gordo aislado". Eso es una hipótesis estructural sobre el conjunto de ceros que ¬RH no implica, que ningún teorema de densidad da, y que tiene exactamente el sabor de las hipótesis tipo "m < ∞" — es decir, **la circularidad con LP-141 que el mandato temía está ahí, sin declarar**. El "verificado en §5 con el cero de parte real máxima" de §6.3 es falso como verificación: es un deseo con nombre de teorema.

### 5.3. Lo que sí está bien en §5

El análisis de condicionamiento es correcto en su alcance: si los nodos de aniquilación tienen Re ≤ ½ + β_w y el punto de prescripción es el de Re máximo, entonces b₀ = min|B(nodos)| lo fija un nodo on-line y no decae con a₀, y la constante de Lagrange es O(1) a nodos separados. Eso responde la pregunta estrecha de R2 (la Vandermonde no reintroduce el divergente **por la puerta de b₀**). Lo que §5 no toca: el signo (§2.1), los pares de tasa igual (§2.3), y la existencia del máximo (§5.2). Tres puertas abiertas de cuatro.

### 5.4. La reparación honesta que queda viva (segunda reparación, nombrada, no ejecutada)

Para registro de Phase 48 — lo que un Doc 15x podría probar de verdad, y con qué límites:

**Enunciado candidato (defecto finito):** *Bajo ¬RH de defecto finito (4m̄ ceros off), sea ρ* el cero off de parte real máxima β* (existe: conjunto finito). Entonces existe una celda de la grilla (con o sin eje real) con neg.ind ≥ 1.* Ingredientes de la prueba que esta auditoría identifica como suficientes y disponibles: (1) prescripción Vandermonde **a escala** (ĝ(σ*) = R, ĝ(σ*′) = −R con R ≍ |B(σ*)| ≍ e^{β*a₀/2}, coeficientes O(1) por `hyp:band`-demostrada y §5.3) — esto fija el **signo** mecánicamente, sin (†) y sin ajuste de fase: el término objetivo es −(m₀²/2)φ̂(0)²R² < 0 exacto, como en D136 Paso 2 pero sin normalizar a 1; (2) aniquilación σ y τ de **todos** los pares de tasa e^{β*a₀} (finitos bajo defecto finito: pares off×off del conjunto off, incluidos los (z₁,z₂) y (z₁,z₃) de §2.3 — nodos σ = ½+β-mixtos y τ ∈ {±δ-mixtos, ±iγ-mixtos}); (3) soporte asimétrico o τ-bump de soporte fijo para que la coordenada τ no fabrique exponenciales; (4) presupuesto de cola con los off restantes a tasa ≤ e^{(β*+β')a₀/2} < e^{β*a₀} (β′ < β* el segundo valor real distinto — aquí entra que el defecto es finito) y mar on-line polinomial; (5) re-cuantificación del Teorema 4.4 en régimen exponencial (E-149.3). **Bajo ¬RH general la rama queda abierta**, con la frontera exacta de §5.2: o un teorema de "gap en β" (no disponible, probablemente RH-duro), o celdas de clase Gevrey (bumps con decaimiento e^{−c|t|^{1/s}}, 1 < s < 1/θ(β*), legítimos por Denjoy–Carleman) más los teoremas de densidad como insumo — una ruta nueva, con cambio de diseño de la Def. 3.1, que esta auditoría registra como **Problema 149.A** sin prejuzgar su éxito (el escenario εₙ de 149.5 muestra que ni siquiera Gevrey basta si el sup no se alcanza; haría falta además elegir el cero testigo en función de a₀ y probar dominancia por subsucesiones — nada de esto es trivial).

---

## 6. Consecuencias para P47 y para el criterio logístico

1. **139.A sigue ABIERTO.** El veredicto "CERRADO-PARCIAL" del Doc 147 se revoca. La cadena `hyp:band` ⟹ Thm. 4.2 tiene el eslabón central (Prop. 3.1) roto en (3.4) y en (†), el trasplante a celdas sin derivar, y una hipótesis estructural tácita ("β* alcanzado y aislado") no declarada. El estado del criterio es el que dejó D139:
$$\mathrm{RH}\iff\lim_k\sigma_{loc}^{(k)}=0:\quad \text{rama RH: TEOREMA};\quad \text{rama ¬RH: ABIERTA (139.A)}.$$
2. **P47 no debe tocarse en la dirección que §6.3 de D147 propone.** Ni sustituir `hyp:pw` por `hyp:band` como hipótesis *suficiente* (no lo es: falta el signo), ni restaurar "both branches theorems" (falso con o sin eje real). Lo único importable de D147 a P47, con redacción honesta: (a) el diagnóstico estructural §1.3 (la normalización a 1 era el error; el marco no-normalizado es el correcto) — eso sí es un avance conceptual real; (b) `hyp:band` reparada como **lema demostrable de diseño** (§3.2, sin estatus de hipótesis-puente); (c) el eje de centro real como ampliación inocua de la grilla (§4.3), si se desea, sin ninguna afirmación de incondicionalidad.
3. **Dónde está ahora el muro, con coordenadas exactas:** ya no en una constante de Paley–Wiener (eso D147 sí lo disolvió: no hay 139.1-bis, el módulo es barato), sino en dos sitios nuevos y más profundos: (i) **fase**: el signo del plano objetivo es una fase que rota con a₀, controlable solo por prescripción Vandermonde a escala o por elección de a₀ en ventanas — ejecutable bajo defecto finito; (ii) **acumulación**: bajo ¬RH general, los ceros off no extremos de signo no controlado a tasa casi-máxima exigen un gap espectral en β que nadie tiene. La rama ¬RH del criterio logístico es hoy, honestamente: *teorema-esbozable bajo defecto finito (Doc 15x pendiente, lista §5.4); abierta en general, con obstrucción nombrada (Problema 149.A / escenario 149.5)*.
4. **Erratas para el expediente** (ERRATA.md): E-149.1 (cuantificador de (4.1)); E-149.2 = el error de conjugación de (3.4) y del párrafo "ι-fija aporta +" — **CRÍTICA**; E-149.3 (Teorema 4.4 sin re-cuantificar en régimen exponencial); E-149.4 (normalización B(0)=1 vs franja centrada en ½, D136 (3.1), alimenta la falacia de §6.2); E-149.5 (Lema 2.1: constantes dependen de γ₀; el enunciado con bump plano es falso en el conjunto de ceros de la transformada); E-149.6 (Prop. 3.1/Thm. 4.2 enuncian "cero off mínimo" mientras §5 exige parte real máxima — contradicción interna); E-149.7 ((3.6): término "poly(a₀)" para una cola que bajo ¬RH general es exponencial; pares (z₁,z₂)/(z₁,z₃) de tasa máxima omitidos).
5. **El patrón histórico, confirmado por tercera vez:** W_λ (una constante con signo equivocado sobrevivió meses); D136 (una constante que no era constante); D147 (un polinomio que era exponencial + una conjugación de más + un máximo que puede no existir). Las reparaciones de reparaciones concentran el error en el punto exacto donde el documento declara haber sido más cuidadoso: §3.4 se titula a sí mismo "la verificación de que NO hay constante divergente escondida" y contiene el error de conjugación; §5 se titula "anti-falsa-victoria" y presupone el máximo no garantizado. La regla operativa para Phase 48: **las secciones tituladas "verificación" se auditan primero.**

---

## Referencias

**Internas (backward-only):** D147 (todo); D139 (GAP-A, Lema 139.1, GAP-B, §4.4, Problema 139.A, E-139.5); D136 (Defs. 3.1–3.2, Lemas 5.2–5.3, Thms. 4.1–4.4, 5.4, Prop. 5.5, Obs. 5.1, (1.1)–(1.2), (3.1)); D108 (Prop. 2.2); D107 (Lemas 2.2(b), 5.2(b), Thm. 5.5, Prop. 6.1, cerradura x∂ₓ y modulación); D144 (sub-resolución); P43 (autonomía); ERRATA.md (Phase 38).

**Literatura (real, publicada; solo enunciados estándar):**
- R. P. Boas, *Entire Functions*, Academic Press (1954) — Cap. 1 §1.4 (tres rectas/Phragmén–Lindelöf), Cap. 2 (Hadamard, infinitud de ceros de funciones de tipo exponencial no triviales), Thm. 6.8.1 (Paley–Wiener).
- B. Ya. Levin, *Lectures on Entire Functions*, AMS TMM 150 (1996) — Lecc. 8–9 (indicador h(θ), crecimiento direccional; base del análisis §4.2).
- L. Hörmander, *The Analysis of Linear Partial Differential Operators I*, Springer (1990) — Thm. 7.3.1 (Paley–Wiener para C_c^∞; decaimiento superpolinomial con constantes dependientes del test, §1.2).
- A. E. Ingham, *On the estimation of N(σ,T)*, Quart. J. Math. Oxford 11 (1940) — N(σ,T) ≪ T^{4σ(1−σ)}log T (insumo del Cálculo 149.5; acota conteos, no la velocidad de acumulación en β).
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. 53 (2004) — Thm. 5.8 (N(t+1)−N(t) ≪ log t).
- A. Weil, *Sur les "formules explicites"…*, Comm. Sém. Math. Lund (1952) — el sentido ¬RH ⟹ ∃f: Q(f) < 0; nótese que su mecanismo real adapta el test al cero (fase incluida), no se sigue de paridad sola — la atribución de (3.3) de D147 a Weil con "c_W > 0 automático" no corresponde al argumento clásico.
- E. C. Titchmarsh, *The Zeros of Certain Integral Functions*, Proc. London Math. Soc. 25 (1926) — densidad de ceros de transformadas de soporte compacto (contexto §1.2: los ceros existen y se mueven con el test).

*Fin del Doc 149.*
