# Ronda 4, candidata A — La meta SP-161 / L161.1 con pesos con signo y pesos de criba (memo de selección)

Memo de selección, no de construcción. Objetivo (★): λ_A(T) ≥ 0 para todo T, definiciones de
`../phase-211-sign-sandbox/STATEMENT_001.md`. Notación de `../phase-161-row-d-sum-product-square/R161_001`
(S_N, K_N, L_M, A_M = 𝓜 − L_M − L_M*, E_N, H_{M,N}) y de `ROUND_003_6.md` (M_N, U_N, c_N(k), f_0, f_1,
g, R_0, R_1). Para un polinomio de Dirichlet finito P(s) = Σ p_n n^{−s} escribo P(∂) = Σ p_n n^{−1/2}τ_{log n};
los traslados forman un álgebra conmutativa indexada por ℚ_{>0} (τ_{log r}, r = a/b), y «coeficiente en r»
se refiere a esa álgebra. Etiquetas: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMÉRICO.

## Cotejo

Búsquedas hechas (grep sin distinción de mayúsculas, después lectura primaria de lo encontrado):
«Selberg sieve / criba de Selberg / Barban / Vehov / GPY / Λ_R / mollif / Levinson / signed weights /
pesos con signo / truncated Möbius / Möbius truncado / M_N S_N / discrete derivative» en todo
`03-research/`, P47, P48, el índice, el grid y el crucigrama; «Möbius / M_N / truncat» en las fases 106,
121, 122, 124 y en R162_405–408, R162_206, R162_401.

Leídos en primaria: R161_000–004 enteros; `ROUND_003_6.md` entero; R170_853 §0, R170_878 §0 (con sus
correcciones de truncamiento), R170_879–883 §0, R170_896 §§0–1; fase 200: `Q2_LADDER_001.md` §§0–2,
`SPEC_SIGN_OBJECT_002.md` §B (Q1), `AUDIT_200_SPEC_002.md` §§3–5; índice README, entradas
PROOF_L_SHARP_GG_001, AUDIT_200_SPEC_002, Q2 ladder, PI_MU_001, MULT_GAUGE_001; R162_1003 §§4–5;
`P121_CAUSAL_MOBIUS_OBSERVABILITY.md` §§1–2; fase 167 (R167_102 Teor. B, R167_103 §§2, 4.1, R167_190);
índice 04 filas G3D-159, G3E-159, G1C-R162_1003, P58-1; índice 05 L62.

No abiertos en primaria (sólo título o línea de grep): los 15 archivos de la fase 106 que nombran Möbius
(entre ellos 106_40, 106_117, 106_144), `P121_CMO_SOURCE_MATRIX_NO_GO.md` (lo conozco por R161_004 §3),
R162_405 §4.3 («tests conjugados por Möbius»), R162_406 Prop. en l. 131, `phase-104/104_87`, fase 33
(82, 83). En 122, 124, R162_206, R162_401 no hubo coincidencias. Una búsqueda sin coincidencias no
prueba novedad.

### (1) Antecedentes más cercanos

1. **R161_002 §§4–5 y §8** (meta L161.1 y Teor. 8.1): ninguna ponderación w_N ≥ 0 cancela la cola de
   hipérbola; Cor. 8.2 sitúa el signo en la derivada discreta terminal −log p. La rama con signo no está
   escrita en la fase (confirmado: `RULES_AVOID.md` K5, K7).
2. **`ROUND_003_6.md` (4.2)–(4.5) y R170_878 (0.2)–(0.4)**: el test de Möbius, completo en R170_878
   ((PS_N*P)^{−1} = PM*P) y truncado en 003_6; R3-e cierra los bloques exteriores separados con test
   independiente del peso.
3. **Fase 200, Q1–Q3 y escalera Q2** (`SPEC_SIGN_OBJECT_002` §B, `AUDIT_200_SPEC_002` §5,
   `Q2_LADDER_001`): forma de Selberg del retículo cociente con varianza de Selberg como parte positiva
   (Q1: tautología, y^T𝔅y = 𝒲[g]); escalera de mollifiers truncados c^{(Y)}_N (Q2: diferencia radical,
   𝒲 = 0); correlaciones de c_N «de tipo Λ_R de Selberg» (Q3: no dependen del peine, no ven cΛ). Lema SQ.0:
   todo exterior mollificado a cualquier nivel es −g módulo el radical.
4. **MULT_GAUGE_001 (clase R-MOM, PROVED)**: todo |1 + ζH|², mollifier de cualquier longitud, da W_T
   exacta. **PROOF_L_SHARP_GG_001**: «factorización del defecto del mollifier como fuente de signo», no
   reintentar.
5. **R162_1003 §4**: el problema de primer contacto es un problema extremal de tipo Selberg (Prop. 4.1);
   el núcleo de Weil no es de tipo mcd (Prop. 4.2); toda representación de Selberg Z*DZ con Z unipotente es
   una congruencia (Cor. 4.3).
6. **Fase 167, Teor. B** (ceguera de las cribas: b_θ satisface toda cota superior de criba que cumple Λ) y
   P121 (eliminación de Möbius unitriangular sobre el poset de divisores).

Conclusión del cotejo: la pregunta (iii) —pesos de criba de Selberg o Barban–Vehov como test o como
mollifier— está cubierta por los antecedentes 3–5 en las formulaciones del radical y de la recta. Lo que
no está escrito es la versión de L161.1 con pesos con signo en N y la comparación exacta entre L161.1 y la
identidad de Möbius de 003_6. Eso es lo que esta memo escribe (§§(4)–(5)); son lemas de formato, sin signo.

### (2) Objeto realmente nuevo

No hay objeto (ℋ_T, V_T, ρ_T). Se escriben tres lemas cortos, todos de clase declarada y sin signo:

- **Lema 1** (telescopado con pesos escalares con signo en N): el único peso finito real que hace
  telescopar exactamente los términos interiores de Σ_N w_N S_N*S_N es w = δ_{N=1}, y la identidad
  resultante es a_T = a_T con borde nulo. Cierra la rama con signo de L161.1 en la clase algebraica de
  R161_002 Teor. 8.1.
- **Proposición 2** (respuesta a (i)): la identidad (4.2) de 003_6 no es instancia de L161.1 para ningún
  peso con signo; sus pesos viven en el índice de dilatación n (μ(n)), no en N.
- **Lema 3** (respuesta a (iii)): la identidad M^λS_N = I + (exterior) es exacta si y sólo si λ = μ en
  [1, N]; los pesos de Selberg/Barban–Vehov la rompen con un bloque interior explícito, y la variante
  cuadrática |M^λD_N|² no produce un cuadrado sino la forma A_M sobre vectores fuera de P_T.

### (3) ¿Evita la dificultad del antecedente?

No. Los tres lemas confirman la dificultad registrada: los pesos de Möbius o de criba fijados sin usar el
peso dejan toda la identidad afín en Λ (R3-e) y la parte «cuadrática en λ» se aparea con A_M, cuyo signo es
el objetivo (R162_1003 Cor. 4.3; fase 200 Q1). Ninguna de las elecciones introduce dependencia de grado ≥ 2
en el peso.

### (4) Identidades que conectan con la forma completa

Convenciones: F liso con soporte en I_T, T > ½ log 2, M ≥ N ≥ e^{2T}. De R161_001 §1 (CITED de esa memo):
𝓕 es involución unitaria, 𝓕τ_a𝓕 = τ_{−a}, y 𝓕 conmuta con multiplicadores pares; como m es par y
P_M = L_M + L_M* es par, 𝓕A_M𝓕 = A_M. Por tanto, para la forma orientada de R161_002 (OR),

    B_{M,N}(F) = ⟨A_M𝓕F, S_N*S_N𝓕F⟩ = ⟨A_MF, S_N*S_NF⟩,                                 (4.1)

y a_T(F) = ⟨A_MF, F⟩ (003_6 Paso 1).

**Coeficientes de S_N*S_N (PROVED).** S_N*S_N = Σ_{m,n≤N}(mn)^{−1/2}τ_{log m − log n}. Para r = a/b con
mcd(a,b) = 1 y q = max(a,b), los pares (m,n) = (ja, jb), j ≤ N/q, dan el coeficiente
(ab)^{−1/2}Σ_{j ≤ N/q} 1/j. Para pesos reales w_N de soporte finito y Ω(m) := Σ_{N≥m} w_N,

    [r](Σ_N w_N S_N*S_N) = (ab)^{−1/2} G(q),   G(q) := Σ_{j≥1} Ω(jq)/j.                     (4.2)

**Lema 1 (telescopado escalar con signo; PROVED).** Clase 𝒞_w: pesos reales w_N de soporte finito, test
S_N𝓕F, y exigencia de L161.1 de que, en el álgebra de traslados, Σ_N w_N S_N*S_N = I + (términos en r
con |log r| ≥ 2T). Entonces w = δ_{N=1}, Σ_N w_N B_{M,N} = B_{M,1} = a_T, el resto de borde es 0 y la cola
de hipérbola es H_{M,1} = L_M entera.

*Demostración.* Para q ≥ 2 el par (q, q − 1) es coprimo y |log(q/(q−1))| ≤ log 2 < 2T; por (4.2), G(q) = 0
para todo q ≥ 2, y G(1) = 1 por el coeficiente en r = 1. La inversión sobre múltiplos
Ω(m) = Σ_j μ(j)G(jm)/j (comprobación: Σ_j μ(j)j^{−1}Σ_i Ω(ijm)/i = Σ_l Ω(lm)l^{−1}Σ_{j|l}μ(j) = Ω(m); las
sumas son finitas) da Ω(1) = 1 y Ω(m) = 0 para m ≥ 2, luego w_1 = 1 y w_N = 0 para N ≥ 2. Con S_1 = I,
(4.1) da B_{M,1} = a_T; K_1 = 0 y H_{M,1} = L_MS_1 − K_1 = L_M. ∎

Lectura. La exigencia de L161.1 («los términos interiores telescopan») ya fija los pesos sin ver Λ: con
signo o sin él, la única solución es la trivial. Además el Teor. 8.1 de R161_002 en versión con signo pide
algo incompatible: con soporte de w en N ≤ N_1 y un primo p > N_1, el coeficiente de Σ w_N H_{M,N} en p es
log p · Σ_N w_N, de modo que cancelar la cola en los primos grandes exige Σ_N w_N = 0, mientras el Lema 1
exige Σ_N w_N = Ω(1) = 1. **Corolario (PROVED):** en 𝒞_w no hay peso que telescope el interior y cancele
la cola a la vez. La derivada discreta pura w = δ_{N+1} − δ_N (suma 0) da S_{N+1} − S_N =
(N+1)^{−1/2}τ_{log(N+1)} y H_{M,N+1} − H_{M,N} = (N+1)^{−1/2}(L_M − log(N+1))τ_{log(N+1)}: es la identidad
PC de un solo traslado, cuyo coeficiente en r = 1 de (4.2) es G(1) = Ω(1) = 0, de modo que a_T no aparece
(PROVED, cálculo directo). No excluido: tests distintos de S_N𝓕F, pesos dependientes de F, telescopado
sólo después de comprimir a la ventana (ahí 𝓜 no es local y los coeficientes con |log r| ≥ 2T no se
anulan), y el uso de los cuadrados de fuga de C_T, que ningún peso de esta clase produce.

**Proposición 2 (respuesta a (i); PROVED, con Bertrand CITED).** Para N ≥ 2, el multiplicador real de
(4.2) de 003_6, I + ½(U_N + U_N*), no pertenece a span_ℝ{S_{N′}*S_{N′} : N′ ≥ 1}. Por tanto la identidad
a_T = f_0 − f_1 − R_0 + R_1 no es instancia de L161.1 para ningún peso w_N con signo.

*Demostración.* Si Σ w_{N′}S_{N′}*S_{N′} = I + ½(U_N + U_N*), los coeficientes en r = a/b con a, b ≥ 2
son 0 a la derecha (U_N sólo tiene coeficientes en enteros k ∈ (N, N²]); por (4.2), G(q) = 0 para todo
q ≥ 3 (par (q, q − 1)), y el coeficiente en r = 2 es 0 a la derecha (2 ≤ N), luego G(2) = 0. Entonces la
izquierda tiene coeficiente 0 en todo entero k ≥ 2, y haría falta c_N(k) = 0 para todo k ∈ (N, N²]. Sea p
primo con N/2 < p ≤ N (Bertrand) y k = 2p ∈ (N, N²]: los divisores d de k con d ≤ N y k/d ≤ N son d = 2
y d = p (si p ≠ 2), luego c_N(2p) = −2; para N = 2, k = 4 y c_2(4) = μ(2) = −1. Contradicción. ∎

Correspondencia exacta. L161.1 pondera en el índice de corte N una familia de Grams autoadjuntos
S_N*S_N (símbolo |D_N(½+iτ)|²). La identidad de 003_6 usa un único N y pondera en el índice de dilatación
n con μ(n): su test M_N*F es causal (unilateral), y su símbolo real Re[M_N D_N] = 1 + Re U_N está fuera del
cono y del span de {|D_{N′}|²}. Lo que ambas comparten es el álgebra PC; lo que 003_6 tiene y L161.1 no,
es que el coeficiente 1 se aísla exactamente (M_NS_N = I + exterior); lo que L161.1 pide y 003_6 no tiene,
es el término de borde con C_T. En (4.2)–(4.3) de 003_6 no aparece ningún cuadrado de fuga.

**Lema 3 (exactitud fuerza Möbius; pesos de criba; PROVED).** Sea λ real con λ_1 = 1, soporte en d ≤ R,
M^λ = Σ_{d≤R} λ_d d^{−1/2}τ_{log d} y θ^λ_N(k) = Σ_{d|k, d≤R, k/d≤N} λ_d. Entonces
M^λS_N = I + Σ_{k>N} θ^λ_N(k)k^{−1/2}τ_{log k} (sin coeficientes en 1 < k ≤ N) si y sólo si, extendiendo
λ_d := 0 para d > R, se tiene λ_d = μ(d) para todo d ≤ N. (Si R < N esto exige μ(k) = 0 en (R, N], lo que
ocurre sólo en casos degenerados como R = 3, N = 4; si R ≥ N, los λ_d con d > N quedan libres y sólo tocan
k > N.)

*Demostración.* Para k ≤ N la condición k/d ≤ N es automática, y θ(k) = Σ_{d|k}λ_d con λ extendida por 0.
La anulación para 1 < k ≤ N, junto con λ_1 = 1, determina por inducción λ_k = −Σ_{d|k, d<k}λ_d = μ(k) para
k ≤ N; recíprocamente λ = μ en [1, N] da Σ_{d|k}μ(d) = 0. ∎

Consecuencia para los pesos de Selberg/Barban–Vehov λ_d = μ(d)P(log(R/d)/log R) (P(0) = 0, P(1) = 1): para
un primo p ≤ min(R, N), θ(p) = 1 − P(log(R/p)/log R) ≠ 0 en general, y la identidad deja de ser «I más
exterior». Sigue siendo exacta como álgebra, con un bloque interior adicional:

    Re⟨M^λS_NA_MF, F⟩ = a_T(F) + I^λ(F) + R^λ(F),
    I^λ(F) = Σ_{1<k≤N} θ^λ(k)k^{−1/2} Re⟨A_Mτ_{−log k}F, F⟩,
    R^λ(F) = Σ_{k>N} θ^λ(k)k^{−1/2} Re⟨A_Mτ_{−log k}F, F⟩.                                (4.3)

I^λ es una forma de casi-coincidencias dentro de la ventana con coeficientes θ^λ pequeños en media, sin
signo; R^λ es el resto exterior de 003_6 con c_N sustituido por θ^λ.

**El «cuadrado de Selberg» (respuesta a (iii); PROVED como identidad).** La única forma en que el cuadrado
(Σ_{d|k}λ_d)² entra es con el test M^λS_NF en los dos lados. Con V := M^λS_N − I, para F ∈ P_T liso,

    ⟨A_M M^λS_NF, M^λS_NF⟩ = a_T(F) + 2 Re⟨A_M VF, F⟩ + ⟨A_M VF, VF⟩,                    (4.4)

cuyo símbolo en la recta es s_M(τ)|M^λ(½+iτ)D_N(½+iτ)|² con coeficientes de Dirichlet θ^λ_N(k). Es decir:
forma = Q^λ(F) − 2Re⟨A_MVF,F⟩ − ⟨A_MVF,VF⟩ con Q^λ el lado izquierdo de (4.4). Q^λ no es un cuadrado: es la
forma A_M evaluada en M^λS_NF, que no está en P_T (soporte en [−T, T + log(NR)]); A_M sobre la recta es
indefinida (R161_002 §2: fondo semilocal negativo). El resto 2Re⟨A_MVF,F⟩ + ⟨A_MVF,VF⟩ es afín en Λ
(A_M lo es) y cuadrático en λ. La positividad de Selberg Σ_k θ(k)²w(k) ≥ 0 usa una medida w ≥ 0 sobre
los enteros; aquí el lugar de w lo ocupa s_M, que es el objetivo. Es exactamente la situación de R162_1003
Cor. 4.3 (congruencia) y de la fase 200 Q1 (tautología). Elegir λ minimizando la parte cuadrática es el
problema extremal de R162_1003 Prop. 4.1: instala la respuesta.

**Respuesta a (iv): grado en el peso (PROVED).** Con λ fijado sin usar el peso (μ, Selberg, Barban–Vehov,
GPY, Λ_R: todos se construyen con μ y log sobre los enteros, no con el peso), M^λ, S_N, V, E_N, 𝓕 no
dependen del peso y A_M^{(c)} = 𝓜 − c(L_M + L_M*). Luego (4.3) y (4.4) son afines en c, con I^λ, R^λ y el
resto de (4.4) de la forma (bloque independiente) − c·(bloque de primos). El test es independiente del
peso, así que el Corolario 2 de 003_6 (R3-e) se aplica literalmente a I^λ_1 y R^λ_1: toda afirmación de
signo sobre ellos por separado vale para todo c > 0 o para ninguno. La parte cuadrática en λ no aumenta el
grado en el peso: sigue siendo 1. Los pesos de criba no introducen dependencia de grado ≥ 2 en el peso.

Observación (ARGUED). La única manera de que λ dependa del peso de modo no lineal es usar el «Möbius del
sistema»: para el peso a, μ_a = coeficientes de 1/ζ_a con −ζ_a′/ζ_a = Σ a(n)n^{−s}; para cΛ, ζ_{cΛ} = ζ^c y
μ_{cΛ} son los coeficientes de ζ^{−c}, no polinomiales en c. Pero entonces el análogo de M_NS_N = I + exterior
exige S^{(c)} con coeficientes de ζ^c, y L^{(c)}S^{(c)} = K^{(c)} vale para todo c: la anulación interior
se vuelve una identidad válida para toda la familia (patrón B1), y E_N^{(c)} = S^{(c)}𝓕 − JS^{(c)} pierde
la estructura de Poisson para c ≠ 1. No se ha escrito; no está excluido.

### (5) cΛ y a_P: por qué el resto deja de ser ≥ 0

No hay resto ρ con signo: ninguna de (4.1)–(4.4) separa una parte manifiestamente no negativa. Lo único
que se puede decir con precisión es qué línea cambia:

- **cΛ, c ≠ 1.** Lema 1: los pesos no dependen de Λ, la identidad trivial a_T = a_T se rompe sólo en el
  sentido trivial. (4.3)–(4.4): todos los bloques que ven primos se multiplican por c; un signo de un bloque
  separado sobrevive a todo c > 0 (R3-e), luego no puede ser el paso de signo.
- **a_P, P > N.** Lema 3 y Prop. 2 no dependen del peso; en (4.3) cambian I^λ_1 y R^λ_1 (pierden los
  términos con d < P y no son proporcionales a los de Λ). Como ninguno de ellos tiene signo escrito, no hay
  «resto que deje de ser ≥ 0» que señalar.

## Resultado

Sin mecanismo nuevo. Repetición en lo esencial para (iii) (fase 200 Q1–Q3 y escalera Q2, MULT_GAUGE R-MOM,
GG_001, R162_1003 §4). Se añaden tres lemas de formato PROVED, sin signo, que cierran la rama con signo de
L161.1 en su clase algebraica y responden (i) negativamente.

## Qué se probó

1. Lema 1 (PROVED): en la clase 𝒞_w (pesos escalares reales finitos en N, test S_N𝓕F, telescopado exacto
   de coeficientes interiores), el único peso es δ_{N=1} y la identidad es a_T = a_T. Corolario (PROVED):
   telescopar el interior (Σw = 1) y cancelar la cola de hipérbola en los primos grandes (Σw = 0) son
   incompatibles. La derivada discreta en N es la PC de un solo traslado y no contiene a_T.
2. Proposición 2 (PROVED, Bertrand CITED): la identidad de Möbius truncado de 003_6 no es instancia de
   L161.1 para ningún peso con signo; c_N(2p) = −2 es el testigo.
3. Lema 3 (PROVED): M^λS_N = I + exterior exactamente si y sólo si λ = μ en [1, N]. Pesos de Selberg o
   Barban–Vehov añaden el bloque interior I^λ de (4.3). La versión cuadrática (4.4) da A_M sobre vectores
   fuera de P_T, no un cuadrado.
4. (iv) (PROVED): con pesos de criba fijados sin el peso, todo es afín en c; R3-e se aplica literalmente.

## Qué falló y por qué

- L161.1 fija sus pesos por una condición que no ve Λ y que sólo admite la solución trivial (Lema 1).
- La positividad de Selberg necesita una medida positiva sobre los enteros; en la forma esa medida es s_M,
  el propio objetivo (Cor. 4.3 de R162_1003).
- Los pesos de criba o de Möbius son de grado 0 en el peso; la identidad queda afín (R3-e).

NO excluido (sin objeto escrito):
1. tests no de la forma S_N𝓕F o M^λ*F, y pesos que dependan de F;
2. telescopado tras la compresión a la ventana, con los cuadrados de fuga de C_T (ninguna identidad de
   este memo los produce; la contabilidad conjunta R161_032 (4.2) sigue sin derivar);
3. el «Möbius del sistema» μ_a (no polinomial en c), con su E_N^{(a)} sin Poisson para c ≠ 1;
4. el bloque interior I^λ de (4.3) como forma de casi-coincidencias con coeficientes θ^λ de criba: su
   signo no se examinó; por R3-e no puede dar signo por separado si λ no depende del peso.

## Siguiente paso concreto

No construir en esta zona. Anotar en índice y grid: «Fase 212, ronda 4A: L161.1 con pesos con signo en N:
NO-GO con clase 𝒞_w PROVED (telescopado exacto fuerza w = δ_1, identidad tautológica; incompatible con la
cancelación de la cola); la identidad de Möbius truncado de 003_6 no es instancia de L161.1 (Prop. 2);
exactitud de M^λS_N = I + exterior ⟺ λ = μ en [1, N]; pesos de Selberg/Barban–Vehov dan bloque interior
y forma afín en c (R3-e). Repetición de fase 200 Q1–Q3, R-MOM, GG_001 y R162_1003 §4 para (iii). Signo
global OPEN.» Un segundo lector debe verificar (4.1) (𝓕A_M𝓕 = A_M, que depende de las convenciones de
R161_001 §1) y el cálculo de coeficientes (4.2).
