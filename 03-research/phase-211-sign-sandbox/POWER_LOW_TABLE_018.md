# POWER_LOW_TABLE_018 — Presupuesto exacto del error absoluto en la fila k=0

Estado: PROVED fórmula del presupuesto y sus tres regímenes asintóticos. OPEN signo de la familia interior. No es un avance positivo del signo ni un nuevo NO-GO global. Papers intactos.

## 1. Corpus, diferencia acotada y alcance

Leídos las reglas del proyecto, TATE_CHAIN009, PACKET_SCOPE_AUDIT009, JOINT_SCALE016, QUADRATIC017 y su extensión; índice ROUTES-TRIED-INDEX/06 (R2/R5, prohibición de relanzar errores absolutos psi−x con exponente>1/2), grid parte3 (envolventes con valor absoluto) y CROSSWORD-TO-D (criticidad central y fluctuación).

La cancelación polar–término principal y el residuo central E0 YA ESTÁN registrados: no se presentan como novedades. La única contribución nueva aquí es calcular EXACTAMENTE el coste que tendría un bound absoluto para ESTA fila racional k=0 y obtener su tasa de crecimiento, incluidos el extremo theta=0 y el umbral theta=1/2. Esta cuantificación explica por qué no se ha cerrado el interior usando la herramienta de banda de017. No se modifica un peso primo ni se invoca un falsificador ajeno al test.

## 2. Fila concreta y monotonicidad de su autocorrelación

Fije u=63/2, N>=2, g_N(y)=y^(N−1)e^-uy/(N−1)!·1_(y>0), y C_N(t)=c_gN(t). Escriba c0=C_N(0)=||g_N||². Su transformada cuadrática es (u²+tau²)^-N.

La representación gamma y la integral gaussiana dan, para t>=0,

    C_N(t)=1/[2sqrt(pi)Gamma(N)]
       ·∫_0^infinito s^(N−3/2)exp(−u²s−t²/(4s))ds.

De aquí C_N(t)>0 y C_N'(t)<0 para t>0. Además C_N(t)<=c0 por Cauchy–Schwarz y C_N(t)/c0->1 para cada t fijo cuando N crece, por la concentración beta central ya demostrada.

Estas propiedades permiten calcular un presupuesto absoluto SIN perder una segunda cancelación entre dos partes de un derivado firmado: el kernel después de integrar por partes será genuinamente positivo.

## 3. Endpoint y cancelación del término principal

Sea psi_Lambda(x)=Σ(q<=x)Lambda(q). Para fijar correctamente el endpoint defina

    E0(x)=psi_Lambda(x)−x+1, x>=1; E0(1)=0,
    w_N(x)=x^-1/2 C_N(logx).

La fluctuación normalizada es

    F_N=2/c0 ∫_[1,infinito) w_N(x)d(psi_Lambda(x)−x).

Sumar1 al residuo no cambia su medida derivada y anula el término de borde en1. En infinito, w_N E0 tiende a0: C_N decae como e^-ut por polinomio, y basta el bound elemental psi_Lambda(x)=O(x logx). Por integración por partes y x=e^t,

    F_N=2/c0 ∫_0^infinito E0(e^t)e^-t/2
                          [C_N(t)/2−C_N'(t)]dt.         (ERR)

El kernel entre corchetes es positivo. Si se utilizara psi_Lambda(x)−x SIN el+1, su valor inicial sería−1 y aparecería un término explícito +2; omitir ambos sería un error de endpoint.

La identidad ya conocida de cancelación del principal es

    2AB−2∫_1^infinito x^-1/2 C_N(logx)dx
       =(1/2pi)∫ |ghat_N(tau)|²/(tau²+1/4)d tau.

Por tanto W[g_N]/c0=Arch_sharp[g_N]/c0−F_N, donde Arch_sharp tiene símbolo m(tau)+1/(tau²+1/4). Su límite es C0+4<0, el MISMO residuo central registrado en009 y el corpus. No se presenta esta igualdad ni su valor como progreso de signo.

## 4. Presupuesto exacto D_N(theta)

Suponga que se dispone SOLO de una cota absoluta |E0(x)|<=A x^theta, con

    0<=theta<u+1/2.

Este rango asegura todos los términos de borde y las integrales siguientes; para la aplicación usual theta está cerca de1/2 o1. Defina

    b=theta−1/2,
    J_N(b)=∫_0^infinito e^(bt) C_N(t)/c0 dt.

ERR da |F_N|<=A D_N(theta), y el presupuesto de esa cota es EXACTAMENTE

    D_N(theta)=2/c0 ∫_0^infinito e^(bt)
                                  [C_N/2−C_N']dt
              =2+2theta J_N(theta−1/2).                 (D)

Prueba: la integración de −C_N' produce c0+b∫e^(bt)C_N, y b+1/2=theta. En particular

    D_N(0)=2 para TODO N.

No hay un término indefinido «0 por infinito»: b=−1/2, J_N es finito. La igualdad D calcula la integral del mayorante positivo usado por el método; no afirma que el error aritmético real alcance ese mayorante.

## 5. Los tres regímenes, con crecimiento explícito

**Subcrítico, 0<=theta<1/2.** Puesto que C_N/c0<=1 y tiende a1 localmente, convergencia dominada da J_N(b)->−1/b. Entonces

    D_N(theta)->1/(1/2−theta).

Esto incluye theta0, cuyo valor exacto es2. Ni siquiera este presupuesto acotado prescribe el signo de F_N: sigue siendo una cota bilateral de magnitud.

**Crítico, theta=1/2.** La transformada bilateral de C_N en cero da

    J_N(0)=1/[2u^(2N)c0],
    D_N(1/2)=2+1/[2u^(2N)c0]
             ~[sqrt(pi)/u]sqrt(N).

**Supercrítico, 1/2<theta<u+1/2.** Para b=theta−1/2>0,

    ∫_R e^(bt)C_N(t)dt=(u²−b²)^-N.

La paridad de C_N y cosh(bt)<=e^(bt)<=2cosh(bt), t>=0, dan

    1/[2c0(u²−b²)^N] <=J_N(b)<=1/[c0(u²−b²)^N].        (L)

La norma exacta es

    c0=u^(1−2N)B(1/2,N−1/2)/(2pi)
       ~u^(1−2N)/[2sqrt(pi N)].

En consecuencia, para theta fijo>1/2,

    D_N(theta)=Theta_(u,theta)(sqrt(N)
                                  [1−b²/u²]^-N).       (GROWTH)

Ésta es la cuantificación nueva: el presupuesto absoluto no solo pierde una constante, sino que crece exponencialmente en N para cualquier exponente estrictamente superior a1/2. En el extremo1/2 crece como sqrt(N). Las tasas provienen de integrales gamma cerradas del MISMO test, sin estimar individualmente un gran número de contactos.

## 6. Qué se concluye y qué no

El corpus ya excluía usar errores absolutos de tipo PNT como paso decisivo en el régimen central. D/GROWTH no reabren ni renombran esa ruta: miden exactamente su pérdida para P=1,k=0 y separan los endpoints que una afirmación cualitativa no especificaba.

No se probó W[g_N]>=0 para todos N. Tampoco se probó W[g_N]<0. Para una prueba positiva falta una desigualdad ARITMÉTICA FIRMADA sobre ERR que compense el residuo central negativo; ni el presupuesto D ni la identidad de Euler suministran ese signo. La herramienta de banda017 controla otra escala, k>=10000N², y este análisis muestra por qué su control absoluto no se trasplanta sin una cancelación adicional a k=0.
