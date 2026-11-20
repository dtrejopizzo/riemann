# Revisión de la ronda 4 (meta SP-161 con pesos con signo y cuatro zonas no excluidas)

Memos revisadas: `ROUND_004_A.md` … `ROUND_004_E.md`. Cada demostración etiquetada PROVED se rehízo salvo
donde se indica. Ninguna memo pasa la puerta de selección: no hay candidata lista para construcción.
Signo global OPEN. Ningún resultado de esta ronda lleva signo.

## Veredictos

| Zona | Memo | Veredicto | Comprobado | Corrección o reserva |
|---|---|---|---|---|
| A meta L161.1 con pesos con signo; pesos de criba | 004_A | ACEPTADO | (4.2) coeficientes de S_N*S_N; Lema 1 (G(q) = 0 para q ≥ 2 por el par coprimo (q, q−1), inversión sobre múltiplos, w = δ_{N=1}); Prop. 2 (c_N(2p) = −2); Lema 3 (inducción λ = μ en [1, N]) | (4.1) usa las convenciones de R161_001 §1, citadas. La observación sobre el «Möbius del sistema» es ARGUED |
| B defecto de divisores cuadrático que suma | 004_B | ACEPTADO CON RESERVA | Lema 1: minimizar en ℓ la forma a_T − ⟨ℓ, η⟩ + ⟨ℓ, Kℓ⟩ da η ∈ ran K y a_T ≥ ¼⟨η, K⁺η⟩ | El cambio de variables ⟨e, γ⟩ = ⟨ℓ, U^{−T}γ⟩ y el caso Q(u) = 0 del Lema 2(c) no se rehicieron aquí. Las violaciones con núcleos naturales son NUMÉRICO con valores tomados de 211 ROUND_017_A; el caso T grande es CONDITIONAL |
| C resto de Möbius truncado | 004_C | ACEPTADO CON RESERVA | Lema 3 (multiplicadores); Lema 4; Lema 5: φ = (¼ − ∂²)ψ_ε ∈ P_T, ‖φ‖² ≍ h²ε^{−3}, momentos O(hε), y c_N(p^j) = −1 cuando p^{j−1} ≤ N < p^j, de donde la constante diagonal κ_N > 0 | El Lema 2 (forma cerrada de R_0) no se rehízo. La indefinición de R es NUMÉRICO (T = 1, T = 1.5) |
| D casi-divisibilidad en (S) | 004_D | ACEPTADO CON CORRECCIONES | Lema A; Lema B (1 ⊲ 2 ⊲ 6 y no 1 ⊲ 6 si 2T_0 < log(7/6)); Lema C(a)–(c) (analiticidad contra el término v_2 en d = log 2) | En el Lema C(d), el paso del núcleo continuo a su muestreo en logaritmos de enteros para excluir matrices semiseparables es ARGUED. N_BUILD_022, L2_BUILD_031, CA_K_001/002 y la fase 202 no fueron abiertas en primaria por la memo |
| E formas indefinidas e inercia | 004_E | ACEPTADO CON RESERVA | Lemas 2, 3 y 5 (constancia de índices para \|c − 1\| < λ_A(T)/Σ\|v_n\|); citas P47 thm:parityschur, prop:polarcap, subsec:inertia-excl confirmadas | La Prop. 1(c) es PROVED en dimensión finita y ARGUED para formas no acotadas. Fases 155 (ronda 5) y 156, R161_023, 061–063 y R170_854 no fueron abiertas en primaria por la memo |

## Resultados que se anotan (todos sin signo)

R4-a (PROVED, `ROUND_004_A.md` Lema 1 y corolario). Clase: pesos reales w_N de soporte finito en el
índice de corte, test S_N𝓕F, con la exigencia de L161.1 de que el interior telescope. El único peso es
w = δ_{N=1} y la identidad es a_T = a_T. Telescopar el interior exige Σw = 1; cancelar la cola de
hipérbola en primos grandes exige Σw = 0. Cierra la rama con signo de R161_002 §§4–5. No excluye tests
distintos, pesos dependientes de F, ni telescopar después de comprimir a la ventana.

R4-b (PROVED, `ROUND_004_A.md` Prop. 2, Lema 3, (4.3)–(4.4)). La identidad de Möbius de `ROUND_003_6.md` no
es instancia de L161.1. M^λS_N = I + exterior exactamente si y sólo si λ = μ en [1, N]; con pesos de
Selberg o Barban–Vehov aparece un bloque interior I^λ sin signo. El «cuadrado de Selberg» es la forma A_M
sobre un vector fuera de P_T. Los pesos de criba no elevan el grado en el peso. Antecedentes: fase 200
(Q1–Q3, MULT_GAUGE R-MOM, GG_001), R162_1003 §4.

R4-c (PROVED, `ROUND_004_B.md` Lemas 0–1). Formato a_T^{(a)}(F) + 𝔇_a(F) ≥ 0 para todo peso a, con 𝔇
cuadrático semidefinido en los átomos y nulo en Λ: equivale, para cada F, a η(F) ∈ ran K(F) y
a_T(F) ≥ ¼⟨η, K⁺η⟩. Es el objetivo con margen; el término de segundo orden no paga el primer jet.
Antecedente: fase 197 BARRIER_D2_001 Teor. 1. No excluye K no acotado, clases de pesos que no contienen
un entorno de Λ, ni defectos no polinómicos.

R4-d (PROVED, `ROUND_004_C.md` Lemas 3–5). Clase 𝒯_inv de inversos aproximados invariantes por traslación:
a_T + R_b tiene símbolo Re P̂_b · s_M; dos escrituras manifiestas de a_T + R ≥ 0 y −R ≥ 0 se suman en un
certificado de a_T en el que el inverso no aparece. Para el Möbius truncado con M ≥ N², N ≥ 4, R ≤ 0 es
falso sobre P_T. Antecedente: fase 200 A_MU_FACTORIZATION_001 (d). No excluye inversos comprimidos a la
ventana (recorridos en R170_878–883) ni el bloque cociente de Z_CARRIER (Lema Z.2, OPEN).

R4-e (PROVED salvo el punto ARGUED indicado, `ROUND_004_D.md` Lemas A–C). El soporte de Div + Near no es un
orden parcial; para razones grandes llena el semiorden de umbral y no depende del peso. 𝖡 no es
totalmente positiva ni de Pólya ni una transformada de Laplace en (0, ∞). Pivotes determinados por el
patrón de soporte: NO-GO de clase. No excluye W con valores de fórmula propia ni el cierre de {𝔸_M} bajo
complemento de Schur con un peso transformado explícito.

R4-f (PROVED, `ROUND_004_E.md` Lemas 2, 3, 5, 6). Una cota superior del índice negativo es una positividad
sobre un subespacio de codimensión finita. En cada ventana con λ_A(T) > 0 los índices de inercia son
constantes para c en un entorno de 1: un conteo de inercia no distingue c = 1. El formato de Pontryagin
ya está en P47 thm:parityschur y prop:polarcap. Los conteos crecientes en T son de la forma arquimediana
sin peine.

## Lo que la ronda deja sin excluir, y sin objeto escrito

1. Cierre de la familia {𝔸_M} bajo complemento de Schur con un peso transformado explícito (R4-e). Debe
   cotejarse antes con R3-b y con la fase 70 (E70_10–12).
2. El «Möbius del sistema» μ_a, coeficientes del inverso de la serie del peso, no polinomial en c (R4-b).
3. Telescopar después de comprimir a la ventana con los cuadrados de fuga de C_T; contabilidad
   R161_032 (4.2).
4. El bloque cociente de Z_CARRIER (Lema Z.2).
5. Un conteo por principio del argumento de una función explícita de un parámetro espectral distinta de
   det Γ_T(z) (R4-f).
6. Sin cambios respecto de `REVIEW_003.md`: generadores distintos de la dilatación pura; VIR–LB y
   VIR–DET; salida A de R161_033.
