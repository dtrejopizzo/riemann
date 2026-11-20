# Anexo 211 — Archivos AUDIT_001 … POWER_DEFICIT_LIMIT_013 (61 archivos)

Lectura completa, en orden alfabético (`ls *.md | sort`), de los 61 archivos de
`../phase-211-sign-sandbox/` comprendidos entre `AUDIT_001.md` y `POWER_DEFICIT_LIMIT_013.md`.
Notación de `STATEMENT_001.md` y `POWER_CONE_001.md`: (★) es λ_A(T) ≥ 0 para todo T; W es la forma
completa (ARCH + peine + polar); AP = ARCH + POLAR; u = 63/2 es la tasa fija de la escalera; V_n(u)
es el bloque confluente {P(s)/(s+u)^n}; f_{N,k} es el átomo de transformada s^k/(s+u)^{N+k}.
Las etiquetas se copian tal como figuran en cada archivo. Donde una fuente usa una equivalencia
con otro enunciado, aquí se escribe «(★)».

## Entradas por archivo

1. **AUDIT_001.md** — Relectura de las fases 0–99 frente a la forma de ventana. Objeto: todo el
   material previo (realizaciones de Kreĭn, triples prolatos, cadena Fredholm/Feshbach) indexado por
   el conjunto de ceros. Resultado: «Hits: (honest) empty»; «Mislabels: none»; sólo una laguna
   documental (celda «why» vacía de P60-5 en el índice 03). Ningún resto firmado nuevo; ningún
   resultado positivo reutilizable. Analogías estructurales (división por profundidad, cálculo de
   símbolo de la fase 45, obstrucción de paridad) declaradas no-rutas.

2. **AUDIT_002.md** — Relectura de las fases 100–160. Resultado: sin hits fuertes ni mislabels.
   Hit débil 1: la identidad 𝔊_T = S^{Sch}_T + J de la memoria M4 (fase 160) nunca se cotejó con
   thm:coer-schur/(L2) (¿afina el término ‖K‖ no controlado?). Hit 2 (administrativo): la ruta N
   (rigidez de Carathéodory–Fejér en el estado de primer contacto de ventana finita, sin límite)
   quedó a medio argumento; no está cerrada en el índice; reapertura con razón escrita de por qué la
   ventana finita evita el fallo «muere en el límite». Positivo citado: lema de cono de contacto de
   M2 (PROVED, convexidad, sin signo).

3. **AUDIT_003.md** — Relectura de las fases 161–210. Resultado: «None found» (hits), «None»
   (mislabels vivos). Stopped-not-dead: fase 209 bloqueada por falta de ingrediente (no NO-GO);
   residuo «bordes de capa κ_{T+log n}» de la fase 202 «sin propuesta»; Lema RF.1 de la fase 205
   (n₊(Φ_N) ≥ 1.95T − 2, PROVED-elemental, no integrado); escalares candidatos de la fase 210
   pendientes. Positivo: identidad SPD −R_α de la fase 209 (sobrevive a borrados, por eso no
   transfiere). Corrección ya reparada: techo de λ_A es exponencial simple, no doble.

4. **BRIEF_CONSTRUCTOR.md** — Reglas de las memorias de la fase. Objeto: protocolo (sandbox, chequeo
   de corpus, etiquetas, test de falsificadores (a) cΛ, (b) a_P, (c) Beurling, (d) modificación finita
   de pesos). Sin resultado matemático. Cierre obligatorio «Result / What was proved / What failed /
   Next step».

5. **CORRECTION_RESIDUE_BALANCE_031.md** — Corrección de L2_BUILD_031 (fase 188). Objeto: pairing de
   la componente Ramanujan de módulo 2 sobre un bloque equilibrado (B_Q), M=Q=2, s=(1,1), perfil con
   2T_0 < log(3/2), interpolante suave S explícito. Resultado PROVED: P_2 = v_2/2 = log2/√2 > 0, luego
   la omisión de componentes pequeñas en §3 de 031 es falsa (falsificador explícito). §5 PROVED
   (alcance restringido): en soporte rough R_Q la anulación universal de la componente 2 sólo vale para
   s = 0. El Teorema E de 031 queda intacto; no se afirma colapso en soporte mixto.

6. **CORRECTION_RESIDUE_BALANCE_AUDIT_031.md** — Auditoría de la anterior. APROBADO: refuta la
   omisión de §3/§4 de 031 para la interpolación declarada; la transferencia de balance por
   multiplicación no coprima falla. Aprobada la reparación rough (sólo R_Q, todos los perfiles e
   interpolantes). Sin nueva negatividad de W.

7. **DOSSIER_001.md** — Ingeniería inversa del signo (Papers 43–48). Objeto: definiciones,
   formas reducidas (L2), (N), (S), (L), nodo, inercia par; herramientas PROVED; tabla de barreras;
   cláusulas de Problem (R) y prop:spec. Resultados propios §6 (PROVED, elementales): (a) el sándwich
   de thm:coer-schur y lem:wh-schurabs(ii) se invierte si λ_S < 0 (correcto: λ_S ≤ λ_A ≤ λ_S/(1+‖Ke_S‖²));
   (b) falta normalizar F_0; (c) «exactamente un autovalor negativo para todo T» falso para T
   pequeño (vale ≤1, o =1 para T ≥ 0.12); (d) la identidad de semirrecta no es genérica en el peine
   (ARGUED); (e) cuadrados aritméticos en (½log2, ½log3) ⟺ λ^{∞,P}_min(T) ≥ v_2 = √2 log2 (un solo
   número; debería cerrarse); (f) T ↦ n_−(A_ev(T)) no decreciente; (g) (L) a ventana fija es trivial,
   sólo cuenta la uniformidad; (h) S_η (η↓0) es reducción exacta menor que (L2), propuesta como (L2′).
   OPEN: si el conjunto negativo de Nyquist crece como O(T) o e^{A_T}.

8. **LEDGER.md** — Libro de candidatos C1–C51 + F1. Etiquetas por fila (NO-GO, PIVOT, PROVED piece,
   NUMERICAL, NOT STARTED). Positivos reutilizables: Thm 1 de C8 (max_c λ_A(T;cΛ) = Θ_T, (★) ⟺
   Θ_T ≥ 0 ∧ 1 ∈ J_T); λ_max(Π_T)/A_T ∈ [¼,½] (C14); cota de clúster exp(2e^T(1+o(1))) (C15);
   coercividad de primera celda (1/2π)∫m|F̂|² ≥ 0.069611‖F‖² sobre ∫Fe^{−y/2}=0 (C37, certificada);
   λ_A(1) ≥ 10⁻²³, λ_A(1.035) ≥ 2·10⁻²⁶ (C50, asistido); falsificadores certificados a_3, Beurling,
   1.1Λ (F1). Restos abiertos: (SL_T), (EB_C), (HR)/(HR_g), (U) λ_max(A_τ) ≤ m − κ, signo de ∂_tQ.
   NOT STARTED: C4, C6, C7.

9. **LITERATURE_001.md** — Barrido bibliográfico (sólo ítems nuevos). Resultado: nada supera el
   frontera citado ½log15; dos ítems nuevos (simplicidad ⟹ paridad del estado fundamental de la forma
   truncada; certificado de simplicidad/paridad hasta semiancho 1.19), ambos de valor bajo, sin signo.
   Categorías 2–5 (cotas firmadas de Chebyshev suavizado, acoplamiento de Λ con la ecuación funcional
   fuera de ζ(½+it), Bochner sobre ℚ^×_{>0}, extensión de Kreĭn con átomos primos, espacios de de
   Branges) «nothing new». Hueco señalado: extensión de Kreĭn con átomos en log p, nunca intentada.

10. **OBJECT_SPEC_001.md** — Especificación R1–R5 del objeto (ronda 5 en adelante). R1 dim E_T → ∞
    (ningún subespacio finito libre de Λ lleva el signo: ROUND_004_A Prop. B); R2 entradas no
    lineales en v_n, fallo para cΛ, a_P, modificaciones finitas, Beurling; R3 reducción exacta o
    captura al margen; R4 entrada conjunta arquimediana + Euler; familia «primero el peine» escapa al
    conteo de arena N*(T) ≥ exp(4e^T(1+o(1))); R5 falsificadores. Sin resultado propio.

11. **POWER_ARCH_CELL_026.md** — Déficit sharp y kernel conjunto. Objeto: N = 129, u = 63/2,
    W[g_N]/norm² = ∫ K_N Ω, Ω(t) = d_*D(t) + 2C_B(t) + 2∫k(x)[D(t) − x^{3/2}E_x(t)]dx. PROVED:
    ARCH_sharp[g_129]/norm² < −81/100, luego la garantía ERR_129 < −33/50 deja déficit > 0.15 (no es
    W<0); identidad JOINT con Fubini absoluto; falsificador exacto Ω(3/2) < −1/10 (lema «Ω ≥ 0
    puntual» FALSO). Resto: cota unilateral de ∫K_NΩ que use la restricción gamma real de K_N.

12. **POWER_ARCH_CELL_AUDIT_026.md** — Auditoría. ARCH_CELL026 y UNIFORM_CUTOFF026 APROBADOS.
    Positivo reutilizable (de UNIFORM_CUTOFF026): dos cortes uniformes (Jensen d ≥ 2 con
    t_J = d(d+220)/(330d+6300); Riccati 0 < q′ < M_d) que prueban K > 0 en toda la cola declarada para
    2 ≤ N ≤ 129. Ω(3/2) < 0 y ARCH+0.66 < 0 no son W < 0.

13. **POWER_ARCH_EXACT_032.md** — Fórmula estable de ARCH. PROVED: para todo N,
    A_{N,0} = a(u) − Σ_{j=1}^{d} b_j S_{j+1}(x) (todos los restados positivos) y
    A_{N,1} = a + (u/2)S_2 − Σ(j+1)b_j[S_{j+1} − (u/2)S_{j+2}] (corchetes > 0); resto Euler–Maclaurin
    absoluto (B_16) sin hipótesis de término siguiente. Certificado del átomo N=211, k=1: ARCH en un
    intervalo de anchura < 10⁻¹⁸. Reutilizable: la fórmula (A0)/(A1) para todo N y u.

14. **POWER_ARCH_TRIPLE_004.md** — Cota de densidad en dimensión 3. PROVED: |ĥ(τ)|²/(2π‖h‖²) ≤
    Σ u_j/[π(u_j²+τ²)] (base de Malmquist) y la cota arch ≥ (2n/π)∫_0^R m·a/(a²+τ²). NUMERICAL: a = 31.5,
    n = 3 da ≈ −0.0506, insuficiente. OPEN: mejorar el cap escalar en ≥ 0.051 o probar que la menor
    energía arquimediana crece al separar tasas (resuelto después por CONFLUENT_004).

15. **POWER_ARITHMETIC_BLOCK_007.md** — Bloque Laguerre completo de dimensión 12. PROVED (certificado
    racional): W[h] > 10⁻⁴‖h‖² para todo h ∈ V12 = span{√63 e^{−uy}L_j(63y), j ≤ 11}, u = 63/2, con
    todos los contactos. Usa decisivamente el contacto 2 (AP+contacto2 > (1/1250 − 10⁻⁸)I; cola n ≥ 3
    en norma < 3/5000). OPEN: dimensión ≥ 13 o principio uniforme.

16. **POWER_ARITHMETIC_DIFFERENCES_019.md** — Frontera firmada del peine. PROVED: para todo N ≥ 1,
    c_{f_{N,1}}(t) tiene exactamente una raíz simple χ_N en ut, con √(2N−3) < χ_N < (1+√(8N−11))/2;
    corolario P_{N,1}(u) > 0 para 1 ≤ N ≤ 211, u ≥ 63/2 (todo contacto favorable); P_{N,0} < 0 siempre.
    Falsificador: (−Δ)^r P_{1,0} < 0, refuta «Λ ≥ 0 hace no negativas las diferencias del peine en la
    fila 1». OPEN: desigualdad que conserve la cancelación ARCH/peine/polar a órdenes variables.

17. **POWER_ARITHMETIC_WITNESS_006.md** — Test explícito. PROVED: con v racional de 12 coordenadas en
    V12, −2/125 < AP/N < −1/100, todo contacto primo-potencia aporta > 0 (Q(x+40) con coeficientes
    negativos) y el contacto 2 solo aporta > 1/25; W > N/50. §4: retirar sólo el contacto 2 da
    W < −N/125. Contraejemplo a «AP ≥ 0 en V12»; no a W.

18. **POWER_AUDIT_002.md** — Auditoría de polarización y puente. PROVED: W(h_u,h_v) =
    [L(a)+L(b)]/(a+b−1); falsificador H = 3+cosh (det < 0) refuta «representación cosh positiva ⟹
    signo de mezclas»; puente H_η (densidad de exp(−(31.5+k)y)); puente fraccionario a todo PW_N C²;
    inversión finita por Möbius; obligación suficiente explícita: K^{(m)}_{ij} = [L(32+i)+L(32+j)]/(63+i+j)
    ⪰ 0 para todo m. Aprobados THREE002 (orden 3 en [u,3u], u ≥ 2³⁰) y su extensión a todo n con
    u ≥ 2^{40n}; la unión de esos espacios NO es densa (falsificador explícito). OPEN: signo de órdenes ≥ 3
    de la escalera fija.

19. **POWER_AUDIT_004.md** — Movimiento de polos. PROVED: con numerador fijo, el cociente arquimediano no
    disminuye al aumentar cualquier polo (covarianza de m y R crecientes); cota ponderada 1302 en
    dimensión ≤ 3; peine < 0.002‖f‖², polar > −0.042‖f‖² para u ≥ 63/2; con CONFLUENT_004: W >
    (7/125)‖f‖² para toda terna de potencias con exponentes ≥ 32. No se extrapola a orden arbitrario
    (B_n = (25^n−1)/12 no uniforme).

20. **POWER_AUDIT_005.md** — Movimiento con polar. PROVED: identidad exacta (AP)
    E_v − E_u = [Cov_μ(m,R) + (r_0 − E_μ[R])p_u]/E_μ[R]; falsificador exacto E(2) − E(1) = 4/5 − π < 0
    (dimensión 1, polos 1→2) refuta el transporte de AP para todos los polos > 1/2. OPEN: comparación
    Cov_μ(m,R) ≥ (E_μ[R] − r_0)p_u en orden 4 con tasas ≥ 31.5. Aprobados FOUR005 (W > (1/5) en V4),
    cuártica D4 > 0.075N² (transporte local de 4 polos, sin radio) y teorema escalar n=1, u ≥ 8.

21. **POWER_AUDIT_006.md** — Auditoría del test 006. PROVED y reejecutado: −2/125 < AP/N < −1/100,
    autocorrelación recalculada independientemente, W/N > 3/125; ampliación aprobada: sin contacto 2,
    W/N < −1/125. Alcance: un test explícito, no el bloque.

22. **POWER_AUDIT_007.md** — Falsificador de transporte uniforme en dimensión alta. PROVED:
    0 ≤ τm′(τ) < 4 globalmente; P_n = 4^n/[u·binom(2n−2,n−1)](1−1/(4u²))^{−n}; en u = 63/2, n = 131072,
    uE′_diag < −140/31: el cociente AP de un numerador fijo disminuye al mover un polo. Clase falsada:
    monotonía del cociente AP para todos los numeradores y órdenes. No refuta monotonía de λ_min ni
    transporte que preserve sólo el signo.

23. **POWER_AUDIT_008.md** — Auditoría del patrón contrario de contactos bajos. PROVED: f = (D²−¼)g,
    g = y^{n−1}e^{−uy}, n = 131072: ambos momentos nulos, AP/‖f‖² < −383/100, todos los contactos
    q ≤ 1024 negativos; obligación necesaria: la cola q > 1024 tendría que superar
    383/100 + Σ_{q≤1024}Λ(q)q^{−1/2}. El patrón «reparación por contactos bajos» (006) no es universal.
    No prueba W < 0.

24. **POWER_BALANCE_AUDIT_020.md** — Auditoría de SIGNED_BALANCE020 e INVERSE_KERNEL020. APROBADOS:
    FAIL2 en N=211, k=1 (ARCH/norma < −0.74, 0 < P_2 < 0.075, polar < 0 ⟹ forma con sólo el contacto 2
    < −0.66); kernel Möbius completo h ≥ H/4 > 0 en log x ≥ (N−1)/30 para todo N, y global para N = 2.
    OPEN: cota del emparejamiento interior en [1, exp((N−1)/30)] y magnitud del resto del peine.

25. **POWER_BALANCE_AUDIT_033.md** — Auditoría de PRIME_BALANCE033 y COEFFICIENT_BALANCE033.
    APROBADOS: decaimiento w(mq) ≤ m^{−2}w(q) para q ≥ 5; telescopía con brackets de signo alterno
    (ρ < 2/3); A(w) ≥ 3600L(w)/5989; mezcla finita Erlang y Abel; E_22 ∈ (−0.01, −0.006) en un perfil
    no definido positivo. OPEN: signo del lower del comparador; T_m ≥ 0. Advierte que márgenes de
    10⁻¹⁵ exigen conservar cancelación, no presupuestos por componentes.

26. **POWER_BLOCK_AUDIT_007.md** — Auditoría del bloque V12. PROVED: W|V12 > 10⁻⁴ I, con revisión de
    factores de contacto, Euler–Maclaurin, LDL exacto y cola completa (Λ ≤ log n para todo n ≥ 3). No
    se deduce positividad al añadir modos ni para otras 12 tasas.

27. **POWER_BOUNDARY_AUDIT_035.md** — Auditoría de BOUNDARY_BALANCE035 y SIGNED_TRANSFORM035.
    APROBADOS: terminal W[f_{17,0}] > 0.041 n_17; descenso convexo; filas 1..17, todo k ≥ 0, u = 63/2,
    W > ‖f‖²/40. SIGNED_TRANSFORM035: A_N es esperanza de t_m = T_m/h_m firmado bajo la ley P_d; BUDGET
    O(N⁻²) para prefijos finitos. OPEN: control aritmético de la ventana móvil; terminal ≥ 18.

28. **POWER_BOUNDARY_BALANCE_035.md** — Dato terminal y descenso. PROVED: W[f_{17,0}]/n_17 > 1/25
    (ARCH_17 > −0.868, polar_17 > 0.911, peine adverso < 1/500 por cota de pendiente q(log2) > 15);
    con a_{N,0} = a_{N,1} + u²a_{N+1,0} (combinación convexa normalizada) y la columna k=1 de 034:
    W[f_{N,k}] > ‖f‖²/40 para 1 ≤ N ≤ 17, todo k ≥ 0, u = 63/2. Patrón reutilizable: columna k=1
    positiva + un terminal k=0 positivo ⟹ descenso. OPEN: M ≥ 18, tasas variables, mezclas.

29. **POWER_BOUNDARY_WEDGE_029.md** — Región uniforme. PROVED: para todos N ≥ 1, k ≥ 0, u ≥ 64√N,
    W[f] > (2/5)‖f‖² (pesos bilaterales ±η que cancelan el desplazamiento; ARCH > 9/20; peine < 1/5000;
    polar par ≥ 0, impar > −1/1000). Alcance: el wedge no basta para el puente de tasa fija; las mezclas
    positivas de sus densidades no aproximan átomos de tasa fija (SCALE_BRIDGE_LIMIT_029).

30. **POWER_BRIDGE_002.md** — Puente de potencias a PW_N. PROVED: espacio B (g = e^{5y/4}ρ(e^y) ∈
    H^{1/4}); Q continua en B (B1/B2); PW_N ⊂ B; densidad de X^{−(32+n)}; realización finita por Möbius
    de todo test compacto. Consecuencia CONDITIONAL: K^{(m)} ⪰ 0 ∀m ⟹ W ≥ 0 en todo test ⟹ (★).
    Polarización verificada (P_ab = R_ab). OPEN: el signo de la escalera.

31. **POWER_CELL_AUDIT_024.md** — Auditoría de CELL_BALANCE024 y CELL_TEST024. APROBADOS: LOCAL/
    BUFFER, OUT-CELL (toda celda con n−1 ≥ exp((N−1)/30) favorable), interfaz Möbius 31Q − Q′ = P;
    primera celda N=129: 31/100 < ∫_1²K C_B < 8/25, 33/100 < S(2) < 1/3. K_129(1) < 0 compatible con
    medias positivas. OPEN: celdas interiores y déficit ARCH_sharp.

32. **POWER_CELL_BALANCE_024.md** — Presupuesto de K negativo. PROVED: S_N(n) = b_nJ_N(n) +
    (H_{n−1}/2)∫_{n−1}^{n}[1 − (n−1)²/t²]K_N; BUFFER S_N(n) ≥ b_nJ_N(n) − [H_{n−1}/(2n)]M_N(n);
    criterio integrado J ≥ 0 y M ≤ 4aJ ⟹ S ≥ 0 (a = ¾ − log2); OUT-CELL para todo N. Falta:
    Σ S_N(n) ≥ −ARCH_sharp/[2C_N(0)]. §7: con LOGCONCAVITY025, K_129 > 0 en x ≥ 2, ERR_129 < −33/50.

33. **POWER_CELL_TEST_024.md** — Test de primera celda. PROVED (certificado racional, cola Möbius
    completa < 10⁻¹⁰): para N = 129, 31/100 < ∫_1²K C_B < 8/25, 33/100 < S(2) < 1/3,
    1/2 < ∫_1²K x⁻² < 3/5. Sin signo de ERR total ni de W.

34. **POWER_CENTERED_CUTOFF_049.md** — Corte efectivo j = 14. PROVED: para todo polinomio P de grado
    ≤ 11 y todo j ≥ 14, E_{μ_j}[(1−q)/q] < 49/20 (Bernstein ponderado probado por autopolinomios de
    Gegenbauer + integración por partes); por tanto E_G[τ⁻²] < 1/405 y ARCH[Q^jF_0] > (859/800)‖·‖²
    para toda F_0 ∈ V12. OPEN: índices j < 14, contacto 2, polar, cola de primos; signo global.

35. **POWER_CENTERED_MOMENT_053.md** — Momento matricial exacto. PROVED (13 pivotes LDL): (6/5)T_96 −
    T_95 ≻ 0 con (T_j)_{ab} = 4^{−j}binom(2j, j+a−b); monotonía r_{j+1} ≤ r_j por covarianza; para todo
    j ≥ 96 y F ∈ V13: ARCH > (12/5)‖·‖², E23 = AP + contactos 2,3 > (1/10)‖·‖². OPEN: segmento
    j = 1..95 y contactos n ≥ 4.

36. **POWER_CENTERED_MOMENT_AUDIT_053.md** — Auditoría. APROBADO: Gram binomial, monotonía por
    covarianza para cada numerador, constantes; fija el segmento pendiente j = 1..95 y la cola n ≥ 4.

37. **POWER_COEFFICIENT_BALANCE_033.md** — Mezcla Erlang y Abel. PROVED: MIX ρ_N = Σ w_{Nj}S_j con
    w_{Nj} ≥ 0, Σ = 1; W[g_N]/norm² = Σ w_{Nj}E_j; ERLANG-FAIL −1/100 < E_22 < −3/500 (perfil no
    PD: transformada −1/(2048u)); WEIGHT −11/(50d) < w_{N,22}E_22 < 0; ABEL W = Σ(v_m − v_{m+1})T_m,
    T_m = Σ_{j≤m} jE_j. La premisa «T_m ≥ 0 ∀m» FALSIFIED en 034. Reapertura: cambiar la agrupación
    o introducir una compensación real.

38. **POWER_COMMON_TRANSFER_010.md** — Criterio común de transporte. PROVED: si
    η = b − c − DK_n − Cn/(4u²) > 0 (K_n = [(1+X/u²)^n − 1]/X), entonces AP[f] > c‖f‖² para todos los
    polos ≥ u; cotas ponderadas B_Y (Young), B_F = (1−α)⁻¹Σ r_F^{2j} (Fourier), B_T (traza máxima en la
    confluencia, monótona en cada polo); paso a W con L = 2√B Σ Λ(q)q^{−σ−1/2}. No signo a dimensión
    arbitraria.

39. **POWER_COMPARISON_AUDIT_034.md** — Auditoría de DIVISOR_COMPARISON034 y WEIGHTED_COEFFICIENT034.
    APROBADOS: W > ‖f‖²/40 para k = 1 y k ≥ 2 en la región N ≥ 3, u ≥ 31.5, u² ≥ 225N/4; cobertura
    combinada: filas 1..12 a u = 31.5, filas 1..8 para todo u ≥ 31.5. PROVED: T_m toma valores
    positivos y negativos en índices arbitrariamente grandes (Pringsheim + paridad), refuta «T_m ≥ 0»
    incluso eventualmente; no refuta las combinaciones Abel ni W.

40. **POWER_CONE_001.md** — Cono de potencias. PROVED: Q[Σ c_iX^{−a_i}] = Σ d_id_j[L(a_i)+L(a_j)]/
    (a_i+a_j−1); L(a) > 0 para a > 1; criterio de dos generadores |u d/du log L| ≤ 1; L − uL′ > 0 para
    a ≥ 32 ⟹ Q ≥ 0 en todo plano de dos potencias con exponentes ≥ 32. Falsificador: H = 3+cosh (lema
    theta genérico falso). OPEN: 1 < a < 32 y determinantes de orden 3.

41. **POWER_CONFLUENT_004.md** — Matriz arquimediana confluente de orden 3. PROVED (racional): con
    d = ψ(16) − log π, b = (63/4)ψ′(16), c = b + (3969/16)ψ″(16), M ≥ (d − √2 b − |c|)I > (1/10)I en
    span{e^{−31.5y}, ye^{−31.5y}, y²e^{−31.5y}}. Peine y polar aparte (AUDIT_004).

42. **POWER_CONFLUENT_BRIDGE_014.md** — Puente con una sola tasa. PROVED: span{y^k e^{−ay}} denso en
    H¹(0,∞); si para una sola u todos los bloques V_N(u) son W-no negativos, entonces (★) (CONDITIONAL).
    §6: aproximación fuerte en H_η con tasas u_N ⟺ N/u_N → ∞ (MOV-DIST exacto); falsificador
    trasladado: con u_N = N^{3/4} el contacto 2 no se suprime como O(N/u_N²). §7 MOV-TAIL: corte
    Q_cut = ⌈exp(40N/u)⌉ con error < e^{−N}. §8 MOV-NEC: corte con log Q ≤ (2−δ)N/u da W_{≤Q} → −∞.
    §9 PRIM-CUT: primitivo con W_{≤Q} < −3 si log Q ≤ 2⁻¹²N/u. OPEN: W_{≤Q_cut} ≥ −ε_N‖f‖² en V_N(N^{3/4}).

43. **POWER_CONFLUENT_BRIDGE_REVIEW_014.md** — Revisión breve. APROBADO: convención compleja,
    integración por partes (h(0)=0), norma fuerte, paso al signo sin margen uniforme, confluencia
    exterior con diagonal (−1)^kζ(a). Suficiencia sólo para bloques completos con todos sus cruces.

44. **POWER_CONFLUENT_FOUR_005.md** — Cuatro polos confluentes. PROVED: AP > (49/200)I y |peine| <
    (13/1000)I ⟹ W > (1/5)‖h‖² en V4(31.5). Falsificador: Arch[(1,−1,1,−1)]/‖v‖² < −1/10 refuta «ARCH
    positiva para cualquier número de polos ≥ 31.5 con resto pequeño». No cuatro tasas arbitrarias.

45. **POWER_CONFLUENT_THIRTEEN_052.md** — V13 confluente. PROVED: W[f] > ‖f‖²/4000 en V13(63/2) con
    toda la aritmética (E2 > 3/10⁴, E23 > 7/25000, cola n ≥ 4 < 10⁻⁵); pivote complementario a ZERO13:
    0.0003 < σ(W) < 0.0005. En la dirección del Schur, AP ≈ +0.0184 y el contacto 2 ≈ −0.0180 (adverso),
    el 3 también adverso. No trece polos arbitrarios.

46. **POWER_CONFLUENT_THIRTEEN_AUDIT_052.md** — Auditoría. APROBADO, cinco PASS; lectura correcta de
    componentes en vector fijo (no cocientes de Rayleigh) y de la cola n ≥ 4.

47. **POWER_CONTACT_AUDIT_032.md** — Auditoría de ARCH_EXACT032 y CONTACT_DECISION032. APROBADOS:
    3.4·10⁻¹⁵ < W[f_{211,1}]/‖f‖² < 4.5·10⁻¹⁵. El parcial negativo hasta 300 de 021 se debía a
    contactos favorables omitidos. Un único átomo.

48. **POWER_CONTACT_BALANCE_021.md** — Escala de cancelación en un átomo. PROVED: FAIL234
    (AP + P_2 + P_3 + P_4 < −0.21) y cola 0 < Σ_{q>300}P_q < 5·10⁻¹³. NUMERICAL: parcial hasta 300
    ≈ −6.08·10⁻¹⁴. Sin signo de W; resuelto en 032. Lección: separar componentes por cotas gruesas no
    resuelve el balance.

49. **POWER_CONTACT_BALANCE_AUDIT_021.md** — Auditoría. APROBADO con separación entre pruebas
    exactas (FAIL234, cola) y diagnóstico NUMERICAL.

50. **POWER_CONTACT_DECISION_032.md** — Decisión del átomo F(s) = s/(s+63/2)^{212}. PROVED:
    3.4·10⁻¹⁵ < W/‖f‖² < 4.5·10⁻¹⁵ (ARCH < 10⁻¹⁸ de anchura, polar exacto, contactos ≤ 512, cola
    < 1.1·10⁻¹⁵ de signo favorable). No fila, vecindario ni ventana.

51. **POWER_CONTACT_FLOOR_045.md** — Corte 240 al entrar 5. PROVED (alcance específico): para
    ½log5 < T ≤ ½log7, A_T > 17/4 y m(240) < 15/4, luego s_∞ ≤ m(τ_N) − A_T < −1/2 (FIXED-FLOOR-FAIL):
    el certificado heredado de corte 240 y floor de masa total no puede mantenerse. Escribe los cruces
    lineal, cuadrático y polar que una nueva representación debe conservar. Cambiar corte/floor o
    repetir certificaciones ya está registrado (008/026).

52. **POWER_CONTACT_OSCILLATION_065.md** — Oscilación exacta. PROVED: para todo N ≥ 1, k ≥ 1,
    K_{N,k} = c_{f_{N,k}} tiene exactamente k raíces positivas simples, alterna signo, última raíz
    χ < 4k(N+k−1); por tanto, para u log q ≥ 4k(N+k−1), cada término del peine tiene signo (−1)^{k+1}
    (cola favorable k impar, adversa k par). Sin magnitud ni signo de W.

53. **POWER_CONTACT_OSCILLATION_AUDIT_065.md** — Auditoría. APROBADO íntegro (perfil, momentos
    nulos, lema de convolución unilateral, cota de última raíz, signo de cola).

54. **POWER_CORPUS_OPPORTUNITY_AUDIT.md** — Revisión estratégica. Tabla de decisiones: no reconstruir
    puentes; no más dimensiones por filtros; no inferir densidad de una unión positiva (exige
    liminf r(n)²/n = 0 más otra topología y cruces); no recurrencia sola (falta cota firmada del resto);
    monotonías Schur/Green sólo con invariante conjunto nuevo; no extender la torre MIXED4; representación
    Stieltjes/anti-Löwner = objetivo legítimo sin candidata; no «hacerlo global/no lineal»; completitud
    parcial sólo preliminar. Calor/theta/Poisson: reabrir sólo con desigualdad conjunta concreta.
    Correcciones de lectura (O-151.4, 06R4, TB3-neg(ii), REF-D ≠ exclusión).

55. **POWER_CRITICAL_AUDIT_040.md** — Auditoría. APROBADOS núcleo y CONSTANT-CUTOFF. Signos opuestos
    reales del inverso completo cerca del centro; no W.

56. **POWER_CRITICAL_BALANCE_040.md** — Inverso completo cerca del centro. PROVED: 1/ζ(1+z) =
    z − γz² + R_3, |R_3| ≤ 9|z|³ (|z| ≤ 1/8, Re z ≥ 0); expansión de R_c con resto absoluto;
    CURVATURE −2q′/t < q″ < 0; CENTRAL-SIGNS h_N/H_N < −1/N, K_N/G_N > 1/N en v = ½ + N⁻²,
    N ≥ 2⁸⁰; CONSTANT-CUTOFF h_N(e^t), K_N(e^t) > 0 para t ≥ (N−1)/992 + 5. OPEN: integral interior y
    balance con ARCH_sharp.

57. **POWER_CUMULATIVE_AUDIT_023.md** — Auditoría. APROBADOS criterio CELL (condicional), punto 128 y
    falsificador 129; hipótesis universal K ≥ 0 FALSIFIED; §7 (CB-ID, CB-POS, K-MASS, BOUNDARY)
    aprobado; balance y compensación de ARCH_sharp abiertos.

58. **POWER_CUMULATIVE_INVERSE_022.md** — Primitiva compensada. PROVED: J_N = Σμ(m)w_N(m·);
    MASS Σ_n J_N(n) = 1; CELL (si K_N ≥ 0 global, F_N ≤ −2(¾ − log2)(1 − J_N(1)) ≤ 0); OUT-K; POINT
    0.003 < K_128(1) < 0.004; CB-ID F_N = −2∫K_N C_B; CB-POS; K-MASS; BOUNDARY. FALSIFIED: K_N ≥ 0
    universal (023). OPEN: control cuantitativo de BUDGET F = −2∫K⁺C_B + 2∫K⁻C_B que además compense
    ARCH_sharp.

59. **POWER_CUMULATIVE_TEST_023.md** — Test N = 129. PROVED: −1/250 < K_129(1) < −1/251 (cola
    Möbius completa < 10⁻¹⁰). Refuta el criterio K ≥ 0; no da signo de J, ERR ni W.

60. **POWER_DEFICIT_AUDIT_013.md** — Auditoría de DEFICIT_LIMIT013. PROVED para la clase declarada:
    0 < Rayleigh < 1/25, m(4) < −2/5, L8(c) > 1/20 ∀c ≥ 0. Fuera de la clase: estimaciones que
    conserven medida racional, ganancias positivas, acoplamiento polar o filtros específicos.

61. **POWER_DEFICIT_LIMIT_013.md** — NO-GO (PROVED) de la clase «transporte separable por déficit
    puntual» en orden 8, u = 63/2: con v = (169,−310,405,−460,460,−405,310,−169), b < 1/25; con
    m(4) < −2/5, toda pérdida puntual L8(c) > 1/20, luego b − c − L8(c) − p_loss < −1/100. Reapertura:
    retener ganancia en m ≥ c, distribución espectral del numerador, acoplamiento polar, filtros
    específicos o contribución aritmética. No prueba AP[v] < 0 ni W < 0.

## A. Lista deduplicada «no relanzar» (con condición de reapertura) y cotejo con RULES_AVOID.md

Marcas: [OK] presente y fiel; [INEXACTO] presente con diferencia; [AUSENTE] no figura.

A1. Reconstruir el puente de densidad o reparametrizar la escalera (POWER_CORPUS_OPPORTUNITY_AUDIT,
    tabla; BRIDGE_002; CONFLUENT_BRIDGE_014). [OK] = RULES D1.
A2. Más dimensiones mediante filtros u optimizar umbrales (CORPUS_OPPORTUNITY). [OK] = D2.
A3. Densidad desde una unión positiva. Fuente: «Criterio L2 exige liminf r(n)^2/n=0; el puente de
    forma requiere además otra topología y cruces». RULES D3: «sólo con liminf r(n)²/n = 0 y un bloque
    que repare el momento». [INEXACTO]: falta «otra topología (la de la forma) y los cruces»; la fuente
    no dice «un bloque que repare el momento». Añádase también, de AUDIT_002 §8 y CONFLUENT_BRIDGE_014
    §5: una unión de espacios de dimensión acotada o una cadena de vectores no hereda la suficiencia.
A4. Recurrencia o descenso solos (CORPUS_OPPORTUNITY; BOUNDARY_BALANCE_035 §6: sólo con una columna
    k = 1 positiva y un terminal k = 0 positivo reales). [OK] D4 en cuanto al resto; [AUSENTE] el patrón
    positivo reutilizable «columna + terminal ⟹ descenso» de 035.
A5. Monotonías Schur/Green, clase BASE (CORPUS_OPPORTUNITY). [OK] = D5.
A6. Extender la torre MIXED4 «por rutina; TP2 real no es TP de todos los órdenes». [INEXACTO] D2 dice
    «extender la torre de órdenes finitos» sin la advertencia TP2 ≠ TP∞.
A7. Calor/theta/Poisson renombrados (CORPUS_OPPORTUNITY, contraste adicional). [OK] = D6.
A8. «Hacerlo global/no lineal» sin operación (CORPUS_OPPORTUNITY). [OK] = A4 de RULES.
A9. Representación positiva tipo Stieltjes/anti-Löwner: «objetivo legítimo, sin nueva candidata;
    hace falta fórmula y prueba de signo independientes». [AUSENTE] en RULES (ni como prohibición
    ni como terreno).
A10. Completitud parcial fuera de una ventana: «sólo investigación preliminar: especificar E y
    comprobar identificación, falsificadores y antecedentes». [INEXACTO]: RULES F la lista como
    «casillero sin objeto» (O166.802.1) sin la condición de especificar E.
A11. Completitud de cuadrados / todas las potencias (CORPUS_OPPORTUNITY). [OK] = D14.
A12. Positividad de todos los prefijos Abel T_m (COEFFICIENT_BALANCE_033 «Seguimiento034»: «No
    relanzar positividad de todos T_m como lema sin cambiar la agrupación o introducir una compensación
    real»; COMPARISON_AUDIT_034 §3). [AUSENTE].
A13. Positividad de cada componente Erlang E_j (ERLANG-FAIL, 033). [AUSENTE].
A14. Positividad puntual del kernel conjunto Ω (ARCH_CELL_026: Ω(3/2) < −1/10); reapertura: cota
    unilateral de ∫K_NΩ con la restricción gamma real. [AUSENTE] (RULES D10/D11 no lo cubren).
A15. Positividad universal de K_N = J_N + xh_N y de h_N (022/023: K_129(1) < 0, h_128(1) < 0);
    reapertura: criterio integrado (BUFFER/BUDGET) con estimación real. [AUSENTE].
A16. Omisión de componentes Ramanujan pequeñas por balance de bloque (CORRECTION_031). [AUSENTE].
A17. Transporte separable por déficit puntual en orden 8 (DEFICIT_LIMIT_013, NO-GO PROVED de clase);
    reapertura: retener ganancia positiva, medida espectral, polar, filtros o aritmética. [AUSENTE].
A18. Monotonía del cociente AP bajo movimiento de polos para todos los numeradores (AUDIT_005
    falsificador 4/5 − π; AUDIT_007 uE′ < −140/31 en n = 131072). [AUSENTE].
A19. «ARCH positiva para cualquier número de polos ≥ 31.5 con resto pequeño» (FOUR_005, vector
    (1,−1,1,−1)). [AUSENTE].
A20. «AP ≥ 0 en el bloque y aritmética como perturbación» (WITNESS_006; CONFLUENT_BRIDGE_014 §6: el
    contacto 2 no se suprime como O(N/u_N²)). [AUSENTE].
A21. Patrón universal de reparación por contactos bajos (AUDIT_008) y signo de un primo uniforme en
    todas las direcciones (THIRTEEN_052: el contacto 2 es adverso en la dirección del Schur). [AUSENTE].
A22. Principal truncado con corte polinómico (CONFLUENT_BRIDGE_014 §§8–9: MOV-NEC, PRIM-CUT; incluso
    con ambos momentos nulos). Condición necesaria: liminf u_N log Q_N/N ≥ 2. [AUSENTE].
A23. «Representación cosh/theta positiva ⟹ signo de mezclas» (CONE_001 §4, AUDIT_002: H = 3+cosh).
    [INEXACTO]: RULES C1 dice «cierres por productos cosh», que no recoge este falsificador de dos
    generadores.
A24. Positividad sobre la unión de planos de dos potencias como si fuera sobre la suma (CONE_001 §5,
    BRIDGE_002 §4). [AUSENTE].
A25. Floor de masa total m(τ_N) − A_T con corte fijo 240 tras entrar 5; cambiar corte o floor o
    repetir certificaciones (CONTACT_FLOOR_045). [AUSENTE].
A26. Presupuestos por componentes de orden 1 frente a márgenes de 10⁻¹⁵ (BALANCE_AUDIT_033 §4,
    CONTACT_BALANCE_021 §5). [INEXACTO]: RULES B2 trata la holgura frente al margen global; no la
    cancelación crítica entre ARCH, peine y polar de un átomo.
A27. NO-GO de candidatos del LEDGER no recogidos: C1 (transferencia retículo→continuo), C9 (Schur
    con métrica δ = log(lcm/gcd)), C12 (planos finitos libres de Λ, margen ε abierto), C13 (Krylov a j
    acotado), C17 (clase 𝒦_gap), C21 (Neumann de grado finito), C24 (clase de sólo masa de peine),
    C25 (cota de medida + Logvinenko–Sereda), C28/C29 (perfil fijo, clase de Vaughan + proceso B), C30
    (Schur por clases), C31 (barrido del eje de índices), C39 (positividad 2×2 de peldaños), C41/C42
    (desigualdad de cola con gauge; multiplicador S-lema forzado a 1), C43 (ventana J_R → {1}), C48
    (entrada de contacto genérica), C49 (Schur local × arquimediano), C51 (argmax del fondo cóncavo).
    [AUSENTE] salvo C5 (germen) y C18 (palabras homogéneas), que RULES C1 menciona.
A28. DOSSIER §6(e): «arithmetic squares on (½log2,½log3)» se reduce a un número (λ^{∞,P}_min vs
    v_2 = 0.980…; numéricamente ≈ 0.49 en T ≈ 0.367) y «should be closed rather than listed as open».
    RULES F: «Medidas exteriores con signo; cuadrados aritméticos en (½log2, ½log3)». [INEXACTO]:
    lo presenta como terreno abierto.
A29. Leyes bilaterales: RULES F lista «λ_A = L(T)(1+o(1)) en rangos no acotados» como no excluido;
    LEDGER C20 registra NO-GO de la ley exponencial simple y reduce la mitad inferior a (N1′).
    [INEXACTO]: falta la exclusión de la ley simple.
A30. Ruta N (Carathéodory–Fejér en ventana finita) y C7: no cerrada; reapertura con razón escrita
    frente al fallo «en el límite». [AUSENTE] (ni prohibida ni listada como terreno).

## B. Resultados positivos PROVED (alcance exacto)

B1. Puentes y suficiencias (CONDITIONAL hacia (★)): K^{(m)} ⪰ 0 ∀m ⟹ (★) (BRIDGE_002, AUDIT_002);
    bloques V_N(u) completos W ⪰ 0 para una sola u ⟹ (★) (CONFLUENT_BRIDGE_014 §4); tasas móviles
    exige N/u_N → ∞ (§6); W_{≤Q_cut} ≥ −ε_N, ε_N → 0, en V_N(N^{3/4}) ⟹ (★) (§7, MOV-TAIL error < e^{−N}).
B2. Escalera de potencias: Q ≥ 0 en todo plano {X^{−a}, X^{−b}}, a, b ≥ 32 (CONE_001); toda terna con
    exponentes ≥ 32: W > (7/125)‖f‖² (AUDIT_004 + CONFLUENT_004).
B3. Bloques confluentes a u = 63/2: V3 arquimediano > 1/10; V4 W > 1/5 (FOUR_005); V12 W > 10⁻⁴
    (BLOCK_007); V13 W > 1/4000 y pivote ZERO13 ∈ (0.0003, 0.0005) (THIRTEEN_052).
B4. Órbitas highpass: dim 12, j ≥ 14: ARCH > 859/800 (CENTERED_CUTOFF_049); dim 13, j ≥ 96: E23 > 1/10
    (CENTERED_MOMENT_053).
B5. Átomos f_{N,k}: wedge u ≥ 64√N, todo N, k: W > 2/5 (029); k ≥ 1 y u² ≥ 225N/4, N ≥ 3: W > 1/40
    (034); filas 1..17, todo k, u = 63/2: W > 1/40 (035); filas 1..12 a u = 31.5 y 1..8 para todo
    u ≥ 31.5 (034 combinado); átomo (211,1): W ∈ (3.4, 4.5)·10⁻¹⁵ (032).
B6. Peine: una raíz para k = 1 y P_{N,1} > 0 para N ≤ 211, u ≥ 31.5 (019); exactamente k raíces y
    signo (−1)^{k+1} de la cola para u log q ≥ 4k(N+k−1) (065).
B7. Herramientas: fórmula estable de ARCH para todo N (032); lema de movimiento de polos arquimediano
    (AUDIT_004); identidad (AP) (AUDIT_005); criterio de transporte η > 0 y cotas B_Y, B_F, B_T (010);
    0 ≤ τm′ < 4 (AUDIT_007); Bernstein ponderado (049); 1/ζ(1+z) = z − γz² + R_3, |R_3| ≤ 9|z|³ (040);
    CURVATURE −2q′/t < q″ < 0 (040); pesos bilaterales BILAT (029).
B8. Inverso Möbius: h ≥ H/4 en log x ≥ (N−1)/30 (todo N), global N = 2 (020); MASS, CB-ID, CB-POS,
    K-MASS, BOUNDARY, OUT-K (022); LOCAL/BUFFER, OUT-CELL (024); CENTRAL-SIGNS y CONSTANT-CUTOFF para
    N ≥ 2⁸⁰ (040); cortes uniformes 2 ≤ N ≤ 129 (UNIFORM_CUTOFF026 vía 026-audit).
B9. Identidades de mezcla MIX y ABEL con pesos no negativos (033); oscilación de T_m (034).
B10. DOSSIER §6: corrección del sándwich para λ_S < 0; monotonía de n_−(A_ev); reducción exacta S_η;
    cuadrados aritméticos ⟺ λ^{∞,P}_min ≥ v_2. CORRECTION_031 §5: colapso rough.
B11. LEDGER: max_c λ_A(T;cΛ) = Θ_T; λ_max(Π_T)/A_T ∈ [¼,½]; coercividad de primera celda 0.069611;
    λ_A(1) ≥ 10⁻²³, λ_A(1.035) ≥ 2·10⁻²⁶; falsificadores certificados a_3, Beurling, 1.1Λ.

## C. Obligaciones OPEN (enunciado preciso; qué se intentó)

C1. Para todo m: [L(32+i)+L(32+j)]/(63+i+j) ⪰ 0, 0 ≤ i, j ≤ m. Intentado: planos (orden 2), ternas,
    certificados de grilla fija hasta 6 pivotes; sin principio para todo m.
C2. Para u = 63/2 y todo N: W ⪰ 0 en V_N(u). Certificado hasta N = 13 (y N = 4, 12); bloqueo:
    margen decreciente, contactos adversos en la dirección del Schur.
C3. En V_N(N^{3/4}), Q = ⌈exp(40N^{1/4})⌉: W_{≤Q}[f] ≥ −ε_N‖f‖² con ε_N → 0. Sólo se probó la
    cola y la necesidad de un corte exponencial.
C4. Transporte V13 completo: certificar j = 1..95 y pagar contactos n ≥ 4 (053).
C5. Filas N ≥ 18 a u = 63/2 (terminal k = 0), tasas variables, mezclas arbitrarias de átomos (035).
C6. Átomos: Σ_n S_N(n) ≥ −ARCH_sharp[g_N]/[2C_N(0)]; equivalentemente cota de BUDGET
    −2∫K⁺C_B + 2∫K⁻C_B que compense ARCH_sharp (022, 024, 026). Intentado: K ≥ 0 (falso), Ω ≥ 0
    (falso), criterio celular (sólo celdas exteriores).
C7. Cota de ∫K_NΩ usando que K_N viene de la autocorrelación gamma (026).
C8. Abel: signo de Σ(v_m − v_{m+1})T_m sin exigir T_m ≥ 0 (033/034).
C9. Ventana móvil de SIGNED_TRANSFORM035: control aritmético de t_m bajo P_d.
C10. AP en 4 polos ≥ 31.5 con p_u > 0: Cov_μ(m,R) ≥ (E_μ[R] − r_0)p_u (AUDIT_005).
C11. CONE_001: L(a) − uL′(a) > 0 para 1 < a < 32 y determinantes de orden 3.
C12. DOSSIER: (L2) S_{T,k(T)} ⪰ 0; (N) 𝓕_T ≤ 𝔞^♯ en P_T; (S) Arch_M − Div_M − Near_M ⪰ 0;
    (L2′) S_η ⪰ 0; crecimiento del conjunto negativo de Nyquist (O(T) o e^{A_T}); cláusula (5).
C13. LEDGER: (SL_T) ℛ ≤ κ − |σ_T| en E_T; (EB_C) presupuesto de borde ≤ 8πe^{2T}hλ_A; (HR_g) suelo de
    coercividad en ℓ_g; (U) λ_max(A_τ) ≤ m − κ uniforme para T > log2; signo de ∂_tQ en el clúster.
C14. ARCH_TRIPLE_004: monotonía de la menor eigenenergía arquimediana al separar tasas (no probada).

## D. Objetos o ideas no iniciados / no examinados

D1. LEDGER C4: lente corona/símbolo sobre M ↦ 𝔸_M (NOT STARTED).
D2. LEDGER C6: defecto de transporte M → M+1 y coercividad de ventanas adyacentes (NOT STARTED).
D3. LEDGER C7 / AUDIT_002 hit 2: ruta N (Carathéodory–Fejér en ventana finita, sin límite) (NOT
    STARTED; a medio argumento en fase 160).
D4. AUDIT_002 hit 1: cotejo de 𝔊_T = S^{Sch}_T + J (M4) contra thm:coer-schur.
D5. LITERATURE_001: extensión de Kreĭn con átomos en log p (nunca intentada).
D6. AUDIT_003: residuo «bordes de capa κ_{T+log n}» (fase 202, sin propuesta); Lema RF.1 sin integrar.
D7. DOSSIER §6(g)/(A2): test de fuga gauge-minimizada de los cuasi-minimizadores; §6(h): crecimiento
    del conjunto negativo de Nyquist; §7.3: valor medio de |P_{s_w}|² con ecuación funcional aproximada
    (cotejar celda vacía de P48); §7.7: compresión de ½(D_e + HᵀD_oH) al bloque negativo.
D8. CORPUS_OPPORTUNITY: representación Stieltjes/anti-Löwner (sin candidata); selección E de completitud
    parcial (preliminar).
D9. AUDIT_005 §4: no se buscó falsificador para cuatro tasas ≥ 31.5.
D10. LEDGER «next» no ejecutados: resumación de Chebyshev (C21), barrido Lanczos r ∈ [1.1,1.3] a T ≥ 4
    (C44/C46), cota de Lipschitz certificada del margen de banda (C46), Schur del superviviente con la
    pieza de paridad (C39).

## E. Cobertura

Leídos íntegramente 61 de 61 archivos (de AUDIT_001.md a POWER_DEFICIT_LIMIT_013.md, orden `ls`),
más RULES_AVOID.md, OBJECT_SPEC.md (fase 212), STATEMENT_001.md, POWER_CONE_001.md y
POWER_BRIDGE_002.md para notación. Ningún archivo ni tramo del rango quedó sin leer. No se leyeron
los .py ni los archivos citados fuera del rango (p. ej. UNIFORM_CUTOFF026, PRIME_BALANCE033,
SIGNED_TRANSFORM035, DIVISOR_COMPARISON034, THREE002); lo que se dice de ellos procede de las
auditorías del rango.
