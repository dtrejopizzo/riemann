# Anexo 211 — Archivos, segunda tanda (POWER_DESCENT_016 … POWER_INVERSE_INTERIOR_022)

Lectura íntegra, archivo por archivo, de los `.md` de `../phase-211-sign-sandbox/` comprendidos en orden
alfabético entre `POWER_DESCENT_016.md` y `POWER_INVERSE_INTERIOR_022.md` inclusive, excepto
`POWER_GLOBAL_ROUTE_REVIEW.md` y `POWER_GRAM_SLICES_OBSTRUCTION.md`. Notación de
`../phase-211-sign-sandbox/STATEMENT_001.md`, `POWER_CONE_001.md` y `POWER_BRIDGE_002.md`. En estos archivos
W es la forma completa de la línea (ARCH + POLAR − peine), V_n={P(s)/(s+u)^n: deg P<n}, Q(s)=s/(s+u),
u=63/2 salvo indicación; g_N(t)=t^{N−1}e^{−ut}/(N−1)!; L(a), K(a,b) son los de POWER_CONE_001. El
objetivo es (★) de STATEMENT_001. Las etiquetas se copian tal como figuran en cada fuente.

## Entradas por archivo
### 1. POWER_DESCENT_016.md
- Objeto: filtros complementarios Q=s/(s+u), L=u/(s+u) (u>1); identidad exacta W[f]=W[Qf]+W[Lf] (DEF), incluida la polar; iteración binomial (BIN); diferencias (−1)^rΔ^r a_k=W[L^rQ^k f] (FD); ley binomial espectral (LAW).
- Resultado: PROVED (identidades, monotonía eventual de diferencias, localización (LOC) con error Lip(φ)/(2√m), (EDGE): el borde de 015 tiene masa y energía total →0). Falsificador W_4=W−4‖·‖²: conserva DEF/BIN/eventualidad y W_4[e^{−63y/2}]/‖·‖²<−1 (2L(32)<3). Descenso aritmético global OPEN.
- Resto sin signo: el defecto W[f]−W[Qf]=W[Lf] (forma completa del bloque de baja frecuencia) en los primeros pasos; el interior j/m≈θ<1 de (BIN).
- Reapertura: un descenso que controle W[Lf] con el dato aritmético completo o use la distribución espectral del numerador.
- PROVED reutilizable: (DEF)/(BIN)/(FD) para toda f racional causal; telescopado W[f]=Σ_k W[LQ^k f] absolutamente convergente.

### 2. POWER_DESCENT_AUDIT_016.md
- Objeto: momentos ℓ_r(f)=∫y^r f en L²_η; uniones de Q^kV_N; filtro desplazado Q_δ=(s+δ)/(s+u).
- Resultado: PROVED y APROBADO: (i) la unión de Q^kV_N, k≥1, está en el hiperplano ℓ_0=0, no es densa (incluso en P_T: F=(¼−D²)g); (ii) k_j→∞ ⇒ todo límite fuerte es 0; (iii) falsificador lógico W_C, C=4; (iv) §9: span{Q_δ^r f_0: r≥R} denso, W_4[f_r]>0 eventual, pero existe combinación finita con W_4<0.
- Falsificador: refuta «span denso + signo individual eventual de generadores ⇒ signo en el span» y «partición+mezcla positiva+eventualidad ⇒ signo inicial».
- Reapertura: desigualdad que controle el defecto de bloques iniciales con información adicional, o uniformidad conjunta sobre la masa pertinente; topología donde los momentos no sean continuos con continuidad de la forma completa reverificada.
- PROVED reutilizable: obstrucciones de momentos (hiperplano ℓ_0=0; límite cero) en L²_η, η>0; aprobación de JOINT_SCALE_016 (ley Beta(k+½,N−½)).

### 3. POWER_DIMENSIONAL_AUDIT_051.md
- Objeto: auditoría de DIMENSIONAL_CUTOFF_051.
- Resultado: APROBADO como cota de momento y de ARCH, no de W; corrección del factor del segundo sector (d−1)(d+2j+1).
- Resto: segmento inicial dependiente de n, polar y peine completo. Falsificador citado (PRIME_TRANSFER014): n=2^17, F=(s²−¼)/(s+u)^n, E2[QF]<0 impide declarar positivos todos los segmentos iniciales de E2.
- Observación: ZERO13 controla un subespacio de codimensión uno; el acoplamiento de Schur queda sin control; no se registra NO-GO nuevo.
- PROVED reutilizable: ninguno propio (valida 051).

### 4. POWER_DIMENSIONAL_CUTOFF_051.md
- Objeto: r=u²E_G[τ^{−2}] para G=Q^jF, F∈V_n={P/(s+u)^n}, u=63/2.
- Resultado: PROVED (auditado): (GENERAL) t r≤1+2√(d(d+2j)r), d=n−1, t=2j−1; (LINEAR) para todo n≥1, j≥⌈7n/6⌉: r<49/20, E τ^{−2}<1/405, ARCH/‖G‖²>859/800; corte J(n,b) para cualquier margen h.
- Resto: los índices j<⌈7n/6⌉, el polar y todos los contactos; la traza ponderada 010 que paga contactos crece con la dimensión. No es corte de signo de W.
- PROVED reutilizable: GENERAL/ROOT/LINEAR/ARCH-b, para todos los numeradores reales o complejos, sólo la parte arquimediana.

### 5. POWER_DIRECT_RECIPROCAL_TURAN_097.md
- Objeto: h(x)=u²M(u)/[au−M(u)], x=u², a=M′(0); T_h=2h′h‴−3h″².
- Resultado: PROVED la fórmula (DIRECT) T_h=a[auN_S−4C_h]/[16u³(au−c)^4], la regularización analítica en el origen, T_h(0)=(12a/b_1^4)·det Hankel₃(a,b_1,…,b_4) (ORIGIN-HANKEL) y T_h>0 para todo u≥512 (DIRECT-TAIL). Compacto 0<u<512 OPEN en esta ronda (cerrado después en 099).
- Resto: cota conjunta de auN_S−4C_h en 0<u<512; signo de ORIGIN-HANKEL no calculado. La herencia al siguiente nivel sigue abierta.
- PROVED reutilizable: DIRECT, COST C_h<4c³ para A≥128, T_h>0 para u≥512 (dato real, todos los contactos).

### 6. POWER_DIRECT_RECIPROCAL_TURAN_AUDIT_097.md
- Objeto: auditoría de 097.
- Resultado: APROBADO / PROVED fórmula y T_h>0 para u≥512; compacto y signo del origen OPEN.
- Advertencia de alcance: no da T_h global, R_G″ en todos los pivotes, triples G_p, cinco/todos los generadores ni nueva cobertura W/T; el lema anclado se aplica sólo si todo el segmento entre x y P está en el dominio probado.
- PROVED reutilizable: confirma 097.

### 7. POWER_DISCRETE_BALANCE_027.md
- Objeto: kernel conjunto Ω(t) por pisos (FLOOR), masas Σ K_N(n)=3/2 (SAMPLE), Σ K_N(nx)=G_N(x)=x^{−32}D_N(log x) (SCALES).
- Resultado: PROVED: Ω(t)≥ℓ−(4log t+9)/t, ℓ=1+γ/2−½log(4π)>1/50; Ω>9/1000 para t≥4096; (JOINT-TAIL) 0<(9/4000)∫_T^∞G_N≤∫_T^∞K_NΩ≤(7/4)G_N(T){T(logT+2)+3T²}; en N=129, 0<cola<10^{−36} (SCALE). Interior y signo W OPEN.
- Resto: ∫_1^{4096}K_129Ω (interior); dos masas escalares no fuerzan el emparejamiento (bump cerca de 3/2 donde Ω<−0,1).
- PROVED reutilizable: OMEGA-TAIL y JOINT-TAIL para el K gamma real en x≥exp(τ_N).

### 8. POWER_DIVISOR_COMPARISON_034.md
- Objeto: átomos f_{N,k} (filas N, columnas k), comparador B_N+S_K de 033.
- Resultado: PROVED (auditado): para todo N≥3, k≥1, u≥63/2, u²≥225N/4: W[f_{N,k}]>(1/40)‖f‖² (NEW-REGION); k≥2 margen >3/20. Corolarios: en u=63/2 filas 3≤N≤12 para todo k≥0 (margen >10^{−4}); para toda u≥63/2 filas 3≤N≤8 uniformes (margen >10^{−3}).
- Resto: k=0 para N≥13 a tasa fija; interior N≥18; rango N/u² cerca de 2/9.
- PROVED reutilizable: NEW-REGION (átomos individuales, no combinaciones), ARCH>7/200 y ARCH2>19/40, |POLAR|<9/1000.

### 9. POWER_EFFECTIVE_HIGHPASS_054.md
- Objeto: órbita high-pass Q^jF_0, Q=s/(s+u), u=63/2, F_0=P/(s+u)^n, deg P<n.
- Resultado: PROVED (auditado): para todo P real no nulo y todo j≥K(n)=max{10000n², A_n·3^{4D_n+20}} (C_n=9n²9^n, D_n=10C_n n!, A_n=6C_n n n!): W[Q^jF_0]>‖Q^jF_0‖² (EFFECTIVE). Incluye contorno STRIP≤D_n, cota del peine completo, polar <‖·‖².
- Resto: todos los índices j<K(n) (el corte es enorme); no da signo de la tabla ni ventana T.
- PROVED reutilizable: EFFECTIVE (dimensión variable, todos los numeradores); MOMENTS M_r≤Γ(r+½); |c_{Q^jF_0}(t)|≤D_n e^{−15t}‖·‖².

### 10. POWER_EFFECTIVE_HIGHPASS_AUDIT_054.md
- Objeto: auditoría de 054.
- Resultado: APROBADO; efectivización de la eventualidad 015 vía COEFF054 y contorno escalar 017; dos pesos sólo en dimensión 1.
- Resto: segmento j<K(n) y signo global, explícitamente fuera.
- PROVED reutilizable: confirma 054.

### 11. POWER_ENERGY_AUDIT_041.md
- Objeto: auditoría de ENERGY_BAND_041 y de su §7 (expansión periódica de B).
- Resultado: APROBADO; BAND uniforme para N≥2^80; SAWTOOTH y PERIODIC-ERROR aprobados como expansión clásica, no principio de signo.
- Resto: complemento anterior y posterior de la banda y su balance con ARCH_♯.
- PROVED reutilizable: confirma 041.

### 12. POWER_ENERGY_BAND_041.md
- Objeto: banda energética móvil [e^T,e^{T+L}], T=2dv/(u²−v²), L=√N/100, inverso Möbius completo h_N, B(x)=log(⌊x⌋!)−xH_{⌊x⌋}+⌊x⌋.
- Resultado: PROVED BAND: para todo N≥2^80, 2∫_{e^T}^{e^{T+L}}h_N B dx<−C_N/25600 (favorable en W/‖·‖²=ARCH_♯−2∫hB). También SAWTOOTH B=−γx−B_1(θ)log x+κ+E, −1/x<E<1/(2x), y PERIODIC-ERROR.
- Resto: complemento de la banda (interior antes de T y otras bandas); el residuo total W puede ser mucho menor que cada energía.
- PROVED reutilizable: BAND, B-REAL |B+γx|≤log x+1, SAWTOOTH, ELEMENTARY-EM, PERIODIC-ERROR.

### 13. POWER_ENERGY_GROUP_037.md
- Objeto: dilatación D_N(m)=mH_N(mx_N)/H_N(x_N) en el centro energético t_N=d/992; grupos K_{N,Q}(m)=Σ_{b|Q}μ(b)D_N(mb).
- Resultado: PROVED: (CENTER), (DILATE) m^{−1}e^{−M_N(...)}≤D_N≤m^{−1}(1+M_N ℓ); falsificador ABS-FAIL: Σ_{m≥2}|μ(m)|D_N(m)>1 para todo N≥2^16 (refuta contracción absoluta); SIGNED y WINDOW (grupos finitos positivos); §8 con Q=∏_{p≤N^{1/8}}p: grupos positivos pero GROW-ABS Σ|μ||K|>37/25 >K(1)<0,505.
- Resto: la suma firmada exterior FULL Σ_{(m,Q)=1}μ(m)K_{N,Q}(m); el mayorante (log m)²/m no es sumable.
- Reapertura: un bound firmado del complemento sin sumar error no sumable.
- PROVED reutilizable: DILATE, SIGNED, WINDOW; NO-GO de contracción absoluta (incluso tras agrupar con Q creciente).

### 14. POWER_EXACT_H_GLOBAL_AUDIT_099.md
- Objeto: auditoría del certificado global de T_h (099).
- Resultado: APROBADO / PROVED (FULL PASS 2048 paneles en [0,512], hash fijado): T_h(x)>0 para todo x>0 con la Φ real; los datos recíprocos R_G, S_G de G_p son estrictamente cóncavos en todos p,x>0; todos los triples distintos de G_p PD; bloque anclado {0,p,z_1,z_2,z_3} PD.
- Alcance: el nodo 0 corresponde al exponente ½, fuera del portador; no prueba cinco generadores admisibles arbitrarios ni herencia Turán ni todos los órdenes; 090 (contraejemplo genérico), 091, 092 siguen vigentes.
- PROVED reutilizable: T_h>0 global; triples del resto de G_p PD; bloque auxiliar de cinco nodos anclado PD.

### 15. POWER_EXACT_H_GLOBAL_DESIGN_099.md
- Objeto: funciones enteras U(x)=E′(u)/u, V(x)=[aE(u)−U(x)]/u²; S(u)=Ñ(u)/u^15=(16/a)NUM_x(u²) entera y par (ENTIRE-S), NUM_x=V^4T_h; gauge G_c=exp[−4M(c)(u−c)]S/E(c)^4.
- Resultado: PROVED (certificado intervalar 2048 paneles en [0,512], FULL PASS; reproducido): T_h(x)>0 para todo x>0 (empalmado con 097 y 098), en la Φ real con aritmética completa.
- Resto: no se infiere herencia de Turán al siguiente resto, iteración a todos los órdenes, signo W ni ventana T; el Wronskiano temporal 093/095 (más fuerte) sigue sin signo global.
- PROVED reutilizable: T_h>0 global; representación entera regularizada S; cota CAUCHY-S |S|/E(c)^4<2^151.

### 16. POWER_EXACT_H_ORIGIN_AUDIT_098.md
- Objeto: auditoría del jet en 0.
- Resultado: APROBADO: H_3>0 (≈1,738·10^{−21}) y T_h(0)>0 (≈3,155·10^{−5}) para la Φ real, NUMÉRICO certificado (intervalos Arb, 128 paneles, reproducido).
- Resto (en esta ronda): intervalo intermedio OPEN (cerrado en 099).
- PROVED reutilizable: T_h(0)>0 con a>0, b<0.

### 17. POWER_EXACT_H_ORIGIN_DESIGN_098.md
- Objeto: T_h(0)=12aH_3/b^4, H_3=det[[a,b,c],[b,c,d],[c,d,e]] con coeficientes de cumulantes normalizados (κ_{2j}) de Φ/Z(0); seis momentos pares I_0..I_10.
- Resultado: PROVED PUNTUAL (certificado intervalar): T_h(0)>0, vecindad sin radio certificado. Valores a≈0,04621, b≈−7,43·10^{−5}.
- Resto: el compacto 0<u<512 en esta ronda; ningún signo global ni de W.
- PROVED reutilizable: T_h(0)>0; cola temporal ∫_2^∞ t^rΦ<2^{−138} (r≤10).

### 18. POWER_FIVE_AUDIT_010.md
- Objeto: auditoría de FIVE_GLOBAL_010.
- Resultado: PROVED / PASS: W>0,01‖f‖² en todos los espacios de cinco polos reales ≥31,5, con repetición, sin separación.
- Resto: dimensión fija; no se extiende a seis ni a todos los órdenes.
- PROVED reutilizable: confirma 010.

### 19. POWER_FIVE_GLOBAL_010.md
- Objeto: f con Laplace P(s)/∏_{j≤5}(s+v_j), v_j≥63/2, deg P<5.
- Resultado: PROVED (certificado racional): W[f]>(1/100)‖f‖² (FIVE); BASE5 AP>(19/100)‖f_0‖²; AP5 AP>(1/50)‖f‖² por transporte; peine |Comb|<1/100 con peso all-pass σ=21, B_5=(49^5−1)/16.
- Resto: dimensión 12 necesita contribución aritmética con signo; sin constante uniforme al crecer la dimensión.
- PROVED reutilizable: FIVE (incluye mezclas de hasta cinco potencias X^{−a}, a≥32, y límites confluentes); identidad de transporte AP[f]−c‖f‖²=R_0(...)+∫(R−R_0)(m−c)|F_0|²+(r_0−R_0)Polar.

### 20. POWER_FIXED_BLOCK_ASSEMBLY_AUDIT.md
- Objeto: auditoría de la obstrucción por bloques PSD de soporte acotado.
- Resultado: APROBADO; exclusión sólo en la base original y para k fijo.
- Reapertura (no excluido): otra base, tamaño creciente, parte PSD global densa, Schur, controles firmados de cruces.
- PROVED reutilizable: confirma la obstrucción.

### 21. POWER_FIXED_BLOCK_ASSEMBLY_OBSTRUCTION.md
- Objeto: certificados C=ΣB_α, B_α PSD soportadas en ≤k coordenadas de la escalera a=32+m; condición necesaria 1ᵀC1≤k·tr C.
- Resultado: NO-GO PROVED (clase: sumas de PSD de soporte ≤k fijo en la base de potencias, cerrada por límites y congruencias diagonales): para cada k existe un bloque de nodos a_j=32+2N+2j, j=0..k, con C_ij→1 que viola NECESSARY; también falla la dominancia diagonal escalada.
- Falsificador: el propio bloque normalizado de la escalera real (no prueba dirección negativa).
- Reapertura: cambios de base generales, bloques de tamaño creciente, Schur, parte PSD global densa.
- PROVED reutilizable: L(a_j)=½log N+O_k(1); condición LOCAL/NECESSARY.

### 22. POWER_FIXED_GRID_003.md
- Objeto: escalera fija a_j=32+j, K_ij=(L_i+L_j)/(s_i+s_j), s_j=63/2+j; congruencia a B_ij=(1−q_iq_j)/(1−x_ix_j), x_j=j/(63+j), q_j=(L_j−L_0)/(L_j+L_0); recurrencia de eliminación (E) con parámetros α_r.
- Resultado: PROVED: K_n PD ⟺ α_0..α_{n−1} definidos y |α_r|<1 (identidad algebraica finita); órdenes 1–6 certificados (intervalos racionales): signo para toda mezcla real de X^{−32},…,X^{−37}. Falsificador algebraico: s=(1,5/3,3), L=(1,3/2,121/79): L creciente, L/s decreciente, todos los menores 2×2 >0, det K=−332001/391435520<0.
- Resto: |α_r|<1 para todo r con los L(32+j) reales; no hay ley de alternancia ni cota uniforme.
- Reapertura: un resto de signo que se preserve bajo (E).
- PROVED reutilizable: criterio de Schur/Pick por (E) en la escalera; seis primeros órdenes.

### 23. POWER_FOUR_GENERATORS_085.md
- Objeto: N_R, N_S (obligaciones Turán de R(x)=u/M(u), S(x)=uM(u)) en el compacto ½≤u≤127,5.
- Resultado: PROVED (certificado 16384 paneles, FULL PASS, reproducido): T_R,T_S>0 para todo u≥½; con Rolle (084), factorización (083) y menores (080): W completa positiva en toda combinación no nula de hasta CUATRO potencias X^{−a_i}, a_i>1 arbitrarios (ARCH, polar y todos los contactos).
- Resto: cinco generadores, todos los órdenes, envolvente completa; obligaciones pfaffianas superiores OPEN.
- PROVED reutilizable: positividad para cuatro generadores arbitrarios a_i>1.

### 24. POWER_FOUR_GENERATORS_AUDIT_085.md
- Objeto: auditoría de 085.
- Resultado: APROBADO / PROVED (hash coincidente). Amplía exponentes pequeños/mixtos más allá de la región de tasas grandes 053.
- Resto: cinco generadores y órdenes superiores OPEN.
- PROVED reutilizable: confirma 085.

### 25. POWER_FOUR_GLOBAL_009.md
- Objeto: espacios de cuatro polos reales v_j≥63/2 (con repetición); transporte de déficit por filtro H=∏(s+u)/(s+v_j).
- Resultado: PROVED: W[f]>(2/25)‖f‖² (FOUR); AP4 AP>(1/10)‖f‖²; (NEG) m≥1/10 para τ²≥81 y τ²(1/10−m)_+<23; peine <13/1000 con B_4=32552.
- Resto: dimensión creciente: BASE puede fallar sin contribución aritmética positiva (dimensión 12).
- PROVED reutilizable: identidad de transporte (ID) y cota coerciva; FOUR.

### 26. POWER_FOUR_GLOBAL_AUDIT_009.md
- Objeto: auditoría de 009.
- Resultado: PROVED / APROBADO; corchete exacto 3669270349/93389776200>3/100.
- Resto: no se infiere cinco polos ni dimensión arbitraria.
- PROVED reutilizable: confirma 009.

### 27. POWER_FOUR_TURAN_084.md
- Objeto: Pfaffiano de cuatro nodos, A_{f,ij}=[f(x_j)−f(x_i)]/(u_i+u_j); Pf(A_f)=−D_f/P (PF-DET), D_f=det[1,x_i,f,x_if]; det K=Pf(A_R)Pf(A_S)/∏R(x_i).
- Resultado: PROVED: criterio global por Rolle: f′>0, f″<0, T_f=2f′f‴−3f″²>0 en el intervalo ⇒ Pf(A_f)>0 para toda cuádrupla; OUTER-TURAN N_R>¼, N_S>19/4 para A≥128. Falsificador de herencia: R=1+x−x²/16, S=x/R (RS=x, concavidades, triples PD) con det K_4=−ε³V²/[∏R]²<0.
- Resto (en esta ronda): compacto ½<u<127,5 (cerrado en 085); o pagar el producto de Pfaffianos sin signos individuales.
- PROVED reutilizable: PF-DET; criterio de Rolle suficiente; REAL-TURAN; cotas de P_j(A).

### 28. POWER_FOUR_TURAN_AUDIT_084.md
- Objeto: auditoría de 084.
- Resultado: APROBADO / PROVED como criterio suficiente, falsificador de clase y aplicación exterior. El criterio es suficiente, no necesario para cada Pfaffiano.
- Resto: compacto pendiente en esa ronda; sin nueva cobertura W/T (cola ya cubierta por 053).
- PROVED reutilizable: confirma 084.

### 29. POWER_FRONTIER_AUDIT_036.md
- Objeto: auditoría de RECURRENCE_BOUNDARY_036 y MOVING_BALANCE_036.
- Resultado: APROBADOS: frontera diagonal completa 0≤C_L≤M_L(H_L+0,002)=O(log L/√L) sobre el cono parabólico; frontera detenida (SURVIVAL con probabilidad positiva; la región 034 N′≤17 es inaccesible desde N≥18); ventana energética: ambas energías reales (polar y prima) concentran en m/d→1/32 con fases λ^N coincidentes; CHEB ψ≥x/2−16 para Λ real.
- Resto: el lower firmado del complemento R_L; no se deduce Π/P→1 ni precisión del residuo; compensación dentro del funcional firmado antes de promediar no refutada.
- PROVED reutilizable: cotas de energía del cono parabólico; concentración m/d→1/32.

### 30. POWER_FULL_THIRTEEN_053.md
- Objeto: espacios de trece polos reales v_i≥63/2, numerador P de grado<13; ganancia ZERO14 (catorce polos con D(0)=0).
- Resultado: PROVED (certificado: 95 LDL racionales j=1..95 más cola analítica j≥96, auditado): W[P/∏_{i≤13}(s+v_i)]>‖·‖²/4000 (TARGET); W>‖·‖²/1000 en catorce polos con numerador cero.
- Resto: dimensión arbitraria; catorce polos con numerador general; el mayorante de cola desde n=3 (0,0464) es insuficiente para E2, por eso se conserva el contacto 3.
- PROVED reutilizable: TARGET (13 polos); ZERO14; identidad FULLTEL con κ_j≥0.

### 31. POWER_FULL_THIRTEEN_AUDIT_053.md
- Objeto: auditoría de 053.
- Resultado: APROBADO (reproducción exit 0, 95 LDL PASS, B_T14=947334302964<973312²).
- Resto: no dimensión arbitraria ni ventana temporal.
- PROVED reutilizable: confirma 053.

### 32. POWER_FULL_TRANSFER_PLAN_050.md
- Objeto: plan MULTI con contactos {2}, {2,3}, {2,3,4}; MULTI-E2: E2[F]>‖F‖²/2500 en todos los doce polos ≥u.
- Resultado: EXPLORACIÓN SUPERADA por FULL_TWELVE_050; PROVED MULTI-E2 (ARCH+POLAR+contacto 2) y TAIL-M (mayorante de cola desde M). La obligación NEXT (E_{2,3}≥‖·‖²/2500 en toda la órbita) quedó OPEN y luego evitada; «no tratar NEXT como obligación vigente».
- Resto: ninguno vigente propio.
- PROVED reutilizable: MULTI-E2; cota TAIL-M con B=1282776893780652.

### 33. POWER_FULL_TWELVE_050.md
- Objeto: doce polos reales v_i≥63/2, deg P<12; ZERO13.
- Resultado: PROVED (auditado): W[f]>‖f‖²/10000 (TWELVE); ZERO13: W>‖·‖²/250 en trece polos con D(0)=0; ORBIT E2[Q^jF_0]>‖·‖²/50 para j≥1.
- Resto: trece polos con numerador general (cerrado en 053), orden arbitrario, puente global de bloques crecientes.
- PROVED reutilizable: TWELVE; ZERO13; ORBIT; B_T13=109543953194.

### 34. POWER_FULL_TWELVE_AUDIT_050.md
- Objeto: auditoría de 050.
- Resultado: APROBADO; trece PASS; cola ≤2942000/186535791<2/125.
- PROVED reutilizable: confirma 050.

### 35. POWER_GAMMA_129_AUDIT_061.md
- Objeto: auditoría de la decisión del átomo N=129, k=0.
- Resultado: APROBADO; W/‖g‖²∈[13456684165,13456684168]/10^{20}; beneficio de las células n≥3 entre 0,3755 y 0,3822.
- Resto: no decide filas, bloques, órdenes arbitrarios ni ventana.
- PROVED reutilizable: confirma 061.

### 36. POWER_GAMMA_129_DECISION_061.md
- Objeto: átomo g_129(t)=t^{128}e^{−ut}/128!, u=63/2.
- Resultado: PROVED (certificado racional): 1,34·10^{−10}<W[g_129]/‖g_129‖²<1,35·10^{−10}; −ERR≈1,04219397031519 y −ARCH_♯≈1,04219397018063 (cancelación a 10^{−10}); K_129(1)<0 no implicaba W<0.
- Resto: propagación en N; el balance firmado debe conservarse con precisión relativa al residuo; no rehabilita K≥0 universal.
- PROVED reutilizable: signo del átomo (129,0); 0,3755<2Σ_{m≥3}S_129(m)<0,3822.

### 37. POWER_GAMMA_AFFINE_AUDIT_062.md
- Objeto: auditoría del diagnóstico afín 062.
- Resultado: APROBADO; R es el residuo global completo de 042; ABS-TAIL (N≥2^80) no aplica a 129; R obtenido de ERR061, no estimación independiente.
- Resto: control del balance firmado interior al variar N.
- PROVED reutilizable: confirma 062.

### 38. POWER_GAMMA_AFFINE_BALANCE_062.md
- Objeto: AFF=ARCH_♯+2γ−βJ_1, β=log(2π)−1−γ; W/‖g_129‖²=AFF−2R (EXACT), R residuo renormalizado completo.
- Resultado: PROVED (certificado): AFF<−1/100 (≈−0,0604), R<−1/200; NO-GO puntual: la parte afín 042 no es base positiva en N=129.
- Resto: R (orden 0,03) frente a W (orden 10^{−10}); comparación uniforme celdas–ARCH_♯ OPEN.
- Reapertura: cualquier continuación desde la parte afín debe estimar de verdad el residuo completo.
- PROVED reutilizable: las cajas BOXES (sólo N=129).

### 39. POWER_GAMMA_BALANCE_030.md
- Objeto: ley gamma real V=β/G, G~Gamma(b,1), β=u²/4, b=N−½; L_N(a)=E(V−a)_+−(m−a)_+; G_W(v) forma completa del test gaussiano; identidad FULL-GAP W[g_N]/‖g_N‖²−G_W(m)=∫L_N G_W″.
- Resultado: PROVED: SHARP-GAP 0<A_♯(m)−ARCH_♯[g_N]/‖·‖²≤½[ψ(b)−log(b−1)]<1/(2(b−1)) para todo N≥2. Falsificador (N=2, u=63/2): W[g_2]/‖·‖²<17/20, G_W(u²/2)>7/8, ∫L_2G_W″<−1/40 (NEG-GAP): refuta «el test gamma domina a la gaussiana de igual segundo momento».
- Resto: el cambio firmado de ERR junto con la pérdida; el emparejamiento completo L_N G_W″.
- PROVED reutilizable: SHARP-GAP (lower de la parte sharp con coste O(1/N)); lower digamma Re ψ(a+it)≥log|a+it|−Re[1/(2(a+it))]−1/(6a²).

### 40. POWER_GAMMA_WEIGHT_031.md
- Objeto: R(t)=ρ(t)−(2/3)ρ′(t), máximo T_N; primitiva I_*(X)=∫_1^X(3/2)x^{−½}H(x)dx con H(x)=1+[log((x+1)/(x−1))+c_0−1−2Ψ_1(x)]/x², Ψ_1(x)=Σ_{q≤x}qΛ(q).
- Resultado: PROVED (auditado): T_N≤(2/3)d/(d+20), q″<0, PEAK 0<R(T_N)−1≤2M_2/9, M_2=u²/(2N−3); BUDGET W[g_N]/‖·‖²≥∫_{T_N}^∞I_*(e^t)[−R′]dt−M_2; criterio suficiente E_ν[I_*]>M_2/R(T) (no probado).
- Resto: I_* toma valores negativos después de 3 (WEIGHTED_BLOCK031); falta una desigualdad aritmética firmada para E_ν[I_*].
- PROVED reutilizable: PEAK, BUDGET, concavidad de q, identidad IBP sin borde.

### 41. POWER_GEOMETRIC_TRANSFER_015.md
- Objeto: iteración de un polo W[f_v]=ρΣ_{k≤K}a^kW[h_k]+a^{K+1}W[g_{K+1,v}], ρ=u²/v², a=1−ρ; topología X=H^t∩L²(e^{ηy}), 0<t<½, ½<η<u/2.
- Resultado: PROVED (u>1): W continua en X; Q^k f→0 fuertemente; mezcla (MIX) y (MULTI) W[f]=Σw_kW[Q^kf_0] con w_k≥0, Σw_k=1; cociente arquimediano no decreciente en k; Polar[h_k]=[−1/(4u²−1)]^kPolar[h_0].
- Resto: positividad de los bloques iniciales de la órbita Q^kV_N (segmento finito para cada N, sin extremo efectivo universal).
- PROVED reutilizable: MULTI (suficiencia: toda la órbita high-pass positiva ⇒ todos los N polos ≥u); continuidad en X.

### 42. POWER_GRAM_SLICES_AUDIT.md
- Objeto: auditoría de GRAM_SLICES_OBSTRUCTION (fuera del rango a resumir; su auditoría sí está en el rango).
- Resultado: APROBADO: refuta sólo que todas las capas (desintegración en v=σ²−τ²) sean PSD; ganancia (β−α)²f(R)/R³ divergente; addendum: criterio hazard con diagonal negativa por 073; multiplicador gaussiano B_op(−Φ′)=tΦ no controla el término de semirrecta de Q_A.
- Resto: PSD del integral OPEN; controlar compensación entre capas o construir otro Gram.
- PROVED reutilizable: ninguno nuevo (confirma la obstrucción de capas).

### 43. POWER_GREEN_PAIR_TP2_AUDIT_111.md
- Objeto: auditoría de 111 (Green balanceados V_p, pareja J,K compacta).
- Resultado: APROBADO (base, extensión estricta r_ε, ampliación CM en x=p²).
- Resto: no se afirma CM de la familia real ni se excluye un método con más estructura.
- PROVED reutilizable: confirma 111.

### 44. POWER_GREEN_PAIR_TP2_SCOPE_111.md
- Objeto: K=1_{|t|<2}, J=[1+1_{1<|t|<2}]K; λ_p=2−1/(2cosh p); V_p Green balanceado con V_p″−p²V_p=J−λ_pK.
- Resultado: NO-GO PROVED (clase: parejas pares compactas con J/K no decreciente, incluso estrictamente creciente, todos los V_p>0 con V_p/K decreciente, aun con monotonía completa de V en x=p²): no implican TP2; menores OPPOSITE-MINORS de signos opuestos con p=1,2 en t∈{¼,½} y {3/2,7/4}.
- Falsificador: la pareja explícita (no es la Φ real; no cumple J′=−tΦ, K″=aΦ−J ni MIXED4).
- Reapertura: una inducción que use la compatibilidad real J′=−tΦ, K″=aΦ−J o MIXED4.
- PROVED reutilizable: COMPLETE-MONOTONICITY para la contraclase; menores explícitos.

### 45. POWER_GROUP_AUDIT_037.md
- Objeto: auditoría de ENERGY_GROUP_037.
- Resultado: APROBADO (núcleo, ABS-FAIL, SIGNED/WINDOW y elección Q creciente).
- Resto: el complemento aritmético firmado y su integración con precisión suficiente.
- PROVED reutilizable: confirma 037.

### 46. POWER_HIGH_ORDER_PM_NOGO_007.md
- Objeto: f_{n,u}=y^{n−1}e^{−uy}; polar normalizado P_n(u)=4^n/[u·binom(2n−2,n−1)](1−1/(4u²))^{−n}; lema (G) 0≤τm′(τ)<4.
- Resultado: PROVED / NO-GO: para u=63/2, n=2^17: uE_n′(u)<−140/31 (NEG); aumentar un solo polo reduce el cociente ARCH+POLAR. FALSIFIED «aumentar individualmente polos ≥63/2 no reduce el cociente arch+polar de ningún numerador, uniformemente en n».
- Alcance: no refuta transporte que preserve sólo el signo, ni n=4, ni monotonía de λ_min; no incluye el peine.
- PROVED reutilizable: (G) y fórmula polar exacta (P).

### 47. POWER_HIGHPASS_015.md
- Objeto: órbita f_{k,P} con F=[s/(s+u)]^kP(s)/(s+u)^N, u>1, deg P<N.
- Resultado: PROVED (auditado): EVENTUAL: existe K_N (independiente de P) con W[f_{k,P}]>0 para todo k≥K_N; uniformemente Arch/‖·‖²≥½log k−C_N, Comb/‖·‖²→0, Polar/‖·‖²→0; para P fijo ASYM W/‖·‖²=½log k+log(u/2π)−½ψ(r−½)+o(1).
- Resto: signo de los primeros k; K_N no uniforme en N; positividad de cola no implica positividad de la mezcla.
- PROVED reutilizable: EVENTUAL, GRAM/LIMIT, WT ‖e^{ηy}f‖²≤C_{N,η}‖f‖², ASYM.

### 48. POWER_HIGHPASS_AUDIT_015.md
- Objeto: auditoría de HIGHPASS_015 y GEOMETRIC_TRANSFER_015.
- Resultado: PROVED: dos herramientas (mezcla completa exacta y cola high-pass uniformemente positiva para cada N fijo); reducen la condición suficiente al signo de un segmento finito de bloques iniciales.
- Resto: extremo efectivo del segmento y su signo para todo N; una mezcla puede contener términos iniciales negativos.
- PROVED reutilizable: confirma 015.

### 49. POWER_HIGHPASS_CUTOFF_049.md
- Objeto: corte J=32 para E2 sobre Q^jV_12; lema JAC αR≤β+1+2√(m(m+α+β+1)R).
- Resultado: BORRADOR SUPERADO (por CENTERED_CUTOFF_049, corte 14, y R12_TRANSPORT_049); «no registrar este corte 32 como resultado adicional». Contiene prueba de JAC y TAIL E2>(99/1000)‖·‖², j≥32.
- Resto (histórico): bloques j=1..31.
- PROVED reutilizable: el lema JAC (polinomios ponderados) es demostración autocontenida, aunque el documento está superado.

### 50. POWER_HIGHPASS_DIAGONAL_DENSITY_094.md
- Objeto: E_{n,r}=Q^rV_n(u) ↔ S_{n,r}={(1+z)^rP(z): deg P<n} en H² (CAYLEY); distancia exacta dist(1,S_{n,r})²=1−A(n,r), A=[(n+r−1)!]²/[(n−1)!(n+2r−1)!].
- Resultado: PROVED (auditado): BINOMIAL-DET por Dodgson; e^{−r²/n}≤A≤e^{−r²/(n+2r−1)}; DIAGONAL-DENSITY: la unión ∪E_{n,r(n)} es densa en L² ⟺ liminf r(n)²/n=0; NO-GO de densidad: la unión de bloques con r≥n (incluido el cono 060 r≥10^{12}[n⌈log_2(n+1)⌉]³) está a distancia >½ de 1, aun añadiendo finitos bloques confluentes.
- Resto: envolvente lineal de la unión, cruces entre bloques, continuidad de W en la topología usada.
- Reapertura: un cono positivo con r=o(√n) en una subsucesión, más continuidad de la forma completa.
- PROVED reutilizable: EXACT-DISTANCE, BINOMIAL-DET, DIAGONAL-DENSITY, POLYNOMIAL-APPROX.

### 51. POWER_HIGHPASS_DIAGONAL_DENSITY_AUDIT_094.md
- Objeto: auditoría de 094.
- Resultado: APROBADO / PROVED.
- Resto: la no densidad del cono no excluye su envolvente lineal, cruces, control firmado, mezclas o descenso compensado.
- PROVED reutilizable: confirma 094.

### 52. POWER_HYPERBOLIC_MODEL_GRAM.md (71 KB, 13 secciones)
- Objeto: modelo φ_a(t)=exp(−a cosh 2t), Z_a=y_{u²/4}(0), y_x″=[a²e^{2r}+x]y_x; H=−D_r²+a²e^{2r} (Dirichlet), M_a(u)/u=½Tr(H+u²/4)^{−1} (REP).
- Resultados PROVED (con su clase): §5 GRAM: K_ij=(M_a(u_i)+M_a(u_j))/(u_i+u_j) PSD en todos los tamaños (suma de cuadrados HS) para el modelo; §8 extensión Robin φ_{a,β}=[β+a cosh 2t]e^{−a cosh 2t} también PSD. NO-GO: §7.1 Φ no es mezcla positiva ∫e^{−a cosh 2t}dμ(a); §7.2 Φ≠φ_a∗ν (ν≥0 finita); §9 el flujo −a∂_aK_a no es PSD en todos los tamaños (NEG-MOM); §10 prefactor fijo q no da potencial escalar independiente de ν (salvo q constante); §10.1 con primera derivada sólo q=C o C cosh(v/2), excluido para la q real (también con peso espectral variable y cambio de escala); §11 Φ≠C e^{−a cosh 2t}∏cosh(α_jt) (c_1=π−3/(2π)∉ℕ); §11.4 ni aproximación localuniforme a escala 2π fija; §12 vector finito de prefactores fijos sin deriva; §12.1 con deriva matricial (anulador racional imposible); §12.2 dimensión infinita simétrica sin deriva (‖Q‖²=A+c log cosh v); §12.3 deriva escalar constante (kernel DRIFT-K, cúspide par w=2i); §12.4 deriva escalar dependiente de escala forzada constante; métrica local imposible para el ejemplo 2×2; §12.7 la realización 12.6 no admite métrica local positiva acotada compatible; §13 productos cosh desplazados (−1<c<1) dan límite entero, incompatible con la cúspide par; §13.1 también con escala a_n variable.
- PROVED positivo adicional: §12.5 la deriva operatorial determina L=[G(v+z)+G(v−z)]/2, G=−coth(t/2)F′; §12.6 realización explícita Q,B,C,D en H=L²(ρdω)⊕ℝ³ (ρ=sech(πω/2)) con observación continua exacta ⟨Q(v),h⟩=q_θ(v) y ecuación fuerte Y_rr=(b²+ν²)Y+2DY_r+(−C+2bB̄)Y, ⟨Y_ν(2π),h⟩=Z(2ν).
- Resto: una métrica (no local o no acotada) y una identidad Green POSITIVA que reproduzca la forma completa; la comparación K_Φ≥εK_{2π} está refutada (GLOBAL).
- Reapertura (declarada): métricas no locales, no acotadas, conexiones nuevas, prefactores dependientes de b, observaciones no continuas, otras realizaciones; escalas base variables de frecuencia, potencias reales, sumas, cocientes, comparaciones relativas de formas.
- PROVED reutilizable: Green/traza del modelo; THETA-TAIL Φ(t)~2π²e^{9t/2}e^{−πe^{2t}}; expansión de cúspide par; realización 12.6.

### 53. POWER_INFINITE_SHOULDER_039.md
- Objeto: inversos aritméticos completos h_N, K_N=J_N+xh_N (Möbius completo) en el hombro x=e^{t_v}, t_v=2dv/(u²−v²), v=½+δ, σ=v+½>1; operador M_σf(ℓ)=U_σ^{−1}Σμ(n)n^{−σ}f(ℓ+log n).
- Resultado: PROVED (auditado): ψ_Λ(x)≤2x para todo x≥1; A_σ≤2σ/δ, B_σ≤2σ/δ²; (INFINITE) |M_σf(0)−f(−A_σ)|≤12000B_σ/N+…; SHOULDER (9/10)U_σ<h_N/H_N, K_N/G_N<(11/10)U_σ; TAIL: para todo N≥4·10^6 y x≥e^{T_N}, T_N=d/992+O(√N): h_N(x)>0, K_N(x)>0.
- Resto: región interior (centro crítico δ→0, σ=1 no alcanzado); comparación de la cola favorable de F_N=2∫h_NB con la parte adversa interior y ARCH_♯; precisión del residuo polar−peine.
- PROVED reutilizable: ψ_Λ(x)≤2x elemental; MOMENTS; SHOULDER/TAIL (positividad de los inversos completos en x≥e^{T_N}).

### 54. POWER_INTERIOR_017.md
- Objeto: fila N=1, F_k(s)=s^k/(s+u)^{k+1}, u≥63/2; norma ponderada N_k(η).
- Resultado: PROVED: (WR) ‖e^{ηy}h_k‖²/‖h_k‖²≤(u−η)/(u−2η) para todo k≥0 (generadora GEN y Vandermonde c_{k−j}c_j≤c_k); ROW1 W[h_k]>(4/3)‖h_k‖² para todo k≥0, u≥63/2; §7 WRN: ‖e^{ηy}f_{N,k}‖²/‖f_{N,k}‖²≤R_N(u,η)=(u/a)^{2N−1}S_N(ρ), S_N racional, para todas las filas, uniforme en k.
- Resto: el régimen conjunto k/N finito con N creciente; la dependencia en N de R_N no basta para la tabla.
- PROVED reutilizable: WR, W11, ROW1, WRN; polar exacto Polar[h_k]=2(−¼)^k/(u²−¼)^{k+1}.

### 55. POWER_INTERIOR_AUDIT_017.md
- Objeto: auditoría de la tabla escalar: puente escalar Bernstein (SCALAR_BRIDGE_017), fila N=1, WRN, cono cuadrático (QUADRATIC_017 y QUADRATIC_EXPLICIT_017).
- Resultado: PROVED los resultados específicos: puente Bernstein: W[f]+εW[f_1] es suma positiva de valores atómicos W[h_{N,k}], por lo que la tabla escalar COMPLETA (todos los átomos (N,k)) es SUFICIENTE; ROW1; WRN; cono cuadrático: positividad eventual para P=1 en k≥cN², N≥N_0(c); explícito: W>(49/50)‖f‖² para todo N≥2, k≥10000N², u=31,5, P=1. Signo de toda la tabla escalar OPEN.
- Resto: los átomos (N,k) fuera de la fila 1 y del cono cuadrático.
- PROVED reutilizable: puente escalar Bernstein (reducción a átomos); cono cuadrático explícito; lower m(τ)≥log(|τ|/2π)−4 y |m−log(|τ|/2π)|≤1/|τ|+1/(2τ²).

### 56. POWER_INTERIOR_AUDIT_030.md
- Objeto: auditoría de GAMMA_BALANCE_030 e INTERIOR_SCALE_030.
- Resultado: APROBADOS: SHARP-GAP; falsificador NEG-GAP (N=2, sólo de la comparación sin coste); bloque interior real (x∈[1,9/4]): I_*>0,02, error <0,005 para N≥2^{20}, bloque >0,01; identidad JOINT-G con H=1+[log((x+1)/(x−1))+c−1−2Ψ_1(x)]/x².
- Resto: el resto [9/4,∞) sin control; BLOCK no es W total.
- PROVED reutilizable: confirma 030 y la fórmula de H.

### 57. POWER_INTERIOR_CONSTRAINT_027.md
- Objeto: mezcla gamma real ρ_N(t)=E e^{−V_Nt²}, V_N=β/G, G~Gamma(N−½,1); W[g_N]/‖g_N‖²=E G_W(V_N) (WG); peso bisagra L_N(a)=E(V_N−a)_+−(m_N−a)_+≥0; GAP δ_N(t)=t^4∫e^{−at²}L_N(a)da.
- Resultado: PROVED: UPPER ARCH_♯[g_N]/‖·‖²=E A_♯(V_N)<A_♯(EV_N) (Jensen va en el sentido INCORRECTO para un lower); JOINT-GAP W[g_N]/‖·‖²−G_W(m_N)=∫L_N(a)G_W″(a)da; FAIL-CONVEX G_W″(v)<0 para todo v≥65536. §8: por INV-MIX y los certificados 022/023 existen a_h, a_K>0 con h_{a_h}(1)<0 y K_{a_K}(1)<0: refutadas las premisas universales gaussianas h_a≥0, K_a≥0.
- Resto: G_W(m_N)+∫L_NR≥0, es decir, controlar unilateralmente la parte negativa de R=G_W″ contra la ley L_N real.
- PROVED reutilizable: WG, GAP, JOINT-GAP, INV-MIX.

### 58. POWER_INTERIOR_SCALE_030.md
- Objeto: inversión adjunta H(x)=Σ_{m≤x}μ(m)Ω(x/m)/m=1+[log((x+1)/(x−1))+c−1−2Ψ_1(x)]/x², c=−γ−log 4π; JOINT-G W[g_N]/‖·‖²=∫_1^∞G_N H, G_N=x^{−32}D_N(log x).
- Resultado: PROVED (auditado): BLOCK ∫_1^{9/4}G_N H>1/100 para todo N≥2^{20} (u=63/2), con el contacto 2 incluido; PRIMITIVE-FAIL ∫_1^{5/2}H<−1/50 y ∫_1^{5/2}x²H<−1/4 (falla el criterio de primitivas positivas); G_N decreciente para N≥663, G_N/x² para N≥134.
- Resto: ∫_{9/4}^∞G_N H (todos los contactos siguientes), sin control.
- PROVED reutilizable: fórmula H, JOINT-G, BLOCK, GAMMA-ERROR |G_N−G_*|≤(7/4)M2_N en [1,9/4].

### 59. POWER_INVERSE_COEFFICIENT_054.md
- Objeto: R(y)=y^{n−1}P(ia/y), a=u√j, peso w=(1+y²/j)^{−(n+j)}; ‖Q^jF_0‖²=a^{1−2n}D_{n,j}[R]/(2π).
- Resultado: PROVED (auditado): COEFF (Σ|c_r|)²≤C_nD_{n,j}[R], C_n=9n²9^n, para todo R complejo y todo j≥n; EVAL |R(z)R(−z)|≤C_nD·max(1,|z|^{2n−2}); identidad DENSITY con el factor (−1)^{n−1}.
- Resto (en el memo): integración de contorno y cola sumable (desarrolladas en 054 EFFECTIVE).
- PROVED reutilizable: COEFF/EVAL (condicionamiento efectivo dependiente sólo de n).

### 60. POWER_INVERSE_COEFFICIENT_AUDIT_054.md
- Objeto: auditoría de COEFF/EVAL.
- Resultado: APROBADO; no demuestra cola aritmética sumable ni corte K(n); un bound IBP ∝1/t no suma el peine; N′=1 no se importa de N′≥2.
- PROVED reutilizable: confirma 054.

### 61. POWER_INVERSE_INTERIOR_022.md
- Objeto: inverso Möbius completo h_128(1)=Σ_{m≥1}μ(m)m^{−32}A_128(log m), A_128 con coeficientes racionales positivos.
- Resultado: PROVED (certificado racional, cola m≥65 <10^{−10}): −2/3<h_128(1)<−33/50<0. Falsificador: «h_N(x)≥0 para todos N≥2, x≥1» es falso; existe intervalo a la derecha de 1 con h_N<0 y B<0 (contribución adversa real en F_N=2∫h_NB).
- Resto: el emparejamiento total F_N; no se afirma W[g_128]<0.
- Reapertura: los presupuestos firmados que no supongan h_N≥0 siguen legítimos.
- PROVED reutilizable: el valor certificado de h_128(1); exterior h_128≥H_128/4 para log x≥127/30 (citado de 020).

## A. Lista deduplicada «no relanzar», con condición de reapertura, y cotejo con RULES_AVOID.md

Marcas: **[AUSENTE]** no figura en `RULES_AVOID.md`; **[PARCIAL/INEXACTO]** figura con alcance o condición
distintos (se citan ambos); **[PRESENTE]** figura correctamente.

A1. **Descenso desde particiones exactas + mezcla positiva + positividad eventual en cada orden fijo**
(016 §5, AUDIT_016 §4). Falsificador: W_4=W−4‖·‖² conserva DEF/BIN/MULTI/EVENTUAL y W_4[e^{−63y/2}]<−‖·‖².
Reapertura: «un descenso que controle W[Lf] con el dato aritmético completo o utilice la distribución
espectral del numerador» (016 §5); «una desigualdad que controle el defecto de los bloques iniciales por
información adicional» (AUDIT_016 §5). **[PARCIAL/INEXACTO]** RULES_AVOID D4: «Recurrencia o descenso solos —
sólo con una cota aritmética firmada del resto R_L ≥ −ε_L». No menciona el falsificador W_4 ni que la
cota debe distinguir el multiplicador real del desplazado m−C (016: «Incluso conservar exactamente Lambda
no basta si su interacción con la constante arquimediana no aparece en esa estimación»).

A2. **Puente de densidad por uniones de colas high-pass** (AUDIT_016 §§2–3, §9; 094). (i) La unión de
Q^kV_N, k≥1, está en ℓ_0=0 (no densa en L²_η); (ii) con k_j→∞ todo límite fuerte es 0; (iii) incluso
reparando el momento con un filtro invertible Q_δ (span denso), «span denso en norma de forma + signo
individual eventual de sus generadores» NO implica signo (contraejemplo con W_4); (iv) en L² sin peso la
unión diagonal es densa ⟺ liminf r(n)²/n=0, y aun así falta continuidad de la forma completa.
Reapertura: cono positivo con r=o(√n) en una subsucesión más continuidad de W en esa topología; o control
específico de cruces del dato real. **[PARCIAL/INEXACTO]** RULES_AVOID D3: «Inferir densidad o signo de una
unión positiva — sólo con liminf r(n)²/n = 0 y un bloque que repare el momento (211/GLOBAL §4)». AUDIT_016
§9 muestra que reparar el momento con generadores individualmente positivos no basta: falta el control de
cruces, y 094 exige además la continuidad de la forma completa.

A3. **Contracción absoluta de la inversión Möbius**, también tras agrupar con Q creciente (037 ABS-FAIL,
GROW-ABS). Reapertura: «un bound firmado del complemento, sin sumar un error no sumable ni convertir el signo
de un grupo finito en el de FULL». **[AUSENTE]**.

A4. **Positividad universal del inverso completo** h_N≥0, K≥0 universal, y sus versiones gaussianas h_a≥0,
K_a≥0 (022; 027 §8; 061 «no rehabilita K≥0 universal»). Reapertura: presupuestos firmados que no supongan
ese signo. **[AUSENTE]**.

A5. **Comparación con la gaussiana de igual segundo momento / Jensen / convexidad** (027 UPPER y
FAIL-CONVEX; 030 NEG-GAP). Jensen da cota SUPERIOR de ARCH_♯; G_W″<0 para v≥65536; el test gamma no domina a
la gaussiana (N=2). Reapertura: controlar la parte negativa de R=G_W″ contra la ley L_N real, o el cambio
firmado de ERR junto con SHARP-GAP. **[PARCIAL/INEXACTO]** RULES_AVOID D11 sólo dice «concavidad de Jensen /
de operadores»; no registra la convexidad global de G_W ni la comparación gaussiana.

A6. **Criterio de primitivas positivas** del peso H o I_* (030 PRIMITIVE-FAIL; 031: I_* negativa después de
3). Reapertura: desigualdad aritmética firmada para E_ν[I_*]>M_2/R(T). **[AUSENTE]** (la «primitivas
compensadas de capas» de D16 es otro objeto).

A7. **Parte afín de la representación renormalizada 042 como base positiva** (062: AFF<−1/100 en N=129).
Reapertura: estimar de verdad el residuo completo R. **[AUSENTE]**.

A8. **Bounds separados de orden constante en lugar del balance firmado** (061: la cancelación es a 10^{−10};
ERR<−0,66 perdía el beneficio). **[PRESENTE]** genéricamente en RULES_AVOID B2.

A9. **Herencia de pares a triples y de concavidades a cuatro nodos** (003 §4: L creciente y L/s decreciente
no bastan para tres; 084 §4: R=1+x−x²/16 conserva RS=x, concavidades y triples pero det K_4<0). Reapertura:
un resto de signo preservado por la eliminación (E) (003), o la condición cuantitativa TURAN (084).
**[AUSENTE]** (la memoria de las reglas del proyecto cita 084 sólo para los Pfaffianos por reciprocidad).

A10. **Extender a la dimensión siguiente** los cierres de 4, 5, 12, 13 polos por extrapolación de márgenes
(009 §7, 010 §5, 050 §7, 053 §5) y declarar positivos todos los segmentos iniciales de E2 (051 con el
falsificador n=2^17, F=(s²−¼)/(s+u)^n, E2[QF]<0). **[PRESENTE]** como D2 («extender la torre de órdenes
finitos»); el falsificador E2 **[AUSENTE]**.

A11. **Ensamblaje de certificados PSD de soporte ≤k fijo** en la base de potencias (FIXED_BLOCK_ASSEMBLY).
Reapertura: otra base, bloques de tamaño creciente, complementos de Schur, parte PSD global densa.
**[PARCIAL]** RULES_AVOID D12 lo nombra sin condición de reapertura.

A12. **Monotonía uniforme en dimensión del cociente ARCH+POLAR al aumentar polos** (007, n=2^17).
Reapertura: transporte que preserve sólo el signo. **[AUSENTE]**.

A13. **Monotonías individuales (incluida monotonía completa en x=p²) ⇒ TP2** de la familia de Green
balanceados (111). Reapertura: usar la compatibilidad real J′=−tΦ, K″=aΦ−J o MIXED4. **[AUSENTE]**.

A14. **Modelo hiperbólico y transferencias** (HYPERBOLIC §§7–13): mezcla positiva y convolución positiva
(§7), flujo de escala −a∂_aK_a (§9), prefactores fijos con potencial escalar, deriva escalar/matricial,
dimensión infinita simétrica (§§10–12.4), métrica local para la realización theta (§12.7), productos cosh
con o sin desplazamiento y escala variable (§§11, 13). Reapertura declarada: métricas no locales o no
acotadas con identidad Green positiva, conexiones nuevas, prefactores dependientes de b, observaciones no
continuas, otras frecuencias base, sumas/cocientes/potencias reales, comparaciones relativas de formas.
**[PRESENTE]** en B4 («211/HYPERBOLIC §§6–13»), D15 (§12.7) y C1 («cierres por productos cosh»); el flujo de
escala §9 y la familia de cierres §§10–12.4 **[AUSENTE]** como entradas explícitas.

A15. **Inferir densidad o masa de dos masas escalares** (027 DISCRETE §1: un bump cerca de 3/2 donde Ω<−0,1
puede llevar la masa). **[AUSENTE]** (menor).

A16. **Positividad en codimensión uno implica bloque** (051, ZERO13: el acoplamiento de Schur no se
controla). **[PARCIAL]** D5 trata «Monotonías Schur–Green», no este acoplamiento.

A17. **Capas PSD de la desintegración Gram** (GRAM_SLICES_AUDIT). **[PRESENTE]** vía D16/memoria de
las reglas del proyecto.

Observación sobre D7 de RULES_AVOID («Variantes del presupuesto 022»): en este rango `POWER_INVERSE_INTERIOR_022`
es un falsificador puntual, no un presupuesto; la referencia de D7 parece apuntar a CUMULATIVE_INVERSE022
(fuera de este rango). Conviene precisarla.

## B. Resultados positivos PROVED, con alcance exacto

B1. Identidades exactas de filtros (016): W[f]=W[Qf]+W[Lf], binomial, (−1)^rΔ^r W[Q^kf]=W[L^rQ^kf], para f
racional causal, polar incluida.
B2. Mezcla geométrica y continuidad (015 GEOMETRIC): W continua en X=H^t∩L²(e^{ηy}); para todos v_j≥u>1,
W[f]=Σw_kW[Q^kf_0], w_k≥0, Σw_k=1: la positividad de toda la órbita Q^kV_N basta para todos los N polos ≥u.
B3. Eventualidad (015 HIGHPASS): para N fijo existe K_N independiente de P con W>0 en Q^kV_N, k≥K_N.
B4. Corte efectivo (054): W[Q^jF_0]>‖·‖² para todo P, todo n, j≥K(n) (entero explícito enorme). COEFF/EVAL.
B5. Corte arquimediano lineal (051): para todo n y j≥⌈7n/6⌉, ARCH>859/800 (sólo ARCH).
B6. Fila N=1 (017): W[h_k]>(4/3)‖h_k‖², todo k≥0, u≥63/2; WR y WRN (normas ponderadas uniformes en k).
B7. Puente escalar Bernstein (AUDIT_017): si todos los átomos W[h_{N,k}]≥0 entonces W≥0 en todos los
numeradores (reducción a la tabla escalar); cono cuadrático explícito W>(49/50)‖f‖² para N≥2, k≥10000N²,
P=1.
B8. Región de átomos (034): W[f_{N,k}]>‖·‖²/40 para N≥3, k≥1, u≥63/2, u²≥225N/4; filas 3≤N≤12 en u=63/2
para todo k≥0; filas 3≤N≤8 uniformes en u≥63/2.
B9. Dimensión fija, todas las tasas ≥63/2 con repetición: 4 polos W>(2/25)‖·‖² (009); 5 polos
W>‖·‖²/100 (010); 12 polos W>‖·‖²/10000 (050); 13 polos W>‖·‖²/4000 y 14 polos con D(0)=0
W>‖·‖²/1000 (053).
B10. Escalera de potencias: mezclas de X^{−32},…,X^{−37} (003, órdenes 1–6); cuatro potencias arbitrarias
a_i>1 (085, vía T_R,T_S>0 global, Rolle 084, factorización 083); T_h>0 para todo x>0 y todos los triples del
resto G_p PD, bloque auxiliar anclado de cinco nodos PD (099; no son cinco generadores admisibles).
B11. Átomo (129,0): 1,34·10^{−10}<W[g_129]/‖·‖²<1,35·10^{−10} (061).
B12. Balances parciales firmados: OMEGA-TAIL y JOINT-TAIL (027); BLOCK ∫_1^{9/4}G_NH>1/100, N≥2^{20} (030);
SHARP-GAP (030); PEAK y BUDGET (031); BAND, N≥2^{80} (041); DILATE/SIGNED/WINDOW (037); SHOULDER y TAIL:
h_N,K_N>0 para x≥e^{T_N}, N≥4·10^6 (039); ψ_Λ(x)≤2x (039).
B13. Modelo hiperbólico (HYPERBOLIC §§5, 8): kernel [M_a(u_i)+M_a(u_j)]/(u_i+u_j) PSD en todos los
tamaños para φ_a y su extensión Robin; realización explícita (§12.6) de Q,B,C,D con observación continua
exacta de q_θ y ecuación fuerte para Y_ν. No transferido a Φ.
B14. Densidad (094): distancia exacta, BINOMIAL-DET, criterio DIAGONAL-DENSITY.
B15. Herramientas: lema (G) 0≤τm′(τ)<4 y polar exacto P_n(u) (007); identidad de transporte con déficit
(009/010); PF-DET y criterio de Rolle (084); JAC (049, documento superado).

## C. Obligaciones OPEN como enunciados matemáticos

C1. **Segmento inicial de la órbita high-pass.** Para todo n≥1, todo P real con deg P<n y todo
0≤j<K(n): W[Q^jP/(s+u)^n]≥0 (o, por B2, para un N fijo, para todos los j<K_N). Intentado: eventualidad
(015), cortes efectivos (049, 051, 053, 054), descenso binomial (016), uniones densas (AUDIT_016, 094).
C2. **Escalera de potencias en todos los órdenes.** [ (L(32+i)+L(32+j))/(63+i+j) ]_{0≤i,j≤m} ⪰ 0 para
todo m; equivalentemente |α_r|<1 para todo r en la recurrencia (E) de 003. Intentado: eliminación (003),
pares/triples/cuatro (084, 085), Turán T_h (097–099); obligaciones pfaffianas de orden ≥5 y herencia al
siguiente resto abiertas.
C3. **Tabla escalar completa.** W[h_{N,k}]≥0 para todo N≥1, k≥0 (h_{N,k} con Laplace s^k/(s+u)^{N+k});
cubiertos N=1, N≤17 con k≥1 (y otras filas), el cono k≥10000N² y la región u²≥225N/4. Falta el interior
N≥18 con k<10000N², y k=0 para N≥13 a tasa fija.
C4. **Balance interior gamma** (átomo k=0): para N grande, ∫_1^∞G_N(x)H(x)dx≥0 con H de 030; quedan
∫_{9/4}^∞G_NH (030), ∫_1^{4096}K_NΩ (027), E_ν[I_*(e^t)]>M_2/R(T_N) (031), el complemento de la banda
[e^T,e^{T+L}] (041), la suma firmada FULL Σ_{(m,Q)=1}μ(m)K_{N,Q}(m) (037) y la región interior x<e^{T_N} del
inverso (039). Forma equivalente: G_W(m_N)+∫_0^∞L_N(a)G_W″(a)da≥0 (027).
C5. **Propagación en N** del balance firmado con precisión relativa al residuo (061, 062): estimar R (orden
0,03) y W (orden 10^{−10}) sin sumar cajas independientes.
C6. **Transferencia del modelo hiperbólico a Φ**: una métrica (no local o no acotada) y una identidad de
Green positiva que reproduzca la forma completa a partir de la realización 12.6.
C7. **Dimensión arbitraria de polos**: W>0 en todos los espacios de n polos ≥63/2 para todo n (y 14 polos
con numerador general).
C8. **Densidad + continuidad**: envolvente lineal de uniones de bloques positivos y continuidad de W en la
topología usada (094); cruces entre bloques.

## D. Objetos o ideas mencionados como no iniciados o no examinados

D1. ORIGIN-HANKEL «no se inició ese cálculo aquí» (097) — ejecutado después en 098.
D2. Ruta larga E_{2,3} (NEXT) del plan 050: «no se ejecutó»; superada.
D3. Topologías donde los momentos ℓ_r no son continuos (AUDIT_016 §3): no examinadas.
D4. Otras agrupaciones o estimaciones firmadas del complemento Möbius (037 §8): «no se excluyen».
D5. Otras representaciones afines distintas de 042 (062): no examinadas.
D6. COMPLETE-MONOTONICITY para las densidades reales de 103: «no se ha demostrado ni refutado» (111).
D7. Si un factor cosh aislado (con o sin desplazamiento) preserva PSD del kernel: «no se ha demostrado ni
refutado» (HYPERBOLIC §§11, 13).
D8. Métricas no locales o no acotadas, conexiones nuevas, prefactores dependientes de b, sistemas no
simétricos, observaciones no continuas para la realización 12.6 (HYPERBOLIC §§12.4–12.7).
D9. Escalas base de frecuencia variable, potencias reales, sumas y cocientes de productos cosh (§13.1).
D10. Signo global del Wronskiano temporal de densidades 093/095 (097, 099): no usado ni probado.
D11. Signo para todos los numeradores en el cono cuadrático (AUDIT_017 §8): no afirmado.
D12. Un bound de operador de correlación distinto del mayorante de Cauchy de la cola desde 3 (053 §1):
«no excluye otro bound».

## E. Cobertura

Rango: los `.md` de `phase-211-sign-sandbox/` en orden de `ls *.md | sort` desde `POWER_DESCENT_016.md`
hasta `POWER_INVERSE_INTERIOR_022.md` inclusive, excluidos `POWER_GLOBAL_ROUTE_REVIEW.md` y
`POWER_GRAM_SLICES_OBSTRUCTION.md`: **61 archivos**. Leídos íntegramente: **61/61** (incluido
`POWER_HYPERBOLIC_MODEL_GRAM.md`, 966 líneas, en dos tramos completos). Ningún archivo ni tramo del rango
quedó sin leer. Se leyeron además, para notación, `RULES_AVOID.md`, `OBJECT_SPEC.md`, `STATEMENT_001.md`,
`POWER_CONE_001.md` y `POWER_BRIDGE_002.md`. No se leyeron los verificadores `tools/*.py` ni los archivos
citados fuera del rango (p. ej. 018–026, 032–033, 042, 073–096, POWER_STATE_*); sus contenidos sólo se
reflejan tal como los citan los archivos leídos.
