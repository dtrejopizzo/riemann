# Anexo 211 — Archivos POWER_REDUCTION_AUDIT_044 … POWER_THETA_DENSITY_ORIGIN_087 (106 archivos)

Lectura completa, en orden alfabético (`ls *.md | sort`), de los 106 archivos de
`../phase-211-sign-sandbox/` comprendidos entre `POWER_REDUCTION_AUDIT_044.md` y
`POWER_THETA_DENSITY_ORIGIN_087.md`, ambos incluidos. Notación de `STATEMENT_001.md`,
`POWER_CONE_001.md` y `POWER_BRIDGE_002.md`: (★) es λ_A(T) ≥ 0 para todo T; W es la forma completa
(ARCH + peine + polar); AP = ARCH + POLAR; u = 63/2 es la tasa fija; V_n es el bloque confluente
{P(s)/(s+u)^n}; f_{N,k} (o h_{N,k}) es el átomo de transformada s^k/(s+u)^{N+k}; g_N es el átomo
gamma y^{N−1}e^{−uy}/(N−1)!; Q = s/(s+u), L = u/(s+u); Φ es la densidad theta par de CONE_001,
M(u) = L(u+½), K_ij = [L(a_i)+L(a_j)]/(a_i+a_j−1). E_0(x) = ψ_Λ(x) − x + 1;
B(x) = Σ_{m≤x}E_0(x/m); h_N(x) = Σμ(m)mH_N(mx) es el inverso de dilataciones. Las etiquetas se copian
como figuran en cada archivo. Los archivos POWER_STATE_* son resúmenes de ronda: su entrada señala qué
registran y qué añaden (no se repite la prueba de la fuente).

## Entradas por archivo

1. **POWER_REDUCTION_AUDIT_044.md** — Auditoría de REFLECTION_TEST_044 y del candidato L55-B (par
   primal positivo en un dato arquimediano desplazado). Resultado: reflexión APROBADA (verificador PASS);
   L55-B «permanece abierto, sin piso nuevo probado»; «no es un no-go global». Resto: una
   representación positiva de TODAS las formas primitivas con slack ≤ ε y desajuste primal en variación
   total ≤ η daría λ_A ≥ −ε−η, pero «sería ya una extensión positiva de la forma»; los vectores de la LP
   dual sólo dan cotas superiores; un desajuste que sea medida positiva no basta (c_F tiene signos).
   Sin positivo reutilizable.

2. **POWER_REFLECTION_TEST_044.md** — Hipótesis: eliminar por la simetría q ↔ 1−q
   (q = τ²/(u²+τ²), R(q) = A(q(1−q)) + (2q−1)B(q(1−q))) el sector antisimétrico del puente 017.
   PROVED (PASS), u = 63/2: con g_Q = √(4u)(1−uy)e^{−uy}, g_L = √(4u)uy e^{−uy},
   W[g_Q] − W[g_L] > 3/2 (gap ARCH 2b > 2, polar −2u(1+4u²)/(u²−¼)² > −½, peine
   4uΣΛ(n)log n·n^{−u−½} > 0). Falsificador de la simetría (falla ya B = 1 en el dato real), no de W.
   Reapertura: control cuantitativo del sector antisimétrico. Positivo: ASYMMETRY.

3. **POWER_RENORMALIZED_AUDIT_042.md** — Auditoría de RENORMALIZED_TAIL_042. APROBADO (PASS):
   identidad W = ARCH_♯ + 2γ − (2κ−γ)J(1) − 2R y |R_tail| < e^{−N/1000} para N ≥ 2^80, con todos los
   bordes, saltos y divisores. Resto: el interior renormalizado y su balance con ARCH_♯, J(1) «no se han
   decidido»; no se suma el beneficio C_N de 041 sin contabilidad de bordes.

4. **POWER_RENORMALIZED_TAIL_042.md** — Cancelación global del afín −γx por la masa exacta
   ΣJ_N(n) = 1: F_N/2 = −γ + (κ−γ/2)J_N(1) + R_N, κ = ½log(2π) − ½,
   R_N = −∫_1^∞h_N B_1({x})(log x+γ)dx + ∫h_N E. PROVED (PASS), u = 63/2, N ≥ 2^80,
   T = (N−1)/992 + 5: |R_N^tail| ≤ N(T+2)e^{−3T/2} < e^{−N/1000} (ABS-TAIL);
   W[g_N]/‖·‖² = ARCH_♯ + 2γ − (2κ−γ)J_N(1) − 2R_N^inside + ε_N, |ε_N| < 2e^{−N/1000};
   DILATION y REAL-DECAY |h_N| ≤ Nx^{−3/2}, |h_N′| ≤ 2Nx^{−5/2} (x ≥ e^T). Resto: R_N^inside
   (de 1 a e^T) sin signo. Positivo reutilizable: ABS-TAIL y la identidad (N ≥ 2^80).

5. **POWER_ROW_FOUR_028.md** — Fila N = 4. PROVED (PASS): W[f_{4,k}] > (1/50)‖f‖² ∀k ≥ 0,
   ∀u ≥ 63/2 (ROW4); ARCH_{4,0}/norm² = d − ud′ + (2u²/5)d″ − (u³/15)d‴ con A4(u_0) > 11/400; peine
   < 3/500 (peso η = 12, R4 < 400); polar impar < 1/1000. Corolario (−Δ)³a_{1,k} = u⁶a_{4,k} > 0.
   Resto: no cierra la tabla de SCALAR_BRIDGE_017; no da ventana T. Se mantiene la prohibición de
   sustituir prueba universal por campaña de filas. Positivo: ROW4 y monotonía MON de ARCH en u y k.

6. **POWER_ROW_PATTERN_029.md** — Región u² ≥ 256N, k ≥ 1, con Cauchy–Schwarz de pesos ±η.
   PROVED (PASS): W[f_{N,k}] > (7/10)‖f‖² ∀N ≥ 2, k ≥ 1, u² ≥ 256N. Lemas: PSI
   Re ψ(¼+it) ≥ log|t| − 9/(8t²); GAIN A_{N,1} = A_{N,0} + uA_{N,0}′; CENTERED
   |c_f(t)|/norm² ≤ e^{−ηt}[(u²−η²)/(u²−4η²)]^{N−½}. Resto: a u fijo sólo cubre N ≤ u²/256 (no
   cierra la tabla de u = 31.5); en k = 0 diverge E τ^{−2}. Positivo: REGION, PSI, CENTERED.

7. **POWER_ROWS_AUDIT_028.md** — Auditoría de ROW_FOUR_028 y ROW_SPLIT_028: ambas APROBADAS (PASS).
   Fila 5: W > norma²/25 (k ≥ 0) y > 4norma²/5 (k ≥ 1), u ≥ 31.5; tercera y cuarta diferencias
   estrictas de la fila 1. Resto: «La tabla suficiente completa sigue abierta»; el criterio §7 de
   028 es sólo suficiente; no monotonía completa ni ventana T.

8. **POWER_ROW_SPLIT_028.md** — Fila N = 5 separando k = 0 (polar positivo) de k ≥ 1 (covarianza).
   PROVED (PASS): W[f_{5,k,u}] > (1/25)‖f‖² ∀k ≥ 0, u ≥ 63/2; > (4/5)‖f‖² si k ≥ 1;
   ARCH_{5,0}(63/2) ∈ (−13/100, −1/10) («ARCH positiva desde k0» no sirve). Criterio reutilizable
   (suficiente) para una fila N: min(b_0 + p_{N,0}(U), b_U) > L_N, b_1 > L_N + p_1; identidad
   A_{N,1} = A_{N,0} + u∂_uA_{N,0}. Resto: filas N crecientes requieren desigualdad aritmética adicional.

9. **POWER_SCALAR_BRIDGE_017.md** — Elevación de grado Bernstein de la densidad racional.
   PROVED: (A) W[h_{N,k}] ≥ 0 ∀N ≥ 1, k ≥ 0 ⟺ (B) W[f] ≥ 0 ∀F = P/(s+u)^M, grado P < M (u > 1);
   identidad FORM W[f] + εW[f_1] = Σ_j b_{D,j}C(D,j)W[g_{D,j}], b_{D,j} > 0 si D > C_R/ε,
   C_R = ½Σ|r_l|l(l−1), con el polar conservado por evaluación en x = −¼; un W[f] < 0 produce un átomo
   negativo h_{D+1−j,j} a orden finito acotable. Resto OPEN: (A), «el signo de toda la tabla escalar con
   el dato aritmético completo»; EVENTUAL_015 y colas de dimensión fija no bastan (W4 de 016).

10. **POWER_SCALE_AUDIT_029.md** — Auditoría de ROW_PATTERN_029, BOUNDARY_WEDGE_029 y
    SCALE_BRIDGE_LIMIT_029: los tres APROBADOS (PASS). Registra BOUNDARY_WEDGE: W/norma² > 0.4
    ∀N ≥ 1, k ≥ 0, u ≥ 64√N (ARCH > 0.45, peine < 1/5000, polar < 0.001). Resto: a u = 31.5 la
    región k ≥ 1 sólo alcanza N ≤ 3 y la de k = 0 no añade órdenes; «nueva información para N/u²
    grande». Positivo: región u ≥ 64√N.

11. **POWER_SCALE_BRIDGE_LIMIT_029.md** — Densidades espectrales normalizadas p_{N,k,u} en u ≥ C√N.
    PROVED (APROBADO): HEIGHT sup p_{N,k,u} < √N/(u√π); toda mezcla positiva normalizada de ese
    dominio dista en L¹ más de ½ de p_{M,0,63/2} si 2M−3 > 256u_0²/C² (GAP). NO-GO (clase:
    aproximación por conos positivos de densidades, normalizados o de masa → 1, desde u ≥ C√N): no se
    traslada automáticamente el puente 017. No excluye otros puentes, identidades con estructura
    adicional ni control directo.

12. **POWER_SCHUR_003.md** — Paso Schur–Nevanlinna sobre F(z) = L(z+½), pivote u ≥ 31.5:
    F_1(z) = c[zF − uc]/[zc − uF], c = F(u). PROVED: F_1 > 0 en z ≥ 31.5. OPEN: preservación
    iterada. Falsificadores: 3 + cosh z (F_1 = −129/17); F = (z²−z+10)/10 en [1,3] (todos los 2×2
    positivos, det K(1,2,3) = −13/270000); min((2+3z)/5, (14+z)/10) (cóncava, det = −53/270000).
    NO-GO (clase: F′ ≥ 0 y F/z decreciente, también con concavidad por tramos); F_1′ ≥ 0 no es
    invariante. Resto: jet |u(cd − ud² + uce)| ≤ c² − u²d² y una propiedad aritmética conservada.

13. **POWER_SCHUR_BASE_AUDIT_081.md** — Auditoría de SCHUR_BASE_OBSTRUCTION_081. APROBADO / PROVED en
    la clase declarada: G_p′(1024) < 0 para todo pivote p ≥ p_0 = [25(L+2)]²; un G_p positivo con
    derivada negativa no es cóncavo global. NO-GO (clase: imponer a TODOS los restos G_p las condiciones
    BASE_073, G′ > 0 y G″ ≤ 0). G_p > 0 sigue probado; no excluye recursión general ni otra clase.

14. **POWER_SCHUR_BASE_OBSTRUCTION_081.md** — Resto regularizado
    G_p(z) = az[B(p)−B(z)]/[B(p)(z²B(z) − p²B(p))], B(z) = [az/M(z) − 1]/z², a = M′(0); normalización
    C_p = z[B(z)−B(p)]/[1 − g(z)/K_p]. PROVED (auditado): F = zB cumple F′(1024) < −1/(3·1024²);
    G_p′(1024) < 0 ∀p ≥ p_0 (FAIL-BASE). Reapertura: «una clase más amplia que permita funciones
    decrecientes, o una prueba que conserve el residuo y controle los cruces directamente»; la doble
    concavidad de 078 no se refuta. Positivo: cotas M(z) < √z (z ≥ 128), M′(z) > 1/(3(z+½)).

15. **POWER_SCHUR_TRIPLES_APPLICATION_099.md** — Kernel K_{G_p}(z,w) = [G_p(z)+G_p(w)]/(z+w) y doble
    complemento de Schur sobre K_M con nodos {0, p}. PROVED (certificado 099 FULL PASS, reproducido):
    T_h > 0 en toda la semirrecta; R_G″ < 0 y S_G″ < 0 ∀p, x > 0; TODOS los triples de nodos positivos
    distintos de K_{G_p} son PD ∀p > 0; bloque {0, p, z_1, z_2, z_3} de K_M PD (identidad
    S_uv − S_0uS_0v/δ = d_p(u)d_p(v)K_{G_p}(u,v)). Alcance: el nodo 0 (exponente ½) está fuera del
    portador; no da cinco generadores admisibles. Resto: «El siguiente nivel requiere un input nuevo».

16. **POWER_SELBERG_DROP_AUDIT_067.md** — Auditoría de SELBERG_DROP_OBSTRUCTION_067: APROBADO.
    Reconfirma S = U − V, 2V > 1/243, 0 < W/c_0 < 27/(2·10^{11}), θ < 3.2805·10^{−8}. Alcance: sólo
    la pérdida AISLADA del aporte positivo en esa descomposición; «no descarta conservar la cancelación
    entre U y V»; no NO-GO global.

17. **POWER_SELBERG_DROP_OBSTRUCTION_067.md** — Test gamma N = 129, u = 63/2;
    S = ΣΛ(m)m^{−½}ρ(log m), U = Σ(μ∗log²)(m)m^{−½}ρ(log m)/log m,
    V = Σ(Λ∗Λ)(m)m^{−½}ρ(log m)/log m; de Λ·log + Λ∗Λ = μ∗log²: W/c_0 = ARCH/c_0 + POLAR/c_0 − 2U + 2V.
    PROVED/APROBADO: el criterio W/c_0 ≥ 2V es falso (ARCH + POLAR − 2U < −1/250); retener 1−θ de 2V
    exige θ < 3.2805·10^{−8}. NO-GO (clase: suprimir 2V o una fracción aislada θ ≥ 3.3·10^{−8} en
    esta descomposición). No excluye otra organización ni estimación compensada U−V. Positivo: 2V > 1/243.

18. **POWER_SEVEN_AUDIT_012.md** — Auditoría de SEVEN_GLOBAL_012. PROVED (PASS): bandas AP, 196
    paneles DIRECT, traza T7 = 176673441, peine < 1/125; W > (1/500)‖f‖². Resto: «Nada en este
    certificado implica el resultado para ocho polos o todos los grados».

19. **POWER_SEVEN_GLOBAL_012.md** — F = P(s)/Π_{j=1}^7(s+v_j), v_j ≥ 63/2, grado P < 7.
    PROVED (certificado racional, auditado): W[f] > (1/500)‖f‖² (SEVEN); BASE7 AP − (69/1000)I PD;
    AP7 AP > (1/100)‖f‖² por la identidad de transporte con déficit DIRECT < 57/1000; peine por traza
    ponderada (σ = 21). Resto: el test Tate de gran orden y el bloque de dimensión doce «no quedan
    resueltos por extrapolar AP7». Positivo: SEVEN (siete polos arbitrarios ≥ 63/2).

20. **POWER_SHIFTED_WRONSKIAN_092.md** — Determinante de eliminación Δ de la carta F = K/w
    (w = tΦ, ODE F″ + mF′ + AF = s), identidad SHIFT Δ = −W_t(w″, v″, w⁗)/[w³k²J]. PROVED (auditado):
    W_shift < 0 cerca de 0 (D0 ∈ (−56488961026, −56488961025)) y > 0 en una cola
    (P = 4096(2t²−1)y⁹ + Q, |Q| ≤ C*t²y⁸); existe t* con Δ(t*) = 0. NO-GO (clase: carta invertible
    global que divide por Δ; ODE homogénea mónica de orden 2 con coeficientes continuos en toda la
    semirrecta que contenga D3(1/w) y D3(t/w)). No excluye cancelación para K, ODE inhomogénea, otro
    orden, representación o gauge.

21. **POWER_SHIFTED_WRONSKIAN_AUDIT_092.md** — Auditoría de 092: APROBADO / PROVED para la carta
    declarada; reproducción independiente de D0 y del coeficiente 4096(2t²−1) de y⁹. «No hay nuevo W
    negativo, menor anclado decidido, cobertura W/T ni obstrucción global»; otras cartas disponibles.

22. **POWER_SHOULDER_AUDIT_039.md** — Auditoría de INFINITE_SHOULDER_039 (producto de Euler infinito
    en σ > 1). APROBADO (PASS): h_N > 0 y K_N > 0 para x ≥ e^{T_N} y N ≥ 4·10^6, con ψ(x) ≤ 2x,
    A ≤ 5/δ, B ≤ 5/δ² y razones entre 0.9U_σ y 1.1U_σ; T_N < d/330. Resto: «La región σ1 crítica y el
    interior restante no están cubiertos»; sin compensación cuantitativa con ARCH_♯.

23. **POWER_SIGNED_AUDIT_014.md** — Auditoría de SIGNED_TRANSFER_014. PROVED (PASS): telescopaje TEL
    con κ_j ≥ 0 exacto; bloque restringido Q(0) = 0 con γ = ¼; AP > 0.03; peine < 29/1000;
    W > 0.001‖f‖² en ocho polos ≥ 31.5 arbitrarios. Alcance: cambia una hipótesis esencial de la clase
    descartada en 013 (conserva la integral firmada); no infiere dimensión mayor.

24. **POWER_SIGNED_AUDIT_019.md** — Auditoría de SIGNED_MEAN_019 y ARITHMETIC_DIFFERENCES_019: ambos
    APROBADOS con alcance local. Columna k = 1: raíz única de r_N = p_N − 2p_N′ + p_N″ (Descartes); para
    N ≤ 211 (u = 31.5) todos los contactos tienen autocorrelación negativa y el peine completo es
    estrictamente positivo; todas las diferencias (−Δ)^rP_{1,0} del peine aislado son negativas.
    NO-GO: positividad de cada prefijo inverso; atribuir diferencias positivas al peine por Λ ≥ 0.
    Resto: kernel inverso completo y tabla global abiertos.

25. **POWER_SIGNED_AUDIT_038.md** — Auditoría de SIGNED_MOMENTS_038: APROBADO (PASS), incluido el
    corolario de ventana √N. Resto: no controla el complemento infinito (m coprimo con Q) ni su
    integral con B; el error polinómico no es precisión relativa frente a componentes exponenciales; no
    incluye m = 1. Momentos firmados no son probabilidad (no Jensen).

26. **POWER_SIGNED_BALANCE_020.md** — Átomo F_{211,1}, u = 63/2. PROVED (PASS): cota superior uniforme
    ARCH_{N,1}/norm² ≤ U_N(u) (N ≥ 2, u > 0, por Jensen); U_211(63/2) < −0.74; 0 < P_2/norm² < 0.075;
    [ARCH + POLAR + P_2]/norm² < −0.66 (FAIL2). NO-GO (clase: reparar ARCH+POLAR en la columna k = 1
    sólo con el contacto 2). Reapertura: «cota unilateral de varios contactos o de su masa conjunta que
    conserve las compensaciones con ARCH y el polar». Positivo: la cota U_N(u).

27. **POWER_SIGNED_MEAN_019.md** — ERR: W[g_N]/c_0 = Arch_♯/c_0 − F_N, F_N = 2∫H_N E_0,
    H_N(x) = x^{−3/2}[½ρ_N − ρ_N′](log x). PROVED: B(x) = log(n!) − xH_n + n ≤ −(1−log 2)(x−1) (NEG);
    media de dilataciones A_N = 2∫H_N B ≤ −2(1−log 2)J_N(½) < 0 ∀N ≥ 2 (MEAN); F_N = 2∫h_N B (PAIR);
    h_N^{[3]}(1) < −19/256 para N ≥ 2^17 (FAIL3). NO-GO: «la inversión por dilataciones preserva
    positividad en cada prefijo»; sustituir h_N por su módulo. OPEN: (SIGNED)
    2∫h_N^+(−B) − 2∫h_N^−(−B) ≥ −Arch_♯[g_N]/c_0.

28. **POWER_SIGNED_MOMENTS_038.md** — Operador Möbius finito
    M_Qf(ℓ) = U_Q^{−1}Σ_{b|Q}μ(b)b^{−1}f(ℓ + log b) sobre el perfil gamma f_N. PROVED (auditado): para
    N ≥ 16, B_Q ≤ N/1000, ∀ℓ: |M_Qf_N(ℓ) − f_N(ℓ − A_Q)| ≤ 12000B_Q/N + 65√N(V_Q/U_Q + 1)e^{−N/2000}
    (SIGNED-FOURIER); WIDE-WINDOW (0.8)U_Q/m < K_{N,Q}(m) < (1.2)U_Q/m si A_Q ≤ log m ≤ A_Q + √N/100,
    N ≥ 2^80, Q = Π_{p ≤ N^{1/8}}p. Resto: suma exterior sobre m coprimo con Q e integral del residuo
    polar−peine.

29. **POWER_SIGNED_TRANSFER_014.md** — Telescopaje TEL (R − R_0)|F_0|² = R_0Σκ_j|G_j|²,
    G_j = sP/[(s+u)^{n−j+1}Π_{k≤j}(s+v_k)], y POLTEL. PROVED: EIGHT W > (1/1000)‖f‖² en ocho polos
    reales ≥ 63/2 arbitrarios; identidad FULL W[f] − c‖f‖² = R_0[(W[f_0] − c‖f_0‖²) +
    Σκ_j(W[G_j] − c‖G_j‖²)]; ONE W[f_v] = ρW[f_u] + (1−ρ)W[sF_u/(s+v)], ρ = u²/v². Criterio (no probado
    a todo orden): base confluente n y n+1 polos con transformada nula en 0 ⇒ n polos. Resto: «el test
    de dimensión doce con AP negativa sigue vigente».

30. **POWER_SIGNED_TRANSFORM_035.md** — Media de Abel A_N = W[g_N]/norm² = Σ_{m≤d}P_d(m)t_m,
    P_d(m) = a_m m(m²−1)/[2(2d−m)(2d−m−1)], d = N−1. PROVED (auditado): TAIL, SMALL, LARGE, WINDOW
    (M(M−1)/(4d) → Gamma(2)), BUDGET Σ_{m≤R}P_d(m)t_m ≥ −B_R·O(N^{−2}). Falsificador genérico:
    Θ = 3 + cosh(av) da A_{2,model} < 0. NO-GO: premisa T_m ≥ 0 (refutada en 034). Resto: estimar el
    promedio aritmético en la ventana móvil m ~ √N y sus colas ponderadas por t_m.

31. **POWER_SIMULTANEOUS_SHIFT_AUDIT.md** — Auditoría de SIMULTANEOUS_SHIFT_OBSTRUCTION: APROBADO.
    Determinante límite −9log²2/32; bloque inicial K(32+i,32+j) − K(34+i,34+j) no PSD; ampliación IMS
    aprobada (CrossR → −3√2/8). Sólo se refuta el orden Loewner con desplazamiento 2; no W, ni PSD de
    K, ni otros transportes restringidos.

32. **POWER_SIMULTANEOUS_SHIFT_OBSTRUCTION.md** — Defecto D(f,g) = W(f,g) − W(Tf,Tg), Tf = e^{−2t}f,
    paquetes concentrados en (ε, 2ε) y (log 2 + ε, log 2 + 2ε); resto IMS R = W[f] − W[Tf] − W[Sf],
    S = √(1−T²). PROVED: det D → −9(log 2)²/32; existe N finito con
    [K(32+i,32+j) − K(34+i,34+j)]_{i,j≤N} no PSD; R(f_ε, g_ε) → −3v_2/8 (IMS indefinido); Σ_rR[T^rf]
    tiene coeficiente d/(1−TT) → 1 cerca de (0, log 2). NO-GO (clase: orden PSD universal K − K_shift
    con desplazamiento 2; borrar IMS por telescopado). No excluye otros desplazamientos, normalizaciones
    con hipótesis nuevas, control firmado conjunto más fino.

33. **POWER_SIX_AUDIT_011.md** — Auditoría de SIX_GLOBAL_011. PROVED (PASS): BASE6 AP − (3/25)I PD;
    25 paneles x(c−m)_+ < 9; B6 = (49^6−1)/12; W > (23/500)‖f‖² en seis polos ≥ 31.5. Resto: siete
    o dimensión arbitraria «requiere hipótesis nuevas verificadas».

34. **POWER_SIX_GLOBAL_011.md** — Seis polos v_j ≥ 63/2; criterio CRIT b − c − DK_n − pη_n > 0 con
    K_n = [(1+X/u²)^n − 1]/X, η_n = 1 − (1−1/(4u²))^n; cota all-pass WT ‖e^{σy}f‖² ≤ B_n(α)‖f‖².
    PROVED: SIX W > (1/25)‖f‖²; CRIT y WT como teoremas generales (todo n, condicionales a las
    constantes). Resto: «no asegura que esas constantes existan con margen para todos n»; la mejora
    ponderada «no reemplaza la compensación positiva del peine cuando resulta necesaria».

35. **POWER_STATE_003.md** — Estado OPEN. Registra BRIDGE_002 (basta K_ij PSD en la escalera
    a = 32+i), FIXED_GRID_003 (órdenes 1–6 certificados), POLYNOMIAL_003 (dilataciones no autoadjuntas
    ni contractivas; identidades sin signo), falsificadores de SCHUR_003. No relanzar: «La unión de
    rangos altos u ≥ 2^{40n} no es densa […]: no extrapolar esa familia»; evitar Gram monomial cerca de
    la confluencia (falsos negativos).

36. **POWER_STATE_004.md** — Registra PROVED tres potencias a_i ≥ 32: Q[ρ] ≥ (1/20)‖f‖²
    (POLE_MOVEMENT_004; monotonía de ARCH por covarianza al subir polos). NUMÉRICO (diagnóstico):
    confluente de dimensión 4, ARCH ≈ −0.17005, ARCH+POLAR ≈ 0.32259. Resto: escalera 32+k a todo
    orden. «No extrapolar triples ni los seis tamaños ya certificados».

37. **POWER_STATE_006.md** — Registra CONFLUENT_FOUR_005 (W > 1/5), POLAR_MOVEMENT_005 (transporte AP
    LOCAL), ARITHMETIC_WITNESS_006 (vector de dimensión 12: AP ∈ (−2/125, −1/100), W > norm²/50; sin el
    contacto 2, W < −norm²/125). NO-GO: monotonía ARCH+POLAR sin restricción de tasas (u: 1 → 2);
    monotonía universal de Rayleigh AP a numerador fijo (HIGH_ORDER_PM_NOGO_007). Resto: compensación
    conjunta en una familia densa, «no sumar familias positivas por separado».

38. **POWER_STATE_008.md** — Registra ARITHMETIC_BLOCK_007: W > ‖h‖²/10000 en todo V12 (AP indefinida;
    contacto 2 necesario). NO-GO: PRIME_PATTERN_FALSIFIER_008, f = (D² − ¼)[y^{n−1}e^{−31.5y}],
    n = 2^17: ARCH < −3.83‖f‖² y cada contacto ≤ 1024 empeora («2 repara» no es patrón universal).
    Resto: (TAIL) del test 008; desigualdad para la suma aritmética COMPLETA con autocorrelación de
    signos mixtos. No repetir monotonía AP en dimensión ni inferencia desde contactos favorables.

39. **POWER_STATE_012.md** — Tabla PROVED de polos arbitrarios ≥ 31.5: ≤ 3 (1/20), ≤ 4 (2/25),
    ≤ 5 (1/100), ≤ 6 (1/25), ≤ 7 (1/500). Cadena Tate W[f_n] = 992^{2−n}Δ²q_n con convexidad abierta.
    NO-GO (DEFICIT_LIMIT_013): en dimensión 8 el mejor déficit uniforme puntual directo no permite el
    transporte (margen < 1/25 < pérdida > 1/20); excluye afinar constantes en esa clase. Reapertura:
    conservar la integral firmada del filtro (hecho en 014).

40. **POWER_STATE_014.md** — Registra EIGHT y CONFLUENT_BRIDGE_014: para u > ½ fijo los bloques
    span{y^ke^{−uy}: k < N} son densos en una norma H¹ ponderada que controla la forma; basta W ≥ 0 en
    cada bloque confluente de una tasa, sin margen uniforme. Identidad de un polo
    W[f_v] − R_0W[f_u] = (1−R_0)W[sF_u/(s+v)]. Resto: todos los tamaños confluentes > 12.

41. **POWER_STATE_015.md** — Registra HIGHPASS_015 (para u > 1, N fijos existe K_N con W > 0 en Q^kV_N,
    k ≥ K_N; ARCH normalizada ≥ (log k)/2 − C_N; K_N no efectivo) y GEOMETRIC_TRANSFER_015 (transporte
    de polos como mezcla positiva de W[Q^kf_base]). Resto: segmento finito inicial de bloques para cada
    N; la positividad eventual no da la inicial. «No repetir una campaña de certificados finitos».

42. **POWER_STATE_016.md** — Registra DESCENT_016 W[f] = W[Qf] + W[Lf]; refinamiento binomial;
    JOINT_SCALE_016 (contactos → cos(u√c t) si k/N → c; Jensen impide uniformizar pesos exponenciales en
    N); DESCENT_AUDIT_016 (límite fuerte común sólo 0); falsificador W_4 = W − 4‖·‖². No relanzar:
    densidad de colas, desaparición uniforme de contactos en conos lineales, pesos exponenciales
    uniformes en N. OPEN no refutados: escala cuadrática espectral y conos de signo.

43. **POWER_STATE_017.md** — Registra SCALAR_BRIDGE_017; INTERIOR_017 (N = 1, todo k, u ≥ 63/2:
    W > 4norma²/3); QUADRATIC_017 (W > 0 para k ≥ cN², N ≥ N_0(c)); QUADRATIC_EXPLICIT_017
    (W > 49norma²/50 para N ≥ 2, k ≥ 10000N², u = 31.5). Resto: regiones inferiores con ambos índices
    crecientes fuera del cono.

44. **POWER_STATE_018.md** — Registra filas 2 y 3 (> 1/8), recurrencia a_{N,k} = a_{N,k+1} + u²a_{N+1,k},
    LOW_TABLE_018 (presupuesto D_N(θ) = 2 + 2θJ_N(θ−½)). NO-GO: modelo arcoseno
    V[f] = 2‖f‖² − (u/100)|F(iu)|² conserva identidades, 12 polos, filas 1–3 y el cono, con entrada
    (40402, 40401) negativa. Resto: N ≥ 4, k < 10000N². «No se continuará una campaña fila4, fila5».

45. **POWER_STATE_019.md** — Registra ARITHMETIC_DIFFERENCES_019 (raíz simple χ_N,
    √(2N−3) < χ_N < (1+√(8N−11))/2; peine completo > 0 en k = 1, N ≤ 211; < 0 en k = 0 ∀N) y
    SIGNED_MEAN_019. Resto: combinar peine firmado con ARCH y polar a órdenes variables; no extrapolar
    dilataciones a ERR ni prefijos al inverso.

46. **POWER_STATE_020.md** — Registra INVERSE_KERNEL_020: H_N/4 ≤ h_N ≤ 7H_N/4 si N ≥ 2 y
    log x ≥ (N−1)/30; h_2 ≥ H_2/[2ζ(32)] en toda la semirrecta (parte negativa de h_N localizada en
    [1, e^{(N−1)/30})), y FAIL2. Resto: emparejamiento interior de h_N con B.

47. **POWER_STATE_021.md** — Registra CONTACT_BALANCE_021 PROVED (átomo 211,1): ARCH + POLAR + contactos
    2,3,4 < −0.21norma²; cola q > 300 ∈ [0, 5·10^{−13}]norma². NUMÉRICO: parcial hasta 300 ≈
    −6.08·10^{−14}norma² (no certifica). Resto: desigualdad que conserve cancelaciones; no volver a la
    reparación por un solo contacto.

48. **POWER_STATE_022.md** — PROVED −2/3 < h_128(1) < −33/50 (cola Möbius < 10^{−10}). NO-GO
    (falsificador): h_N(x) ≥ 0 ∀N, x. Pivot: primitiva J_N = ∫_x^∞h_N y K_N = J_N + xh_N. «No se relanza
    la positividad global de h_N […] ni se usa el módulo para borrar la región adversa».

49. **POWER_STATE_023.md** — PROVED −1/250 < K_129(1) < −1/251; ΣJ_N(n) = 1;
    ERR = −2∫K_N C_B, C_B(t) = −t^{−2}∫_1^t x dB > 0; daño de K^− en [1, 1+δ] ≤ δ²sup K^−. NO-GO: h ≥ 0 y
    K ≥ 0 universales. Resto: promedios celulares o parte negativa ponderada por C_B.

50. **POWER_STATE_025.md** — Registra ERR_129 < −33/50 (LOGCONCAVITY_025; CELL_TEST_024
    S_129(2) > 33/100); D_N = 33P_N − P_N′ con D_N′/D_N decreciente ∀N; presupuesto celular
    S_n = b_nJ(n) + (H_{n−1}/2)∫_cell[1 − (n−1)²/t²]K, b_n ≥ 0.75 − log 2. Resto: comparar ERR con
    ARCH_♯; extensión a órdenes variables. No relanzar K ≥ 0 universal.

51. **POWER_STATE_026.md** — Registra UNIFORM_CUTOFF_026 (K_N(x) ≥ x^{−32}D_N(log x)/4 > 0 tras un corte
    d/330 + O(1); K_N > 0 para 2 ≤ N ≤ 129, x ≥ e^{2/3}) y ARCH_CELL_026 (ARCH_♯129/norma² < −0.81;
    W[g_N]/norma² = ∫K_NΩ con Ω(3/2) < −0.1). NO-GO: positividad puntual universal de Ω y de K. Resto:
    balance conjunto con la curvatura gamma.

52. **POWER_STATE_027.md** — Registra DISCRETE_BALANCE_027 (Ω(t) ≥ ℓ − (4log t + 9)/t, ℓ > 1/50; cola
    0 < ∫_{4096}^∞K_129Ω < 10^{−36}) e INTERIOR_CONSTRAINT_027 (W_gamma − W_gauss = ∫L_N(a)G_W″(a)da;
    G_W″(a) < 0 ∀a ≥ 65536). NO-GO: convexidad global del funcional gaussiano real. Resto: interior
    ∫_1^{4096}K_129Ω sin signo; «No basta una mezcla positiva con curvatura firmada ni otra cola
    favorable diminuta».

53. **POWER_STATE_028.md** — Registra ROW4 y ROW5; cobertura: filas 1..5 ∀k, u ≥ 31.5; cono
    k ≥ 10000N²; ocho polos; V12. Resto: N ≥ 6 bajo el cono. «No se sustituye el objetivo de todos N a
    tasa fija por un resultado con tasa creciente».

54. **POWER_STATE_029.md** — Registra ROW_PATTERN_029 (u² ≥ 256N, k ≥ 1: > 7/10), BOUNDARY_WEDGE_029
    (u² ≥ 4096N: > 2/5) y la obstrucción GAP. Resto: «recuperar información en N/u² grande y conservar
    las cancelaciones aritméticas».

55. **POWER_STATE_030.md** — Registra INTERIOR_SCALE_030: W[g_N]/norma² = ∫_1^∞G_N H,
    H(x) = 1 + [log((x+1)/(x−1)) − γ − log(4π) − 1 − 2Σ_{q≤x}qΛ(q)]/x²; ∫_1^{9/4}G_N H > 1/100
    (N ≥ 2^20); GAMMA_BALANCE_030: 0 < A_♯(EV) − ARCH_♯/norma² < 1/[2(N−3/2)]. NO-GO: primitivas de H
    positivas (falsas hasta 5/2); comparación gamma–gaussiana de formas completas sin coste (falsa en
    N = 2). Resto: ∫_{9/4}^∞G_N H.

56. **POWER_STATE_031.md** — Registra WEIGHTED_BLOCK_031 (∫_1^{225/64}G_NH < −3/1000, ∫_1^4 > 3/200)
    y GAMMA_WEIGHT_031 (R_N = ρ_N − (2/3)ρ_N′, máximo único T_N < 2/3;
    W/norma² ≥ ∫_{T_N}^∞I_*(e^t)[−R_N′]dt − M2). NO-GO: I_* ≥ 0 universal. Resto OPEN: promedio
    firmado de I_* contra −R_N′; «Enumerar otros bloques […] no sustituiría esa obligación».

57. **POWER_STATE_032.md** — Registra CONTACT_DECISION_032 PROVED: 3.4·10^{−15} < W[f]/‖f‖² <
    4.5·10^{−15} para F = s/(s+63/2)^{212}; ARCH_EXACT_032. Resto: compensación estructural de todos los
    contactos o el promedio 031; «no lanzar una campaña de más puntos».

58. **POWER_STATE_033.md** — Registra PRIME_BALANCE_033 (w(mq) ≤ m^{−2}w(q), contracción ρ = 2389/3600,
    0 < S_K ≤ A(w) ≤ S_K/(1−ρ^{K+1})) y COEFFICIENT_BALANCE_033 (mezcla Erlang S_j; −0.01 < L[S_22] <
    −0.006). NO-GO: funcional positivo por componente Erlang. OPEN (luego refutado en 034):
    T_m = Σ_{j≤m}jL[S_j] ≥ 0 ∀m.

59. **POWER_STATE_034.md** — Registra DIVISOR_COMPARISON_034: W[f_{N,k,u}] > ‖f‖²/40 para N ≥ 3, k ≥ 1,
    u² ≥ 225N/4 (k ≥ 2: > 3/20); a u_0: filas 1..12 completas; a todo u ≥ u_0: filas 1..8;
    WEIGHTED_COEFFICIENT_034: T_m cambia de signo en índices arbitrariamente grandes. NO-GO:
    positividad de T_m componente a componente (ni salvo finitos índices). Resto: k = 0 para N ≥ 13.

60. **POWER_STATE_035.md** — Registra BOUNDARY_BALANCE_035 (terminal N = 17, k = 0, margen > 0.041;
    recurrencia A_{N0} = A_{N1}/(2N) + (2N−1)A_{N+1,0}/(2N)): W > norma²/40 para 1 ≤ N ≤ 17, todo k,
    u = 63/2 (átomos individuales). Resto: N ≥ 18 bajo el cono; promedio firmado de 035 OPEN.

61. **POWER_STATE_036.md** — Registra RECURRENCE_BOUNDARY_036 (contribución del cono en profundidad L:
    0 ≤ C_L = O(log(L+2)/√(L+1)) → 0) y MOVING_BALANCE_036 (leyes ponderadas por polar y por |peine|:
    m/d → 1/32; fase (3969/3968)^N). NO-GO: omitir el resto diagonal; descartar colas por separado por la
    concentración de 035. Resto: conservar conjuntamente polar y aritmética antes de estimar colas.

62. **POWER_STATE_037.md** — Registra ENERGY_GROUP_037: cotas de mH_N(mx_N)/H_N(x_N) ~ 1/m; suma
    absoluta de términos Möbius no principales > 1 (N ≥ 2^16); con Q = Π_{p ≤ N^{1/8}}p, módulos del
    resto agrupado > 1.48 frente a principal < 0.505. NO-GO: contracción o dominación absoluta del resto
    (también agrupado); «mejorar sólo constantes de las mismas cotas absolutas no resuelve». Resto:
    complemento firmado y su integral.

63. **POWER_STATE_038.md** — Registra SIGNED-FOURIER y WIDE-WINDOW (entrada 28). Resto: suma sobre m
    coprimo con Q y su integral en el residuo polar−peine; precisión frente a componentes exponenciales.

64. **POWER_STATE_039.md** — Registra INFINITE_SHOULDER_039: h_N, K_N > 0 para x ≥ e^{T_N},
    N ≥ 4·10^6, T_N = 2(N−1)v_N/(u² − v_N²), v_N = ½ + 1000/√N; ψ_Λ(x) ≤ 2x. Resto: interior y σ = 1.

65. **POWER_STATE_040.md** — Registra CRITICAL_BALANCE_040 (N ≥ 2^80, v = ½ + N^{−2}):
    h_N/H_N < −1/N y K_N/G_N > 1/N en el mismo centro e^{t_v}; h_N, K_N > 0 para t ≥ (N−1)/992 + 5;
    1/ζ(1+z) = z − γz² + R_3, |R_3| ≤ 9|z|³. Resto: contribución interior y balance con ARCH_♯.

66. **POWER_STATE_041.md** — Registra ENERGY_BAND_041: 2∫_{e^T}^{e^{T+L}}h_N B < −C_N/25600
    (N ≥ 2^80, L = √N/100); B(x) = −γx − B_1({x})log x + κ + E(x), −1/x < E < 1/(2x). Resto: el
    complemento; no sumar beneficios de representaciones distintas sin bordes; no intercambiar con
    Σ|μ(n)|/n (diverge).

67. **POWER_STATE_042.md** — Registra RENORMALIZED_TAIL_042 (entrada 4). Resto: interior renormalizado de
    1 a X y después la tabla/portador.

68. **POWER_STATE_044.md** — Registra ASYMMETRY (reflexión falsa) y la revisión de L55-B: medida positiva
    discrepante no basta; candidatos primales no dan lower; L55-B «permanece abierta como construcción
    pendiente». Sin región nueva.

69. **POWER_STATE_045.md** — Corrección documental: ROUND_026_A registra λ_A(T) ≥ 2·10^{−26} para
    0 < T ≤ 1.035 (certificación asistida por computadora, logs revisados, no reproducidos); T = 1.098 sin
    certificado final. CONTACT_FLOOR_045: m(240) − A_T < −½ al entrar el contacto 5. PRIMAL_PAIR_045:
    para medidas PARES, cola real fija + corrección compacta ⇒ corrección nula; a T = 3/5 símbolo en 0
    < −15/2. NO-GO: corte 240 + piso de masa total en lowercert; ansatz par compacto para L55-B. No
    excluye correcciones no compactas o no pares.

70. **POWER_STATE_048.md** — Registra SUBQUADRATIC_048 (N ≥ e^{10^6}, k ≥ 2N²/log log N:
    W > (2/5)log N·‖f‖²) y R12_ENDPOINT_048 (E2[G] > ‖G‖²/50 en V13 con G(0) = 0; E2 = AP + contacto 2;
    polar de Q^jV12 con razón ≤ 9/62). Resto: banda inferior; hipótesis uniforme de 046; R12 para v ≥ u.

71. **POWER_STATE_049.md** — Registra R12 PROVED: E2[sF/(s+v)] > ‖·‖²/2500 ∀F ∈ V12, v ≥ u;
    CENTERED_CUTOFF_049 (j ≥ 14: E[τ^{−2}] < 1/405, ARCH > 859/800; j = 1..13 por LDL). Resto: contactos
    n ≥ 3 no transportados; varios polos movidos no se iteran automáticamente.

72. **POWER_STATE_050.md** — PROVED (FULL_TWELVE_050): W[P/Π_{i=1}^{12}(s+v_i)] > ‖·‖²/10000 ∀v_i ≥ 63/2,
    grado P < 12; trece polos con numerador divisible por s: W > ‖·‖²/250. Mecanismo: MULTI_015 +
    FULLTEL_014 + traza (α = ½). Resto: órdenes arbitrarios. Positivo: doce polos arbitrarios.

73. **POWER_STATE_052.md** — PROVED (CONFLUENT_THIRTEEN_052): W > ‖f‖²/4000 en V13; pivote de Schur
    complementario a F(0) = 0 en (0.0003, 0.0005); contacto 3 adverso en el pivote; contacto 2 adverso en
    la dirección central de E2. No relanzar: «patrón de mejora por cada contacto añadido». No obtenido
    (sin declarar imposible): norma ponderada uniforme en j para Q^jV_n.

74. **POWER_STATE_053.md** — PROVED (FULL_THIRTEEN_053): W[P/Π_{i=1}^{13}(s+v_i)] > ‖·‖²/4000; catorce
    polos con D(0) = 0: W > norma²/1000; E23[Q^jF] > norma²/10 para j ≥ 96 y > norma²/500 para j ≤ 95.
    Resto: control uniforme del segmento inicial al variar la dimensión; catorce polos generales.

75. **POWER_STATE_054.md** — PROVED (EFFECTIVE_HIGHPASS_054): C_n = 9n²9^n, D_n = 10C_n n!,
    A_n = 6C_n n·n!, K(n) = max(10000n², A_n3^{4D_n+20}); ∀n, P de grado < n, j ≥ K(n):
    W[Q^jP/(s+u)^n] > ‖·‖². Duplicados: extrapolación absoluta de momentos (= 016); renombrar el resto
    como energía negativa (= 036). Resto: segmento j < K(n), sin eliminarlo por recurrencia ni masa.

76. **POWER_STATE_055.md** — Auditoría de alcance: W_4 conserva DEF/BIN/MIX/MULTI/FULLTEL y el corte K(n)
    pero es negativa en e^{−63t/2} (corte efectivo + identidades no dan signo inicial). Selberg S = U − V
    (actualización: criterio W ≥ 2V refutado en 067). Turán:
    a_{N,k}a_{N+2,k} − a_{N+1,k}² = W restringida a numeradores {1, u² − s²}. Duplicados: bolsillo
    225/64 + recuperación 4 (= 031); recombinación 042 (= 030); Turán de valores completos (= 046).

77. **POWER_STATE_059.md** — Registra STRIP_NECESSITY_059 (no hay contorno uniforme con p < 2). Pendiente
    (no probado): contorno independiente de n en un cono polinómico separando partes par/impar; el
    generador −i(y²h′ + yh) no autoriza comparación gaussiana global. Duplicados 055–058: Selberg/Turán,
    cruces de filtros, representaciones exteriores.

78. **POWER_STATE_060.md** — PROVED (UNIFORM_STRIP_060): J(n) = 10^{12}(nq_n)³, q_n = ⌈log₂(n+1)⌉;
    ∀n, P de grado < n, j ≥ J(n): W[Q^jP/(s+u)^n] > ‖·‖²; densidad desplazada a altura 3 con integral
    absoluta < 2× la real, constante independiente de n y P. Resto: j < J(n); sin cono cuadrático
    uniforme.

79. **POWER_STATE_061.md** — PROVED (GAMMA_129_DECISION_061): 1.34·10^{−10} < W[g_129]/‖g‖² <
    1.35·10^{−10}; ARCH_♯ ≈ −1.042193970181, ERR ≈ −1.042193970315. NO-GO (aplicación de 016/029): el
    cono 060 no sustituye por aproximación positiva la familia completa (masa en [−u,u] ≤ 16·10^{−12}).
    Resto: controlar el balance firmado al tamaño del residuo.

80. **POWER_STATE_062.md** — Balance renormalizado en el átomo 129: AFF ∈ [−60446492280,
    −60446492279]/10^{12}, R ∈ [−30223246208, −30223246207]/10^{12}, W/norma² = AFF − 2R (PROVED,
    diagnóstico). NO-GO: la parte afín no es base positiva para despreciar el resto. Duplicados: acotar R
    por celdas; vía factorial/Stirling. Resto: diferencias en N de J, K y ARCH_♯.

81. **POWER_STATE_064.md** — Registra STRIP_CUBIC_NECESSITY_064 (p ≥ 3 necesario para STRIP en todos los
    numeradores). Identidades B_N = A_N + u∂_uA_N, A_{N+1} = (2NA_N − B_N)/(2N−1) (deduplicadas). Resto
    OPEN: B_N ≤ 2NA_N (propagaría A_N ≥ 0), o B_N ≥ A_N con liminf A_N ≥ 0.

82. **POWER_STATE_065.md** — PROVED (CONTACT_OSCILLATION_065): la autocorrelación de s^k/(s+u)^{N+k}
    tiene exactamente k ceros positivos simples, alternancia desde +, última raíz en ut < 4k(N+k−1);
    cola de contactos con signo (−1)^{k+1}. Identidad W/‖f‖² = ARCH_♯/‖f‖² + 2∫D(x)w′(x)dx; Rodrigues
    para pesos φ(t²). NO-GO: atribuir convexidad φ^{(k)} ≥ 0 al peso completo de W (átomos ⇒ derivada de
    δ). Resto: comparar E_{ν+}D − E_{ν−}D por intervalo nodal; bordes [E_1w′] no omitibles.

83. **POWER_STATE_067.md** — Registra SELBERG_DROP_067. Reagrupación por soporte primo (coeficientes de
    μ∗log² y Λ∗Λ: (2a−1)log²p y (a−1)log²p en p^a; 2log p log q en p^aq^b; 0 con ≥ 3 primos) reconstruye
    S. OPEN: G_W(v) ≥ 0 ∀v > 0 (transferiría a toda la fila k = 0). Duplicados: cruces entre contactos;
    productos ρ(log a)ρ(log b).

84. **POWER_STATE_073.md** — PROVED (THETA_HAZARD_COMPACT_073, THETA_TWO_COPY_073; 4096 paneles):
    V‴ > 0 ∀t > 0; M″ < 0, M − uM′ > 0 ∀u > 0; 1 < L(a)/L(b) < (a−½)/(b−½) para a > b > 1; K de dos
    exponentes distintos > 1 PD (forma completa). Resto: tres generadores, todo orden, cinco tilts de
    103_43. Positivo: todos los pares a, b > 1.

85. **POWER_STATE_074.md** — PROVED (contraejemplo auxiliar TWO_COPY_SCOPE_074):
    V(x) = A[x²/2 + x^{2p}/(2p·2^{2p−2})], p = 10^6, A = 4·10^8, cumple toda la hipótesis de 073 pero
    cᵀKc < −53111/(10000A) en nodos A, 2A, 3A, c = (40, −40, 3). NO-GO (clase: la hipótesis de potencial
    de 073 implica orden tres). OPEN-JET: t ≤ (1−r)(1+2r), r = uM′/M, t = −u²M″/M.

86. **POWER_STATE_075.md** — PROVED (THETA_SCHUR_DENSITY_075): H_u = D_u/[z(z²−u²)] = ∫Φ_ue^{zx} con
    Φ_u > 0, (log H_u)″ > 0; F1 = −cz/u + c²Z/(uzH_u), R = uc²/(ua−c). Consulta 076: defecto T_u con
    densidad (u/c)[J − βΦ_u] de masa 0; criterio suficiente de un cruce. NO-GO: en el auxiliar 074
    G_A(3A) < 0 (el cruce no es genérico).

87. **POWER_STATE_077.md** — PROVED (THETA_REMAINDER_077 y certificados): F_u = J − βΦ_u con un único
    cero positivo simple; T_u > 0, G_u > 0 ∀u, z > 0; C > 0, N > 0 en t > 0. Corolario anclado {0,u,v}.
    Apéndice 078: CURVATURE-OPEN (h″, g″ ≤ 0) suficiente para pares de G_p; g″ ≤ 0 ⟺ OPEN-JET;
    g″ < 0 (u ≥ 63/2), h″ < 0 (u ≥ 128), a > 1/25. Resto: G_u > 0 no da kernel PSD.

88. **POWER_STATE_080.md** — PROVED (THETA_G_COMPACT_080 + THREE_SECANTS_079; 4096 paneles, hash): para
    a_i > 1 cualesquiera, W > 0 en el espacio de hasta tres potencias. Resto: cuatro generadores (luego
    085); no se usa herencia de BASE por G_p (refutada en 081).

89. **POWER_STATE_085.md** — PROVED (FOUR_GENERATORS_085, FOUR_TURAN_084, RECIPROCAL_PFAFFIANS_083;
    16384 paneles, hash): para a_i > 1 cualesquiera, W > 0 en el espacio de hasta cuatro potencias;
    det K4 = Pf_R·Pf_S/ΠR. Resto: cinco generadores, todo orden.

90. **POWER_STATE_089.md** — PROVED: W_t(1,A,B,C) < 0 ∀t > 0; T_R = 2R′R‴ − 3R″² > 0 ∀λ > 0; h = 1/b
    estrictamente cóncava; todos los pares de G_p PD. NO-GO: herencia genérica T_f ⇒ T_H
    (w = (5−e^{−x})/4: T_H(0) = −1/192); G_p no hereda BASE ni sus Turán. Resto: S4 global; T_h
    (luego 099).

91. **POWER_STATE_099.md** — PROVED (EXACT_H_GLOBAL_099, 2048 paneles, hash): T_h > 0 ∀x > 0;
    R_G″, S_G″ < 0; todos los triples de K_{G_p} PD; K_M en {0, p, z_1, z_2, z_3} PD (0 auxiliar). Resto:
    cinco generadores admisibles; herencia al siguiente nivel.

92. **POWER_STRIP_CUBIC_AUDIT_064.md** — Auditoría de STRIP_CUBIC_NECESSITY_064: APROBADO, umbral
    mejorado a j ≥ 10^6n. Alcance: sólo excluye la estimación ABSOLUTA de contorno uniforme; «Los
    métodos que conserven cancelación firmada y el problema del interior siguen abiertos».

93. **POWER_STRIP_CUBIC_NECESSITY_064.md** — Numerador P_{n,j} desde el polinomio ortonormal de grado
    n−1 del peso Student (1+y²/j)^{−(n+j)}. PROVED/APROBADO: para n ≥ 4, j ≥ 10^6n,
    ∫|ρ(x+iη)|/∫ρ ≥ 1 + η²n³/(1152u²j). NO-GO (clase: STRIP absoluto con η, D fijos, uniforme en
    todos los numeradores, en conos j ≥ Cn^p, p < 3). No excluye cono de signo W con exponente menor.

94. **POWER_STRIP_NECESSITY_059.md** — (STRIP) ∫|ρ_{n,j}(x+iη)| ≤ D∫ρ_{n,j} para s^j/(s+u)^{n+j}.
    PROVED: falla en toda sucesión n ≤ j = o(n²) (varianza exacta y paquete E cos(t_nZ) → 1). NO-GO
    (clase: STRIP con η, D fijos, p < 2, ya con P = 1). No refuta D dependiente de n ni cono de signo.

95. **POWER_SUBQUADRATIC_AUDIT_048.md** — Auditoría de SUBQUADRATIC_COROLLARY_048: APROBADO
    (W/norma² > L/2 − (113/2)√L − 20 > (2/5)L, L = log N ≥ 10^6); «extracción de 017, no una nueva
    desigualdad aritmética». Resto: banda inferior, lower de 046, resto energético 036.

96. **POWER_SUBQUADRATIC_COROLLARY_048.md** — Cuatro bounds de QUADRATIC_017 válidos ∀c > 0, N ≥ 2,
    k ≥ max(cN², 4N), con c_N = 2/log log N. PROVED: N ≥ exp(10^6), k ≥ 2N²/log log N ⇒
    W[f_{N,k}] > (2/5)log N·‖f‖² (SUBQUADRATIC). Resto: k < 2N²/log log N; el complemento de la nueva
    frontera no se vuelve energía evanescente (036 sigue).

97. **POWER_TABLE_AUDIT_018.md** — Auditoría de TABLE_DESCENT_018 y LOW_TABLE_018 y modelo
    V[f] = 2‖f‖² − εu_0|F(iu_0)|² (ε = 1/100). APROBADO: filas 2, 3; presupuesto D_N(θ). V conserva
    Pascal, filtros, ≤ 12 polos (V ≥ (47/25)‖f‖²), filas 1–3, cono (1.98), positividad eventual, pero
    b_{40402,40401} < 0. NO-GO (clase: completar la tabla con recurrencias, identidades de filtros y
    regiones positivas). Reapertura: «información adicional de la forma aritmética concreta».

98. **POWER_TABLE_DESCENT_018.md** — Filas 2 y 3. PROVED: W[f_{2,k}], W[f_{3,k}] > (1/8)‖f‖² ∀k ≥ 0,
    u ≥ 63/2 (ROWS23); DIFF: a_{1,k} − a_{1,k+1} > c_k/[32u(k+1)], segunda diferencia >
    3c_k/[64u(k+1)(k+2)]; ψ′ ≤ 1/x + 1/x², ψ″ ≥ −2/x³ − 1/x². Resto: N ≥ 4; no monotonía completa;
    monotonía AP bajo movimiento de polos «en general es falsa». Positivo: ROWS23, DIFF.

99. **POWER_TATE_CHAIN_009.md** — Cadena f_n = (∂² − ¼)g_n: c_{f_n} = a²C_n − 2aC_{n−1} + C_{n−2},
    a = 992; q_n = a^n(I_n − J_n) + 2, J_n = (2/Γ(n)²)Σβ_{nj}(−1)^jD^{(j)}(u+½), D = −ζ′/ζ. PROVED:
    W[f_n] = a^{2−n}Δ²q_n (CHAIN); ARCH normalizada estrictamente decreciente en n (MON); para
    n ≥ 64u², n ≥ 2u²(log R)², cada contacto ≤ R perjudica; los miembros individuales no son densos.
    OPEN: Δ²[a^n(I_n − J_n)] ≥ 0 ∀n ≥ 4. No relanzar: Λ∗1 = log, H_j > 0, convexidad genérica.

100. **POWER_THETA_AUDIT_073.md** — Auditoría de HAZARD_COMPACT_073, exterior 103_43 y TWO_COPY_073:
     APROBADO (4096 paneles PASS); (log Φ)‴ < −20 para t ≥ ¼; dos copias M″ = 4Cov(S, D²) < 0;
     L′ > 0, L″ < 0, L − (a−½)L′ > 0 ∀a > 1. Alcance: no es «un principio general Pick ni una inducción
     de todos los órdenes»; las inclinaciones polinómicas de 103_43 son otra obligación.

101. **POWER_THETA_CURVATURE_AUDIT_078.md** — Auditoría del apéndice 078: APROBADO.
     g″ = v[2r² − r + t − 1]/(4u⁴), h″ = v[(r−1)(2r+v−3) − (v−1)t]/[4u²(v−1)³]; g″ < 0 (u ≥ 63/2,
     Δ > 423/10000), h″ < 0 (u ≥ 128, v > 3, a_0 > 1/25); b(u²) = Z_K/Z_J. Resto (entonces): compactos
     de g″ y h″; luego cerrados en 080/089.

102. **POWER_THETA_DENSITY_COMPACT_089.md** — Wronskiano de ρ = tΦ(1,A,B,C), A = p² − q − 2p/t,
     B = p/t, C = (p³−3pq+r)/t; K = W_t(ρ) = 64t^{10}W_λ(Ψ). PROVED (1024 + 8192 paneles, hash):
     W_t(1,A,B,C) < 0 ∀t > 0 (GLOBAL-R4); determinante de densidades < 0 en todos los nodos (Rolle en
     coordenada B); kernel sinh(√λt)/√λ TP4; Andreief: T_R = 2R′R‴ − 3R″² > 0 ∀λ > 0. Resto: lado S,
     niveles superiores; sin nueva cobertura W.

103. **POWER_THETA_DENSITY_COMPACT_AUDIT_089.md** — Auditoría de 089: APROBADO / PROVED (FULL PASS,
     hash); colas theta 304·17⁴/4^{289} y 8576·17⁴/8^{289}; restos < 10^{−18}, < 10^{−39}; consecuencia
     h = 1/b estrictamente cóncava y todos los pares de G_p PD. Resto: «No se descarga la otra curvatura
     recíproca del resto ni Turán su posterior, no herencia general Schur. No S4».

104. **POWER_THETA_DENSITY_CONCAVITY_086.md** — Tres densidades ρ = (tΦ, (tΦ)″, −Φ′) = tΦ(1,A,B);
     (A′/B′)′ = tN/(pD²) > 0 (N de 077). PROVED (auditado): det[ρ_l(t_j)] < 0 en nodos ordenados;
     sinh TP3 y versión confluente; (Z′, u²Z′, uZ) = 2∫sinh(ut)ρ; R(λ) = √λ/M(√λ) cumple R″(λ) < 0
     ∀λ > 0 (GLOBAL-CURVATURE), luego triples PD sin el certificado 080. Resto: densidades superiores de
     083 («el signo de su determinante no se obtiene de este menor»).

105. **POWER_THETA_DENSITY_CONCAVITY_AUDIT_086.md** — Auditoría de 086: APROBADO / PROVED para Φ real
     (identidad (A′/B′)′ reproducida simbólicamente; Andreief con densidades firmadas; factor 8 correcto;
     W(f) = f_1³R″). No extiende admisibilidad a a_i ≤ 1; no nueva cobertura frente a 080/085; queda «un
     mecanismo estructural concreto para estudiar esas obligaciones superiores».

106. **POWER_THETA_DENSITY_ORIGIN_087.md** — Cuatro densidades (1,A,B,C); RAISE
     W_t(1,A,B,C) = −k³J²(E/J)′, coeficiente de V^{(6)} en W_t igual a −N/(pt⁴); matriz ORIGIN-MATRIX
     en λ = 0 con a_j = Φ^{(2j)}(0)/[(2j)!Φ(0)]. PROVED (punto y entorno no cuantificado): Wronskiano en
     el origen NEGATIVE (≈ −3.56·10^9, intervalo racional); JET-RAISE [v10]W_R4 = W_R3/840. Resto
     (entonces): (E/J)′ > 0 global, cerrado después en 089; S4 no tratado.

## A. «No relanzar» deduplicado, con condición de reapertura

Cada ítem indica su fuente en este bloque y su situación en `RULES_AVOID.md` («RA»): **AUSENTE**,
**PARCIAL** (cubierto sólo por una fórmula general) o **INEXACTO** (se citan ambos textos).

A1. Simetría de reflexión q ↔ 1−q para eliminar el sector antisimétrico del puente escalar (2, 68).
    Reapertura: control cuantitativo desigual del sector restante. **AUSENTE.**
A2. L55-B con ansatz par, cola real fija y corrección compacta; masa espectral total finita; medida
    positiva discrepante; candidatos primales como lower (1, 68, 69). Reapertura: corrección no compacta
    o no par, con igualdad en todo el portador primitivo y discrepancia controlada. **AUSENTE.**
A3. Corte 240 y piso de masa total m(240) − A_T en lowercert (69). Reapertura: otro corte o cotas del
    símbolo real (como ROUND_026_A). **AUSENTE.**
A4. Sustituir el cono de átomos del puente 017 por regiones de tasa creciente u ≥ C√N o por el cono 060
    mediante mezclas positivas de densidades (11, 79). Reapertura: otro puente, identidad con
    estructura adicional o control directo. **PARCIAL**: RA D3 dice «Inferir densidad o signo de una
    unión positiva»; no menciona la obstrucción GAP de aproximación L¹.
A5. Preservación del paso Schur desde F′ ≥ 0, F/z decreciente (y concavidad); F_1′ ≥ 0 como invariante
    (12, 35). Reapertura: propiedad aritmética adicional conservada por los transformados. **PARCIAL**:
    RA D5 «Monotonías Schur–Green — sólo con un invariante conjunto distinto conservado por cada
    operación» (correcto en espíritu, sin los falsificadores).
A6. Heredar BASE_073 (G′ > 0, G″ ≤ 0) por cada resto G_p (13, 14, 88). Reapertura: clase que permita
    G_p decreciente, o conservar el residuo R_p/z y controlar cruces. **AUSENTE.**
A7. Hipótesis genérica de potencial (V‴ > 0, M″ < 0, M − uM′ > 0) como suficiente para orden tres; el
    cruce de G_u como consecuencia genérica de 073/075 (85, 86). Reapertura: propiedad específica de Φ o
    comparación cuantitativa del cruce. **AUSENTE.**
A8. Herencia genérica T_f ⇒ T_H de las desigualdades de Turán por el paso Schur (90). Reapertura: dato
    específico de Φ (como en 099). **AUSENTE.**
A9. Carta de eliminación global que divide por Δ; ODE homogénea mónica de orden 2 común a D3(1/w),
    D3(t/w) (20, 21). Reapertura: otra carta, ODE inhomogénea, otro orden o representación. **AUSENTE.**
A10. Orden Loewner K ⪰ K_shift con desplazamiento simultáneo 2; borrar el resto IMS por telescopado
     (31, 32). Reapertura: otros desplazamientos, normalizaciones con hipótesis nuevas, control firmado
     conjunto. **INEXACTO por generalidad**: RA D13 «Orden matricial por desplazamiento K − K_shift»;
     la fuente sólo refuta desplazamiento 2 y declara: «No se descartan normalizaciones diferentes con
     hipótesis nuevas y prueba propia, otros tamaños de desplazamiento no tratados aquí».
A11. Descartar el término positivo 2V de la identidad S = U − V, o una fracción aislada
     θ ≥ 3.3·10^{−8}; productos ρ(log a)ρ(log b) y cruces entre contactos como cota (16, 17, 83).
     Reapertura: comparación que conserve la cancelación U−V. **AUSENTE.**
A12. Reparar el déficit sólo con el contacto 2 (columna k = 1); «2 repara» como patrón universal;
     mejora por cada contacto añadido (26, 37, 38, 47, 73). Reapertura: cota unilateral de varios
     contactos o de su masa conjunta. **AUSENTE.**
A13. Positividad puntual universal de h_N, de K_N = J_N + xh_N, de Ω, de I_* y de las primitivas de H;
     positividad de prefijos de la inversión Möbius; sustituir h_N por su módulo (27, 48, 49, 51, 55, 56).
     Reapertura: promedios celulares, parte negativa ponderada por C_B o −R_N′. **AUSENTE.**
A14. T_m ≥ 0 (aun salvo finitos índices); funcional positivo por componente Erlang (30, 58, 59).
     Reapertura: compensación con los pesos reales P_d en la ventana m ~ √N. **AUSENTE.**
A15. Contracción o dominación absoluta del resto Möbius (también agrupado con Q = Π_{p≤N^{1/8}}p);
     mejorar constantes de cotas absolutas (62). Reapertura: control firmado del complemento.
     **PARCIAL**: RA B2 («toda cota con resto pierde más») lo cubre en general.
A16. Convexidad global del funcional gaussiano G_W; comparación gamma–gaussiana de formas completas sin
     coste (52, 55). Reapertura: compensar la fluctuación firmada junto a la pérdida ♯. **AUSENTE.**
A17. Descartar por separado las colas polar y aritmética por la concentración m ~ √N; omitir el resto
     diagonal de la recurrencia (61). Reapertura: conservarlas conjuntamente antes de estimar colas.
     **PARCIAL**: RA D4 conserva sólo la reapertura «R_L ≥ −ε_L».
A18. Completar la tabla con recurrencias, identidades de filtros, regiones positivas, positividad
     eventual y corte efectivo K(n) (falsificadores W_4 y arcoseno) (42, 44, 76, 97). Reapertura:
     información aritmética concreta. **Presente** en RA D4 («Recurrencia o descenso solos»).
A19. Campañas fila a fila, de átomos o de certificados finitos; extrapolar triples o tamaños certificados
     (5, 35, 36, 41, 44, 57). **Presente** en RA D2 y A4.
A20. Monotonía universal AP a numerador fijo; monotonía ARCH+POLAR sin restricción de tasas;
     monotonía AP bajo movimiento de polos en dimensión arbitraria (37, 98). **AUSENTE** en RA.
A21. Afinar constantes del déficit uniforme puntual directo en dimensión 8 (39). Reapertura: conservar la
     integral firmada (hecho en 014). **PARCIAL** (RA D2 «optimizar umbrales»).
A22. Densidad de colas high-pass, desaparición uniforme de contactos en conos lineales, pesos
     exponenciales uniformes en N, extrapolación absoluta de momentos (42, 75). **PARCIAL** (RA D3).
A23. Contorno STRIP absoluto con altura y constante fijas, uniforme en numeradores, en conos
     j ≥ Cn^p con p < 3 (p < 2 ya con P = 1) (77, 81, 92-94). Reapertura: métodos con cancelación
     firmada, D dependiente de n. **AUSENTE.**
A24. Atribuir convexidad φ^{(k)} ≥ 0 al peso completo de W (82). **AUSENTE.**
A25. Usar la parte afín AFF como base positiva; acotar R por celdas o por Stirling (80). **AUSENTE.**
A26. Turán de los valores completos a_{N,k} sin cota aritmética nueva (76). Reapertura: prueba aritmética
     del determinante (no descartada). **AUSENTE** (RA D18 sólo nombra Pfaffianos por reciprocidad).
A27. Promover identidades (Λ∗1 = log, H_j > 0, logconvexidad de Z_j, MASS, Abel, Rodrigues) a signo;
     signo de diagonales de una familia como signo de combinaciones (9, 50, 82, 99). **PARCIAL** (RA B1,
     B3).
A28. Simetría cosh positiva genérica como argumento de signo para un promedio (30). **Presente** en
     RA B4/C1 («cierres por productos cosh»).
A29. Inferir signo de positividad de cada contribución parcial o de una decisión puntual (57, 79).
     **PARCIAL** (RA B2/B9 genéricos).

## B. Resultados positivos PROVED, con alcance exacto

B1. SCALAR_BRIDGE_017: W ≥ 0 en todos los átomos h_{N,k} ⟺ W ≥ 0 en todo P/(s+u)^M (u > 1), con la
    identidad FORM exacta (polar incluido).
B2. Familias de polos arbitrarios ≥ 63/2 (multiplicidades, sin separación): 6 polos W > ‖f‖²/25 (SIX);
    7 polos > ‖f‖²/500; 8 polos > ‖f‖²/1000; 12 polos > ‖f‖²/10000; 13 polos > ‖f‖²/4000;
    14 polos con transformada nula en 0: > ‖f‖²/1000; V13 confluente > ‖f‖²/4000.
B3. Identidades exactas de transporte: TEL, POLTEL, FULL, ONE (todo n, u > ½); criterio CRIT y cota
    all-pass WT (todo n, condicionales a las constantes).
B4. Potencias arbitrarias a_i > 1 (forma completa): pares (073), triples (080, también 086), cuádruples
    (085). Para la Φ real: V‴ > 0; M″ < 0; M − uM′ > 0; R″ < 0 (086); GLOBAL-R4 y T_R > 0 (089);
    T_h > 0 (099); G_u > 0 (077); pares y triples de K_{G_p} PD ∀p > 0 (089, 099).
B5. Filas completas a u ≥ 63/2: N = 1 (> 4/3), 2 y 3 (> 1/8), 4 (> 1/50), 5 (> 1/25), todo k; filas
    1..8 a todo u ≥ u_0 y 1..17 a u = 63/2 (> 1/40, átomos individuales); DIFF y diferencias 3ª y 4ª.
B6. Regiones: u² ≥ 256N, k ≥ 1 (> 7/10); u ≥ 64√N, todo k (> 2/5); u² ≥ 225N/4, N ≥ 3, k ≥ 1
    (> 1/40); k ≥ 10000N², N ≥ 2, u = 31.5 (> 49/50); N ≥ e^{10^6}, k ≥ 2N²/log log N
    (> (2/5)log N); Q^jP/(s+u)^n con j ≥ K(n) (054) y j ≥ 10^{12}(nq_n)³ (060), todo P (> ‖·‖²).
B7. Átomos decididos: F_{211,1} (3.4·10^{−15} < W/‖f‖² < 4.5·10^{−15}); g_129
    (1.34·10^{−10} < W/‖g‖² < 1.35·10^{−10}).
B8. Signos auxiliares aritméticos: NEG y MEAN (todo N ≥ 2); h_N, K_N > 0 en colas explícitas (020, 026,
    039, 040); banda 041; ABS-TAIL (N ≥ 2^80); SIGNED-FOURIER y WIDE-WINDOW; 2V > 1/243 (g_129);
    peine completo de la columna k = 1 positivo para N ≤ 211; oscilación exacta de autocorrelaciones (065).
B9. Lemas analíticos: PSI Re ψ(¼+it) ≥ log|t| − 9/(8t²); CENTERED; HEIGHT; cota U_N(u); cotas de
    ψ′, ψ″; Abel P_d con TAIL/SMALL/LARGE/WINDOW/BUDGET; R12 de un polo (049); E2 en V13 con G(0) = 0.
B10. Documental (no reproducido en estas rondas): λ_A(T) ≥ 2·10^{−26} para 0 < T ≤ 1.035 (ROUND_026_A).

## C. Obligaciones OPEN (enunciado preciso y qué se intentó)

C1. W[h_{N,k}] ≥ 0 para todo N ≥ 6 (a u = 63/2: N ≥ 18) y k < 10000N² (ó k < 2N²/log log N). Intentado:
    filas, regiones, recurrencias, descenso, mezclas; falsificadores W_4 y arcoseno muestran que la
    estructura no basta.
C2. W ≥ 0 en los bloques confluentes V_n de tamaño n ≥ 14, o en Q^jV_n para j < J(n). Intentado:
    transporte MULTI/FULLTEL con LDL por bloque; corte efectivo; norma ponderada uniforme no obtenida.
C3. K = [K(a_i,a_j)] PSD para cinco o más potencias a_i > 1. Intentado: recursión de Schur sobre el resto
    G_p (pares y triples probados), jerarquía de Pfaffianos 083, densidades lineales (R4 probado; S4 sin
    tratar); el siguiente nivel «requiere un input nuevo».
C4. (SIGNED) 2∫h_N^+(−B) − 2∫h_N^−(−B) ≥ −Arch_♯[g_N]/c_0 para todo N; equivalente a controlar el
    interior renormalizado R_N^inside de 1 a e^T frente a ARCH_♯ + 2γ − (2κ−γ)J_N(1). Intentado: inverso
    completo, colas, banda, agrupación Möbius, Fourier firmado; los márgenes son del orden 10^{−10}.
C5. Promedio de I_*(e^t) contra −R_N′(t) en t ≥ T_N no negativo (031). Intentado: bloques alternos.
C6. A_N = Σ_m P_d(m)t_m ≥ 0 controlando la ventana m ~ √N (035). Intentado: T_m ≥ 0 (refutado), BUDGET.
C7. Δ²[a^n(I_n − J_n)] ≥ 0 para todo n ≥ 4 (cadena Tate 009).
C8. G_W(v) ≥ 0 para todo v > 0 (funcional gaussiano; daría toda la fila k = 0).
C9. B_N ≤ 2NA_N para todo N (propagaría A_N ≥ 0), o B_N ≥ A_N con liminf A_N ≥ 0.
C10. E_{ν+}D − E_{ν−}D ≥ 0 por intervalo nodal de w (065), con bordes [E_1w′].
C11. Comparación conjunta U − V (Selberg) uniforme en N.
C12. Cota unilateral de la masa conjunta de contactos q ≥ 3 frente a ARCH + POLAR en la columna k = 1.
C13. Jet local del paso Schur |u(cd − ud² + uce)| ≤ c² − u²d² y su conservación (para la familia
     aritmética los pares y triples ya están cubiertos; el nivel siguiente sigue abierto).
C14. L55-B: representación positiva exacta del dato arquimediano desplazado en todo el portador
     primitivo, con discrepancia aritmética controlada.

## D. Objetos o ideas mencionados como no iniciados o no examinados

D1. Correcciones L55-B no compactas, no pares, o por medidas singulares/distribuciones exteriores (entrada 69).
D2. Otros tamaños de desplazamiento y transportes restringidos distintos de K − K_shift(2) (entrada 32).
D3. Otras cartas, gauges, órdenes o ecuaciones inhomogéneas para la ODE de K (entrada 20).
D4. Lado S (cuatro densidades) y transporte S4 global (entradas 90, 102); jerarquía superior de densidades (entrada 104).
D5. Comparación de inclinaciones polinómicas superiores (cinco tilts) de 103_43 (entradas 84, 100).
D6. Contorno uniforme independiente de n con separación par/impar de P(iτ) (entrada 77, en estudio).
D7. Ruta FULL_TRANSFER_PLAN050 conservando el contacto 3: «no fue necesario ejecutar» (entrada 72).
D8. Norma ponderada uniforme en j para Q^jV_n: «no se declara una imposibilidad» (entrada 73).
D9. Determinante de Turán con prueba aritmética (entrada 76): «no descarta una futura prueba».
D10. Estimaciones que exploten cancelación y conos de signo; escala cuadrática espectral (entrada 42): OPEN,
     no refutadas.
D11. Relaciones desiguales entre franjas y otras subfamilias (entrada 2).
D12. Comparación de diferencias en N de J, K y ARCH_♯ (entrada 80).
D13. Hipótesis uniforme −o(1) de la banda pendiente de 046 (entradas 70, 95, 96): mencionada, no probada.
D14. Sustituir el nodo auxiliar 0 por un nodo positivo libre (entrada 15): «sin otra prueba».
D15. Diagnóstico numérico autorizado en el átomo 211 para cotas separadas de componentes (entrada 46): no
     incorporado; luego superado por la decisión 032.

## E. Cobertura

Archivos en el rango (`ls *.md | sort`, de POWER_REDUCTION_AUDIT_044.md a
POWER_THETA_DENSITY_ORIGIN_087.md inclusive): 106. Archivos leídos íntegramente: 106 (≈ 449 KB). No
quedó ningún archivo ni tramo sin leer. Las fuentes citadas por los POWER_STATE_* que caen fuera del
rango (por ejemplo POWER_ARITHMETIC_BLOCK_007, POWER_HIGHPASS_015, POWER_CONTACT_DECISION_032,
POWER_GAMMA_129_DECISION_061, POWER_THETA_REMAINDER_077) no se leyeron aquí; sus enunciados se toman de
los resúmenes de estado y de las auditorías del rango.
