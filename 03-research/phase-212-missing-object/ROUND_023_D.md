# Ronda 23, memo D — ¿identidad exacta de la cancelación por átomo para vectores generales?

Puerta de selección. Sin derivaciones nuevas ni cómputos. Objeto: 𝔸_M = Arch_M − Div_M − Near_M (P47 prop:AM).

## 0. Qué está probado y qué es numérico (lectura de las fuentes)
- **Identidad (PROVED, elemental, clase W7).** Para s = m^{−½} exacto:
  sᵀ(Div+Near)s = 2Σ_N N^{−½} log N · E_M(N), E_M(N) = Σ_{m≤M} m^{−½} c₀(log(N/m))
  (fase 190 EXP_003 §4; comprobada a 12 dígitos, M = 800). Usa Λ∗1 = log una vez, linealmente.
- **Familia s_w = m^{−½}w(m/M)** (P47 prop:shape-family, l.≈9008–9045, (i)–(iii) PROVED): colapso
  sᵀ𝔸s = sᵀArch s − Σ_{N<Me^{2T₀}} N^{−½} D_w(N) E_w(N); (iv) Ψ_w, análogo continuo del átomo n, con ∫Ψ_w = 0.
  EI_002 Thm 3(iii) (fase 192): «Div ≈ −Near» como identidad, con restos: borde a escala M (no estimado),
  defectos de divisores pequeños y términos duales de Poisson (Thm 3(ii)).
- **Mecanismo por átomo (PROVED-elemental, no específico del peso).** Para s_m = S(m) suave,
  Σ_m s_m c₀(log(kn/m)) es suma de Riemann de (kn)^{½}∫S(kn e^{−u})e^{−u}c₀(u)du, nula para S = y^{−½} por la
  condición de Tate ∫c₀(u)e^{u/2}du = 0 (lem:transl(iii)). Error de discretización grande sólo si kn ≲ 1/(2T₀).
- **NUMÉRICO.** Que en el *minimizador* (solapamiento 0.993 con m^{−½}) cada n ≥ 5 cancele a 3 decimales:
  δ_n = Near_n + Div_n = +0.169, +0.120, +0.027 (n = 2,3,4), +0.003 (n = 5), ≤ 0.001 después; Σδ_n = 0.322 = Arch − λ
  (EXP_003 §4, M = 800, T₀ = 0.3). E_M(2,3,4) = 0.778, 0.636, 0.287; |E_M(N)| ≤ 2·10⁻⁶ en 50 ≤ N ≤ 400 (NUMÉRICO;
  decaimiento ARGUED por Euler–Maclaurin). El signo lo decide la corrección de 0.7 % del minimizador respecto de m^{−½}
  (EXP_003 §2–4), que NO está en la identidad.
- **L2_BUILD_030 (fase 188) §§1–3**: Near = resto de resolución finita (muestra Toeplitz de Ξ_{F₀} menos coincidencias
  exactas) de |P_s|²V; identidades PROVED, sin signo propio (§2).

## 1. Antecedente más cercano
(a) **211 ROUND_001_A §1** (Poisson en ℤ / Mellin–Euler–Maclaurin a lo largo de polinomios de Dirichlet): para s
general, cada átomo se escribe como parte continua + frecuencias duales no nulas; NO-GO para el signo (sobrevive a cΛ,
a_P, modificación finita y Beurling a primer orden; §3, «Result»). (b) **192 EI_002 Thm 3(ii)–(iii)**: la misma
descomposición por átomo, con «Div ≈ −Near» como identidad y restos dual/borde/divisores pequeños. (c) **191 SPEC_B
T*₃/C*₃**: colapso por divisores D_w(N) = 2c log N − defectos; C*₃ OPEN, REF-D para η ≤ η₀ (NUMÉRICO); T*₃ NUMÉRICO-falso
bajo modificaciones finitas. (d) **193 CA_K_002 Thm 3.2(iii)** y **CA_M_001**: en sitios primos Arch ≥ Near es la
afirmación misma (equivalente bajo la premisa), no un mecanismo. (e) **188 N_BUILD_022 §3**: NO-GO PROVED, ninguna
identidad derivada de 1∗Λ = log alcanza la parte no divisora (𝒟_M = Near).

## 2. Objeto pedido, con fórmula
Lo único que puede escribirse para s general es, por átomo n,
  δ_n(s) := Div_n(s) + Near_n(s) = (v_n/2) Σ_{m,k≤M} s_m s_k c₀(log(kn/m))  (suma completa, kn = m incluido),
y la «cancelación» exacta exige elegir un interpolante S de s y escribir δ_n(s) = (v_n/2)[𝓘_n(S) + 𝓔_n(s,S)], con
𝓘_n la integral (nula sólo si S ∝ y^{−½} en el soporte de la ventana) y 𝓔_n el resto de discretización/Poisson.
Entonces 𝔸_M(s) = Arch(s) − Σ_n δ_n(s) es tautológico (suma por átomos de la definición), y la comparación «Σδ_n con
Arch en un paso» es literalmente (S). No hay operación nueva: para s fuera de la familia s_w, 𝓘_n ≠ 0 y es de tamaño
completo; la elección de S es exactamente la transferencia red→continuo de ROUND_001_A / EI_002 Thm 3.
No se pudo escribir un objeto distinto que dé δ_n(s) con significado de «defecto» para s general sin ese paso.

## 3. ¿Evita el motivo de fracaso?
No. (i) δ_n(s) es (v_n) × (forma cuadrática del monoide independiente del peso): afín en el peso y firmado átomo a
átomo → F3 y B″ (NEAR_DOSSIER §«Linealidad en Λ», ítems C3, CA_C_002, CA_H_002, CA_K_002). (ii) La cancelación de los
n ≥ 5 es Tate + suma de Riemann: vale para todo peine de densidad 1 sobre vectores suaves (EXP_005 R5, clase (a));
no distingue Λ de ningún control. (iii) La parte que sí depende del peso (Σ_{d|N}a(d) = log N) entra linealmente una
vez (W7, EXP_005 R7) y sólo en vectores tipo m^{−½}. (iv) El residuo n = 2,3,4 es el conjunto de contacto de las
ventanas certificadas (thm:log5A): restringirse a él es (S) con otro nombre (también L2_BUILD_031 Thm E: subespacios
restringidos equivalen al objetivo completo).

## 4. Conexión con 𝔸_M ⪰ 0 y controles
La desigualdad necesaria sería Σ_n δ_n(s) ≤ Arch(s) ∀s, ∀M, con precisión M^{−3} (F4). No hay paso con nombre que
falle bajo los controles, porque los controles NO rompen la identidad por átomo donde ésta vive:
- **Dónde fallan los controles (EXP_002 §§3–4, NUMÉRICO).** El autovector negativo es un paquete suave de enteros
  consecutivos en la escala superior (pico ≈ 0.15–0.25 M), no m^{−½}. Allí Div ≈ 0 (pocas relaciones exactas kn = m
  entre enteros consecutivos grandes) y Near ≈ Arch + |λ|. Ejemplo pert₂(+10⁻⁵), M = 1500: Arch 120.12, Div 0.60,
  Near 119.52, λ = −7.9·10⁻⁴. Por átomos (M = 800): Near_n = +41.9 (n = 2), +27.9 (3), +10.5 (4), −14.1 (5): átomos
  pequeños, tamaño O(M), sin cancelación por átomo **ni para Λ** en ese vector (la cancelación es propiedad de
  S ≈ y^{−½}, no del peso). El control cambia la forma en ε·(Near₂ ≈ O(M)) frente a un margen ≍ M^{−3}: umbral
  c*(M) ≍ M^{−3} (EXP_002 §2). Borrados a₃/a₅: λ −1.5/−2.4 ya en M = 50; Beurling ±0.02: −1.5 en M = 50.
- **Bajo cada control**: (peso sustituido) la identidad C3 se rompe exactamente en Σ_{n|N}a(n) − log N, pero sobre
  m^{−½}, donde la forma tiene margen 2.58/7.26 y no decide el signo; (potencia borrada) idem, un término lineal;
  (Beurling) la red ℤ deja de ser el monoide y la suma de Riemann cambia, otra vez linealmente. Ninguno de esos
  pasos es donde fallan los controles (paquetes de escala superior), así que el objeto no ve el fallo: F1 no se cumple.

## Veredicto
**NO PASA (repetición + sin mecanismo).** La versión exacta para s general es la descomposición por Poisson/Riemann
de ROUND_001_A y EI_002 Thm 3 (NO-GO), sus piezas δ_n son afines en el peso y firmadas por átomo (F3), y comparar Σδ_n
con Arch es (S) o el candidato de CA_K_002 reetiquetado. Probado: identidad C3 en s = m^{−½}, colapso en s_w, mecanismo
Tate+Riemann. Numérico: cancelación a 3 decimales en el minimizador, residuos en n = 2,3,4, tamaños de E_M y los datos
de paquetes de los controles.
