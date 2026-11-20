# POWER_INTERIOR_SCALE_030 — Compensación interior real a tasa fija

Estado: **PROVED**, revisión independiente APROBADA en POWER_INTERIOR_AUDIT_030.md. Con u=63/2 FIJO, para TODOS N>=2^20,

    int_1^(9/4) G_N(x) H(x)dx>1/100.                      (BLOCK)

Aquí G_N es el kernel gamma real y H conserva la aritmética completa del balance conjunto; en el bloque aparece el contacto q2. No es el valor total de W. Resto interior, cola y signo W global **OPEN**. Papers intactos.

## 1. Corpus y razón nueva

Leídos las reglas del proyecto, SIGNED_MEAN019 (PAIR), INVERSE_KERNEL020, CUMULATIVE_INVERSE022, ARCH_CELL026, DISCRETE_BALANCE027 y STATE029. Consultados índice ROUTES-TRIED-INDEX, grid maestro y CROSSWORD-TO-D.md sobre muestreo, Euler/Möbius, sumación por divisores, medias Riesz y errores aritméticos firmados.

Las inversiones de divisores y las identidades no se presentan como resultados nuevos de signo. Frente019–027, se utiliza la restricción FUNCIONAL completa para eliminar el inverso Möbius de la función gamma y cancelar todas las singularidades logarítmicas en enteros>1. El peso resultante sigue firmado. La novedad positiva es demostrar que el kernel gamma REAL compensa un bloque interior que contiene un contacto adverso, UNIFORMEMENTE a órdenes grandes y a la tasa FIJA31.5. No se mejora otra constante de una cuña de tasa variable y no se verifica una campaña de N.

El cálculo de una primitiva negativa registra además por qué la monotonía gamma sola no basta; el resultado principal BLOCK conserva su magnitud y obtiene compensación, no sólo otra obstrucción abstracta.

## 2. Inversión del peso conjunto y cancelación exacta de singularidades

Conserve K_N y Omega de026, de modo que W[g_N]/norm²=int_1^infty K_N(t)Omega(t)dt. La restricción de escalas REAL es

    G_N(x):=sum_(n>=1)K_N(nx)
           =w_N(x)−xw_N'(x)=x^(−32)D_N(logx)>0,
    D_N=33P_N−P_N', w_N=x^(−1/2)rho_N(logx).

La inversión adjunta finita del peso es

    H(x)=sum_(m<=x)mu(m)Omega(x/m)/m.

La fórmula FLOOR027 y las identidades sum_(m|r)mu(m)=1_(r=1), sum_(m|r)mu(m)log(r/m)=Lambda(r) simplifican EXACTAMENTE a

    H(x)=1+[log((x+1)/(x−1))+c−1−2Psi_1(x)]/x²,
    c=−gamma−log(4pi),
    Psi_1(x)=sum_(q<=x)qLambda(q).                         (H)

Por ejemplo, la parte H_floor de Omega se convierte en1, y todas las singularidades log((x+q)/(x−q)) con q>1 cancelan al sumar sus divisores. Sólo queda la singularidad integrable en x1. Los saltos de H en potencias primas son NEGATIVOS de tamaño2Lambda(q)/q. No se borran esos saltos.

La identidad conjunta queda

    W[g_N]/norm²=int_1^infty G_N(x)H(x)dx.                (JOINT-G)

Todo es absoluto para N fijo: G_N,K_N decaen como x^(-32) por polinomios en logx; H crece a lo sumo como O(1+logx) y tiene una singularidad logarítmica integrable en1. Para el intercambio de escalas, la suma de módulos se domina por sum_n n^(-32) por polinomios en logn, multiplicada por una integral convergente en x. Los valores en los puntos de salto no afectan la integral.

JOINT-G sola no es una desigualdad de signo y coincide con una aplicación legítima de la inversión clásica. Se utiliza a continuación para un bound firmado específico.

## 3. La monotonía gamma es real, pero falla el criterio de primitivas positivas

Por025, D_N es logcóncavo y

    D_N'(0)/D_N(0)=63(d+10)/(2d−1), d=N−1.

Decrece en d. Por tanto G_N es decreciente para TODOS N>=663, y G_N/x² es decreciente para TODOS N>=134: basta comparar el cociente anterior con32 y34, respectivamente. Son propiedades de la función gamma REAL, no hipótesis añadidas.

Sin embargo las premisas suficientes naturales de una integración de Stieltjes no se cumplen. El verificador racional prueba sobre el MISMO H completo

    int_1^(5/2) H(x)dx<−1/50,
    int_1^(5/2) x²H(x)dx<−1/4.                           (PRIMITIVE-FAIL)

Sólo q2 aparece en ese intervalo, con su valor real Lambda(2)=log2. Así el fallo del criterio es aritmético y cuantitativo, no un contraejemplo a la monotonía real de G. No se infiere de PRIMITIVE-FAIL que el emparejamiento con G_N sea negativo.

Para reproducir el primer bound, una primitiva desde1, en2<=T<3, es

    T−1+(c−1)(1−1/T)−log((T+1)/(T−1))/T
       +2logT−log(T²−1)+4log2/T.

La segunda es (T³−1)/3+(c−1)(T−1)+(T+1)log(T+1)−(T−1)log(T−1)−2log2−4log2(T−2). Las comparaciones en T5/2 usan exclusivamente intervalos de logaritmos/gamma, sin cuadratura ni prueba de otro N.

## 4. Comparación gamma uniforme en un bloque finito

Escriba rho_N(y)=C_N(y)/C_N(0). Su probabilidad espectral tiene momento EXACTO

    M2_N=E tau²=u²/(2N−3), u=63/2.

Las desigualdades elementales de coseno/seno dan

    |rho_N(y)−1|<=M2_N y²/2,
    |rho_N'(y)|<=M2_N |y|.

La forma gamma real del kernel positivo de escalas es

    G_N(x)=x^(−1/2)[(3/2)rho_N(logx)−rho_N'(logx)].

Compare con G_*(x)=(3/2)x^(−1/2). Puesto que log(9/4)<1, en TODO1<=x<=9/4,

    |G_N(x)−G_*(x)|<=(7/4)M2_N.                          (GAMMA-ERROR)

Se trata de una comparación local uniforme con error explícito; no se intercambia un límite N infinito con la forma completa ni se usa un modelo genérico en lugar del dato gamma.

También, usando (H) y ampliando sólo para un mayorante hasta5/2,

    int_1^(9/4)|H(x)|dx<6.                               (H-NORM)

En efecto |c−1|<23/5, int_1^(5/2)x^(-2)dx=3/5, int_1^infty x^(-2)log((x+1)/(x−1))dx=2log2<7/5, y el único término primo se acota por4log2 int_2^(5/2)x^(-2)dx<7/25. Sumando con la longitud3/2 da297/50<6.

De GAMMA-ERROR y H-NORM,

    |int_1^(9/4)(G_N−G_*)H|
      <(21/2)u²/(2N−3).                                 (ERROR)

La comparación conserva el SIGNO y TODOS los contactos del bloque en el término principal; el módulo sólo controla el error de aproximación gamma.

## 5. Integral principal exacta, con contacto2 incluido

Para1<=x<=9/4, Psi_1(x)=0 si x<2 y2log2 si x>=2. El integral de comparación I_*:=int_1^(9/4)G_*(x)H(x)dx es exactamente

    I_*=3/2+(19/27)(c−1)+(3/2)J
                   −log2(sqrt2−32/27),
    J=8/9−(16/81)log(13/5)+(2/3)log(5/2)
                                      −(4/3)arctan(1/5). (I)

La última contribución es precisamente la del contacto2. No se omite ninguna potencia prima: las siguientes empiezan en3, fuera del bloque.

Para verificar (I), integrar x^(-1/2), x^(-5/2) y el escalón en2. En el término logarítmico, el cambio x=z² lleva el extremo superior a z3/2; integración por partes y arctan(3/2)=pi/4+arctan(1/5) dan la fórmula J sin ningún resto numérico.

Los intervalos racionales003 de logaritmos, gamma y arctan(1/5), junto a sqrt2<99/70, prueban

    I_*>1/50.                                           (MAIN)

Su valor aproximado.0219844 sólo orienta; no se usa en la prueba.

## 6. Compensación real uniforme a tasa FIJA

Para TODOS N>=2^20,

    (21/2)u²/(2N−3)<1/200.

Combinar MAIN y ERROR prueba

    int_1^(9/4)G_N H>1/50−1/200=3/200>1/100.

Esto demuestra BLOCK sobre el kernel gamma real, pese a PRIMITIVE-FAIL. El resultado no usa un N elegido y certificado por separado: el único umbral pertenece a la cota monótona explícita de error en N.

El balance favorable incluye una región negativa real del peso después del salto en2. Por tanto es una compensación integrada, y no la suma de términos supuestamente positivos ni otra cola exterior que se vuelve despreciable.

## 7. Qué falta para el balance total

JOINT-G da

    W[g_N]/norm²=int_1^(9/4)G_NH+int_(9/4)^infty G_NH.

Sólo el primer término tiene el bound BLOCK. El segundo conserva todos los contactos siguientes y no se declara favorable ni pequeño. La cola positiva en la representación K Omega de027 sigue válida, pero no puede sumarse dos veces ni trasladarse sin contabilidad a un truncamiento diferente de JOINT-G.

El objetivo que queda es controlar el tramo adverso restante CONTRA G_N real y compararlo con las compensaciones favorables. No se propone una nueva cadena abstracta de primitivas; PRIMITIVE-FAIL explica el límite de ese criterio, y GAMMA-ERROR/MAIN suministran el retorno concreto al balance. No se afirma W>=0, ERR total de otro N, una nueva ventanaT ni cobertura completa de la tabla.

Verificador: tools/power_interior_scale_030_verify.py, aritmética Fraction/intervalos exactos; PASS. Certifica MAIN, H-NORM, el umbral analítico y PRIMITIVE-FAIL. La uniformidad en TODOS N>=2^20 se prueba en el texto. Papers intactos.
