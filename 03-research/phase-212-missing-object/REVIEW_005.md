# Revisión de la ronda 5 (generativa: escribir un objeto desde la especificación A1–A6)

Memos revisadas: `ROUND_005_G1.md` … `ROUND_005_G5.md`. Las cinco concluyen «no logré escribir un objeto que
cumpla A1–A6». Ninguna candidata. Signo global OPEN. Ningún resultado de esta ronda lleva signo.

## Veredictos

| Semilla | Memo | Veredicto | Comprobado | Reserva |
|---|---|---|---|---|
| G1 objeto de grado ≥ 3 con hessiana −a_T | 005_G1 | ACEPTADO | Lema 2–3: con p(e + sF) = p(e)∏(1 + sλ_i), Σλ_i = 0 y Σλ_i² proporcional a a_T(F) sobre P_T, de donde \|e_k(λ)\| ≤ (Σλ_i²)^{k/2}; para d = 3 el discriminante da a_T³ ≥ 54 p(F)² | La reducción de las cuatro clases de certificado a (G) se leyó, no se rehízo entera. «Probablemente falso en casi-minimizantes» es ARGUED. La cita de G2_B8_R5 no tiene aritmética de intervalos |
| G2 cierre bajo producto sobre la signatura | 005_G2 | ACEPTADO | Lema 1 (homomorfismo: producto de factores ↦ suma de formas); Lema 2 (un semigrupo cerrado bajo producto contiene x_∞ ⊛ x_2^{⊛n}, cuya forma 𝔪_T − nΠ_{T,2} tiene índice negativo no acotado sobre P_T para T > ½ log 2) | Lemas 3–5 leídos, no rehechos. «c = 2 exactamente falla» no se comprueba; sólo c grande |
| G3 la forma como varianza | 005_G3 | ACEPTADO CON RESERVA | Lema 1 (formato de varianza ⟺ (G)); Lema 3 (las leyes de ζ^c son probabilidades para todo c > 0) | El Lema 2 (Π_T con subespacios definidos de dimensión arbitraria de ambos signos sobre P_T) se revisó sólo en su plausibilidad |
| G4 inducción que alarga la ventana | 005_G4 | ACEPTADO | Lema 1 (c_F(±2T) = 0: en el cruce λ_A no depende del peso entrante); Lema 2 (intervalo admisible con interior cuando λ_A(T) > 0); Lema 3 (todo peso cumple a(n) = (a∗1)(n) − Σ_{d\|n, d<n}a(d)) | La premisa de la semilla era falsa (Lema 3). El análisis del forzante de Riccati es ARGUED |
| G5 invención libre | 005_G5 | ACEPTADO | L1 (−∇² log det(X_0 + ΣxA)[u,u] = tr((X_0⁻¹A_u)²): forma de Gram); L3 (para p homogéneo, por la identidad de Euler ∇²p(x_0)x_0 = (d−1)∇p(x_0), «a lo sumo un autovalor positivo» ⟺ ∇² log p ⪯ 0 sobre el ortogonal del gradiente) | L2 es PROVED en dimensión finita; su punto (e) es relativo a G2_B8_R1 |

## Resultados que se anotan (todos sin signo)

R5-a (PROVED, `ROUND_005_G5.md` L1, L3; `ROUND_005_G3.md` Lema 1). Log-concavidad en un punto base
(determinante, función de partición, varianza) y signatura de Lorentz de la hessiana de un polinomio
homogéneo en un punto: equivalen a una realización de Gram (G) o al enunciado en el sector. No añaden
mecanismo. No excluye una propiedad válida en un cono entero con certificado propio.

R5-b (PROVED, `ROUND_005_G1.md` Lema 3). Si p es hiperbólico de grado d ≥ 3 respecto de e con hessiana −a_T
sobre P_T, entonces \|D^k p(e)[F^k]\| ≤ C a_T(F)^{k/2}: o los términos de grado ≥ 3 se anulan sobre P_T
(clase de R160_C7_R1 Prop. 6.2), o la hiperbolicidad es el objetivo con margen (para d = 3,
a_T³ ≥ 54 p(F)²). Responde a R160_C7_R1 §6.3(2) en las cuatro clases de certificado examinadas.

R5-c (PROVED, `ROUND_005_G2.md` Lemas 1–2). Multiplicar factores de Euler es sumar formas. Ningún semigrupo
cerrado bajo producto que contenga el factor arquimediano y el del primo 2 admite un teorema de cierre
«n₋ ≤ κ sobre P_T» para T > ½ log 2. Con la condición de balance (cada factor local una vez por cada
factor arquimediano, equivalente a la imparidad de la derivada logarítmica bajo s ↦ 1 − s) y coeficientes
en {0, 1} no queda operación de cierre: la afirmación es el enunciado. Las etapas intermedias con
ecuación funcional torcida están en la fase 122 (P122_018).

R5-d (PROVED, `ROUND_005_G4.md` Lemas 1–3). En el instante en que la ventana alcanza log n, λ_A no depende
del peso entrante; en toda ventana con λ_A(T) > 0 el conjunto de pesos admisibles en n es un intervalo
con interior. Todo peso está determinado por su suma sobre divisores y los pesos anteriores; lo propio de
Λ es que esa suma es log n. Antecedentes: R162_802 §§4–5, R162_2701, fase 197 BARRIER_W_001.

R5-e (PROVED, `ROUND_005_G3.md` Lema 3; Lema 2 con la reserva indicada). Las leyes de valuaciones de ζ^c son
probabilidades para todo c > 0; ninguna identidad de varianza se rompe en c = 2. El peine no es una
varianza explicada. Antecedentes: fase 209 CONSTRUCTOR_005 §10, ANTICORRELATION_003; 106_114 Teor. 2;
211 POWER_GLOBAL_ROUTE_REVIEW.

## Lo que la ronda deja sin excluir, y sin objeto escrito

Las cinco memos señalan, con palabras distintas, el mismo hueco:
1. Un reparto local a_T = q_∞ + Σ_p q_p con q_v ⪰ 0, donde q_p no es invariante por traslación ni de tipo
   Lévy y tiene fórmula propia (G1, G5). Con reparto libre su existencia equivale al objetivo.
2. Un predicado de etapa para la inducción por primos, con fórmula propia (G2).
3. Una relación no lineal en el peso entre componer desplazamientos (convolución) y componer longitudes
   (ventana) (G4).
4. Certificados de raíces reales fuera de las cuatro clases examinadas; un punto base dependiente de F (G1).
