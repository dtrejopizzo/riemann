# Ronda 032-A — ¿Es la existencia de pesos con margen una propiedad de los enteros? (NUMÉRICO)

Etiqueta global: **NUMÉRICO**. Nada de lo que sigue es un teorema.

## 1. Objeto y método
- a^{X,w}_T(F) = C_0‖F‖² + ∫_0^∞(c_F(0)−c_F(u))K(u)du − Σ_j w_j c_F(x_j) sobre P_T (Paper 47, eq:Aform),
  con el Galerkin de Legendre auditado (`free_weight_scripts/forms.py`, sin cambios; P_T por SVD).
- V*(X,T) = max_w λ_min (w libre); V*⁺ = ídem con w ≥ 0. Base: λ_min(Arch|P_T) (w = 0).
- Maximización: λ_min es cóncava en w; se maximiza la mínima suave −β⁻¹log Σ e^{−βλ_k} con L-BFGS(-B)
  y continuación β = 10 … 3·10⁴; el valor reportado es el λ_min EXACTO (en el espacio de Galerkin) en
  el w devuelto, es decir una cota inferior del máximo de Galerkin. Sin cvxpy (no hacía falta).
- Multiplicidad: nº de autovalores dentro del 1 % de |λ_min| (+10⁻⁶). Con la mínima suave el óptimo se
  aproxima, no se alcanza: la multiplicidad es indicativa (agrupamiento), no exacta.
- Script: `free_weight_scripts/lattice_032A.py`; salidas: `free_weight_scripts/out_032A/` (logs y JSON con
  los 12 primeros puntos y pesos w⁺).

## 2. Validación (enteros)
| T | V* (ref / N=60 / N=100) | V*⁺ (ref / N=60 / N=100) |
|---|---|---|
| 0.8 | 0.0458 / 0.04581 / 0.04577 | 0.0286 / 0.02864 / 0.02863 |
| 1.2 | 0.0324 / 0.03313 / 0.03235 | 0.0131 / 0.01305 / 0.01304 |
| 1.6 | — / 0.03495 / 0.02987 | 0.0086 / 0.00855 / 0.00854 |
Reproduce ROUND_026_A. Convergencia: V*⁺ estable a 3–4 cifras en todo el rango; V* (libre) NO convergido
para T ≥ 1.6 (variación 15 % entre N = 60 y 100). Como el Galerkin restringe a un subespacio, el valor
verdadero está, salvo error del optimizador, por debajo del de N = 100.

## 3. Tabla comparativa (N = 100; entre paréntesis N = 60 si difiere > 5 %; * = no convergido)
Base λ_min(Arch|P_T): −0.302 (0.8), −0.732 (1.2), −1.066 (1.6), −1.364 (2.0).

V* (w libre):
| retículo | T=0.8 | 1.2 | 1.6 | 2.0 |
|---|---|---|---|---|
| (1) enteros | +0.0458 | +0.0324 | +0.030 (0.035)* | +0.035 (0.040)* |
| (2) impares | −0.262 | −0.333 | −0.365 (−0.354) | −0.367 (−0.342)* |
| (3) coprimos con 3 | +0.0321 | −0.054 | −0.135 (−0.124)* | −0.152 (−0.104)* |
| (4) Beurling 2→2.2 | −0.037 | −0.078 | −0.108 (−0.093)* | −0.108 (−0.078)* |
| (5) Beurling 2→2.02 | +0.0512 | +0.0221 | +0.012 (0.019)* | +0.013 (0.033)* |
| (6) log(n+0.3) | +0.0100 | −0.080 | −0.099 (−0.067)* | −0.076 (−0.045)* |
| (7) ruido s1 / s2 / s3 | +.029/+.091/+.122 | +.026/+.090/+.081 | +.026/+.088/+.058* | +.026/+.089/+.077* |
| (8) sólo primos | +0.0286 | −0.068 | −0.120 | −0.150 |
| (9) potencias de primos | +0.0458 | +0.0263 | +0.0161 | +0.014 (0.015) |

V*⁺ (w ≥ 0), convergido a ≤ 1 % salvo donde se marca:
| retículo | T=0.8 | 1.2 | 1.6 | 2.0 |
|---|---|---|---|---|
| (1) enteros | +0.0286 | +0.0130 | +0.0085 | +0.0066 |
| (2) impares | −0.302 (= base) | −0.433 | −0.460 | −0.469 |
| (3) coprimos con 3 | +0.00001 (≈0) | −0.406 | −0.481 | −0.485 |
| (4) Beurling 2.2 | −0.095 | −0.209 | −0.223 | −0.263 |
| (5) Beurling 2.02 | +0.0170 | −0.0121 | −0.0164 | −0.046 (−0.020)* |
| (6) log(n+0.3) | −0.149 | −0.177 | −0.187 | −0.189 |
| (7) ruido s1 / s2 / s3 | +.007/+.057/+.028 | −.099/+.010/−.026 | −.134/+.0001/−.044 | −.147/−.009/−.054 |
| (8) sólo primos | +0.0286 | −0.111 | −0.215 | −0.314 |
| (9) potencias de primos | +0.0286 | +0.0122 | +0.0084 | +0.0064 |

Peso óptimo w⁺ (N = 100, primeros puntos; tabla completa de 12 en los JSON). Ejemplos a T = 2.0:
- enteros n=2..13: .886 1.008 .501 .896 .041 .747 .244 .302 .083 .498 0 .421
- potencias de primos (2,3,4,5,7,8,9,11,13,16,17,19): .886 1.010 .499 .913 .830 .144 .400 .559 .427 .129 .395 .197
- primos (2,3,5,…,37): .283 .973 .860 .792 .813 .358 .097 .416 .348 .247 0 0
- Beurling 2.02 (2.02,3,4.08,5,6.06,7,…): .804 .981 .523 .813 .067 .849 .251 .159 0 .869 0 .319
Multiplicidad agrupada en el óptimo: crece con T y con el nº de puntos (T = 0.8: 2–4; T = 2.0: 8–24 para
w libre, 6–15 para w ≥ 0); es el comportamiento típico de un máximo de λ_min (muchos autovalores se
igualan), no un rasgo distintivo de un retículo.

## 4. Lectura
1. **Pesos libres (V*).** Todos los retículos superan con creces la base (ganan ≥ 0.25–1.4), pero sólo
   algunos llegan a V* > 0. Son claramente positivos en todo el rango: enteros, potencias de primos, la
   perturbación Beurling 2.02 (margen decreciente, no convergido) y **los tres retículos aleatorios**.
   Claramente negativos para T ≥ 1.2: impares, coprimos con 3, Beurling 2.2, log(n+0.3), sólo primos.
2. **Enteros frente a genéricos con los mismos huecos, w libre:** el margen de los enteros NO es mayor.
   Dos de tres semillas de ruido dan V* ≈ 0.08–0.09, más del doble que los enteros (≈ 0.03); la tercera
   ≈ 0.026, comparable. El ruido de V* es casi constante en T (≈ fijado por los primeros puntos).
   Con w libre, la positividad parece depender de tener puntos cerca de log 2, log 3, log 4 con el
   espaciado del retículo, no de la estructura multiplicativa; log(n+0.3) (primer punto log 2.3) falla.
3. **Pesos no negativos (V*⁺).** Aquí la imagen cambia: en T ≥ 1.6 sólo enteros y potencias de primos
   tienen V*⁺ > 0 claramente (≈ 0.0085, 0.0066 en 1.6, 2.0). Ruido s2 queda en +0.0001 (≈ 0, dentro de la
   resolución del optimizador) en 1.6 y pasa a −0.009 en 2.0; s1, s3 negativos desde 1.2.
4. **Transiciones de signo en el rango (w ≥ 0):** coprimos con 3 (≈0 en 0.8 → −0.41 en 1.2); Beurling 2.02
   (+0.017 → −0.012 entre 0.8 y 1.2: una perturbación del 1 % del generador destruye V*⁺ > 0); sólo primos
   (+0.029 → −0.111); ruido s1 y s3 (positivo → negativo entre 0.8 y 1.2); ruido s2 entre 1.6 y 2.0.
   Para w libre: coprimos con 3, log(n+0.3) y sólo primos cambian de signo entre 0.8 y 1.2.
   En T = 0.8 la prueba es poco discriminante (2–3 puntos): muchos retículos aún pasan.
5. **Qué puntos importan.** Sólo primos falla y potencias de primos ≈ enteros: los compuestos que no son
   potencias de primo (6, 10, 12, …) aportan poco (w⁺ en n=6, 10, 12 ≈ 0.04, 0.08, 0); las potencias
   (4, 8, 9, 16) sí son necesarias. Quitar el 2 (impares) o el 3 (coprimos) hunde el margen.

## 5. Conclusión explícita
- Con **pesos libres**, (PBP_T) a T fijo **no distingue a los enteros**: retículos aleatorios con los
  mismos huecos tienen margen igual o mayor en todo T ∈ [0.8, 2.0] (valores de T ≥ 1.6 no convergidos,
  pero la diferencia, factor ≈ 2–3, supera la variación en N).
- Con **pesos no negativos**, en el rango T ∈ [1.6, 2.0] los únicos retículos probados con V*⁺ > 0
  claramente son los enteros y sus potencias de primos; los genéricos con mismos huecos, la perturbación
  Beurling 2.02 y log(n+0.3) dan V*⁺ ≤ 0 (ruido s2: ≈ 0 en 1.6, negativo en 2.0). Esto es compatible con
  que la restricción de signo w ≥ 0 sea donde entra la aritmética, con dos reservas: (a) el margen de
  los enteros también decrece (0.0286 → 0.0066) y su comportamiento en T mayor no se ha medido;
  (b) tres semillas y dos perturbaciones Beurling son una muestra pequeña; el contraste es NUMÉRICO.
- La sensibilidad a Beurling 2.02 (V*⁺ negativo desde T = 1.2) indica que, con w ≥ 0, lo que importa
  es la coincidencia exacta de posiciones del tipo log(2^k·m) con el espaciado de log n, no sólo los huecos.

## 6. Limitaciones
- Optimizador de mínima suave: cota inferior del máximo de Galerkin; no hay certificado dual.
- V* libre en T ≥ 1.6 sin convergencia en N; V*⁺ convergido salvo Beurling 2.02 en T = 2.0.
- Multiplicidades con umbral del 1 %: indicativas.
