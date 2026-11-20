# Revisión de la ronda 3 (selección sobre nueve zonas no excluidas)

Memos revisadas: `ROUND_003_1.md` … `ROUND_003_9.md`. Cada demostración etiquetada PROVED se rehízo
línea por línea; las citas señaladas se abrieron en primaria. Ninguna memo pasa la puerta de selección:
no hay candidata lista para construcción. Signo global OPEN. Ningún resultado de esta ronda lleva signo.

## Veredictos

| Zona | Memo | Veredicto | Comprobado | Corrección o reserva |
|---|---|---|---|---|
| 1 familias por ventana | 003_1 | ACEPTADO: sin mecanismo nuevo | Lema E (cota N_T y construcción g_λ; N_T(g_λ)² = O(λ^{−2j−1} log λ)); Lema F (traslación a (−T, T − log I), fuga nula, a_T = a_{T′} por soporte de c_G); Lema S | Lema F es condición necesaria, no imposibilidad. Fases 60, 72, 114, 121, 124, 155, 159, 161, 199, 200 no abiertas en primaria |
| 2 funcionales con Λ | 003_2 | ACEPTADO CON CORRECCIONES | Lema 1 (cambio unitriangular); Lema 2 (tautológico); Lema 3 (ρ^{(c)} = Arch − ‖V_0F‖² − c²‖V_1F‖²; cita P47 cor:Tarch confirmada) | «Con dependencia racional vale lo mismo en la localización» es ARGUED. El Lema 3 exige el emparejamiento (E) para todo F y coeficientes independientes del peso |
| 3 operadores por primo con J | 003_3 | ACEPTADO: sin mecanismo nuevo | P0 (J intercambia A y B; símbolo par); P1, P2; Q_ε = ε⟨X²F, F⟩ para JF = εF | La lectura de la paridad de R170_870 frente a la de J es ARGUED. R161_030–031, 033, 036–039 no abiertas en primaria |
| 4 ancla nula con borde | 003_4 | ACEPTADO | Lema 1 (Cauchy–Schwarz semidefinido), Prop. 2, Lema 3 (distancia a un subespacio) | En el Lema 4 sólo el coeficiente principal es PROVED; la no anulación de la pendiente es ARGUED (la memo lo dice) |
| 5 par virial | 003_5 | ACEPTADO | Lema 1; Lema 2 (dos bultos a distancia log 2 + εθ: 𝒱 = −v_2 log 2 · c_φ′(−θ)/ε + O(1), a_T = O(log(1/ε))); Lema 3 (valores de a_P·log + a_P∗a_P en p^k y p^iq^j). Citas R162_501 Teor. 2.2, Prop. 3.1 y 106_124 §1 confirmadas | El Lema 2 sólo usa v_2 ≠ 0: obstrucción de formato, genérica en el peine. La sección 2 es ARGUED |
| 6 conversión conjunta | 003_6 | ACEPTADO CON RESERVA | M_NS_N = I + U_N; H^{cΛ} = cH + (c − 1)S′_N; Lema 3 (resta de (4.4) en c = 0 y c = 1) | (4.3) depende de la forma exacta de P47 thm:PCfinite, no re-derivada aquí: PROVED relativo a ese teorema, sobre el núcleo liso. El Corolario 2 es homogeneidad en c: correcto y elemental. «Ninguna cantidad escrita distingue c > 1» es ARGUED |
| 7 formulación (S) | 003_7 | ACEPTADO CON RESERVA | Lema 1 pasos 1–4 (rango uno en cuaternas de primos; paso al continuo; 𝖡² constante; momento cuarto divergente); Lema 2; Corolario 3 | El Lema 1 usa la fórmula de F̂_0 y la forma 𝔸_M = [𝖡(log m − log k)] de P47 thm:oneprofile, citadas y no re-derivadas. No efectivo. Genérico en el peine. CA_K_001, CA_K_002 no abiertas aquí |
| 8 objeto cuadrático en el peso | 003_8 | ACEPTADO: repetición | Antecedente confirmado en primaria: `phase-70-lee-yang-dbn/E70_12` (δV + V² = Z⁻¹δ²Z, «entirely Euler-side») y E70_10 (opción graduada). Lemas 1 y 2 | Ninguna |
| 9 métrica no local | 003_9 | ACEPTADO CON RESERVA | Lema 2(a): u/(λ+u²) + v/(λ+v²) = (u+v)(λ+uv)/((λ+u²)(λ+v²)), suma de dos rangos uno ≥ 0 para λ ≥ 0 | (b)–(d) relativos a `ROUND_001_L.md` y a la inversión de Stieltjes (CITED). GS §§17–19 y LINK_014 no releídos en primaria por la memo |

## Resultados que se anotan (todos sin signo)

R3-a (PROVED, `ROUND_003_3.md` P0–P2). En el álgebra generada por multiplicadores y la reflexión J, sobre
cada sector de paridad de P_T, toda identidad con cuadrados y apareamientos por J es un reparto puntual
del símbolo; los productos mn aparecen sólo en ε⟨X²F, F⟩, lineal en la autocorrelación y de signo opuesto
en los dos sectores. No excluye operadores que usan la compresión a la ventana, M_t o rango finito.

R3-b (PROVED, `ROUND_003_2.md` Lema 3; `ROUND_003_7.md` Cor. 3). Clase afín emparejada: V = V_0 + V_1(Λ)
con coeficientes independientes del peso y término cruzado igual al peine. Entonces ρ ≤ Arch (≤ Arch_M
en (S)), que no es ⪰ 0 para T ≥ 0.60 (resp. M ≥ M_1). No excluye V afín sin emparejar, V_0 dependiente
del peso, ni V no afín en Λ.

R3-c (PROVED, `ROUND_003_4.md` Lema 1, Prop. 2, Lema 3). En una realización de a_T por restricción o
ínfimo parcial de una forma semidefinida, un vector nulo (en particular el ancla con borde) no influye
en la identidad; el formato con borde coincide con (G). No excluye formas indefinidas con vector neutro
no radical ni el esquema por contradicción de R170_862.

R3-d (PROVED, `ROUND_003_5.md` Lema 2). Para T > ½ log 2 no existe a_T = κ𝒱_T + ρ_T sobre P_T ∩ C_c^∞
con κ ≠ 0 y ρ_T ≥ −C‖·‖². Genérico en el peine. No excluye generadores distintos de la dilatación pura
ni el par VIR–LB/VIR–DET sobre el radical.

R3-e (PROVED relativo a P47 thm:PCfinite, `ROUND_003_6.md` Lema 1, Cor. 2, Lema 3). Identidad sobre todo
P_T con test de Möbius truncado: a_T = f_0 − f_1 − R_0 + R_1. Bajo cΛ cada bloque exterior es
proporcional a c; toda afirmación de signo sobre un bloque exterior separado vale para todo c > 0 o para
ninguno. La anulación interior se reabsorbe: g = b_T − f_1 + R_1. No examinado: el signo del resto R(F).

R3-f (PROVED relativo a P47 thm:oneprofile, no efectivo, `ROUND_003_7.md` Lema 1). Para M ≥ M_0 no existe
𝔸_M = WᵀDW con W soportada en la divisibilidad y D diagonal real. Genérico en el peine. No excluye W con
soporte en los pares m ≈ kn ni identidades con resto.

R3-g (PROVED relativo a `ROUND_001_L.md`, `ROUND_003_9.md` Lema 2). Clase de identidades de Green de tipo
resolvente M(u) = βu + u⟨g, (H + u²)⁻¹g⟩, H ⪰ 0, sobre cualquier Hilbert: la medida espectral queda
fijada por M y su positividad equivale a la de la escalera. Circularidad con clase. No excluye
dependencias en u que no sean de tipo resolvente ni formas indefinidas.

R3-h (PROVED, `ROUND_003_1.md` Lemas E y F). Si vale (G), V_T es acotado en la norma
N_T² = ∫(1 + log(2 + |τ|))|F̂|²: valores y jets puntuales no son componentes admisibles. Para cuadrados
de traslaciones truncadas agrupadas con índices ≤ I, (G) en T implica
a_{T′}(F) ≥ (1/2π)∫σ_B|F̂|² sobre P_{T′}, T′ = T − ½ log I: condición necesaria.

R3-i (PROVED en dos memos independientes: `ROUND_003_2.md` Lema 1; `ROUND_003_4.md` Lema 4, parte del
coeficiente principal). Que una identidad deje de valer para cΛ no caracteriza un paso de signo: toda
identidad polinómica en el peso válida en Λ difiere de su versión en otro peso por una combinación de
los átomos Σ_{d|n}a(d) − log n. Precisión posterior de O4: una ruptura formal aislada no demuestra signo,
pero una identidad completa demostrada con lado derecho positivo puede fallar sólo en su igualdad bajo
un falsificador. No es necesario que el resto auxiliar pierda positividad. Véase la auditoría de O4/O17
y del Lema T al final de la Parte V del índice maestro.

## Lo que la ronda deja sin excluir, y sin objeto escrito

1. Un término de grado ≥ 2 en el peso que entre **sumando** y se anule en Λ por la identidad de divisores
   (del tipo (c − 1)²‖v‖² a lo largo de cΛ); R3-b sólo cierra el caso en que resta.
2. Operadores que usan la compresión a la ventana (fuga), M_t o rango finito; la contabilidad conjunta
   con el bloque de Tate de R161_032 (4.2).
3. El resto R(F) de casi-coincidencias con pesos de Möbius de R3-e.
4. W en (S) con soporte en los pares m ≈ kn y fórmula propia.
5. Formas indefinidas con vector neutro no radical.
6. Generadores distintos de la dilatación pura con conmutador relativamente acotado por a_T.
7. VIR–LB y VIR–DET sobre el radical; la salida A de R161_033 (dilatación de fuente isométrica).

Antes de proponer sobre 2 hay que leer por archivo la fase 161 (tres antecedentes de esta ronda estaban
allí) y 106_124 §§3–8 para 6.
