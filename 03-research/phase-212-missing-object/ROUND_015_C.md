# Ronda 15, memo C — Funcional convexo con hessiano a_T (O14) y emparejamiento impar no lineal en A_M (O-odd)

Notación del brief común: a_T(F) = Arch(F) − Σ_n v_n c_F(log n) sobre P_T, v_n = 2Λ(n)/√n. Controles: cΛ con c = 2,
borrado de una potencia de primo, peso de tipo Beurling. Escribo a^{(c)} para la forma con peso cΛ.

## 0. Cotejo (leído en primaria)

- `RULES_AVOID.md` M1, M4, M5, N1–N5, W4, X2; `REVIEW_005.md` R5-a…R5-e; `ROUND_013_C.md` §4.2 (Lema K) y §5;
  `ANNEX_COTEJO_LORENTZ_2.md` (lista de no encontrados, ítem 6: «Prékopa–Leindler o Brascamp–Lieb aplicados a la
  forma. Sólo hay menciones en listas»); `ROUND_009_G3.md` §0 (búsqueda «Prékopa» sin uso).
- Fase 197 `BARRIER_W_001` §§0–4: Teoremas W1 (n₋(T) monótono, todo cruce descendente), W2 (camino rectilíneo
  a_s = (1−s)a_0 + sΛ: a lo sumo un cruce, «sin núcleo antes de s = 1» ⟺ μ_T(Λ) ≥ 0), W3 (codimensión). Su §0
  ya registra: AUDIT_193 #101 (invariante entero/flujo espectral, «constancia = positividad»), P35-3 y P49-2 (Maslov),
  ES-18 (índice de Pontryagin finito, DEAD), A14a-5 (inercia de Sylvester ciega), Teorema P / thm:index.
- Fase 186: `R186_034` (muro W-det: D_B(s;T) = det(1 − s·Pos^{−1/2}Neg·Pos^{−1/2}) entera, λ_A > 0 ⟺ β_max < 1;
  Thm 3.1: todo determinante cuyo signo decide λ_A factoriza como λ_A·R y su término principal con error
  multiplicativo O(1) nunca decide); `R186_045` §3.2 (criterio de momentos m_k = tr B^k: «es W-det como serie de
  potencias»); grid entrada 28.

Una búsqueda sin coincidencias no prueba novedad; las coincidencias de abajo sí prueban repetición.

## 1. Idea (1): log-concavidad, hessiano de log(Γ × Euler)

**Qué cerró el corpus.** M1 (`R160_C7_R1` §§5–6, Prop. 6.2): clase cuadrática lorentziana, Alexandrov–Fenchel y su
versión combinatoria se reducen sobre la forma al enunciado. N1/R5-a: log-concavidad en un punto base (determinante,
función de partición, varianza) y signatura de Lorentz de una hessiana en un punto equivalen a (G) o al enunciado.
N2/R5-b: grado ≥ 3 hiperbólico con hessiana −a_T es grado dos o el objetivo con margen. Lema K: convexidad de una
medida o de pesos positivos da hessiano ⪰ 0 para todo peso. **«Hessiano de un funcional log-cóncavo en un punto base
determinado por los enteros» está dentro de R5-a** (el punto base no figura como hipótesis de R5-a: la equivalencia
se prueba en un punto cualquiera). Repetición, salvo el apartado 1.2.

**1.1 Lema A (PROVED). El camino s ↦ s + εF no distingue c.** Sea Φ_c(F) = Φ_∞(F) + c·Φ_pr(F) con Φ_pr cualquier
funcional construido linealmente a partir de log ζ = Σ_n (Λ(n)/log n) n^{−s} (segunda variación a lo largo de
cualquier camino s(ε), incluido s + εF con F función u operador). Entonces D²Φ_c(F_0) = D²Φ_∞(F_0) + c·D²Φ_pr(F_0)
es afín en c en todo punto base F_0 independiente de c.
*Prueba.* log(ζ^c) = c log ζ y la segunda variación es lineal en el funcional. ∎
Consecuencias. (a) Si además cada factor −log(1 − p^{−s}) es una log-transformada de Laplace de una ley positiva
(lo es: ley geométrica de la valuación), D²Φ_pr ⪰ 0 para todo c > 0 (Lema K); la forma a_T tiene la parte prima con
signo opuesto, de modo que −a_T = D²(log Euler) − D²(log Γ) es diferencia de dos hessianos convexos y la convexidad
no aporta signo. (b) La positividad de una forma afín en c es un intervalo en c (W1 de la ronda 13): el camino s + εF
no separa c = 1 de c = 2 por estructura, sólo por tamaño. Coincide con R5-e y W2 de la fase 197.
Además, la segunda variación de n^{−(s+εH)} da (log n)² H² n^{−s}, un término diagonal, no la autocorrelación
c_F(log n): para producir c_F(log n) el funcional tiene que ser ya la forma (tautología).

**1.2 Lo que cambia con el punto base: Prékopa (convexidad por marginalización).** Única fuente de convexidad que no
es «medida positiva» ni «pesos positivos» y que el cotejo de Lorentz lista como no usada. Sea
Z(F) = ∫ e^{−V(x,F)} dx con V conjuntamente convexa en (x, F). Prékopa (CITED): log Z cóncava.

**Proposición B (PROVED, cálculo estándar + desigualdad de Brascamp–Lieb CITED).** Con μ_F ∝ e^{−V(·,F)}dx,
−D² log Z(F) = E_{μ_F}[V_FF] − Cov_{μ_F}(V_F) = E_{μ_F}[V_FF − V_Fx V_xx^{−1} V_xF] + G(F),
con G(F) = E[V_Fx V_xx^{−1} V_xF] − Cov(V_F) ⪰ 0 (Brascamp–Lieb aplicado a cada componente lineal de V_F).
Si V es cuadrática en x, G = 0 y −D² log Z es exactamente el complemento de Schur del bloque conjunto.
*Prueba.* Derivar dos veces log Z; la segunda igualdad es reordenar; G ⪰ 0 es la desigualdad de varianza de
Brascamp–Lieb para medidas log-cóncavas. ∎

**Corolario B′ (PROVED, en la clase declarada).** Si a_T = −D² log Z(F_0) en un punto base, el signo procede de
(i) la convexidad puntual de V en cada x y (ii) G ≥ 0. (ii) es válido para toda V convexa, luego ciego (Lema T).
(i) es una familia de enunciados PSD puntuales sobre bloques que contienen el peso. Si V es cuadrática en x, el
resultado es el complemento de Schur de un bloque, que cae en la dicotomía W2 de la ronda 13 (Gram ⇒ ciego; no Gram
⇒ equivale a la forma). Si V es convexa para todo peso de una de las tres clases de control, la conclusión valdría en
ese control: Lema T. Por tanto la única variante no cerrada es: V(x,F) **no cuadrática en x**, convexa sólo para el
peso verdadero, con la convexidad puntual en cada x verificable por una afirmación finita que falle en los tres
controles. OPEN; no tengo tal V. Nota: reparto en x de bloques PSD es estructuralmente un reparto puntual con signo
(clase O/O3, «partes con signo sin regla»); la diferencia es el término G, que es ciego. **No pasa la puerta.**

## 2. Idea (2): emparejamiento impar no lineal (signo, Cayley, resolvente, desplazamiento espectral, índice)

**Lema C (PROVED, dimensión finita; ARGUED a nivel de formas con resolvente compacto).** Sea A el operador de a_T
relativo a una métrica positiva fija sobre P_T y f: ℝ → ℝ impar, estrictamente creciente, f(0) = 0 (sign, arctan,
parte de Cayley, etc.). Toda magnitud de la forma tr g(A) con g impar no lineal, el índice del par de proyecciones
(1_{(−∞,0)}(Arch), 1_{(−∞,0)}(A)) o la función de desplazamiento espectral ξ(0; Arch, A) se determina por, o
determina, n₋(A) solo cuando se le añade el espectro de A: en particular ind = n₋(A) − n₋(Arch) (cuando la diferencia
de proyecciones es Hilbert–Schmidt) y «n₋(A) = 0» se lee como «ind = −n₋(Arch)».
*Prueba.* Para pares de proyecciones con P − Q en S_{2k+1}, ind = tr(P − Q)^{2k+1} (CITED, Avron–Seiler–Simon);
con P, Q proyecciones espectrales negativas de dos formas cuyo dominio común es P_T, el índice es la diferencia de
dimensiones de los espacios negativos. ∎
**Lectura.** La fórmula de índice es exacta e impar no lineal en A, pero exige las proyecciones espectrales de a_T,
es decir diagonalizar la forma (circular, J3). El entero es n₋ mismo; W1 de la fase 197 prueba que no hay otro
invariante conservado: n₋ es monótono en T y todo cruce es descendente.

**2.1 Flujo espectral en el acoplamiento c ∈ [0,1].** Es W2 de `BARRIER_W_001` con a_0 = 0 (camino a^{(c)}): concavidad
de c ↦ μ_T(a^{(c)}) da a lo sumo un cruce, y «número de ceros de D_T(c) en (0,1)» = n₋(a^{(1)}) − n₋(a^{(0)}) es
tautológico. Por encima del umbral arquimediano (Arch con direcciones negativas sobre P_T) se añade n₋(Arch) =
thm:index, archimedean, que no ve el peso. **Repetición.**

**2.2 Determinante de Fredholm y expansión en ciclos.** D_T(c) = det(1 − cK_T), K_T = Arch^{−1/2}·Prime·Arch^{−1/2}
(debajo del umbral) es D_B de `R186_034` Thm 2.1; −log D_T(c) = Σ_k c^k m_k/k con m_k = tr K_T^k es exactamente el
criterio de momentos de `R186_045` §3.2 (β_max < 1 ⟺ ∃k: m_k < 1), declarado «W-det como serie de potencias».
**Qué cierra W-det, exactamente:** Thm 3.1 de R186_034 — todo funcional determinantal continuo cuyo signo decide λ_A
factoriza como λ_A·R, y ningún término principal (Szegő, Kac–Akhiezer, Fisher–Hartwig, Landau–Widom) con error
multiplicativo O(1) decide; el signo vive en la fuga prolata. No cierra una cota explícita y uniforme en T de algún
m_k < 1.
**Lo genuinamente aritmético de la expansión (ARGUED, no nuevo como criterio).** Con S_u la traslación por u
comprimida a I, tr K^k = Σ_{n_1,…,n_k} v_{n_1}⋯v_{n_k} tr(Arch^{−1} S_{±log n_1} ⋯ Arch^{−1} S_{±log n_k}); como
Arch^{−1} es casi local en escala O(1) dentro de una ventana de ancho 2T, el término sólo es apreciable cuando las
sumas parciales Σ ±log n_i quedan en I y la cadena cierra, es decir n_1^{±1}⋯n_k^{±1} ≈ 1: casi-coincidencias
multiplicativas entre primos distintos, el lugar que señalan los tres residuos. Pero el criterio pide una **cota
superior** m_k < 1, no un signo; todas las v_n > 0, y lo que hay que acotar es la suma de cadenas, que el control
c = 2 multiplica por 2^k (m_k^{(2)} = 2^k m_k): el control falla en m_k ≥ 2^{−k}, de modo que una cota de m_k debe
tener precisión relativa 2^{−k}·(margen), que es W1 de la ronda 13 por otra vía. Sin objeto que acote m_k: **no pasa**.

## 3. Puerta de cuatro puntos

| Candidata | (1) antecedente | (2) objeto nuevo | (3) evita la dificultad | (4) identidad global | Veredicto |
|---|---|---|---|---|---|
| Log-concavidad en punto base | R5-a, M1 | ninguno | no | — | repetición |
| Camino s + εF de log ζ | R5-e; Lema A aquí | Lema A (afinidad en c) | no | — | NO-GO en la clase |
| Prékopa/marginalización | Lema K, W2 ronda 13 | Prop. B / Cor. B′ (reducción) | sólo si V no cuadrática y convexa sólo para Λ | a_T = E[Schur] + G | sin objeto |
| Índice/Cayley/ξ | BARRIER_W_001 W1, ES-18, #101 | ninguno | no (circular) | — | repetición |
| Flujo espectral en c | BARRIER_W_001 W2 | ninguno | no | — | repetición |
| det(1 − cK), ciclos | R186_034 Thm 3.1, R186_045 §3.2 | lectura de cadenas como casi-coincidencias | no (cota, no signo) | ∃k: m_k < 1 | repetición (W-det) |

Ninguna candidata pasa. No se construye nada más.

## 4. Siguiente operación explícita (OPEN)

Escribir V(x,F) con x ∈ ℝ^{𝒫} indexado por potencias de primo de la ventana, no cuadrática en x, tal que el bloque
mixto V_Fx acople la coordenada x_m con la x_n sólo cuando |log(m/(kn))| es pequeño, y tal que la convexidad conjunta
en cada x se reduzca a una desigualdad finita que use una relación aditiva exacta (n+1 coprimo con n, 4 = 1+3) y
falle en c = 2, en el borrado y en Beurling. Primera prueba: T = ½ log 5, contactos 2, 3, 4, con el resto G de la
Prop. B explícito. Si V resulta cuadrática en x, la candidata cae en W2 de la ronda 13 y se detiene.

## 5. Etiquetas

| # | Enunciado | Etiqueta |
|---|---|---|
| 1 | Lema A (afinidad en c del hessiano por cualquier camino de log ζ) | PROVED |
| 2 | Prop. B (fórmula de Brascamp–Lieb para −D² log Z) | PROVED mod. CITED |
| 3 | Cor. B′ (reducción de Prékopa a Schur + resto ciego) | PROVED en la clase declarada |
| 4 | Lema C (índice = diferencia de n₋) | PROVED (dim. finita) / ARGUED (formas) |
| 5 | Lectura de tr K^k como cadenas cerradas y escala 2^k del control | ARGUED |
| 6 | O14 y O-odd con objeto escrito | OPEN |

Para el revisor: rederivar el Lema A, la Prop. B (en particular G ⪰ 0 componente a componente) y la identificación
m_k^{(c)} = c^k m_k (K_T es lineal en el peso debajo del umbral arquimediano).
