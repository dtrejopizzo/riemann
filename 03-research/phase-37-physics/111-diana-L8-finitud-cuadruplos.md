# Doc 111 — La diana L8: ¿es alcanzable una cota incondicional sobre el número de cuádruplos off-críticos?

**Phase 37 — Modo físico · junio 2026**
**Autor: David Alejandro Trejo Pizzo**
**Prerrequisitos:** Doc 108 (Prop. 2.3/2.5; Teorema 3.4 "dos mundos"; Conjetura 108-N y Teorema 4.3; §5; §8.1–8.2: κ_W ≤ C·n_W ⟹ m ≤ C/2); P43 (Principio 3.1; ledger L8; §6); Doc 98 (juguete m = 1: κ = 2, Prop. 6.1; Cor. 2.4); Doc 107 (Prop. 6.1); Doc 100 (positividad semilocal, MW-7); P35 (κ = 2m); P41; P42 (§6).
**Regla absoluta:** ninguna prueba se fabrica; cada paso es demostración completa, cálculo cerrado o GAP declarado. Sin numéricos ni simulaciones. Citas backward-only; lo no verificado se marca [NO VERIFICADO].

---

## 0. Resumen ejecutivo

**La diana.** Sea m el número de cuádruplos de ceros off-críticos de ζ (Doc 98, Hipótesis T1:
cada violación de RH aporta un cuádruplo {½±δ±iγ₀}; m = 0 ⟺ RH; bajo ¬RH, m ∈ {1, 2, …}
∪ {∞}). El ítem L8 del ledger de P43 registra: una cota incondicional κ_W ≤ C·n_W sobre los
índices por ventana daría m ≤ C/2 (Doc 108, Obs. 8.1) — un teorema **estrictamente más débil
que RH** ("a lo sumo C/2 excepciones") que sería histórico aunque no resuelva RH. Este
documento mide si ALGUNA cota de finitud sobre m es alcanzable, o si "m finito" ya está
detrás del mismo muro que "m = 0".

**Hallazgos, en orden:**

1. **(§2) El inventario incondicional no contiene ningún teorema que prohíba m finito no
   nulo, y no puede contenerlo sin aritmética.** Se demuestra (Prop. 2.2) que en la clase
   "física" del programa (enteras de orden 1, ecuación funcional, simetría real — la
   clase ℰ del arco variacional) existen elementos con exactamente m cuádruplos para todo
   m finito: cualquier teorema "m ≥ 1 ⟹ m = ∞" debe usar el producto de Euler. En la
   literatura no existe tal teorema (§2.5). La región hoy excluida de (δ, γ₀) es
   {γ₀ ≤ 3·10¹²} (Platt–Trudgian) ∪ {δ > ½ − c/((log γ₀)^{2/3}(log log γ₀)^{1/3})}
   (Korobov–Vinogradov); las positividades parciales probadas no agregan nada (§2.4).

2. **(§2.6) El inventario completo es binario.** Todo teorema conocido sobre conteos de
   ceros off-críticos produce o bien **0** (regiones libres) o bien **T^θ, θ > 0**
   (densidad): no existe enunciado que produzca un conteo "finito no nulo uniforme en la
   altura". La binariedad del índice por ventanas (Doc 108, Prop. 2.5) es caso particular
   de una binariedad de todo el inventario.

3. **(§3) El mecanismo de Siegel NO tiene análogo para cuádruplos de ζ.** La repulsión de
   Landau–Page–Siegel funciona porque cerca de s = 1 el presupuesto de positividad es **el
   polo simple — un presupuesto global O(1)** — y dos ceros no pueden comérselo a la vez.
   Para ζ misma: (a) la "zona de Siegel" en el aspecto s (β cerca de 1) **ya es libre de
   ceros incondicionalmente** — la región libre clásica ES la repulsión polo→cero, vía
   3+4cos θ+cos 2θ ≥ 0; (b) en el interior de la franja el presupuesto local de positividad
   a altura γ₀ es el mar arquimediano ≍ log γ₀: **crece**, no hay escasez, no hay
   repulsión; (c) el término cruzado de dos cuádruplos en la fórmula explícita, de tamaño
   X^{δ₁+δ₂} < X, queda **debajo** de la barra de error de Montgomery–Vaughan igual que los
   diagonales X^{2δᵢ} < X, y su detección exige resolución simultánea en dos frecuencias
   desconocidas: la pareja se ve **peor** que el cuádruplo solo (anti-Siegel, §3.4).

4. **(§4) Turán no da finitud.** Las sumas de potencias dan cotas inferiores de oscilación
   de ψ(x)−x forzadas por los cuádruplos (degradándose exponencialmente en el número de
   términos); la contradicción exigiría una cota superior |ψ(x)−x| = o(x^{½+δ}), y por el
   teorema recíproco clásico (Landau/Ingham) esa cota ES la cuasi-RH que se quería
   concluir: circularidad exacta. Queda solo finitud en cajas compactas,
   m(δ₀, Γ) ≤ N(½+δ₀, Γ) < ∞, que ya la dan los teoremas de densidad trivialmente; toda
   la no-trivialidad de L8 es la uniformidad en Γ (§4.3).

5. **(§5) La cuenta central — ventanas excepcionales vs. momentos incondicionales:**
   (a) las estadísticas con teorema límite incondicional (S(T), CLT de Selberg) son
   **ciegas** a la abscisa: un cuádruplo es indistinguible, para S(t), de un cero doble
   on-line a la misma altura (Lema 5.1); la concentración gaussiana no limita m en
   absoluto. (b) La estadística que sí ve (déficit de segundo orden) aporta por cuádruplo
   señal ≍ X^{2δ} contra una barra de error incondicional O(X·log²X) en el valor medio de
   Montgomery–Vaughan: invisible para todo δ < ½ y todo m, **incluso m = ∞ de densidad
   cero** (Prop. 5.3). (c) Los valores grandes toleran R ≪ T^{θ(δ)} ventanas excepcionales
   con θ(δ) > 0 estricto para todo δ < ½ — eso ES el teorema de densidad leído al revés;
   ningún momento finito baja la tolerancia a O(1); el límite k → ∞ uniforme es el
   cuantificador maestro otra vez (§5.4). (d) El pigeonhole "m ≥ M ⟹ M ventanas con
   déficit simultáneo" no rompe la circularidad: el déficit acumulado M/log T queda debajo
   de la barra de error de todo valor medio accesible (§5.5).

6. **(§6) Síntesis — la dicotomía presupuesto/costo.** Un teorema m ≤ C exige un funcional
   B con (P1) cota incondicional y (P2) costo mínimo uniforme c > 0 por cuádruplo. El
   inventario entero se parte en dos clases excluyentes: acotados con costo evanescente
   (T_λ: costo 2δ²K_λ(γ₀) → 0, Doc 98 Cor. 2.4) y de costo uniforme con acotación
   RH-equivalente (κ_W: costo 2, cota uniforme = RH, Doc 108 Prop. 2.5). Los dos
   precedentes históricos de "a lo sumo k excepciones" tienen exactamente (P1)+(P2):
   Siegel (presupuesto = orden del polo = 1) y Weil en cuerpos de funciones (presupuesto =
   dim H¹ = 2g, finitud ANTES de pureza). L8 es el avatar contable de la
   finito-dimensionalidad cohomológica; el análisis no dispone de ningún presupuesto O(1)
   con costo uniforme, y fabricarlo desde promedios es la inversión del cuantificador.

**VEREDICTO: DIANA INALCANZABLE con las formas de argumento catalogadas** (§7), con la
precisión de que L8 NO colapsa a RH: "m finito" sigue siendo lógicamente estrictamente más
débil que RH (no probamos ni existe "m ≥ 1 ⟹ m = ∞"), de modo que la diana queda viva como
objetivo para un mecanismo nuevo — y el §6 dice exactamente qué forma debe tener ese
mecanismo: un presupuesto global acotado con costo mínimo por cuádruplo.

---

## 1. La diana: definiciones y estatus lógico

### 1.1. El parámetro m

**Definición 1.1.** Por la ecuación funcional ξ(s) = ξ(1−s) y la realidad de ξ sobre la
recta crítica (reflexión de Schwarz), todo cero ρ = β+iγ con β ≠ ½ genera el cuádruplo
{ρ, ρ̄, 1−ρ, 1−ρ̄} = {½±δ±iγ₀} con δ = β−½ ∈ (0,½), γ₀ = |γ| > 0 (Doc 98, §1.1; el caso
γ = 0 está excluido: ζ no tiene ceros reales en (0,1), hecho clásico). Definimos
$$m := \#\{\text{cuádruplos off-críticos de } \zeta\} \in \{0, 1, 2, \dots\} \cup \{\infty\},$$
contados con multiplicidad. Entonces m = 0 ⟺ RH.

**Definición 1.2 (la diana L8).** Un enunciado incondicional de la forma **m ≤ C** para
alguna constante absoluta C < ∞. Por P43 (ledger, L8) y Doc 108 (§8.2, Obs. 8.1), la ruta
identificada es κ_W ≤ C·n_W (cota lineal-en-densidad del índice por ventanas de la forma
doble Q₂), que implica 2m·n_W(1+o(1)) ≤ C·n_W y de ahí m ≤ C/2.

### 1.2. Qué valdría m ≤ C

Tres observaciones sobre el valor del enunciado, para calibrar la honestidad de la medición:

(a) **Sería más fuerte que todo teorema de densidad conocido en su región:** los N(σ,T)
dan o(T) ceros off hasta altura T; una cota absoluta independiente de T no existe para
ningún σ < 1 (§2.6).

(b) **Daría "RH salvo finitas excepciones acotadas":** ψ(x) = x + O(x^{½+δ_max+ε}) con a
lo sumo C/2 términos oscilantes explícitos; positividad de Weil sobre un subespacio de
codimensión ≤ 2C (P35: κ = 2m ≤ C); un espacio de Pontryagin con parte negativa de
dimensión a priori finita — la situación de partida de la teoría de cuerpos de funciones
antes de la positividad de Castelnuovo (§6.3).

(c) **No implicaría RH** (para C ≥ 2 no fuerza m = 0): pasa el test de "RH disfrazada"
(discriminador I2a, Doc 99) en su enunciado. La pregunta del documento es si lo pasa en su
**demostrabilidad**: si toda ruta de prueba re-encodea la uniformidad RH-equivalente.

### 1.3. Las tres salidas posibles (encargo, punto (v))

(A) Existe un camino concebible a m ≤ C con técnica actual — habría que enunciar el lema
exacto y su insumo. (B) "m finito" es equivalente o casi-equivalente a RH — en particular
si existe o se prueba "m ≥ 1 ⟹ m = ∞", la diana colapsa: finito = 0 y toda cota de finitud
ES RH. (C) La diana queda detrás del cuantificador maestro (P43, Principio 3.1), con
localización exacta. Los §§2–5 ejecutan la medición; el §6 decide.

---

## 2. (i) Inventario exhaustivo: qué se sabe sobre la estructura de ¬RH

### 2.1. La simetría cuádruple y su única consecuencia estructural gratuita

La simetría (Def. 1.1) es el único teorema incondicional de la forma "si existe un cero
off-crítico, entonces…" cuyo contenido es sobre la **configuración**: el cero trae consigo
otros tres. Consecuencia: m está bien definido y κ = 2m (P35; Doc 98, Prop. 6.1: dos planos
hiperbólicos por cuádruplo). No se conoce ninguna otra rigidez configuracional
incondicional: nada fuerza que dos cuádruplos compartan altura, abscisa, ni relación
aritmética alguna.

### 2.2. ¿Puede la parte "física" (simetría + crecimiento) prohibir m finito?

No. Lo demostramos en la clase del propio programa.

**Proposición 2.2 (realizabilidad de todo m finito en la clase ℰ).** Sea ℰ la clase de
funciones enteras F de orden ≤ 1, con F(s) = F(1−s) y F(½+is) real para s real (la clase
del arco variacional, Docs 93–98). Para todo m ∈ {0, 1, 2, …} existe F ∈ ℰ con exactamente
m cuádruplos de ceros fuera de la recta Re s = ½ y todos los demás ceros sobre ella, en
cantidad infinita.

*Demostración.* Sea F₀(s) := cosh(a(s−½)) con a > 0: entera de orden 1, F₀(1−s) =
cosh(−a(s−½)) = F₀(s), y F₀(½+is) = cos(as) ∈ ℝ para s ∈ ℝ, con ceros exactamente en
s = ½ + iπ(k+½)/a, k ∈ ℤ — todos sobre la recta crítica, simples, infinitos. Para cada
j = 1, …, m elíjase δⱼ ∈ (0,½), γⱼ > 0, y póngase
$$P_j(s) := \bigl((s-\tfrac12)^2-(\delta_j+i\gamma_j)^2\bigr)\,\bigl((s-\tfrac12)^2-(\delta_j-i\gamma_j)^2\bigr),$$
polinomio mónico de grado 4 en (s−½), par en (s−½) — luego Pⱼ(1−s) = Pⱼ(s) — y con
coeficientes reales en (s−½)² (el producto de los dos factores conjugados), luego
Pⱼ(½+is) = (−s²−(δⱼ+iγⱼ)²)(−s²−(δⱼ−iγⱼ)²) = |s²+(δⱼ+iγⱼ)²|² ≥ 0 real para s real. Sus
ceros son exactamente el cuádruplo {½±δⱼ±iγⱼ}. Entonces F := P₁⋯P_m·F₀ ∈ ℰ (producto de
entera de orden 1 por polinomio: orden 1; las simetrías se multiplican) tiene exactamente
m cuádruplos off y los infinitos ceros de F₀ on-line. ∎

**Corolario 2.3 (la finitud no está obstruida por la física).** Cualquier teorema
"m ≥ 1 ⟹ m = ∞" para ζ debe usar la estructura aritmética (serie de Dirichlet con
coeficientes 1, producto de Euler), no solo la ecuación funcional, la realidad y el orden
de crecimiento: en la clase definida por estas últimas, m = 1 es realizable (Prop. 2.2 con
m = 1). Lo mismo vale para cualquier cota m ≤ C: como teorema sobre ℰ es falso para todo
C (tomar m = C+1 cuádruplos); como teorema sobre ζ requiere insumo aritmético.

**Observación 2.4 (el escalón siguiente, declarado abierto).** Con serie de Dirichlet y
ecuación funcional pero **sin** producto de Euler, se conocen ejemplos con infinitos ceros
off-críticos (Davenport–Heilbronn, 1936: combinación de L-funciones con ecuación funcional
de tipo Riemann y ceros en Re s > 1; exposición en Titchmarsh [T86], §10.25). No se conoce
ningún ejemplo en esa clase intermedia con **exactamente un** cuádruplo off, ni una prueba
de que no exista: GAP declarado (no load-bearing: el Corolario 2.3 ya fija que el insumo
necesario es aritmético; este gap solo mediría cuánta aritmética).

### 2.3. Teoremas de densidad: lo que dicen y lo que no

Inventario verificado (enunciados estándar; [T86] Cap. IX, [IK04] Cap. 10):

- **Bohr–Landau (1914).** Para σ > ½ fijo, N(σ,T) = O(T): la proporción de ceros con
  β > ½+ε es 0 (contra N(T) ∼ (T/2π)log T). Primer teorema de "densidad cero" de las
  excepciones; compatible con m = 1 y con m = ∞.
- **Carlson (1920).** N(σ,T) ≪ T^{4σ(1−σ)+ε}.
- **Ingham (1940).** N(σ,T) ≪ T^{3(1−σ)/(2−σ)} log⁵T; bajo Lindelöf, N(σ,T) ≪ T^{2(1−σ)+ε}
  (densidad). Además [In40]: el exponente de densidad controla huecos entre primos.
- **Huxley (1972).** N(σ,T) ≪ T^{12(1−σ)/5+ε}; el rango σ ≥ ¾ mejorado desde entonces
  (Bourgain y otros; constantes exactas no load-bearing aquí).
- **Halász–Turán (1969).** Cerca de σ = 1: N(σ,T) ≪ T^{c(1−σ)^{3/2}} (log T)^{O(1)} —
  el método de sumas de potencias de Turán (relevante en §4).
- **Linnik (log-free, 1944; forma moderna [IK04] Thm. 10.4 y Cap. 18).** Densidad log-free
  N(σ,T) ≪ T^{c(1−σ)}: la base de Deuring–Heilbronn cuantitativo.
- **Vinogradov–Korobov (1958).** Región libre: no hay ceros con
  β ≥ 1 − c/((log|γ|)^{2/3}(log log|γ|)^{1/3}), |γ| ≥ 3. Conteo **cero** en esa región.
- **Selberg (1942) / Levinson (1974) / Conrey (1989).** Proporción positiva de ceros ON
  line: ≥ 1/3, ≥ 2/5; mejoras por encima de 5/12 [valor y autoría NO VERIFICADOS; no
  load-bearing]. Acotan la proporción que NO puede ser excepción; nada sobre el conteo
  absoluto de excepciones.

**Qué no hay:** ningún teorema de la lista (ni ninguno conocido) prohíbe m finito no
nulo, ni fuerza acumulación ("si hay un cero off, hay otro cerca"), ni produce una cota
de conteo independiente de T para ningún σ < 1. Tampoco vía ζ′: el teorema de Speiser
(1934; refinado por Levinson–Montgomery 1974: N⁻(T) = N₁⁻(T) + O(log T)) **transporta**
la pregunta de finitud a ζ′ con el mismo estatus; no la reduce.

### 2.4. Positividades parciales probadas: ¿excluye algo un cuádruplo extremo?

La pregunta del encargo: ¿un cuádruplo con (δ, γ₀) extremos contradice alguna positividad
**probada**? Las positividades probadas y su alcance:

(a) **Positividad de Weil de soporte chico / semilocal (Connes–Consani; Doc 100).** Para
tests con soporte multiplicativo chico (solo finitos primos — o ninguno — en el lado
aritmético), la positividad del funcional de Weil está probada incondicionalmente en el
marco semilocal (Doc 100; Connes–Consani 2021–22 [detalles bibliográficos NO VERIFICADOS;
el contenido citado es el del Doc 100]). ¿Puede un cuádruplo violarla? No: por MW-7
(P43 §3.2; Doc 100), para que el término negativo del cuádruplo supere el mar arquimediano
positivo, ĥ debe resolver la frecuencia γ₀ y la abscisa δ: soporte a ≳ log γ₀ (Doc 108,
Teorema 3.3: ceguera sub-resolución). Los soportes donde la positividad está probada son
O(1); los γ₀ con log γ₀ = O(1) están numéricamente excluidos (ítem (c)). **Los regímenes
probados no intersecan jamás el régimen de visibilidad: ninguna elección de (δ, γ₀)
produce contradicción.**

(b) **Positividad de Li parcial.** λ_n ≥ 0 ∀n ⟺ RH (Li 1997; Bombieri–Lagarias 1999: es
positividad de Weil en la familia de tests (1−(1−1/s)ⁿ)). Un cuádruplo con cero ρ
(Re ρ > ½) hace |1−1/ρ| > 1 y por tanto λ_n → −∞ exponencialmente sobre una subsucesión,
con primer índice negativo n* ≍ (γ₀²/δ)·log(γ₀²/δ) (el término del cuádruplo crece como
r^n, r−1 ≍ δ/γ₀², contra el término principal ∼ (n/2)log n; cálculo de orden, las
constantes no son load-bearing). La positividad λ_n ≥ 0 está verificada computacionalmente
para n hasta cierto rango finito [rango exacto NO VERIFICADO; literatura: cómputos de
Maślanka y otros]; eso excluye la región compacta {γ₀²/δ ≲ n*/log} — estrictamente más
débil que la verificación directa de RH en altura, que excluye γ₀ ≤ 3·10¹² para TODO δ.
**Li parcial no agrega región.**

(c) **Verificación numérica publicada (cota de altura).** Platt–Trudgian, *The Riemann
hypothesis is true up to 3·10¹²*, Bull. London Math. Soc. 53 (2021), 792–797: todo cero
con 0 < γ ≤ 3·10¹² tiene β = ½. Excluye γ₀ ≤ 3·10¹².

(d) **Regiones libres clásicas.** de la Vallée Poussin: β < 1 − c/log|γ|;
Korobov–Vinogradov (§2.3): excluye δ > ½ − c/((log γ₀)^{2/3}(log log γ₀)^{1/3}).

**Región excluida hoy, exacta:**
$$\mathcal{R}_{\mathrm{exc}} = \{\gamma_0 \le 3\cdot10^{12}\} \;\cup\;
\Bigl\{\delta > \tfrac12 - \frac{c}{(\log\gamma_0)^{2/3}(\log\log\gamma_0)^{1/3}}\Bigr\}.$$
Es una franja delgada pegada al borde δ = ½ más una caja de altura finita. Todo el
rectángulo {δ ∈ (0, ½−ε), γ₀ > 3·10¹²} está permitido por todo lo probado, **con cualquier
multiplicidad m, incluida m = 1 y m = ∞**. La cota L8 (m ≤ C) sería ortogonal a
𝓡_exc: no excluye región, acota el **cardinal** — un tipo de enunciado del que el
inventario no contiene ningún ejemplar (§2.6).

### 2.5. ¿Existe el teorema "m ≥ 1 ⟹ m = ∞"?

Búsqueda hecha (literatura clásica + revisión actual): **no existe** tal teorema en la
literatura arbitrada. Lo que circula con esa forma son preprints no aceptados que lo usan
como paso hacia "disproofs" de RH (no citables; el hecho relevante y verificable es la
ausencia del teorema en las referencias estándar [T86], [IK04] y en los surveys de la
zona). Tampoco existe el recíproco ("existe configuración con m finito realizable por una
función de la clase de Selberg"): ambas direcciones están abiertas, y el Corolario 2.3
muestra que cualquier prueba de la primera necesita el producto de Euler de manera
esencial. Estado honesto: **"m ≥ 1 ⟹ m = ∞" no es un teorema, no es refutable con lo
conocido, y no hay ataque conocido**. Para la lógica de las salidas (§1.3): la salida (B)
no puede certificarse hoy en ninguna de sus dos formas (ni el colapso finito = 0, ni la
equivalencia m-finito ⟺ RH).

### 2.6. Conclusión del inventario: binariedad global

**Observación 2.6 (el inventario es binario).** Recorrida la lista completa
(§2.3, §2.4), todo enunciado incondicional conocido que acote ceros off-críticos cae en
exactamente una de dos formas:

| forma | ejemplos | conteo que produce |
|---|---|---|
| región libre | VP, VK, verificación de altura | **0** en la región |
| densidad / valores grandes | Bohr–Landau, Carlson…Huxley, log-free | **≪ T^θ, θ > 0** |

No existe ningún teorema de la tercera forma — "conteo finito no nulo uniforme en T" — en
ninguna región del espacio de parámetros. Esta es la misma binariedad que el Doc 108
(Prop. 2.5) encontró en el índice test-accesible (0 bajo RH, ≍ m log T bajo ¬RH), ahora
verificada a nivel de TODO el inventario clásico. El §5.4 explicará la razón estructural
(la forma de los presupuestos de momentos) y el §6 la elevará a dicotomía.

---

## 3. (ii) El análogo Siegel: anatomía, transporte y fracaso

### 3.1. Anatomía del mecanismo de Siegel

El único precedente analítico de "a lo sumo UNA excepción" es la teoría del cero
excepcional (Landau 1918; Page 1935; Siegel 1935; Deuring 1933 / Heilbronn 1934; Linnik
1944). Conviene desarmarlo en sus piezas load-bearing:

(S1) **Localización real.** El cero excepcional β₁ de L(s,χ) (χ real primitivo mod q) es
REAL y está pegado a s = 1: β₁ > 1 − c/log q. Toda la maquinaria vive en el segmento real
[1−c/log q, 1], dentro del alcance perturbativo de la región de convergencia absoluta.

(S2) **Positividad termwise de un producto auxiliar.** Para dos caracteres reales
primitivos distintos χ₁ mod q₁, χ₂ mod q₂:
$$F(s) := \zeta(s)\,L(s,\chi_1)\,L(s,\chi_2)\,L(s,\chi_1\chi_2)$$
tiene coeficientes de Dirichlet **no negativos** (es, para χᵢ cuadráticos, la ζ de Dedekind
de un cuerpo bicuadrático, o en general: log F tiene coeficientes ≥ 0 porque
(1+χ₁(p^k))(1+χ₂(p^k)) ≥ 0).

(S3) **Presupuesto = polo simple.** F tiene en s = 1 un polo SIMPLE (solo ζ lo aporta).
El lema de Landau sobre series con coeficientes positivos da: si β₁ y β₂ son ceros reales
de L(s,χ₁), L(s,χ₂) respectivamente, entonces F(σ) tendría, para σ real → 1⁺, una
estructura de signos imposible salvo que min(β₁,β₂) < 1 − c/log(q₁q₂). **Dos ceros no
pueden comerse un polo de orden 1**: la repulsión es la escasez de un presupuesto global
de tamaño exactamente 1.

(S4) **Amplificación (Deuring–Heilbronn / Linnik).** El cero excepcional, si existe,
repele a todos los demás ceros de la familia mod q, con constante que explota cuando
β₁ → 1. Insumo: densidad log-free (Linnik) + (S2)–(S3).

### 3.2. Transporte a ζ, primer intento: la zona de Siegel de ζ ya está cerrada

¿Qué sería un "cero de Siegel de ζ" en el aspecto s? Un cero β+iγ con β → 1. La pieza
(S2)–(S3) para ζ misma existe y es **clásica**: la desigualdad 3+4cos θ+cos 2θ ≥ 0
aplicada a −Re(ζ′/ζ)(σ) −Re(ζ′/ζ)(σ+iγ)-combinaciones es exactamente "el polo de ζ³ϕ⁴ψ
repele al cero": su salida es la región libre de de la Vallée Poussin, y con las sumas de
Vinogradov la de Korobov–Vinogradov. Es decir: **el análogo del mecanismo de Siegel para
ζ misma ya está ejecutado, y su producto íntegro es la región libre clásica** — la franja
de §2.4(d). El mecanismo no produce conteos: produce la región donde el presupuesto del
polo alcanza, y esa región tiene profundidad O(1/log γ) (mejorada a (log γ)^{−2/3}…), nunca
profundidad fija ε > 0. La razón: el control termwise de −ζ′/ζ(σ+it) — la fuente de toda
la positividad (S2) — muere en la abscisa de convergencia absoluta σ = 1; su alcance al
interior de la franja es el alcance perturbativo O(1/log) del polo. **Los cuádruplos
supervivientes (δ < ½ − c/(log γ₀)^{2/3}…) viven, por definición de la región excluida,
exactamente donde el mecanismo de Siegel no tiene ninguna palanca.**

### 3.3. Transporte, segundo intento: ¿dos cuádruplos se repelen vía la fórmula explícita?

Tomamos ¬RH con dos cuádruplos {δ₁,γ₁}, {δ₂,γ₂} (heredando el marco del juguete, Doc 98
T1 extendido a m = 2) y buscamos el análogo de (S2)–(S3): una función de prueba cuya
positividad PARCIAL probada se viole con ambos presentes pero no con uno.

**(a) En el funcional de Weil lineal (una variable).** El término de los ceros es
Σ_ρ ĥ(ρ); los dos cuádruplos aportan Σ_{j=1,2} Σ_{cuád_j} ĥ(ρ). No hay término cruzado:
el funcional es LINEAL en los ceros — la estructura producto de (S2) (cuatro L-funciones
multiplicadas ⟹ los dos ceros entran en el MISMO objeto positivo) no tiene análogo, porque
solo hay una ζ: el "producto" ζ·ζ es ζ², que no agrega información (sus ceros son los
mismos con multiplicidad doble; en (S2) la información nueva la trae χ₁χ₂, un carácter
TERCERO — para ζ sola no existe el tercero). Para que dos cuádruplos interactúen hace
falta un funcional **cuadrático** en los ceros: exactamente la forma Q₂ del Doc 107/108.

**(b) En la forma cuadrática Q₂.** Los pares mixtos (ρ ∈ cuád₁, ρ′ ∈ cuád₂) existen y
contribuyen. Su estructura espectral: la involución (ρ₁,ρ₂) ↦ (1−ρ̄₁,1−ρ̄₂) actúa
libremente sobre esos pares (ninguno es punto fijo: ambas ranuras son off), luego forman
**planos hiperbólicos** — signatura (k,k), aporte NETO nulo a la definitud y aporte
ADITIVO al índice negativo. Cálculo de conteo (mismo aparato que Doc 107 Teorema 5.5,
Doc 108 Prop. 2.3): con m = 2, el bloque off×off tiene (4·2)²/2 = 32 planos; los
16² = 64 pares incluyen los 2·(16·... ) pares cruzados, todos en órbitas libres. **El
índice crece con m (κ(Q₂^rel) = 8m²); jamás decrece.** No hay en la forma cuadrática
ningún término donde la presencia del segundo cuádruplo DIFICULTE la del primero: la
estructura es de suma directa perturbada, no de competencia por un presupuesto. La
competencia exigiría que ambos cuádruplos carguen contra un mismo término positivo
ACOTADO; pero el término positivo local (el mar on×on de la ventana, ≍ n_W² con
n_W ≍ log T) **crece** con la altura: presupuesto ilimitado, escasez nula, repulsión nula.
Contraste exacto con (S3): allí el presupuesto era el orden del polo, = 1, fijo.

**(c) El término cruzado en el lado de primos.** Con la fórmula explícita sobre un
polinomio de Dirichlet suavizado P_w(t) = Σ_n Λ(n)w(n/X)n^{−½−it} (desarrollo estándar:
P_w(t) = Σ_ρ X^{ρ−½}·ŵ-localización en |t−γ(ρ)| ≲ 1, más polo y términos menores;
[IK04] Thm. 5.12 + Mellin), la contribución de los cuádruplos a ∫|P_w|²dt es
$$\underbrace{m_1\,X^{2\delta_1} + m_2\,X^{2\delta_2}}_{\text{diagonal}}
\;+\; \underbrace{O\bigl(X^{\delta_1+\delta_2}\bigr)\cdot \mathbf{1}_{|\gamma_1-\gamma_2|\lesssim 1}}_{\text{cruzado}},$$
el cruzado solo si las alturas se solapan a la resolución del test. Tamaños: δ₁+δ₂ <
½+½ = 1 SIEMPRE (los ceros están en la franja), luego **el término cruzado, igual que los
diagonales (2δᵢ < 1), queda estrictamente por debajo de la barra de error incondicional
O(X log²X) del teorema de valor medio de Montgomery–Vaughan** (la cuenta completa en
§5.3). El cruce no cambia la accesibilidad: vive en la misma escala invisible. Y en el
detector cuadrático localizado, ver el término cruzado exige que ĥ resuelva
SIMULTÁNEAMENTE las dos frecuencias desconocidas γ₁, γ₂ y las dos abscisas δ₁, δ₂: el
costo de resolución es el máximo de los costos, la señal es el producto de dos factores
chicos. **Detectar la pareja es más difícil que detectar un cuádruplo**, no más fácil.

### 3.4. Veredicto del frente Siegel: anti-repulsión

**Proposición 3.1 (no hay análogo de Siegel; resumen demostrado).**
(a) La pieza (S2) (producto auxiliar con coeficientes positivos que contiene a ambos
ceros) no tiene análogo para dos cuádruplos de ζ: requiere un tercer objeto (χ₁χ₂) que
no existe en una familia de un solo elemento. (b) La pieza (S3) (presupuesto O(1)) no
tiene análogo en el interior de la franja: el presupuesto local de positividad a altura
γ es ≍ log γ y crece. (c) El único transporte válido del mecanismo (positividad termwise
+ polo) es la región libre clásica, ya cobrada (§3.2). (d) En los funcionales cuadráticos
del programa, dos cuádruplos se suman (κ = 4, planos hiperbólicos adicionales), y su
término cruzado de primos es de tamaño X^{δ₁+δ₂} < X, bajo la barra de error de los
valores medios incondicionales. **No existe, con la tecnología catalogada, ningún teorema
de la forma "m ≥ 2 es más difícil que m = 1": las direcciones detectables apuntan al
revés (la pareja se detecta peor que el solitario).**

*Demostración.* (a)–(d) = §3.1–§3.3. ∎

Lectura física: la repulsión de Siegel es un fenómeno de **borde de convergencia
absoluta** (escasez de positividad junto al polo). Los cuádruplos de ζ viven en el
interior profundo de la franja, donde la positividad disponible es oceánica y nada
escasea: sin escasez no hay repulsión. La frontera entre ambas fenomenologías es la
región libre clásica.

---

## 4. (iii) Turán power sums: medición

### 4.1. Lo que la maquinaria da

El segundo teorema principal de Turán (forma estándar; P. Turán, *On a New Method of
Analysis and its Applications*, Wiley 1984; también Halász–Turán 1969 para el uso en
densidad): para z₁,…,z_n ∈ ℂ con |z₁| ≥ … ≥ |z_n| y coeficientes b_j,
$$\max_{\nu = M+1,\dots,M+n} \Bigl|\sum_j b_j z_j^\nu\Bigr| \;\ge\;
\Bigl(\frac{n}{8e(M+n)}\Bigr)^{n}\,\Bigl|\sum_{j} b_j\Bigr|\,|z_n|^{M+n}\!,$$
(variantes con mín-condiciones sobre subconjuntos; lo load-bearing es la **degradación
exponencial en n**, el número de términos seguidos). Aplicación al problema: bajo ¬RH con
m cuádruplos de parámetros (δⱼ, γⱼ), δ_min := min δⱼ, la fórmula explícita da
ψ(x) − x = −Σ_off x^{ρ}/ρ + O(x^{½}log²x), y las sumas de potencias sobre los 4m términos
off (z_j = e^{(½+δ_j±iγ_j)u} en la variable u = log x) fuerzan, en toda progresión
u ∈ [U, U(1+1/m-escala)], la existencia de x con
$$|\psi(x) - x| \;\gg_{m,\,\delta_{\min},\,\gamma_{\max}}\; x^{\frac12+\delta_{\min}-\varepsilon}.$$
Esto es un teorema de **detección**: m cuádruplos garantizan oscilación localizable en
todas las escalas, con constantes explícitas en (m, δ_min, γ_max) que se degradan
exponencialmente en m (n = 4m términos en el teorema de Turán; si además hay que separar
los off de los on-line vecinos, n crece a ≍ log γ_max y la constante a una pérdida
polinomial en γ_max — el mismo fenómeno que hace polinomiales los teoremas de densidad
producidos por el método, §2.3 Halász–Turán). Nótese el sentido de la degradación: **más
cuádruplos ⟹ peor cota garantizada** (pueden conspirar a cancelarse durante más tiempo).
El método de Turán es estructuralmente anti-repulsivo: cuantifica cuánto pueden
esconderse, no cuánto se estorban.

### 4.2. La circularidad de la cota superior (donde muere la finitud)

Para convertir la detección en contradicción — y de ahí "m ≤ f(δ_min, γ_max)" — hace
falta una cota superior incondicional que la oscilación garantizada viole:
$$|\psi(x) - x| \;\le\; B(x) \quad\text{con}\quad B(x) = o\bigl(x^{\frac12+\delta_{\min}}\bigr)
\ \text{en el rango de x donde Turán garantiza el mínimo.}$$
Inventario de cotas superiores incondicionales: la mejor es
ψ(x) − x ≪ x·exp(−c(log x)^{3/5−ε}) (Vinogradov–Korobov; [IK04] Cor. 8.30) — de tamaño
x^{1−o(1)}, **enormemente por encima** de x^{½+δ} para todo δ < ½. Y no es mala suerte:
por el teorema recíproco clásico (Landau; en la forma usada por Ingham [In40] y
expuesta en [T86] §Cap. III: ψ(x) − x ≪ x^θ implica que ζ no tiene ceros con β > θ, vía
la representación de Mellin de ζ′/ζ), **cualquier** cota superior ψ(x)−x = O(x^{½+δ_min−ε})
implica que no hay ceros con β > ½+δ_min−ε: es decir, la cota superior que el argumento de
Turán necesita como insumo ES la conclusión cuasi-RH que se pretendía obtener.
**Circularidad exacta, sin holgura:** el método no puede producir ni "m ≤ f(δ_min, γ_max)"
ni ninguna finitud, porque su mitad superior es idéntica al teorema buscado.

### 4.3. Lo que sí queda: finitud en cajas compactas (y por qué no es la diana)

**Observación 4.1.** En cualquier caja compacta {δ ≥ δ₀, γ₀ ≤ Γ}, la finitud es trivial
e incondicional: m(δ₀, Γ) ≤ N(½+δ₀, Γ) ≪ Γ^{12(½−δ₀)/5+ε} (Huxley) — finito, explícito,
polinomial en Γ. Esto no usa Turán (aunque Halász–Turán mejora el exponente cerca de
δ₀ → ½). La diana L8 es exactamente el límite Γ → ∞ con cota independiente de Γ: **toda
la no-trivialidad de L8 es la uniformidad en la altura**, el mismo cuantificador de
siempre (P41: interior controlado / frontera = el enunciado). La "finitud en regiones
compactas del espacio de parámetros" que el encargo preguntaba ya existe y es barata; no
es un peldaño hacia L8 porque la dependencia en Γ es polinomial creciente y ninguna
amplificación conocida la aplana (Doc 108, Prop. 7.3: la frontera es k-invariante).

---

## 5. (iv) La cuenta central: ventanas excepcionales vs. momentos incondicionales

Esta sección ejecuta la cuenta pedida: ¿cuántas ventanas con déficit tolera la asintótica
en media incondicional? La respuesta requiere primero decidir QUÉ estadística por ventana
ve un cuádruplo.

### 5.1. Las estadísticas con teorema límite incondicional son ciegas

**Lema 5.1 (ceguera de S(t) y del CLT de Selberg).** Sean dos configuraciones de ceros:
(I) un cuádruplo {½±δ±iγ₀} (más ceros on-line Z); (II) dos ceros dobles on-line en
½±iγ₀ (más los mismos Z). Entonces las funciones de conteo N(t) de (I) y (II) son
idénticas, y S(t) = π⁻¹arg ζ(½+it) difiere entre ambas configuraciones solo en
|t−γ₀| ≲ δ, con diferencia O(1).

*Demostración.* N(t) cuenta ceros en el rectángulo 0 < β < 1, 0 < γ ≤ t (argumento
principal sobre el contorno): la abscisa β no entra en el conteo; (I) y (II) tienen los
mismos γ con las mismas multiplicidades totales (el cuádruplo aporta 2 en altura γ₀ y 2 en
−γ₀; los dos ceros dobles también). S(t) = N(t) − (término suave) + O(1) y la variación
fina de arg ζ entre ambas configuraciones proviene del factor
(s−ρ)(s−(1−ρ̄)) vs (s−½−iγ₀)², cuyos argumentos sobre la recta difieren en O(1) y
coinciden fuera de |t−γ₀| ≲ δ (los factores son iguales a primer orden lejos del cero). ∎

**Consecuencia 5.2.** El CLT incondicional de Selberg (momentos de S(t):
∫₀^T S(t)^{2k}dt = c_k T(log log T)^k(1+o(1)), Selberg 1946; exposición [T86] y Tsang)
**no restringe m en absoluto**: las dos configuraciones del Lema 5.1 tienen estadísticas S
idénticas salvo en m ventanas de tamaño O(1) con perturbación O(1), y la configuración
(II) es RH-compatible. Una concentración gaussiana con varianza log log T tolera, por
Chebyshev, hasta ≍ T/(log log T)^k ventanas con desviación O(1) — astronómicamente más que
cualquier m; pero el punto fuerte es previo a la tolerancia: **la estadística no distingue
los mundos ni con tolerancia cero**, porque la abscisa no entra en S. La respuesta al
encargo ("¿una concentración así limita cuántas ventanas pueden tener déficit ≍ 1?") es:
limita las ventanas con déficit de S, y el déficit de off-criticidad **no es un déficit de
S**. Ídem log|ζ(½+it)|: la diferencia entre (I) y (II) es un factor acotado lejos de γ₀ y
una singularidad logarítmica suavizada (log δ en vez de −∞) en una ventana O(1):
perturbación O(polylog) contra momentos ≍ T(log log T)^k — invisible y de signo ambiguo.

**El catálogo de "qué ve qué", consolidado:** la abscisa δ la ven solo los funcionales de
**segundo orden** (correlación de pares / déficit casi-primo ΔK, Doc 108 Def. 3.6; los
índices κ_W). Toda estadística de primer orden con teorema límite incondicional (N, S,
log|ζ| en media) es ciega por construcción: la información de abscisa está en la posición
de los ceros relativa a la involución s ↦ 1−s̄, y el primer orden solo lee alturas.

### 5.2. La cuenta del déficit por ventana, hecha con cuidado

Heredamos del Doc 108 (Prop. 2.3, Teorema 3.4) la estructura exacta del déficit visible:

- Ventanas de la variable suma a altura T, ancho Δ: bajo ¬RH con m cuádruplos (alturas
  ≤ γ_max fijas), **toda** ventana alta tiene índice κ_W ≍ 2m·n_W (contaminación off×on),
  con n_W ≍ (2Δ/π)log T. El déficit realizable del funcional por familia de tests
  normalizada: señal ≍ m·n_W contra masa arquimediana ≍ n_W²: **déficit relativo
  ≍ m/log T por ventana, en TODAS las ventanas** (no solo en m de ellas — este es el punto
  que el pigeonhole ingenuo del encargo subestima a favor: la señal está en todas partes).
- En la lectura de una variable (funcional de Weil por ventana de altura t, ancho Δ): los
  términos espectrales del cuádruplo viven solo en |t−γⱼ| ≲ Δ: m ventanas excepcionales
  con déficit local ≍ 1 unidad de cero (relativo 1/n_W ≍ 1/log T del total de la ventana).

En ambas lecturas el déficit acumulado en el promedio sobre M ventanas hasta altura T₀ es
**relativo ≍ m/log T₀** (en la primera lectura porque cada ventana lo porta; en la
segunda porque m ventanas de déficit 1/log T₀ se diluyen en M ventanas: m/(M log T₀),
aún menor). La pregunta cuantitativa: ¿qué precisión relativa tienen los valores medios
incondicionales que promedian ese funcional?

### 5.3. Montgomery–Vaughan: la barra de error absorbe todo δ < ½, y el porqué exacto

**Proposición 5.3 (la invisibilidad media, cuantificada).** Sea
P_w(t) = Σ_n Λ(n)w(n/X)n^{−½−it} con w suave de soporte compacto. Entonces:

(a) [MV74] ∫₀^{T₀}|P_w(t)|²dt = (T₀ + O(X))·Σ_n Λ(n)²w(n/X)²/n = (T₀ + O(X))·(½+o(1))(log X)²·c_w.

(b) Por la fórmula explícita ([IK04] Thm. 5.12, vía Mellin con ŵ de decaimiento rápido),
cada cero ρ = β+iγ contribuye a P_w(t) un término de amplitud ≍ X^{β−½} localizado en
|t−γ| ≲ 1; la contribución total de m cuádruplos (alturas ≤ T₀) a ∫₀^{T₀}|P_w|²dt es
$$\Delta_{\mathrm{off}} \;\asymp\; \sum_{j\le m} X^{2\delta_j}
\;+\; O\Bigl(\sum_{|\gamma_i-\gamma_j|\lesssim 1} X^{\delta_i+\delta_j}\Bigr).$$

(c) Como δⱼ < ½ y δᵢ+δⱼ < 1, se tiene Δ_off = o(X·(número de términos)) y por tanto
Δ_off queda dentro del término de error O(X log²X) de (a) para todo m ≤ X^{1−2δ_max−ε} —
en particular **para todo m fijo, para m = m(T₀) → ∞ de densidad cero, y aún para m
polinomial en X de exponente < 1−2δ_max**. El valor medio de Montgomery–Vaughan es
lógicamente compatible con todos esos mundos a la vez.

*Demostración.* (a) es el teorema de valor medio de Montgomery–Vaughan [MV74] aplicado a
a_n = Λ(n)w(n/X)n^{−½}, con Σ|a_n|² ≍ (log X)²·c_w por sumación parcial con PNT. (b) es
el desarrollo estándar: P_w(t) = (1/2πi)∫(−ζ′/ζ)(½+it+u)X^u ŵ(u)du desplazando el
contorno: residuos en los ceros (término X^{ρ−½−it}ŵ(ρ−½−it), con |ŵ| de decaimiento
rápido ⟹ localización en |t−γ| ≲ 1) y en el polo. La integral del cuadrado del término
del cero j sobre su ventana de localización es ≍ X^{2δ_j}; los productos cruzados entre
ceros a distancia > 1 decaen rápido (decaimiento de ŵ), los cercanos dan el término
indicado. (c) aritmética de exponentes: X^{2δ} ≤ X^{1−2ε′} si δ ≤ ½−ε′; comparar con
O(X log²X). ∎

**Lectura.** La barrera tiene una forma llamativamente limpia: **la franja crítica entera
(δ < ½) está fabricada para caber dentro del término de error diagonal O(X) de la gran
criba.** El error O(X) de MV74 es esencialmente óptimo (es el costo de los no-diagonales
n = n′ ± pequeños); mejorar la barra a o(X^{2δ}) para todo δ > 0 — lo necesario para que
el promedio VEA un cuádruplo — es mejorar O(X) a O(X^ε), es decir suprimir el rango
off-diagonal por completo, que es la asintótica "en toda ventana" otra vez (la Conjetura
108-N en versión de valor medio). El muro del Doc 108 reaparece en la cuenta de exponentes
más elemental posible.

### 5.4. Valores grandes y momentos altos: la tolerancia nunca baja de T^θ

Segunda mitad de la cuenta pedida: en lugar del promedio, contar directamente las ventanas
donde |P_w| es grande (las que un cuádruplo de abscisa δ produce con |P_w| ≍ V = X^δ).
El inventario de cotas de valores grandes incondicionales (MV large values, Huxley,
Jutila; [IK04] Cap. 9–10):
$$R(V) \;\ll\; \frac{G\,X}{V^2}\,(\log)^{O(1)} \;+\; \frac{G^3\,T_0\,X}{V^6}\,(\log)^{O(1)},
\qquad G := \textstyle\sum|a_n|^2 \asymp (\log X)^2,$$
y refinamientos de Halász–Montgomery con el mismo carácter. Con V = X^δ:
R ≪ X^{1−2δ+ε} + T₀X^{1−6δ+ε}: **polinomial en (X, T₀), jamás O(1)**. Esto no es un
defecto mejorable: las cotas de valores grandes con momentos 2k dan
R ≪ T₀^{c_k}·X^{k(1−2δ)+ε}-tipo; para matar la dependencia polinomial habría que tomar
k ≍ log T₀ con constantes uniformes en k — y un control de TODOS los momentos con
constantes uniformes es equivalente al control del supremo: la inversión
media → uniforme del cuantificador maestro (P43, Principio 3.1), en su presentación de
momentos. De hecho la dualidad es exacta en las dos direcciones: **los teoremas de
densidad de ceros SON las cotas de valores grandes** (así se prueban Ingham, Huxley,
Montgomery), de modo que "cuántas ventanas excepcionales toleran los segundos momentos"
ya tiene nombre en la literatura: N(σ,T) ≪ T^{θ(σ)} — la columna derecha de la tabla de
§2.6. La pregunta del encargo queda respondida con su forma cerrada:

**Respuesta cuantitativa (iv).** Las varianzas y momentos incondicionales (MV74, momentos
de S(T), CLT de Selberg, momentos 2k de polinomios de Dirichlet) toleran
$$R_{\mathrm{tolerado}}(\delta, T) \;\asymp\; T^{\theta_k(\delta)} \quad\text{con } \theta_k(\delta) > 0
\ \ \forall k < \infty,\ \forall \delta < \tfrac12,$$
ventanas excepcionales; los m cuádruplos producen ≍ m (lectura lineal) o "todas con
déficit m/log T" (lectura cuadrática). Como m ≪ T^θ para todo m fijo e incluso para
m = ∞ con densidad cero (la única restricción real: m(T) ≤ N(½+δ, T) ≪ T^θ — ¡que es el
teorema de densidad mismo!), **el promedio tolera m infinito de densidad cero: ahí está
el muro de nuevo**, ahora con su forma cuantitativa exacta: la brecha entre la tolerancia
T^θ y la meta O(1) no se estrecha con ningún momento de orden finito, y cerrarla con
k → ∞ uniforme es el cuantificador.

### 5.5. El pigeonhole y la circularidad de bootstrapping, resueltos en contra

El argumento esperanzador era: "para m ≤ C solo se necesita uniformidad en las ventanas
que contienen los γⱼ — finitas si m finito; y si m ≥ M, hay M ventanas disjuntas con
déficit simultáneo que quizá violen una cota promedio". Tres fallas demostrables:

1. **La localización es ilusoria en la lectura cuadrática:** bajo ¬RH el déficit
   κ_W ≍ m·n_W está en TODAS las ventanas altas (Doc 108, Prop. 2.3: contaminación
   off×on), de modo que "solo las ventanas de los γⱼ" describe la lectura lineal — y en
   la lectura lineal el déficit por ventana es de primer orden en una estadística ciega
   (Lema 5.1) o de segundo orden en una estadística sin teorema de media a esa precisión.
2. **El déficit acumulado M/log T no viola ninguna media accesible:** por la Prop. 5.3,
   la media accesible tiene barra de error relativa O(X/T₀) ≥ O(1) en el régimen de
   resolución (X ≥ T₀) y absorbe X^{2δ} en el régimen sub-resolución: en ningún régimen
   la barra baja a o(M/log T) para M fijo. No hay desigualdad que el pigeonhole pueda
   activar.
3. **La circularidad no se rompe sino que se re-encodea:** el pigeonhole convierte
   "m ≥ M" en "M eventos individuales de medida cero simultáneos"; pero M eventos de
   medida cero siguen siendo un evento de medida cero, y el Principio 3.1 de P43 aplica
   sin modificación: la genericidad no detecta eventos de medida nula, sean uno o M. La
   única manera de que M eventos sean detectables donde uno no lo es sería un término de
   interacción supra-aditivo (repulsión) — exactamente lo que §3 demostró que no existe
   (la interacción es aditiva en κ y sub-barra-de-error en primos).

---

## 6. (v) Síntesis: la dicotomía presupuesto/costo y la decisión entre salidas

### 6.1. Salida (B): descartada como certificable, con su mitad útil registrada

No existe teorema "m ≥ 1 ⟹ m = ∞" (§2.5) ni puede producirse sin insumo aritmético
esencial (Cor. 2.3); tampoco hay prueba de "m finito ⟺ RH". Por tanto la diana L8 **no
colapsa**: sigue siendo lógicamente estrictamente más débil que RH. Esta es la mitad
buena del documento: L8 queda viva como enunciado. La mitad mala es metodológica y la
decide §6.2.

### 6.2. La dicotomía presupuesto/costo

**Definición 6.1.** Un **certificado de finitud** es un funcional B, computable desde el
lado aritmético (test-accesible en el sentido del Doc 108, Def. 1.2), con:
(P1) **presupuesto**: un teorema incondicional B ≤ C_B < ∞;
(P2) **costo mínimo**: un teorema incondicional "cada cuádruplo aporta ≥ c > 0 a B", con
c uniforme en (δ, γ₀) sobre la región no excluida.
Entonces m ≤ C_B/c. Toda ruta a L8 es un certificado de finitud (la ruta κ_W ≤ C·n_W es
el caso B = sup_W κ_W/n_W, c = 2).

**Proposición 6.2 (el inventario se parte; ningún candidato cumple (P1)+(P2)).**
Sobre los funcionales catalogados por el programa y la literatura:

(a) *Funcionales con (P1) sin (P2):* T_λ = ∫W_λ dν cumple (P1) en la forma relevante
(es finito y su valor es computable/acotable en mundos fijos), pero su costo por cuádruplo
es 2δ²K_λ(γ₀) (Doc 98, Cor. 2.4; Doc 86 §6), que **tiende a 0** cuando δ → 0 o γ₀ → ∞
(K_λ decae con la medida dm_∞ ≍ e^{−πγ₀/2}): cuádruplos arbitrariamente baratos, ninguna
cota de m. Lo mismo le pasa a todo funcional de traza/medida fija (los ocho equivalentes
del Doc 89): la positividad d ν ≥ 0 da presupuesto, pero el costo se desvanece en las
colas del espacio de parámetros.

(b) *Funcionales con (P2) sin (P1):* κ_W/n_W tiene costo uniforme c = 2 por cuádruplo
(Doc 108, Prop. 2.3 — el costo NO decae con γ₀ ni con δ: por eso es el candidato L8),
pero su acotación uniforme sobre ventanas es **RH-equivalente ya en su versión o(n_W)**
(Doc 108, Prop. 2.5 y Teorema 4.3) y su versión a constante C·n_W exige la misma
precisión de segundo orden o(C/log T) uniforme (Doc 108, §8.1): (P1) es exactamente el
enunciado detrás del muro. Igual para todo índice/supremo sobre ventanas o frecuencias.

(c) *No hay tercera clase:* un funcional con costo uniforme debe detectar un cuádruplo a
altura γ₀ arbitraria con respuesta ≥ c; por la ceguera sub-resolución (Doc 108, Teorema
3.3) la detección exige tests de resolución a ≳ log γ₀, luego B es (al menos) un supremo
sobre la frecuencia/altura de funcionales de ventana; y su acotación incondicional es una
cota uniforme-en-ventanas de un funcional cuya versión en media es teorema y cuya versión
uniforme separa los dos mundos al segundo orden — el Teorema 3.4 del Doc 108 (dos mundos)
aplica mutatis mutandis: (P1) para un B de clase (P2) implica evaluar Π con precisión
relativa O(c/log T) uniforme en T. Esto no se afirma como teorema general sobre "todo
funcional concebible" (no hay tal clasificación); se afirma, con demostración, sobre la
clase test-accesible del programa, que es donde viven todos los candidatos conocidos.
GAP declarado: la dicotomía es exhaustiva sobre el inventario, no sobre el espacio de
todos los funcionales matemáticamente posibles.

*Demostración.* (a): Doc 98 Cor. 2.4 más el decaimiento de K_λ (Doc 95, Lema 2.2:
dm_∞ ≍ |s|^{−1/2}e^{−π|s|/2}ds). (b): las citas indicadas del Doc 108. (c): cadena de
ceguera sub-resolución + dos mundos, como se indica. ∎

### 6.3. Los dos precedentes de "a lo sumo k excepciones" confirman la dicotomía

- **Siegel:** B = orden del polo de F(s) en s = 1 (= 1); costo: cada cero excepcional
  consume ≥ c del polo por positividad termwise (S2)–(S3). **(P1) trivial (¡el
  presupuesto es un entero visible!), (P2) probado cerca de s = 1.** Resultado: a lo sumo
  1 excepción. El mecanismo vive donde vive porque solo ahí hay (P2).
- **Weil (cuerpos de funciones):** B = dim H¹(C̄, ℚ_ℓ) = 2g; costo: cada cero es un
  autovalor de Frobenius en H¹, costo 1. **(P1) es la finito-dimensionalidad de la
  cohomología — un teorema previo e independiente de la pureza**; la "RH" (pureza) viene
  después, por positividad de Castelnuovo. Obsérvese el orden lógico: en el único mundo
  donde el análogo de RH se probó, el análogo de L8 ("a lo sumo 2g ceros en total, en
  particular finitas excepciones posibles") fue **gratis y anterior**, regalado por la
  estructura finito-dimensional.

**Observación 6.3 (L8 es el avatar contable de la finito-dimensionalidad).** La diana L8
pide exactamente lo que la cohomología regala: un receptáculo de dimensión finita acotada
a priori donde las excepciones deban vivir. El análisis dispone del receptáculo correcto —
𝒦_off ⊂ (𝒦, Q), de dimensión 4m (P35, Doc 96/98) — pero su dimensión es función del
desconocido m: el receptáculo **mide** las excepciones, no las acota; convertir "dim = 4m"
en "dim ≤ D" requiere el presupuesto (P1) que la Prop. 6.2(b) sitúa detrás del muro. Esto
afina P43 §6 (el mecanismo faltante debe leer inercia, no valor): el primer dividendo de
un invariante cohomológico genuino sobre Spec ℤ no sería RH sino L8 — y recíprocamente,
**una prueba analítica de L8 equivaldría a fabricar dimensión finita a partir de
promedios**: la inversión del cuantificador maestro en su forma más desnuda.

### 6.4. Decisión

- **(A) — descartada con la localización del lema.** El único lema con la forma correcta
  es el del Doc 108 §8.1 (κ_W ≤ C·n_W uniforme), u, equivalentemente por la Prop. 6.2(c),
  cualquier par (P1)+(P2): su insumo es la evaluación del déficit casi-primo al segundo
  orden, con error relativo O(C/log T), uniforme en la frecuencia — la escala de los
  términos de orden inferior de correlación de pares, conjeturales incluso bajo RH
  (Doc 108, §5.3 y §6.2). No hay camino con técnica actual.
- **(B) — descartada como certificable** (§6.1): ni colapso ni equivalencia demostrables;
  L8 permanece estrictamente más débil que RH. (Registrar esto es en sí un resultado del
  documento: la diana no es RH disfrazada.)
- **(C) — es la que ocurre.** Con localización exacta y triple: (i) la interacción entre
  cuádruplos es aditiva/sub-error, no repulsiva — no hay palanca tipo Siegel (§3); (ii)
  la cota superior que Turán necesita es el teorema buscado — circularidad (§4); (iii)
  todos los promedios incondicionales toleran m = ∞ de densidad cero, con tolerancia
  T^θ que ningún momento finito reduce a O(1) (§5). Las tres localizaciones son la misma:
  distinguir "m ≤ C" de "m = C+1" es un evento individual de medida cero para toda
  estadística accesible — el cuantificador maestro (P43, Principio 3.1) gobierna también
  la finitud, no solo la anulación.

**La frase que resume la medición:** *"m finito" no es el mismo enunciado que "m = 0",
pero está detrás del mismo muro, porque el muro nunca fue sobre el valor de m: es sobre la
capacidad de cualquier promedio de ver UNA unidad de m.*

---

## 7. VEREDICTO

**VEREDICTO: DIANA INALCANZABLE** — con técnica actual y con todas las formas de argumento
catalogadas por el programa (propagación, amplificación, recurrencia, positividad, criba,
repulsión, sumas de potencias, momentos/concentración), por la razón siguiente:

> Toda ruta a "m ≤ C" es un certificado presupuesto/costo (Def. 6.1), y la dicotomía de
> la Prop. 6.2 es exhaustiva sobre el inventario: los funcionales acotados tienen costo
> por cuádruplo evanescente (T_λ: 2δ²K_λ(γ₀) → 0) y los de costo uniforme (κ_W/n_W) tienen
> acotación RH-equivalente o de la misma precisión de segundo orden uniforme-en-ventanas
> (Doc 108). No hay repulsión entre cuádruplos (§3: anti-Siegel, interacción aditiva y
> sub-barra-de-error), no existe la cota superior que Turán necesita (§4: circularidad de
> Landau–Ingham), y todos los promedios incondicionales — incluido el CLT de Selberg,
> directamente ciego a la abscisa — toleran m = ∞ de densidad cero (§5). La finitud está
> detrás del cuantificador maestro, en el mismo punto que la anulación.

**Matices que el veredicto NO incluye (los resultados positivos del doc):**

1. L8 **no colapsa a RH**: no existe ni se vislumbra "m ≥ 1 ⟹ m = ∞" (§2.5), y cualquier
   prueba futura necesitará el producto de Euler de manera esencial (Prop. 2.2/Cor. 2.3 —
   demostrado). La diana queda registrada como enunciado abierto genuinamente intermedio.
2. La finitud en cajas compactas m(δ₀,Γ) ≤ N(½+δ₀,Γ) < ∞ es teorema trivial (§4.3); el
   contenido íntegro de L8 es la uniformidad en Γ.
3. La forma exacta del mecanismo que alcanzaría L8 queda enunciada (Def. 6.1 + Obs. 6.3):
   un presupuesto global O(1) con costo mínimo uniforme por cuádruplo — lo que el polo da
   cerca de s = 1 (Siegel) y dim H¹ da en cuerpos de funciones (Weil). Si el programa
   Connes–Consani (o cualquier otro) produce un invariante finito-dimensional sobre
   Spec ℤ, su PRIMER dividendo verificable sería L8, antes que RH. Lectura física final:
   **la diana L8 es el detector más barato posible de cohomología genuina — y por eso
   mismo es inalcanzable para el análisis puro.**

---

## Referencias

**Internas (backward-only):** Doc 108 (Prop. 2.3, 2.5; Teoremas 3.3, 3.4, 4.3; §5; §8.1,
Obs. 8.1; Prop. 7.3); Doc 107 (Teorema 5.5, Prop. 6.1); Doc 106 (Prop. 3.6); Doc 100
(positividad semilocal; MW-7); Doc 99 (discriminador I2a); Doc 98 (Hipótesis T1, Cor. 2.4,
Prop. 6.1); Doc 96 (Teorema 8.1); Doc 95 (Lema 2.2); Doc 89 (ocho equivalencias); Doc 86
(§6, K_λ); P43 (Principio 3.1, ledger L1–L8, §6); P42 (§6); P41 (no-go interior/frontera);
P35 (κ = 2m).

**Literatura (verificable):**
- D. Platt, T. Trudgian, *The Riemann hypothesis is true up to 3·10¹²*, Bull. London
  Math. Soc. **53** (2021), 792–797. [verificado: altura 3 000 175 332 800]
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2ª ed. (rev. D. R.
  Heath-Brown), Oxford, 1986. [T86] (Cap. IX: densidad; §10.25: Davenport–Heilbronn;
  Cap. III: región libre y teorema recíproco de Landau; ζ sin ceros en (0,1).)
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. Publ. 53, 2004. [IK04]
  (Thm. 5.8, 5.12; Cor. 8.30; Cap. 9–10: valores grandes y densidad; Cap. 18: log-free y
  Deuring–Heilbronn.)
- H. Bohr, E. Landau (1914): N(σ,T) = O(T) para σ > ½. F. Carlson (1920); A. E. Ingham,
  *On the estimation of N(σ,T)*, Quart. J. Math. **11** (1940) [In40]; M. N. Huxley,
  Invent. Math. **15** (1972): exponentes de densidad citados.
- G. Halász, P. Turán, J. Number Theory **1** (1969); P. Turán, *On a New Method of
  Analysis and its Applications*, Wiley, 1984 (segundo teorema principal; constantes
  exactas no load-bearing).
- Yu. V. Linnik (1944), densidad log-free y repulsión (exposición [IK04] Cap. 18);
  E. Landau (1918); A. Page (1935); C. L. Siegel (1935); M. Deuring (1933);
  H. Heilbronn (1934): teoría del cero excepcional, enunciados estándar.
- A. Selberg, Arch. Math. Naturvid. **48** (1946): momentos incondicionales de S(t);
  N. Levinson (1974) ≥ 1/3; J. B. Conrey, J. reine angew. Math. **399** (1989) ≥ 2/5.
  Mejora por encima de 5/12: [NO VERIFICADO; no load-bearing].
- A. Speiser, Math. Ann. **110** (1934); N. Levinson, H. L. Montgomery, Acta Math.
  **133** (1974): ceros de ζ′ y la línea crítica.
- H. L. Montgomery, R. C. Vaughan, *Hilbert's inequality*, J. London Math. Soc. (2)
  **8** (1974). [MV74]
- X.-J. Li, J. Number Theory **65** (1997); E. Bombieri, J. C. Lagarias, J. Number
  Theory **77** (1999). (Rango numérico verificado de λ_n ≥ 0: [NO VERIFICADO].)
- H. Davenport, H. Heilbronn, J. London Math. Soc. **11** (1936).
- A. Connes, C. Consani, positividad de Weil semilocal (2021–22), citada vía Doc 100
  [detalles bibliográficos NO VERIFICADOS aquí].

*Fin del Doc 111.*
