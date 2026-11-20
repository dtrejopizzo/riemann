# Anexo 211 — tercer tramo de archivos (POWER_INVERSE_INTERIOR_AUDIT_022 … POWER_RECURRENCE_BOUNDARY_036)

Lectura completa, archivo por archivo, de los 66 archivos `*.md` de `../phase-211-sign-sandbox/` que
quedan entre `POWER_INVERSE_INTERIOR_AUDIT_022.md` y `POWER_RECURRENCE_BOUNDARY_036.md` inclusive, en el
orden alfabético de `ls *.md | sort`. Notación de `STATEMENT_001.md`, `POWER_CONE_001.md` y
`POWER_BRIDGE_002.md`. (★) designa el signo λ_A(T) ≥ 0 para todo T. Abreviaturas recurrentes de las
fuentes: u = 63/2; W = forma completa (ARCH + POLAR − peine); f_(N,k) de transformada s^k/(s+u)^(N+k);
g_N = y^(N−1)e^(−uy)/(N−1)!; Φ = densidad theta par real; J(t)=∫_|t|^∞ sΦ, K par con K''=aΦ−J,
a=M'(0)=I2/I0; τ=J/Φ; V12 = bloque confluente de 12 funciones Laguerre a tasa u; E2 = ARCH+POLAR−contacto 2.
Las etiquetas se copian tal como figuran en cada fuente. «Computacional certificado» = intervalos
racionales/Arb exteriores con verificador; se indica cuando el resultado depende de él.

---

## Entradas por archivo

**1. POWER_INVERSE_INTERIOR_AUDIT_022.md** — Auditoría de `POWER_INVERSE_INTERIOR_022` (fuera del rango).
Objeto: h_128(1)=Σ_m μ(m)m^−32 A_128(log m), inverso Möbius completo del kernel gamma de 020.
Resultado: APROBADO, verificador PASS: −2/3 < h_128(1) < −33/50 con cola completa m≥65 < 10^−10.
Falsificador: refuta «h_N(x) ≥ 0 para todos N,x». No prueba negatividad de F_N, del emparejamiento con B ni
de W; continuidad + OUTER020 dan al menos un cambio de signo antes de log x = 127/30.
Positivo reutilizable: valor puntual certificado (computacional) del inverso completo en x=1, N=128.

**2. POWER_INVERSE_KERNEL_020.md** — Inverso h_N(x)=Σ μ(m) m H_N(mx), H_N = x^−33 A_N(log x),
A_N = 32P_N − P_N′ (coeficientes positivos). Etiqueta: PROVED (región explícita todos N; global N=2).
Resultados: (OUTER) H_N/4 ≤ h_N ≤ 7H_N/4 si log x ≥ (N−1)/30; (ROW2) h_2 ≥ H_2/[2ζ(32)] > 0 en x≥1;
(RANGE) |h_N/H_N−1| ≤ 2^−q[1+2/(q−1)], q=32−d/log x>1; (LOCAL) F_N acotado por emparejamiento interior en
[1,X_N] más cola favorable explícita. Resto sin signo: emparejamiento interior ∫_1^{X_N} h_N B; signo de ERR.
Positivo reutilizable: OUTER y ROW2 tal como están, sólo para este kernel gamma a u=63/2.

**3. POWER_INVERSE_LOGCONCAVITY_025.md** — D_N=33P_N−P_N′, c_j=p_j(3d+30j)/(2d−j); inverso compensado
K_N(x)=x^−32 Σ μ(m)m^−32 D_N(log x+log m). Etiqueta: PROVED (LC todos N; corte N=129; ERR129<−33/50).
Resultados: (LC) log D_N cóncava para todo N≥2 (covarianza de razones decrecientes); (CUT) si
D_N′(t0) ≤ 30D_N(t0) entonces K_N ≥ x^−32 D_N(log x)/4 > 0 para log x ≥ t0; N=129, t0=2/3 (certificado
Fraction): K_129>0 en x≥2; (FULL) ERR_129 = −2Σ S_129(n) < −33/50 (con CELL_TEST024 para n=2).
Resto: comparar el déficit ARCH_♯ con −ERR: W[g_129]/C(0)=ARCH_♯/C(0)−ERR sigue sin signo.
Positivo: LC para todo N; FULL sólo en N=129.

**4. POWER_INVERSE_LOGCONCAVITY_AUDIT_025.md** — Auditoría de 025. APROBADO, verificador PASS.
Confirma LC, CUT (K_129>0 en x≥2), ERR_129<−33/50 sobre toda la semirrecta, K_129(1)<0 intacta.
Declara: covarianza y razones de coeficientes son clásicas; el avance es el corte mejorado. No es W≥0;
no se extiende a otros N ni a una ventana T nueva.

**5. POWER_JOINT_AUDIT_027.md** — Auditoría de DISCRETE_BALANCE027 e INTERIOR_CONSTRAINT027 (fuera del
rango) y de una ampliación §8. Etiqueta: APROBADOS, PASS.
Resultados: (JOINT-TAIL) W/C0 = ∫_1^4096 K·Ω + R con 0<R<10^−36 (N=129, cola conjunta real); Ω ≥ ℓ −
(4log t+9)/t, Ω>0.009 en la cola. (JOINT-GAP) identidad exacta de Jensen para la mezcla gaussiana
V=β/G; curvatura negativa del funcional gaussiano completo para v ≥ 65536 (refuta convexidad global).
§8: h_N = E h_a, K_N = E K_a (mezcla de inversos gaussianos), NEG128/NEG129 fuerzan a_h,a_K.
Resto sin signo: ∫_1^4096 K Ω (interior). El déficit .15 de 026 era del comparador, no de W.

**6. POWER_JOINT_SCALE_016.md** — Familia f_(N,k). Etiqueta: PROVED fórmulas; OPEN cono de signo;
FALSIFIED dos justificaciones. Resultados: (BETA) Z=τ²/(u²+τ²) ~ Beta(k+½, N−½); (PACKET) en k/N→c,
c_f(t)/‖f‖² → cos(u√c t): el contacto 2 no desaparece en el cono lineal; (MEAN) E y = (N−½)/u;
(WEIGHT) ‖e^{ηy}f‖²/‖f‖² ≥ exp[2η(N−½)/u] para todo k; (VAR) dispersión; (GRAM) Gram beta completa.
NO-GO (falsificador): desaparición uniforme de contactos en el cono lineal; constante exponencial ponderada
uniforme en N en cualquier cono de k; también para dos pesos centrados de amplitud fija.
OPEN: ∃C con W ≥ 0 para todos los numeradores y k ≥ CN o k ≥ CN². Positivo: BETA, MEAN, VAR, GRAM.

**7. POWER_LOGCONVEX_CURVATURE_AUDIT_101.md** — Auditoría de 101. APROBADO / PROVED para la clase
auxiliar. Reproduce coeficientes, inversa, concentración y margen −393/250 δ⁴. Alcance: refuta sólo
suficiencia genérica de convexidad fuerte + V″ logconvexa + signos de derivadas para triples; no es Φ real
ni W negativo; no refuta una clase invariante que incorpore los datos reales 077/089/099.

**8. POWER_LOGCONVEX_CURVATURE_OBSTRUCTION_101.md** — Potencial v=cosh t + 10^−4 cosh 10t, A=10^46,
tres nodos u_i = i·10^−4, vector (1,−2,1), núcleo K_M(U,W)=[M(U)+M(W)]/(U+W).
Etiqueta: PROVED (falsificador analítico de clase auxiliar). Resultado: c^t K_M c < −3δ⁴/(2A) < 0.
Contramodelo para la clase: V par, v″ ≥ 101/100, (log V″)″ > 0, todas las derivadas pares > 0, impares > 0
en t>0. Reapertura: sólo una clase que conserve los inputs reales de pares 077/089/099; no se justifica una
«sucesión de fortalecimientos genéricos» que los omita. Positivo reutilizable: ninguno de signo.

**9. POWER_LOW_TABLE_018.md** — Fila k=0, g_N; ERR: F_N = (2/c0)∫_0^∞ E0(e^t)e^{−t/2}[C_N/2−C_N′]dt con
E0 = ψ_Λ(x)−x+1. Etiqueta: PROVED fórmula del presupuesto; OPEN signo interior.
Resultado: con sólo |E0| ≤ A x^θ, presupuesto exacto D_N(θ)=2+2θ J_N(θ−½); D_N(0)=2; D_N(θ)→1/(½−θ)
(θ<½); D_N(½) ~ (√π/u)√N; para θ>½, D_N(θ)=Θ(√N[1−b²/u²]^−N) (crecimiento exponencial).
Resto: W[g_N]/c0 = ARCH_♯/c0 − F_N, límite C0+4<0: falta desigualdad aritmética FIRMADA sobre ERR.
Positivo: fórmula (ERR) con endpoint correcto y (D), para este test.

**10. POWER_MIXED_FOUR_CAUCHY_CLIP_AUDIT_109.md** — Auditoría del diseño 109 (intersección de coeficientes
con cotas de Cauchy |φ_k| ≤ 2^{40+k}, |J_k|,|K_k| ≤ 2^{42+k}). Diseño y literal APROBADOS; resultado final:
exit2 / INCONCLUSO por presupuesto (8192 evaluaciones REST), origen PASS 16/16, REST certificado sólo
[½, 2645/512]. Sin reproducción independiente de 109. Insuficiencia de encierro, no obstrucción.

**11. POWER_MIXED_FOUR_CAUCHY_CLIP_DESIGN_109.md** — Diseño 109 sobre el compacto del Wronskiano mixto
W_t(K,J,Φ,J″), 0<t<64. Etiqueta: CONSTRUCTOR TERMINADO exit2/INCONCLUSO. Mismo resultado que 10.
Condición: 110 se ejecuta sólo si 109 no da FULLPASS (cumplida). Ningún signo nuevo.

**12. POWER_MIXED_FOUR_COMPACT_AUDIT_107.md** — Auditoría del diseño 107. Diseño y literales APROBADOS;
ejecución fija INCONCLUSA reproducida: 11 evaluaciones, 0 hojas aceptadas, profundidad 10 en
λ∈[0,1/65536], determinante [±2.94e−3]; REST no arrancó. Fallo de encierro, no refutación. Reapertura:
otro objeto o representación, diseñado y auditado antes de correr; no reajustar profundidad/precisión.

**13. POWER_MIXED_FOUR_COMPACT_DESIGN_107.md** — Diseño del certificado compacto de W_t(K,J,Φ,J″)>0 en
(0,64): origen en λ=t² (polinomios de grado 512, 128 modos), REST con integrales normalizadas de 106 y
Gauss–Legendre 64. Etiqueta: DISEÑO AUDITADO; CORRIDA INCONCLUSA EN ORIGEN. Fórmulas reutilizables:
J_k=−φ_{k−1}/(2k), K_k=(aφ_{k−1}−J_{k−1})/(2k(2k−1)); W_t=64t⁶W_λ; cotas |φ|<2^40, |J|,|K|<2^42 en |λ|≤½.
Sugerencia registrada: formar el determinante como polinomio en λ antes de evaluar (ejecutada en 108).

**14. POWER_MIXED_FOUR_FACTORED_RATIO_AUDIT_110.md** — Auditoría del diseño 110. Diseño y literal
APROBADOS; corrida principal y reproducción independiente terminaron exit2/INCONCLUSIVE por 8192
evaluaciones, logs idénticos byte a byte; cobertura certificada: origen λ∈[0,¼] y REST [½, 845/32].
Actualización: con la cola analítica de 104 (t≥16) se declara **WM: W_t(K,J,Φ,J″)>0 para todo t>0**
(PROVED, computacional certificado + analítico) y se activan las implicaciones de 112. Global OPEN.

**15. POWER_MIXED_FOUR_FACTORED_RATIO_DESIGN_110.md** — Identidad exacta Θ16(y)=d(1+R16(y)), d=2y−3,
B_m=m⁴+3m²(m²−1)/d; cociente Θ16(y+v)/Θ16(y)=(1+2v/d)(1+R16(y+v))/(1+R16(y)); p16 = 2y−9/2−6/d−R_t/(1+R16).
Etiqueta y resultado: como en 14 (INCONCLUSO solo; WM activada junto con 104). Positivo reutilizable:
la factorización algebraica del cociente theta.

**16. POWER_MIXED_FOUR_ORIGIN_AUDIT_104.md** — Auditoría de 104. PROVED / aprobada; gate PASS
(Dmix>0) reproducido. Exterior analítico: W_mixto/Φ⁴ > 6t²/y² para t≥64, mejorado a **t≥16**.
Advertencia registrada: Dmix<0 habría descartado sólo Chebyshev4 global de esa familia; Dmix>0 sólo da
signo en una vecindad sin radio. Compacto intermedio OPEN en ese momento (cerrado después por 110).

**17. POWER_MIXED_FOUR_ORIGIN_DESIGN_104.md** — Sistema mixto [K,J,Φ,J″] (K par). Etiqueta: PROVED gate
puntual positivo y cola analítica. Resultados: W_t = 64Φ0⁴ t⁶[Dmix+O(t²)], Dmix>0 (intervalo racional
exterior, computacional certificado); modelo exterior W[a/P²,t/P,1,tP]=128a(6t²+4t−1)/P²; (POSITIVE-TAIL)
W_mixto(t)/Φ(t)⁴ > 6t²/y² > 0 para todo t ≥ 64, ampliado a t ≥ 16. Cotas holomorfas reutilizables del
strip (|p−2y|<6, |p′|≤5Y, Re p ≥ Y; |T1−1/p²|≤15/Y³; |K/Φ − a/p²| < (16+|z|)/Y³).

**18. POWER_MIXED_FOUR_POLYNOMIAL_AUDIT_108.md** — Auditoría de 108. Diseño y literal APROBADOS;
ejecución INCONCLUSA reproducida: grado 2042, 15 evaluaciones, 4 hojas, cobertura λ∈[0,141/8192], parada
en profundidad 10 con coeficiente central ya [±1.79e−4]. No falsificador ni obstrucción.

**19. POWER_MIXED_FOUR_POLYNOMIAL_DESIGN_108.md** — Determinante formado en el anillo de polinomios
intervalares en λ antes de evaluar; cota |det exacto − P| ≤ 96·2^−400·(2^62+1)³ < 2^−200; traslado de
Taylor exacto. Etiqueta: EJECUTADO / INCONCLUSO. Ningún signo nuevo.

**20. POWER_MIXED_NORMALIZED_INTEGRAL_106.md** — Integrales normalizadas holomorfas τ=J/Φ, κ=K/Φ en el
strip S={Re z ≥ −1/16, |Im z| ≤ 1/16}. Etiqueta: LEMA ANALÍTICO PROBADO; SIGNO GLOBAL OPEN.
Resultados: (ZERO-FREE) |Rθ|<1/4: Θ y Φ sin ceros en S; (NORMALIZED) τ=∫(z+r)A dv, κ=∫[ar−(z+r)r²/2]A dv
con factor e^{−v}; (COLUMN), (V-TAIL) < 2^−450, (MODE-TAIL) < 2^−698, (W-BOUND) 2^108,
(REGULARIZED-BOUND) 2^168; §8 (GAUSS-ERROR) 2^(−83+5j). Positivo reutilizable: todas estas cotas
(herramienta de evaluación, no de signo).

**21. POWER_MIXED_NORMALIZED_INTEGRAL_AUDIT_106.md** — Auditoría de 106 y §8. LEMA ANALÍTICO APROBADO,
sin ejecución. Confirma todas las cotas; advierte que el compacto, Chebyshev4 mixto, el cruce de U finito
y W global siguen OPEN (en ese momento).

**22. POWER_MIXED_VOLTERRA_AUDIT_105.md** — Auditoría de 105. Prueba y literal APROBADOS. Confirma la
identidad E w′ + (2−2qτ)w + X′S − Y′D = E y el cambio de signo del kernel bruto H(t,s)=R(t)−T(t)τ(s)
(H(t,t)<0 para t grande; H(t,s)→R(t)>0 si s→∞). Alcance: sólo positividad del kernel BRUTO.

**23. POWER_MIXED_VOLTERRA_OBSTRUCTION_105.md** — Ecuación (RAW-VOLTERRA) w′+Bw+∫_t^∞ H(t,s)w(s)ds = 1,
w = −S′, S = κ′/τ′. Etiqueta: PROVED analítico. NO-GO (clase: kernel Volterra bruto puntualmente no
negativo): [X′−τY′]/(tp) → −2, luego H cambia de signo para todo t grande. Reapertura explícita: otras
ecuaciones obtenidas por gauge, integración por partes, compensación, cambio de incógnita o reordenación
no quedan excluidas. Positivos auxiliares: τp/t → 1 (TAU-LIMIT); S(∞)=0; D=∫_t^∞ τw.

**24. POWER_MIXTURE_AUDIT_015.md** — Filtro H=(s+u)/(s+v), Q=s/(s+u). Etiqueta: PROVED identidades y
convergencia para u>1; sin signo de componentes. Resultados: (FIN) W[f_v]=R0Σ_{k≤K}a^kW[Q^k f0] +
a^{K+1}W[Q^{K+1}f_v]; (INF) W[f_v]=R0Σ_k a^k W[Q^k f0] absolutamente convergente (u>1); mezcla de todos
los polos nuevos con pesos w_k ≥ 0; Rayleigh_ARCH(Q^{k+1}f0) ≥ Rayleigh_ARCH(Q^k f0) (no para W).
Advertencia: para ½<u<√½ el multiplicador polar de Q tiene módulo >1. Obligación: W[Q^k f0] ≥ 0 para
todo k y todo P de grado <n transportaría el signo a todas las tasas ≥ u.

**25. POWER_MOVING_BALANCE_036.md** — Ley P_d(m) de 035, inclinaciones energéticas Q^P, Q^Π (polar y
módulo del peine real). Etiqueta: PROVED. Resultados: representación binomial (BETA)/(BINOMIAL);
(CONCENTRATION) M/d → 1/32 bajo ambas energías (no √N); (POLAR-DOM) factor 3969; (CHEB)
ψ_Λ(x) ≥ x/2 − 16 (prueba por binomial central); (PRIME-LOWER) Π_N ≥ P_N/2 − 33; log Π_N/N → log(3969/3968).
NO-GO de procedimiento: «la cola fuera de C√N tiene poca probabilidad, luego se omiten por separado polar y
peine» es falso. Reapertura: compensación firmada hecha ANTES de separar componentes, dentro de t_m.

**26. POWER_PACKET_SCOPE_AUDIT_009.md** — Familia f_n=(D²−¼)y^{n−1}e^{−uy}. Etiqueta: PROVED
concentración, identidades, re-auditoría del puente; OPEN desigualdad aritmética finita.
Resultados: E_n τ² = u²/(2n)(1+O(1/n)); W_n = Arch_n + e_n − 𝓕_n, umbral límite C0+4 (mismo centro E0
ya registrado); recurrencia J_{n+1} = −(2nu)^{−1}∂_u J_n; Arch_{n+1} − Arch_n = Cov(m,w)/E(w) ≤ 0.
Resto: W_{n+1}−W_n = (Arch) − Σ 2Λ(q)q^{−½}[ρ_{n+1}−ρ_n](log q), sin signo. Puente 002 re-auditado sin
defecto: positividad de TODOS los tamaños de la escalera 32+n bastaría; no aporta su signo.

**27. POWER_PAIR_OBSERVABLE_SCOPE_100.md** — Observable η = −K′/J de la pareja real. Etiqueta: PROVED.
Resultado: 0 < η(t) < a/t para t>0 (POINTWISE), η(0)=0: η no es monótona en ningún sentido;
E_{J,u}[η] = a/M(u) − 1/u, h(u²) = u/E_{J,u}[η]. NO-GO: usar esta η en una clase de comparación de dos
copias que EXIJA observable creciente (extensión de 073). Abierto: comparaciones que admitan ascenso y
descenso, otras observables o parejas.

**28. POWER_PAIR_OBSERVABLE_SCOPE_AUDIT_100.md** — Auditoría de 100. APROBADO. Confirma −K′>0, la cota
a/t y la identidad de medias; atribuye a 081 la no monotonía de F(u); alcance acotado a la clase que exige
monotonía.

**29. POWER_PARTICULAR_ORIGIN_AUDIT_093.md** — Auditoría de 093. APROBADO; corrida y reproducción
FULL PASS 128 paneles; NUM<0, Dpart ≈ −21658.198 (encierro estricto). Alcance: signo cerca de 0 sin radio;
no signo global del Wronskiano particular ni invariancia de cono.

**30. POWER_PARTICULAR_ORIGIN_DESIGN_093.md** — Wronskiano particular W(w,v,w″,K), w=tΦ, v=−Φ′,
K″ = v − cw, c=1/a, K impar con K(0)=K(∞)=0; W = 64Φ0⁴t^10[Dpart + O(t²)], Dpart = Pκ + Qc + R (fórmulas
explícitas de P,Q,R en a_1..a_4). Etiqueta: PROVED PUNTUAL (computacional certificado).
Resultado: Dpart < 0, luego W_t(w,v,w″,K) < 0 para t>0 pequeño (signo requerido, verificado localmente).
Intervalos certificados de I0, I1, I2, a, τ0 reutilizables.

**31. POWER_PARTICULAR_TAIL_095.md** — Misma familia particular. Etiqueta: PROVED analítico.
Resultado: (TAIL-PARTICULAR) W_t(tΦ, −Φ′, (tΦ)″, K) < 0 para todo t ≥ 64, con modelo
W[t,q,tq²,1/q] = −128q²(6t²+4t−1) y resto C t³y0, C<2^98. Cotas holomorfas (COMPLEX) en Re z ≥ 3:
|p−2y|<6, |p′| ≤ 5Y, Re p ≥ Y; (IBP-REM) |K/Φ − 1/p| < (6+25|z|)/Y². Intervalo intermedio OPEN en la fuente.

**32. POWER_PARTICULAR_TAIL_AUDIT_095.md** — Auditoría de 095. APROBADO / PROVED para t ≥ 64.
Reproduce el determinante modelo y los 7 términos multilineales; precisa que 093 (vecindad de 0) y 095
(t ≥ 64) no se unen como cobertura de todo t>0.

**33. POWER_PEANO_MONOTONICITY_AUDIT_091.md** — Auditoría de 091. APROBADO / PROVED en la clase
declarada. Confirma REAL-W3 = w³(B′)²J > 0, cofactores ε³W3(−1,3,−3,1) y los dos prefijos de signos
opuestos. Signo de la integral Peano, menor anclado y T_h real: OPEN en ese momento.

**34. POWER_PEANO_MONOTONICITY_OBSTRUCTION_091.md** — det[w,v,w″,K] en cuatro nodos = ∫_0^∞ sζ(s)
[Π(s)/s − Π(b)/b]ds (PEANO), ζ = v − w/a, Π = Σ ℓ_i (s−t_i)_+. Etiqueta: PROVED.
NO-GO (clase: monotonía global de Π(s)/s para todos los conjuntos de cuatro nodos): para nodos
equiespaciados cerca de cualquier t0>0, Π/s decrece en (t1,t2) y crece en (t2,t3).
Reapertura: compensación entre intervalos, comparación con posición/masa del cruce b, o kernel distinto.
Positivo: (REAL-W3) W(w,v,w″) = w³(B′)²J > 0 para todo t>0; ∫_0^∞ sζ = 0, cruce único de ζ.

**35. POWER_POLAR_MOVEMENT_005.md** — Movimiento de polos con polar: (F) E_new − E_old =
[Cov_μ(m,R) + (r0 − E_μR)P_old]/E_μR. Etiqueta: PROVED (identidades, sector, falsificador, orden uno alto,
derivada orden 4); OPEN transporte global orden 4. Resultados: sector P_old ≤ 0 se transporta; falsificador:
E(2) − E(1) = 4/5 − π < 0 en orden uno (refuta «arch+polar crece al aumentar polos» en general); orden uno con
u ≥ 8 PROVED; (D4) identidad cuártica; certificado SOS racional: dE/dv_j > 1/420 en (u,u,u,u), u=63/2,
para todo numerador de grado <4 (computacional certificado, Fraction). Resto: dominar (E_μR − r0)P_old por
la covarianza cuando P_old > 0; una cota absoluta del polar no basta.

**36. POWER_POLE_MOVEMENT_004.md** — Rayleigh_v(P) − Rayleigh_u(P) = Cov_μ(m,R)/E_μR ≥ 0. Etiqueta:
PROVED (CITED el certificado confluente 004). Resultados: (PM) todas las eigenenergías arquimedianas
comprimidas crecen al aumentar individualmente polos; (WT) ‖e^{uy/2}f‖² ≤ B_n‖f‖², B_n=(25^n−1)/12;
peine ≤ 3/1000, polar ≥ −21/500 para n=3; Q[Σ c_i X^{−a_i}] ≥ ‖f‖²/20 para TODAS las ternas de exponentes
≥ 32. Límite: B_n crece como 25^n y la menor eigenenergía confluente baja con n; no hay uniformidad en n.

**37. POWER_POLYNOMIAL_003.md** — h = e^{−63y/2}P(e^{−y}), z=e^{−y}, ⟨P,Q⟩_J = ∫_0^1 z^62 PQ,
D_nP(z)=P(z/n). Etiqueta: PROVED identidades; OPEN signo uniforme. Resultados: (C) Comb = −2Σ Λ(n)n^−32
⟨P,D_nP⟩_J; (P) polar con momentos z^30, z^31; (A) matriz arquimediana; base Jacobi por Rodrigues con
normas y momentos racionales; D_n triangular, no autoadjunto (no se puede sustituir por contracción
positiva). Objetivo no logrado: estimación en la base e_j que controle C+P frente a A conservando la
triangularidad de D_n.

**38. POWER_POST013_CONSTRAINTS_014.md** — Auditoría de alcance (no cierra rutas). Precisa: prop:opcalc
cubre identidades de convolución, no excluye desigualdades que conserven medida espectral restringida,
términos positivos o acoplamiento exacto con el polar. Registra: WITNESS006 (dimensión 12) da AP negativa y
signo negativo si se borra SÓLO el contacto 2 — todo teorema válido tras ese borrado no da (★).
Blanco suficiente: semidefinitud de TODOS los bloques Laguerre a una sola tasa (CONFLUENT_BRIDGE_014).
Una sola cadena escalar f_n o una unión de espacios pequeños no hereda esa suficiencia.

**39. POWER_PRIMAL_AUDIT_045.md** — Auditoría de CONTACT_FLOOR045 y PRIMAL_PAIR045. APROBADOS, PASS.
Floor crudo m(240) − A_{2345} < −0.5: falla sólo ese criterio de corte 240. Corrección documental: el
mayor extremo PROVED localizado en el pipeline local de certificados es T = 207/200 (logs certified:true
μ = 2·10^−26); para T ≈ 1.098 no hay log de certificación final. Condiciones L55-B: par representante
positivo explícito en TODO el portador primitivo, con slack controlado y coincidencia aritmética in-band.

**40. POWER_PRIMAL_PAIR_045.md** — Par representante (μ, ν) con ARCH + ε‖F‖² = ∫Φ_F dμ + ∫c_F dν y
ν|(−2T,2T) = ν_Λ, en T = 3/5 (contactos 2, 3). Etiqueta: PROVED. Lema de rigidez: si η = μ − (q_T+ε)dτ
es medida par compacta, η = 0. Falsificador: q_T(0) < −15/2, luego no existe par de cola fija con
corrección compacta y ε ≤ 15/2. Subcaso no compacto (r par templada, resto exterior medida finita par)
coincide EXACTAMENTE con un certificado del programa dual (D) de Paper 47. Reapertura: correcciones no
compactas fuera de ese subcaso (medidas singulares, distribuciones). El contacto 4 no se añade como
reparación compacta.

**41. POWER_PRIME_AUDIT_014.md** — Auditoría de PRIME_TRANSFER014. PROVED identidades y falsificador
universal de E2; OPEN desigualdades restringidas. Confirma la identidad exacta W[f_v] − R0W[f0] =
(1−R0)W[G], G = sF0/(s+v); el contraejemplo sólo prueba E2[G] < 0, no W[G] < 0. R12 basta para el primer
movimiento, no para una secuencia sin hipótesis en espacios intermedios.

**42. POWER_PRIME_BALANCE_033.md** — Peine normalizado Σ Λ(q)w(q), w(q)=2q^−½C″_{N+1}(log q)/‖f_{N,1}‖²,
en REGION (u ≥ 63/2, 3 ≤ N ≤ 2u²/9 − u/3 + 3/2). Etiqueta: PROVED. Resultados: (DECAY) w(mq) ≤ m^−2 w(q),
q ≥ 5; operador D f(q) = Σ_{m≥2} f(mq) con 0 ≤ D^j w ≤ ρ0^j w, ρ0 = 2389/3600; b(n) = log n −
log2·1_{2|n} − log3·1_{3|n} − log2·1_{4|n} ≥ 0; (BRACKET) para K impar S_K ≤ A(w) ≤ S_K + ρ0^{K+1}L(w);
(FULL) B_N + S_K ≤ W/‖·‖² ≤ B_N + S_K + ρ0^{K+1}L(w). OPEN: B_N(u) + S_K > 0 en un rango nuevo.

**43. POWER_PRIME_PATTERN_FALSIFIER_008.md** — f = (d²/dy² − ¼)y^{n−1}e^{−uy}, n = 2^17, polar nulo.
Etiqueta: PROVED. Resultados: E_f τ² < 1/100; Arch/‖f‖² < −383/100; cada contacto q ≤ 1024 aporta
< −Λ(q)q^−½‖f‖² (todos perjudican). NO-GO del patrón universal «los contactos bajos siempre reparan las
direcciones arch+polar negativas» en la familia confluente fija. Obligación (TAIL): el segmento q > 1024
debe superar 383/100 + Σ_{q≤1024} Λ(q)q^−½. No se afirma W[f] < 0.

**44. POWER_PRIME_TRANSFER_014.md** — Filtro de un polo. Etiqueta: PROVED identidades y falsificador;
OPEN transporte restringido a V12. Resultados: (C) c_{f_v} − R0c_{f0} = (1−R0)[c_{f0} − P_v∗c_{f0}] con
núcleo δ − P_v de masa cero; (T2) identidad acoplada ARCH+contacto2+POLAR; (GAIN) W[f_v] − R0W[f0] =
(1−R0)W[G]. Falsificador: E2[f_v] < (u²/v²)E2[f0] para el test Tate de orden 2^17 y v = 65/2.
Ruta declarada: desigualdad firmada para W sobre correcciones G_j de numerador divisible por s, con TODOS
los contactos; condición R12 (resuelta después en 049 para el primer paso).

**45. POWER_QUADRATIC_017.md** — Cono k ≥ max(cN², 4N), P=1. Etiqueta: PROVED. Resultados: (STRIP),
(CORR) |R_{N,k}(t)| ≤ C(c)e^{−|t|} desplazando la densidad (no las normas); (PRIME) |Comb| ≤ 14C(c)‖f‖²;
teorema de signo eventual: W[f_{N,k}] > 0 para N ≥ N0(c), k ≥ cN²; (GAUSS) y (PROFILE)
W/‖f‖² = ½log N + log[u√c/(2π)] − 2ΣΛ(q)q^−½ e^{−u²c(log q)²/8}cos(μ_N log q) + o(1); apéndice:
m(τ) ≥ log(|τ|/2π) − 4. Límite: sólo P=1; no primeras dimensiones; la serie de PROFILE no tiene signo probado.

**46. POWER_QUADRATIC_EXPLICIT_017.md** — Mismo objeto con banda Im z = 15. Etiqueta: PROVED.
Resultado: para N ≥ 2, k ≥ 10000N²: |c_f(t)|/‖f‖² < 5e^{−15|t|} (CORR15) y W[f] > (49/50)‖f‖² (CONE),
todos los contactos incluidos. Límite: sólo P = 1; no k < 10000N².

**47. POWER_QUADRATIC_EXPLICIT_AUDIT_017.md** — Auditoría de 46. APROBADO, PROVED, verificador PASS.
Confirma cada constante y dirección de desigualdad; también re-audita QUADRATIC017 sin defectos.

**48. POWER_R12_AUDIT_048.md** — Auditoría de ENDPOINT048. APROBADO el extremo y el complemento polar;
OPEN R12 uniforme (en ese momento). Confirma E2[G] > ‖G‖²/50 en V13 ∩ {G(0)=0} y |Polar[Q^jF]|/M_j ≤
(9/62)^j|Polar[F]|/M_0. Continuidad da sólo un entorno sin radio efectivo.

**49. POWER_R12_AUDIT_049.md** — Auditoría de CENTERED_CUTOFF049 (fuera del rango) y R12_TRANSPORT049.
APROBADOS; certificado finito PASS para j = 1..13. Corte analítico: E(τ^−2) < 1/405 y ARCH > 859/800 para
todo j ≥ 14. Resuelve R12 en el primer movimiento desde V12 con c = 1/2500; no W completo ni iteración.

**50. POWER_R12_ENDPOINT_048.md** — Extremo v=u de R12. Etiqueta: certificado racional del extremo;
OPEN R12 uniforme (en la fuente). Resultado: (ENDPOINT) E2[G] > (1/50)‖G‖² para G ∈ V13, G(0)=0
(computacional certificado, LDL racional). Complemento: compresión de q tridiagonal, ⟨qF,F⟩ ≥ ‖F‖²/576,
M_j ≥ 576^−j M_0, Polar[Q^jF] = (−1/3968)^j Polar[F].

**51. POWER_R12_TRANSPORT_049.md** — Etiqueta: PROVED. Resultado: (R12-PROVED) E2[G_v] > (1/2500)‖G_v‖²
para todo F ∈ V12∖{0} y todo v ≥ u, G_v = sF/(s+v) (FINITE j=1..13 computacional + TAIL j ≥ 14 analítico +
mezcla MIX). Consecuencia: (E2 − c‖·‖²)[f_v] ≥ (u²/v²)(E2 − c‖·‖²)[F]. Resto: contactos q ≥ 3 sobre el
espacio desplazado no acotados; iteración a bases intermedias no probada.

**52. POWER_REAL_PAIR_DOUBLE_LIMIT_103.md** — Pareja (D_p, Ψ_p), siguiente paso E = G_q(dA − qB),
U = B − γE. Etiqueta: PROVED analítico + test puntual NEGATIVO; criterio §11 CONDITIONAL. Resultados:
(PAIR-LIMIT) pD_p → J, (ap/c)Ψ_p → K; U_lim(0) < 0 (computacional certificado; luego redundante);
(H-RATIO) (H/K)′ < 0; (ALL-Q-RATIO) (E_q/K)′ < 0 y Ξ_q > 0 para todo q > 0 en la pareja límite;
(FINITE-BRIDGE) βD_p + p²Ψ_p = λK, Ψ_p = (λ/p)E_p, (Ψ_p/K)′ < 0, (D_p/K)′ > 0 para todo p finito;
(MIXED-FORCING); §11.4: [K,Φ,J] Chebyshev3, S′ < 0 (MIXED-CONVEXITY), tres primeros Wronskianos de
[K,J,Φ,J″] positivos. Pendiente en la fuente: cuarto Wronskiano (cerrado después por 104+110).

**53. POWER_REAL_PAIR_DOUBLE_LIMIT_AUDIT_103.md** — Auditoría de 103 y sus ampliaciones. PROVED /
APROBADA; FULLPASS reproducido. Confirma el orden iterado de límites (p→∞ luego q→0), que la convergencia
en compactos NO transfiere el conteo global de raíces a p finito, y que Chebyshev4 mixto no se deduce de EVEN4.

**54. POWER_REAL_PAIR_LIMIT_ORIGIN_DESIGN_103.md** — Test P = 720I0²(K0Hmass − Kmass H0) (polinomio
homogéneo de grado 4 en I0..I6). Etiqueta: DISEÑO FIJO ejecutado; resultado NEGATIVO reproducido:
P ∈ [−3.168e−13 ± 2.2e−30]. Verifica una condición necesaria; no falsificador.

**55. POWER_REAL_PAIR_MONOTONICITY_102.md** — Etiqueta: PROVED analítico (usa 075/077/078/089).
Resultados: lemas de Rolle con multiplicidades y bordes (un extremo, D2, Lp, GAIN); (K-RATIO) (K/J)′ < 0;
(EVEN4) [J,Φ,J″,Φ″] Chebyshev de dimensión 4; (PAIR-RATIO) (Ψ_p/D_p)′ < 0 para todos p,t > 0; §8:
(NEXT-DENSITY) E > 0, (NEXT-TRANSFORM), (NEXT-RESIDUE) r_q > 0; complemento con 099: R_next(z) > 0 para
todos p,q,z > 0. Pendiente en la fuente: cruce de U = B − γE (cerrado después en 112 bajo WM).

**56. POWER_REAL_PAIR_MONOTONICITY_AUDIT_102.md** — Auditoría de 102 y §8. APROBADO / PROVED para Φ
real y todos p,t > 0. Precisa que el nodo 0 de las congruencias es auxiliar, no generador admisible de W.

**57. POWER_REAL_SECOND_PAIR_AND_TP2_112.md** — Bajo WM (activada por 110+104). Etiqueta en cabecera:
implicaciones activadas, global OPEN. Resultados: (SECOND-POSITIVE) U tiene un único cruce −/+ y Ξ > 0
para todos p,q > 0; (SECOND-RATIO) (E_{p,q}/Ψ_p)′ < 0; (DIVIDED-GREEN) E_{p,q} = η(Ψ_p − Ψ_q)/(q²−p²);
(STRICT-TP2) para V(x,t)=Ψ_{√x}(t); (STRICT-CONFLUENT) ∂_t∂_x log V > 0; §8 (STAR-RATIO), (ZERO-STAR-RATIO).
Resto: para la pareja finita, Ξ_{p,q}/E_{p,q} decreciente exige la familia de cinco funciones
[K,J,Φ,J″,Φ″] (aparece Φ″ en la fuerza); no TP3, no todos los órdenes.

**58. POWER_REAL_SECOND_PAIR_AND_TP2_AUDIT_112.md** — Auditoría de 112. APROBADA la implicación; aplicación
real activada por la actualización WM. Confirma que TP2 no se deduce de monotonías individuales (111) y que
la siguiente fuerza contiene Φ″ con coeficiente −raC: no se repite ECT4 mixto automáticamente.

**59. POWER_REASSESSMENT.md** — Revisión estratégica. Signo global OPEN. Antecedente explícito:
M(u) = L(u+½) y K_M es la misma función generadora del corpus (R162_803 Theorem H, D-16 del crucigrama).
Balance: puentes en norma; cuatro potencias arbitrarias con exponentes > 1; trece con exponentes ≥ 32;
WM y consecuencias 112; ninguna ventana T nueva (certificado asistido 207/200 se mantiene). Regla
operativa: no lanzar otro certificado de orden superior; antes de construir, escribir qué propiedad
controla simultáneamente todos los tamaños, cómo se prueba sin asumir el signo y qué hipótesis evita la
obstrucción del antecedente.

**60. POWER_RECIPROCAL_PFAFFIANS_083.md** — K_ij = (F_i+F_j)/(u_i+u_j), R = u/F, S = uF.
Etiqueta: PROVED como identidad algebraica; apéndice: identidades y criterio suficiente PROVED, descarga
real CONDITIONAL/OPEN. Resultado: (ALL-ORDERS) det K = P_n(A_R)P_n(A_S)/∏R_i (Pfaffianos bordeados en
orden impar); (INTERPOLATION-EVEN/ODD); jerarquía Rolle D_{k,j}; (TAYLOR-HANKEL). Obligación:
P_n(A_R)P_n(A_S) ≥ 0 para todos los subconjuntos principales y todo n; condición suficiente no verificada:
μ_m = (−1)^m a_{m+1} sucesión de momentos con menores desplazados positivos, para R y S.

**61. POWER_RECIPROCAL_PFAFFIANS_AUDIT_083.md** — Auditoría de 083. APROBADO / PROVED identidad.
Precisa: un determinante total positivo no basta para PSD; signos de Pfaffianos en orden arbitrario no
probados; la positividad de J/K no da la condición de momentos.

**62. POWER_RECIPROCAL_SECANT_CONCAVITY_090.md** — Etiqueta: PROVED (lema; aplicación theta con input
089). Resultados: (SECANT-CONCAVITY) f′ > 0, T_f = 2f′f‴ − 3f″² > 0 ⇒ x/(f(x)−f(0)) estrictamente cóncava
(también con ancla interior, ambas orientaciones); h″ < 0 global; pares de G_p PD; (ONE-REST-CURVATURE)
S_G″ < 0 para todos p,x > 0; (ANCHORED-FIVE) W(x,x²,G,xG) = −a²G⁴T_h. NO-GO (§9, falsificador explícito
w = (5−e^{−x})/4): T_f > 0 global no implica T_H > 0, T_H(0) = −1/192. T_h real: cerrado después por 099
según la actualización de cabecera; herencia al nivel siguiente abierta.

**63. POWER_RECIPROCAL_SECANT_CONCAVITY_AUDIT_090.md** — Auditoría de 090 y apéndices. APROBADO.
Confirma el lema, la promoción a PROVED tras 089 FULL PASS, S_G″ < 0, ANCHORED-FIVE y el falsificador de
herencia genérica (sólo esa promoción automática).

**64. POWER_RECIPROCAL_SECANTS_082.md** — Etiqueta: PROVED como criterio algebraico. Resultado: bajo pares
estrictamente PD, todos los triples de K_F son PSD ⟺ R y S cóncavas en x = u²; (DET2), (RECIPROCAL),
(DET3) det K_F = Vandermonde²/(H1H2H3)·R[u²,v²,w²]S[u²,v²,w²]. Admite F no monótona. Pendiente en la fuente:
descarga para G_p y preservación por Schur.

**65. POWER_RECIPROCAL_SECANTS_AUDIT_082.md** — Auditoría de 082. APROBADO / PROVED. Confirma que δ_R,
δ_S no pueden ser ambos negativos y que el criterio es exacto de orden 3, no un patrón para orden 4.

**66. POWER_RECURRENCE_BOUNDARY_036.md** — Recurrencia A_{N,k} = (α/S)A_{N,k+1} + (β/S)A_{N+1,k}.
Etiqueta: PROVED. Resultados: (FRONT) identidad finita de frontera con pesos beta-binomiales; (INV)
E[1/(N+J−3/2)] = (S−1)/[(N−3/2)(S+L−1)]; (ARCH-UP); (ENERGY) energía del cono 017 en la frontera
diagonal = O(log L/√L) → 0; (REMAINDER) R_L → A_{N,k}; (STOP-WEIGHT); (SURVIVAL) masa que nunca toca el
cono > 0. Resto exacto: R_L. Condición suficiente: R_L ≥ −ε_L con ε_L → 0 (estimación aritmética real);
no se declara vía nueva. No excluye otras fronteras con control de energía.

---

## A. Lista deduplicada «no relanzar» y cotejo con RULES_AVOID.md

Formato: ítem — fuente — condición de reapertura — estado en `RULES_AVOID.md`.

A1. Presupuestos absolutos |ψ−x| ≤ A x^θ como paso decisivo en la fila k=0 — 018 — sólo con desigualdad
aritmética FIRMADA sobre ERR que compense C0+4. **Presente de forma genérica** (B2: «Incluye cotas en valor
absoluto de ψ(y) − y»); falta la cuantificación: «D_N(θ) crece exponencialmente en N para θ > ½ y como √N
en θ = ½».

A2. Desaparición uniforme de contactos en el cono lineal; constante exponencial ponderada uniforme en N
(también centrada, amplitud fija) — 016 — reapertura: pesos con η dependiente de N o cancelación en vez de
valores absolutos. **Ausente.**

A3. Omitir por separado polar y peine en la cola de la ley de masa P_d — 036 MOVING — sólo compensación
firmada ANTES de separar, en la banda m ~ N/32. **Ausente.**

A4. Recurrencia/frontera diagonal sola — 036 RECURRENCE — sólo con R_L ≥ −ε_L. **Presente y exacto** (D4:
«Recurrencia o descenso solos — sólo con una cota aritmética firmada del resto R_L ≥ −ε_L»).

A5. Ordenación universal E2[f_v] ≥ R0E2[f0] — 014 — sólo sobre base restringida positiva (R12, resuelta
para el primer paso). **Ausente.**

A6. «Los contactos bajos siempre reparan las direcciones arch+polar negativas» — 008 — sin reapertura;
la obligación es (TAIL) con la cola completa. **Ausente** (B8 «patrón de observables» es otra cosa).

A7. «Arch+polar crece al aumentar polos» en general; cota absoluta |polar| en orden 4 — 005 — sólo con
hipótesis de rango y dimensión, conservando P_old > 0 con la covarianza. **Ausente.**

A8. Positividad puntual del inverso Möbius h_N ≥ 0 para todos N,x — 022 audit — falsificado; reapertura no
indicada. **Ausente.** D7 de RULES_AVOID («Variantes del presupuesto 022 — sólo si pagan también ARCH_♯ y
justifican su alcance en k») es coherente con 025/027 (falta comparar con ARCH_♯), pero no menciona este
falsificador puntual.

A9. Par representante con corrección espectral compacta y cola fija — 045 — reapertura: correcciones no
compactas fuera del subcaso que regresa a (D). **Ausente.**

A10. Kernel Volterra bruto H(t,s) = R(t) − T(t)τ(s) tratado como positivo — 105 — reapertura: gauge, IBP,
cambio de incógnita o reordenación. **Ausente.**

A11. Monotonía global de Π(s)/s (Peano) para todos los nodos — 091 — reapertura: compensación entre
intervalos o comparación con el cruce. **Ausente.**

A12. Fortalecimientos genéricos de hipótesis del potencial (convexidad fuerte, V″ logconvexa, signos de
derivadas) como suficientes para triples — 101 (y 074) — sólo una clase que conserve los inputs reales
077/089/099. **Ausente.**

A13. Observable η = −K′/J en clases que exigen observable creciente — 100 — reapertura: comparaciones con
ascenso y descenso. **Ausente.**

A14. Herencia genérica T_f > 0 ⇒ T_H > 0 bajo H = x/(f − f0) — 090 §9 — falsificado; T_h real exige dato
específico (menor anclado de cinco columnas). **Ausente.** D5 («Monotonías Schur–Green — sólo con un
invariante conjunto distinto conservado por cada operación») cubre el espíritu, no este falsificador.

A15. Transferir conteos globales de raíces de p → ∞ a p finito por convergencia en compactos — 103 —
falsable sólo con control uniforme de colas; resuelto después por vía distinta (WM). **Ausente.**

A16. TP2 deducida de monotonías individuales — 111 (citado en 112) — **Ausente.**

A17. Repetir certificados intervalares reajustando profundidad, precisión o presupuesto tras ver datos —
107–110 — sólo un objeto o representación nuevos, auditados antes de correr. **Presente parcialmente**
(D2: «Añadir dimensiones de filtro, optimizar umbrales, extender la torre de órdenes finitos»; la regla
operativa de REASSESSMENT «no lanzar otro certificado de orden superior» no está citada).

A18. Convexidad global del funcional gaussiano completo — 027 audit — falsificada (curvatura negativa para
v ≥ 65536). **Ausente.**

A19. Comparar sólo AP para todos los grados; teoremas válidos tras borrar sólo el contacto 2 — 014 POST
(WITNESS006) — reapertura: uso exacto de pesos que distinga ese borrado. **Presente genéricamente** (B5,
E «borrado finito»), sin la mención «borrado exclusivo del contacto 2».

A20. Cancelación conjunta de Pfaffianos usando sólo reciprocidad — 083 — **Presente y exacto** (D16,
memoria de las reglas del proyecto): «Expandir emparejamientos y volver a usar sólo reciprocidad no aporta mecanismo
nuevo». La fuente añade la condición suficiente concreta (sucesión de momentos de Taylor para R y S) que
RULES_AVOID no recoge.

A21. Bridge: reconstruir el puente de densidad — 002/009 — **Presente y exacto** (D1).

Inexactitudes detectadas: ninguna afirmación de RULES_AVOID contradice estos archivos. Dos puntos de
precisión: (i) C5 «positividad total de orden ≤ 4 (PF₄ ABIERTO)» y C1 «positividad total de orden ≥ 5»
se refieren a otro núcleo; 112 prueba STRICT-TP2 para la familia V(x,t) = Ψ_{√x}(t), que no debe leerse
como avance en ese PF₄; (ii) D7 cita «presupuesto 022» sin distinguir el inverso INTERIOR 022 de este
tramo, cuya conclusión es un falsificador puntual, no un presupuesto.

## B. Resultados positivos PROVED con alcance exacto

B1. 020 OUTER/RANGE (todo N, log x ≥ (N−1)/30) y ROW2 (N = 2, todo x ≥ 1): inverso Möbius completo del
kernel gamma a u = 63/2.
B2. 025 LC: log(33P_N − P_N′) cóncava para todo N ≥ 2; CUT general; K_129 > 0 en x ≥ 2; ERR_129 < −33/50
(computacional certificado en la celda n = 2).
B3. 027: JOINT-TAIL (N = 129, T = 4096, 0 < R < 10^−36) y JOINT-GAP (identidad exacta).
B4. 016: BETA, MEAN, VAR, GRAM (fórmulas exactas para f_{N,k}).
B5. 015: FIN (u > 1/2), INF (u > 1), mezcla de polos; monotonía de Rayleigh_ARCH bajo Q.
B6. 017: signo eventual W[f_{N,k}] > 0, N ≥ N0(c), k ≥ cN², P = 1; 017 explícito: W > (49/50)‖f‖² para
N ≥ 2, k ≥ 10000N², P = 1; m(τ) ≥ log(|τ|/2π) − 4.
B7. 018: fórmula ERR con endpoint y presupuesto D_N(θ) con sus tres regímenes.
B8. 004: PM (todas las eigenenergías arquimedianas al mover polos); WT; Q ≥ ‖f‖²/20 en todas las ternas
de exponentes ≥ 32 (usa certificado confluente 004, CITED).
B9. 005: identidad (F); sector P_old ≤ 0; orden uno u ≥ 8; dE/dv_j > 1/420 en el punto confluente
u = 63/2, grado < 4 (SOS racional), con vecindad sin radio.
B10. 003: coordenadas Jacobi exactas (C), (P), (A), (D).
B11. 033: DECAY, CONTRACT, BRACKET, FULL, MAGNITUDE en REGION.
B12. 036 MOVING: CONCENTRATION, POLAR-DOM, PRIME-DOM, CHEB ψ_Λ(x) ≥ x/2 − 16, PRIME-LOWER.
B13. 036 RECURRENCE: FRONT, INV, ARCH-UP, ENERGY, REMAINDER, STOP-WEIGHT, SURVIVAL (u = 63/2, N ≥ 18
para la parte de frontera; N ≥ 2 para ARCH-UP).
B14. 045: lema de rigidez de medidas compactas pares; q_{3/5}(0) < −15/2; identificación del subcaso no
compacto con (D).
B15. 048 ENDPOINT (E2 > ‖·‖²/50 en V13 ∩ {G(0)=0}); resto polar (9/62)^j de la órbita Q^jV12.
B16. 049 R12-PROVED: E2[G_v] > ‖G_v‖²/2500, F ∈ V12, todo v ≥ u (E2 = ARCH+POLAR+contacto 2 únicamente).
B17. 082 criterio exacto de orden 3 (DET2, DET3); 083 ALL-ORDERS (identidad), INTERPOLATION, TAYLOR-HANKEL.
B18. 090 SECANT-CONCAVITY (con ancla interior); h″ < 0; pares de G_p PD; S_G″ < 0 para todo p; ANCHORED-FIVE.
B19. 091 REAL-W3 > 0. 093 Dpart < 0 (vecindad de 0). 095 W_part < 0 para t ≥ 64. 100 0 < η < a/t.
B20. 102: lemas de Rolle; K-RATIO; EVEN4 Chebyshev4; PAIR-RATIO; NEXT-DENSITY; R_next > 0 (todos p,q,z).
B21. 103: PAIR-LIMIT; H-RATIO; ALL-Q-RATIO y Ξ_q > 0 (pareja límite, todo q > 0); FINITE-BRIDGE;
FINITE-RATIOS; Chebyshev3 de [K,Φ,J]; MIXED-CONVEXITY.
B22. 104 + 110: **WM, W_t(K,J,Φ,J″) > 0 para todo t > 0** (analítico para t ≥ 16; computacional
certificado y reproducido en [0, 845/32]); 106 lemas holomorfos de evaluación.
B23. 112 (bajo WM, activado): SECOND-POSITIVE, SECOND-RATIO, DIVIDED-GREEN, STRICT-TP2, STRICT-CONFLUENT,
STAR-RATIO, ZERO-STAR-RATIO.
Ninguno de B1–B23 es una cota inferior de λ_A(T) en una ventana nueva.

## C. Obligaciones OPEN (enunciado preciso y lo intentado)

C1. ∃C: W[f] ≥ 0 para todo f = P(s)/(s+u)^{N+k}·s^k con deg P < N y k ≥ CN (o CN²). Intentado: escala beta,
PACKET, pesos uniformes (falsificados), banda analítica (sólo P = 1).
C2. W[g_N] ≥ 0 para todo N, i.e. F_N ≤ ARCH_♯[g_N]/c0 con límite C0 + 4 < 0. Intentado: presupuestos
absolutos (018), inversos Möbius 020–025, balance celular (ERR_129 < −33/50), cola conjunta 027.
C3. Signo de ∫_1^{4096} K_129(x)Ω(x)dx (interior de N = 129) y de ∫_1^{X_N} h_N B (020 LOCAL).
C4. (TAIL de 008): −Σ_{q>1024} 2Λ(q)q^{−½}c_f(log q)/‖f‖² > 383/100 + Σ_{q≤1024}Λ(q)q^{−½}.
C5. R_L ≥ −ε_L, ε_L → 0, en la frontera diagonal (036); cancelación en t_m en la banda m ~ N/32.
C6. B_N(u) + S_K > 0 en REGION para un rango nuevo (033).
C7. W[G_j] ≥ 0 (o W − c‖·‖² ≥ 0) sobre correcciones G de numerador divisible por s, con TODOS los
contactos y en todos los órdenes (014 GAIN); extensión de R12 a bases intermedias; contactos q ≥ 3 sobre
el espacio desplazado de V12 (049).
C8. Orden 4: transporte de signo cuando P_old > 0, dominando (E_μR − r0)P_old por Cov_μ(m,R) (005).
C9. W[Q^k f0] ≥ 0 para todo k y todo P de grado < n (015); positividad uniforme en n de ternas de 004.
C10. PSD de K_ij = (L(32+i) + L(32+j))/(63+i+j) para todo m (puente 002, re-auditado en 009).
C11. P_n(A_R)P_n(A_S) ≥ 0 para todos los subconjuntos y todo n (083); o la condición de momentos de Taylor
para R y S.
C12. Ξ_{p,q}/E_{p,q} decreciente para p,q finitos: requiere una comparación para [K,J,Φ,J″,Φ″] o para
sus coeficientes restringidos (112 §7); conservación indefinida; TP3.
C13. Signo de la integral PEANO (091) — pendiente en la fuente; T_h real resuelto después según 090.
C14. W_{n+1} − W_n con signo para la familia Tate racional (009).
C15. Par representante positivo L55-B en todo el portador primitivo (045).
C16. Estimación en la base Jacobi e_j que controle C + P frente a A conservando la triangularidad de D_n (003).

## D. Objetos o ideas mencionados como no iniciados o no examinados

D1. Cono cuadrático para TODOS los numeradores (control conjunto del factor polinomial complejo y de su
Gram) — 017, 017 explícito.
D2. Pesos centrados con η dependiente de N; análisis por cancelación en lugar de valores absolutos — 016.
D3. Compensación firmada dentro de t_m antes de promediar — 036 MOVING.
D4. Otras fronteras (detenidas u otras) con control de energía — 036 RECURRENCE.
D5. Correcciones espectrales no compactas fuera del subcaso (D): medidas singulares, distribuciones — 045.
D6. Otras representaciones Volterra (gauge, IBP, reordenación) — 105.
D7. Compensación entre intervalos del kernel Peano; comparación con posición/masa del cruce — 091.
D8. Comparaciones de dos copias que admitan ascenso y descenso; clases duales — 100.
D9. Clase invariante que incorpore los inputs reales de pares 077/089/099 — 101.
D10. Representación integral positiva (tipo anti-Löwner) para M real; recurrencia que preserve los menores
de TAYLOR-HANKEL — 083.
D11. Desigualdades que conserven medida espectral restringida, términos positivos de frecuencia o
acoplamiento exacto con el polar (no cubiertas por prop:opcalc) — 014 POST.
D12. Representación C_B de 022 como asignación alternativa del emparejamiento (no sumada a S_2) — 025.
D13. Comparación para la familia de cinco funciones [K,J,Φ,J″,Φ″] — 112 §7.

## E. Cobertura

Archivos en el rango (orden de `ls *.md | sort`, de POWER_INVERSE_INTERIOR_AUDIT_022.md a
POWER_RECURRENCE_BOUNDARY_036.md): 66. Archivos leídos íntegramente: 66. Ninguno omitido ni muestreado.
Leídos además, para notación y cotejo: `RULES_AVOID.md`, `OBJECT_SPEC.md`, `STATEMENT_001.md`,
`POWER_CONE_001.md`, `POWER_BRIDGE_002.md`. No se leyeron las fuentes citadas fuera del rango (p. ej.
INVERSE_INTERIOR_022, DISCRETE_BALANCE027, CENTERED_CUTOFF049, 077–089, 099, 111, logs y verificadores);
sus contenidos se registran sólo tal como los resumen los archivos del rango.
