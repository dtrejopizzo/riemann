# POWER_RECIPROCAL_SECANT_CONCAVITY_090 — Concavidad de una secante recíproca

**Actualización099:** la obligación REAL T_h>0 global quedó cerrada en `POWER_EXACT_H_GLOBAL_DESIGN_099.md`, auditada en `POWER_EXACT_H_GLOBAL_AUDIT_099.md` y resumida en `POWER_STATE_099.md`. Se prueban ambas curvaturas y todos los triples del resto G_p; el bloque auxiliar de cinco nodos está anclado en0 y NO son cinco generadores W admisibles. Las menciones de compacto/hipótesis pendiente abajo conservan el estado histórico de esta ronda; la herencia al siguiente nivel sigue abierta.

Estado: **PROVED el lema elemental y su aplicación theta por el dato global T_R>0 probado089, con constructor y reproducción root FULL PASS.** Auditoría independiente aprobada; véase `POWER_RECIPROCAL_SECANT_CONCAVITY_AUDIT_090.md`. No se afirma que los restos hereden nuevas desigualdades de Turán, ni signo global de W. Papers intactos.

## 1. Consulta y diferencia precisa

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; cotejados078,081–089.078 dejó abierta una segunda concavidad para controlar los pares del resto G_p;079/082 evitaron necesitarla para tres generadores originales.084 introdujo T_f=2f'f'''−3f''² para cuatro nodos.081 impide heredar ingenuamente monotonía y concavidad de la función original en todos los restos.

El nuevo paso respecto del corpus es una desigualdad integral: T_f>0 implica concavidad estricta del recíproco de la secante desde0. Se demuestra bajo hipótesis que no exigen f creciente y cóncava a la vez: basta f'>0 y T_f>0. Esto conecta el dato T_R global buscado089 con la obligación h de078. No se reclama prioridad mundial del lema ni se presume la hipótesis theta que falta.

## 2. Lema y extremo removible

Sea 0<L<=infinito y f∈C³([0,L)), con f'(x)>0 en TODO [0,L). Suponer

    T_f(x)=2f'(x)f'''(x)−3f''(x)²>0, 0<x<L.

Definir, para x>0,

    g(x)=f(x)−f(0)>0,
    h_0(x)=x/g(x).

Entonces h_0 se extiende como función C² al extremo0, con

    h_0(0)=1/f'(0),
    h_0''(x)<0, TODOS0<x<L.                         (SECANT-CONCAVITY)

No se requiere f>0 ni f''<0. En0 sólo se deduce h_0''(0)<=0; la desigualdad estricta allí necesita T_f(0)>0.

La extensión C² sigue de

    g(x)/x=int_0^1 f'(sx)ds,

cuyo lado derecho es C² y positivo hasta0. Además

    h_0''(0)=[3f''(0)²−2f'(0)f'''(0)]/[6f'(0)³]
             =−T_f(0)/[6f'(0)³]<=0.

## 3. Prueba por integración de la tangente

Poner w=(f')^(-1/2)>0. Derivar dos veces da

    w''=[3f''²−2f'f''']/(4f'^(5/2))
        =−T_f/(4f'^(5/2))<0, 0<x<L.

Así w es estrictamente cóncava en cada intervalo [0,x], y w(0)>0. Fijar x>0 y su tangente

    ell_x(s)=w(x)+w'(x)(s−x), 0<=s<=x.

La concavidad estricta implica w(s)<ell_x(s) para0<=s<x. En particular

    d_x=w(x)−xw'(x)>=w(0)>0.

Como ell_x es lineal y sus dos extremos son positivos, no hay un polo oculto al integrar su recíproco cuadrado. Se obtiene la desigualdad estricta

    g(x)=int_0^x ds/w(s)²
         >int_0^x ds/ell_x(s)²
         =x/[w(x)(w(x)−xw'(x))].                   (TANGENT-INTEGRAL)

La igualdad integral también vale si w'(x)=0, por cálculo directo o continuidad; no se divide por w' sin tratar ese borde. Tampoco se usa un signo de w'.

Escribir d=f'=1/w² y e=f''=−2w'/w³. El cálculo exacto del segundo cociente es

    h_0''=[2xd²−2gd−xge]/g³
          =2[x−g w(w−xw')]/(w⁴g³).

TANGENT-INTEGRAL prueba que el numerador es estrictamente negativo, mientras el denominador es positivo. Esto demuestra SECANT-CONCAVITY. La ganancia de signo procede de la desigualdad de tangentes integrada, no de una identidad del cociente por sí sola.

## 4. Aplicación theta, input global probado089

Usar las coordenadas reales073/077/078/086:

    a=M'(0)>0,
    R(x)=u/M(u), x=u²,
    b(x)=[au/M(u)−1]/u²=a[R(x)−R(0)]/x,
    h(x)=1/b(x).

La paridad analítica de Z y M(u)/u→a muestran que R es analítica en0 y R(0)=1/a.073 da R'>0 para x>0, y086 prueba R''<0 en TODO x>0. Por tanto R' decrece estrictamente, y su límite finito en0 satisface R'(0)>R'(x)>0. Se verifica así el extremo no degenerado que exige el lema, sin asumir un signo no demostrado para un cumulante en0.

089, su transporte de cuatro densidades y reproducción root87911 FULL PASS prueban

    T_R=2R'R'''−3R''²>0, TODO x>0.                 (THETA-INPUT-PROVED)

Por tanto SECANT-CONCAVITY se aplica a f=R y da

    h(x)=[x/(R(x)−R(0))]/a,
    h''(x)<0, TODO x>0.                            (THETA-PROVED)

El dato global procede del transporte probado089, no de extender085 fuera de su dominio:085 por sí solo, desde un extremo positivo, no reemplazaba la hipótesis en todo0..x. La prueba089 incluye ambos encierros compactos y la cola088 con reproducción independiente FULL PASS.

## 5. Consecuencia probada para los pares de G_p

El otro dato de078 ya está descargado086: g_*(x)=xb(x)=aR(x)−1 satisface g_*''<0. Por THETA-INPUT-PROVED y§4, h''<0 global. Por tanto, para cada P=p², poner

    C_P(x)=[b(P)−b(x)]/[xb(x)−Pb(P)].

Las fórmulas de078 son

    C_P'(x)=−b(P)b(x)²
        ·[h(x)−h(P)−(x−P)h'(x)]/[xb(x)−Pb(P)]²,
    [xC_P(x)]'=b(P)
        ·[g_*(x)−g_*(P)−(x−P)g_*'(x)]/[xb(x)−Pb(P)]².

Las concavidades estrictas dan C_P'<0 y(xC_P)'>0 para x≠P. En x=P sus límites también son estrictos: los numeradores de los errores de tangentes son respectivamente −h''(P)(x−P)²/2 y−g_*''(P)(x−P)²/2, mientras el denominador tiene término principal g_*'(P)²(x−P)² y g_*'(P)>0. Las singularidades son removibles, como en077.

Como G_p(z)=[a/B(p)]zC_P(z²)>0,

    −1<zG_p'(z)/G_p(z)<1, TODOS p,z>0.

El criterio de pares CONE001 prueba entonces todos los pares del kernel G_p definidos positivos para nodos distintos. No se exige G_p'>0; por ello el resultado es compatible con la obstrucción081.

Esta aplicación ya queda probada por089. No afirma T_(R_G)>0, ni concavidad de ambos datos recíprocos de G_p, ni preservación de las hipótesis al iterar Schur. Se obtiene un posible paso concreto sobre los cruces del resto, no un cierre de todos los órdenes o del objetivo global.

## 6. Extensión a un ancla interior: prueba con ambas orientaciones

Sea f∈C³(I), I un intervalo, f'>0 y T_f>0 en I. Para P∈I definir

    H_P(x)=(x−P)/[f(x)−f(P)], x≠P,
    H_P(P)=1/f'(P).

Entonces H_P es C² y H_P''<0 en TODO I, incluido x=P. No se requiere que P sea un extremo del intervalo ni que f sea cóncava.

La extensión C² sigue de [f(x)−f(P)]/(x−P)=int_0^1 f'(P+s(x−P))ds>0. Poner y=x−P, G=f(x)−f(P), w=(f')^(-1/2), y fijar la tangente ell_x(s)=w(x)+w'(x)(s−x). Como w''<0, esta tangente es estrictamente mayor que w(s) para s≠x en el segmento de extremos P,x. En particular d=w(x)−yw'(x)=ell_x(P)>w(P)>0, y la tangente es positiva en todo ese segmento.

Si x>P, integrar en la orientación positiva da

    G=int_P^x ds/w(s)²
      >int_P^x ds/ell_x(s)²=y/[w(x)d].

Si x<P, ambas integrales se orientan al revés y dan

    G=−int_x^P ds/w(s)²
      <−int_x^P ds/ell_x(s)²=y/[w(x)d].

La evaluación de la integral lineal vale también si w'(x)=0. La fórmula de derivada es

    H_P''(x)=2[y−G w(x)d]/[w(x)^4 G³].

Para x>P el numerador es negativo y G³>0. Para x<P el numerador es positivo y G³<0. En ambos casos H_P''<0. En el punto removible,

    H_P''(P)=−T_f(P)/[6f'(P)³]<0.

Así se comprueban explícitamente ambas orientaciones y el propio ancla.

## 7. Una curvatura del resto se descarga con el mismo dato T_R

Conservar x=z², P=p², b_P=b(P), g(x)=xb(x)=aR(x)−1 y h(x)=1/b(x). En esta sección R_G,S_G son los datos recíprocos del RESTO, no los de M:

    R_G(x)=z/G_p(z), S_G(x)=zG_p(z).

La expresión exacta077 de G_p da

    R_G(x)=(1/a){(x−P)/[h(x)−h(P)]−P b_P},
    S_G(x)=a{(x−P)/[g(x)−g(P)]−h(P)}.             (REST-SECANTS)

Para verificar la primera, usar h−h(P)=(b_P−b)/(bb_P); para la segunda, usar g(P)=Pb_P. Son igualdades algebraicas que se extienden a x=P por sus valores removibles.

Por THETA-INPUT-PROVED de089, g'>0 y T_g=a²T_R>0 en toda la semirrecta. El lema de ancla interior aplica a f=g y prueba

    S_G''(x)<0, TODOS p>0,x>0.                     (ONE-REST-CURVATURE)

Por tanto esta curvatura no exige ninguna hipótesis nueva por encima del dato T_R global: usa el mismo dato para TODOS los pivotes. Es una desigualdad efectiva de forma, no simplemente la identidad REST-SECANTS. El input089 ya tiene auditoría matemática/código y reproducción root87911 exit0/FULL PASS, por lo que ONE-REST-CURVATURE es PROVED para la Phi real.

En cambio R_G''<0 quedaría probado por el mismo lema SI se demostrara T_h>0 global, pues h'>0 ya se conoce077. No se afirma que T_h se herede. De hecho, la fórmula removible de§6 muestra que R_G''(P)<0 para TODOS los pivotes exigiría necesariamente T_h(P)>0. Así la familia de esas curvaturas tiene como obligación exacta adicional T_h>0, no la monotonía de G_p refutada081.

Si ese dato adicional se demostrara,082 aplicado a G_p, cuyos pares son PD por§5 bajo el input089, daría todos sus triples definidos positivos. Esto todavía no prueba que las mismas condiciones se preserven al siguiente resto.

## 8. La obligación T_h es un siguiente menor anclado, no herencia automática

Consulta adicional:083 identifica el Pfaffiano bordeado de tamaño cinco con el determinante de interpolación de las columnas

    (1,x,x²,R,xR).

Su especialización con un nodo en0 aclara exactamente qué dato nuevo se solicita. Escribir R0=R(0), G=R−R0>0 y H=x/G=ah. Restar R0 veces la primera columna a la cuarta y R0 veces la segunda a la quinta. Al expandir la fila correspondiente a0, queda el determinante de cuatro nodos de (x,x²,G,xG).

Dividir cada fila restante por su G_i>0 da (H,xH,1,x). Pasar los dos bloques de dos columnas a (1,x,H,xH) usa cuatro transposiciones y tiene signo positivo. En consecuencia, para cuatro nodos distintos positivos,

    det[1,x,x²,R,xR]_(nodos 0,x1,x2,x3,x4)
        =(producto_(i=1)^4G(xi))
             ·det[1,x,H,xH]_(nodos x1,x2,x3,x4).    (ANCHORED-FIVE)

La versión con los cuatro nodos positivos confluentes es exactamente

    W(x,x²,G,xG)=G⁴ W(1,x,H,xH)
                 =−G⁴T_H=−a²G⁴T_h.              (ANCHORED-JET)

Se usa la misma orientación de columnas que en084. El nodo0 aquí es auxiliar algebraico y no se convierte en un exponente admisible para W.

Así T_h>0 es la condición local del siguiente determinante de cinco columnas, con un nodo anclado en0 y los otros cuatro confluentes. El signo de T_R de cuatro columnas no la suministra. La identidad muestra la obligación real adicional sin declararla resuelta, ni afirmar positividad de todos los cinco nodos arbitrarios o preservación de todos los órdenes.

## 9. NO-GO de herencia genérica: contraejemplo global explícito

Estado de esta sección: **PROVED, auditorías independientes aprobadas.** Se refuta conservar automáticamente T_f>0 bajo H=x/(f−f0), incluso para f positiva, creciente y estrictamente cóncava en TODA la semirrecta. La diferencia frente084 es que el dato inicial aquí SÍ tiene T_f>0 global. No se modifica ningún dato theta ni se refuta T_h de la Phi real.

Definir para TODO x>=0

    w(x)=(5−exp(−x))/4,
    f(x)=1+(16/25){log[(5exp(x)−1)/4]
                          −1/[5exp(x)−1]+1/4}.

Entonces f(0)=1 y

    f'(x)=1/w(x)²>0,
    f''(x)=−2w'(x)/w(x)³<0,
    T_f(x)=−4w''(x)/w(x)^5=exp(−x)/w(x)^5>0.

Aquí w>0,w'=exp(−x)/4>0,w''=−exp(−x)/4<0 globalmente. f es positiva porque parte de1 y crece. La fórmula explícita de f se verifica derivando, sin cuadratura ni empalmes.

Sin embargo H(x)=x/[f(x)−f(0)] NO conserva T_H>0. La extensión regular en0 tiene series exactas

    f(x)−f(0)=x−x²/4+7x³/48−x⁴/12+O(x^5),
    H(x)=1+x/4−x²/12+5x³/192+O(x^4).

Por tanto

    H'(0)=1/4, H''(0)=−1/6, H'''(0)=5/32,
    T_H(0)=2H'(0)H'''(0)−3H''(0)²
           =5/64−1/12=−1/192<0.

Las funciones son analíticas en un entorno de0. Por continuidad, T_H<0 en algún intervalo positivo: no es sólo un fallo en un extremo excluido. No se pretende cuantificar ese intervalo, porque el signo ya decide la afirmación universal de herencia.

Una comprobación general del jet localiza el dato adicional. Si w(0)=1, b=w'(0), c=−w''(0), d=w'''(0), entonces

    H'(0)=b, H''(0)=−2c/3, H'''(0)=(bc+d)/2,
    T_H(0)=b²c+bd−4c²/3.

El ejemplo fija b=c=d=1/4. No se variaron parámetros en una campaña numérica. Aunque H''<0 queda garantizada por el lema de esta fuente, su nueva desigualdad de Turán falla.

Alcance: sólo se refuta esa herencia genérica. La curvatura REAL S_G''<0 de§7 permanece probada. T_h de la Phi real sigue OPEN y exigiría información específica, por ejemplo el menor de cinco columnas anclado de§8. No se refutan W, las coberturas085, otros invariantes ni la recursión general de Schur. No se afirma positividad de todos los triples de G_p, de cinco generadores originales o de todos los órdenes.
