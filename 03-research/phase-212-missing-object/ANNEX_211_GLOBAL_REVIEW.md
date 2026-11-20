# Anexo — Lectura completa de `phase-211-sign-sandbox/POWER_GLOBAL_ROUTE_REVIEW.md`

Fuente: `../phase-211-sign-sandbox/POWER_GLOBAL_ROUTE_REVIEW.md` (2611 líneas, leídas todas, 1–2611).
Notación: la de `POWER_CONE_001.md` y `POWER_BRIDGE_002.md` (kernel de potencias
K(u,v)=(M(u)+M(v))/(u+v), M=Z'/Z, kernel temporal A(t,s)=∫_0^∞(t+s+2r)Phi(t+r)Phi(s+r)dr,
W la forma completa). «GRAM» = `POWER_GRAM_SLICES_OBSTRUCTION.md`, «HYPER» =
`POWER_HYPERBOLIC_MODEL_GRAM.md`, «BPY» = ley de la densidad theta como suma de exponenciales
de tasas πn². Etiquetas copiadas tal como figuran en la fuente. «Reutilizable» indica si el
resultado es positivo (una identidad o un signo demostrado utilizable como pieza) y su alcance exacto.

Este anexo no modifica ninguna fuente. Una entrada «NO-GO» de la fuente se refiere sólo a la clase
declarada en ella.

---

## Parte I. Entradas por sección, en orden de archivo

### 0. Encabezado (L1–3)
- Objeto: auditoría transversal de mecanismos globales fuera de la torre Schur.
- Resultado: «revisión estratégica y descartes de clases concretas, sin nueva prueba de positividad
  global. Signo global OPEN». REF-D identifica una obligación interna, no imposibilidad.
- Reutilizable: no.

### 1. «Cobertura comprobada y límites» (L5)
- Objeto: alcance de la búsqueda (índices, grid, crucigrama; lectura selectiva).
- Resultado: no es auditoría exhaustiva; WM y 112 activados mediante cobertura 110 y cola 104 desde 16;
  programa 110 INCONCLUSO respecto de su objetivo hasta 64. No se propone otra cadena de órdenes finitos.
- Reapertura: —. Reutilizable: no (estado documental).

### 2. «1. Gram y sumas de cuadrados que incluyan la aritmética completa» (L11)
- Objeto: identidades de multiplicadores + Bochner/Cauchy–Schwarz; SOS aritmética pura (N019).
- Resultado: SOS puramente aritmética imposible para T ≥ log(3)/2 (átomos negativos exigen masa
  diagonal ≥ A_T); «NO afecta a toda suma de cuadrados mixta». Parte positiva libre = clase dual
  (reducción, no imposibilidad).
- Resto sin signo: la factorización conjunta.
- Reapertura («Cambio admisible»): construir explícitamente una factorización conjunta de la medida
  arquimediana y TODOS los contactos, con control uniforme de términos y Tate, sin postular que la parte
  libre sea positiva.
- Reutilizable: no (descarte de clase + obligación).

### 3. «2. Transferencia aritmética exacta y casi coincidencias» (L19)
- Objeto: descomposición Arch−Div−Near de la matriz del perfil suficiente.
- Resultado: Near no tiene signo separado (resto de resolución finita del producto con la convolución
  divisoria); progresiones como propiedades de clase son estables bajo modificación finita. Corrección
  lógica de TB3-neg(ii): la exclusión alcanza sólo premisas estables por borrado.
- Reapertura («Cambio necesario»): desigualdad FIRMADA conjunta entre Arch y los términos m≈kn, uniforme
  en vectores y tamaños del portador suficiente, que conserve fases y bordes. Reescribir como convolución o
  estimar Near en valor absoluto no cuenta. «Obligación sustantiva viva».
- Reutilizable: no.

### 4. «3. Primer contacto, continuación y defectos globales» (L29)
- Objeto: entrada de un contacto, continuación positiva; defecto global no lineal (fase 197).
- Resultado: la auditoría exige etiquetar 197 como **PROVED reduction**, no NO-GO universal; corrige
  factor 2 de la métrica. La cota de margen demostrada es exponencial simple; no se usa un patrón
  doble exponencial como barrera probada.
- Resto: el acoplamiento collar/campo exterior en el cruce.
- Reapertura: mecanismo que pruebe un bound firmado del extremo o del resto del camino, o una
  obstrucción estructural independiente al cruce.
- Reutilizable: no.

### 5. «4. Densidad, descenso y una cota inferior uniforme» (L37)
- Objeto: unión diagonal filtrada a tasa fija (094/096), puente 002, descenso 036.
- Resultado: densidad L² sólo si liminf r(n)²/n = 0 (094); 096 mantiene distancia positiva a un
  exponencial fijo. Aunque se probaran todos los cruces, el puente 002 falla: ell0(h)=∫h se anula en TODO
  highpass r≥1, su span y su cierre fuerte; el objetivo primitivo h=(1/4−D²)g tiene ell0=∫g/4>0. Falta un
  bloque que repare ese momento. «Aclaración deductiva 016+002, no un nuevo NO-GO».
- Resto (descenso 036): energía completa; el cono conocido aporta O(log L/√L), el complemento conserva
  el valor inicial.
- Reapertura («Input suficiente»): cota aritmética uniforme R_L ≥ −ε_L, ε_L→0; o una familia de
  subespacios conjuntamente positivos que aproxime en una topología donde W sea continua.
- Reutilizable: sí, la cota |ell0(Zrho)| ≤ ζ(5/4)/√(3/2)·‖rho‖_B (de BRIDGE002 B1), como herramienta.

### 6. «5. Un par representante positivo que dé un lower» (L45)
- Objeto: representante par (045).
- Resultado: la reparación PAR compacta de un símbolo con cola fija falla en la clase 045 (reparación
  nula forzada); subcaso no compacto con exterior finito firmado recupera el dual. No es NO-GO de todos
  los pares positivos.
- Reapertura («Cambio admisible»): representante real positivo con corrección no compacta, identidad en
  todo el portador y control exacto (o coste) de la coincidencia aritmética interior, uniforme en T.
- Reutilizable: no.

### 7. «Estados obsoletos detectados» (L53)
- Objeto: filas 06 O-151.4 y 06R4 del índice.
- Resultado: corregidas; «ya tratada; no mecanismo nuevo con aquellas hipótesis»; 197 son reducciones.
- Reutilizable: no.

### 8. «Conclusión operativa» (L58–85)
Subentradas (todas resumen resultados de GRAM):
- HK ≥ J²: GRAM §12 lo prueba (convexidad global del recíproco temporal r/V'(r), cola analítica y
  certificado compacto); positividad de triples temporales simétricos suficientemente pequeños.
  **Reutilizable** (alcance: triples pequeños; no global, no nueva T).
- Límite §13: contramodelos C⁶ con convexidad recíproca y V'''>0 cuyo kernel falla en algún tamaño. No
  usar esas hipótesis como base de inducción. Extensión de triples a todo R, monotonía del cociente
  normalizado y conservación por Schur: sin prueba.
- §14: no hay extensión holomorfa de q(u)=√u/V'(√u) a Re u>0 ⇒ no hay representación Laplace positiva
  de q (descarte).
- K_Phi ≥ εK_0, modelo a=2π: posteriormente REFUTADA para todo ε>0. No relanzar suavizado,
  Cauchy–Schwarz ordinario o el menor negativo en ε=1.
- Matriz (S): potencial positivo sobre cuadrados firmados = comparación absoluta CA_K_001.
- Agrupar nodos próximos en log m: la doble cancelación lleva cruces al kernel −B''; sin desigualdad
  relativa para esos cruces; «No hay NO-GO general para agrupamientos».
- GRAM §§16–17: principal del A completo en escalas enteras fijas = matriz gcd, límite no uniforme
  (§16.5); parte resonante EXACTA R_res admite SOS de todos los órdenes, válida en y=0, con margen
  uniforme respecto de su energía divisorial (§17.5). **Reutilizable** (positivo auditado; sólo R_res).
- Obligación restante: Off no admite cota inferior uniforme por múltiplo finito de la energía
  divisorial; A no domina fracción fija de R_res (§17.6, incluye y=0); §17.7 descarta pagar el operador
  de dilataciones con la energía física ponderada por 1+log t. «La desigualdad crítica conjunta, sin
  margen adicional, sigue abierta.»
- Puente §18: PSD de A COMPLETO en y=0 sobre todos los bloques de escalas enteras ⟺ PSD sobre todos los
  nodos reales ⟺ (§18.9) λ_A(T) ≥ 0 para TODO T. **Reutilizable** (reducción exacta PROVED).
- §§19.7–19.9: Q(E1) > 1/2000; plano span{E1,E2} firmado: Q11>179/100000, Q22>17/10000,
  |Q12|<79/50000, detQ>2733/5000000000 (certificado FULLPASS). Q_B(E1+E2)<−1/20000. **Reutilizable**
  (sólo ese plano). Core §19.8: firmar TODOS los Gram de E_j=p(t)(t−1)q_j(t) ⟺ objetivo para todas las
  ventanas.
- §19.10 (alcance PROVED): para cualquier J≥1 FIJO, firmar todos los bloques de E_j, j≥J ⟺ objetivo
  global (restricciones P(1)=0, ∫t^kP=0, k<J). No uniformidad en J. **Reutilizable** (reducción).
- §19.11 (PROVED, aplicación de 008): Q0 sobre p0R, p0=exp(−πt), con log t y Lg pero sin C, NO es PSD
  aun con R(1)=0 y ∫pR=0. No refuta Q completo.
- §19.12 (PROVED elemental): J*Theta(exp 2r)=2g(r)−4rPhi(r), g=−∫k(r+s)Phi(s)ds; potencial
  ∫Phi g|f|² de la identidad de diferencias NO es globalmente favorable: g(log2+)<−19/300; existe
  combinación exactamente primitiva con V<0. No demuestra Q/A negativo.
- Control §18.5: con u=½log t, la forma completa vuelve a W causal de CONE001/SHIFT§2/fase 199;
  kernel 4cosh(h/2)−2e^{−h/2}/(1−e^{−2h}); C0=ψ(1/4)−log π. «No relanzar sólo Mellin o ese cambio de
  variable como mecanismo nuevo.»
- Componente común y contrastes: separar un rango uno evita la clase de soporte fijo pero no prueba;
  cercanía a la matriz de unos no controla contrastes; THREE002 §7 (dimensión fija, tasas grandes) no
  es avance.
- Conclusión: obligaciones legítimas = factorización mixta explícita, balance aritmético conjunto, cota
  unilateral uniforme de un resto, representante positivo completo. «Otra representación», «no
  lineal/global» o nueva dimensión no bastan.
- Reapertura general: «una estimación firmada adicional concreta, no repetir el cambio de variables,
  de normalización o de base».

### 9. «Auditoría posterior: Gram theta por capas» (L88)
- Objeto: candidata A con doble transformada y modelo cuártico Gram de todos los tamaños.
- Resultado: certificación capa por capa PSD falla para Phi real (CND y crecimiento de V'). No decide A.
- Subentrada paridad/modularidad: sectores par e impar dan [S(x)−S(y)]/(x−y) y uv[N(y)−N(x)]/(x−y);
  pedir ambos PSD vuelve a la obligación Stieltjes/diferencias divididas de 083. Modularidad del producto
  theta completo no se reparte por modo; pares de modos conservan cruces. «Estas dos propuestas no
  justifican por sí solas reabrir.»
- Resto: compensación entre capas sin cota conjunta.
- Reutilizable: identidad de sectores par/impar (exacta, sin signo).

### 10. «Revisión aritmética posterior: celdas y división euclídea» (L97)
- Objeto: ledger, SPEC_B, EI_002, CA_M.
- Resultado: el ledger identifica coeficientes, no desigualdad; EI_002: tras cortar y≥1 hay salto y
  borde; Poisson no es absolutamente convergente sin ellos. Error concreto en L2_BUILD_031 §3 (B_Q no
  elimina componentes pequeñas; ejemplo M=Q=2, s=(1,1), componente q2=v2/2>0); Teorema E sigue válido.
- Reapertura (gate): factorización conjunta positiva que empareje defecto de divisor pequeño y borde de
  segundo orden, conservando y=1, cambios de cociente y extremo de truncación.
- Reutilizable: no.

### 11. «Complemento del análisis de densidad: reparar el momento no paga los cruces» (L106)
- Objeto: DESCENT_AUDIT016 §9, Qδ=(s+1)/(s+63/2) invertible en H_{3/4}.
- Resultado: span de cualquier cola de generadores es denso y diagonales eventualmente positivas aun para
  W4=W−4‖·‖², pero W4[f0]<0 ⇒ alguna combinación finita negativa. Falsifica sólo la inferencia «densidad
  + positividad individual ⇒ signo».
- Resto: los cruces. Reutilizable: no.

### 12. «Límite de ensamblar certificados PSD pequeños» (L111)
- Resultado: ningún tamaño fijo k de soportes coordenados PSD basta para la escalera 002 (condición
  1ᵀC1 ≤ k·trC falla en bloques tardíos → matriz de unos de tamaño k+1). No excluye bases adaptadas,
  bloques crecientes, Schur ni parte positiva global.
- Reutilizable: no.

### 13. «Diferencias en exponentes: identidad digamma no implica orden de bloques» (L116)
- Resultado: refutado el orden universal K−K_shift (shift 2), incluso en bloques iniciales; orden inverso
  falla por la diagonal 073. Reparación IMS literal (SHIFT §7): resto con ambos signos; coeficiente
  d/(1−TtTs)→1 cerca del eco causal (0, log2).
- Reapertura: reparación distinta con coste independiente demostrado.
- Reutilizable: no.

### 14. «Aclaración del objetivo Stieltjes: la derivada L' en a no tiene medida Laplace positiva» (L124)
- Etiqueta: **PROVED**.
- Objeto: L'(a)=∫e^{−at}b(t)dt+ΣΛ(n)log n·e^{−a log n}, b(t)=t[1/(e^{2t}−1)−e^t].
- Resultado: b<0 en (log2, log3) sin átomos ⇒ NO existe representación L'(a)=∫e^{−at}dν, ν≥0, en
  NINGUNA raya de a>1 (unicidad de momentos/Bernstein).
- Alcance: no dice nada de N(x)=M(√x)/√x; el objetivo anti-Löwner/Stieltjes de 083 sigue OPEN.
- Reutilizable: sí como descarte (L' exacta, toda raya).

### 15. «Deduplicación exacta de la subordinación gaussiana de N» (L145)
- Resultado: la fórmula N(x)=∫e^{−xv}[H_A(v)−P(v)]dv, x>1/4, ya está en E101_036 §§1–3; obligación:
  signos alternados de TODAS las derivadas de H_A−P (orden 0 no basta). Revisión del resto:
  H_A−P=B(v)+R_v, R_v=(πv)^{−1/2}∫_1^∞E(x)w_v'(x)dx, B(v)=[1+m(0)/2]/√(πv)+O(v^{−3/2}), m(0)=ψ(1/4)−log π<−2
  ⇒ B eventualmente negativa; el resto firmado debe compensarla.
- Reutilizable: identidad con borde explícito (sin signo).

### 16. «Transferencia comprobada a los inversos gaussianos» (L154)
- Resultado: mezcla REAL027 con Fubini absoluto: h_N(1)=E h_{VN}(1), K_N(1)=E K_{VN}(1); los
  certificados 128/129 fuerzan alguna gaussiana con h_a(1)<0 y alguna (quizá distinta) con K_a(1)<0.
  «La positividad inversa universal gaussiana no puede servir de premisa.»
- Reutilizable: no.

### 17. «Revisión del presupuesto022: alcance y antecedentes antes de reabrirlo» (L158)
- Resultado: «No hay nuevo teorema ni NO-GO». Para k=0 la obligación es A_N+2∫K_N C_B ≥ 0; ∫K_N C_B ≥ 0
  solo no basta (A_N límite negativo, LOW_TABLE018); SCALAR_BRIDGE017 exige todos los pares (N,k).
  K_N M dt es firmada; GAMMA_AFFINE_BALANCE062 muestra déficit de la parte afín.
- Reapertura: «desigualdad independiente que pague también ARCH_sharp y una justificación de su alcance
  en k».
- Reutilizable: no.

### 18. «Balance de la rama hiperbólica: todos los órdenes en un modelo, transferencia real abierta» (L166)
- **PROVED para el modelo:** phi_a=exp(−a cosh 2t): operador H=−d²/dr²+a²e^{2r} independiente de u, Green
  ⇒ Gram de (M_a(u)+M_a(v))/(u+v) en toda dimensión; extensión Robin phi_{a,β}=(β+a cosh 2t)phi_a.
  **Reutilizable** (sólo modelos).
- Descartes: Phi no es mezcla positiva pura de exp(−a cosh 2t) ni convolución de un modelo fijo con medida
  positiva finita (§7); −a∂_aK_a no PSD (§9).
- OPEN: deformación por Phi/phi_{2π} introduce fuente; residual de rango uno asintótico, nulo en
  contrastes. §10: absorción de la fuente en potencial escalar independiente del parámetro obliga prefactor
  constante.
- Reapertura: «una operación preservante aplicable a la Phi real o una estimación independiente de toda la
  corrección, válida para cualquier dimensión».

### 19. «Relectura del puente escalar: preservar la obligación promediada» (L182)
- Resultado: u^{2N}W[h_{N,k}]=Σ_j(−1)^j C(k,j) b_{N+j}: pedir esos signos es la misma obligación. Basta
  el PROMEDIO firmado R_L ≥ −ε_L, ε_L→0 para cada entrada inicial (no cada átomo). R_L=A_{N,k}−C_L, C_L→0
  no prueba la cota.
- Reutilizable: no (precisión de la obligación).

### 20. «Estado consolidado del núcleo temporal y de las truncaciones theta» (L189)
- Resultado: PSD del kernel transformado ⟺ PSD temporal (cota gaussiana); por holomorfía basta PSD en
  cualquier intervalo abierto (GRAM §2.1–2.2). **Reutilizable** (principio de continuación).
- Descartes: cada modo, TODO prefijo theta finito, cortes suaves positivos con Σw_n n² finita fallan PSD en
  cualquier intervalo; añadir cola continua falla para M grande; simetrizar falla para todo M.
- Decisión: no usar pequeñez puntual de la cola ni un número fijo de derivadas como transferencia.

### 21. «Deduplicación de la primitiva theta: conservar el borde antes de transformar» (L197)
- Resultado: Phi=(D²−1/4)q/2 (E101_070 §4); Z_Phi(u)=1/4+(u²−1/4)∫_0^∞q cosh(ut)dt (afín, no producto);
  g=2e^{−|·|/2}*Phi, Z_g=2Z_Phi/(1/4−u²); K_g−K_Phi=2(1/4−uv)/[(1/4−u²)(1/4−v²)] indefinida (det de dos
  nodos −(u−v)²/…<0). Sin orden PSD entre los dos kernels.
- Reutilizable: identidades (sin signo).

### 22. «La primitiva regularizada tampoco es un núcleo temporal PSD» (L216)
- Etiqueta: **PROVED**. U=2cosh(t/2)−F=2g; (4/5)e^{−t/2}<U<e^{−t/2}; menor de nodos (0,8) de A_U:
  det < −(124/25)e^{−8} < 0.
- Reutilizable: no.

### 23. «Transferencia multiplicativa hiperbólica: descarte previo a otro estudio de modelos» (L247)
- Resultado (HYPER §11): Phi ≠ C exp(−a cosh 2t)Π cosh(α_j t) con Σα_j² finita (a=2π, Σα_j=9/2, multiplicidad
  π−3/(2π) no entera). No excluye potencias reales, cocientes, otros prefactores ni comparaciones de formas.
- Reutilizable: no.

### 24. «Producto de Jacobi: el momento perdido impide usar sus cortes como núcleos PSD» (L253)
- Resultado: criterio GRAM §8.4 (probado/auditado): momento exponencial nulo de densidad no nula ⇒ A no
  PSD; descarta todos los cortes polinómicos no constantes en q=e^{−πe^{2t}}, incluidos Jacobi finitos.
  §8.5: simetrización de esos cortes introduce cola β=2J+1/2; dos nodos próximos dan det<0.
- Reapertura: compensación que mantenga el momento completo.
- Reutilizable: el criterio de momento nulo (herramienta de falsificación).

### 25. «Retorno a(S): conmutador divisor deduplicado y normalización corregida» (L261)
- Resultado: ZΔ=[L,Z] ya en N_BUILD_022 §1; no da cota inferior de Arch−Div−Near. Corrección de factor 2:
  D_sym es la MITAD de Div_P47; sᵀDiv_P47 s=2sᵀ(Z^{−1}LZ−L)s. NO-GO de N022 §3 queda ARGUED.
- Reutilizable: normalización corregida.

### 26. «Selberg completo: precisión de dominio al separar los cuadrados» (L267)
- Resultado: Re⟨g,B²g⟩=‖Bg‖²−½‖(B−B*)g‖²; la primera integral diverge (≥½Σ_{p≤X}log p/p); sólo la
  diferencia con corte común converge a V de 055. No refuta Selberg compensado.
- Resto: comparación conjunta con ARCH y polar. Reutilizable: no.

### 27. «La amortiguación modal débil tampoco da aproximantes PSD» (L282)
- Resultado: phi_δ=Σn^{−δ}Phi_n no PSD para TODO δ≠0 (GRAM §8.6); ∫e^{t/2}phi_δ=0 frente a 1/4 para Phi.
- Reutilizable: no.

### 28. «Auditoría de residuos abiertos: suficiencia y antecedentes» (L288)
- Resultado: corrección de 06: R172_CAND conserva dos obligaciones; ROUND026 no certifica el bloque polar.
  (N) es objetivo suficiente con estimación firmada conjunta pendiente; R8 necesita portador positivo
  independiente + identificación con dominios; R10 sin desigualdad concreta.
- Reapertura: Arch−Div−Near por Poisson/divisores, familia s_w, colas con gauge, patrones near: sólo con
  «hipótesis nueva explícita que resuelva su fallo identificado».
- Reutilizable: no.

### 29. «Comparación aditiva hiperbólica: dos condiciones necesarias sin falsificador» (L294)
- Estado: comparación K_Phi−K_{2π} posteriormente FALSIFIED (§33). Conservado: x·N_diff(x)=9/4+(3/16−2π²)/√x+…;
  test Jensen n0 ≥ (9/4)C^{8/9}; diagnóstico NUMÉRICO (n0≈0.00915 > umbral≈0.00555).
- Reutilizable: no («No relanzar esta comprobación como construcción»).

### 30. «Interpolación geométrica: filtro de antecedentes y obligación exacta» (L315)
- Objeto: phi_s=phi_0 e^{sh}, h=log(Phi/phi_0); ∂_sK_s=[Cov_{s,u}(t,h)+Cov_{s,v}(t,h)]/(u+v).
- Resultado: PSD de la derivada para cada s es MÁS FUERTE que la integral; contraejemplo de modelo
  h=a cosh 2t (derivada −a∂_aK_a no PSD). Precisión de alcance: el falsificador no excluye una cota
  RELATIVA ∂_sK_{s,U} ≥ −C_U(s)K_{s,U} con C_U integrable para cada lista finita U (Grönwall; constantes
  dependientes de U bastan).
- Estado: interpolación y comparación integrada OPEN.
- Reapertura: propiedad específica de h que dé la cota relativa y su integrabilidad sin suponer el signo.
- Reutilizable: identidad de covarianza (sin signo).

### 31. «Covarianza divisorial agrupada: los coeficientes tienen ambos signos» (L328)
- Etiqueta: **PROVED**. C_s(n)=Σ_{dm=n}μ(d)log m(gcd(d,m)^s−1); C_s(p²)=−(p^s−1)log p<0;
  C_s(p²q²)=(B−1)(A−2)log p+(A−1)(B−2)log q>0 si p^s,q^s>2 (p=5,q=7 en s=1/2).
- Falsifica sólo el signo uniforme de los COEFICIENTES. Reutilizable: no.

### 32. «El resto divisorial es indefinido incluso sobre tests pares primitivos» (L351)
- Etiqueta: **PROVED**. R(F)=Σn^{−1/2}C_{1/2}(n)Re c_F(log n). Tests palindrómicos con c₊=(1,−5/2,1),
  c₋=(1,−3/2,−1/2,−1/2,−1/2,−3/2,1) (ambos momentos nulos, T=3log4+ε): R(F₊)=(7/4)κ‖g‖²>0,
  R(F₋)=−(1/4)κ‖g‖²<0, κ=(√2−1)log2.
- Descarta usar R o −R como pieza positiva aislada. No refuta compensación con ARCH. Reutilizable: no.

### 33. «Comparador Robin ajustado: falla ya en pares lejanos» (L390)
- Etiqueta: **PROVED**. M_*=wbM_{a,β}(bu), w=7/2, b=2/7, a=4π/7, β=4π²/49−33/392; D=M_Phi−M_*=d/u³+…, d>0;
  det K_D|_{(u,2u)}=−5d²/(64u⁸)+…<0.
- **Filtro general reutilizable (PROVED):** si D=o(1/u) en una semirrecta y K_D es PSD en todos sus pares,
  D≡0. **Reutilizable** como filtro de comparadores.
- Diagnóstico NUMÉRICO N_Phi(0)−N_*(0)≈0.00454>0 (no interviene).

### 34. «Comparador asinh: menor confluyente negativo certificado» (L428)
- Etiqueta: **PROVED con certificado de intervalos**. M_0=½asinh(u/4π): K_0 PSD (resolventes positivos).
  Jets J=[[n10,n11],[n11,n12]] de N_D: det J ∈ [−1.684,−1.683]·10^{−57}<0 (SHA dff604bc…).
- Resultado: K_Phi−K_0 NO PSD (y en ningún intervalo abierto, por GRAM §2.2). Reutilizable: no (descarte);
  la positividad de K_0 sí es un modelo PSD explícito.

### 35. «Comparación hiperbólica original: resto indefinido certificado» (L467)
- Etiqueta: **PROVED con certificado de intervalos**. det J ∈ [−3.307,−3.306]·10^{−59}<0 (SHA 6749a763…).
- Resultado: K_Phi−K_{2π} no PSD (ni en intervalo abierto). K_{2π} sigue PSD. Reutilizable: no.

### 36. «HCM, reciprocidad y supercolas no bastan para el kernel logarítmico» (L496)
- Etiqueta: **PROVED**. Contramodelo f_ε=C(1+x)^{−2}exp[−ε(x+1/x)], ε=2^{−100}: HCM, recíproca, todos los
  momentos Mellin; κ4>0 ⇒ det K|_{(h,2h)}=−(κ2κ4/6)h²+…<0.
- Alcance: refuta la suficiencia de HCM+reciprocidad+momentos (con paridad, analiticidad, supercolas).
  Reapertura: desigualdad adicional demostrada para el dato completo que excluya este ejemplo.

### 37. «La densidad theta en S=exp(2t) no es HCM» (L546)
- Etiqueta: **PROVED**. H(w)~(π⁴/Z0²)w^{9/2}e^{−2πw} incompatible con log-convexidad ⇒ f no HCM; tampoco
  sus tilts x^r ni escalas.
- Reutilizable: no.

### 38. «Comparaciones primitivas: transferencia analítica del descarte» (L576)
- Etiqueta: **PROVED**. **Lema:** D impar real-analítica en R, c>0: PSD de K_D sobre todos los bloques de
  un intervalo abierto I⊂(c,∞) con Σd_i/(u_i−c)=Σd_i/(u_i+c)=0 ⟹ PSD completa (CPD2 + anclas +
  continuación + masas en ±c).
- Aplicación: K_Phi−K_{2π} y K_Phi−K_asinh fallan también sobre bloques primitivos de cualquier I⊂(1/2,∞).
- **Reutilizable:** el lema (primitivo ⟺ completo para kernels de este tipo).

### 39. «Normalizar por Phi no produce una derivada traslacional positiva» (L608)
- Etiqueta: **PROVED**. B=A/(Phi(t)Phi(s)), C=−(∂_t+∂_s)B=t+s−(p(t)+p(s))B; C(0,0)=0, ∂_sC(0,0)=1−aB(0,0)>0
  ⇒ menor −C(0,s)²<0. Corolario (PROVED): ninguna normalización g par analítica repara el generador
  (C_g impar ⇒ C_g=0 ⇒ B_g=F(t−s), imposible por H(L,L)=1−1/(4L²)+…).
- Reutilizable: no.

### 40. «Generador con inclinación exponencial: diagnóstico inicial y descarte posterior» (L641)
- Estado: identidades y necesidad c≥1 PROVED; diagnóstico local NUMÉRICO (det≈+0.00789); comparación
  posteriormente FALSIFIED (§41). Identidad B(t,s)=∫_0^∞e^{−2cr}C_c(t+r,s+r)dr para c≥1.
- Reutilizable: la identidad de integración del generador (condición suficiente, sin signo).

### 41. «Cúspides modulares: ningún generador C_c con c finito es PSD» (L692)
- Etiqueta: **PROVED**. Mecanismo: PSD real ⇒ H_h(iy,−iy) ≥ 0 (jets + Taylor); en y→π/4: |Phi(iy)| ≤
  Cε^{−K}e^{−a/ε} (SMALL), |Phi(h+iy)| ≥ c0ε^{−5/2} (LARGE), A0 ≥ c1ε^{−4}, Ah ≤ C1ε^{−5} ⇒ contradicción.
- **Reutilizable:** las estimaciones de cúspide (SMALL, LARGE, A0, Ah) y el test (NEC) como herramienta de
  falsificación para cualquier kernel holomorfo en |Im|<π/4.

### 42. «Normalización por la diagonal completa: tampoco admite un generador inclinado positivo» (L770)
- Etiqueta: **PROVED**. g_c=√A(t,t)e^{ct}, todo c real; vía Schur exp(4ch)R_h²−R² y DIAG-CUSP
  d(z)=−(9/16)z_*(2i)^{3/2}ζ^{−4}+O(|ζ|^{−3}). Corolario PROVED: dividir por la theta primitiva F tampoco.
- Reutilizable: DIAG-CUSP (asintótica de la diagonal en la cúspide par).

### 43. «Gauge asimétrico de escala theta: falsificador real de dos puntos» (L843)
- Etiqueta: **PROVED**. g=exp(2π sinh 2t): nodos (−L,L), det C/P⁴ ≤ O(L²/Y)−16κ²<0. Extensión PROVED: todo a
  real en g_a=exp(a sinh 2t) (jets en −h).
- Reutilizable: no.

### 44. «Alcance de RES-SOS frente a los restos de 106_38» (L907)
- Resultado: Phi(x)=Σi^{−1/2}h_{n²i²}(v), R_n=Σ_{n∤j}j^{−1/2}h_{j²}(v): frecuencias distintas; síntesis
  bilateral con c=δ_1 da X_frac+X_ctr=0 mientras R_res[δ_1]>0. RES-SOS no firma esos restos.
- Resto: compensación conjunta. Reutilizable: identidad de perfiles (sin signo).

### 45. «Comparación hiperbólica pequeña: condición necesaria de anulación» (L923)
- Etiqueta: **PROVED como implicación**; comparación posteriormente REFUTADA. Cota ‖U_f‖_HS ≤
  ½√(Tr H^{−1})(|f(0)|+‖f'‖_{L1}); K_Phi ≥ εK_h ⟹ U_Phi=0 (vía W_Phi[Phi]=0, GRAM §19.12).
- Reutilizable: la cota HS y W_Phi[Phi]=0 (identidad física).

### 46. «Dos fases exactas no se ordenan por PSD» (L941)
- Etiqueta: **PROVED**. Promedio en θ de A_θ = R_res; D=A_0−A_π tiene D22=0, D12>0 ⇒ indefinido.
- Subentradas (L973–985), todas con alcance declarado:
  - «Cierre infinito simétrico sin deriva» (HYPER §12.2): ‖Q(v)‖²=A+c log cosh v; excluye coordenada
    continua q_θ con operadores simétricos.
  - «Extensión con deriva escalar constante» (§12.3): excluida para α≥0 y α<0.
  - «Deriva escalar variable» (§12.4): reduce a 12.3. No excluye deriva operatorial, métricas variables.
  - «Tasas móviles y puente fuerte» (BRIDGE014 §6): unión densa en H_η ⟺ limsup N/u_N=∞; a lo largo de N ⟺
    N/u_N→∞. **Reutilizable** (umbral de densidad). Falta W ≥ −ε_N‖f‖².
  - «Cola aritmética en régimen denso» (§7): |W−W_{≤⌈exp(40N/u)⌉}|<e^{−N}‖f‖² en V_N(u), u≥2.
    **Reutilizable** (control de cola). Obligación finita: lower −ε_N‖f‖² para ARCH+POLAR y contactos
    hasta exp(40N^{1/4}) con u_N=N^{3/4}.

### 47. «Phase211 — corte móvil subcrítico: umbral necesario» (L988)
- Etiqueta: **PROVED, principal truncado solamente**. Corte log Q_N ≤ (2−δ)N/u_N ⇒ W_{≤Q_N}→−∞ en un vector de
  dos coordenadas Laguerre; lower evanescente exige liminf u_N log Q_N/N ≥ 2.
- Reutilizable: umbral necesario (no signo).

### 48. «Phase211 — corte móvil insuficiente aun en primitivas» (L993)
- Etiqueta: **PROVED para W truncada, no para W completa**. N ≥ 2^{60}, log Q ≤ 2^{−12}N/u: vector unitario con
  momentos Tate nulos, f(0)=0, W_{≤Q}[f]<−3.
- Reutilizable: no.

### 49. «Cierre de la comparación hiperbólica pequeña» (L998)
- Etiqueta: **PROVED asistido: K_Phi no domina εK_{2π} para NINGÚN ε>0.** λ1 ∈ [a²+4a√3−9, 25+a²(5/4)³],
  17<ω1<41/2; certificado G(ω)<−10^{−8} en [17,41/2] (SHA cddcc0bf…); U_Phi v1=G(ω1)v1≠0.
- Subentradas: «Alcance primitivo del cierre» (por el lema §38, falla en bloques primitivos de cada
  I⊂(1/2,∞)); «Familia física primitiva» (g_R=(D²−1/4)(χ_RPhi), momentos nulos, W[g_R]→0 mientras
  2‖U_{g_R}‖²_HS → valor positivo).
- **Reutilizable:** f_*=(D²−1/4)Phi con W[f_*]=0 y la familia primitiva g_R (tests casi nulos de W).

### 50. «Phase211 — antecedente bibliográfico directo del kernel temporal» (L1052)
- Resultado: manuscrito público externo con j=A/(∫Phi)² y misma respuesta logarítmica (antecedente de
  representación). Compañero causal: majorante separado ≥[1/(r−1/2)−1/(4r)]/B0(r) diverge en r↓1/2; no implica
  divergencia de la norma real de k.
- Resto: cota uniforme de la inversa del operador causal. Reutilizable: no.

### 51. «Ramificación theta: candidata examinada, preservación OPEN» (L1060)
- Objeto: paso T'=A1T1+A2T2 (BPY), simetrización S.
- Resultado: semilla S δ_c con M=b tanh(bu) PSD (Gram explícito); diagnóstico NUMÉRICO de jets 0..4 positivo.
  Término de entropía sin signo; borde firmado (p−1)F(p)=B_1(p)−2B_{1/4}(p).
- Subentradas: pérdida de información (S δ_c=S δ_{1/c}, salidas distintas); la media fija tampoco determina
  el paso (ν con Rν=−ν, μ±); cuarto cumulante κ4_salida<−1/5000 para TODO c>0 (certificado intervalar,
  no falsifica); condicionamiento: C(u,u)=−Var_ν(h_θ)u²/2+…<0 en el segundo paso.
- Estado: preservación OPEN. Reapertura: «estimación conjunta concreta para el paso o test falsificador
  justificado».
- Reutilizable: semilla PSD (sólo la semilla).

### 52. «Fuente externa de ventana log11: CITED, pendiente de reproducción» (L1187)
- Etiqueta final (L1213): **PROVED con asistencia computacional, resultado EXTERNO reproducido**, forma
  completa W_T en ambas paridades, 0<T ≤ log(11)/2 (≈1.1989). Frontera local verificada pasa de 1.035 a
  log(11)/2. No da margen espectral ni uniformidad.
- Reapertura de ventanas: «falta una estimación estructural uniforme del bloque Schur completo».
- Reutilizable: sí (ventana certificada; no original, no para todo T).

### 53. «Resta de dos cortes suaves: principal y resto pendiente» (L1216)
- Resultado: Q_M(v)=MA(v)+(1/2π)∫Phi s_N[2Re(C_M conj R_M)+|R_M|²]; toda v suave compacta es diferencia de
  dos cortes ⇒ el principal conserva la obligación global. «Ni nueva ruta ni falsificador».
- Resto: signo del resto, cota uniforme para interpolantes dependientes de M.

### 54. «Densidad BPY: PF infinito aditivo y reciprocidad, puente multiplicativo OPEN» (L1227)
- Resultados PROVED (clásicos aplicados): Phi(½log v)=πv^{5/4}q(v), q(1/v)=v^{5/2}q(v), 2π∫q=1,
  L(s)=Π(1+s/(πn²))^{−2}; det[q(x_i−y_j)] ≥ 0 todos los tamaños (PF∞ aditivo); q_aq_a''−q_a'²<0 por modo
  (no contradice).
- Fórmula: A(t,s)=π²(ab)^{5/4}/4∫_1^∞v^{3/2}log(abv²)q(av)q(bv)dv.
- Subentradas: consecuencia del paquete −(log Phi)'' ≥ 5 (PROVED); Gamma(2) exponencial: A_a(t,t)<0 para
  t muy negativo (sin reciprocidad); aproximantes finitos simetrizados: A[S_N] no PSD y f̃_N no PF₂.
- Estado: puente multiplicativo OPEN. **Reutilizable:** PF∞ aditivo de q, la fórmula de A, −(log Phi)'' ≥ 5.

### 55. «Rigidez frente a modificaciones finitas de tasas BPY (clase delimitada)» (L1318)
- Etiqueta: **PROVED**. Modificar finitas tasas (dos copias de π intactas, resto >π) y exigir
  reciprocidad ⇒ R≡1, f=2πq.
- Reutilizable: sí como restricción (no hay otra ley recíproca en esa clase).

### 56. «Renovación aditiva BPY y mezcla recíproca: construcción, sin puente de signo» (L1368)
- Resultado: v f(v)=∫_0^v k(v−u)f(u)du, k=2Σe^{−πn²x}; P_down, P_up transiciones de masa 1; la mezcla
  equiprobable no es reversible para ninguna densidad (cociclo R(L,2L)R(2L,3L)/R(L,3L)~1/√(2L)).
- Reutilizable: identidad de renovación (exacta).

### 57. «Identidad bilineal de renovación plegada y fallo de sus capas individuales» (L1396)
- Etiqueta: **PROVED en el alcance indicado**. A(t,s)=∫∫f(u)f(w)B_ab(u,w)dudw exacta; capas simétricas
  S^{(u,w)} no PSD en cualquier intervalo de (1,∞) (det confluente −C²/δ+…). Corolario: integrar una fuente
  (C_ab(u)) tampoco: −uf(u)²(log u)²/(256δ)+…<0.
- Reutilizable: la identidad (sin signo).

### 58. «Autodescomposición BPY por escala: energía positiva auxiliar, sin transporte de la órbita» (L1460)
- Resultado: cX+Y_c ~ X; generador G con −Re∫h̄Ghf=½∫∫fρ|h(x+y)−h(x)|² ≥ 0 (PROVED); el semigrupo no
  preserva la órbita de dilataciones (Var defecto −2σ²c(1−c)(d−1)≠0).
- Reutilizable: la energía auxiliar positiva (no identificada con A).

### 59. «El presupuesto resonante exige una comparación unilateral, no una norma uniforme» (L1492)
- Etiqueta: **PROVED sólo en el alcance siguiente, y=0**. Bloques k..k+N−1, k>N²: R diagonal,
  R^{−1/2}AR^{−1/2}→J_N; refuta Off ≤ CR y |Off| ≤ CR para todo C. NO refuta H ≤ I.
- Estado: Off ≥ −R OPEN.

### 60. «Extensión factorial antes de resonancia: identidad completa con restos firmados» (L1512)
- Identidad exacta (PROVED): Q[c]=Σ_mΛ(m)‖P_mb−R_mb‖²_K+b*Db+E(b). Entradas de D positivas pero D no PSD;
  E(δ_1)<0.
- Subentradas: E no se paga sólo con cuadrados (S_sq[δ_1]=0, E<0); núcleo de S_sq = soporte libre de cuadrados
  (Q=D+E allí); en SF, Q=L+M, 0 ≤ B ≤ L (PROVED), B+M ≥ 0 FALSA (test c=(1,−1/100), cotas racionales).
- **Reutilizable:** identidad factorial, núcleo SF, Q=L+M y 0 ≤ B ≤ L.

### 61. «Escalas libres de cuadrados: aproximación de grafo y exclusión de toda fracción fija» (L1615)
- Resultado PROVED: la clausura del span de P_d, d SF de una cola, contiene todos los P_k y los compactos
  (Schwarz + Σ_{SF}1/d=∞). Q ≥ ε(L−B) falsa para todo ε>0 (familia g_R). Consecuencia: D+E no PSD sobre
  theta finitos; Q ≥ εS_sq falsa; S_sq no continua en B_a².
- Estado: Q ≥ 0 (α=1) OPEN. **Reutilizable:** densidad SF en B_a².

### 62. «Resolventes escalares del producto: la positividad por parámetros falla» (L1671)
- Resultado PROVED: A=∫_0^∞J_u du; J_u no PSD para todo 0 ≤ u<1 (diagonal límite <0); en SF finito para u
  en [0,η).
- Subentrada «Emparejamiento recíproco»: C_u=J_u+u^{−2}J_{1/u}, A=∫_0^1C_u du, C_u(x,x)>0 todo x; candidata
  OPEN; obligación: desigualdad integrada de cruces para C_u o falsificador.
- Reutilizable: las identidades (Frullani, parejas).

### 63. «Extremo recíproco C_0: positividad de todos los órdenes (no cierre de A)» (L1725)
- Etiqueta: **PROVED**. C_0=∫2sinh(2r+x+y)Phi(r+x)Phi(r+y)dr; (a+b)Ĉ_0=Z(a+1)Z(b+1)−Z(a−1)Z(b−1);
  S(a)=Z(a−1)/Z(a+1) contractiva en Re a>0 (cociente explícito con producto de Euler y Bernoulli);
  K_S PSD (Hardy) ⇒ C_0 PSD en todos los nodos reales.
- **Reutilizable:** C_0 PSD, todos los órdenes (alcance: u=0, medida cero en A=∫C_u).

### 64. «Dos transportes desde C_0 que no conservan el signo requerido» (L1778)
- Etiqueta: **PROVED en las clases declaradas**. q_u log-cóncavo ⇒ no multiplicador Schur; no existe medida
  positiva fija μ con C_u ≥ ∫C_0(x+t,y+t)μ(dt) (D_u ≤ u^{−1}e^{−2x}D_0).

### 65. «El extremo hiperbólico positivo no implica el límite lineal: contramodelo suave» (L1808)
- Etiqueta: **PROVED en clase genérica**. phi=3g+(g(t−2)+g(t+2))/2: B_1 PSD todos los órdenes, B_0 no PSD
  ((42,−41)K(42,−41)ᵗ=1−516/(34ℓ)<0).
- Estado: descenso para theta OPEN (requiere hipótesis o identidad adicional).

### 66. «PF aditivo e inversión: defecto exacto de la composición por contracciones» (L1859)
- Etiqueta: **PROVED en la clase declarada**. V_λ no contractivo en L²(x^{3/2}dx) para ningún λ>0.
  Cotejo: x²f=(k*k+xk)*f, conjugación Möbius: repeticiones detenidas.

### 67. «El producto BPY completo tampoco es acotado en la métrica recíproca» (L1882)
- Etiqueta: **PROVED, clase precisa**. ‖T_fh_ε‖_H ≥ cε^{−1/4}→∞; lejos del borde ‖T_fh_R‖²−‖h_R‖²>0.
  T_fq ≠ q.

### 68. «Diagnóstico único de falsificación de la pareja C_1» (L1918)
- Etiqueta: **NUMÉRICO exploratorio, NO certificado**. Bloque de 5 nodos, autovalores positivos aprox.
  Candidata OPEN.

### 69. «Conservar ambas ramas no restaura la monotonía usual del proceso físico» (L1930)
- Etiqueta: **PROVED, clase precisa**. dQ_x(z)/dx|_0 <0 (K'/K(u0)<−19) ⇒ no preserva orden usual.

### 70. «El semigrupo físico tampoco conserva las funciones pares convexas» (L1970)
- Etiqueta: **PROVED**. (A_markov f_R)''(0)/(2c) → <(2−38/3)K0<0.

### 71. «Control de duplicación: integración por partes de T y energía ponderada» (L2016)
- Etiqueta: **Identidad comprobada, SIN desigualdad nueva**. Q(P)=(π²/2)[4E_4(P')−6E_2(P)−6∫t^{3/2}|P|²],
  P(1)=0. Reformula como E_4(P') ≥ (3/2)[E_2(P)+∫t^{3/2}|P|²]; no demostrada.
- Reutilizable: identidad.

### 72. «Traslaciones imaginarias conjugadas: tampoco minoran la forma completa» (L2040)
- Etiqueta: **PROVED**. No existe μ ≥ 0 fija con B ≥ ∫K_η dμ(η), B=A o C_u: K_η(x,x)/D_0 ≥ 1/2,
  A(x,x)/D_0(x) ≤ x/sinh(2x)→0.
- Reutilizable: la cota A(x,x) ≤ (x/sinh 2x)C_0(x,x), x>0.

### 73. «El cociente integrado A/C_0 tampoco es un multiplicador positivo» (L2080)
- Etiqueta: **PROVED**. H=A/C_0: H(x,−x)→1/2, H(x,x)→0 ⇒ det→−1/4; H_u análogo −(1+u)^{−4}. Gauges no reparan.

### 74. «Control de la sustitución ortogonal en la identidad factorial» (L2129)
- Etiqueta: **PROVED como aplicación de densidad previa**. Π_m=I; Σ_mΛ(m)‖F−R_mF‖²=∞.

### 75. «Realización operatorial theta: pieza construida, signo pendiente» (L2142)
- Etiqueta: **PROVED, no signo** (HYPER §12.6): H=L²(sech(πω/2)dω)⊕R³, Q=(cos ωv, cosh(v/4), cosh(5v/4),
  cosh(9v/4)), D continuo/discreto explícitos, q_θ=Phi(v/2)e^{2π cosh v} observación exacta. Extensión
  integral: Y_rr=(b²+ν²)Y+2DY_r+(−C+2bB̄)Y, ⟨Y_ν(2π),h⟩=Z(2ν).
- Métrica local acotada imposible (§12.7, PROVED, clase). No decide métricas no acotadas/no locales.
- **Reutilizable:** la realización (objetos y observación exacta).

### 76. «Laplace de las parejas recíprocas: identidad válida, premisa de capas posteriormente refutada» (L2153)
- Identidades PROVED: C_u=∫e^{−uv}D_v dv, A=∫[(1−e^{−v})/v]D_v dv, D_v/v→C_0. Premisa «D_v PSD ∀v» FALSIFIED.
- «Ensayo de factorización detenido»: el término vab no produce forma no diagonal en (n,m).

### 77. «La capa de Laplace D_(2pi) es indefinida: falsificador certificado» (L2183)
- Etiqueta: **PROVED mediante intervalos con colas analíticas completas**. (d1+e)d0−2c² ∈ [−6e−21 ± 8.08e−22]<0;
  test (1,−1/1300000,1) upper −11286479/4.225·10^{23}<−2.6e−17 (SHA e6fee17a…).
- Corolario: no monotonía completa en toda raya u ≥ U. Control NUMÉRICO en u=1/(2π): positivo.
- Estado: compensación integrada en v abierta.

### 78. «Primitivas de las capas: deduplicación y límite del argumento por radicales» (L2251)
- Resultado: G_V, F_R, A=∫[−w'(V)]G_V dV; PSD de todos G_V «NO está probada ni refutada»;
  G_V(x,x)/C_0(x,x) ≤ V/[2sinh 2x]→0 pero →1 cuando V→∞: no se intercambian límites.
- Decisión: no lanzar campaña. Reutilizable: identidades.

### 79. «Productos cosh desplazados: ampliación descartada antes de conservación» (L2273)
- Etiqueta: **PROVED en clase delimitada** (HYPER §13, §13.1: base exp(−a_n cosh 2t), a_n>0 variable,
  factores (cosh(bt)−c)/(1−c)). No otras bases/factores.

### 80. «Control de duplicación posterior: cuatro propuestas sin construcción» (L2280)
- Etiqueta: **REGISTRO DE COTEJO; sin resultado matemático nuevo**. (i) localización nodal de testigo negativo;
  (ii) tasas positivas antes de T; (iii) Jensen/concavidad de operadores; (iv) BPY par/impar escala 1/4.
- Reapertura: «afirmación adicional explícita que controle el obstáculo indicado y conecte con la forma
  completa».

### 81. «Aproximantes BPY geométricamente simetrizados: examen G2 inconcluso» (L2292)
- Etiqueta: **OPEN / NUMÉRICO exploratorio**. G_N=√(Phi_N(t)Phi_N(−t)); f_2=Ce^{−av}H(dv); G_2 cola
  [8π³/(3√6)]e^{−2|t|−π cosh 2t}. Diagnóstico de jets positivo (no certificado).
- Reapertura: «hipótesis estructural nueva».

### 82. «Paso al límite de los aproximantes geométricos: dominación uniforme» (L2313)
- Etiqueta: **PROVED como puente analítico, no signo**. E e^{πY_N}=[2N/(N+1)]² ≤ 4; G_N ≤ 2π²e^{−π cosh 2t}
  (G-DOM); A[G_N]→A[Phi] localmente uniforme.
- **Reutilizable:** PSD de A[G_N] para infinitos N ⟹ signo global.

### 83. «Filtros posteriores: acoplamiento consecutivo y simplex» (L2345)
- Etiqueta: **REGISTRO DE COTEJO**. Innovación común y simplex/Dirichlet(2,…,2) sin identidad firmada.
- Reapertura: desigualdad conjunta explícita o falsificador concreto.

### 84. «Filtro posterior: variación compensada de dos tasas BPY» (L2354)
- **REGISTRO DE COTEJO**. Cubierto por la rigidez (§55) y la interpolación (§30). No habilitada.

### 85. «Filtro posterior: corte de un puente gaussiano que realiza la ley BPY» (L2362)
- **REGISTRO DE COTEJO**. Reapertura: «especificar y justificar el operador de frontera o la identidad de
  corte que dé A completa, con medida positiva y sin resto de signo pendiente».

### 86. «Filtro posterior: operador de etiquetas en el sector libre de cuadrados» (L2370)
- **REGISTRO DE COTEJO**. GRAPH: G(P_d)=(log d)Θ_d/2, G=(T Lg)/2−CT; sustituir por derivada de Euler omite la
  cancelación. Núcleo SF corresponde a S_sq, no a RES-SOS.

### 87. «Comparación consecutiva BPY con congruencia sech: falsificador analítico para todo c>0» (L2376)
- Etiqueta: **NO-GO PROVED en la comparación declarada**. A_2 − c sech(2x)A_1 sech(2y) no PSD ∀c>0
  (A_2(iy,−iy) ≤ M/8, A_1(iy,−iy) ≥ a_*, factor 1/cos²(2y)).
- Reutilizable: H no se anula en Re z>0; G_2 holomorfa en |Im|<π/4.

### 88. «Ampliación: ninguna congruencia holomorfa no nula transfiere G1 a G2» (L2440)
- Etiqueta: **NO-GO PROVED en la clase declarada** (D holomorfa en la franja, real en R ⇒ D≡0).

### 89. «Cierre de la transferencia diagonal: regularidad automática del factor» (L2471)
- Etiqueta: **NO-GO PROVED para TODO factor real** D:R→R arbitrario ⇒ D≡0. No excluye transferencias no
  diagonales.

### 90. «Filtros posteriores: transferencia triangular y dos secciones de borde» (L2529)
- **REGISTRO DE COTEJO**. (1) Th=h+∫_x^∞k(x,s)h(s)ds sin k ni entrelazamiento especificados: no excluido.
  (2) Alineación de dos raíces de H(iu): no controla las demás.
- Reapertura (1): mecanismo explícito que controle cruces, peso 2r+x+y y bordes, extensible a la sucesión;
  (2): control conjunto previo a bloques.

### 91. «Deduplicación: factores diferenciales positivos sobre el modelo fijo» (L2539)
- **Aplicación de un descarte existente**. ΔK=f(u)f(v)+g(u)g(v) ⇒ K_new ≥ K_{2π}; llegar a K_Phi exigiría
  K_Phi ≥ K_{2π}, FALSIFIED.

### 92. «G2: la energía derivada de borde supera cualquier colección fija de ramas» (L2554)
- Etiqueta: **PROVED en el alcance indicado**. E_x(ε)/log(1/ε)→+∞; cada colección fija de ramas aporta
  O(log 1/ε). B_x(ε)=E_x(ε)−|G2(x+iy_ε)|².
- Pendiente: |B_12|² frente a B_11B_22. PSD de A[G2] ni probada ni refutada.

---

## A. Lista deduplicada «no relanzar», con condición de reapertura

Cada ítem: qué no se relanza / condición de reapertura según la fuente / estado en `RULES_AVOID.md` §D.

1. SOS aritmética pura para T ≥ ½log3 / factorización conjunta explícita de Arch y todos los contactos con
   Tate (L17) — en §C de RULES_AVOID («SOS aritmética pura (vacía para T ≥ ½log3)»), no en §D; reapertura
   ausente.
2. Near en valor absoluto, Euler reindexado, Cauchy–Schwarz separado, reescritura como convolución / desigualdad
   firmada conjunta Arch–m≈kn uniforme (L27, L101) — **D8** sólo menciona «Arch − Div − Near por
   Poisson/divisores». Falta la condición positiva de L27.
3. Continuación del primer contacto / defecto global no lineal (197) / bound firmado del extremo o del resto del
   camino o una obstrucción independiente (L35) — ausente de §D.
4. Densidad de la unión filtrada / ver ítem en E (D3 inexacto).
5. Descenso 036 / R_L ≥ −ε_L **o** familia de subespacios conjuntamente positivos que aproxime en topología donde
   W sea continua (L43) — **D4** omite la segunda alternativa y la precisión «promedio, para cada entrada
   inicial, no átomo por átomo» (L186).
6. Reparación PAR compacta del representante (045) / representante no compacto con identidad global (L51) —
   ausente.
7. Agrupar nodos próximos sin desigualdad relativa para cruces (L67) — ausente.
8. Comparaciones Off frente a energía divisorial / fracción fija de R_res / dilataciones con peso 1+log t (L69,
   L1507) — **D9** correcto; falta que tampoco hay cota SUPERIOR uniforme (L1507) y el descarte §17.7.
9. Mellin o el cambio u=½log t como mecanismo (L77) — cubierto por A4.
10. Gram theta por capas / sectores par-impar / modularidad por modo (L90–94) — ausente de §D (las reglas del proyecto lo cita
    como «Cambio (m,n)…»); D16 lo incluye parcialmente.
11. «Celdas/división euclídea» sin factorización que empareje defecto de divisor pequeño y borde de segundo orden
    (L101) — ausente.
12. Ensamblaje de certificados PSD de soporte fijo — **D12** correcto.
13. K − K_shift; reparación IMS — **D13** correcto; falta la reparación IMS (L121).
14. Representación Laplace positiva de L' en cualquier raya (L138) — ausente.
15. Subordinación gaussiana de N como representación nueva (L147); premisa de positividad inversa gaussiana
    universal (L156) — ausente (D6 la cubre genéricamente).
16. Variantes del presupuesto 022 — **D7** correcto.
17. Mezclas/convoluciones positivas de exp(−a cosh 2t), monotonía de escala −a∂_aK_a, sucesión de modelos / operación
    preservante para la Phi real o estimación de toda la corrección (L176) — B4 lo menciona; ausente de §D.
18. Pequeñez puntual de cola / número fijo de derivadas — **D10** correcto.
19. Prefijos theta, cortes suaves con Σw_n n² finita, cola continua, simetrizaciones, cortes Jacobi, amortiguación
    n^{−δ}, primitiva regularizada U (L193, L245, L257, L286) — ausente de §D.
20. Productos cosh multiplicativos (§11, §13, §13.1) — en §C («cierres por productos cosh»), sin alcance de clase.
21. Conmutador ZΔ=[L,Z] como cota (L263) — ausente.
22. Separar Selberg en dos energías finitas (L280) — ausente.
23. ARCH−Div−Near por Poisson, s_w, colas con gauge, patrones near — **D8** correcto.
24. Tests asintótico/Jensen de K_Phi−K_{2π} como construcción (L312) — ausente.
25. Interpolación geométrica phi_s con PSD de la derivada en cada s / cota relativa ∂_sK ≥ −C_U(s)K integrable
    (L323) — ausente; RULES_AVOID B4 la trata como patrón cerrado («interpolaciones»), lo cual es más fuerte que la
    fuente.
26. Signo uniforme de coeficientes de la covarianza divisorial; R o −R como pieza positiva (L348, L387) — ausente.
27. Comparadores aditivos K_Phi − K_* (Robin ajustado, asinh, hiperbólico 2π), también primitivos; filtro D=o(1/u)
    (L421–L605) — ausente de §D.
28. HCM + reciprocidad + momentos como hipótesis suficientes; HCM de la densidad theta (L543, L573) / desigualdad
    adicional que excluya el contramodelo — ausente.
29. Generadores traslacionales normalizados: por Phi, por g par analítica, por e^{ct}Phi (todo c), por √A(t,t)e^{ct},
    por √d/F, por exp(a sinh 2t) (todo a) (L627–L904) — ausente; las reglas del proyecto «Transporte por desplazamiento y
    congruencia» (D16) cubre parcialmente.
30. Poincaré/caminos con pérdida como consecuencia de RES-SOS para restos 106_38 (L921) — ausente.
31. Orden PSD entre fases A_0, A_π (L970) — ausente.
32. Coordenada continua simétrica sin deriva / deriva escalar constante o variable (L973–979) — ausente (D15 cubre
    sólo §12.7).
33. Optimización de constantes del margen fijo 9 (L982); cortes móviles polinómicos (L990–995) — D2 lo cubre
    genéricamente.
34. Ramificación theta: torre de certificados, «otra coordenada del resto» (L1079) / estimación conjunta del paso
    o falsificador justificado — ausente.
35. Campaña de ventanas (log11) sin estimación estructural uniforme del bloque Schur (L1213) — D2 genérico.
36. Torre de determinantes para PF∞ + reciprocidad (L1269) — ausente.
37. Modificaciones finitas de tasas BPY recíprocas (L1365); variación de dos tasas (L2360) — ausente.
38. Mezcla P_down/P_up reversible (L1393) — ausente.
39. Capas de la renovación plegada y fuente integrada (L1438, L1457) — ausente.
40. Semigrupo de autodescomposición como transporte de la órbita (L1489); par/impar escala 1/4 — **D11** cubre el
    último.
41. D ≥ 0 y E ≥ 0 por separado; E ≥ −C·S_sq; B+M ≥ 0; Q ≥ ε(L−B); Q ≥ εS_sq; sustitución Π_m (L1558–L2139) — D16
    cubre «cuadrados factoriales» y la sustitución ortogonal sólo por nombre.
42. Capas de resolvente J_u individuales (L1708) — ausente.
43. Transportes desde C_0: multiplicador q_u, mezclas de traslaciones reales, traslaciones imaginarias conjugadas,
    cociente A/C_0 con gauges (L1805, L2077, L2126) — B4 cita «Dos transportes desde C_0»; faltan los otros dos.
44. Descenso B_1 → B_0 sin hipótesis adicional (L1856) — ausente.
45. Contractividad de factores V_λ y del producto BPY en la métrica recíproca (L1877, L1915) — ausente.
46. Monotonía estocástica del proceso físico, cono par convexo (L1967, L2013) — ausente.
47. Hardy sobre las normas positivas para la identidad de T (L2037); tasas antes de T — D11 parcial.
48. Capas D_v PSD para todo v; expansión en v; factorización vab (L2180, L2238) — en §C («capa de Laplace D_{2π}»).
49. Primitivas G_V, F_R sin operación theta adicional (L2270) — **D16** («primitivas compensadas»).
50. Campañas finitas sobre G_N, G_2 (L2310); acoplamiento consecutivo, simplex, puente gaussiano, operador de
    etiquetas (L2352–L2374) — ausente.
51. Congruencia diagonal G1→G2 con cualquier D real (L2527) — RULES_AVOID B4 («congruencia BPY G1→G2»).
52. Transferencia triangular sin k especificado; alineación de dos ramas (L2533–2535) / ver §90 — ausente.
53. Factores (D_t²+λ) sobre el modelo fijo 2π (L2550) — ausente.
54. Aislar una o dos ramas de G2 como energía diagonal (L2611) — ausente.

---

## B. Resultados positivos PROVED (con alcance exacto)

1. HK > J² y PSD de triples temporales simétricos suficientemente pequeños (GRAM §12; L62).
2. R_res (parte resonante exacta) admite SOS de todos los órdenes, válida en y=0, con margen uniforme respecto de su
   energía divisorial (GRAM §17, §17.5; L68).
3. Reducción: PSD de A completo en y=0 sobre bloques de escalas enteras ⟺ PSD en nodos reales ⟺ λ_A(T) ≥ 0 ∀T (GRAM
   §18, §18.9; L69).
4. Plano span{E1,E2} firmado con cotas racionales (GRAM §19.9; L71). Q(E1)>1/2000.
5. Reducción a colas de grados E_j, j ≥ J para J fijo (GRAM §19.10; L72).
6. Identidad del potencial causal J*Θ (GRAM §19.12; L75) — identidad, signo desfavorable.
7. Modelo hiperbólico phi_a y extensión Robin: Gram en toda dimensión (HYPER §§1–9; L170).
8. Principio de continuación: PSD en un intervalo abierto ⟹ PSD en R para kernels holomorfos; PSD transformado ⟺
   temporal (GRAM §2.1–2.2; L191).
9. Filtro de pares: D=o(1/u) y K_D PSD en pares ⟹ D≡0 (L423).
10. Lema primitivo ⟺ completo para K_D con D impar real-analítica (L586).
11. Modelo asinh: K_0 PSD (L432–440).
12. Estimaciones de cúspide SMALL/LARGE, A0 ≥ cε^{−4}, Ah ≤ Cε^{−5}, DIAG-CUSP (L730–816).
13. Cotas de densidad/cola de BRIDGE014 §6–§7: umbral limsup N/u_N=∞; |W−W_{≤⌈exp(40N/u)⌉}|<e^{−N}‖f‖² en V_N(u)
    (L982–985).
14. W[f_*]=0, f_*=(D²−1/4)Phi; familia primitiva g_R con W[g_R]→0 (L1043–1049).
15. Ventana completa W_T ≥ 0 para 0<T ≤ log(11)/2, ambas paridades (resultado externo reproducido; L1213).
16. Semilla S δ_c: M=b tanh(bu), kernel con Gram explícito (L1066–1069).
17. PF∞ aditivo de q; 2π∫q=1; L(s)=Π(1+s/(πn²))^{−2}; fórmula de A en q; −(log Phi)'' ≥ 5 bajo el paquete
    (L1231–1278).
18. Rigidez de la ley recíproca bajo modificaciones finitas de tasas (L1318–1365).
19. Renovación v f(v)=∫k(v−u)f(u)du y su versión plegada (identidades exactas; L1374, L1406–1413).
20. Energía auxiliar positiva del semigrupo de autodescomposición (L1476).
21. Identidad factorial Q=Σ_mΛ(m)‖P_mb−R_mb‖²+b*Db+E(b); núcleo SF de S_sq; Q=L+M sobre SF; 0 ≤ B ≤ L (L1534–1583).
22. Densidad SF en B_a² (contiene todos los P_k y los compactos) (L1619–1635).
23. Representaciones A=∫_0^∞J_u du, A=∫_0^1C_u du, C_u(x,x)>0 (L1680–1722).
24. **C_0 PSD en todos los órdenes** (contracción S(a)=Z(a−1)/Z(a+1)) (L1725–1775).
25. Contramodelo genérico B_1 PSD con B_0 no PSD (L1808–1856) — positivo sólo como modelo.
26. Identidad de duplicación Q(P)=(π²/2)[4E_4(P')−6E_2(P)−6∫t^{3/2}|P|²] (L2027).
27. Cota A(x,x) ≤ (x/sinh 2x)C_0(x,x), x>0 (L2073).
28. Realización operatorial theta exacta y su extensión integral (L2144–2147).
29. Identidades C_u=∫e^{−uv}D_v dv, A=∫[(1−e^{−v})/v]D_v dv; G_V, F_R (L2169–2260).
30. Dominación uniforme G-DOM y A[G_N]→A[Phi] localmente uniforme (L2330–2342).
31. H(z)=z−2+(z+2)e^{−z} sin ceros en Re z>0; G_2 holomorfa en |Im|<π/4 (L2392–2397).

---

## C. Obligaciones explícitamente abiertas (enunciados precisos)

C1. (Factorización mixta, L17) Existen un Hilbert ℋ y una aplicación V con a_T(F)=‖VF‖²+(resto manifiestamente
    ≥0) que factoriza conjuntamente la medida arquimediana y TODOS los contactos m=kn, m≈kn, con control uniforme
    en T de los términos y de Tate. Intentado: multiplicadores + Bochner (clase dual), SOS pura (vacía T ≥ ½log3).
C2. (Balance aritmético conjunto, L27) Para todo tamaño M del portador suficiente y todo vector s:
    sᵀ(Arch − Div − Near)s ≥ 0 demostrado mediante una desigualdad firmada entre Arch y los términos m≈kn que
    conserve fases y bordes. Intentado: convolución desplazada, Near absoluto, Euler reindexado, conmutador ZΔ.
C3. (Primer contacto, L35) Bound firmado del extremo o del resto del camino de continuación. Intentado: 197.
C4. (Descenso, L43, L186) Para cada entrada inicial (N,k): el promedio firmado R_L del complemento de frontera
    cumple R_L ≥ −ε_L con ε_L→0; o una familia de subespacios conjuntamente positivos densa en una topología donde
    W es continua. Intentado: 036, 055, 065, 067, puente escalar 017.
C5. (Representante positivo, L51) Representante real positivo con corrección no compacta, identidad en todo el
    portador, control uniforme en T de la coincidencia aritmética interior. Intentado: 045.
C6. (Comparación crítica resonante, L69, L1509) En y=0, sobre todos los bloques finitos de escalas enteras:
    Off ≥ −R_res (equivalentemente H=−R^{−1/2}OffR^{−1/2} ≤ I). Intentado: márgenes fijos (refutados), norma
    uniforme (refutada).
C7. (Reducciones abiertas, L69–72) PSD de A completo sobre todos los bloques enteros en y=0; o PSD de todos los
    Gram de E_j, j ≥ J, para un J fijo. Sólo E1,E2 firmados.
C8. (Gram theta por capas, L90) Cota conjunta que compense capas no PSD.
C9. (Stieltjes de 083, L142) Medida positiva que represente N(x)=M(√x)/√x como función de Stieltjes; equivalente a
    signos alternados de todas las derivadas de H_A−P (L149).
C10. (Presupuesto 022, L160) Para todos (N,k): desigualdad independiente que pague ARCH_♯ (fila k=0: A_N+2∫K_NC_B ≥ 0).
C11. (Hiperbólico, L174, L179) Operación preservante aplicable a la Phi real, o estimación de toda la corrección
     Phi/phi_{2π} en toda dimensión; compensación de la fuente.
C12. (Interpolación geométrica, L323) Para cada lista finita U: ∂_sK_{s,U} ≥ −C_U(s)K_{s,U}, C_U ∈ L¹[0,1].
C13. (Selberg compensado, L280) Comparación conjunta con ARCH y polar.
C14. (N) completa, uniforme en todos los tests (L292); R8 con portador positivo independiente e identificación de
     dominios; R10.
C15. (Régimen denso, L985) Con u_N=N^{3/4}: inf_{f∈V_N(u_N)} W_{trunc}[f]/‖f‖² ≥ −ε_N, ε_N→0, para ARCH+POLAR y todos
     los contactos hasta exp(40N^{1/4}).
C16. (Operador causal, L1057) Cota uniforme de la inversa sin peso.
C17. (Ramificación theta, L1079) Desigualdad que preserve PSD en el paso B∘S de la órbita desde δ_{π/3}.
C18. (Dos cortes, L1224) Signo del resto R_M, cota uniforme para interpolantes dependientes de M.
C19. (Paquete BPY, L1269, L1877) PF∞ aditivo de q + reciprocidad + integrabilidad ⟹ A PSD, o falsificador que
     satisfaga el paquete.
C20. (SF, L1653) Q=L+M ≥ 0 sobre todos los coeficientes finitos libres de cuadrados (α=1); balance conjunto D+E con
     los cuadrados (L1668).
C21. (Parejas, L1722, L1775) Desigualdad integrada de cruces para C_u, 0<u ≤ 1 (o para ∫_0^1C_u du), o falsificador
     que conserve el emparejamiento; candidata C_1 (L1927).
C22. (Descenso hiperbólico theta, L1856) Hipótesis o identidad adicional demostrada para theta que lleve de B_1 PSD a
     B_0=A PSD.
C23. (Duplicación, L2037) E_4(P') ≥ (3/2)[E_2(P)+∫_1^∞t^{3/2}|P|²dt] para P suave compacto con P(1)=0.
C24. (Laplace, L2238, L2262) PSD de A tras integrar v (compensación); PSD de G_V para todo V (ni probada ni refutada).
C25. (Aproximantes, L2342, L2611) PSD de A[G_N] para todo N (o subsucesión infinita), incluso A[G_2] en todos los
     tamaños; |B_12|² ≤ B_11B_22 del menor cruzado completo.
C26. (Triples, L63) Extensión de triples pequeños a todo R; monotonía del cociente normalizado; conservación Schur.
C27. (Agrupamiento, L67) Desigualdad relativa para cruces en el kernel −B''.
C28. (Métrica, L2150) Métrica compatible / Green positivo no local o no acotado para la realización §12.6.
C29. (RES-SOS vs 106_38, L921) Compensación conjunta de los restos.
C30. (Ventanas, L1213) Estimación estructural uniforme del bloque Schur completo.

---

## D. «Inputs que cambiarían la obligación» nombrados en la fuente

- L17: factorización conjunta explícita (Arch + todos los contactos, control uniforme y Tate).
- L27: desigualdad firmada conjunta Arch–m≈kn, uniforme, con fases y bordes.
- L35: bound firmado del extremo o del resto del camino, u obstrucción independiente al cruce.
- L43 («Input suficiente»): R_L ≥ −ε_L uniforme; o familia de subespacios conjuntamente positivos en topología donde W
  es continua.
- L51: representante positivo no compacto con identidad global y control de coincidencia interior uniforme en T.
- L79: «estimación firmada adicional concreta».
- L83: uno de los cuatro: factorización mixta, balance aritmético conjunto, cota unilateral uniforme de un resto,
  representante positivo completo.
- L101: factorización positiva que empareje defecto de divisor pequeño y borde de segundo orden.
- L121: reparación con coste independiente demostrado.
- L164: desigualdad que pague ARCH_sharp con alcance en k justificado.
- L176: operación preservante para Phi real o estimación de toda la corrección.
- L292: hipótesis nueva que resuelva el fallo identificado.
- L323: cota relativa ∂_sK ≥ −C_U(s)K integrable (Grönwall).
- L543: desigualdad adicional para el dato completo que excluya el contramodelo HCM.
- L1079: estimación conjunta para el paso o test falsificador justificado.
- L1213: estimación estructural uniforme del bloque Schur completo.
- L1269: identidad conjunta que conserve reciprocidad y firme los cruces logarítmicos.
- L1722: desigualdad integrada de cruces para C_u.
- L1775: control de las parejas interiores o de su integral.
- L1856: hipótesis o identidad adicional para theta.
- L2289: afirmación adicional que controle el obstáculo y conecte con la forma completa.
- L2310/L2342: hipótesis estructural nueva; PSD de A[G_N] para todo N.
- L2352: desigualdad conjunta explícita o falsificador concreto.
- L2368: operador de frontera o identidad de corte que dé A completa con medida positiva.
- L2533: mecanismo explícito (k, entrelazamiento) que controle cruces, peso 2r+x+y y bordes.
- L2535: control conjunto de todas las singularidades.
- L2611: control de |B_12|² frente a B_11B_22.

---

## E. Contradicciones o debilitamientos respecto de `RULES_AVOID.md` y `OBJECT_SPEC.md`

E1. **RULES_AVOID D3** dice: «Inferir densidad o signo de una unión positiva — sólo con liminf r(n)²/n = 0 y un
    bloque que repare el momento (211/GLOBAL §4).» La fuente: liminf r(n)²/n=0 es la condición de densidad L² de la
    unión a tasa fija (L41); y L108: «Esto repara la objeción de momento cero y muestra que aún queda la obligación
    independiente sobre los cruces». La condición de D3 es insuficiente: falta el control firmado de los cruces
    (y continuidad de la forma completa: «Densidad L² sola no da continuidad», L41).
E2. **RULES_AVOID D4** («sólo con una cota aritmética firmada del resto R_L ≥ −ε_L») omite la alternativa de L43
    («o una familia de subespacios positivos conjuntamente que aproxime en una topología donde W sea continua») y la
    precisión de L186 (basta el PROMEDIO por entrada inicial).
E3. **RULES_AVOID B4** pone como patrón de parada «Mezclas, convoluciones, congruencias, transportes,
    interpolaciones y comparaciones K ≥ εK₀ desde un modelo PSD». La fuente limita cada cierre a su clase: L323
    deja abierta la interpolación con cota relativa; L2527 «no se excluyen transferencias no diagonales»; L2533 la
    transferencia triangular «NO» está excluida; L1037 «no se excluyen todos los modelos o compensaciones». B4 es más
    fuerte que la fuente.
E4. **RULES_AVOID §C** incluye «defecto/continuación» y «cierres por productos cosh, capa de Laplace D_{2π}» como
    familias cerradas. La fuente: 197 es «PROVED reduction, no un NO-GO universal» (L35); productos cosh sólo «base fija
    2π / exp(−a_n cosh 2t)… no otras bases/factores» (L2275–2278); D_{2π} refuta sólo la premisa de todas las capas,
    «La compensación tras integrar v permanece posible» (L2238).
E5. **OBJECT_SPEC §3 (L-comp)** concluye «ℋ_T no puede venir de un modelo exterior». La fuente cierra K_Phi ≥ εK_{2π}
    mediante U_Phi v_1 ≠ 0 (no mediante medida de borde) y declara «no se excluyen todos los modelos» (L1037), «no
    otras escalas, reponderaciones ni compensaciones firmadas» (L493). L-comp no está demostrada en la fuente.
E6. **OBJECT_SPEC §1** (variantes admitidas de (G)) no lista reducciones PROVED de la fuente: PSD de A en bloques
    enteros y=0 (L69), colas E_j, j ≥ J (L72), PSD de A[G_N] para infinitos N (L2342), y la ventana externa log(11)/2
    (L1213) como frontera verificada actual. No contradicción, sí omisión.
E7. **RULES_AVOID D9** coincide, pero omite la refutación de la cota superior uniforme (L1507: «tampoco hay cota
    SUPERIOR uniforme») y el descarte §17.7 de dilataciones (L69).
E8. **RULES_AVOID D11** cita «concavidad de Jensen / de operadores» como no relanzar; la fuente (L2286) dice
    «Ninguno autoriza excluir toda comparación logarítmica»; la reapertura requiere par de operadores y dominios con
    desigualdad suficiente. Compatible si se lee con esa condición, que D11 no enuncia.
E9. **RULES_AVOID B2** («toda cota con resto pierde más») es compatible con L35 (margen exponencial simple), pero la
    fuente usa también cotas con resto que sí son útiles cuando cancelan exactamente (p. ej. control de cola
    |W−W_{≤Q}|<e^{−N}‖f‖², L985). No contradicción.

---

## F. Cobertura

Última línea leída: 2611 (fin del archivo). Rangos leídos consecutivamente: 1–124, 125–249, 250–349, 350–499,
500–649, 650–799, 800–949, 950–1069, 1070–1219, 1220–1368, 1369–1492, 1493–1617, 1618–1737, 1738–1861,
1862–1985, 1986–2109, 2110–2253, 2254–2378, 2379–2498, 2499–2611. Ningún rango sin leer.
