# Documento 192 — Ataque a la Conjetura 179.6 (141.E-mínima): la rigidez de continuación de Euler contra los casi-dobles evanescentes

**Programa:** Hipótesis de Riemann — Fase 58 (auditoría total)
**Fecha:** 2026-06-12
**Mandato:** atacar la [CONJ 179.6] — la cara de Euler del frente aritmético de la segunda torre — por el mecanismo de rigidez de continuación del D131 (Teo. 6.7, pureza local), con el test Davenport–Heilbronn (GAP-141.DH) como calibración previa del mecanismo. Aplicar las correcciones de la auditoría D187 (E-187.7, degradación de 179.5, cláusula de aislamiento de 179.4). Honestidad total; sin numérica.
**Prerrequisitos (certificados, no re-derivados):** D131 (Teo. 6.7 pureza local; Prop. 6.8 D–H; Deseo 6.9 H⁺; test de Mertens de dos protuberancias); D141 (Conj. 141.E, GAP-141.G1, GAP-141.DH, Cálculo 141.M5); D150 (veredicto GAP-141.DH corregido: liminf δ=0 vía Prop. 150.2, gordos β>1 incondicionales, LP-134^(log) para D–H ABIERTO); D179 (Def. 179.1, Prop. 179.2, GAP-179.A, Conj. 179.6) con las correcciones de D187 (§2.1–2.5); D178/187 (Cor 178.11 certificado: 178.C ∧ LP-134∞ ⟹ m<∞).

---

## 0. Convenciones (autocontenidas)

ζ = zeta de Riemann. **Cuádruplo off**: cero ρ=β+iγ con β>½, γ>0, más sus tres espejos; b:=β−½. **LP-134** (Def. 141.1): liminf_{off} b·log γ > 0. **LP-134∞** (forma mínima, Def. 179.1): ∃c>0 con b_j log γ_j ≥ c para infinitos j — equivalentemente, ¬(b_j log γ_j → 0 sobre toda la sucesión). **Categoría D131-H⁺ / "categoría de Euler"**: producto de Euler convergente en Re s>1 con dato local hermitiano + continuación meromorfa + ecuación funcional (tipo clase de Selberg [S92, CG93, KP99]).

**[CONJ 179.6 = 141.E-mínima]** (texto del D179 §5.3): *en la categoría de Euler con continuación, no existe ninguna sucesión infinita de cuádruplos off con b_j·log γ_j → 0.*

### 0.1. [E-192.1] Errata de cuantificador en el D179 — corregida antes de empezar

El D179 declara la Conj 179.6 "equivalente a LP-134∞ para los miembros de la categoría". **Falso tal como está escrita.** "No existe sucesión infinita con b_j log γ_j → 0" prohíbe toda *subsucesión* convergente a 0, i.e. equivale a liminf b log γ > 0 = **LP-134 plena**, no a LP-134∞ (que solo niega la convergencia de la sucesión *entera*). Una configuración con gordos en j=2^k y b_j log γ_j = 1/j en el resto satisface LP-134∞ y viola la 179.6 literal. Distinguimos:

- **[CONJ 179.6-fuerte]** (la literal): liminf b log γ > 0 en la categoría. = Conj. 141.E con escala log.
- **[CONJ 179.6∞]** (la que la torre necesita): ningún miembro de la categoría tiene b_j log γ_j → 0 sobre toda su sucesión de cuádruplos. Con [Cor 178.11, certificado en D187 §1.11]: 178.C ∧ 179.6∞(ζ) ⟹ m<∞.

Todo lo que sigue ataca 179.6∞ (lo mínimo) y registra qué diría para la fuerte. La errata se reporta para el registro de la fase; no daña la arquitectura (D187 §1.11 ya usaba la forma ∞ correcta).

---

## 1. Calibración previa: el test Davenport–Heilbronn (GAP-141.DH)

**Diseño del test.** La función f_DH de Davenport–Heilbronn [DH36] tiene ecuación funcional tipo ζ pero NO producto de Euler (combinación lineal de dos L de Dirichlet; D131 §6.6). Si D–H **viola** el análogo de 179.6, el Euler es esencial al mecanismo y la conjetura apunta bien; si D–H lo **satisface**, el mecanismo no es Euler y la conjetura apunta mal.

**Estado de los hechos, tras la corrección del D150 (que REFUTÓ el veredicto "GORDOS" del D146):**

1. **[DH36, incondicional]:** infinitos ceros off con β>1, i.e. b ≥ ½ ⟹ b log γ → ∞ sobre esa subsucesión. D–H satisface LP-134∞-análogo trivialmente (los gordos existen).
2. **[Prop. 150.2, incondicional]** (universalidad conjunta de Voronin + Rouché): para cada ε>0 fijo, ≫_ε T ceros de D–H con b ≍ ε. Luego **liminf_{off} b = 0**: D–H **viola la separación de banda** y viola toda forma "liminf b·(escala acotada) > 0".
3. **La escala crítica — ¿hay subsucesión con b_j log γ_j → 0 en D–H?** Esto es exactamente el caso (b)-vs-(d) de la Prop. 144.9, declarado ABIERTO por el D150 §4.4: la Prop. 150.2 da b ≍ ε a alturas de densidad positiva *para cada ε fijo*, pero el régimen ε = ε(T) → 0 requiere **universalidad efectiva** (control del tamaño de la primera τ admisible en función de ε), no disponible. **[GAP de literatura, heredado de D150 y no cerrado aquí]:** no conozco ningún resultado efectivo de acercamiento b vs altura para los ceros de D–H ([BS07] y la línea de Vaughan/Spira son cómputos y localizaciones a altura baja, no asintótica efectiva); no afirmo ninguno.

**[VEREDICTO DEL TEST 192.2 — el test decide a MEDIA escala].**
- **Para la 179.6-fuerte (liminf):** el test ESTÁ decidido y es **favorable al mecanismo-Euler**. D–H (sin Euler) tiene liminf b = 0 (Prop. 150.2): viola la versión sin-escala de la rigidez. La conjetura fuerte para la categoría de Euler no es vacía de contenido discriminante: hay un objeto natural con ecuación funcional que hace lo prohibido en cuanto se le quita el Euler. Pero atención a la honestidad de la escala: 150.2 da liminf b = 0, **no** liminf b log γ = 0 — en la escala log el test fuerte también queda abierto.
- **Para la 179.6∞ (la mínima):** el test está **ABIERTO en ambas direcciones**, y además es estructuralmente más exigente: ¬179.6∞ pide b_j log γ_j → 0 sobre *toda* la sucesión, y D–H NO puede satisfacer eso jamás — los gordos de [DH36] son infinitos y persisten. **Hallazgo del test: D–H no puede ser contraejemplo del análogo de 179.6∞ aunque su universalidad efectiva se probara.** La forma mínima es invulnerable al único contraejemplo natural conocido; el test solo muerde contra la forma fuerte.

**Lectura de calibración.** (i) El mecanismo-Euler queda **apoyado pero no confirmado**: la separación Euler/no-Euler está realizada en la naturaleza a escala ψ≍1 ("gordura barata, repulsión no", D150 §5.2), exactamente la dirección que 141.E predice; a la escala polilog —la única que importa para la torre— el test está fuera del alcance de la literatura. (ii) Subproducto lógico no trivial: la jerarquía D179 §1 se refleja en la testabilidad — la forma fuerte es falsable por D–H-efectivo, la forma mínima no es falsable por D–H en absoluto (los gordos la blindan). Debilitar la conjetura la hizo **menos falsable**, no más atacable: el patrón del GAP-179.A otra vez, ahora del lado de los tests.

---

## 2. El ataque cuantitativo

Sea (b_j, γ_j) una sucesión hipotética de cuádruplos de una L de la categoría (o de ζ) con ε_j := b_j log γ_j → 0.

### 2.1. Vía (a): el doblete en la derivada logarítmica — la pared, medida exacta

Un cuádruplo off es, a ordenada γ_j, el par gemelo {½±b_j+iγ_j}. La cantidad que el producto de Euler controla directamente es −ζ'/ζ(s) = Σ Λ(n) n^{−s} en Re s>1. ¿Distingue el semiplano de Euler un par gemelo de un cero doble en la línea?

**[LEMA 192.3] (invisibilidad del discriminante desde el semiplano de Euler).** Sea w := s−(½+iγ_j) con Re s ≥ 1 (luego |w| ≥ ½). La diferencia entre la contribución del par gemelo y la de un cero doble en ½+iγ_j a la derivada logarítmica es
$$\Delta_j(s)\;=\;\frac{1}{w-b_j}+\frac{1}{w+b_j}-\frac{2}{w}\;=\;\frac{2b_j^2}{w(w^2-b_j^2)},\qquad |\Delta_j(s)|\;\le\;\frac{2b_j^2}{|w|\,(|w|^2-b_j^2)}\;\le\;17\,b_j^2$$
para b_j ≤ 1/10. En particular, sobre todo el semiplano cerrado Re s ≥ 1 la señal del discriminante es uniformemente O(b_j²) = O(ε_j²/(log γ_j)²).

*Demostración.* Identidad algebraica directa (común denominador). La cota: |w−b_j||w+b_j| ≥ |w|²−b_j² ≥ ¼−1/100, y |w|≥½; 2b²/(½·(¼−b²)) ≤ 17b². ∎

**La pared, con números.** Para detectar Δ_j desde la aritmética hay que evaluar Σ Λ(n) n^{−s} cerca de s = 1+iγ_j con error o(b_j²) = o(ε_j²/(log γ_j)²). Lo que se sabe incondicionalmente: (i) Mertens/Chebyshev dan Σ_{p≤x} (log p)/p = log x + O(1) — error O(1); (ii) el "mar" de los demás ceros aporta a −ζ'/ζ(1+iγ) términos de tamaño total O(log γ_j) (densidad RvM); (iii) ninguna región libre de ceros incondicional (Vinogradov–Korobov incluida) resuelve por debajo de b ≍ (log γ)^{−2/3−}. Cociente señal/ruido:
$$\frac{\text{señal}}{\text{ruido}}\;\asymp\;\frac{\varepsilon_j^2/(\log\gamma_j)^2}{\log\gamma_j}\;=\;\frac{\varepsilon_j^2}{(\log\gamma_j)^3}\;\longrightarrow\;0\ \text{(cúbicamente, y con } \varepsilon_j\to0\text{ encima)}.$$
**Es el mismo muro que GAP-141.G1/GAP-179.A, en su peor cara.** Identificación precisa: GAP-141.G1 pedía error o(1) relativo a señal (bL)² con b ≍ 1/log γ en ventanas en la *línea*; GAP-179.A (D179 §5.2) lo endureció a o((b_jL_j)²) con (b_jL_j)² = ε_j² → 0 en infinitas ventanas enemigas; la versión semiplano de aquí pierde **además** el factor (log γ)² de la ventana resonante (en Re s ≥ 1 no hay resonancia que amplifique: la señal es b², no (bL)²). Conclusión: **no es un gap nuevo — es GAP-179.A degradado por el cambio de carta al semiplano**. El producto de Euler, usado como *estimación*, es estrictamente peor que la fórmula explícita en la línea. La vía (a) muere; el dividendo es el Lema 192.3, que convierte "la señal es de segundo orden" (sabido) en una cota uniforme exacta con constante, y el corolario de no-go:

**[COR 192.4].** Ningún esquema de detección que use finitos valores de −L'/L en Re s ≥ 1 con precisión peor que cb_j² puede distinguir el par gemelo (b_j, γ_j) de un cero doble en la línea; en particular ninguna cota incondicional conocida de sumas de primos (error ≥ O(1)) detecta cuádruplos con ε_j → 0. *Prueba: Lema 192.3 más (i)–(ii).* ∎

### 2.2. Vía (b): ¿qué da el Teo. 6.7 del D131 aquí?

El mecanismo del Teo. 6.7 (test de Mertens de dos protuberancias): la impureza local δ' de F_{p,α} (|α| = p^{½+δ'}) se detecta porque |c_M| > 2p^{M/2} **para M grande** — cuantitativamente, p^{Mδ'} − p^{−Mδ'} > 2 exige M ≳ 1/(δ' log p): **soporte del test ≍ 1/δ'**. Tres razones por las que NO se transporta a 179.6:

1. **Geometría del divisor.** El objeto de 6.7 tiene *progresiones verticales completas* de ceros en Re = β — la impureza es global y periódica, y el coeficiente c_M la acumula coherentemente (c_M = α^M + (p/ᾱ)^M, crecimiento exponencial puro). El enemigo de 179.6 tiene **un** cuádruplo por altura, con b_j *decreciente*: su huella en los coeficientes es la de un solo término oscilante x^{b_j}cos(γ_j log x) — sin acumulación coherente. La pureza local es un dial de toda-una-columna; 179.6 es sobre ceros individuales.
2. **La cuenta de soporte.** Trasladando el umbral de 6.7: impureza efectiva b_j visible recién a soporte log x ≍ 1/b_j = (log γ_j)/ε_j, i.e. **x ≥ γ_j^{1/ε_j}**, super-polinomial en γ_j. Es exactamente la encarnación-Euler del Cálculo 141.M5 (señal de ancho b necesita resolución e^{1/b}); el Teo. 6.7 puede pagar ese soporte porque su categoría tiene UN primo y cero ruido — ζ tiene el mar on-line aportando O(log γ) por ventana (§2.1). **El Teo. 6.7 es el caso ruido-cero del problema; su prueba mide el tamaño de la pared, no la atraviesa.**
3. **El propio D131 lo advierte** (§6.5, comentario (iii)): "el producto de Euler no implica H" — F_{p,α} impuro tiene Euler, ecuación funcional y viola la positividad con ceros off en columna a b fijo. Eso no toca a 179.6∞ (esa configuración tiene b constante: LP-134 se cumple de sobra), pero sí enseña que la rigidez de Euler, si existe, no es la multiplicatividad sola: es multiplicatividad + **positividad del dato** (a = Λ ≥ 0, Deseo 6.9) + continuación. La Conj 179.6 hereda esa condición: debe enunciarse en la subcategoría a ≥ 0 (en la clase de Selberg general hay que asumir al menos hermitianidad del dato local, como hace la definición §0).

**Veredicto de la vía (b): el D131 da la *forma* del mecanismo (impureza visible a soporte 1/impureza; la continuación acopla los datos locales) y ningún teorema cuantitativo aplicable.** La rigidez de continuación sigue siendo conjetura con mecanismo plausible y cero estimaciones.

### 2.3. Vía (c): rigidez de deformación de la clase de Selberg

Hechos de rigidez reales y backward-verificables: grado d ∈ {0} ∪ [1,∞) con (0,1) vacío [CG93]; d=1 clasificado (ζ y L de Dirichlet desplazadas) [KP99]; 1<d<2 vacío [KP02-11]. La clase es **discreta en sus invariantes**: no hay familias continuas no triviales (deformar el dato de Euler manteniendo continuación + ecuación funcional cae fuera de la clase salvo en los parámetros aritméticos discretos).

**¿Da eso 179.6?** No, y la razón es de cuantificadores: la rigidez de deformación prohíbe *familias de funciones*; el enemigo de 179.6 es **una sola función** cuya sucesión interna de cuádruplos degenera (b_j → 0 es un límite *dentro* del divisor de un único objeto, no una curva en el espacio de objetos). Para que la rigidez de la clase mordiera haría falta un puente del tipo "una sucesión de casi-degeneraciones internas induce una deformación del dato local en el límite" — que es exactamente la Conj. 141.E sin probar, reformulada. **Enunciado mínimo de esta vía, formulado para el registro:**

**[ENUNCIADO MÍNIMO 192.5 — rigidez espectral de la clase, forma necesaria].** *Si L ∈ S (clase de Selberg, dato hermitiano) tiene cuádruplos con b_j log γ_j → 0, entonces la sucesión de "datos locales renormalizados a la ventana de γ_j" tiene un punto de acumulación que es el dato de un objeto con cero doble en la línea — objeto que la clase prohíbe (o cuya existencia implicaría una familia continua, prohibida por [CG93/KP]).* Estatus: **[GAP-192.A]** — la primera mitad (compacidad de datos locales renormalizados + identificación del límite) no existe en la literatura ni en el programa; la segunda mitad (la prohibición del límite) tampoco: un cero doble EN la línea no está prohibido en S (la simplicidad de ceros es conjetura abierta, D179 §3.2). Tal como está, la vía (c) reduce 179.6 a dos enunciados desconocidos. Honestidad: es la vía con mejor *forma* (es la única donde el límite b→0 se convierte en objeto) y peor *suelo* (ninguna de sus dos piezas tiene análogo probado).

---

## 3. La dirección inversa: ¿es 179.6 siquiera cierta? — el mundo lógico que habita

**Búsqueda de contraejemplo en la categoría.** (i) Zetas de Epstein con número de clase h>1: ceros off conocidos (Davenport–Heilbronn mismo método) pero **sin Euler** (la forma cuadrática no es multiplicativa para h>1) — fuera de la categoría ✓ consistente. (ii) Combinaciones lineales de caracteres (D–H incluido): sin Euler, fuera ✓. (iii) L de Artin no probadamente enteras: tienen Euler; su pertenencia a S depende de holomorfía (Artin abierta), y bajo las conjeturas estándar son automorfas ⟹ GRH esperada — ningún cero off conocido. (iv) **No se conoce ningún miembro de la clase de Selberg con un solo cero off**, mucho menos con la sucesión evanescente. Resultado de la búsqueda: vacía, y vacía por la razón estructural correcta (todo lo que tiene ceros off conocidos carece de Euler).

**El mundo lógico de 179.6.** Bajo la conjetura estándar (GRH para S), 179.6 es **vacuamente cierta** (no hay cuádruplos). Su contenido entero vive en el mundo ¬GRH: dice que *si* los ceros off existen, respetan la repulsión polilog (al menos no son todos evanescentes). Es un peldaño estrictamente más débil que RH-para-la-clase y estrictamente más fuerte que nada: el primer enunciado de la cadena GRH ⟹ LP-134(S) ⟹ 179.6-fuerte ⟹ 179.6∞ que tiene mecanismo candidato propio (la continuación) en vez de positividad. Eso es lo que la hace atacable en principio — y es lo único: ninguna conjetura estándar *distinta de GRH* la implica (los teoremas/conjeturas de densidad mueren en s ≍ 1/log T por la Prop. 176.9, aplicable miembro a miembro; la simplicidad de ceros no da separación, D179 §3.2).

---

## 4. Test anti-circularidad

| Objeto | ¿RH-libre? | ¿ζ-libre? | Dónde reentra ζ/aritmética |
|---|---|---|---|
| E-192.1 (cuantificador) | sí (lógica) | sí | no reentra |
| Veredicto del test 192.2 | sí | sí (D–H + Voronin, citados) | el GAP de literatura es de D–H, no de ζ |
| Lema 192.3 / Cor 192.4 | sí | sí (álgebra de fracciones parciales + Mertens) | el no-go usa solo cotas incondicionales |
| §2.2 (D131) | sí | sí (categoría) | la rigidez conjetural ES el lugar donde Euler debe entrar |
| Enunciado 192.5 / GAP-192.A | — | no (clase de Selberg) | compacidad de datos locales: aritmética pura, sin candidato |

Ninguna prueba usa RH ni numérica. El patrón se mantiene: lo demostrado (192.3/192.4) es un no-go; la aritmética queda en los GAPs.

---

## 5. Veredicto

**CONJ 179.6: NI PROBADA NI REFUTADA. Estado final: CALIBRADA-CONDICIONAL (implicada solo por GRH-para-S, vacuamente) y REDUCIDA en su única vía cuantitativa al MISMO muro (GAP-179.A, cara semiplano, estrictamente peor), con el mecanismo-Euler APOYADO a media escala por el test D–H.**

1. **[E-192.1]** La 179.6 literal del D179 es LP-134-fuerte, no LP-134∞; la torre solo necesita 179.6∞. Errata reportada; arquitectura intacta (Cor 178.11 ya usaba la forma correcta).
2. **[Test D–H, 192.2 — la calibración encargada]:** decidido a escala banda (**favorable**: D–H sin Euler tiene liminf b = 0, Prop. 150.2 — el Euler es esencial para la forma fuerte de la rigidez); **abierto a escala polilog** (caso (b)-vs-(d) de 144.9, requiere universalidad efectiva — [GAP de literatura] heredado de D150, no cerrado). Hallazgo: **D–H no puede refutar 179.6∞ jamás** (sus gordos [DH36] son infinitos): la forma mínima es estructuralmente in-falsable por el único contraejemplo natural. El mecanismo apunta bien para la fuerte; para la mínima el test es mudo.
3. **[LEMA 192.3 + COR 192.4] (lo probado):** desde el semiplano de Euler, el discriminante par-gemelo/cero-doble es uniformemente ≤ 17b² ; ninguna estimación incondicional de sumas de primos (error ≥ O(1) contra señal ε_j²/(log γ_j)² y ruido O(log γ)) lo detecta. **El muro de la vía Euler-cuantitativa es GAP-179.A otra vez — no uno nuevo — y en peor carta** (sin el factor resonante (log γ)² de la línea): el producto de Euler usado como estimación es más débil que la fórmula explícita, no más fuerte.
4. **[Vía D131]:** el Teo. 6.7 da la forma del mecanismo (impureza visible a soporte 1/impureza) y nada cuantitativo transportable: es el caso ruido-cero y columna-completa; el enemigo de 179.6 es individual y evanescente. La rigidez de continuación sigue sin una sola estimación.
5. **[Vía rigidez de clase, 192.5 / GAP-192.A]:** la discreción de la clase de Selberg ([CG93], [KP99-11]) ataca el cuantificador equivocado (familias, no degeneraciones internas); el puente "casi-degeneración interna ⟹ deformación del dato" es 141.E renombrada. Reducción honesta: 179.6 ⟸ (compacidad de datos locales renormalizados) ∧ (prohibición del cero doble límite) — dos piezas sin análogo en la literatura, la segunda equivalente a una forma efectiva de simplicidad (= GAP-179.B otra vez).

**GAPs numerados:**
- **[GAP-192.A]** (vía de clase): compacidad/convergencia de datos locales renormalizados a la ventana de γ_j para una L ∈ S con b_j log γ_j → 0, e identificación del límite como objeto con cero doble en línea. Sin candidato de herramienta; la mitad "prohibición del límite" colapsa a GAP-179.B (separación efectiva ≡ Liouville del discriminante).
- **[GAP-192.B = GAP de literatura, heredado de D150]:** universalidad efectiva para D–H (primera τ admisible en función de ε) — decidiría el test a escala polilog y, con él, si la 179.6-fuerte está bien apuntada.
- **El muro residual NO es nuevo:** la vía cuantitativa muere en GAP-179.A (forma io de GAP-141.G1), confirmando la jerarquía del D179 §5.2 con una cara más: línea (G1) < línea-io (179.A) < semiplano (192.4, sin resonancia). Tres caras, un muro.

**Dirección sucesora.** (i) La única vía con forma nueva es GAP-192.A: intentar la compacidad de datos locales con la topología del D131 (la categoría ya tiene la noción de dato local; falta la renormalización a ventana) — sesión de construcción, riesgo alto, pero es el único lugar donde "b_j → 0" se vuelve objeto en vez de estimación. (ii) GAP-192.B es el único ítem decidible con literatura previsible (universalidad efectiva es un área activa); cerrarlo calibraría la fuerte de una vez. (iii) Para la torre: nada de esta sesión mueve la pinza 178.C ∧ LP-134∞ — el frente aritmético sigue siendo un enunciado con tres caras (179.4 dinámica / 179.B estática / 179.6 de Euler) y las tres reconducen al mismo muro de segundo orden; la asimetría descubierta aquí (la forma mínima es la menos falsable) sugiere que el próximo ataque debe ir a la **fuerte** vía 192.B, no a la mínima.

---

### Referencias

**Internas (backward-only):** D131 (Teo. 6.7, §6.5 test de Mertens, §6.6 Prop. 6.8, Deseo 6.9); D141 (Conj. 141.E, GAP-141.G1, GAP-141.DH, Cálculo 141.M5); D144 (Prop. 144.9, Cor. 144.10); D146 con el veredicto corregido por D150 ([Prop. 150.2], veredicto GAP-141.DH corregido §4.4, "gordura barata" §5.2); D176 (Prop. 176.9); D178 (Cor 178.11); D179 (Def. 179.1, Prop. 179.2, §3.2, GAP-179.A, GAP-179.B, Conj. 179.6); D187 (E-187.7, §1.11, §2.3–2.5, degradación de 179.5).

**Literatura:** H. Davenport, H. Heilbronn, *On the zeros of certain Dirichlet series I, II*, J. London Math. Soc. 11 (1936), 181–185, 307–312. — A. Selberg, *Old and new conjectures and results about a class of Dirichlet series*, Proc. Amalfi Conf. (1989), Salerno 1992. — J. B. Conrey, A. Ghosh, *On the Selberg class of Dirichlet series: small degrees*, Duke Math. J. 72 (1993), 673–693. — J. Kaczorowski, A. Perelli, *On the structure of the Selberg class I: 0≤d≤1*, Acta Math. 182 (1999), 207–241; *VII: 1<d<2*, Ann. of Math. 173 (2011), 1397–1441. — E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2.ª ed. (Heath-Brown), Oxford 1986, §10.25. — E. P. Balanzario, J. Sánchez-Ortiz, *Zeros of the Davenport–Heilbronn counterexample*, Math. Comp. 76 (2007), 2045–2049. — R. Spira, *Some zeros of the Titchmarsh counterexample*, Math. Comp. (1968). — S. M. Voronin, *Theorem on the "universality" of the Riemann zeta-function*, Izv. Akad. Nauk SSSR 39 (1975).
