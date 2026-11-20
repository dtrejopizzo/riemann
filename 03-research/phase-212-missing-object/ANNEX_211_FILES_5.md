# Anexo 211, bloque 5 — lectura completa de `POWER_THETA_DENSITY_ORIGIN_AUDIT_087.md` … `ROUND_001_A.md`

Fuente: `03-research/phase-211-sign-sandbox/`, archivos `*.md` en orden alfabético (`ls *.md | sort`), del
`POWER_THETA_DENSITY_ORIGIN_AUDIT_087.md` al `ROUND_001_A.md` inclusive: 41 archivos, unos 454 KB, leídos
enteros. Notación de `STATEMENT_001.md`, `POWER_CONE_001.md` y `POWER_BRIDGE_002.md`: (★) es λ_A(T) ≥ 0 para todo
T; W es la forma exterior completa (ARCH + polar + peine); L(a) = 1/a + 1/(a−1) − (log π)/2 + ψ(a/2)/2 + ζ′/ζ(a);
K_ij = [L(a_i)+L(a_j)]/(a_i+a_j−1) es la matriz de W sobre exponenciales e^{−(a−½)y}1_{y>0}; Φ es la densidad theta
par positiva de CONE_001 §7; Z(u) = ∫Φ e^{ut}, M = Z′/Z (M(u) = L(u+½)); V = −log Φ. Etiquetas tal como constan en
la fuente. Cuando una fuente usa un enunciado externo a la forma, se parafrasea como «(★)» o «fuera del sandbox».
Dos nombres de archivo llevan un sufijo de fecha que aquí se omite (`*_[sufijo]`).

## Entradas por archivo

**1. POWER_THETA_DENSITY_ORIGIN_AUDIT_087.md** — Auditoría del signo en el origen del Wronskiano de cuatro
densidades R4: W_λ(1,A,B,C)(0) con A = p²−q−2p/t, B = p/t, C = (p³−3pq+r)/t (p,q,r jets de V), vía la matriz de
jets de Φ hasta orden 10 y la identidad RAISE W(1,A,B,C) = −k³J²(E/J)′, k = B′. Etiqueta: APROBADO / PROVED para
el punto t = 0 y un entorno no cuantificado (certificado racional por intervalos, cola theta pagada). Resto: signo
global en t > 0 y propiedad de Chebyshev de las cuatro densidades en la semirrecta; criterio Darboux global y rama
S4 OPEN. Positivo reutilizable: W_λ(1,A,B,C)(0) < 0 (sólo el origen y un entorno sin radio).

**2. POWER_THETA_DENSITY_OUTER_088.md** — Mismo Wronskiano en t ≥ 1. PROVED (certificado polinómico/racional
exit0/PASS, auditado): G = t⁴W_t(1,A,B,C) < −4000 t²y⁶ y W4 < −4000y⁶/t² para todo t ≥ 1, y = πe^{2t}; primer modo
por polinomio con 27 coeficientes positivos tras t = 1+T, y = 21+Y; cola theta completa hasta orden 6 pagada
(E = 62523502209/6553600000000000000000). Consecuencia: (E_raise/J)′ > 0 en t ≥ 1 y determinante de densidades
negativo para cuatro nodos todos ≥ 1. Resto: el compacto 0 < t < 1 (pendiente para Andreief en la semirrecta). No
transporte PF4 global, no región W nueva, no cinco órdenes.

**3. POWER_THETA_DENSITY_OUTER_AUDIT_088.md** — Auditoría de 088. APROBADO / PROVED para todo t ≥ 1 (mismo hash).
Confirma normalización del primer modo, cola hasta V⁽⁶⁾, polinomio genérico de 55 monomios y K = 30936927338496.
Límite: no Andreief en toda la semirrecta mientras falte 0 < t < 1; 087 sólo da un entorno del origen.

**4. POWER_THETA_DENSITY_TRANSPORT_089.md** — Transporte del signo R4 al Turán global. PROVED (usa el certificado
compacto 089 en 0 < t ≤ 1, archivo `POWER_THETA_DENSITY_COMPACT_089.md`, fuera de este bloque, más 088 en t ≥ 1).
Sistema [1,B,A,C] con Wronskianos 1, k, k²J, −W(1,A,B,C) > 0 ⇒ sistema de Chebyshev extendido ⇒
det[ρ_j(t_i)] < 0 para todo 0 < t1 < … < t4; sinh(ut) estrictamente TP4; Andreief ⇒ det[Z′, u²Z′, uZ, u³Z](u_i) < 0;
confluencia ⇒ **T_R = 2R′R‴ − 3(R″)² > 0 para todo λ > 0** (R(λ) definido por f = f₁(1, λ, R, λR)). Con 090 (fuera
de bloque) y 086: h = 1/b estrictamente cóncava y todos los pares distintos del resto regularizado G_p PD para todo
p > 0. Resto: concavidad de ambos datos recíprocos de G_p, sus Turán, un segundo paso Schur, S4, cinco/todos los
órdenes. Positivo reutilizable: T_R > 0 global; det de cuatro densidades < 0 en todos los nodos positivos.

**5. POWER_THETA_G_COMPACT_080.md** — Curvatura Δ(u) = c² + ucd + u²ce − 2u²d² (c,d,e = M, M′, M″) con
g″(u²) = −aΔ/(4u³c³), g(x) = a√x/M(√x) − 1, a = M′(0), en el compacto 1/2 ≤ u ≤ 63/2. PROVED (certificado 4096
paneles, resto de Cauchy uniforme r = 1/16, B = 6·10⁷, cola < 10⁻¹², función entera E(A) = A(A−1)ζ(A)Γ(A/2)π^{−A/2}).
Con 078 (u ≥ 63/2, fuera de bloque): **g″(x) < 0 para todo x ≥ 1/4**; con 079: **K es definida positiva para tres
exponentes distintos cualesquiera a_i > 1** (forma completa ARCH + polar + todos los contactos; congruencia diagonal
a potencias X^{−a}). Historia: encierros directos/Taylor2/Taylor4 fallaron por dependencia, no son contraejemplos.
No cuatro generadores, no todos los órdenes, no ventana T.

**6. POWER_THETA_G_COMPACT_AUDIT_080.md** — Auditoría de 080. APROBADO en matemática y código; reproducción
independiente FULL PASS. Confirma deflación, resto de Cauchy, malla diádica exacta sin huecos. Resultado:
triples positivos para todos a_i > 1; no cuatro ni todos los órdenes; 081/082 y obligaciones recursivas aparte.

**7. POWER_THETA_HAZARD_COMPACT_073.md** — (log Φ)⁗ < 0 en [0, 1/4] (cinco sumas theta S⁽ʳ⁾, polinomios
Q_{r+1} = 2y(Q_r′ − Q_r), numerador NUM = ea³ − 4dba² − 3c²a² + 12cb²a − 6b⁴, cola desde m = 5, malla 4096).
PROVED/APROBADO. Con el exterior de la fase 103 (t ≥ 1/4): **V‴(t) > 0 para todo t > 0 (HAZARD)**. Alcance: propiedad
estructural de Φ; no da W ≥ 0, ni ordena los cinco covariantes de 103_43 §4.

**8. POWER_THETA_RATIO_COMPACT_077.md** — Dos signos locales C > 0, N > 0 en 0 < x ≤ 1, con
C = p³ + xp²q − pq − xpr + xq², N = (xq−p)C′ − xrC (p,q,r,s = V′…V⁗). PROVED/APROBADO: origen desingularizado
(V⁽⁶⁾ < 0 en [0,1/16] y b < 2a², a = V″(0), b = V⁗(0), por 1024 paneles) y 8192 paneles en [1/16,1]. Da L = (xq−p)/C > 0
y L′ < 0 allí. Solo, no da G_u > 0; con 077 OUTER y REMAINDER sí.

**9. POWER_THETA_RATIO_OUTER_077.md** — Los mismos C, J en x ≥ 1. PROVED/APROBADO (verificador Fraction, tres PASS):
C > 3(1+x)y³, J > 31x²y⁴, y = πe^{2x}; primer modo con 16 y 36 coeficientes positivos; cola theta hasta orden 4.
Bordes: 0 < L ≤ 20/(3y²) → 0, wΦ → 0. No resuelve 0 < x < 1 (hecho en 8).

**10. POWER_THETA_REMAINDER_077.md** — Criterio de un valle para el resto Schur real. Objeto: F_u = J − βΦ_u,
J(x) = ∫_{|x|}^∞ yΦ, β = u²a/(ua−c); hipótesis R-HYP: R = (V′+xV″)/(−τ′) creciente y → ∞ (τ = J/Φ). Prueba: forzante
f_u = Φ·B_λ con dos momentos nulos ⇒ patrón +,−,+; interpolación convexa de H(v) = v − √(v²−1) ⇒ F_u(0) < 0; conteo de
ceros por Rolle ⇒ un único cero positivo simple. Condición local suficiente LOCAL-HYP (C > 0, L decreciente → 0,
wΦ → 0), descargada por 8 y 9. **PROVED: T_u(z) > 0 y G_u(z) > 0 para todo u, z > 0 (REAL-REMAINDER)**. §9 corolario
PROVED: matriz anclada en {0,u,v} definida positiva para u ≠ v > 0 (vía K_F con F = uB, |uF′/F| < 1); el nodo 0 es el
exponente ½, fuera de la clase a > 1, no es un tercer test W. Resto: positividad del kernel de dos nodos de G, tres
generadores (luego hechos por 080 por otra vía), todos los órdenes.

**11. POWER_THETA_REMAINDER_AUDIT_077.md** — Auditoría del ensamblaje 077. APROBADO para Φ real (forzante, dos
momentos, interpolación, Green negativo, conteo de ceros, LOCAL-HYP, certificados compacto/exterior, corolario
anclado). Resto explícito: «controlar los términos cruzados del kernel de dos nodos de G o una propiedad que los
domine». No tres generadores (en esta ronda), no W, no ventana T.

**12. POWER_THETA_SCHUR_DENSITY_075.md** — Densidad positiva del denominador regularizado:
h_u = Φ[cV′ − ux], k_u = ∫_x^∞ h_u, Φ_u(x) = (1/u)∫_{|x|}^∞ sinh(u(y−|x|))k_u(y)dy. PROVED/APROBADO: k_u tiene un solo
cruce (−/+), balance ∫cosh(uy)k_u = 0, **Φ_u > 0 en toda la recta**, Φ_u″ − u²Φ_u = k_u,
H_u(z) = ∫Φ_u e^{zx} = D_u(z)/[z(z²−u²)], D_u = zcZ − uZ′, H_u > 0 y log H_u estrictamente convexa en ℝ. Resto: comparar Φ
con Φ_u para ordenar Z/H_u y controlar el kernel de G_u = (c²/(uz))[Z/H_u − Z(0)/H_u(0)] − cz/u (abierto en esta ronda).

**13. POWER_THETA_SCHUR_DENSITY_AUDIT_075.md** — Auditoría de 075. APROBADO (aclaración de Fubini en NEG-MASS).
Confirma F₁(z) = −cz/u + c²Z/(uzH_u) y residuo uc²/(ua−c). Nada convierte F₁ en H_u′/H_u; no se preserva V_u‴ > 0; no
kernel Pick de orden dos para F₁. Comparación Φ–Φ_u OPEN.

**14. POWER_THETA_TWO_COPY_073.md** — Concavidad de la media inclinada por dos copias. Teorema bajo (H): V par C³,
V‴ > 0 en x > 0, V/|x| → ∞: **M″ < 0, M − uM′ > 0, 0 < uM′ < M para u > 0** (identidad 4Cov(S,D²) = M″, varianza
condicional decreciente en |S|). PROVED/APROBADO también para Φ real (THETA-H por 7). Corolario PROVED: **para todo
a ≠ b > 1 la matriz 2×2 K es definida positiva; W[c₁e^{−(a−½)t} + c₂e^{−(b−½)t}] > 0** y lo mismo para potencias
exteriores (congruencia ζ(a_i)). Extiende CONE_001 §5 (a ≥ 32) a todo a > 1. No tres generadores, no ventana T.

**15. POWER_THREE_002.md** — Tres potencias por concentración. PROVED: para A ≥ 2³¹, 0 < h ≤ A/2,
Q[Σ_{j≤2}c_jX^{−(A+jh)}] ≥ 9‖f‖² (base racional all-pass, m(τ) ≥ log|τ| − 8, peine < 1/10, polar < 1/10); §7 PROVED:
**para cada n, n tasas distintas en [u,3u] con u ≥ 2^{40n} dan W ≥ 9‖f‖²** (todos los órdenes con umbral creciente,
no uniforme en n). §8 obstrucción PROVED: la unión de estas familias no es densa en L²(0,∞) (distancia > 1,4 a toda
función unitaria en [1,2]); sumas de paquetes trasladados no controladas. Resto: bajar el umbral a una familia común
de exponentes o controlar los cruces entre paquetes.

**16. POWER_THREE_SECANTS_079.md** — Tres generadores desde una concavidad. PROVED (implicación y converso, bajo BASE:
M > 0, M′ > 0, M″ < 0, M(0) = 0, M/u decreciente): **todos los bloques 3×3 de K_ij = [M(u_i)+M(u_j)]/(u_i+u_j) con
nodos en I son PSD si y sólo si g(x) = a√x/M(√x) − 1 es cóncava en {u²: u ∈ I}**; identidades exactas DET, CONC, GAP
(δ_crit − δ_conc > 0). Obligación reducida: g″ ≤ 0 en 1/2 < u < 63/2 (descargada luego por 5). La concavidad de 1/b no
es necesaria. Región u ≥ 63/2 ya cubierta por 053 (trece polos).

**17. POWER_THREE_SECANTS_AUDIT_079.md** — Auditoría de 079. APROBADO / PROVED (implicación y converso bajo BASE).
Falsificadores 003/074 siguen vigentes: BASE sola no basta para tres nodos.

**18. POWER_TWO_COPY_SCOPE_074.md** — Falsificador de clase. PROVED/APROBADO: potencial explícito
V = A[x²/2 + x^{2p}/(2p·2^{2p−2})], p = 10⁶, A = 4·10⁸, que cumple todas las hipótesis (H) de 14 (V‴ > 0, todos los pares
PD, M″ < 0), con nodos A, 2A, 3A y vector (40,−40,3): c^T K c < −53111/(10000A) < 0. Refuta «hipótesis de potencial
de 073 ⇒ positividad 3×3». Test jet de x⁶ positivo (no falsifica). Contraejemplo auxiliar, no del dato theta ni de W.
Reapertura: «propiedad específica adicional de Φ o estimación concreta de su cruce».

**19. POWER_TWO_COPY_SCOPE_AUDIT_074.md** — Auditoría de 074. APROBADO, exit0/PASS. Mismo alcance.

**20. POWER_UNIFORM_CUTOFF_026.md** — Cortes analíticos en N para el kernel compensado K_N (suma Möbius completa,
D_N = 33P_N − P_N′, u = 63/2). PROVED: t_J(d) = d(d+220)/(330d+6300) por Jensen sobre coeficientes; t_R(d) por Riccati
(0 < q′ < u²/(2d−1)); **D_N′/D_N ≤ 30 y K_N(x) ≥ x^{−32}D_N(log x)/4 > 0 para x ≥ e^{t_*(N)}**; **K_N > 0 para
2 ≤ N ≤ 129, x ≥ e^{2/3}**; celdas de cola favorables S_N(n) ≥ (3/4 − log 2)J_N(n). Resto: las celdas interiores
(número ≤ ⌈X_N⌉, exponente d/330 + O(1), creciente en N); signo de W no probado.

**21. POWER_UNIFORM_STRIP_060.md** — Contorno uniforme. PROVED: para P real de grado < n,
F(s) = (s/(s+u))^j P(s)/(s+u)^n y **j ≥ J(n) = 10¹²(nq_n)³** (q_n = ⌈log₂(n+1)⌉; basta j ≥ 10¹²n⁶):
∫|ρ(x+3i)| < 2∫ρ y **W[F] > ‖F‖²** (polinomios ortogonales del peso Student, derivada de amplitud sin fase, cola de
Taylor por Cauchy). Resto: el interior j < J(n); no cono cuadrático uniforme, no ventana T.

**22. POWER_UNIFORM_STRIP_AUDIT_060.md** — Auditoría de 060. APROBADO. Interior abierto; NECESSITY059 y 016 intactos.

**23. POWER_VARIABLE_RATE_HIGHPASS_096.md** — Proyección de un exponencial fijo f₀ = √(2u₀)e^{−u₀t} sobre
Q_u^rV_n(u) uniforme en la tasa u. PROVED: A_{n,r}(ξ) = (1−ξ²)(1+ξ)^{2r}vᵀG^{−1}v ≤ 200n/√r para todo n ≥ 1,
r ≥ 10¹²n³, ξ ∈ (−1,1) (Gegenbauer en ξ = e^{−η}, Gram en el resto). Consecuencia: **distancia de f₀ a la unión de
todos esos espacios, con todas las tasas, ≥ √(1 − 1/5000)**; la variación de la tasa no repara la densidad L² de la
unión (incluye el cono 060). No trata envolvente lineal, cruces entre bloques, otras familias continuas.

**24. POWER_VARIABLE_RATE_HIGHPASS_AUDIT_096.md** — Auditoría de 096. APROBADO / PROVED. No W negativo, no
imposibilidad global, no nueva cobertura W/T.

**25. POWER_WEIGHTED_AUDIT_031.md** — Auditoría de WEIGHTED_BLOCK031 y GAMMA_WEIGHT031 (este último fuera de
bloque). APROBADOS. Del factor gamma real: máximo único de R = e^{−ut}D/(3/2) en t₀ = (2/3)d/(d+20), q″ < 0 global,
costo adverso de la rama creciente ≤ M2 = u²/(2N−3); criterio de esperanza suficiente sin prueba. La negatividad del
prefijo refuta I_* ≥ 0 universal, no W. Resto: [4, ∞).

**26. POWER_WEIGHTED_BLOCK_031.md** — Prefijo ponderado I_*(X) = ∫_1^X (3/2)x^{−1/2}H(x)dx, H el integrando real de
W[g_N]/‖·‖² = ∫G_NH. PROVED: I_*(225/64) < −1/250, I_*(4) > 1/50; transferencia a G_N real:
**∫_1^{225/64}G_NH < −3/1000 (N ≥ 2²⁴), ∫_1^4 G_NH > 3/200 (N ≥ 2²²), ∫_{225/64}^4 G_NH > 9/500 (N ≥ 2²⁴)** a tasa
u = 63/2. Falsificador: «I_* ≥ 0 para todo X» es falso. Resto: ∫_4^∞ G_NH; desigualdad de emparejamiento de todos los
contactos contra el peso gamma completo.

**27. POWER_WEIGHTED_COEFFICIENT_034.md** — Prefijos Erlang T_m = Σ_{j≤m} jL[S_j] de 033. PROVED: generador
F(z) = [E(v) − vE′(v)]/(1−z)³, v = u(1−z), E = 2Θ′/Θ impar ⇒ F(1+s) = F(1−s); lema elemental tipo Pringsheim ⇒
**T_m toma ambos signos en índices arbitrariamente grandes** (ni T_m ≥ 0 eventual ni ≤ 0). Refuta el criterio suficiente
«T_m ≥ 0 ∀m» (y salvo finitas excepciones). No dice que la combinación gamma sea negativa. Resto: cota firmada de las
contribuciones adversas contra los pesos gamma reales, o agrupación aritmética que preserve la compensación.

**28. PROPOSAL_POWER_CASES_*_[sufijo].md** — Propuesta (OPEN, apoyada en un caso PROVED de CONE_001): estudiar P3,
(r₂₃ − r₁₂r₁₃)² ≤ (1−r₁₂²)(1−r₁₃²) para exponentes en progresión A ≥ 32; luego triples desiguales, cuatro generadores,
y puente PW_N en norma de forma. Falsificador recordado: H(u) = 3+cosh u (logconvexa) da −129/(34 log 2) en (42,−41).
Advierte: «no extrapolar casos finitos a todos los órdenes»; densidad L² sola no basta. Estado posterior: P3 superado
por 5 y 14 (pares y triples para todo a > 1).

**29. README.md** — Marco de la fase: formas (L2), (S), (B) internas; túnel este (arquimediano, Nyquist, Schur) y
oeste (fluctuación Σ Λ(n)φ(n/x)); punto de encuentro: objeto con Λ exacto, acoplado a la ecuación funcional por vía
distinta del factor ζ(½+iτ), no lineal, que decida en casi-coincidencias. Hilos detenidos sin NO-GO: núcleo no local
(209), «bordes de capa κ_{T+log n}» (202), ruta N Carathéodory–Fejér de ventana finita (160), Lema RF.1 (205).
Herramientas nunca apuntadas a P47: símbolo Toeplitz/corona (Paper 26), coercividad de ventanas adyacentes (38),
defecto de transporte exacto (39), determinación de Carleman (22), uniformidad finito-a-total (15), truncación
PNT (7). Candidatos C1–C5.

**30. NEAR_CASES_RESULTS_*_[sufijo].md** — Casos elementales. PROVED auxiliar: mejora de nearfree con ε = 1/(KM)
(sin log log M): a(F_b)/‖F_b‖² ≥ log K − C′_χ − E − 2ζ(5)C_χ/K⁵. Falsificadores algebraicos: (i) «activar un contacto
cercano mejora/empeora en orden de Loewner» falso ya en dimensión 2; (ii) matriz 3×3 de diagonal 1 y extradiagonales
−0,6: pares PD, autovalor −0,2 (pares no bastan); (iii) **ciclo (p,p,p²) con Λ(p²) = Λ(p): término cúbico −2x²z < 0
para p = 2** (x = log2/√2, z = log2/2); no hay cancelación favorable del primer ciclo. Ninguno es negatividad de la
forma (d → ∞). Resto: controlar la norma colectiva de la matriz de casi-contactos frente a la energía arquimediana.

**31. REVIEW_001.md** — Revisión de STATEMENT_001 y DOSSIER_001. Confirmaciones y correcciones: §3 de STATEMENT es
P47 lem:transl(iv) + thm:band (no nuevo; necesita 2T₀ < log 2); la banda 2×2 es necesaria, sin signo. Errores de P47
señalados: «λ_A ≤ λ_S» falso si Ke_S ≠ 0, cota inferior λ_S/(1+‖K‖)² ≤ λ_A falsa si K ≠ 0 (válido sólo con λ_S ≥ 0);
normalización de F₀ (c₀(0) = ‖F₀‖²); «exactamente un autovalor negativo para toda ventana» falso (n₋ = 0 para T
pequeño; correcto «≤ 1» o «= 1 para T ≥ 0,12»). Identidad de semirrecta: no-genericidad en el peine ARGUED. Cuadrados
aritméticos en (½log2, ½log3): existen sii λ^{∞,P}_min(T) ≥ v₂ = √2 log 2 (PROVED); el valor OPEN (NUMÉRICO).
Monotonía de n₋(A_ev(T)) PROVED; «ventana de nacimiento» no probada. Reducción de dos sectores con η ↓ 0: «más chica
que (L2)» REFUTADO (mismo orden).

**32. REVIEW_002.md** — Revisión de ROUND_001_A–D (B–D fuera de bloque). A: Teorema 1(a)–(c) PROVED, ℛ_M ARGUED
(cota cruda O(M^{−7/3+ε})); robustez ante falsificadores ARGUED; nueva condición necesaria: (★) ⇒ 𝒜(w) =
a_{T′}(F₀∗W) ≥ 0 con B(F₀∗W) = −iF̂₀′(i/2) ≠ 0. B: Thm 1.1 (identidad de semirrecta) PROVED sin la cita (σ₂ ∈ (−½,0));
Prop 1.3 nota sobre P > N REFUTADA; §1.6(i) indefinición ARGUED; Lema 1.6 (positividad de celdas monótona bajo
w ≤ Λ) = cor:ext-cfals(i); Prop 2.3 (acoplamiento escalar forzado de φ₀) ARGUED. C: (L2′) PROVED; bloque de 11
modos NUMÉRICO; dimensión del bloque monótona en el peine (ciega bajo Λ). D: Prop 2 «nunca determinado» REFUTADA;
NO-GO PROVED (dados los falsificadores CITED): **criterios que usan sólo los momentos de μ (germen de B en 0) son
ciegos al peine**. Tabla de NO-GO con clases corregidas (§5).

**33. REVIEW_003.md** — Revisión de 002_D, 002_E, 002_A, 002_B, 003_B. CONFIRMED: Θ_T = max_c Φ_T y J_T intervalo
(Toeplitz–Hausdorff), Lemas 1–3 y Cor 4 de 002_E (Lipschitz ℓ¹ en w), Teorema F (suelo de Schur por capas), Props S,
L, M; 003_B Props 1, 5, Lema 2, Teoremas 3–4. Rebajas: «Π(F*) = 0 sii c* = 1» CONDITIONAL; Galerkin «riguroso» →
NUMÉRICO (requiere dualidad fuerte en V_ℂ y testigo primal); 002_B Thm 3.1(b) CONDITIONAL. NO-GO: suelo de Schur
NUMÉRICO; sector exterior monótono en el peine ARGUED y asintótico; prescripciones Schur 𝔸_M = 𝕏∘𝕂_t + ℝ con resto
diagonal (Thm 3) y Div/Near (Thm 4, «algún M») PROVED; la clase entera no es NO-GO (contiene 𝕏 = 0).

**34. REVIEW_004.md** — Revisión de 005_C, 005_A, 005_E, 006_A. CONFIRMED: presupuesto de signo exacto en P_T
(σ_T = C₀ + 4 + Σ_{j≥1}2e^{−(4j+1)T}/(2j+½)), con corrección: σ_T < 0 sólo para T > 0,0520; Thm 2 de 005_C (acoplamiento
arquimediano exacto tras un paso de peine con respuestas Tate); Thm 1 de 006_A (π_± alcanzados por paquetes modulados
en P_T); π_+(P_T) ≥ e^T(1+o(1)) (PNT, CITED); cotas de Weyl. REFUTADO: identidad C_q² como convolución completa
(es truncada para N ≥ e^{2T}); «la familia A alcanza λ_A»; «λ_max(Π_T)/A_T → 0». NO-GO registrados: suelo de Schur
sobre respuestas (NUMÉRICO); mecanismos por identidades sobre E_T (lógica PROVED, falsificador numérico);
Π-Krylov desde el cono arquimediano Λ-libre (NUMÉRICO/ARGUED); conteos inferiores por comparación puntual (PROVED,
trivial); topes de Weyl desde a_T ≥ Arch_T − θ (PROVED dado PNT).

**35. REVIEW_005.md** — Revisión de 005_D, 006_B, 006_C, 007_B, 007_C, 007_D, 008_D. CONFIRMED: forma de saltos
h_T, Teorema 3.1 (W(z) Schur paritario), Prop 4.2 (a_T(F,χ_+) = ⟨F, χ_+ω_+⟩); Thm A, Lema B.0, Thm B (grandes valores);
**testigos certificados: λ_A(½log5+10⁻⁴; a₃) ≤ −0,50528, λ_A(½log5+10⁻⁴; w_{3.2}) ≤ −0,23448, λ_A(1; 1,1Λ) ≤ −0,078244** y
toda ventana mayor por extensión por cero; λ_W^{par} ≤ λ_A^{par} ≤ λ_{W,2}^{par}; expansión de Neumann (condicional a
(H₋), OPEN). REFUTADO: W_ev(0) = −½ exacto (es casi-degeneración que sigue a λ^W_{T,par}); cláusula Danskin de 006_B;
μ₀ < 0 por prop:archneg; «K ≈ 7» (basta K = 1). Simplicidad de λ_A OPEN. NO-GO: 𝒦_gap (ARGUED), familias de palabras
v-homogéneas (PROVED mecanismo + NUMÉRICO), momento/grandes valores (ARGUED), presupuesto por minimizador (PROVED
contable), subparte de la cúbica de respuesta (ARGUED), leyes ajustadas (NUMÉRICO), truncación de Neumann (ARGUED).

**36. REVIEW_006.md** — Revisión de 008_E y 008_C. CONFIRMED: Teorema 3.1 de 008_E (cota superior exterior dada
thm:ext-half), Cor 3.2, conteo de índice (cuatro restricciones en dim ≥ 5 para λ_A, dos en dim ≥ 3 para λ_W), Lema 4.3;
008_C: variación de Hadamard en T (bajo (R_E)), Prop 4 (Grönwall discreto: enunciado correcto, prueba reemplazada).
Rebajas: Prop 5.1 de 008_E para c < 1 NUMÉRICO; Prop 3 de 008_C CONDITIONAL (acotación del minimizador cerca de ±T);
(EB_C) no es (★) + Lipschitz. NO-GO: ley de margen con PEψ₀ (NUMÉRICO); robustez bajo cΛ falla en primer orden para
c > 1 (PROVED); mejora de índice por filtración restringida para en 6 (ARGUED); Grönwall en T (reformulación, clase
𝒦_H; (EB_C) con C = 8πe^{2T} OPEN y más fuerte que (★)).

**37. REVIEW_007.md** — Revisión de 009_A (cota de filtración prolata mollificada). CONFIRMED (PROVED dado
thm:ext-half, con constante K no calculada): **λ_A(T) ≤ 4KC₅N⁹(1 − χ₈(2πN)), λ_W(T) ≤ 4KC₃N⁹(1 − χ₄(2πN))** para
N ≥ 1,6·10⁶ (C₅ = 1,3·10¹⁶, C₃ = 8·10¹⁵) y con constante no explícita para 3 ≤ N ≤ 1,6·10⁶. Lemas de prolatos con todas
las constantes. Rebajas: Lema 2.3 requiere c ≥ 12; N ≥ 410; lectura «doblemente exponencial» sólo CITED en tasa,
constantes explícitas OPEN. Es cota superior: ningún signo.

**38. REVIEW_008.md** — Revisión de 009_B (regla de selección de clase de Fourier). CONFIRMED/PROVED: identidad de
Poisson en ventana (1.0); Thm 1.1 P_{−ε}Π_TEf = ½RΠ_TEh (datos C¹ pares compactos; ARGUED para prolatos crudos);
Thm 1.2 defecto de Fourier diagonal 2(1 − εε_k√χ_k); Lema 1.3; Lema 2.1; Prop 2.2; corrección por paridad:
a_T(w_+, w_−) ≡ 0 y a_T(P_+Ef_+) = 𝒲[Ψ_{f_+}] − a_T(w_+). Rebajas: cota (2.1) CONDITIONAL con κ(K) → 0 esperado; §1.7
ARGUED. NO-GO: la regla de clase Poisson–ℱ es Λ-libre, no es paso de signo (PROVED); para a_P falla el
entrelazamiento exacto (PROVED); «ninguna regla vale» ARGUED. (HR) OPEN.

**39. REVIEW_009.md** — Revisión de 010_A, 011_A, 011_C, 012_A, 012_B, 013_A. CONFIRMED: certificado cos²
(Thm 2.2 de 012_A, primera celda fallida [2,660; 2,661]); Prop 3.3 de 010_A (NO-GO 𝒦_S). REFUTADO: rango abierto de
(HR)(a) «2T ≲ log τ < log Ω_B» (es 2T ≲ log τ < Σ₀ + O(1)); lectura Ω_* ≍ e^{λ+O(1)} (es e^{𝒜_T+λ+O(1)}). Thm 3.1 de 011_A
superado por la cota trivial P ≤ Σ₀. Identidad (2.2) de 013_A = fórmula explícita (CITED, P47 thm:Z); su resto R_w vive
fuera del sandbox. Registro NO-GO (10 ítems, §8): 𝒦_S PROVED; lem:ext-hf vacío en índice polinómico PROVED;
grandes valores + Kovrijkine colapsa a cota puntual; clase de momentos ARGUED; cota trivial con perfil fijo PROVED;
paquetes cortos con cruces en valor absoluto ARGUED; valor medio + Sobolev/Gallagher (familia cuadrática cerrada);
Schur tres bloques LM/H± NUMÉRICO; pequeñez de acoplamiento H₊–H₋ por regla de clase PROVED; clase 𝒱
(Vaughan/proceso B) ARGUED.

**40. REVIEW_010.md** — Revisión de las rondas 014_A–024_A (18 memos). Punto definicional: 𝒲 debe incluir el término
polar 2A(Ψ)B(Ψ) (14A/15A sin él son falsos en general); ℓ_g de las rondas = ½ℓ de P47. CONFIRMED: certificados
17C Thm 3.1 (μ₀ ∈ [0,06961173221 ± 4,38·10⁻¹²]) y 18A Thm 3.4 (T = 0,8) reproducidos; 19B Thm 2.1 (𝒜𝒫 − c𝒞 no acotado
inferiormente para c ≠ 1) PROVED; 19A Prop 1.1 PROVED; 20A Thm 1.3; 21A, 22A, 23A, 24A identidades. REFUTADO: prueba
escrita de «ℕ único ℕ^{1+t} aditivamente cerrado» (enunciado verdadero, prueba corregida); constante 5,72 de 16A.
Registro NO-GO (16 ítems, §19). «Ningún paso de las rondas 14–24 es paso de signo.»

**41. ROUND_001_A.md** — Forma de casi-coincidencias Q_M(s) = sᵀ𝔸_Ms en la familia suave s_w = m^{−1/2}w(m/M).
PROVED: Lema 1 (P_{s_w} = ζ(½−iτ) + M^{½+iτ}w̃(½+iτ) + R_M); Teorema 1 (a)–(c): Q_M = M𝒜(w) + 𝒳_M + 𝒵_N + ℛ_M con
𝒜(w) = a_{T′}(F₀∗W) (vector con B ≠ 0, fuera de P_{T′}), 𝒳_M = O(M^{−K}) (término de borde superpolinómicamente
pequeño), 𝒵_N = O(N^{−5/2+ε}); ℛ_M = O(M^{−3+ε}) ARGUED. Resultado: NO-GO, clase «transferencia retículo→continuo por
Poisson/AFE en la familia de corte suave» (renombrada por la revisión 32 a «familia m^{−1/2}w(m/M), orden principal
en M»); robustez de falsificadores ARGUED. Paso siguiente propuesto: test de regularidad (perfil con |F̂₀|² ≍ |τ|^{−8})
y buscar el signo en vectores no suaves (aritméticos).

---

## A. «No relanzar» deduplicado (con condición de reapertura) y cotejo con RULES_AVOID.md

Marca: **[AUSENTE]** no figura en RULES_AVOID; **[PARCIAL]** figura con otro alcance o redacción; **[OK]** figura.

A1. **Promover hipótesis genéricas sobre el potencial (V par, V‴ > 0, superlineal, todos los pares PD, M cóncava) a
positividad 3×3 o superior.** Falsificador explícito (18). Reapertura: «propiedad específica adicional de Φ o una
estimación concreta de su cruce» (18 §7). **[AUSENTE]** RULES_AVOID B4 menciona productos cosh y «modelo positivo»,
no este falsificador de clase.

A2. **Inferir positividad de matrices desde pares (2×2) o desde aristas independientes.** Matriz −0,6 (30 §3); ciclo
(p,p,p²) con término cúbico negativo (30 §4). Reapertura: control de la norma colectiva de la matriz de casi-contactos
frente a la energía arquimediana. **[AUSENTE]**

A3. **«Activar un contacto cercano mejora (o empeora) la forma en orden de Loewner».** Falso en dimensión 2 (30 §2).
**[AUSENTE]**

A4. **Representación cosh positiva o logconvexidad como control de dos generadores.** 3+cosh u (28; CONE_001 §4).
**[PARCIAL]** RULES_AVOID B4: «representación exacta por productos de cosh (§§11, 13; no decide si multiplicar por cosh
conserva la positividad)»; no cita este contraejemplo de dos puntos.

A5. **Criterio suficiente «prefijos Erlang T_m ≥ 0 para todo m» (o salvo finitas excepciones).** Refutado (27).
Reapertura: cota firmada de las contribuciones adversas contra los pesos gamma reales, o agrupación aritmética nueva.
**[AUSENTE]**

A6. **Premisa «la primitiva ponderada I_*(X) ≥ 0 para todo X».** Falsa en X = 225/64 (26). Reapertura: desigualdad de
emparejamiento que use el factor gamma y controle todos los contactos. **[AUSENTE]** (D18 «sumación por partes
discreta» y «primitivas compensadas de capas» tienen otro objeto).

A7. **Pasar de una unión de familias positivas (umbral creciente 2^{40n}, cono 060, cualquier tasa) a densidad o a la
envolvente lineal.** No densa (15 §8; 23). Reapertura: bajar el umbral a una familia común de exponentes, o control
explícito de los cruces entre paquetes trasladados; 23 no cubre otras familias continuas iniciales. **[PARCIAL]**
RULES_AVOID D3: «Inferir densidad o signo de una unión positiva… Se reabre con liminf r(n)²/n = 0, un bloque que
repare el momento y control de sus cruces»; falta registrar que **variar la tasa no repara la densidad** (096) y la
obstrucción explícita de 15 §8.

A8. **Criterios que usan sólo los momentos de la medida representante de B (germen de B en 0).** Ciegos al peine
(32, NO-GO PROVED dados los falsificadores citados). **[OK]** C1 «criterios de germen de Carleman».

A9. **Transferencia retículo→continuo por Poisson/AFE en la familia suave s_w = m^{−1/2}w(m/M), orden principal en
M.** (41, clase corregida en 32). Reapertura implícita: vectores no suaves (aritméticos). **[OK]** D8 «familia suave
s_w».

A10. **Positividad de celdas (cancelación clave de cor:ext-cfals) como todo el paso de signo.** Monótona bajo w ≤ Λ (32,
Lema 1.6). No excluida como ingrediente. **[AUSENTE]** como tal (B5 «propiedades sparse-estables» es afín).

A11. **Dimensión del bloque Nyquist (o conteo de muestras) como portador de signo.** Monótona en el peine, ciega bajo
Λ (32 C). **[AUSENTE]**

A12. **Desigualdades Schur sólo de suelo (escalar c): λ_min(A_EE) − ‖B‖²/c ≥ 0**, sobre el bloque o sus respuestas.
NUMÉRICO (33, 34). **[OK]** D17 «clase suelo de Schur».

A13. **Prescripciones de factorización Schur 𝔸_M = 𝕏∘𝕂_t + ℝ con resto diagonal o con Div/Near.** NO-GO PROVED (33,
003_B Thms 3–4); la clase completa no está cerrada (contiene 𝕏 = 0). **[AUSENTE]**

A14. **Mecanismos de signo por identidades válidas para todo sistema de Beurling y para a_P sobre E_T** (Λ∗1 = log,
Selberg, factores de Euler locales, identidad de Lévy). (34). **[OK]** B1.

A15. **Familias de Krylov / palabras de (M, Π) v-homogéneas desde semilla Λ-libre bajo la dimensión de captura.**
(34, 35). **[OK]** D17.

A16. **Conteos inferiores por comparación puntual arquimediana; topes de Weyl desde a_T ≥ Arch_T − θ.** (34). **[OK]**
D17 «cotas de Weyl desde Arch − θ».

A17. **Cotas inferiores del hueco de la forma de saltos h_T con pérdida independiente del peine (𝒦_gap)**, en
ventanas con λ_A^{ev}/|μ₀| bajo la pérdida (35, ARGUED). **[AUSENTE]**

A18. **Enunciados de presupuesto por minimizador / ventana de cruce T_×** (35, contable PROVED). **[AUSENTE]**

A19. **Firmar una subparte propia de la cúbica de respuesta con error mayor que λ_A** (35, ARGUED). **[AUSENTE]**

A20. **Leyes ajustadas como portadoras de signo** (35, NUMÉRICO). **[AUSENTE]** (B8 «ley en un rango acotado de
ventanas» es afín pero no idéntico.)

A21. **Truncación de Neumann de grado finito del acoplamiento Schur sobre E_T con cola acotada por ρ(X)** (35;
condicional a (H₋), OPEN). **[AUSENTE]**

A22. **Grönwall en la variable ventana (D ≤ Cλ_A, (EB_C), (VE_C)).** Reformulación, clase 𝒦_H; (EB_C) con
C = 8πe^{2T} OPEN y más fuerte que (★); versión estructurada más débil «ARGUED ausente» (36). **[AUSENTE]**

A23. **Ley de margen superior con la única función test PEψ₀; robustez de la ley bajo cΛ** (falla en primer orden para
c > 1, PROVED) (36). **[AUSENTE]**

A24. **Mejora del índice inferior por filtración restringida (ruta Lema 4.3)**: se detiene en índice 6 (36, ARGUED;
condicional al condicionamiento polinómico κ_C(T), OPEN). **[AUSENTE]**

A25. **Pequeñez del acoplamiento entre clases H₊–H₋ derivada de la regla de selección ℱ** (PROVED NO-GO, 39); regla
de clase Poisson–ℱ como paso de signo (Λ-libre, 38). **[PARCIAL]** D17 «regla Poisson/ℱ» sin la parte de acoplamiento.

A26. **Estimaciones sólo de masa del peine en alta frecuencia (𝒦_S)** (PROVED, 39); **lem:ext-hf con datos de índice
polinómico** (vacío salvo K ≥ c′N^{−1/2}e^{(K_T+λ+1)/4}, PROVED). **[AUSENTE]**

A27. **Medida de grandes valores + Logvinenko–Sereda/Kovrijkine** (colapsa a cota puntual); **clase de momentos con
error de espaciado entero** (irrelevante: la cota trivial P ≤ Σ₀ ya despeja esas alturas) (39). **[AUSENTE]**

A28. **Cota trivial con perfil fijo** (PROVED: T_β finito para todo β, 39); **paquetes cortos con cruces en valor
absoluto** (ARGUED); **valor medio + Sobolev/Gallagher** (familia cuadrática cerrada). **[PARCIAL]** B2 cubre la
familia cuadrática; las dos primeras ausentes.

A29. **Ensamblaje Schur de tres bloques LM/H₊/H₋ con normalización ℓ_g diagonal por bloques** (NUMÉRICO, 39).
**[PARCIAL]** D17 «ensamblajes de dos y tres bloques» (sin la normalización).

A30. **Clase 𝒱 (Vaughan/Heath-Brown + Poisson/proceso B sobre el polinomio de paquete)**: ARGUED; el dual completo
devuelve la fórmula explícita, cuyo resto vive fuera del sandbox (39). **[OK]** D17 «proceso B / Vaughan».

A31. **Símbolo en el eje de índices + error de banda/Toeplitz en unidades D** (NUMÉRICO, 40; no cubre barridos
normalizados por ℓ_g). **[AUSENTE]**

A32. **Clase de celdas R idealizada con restricciones transportadas, κ uniforme en R** (NUMÉRICO); **pieza de
escalón de la desigualdad Schur con peso colapsado c·log N** (NUMÉRICO) (40). **[AUSENTE]**

A33. **Restricción cualitativa de banda sobre datos de celdas R** (PROVED, 40); **cotas absolutas de defecto de banda**
(NUMÉRICO). **[AUSENTE]**

A34. **Cotas robustas en el peine 𝒜𝒫 − c𝒞 ≥ 0 sobre toda la clase de colas admisibles, c ≠ 1** (PROVED, 40). **[OK]**
D17.

A35. **Representante con gauge fijado existencialmente con margen de peine** (PROVED, 40); **secciones canónicas
Λ-libres con δ uniforme** (PIVOT NUMÉRICO). **[AUSENTE]**

A36. **Ventanas de positividad en el peso del peine sobre datos de celdas R** (40). **[AUSENTE]**

A37. **Signo de celda R como invariante de monoide / caracterización aditiva en el rayo de exponentes** (NUMÉRICO,
«la adición singulariza ℕ» ARGUED cerrado) (40). **[PARCIAL]** B7 «sólo monoide».

A38. **Finitas relaciones de suelo de Chebyshev estrictas** (NO-GO CONDITIONAL al ancho numérico de J_T, 40).
**[AUSENTE]**

A39. **Propagación de la positividad a través de las entradas de contacto a lo largo de N** (PROVED NO-GO para el signo
del término de entrada; queda la cota de tasa (EB_C)) (40). **[AUSENTE]**

A40. **Extremalidad de prolatos en el subespacio de índice 8 (Diseño C)**: reintento de L′/L′♯ (40, ARGUED). **[OK]**
C1 «programa L♯».

A41. **«Banda de largo alcance = corrección de radical de rango finito»** (falsificación NUMÉRICA, 40) y **D-suelo del
bloque alto** (ARGUED). **[AUSENTE]**

A42. **Reducción de dos sectores con η ↓ 0 como reducción más chica que (L2)** (REFUTADA, 31: mismo orden; requiere
esparsidad del conjunto no positivo, OPEN). **[AUSENTE]**

Inexactitudes detectadas en RULES_AVOID respecto de este bloque:
- C5: «positividad total de orden ≤ 4 (PF₄ ABIERTO)». En este bloque: cuatro generadores de K PROVED (085, citado en
  4, 2, 5) y el Wronskiano de cuatro densidades de Φ con signo global y Turán global T_R > 0 (4); el transporte «PF4
  global» sigue sin afirmarse (2: «No se afirma transporte PF4 global»). La línea debería distinguir qué parte de
  orden 4 está probada.
- D3 (citado arriba) no recoge la obstrucción por variación de tasa (23) ni la de 15 §8.
- B4 «modelo positivo + transferencia»: no menciona que la clase de potenciales con V‴ > 0 tiene un contraejemplo
  3×3 explícito (18), que es precisamente el límite de las herramientas theta usadas para pares y triples.
- D17 lista «𝒜𝒫 − c𝒞 con c ≠ 1» y «regla Poisson/ℱ» sin su alcance exacto: la primera es «sobre toda la clase de
  colas admisibles» (no sobre un subespacio fijo); la segunda es NO-GO para el signo y para la pequeñez del
  acoplamiento entre clases, no para el uso de la identidad (1.0), que es PROVED y reutilizable.

## B. Resultados positivos PROVED (alcance exacto)

B1. HAZARD: V‴(t) > 0 para todo t > 0, V = −log Φ (7 + fase 103).
B2. Dos copias (14): bajo V par C³, V‴ > 0 (x > 0), V/|x| → ∞: M″ < 0, 0 < uM′ < M (u > 0); aplicado a Φ real.
B3. Pares (14): K 2×2 definida positiva para todo a ≠ b > 1; W > 0 sobre todo plano real de dos exponenciales o dos
potencias exteriores (energía estricta para función representada no nula).
B4. Triples (5 + 16): g″(x) < 0 para todo x ≥ 1/4; K 3×3 definida positiva para todo triple distinto a_i > 1; criterio
general: bajo BASE, bloques 3×3 PSD ⇔ g cóncava en cuadrados (implicación y converso).
B5. Resto Schur real (10): T_u(z) > 0 y G_u(z) > 0 para todo u, z > 0; F_u tiene un único cero positivo simple.
Corolario: matriz anclada {0,u,v} definida positiva (nodo 0 fuera de la clase admisible).
B6. Densidad positiva Φ_u > 0 en ℝ, H_u(z) = D_u(z)/[z(z²−u²)] > 0, log H_u estrictamente convexa (12).
B7. C > 0, L′ < 0, L → 0 para Φ real en todo x > 0 (8, 9).
B8. Wronskiano de cuatro densidades: < 0 en el origen (1), < −4000y⁶/t² en t ≥ 1 (2); con el compacto 089: signo global,
det[ρ_j(t_i)] < 0 para todos los nodos positivos y Turán T_R = 2R′R‴ − 3R″² > 0 para todo λ > 0 (4).
B9. Tres potencias con A ≥ 2³¹, h ≤ A/2: Q ≥ 9‖f‖²; todo orden n con tasas en [u,3u], u ≥ 2^{40n}: W ≥ 9‖f‖² (15).
B10. Cono uniforme (21): W[F] > ‖F‖² para todo numerador real de grado < n y j ≥ 10¹²(n⌈log₂(n+1)⌉)³.
B11. Corte analítico (20): K_N(x) > 0 para x ≥ e^{t_*(N)} (t_* = d/330 + O(1)); K_N > 0 en 2 ≤ N ≤ 129, x ≥ e^{2/3};
celdas de cola favorables.
B12. Bloque ponderado real a u = 63/2 (26): ∫_1^4 G_NH > 3/200 (N ≥ 2²²); recuperación ∫_{225/64}^4 G_NH > 9/500 (N ≥ 2²⁴).
B13. Mejora de nearfree con ε = 1/(KM) (30 §1): margen ≥ 1 para K ≥ K₀(χ), todo M.
B14. Proyección uniforme en la tasa (23): A_{n,r}(ξ) ≤ 200n/√r para r ≥ 10¹²n³ (resultado de distancia, no de signo).
B15. Cotas superiores (37): λ_A ≤ 4KC₅N⁹(1 − χ₈(2πN)), λ_W ≤ 4KC₃N⁹(1 − χ₄(2πN)) dado thm:ext-half (K no calculada).
B16. Testigos certificados de falsificadores (35): λ_A(½log5 + 10⁻⁴; a₃) ≤ −0,50528; λ_A(½log5 + 10⁻⁴; w_{3.2}) ≤
−0,23448; λ_A(1; 1,1Λ) ≤ −0,078244, y toda ventana mayor.
B17. Certificados de positividad en clases restringidas (39, 40): cos² hasta la celda [2,660; 2,661] (perfil fijo);
17C Thm 3.1 μ₀ ∈ [0,06961173221 ± 4,38·10⁻¹²]; 18A Thm 3.4 en T = 0,8 (clase de restricciones transportadas).
B18. Identidades reutilizables: Poisson en ventana (1.0) y P_{−ε}Π_TEf = ½RΠ_TEh (38); defecto de Fourier diagonal
(38); a_T(w_+, w_−) ≡ 0 por paridad (38); identidad de semirrecta sin la cita externa, σ₂ ∈ (−½,0) (32); presupuesto
σ_T exacto en P_T (34); a_T(F,χ_+) = ⟨F, χ_+ω_+⟩ (35); Teorema 1 (a)–(c) de 41 (descomposición de Q_M en s_w);
condición necesaria (★) ⇒ a_{T′}(F₀∗W) ≥ 0 con B(F₀∗W) ≠ 0 (32); monotonía de n₋(A_ev(T)) (31); π_+(P_T) ≥ e^T(1+o(1))
(34, PNT CITED); λ_W^{par} ≤ λ_A^{par} ≤ λ_{W,2}^{par} (35).

## C. Obligaciones OPEN (enunciado preciso; qué se intentó)

C1. **Cuatro y más generadores / todos los órdenes de K en la escalera completa a > 1 (o a = 32+n):** probar que
[(L(a_i)+L(a_j))/(a_i+a_j−1)]_{i,j≤m} ⪰ 0 para todo m. Intentado: pares (14), triples por una curvatura (16, 5),
cuatro (085, fuera de bloque), umbrales crecientes (15, 21); las herramientas genéricas de potencial no bastan (18).
C2. **Kernel de dos nodos del resto regularizado G_p** (y concavidad de ambos datos recíprocos, sus Turán y un
segundo paso Schur) (4, 10, 11). Intentado: positividad puntual (10), pares de G_p vía 090 (4).
C3. **Paso S4 / transporte de orden superior y criterio Darboux global** (1, 2, 4).
C4. **Interior del cono uniforme:** signo de W[F] para j < J(n) (21); celdas interiores del corte de K_N (número
≤ ⌈X_N⌉) (20).
C5. **Cola ∫_4^∞ G_N H** y desigualdad de emparejamiento de todos los contactos contra el peso gamma (26, 25);
**cota firmada de los adversos contra los pesos gamma** en Σ_m (v_{N,m} − v_{N,m+1})T_m (27).
C6. **Densidad de una envolvente positiva en norma de forma:** familia común de exponentes con umbral fijo o control
de cruces entre paquetes trasladados (15 §8, 23).
C7. **Norma colectiva de la matriz de casi-contactos ≤ energía arquimediana** (30).
C8. **Comparación Φ–Φ_u** que ordene Z/H_u (13; parcialmente sustituida por 10).
C9. **(H₋) para la truncación de Neumann** (35); **simplicidad de λ_A(T)** (35); **(R_E)** y acotación del minimizador
cerca de ±T (36); **(EB_C)** con C = 8πe^{2T}(1+o(1)) (36); condicionamiento polinómico κ_C(T) (36); eq:ext-L (36).
C10. **(HR)(a) en forma de paquete** en el rango finito Ω_lo ≤ τ ≤ 2π·exp(Σ₀ + κ + O(1)) (39); (HR) en el rango k > 4N
(38); (U) de 012_A es sólo necesaria (39).
C11. **Valor λ^{∞,P}_min(½log2⁺) ≥ v₂** que decide los cuadrados aritméticos en (½log2, ½log3) (31); **esparsidad del
conjunto no positivo de Nyquist** (31); **continuidad del segundo autovalor de A_ev(T)** («ventana de nacimiento») (31).
C12. **ℛ_M = O(M^{−3+ε})** y robustez de la descomposición de 41 ante falsificadores (32, ARGUED); test de regularidad
con |F̂₀|² ≍ |τ|^{−8} (41).
C13. Constantes explícitas no asintóticas para 1 − χ_k(c) (37).

## D. Objetos o ideas mencionados como no iniciados o no examinados

D1. Hilos detenidos sin NO-GO (29): núcleo no local de la fase 209 (falta operador/identidad/lema de signo);
«bordes de capa κ_{T+log n}» de la fase 202 (después declarado vacío para el residuo arquimediano definido, 32;
los pares de peine por capas no están cubiertos); ruta N Carathéodory–Fejér de ventana finita (fase 160); Lema RF.1
(fase 205).
D2. Herramientas nunca apuntadas a los objetos finitos de P47 (29): símbolo Toeplitz/corona, coercividad de ventanas
adyacentes, defecto de transporte exacto entre cocientes sucesivos, determinación de Carleman, uniformidad
finito-a-total, cota de truncación con sólo PNT.
D3. Candidatos C1–C5 del README (29): identidad exacta para ∫|P_s|²F̂₀²m no genérica en el peine; la fluctuación de dos
momentos como diferencia iterada con transferencia M → M+1; símbolo del campo M ↦ 𝔸_M; los dos hilos inconclusos;
medida de Carleman forzada por los momentos de B (este último cerrado por 32).
D4. Test de regularidad con un perfil más liso y búsqueda del signo en vectores no suaves (41).
D5. Falsificador de Beurling (c) no ejecutado para la Prop 4 de 008_D (35); falsificadores (b) con P ≤ e^{2T}, (c), (d)
de 002_D (33).
D6. Adición de otras familias continuas de bloques iniciales a la unión, sumas con cruces no certificados, mezclas de
densidades (23, 24).
D7. Extensión de la identidad de Poisson (1.0) a datos con salto en el borde (prolatos crudos) (38).
D8. 𝒢 con definición independiente en un dominio común entre clases (barrido en b = Sa) (39).
D9. Diseño C (prolatos índice 8) no proseguido (40).

## E. Cobertura

Archivos del rango (`ls *.md | sort` desde `POWER_THETA_DENSITY_ORIGIN_AUDIT_087.md` hasta `ROUND_001_A.md`): 41.
Leídos completos: 41. Ningún archivo ni tramo sin leer. Los archivos citados por estas fuentes y situados fuera del
rango (por ejemplo 078, 085, 086, 090, `POWER_THETA_DENSITY_COMPACT_089.md`, `POWER_GAMMA_WEIGHT_031.md`, los memos
ROUND_001_B–D y ROUND_002–024 revisados en REVIEW_002–010) no se leyeron; lo dicho sobre ellos procede de lo que
estas 41 fuentes afirman.
