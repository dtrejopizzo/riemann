# Ronda 1 B — Candidata K2: pivotes de Schur a lo largo de un anidamiento multiplicativo de los enteros (memo de selección)

Objetivo (★): λ_A(T) ≥ 0 para todo T, en la forma reducida «𝖡 definida positiva en ℝ» (P47 thm:oneprofile) o
«𝔸_M ⪰ 0 para todo M» (P47 prop:AM). Notación de `../phase-211-sign-sandbox/STATEMENT_001.md` §2: perfil fijo F_0,
c_0 = c_{F_0}, soporte de c_0 en [−2T_0, 2T_0], 2T_0 < log 2, β := 𝖡(0) = 𝔞(F_0).
Para S ⊂ ℕ finito, 𝔸_S := [𝖡(log m − log k)]_{m,k∈S}; e_d := traslado de F_0 por d, de modo que
s^⊤𝔸_S s = 𝔞(Σ_{k∈S} s_k e_{log k}). Para n ∉ S,

    π(S; n) := inf_{s ∈ ℝ^S} 𝔞(e_{log n} − Σ_{k∈S} s_k e_{log k}),

que es el pivote (complemento de Schur escalar) β − b^⊤𝔸_S^{−1}b, b = (𝖡(log n − log k))_{k∈S}, cuando 𝔸_S ≻ 0.
Etiquetas: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMÉRICO.

## 0. Cotejo

**(1) Antecedente más cercano.**
- 211/LEDGER C6 y STATE_001 punto 4 (líneas 213–214): «transporte M → M+1; primer lema: fórmula exacta de
  𝔸_{M+1} ⪰ 0 dado 𝔸_M ≻ 0 como complemento de Schur escalar en la fila nueva». NOT STARTED. Es la candidata K2 en el
  orden natural de los enteros; K2 sólo cambia el orden de adjunción.
- P47 subsec:KEP (thm:KEP1, KEP2, KEPdich) y GRID §6 ítem 27 «KEP: parametrización de Nevanlinna de 𝔖(T)» (celda 7F,
  OPEN-RESIDUE, «nunca escrita»; el propio P47 anota que la parametrización presupone una solución conocida). Es el mismo
  problema de extensión con anidamiento por longitud de ventana.
- 211/LEDGER C7 (ruta N de la fase 160, R160_X_C1 §0.1; fase 35 doc. 99): mecanismo de rigidez sobre aproximantes cuya
  objeción registrada es que el contenido pasa al límite.
- 211/ROUND_025_B (C49): factorización local de (ab)^{−1/2} y test de producto de Schur, NO-GO PROVED; el peso del peine
  es aditivo sobre los primos (una derivación del producto local).
- 211/ROUND_003_B (C9): acoplamiento de Schur de las dos métricas; la dominancia diagonal ponderada se reduce a
  Σ_{n|m}Λ(n) = log m usada linealmente.
- Fase 188, L2_BUILD_028–031: 𝔸_M = Arch − Div − Near; la multiplicatividad diagonaliza sólo Div; Near es el resto de
  resolución finita de |P_s|²·V; familias restringidas equivalentes al objetivo (reformulación).
- Fase 200, A_MU_FACTORIZATION_001 §1(b) (IDX README l. 520): «Cholesky de la matriz agrupada», NO-GO (base fija, depende
  de Λ sólo a través de la forma; existe igual para a_P y cΛ). §1(f) de la misma memo y 211/LEDGER C33b: el peine
  colapsado por Λ∗1 = log como derivada de una norma.
- Fase 204, L2_INTERLACE_001 (IDX README l. 594): entrelazamiento para S_{T,k} NO-GO porque k → k+1 no anida y no hay
  borde de rango uno.
- W-det (P47 thm:wh-detinherit): todo determinante que decide hereda el margen.
- 211/POWER_FIXED_BLOCK_ASSEMBLY_OBSTRUCTION: excluye sumas de bloques PSD de soporte acotado; deja fuera
  expresamente los complementos de Schur y los bloques de tamaño creciente.
- Memoria de selecciones rechazadas (las reglas del proyecto), «Transporte por desplazamiento y congruencia»: un transporte no
  diagonal sin coeficientes explícitos independientes de invertir o factorizar la propia matriz no habilita construcción.

**(2) Objeto o afirmación nuevos.** Lo único no registrado textualmente es la pregunta: ¿existe una cadena
S_1 ⊂ S_2 ⊂ … ordenada por la estructura multiplicativa (conjuntos cerrados por divisores, números suaves, un primo
cada vez) para la cual π(S_j; n_{j+1}) tenga una expresión cerrada, no lineal en Λ, que sea un cuadrado o un cociente
de cantidades manifiestamente positivas? Esta memo no encuentra tal expresión. Encuentra en cambio cinco enunciados
estructurales (§§1–6, PROVED, elementales) que explican por qué el cambio de orden no produce mecanismo.

**(3) Por qué el cambio evitaría la dificultad del antecedente.** No la evita. El anidamiento multiplicativo sí da
lo que faltaba en L2_INTERLACE (un borde de rango uno en cada paso), pero el pivote resultante es el valor de la
forma en un vector que se obtiene invirtiendo la propia 𝔸_S (§1), es invariante bajo toda sustitución triangular del
álgebra de incidencia, incluida la que realiza Λ∗1 = log (§3), y está acotado superiormente por una cantidad
arquimediana independiente del peine que tiende a cero (§5).

**(4) Identidad que conectaría con la positividad global.** Sólo la tautológica: para una cadena que agota un
conjunto 𝒮 con log 𝒮 − log 𝒮 denso, «todos los pivotes > 0» implica (★), y (★) implica «todos los pivotes ≥ 0»
(Prop. 1). No hay identidad adicional.

**(5) Línea que se rompe para cΛ y para a_P.** Ninguna de las identidades que se pueden escribir se rompe: las de
§§1, 2, 5, 6 valen para todo peine y la de §3 vale para todo peine con otra unidad en lugar de la serie de
coeficientes 1 (Lema 4). Por OBJECT_SPEC §4, una candidata que no puede escribir (2) y (5) no está lista.

**Veredicto del cotejo: sin mecanismo nuevo.** La candidata coincide con C6 (orden distinto) y con la lectura
matricial del problema de extensión de P47 subsec:KEP; el resto de esta memo no es una construcción sino el registro
de las razones estructurales precisas, para que la pregunta no se relance.

## 1. Pivote = valor de la forma en la innovación; reformulación (PROVED)

**Proposición 1.** Sea 𝒮 = ℕ, o 𝒮 = {p^x q^y : x, y ≥ 0} con p ≠ q primos, y S_1 ⊂ S_2 ⊂ … una cadena con |S_j| = j y
unión 𝒮, S_{j+1} = S_j ∪ {n_{j+1}}.
(a) Si π(S_j; n_{j+1}) > 0 para todo j, entonces 𝖡 es definida positiva en ℝ, es decir (★).
(b) Si (★), entonces π(S; n) ≥ 0 para todo S finito y todo n ∉ S.
(c) Si 𝔸_S ≻ 0, el ínfimo se alcanza en s* = 𝔸_S^{−1}b y π(S; n) = 𝔞(u), u := e_{log n} − Σ_k s*_k e_{log k} ∈ P_T
(con T tal que los traslados caben en I_T). Además In(𝔸_{S∪{n}}) = In(𝔸_S) + In(π(S; n)).

*Demostración.* (a) Por inducción, det 𝔸_{S_{j+1}} = det 𝔸_{S_j}·π(S_j; n_{j+1}) > 0 (𝔸_{S_1} = (β) y β = π(∅; n_1) > 0),
luego todos los menores principales directores son positivos y 𝔸_{S_j} ≻ 0 (criterio de Sylvester). Todo subconjunto
finito de 𝒮 está en algún S_j, así que 𝔸_S ⪰ 0 para todo S ⊂ 𝒮 finito. Para 𝒮 = ℕ esto es (★) por P47 prop:AM(i);
para 𝒮 = {p^x q^y}, por la Prop. 2. (b) e_{log n} − Σ s_k e_{log k} ∈ P_T (P47 lem:transl(i)) y
𝔞 ≥ 0 en P_T. (c) s ↦ 𝔞(e_{log n} − Σ s_k e_{log k}) = β − 2b^⊤s + s^⊤𝔸_S s es un polinomio cuadrático estrictamente
convexo; su mínimo es β − b^⊤𝔸_S^{−1}b en s*. La aditividad de la inercia es la fórmula de Haynsworth para el bloque
(𝔸_S, b; b^⊤, β). ∎

Entre (a) y (b) queda el caso de un pivote nulo, que no se decide por la cadena sola.

**Proposición 2 (bastan los números 3-suaves; PROVED, variante trivial de L2_028 §1 y L2_031 Teorema E).** Sean p ≠ q
primos y 𝒮 = {p^x q^y : x, y ≥ 0}. Entonces (★) ⟺ 𝔸_S ⪰ 0 para todo S ⊂ 𝒮 finito.

*Demostración.* (⟹) restricción. (⟸) Γ := ℤ log p + ℤ log q es denso en ℝ (log p / log q es irracional por
factorización única). Dados a_1, …, a_K y ε > 0 se eligen γ_i = x_i log p + y_i log q ∈ Γ con |γ_i − a_i| < ε, y
X, Y enteros con x_i + X ≥ 0, y_i + Y ≥ 0. Con m_i := p^{x_i+X} q^{y_i+Y} ∈ 𝒮 se tiene log m_i − log m_l = γ_i − γ_l.
Por continuidad de 𝖡, Σ s_i s_l 𝖡(a_i − a_l) = lim_{ε→0} Σ s_i s_l 𝖡(log m_i − log m_l) ≥ 0. ∎

Lectura. Sobre 𝒮 = ⟨2, 3⟩ la parte Div contiene sólo las potencias de 2 y de 3; todos los demás primos entran
exclusivamente por Near. El mismo argumento vale para los puntos αℕ + βℕ con α/β irracional cualquiera, donde
Div = 0 y todo el peine es «Near». La descomposición Div/Near, y con ella cualquier estructura multiplicativa del
conjunto de índices, es una propiedad de los puntos de muestreo y no de 𝖡: la aritmética del problema está en las
posiciones log n de los átomos dentro de la función 𝖡, no en el retículo donde se la evalúa. Esto ya está
registrado como reformulación (IDX README l. 55); no es avance (RULES_AVOID B3).

**Consecuencia para K2.** El pivote es el valor de 𝔞 en el minimizador de un problema restringido (s_n = 1): es
un funcional del minimizador (RULES_AVOID B9, OBJECT_SPEC O8). Su no linealidad en Λ es la de 𝔸_S^{−1}, es decir,
la que se obtiene invirtiendo el propio objeto (memoria de selecciones, «transporte por desplazamiento y
congruencia»). Como det 𝔸_{S_j} = Π_{i≤j} π_i y, si 𝔸_{S∪{n}} ⪰ 0, λ_min(𝔸_{S∪{n}}) ≤ π(S; n)/(1 + |s*|²) ≤ π(S; n),
los pivotes heredan el margen: es W-det en esta base.

## 2. La realización de Gram sobre el portador 𝖡 es única; el orden sólo cambia la triangulación (PROVED)

**Proposición 3.** Sea 𝒟 ⊂ ℝ y r, r′ : 𝒟 → ℋ, ℋ′ con ⟨r(d), r(d′)⟩ = 𝖡(d − d′) = ⟨r′(d), r′(d′)⟩. Entonces hay una
única isometría del cierre de span r(𝒟) sobre el de span r′(𝒟) con r(d) ↦ r′(d). Si además 𝔸_S = R^⊤R + ρ con ρ ⪰ 0,
la aplicación apilada (R; ρ^{1/2}) es una realización con resto nulo.

*Demostración.* ‖Σ s_i r(d_i)‖² = Σ s_i s_l 𝖡(d_i − d_l) = ‖Σ s_i r′(d_i)‖²; la aplicación Σ s_i r(d_i) ↦ Σ s_i r′(d_i)
está bien definida, es isométrica y se extiende al cierre. La segunda afirmación es R^⊤R + ρ^{1/2}ρ^{1/2}. ∎

Lectura. Sobre el portador de un perfil, la identidad (G) de OBJECT_SPEC §1 tiene, si existe, una sola solución
salvo isometría: una curva d ↦ r(d) con ‖r(d) − r(d′)‖² = 2[β − 𝖡(d − d′)]. Los enteros son muestras r(log n) de esa
curva y la factorización de Cholesky a lo largo de una cadena es la ortogonalización de Gram–Schmidt de esas
muestras en el orden de la cadena: π(S; n) = dist²(r(log n), span{r(log k)}_{k∈S}). La curva sólo ve log n ∈ ℝ. Elegir
un orden multiplicativo cambia la base triangular en la que se escribe la misma realización, no la realización.
Un pivote explícito para una cadena equivale a un factor triangular explícito, es decir, a (G) completa en una forma
normal particular: K2 no es una reducción de (G), es (G) con una condición de forma añadida.

## 3. Λ∗1 = log en el álgebra de incidencia: identidad genérica y neutral para los pivotes (PROVED)

Sea 𝒩 ⊂ ℕ finito y cerrado por divisores. Para f aritmética, (C_f)_{mk} := f(m/k) si k | m, 0 si no (m, k ∈ 𝒩).
Como todo d con k | d | m está en 𝒩, C_f C_g = C_{f∗g}. Sea D := diag(log m), z(n) := n^{−1/2}; z es completamente
multiplicativa, luego (fz)∗(gz) = (f∗g)z, y [D, C_f] = C_{f·log} porque log m − log k = log(m/k).

**Lema 4 (el peine como derivada logarítmica; vale para todo peine).** Sea a aritmética con a(1) = 0 y
𝕍_a := 2C_{az} (la parte de coincidencias exactas del peine a en 𝒩, Div_a = ½(𝕍_a + 𝕍_a^⊤)). Sea u la única función
con u(1) = 1 y u·log = u∗a (recurrencia u(n) log n = Σ_{d|n, d>1} a(d) u(n/d)), y U := C_{uz}. Entonces

    𝕍_a = 2 U^{−1}[D, U],        U Div_a U^⊤ = D G + G D − 2 U D U^⊤,   G := U U^⊤ ⪰ 0.

Para a = Λ, u ≡ 1, U = Z := C_z, G_{mk} = (mk)^{−1/2} σ(mcd(m, k)) y

    (Z Div Z^⊤)_{mk} = (mk)^{−1/2} Σ_{d | mcd(m,k)} d·[log(m/d) + log(k/d)].

Para a = cΛ, u = d_c (coeficientes de la potencia c-ésima de convolución de 1); para a_P, u = indicador de los
enteros sin factores primos < P.

*Demostración.* U es triangular con diagonal 1, luego invertible, y U^{−1} = C_{u^{−1}z} con u^{−1} la inversa de
convolución. U^{−1}[D, U] = C_{u^{−1}z} C_{(u log) z} = C_{(u^{−1}∗(u log)) z} = C_{az}. Entonces
U𝕍_aU^⊤ = 2[D, U]U^⊤ = 2(DG − UDU^⊤) y U𝕍_a^⊤U^⊤ = 2U[D, U]^⊤ = 2(GD − UDU^⊤). Para u ≡ 1,
G_{mk} = Σ_{d | (m,k)} (m/d)^{−1/2}(k/d)^{−1/2} y (UDU^⊤)_{mk} = Σ_{d | (m,k)} (mk)^{−1/2} d log d; se resta. ∎

La identidad Σ_{d|n}Λ(d) = log n es exactamente «u ≡ 1». La forma de la identidad (peine = U^{−1}[D, U]) es
válida para todo peine (RULES_AVOID B1). La versión con u ≡ 1 es la forma sin primos ya registrada: 211/LEDGER C33b,
ROUND_025_B Teorema 1.1/2.1 (pesos (NN′)^{−1/2} log(NN′)), fase 200 A_MU_FACTORIZATION §1(f). Aquí queda escrita en
coordenadas matriciales, sobre coincidencias exactas; no es resultado nuevo.

**Proposición 5 (neutralidad).** Sea S_1 ⊂ … ⊂ S_J = 𝒩 una cadena de conjuntos cerrados por divisores, |S_j| = j, y L
cualquier matriz triangular inferior con diagonal 1 en el orden de la cadena (en particular toda C_f con f(1) = 1).
Entonces, para toda matriz simétrica 𝔸 indexada por 𝒩, los menores principales directores de L𝔸L^⊤ y de 𝔸 a lo
largo de la cadena coinciden; si son no nulos, los pivotes coinciden. Recíprocamente, dos matrices simétricas con
menores directores no nulos tienen los mismos pivotes si y sólo si son congruentes por una tal L.

*Demostración.* Si k | m entonces k precede a m en la cadena, así que C_f es triangular inferior en ese orden. Para
L triangular unitaria, (L𝔸L^⊤)[S_j] = L[S_j] 𝔸[S_j] L[S_j]^⊤ y det L[S_j] = 1. El recíproco es la unicidad de la
factorización 𝔸 = L_0 diag(π) L_0^⊤. ∎

Lectura. Pasar de la forma con Λ a la forma sin primos es la congruencia por Z (Lema 4), que actúa sobre toda
𝔸_𝒩 = Arch − Div − Near. Por la Prop. 5 no cambia ningún pivote de ninguna cadena cerrada por divisores. Los
pivotes son precisamente los invariantes de la acción del grupo unipotente del álgebra de incidencia; la identidad
Λ∗1 = log, usada como sustitución triangular, vive dentro de ese grupo. Por tanto **no existe una «fórmula del
pivote obtenida por Λ∗1 = log»** en esta clase: la identidad cambia la representación de 𝔸 y deja el pivote igual.
Para que la integralidad afecte al signo de un pivote tendría que entrar por una operación que no sea una
congruencia triangular en el orden de divisibilidad. Ninguna está identificada.

## 4. El único mecanismo conocido de pivotes exactos por Σ_{d|n} g(d) = f(n), y por qué 𝔸 no lo tiene

**Proposición 6 (paradigma de mcd; CITED, clásico, demostración de una línea).** Sobre 𝒩 cerrado por divisores,
[f(mcd(m, k))] = E diag(g) E^⊤ con E_{md} = 1_{d|m} y g = f∗μ; los pivotes a lo largo de toda cadena cerrada por
divisores son g(n). Con f = log: [log mcd(m, k)] = E diag(Λ) E^⊤ ⪰ 0, con pivotes Λ(n) ≥ 0.
*Demostración.* Σ_{d | m, d | k} g(d) = Σ_{d | mcd} g(d) = f(mcd). ∎

Éste es el caso en que Σ_{d|n}Λ(d) = log n da pivotes exactos y no negativos. No sirve como paso de signo: vale
igual para cΛ (c > 0) y para todo g ≥ 0, es homogéneo (OBJECT_SPEC O10) y no contiene el factor arquimediano.

**Condición necesaria para que 𝔸 tenga un factor triangular con el patrón de incidencia (PROVED).** Si
𝔸_𝒩 = L diag(π) L^⊤ con L_{md} ≠ 0 sólo para d | m, entonces para m, k coprimos
𝔸_{mk} = L_{m1} π_1 L_{k1}, es decir

    β·𝖡(log m − log k) = 𝖡(log m)·𝖡(log k)      para todo par coprimo m, k ∈ 𝒩.        (4.1)

*Demostración.* 𝔸_{mk} = Σ_{d | m, d | k} L_{md} π_d L_{kd}; si mcd = 1 queda d = 1, π_1 = β, L_{m1} = 𝖡(log m)/β. ∎

(4.1) falla (NUMÉRICO, con los valores de validación de STATEMENT_001 §3, perfil a = 0.15, b = 1: β = 0.01492 y
|𝖡(d)| ≤ 0.0122 para 0 < d ≤ 13): para m = k + 1 con k grande dentro de ese rango, el lado izquierdo es
β² − O(β κ_0/k²) por la Prop. 7 y el derecho es ≤ 0.0122² < β². No se ha hecho ningún cómputo nuevo; κ_0 no se
ha evaluado, y esta observación no sostiene ninguna otra afirmación de la memo. La razón estructural, sin números: en un patrón de
incidencia las columnas de dos enteros coprimos comparten sólo la coordenada del 1, mientras que en la realización
de la Prop. 3 las columnas de k y k + 1 son casi paralelas (§5). Lo mismo excluye cualquier patrón ralo fijado por
la divisibilidad; es el fenómeno C_{ij} → 1 de 211/POWER_FIXED_BLOCK_ASSEMBLY §3 en esta base.

## 5. Colapso de los pivotes: cota superior arquimediana, independiente del peine (PROVED)

**Proposición 7.** Sea κ_0 := (1/2π)∫ |m(τ)| τ² F̂_0(τ)² dτ (finito: F̂_0(τ) = O(τ^{−2}), m(τ) = O(log(2 + |τ|))).
Para todo S finito, n ∉ S y k ∈ S,

    π(S; n) ≤ 2[β − 𝖡(log n − log k)].

Si d := |log n − log k| < log 2 − 2T_0, el lado derecho es (1/π)∫ m F̂_0² (1 − cos τd) dτ, no contiene el peine, y
|2[β − 𝖡(d)]| ≤ κ_0 d². En particular, en el orden natural π({1, …, n−1}; n) ≤ κ_0/(n−1)² para n ≥ n_0(T_0), y
si 𝔸_{[1,n]} ⪰ 0 entonces λ_min(𝔸_{[1,n]}) ≤ κ_0/(n−1)².

*Demostración.* Tomar s = (vector canónico de k) en el ínfimo: 𝔞(e_{log n} − e_{log k}) = 2β − 2𝖡(log n − log k). Para
|d| < log 2 − 2T_0 y n′ ≥ 2, log n′ ± d > 2T_0, luego c_0(log n′ ± d) = 0 y la parte de peine de 𝖡(d) es nula;
también lo es la de 𝖡(0). Queda la parte arquimediana y 1 − cos x ≤ x²/2. En el orden natural d = log(n/(n−1)) ≤
1/(n−1). La cota de λ_min es la del final de §1. ∎

Lectura. Para toda cadena cuyos puntos se acumulan en escala logarítmica (toda cadena en ℕ, y toda cadena en los
números P-suaves con al menos dos primos) los pivotes tienden a cero, con una cota que es la misma para Λ, cΛ,
a_P, borrados y amplificaciones finitos y cualquier peine soportado en log ℕ_{≥2}. Un pivote escrito como «cociente
de cantidades manifiestamente positivas» tendría que tener un numerador que se anule al menos a segundo orden en la
distancia al punto anterior más cercano, por una razón puramente geométrica (la no ortogonalidad de traslados
vecinos de F_0); el peine sólo interviene en el signo de una cantidad ya acotada por κ_0 d². La recursión de pivotes no
tiene margen uniforme en ningún paso tardío y su objeto límite (pivote tras infinitos pasos) es cero. Ésta es la
forma que toma aquí la objeción registrada en C7: el contenido de «pivote ≥ 0 en cada paso» queda en el signo de
cantidades que se anulan, no en una cota en un paso fijo. No es un NO-GO (una identidad exacta podría firmar una
cantidad que tiende a cero); es una restricción de diseño que la candidata no resuelve.

## 6. Donde Near es invisible: suma de Kronecker, no producto (PROVED)

En cajas multiplicativas sin casi-coincidencias visibles la parte de peine es una suma de Kronecker de matrices
de Toeplitz locales (P47 rem:boxes, L2_029 §2). La factorización de Cholesky respeta productos tensoriales, no sumas:

**Proposición 8.** Sea A = A_1 ⊗ I + I ⊗ A_2 con A_2 = (A_2′, b; b^⊤, α) simétrica de orden K + 1. El complemento de
Schur de la última capa (índice K + 1 del segundo factor) es σ(A_1), con σ(x) := α + x − b^⊤(A_2′ + x)^{−1}b
= det(A_2 + x)/det(A_2′ + x), siempre que A_2′ + λ sea invertible para cada autovalor λ de A_1.

*Demostración.* Diagonalizar A_1 = QΛQ^⊤; A es suma directa sobre los autovalores λ_i de las matrices A_2 + λ_i, y
el complemento de Schur de cada una es σ(λ_i). ∎

Así, incluso en el modelo sin Near, el pivote al adjuntar una potencia de un primo no es un producto de pivotes
locales sino una función racional de la matriz de los otros primos, y su positividad es la aditividad de los
espectros, que es el contenido de rem:boxes y de prop:nearfree (cotas locales contra energía arquimediana, con
holgura). Es la versión, para factorizaciones triangulares, de la razón de C49: el peso del peine es aditivo sobre
los primos y un producto (de Schur allí, tensorial aquí) no tiene lugar para él. Con el perfil fijo F_0 las
casi-coincidencias aparecen en toda caja suficientemente grande, de modo que este modelo no describe 𝔸.

## 7. Los anidamientos multiplicativos posibles y respuesta a cada antecedente

Hay tres maneras de anidar «un primo o un entero cada vez».

(I) **Anidar el conjunto de índices** (submatrices principales de la misma 𝖡). Es lo analizado en §§1–6:
reformulación (Prop. 1–2), pivote = funcional del minimizador, neutral frente a Λ∗1 = log (Prop. 5), sin patrón de
incidencia (§4), sin margen (Prop. 7). Near entra en el pivote de forma exacta, pero trivialmente: está en cada
entrada de b y de 𝔸_S, y la fórmula que lo contiene es β − b^⊤𝔸_S^{−1}b.

(II) **Anidar el peine** (adjuntar los átomos de un primo a los pesos, con 𝖡 cambiando en cada paso). Los objetos
intermedios no son semidefinidos positivos: el extremo «faltan primos pequeños» es el falsificador a_P, y para el
otro extremo 211/ROUND_025_B §4 registra (NUMÉRICO) que toda suma parcial por soporte primo es negativa de orden 1
y que la positividad aparece sólo con el conjunto completo. No hay recursión de pivotes positivos que pase por
objetos indefinidos; cada paso resta una matriz de símbolo v_{p^j} cos(τ j log p) F̂_0², sin signo.

(III) **Anidar ambos a la vez** (índices y peine P-suaves). Es la cadena semilocal sobre conjuntos finitos de
lugares, registrada como cerrada sin signo (RULES_AVOID §C, «Sonin, prolatos, semilocal»; IDX fases 183–186). No se
reabre.

Respuestas.
- **C7 / «muere en el límite».** La ruta N aplicaba rigidez a un estado en ventana finita. K2 no usa rigidez;
  su análogo de la objeción es la Prop. 7: los pivotes no tienen margen uniforme y el pivote límite es nulo para todo
  peine. La objeción no queda respondida, queda localizada.
- **P47 subsec:KEP y GRID 7F.** La versión matricial de la parametrización es: dado 𝔸_S ≻ 0, las filas admisibles b
  forman el elipsoide b^⊤𝔸_S^{−1}b ≤ β y el parámetro de Schur es 𝔸_S^{−1/2}b/√β. Presupone 𝔸_S ≻ 0 y su inversa,
  igual que la parametrización continua presupone una solución. Cambiar longitud de ventana por orden multiplicativo
  no altera esa dependencia (Prop. 3: es la misma realización triangulada en otro orden). El residuo 7F sigue como
  está: sin escribir y sin valor para el signo.
- **C49.** §6 es su análogo para factorizaciones triangulares; mismo motivo (aditividad sobre primos).
- **C9.** Allí Σ_{n|m}Λ(n) = log m entra como suma de fila (test de Schur con pesos k^{−1/2}), uso lineal y con
  holgura. En un pivote la fila de Div se empareja con 𝔸_S^{−1}b, no con k^{−1/2}; el único uso exacto de la
  identidad es la congruencia por Z, neutral (Prop. 5).
- **L2_028–031.** Prop. 2 es otra familia restringida equivalente al objetivo; misma etiqueta («reformulación o
  trivial»).
- **POWER_FIXED_BLOCK_ASSEMBLY.** Las columnas de Cholesky tienen soporte creciente, así que K2 no cae en la clase
  excluida allí; la obstrucción de esa memo reaparece sólo como §4 (ningún patrón ralo fijo).
- **Fase 204, Cholesky agrupado y entrelazamiento.** El NO-GO de Cholesky agrupado se aplica tal cual: la base
  triangular depende de Λ sólo a través de la forma y existe igual para cΛ y a_P mientras los menores no se anulen.
  El obstáculo de L2_INTERLACE (no hay borde de rango uno) no se aplica a K2, que sí lo tiene; lo que se obtiene con
  él es la fórmula de inercia de la Prop. 1(c), sin contenido de signo.
- **W-det.** Confirmado en esta base: det 𝔸_{S_j} = Π π_i y π ≥ λ_min (§1, §5).

## 8. Falsificadores

No se da ningún paso de signo. Para cada enunciado, el comportamiento bajo la batería:
- Prop. 1, 2, 3, 8 y la condición (4.1): válidas para todo peine con la misma estructura (cΛ, a_P, borrado y
  amplificación finitos, b_θ, sistemas de Beurling discretos con el retículo de sus enteros generalizados, y los
  modelos sin producto de Euler). Son reformulaciones o álgebra lineal; no distinguen nada.
- Lema 4: la forma de la identidad vale para todo peine con otra unidad u; con u ≡ 1 vale sólo para Λ (para cΛ,
  u = d_c; para a_P, u es el indicador de los enteros P-rugosos; para borrados, amplificaciones y b_θ la
  recurrencia da otra u ≢ 1). Pero la Prop. 5 muestra que esa diferencia no llega a ningún pivote. Para los modelos
  cuyo peine no está soportado en log ℕ con esta estructura (Epstein, Davenport–Heilbronn, Beurling) el lema se
  aplica en el retículo de índices correspondiente o no se aplica; no se ha examinado caso por caso.
- Prop. 7: la cota es idéntica para todos los falsificadores con átomos en log ℕ_{≥2}; para un sistema de Beurling
  con primer entero generalizado g_1 > 1 vale con log g_1 en lugar de log 2.
- Cuartetos y f_t: conservan Λ(n) y por tanto toda afirmación de esta memo que dependa sólo del peine; ninguna
  afirmación aquí los separa.
Si alguna de estas proposiciones se presentara como paso de signo sobreviviría a todos los falsificadores y estaría
mal por la regla 6 del brief. Ninguna se presenta así.

## Resultado

**Sin mecanismo nuevo.** La candidata K2 no está lista para construcción: no puede escribir el objeto (factor
triangular explícito) ni la línea que se rompe para cΛ y a_P. No se declara un NO-GO de clase: no se ha probado que
ningún factor triangular explícito pueda existir; se ha probado que las tres fuentes de explicitud disponibles
(sustitución por Λ∗1 = log, patrón de incidencia, producto sobre primos) no lo producen.

## Qué se probó

- Prop. 1: pivotes a lo largo de una cadena que agota ⟺ objetivo (con la salvedad > / ≥); pivote = 𝔞 en la
  innovación; inercia aditiva. PROVED, reformulación.
- Prop. 2: bastan los índices {p^x q^y}; la partición Div/Near depende de los puntos de muestreo. PROVED, reformulación.
- Prop. 3: unicidad salvo isometría de la realización de Gram sobre el portador 𝖡; una cadena sólo elige el orden de
  ortogonalización. PROVED.
- Lema 4: Div_a = sim(U^{−1}[D, U]) para todo peine; para Λ, Z Div Z^⊤ = DG + GD − 2ZDZ^⊤ con
  G = [(mk)^{−1/2}σ(mcd)]. PROVED; coincide con la forma sin primos ya registrada.
- Prop. 5: los pivotes de cadenas cerradas por divisores son invariantes bajo congruencias triangulares del álgebra
  de incidencia; Λ∗1 = log usada como sustitución es neutral. PROVED.
- Prop. 6 y (4.1): el paradigma de mcd da pivotes Λ(n) para [log mcd]; para 𝔸 exigiría rango uno sobre pares
  coprimos. PROVED la condición; su fallo NUMÉRICO.
- Prop. 7: π(S; n) ≤ 2[β − 𝖡(log n/k)] ≤ κ_0 log²(n/k) para puntos cercanos, sin peine. PROVED.
- Prop. 8: complemento de Schur de una suma de Kronecker = función de la matriz del otro factor. PROVED.

## Qué falló y por qué

- No hay fórmula cerrada del pivote. La dependencia no lineal de Λ en π(S; n) es la de 𝔸_S^{−1}; toda expresión
  explícita equivale a un factor triangular explícito, es decir, a la identidad (G) entera (Prop. 3).
- Σ_{d|n}Λ(d) = log n no produce una identidad de pivotes: como sustitución triangular es neutral (Prop. 5) y como
  suma de fila es lineal y con holgura (C9, prop:nearfree).
- Adjuntar n a un conjunto cerrado por divisores cambia el complemento de Schur en 𝔞(u), con u la innovación en
  P_T: el signo del término nuevo es el objetivo evaluado en un vector que depende de la propia forma (B9).
- La estructura sobre primos es aditiva (suma de Kronecker, derivación), no multiplicativa; Near no es un operador
  aparte sino el defecto de ortogonalidad de los traslados (L2_030 §2), y entra en todas las entradas.
- Los pivotes tardíos no tienen margen y su cota superior es ajena al peine (Prop. 7).

## Siguiente paso concreto

Ninguno dentro de K2. Para el registro (a cargo de quien mantiene los archivos; esta memo no edita otros):
línea de LEDGER de la fase 212 «K2: pivotes por anidamiento multiplicativo — sin mecanismo nuevo; Prop. 5 y 7
como herramientas»; cerrar 211/C6 con la misma referencia; nota en IDX (familia «matrices de retículo entero y
conjuntos multiplicativos») y en GRID 7F: «la variante matricial con orden multiplicativo es la misma realización
(Prop. 3); pivotes invariantes bajo el grupo unipotente de incidencia (Prop. 5)».
Condición de reapertura: una operación explícita, que no sea una congruencia triangular en el orden de
divisibilidad ni requiera invertir 𝔸_S, por la cual u ≡ 1 (Lema 4) entre en el pivote junto con el núcleo
arquimediano, y cuyo numerador se anule al orden exigido por la Prop. 7. No se conoce ninguna.
