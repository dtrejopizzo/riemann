# Anexo 170 — tramo 3: archivos R170_841 a R170_862

Registro de lectura de la fase 170, archivos 841–862 (no existe 842; hay dos archivos 858). Notación de
las memos: ventana (−T,T), N ≥ e^{2T}, P = P_T (ventana), Q = I−P (exterior), Π primitiva, R_T = P−Π
(bloque de Tate, rango dos), S_N = Σ_{m≤N} m^{-1/2}τ_{log m}, L_M = Σ_{d≤M} Λ(d)d^{-1/2}τ_{log d},
K_N = Σ_{k≤N}(log k)k^{-1/2}τ_{log k}, H_{M,N} = L_M S_N − K_N, C_N contínuo polar, Z_N = S_N − C_N,
dilatación U_r f(t) = r^{-1/2}f(t/r), Ḃ = d/dr (U_r^{-1}BU_r)|_{r=1}, τ̇_a = −a∂_tτ_a. «VIR–LB» es la
desigualdad 𝒱_{Λ,T}(F) ≤ 0 en el radical N_T^ε = {F ∈ ker H_T : JF = εF} de una ventana de primer
contacto hipotética, con 𝒱 = (1/2π)∫τm'(τ)|F̂|² − Σ_{n<e^{2T}} 2Λ(n)n^{-1/2} log n c_F'(log n) +
2Re⟨F, t r_F'⟩. Toda la cadena 841–862 trabaja bajo esa hipótesis de primer contacto (argumento por
contradicción en la ventana mínima), no sobre una identidad global del tipo (G).

Cotejo contra el terreno no excluido de la ronda 1 de la 212:
(T1) cuadrados continuos con aritmética en índice/pesos de dilatación; (T2) Gram de incidencia de
divisores E diag(Λ) Eᵀ; (T3) Σ_{d|n}Λ(d) = log n convertida en cota cuadrática; (T4) residuo común:
apareamientos mixtos de Poisson–Chebyshev (H_{M,N}, E_N) como Σ_{k>N} h(k)|ℓ_k(F)|², h ≥ 0.

---

## 1. Entradas por archivo

### R170_841 — Derivada de la hipérbola finita, no-go de primer orden y residuo orientado

**Objeto.** Peso real a con a(1)=0; L_M^a, H^a_{M,N} = L_M^a S_N − K_N = Σ_{k≤MN} q^a_{M,N}(k)k^{-1/2}τ_{log k},
q^a(k) = Σ_{dm=k, d≤M, m≤N} a(d) − 1_{k≤N} log k. Identidad de Ward de escala (Teor. 3.1):
Ḣ^a = −Σ q^a(k) log k k^{-1/2}∂_tτ_{log k}; L̇S + LṠ − K̇ = Ḣ; Π_{≤N}Ḣ^a = −Σ_{k≤N} δ_a(k) log k
k^{-1/2}∂_tτ_{log k}, δ_a = a∗1 − log; para Λ el bloque k ≤ N se anula y queda
Ḣ^Λ = −Σ_{N<k≤MN} h_{M,N}(k) log k k^{-1/2}∂_tτ_{log k}, h ≥ 0 (3.8). Canal antisimétrico
𝒜_{M,N} = L̇_M S_N − L_M Ṡ_N con coeficiente en fibra completa
β_Λ(k) = Σ_{d|k}Λ(d) log(d/(k/d)) = 2Σ_{d|k}Λ(d)log d − (log k)². Descomposición
2L̇S = Ḣ + K̇ + 𝒜 (4.5). Varianza Σ_Λ(k) = Σ_{d|k}Λ(d)(2log d − log k)² ≥ 0 con
|β_Λ(k)|² ≤ (log k)Σ_Λ(k) (Cauchy–Schwarz con la probabilidad Λ(d)/log k). Derivada explícita del
contínuo polar Ċ_N (5.5), con cara de frontera −(log N)√N f(t+log N). Libro mayor (5.8): β interior ⊕
hipérbola incompleta k>N ⊕ Ċ_N ⊕ [P_T,Z_N] ⊕ Tate.

**Afirmaciones.** Declara PROVED: derivada sincronizada (3.4)–(3.8); defecto para peso alterado y
para DH con peine ordinario (3.9); separación de piernas y β_Λ; Σ_Λ y la cota; Ċ_N; no-go de la clase
𝒞_fib^{(1)} (Teor. 6.1). Declara FALSE: signo uniforme de β_Λ (β(p^j) = j(log p)² > 0, β(12) < 0 por
(4.7)); que la varianza oriente β; signo del virial independiente de la fuente (§6.1: familia
F_ξ = φ cos ξt con c'_{F_ξ} ≍ ξ de ambos signos, término arquimediano O(1)). Lo que el texto sostiene:
coincide; el no-go 6.1 es un argumento de clase (cualitativo, «condición 5» se define como no introducir
identidad física nueva), correcto dentro de esa definición.

**Dónde se detuvo.** La única cantidad de primer orden que sobrevive (β_Λ) cambia de signo; la
completación positiva es de segundo orden (par bajo inversión de la diferencia de piernas) y no orienta
un primer momento. Möbius devuelve a Λlog = μ∗log² − Λ∗Λ (no-go de Selberg, apareado con c_F', sin
signo). La cola h ≥ 0 vive sobre ∂_tτ (derivada de correlación) y no da signo. Queda OPEN una «ley de
Green antisimétrica de frontera» (7.1) que oriente 𝒜 con el libro mayor (5.8).

**Corrección posterior.** R170_843 la continúa (reensambla β en una forma Hankel positiva).

**T1–T4.** T1: no (sólo un cuadrado por fibra, Σ_Λ). T2: parcial — agrupa por fibras k = dm con peso
Λ(d) (incidencia), pero no la factorización de Gram; la diagonalización por fibras se declara
prohibida (cambia la Gram física). **T3: sí, directamente** — convierte Σ_{d|k}Λ(d) = log k en la
probabilidad Λ(d)/log k y en la cota cuadrática |β|² ≤ (log k)Σ_Λ; falla porque la cota es par y no
orienta el primer momento β. **T4: sí** — la cola Ḣ^Λ con k>N y h ≥ 0 es exactamente el residuo de la
hipérbola tras usar δ_Λ = 0, pero va acoplada a ∂_tτ_{log k}, no a |ℓ_k(F)|²; sin signo.

### R170_843 — Green antisimétrica de la hipérbola: signo de Laplace, colisión de soporte, levantamiento Hankel mínimo

**Objeto.** 𝒜^raw = L̇S − LṠ y 𝒜^ren = L̇Z − LŻ = 𝒜^raw − (L̇C_N − LĊ_N); maestra
2L̇Z = Ḣ̃ + K̇^Z + 𝒜^ren. β_{M,N}(k) truncado (1.8); 𝒜^raw = −Σ_{k≤MN} β_{M,N}(k)k^{-1/2}∂_tτ_{log k}.
Transformada de Laplace K_F(a) = ∫F e^{-at}: K_{∂_tτ_{log k}F}(a) = a k^{-a}K_F(a), luego
K_{𝒜^raw F}(a) = −a B_{M,N}(s)K_F(a), s = a+½, B_{M,N} = ℓ_M σ_N' − ℓ_M' σ_N (Wronskiano de Dirichlet).
En el límite B_Λ(s) = ζ'' − 2ζ'²/ζ = −ζ²(1/ζ)'' > 0 para s>1. Retícula Gamma a_m = 2m+½, s_m = 2m+1;
observador (𝓡_δ F)_m = e^{-a_m(T+δ)}K_F(a_m), G_δ = 𝓡_δ*𝓡_δ (Hankel). Energía
𝓔^β(F) = −Re⟨𝓡F, 𝓡𝒜^raw_{N,N}F⟩ = Σ_m a_m B_{N,N}(s_m)e^{-2a_m(T+δ)}|K_F(a_m)|² > 0.
Collar tipado (6.6)–(6.8): 𝓡Π𝒜^rawΠ = −D_{β,N}𝓡Π − 𝓡(R+Q)𝒜^rawΠ.

**Afirmaciones.** PROVED: 𝒜^raw finito con todas las fibras; colinealidad de las dos rutas a r=1
(2.2)–(2.3) (toda polarización alternante por ruta es cero); forma de Green comprimida = concomitante
de soporte ⟨g,[P,B]w⟩ (4.2); B_Λ = −ζ²(1/ζ)''; positividad finita uniforme B_{N,N}(s) > 0 para s ≥ 3,
N ≥ N_0 absoluto (Teor. 5.1, por continuidad y cola convergente); energía Hankel estricta; collar
tipado. CITED: B_Λ > 0 en todo s > 1 (teorema publicado de concavidad estricta de 1/ζ en (1,∞)).
FALSE: Herm(P𝒜P) es sólo término de borde; la paridad anula la parte hermítica; uso de λ_δ tras filtrar
por 𝒜 o Z (4.11). Declara «FALSE»: separación de pesos por la energía Gamma aislada (§5.4: muchos pesos
positivos alterados también dan Wronskiano positivo en s_m ≥ 3); «PROVED» separación en el semiplano
completo para un peso alterado — lo que el texto sostiene es sólo el ejemplo δ_2, B_{δ_2}(s) =
2^{-s}ζ(s)(log 2 + ζ'/ζ) < 0 cerca de s=1. OPEN: levantamiento físico (7.3) Π G_δ 𝒜^ren Π = H_T𝒦 +
𝓑^pol + 𝓑^supp + 𝓑^Tate y (7.4).

**Dónde se detuvo.** Pasar de la energía Hankel con signo al operador físico renormalizado añade
L̇C_N − LĊ_N, PZ_NQ, QZ_NP, R_T y el virial de Tate, sin signo; el primer contacto sustituye el
solapamiento positivo ⟨F_δ,E_TF⟩ por uno filtrado sin signo. No-go de la clase 𝒞_Green^{(1)}
(Teor. 8.1): Green estándar con 𝒜, compresión, reflexión, XF, F_δ, sin operador Hankel entre piernas.

**Corrección posterior.** Cabecera añadida por R170_844: (6)–(7) son sólo formales para δ pequeño;
K_{C_NF}(a) = N^{a+½}/(a+½)·K_F(a), el observador interior exige δ > log N; la factorización estática
queda bloqueada por Fredholm. Teor. 5.1 y (5.18) no se afectan.

**T1–T4.** **T1: sí** — G_δ = 𝓡*𝓡 es un cuadrado continuo (observación de Laplace en la retícula
Gamma) con pesos aritméticos a_m B_{N,N}(s_m); su signo existe pero no separa pesos (§5.4) y no se
levanta a la forma física. T2: no. **T3: sí** — usa δ_Λ = 0 para reescribir β y obtener
Σβ_Λ k^{-s} = −ζ²(1/ζ)''; el signo sale de la concavidad citada, no de una cota cuadrática por
fibra. **T4: parcial** — retiene la cola Σ_{N<k≤N²} β_{N,N}(k)k^{-s} dentro de B_{N,N}; la cola
sincronizada h ≥ 0 se mantiene separada.

### R170_844 — Levantamiento físico del Wronskiano: expansión completa, obstrucción de Fredholm y derivada covariante mínima

**Objeto.** Detector 𝒞_β = Π𝓡*D_{β,N}𝓡Π > 0; Wronskiano polar 𝒫^pol_N = L̇_N C_N − L_N Ċ_N.
Puerta de dominio (1.6a)–(1.6c): 𝓡_δ C_N acotado sólo si δ ≥ log N. Identidad (2.4)
ΠG_δ𝒜^renΠ = −𝒞_β − ΠG_δ𝒫^polΠ. Símbolo polar (3.2b)–(3.2c): K_{Ċ_NF}(a) = c_N(s)(1 − 1/(2s) − a log N)K_F,
c_N = N^s/s; π_N(s) = c_N ℓ_N[a(log N − μ_N(s)) − 1 + 1/(2s)], μ_N = −ℓ_N'/ℓ_N ≤ μ_∞(3) =: M_3 para s≥3.
Cola sincronizada Θ_N(s) = Σ_{N<k≤N²} h_{N,N}(k)log k k^{-s} ≥ 0 con K_{Ḣ F}(a) = −aΘ_N K_F (4.4).

**Afirmaciones.** PROVED: (2.3), (2.4), símbolo polar y Re 𝔭(F,F) > 0 tras agrandar N_0 ≥ e^{M_3+1}
(3.2i); cola sincronizada con símbolo positivo; defecto para δ_a ≠ 0 / DH con peine ordinario;
condición necesaria del levantamiento: 𝒱 = Re 𝔭_pol en el radical (5.4); Teor. 6.1 (criterio de
Fredholm: 𝒯 = H𝒦 + 𝓑 exige P_N(𝒯 − 𝓑) = 0). Consecuencia: (5.4) con (3.2i) daría 𝒱 > 0 en el
radical, signo opuesto — el levantamiento estático con orientación (0.5) queda REFUTADO, no pendiente.
Bloque de Tate estático R_T𝒜Π «FALSE IN TYPE» como virial de Tate (éste depende de Π̇, §5.1).
«FORMALLY BUILT»: derivada covariante ∇^PC = d/dr(Π_{rT}𝔓^ren(r)Π_{rT}) (8.1)–(8.2). OPEN: Ward–PC
covariante. Lo que el texto sostiene: correcto; la refutación usa la positividad de π_N, que se prueba
con un argumento de medias monótonas válido.

**Dónde se detuvo.** La suma de bloques soporte/Tate/polar es tautológica (3.10): no queda término
identificable con el virial. δ no puede quedar libre (7.1)–(7.2): Re 𝔭 → 0 cuando δ → ∞.

**Corrección posterior.** R170_846 señala que 𝔓^ren no estaba definido como operador; (8.1) queda
mal tipado hasta elegir lado y polarización.

**T1–T4.** T1: sí (misma observación Gamma, ahora con símbolo polar; la positividad aparece con signo
contrario al requerido). T2: no. T3: hereda δ_Λ = 0. **T4: sí** — Θ_N(s) ≥ 0 es la cola k>N observada
como multiplicador positivo en coordenadas Gamma (una forma Σ_m a_mΘ_N(s_m)e^{…}|K_F(a_m)|² ≥ 0), pero
en la métrica Hankel, no en la física, y no cierra con el resto del libro mayor.

### R170_845 — Conexión de Tate móvil: cálculo exacto y puerta Ward–PC restante

**Objeto.** Columnas transportadas φ_∓(r,t) = e^{∓rt/2}; Gram G_T = 2[[sinh T, T],[T, sinh T]];
Π̇F = −ΦG^{-1}Φ̇*F para F primitivo (1.5); por paridad, b_ε = e^{-t/2} + εe^{t/2}, q_ε = 4(sinh T + εT),
ḃ_ε = t b_ε', Π̇F = −b_ε⟨ḃ_ε,F⟩/q_ε. Identidad (0.1): 2Re⟨Π̇F, r_F⟩ = −2Re⟨F, t r_F'⟩ si r_F = ρb_ε.

**Afirmaciones.** PROVED: derivada de la proyección primitiva, rango uno por paridad, «Π̇ = menos
virial de Tate para el operador completo». DEFINED: defecto d^Tate = R_T𝔓^renF − r_F. OPEN: su
anulación y la derivada de Fourier = virial arquimediano.

**Dónde se detuvo.** Falta probar la igualdad de puerto R_T𝔓F = r_F (0.2).

**Corrección posterior.** Cabecera de R170_846: §4 era condicional; 𝔓 no definido; el defecto (4.1)
no está definido hasta elegir portador. (1.4)–(3.2) quedan válidos.

**T1–T4.** No toca ninguno (geometría de la proyección de Tate).

### R170_846 — Auditoría del portador Ward–PC y filtro transversal del corpus

**Objeto.** PC finita del Paper 47: Y = S_N A_M 𝓕 = {X,E_N} − L_M*E_N − JH_{M,N} − H_{M,N}𝓕 = Z
(igualdad, no operador distinguido). Portador hermítico mínimo 𝒲^ren = ½(S_N^ren A_M𝓕 + 𝓕A_M(S_N^ren)*);
defecto escalar Δ^Tate = ω^ε − ρ_F con ω^ε = ⟨𝒲F, b_ε⟩/‖b_ε‖².

**Afirmaciones.** WITHDRAWN: aplicación a 𝔓 no definido. DEFINED: 𝒲^ren, Δ^Tate. COMPLETED: filtro del
corpus (ocho requisitos: residuos de Hardy polares de R161_009 no son proyección; límites lineales de PC
son tautología; puerto de Tate comprimido ≠ collar cruzado; velocidad polar y nacimientos enteros
juntos; variación lineal de coeficientes PC es cero algebraico (R162_305); cuadrados PC, límites
lineales y Λ∗1 = log tras regularizar excluidos; anomalía de esquina M/N; Wronskiano y cola de
841–844). OPEN: WPC–Tate (4.1)/(4.2) y WPC–bulk (4.3).

**Corrección posterior.** Cabecera de R170_847: el portador (1.1) no es nuevo (anticonmutadores y
potencias hermíticas de R161_062–064) y hermitianiza después de recombinar las piernas; (4.1)–(4.3)
retiradas como ruta preferida.

**T1–T4.** No; es auditoría. Registra que «Λ∗1 = log tras regularizar» está excluido (relevante para T3).

### R170_847 — Curvatura PC de dos parámetros antes de hermitianizar

**Objeto.** Derivación antidiagonal ∂_− = (∂_r − ∂_q)|_{1,1} con L_M(r), Z_N(q):
∂_−[L(r)Z(q)] = 𝒜^ren. Forma 𝔚^−(F,G) hermitianizada de ∂_−⟨F, Π_{rT}G_δL(r)Z(q)Π_{rT}G⟩ (2.2)–(2.3).
PC de dos escalas (Teor. 4.1): con X_r = rX, K_N(r,q) = (r/q)Σ log n n^{-1/2}τ_{log n/q},
A_M(r) = 𝓜_r − L(r) − L(r)*, E_N(r,q) = S(q)𝓕_r − JS(q), H(r,q) = L(r)S(q) − K(r,q):
S(q)A(r)𝓕_r = {X_r,E} − L(r)*E − JH𝓕_r − H𝓕_r ∀ r,q. Jet: ∂_−K = 2K_N + K_N^{(2,∂)},
K^{(2,∂)} = Σ(log n)² n^{-1/2}∂_tτ_{log n}.

**Afirmaciones.** PROVED: ∂_−(LZ) = 𝒜^ren; bulk Wronskiano dentro de la forma (con la puerta de
dominio); PC de dos escalas (la prueba repite la de PCfinite; el factor r/q es necesario para
[X_r,S(q)] = −K(r,q)). COMPUTED: jet de K. OPEN: acoplamiento con PC completa y virial arquimediano;
cancelación Π̇/Tate contra el residuo polar.

**Dónde se detuvo.** La forma no contiene el término arquimediano; hay que derivar todo el lado
S(q)A(r)𝓕_r.

**T1–T4.** T1: sí, hereda G_δ. T4: parcial (H(r,q) a dos escalas, sin signo). T2, T3: no.

### R170_848 — Curvatura PC con el Fourier derecho eliminado

**Objeto.** Multiplicar la PC de dos escalas por 𝓕_r (𝓕_r² = I): S(q)A(r) = {X_r,E}𝓕_r − L*E𝓕_r −
JH𝓕_r − H. Curvatura 𝒞 = SȦ − ṠA = SṀ − Ṡ𝓜 − 𝒜^raw − (SL̇* − ṠL*). ṁ(τ) = −τm'(τ), luego
⟨F,Ṁ F⟩ = −(1/2π)∫τm'|F̂|² (menos el término arquimediano del virial). L̇_M =
−Σ Λ(n)log n n^{-1/2}∂_tτ_{log n}; d/dr⟨F,Π_{rT}A(r)Π_{rT}F⟩ = −𝒱 bajo (REG) (identidad conocida).

**Afirmaciones.** PROVED: PC sin Fourier derecho; curvatura; aparición de −𝒜^raw con la orientación
correcta; Ṁ; identificación del jet interior de A con arquimediano+primo. OPEN: extraer Ȧ de SȦ sin
invertir S_N; agrupar los siete residuos de §5.

**Dónde se detuvo.** No se puede reemplazar ⟨F,G_δSȦF⟩ por ⟨F,ȦF⟩ sin invertir S_N (5.1).

**Corrección posterior.** R170_849 resuelve la extracción en la métrica física.

**T1–T4.** No toca (algebra PC); T1 sólo por el observador heredado.

### R170_849 — Extracción causal finita y choque entre métrica física y métrica Hankel

**Objeto.** PS_NP = P + R_{N,T}, R^{J_T} = 0 con J_T = ⌊2T/log 2⌋+1 (nilpotencia por desplazamientos
≥ log 2); B_{N,T} = (PS_NP)^{-1} = Σ_{j<J_T}(−R)^j. Extracción exacta (2.2):
PȦF = BP𝒞F + BPṠPAF + BPṠQAF − BPSQȦF; en primer contacto PAF = r_F. Defecto métrico
𝔇^met = Re⟨(B* − G_δ)F, P𝒜^rawF⟩ (3.3). Observador modificado G^ext = 𝓡*diag(σ_N(a_m)^{-1})𝓡 que extrae
S_N en coordenadas Gamma, σ_N(a) = Σ_{n≤N} n^{a−½}.

**Afirmaciones.** PROVED: nilpotencia, inverso finito, extracción (2.2), identificación de puertos,
extracción positiva de Laplace (4.1)–(4.3). FALSE IN GENERAL: igualdad entre métrica física y Hankel
(𝓡*D𝓡 es compacto; la identidad no). OPEN: MET–WARD (la diferencia B* − G^ext tiene diagonal ≤ 0 o se
cancela en ker H_T); el texto dice que postularla equivale a postular el puente de signo.

**Dónde se detuvo.** El signo de 843 vive en la métrica Hankel; la extracción exacta pide la métrica
dual de (PSP)^{-1}; no hay identidad que las identifique.

**Corrección posterior.** R170_850 (B = PMP); R170_851 (los puertos PṠP y PṠQ crean átomos; sólo la
suma es legítima).

**T1–T4.** **T1: sí** — dos extracciones: física (pierde signo) y Gamma con pesos 1/σ_N (conserva signo
pero produce virial filtrado). T2: parcial (inverso finito del peine). T3, T4: no.

### R170_850 — Ley aritmética del Wronskiano extraído por Möbius

**Objeto.** B_{N,T} = PMP con M = Σ μ(n)n^{-1/2}τ_{log n} (causalidad: ninguna trayectoria sale y
vuelve). γ_Λ = μ∗β_Λ = −Σ_{d|n}μ(d)(log d)²: γ(p^k) = (log p)², γ(p^aq^b) = −2 log p log q,
γ = 0 si ω(n) ≥ 3 (diferencia finita total de un polinomio cuadrático). Forma extraída (4.2):
Σ_p(log p)²Σ_k p^{-k/2}Re⟨F,∂_tτ_{k log p}F⟩ − 2Σ_{p<q}log p log q Σ_{a,b}(p^aq^b)^{-1/2}Re⟨F,∂_tτ_{a log p+b log q}F⟩
+ 𝒯^cut.

**Afirmaciones.** PROVED: B = PMP, extracción interior, ley γ, soporte ω ≤ 2, uniformidad en T.
RETAINED/OPEN: puerto de corte 𝒯^cut. OPEN: completación con signo del canal de dos bases primas (se
sugiere un objeto de rango dos en la red de bases primas, completando el cuadrado; no afirmado).
Verificado: (3.4) da −x² para r=1 y 2x₁x₂ para r=2, correcto.

**Corrección posterior.** Cabecera de R170_851: γ = Λlog − Λ∗Λ; con W = Λlog + Λ∗Λ vuelve al no-go de
Selberg; la cola sincronizada es cero en fibras bajas; (0.2) no es completación positiva nueva.

**T1–T4.** T2: parcial (inverso de Möbius del peine; el canal −2 log p log q sugiere una forma
cuadrática en bases primas, no construida). **T3: sí** — usa Λ∗1 = log y μ∗1 = δ; el resultado
coeficiente a coeficiente no tiene signo (canal cruzado negativo) y las correlaciones ∂_tτ tampoco.
T1, T4: no.

### R170_851 — Colisión de Selberg de la ley de Möbius y átomos de frontera del puerto extraído

**Objeto.** γ_Λ = Λlog − Λ∗Λ (vía B_Λ/ζ = −𝓛' − 𝓛², 𝓛 = −ζ'/ζ); W = μ∗log² = Λlog + Λ∗Λ;
γ + W = 2Λlog. Átomos: ∂_t(Pg) = Pg' + g(−T+)δ_{−T} − g(T−)δ_T y opuestos para Q; sólo
PṠ(P+Q)AF = PṠAF es legítimo. Extracción corregida (4.1): PȦF = BP𝒞F + BPṠAF − BPSQȦF; puerto
combinado 𝒫^comb = BPṠAF − BPSQȦF.

**Afirmaciones.** PROVED: γ = Λlog − Λ∗Λ, γ + W = 2Λlog, colisión con Selberg (2.2) sin signo,
átomos y su cancelación en el puerto combinado. REJECTED: identificar la cola sincronizada con W
(es cero para k ≤ N). OPEN: proyección de Tate del puerto combinado y cancelación con Π̇.

**Corrección posterior.** R170_854 matiza: W interior sí está en PC, en el segundo jet K²; luego
R170_856 muestra que ese W se cancela con un −W del bloque Poisson–X.

**T1–T4.** **T3: sí** — Selberg como segunda identidad sobre Λ; reproduce el no-go de deconvolución
(W ≥ 0 apareado con c_F' sin signo). T4: registra que la cola k>N no aporta en el interior.

### R170_852 — Defecto de Tate exacto del puerto combinado

**Objeto.** h_ε = B*b_ε con PS_N*Ph_ε = b_ε; en primer contacto PAF = ρ_Fb_ε, QAF = ℓ_F. Coordenada
ω^comb = (1/q_ε){ρ_F⟨PṠ*Ph,b⟩ + ⟨QṠ*Ph,ℓ_F⟩ − ⟨QS*Ph, QȦF⟩}; defecto
Δ^Tate = (κ^ε − 1)ρ_F + 𝓔^{ext,1} − 𝓔^{ext,2}, κ^ε = ⟨PṠ*Ph,b⟩/q_ε (sólo geometría del peine).
Residuo de conexión 𝔑^Tate = 2Re⟨Π̇F, Δ^Tate b_ε⟩.

**Afirmaciones.** PROVED: dual causal, (0.5), (0.6), compatibilidad con átomos. DEFINED: 𝔑^Tate.
OPEN: cancelación con polar + soporte. Pruebas de falsificación: N=1 da κ = 0 (no hay cancelación
automática); κ no ve Λ (la cancelación debe pasar por los residuos exteriores); sin exterior queda
(κ−1)ρ_F.

**T1–T4.** No toca ninguno de forma directa (álgebra de puertos).

### R170_853 — Curvatura del grafo causal y desajuste aritmético exterior

**Objeto.** C_{N,T} = PS*P, 𝒟_{N,T} = QS*P C^{-1}; h = C^{-1}b, q = 𝒟b = QS*Ph (S*Ph = b + 𝒟b,
grafo causal). Desajuste exterior z_F = ℓ_F − ρ_F q. Descomposición (2.2):
q^Gram Δ^Tate = ρ_F 𝔎(F) + ⟨q̇^0, z_F⟩ − ⟨q, ż^0_F⟩ con 𝔎 puramente causal (sin Λ, sin Gamma).

**Afirmaciones.** PROVED: descomposición, aislamiento de la curvatura causal 𝔎, identificación del
residuo como Wronskiano exterior. FORBIDDEN/TAUTOLOGICAL: imponer z_F = 0 (repite L161.6, reciprocidad
exterior). OPEN: ley (5.1) Re(⟨q̇^0,z⟩ − ⟨q,ż^0⟩) = 0 desde la PC de dos escalas.

**T1–T4.** T4: parcial — z_F mide exactamente la parte del exterior QAF no predicha por el peine; no
se convierte en suma de cuadrados. Resto: no.

### R170_854 — Ley de Green graduada para el Wronskiano exterior

**Objeto.** Con producto real (u,v) = Re⟨u,v⟩ y jets congelados ḃ^0 = PṠ*Ph, q̇^0 = QṠ*Ph,
ȧ^0 = PȦF, ℓ̇^0 = QȦF: Teor. 2.1 (h, P(SȦ − ṠA)F) + ((q̇^0,z) − (q,ż^0)) = (b,ȧ^0) − ρ(ḃ^0,b);
𝔚_bulk + 𝔚_ext = 𝔚_Tate. Realización ℤ/2-graduada: 𝔻_{L,S} = [[0,L],[S,0]],
[𝔻̇,𝔻] = Γ𝒜^raw (conmutador ordinario; el anticonmutador da el canal sincronizado). Toda
representación cuadrática del corriente es indefinida (3.4). Segundo jet: M K^{(2,∂)} = W, luego
−M𝒜^raw + MK^{(2,∂)} = −2L̇ (4.6). Fórmula general μ∗β_a = Da − (μ∗a)∗D1 (4.7) (verificada).

**Afirmaciones.** PROVED: polarización antidiagonal, ley (0.4), realización graduada, indefinición de
toda completación por cuadrados, K² extraído por Möbius = W, γ + W = 2Λlog «dentro de PC», corrección
de localización respecto de 851. OPEN: cancelación de 2MK y colas; minimalidad ⟹ (0.5); ley exterior.
Lo que el texto sostiene: la identidad (0.4) es una inserción de I = P+Q, correcta; la afirmación de
que γ + W sobrevive en PC es retirada por 856.

**Dónde se detuvo.** La minimalidad controla la diagonal en F, no el apareamiento cruzado con el dual
causal h; diferenciar PAF = ρb supondría la tangencia buscada.

**Corrección posterior.** R170_855/856: K² no sobrevive como sumando independiente.

**T1–T4.** **T3: sí** — la reconstrucción del peso 2Λ(n)log n por γ + W usa Λ∗1 = log, μ∗1 = δ y
Selberg; queda refutada como contribución física en 856. T1: no (explícitamente: cuadrar el sector
graduado da o ratio-comb con métrica positiva, o forma indefinida con supertraza). T2, T4: no.

### R170_855 — Ensamblaje de Möbius de los dos jets

**Objeto.** ∂_−K_N = 2K_N + K^{(2,∂)}; M K^{(2,∂)} = Σ_{k≤N} W(k)k^{-1/2}∂_tτ_{log k}; Teor. 3.1:
−M𝒜^raw + MK^{(2,∂)} = −2L̇ en toda fibra completa.

**Afirmaciones.** PROVED (coeficientes): jet, M K² = W, γ + W = 2Λlog, ensamblaje. En su tabla:
cancelación completa de 2MK + MK² «PROVED R170_856»; supervivencia física del ensamblaje «REFUTED
R170_856». OPEN: signo de la diagonal física.

**Corrección posterior.** Cabecera de R170_856: en PC completa el jet de {X_r,E}𝓕_r contiene
−K_− − JK_−𝓕 y las dos ramas de −JH𝓕 − H contienen +JK_−𝓕 + K_−; cancelación término a término.

**T1–T4.** T3: sí (misma que 854), cerrada por 856.

### R170_856 — Jet PC completo: cancelación total de Chebyshev y libro mayor de frontera

**Objeto.** H_− = 𝒜^raw − K_−, K_− = 2K + K^{(2,∂)}. Jet Poisson–X (2.1)–(2.2):
{X_r,E}𝓕_r = S𝓜_r − K − JK𝓕_r; 𝒳_− = SṀ − Ṡ𝓜 − K_− − JK_−𝓕 − JK𝓕̇. Cancelación total
(−K_− − JK_−𝓕) + (K_− + JK_−𝓕) = 0. Identidad reducida (3.5):
𝒞 = SṀ − Ṡ𝓜 − L̇*E𝓕 − L*E_−𝓕 − L*E𝓕̇ − J𝒜^raw𝓕 − JK𝓕̇ − JH𝓕̇ − 𝒜^raw. Libro mayor
P𝒞P = 𝓡_int + 𝓡_cross (5.3)–(5.4); átomos (6.1)–(6.4); extracción PȦF = BP𝒞F + 𝒫^comb (7.2);
coordenada de Tate simplificada g_ε ω^comb = (b,PȦF) − (h,P𝒞F) (8.6), defecto
g_εΔ^Tate = (b,PȦF) − (h,P𝒞F) − ρg_ε (8.7); contínuo polar Z Ȧ − ŻA = 𝒞 − 𝒫_{C,A} (9.1)–(9.4).

**Afirmaciones.** PROVED: todas las anteriores. REFUTED: persistencia de K² como contribución física
independiente; 855 válida sólo como identidad de una rama. OPEN: signo del libro mayor; ley exterior.

**Dónde se detuvo.** La cancelación algebraica está completa y es tautológica; lo que falta es orientar
el escalar dual (11.3). Ningún sumando de (11.2) puede borrarse o firmarse por separado. La cola
positiva H aparece en JH𝓕̇ pero el jet de Fourier y la compresión tienen ambos signos.

**T1–T4.** **T4: sí, directamente** — H = Σ_{N<k≤MN} h_{M,N}(k)k^{-1/2}τ_{log k} con h ≥ 0 permanece
en el libro mayor como −JH𝓕̇ y −PJHQ𝓕̇P (ruta reflejada de la cola); su coeficiente positivo no firma
el apareamiento (no tiene forma |ℓ_k(F)|²). T3: cierra la ruta γ + W (el W se cancela con −W de 4.4).
T1, T2: no.

### R170_857 — Reducción radical/transversal de Kato del defecto de Tate

**Objeto.** Bajo un marco C¹ explícito (§1: transporte isométrico, familia de Kato con dominio de forma
común, H_s ≥ 0 para s ≤ 0, velocidad representable): 𝖹 = 1_{0}(H), 𝖰 = I − 𝖹, resolvente reducida R,
B = 𝖹V𝖹, C = 𝖰V𝖹, V = Ḣ. Prop. 2.1: B ⪯ 0. Kato: Bf = νf, 𝖰ḟ = −RCf; levantamiento horizontal
f_s^K = f − sRCf. Observador exterior 𝓛_s = Q_eA_sι_s, conexión χ_F, η = 𝓛_0*q. Identidad principal
(5.3)/(5.5): gΔ^Tate = 𝔚_K(f) + (q,χ_F) − (𝖰η, RCf).

**Afirmaciones.** PROVED bajo el marco C¹: B ⪯ 0, ecuación transversal, reducción exacta. OPEN
(REG): existencia incondicional de la familia C¹. UNDETERMINED: signo de C. IDENTIFIED/OPEN: condición
escalar (6.1) 𝔚_K + (q,χ_F) = (𝖰η, RCf). Falsificador 2×2 (7.1): H = diag(0,1), V = [[−1,c],[c,0]]:
H + sV ≥ 0 para s<0 pequeño, B = −1, RC = c arbitrario (verificado). Lo que el texto sostiene:
correcto como CONDITIONAL a (REG)/C¹; la memo lo dice explícitamente.

**T1–T4.** No toca ninguno (teoría de perturbaciones).

### R170_858 (MOBIUS_RESOLVENT_WARD_COORDINATE) — Coordenada Möbius–resolvente y muro de Ward

**Objeto.** 𝔯_T(f) = Re(𝖰η, R𝖰Ḣ𝖹f) = Re(Y, Ḣf), Y = R𝖰η; observador explícito
η = ΠPAQ_eS*PM_μ*Pb (2.2) desarrollado en (2.3) con 𝓜, Λ(d), Q_e intermedio y M_μ*. Fuente
transversal (3.7): (y,𝖢f) = (𝓑*Y, P𝒞_{PC}F) + (Y, 𝒫^comb) + 𝔱_T(Y,F), 𝔱_T de rango uno por paridad.
Expansión PC completa (4.5); forma espectral Σ_{λ_j>0}(η,φ_j)(φ_j,Ḣf)/λ_j. RES–WARD (7.1).

**Afirmaciones.** PROVED: η, fuente con conexión, expansión completa, identificación con MET–WARD/W12,
falsificador causal finito (§8: H = diag(0,1), V_c, A_0 3×3, celda nilpotente S_2 = I + 2^{-½}N_0,
M_2 = I − 2^{-½}N_0, M_2S_2 = I; coordenada = c arbitrario). REFUTED: cancelación por Ward lineal
(R162_305 da 0 = 0 para todo test). OPEN: RES–WARD. ABSENT: acoplamiento de las aristas de Ward
(defecto finito de a_κ: (κ−1)log2(δ_0 − ν_4), (κ−1)log3(δ_0 − ν_3)) con la resolvente.

**Dónde se detuvo.** Los dos numeradores de la expansión espectral son correlaciones cruzadas
independientes; la minimalidad sólo firma 𝖹Ḣ𝖹, eliminado por R𝖹 = 0. Se pide una identidad mixta
Ward–resolvente, no otra convolución de coeficientes.

**Corrección posterior.** R170_859 (el sándwich no es invariante de gauge).

**T1–T4.** T3: registra que Λ∗1 − log = 0 no puede pasar a través de R (dependencia no causal de toda
H). T2: parcial (M_μ en η). T1, T4: no.

### R170_858 (RESOLVENT_WARD_SANDWICH) — El residuo mínimo es un sándwich resolvente de Ward

**Objeto.** Mismo contenido que el anterior en forma más corta: 𝔖_RW(f) = (Q_Kη, RCf) = (Y, Ḣf),
expansión espectral (2.1), extracción PC (3.4), RES–WARD (5.2): 𝔚_K + (q,χ_f) = (B_μ*Y, P𝒞f) +
(Y,𝒫^comb) + 𝔗_conn. Falsificador 2×2 (6.1)–(6.2).

**Afirmaciones.** DEFINED/PROVED: igual que el otro 858. REFUTED: Ward lineal evalúa el sándwich;
minimalidad lo firma. Cabecera de R170_859: el sándwich no es canónico; (q,χ_f) − 𝔖_RW sí es
invariante de gauge.

**Observación.** Los dos archivos 858 son dos redacciones paralelas del mismo paso; difieren en
notación (𝖰 / Q_K, 𝔯_T / 𝔖_RW, 𝔱_T / 𝔗_conn) y en que el primero añade el análisis de a_κ (§9). Ninguno
cita al otro.

**T1–T4.** No toca directamente.

### R170_859 — Defecto de conexión exterior invariante de gauge

**Objeto.** Cambio de trivialización U_s = I + sK, K* = −K: Ṽ = V + HK − KH, C̃ = C + Q_KHKZ,
RC̃ = RC + Q_KKZ; χ̃ = χ + 𝓛_0Kf; con ZKZ = 0 la combinación Θ_ext = (q,χ_f) − 𝔖_RW es invariante.
Gauge K_C = [[0,(RC)*],[−RC,0]] anula C. gΔ^Tate = 𝔚_K + Θ_ext.

**Afirmaciones.** PROVED: transformaciones, invariancia de Θ_ext, Δ^Tate = (𝔚_K + Θ_ext)/g.
CONSTRUCTED: gauge que anula C. REFUTED: 𝔖_RW como residuo intrínseco. OPEN: (0.4) 𝔚_K + Θ_ext = 0.
Verificado (1.5), (1.6), (3.2).

**T1–T4.** No toca.

### R170_860 — Auditoría de la supuesta holonomía de dos escalas

**Objeto.** Rectángulo escalar 𝓑(r,s) = (q_r, z_s): ∮d𝓑 = 0 pero la derivada antidiagonal no es cero
(ejemplo 𝓑 = r). La familia física sólo depende de r: ∂_qH_r = 0, curvatura de Berry Ω_{rq} = 0.
S(q)A(r) no es autoadjunto. Prop. 4.1: toda congruencia G(q)*H(r)G(q) es transporte puro. Lista de
siete criterios para una segunda conexión no trivial 𝕳(r,q).

**Afirmaciones.** PROVED: circulación cero. REFUTED: circulación cero ⟹ Wronskiano antidiagonal cero;
congruencia por peine causal aporta curvatura nueva. ZERO: Berry r–q. FALSE: S(q)A(r) familia de
contacto autoadjunta. FORMULATED: criterios 1–7. OPEN: 𝔚_K + Θ_ext = 0.

**T1–T4.** T2: parcial — registra que congruencia por el peine (o su inversa de Möbius) es cambio de
coordenadas y no introduce factorización única de forma intrínseca. Resto: no.

### R170_861 — Toda dilatación positiva con Schur físico es congruencia pura

**Objeto.** 𝕳 = [[A,D*],[D,G]], G > 0, Schur A − D*G^{-1}D = H ⟹ 𝕳 = [[I,D*G^{-1}],[0,I]]·(H ⊕ G)·[[I,0],[G^{-1}D,I]];
ker 𝕳 = {(f, −G^{-1}Df): f ∈ ker H}. Si D(r,1) = 0, D*G^{-1}D = O(u²) (sin primer jet). G semidefinida:
misma eliminación con G^† (rango cerrado); G indefinida: se pierde el orden de Hilbert. Aplicación a
D ∈ {E, H_{M,N}, S(q)A(r), 𝒞_PC}.

**Afirmaciones.** PROVED: factorización triangular, positividad y núcleo, dirección q pura gauge con
Schur fijo. REFUTED: acoplamiento con D(r,1)=0 da jet. OPEN CLASS: deformación lineal aritmética del
Schur S(r,q) = H(r) + 𝓡(r,q), 𝓡(r,1) = 0, ∂_q𝓡 ≠ 0. REFUTED por 862: diagonal (6.3) como codificación.

**Corrección posterior.** Cabecera de R170_862: (6.3) tiene homogeneidad incorrecta (cuadrática vs
lineal).

**T1–T4.** T1: sí, en clase — cualquier completación de cuadrado D*G^{-1}D con D aritmético (incluido
H_{M,N} o la PC) es congruencia; sin compensar, el nuevo Schur pide una desigualdad global nueva y
genera ratio-comb. T4: sí, en clase — colocar H_{M,N} en el bloque cruzado no crea energía. T2, T3: no
(«Λ∗1 = log puede simplificar D pero no altera (0.3)»).

### R170_862 — Homogeneidad correcta: la ley necesita un ancla nula con borde

**Objeto.** 𝔏_T(f) = 𝔚_K + Θ_ext = g_εΔ^Tate(f) es lineal en f (directo desde (8.7) de 856, sin REG).
Lema 2.1: familia C¹ con 𝕳(s) ≥ 0 a ambos lados ⟹ P_N𝕳̇(0)P_N = 0 (sólo ⪯ 0 si positiva a un lado).
Codificación homogénea correcta 𝔏_T(f) = (a, 𝕳̇f) con a ∈ ker. Modelo (3.2): 𝕳_c(s) = (sc,1)ᵀ(sc,1)
≥ 0, (e_2, 𝕳̇_c(0)e_1) = c arbitrario si el ancla no es nula. Especificación del «ancla nula con
borde»: coordenada e_T producida por el peine y los puertos, nulidad exacta desde Λ∗1 = log y la
hipérbola finita, igualdad de jet (4.3), positividad bilateral.

**Afirmaciones.** PROVED: linealidad, lema bilateral, ancla nula fuerza cero. REFUTED: codificación
diagonal; ancla fuera del núcleo recibe cancelación. FALSE: la columna de Tate b es ancla nula
(g_ε > 0). NOT PROVED: la cancelación interior de la hipérbola (H_{M,N} sin coeficientes en k ≤ N) da un
vector nulo de una forma positiva. SPECIFIED/OPEN: ley del ancla nula.

**T1–T4.** **T4: sí** — propone realizar la nulidad interior de H_{M,N} (coeficientes k ≤ N nulos) como
coordenada nula de una forma positiva con la cola k>N como flujo de borde; registra que es nulidad de
coeficientes, no de vector, y que su jet K_− se cancela en la PC completa. **T3: sí** — la nulidad
exacta exigida debe venir de Λ∗1 = log; no construida. T1, T2: no.

---

## 2. Síntesis

### (a) Piezas PROVED reutilizables

- Identidad de Ward de escala de la hipérbola finita y soporte k>N tras δ_Λ = 0: R170_841 Teor. 3.1,
  (3.4)–(3.8); defecto δ_a para pesos alterados (3.6), (3.9).
- Coeficiente antisimétrico β_Λ(k) = 2Σ_{d|k}Λ(d)log d − (log k)², ejemplos de signo (4.6)–(4.7); cota
  |β|² ≤ (log k)Σ_Λ (4.9)–(4.10): R170_841 §4.
- Derivada del contínuo polar Ċ_N: R170_841 (5.5); su símbolo de Laplace
  K_{Ċ_NF} = c_N(s)(1 − 1/(2s) − a log N)K_F: R170_844 (3.2b).
- Transformada de Laplace del Wronskiano: K_{𝒜^raw F}(a) = −aB_{M,N}(s)K_F(a), B_{M,N} = ℓσ' − ℓ'σ:
  R170_843 (5.2)–(5.4); B_Λ = −ζ²(1/ζ)'' (5.6)–(5.7) (positividad CITED); B_{N,N}(s) > 0 para s ≥ 3,
  N ≥ N_0 absoluto (Teor. 5.1); energía Hankel 𝓔^β > 0 (5.18); collar tipado (6.6)–(6.8).
- Colinealidad de las dos rutas al derivar en r = 1 (R170_843 §2.1); concomitante universal
  𝔎_P(B;g,w) = ⟨g,[P,B]w⟩ (R170_843 (4.2)).
- Puerta de dominio K_{C_NF}(a) = N^{a+½}K_F(a)/(a+½) y δ > log N: R170_844 §1.1; π_N > 0 (3.2h)–(3.2i);
  criterio de Fredholm (Teor. 6.1).
- Derivada de la proyección primitiva y Π̇F = −b_ε⟨ḃ_ε,F⟩/q_ε, 2Re⟨Π̇F,r_F⟩ = −2Re⟨F,t r_F'⟩:
  R170_845 (1.5), (2.4), (3.1).
- PC de dos escalas (r,q) con el factor r/q: R170_847 Teor. 4.1; jet ∂_−K = 2K + K^{(2,∂)} (4.6);
  versión sin Fourier derecho y ṁ = −τm': R170_848 (1.1), (3.1)–(3.2).
- Nilpotencia e inverso finito de PS_NP: R170_849 (1.2)–(1.3); B_{N,T} = PM_μP: R170_850 (1.5).
- γ_Λ = μ∗β_Λ = −Σμ(d)(log d)² = Λlog − Λ∗Λ, valores por ω(n): R170_850 (0.2), R170_851 (0.1);
  fórmula general μ∗β_a = Da − (μ∗a)∗D1: R170_854 (4.7).
- Átomos de frontera de ∂_t(Pg), ∂_t(Qg) y puerto combinado: R170_851 §§3–4, R170_856 §6.
- Coordenada de Tate del puerto combinado y defecto: R170_852 (0.5)–(0.6); forma simplificada
  g_εΔ^Tate = (b,PȦF) − (h,P𝒞F) − ρg_ε: R170_856 (8.7).
- Grafo causal S*Ph = b + 𝒟b y desajuste z_F: R170_853 (1.1), (2.2).
- Ley de Green graduada 𝔚_bulk + 𝔚_ext = 𝔚_Tate y [𝔻̇,𝔻] = Γ𝒜^raw: R170_854 Teor. 2.1, (3.2).
- Cancelación total de K_− = 2K + K² en la PC derivada y libro mayor P/Q completo: R170_856 (0.2),
  (3.5), (5.3)–(5.4), (9.1)–(9.4).
- (CONDITIONAL a REG/C¹) B = 𝖹Ḣ𝖹 ⪯ 0 y reducción de Kato: R170_857 Prop. 2.1, (5.3)/(5.5).
- Invariancia de gauge de Θ_ext y gauge K_C que anula C: R170_859 (2.6), (3.1)–(3.3).
- Proposición de congruencia pura: R170_860 Prop. 4.1; factorización triangular de extensiones con
  Schur fijo: R170_861 (0.3), (1.3).
- Lema bilateral P_N𝕳̇P_N = 0 y linealidad de 𝔏_T: R170_862 Lema 2.1, §1.

### (b) Cierres (clase y falsificador)

- 𝒞_fib^{(1)} (operaciones diagonales por fibra de primer orden, δ_Λ = 0, positividad de coeficientes,
  cuadrados dentro de la fibra): R170_841 Teor. 6.1. Falsificador: β_Λ(12) < 0; paridad de Σ_Λ; familia
  F_ξ con c'_{F_ξ} ≍ ξ de ambos signos (§6.1).
- 𝒞_Green^{(1)} (Green mixta estándar con 𝒜 comprimida, reflexión, XF, F_δ, sin Hankel entre piernas):
  R170_843 Teor. 8.1. Razón: colinealidad de rutas, (4.2) = concomitante de R161_065, (4.11) sin signo.
- Levantamiento estático (7.3) de 843 con orientación (0.5): R170_844 §5, refutado por signo
  (implicaría 𝒱 > 0 en el radical por π_N > 0) y por Fredholm (Teor. 6.1; sólo con H^†).
- Energía Gamma aislada como separador de pesos: R170_843 §5.4 (muchos pesos positivos alterados
  también dan Wronskiano positivo en s_m ≥ 3).
- Igualdad métrica física = métrica Hankel: R170_849 §4 (𝓡*D𝓡 compacto).
- Completación por la cola sincronizada como W de Selberg: R170_851 §2 (la cola es cero en k ≤ N).
- Supervivencia física de γ + W = 2Λlog: R170_856 §4 (el −W del bloque Poisson–X la cancela).
- Toda completación por cuadrados del corriente graduado: R170_854 (3.4) (métrica indefinida) y §6.3
  (con métrica positiva reaparece ratio-comb).
- Minimalidad firma el bloque transversal / sándwich: R170_857 §7, R170_858 (ambos) — falsificador 2×2
  H = diag(0,1), V_c = [[−1,c],[c,0]]; con celda causal de Möbius (858 §8).
- Ward lineal (R162_305) evalúa la coordenada resolvente: R170_858 §6 (da 0 = 0).
- Sándwich 𝔖_RW como residuo intrínseco: R170_859 (gauge K_C lo anula).
- Holonomía de dos escalas con las familias existentes: R170_860 (circulación cero sin contenido; Berry
  cero; S(q)A(r) no autoadjunto; congruencia = gauge).
- Extensiones positivas con Schur físico fijo (incluye completar cuadrado con D ∈ {E, H_{M,N}, S(q)A(r),
  𝒞_PC}): R170_861 (0.3); acoplamiento que se anula en la fibra física: (3.3).
- Codificación diagonal (cuadrática) del defecto: R170_862 §1; ancla con energía positiva (b, h):
  modelo (3.2), (e_2, 𝕳̇_c e_1) = c.

### (c) Abierto explícito y obstáculo exacto

- Ley de Green antisimétrica de frontera para 𝒜_{M,N} con libro mayor (5.8) (R170_841 §7): falta una
  relación física de primer contacto que oriente un primer momento.
- Levantamiento físico Hankel (R170_843 (7.3)–(7.4)): refutado en su forma estática por 844; su
  sustituto es la derivada covariante (844 (8.1)), luego mal tipada (846).
- Ward–PC covariante (R170_844 §8; R170_847 «PC–curvature»): demostrar que la diagonal hermítica de la
  derivada antidiagonal de la PC completa es −𝒱 − 𝓔^β − energía de cola + residuo polar que cancela Π̇.
- Extracción de Ȧ desde SȦ sin invertir S_N (R170_848): resuelta algebraicamente en 849, pero con
  choque de métricas: MET–WARD (R170_849 §5) — diferencia B* − G^ext con diagonal ≤ 0 en ker H_T.
- Completación con signo del canal de dos bases primas −2 log p log q (R170_850 §5).
- Ley exterior (R170_853 (5.1)) ⇔ igualdad dual (R170_854 (0.5)):
  (h, P(SȦ − ṠA)F) = (b, PȦF) − ρ(PṠ*Ph, b); la minimalidad no controla el apareamiento con el dual
  causal h.
- Signo del escalar dual (R170_856 (11.3)): (b,PȦF) − (h,P𝒞F) − ρ‖b‖².
- Condición escalar de Kato (R170_857 (6.1)); RES–WARD (R170_858 (7.1)/(5.2)), con exigencia de
  acoplar las aristas finitas del defecto de a_κ con la resolvente.
- Identidad intrínseca 𝔚_K(f) + Θ_ext(f) = 0 (R170_859 (0.4)).
- Familia 𝕳(r,q) con los criterios 1–7 (R170_860 §5); clase viva: deformación lineal aritmética del
  Schur S(r,q) = H(r) + 𝓡(r,q) con ∂_q𝓡 ≠ 0 (R170_861 §6).
- Ley del ancla nula con borde (R170_862 §4): construir e_T desde el peine y los puertos, con nulidad
  exacta por Λ∗1 = log, jet (4.3) y positividad bilateral. Obstáculo: la nulidad interior de H_{M,N} es
  de coeficientes, no de vector de una forma positiva.
- Transversal a todo el tramo: (REG)/regularidad C¹ de la familia de ventanas sigue OPEN (841 §1,
  857 §1).

### (d) Lo que este tramo ya recorre de T1–T4, con razón del fracaso

- **T1 (cuadrados continuos con aritmética en el índice/peso de dilatación).**
  R170_843: G_δ = 𝓡_δ*𝓡_δ en la retícula Gamma con pesos a_mB_{N,N}(s_m) da 𝓔^β > 0, pero (i) el signo
  no separa Λ de pesos alterados positivos en s_m ≥ 3 (§5.4), (ii) el paso al operador renormalizado
  añade bloques polar/soporte/Tate sin signo. R170_844: el mismo observador da al residuo polar el
  signo contrario al requerido (3.2i) y la factorización estática es Fredholm-circular. R170_849: el
  observador con pesos 1/σ_N(a_m) extrae S_N con signo, pero es compacto y produce un virial filtrado,
  no el físico. R170_861: completar el cuadrado D*G^{-1}D con D aritmético es congruencia pura; sin
  compensar exige una desigualdad nueva y genera ratio-comb. R170_854 §6.3: cuadrar el sector graduado
  da ratio-comb o métrica indefinida. Ninguno es un cuadrado continuo sobre P_T que reproduzca a_T con
  resto ≥ 0; todos son observaciones auxiliares en coordenadas de Laplace.
- **T2 (Gram de incidencia de divisores).** No aparece la factorización [log mcd] = E diag(Λ) Eᵀ en
  ningún archivo del tramo. Lo más cercano: la agrupación por fibras k = dm (841), declarada prohibida
  como diagonalización porque cambia la Gram física (841 §6, 843 §2.1); el inverso de Möbius del peine
  como cambio de métrica (849–850), que 860 Prop. 4.1 reduce a congruencia; y el canal −2 log p log q
  de γ_Λ (850 §5), que sugiere un cuadrado en la red de bases primas no construido.
- **T3 (Σ_{d|n}Λ(d) = log n como cota cuadrática).** Recorrido directamente en R170_841 §4.2:
  probabilidad Λ(d)/log k y Cauchy–Schwarz |β_Λ|² ≤ (log k)Σ_Λ; falla porque la cota es par en la
  diferencia de piernas y β_Λ es impar (cambia de signo, β(12) < 0). Variantes: 843 (suma de Dirichlet
  con concavidad de 1/ζ: signo en el semiplano, no separa pesos en la retícula), 850–851 (γ = Λlog −
  Λ∗Λ, choque con Selberg sin signo), 854–855 (γ + W = 2Λlog dentro de PC), cerrada por 856 (el W
  aparece con signo opuesto en el jet Poisson–X y se cancela). 858 registra que Λ∗1 − log = 0 no
  atraviesa la resolvente reducida. 862 exige una nulidad exacta por Λ∗1 = log como vector nulo, no
  construida.
- **T4 (residuo común como Σ_{k>N} h(k)|ℓ_k(F)|²).** La cola existe con h_{M,N}(k) ≥ 0 (841 (3.8)), pero
  en todo el tramo va acoplada a ∂_tτ_{log k} o a τ_{log k}𝓕̇, nunca a un módulo al cuadrado: su
  apareamiento es una derivada de correlación sin signo (841 Teor. 6.1, 856 §10.4). En coordenadas
  Gamma sí da un multiplicador positivo Θ_N(s) (844 (4.3)–(4.4)), pero en la métrica Hankel, no en la
  física, y el resto del libro mayor queda sin signo. 861: poner H_{M,N} en un bloque cruzado es
  congruencia. 862: la nulidad interior de H_{M,N} es nulidad de coeficientes, no vector nulo de una
  forma positiva; su jet K_− se cancela en la PC completa. El tramo no intenta la conversión de los
  apareamientos mixtos (H, E_N) en una suma de cuadrados |ℓ_k(F)|² con h ≥ 0; esa forma exacta no
  aparece.

### (e) Inconsistencias o errores entre memos

1. R170_844 (8.1) usa el símbolo 𝔓^ren_{N,N} sin definición; R170_846 lo retira y R170_845 §4 queda
   condicional (las cabeceras lo registran).
2. R170_843 (7.3) se presenta como objetivo abierto; R170_844 prueba que la orientación pedida es
   imposible (signo opuesto de π_N), no sólo abierta. La tabla final de 843 sigue diciendo OPEN; la
   cabecera añadida sólo menciona dominio y Fredholm, no la refutación por signo.
3. R170_843 tabla: «full half-plane separation for an altered weight PROVED» — el texto sólo lo
   muestra para el peso δ_2 (5.21); no es un enunciado general.
4. R170_849 (1.3) dice que el inverso finito vale «simultáneamente para todo N»; la estabilización
   PS_NP = PSP requiere N ≥ e^{2T} (R170_850 (1.3)).
5. R170_851 declara que el W interior no está en la cola; R170_854 corrige que sí está en K²; R170_856
   corrige a su vez que ese W se cancela en la PC completa. La afirmación de 854 «γ + W = 2Λlog inside
   PC PROVED» queda invalidada como contribución física (sólo vale por rama).
6. Notación: R170_852 usa q_ε = ‖b_ε‖²; R170_853–856 usan q para el vector exterior QS*Ph y renombran
   la norma como q^Gram o g_ε.
7. Los dos archivos R170_858 son redacciones paralelas del mismo paso con notaciones distintas
   (𝖰/Q_K, 𝔯_T/𝔖_RW, 𝔱_T/𝔗_conn) y no se citan entre sí; la cabecera de 859 sólo corrige el archivo
   «SANDWICH».
8. R170_861 (6.3) propone una igualdad diagonal cuadrática para un funcional lineal; corregido por 862.
9. R170_849 (2.2) separa PṠPAF y PṠQAF; R170_851 muestra que cada uno lleva átomos de frontera y sólo
   la suma está tipada.
10. Sin errores matemáticos encontrados en las verificaciones puntuales hechas: (3.4) de 850, (4.7) de
    854, (3.2) de 854, (1.5)–(1.6)/(3.2) de 859, falsificadores 2×2 de 857/858/862, (3.2f)–(3.2h) de 844.

### (f) Archivos leídos (lectura completa con Read)

R170_841_VIRIAL_LB.md (718 líneas); R170_843_ANTISYMMETRIC_HYPERBOLA_GREEN.md (1140);
R170_844_WRONSKIAN_PHYSICAL_LIFT.md (947); R170_845_MOVING_TATE_CONNECTION.md (230);
R170_846_PC_CARRIER_AUDIT_AND_CORPUS_FILTER.md (237); R170_847_TWO_PARAMETER_PC_CURVATURE.md (305);
R170_848_FOURIER_REMOVED_PC_CURVATURE.md (221); R170_849_FINITE_EXTRACTION_AND_METRIC_MISMATCH.md (214);
R170_850_MOBIUS_EXTRACTED_WRONSKIAN_LAW.md (233); R170_851_SELBERG_COLLISION_AND_BOUNDARY_ATOMS.md (194);
R170_852_EXACT_COMBINED_TATE_DEFECT.md (203); R170_853_CAUSAL_GRAPH_CURVATURE_AND_ARITHMETIC_MISMATCH.md
(197); R170_854_GRADED_EXTERIOR_WRONSKIAN_GREEN.md (418); R170_855_MOBIUS_TWO_JET_ASSEMBLY.md (181);
R170_856_FULL_PC_JET_AND_BOUNDARY_LEDGER.md (582); R170_857_KATO_RADICAL_TRANSVERSE_REDUCTION.md (364);
R170_858_MOBIUS_RESOLVENT_WARD_COORDINATE.md (489); R170_858_RESOLVENT_WARD_SANDWICH.md (276);
R170_859_GAUGE_INVARIANT_EXTERIOR_CONNECTION.md (264); R170_860_TWO_SCALE_HOLONOMY_AUDIT.md (217);
R170_861_POSITIVE_BLOCK_DILATION_NO_GO.md (234); R170_862_BORDERED_NULL_ANCHOR_LAW.md (225).
Total: 22 archivos (841, 843–857, dos 858, 859–862; 842 no existe). Todos leídos enteros.
