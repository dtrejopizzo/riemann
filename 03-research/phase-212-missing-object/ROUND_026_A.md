# ROUND_026_A — Cómputo del valor cóncavo V*_T frente a λ_A(T)

Etiqueta global: **NUMÉRICO** (Galerkin en coma flotante doble, sin intervalos, no certificado).

## 0. Qué se abrió
- Paper 47 `main.tex`: eq:form, eq:W y λ_A (l.115–135), lem:K y eq:m (l.395–410, C_0 = ψ(1/4) − log π, K(u) = 2e^{3u/2}/(e^{2u}−1)),
  thm:S(iii) (cola ∫_{2T}^∞ K), thm:A / eq:Aform (l.444–455), def:PD, def:W/eq:nuw (l.668, 1225), prop:finite (l.3156),
  valores numéricos publicados (l.169–170, 2521–2551, 11050–11062).
- R160_M2_R1 §§3–4 (Thm 4.1–4.3: V*_T = max_v V_T(v), v ∈ ℝ^{N_T} con signo libre), §7 (PBP_T), H1 (l.378).
- ROUND_025_A §§0–2; índice maestro l.5209, 11995, 12192, 31324–31329 (grep «prime-blind», «V\*_T», «valor cóncav»).
- **Antecedente:** ningún cómputo de V*_T registrado; H1 dice explícitamente «no numerics». Este memo es ese cómputo.
- Código del corpus (phase-162/186 scripts) listado pero no reutilizado: se escribió un Galerkin directo de eq:Aform,
  validado abajo contra los valores del paper.

## 1. Discretización
- a^w_T(F) = C_0‖F‖² + ∫_0^∞ (c_F(0) − c_F(u)) K(u) du − Σ_{2≤n<e^{2T}} w_n c_F(log n) (eq:Aform), F real.
- Base ortonormal de Legendre de grado < N en [−T,T]; c_ij(u) simetrizado por Gauss exacto en el solapamiento;
  integral en u por Gauss–Legendre (240 nodos) en [0,2T] más la cola exacta de thm:S(iii).
- P_T: núcleo de (A,B) por SVD (dim = N − 2). λ_A = λ_min con w = v, v_n = 2Λ(n)/√n.
- V*_T = max_{w∈ℝ^{N_T}} λ_min(a^w_T|P_T) como SDP (cvxpy/SCS, eps 1e-9). El valor reportado es λ_min recomputado
  con numpy en el w devuelto, luego es una cota inferior válida del V*_T discreto. También se calcula V*_T⁺ (w ≥ 0).
- Scripts y salidas: scratchpad `pbp/forms.py`, `pbp/vstar.py`, `pbp/run1.txt`, `run2.txt`, `run3.txt`.

## 2. Validación contra el paper
| control | paper | este cálculo (N=20/30/40) |
|---|---|---|
| λ_A(½log3) | ≈ 9.448·10⁻⁴ (l.169) | 9.77 / 9.52 / 9.49 ·10⁻⁴ (decrece hacia el valor) |
| λ_A(log2) | ≈ 9.83·10⁻⁸ (l.170) | 5.0·10⁻⁷ / 1.056 / 1.042 ·10⁻⁷ |
| λ_min(Arch\|P_T) en 0.58 / 0.60 | > 0 / < 0 (thm:index, T*_ev ∈ [0.58,0.60]) | +0.0273 / −0.0071 |
| λ_A(0.80) | λ_A(½log5=0.8047) ≈ 3.10·10⁻¹² (l.170) | 5.4·10⁻¹² (N=60,100) |
Convergencia algebraica lenta (símbolo con singularidad logarítmica); orden y signo reproducidos.

## 3. Resultados (signo libre, que es la definición de V*_T en R160_M2_R1)
| T | \|N_T\| | N (dim P_T) | λ_A(T) | Arch mín | V*_T | mult. en óptimo | V*_T⁺ (w≥0) |
|---|---|---|---|---|---|---|---|
| 0.60 | 2 | 30/60 (28/58) | 6.7·10⁻⁵ | −0.0071 | 0.07013 / 0.07007 | 2 | 0.04019 |
| 0.80 | 3 | 30/60/100 | 5.4·10⁻¹² | −0.302 | 0.04598 / 0.04581 / 0.04577 | 3 | 0.02864 |
| 1.00 | 6 | 30/60/100 | < 10⁻¹³ (bajo resolución) | −0.535 | 0.04022 / 0.03927 / 0.03921 | 4–5 | 0.01747 |
| 1.20 | 10 | 30/60/100 | bajo resolución | −0.732 | 0.0402 / 0.03325 / 0.03243 | 5 | 0.01306 |
| 1.40 | 15 | 30/60 | bajo resolución | −0.906 | 0.0438 / 0.03258 | 5–7 | 0.01005 |
| 1.60 | 23 | 30/60 | bajo resolución | ≈ −1.05 | 0.0469 / 0.03499 | 7 | 0.00857 |
- λ_A para T ≥ 1 sale ±10⁻¹⁴: es ruido de doble precisión; el paper acota λ_A ≤ 4·10⁹ T e^{−15.449T} y lo ubica en
  10⁻¹² ya en ½log5. No se resuelve λ_A(T) para T ≥ 1 aquí.
- Convergencia en N de V*_T: ≤ 0.1 % en T ≤ 0.8; 0.2 % en T = 1.0 (60→100); 2.5 % en T = 1.2 (60→100); T = 1.4, 1.6
  sólo N ≤ 60, **no convergido** (los valores con N = 30 están claramente sobreestimados; el ligero ascenso
  1.4→1.6 no debe leerse como tendencia). V*_T⁺ converge a 4 cifras en todos los T.
- Multiplicidad: el autovalor mínimo en el óptimo es degenerado siempre (mult. ≥ 2, creciendo hasta ~|N_T|/3);
  esperable: el máximo de λ_min de una familia afín se alcanza en un cúmulo (Thm 3.2 de R160_M2_R1: 0 ∈ conv κ_T).

## 4. Peso óptimo frente al verdadero (N = 100 salvo T = 1.4, 1.6: N = 60)
| T | v (n=2..7) | w* (n=2..7) | ‖w*−v‖/‖v‖ |
|---|---|---|---|
| 0.80 | .980, 1.269, .693 | .116, −1.000, −1.210 | 1.77 |
| 1.00 | .980, 1.269, .693, 1.440, 0, 1.471 | .277, −.591, −.877, −1.904, −1.024, −2.211 | 2.10 |
| 1.20 | (ídem; n=8..11: .490, .732, 0, 1.446) | .442, −.176, −.482, −1.265, −.551, −1.575; n=11: −9.2 | 3.75 |
| 1.60 | (ídem) | .374, −.345, −.647, −1.517, −.731, −1.955, … | 2.66 |
- w* es casi todo negativo (incluso en n = 6, 10 donde v_n = 0), sin parecido con v; no se acerca a v al crecer T.
  Con w ≥ 0, el óptimo (T = 1.2: .794, .751, .315, .354, .104, 0, 0, …) se apoya sólo en n pequeños y anula el resto;
  tampoco es v. El peso verdadero está en el borde de 𝒱_T (λ_A ≈ 0); w* está en su «centro».

## 5. Respuestas
1. **¿V*_T queda no diminuto mientras λ_A cae?** Sí, en el rango calculado (NUMÉRICO): V*_T ≈ 0.07 → 0.033 entre
   T = 0.6 y 1.6, mientras λ_A cae de 7·10⁻⁵ a debajo de 10⁻¹² ya en T = 0.8. El cociente V*_T/λ_A pasa de 10³ a > 10¹⁰.
   Esto es compatible con H1 de R160_M2_R1 (margen de PBP_T no doblemente exponencial) en T ≤ 1.6, no lo prueba.
2. **Escala con T:** V*_T decrece lentamente; con los valores convergidos (T ≤ 1.2) la caída es ~ −0.035 por unidad de T
   y aplanándose (0.0458, 0.0392, 0.0324); para T ≥ 1.4 la tendencia no está resuelta. V*_T⁺ decrece como
   ≈ 0.08·e^{−1.4T} aprox. (0.040, 0.029, 0.017, 0.013, 0.010, 0.0086): exponencial simple, no doble.
3. **¿w* → v?** No. w* se aleja (error relativo 1.8–3.8) y tiene signo opuesto al de v en casi todos los n.
   El margen de 𝒱_T lo dan pesos que no tienen nada de aritmético; esto refuerza que V*_T es ciego a los primos
   (índice l.5209) y que su positividad no transfiere margen a λ_A(T).

## 6. Qué no se abrió / límites
- No hay cota de error certificada; el SDP (SCS) emitió avisos de «inaccurate» en 3 corridas; el λ_min reportado se
  recomputó en el w devuelto (cota inferior honesta del V*_T discreto); la cota superior no se verificó por dual.
- V*_T discreto ≥ V*_T continuo? No: el subespacio de Galerkin restringe F, así que λ_min discreto ≥ continuo y el
  V*_T discreto **sobreestima** el verdadero; la caída 60→100 en T = 1.2 lo confirma. T ≥ 1.4 requiere N mayor.
- No se calculó Z^prim_T (relajación mixta) ni Z^A_T. No se tocó paper ni índice.
