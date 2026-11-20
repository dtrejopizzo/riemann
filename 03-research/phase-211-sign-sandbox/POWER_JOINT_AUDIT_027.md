# POWER JOINT AUDIT 027

Estado: DISCRETE_BALANCE027 e INTERIOR_CONSTRAINT027 APROBADOS. Papers intactos.

## 1. Kernel conjunto y desigualdad uniforme

Revisados `POWER_DISCRETE_BALANCE_027.md` y `tools/power_discrete_balance_027_verify.py`; ejecución independiente PASS. Root reprodujo también el verificador y revisó la prueba.

SAMPLE y SCALES son identidades exactas por inversión absoluta, sin nueva desigualdad de signo por sí solas. La fórmula FLOOR de Omega coincide con026: la parte celular es H_n−(2L_n+T(n))/t² y cada copia de la parte sharp añade j[c+log((t+j)/(t−j))]/t². Se mantienen los picos logarítmicos; no se presupone convergencia uniforme hacia ell.

Las comparaciones suma/integral son correctas: H_n≥log t+γ−2/t; la función ylog((t+y)/(t−y)) es creciente; el tramo faltante de longitudδ≤1/t cuesta a lo sumoδ[log(2/δ)+1]. La cota superior de2L_n se obtiene integrando hasta n+1≤t+1 y usando log(t+1)≤log t+1/t. El signo negativo de c−1 invierte correctamente la comparación de T(n)/t². Las constantes dan Omega≥ell−(4log t+9)/t; ell>1/50 y el extremo4096 certifican Omega>.009 para toda la cola, salvo puntos singulares aislados.

## 2. Cola conjunta del kernel gamma real

El corte026 da G/4≤K≤7G/4 y G′/G≤−2/x; aquí sí se usa la restricción gamma concreta, no sólo dos masas. Para T admisible, ambos factores son positivos y la cota inferior conjunta (.009/4)∫G es válida.

Para el mayorante, Omega≤log t+1+t^−2Σjlog((t+j)/(t−j)). Integrar G(T)(T/t)² da T(log T+2). En la parte logarítmica se intercambian términos positivos y se amplía cada integral hasta j. El cambio t=jz produce j^−2 y la integral z^−4log((z+1)/(z−1)), menor que2log2. Σj^−2<2 da la constante3. Se integran correctamente las singularidades; no se muestrea su máximo.

La evaluación racional del único N129,T4096 prueba0<R<10^−36 para la cola conjunta REAL. El uso del corte exp(2/3) de025 es válido: se deduce directamente de su bound logarítmico, aunque su resumen utilizara el corte más débil2. La pequeña cota superior del certificado inferior no se confunde con un mayorante de R.

## 3. Corpus y alcance

Las identidades divisor/muestreo son antecedentes y no bastan para el signo. El esquema de bumps citado como limitación genérica no conserva la forma gamma real y no se registra como falsificador de W. El avance específico es una desigualdad unilateral completa de la contribución conjunta exterior, con magnitud certificada en un átomo. No controla su interior.

El déficit.15 de026 pertenece al comparador que garantiza sólo.66 de beneficio aritmético, no al valor interior real. El resultado W/C0=∫_1^4096K Omega+R,0<R<10^−36 deja el primer término sin signo. No hay nueva cobertura W ni ventana T.


## 4. Restricción interior gamma real — APROBADA

Revisados `POWER_INTERIOR_CONSTRAINT_027.md` y `tools/power_interior_constraint_027_verify.py`; ejecución independiente PASS. La mezcla de calor normalizada tiene V=β/G, G gamma de parámetro N−1/2 y β=u²/4; su media es u²/[4(N−3/2)]. La gaussiana phi_v indicada tiene norma uno y autocorrelación exp(−vt²). Las contribuciones de Levy, polar y peine tienen integrandos no negativos antes de aplicar sus signos. Tonelli identifica sus esperanzas con las del rho real, finitas por su decaimiento exponencial; WG no elimina la forma completa.

El peso bisagra L≥0 y sus dos fórmulas son correctos. La representación de Jensen delta=t⁴∫exp(−at²)L(a)da conserva el primer momento. Su masa Var(V)/2 sólo se usa para N≥3; N2 tiene masa infinita sin invalidar GAP para t≠0. La fórmula de la varianza coincide con la ley inversa gamma.

A_sharp es estrictamente cóncava y su mezcla queda estrictamente POR DEBAJO del valor en la media. Esta comparación superior no se convierte en un lower bound favorable. Para la forma completa, la segunda derivada R contiene polar positivo y ARCH/peine negativos. El intercambio de GAP con cada pieza es absoluto: sus integrales son los respectivos gaps finitos de Jensen de las piezas originales. Así JOINT-GAP es exacta sin signo inventado para R.

La curvatura negativa en v≥65536 está probada. El Levy original K(t)=e^(t/2)/sinh t satisface K≥1/[2sinh(t/2)]≥1/(2t) para0<t≤1. Su contribución de curvatura es menor que−1/(8v²) para v≥2. El polar es menor que24v^−5/2; los primos añaden curvatura no positiva. Con sqrt v≥256 el total es estrictamente negativo. El script certifica las constantes; la prueba analítica proporciona todo el rango.

Se refuta convexidad global del funcional gaussiano completo, no el signo de su promedio contra la ley real L_N ni el de W. La mezcla gamma era conocida; lo distinto aquí es el peso positivo explícito del resto y la comprobación de dirección de las comparaciones posibles. No se infiere positividad de matrices completas desde las diagonales g_N.

## 5. Cierre

La ronda usa restricciones gamma reales y conserva W completa en JOINT-TAIL y JOINT-GAP. Ninguna de las dos desigualdades controla todavía el emparejamiento interior. Las masas aisladas no aportan esa condición, el comparador negativo no es W negativo, y la curvatura negativa no es una refutación de toda comparación conjunta. No hay nueva ventana T ni cobertura de tabla certificada.


## Ampliación§8: mezcla e inversos gaussianos

Revisiones matemática y literal APROBADAS. Se verifica H_a=x^(-3/2)e^(-a log²x)(.5+2a logx)>0 para x>=1. La derivación bajo MIX en128/129 admite dominación por1+V_N. Las sumas positivas ABS-H/ABS-J son finitas por los polinomios gamma y la potencia m^-32. Fubini da exactamente h_N=E h_a y K_N=E K_a en x1, con inversos COMPLETOS. NEG128 yNEG129 previos fuerzan existencias a_h,a_K, posiblemente distintas. No se emplea convexidad de W, una mezcla arbitraria ni un nuevo valor numérico. El alcance no afecta NStieltjes niheatH_A-P.
