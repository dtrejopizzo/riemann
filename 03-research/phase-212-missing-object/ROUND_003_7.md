# Ronda 3, opción 7 — La formulación (S): incidencia de divisores sobre 𝔸_M (memo de selección)

Objetivo (★): λ_A(T) ≥ 0 para todo T, con las definiciones de `../phase-211-sign-sandbox/STATEMENT_001.md`.
Reducción usada (PROVED, P47 prop:AM): con un perfil fijo F_0 ∈ P_{T_0}, 2T_0 < log 2, (★) equivale a
𝔸_M = [𝖡(log m − log k)]_{m,k≤M} = Arch_M − Div_M − Near_M ⪰ 0 para todo M. Notación de P47 §subsec:oneprofile:
β(d) := (1/2π)∫ m F̂_0² cos(τd) dτ (parte arquimediana de 𝖡), v_n = 2Λ(n)n^{−1/2}, c_0 = c_{F_0}, sop c_0 ⊂ [−2T_0, 2T_0].
Etiquetas: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMÉRICO.

## Cotejo

### Qué se buscó y dónde

Grep en `03-research/` (todas las fases), `04-papers/47` y `48`, grid, crucigrama, índice (README y 06) y anexos de la
fase 212 por: Arch_M, Div_M, Near_M, 𝔸_M, mathbb A_M, prop:AM, «Arch_M − Div_M», GCD/mcd, Smith, meet matrix,
incidencia, Möbius, LDL, Cholesky, Schur, «rango uno», coprimo, «site independence». Abiertos en primaria:
P47 prop:AM con demostración, thm:oneprofile, prop:nearfree, rem:boxes, rem:bar-arith, problema (S) de §sec:open;
fase 188 `N_BUILD_022` (completo), `L2_BUILD_031` (completo), `L2_BUILD_028` §§1–4; fase 193
`CA_K_001` §1 (Lema 1.1, Teor. 1.2, Prop. 1.3), `CA_K_002` §3 (Teor. 3.2) y `CA_K_001_002_REVIEW`; fase 200
`A_MU_FACTORIZATION_001` §§0–1(b); 211 `ROUND_003_B` (encabezados y §§2–5), 211 LEDGER C7, C9, C43; índice 06 §R9;
`RULES_AVOID.md` I1–I3 y §E; esta fase `ROUND_001_B` §4 (Prop. 6, condición (4.1)), `REVIEW_001_ABD` E-B4,
`ROUND_003_2`. No abrí en primaria la fase 205 (Toeplitz−Hankel), la 206 ni las coincidencias de las fases 120 y 162
por «Smith»/«GCD» (por títulos: polarización global y átomos de torsión, no 𝔸_M); queda como límite del cotejo. Una
búsqueda sin coincidencias no prueba novedad.

### Respuesta del corpus a las preguntas (i)–(iv) del encargo

(i) **Arch_M − Div_M no es ⪰ 0** para M grande: ya PROVED en el corpus. `CA_K_001` Prop. 1.3(a): β no es definida
positiva (su densidad de Bochner m F̂_0²/2π es negativa cerca de 0 porque m(0) = C_0 = −5.37… < 0), luego Arch_M es
indefinida para M ≥ M_1. `CA_K_002` Teor. 3.2 (independencia de sitio): (★) equivale a 𝔸_M restringida a primos ⪰ 0
para todo M; allí Div ≡ 0, y Cor. 3.3(ii) da Arch − Div indefinida sobre sitios primos. Además Div_M no es una
matriz de tipo f(mcd): es la convolución de Dirichlet por v (unitriangular a un lado), con la identidad exacta
Δ = Z⁻¹LZ − L (`N_BUILD_022` §1; = R162_903 B2.1). La factorización de Smith [log mcd] = E diag(Λ) Eᵀ existe y es
⪰ 0 (`ROUND_001_B` Prop. 6), pero es homogénea en el peso y no contiene el factor arquimediano.

(ii) **Near como −(cuadrado) + absorbible / 𝔸_M = WᵀDW con W unitriangular en la divisibilidad.** Antecedentes:
`N_BUILD_022` §3 (NO-GO PROVED: ninguna identidad matricial exacta derivada de 1∗Λ = log alcanza Near; Near es
el defecto de discretización); `L2_BUILD_030` §2 en el índice (Near como operador firmado separado: NO-GO);
`ROUND_001_B` (4.1): un factor con patrón de incidencia exige rango uno sobre pares coprimos, con fallo sólo
NUMÉRICO; `ROUND_003_2` Lema 2 (LDL con D ≥ 0 sii 𝔸 ⪰ 0: circular); fase 200 §1(b) (Cholesky agrupado, inercia
mixta, C8). Lo nuevo de esta memo es el Lema 1: el fallo de (4.1) pasa de NUMÉRICO a PROVED, y con más alcance
(cualquier D diagonal, cualquier signo, sin pasar por la fila del 1).

(iii) **Dónde entra la ecuación funcional en (S).** Sólo en dos lugares: el símbolo m(τ) = Re ψ(¼ + iτ/2) − log π
de Arch_M (factor Γ(s/2)π^{−s/2}, conductor 1) y las condiciones de Tate F̂_0(±i/2) = 0, que anulan exactamente el
término principal de Ξ_{F_0} (P47 thm:band, lem:transl(iii)). Las entradas de Div_M y Near_M no la contienen; en
(S) la ecuación funcional entra aditivamente, en el término arquimediano, y ningún antecedente leído escribe una
identidad exacta que ligue entradas de Near_M con entradas de Arch_M (las identidades de Poisson de P47
thm:PCfinite, ya examinadas en K1, son genéricas en el peine). ARGUED.

(iv) Ver §(5) abajo.

### (1) Antecedente más cercano

`ROUND_001_B` §4 (Prop. 6 y condición (4.1)), con su revisión `REVIEW_001_ABD` E-B4; `N_BUILD_022` §§1–3; `CA_K_001`
Prop. 1.3 y `CA_K_002` Teor. 3.2. La candidata del encargo («𝔸_M = WᵀDW, W unitriangular en el orden de
divisibilidad, pivotes funciones explícitas de Λ del tipo Σ_{d|n}Λ(d) = log n») es la de `ROUND_001_B` §4 sobre la
formulación (S): **repetición**, salvo por lo que el Lema 1 decide.

### (2) Objeto realmente nuevo

No hay ℋ, V, ρ nuevos. Lo nuevo son tres piezas cortas, demostradas abajo:

- **Lema 1 (NO-GO de formato, PROVED).** Existe M_0 tal que para todo M ≥ M_0 la matriz 𝔸_M no admite ninguna
  factorización exacta 𝔸_M = WᵀDW con D diagonal real (de cualquier signo) y W_{dk} = 0 salvo d | k. La exclusión
  vale para todo peine soportado en [log 2, ∞) (no usa Λ): es de formato, no de signo.
- **Lema 2 (PROVED, álgebra).** Para cualquier W de ese patrón, (WᵀDW) restringida a los primos ≤ M es
  D_1 wwᵀ + diag(D_p) (rango uno más diagonal). Como la restricción a primos ya es equivalente a (★)
  (`CA_K_002` Teor. 3.2), una identidad 𝔸_M = WᵀDW + ρ deja todo el signo de la reducción equivalente en ρ.
- **Corolario 3 (PROVED, a partir de `ROUND_003_2` Lema 3 y `CA_K_001` Prop. 1.3(a)).** La clase afín emparejada
  sobre (S) también es NO-GO: el caso (iii) que `ROUND_003_2` dejó abierto queda cerrado para M ≥ M_1.

Lo que falta escribir para tener candidata: una W **no** soportada en la divisibilidad (que vea pares coprimos casi
proporcionales m ≈ kn), con fórmula propia no derivada de 𝔸_M, y un ρ con signo manifiesto. No sé escribirla.

### (3) Por qué el cambio evitaría la dificultad del antecedente

No la evita: confirma y prueba la dificultad. La razón estructural, ahora PROVED (Lema 1): en un patrón de incidencia
las columnas de enteros coprimos comparten sólo la coordenada del 1, mientras que 𝖡 es continua en el retardo real,
de modo que primos con cocientes casi iguales tienen columnas casi paralelas. Ningún pivote, por explícito que sea
(log n, Λ(n), f∗μ), repara eso.

### (4) Identidad que conectaría con la positividad global

Ninguna en la clase de divisibilidad (Lema 1). Con resto, sólo 𝔸_M[𝒫] = D_1wwᵀ + diag(D_p) + ρ[𝒫] (Lema 2), donde
probar ρ[𝒫] ⪰ 0 es tan fuerte como (★) por la independencia de sitio: la incidencia no aporta nada en la reducción
equivalente salvo un rango uno y una diagonal.

### (5) Línea que se rompe para cΛ y a_P

- Lema 1: no se rompe para ningún peine: es una imposibilidad de formato. Por eso no es mecanismo.
- Corolario 3: la línea «ρ = Arch_M − V_0ᵀV_0 − V_1ᵀV_1 ⪰ 0» falla ya para Λ; para cΛ el resto es
  ρ^{(c)} = ρ^{(0)} − c²V_1ᵀV_1, par y no creciente en |c|, sin ruptura en c < 1.
- Observación de localidad (PROVED, de P47 prop:AM(ii)): las entradas de 𝔸_M dependen del peso sólo a través de
  a(n), n < M e^{2T_0}. Luego, para un falsificador que conserva a(n) = Λ(n) para n < X (por ejemplo la
  deformación f_t con X = λ₁), toda identidad sobre la familia {𝔸_M} sólo puede romperse en M ≥ X e^{−2T_0}: la
  línea que se rompe tiene que usarse para todo M grande (O5). Para a_P
  (potencias de primos p < P borradas) Div_M ya cambia en M = 2: la ruptura en (S) sería visible en M chico, pero
  ninguna identidad de esta memo la usa.

### Veredicto del cotejo

Repetición de `ROUND_001_B` §4 en la formulación (S), con (i) ya resuelto por `CA_K_001`/`CA_K_002` y (ii) por
`N_BUILD_022` §3 y `ROUND_003_2` Lema 2. Se añade el Lema 1 (cierra con clase, en forma PROVED, la factorización por
incidencia de divisores) y el Corolario 3. Sin candidata lista para construcción.

## 1. Demostraciones

### Lema 1 (no hay factorización en el orden de divisibilidad; PROVED)

*Enunciado.* Sea F_0 el perfil de P47 §subsec:oneprofile con 2T_0 < log 2 y sea a cualquier peso real con peine
soportado en {log n : n ≥ 2} (en particular Λ, cΛ, a_P, borrados, amplificaciones). Sea 𝖡_a la función de un perfil
correspondiente y 𝔸_M = [𝖡_a(log m − log k)]. Existe M_0 tal que, para M ≥ M_0, no existen D = diag(D_1, …, D_M)
real y W real M×M con W_{dk} = 0 salvo d | k, tales que 𝔸_M = WᵀDW.

*Demostración.* Paso 1 (rango uno en primos). Si 𝔸_M = WᵀDW, entonces (𝔸_M)_{mk} = Σ_{d | m, d | k} D_d W_{dm}W_{dk}.
Para primos distintos p, q ≤ M el único divisor común es d = 1, luego (𝔸_M)_{pq} = D_1 W_{1p}W_{1q}. Para cuatro
primos distintos p, p′, q, q′ ≤ M:

    𝖡_a(log p − log q) 𝖡_a(log p′ − log q′) = 𝖡_a(log p − log q′) 𝖡_a(log p′ − log q).        (1.1)

Paso 2 (paso al continuo). Las entradas de 𝔸_M no dependen de M; si la factorización existiera para infinitos M,
(1.1) valdría para toda cuaterna de primos distintos. Dados reales x, x′, y, y′ distintos dos a dos y C > 0, por el
teorema de los números primos (CITED: p_{n+1}/p_n → 1) hay primos distintos con |log p − C − x| < ε, etc., para C
grande; las diferencias de logaritmos tienden a x − y, etc. Como 𝖡_a es continua (P47 thm:oneprofile, enunciado),
(1.1) vale para todas las cuaternas reales distintas dos a dos, y por continuidad para todas. Tomando y′ = x, x′ = y:
𝖡_a(x − y)𝖡_a(y − x) = 𝖡_a(0)², y por paridad 𝖡_a(d)² = 𝖡_a(0)² para todo d. Una función continua de módulo
constante en ℝ es constante (si el módulo es 0 es idénticamente 0; si no, no se anula y no cambia de signo). Luego
𝖡_a es constante.

Paso 3 (𝖡_a no es constante). Para |d| < δ := log 2 − 2T_0 > 0 y n ≥ 2, |log n ± d| > 2T_0, así que la parte del peine
de 𝖡_a(d) es nula y 𝖡_a(d) = β(d) = ∫ w(τ) cos(τd) dτ, w := m F̂_0²/2π. Escribo w = w⁺ − w⁻. El conjunto {m < 0}
es acotado porque m(τ) ≥ log(|τ|/2π) − 4 (P47 lem:mbounds(ii)); luego w⁻ tiene soporte compacto y β_− := ∫w⁻cos(τ·)
es C^∞. Si β fuera constante en (−δ, δ), β_+ = β + β_− sería C^∞ en un entorno de 0, y β_+ es la transformada de la
medida finita positiva w⁺dτ. Por el lema clásico de momentos (CITED: si la transformada de Fourier de una medida
positiva finita tiene derivada de orden 2k en 0, el momento de orden 2k es finito), ∫ w⁺ τ⁴ dτ < ∞. Pero
F̂_0(τ) = (τ² + ¼)|ĝ(τ)|⁴ con |ĝ(τ)| = |e^{(b+iτ)a} − 1|/|b + iτ| ≥ |e^{ba} − 1|/(b² + τ²)^{1/2}, y e^{ba} ≠ 1 pues
b ≠ 0; así F̂_0(τ) ≥ c τ^{−2} y F̂_0² ≥ c² τ^{−4} para |τ| grande, mientras m(τ) ≥ 1 para |τ| grande. Luego
w⁺τ⁴ ≥ c′ > 0 para |τ| grande y ∫w⁺τ⁴ = ∞. Contradicción: β no es constante cerca de 0, luego 𝖡_a no es constante.

Paso 4 (uniformidad). Los pasos 2–3 muestran que (1.1) no puede valer para todas las cuaternas de primos; fijo una
cuaterna donde falla y M_0 su mayor elemento. Para M ≥ M_0 una factorización de 𝔸_M impondría (1.1) en esa
cuaterna (paso 1), luego no existe. ∎

*Alcance.* Cubre la factorización de Smith E diag(f∗μ) Eᵀ, toda LDLᵀ en un orden lineal que extienda la
divisibilidad cuyo factor herede el patrón de incidencia, y todo D con pivotes del tipo Σ_{d|n}Λ(d) = log n. No es
efectivo (no da M_0). No cubre: W con soporte fuera de la divisibilidad; identidades con resto ρ ≠ 0 (Lema 2); otras
reducciones ((L2), escalera, perfil). Mejora `ROUND_001_B` (4.1) de NUMÉRICO a PROVED, sin la fila del 1 y sin
estimar valores de 𝖡.

### Lema 2 (la incidencia es invisible en la reducción a primos; PROVED)

Para W con el patrón del Lema 1 y 𝒫 = primos ≤ M: (WᵀDW)[𝒫] = D_1 wwᵀ + diag(D_p W_{pp}²), w = (W_{1p})_{p∈𝒫}.
*Demostración.* Para p ≠ q primos el único divisor común es 1; para p = q, los divisores son 1 y p. ∎
Con `CA_K_002` Teor. 3.2 ((★) ⟺ 𝔸_M[𝒫] ⪰ 0 para todo M; PROVED allí) y Div_M[𝒫] = 0: en una identidad
𝔸_M = WᵀDW + ρ con D ≥ 0, la parte de incidencia aporta en la reducción equivalente sólo un rango uno más una
diagonal, y el resto ρ[𝒫] = Arch_M[𝒫] − Near_M[𝒫] − D_1wwᵀ − diag(·) lleva todo el signo.

### Corolario 3 (clase afín emparejada sobre (S); PROVED)

Clase: V(a) = V_0 + V_1(a), V_1 lineal en el peso, coeficientes independientes del peso, con
2 sym(V_0ᵀV_1(Λ)) = −(Div_M + Near_M). Entonces ρ := 𝔸_M − V(Λ)ᵀV(Λ) = Arch_M − V_0ᵀV_0 − V_1(Λ)ᵀV_1(Λ) ⪯ Arch_M,
y Arch_M es indefinida para M ≥ M_1 (`CA_K_001` Prop. 1.3(a)); luego ρ no es ⪰ 0. Es la cuenta de `ROUND_003_2`
Lema 3 con Arch_M en lugar de Arch sobre P_T; cierra su caso (iii). ∎

## Resultado

**Repetición en la parte principal (factorización por incidencia de divisores sobre 𝔸_M = `ROUND_001_B` §4 en (S));
(i) ya resuelto en el corpus (Arch_M y Arch_M − Div_M indefinidas: `CA_K_001`/`CA_K_002`). Pieza NO-GO de formato
PROVED (Lema 1), delimitación PROVED (Lema 2) y cierre PROVED del caso (iii) de `ROUND_003_2` (Corolario 3).** Sin
candidata lista para construcción.

## Qué se probó

- Lema 1: para M ≥ M_0, 𝔸_M no tiene factorización exacta WᵀDW con W soportada en la divisibilidad y D diagonal de
  cualquier signo; vale para todo peine (formato). Prueba: rango uno en primos + densidad de log 𝒫 + 𝖡 = β cerca de 0
  y β no es C⁴ en 0 (momento cuarto infinito).
- Lema 2: la incidencia sólo aporta rango uno más diagonal sobre los sitios primos, que ya son una reducción
  equivalente.
- Corolario 3: la clase afín emparejada también falla sobre (S).
- Localidad: 𝔸_M depende de a(n) sólo para n < M e^{2T_0}.

## Qué falló y por qué

- La incidencia de divisores no ve los pares coprimos casi proporcionales, que es donde vive Near; 𝖡 es continua en
  el retardo real y eso fuerza columnas casi paralelas que el patrón de incidencia no admite.
- Los pivotes explícitos en Λ (log n, Λ(n), f∗μ) no pueden salvar el formato: el obstáculo es arquimediano (β no es
  suave de orden 4 en 0), no aritmético.
- La ecuación funcional entra en (S) sólo por Arch_M y las condiciones de Tate, aditivamente; no hay en el corpus
  leído una identidad que la acople a las entradas de Near.

## Qué queda NO excluido

- W cuyo soporte incluya pares coprimos casi proporcionales (m ≈ kn), con fórmula propia, por ejemplo indexada por
  las fracciones de Farey o por las aproximaciones racionales de log m − log k; ningún objeto escrito.
- Identidades con resto ρ ≠ 0 donde ρ[𝒫] tenga signo manifiesto por una razón distinta de la incidencia.
- La clase afín sin emparejamiento (caso (i) de `ROUND_003_2`) y V no afín en Λ (caso (ii)).
- Las demás reducciones PROVED ((L2), escalera, perfil continuo).

## Siguiente paso concreto

1. Anotar en el índice (06 §R9), en el grid y en el ledger: «factorización WᵀDW de 𝔸_M con W en el orden de
   divisibilidad, D cualquiera: NO-GO de formato PROVED (ROUND_003_7 Lema 1), genérico en el peine»; y el Corolario 3
   como cierre del caso (iii) de ROUND_003_2. Corregir en el ledger la etiqueta de (4.1) de K2: de NUMÉRICO a PROVED
   (no efectivo).
2. Una reapertura de (S) por factorización sólo con un W cuyo patrón contenga las casi-coincidencias, escrito antes de
   derivar, con su ρ y con la línea de ruptura para cΛ y a_P, pasando la puerta de cuatro puntos.
