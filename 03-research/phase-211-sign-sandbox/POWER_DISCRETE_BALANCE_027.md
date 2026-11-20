# POWER_DISCRETE_BALANCE_027 — Cola conjunta positiva con magnitud gamma controlada

Estado: **PROVED** masa discreta completa y desigualdad uniforme de la cola CONJUNTA que usa el corte gamma/logconcavo real; **PROVED** 0<cola conjunta N129 desde4096<10^(-36). Interior y signo W **OPEN**. Auditoría independiente aprobada en POWER_JOINT_AUDIT_027.md, verificador PASS reproducido. Papers intactos;026 y su auditoría no se modifican.

## 1. Corpus, razón nueva y límite de las masas

Leídos las reglas del proyecto, CUMULATIVE_INVERSE022, ARCH_CELL026, UNIFORM_CUTOFF026 y STATE026. Consultados índice/grid/crucigrama en muestreo, Euler–Maclaurin, masas y Möbius. La inversión de divisores y la sumación son clásicas. Las identidades adicionales de masa no se presentan como nuevas desigualdades de signo.

La diferencia aquí es combinar el kernel CONJUNTO firmado Omega026 con el corte real y la logconcavidad de D026 para probar una cota unilateral de una contribución completa de W, no sólo de ERR. Se controla también su magnitud en el MISMO N129 para evitar confundir localización favorable con compensación del interior.

Limitación breve: dos masas escalares, incluso con K>=0, no bastan para forzar el emparejamiento positivo. Un bump junto a3/2, donde Omega<−.1, puede llevar casi toda la masa integral; bumps cada vez más estrechos en2 fijan la masa de muestras sin un coste integral fijo, pues la singularidad de Omega es sólo logarítmica. Esta construcción genérica NO conserva la forma gamma real. No se dedica una nueva ruta a ese falsificador: el resultado positivo abajo usa justamente el corte y forma gamma que excluyen elegir K arbitrario.

## 2. Masa discreta completa y restricción funcional

Para cada N>=2, las series de022 son absolutamente convergentes y

    sum_(n>=1)J_N(n)=1,
    sum_(n>=1)n h_N(n)
      =sum_(r>=1)rH_N(r)sum_(m|r)mu(m)=H_N(1)=1/2.

Por tanto

    sum_(n>=1)K_N(n)=3/2.                                (SAMPLE)

La identidad funcional más fuerte, por la misma inversión absoluta, es

    sum_(n>=1)K_N(nx)=G_N(x):=x^(-32)D_N(logx)>0, x>=1.   (SCALES)

Ambas son restricciones exactas reales; ninguna se usa aquí como si implicara por sí sola positividad de int K Omega. El adjunto inverso de SCALES deja el peso Omega intacto en1<t<2, por lo que tampoco elimina automáticamente su región negativa. Se mantiene la forma específica D_N=33P_N−P_N' y su logconcavidad probada025/026.

## 3. Fórmula completa de Omega por pisos

Sea n=floor(t), L_n=sum_(j=1)^n jlogj y c=−gamma−log(4pi). A partir de OMEGA026 se obtiene, para t no entero,

    Omega(t)=H_n+[sum_(j=1)^n jlog((t+j)/(t−j))−2L_n
                      +(c−1)n(n+1)/2]/t².               (FLOOR)

Prueba: T(t)=sum_(j<=t)j permite separar el kernel sharp como suma de n copias del integral I026, con corte t/j. Cada copia aporta c+log((t+j)/(t−j)). Añadir2C_B de022 da FLOOR. Se conservan todos los saltos y las singularidades logarítmicas unilaterales en enteros. No se trata de una aproximación asintótica.

Defina la constante

    ell=1+gamma/2−(1/2)log(4pi)>1/50.                      (ELL)

El bound se prueba por intervalos racionales003. ell es una constante del balance continuo principal; NO se afirma convergencia uniforme Omega(t)->ell, imposible en presencia de los picos logarítmicos arbitrariamente cerca de los enteros.

## 4. Desigualdad uniforme del peso conjunto

**Teorema.** Para t>=2 no entero,

    Omega(t)>=ell−[4logt+9]/t.

En particular Omega(t)>9/1000 para t>=4096, salvo los puntos aislados de singularidad logarítmica que no afectan ninguna integral.                   (OMEGA-TAIL)

Prueba. La sucesión H_n−logn decrece hacia gamma, y n>=t−1. Por tanto

    H_n>=logt+gamma−2/t.

La función f_t(y)=ylog((t+y)/(t−y)) crece en0<=y<t. Su suma de extremos derechos satisface

    t^(-2)sum_(j=1)^n f_t(j)
      >=int_0^(n/t) v log((1+v)/(1−v))dv
      >=1−[log(2t)+1]/t.

Se usó int_0^1 v log((1+v)/(1−v))dv=1 por la serie telescópica; el tramo faltante, de longitud delta=(t−n)/t<=1/t, es <=delta[log(2/delta)+1].

Por monotonía de ylogy,

    2L_n/t²<=logt−1/2+[3logt+1]/t+7/(2t²).

En efecto se compara la suma con int_1^(n+1)ylogy dy, se usa n+1<=t+1 y log(t+1)<=logt+1/t. Finalmente c−1<0 y n(n+1)/(2t²)<=1/2+1/(2t). Sustituir en FLOOR da ell como término constante y un error <=

    [4logt+4+log2+(1−c)/2+7/(2t)]/t
      <[4logt+9]/t.

La última desigualdad usa t>=2, gamma<1, log2<.7 y logpi<1.2. La función (4logt+9)/t decrece para t>=2. En4096, log4096=12log2<8.4 y ELL prueban OMEGA-TAIL por aritmética racional. QED.

## 5. Desigualdad conjunta para el K gamma REAL

Use el corte tau_N=min(t_J,t_R) de UNIFORM_CUTOFF026 (y su caso afín N2). Para x>=exp(tau_N), la prueba de logconcavidad/corte aporta sobre la suma Möbius COMPLETA

    G_N(x)/4<=K_N(x)<=7G_N(x)/4,
    G_N(x)=x^(-32)D_N(logx)>0,
    G_N'(x)/G_N(x)<=−2/x.

Así, para CUALQUIER T>=max(4096,exp(tau_N)), el balance conjunto real satisface

    0<(9/4000)int_T^infty G_N(t)dt
      <=int_T^infty K_N(t)Omega(t)dt
      <=(7/4)G_N(T){T(logT+2)+3T²}.                      (JOINT-TAIL)

La cota inferior usa OMEGA-TAIL; es una desigualdad real firmada, no la identidad de masa aislada.

Para probar la cota superior, FLOOR da

    Omega(t)<=logt+1+t^(-2)sum_(j<=t)jlog((t+j)/(t−j)),

pues −2L_n y (c−1)n(n+1)/2 son no positivos. Además G_N(t)<=G_N(T)(T/t)² por el corte. El primer término integrado es G_N(T)T(logT+2). Para el segundo se intercambia una suma positiva y se amplía cada integral hasta j:

    sum_(j>=1)j int_(max(T,j))^infty t^(-4)log((t+j)/(t−j))dt
      <=sum_(j>=1)j^(-2) int_1^infty z^(-4)log((z+1)/(z−1))dz
      <(2)(2log2)<3.

La integral se acota por reemplazar z^(-4) por z^(-2), cuyo cambio v=1/z da2log2. Esto prueba JOINT-TAIL sin muestreo numérico ni enumeración de nuevas celdas. Las singularidades logarítmicas quedan integradas explícitamente.

## 6. Magnitud en N129: la garantía exterior no resuelve el interior

Para el MISMO N129,025 ya prueba el corte x>=exp(2/3)<2, de modo que T4096 es admisible. Reconstruir D129 con sus coeficientes racionales y evaluar sólo log4096=12log2 prueba

    0<int_4096^infty K129(t)Omega(t)dt<10^(-36).           (SCALE)

No se verifica otro N ni se enumera una campaña de celdas. El mayorante obtenido es aproximadamente6.46·10^(-37), pero sólo se usa la comparación exacta SCALE.

El certificado inferior explícito (9/4000)int_4096^infty G129 es positivo y menor que4·10^(-45). Su integral se calcula por la recurrencia polinomial31Q−Q'=D, ya usada024. La escala pequeña del certificado NO es una cota superior independiente de la contribución real; esa cota superior es SCALE.

Por consiguiente

    W[g129]/norm²=int_1^4096 K129 Omega + R,
    0<R<10^(-36).

No se ha probado el signo de la integral interior ni de W. El déficit de más de.15 observado026 es el del COMPARADOR que sólo usa el beneficio aritmético garantizado.66; no se lo llama déficit interior real. SCALE únicamente muestra que esta cola no mejora sustancialmente ese presupuesto grueso. El balance restante requiere conservar la cancelación en la región interior y usar la forma gamma, no añadir masas sin una desigualdad entre escalas.

## 7. Evidencia y alcance

Verificador exacto: tools/power_discrete_balance_027_verify.py, Fraction/intervalos racionales, PASS. Prueba ELL, las constantes OMEGA-TAIL y el mayorante SCALE del único N129. La uniformidad de JOINT-TAIL se demuestra en el texto; no se infiere del script.

La positividad conjunta exterior es nueva respecto a la positividad de ERR en las celdas025, pero no cierra el emparejamiento interior ni amplía la región W ya certificada. Papers intactos y signo global OPEN.
