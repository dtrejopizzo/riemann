# Ronda 4, zona 3: el resto R(F) del test de Möbius truncado (memo de selección)

Memo de selección, no de construcción. Objetivo (★): λ_A(T) ≥ 0 para todo T, con las definiciones de
`../phase-211-sign-sandbox/STATEMENT_001.md`. Notación de P47 §sec:firstcontact
(`04-papers/47-row-d-dual-certificates/main.tex`, l. 6625–6700): V_{−log n}F(t) = F(t + log n), S_N, S′_N,
L_M = Σ_{d≤M}Λ(d)d^{−1/2}V_{−log d}, A_M = 𝓜 − L_M − L_M*, 𝓜 = m(D). Objeto examinado: el resto R(F) de
`ROUND_003_6.md` (4.2). Etiquetas: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMÉRICO.

## Cotejo

Búsquedas (grep en `03-research/` entero, P47, P48, índice de rutas, grid, crucigrama): «c_N(k)»,
«truncated Möbius», «Möbius truncad», «M_N S_N / M_NS_N», «mollifi», «Levinson», «Barban», «Vehov»,
«Selberg mollifier». Leídos en primaria: P47 l. 6625–6700 (operadores, thm:PCfinite) y l. 6760–6790
(subsec:collars), cor:shape (l. 9167–9190); `ROUND_003_6.md` entera; `R170_853` §§0–2, `R170_878` §§0–2,
`R170_879` §§0–2, `R170_880` §§0–2, `R170_881` §§0–2, `R170_882` §§0–2, `R170_883` §§0–2, `R170_896` §§0–3;
`phase-200-sign-object/A_MU_FACTORIZATION_001.md` (d)–(e) y tabla; `phase-200-sign-object/Z_CARRIER_001.md`
§3.2; `phase-199-frontier-pattern/proof-L-sharp/PROOF_L_SHARP_FF_001_EDGE_RECOMBINATION.md` §§1–3;
`phase-204-refd-tractability/AUDIT_204_TRACT_F_001.md` §3.3; `phase-188-closing-D/L2_BUILD_017` §§1–3;
`N_BUILD_003` (Teorema 1); grid `R162_2300_part6.jsonl` fila «Proportion-of-zeros inputs» (mollificación =
ensanchar la ventana, DEAD). No abiertos en primaria: los ≈ 280 archivos de las fases 101–159 donde
«mollif» aparece en otros sentidos (sólo vistos por línea de grep), `R170_884`, `N_BUILD_002`, `N_BUILD_005`,
`N_BUILD_006`, `D_CONSTRUCTION_001` (Prop. M), fases 106, 121, 162 y 186–187 más allá del grep (sin
coincidencias de c_N(k) o Möbius truncado en ellas). Una búsqueda sin coincidencias no prueba novedad.

**(1) Antecedente más cercano.** Tres, en primaria:
- `phase-200-sign-object/A_MU_FACTORIZATION_001.md` (d): el multiplicador A_μ = 1 − ζM_μ (Möbius truncado)
  como factor de una identidad cuadrada; NO-GO allí: es «pura Möbius, existe para todo falsificador», la
  positividad del resto se reduce a la del objetivo.
- `PROOF_L_SHARP_FF_001` Teor. FF.1 y `Z_CARRIER_001` §3.2: la cola c_N del Möbius truncado actuando sobre
  traslados de la función de ventana; el bloque cociente Σ_N c_N c_{kN} quedó OPEN, con aviso propio de
  ser genérico en el peine.
- `R170_878`–`R170_883`: el inverso causal (PS_N*P)^{−1} = PM*P **comprimido** y sus incidencias de
  Möbius con borde; `L2_BUILD_017` Lema 1: a_T = a_∞ − 2Re⟨U_μF, U_logF⟩ con Möbius truncado.

**(2) Objeto nuevo.** No hay (ℋ_T, V_T, ρ_T). Lo nuevo es estructural y sin signo: la verificación de
(4.2), la fórmula cerrada de la parte arquimediana R_0 (Lema 2), la identidad exacta de símbolos para
cualquier inverso aproximado invariante por traslaciones (Lema 3), y un NO-GO con clase: en esa clase el
resto y la forma «mollificada» son funcionales lineales de c_F y toda escritura manifiesta de ambos se
suma a un certificado de la forma sin inverso (Lema 4). Además R ≤ 0 es falso sobre P_T (Lema 5).

**(3) ¿Evita la dificultad del antecedente?** No. La dificultad de A_MU (d) es que el multiplicador de
Möbius no depende del peso; la de esta zona es la misma, más una: (4.2) no usa en absoluto Σ_{d|n}Λ(d) =
log n, sólo μ ∗ 1 = δ sobre el peine entero (Lema 1). La identidad vale palabra por palabra para todo peso,
luego es del tipo de P47 lem:shape-ident.

**(4) Conexión con la positividad global.** a_T = (a_T + R) − R sobre P_T (Lema 1). Si R ≤ 0 y a_T + R ≥ 0
sobre P_T, entonces (★). Pero la primera es falsa (Lema 5) y, en la clase invariante por traslaciones, la
pareja sólo reparte el símbolo (Lema 4).

**(5) Falsificadores.** (4.2) es genérica en el peso: vale para cΛ, a_P, borrados, amplificaciones y todo
peso, porque no usa el valor del peso. No hay línea que se rompa; el signo tendría que venir enteramente
del resto, que es una forma de símbolo explícito del mismo tipo que a_T. Para cΛ, R^{(c)} = R_0 − cR_1 y,
sobre agujas (Lema 5), R^{(c)} = c·R + O(ε⁵): todo signo detectado por agujas es el mismo para todo c > 0.

**Veredicto del cotejo: repetición en lo esencial** (A_MU (d); el uso lineal de Möbius es un certificado,
P47 cor:shape (a)), más tres lemas cortos que cierran la zona en la clase invariante por traslaciones. Se
escriben abajo porque son completos.

## 1. Verificación de (4.2) contra P47

**Lema 1 (PROVED).** Sea F lisa con soporte en I_T, M ≥ N ≥ e^{2T}, M_N = Σ_{n≤N}μ(n)n^{−1/2}V_{−log n}.
Entonces M_NS_N = I + U_N, U_N = Σ_{N<k≤N²}c_N(k)k^{−1/2}V_{−log k}, c_N(k) = Σ_{d|k, k/N≤d≤N}μ(d), y

  Re⟨S_NA_MF, M_N*F⟩ = a_T(F) + R(F),
  R(F) = R_0(F) − R_1(F),  R_0 = Σ_k c_N(k)k^{−1/2} Re⟨𝓜V_{−log k}F, F⟩,
  R_1 = Σ_{N<k≤N²} Σ_{d≤M} c_N(k)Λ(d)(kd)^{−1/2} Re c_F(log(k/d)).

*Demostración.* Traslados, 𝓜 = m(D) y L_M, L_M* son multiplicadores de Fourier: conmutan. El coeficiente
de k^{−1/2}V_{−log k} en M_NS_N es Σ_{dm=k, d≤N, m≤N}μ(d): vale Σ_{d|k}μ(d) = [k = 1] si k ≤ N y 0 si
k > N². a_T(F) = Re⟨A_MF, F⟩ por P47 subsec:collars (los d con log d ≥ 2T trasladan el soporte fuera de
I_T). Para k > N: ⟨L_MV_{−log k}F, F⟩ = 0 (soportes disjuntos, desplazamiento log(kd) > 2T);
⟨L_M*V_{−log k}F, F⟩ = Σ_{d≤M}Λ(d)d^{−1/2}⟨V_{log d−log k}F, F⟩ y ⟨V_aF, F⟩ = conj c_F(a). ∎

Comprobación respecto de `ROUND_003_6.md`: signo, rango (N, N²] y soporte correctos. Dos precisiones,
ninguna es error: (a) la restricción |log(k/d)| < 2T es automática (c_F tiene soporte en [−2T, 2T]); (b) R
**depende de M** salvo que M ≥ N²e^{2T}: con M < N² se pierden casi-coincidencias d > M y, si M = N, no hay
ningún término diagonal k = d. En lo que sigue M ≥ N²e^{2T} salvo aviso.

c_N(k) en potencias de primo (PROVED, cuenta directa): c_N(p) = 0 para p ∈ (N, N²]; para a ≥ 2,
c_N(p^a) = −1 si p^{a−1} ≤ N < p^a y 0 si no. Luego la diagonal de R_1 es −κ_N‖F‖² con

  κ_N = Σ_{p^a ∈ (N,N²], a≥2, p^{a−1}≤N} (log p)/p^a > 0   (N ≥ 4, por Bertrand: hay p ∈ (√N, N]).

## 2. Estructura de R_0 y de R_1

**Lema 2 (forma cerrada de R_0, PROVED).** Sobre P_T, con 𝔸_j(F) = ∫F e^{(2j+½)t}, 𝔹_j(F) = ∫F e^{−(2j+½)t},

  R_0(F) = −Σ_{j≥1} C_j(N) Re[𝔸_j(F) conj 𝔹_j(F)],   C_j(N) = M_N(2j+1)S_N(2j+1) − 1,

con M_N(s) = Σ_{n≤N}μ(n)n^{−s}, S_N(s) = Σ_{n≤N}n^{−s}.

*Demostración.* Por la forma de Lévy (STATEMENT §1), para G, F de soportes disjuntos
⟨𝓜G, F⟩ = −½∫K(|u|)c_{G,F}(u)du; con G = V_{−log k}F el argumento recorre |u| = log k − v, |v| < 2T,
donde K(|u|) = 2Σ_{j≥0}k^{−(2j+½)}e^{(2j+½)v}. Como Re c_F es par, ∫e^{av}Re c_F(v)dv =
∫cosh(av)Re c_F(v)dv = Re[𝔸 conj 𝔹] (a = 2j+½). El término j = 0 es Re[A(F) conj B(F)] = 0 sobre P_T.
El factor k^{−1/2}·k^{−(2j+½)} = k^{−2j−1}, y Σ_{N<k≤N²}c_N(k)k^{−s} = M_N(s)S_N(s) − 1. ∎
(NUMÉRICO, sólo validación de la identidad de Dirichlet: C_1(8) = −0.0060125… por ambos lados.)

R_0 es pues una suma de formas hiperbólicas de rango ≤ 2 con coeficientes de tamaño O(N^{−2j}) y signo no
fijado: la «parte no local de 𝓜 entre I_T y su traslado» no contiene más que las condiciones de momento
de órdenes 2j+½, j ≥ 1, y la de orden ½ se anula exactamente por las condiciones de Tate.

**Lema 3 (identidad de símbolos, PROVED).** Sea b finitamente soportada con b(1) = 1 y
P_b = Σ b(n)n^{−1/2}V_{−log n}, P̂_b(τ) = Σ b(n)n^{−1/2−iτ}; sea s_M(τ) = m(τ) − 2Re L_M(½ + iτ) el símbolo de
A_M. Para F lisa con soporte en I_T,

  Re⟨P_bA_MF, F⟩ = (1/2π)∫ Re P̂_b(τ) · s_M(τ) |F̂(τ)|² dτ.

Si además b(k) = 0 para 1 < k ≤ e^{2T}, el lado izquierdo es a_T + R_b con
R_b = (1/2π)∫Re(P̂_b − 1)s_M|F̂|². Para el Möbius truncado, P̂ = M_N(½+iτ)S_N(½+iτ) y

  a_T + R = (1/2π)∫ Re[M_N S_N(½+iτ)] s_M |F̂|²,   R_1 = (1/2π)∫ Re[U_N(½+iτ) conj L_M(½+iτ)] |F̂|²,

con U_N = M_NS_N − 1; la otra mitad, Re[U_N L_M], tiene frecuencias log(kd) > 2T y se integra a cero contra
|F̂|² de una F de la ventana.

*Demostración.* P_bA_M es un multiplicador de símbolo P̂_b s_M; s_M es real y Re P̂_b es par (b real), luego
Re⟨P_bA_MF, F⟩ = (1/2π)∫Re(P̂_b)s_M|F̂|². ∎

## 3. Lo que ve la ventana y el NO-GO con clase

La ventana entra sólo por el soporte de F. Todo operador de (4.2) es un multiplicador de Fourier: no hay
compresión Q_T, ni M_t, ni rango finito. Para tales operadores ⟨XF, YF⟩ = (1/2π)∫conj(Ŷ)X̂|F̂|²,
funcional lineal de c_F, y el símbolo está determinado módulo funciones cuyo espectro no toca (−2T, 2T)
(más formas que se anulan sobre P_T). Ése es exactamente el grado de libertad de los certificados de
medida de P47. La restricción a la ventana no introduce nada que el símbolo no vea.

**Lema 4 (NO-GO con clase 𝒯_inv, PROVED).** Clase 𝒯_inv: identidades sobre P_T ∩ C_c^∞(I_T) de la forma
a_T = Q_1 − Q_2, con Q_1 = Re⟨P_bA_MF, F⟩ y Q_2 = R_b para un inverso aproximado P_b invariante por
traslaciones cualquiera (Möbius truncado, Möbius suavizado, pesos de Selberg o de Barban–Vehov,
b independiente del peso o no), y afirmaciones de signo de cada Q_i probadas por una escritura manifiesta:
Q_i = (1/2π)∫σ_i|F̂|² + τ_i(F) con σ_i ≥ 0 en casi todo punto y τ_i ≡ 0 sobre P_T (la ventana se usa sólo
para cambiar σ_i dentro de su clase módulo el anulador). Entonces:
(a) Q_1 ≥ 0 y −Q_2 ≥ 0 manifiestas dan a_T = (1/2π)∫(σ_1 + σ_2)|F̂|² + τ_1 + τ_2: un certificado de clase (D)
    de P47 para a_T, en el que b no aparece. El mismo certificado se obtiene con b = δ_1.
(b) En particular, la pareja «a_T + R manifiestamente ≥ 0 y R manifiestamente ≤ 0» es imposible
    puntualmente (σ_i ≡ símbolos literales): sumando, s_M ≥ 0 en casi todo punto, falso porque
    s_M(0) = m(0) − 2Σ_{d≤M}Λ(d)d^{−1/2} < 0 para M ≥ N ≥ e^{2T} ≥ 2 (m(0) = C_0 < 0).
(c) Toda (G) con V_T en el álgebra de multiplicadores es una partición del símbolo (R3-a sin J).
*Demostración.* (a) Q_1 − Q_2 = a_T y la suma de escrituras manifiestas es manifiesta; los σ_i dependen de b
pero su suma es un símbolo de a_T módulo el anulador. (b) Es (a) con τ_i = 0 y sin anulador.
(c) ‖V_TF‖² = (1/2π)∫|v̂|²|F̂|²; ρ_T = a_T − ‖V_TF‖² tiene símbolo s_T − |v̂|². ∎

Qué no dice el Lema 4: no prueba que no existan certificados de a_T (eso es el contenido de λ^prim, P47
cor:shape (a)); dice que el inverso aproximado no añade nada a esa ruta, ya registrada.

**Lema 5 (R ≤ 0 es falso sobre P_T, PROVED).** Para M ≥ N² y N ≥ 4 existe F ∈ P_T ∩ C_c^∞(I_T) con R(F) > 0.
*Demostración.* Sea ψ_ε ≥ 0 un bulto de ancho ε centrado en el interior de I_T y φ = (¼ − ∂²)ψ_ε: por partes
∫φe^{±t/2} = 0, luego φ ∈ P_T, y lo mismo sus traslados dentro de I_T. Los átomos de R_1 forman un conjunto
finito {u_i} ⊂ (−2T, 2T); tómese ε menor que la mitad de la mínima distancia entre átomos distintos. Entonces
c_φ tiene soporte en |u| < 2ε y R_1(φ) = −κ_N‖φ‖². Para R_0: |𝔸_j(φ)|, |𝔹_j(φ)| ≤ C_j‖ψ_ε‖_1 = O(hε) si ψ_ε
tiene altura h, mientras ‖φ‖² ≍ h²ε^{−3}; y Σ_j|C_j(N)| < ∞, luego R_0(φ) = O(ε⁵)‖φ‖². Así
R(φ) = κ_N‖φ‖²(1 + O(ε⁵)) > 0. ∎

Con F = φ + sV_uφ (u un átomo, s real) se obtiene R(F) = ‖φ‖²[κ_N(1 + s²) − w̃_u s] + O(ε⁵), con w̃_u el
coeficiente de Re c_F(u) en R_1 sumado sobre ±u. Si |w̃_u| > 2κ_N para algún átomo, R también toma valores
negativos y es indefinida. NUMÉRICO (validación de un punto): T = 1, N = 8, M = N²e²: κ_8 = 0.2695,
max|w̃_u| = 1.175 en u = log 5 > 2κ_8; T = 1.5, N = 21: κ = 0.219, max|w̃_u| = 1.304. R es indefinida en
esos casos.

**Corolario 6 (ceguera al peso sobre agujas, PROVED).** Para el peso cΛ, R^{(c)} = R_0 − cR_1 (R_0 y c_N no
ven el peso), y sobre las pruebas de aguja del Lema 5, R^{(c)}(F) = c·R(F) + O(ε⁵)‖φ‖². El signo de R
detectado por agujas es el mismo para todo c > 0. Para a_P (P > e^{2T}) desaparecen de R_1 los átomos con
d < P y los demás quedan igual: el resto cambia de reparto, no por una propiedad de Λ.

## 4. Respuesta a la pregunta de selección (v)

- Dependencia del peso: R_0 no depende del peso; R_1 es lineal en él (proporcional a c bajo cΛ);
  a_T + R = Re⟨S_NA_MF, M_N*F⟩ es afín en c. Correcto como se enunció.
- ¿Elección del inverso con R ≤ 0 sobre P_T? Para el Möbius truncado con M ≥ N², no (Lema 5). Para un b
  general la diagonal de R_b es −Σ_{k potencia de primo}b(k)Λ(k)/k: se puede volver negativa cargando b en
  potencias de primo, pero entonces a_T + R_b ≤ a_T y la pareja sólo traslada el problema; en la clase
  𝒯_inv con escrituras manifiestas la pareja se suma a un certificado independiente de b (Lema 4).
- La zona no muere sólo por «afín en el peso» (el conjunto de c donde vale un par afín es un intervalo y
  podría acabar en 1): muere por ser lineal en c_F dentro del álgebra de multiplicadores (Lema 4) y por ser
  (4.2) genérica en el peso (Lema 1). La afinidad entra sólo en el Corolario 6.

## Resultado

NO-GO con clase 𝒯_inv (Lema 4) más repetición (A_MU_FACTORIZATION_001 (d); P47 cor:shape (a)). Sin mecanismo
nuevo; no hay candidata lista para construcción. Signo global OPEN.

## Qué se probó

1. Lema 1: (4.2) correcta contra P47 (signo, rango (N, N²], soporte); R depende de M salvo M ≥ N²e^{2T};
   c_N en potencias de primo y la diagonal −κ_N de R_1.
2. Lema 2: R_0 = −Σ_{j≥1}(M_NS_N(2j+1) − 1)Re[𝔸_j conj 𝔹_j]; el orden ½ se anula por Tate.
3. Lema 3: identidad de símbolos a_T + R_b = (1/2π)∫Re P̂_b s_M|F̂|² para todo inverso invariante.
4. Lema 4: NO-GO con clase 𝒯_inv; la versión puntual es imposible por s_M(0) < 0.
5. Lema 5: R ≤ 0 es falso sobre P_T (M ≥ N², N ≥ 4); indefinida en T = 1 y 1.5 (NUMÉRICO).
6. Corolario 6: signo de R sobre agujas ciego a c > 0.

## Qué falló y por qué

La identidad (4.2) sólo usa μ ∗ 1 = δ en el peine entero; no toca el peso y por tanto no se rompe ante
ningún falsificador de peso. Todos sus operadores son multiplicadores, de modo que a_T + R y R son
funcionales lineales de c_F: elegir el inverso aproximado sólo reparte el símbolo, y el resto R tiene
diagonal positiva κ_N, que impide R ≤ 0.

NO excluido (sin objeto escrito):
1. inversos **comprimidos** a la ventana (Q_TM_NQ_T, el inverso causal (PS_N*P)^{−1} = PM*P de R170_878–883):
   no son invariantes por traslaciones y quedan fuera del Lema 4; ya recorridos en la fase 170 (RULES_AVOID
   §I2), reapertura con razón nueva;
2. usos no lineales en c_F (productos de dos funcionales de la familia, determinantes de Gram de
   (S_NA_MF, M_N*F)) que sean identidades y no cotas;
3. el bloque cociente Σ_N c_N c_{kN} de `Z_CARRIER_001` §3.2 (Lema Z.2, OPEN), que vive en la otra
   orientación (cola de Möbius actuando sobre la función de ventana, no sobre el resto de la forma);
4. inversos con b dependiente de los valores del peso de modo no afín.

## Siguiente paso concreto

No construir sobre R(F) con inversos invariantes por traslaciones. Anotar en el índice y en el grid:
«Fase 212, ronda 4, zona 3: resto R(F) del Möbius truncado. (4.2) verificada, genérica en el peso; R_0 en
forma cerrada por momentos 2j+½; NO-GO con clase 𝒯_inv (inverso invariante + escrituras manifiestas = un
certificado independiente del inverso); R ≤ 0 falso (diagonal κ_N > 0). Signo global OPEN.» Un segundo
lector debe rehacer el Lema 2 (factor −½·2 y la anulación de j = 0) y el Lema 5 (orden O(ε⁵) de R_0).
