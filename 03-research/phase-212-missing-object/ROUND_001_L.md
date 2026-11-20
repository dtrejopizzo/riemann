# ROUND_001_L — Rigidez de comparadores de tipo Carathéodory en la escalera de potencias

Estado global: **PROVED** (relativo a tres teoremas clásicos CITED, enunciados en §1) el lema de rigidez
L-comp en la clase «comparador de tipo Carathéodory en el mismo portador»; **PROVED** su forma
incondicional de exclusión; **CONDITIONAL** el recíproco (existencia de comparadores admisibles).
No es un paso de signo: no aporta positividad de la forma. Ningún paper ni otro archivo modificado.

Notación de `../phase-211-sign-sandbox/STATEMENT_001.md`, `POWER_CONE_001.md`, `POWER_BRIDGE_002.md`.
Se cita «211/GLOBAL» = `../phase-211-sign-sandbox/POWER_GLOBAL_ROUTE_REVIEW.md`, «211/HYP» =
`../phase-211-sign-sandbox/POWER_HYPERBOLIC_MODEL_GRAM.md`.

## Cotejo

**(1) Antecedente más cercano.** 211/GLOBAL, «Comparación hiperbólica pequeña: condición necesaria de
anulación» y «Cierre de la comparación hiperbólica pequeña»: para UN comparador (el modelo hiperbólico
a = 2π) se prueba K_Phi ≥ εK_h ⟹ U_Phi = 0, y un certificado de intervalos da U_Phi ≠ 0. §6 de esta
memo comprueba que esa condición necesaria es literalmente la de L-comp para ese comparador. Otros
antecedentes, más lejanos:
- 211/GLOBAL, «Filtro general reutilizable»: si D = o(1/u) y K_D es PSD en pares, D ≡ 0 (rigidez en
  el infinito, sólo bloques 2×2, sin medida de borde).
- 211/GLOBAL, «Comparaciones primitivas: transferencia analítica del descarte»: PSD sobre bloques
  primitivos de un intervalo ⟹ PSD completa, para D impar real-analítica (se usa en §7.4).
- 211/GLOBAL, comparaciones K_Phi − K_(2π) y K_Phi − K_asinh (sólo ε = 1, por menores de jets
  certificados).
- Índice: README línea 1791 («POWER usa su núcleo real de tipo Pick»); 04_PHASES_100-189 filas
  G2F-phase-102/115,116 («positive boundary measure», reformulación), G1F-R160_S3 §2.1#2, G7F-R162_803;
  CW D-16. Todos registran la positividad de tipo Herglotz como reformulación del objetivo; ninguno
  enuncia una rigidez de comparadores.
- Paper 20 thm:boundary: identidad de borde incondicional (se re-demuestra en §0 para M, en dos líneas).
- P47 thm:noimport / IDX CPOS_CLASS_001: «positividad importada» para construcciones uniformes en el
  peine; clase de hipótesis distinta (uniformidad en el dato), no usa la medida de borde.
- Búsqueda de «medida de borde», «boundary measure», Herglotz, Carathéodory, Pick, Nevanlinna en el
  índice, el grid, el crucigrama, P48 y la fase 211: ningún enunciado del lema general. Una búsqueda
  sin coincidencias no prueba novedad; el principio usado (unicidad de la representación integral de
  una función real-positiva) es clásico y no se le atribuye novedad.

**(2) Afirmación nueva respecto del corpus.** El enunciado general: para TODO comparador de tipo
Carathéodory y todo ε > 0, la dominación K_M − εK_{M0} ⪰ 0 sobre un conjunto de unicidad (basta la
escalera 31.5 + n) obliga a M0 = Σ_k m_k·2u/(u² + τ_k²) con iτ_k polos de M sobre el eje imaginario y
0 ≤ m_k ≤ r_k/ε; sin término lineal, sin parte continua, sin átomos ajenos. Su contrarrecíproco es
incondicional. Corolario nuevo: K_M − ε·K_asinh no es PSD para NINGÚN ε > 0 (el corpus sólo tenía
ε = 1), sin certificado numérico.

**(3) Por qué evita la dificultad del antecedente.** El antecedente necesitaba, por comparador, una
realización operatorial del modelo, la continuidad en H_η, la identidad W_Phi[Phi] = 0 y un certificado.
Aquí la condición necesaria sale de la unicidad de la medida de borde y vale para la clase completa a
la vez. No evita, ni pretende evitar, el certificado final cuando el comparador es puramente atómico
(§6.2): decidir si un átomo concreto del modelo es o no un polo de M sigue siendo un cómputo.

**(4) Conexión con la positividad global.** Ninguna como paso de signo. Es una restricción de diseño
(OBJECT_SPEC §3): dentro de la clase Carathéodory, el espacio ℋ de una realización de Gram del núcleo
de la escalera es un subespacio pesado de L²(μ_M), con μ_M la medida de borde de M. Cae a sabiendas en
RULES_AVOID B4 como herramienta de descarte, no como ruta.

## 0. Objetos y hechos de partida

Π = {Re u > 0}. H(u) = ½a(a−1)π^{−a/2}Γ(a/2)ζ(a) con a = u + ½; M = H′/H, de modo que
M(u) = L(u + ½) con la L de POWER_CONE_001 §1. Para f definida en un conjunto de nodos X ⊂ (0,∞),

    K_f(u,v) = [f(u) + f(v)]/(u + v),   u, v ∈ X.

El núcleo es lineal en f: K_M − εK_{M0} = K_{M−εM0}.

**F1 (CITED, POWER_CONE_001 §2, §7).** H es entera, par, real en ℝ, y H(u) = C∫_0^∞ Φ(t)cosh(ut)dt
con C > 0, Φ > 0. En particular H > 0 en ℝ, M es meromorfa en ℂ, impar, real-analítica en todo ℝ,
M(0) = 0, y M es holomorfa en Re u > ½.

**F2 (PROVED). Identidad de borde.** Para τ real con H(iτ) ≠ 0, Re M(iτ) = 0.
Prueba. H par y real en ℝ da H(iτ) = H(−iτ) = conj H(iτ), luego τ ↦ H(iτ) es real; su derivada
iH′(iτ) es real, luego H′(iτ) ∈ iℝ y M(iτ) ∈ iℝ. ∎ (Es thm:boundary del Paper 20 en la variable u;
sólo usa paridad y realidad de H.)

**F3 (PROVED). Polos.** Los polos de M son simples, con residuo r entero ≥ 1 (orden de anulación de H
en el punto). Los polos sobre el eje imaginario forman un conjunto discreto {±iτ_k}, τ_k > 0, simétrico
(M impar), y 0 no es polo (H(0) > 0). Se escribe r_k para el residuo en ±iτ_k. No se afirma ni se usa
nada sobre la existencia o ausencia de polos de M en 0 < Re u ≤ ½.

**F4 (PROVED). Crecimiento.** (a) M(x) = O(log x) para x real → +∞. (b) |M(u)| ≤ C(1 + |u|) en
Re u ≥ 3/2.
Prueba. Con a = u + ½, Re a ≥ 2: |1/a| + |1/(a−1)| ≤ 2; |ζ′/ζ(a)| ≤ ΣΛ(n)n^{−2} < ∞; y para
Re z ≥ 1, ψ(z) = −γ + Σ_{k≥0}(z−1)/((k+1)(k+z)) con |k+z| ≥ k+1 da |ψ(z)| ≤ γ + (π²/6)|z−1|. Esto
prueba (b). Para (a), en z real > 0 vale log z − 1/z ≤ ψ(z) ≤ log z (las cotas usadas en
POWER_CONE_001 §5). ∎

## 1. Herramientas clásicas (CITED)

Una función F es **real-positiva** (de Carathéodory) en Π si es holomorfa en Π con Re F ≥ 0.

**C1 (CITED, representación de Herglotz–Riesz en el semiplano).** F es real-positiva en Π si y sólo si

    F(u) = iβ + c·u + ∫_ℝ [1/(u − iτ) − iτ/(1+τ²)] dμ(τ),

con β real, c ≥ 0 y μ medida positiva con ∫dμ/(1+τ²) < ∞. La terna (β, c, μ) es única:
c = lim_{x→+∞} F(x)/x, y μ es el límite débil-* de (1/π)Re F(σ + iτ)dτ cuando σ ↓ 0 (inversión de
Stieltjes sobre funciones continuas de soporte compacto). μ es la **medida de borde** de F. Si F es real
en (0,∞), entonces β = 0, μ es par y F(u) = c·u + ∫ u/(u²+τ²) dμ(τ).

**C2 (CITED, teorema de Pick, nodos finitos).** Sean u_1,…,u_n ∈ Π distintos y w_1,…,w_n ∈ ℂ. Existe F
real-positiva en Π con F(u_i) = w_i si y sólo si la matriz [(w_i + conj w_j)/(u_i + conj u_j)] es
semidefinida positiva. (Es la forma de Carathéodory del teorema de Nevanlinna–Pick; se obtiene de la
forma del disco con z = (u−1)/(u+1), S = (F−1)/(F+1), mediante
(1 − S(u)conj S(v))/(1 − z conj z′) = [(u+1)/(F(u)+1)]·conj[(v+1)/(F(v)+1)]·(F(u)+conj F(v))/(u+conj v);
el factor está definido porque la diagonal PSD obliga Re w_i ≥ 0.)

**C3 (CITED, condición de Blaschke para tipo acotado).** Si G ≢ 0 es cociente de dos funciones
holomorfas acotadas en Π, sus ceros u_n cumplen Σ Re u_n/(1+|u_n|²) < ∞. Toda F real-positiva es de
tipo acotado: F = (1+S)/(1−S) con |S| ≤ 1, S ≢ 1.

**Lema 1.1 (PROVED). Dirección fácil con Gram explícito.** Si F es real-positiva con datos (β, c, μ),

    [F(u) + conj F(v)]/(u + conj v) = c + ∫ dμ(τ)/[(u − iτ)·conj(v − iτ)],   u, v ∈ Π,

que es un Gram en ℂ ⊕ L²(μ). Prueba: sumar las representaciones C1 y usar
1/(u−iτ) + 1/(conj v + iτ) = (u + conj v)/[(u−iτ)(conj v + iτ)]. ∎

**Definición (conjunto de unicidad).** X ⊂ (0,∞) es de unicidad si
(i) X tiene un punto de acumulación en (0,∞), o
(ii) Σ_{u∈X, u≥2} 1/u = ∞.

**Lema 1.2 (PROVED). La escalera es de unicidad.** X = {31.5 + n : n ≥ 0} cumple (ii) (serie armónica).
Además, en ambos casos Σ_{u∈X} u/(1+u²) = ∞ (pues x/(1+x²) ≥ 1/(2x) para x ≥ 1), y para todo c ≥ 0 el
conjunto trasladado {u − c : u ∈ X, u > c + 1} sigue sin cumplir la condición de Blaschke de Π en el
caso (ii). ∎

La condición es también necesaria para la unicidad en la clase acotada: si Σ u/(1+u²) < ∞ existe el
producto de Blaschke de X (CITED), y la conclusión del Teorema 3.1 deja de estar determinada por X.

**Lema 1.3 (PROVED). Pick en conjuntos infinitos y unicidad.** Sea X ⊂ (0,∞) de unicidad y f: X → ℝ.
Si K_f es PSD en todo subconjunto finito de X, existe una única F real-positiva en Π con F|_X = f;
además F es real en (0,∞).
Prueba. Unicidad: si F_1, F_2 interpolan, F_1 − F_2 es de tipo acotado y se anula en X, que viola la
condición de Blaschke; por C3, F_1 = F_2. Existencia, X numerable: sea x_1, x_2,… una enumeración y F_n
real-positiva con F_n(x_j) = f(x_j), j ≤ n (C2). Las S_n = (F_n − 1)/(F_n + 1) están acotadas por 1;
por Montel una subsucesión converge localmente uniformemente a S con |S| ≤ 1 y
S(x_j) = (f(x_j)−1)/(f(x_j)+1) ≠ 1, luego S ≢ 1 y F = (1+S)/(1−S) es real-positiva e interpola.
X no numerable: elegir X′ ⊂ X numerable y de unicidad, con interpolante F; para x ∈ X, el interpolante
de X′ ∪ {x} coincide con F por unicidad, luego F(x) = f(x). Realidad: conj F(conj u) también interpola;
por unicidad coincide con F. ∎

## 2. Teorema general (sin hipótesis sobre M ni sobre el comparador)

**Teorema 2.1 (PROVED, relativo a C2–C3).** Sea X ⊂ (0,∞) de unicidad, M0: X → ℝ cualquiera, ε > 0.
Son equivalentes:
(a) K_M − εK_{M0} es PSD en todo subconjunto finito de X;
(b) existe F real-positiva en Π, real en (0,∞), con M − εM0 = F sobre X.
En tal caso F es única.
Prueba. (a)⟹(b) es el Lema 1.3 con f = (M − εM0)|_X; (b)⟹(a) es el Lema 1.1 restringido a X. ∎

**Corolario 2.2 (PROVED). Caso M0 = 0; reformulación ya registrada.** Los bloques de la escalera
[(L(32+i)+L(32+j))/(63+i+j)] son PSD para todo tamaño si y sólo si M es real-positiva en Π.
Prueba. Si son PSD, existe F real-positiva con F = M en la escalera. Por F4(b), M/(u+1) es acotada en
Re u > 3/2, luego M − F es de tipo acotado allí y se anula en un conjunto que viola Blaschke (Lema 1.2):
M = F en Re u > 3/2, y por el teorema de identidad para funciones meromorfas en Π conexo, M = F en Π.
Recíproco: Lema 1.1. ∎
Esto es la lectura «núcleo real de tipo Pick» ya anotada en el índice (README línea 1791); se usa aquí
como herramienta y no se presenta como avance (RULES_AVOID B3).

## 3. Rigidez de comparadores real-positivos

**Teorema 3.1 (PROVED, relativo a C1–C3; ninguna hipótesis sobre el signo de K_M).** Sea X ⊂ (0,∞) de
unicidad (por ejemplo la escalera 31.5 + n, o cualquier intervalo), ε > 0, y M0 real-positiva en Π,
real en (0,∞), con datos de Herglotz (c_0, μ_0). Si K_M − εK_{M0} es PSD en todo subconjunto finito de
X, entonces:

1. M − εM0 se extiende a una función F real-positiva en Π; en particular M no tiene polos en Π y
   Re M ≥ 0 en Π (y por tanto K_M es PSD en todos los nodos de Π: la hipótesis contiene el signo de la
   escalera completa).
2. La medida de borde de M es puramente atómica: μ_M = Σ_k r_k(δ_{τ_k} + δ_{−τ_k}), con ±iτ_k los
   polos de M en el eje imaginario y r_k sus residuos; el coeficiente lineal de M es c_M = 0.
3. c_0 = 0 y εμ_0 ≤ μ_M. Es decir,

       M0(u) = Σ_k m_k · 2u/(u² + τ_k²),   0 ≤ m_k ≤ r_k/ε,   Σ_k m_k/(1+τ_k²) < ∞.

   En particular μ_0 no tiene parte absolutamente continua ni singular continua, no tiene átomos fuera
   de {±τ_k}, no tiene átomo en 0, y M0 no tiene término lineal.

Prueba.
*Paso 1.* Por el Teorema 2.1 hay F real-positiva con M − εM0 − F = 0 en X. Sea G = M − εM0 − F.
Caso (i): G es meromorfa en Π (M lo es; M0 y F son holomorfas) y se anula en un conjunto con punto de
acumulación x* ∈ (0,∞), que no es polo de G (F1: M es holomorfa en el eje real); G ≡ 0 en Π.
Caso (ii): en Re u > 3/2, M es de tipo acotado (F4(b): M/(u+1) acotada y 1/(u+1) acotada) y M0, F lo
son (C3); G es de tipo acotado en ese semiplano y se anula en {u ∈ X, u > 5/2}, que viola la condición
de Blaschke del semiplano Re u > 3/2 (Lema 1.2). Luego G ≡ 0 en Re u > 3/2 y, por identidad de
funciones meromorfas en Π, G ≡ 0 en Π. En ambos casos M = εM0 + F en Π: el lado derecho es holomorfo
con parte real ≥ 0. Esto da 1.
*Paso 2.* M es ahora real-positiva, real en (0,∞); por C1, c_M = lim M(x)/x = 0 (F4(a)). Sea φ continua
con soporte compacto en un intervalo abierto J del eje sin polos de M. M es holomorfa en un entorno de
i·sop φ, luego Re M(σ+iτ) → Re M(iτ) = 0 uniformemente en sop φ (F2), y ∫φ dμ_M = 0. Cerca de un polo
iτ_k, M(u) = r_k/(u − iτ_k) + g(u) con g holomorfa; Re g(iτ) = 0 para τ ≠ τ_k próximo (F2 y
Re[r_k/(i(τ−τ_k))] = 0), y por continuidad también en τ_k. Para φ soportada cerca de τ_k,

    ∫φ dμ_M = lim_{σ↓0} (1/π)∫φ(τ)·r_kσ/(σ² + (τ−τ_k)²)dτ + 0 = r_kφ(τ_k).

Por una partición de la unidad, μ_M = Σ r_k(δ_{τ_k}+δ_{−τ_k}); 0 no es polo (F3). Esto da 2.
*Paso 3.* M = εM0 + F con las tres real-positivas; por unicidad de C1, c_M = εc_0 + c_F y
μ_M = εμ_0 + μ_F con c_F ≥ 0, μ_F ≥ 0. Luego c_0 = 0 y εμ_0 ≤ μ_M. Una medida positiva dominada por
una puramente atómica es atómica con átomos en los mismos puntos y masas menores; μ_0 par y C1 dan la
fórmula de 3. ∎

**Observación 3.2 (PROVED). Espacio de la realización.** Bajo la hipótesis del teorema, el Gram del
Lema 1.1 para el comparador es K_{M0}(u,v) = Σ_k m_k[1/((u−iτ_k)(v+iτ_k)) + 1/((u+iτ_k)(v−iτ_k))]:
vive en ℓ² sobre los polos de M del eje, con pesos m_k ≤ r_k/ε. Un espacio ℋ de tipo Carathéodory que
minore al objetivo no puede venir de un modelo cuyo espectro de borde no sea una parte de ese conjunto.

## 4. Forma incondicional y recíproco condicional

**Corolario 4.1 (PROVED, incondicional). Exclusión.** Sea M0 real-positiva en Π, real en (0,∞), y
supóngase una de:
(E1) c_0 > 0;
(E2) μ_0 tiene parte continua no nula (absolutamente continua o singular continua);
(E3) μ_0 tiene un átomo en un punto τ* tal que iτ* no es polo de M (incluido τ* = 0);
(E4) μ_0({τ_k}) > r_k/ε para algún polo iτ_k de M.
Entonces, para ese ε (en E1–E3, para todo ε > 0) y para cada conjunto de unicidad X, existen un bloque
finito de nodos en X y un vector real con energía negativa para K_M − εK_{M0}. En particular esto ocurre
con nodos en la escalera 31.5 + n.
Prueba. Contrarrecíproco del Teorema 3.1. ∎
No se supone ni se concluye nada sobre el signo de K_M; no se da el tamaño del bloque ni el vector.

**Proposición 4.2 (CONDITIONAL en «M real-positiva en Π», es decir, en el signo de la escalera,
Cor. 2.2). Recíproco.** Si M es real-positiva en Π, entonces M = Σ_k r_k·2u/(u²+τ_k²) y, para toda
elección 0 ≤ m_k ≤ r_k/ε, M0 = Σ m_k·2u/(u²+τ_k²) cumple K_M − εK_{M0} ⪰ 0 en todos los nodos de Π.
Prueba. Paso 2 del Teorema 3.1 (que sólo usa que M es real-positiva) da la representación de M; entonces
M − εM0 = Σ(r_k − εm_k)·2u/(u²+τ_k²) es real-positiva y se aplica el Lema 1.1. ∎

**Resumen de lo condicional y lo incondicional.**
- Incondicional: el Teorema 3.1 (implicación) y el Corolario 4.1 (exclusión). La hipótesis «diferencia
  PSD con M0 real-positiva» NO necesita suponer M real-positiva: la implica (trivialmente, pues
  K_M = (K_M − εK_{M0}) + εK_{M0}; el contenido del teorema es el paso de los nodos a Π y la medida).
- Condicional: que exista algún comparador real-positivo no nulo. Existe uno si y sólo si M es
  real-positiva en Π y tiene al menos un polo en el eje (PROVED como equivalencia; ninguno de los dos
  miembros se afirma).
- Si M0 no es real-positiva (comparador con K_{M0} no PSD), sólo vale el Teorema 2.1: la conclusión es
  «M − εM0 es real-positiva», sin dominación de medidas, porque M0 no tiene medida de borde positiva.
  Si además M0 es meromorfa en Π y X es de tipo (i), entonces M0 = (M − F)/ε en Π: M0 tiene en Π
  exactamente los polos de M, con residuos r/ε (PROVED, identidad de funciones meromorfas).

## 5. Infinito y término lineal

- **PROVED.** c_M = 0 por F4(a), sin hipótesis. De ahí c_0 = 0 y c_F = 0 en toda dominación: ningún
  comparador con término lineal c_0·u, c_0 > 0, es admisible. El núcleo de c_0·u es la constante c_0
  (rango uno, vector de unos): K_M − ε·c_0·𝟙𝟙ᵗ nunca es PSD en todos los tamaños de un conjunto de
  unicidad.
- **PROVED.** En el origen: M(0) = 0 y M es analítica en 0; no hay átomo en τ = 0. Un comparador con
  término m/u, m > 0 (átomo en 0) queda excluido para todo ε.
- **PROVED.** El crecimiento logarítmico M(x) ~ ½log x no está en contradicción con c_M = 0: para una
  real-positiva con c = 0, F(x) = ∫x/(x²+τ²)dμ puede crecer como log x si μ([−R,R]) ~ R log R.
- Relación con el «Filtro general reutilizable» de 211/GLOBAL (D = o(1/u) y pares PSD ⟹ D ≡ 0): es
  el caso en que F = D tiene c_F = 0 y masa total nula; aquí se obtiene con todos los tamaños la
  conclusión más fuerte (F queda determinada por su medida), a cambio de pedir todos los tamaños.

## 6. La comparación hiperbólica pequeña de la fase 211 como instancia

**6.1 (PROVED). Mismo tipo y mismo portador, sin congruencia intermedia.** En 211, K_Phi es K_f con
f = M_Phi = Z_Phi′/Z_Phi, Z_Phi(u) = ∫Φ(t)e^{ut}dt; por F1, Z_Phi = H salvo constante positiva, luego
M_Phi = M (comprobado además contra el desarrollo ½log(u/2π) + 7/(4u) + … de 211/GLOBAL: los términos
2/u de 1/a + 1/(a−1) y −1/(4u) de ½ψ(a/2) suman 7/(4u)). K_(2π) es K_f con f = M_a = Z_a′/Z_a,
a = 2π, sobre los mismos nodos reales positivos («bloques de tasas u > ½»). Ambos son núcleos
[f(u)+f(v)]/(u+v) en el mismo portador. La única congruencia presente en la escalera es la diagonal
d_i = c_iζ(u_i+½) de POWER_CONE_001 §1, común a ambos núcleos; una congruencia invertible común
conserva el orden PSD de la diferencia en cada bloque, así que el enunciado no cambia.

**6.2 (PROVED). Medida de borde del modelo.** Por 211/HYP §4 (REP), M_a(u)/u = ½Tr(H_a + u²/4)^{-1}
con H_a = −D_r² + a²e^{2r} (Dirichlet en 0), positivo, de resolvente de traza finita. Con autovalores
λ_1 ≤ λ_2 ≤ … y ω_k = 2√λ_k,

    M_a(u) = Σ_k 2u/(u² + ω_k²),

real-positiva con c = 0 y μ_a = Σ_k(δ_{ω_k} + δ_{−ω_k}): puramente atómica, masas 1.

**6.3 (PROVED). Coincidencia de las condiciones necesarias.** El Teorema 3.1 da:
K_M ⪰ εK_a en la escalera ⟹ para todo k, iω_k es polo de M con residuo ≥ ε; es decir G(ω_k) = 0
para todo k, con G(ω) = 2∫_0^∞Φ(t)cos(ωt)dt = H(iω)/C′. La condición de 211 es U_Phi = 0 con
U_Phi = ∫Φ(t)exp(2it√H_a)dt, que por cálculo funcional y paridad de Φ equivale a G(ω_k) = 0 para
todo k. Son la misma condición. El cierre de 211 (G < −10⁻⁸ en [17, 41/2] ∋ ω_1, certificado) es
entonces exactamente la verificación de (E3) de Cor. 4.1 en el primer átomo del modelo.
Lo que añade el Teorema 3.1: (a) vale para todo a > 0 y para las variantes Robin y las sumas
w·b·M_{a,β}(bu) de 211/GLOBAL, sin rehacer la cadena de densidad y continuidad en H_η ni usar
W_Phi[Phi] = 0; (b) basta la escalera; (c) la cota de residuos (para ε > 1 exige r_k ≥ ε).
Lo que NO sustituye: el certificado de que un átomo concreto del modelo no es polo de M. Para un
comparador puramente atómico la exclusión sigue requiriendo ese dato puntual. **NUMÉRICO/CITED** el
certificado de 211; no se recomputa.

**6.4 (PROVED). Comparador asinh: exclusión para todo ε sin certificado.** M_0(u) = ½asinh(u/c),
c = 4π. asinh aplica Π conformemente en {Re w > 0, |Im w| < π/2} (sinh(x+iy) = sinh x cos y +
i cosh x sin y), luego M_0 es real-positiva. En el borde, asinh(iτ/c) = arccosh(|τ|/c) + i·sgn(τ)π/2
para |τ| > c: μ_0 tiene densidad (1/2π)arccosh(|τ|/c) > 0 en |τ| > c. Es absolutamente continua y no
nula: (E2). Por Cor. 4.1, K_M − ε·K_{M_0} no es PSD para ningún ε > 0, con bloque negativo en la
escalera. El corpus tenía sólo ε = 1 (menor de jets con certificado de intervalos).

## 7. Alcance: qué NO cubre el lema

7.1 **Comparadores PSD que no son de tipo Carathéodory (PROVED que la clase general no tiene rigidez).**
Si N(u,v) es un núcleo PSD cualquiera, K_M − εN ⪰ 0 no impone nada del estilo anterior: si K_M es PSD
y no nulo, N = g⊗g con g = K_M(·,w) y ε = 1/K_M(w,w) cumple la dominación (Cauchy–Schwarz en el espacio
reproductor); recíprocamente cualquier dominación de un PSD da K_M PSD. Así «existe N PSD no nulo
dominado» equivale a «K_M PSD y no nulo»: la clase general no restringe el diseño y el Teorema 3.1 no
dice nada de ella.

7.2 **Comparadores de tipo Carathéodory tras una congruencia NO común.** Núcleos
g(u)g(v)[M0(u)+M0(v)]/(u+v) con g no constante, o comparadores que son de tipo Carathéodory en otra
coordenada (por ejemplo en los coeficientes c_i y no en d_i = c_iζ(u_i+½), o en x = u²), no son
diferencias K_{M−εM0}; no cubiertos. La congruencia común sí está cubierta (§6.1).

7.3 **Compensaciones conjuntas.** Descomposiciones K_M = Σ_j N_j con sumandos sin signo individual, o
K_M − εK_{M0} + (corrección) con corrección no PSD, quedan fuera: el teorema sólo trata la diferencia
de dos núcleos del tipo. Tampoco cubre comparadores con signo (M0 no real-positiva) más allá del
Teorema 2.1.

7.4 **Restricción a bloques primitivos (CITED + PROVED).** Si M0 es además impar y real-analítica en
todo ℝ (por ejemplo μ_0 con un hueco alrededor de 0, como M_a y asinh), el lema «Comparaciones
primitivas» de 211/GLOBAL (c = ½) da: PSD de K_{M−εM0} sobre los bloques primitivos de un intervalo
abierto I ⊂ (½,∞) ⟹ PSD completa. Entonces el Teorema 3.1 y el Cor. 4.1 valen también con la
hipótesis restringida a bloques primitivos de un intervalo. Para la escalera discreta con las dos
restricciones de momento el lema citado no se aplica tal cual (pide un intervalo): **OPEN**.

7.5 **Conjuntos de nodos que sólo se acumulan en 0.** Si X ⊂ (0,∞) sólo se acumula en 0 con Σu = ∞,
la unicidad se obtiene trabajando en un semidisco {|u| < δ, Re u > 0}, donde M es acotada y la
condición de Blaschke para puntos reales que tienden a 0 es Σu < ∞. **ARGUED** (no se escribe la
transformación conforme); no se necesita para la escalera.

7.6 **Dominaciones en un número finito de tamaños o en nodos de Blaschke.** Si Σ_{u∈X}u/(1+u²) < ∞
(por ejemplo nodos 2^n), el interpolante no es único y no hay rigidez. Bloques de tamaño acotado:
nada.

7.7 **Ventana fija.** El lema vive en la escalera de potencias (todas las ventanas a la vez). No dice
nada sobre comparadores de la forma a_T para un T fijo.

## 8. Batería de falsificadores

El lema no es un paso de signo; se indica qué línea usa cada estructura, para que no se lea como tal.
- El Teorema 2.1 y el Paso 1 del Teorema 3.1 valen para cualquier M meromorfa en Π, real en (0,∞) y
  de tipo acotado en algún semiplano Re u > c: son genéricos (RULES_AVOID B1) y no llevan signo.
- Los Pasos 2–3 (medida atómica) usan sólo F2 (paridad de H) y F4(a). Valen por tanto idénticamente
  para todo modelo con la misma simetría: Davenport–Heilbronn, Epstein, cuartetos y f_t. En esos
  modelos el teorema sigue siendo cierto como implicación; lo que cambia es que su hipótesis es vacía
  cuando el M del modelo tiene polos en Π. No distingue esos modelos por sí solo: correcto para una
  herramienta de descarte, insuficiente como mecanismo.
- Para cΛ (c ≠ 1), a_P, borrado y amplificación finitos, b_θ y sistemas de Beurling sin simetría: falla
  F2 (la función correspondiente no es H′/H con H par; Re M(iτ) deja de anularse), y con ella el Paso 2:
  la medida de borde, si existe, no es puramente atómica. El Teorema 2.1 sigue valiendo.

## 9. Consecuencia para OBJECT_SPEC §3

La conjetura de trabajo L-comp es **correcta en su clase** y debe leerse así:

- **PROVED.** En la escalera de potencias, un espacio ℋ que provenga de un comparador de tipo
  Carathéodory en el mismo portador (K_M = ε·K_{M0} + resto de tipo Carathéodory PSD) es
  necesariamente ℓ² sobre una parte de los polos de M en el eje imaginario, con pesos ≤ r_k/ε, sin
  componente continua ni lineal. Ningún modelo exterior con medida de borde continua (asinh) o con un
  átomo fuera de los polos de M (hiperbólico a = 2π) sirve, para ningún ε.
- **PROVED.** Fuera de esa clase la restricción no existe (§7.1): comparadores PSD generales son
  admisibles en cuanto el objetivo es cierto, y no dan información previa.
- Precisión al texto de OBJECT_SPEC §3: «la medida de borde de M, que es puramente atómica» es una
  conclusión bajo la hipótesis de dominación (o bajo «M real-positiva»), no un hecho incondicional;
  lo incondicional es Re M(iτ) = 0 fuera de los polos (F2) y la forma de exclusión (Cor. 4.1).
  Además el término lineal queda excluido (c_0 = 0), no sólo acotado.

## Resultado

Pieza **PROVED** (lema de rigidez, relativa a C1–C3 clásicos) y **NO-GO con clase**: clase =
comparadores real-positivos en Π, reales en (0,∞), comparados con el núcleo de la escalera en el mismo
portador (o tras congruencia común), con dominación en todos los tamaños sobre un conjunto de unicidad.
Dentro de la clase sólo son admisibles las sub-sumas atómicas de M; fuera de la clase el lema no dice
nada. No es candidata a construcción y no aporta signo.

## Qué se probó

1. F2: Re M = 0 en el eje imaginario fuera de los polos (PROVED, incondicional).
2. Lema 1.2: la escalera 31.5 + n es conjunto de unicidad (viola Blaschke) (PROVED).
3. Teorema 2.1: dominación en X ⟺ M − εM0 coincide en X con una real-positiva única (PROVED rel. C2–C3).
4. Teorema 3.1: rigidez con comparador real-positivo; c_0 = 0, εμ_0 ≤ μ_M atómica (PROVED rel. C1–C3).
5. Corolario 4.1: forma incondicional de exclusión (E1)–(E4) (PROVED).
6. Proposición 4.2: recíproco (CONDITIONAL en M real-positiva).
7. §6: la comparación hiperbólica pequeña de 211 es una instancia con la misma condición necesaria;
   asinh queda excluido para todo ε sin certificado (PROVED).
8. §7.1: la clase PSD general no tiene rigidez (PROVED).

## Qué falló y por qué

- No se obtiene una exclusión sin certificado para comparadores puramente atómicos (modelo hiperbólico):
  la condición es «cada átomo del modelo es polo de M», y decidirla en un átomo es un dato puntual sobre
  G(ω_k) que el lema no produce.
- No se extiende la rigidez a la escalera discreta con las dos restricciones primitivas (§7.4): el lema
  de continuación disponible pide un intervalo. **OPEN.**
- No hay rigidez para comparadores PSD generales ni para compensaciones conjuntas (§7.1, §7.3): no es un
  defecto de la prueba, es falso que la haya.
- C1–C3 se citan como teoremas clásicos; no se re-demuestran aquí. §7.5 queda ARGUED.

## Siguiente paso concreto

Ajustar OBJECT_SPEC §3 al enunciado del §9 (clase exacta; término lineal excluido; «puramente atómica»
como conclusión condicionada) y usar el Cor. 4.1 como filtro previo de toda candidata cuyo ℋ_T sea de
tipo Carathéodory en la escalera: debe exhibir su medida de borde y mostrar que es una sub-suma atómica
de la de M, o declararse fuera de la clase (§7.1–7.3) y decir por cuál de las tres salidas. Anotar el
NO-GO con su clase en el índice de rutas y en el grid (esta memo no los edita).
