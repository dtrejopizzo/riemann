# POWER_UNIFORM_CUTOFF_026 — Corte analítico en N para la cola del kernel compensado

Estado: PROVED dos cortes analíticos uniformes en N y control completo de la cola de K y de sus celdas. Revisión independiente aprobada en POWER_ARCH_CELL_AUDIT_026.md; verificador reproducido por root: PASS. Sin certificados fila a fila. Papers intactos.

## Corpus y razón nueva antes de construir

Leídos las reglas del proyecto, INVERSE_KERNEL020, CUMULATIVE_INVERSE022, CELL_TEST024 y el lema logcóncavo025; búsquedas en índice/grid/crucigrama (Riccati/Bessel/coeficientes/logconcavidad/corte). Los signos de h y K ya tienen falsificadores interiores. La diferencia aquí es reemplazar el corte certificado para un solo N por una FÓRMULA en N, utilizando ratios de coeficientes y la ecuación diferencial del mismo kernel gamma. No se coleccionan puntos ni se extrapola positividad de una fila a otras.

## 1. Resultado uniforme

Fije u=63/2 y d=N−1. Para N>=3 defina

    t_J(d)=d(d+220)/(330d+6300),
    M_d=u²/(2d−1), Q_d=sqrt(9/4+M_d),
    t_R(d)=2d Q_d/(u²−Q_d²),
    t_*(N)=min(t_J(d),t_R(d)).

Los denominadores son positivos. Para N=2 ponga t_*(2)=1/30−1/693. Entonces

    D_N'(t)/D_N(t)<=30 para TODO t>=t_*(N),             (LOG)
    K_N(x)>=x^-32D_N(logx)/4>0
                       para TODO x>=exp(t_*(N)).       (TAIL)

Aquí D_N=33P_N−P_N' y K_N es la suma Möbius COMPLETA, no un polinomio aproximado ni un prefijo. En particular t_J(d)<d/30 para todos d>1 y ambos cortes son d/330+O(1): el exponente del corte exterior mejora de escala d/30 a d/330.

Se obtiene además sin barrido de N el rango uniforme

    K_N(x)>0 para TODOS2<=N<=129, x>=exp(2/3).           (RANGE)

No se prueba signo de K en la región interior ni positividad de W en todos esos N.

## 2. Corte racional por Jensen sobre los coeficientes

Use los coeficientes positivos de P_N=Σp_jt^j. Los de D_N son

    D_j=p_j(3d+30j)/(2d−j)>0.

Para d>1, sus cocientes de derivación satisfacen, j0..d−1,

    r_j=(j+1)D_(j+1)/D_j
       =63(d−j)/(2d−j−1)·(1+10/(d+10j)); r_d=0.

La función f(z)=(d−z)/(2d−z−1) es decreciente y cóncava en[0,d]. Si L=D_N'(t)/D_N(t), la probabilidad con pesos D_jt^j/D_N(t) tiene media del índice tL. Así

    L=E r_j<=63(1+10/d)E f(j)
              <=63(1+10/d)f(tL).                       (JEN)

Se tiene tL<d porque todos los coeficientes son positivos. En t=t_J se comprueba exactamente

    30=63(1+10/d)f(30t_J),
    30t_J<d,

pues la diferencia después de multiplicar por el denominador positivo es −3d−660+990t+18900t/d. Si L>30, f(tL)<f(30t_J), contradiciendo JEN. Para t>=t_J, si30t>=d es inmediato L<d/t<=30; si30t<d se aplica la misma comparación por monotonía de f. Esto prueba LOG con t_J para TODOS N>=3 sin chequear cada fila.

La desigualdad t_J<d/30 equivale a d>1. Su expansión asintótica tiene término principal d/330. La logconcavidad de D de025 es compatible con esta prueba, pero no se necesita invocarla para interpolar filas.

## 3. Corte Riccati por la autocorrelación gamma

Escriba rho_N(t)=e^-ut P_N(t)>0 y q(t)=−rho_N'(t)/rho_N(t)>0 para t>0. La positividad se sigue de la representación de calor gamma de018. La recurrencia de p_j demuestra la ecuación diferencial

    rho_N''−(2d/t)rho_N'−u²rho_N=0,
    q'=q²+(2d/t)q−u².                                 (RIC)

Como P_N tiene grado d y coeficiente principal positivo,

    q(t)=u−d/t+O(t^-2),
    q'(t)=d/t²+O(t^-3)>0 para t grande.

Se puede demostrar una cota global de curvatura SIN citar una desigualdad especial de Bessel:

    0<q'(t)<M_d=u²/(2d−1), t>0.                       (CURV)

En efecto, al derivar RIC, si q'=0 se obtiene q''=−2dq/t²<0. Cualquier paso de valores no positivos a los valores positivos finales requeriría un cruce ascendente, imposible con esa derivada. Si q'=M_d, RIC da2dq/t=2dM_d−q², y por ello q''=2qM_d+q²/t>0. Cualquier valor por encima de M_d debería volver a bajar porque q'->0, pero todo cruce del nivel M_d tiene derivada positiva. También se excluyen los contactos exactos por el mismo argumento. Así CURV vale en todo t>0, no solo cerca del origen.

La parte inferior de CURV y RIC dan

    q(t)>sqrt[(d/t)²+u²]−d/t.                           (ROOT)

Por otro lado D_N=e^ut rho_N(3/2+q), luego

    D_N'/D_N=u−q+q'/(3/2+q)
             <u−q+M_d/(3/2+q).

El último lado es <=u−3/2=30 si q>=Q_d=sqrt(9/4+M_d). Para d>=2, Q_d<u. El lado derecho de ROOT alcanza Q_d exactamente en t_R=2dQ_d/(u²−Q_d²). Por tanto LOG vale con t_R para todo N>=3. Su término principal es3d/(u²−9/4)=d/330.

Para N=2, D_N(t)=3/2+(2079/2)t; su logderivada es <=30 cuando t>=1/30−1/693, dando el caso separado sin usar un denominador de t_R no positivo.

## 4. Un rango entero de N sin certificados individuales

El corte Riccati permite recuperar y extender analíticamente el sitio2/3 que025 certificaba solo para N129. Con x=2d−1,

    t_R=(2/3)(x+1)sqrt[x(x+441)]/(440x−441).

Dos veces su derivada logarítmica tiene signo del polinomio

    T(x)=880x³+192276x²−778365x−194481.

La expansión T(5+y)=830594+1210395y+205476y²+880y³ tiene todos los coeficientes positivos. Por tanto t_R crece para d>=3. La comparación t_R(128)<2/3 se reduce a la desigualdad racional

    9·128² Q_128² <(u²−Q_128²)².

Para d=2 se comprueba la misma comparación racional; para d=1 se usa el corte lineal anterior. Son DOS comparaciones de los extremos de una fórmula monótona, no una campaña de certificados de129 filas. Esto prueba LOG para todo2<=N<=129,t>=2/3 y por§5 prueba RANGE.

## 5. La cola Möbius completa y las celdas restantes

La fórmula exacta es

    K_N(x)=x^-32Σ(m>=1)mu(m)m^-32D_N(logx+logm).

Si logx>=t_*(N), integrar LOG da D_N(logx+logm)<=m^30D_N(logx). Por |mu|<=1 y Σ(m>=2)m^-2<=3/4,

    |K_N(x)/(x^-32D_N(logx))−1|<=3/4,

que prueba TAIL con TODA la suma. No se resta una cola de signo desconocido sin controlarla.

Ponga X_N=exp(t_*(N)). La identidad (J_N/x)'=−K_N/x² y J_N/x->0 da, para x>=X_N,

    J_N(x)=x∫_x^infinito K_N(t)t^-2dt
      >=(x/4)∫_x^infinito t^-34D_N(logt)dt>0.           (JTAIL)

Para cualquier celda[n−1,n] con n−1>=X_N, la monotonía de J_N/x implica

    S_N(n)=H_(n−1)∫_(n−1)^nJ_N−logn J_N(n)
      >=[H_(n−1)(1−1/(2n))−logn]J_N(n)
      >=(3/4−log2)J_N(n)>0.                           (CELLTAIL)

Las dos cotas armónicas empleadas, ya demostradas en el criterio celular, son H_(n−1)−logn>=1−log2 y H_(n−1)/(2n)<=1/4. JTAIL permite incluso sustituir J_N(n) por una integral gamma positiva explícita. Así la parte de ERR=−2ΣS_N(n) formada por esas celdas es favorable, con una cota cuantitativa completa.

El número de celdas interiores aún necesitadas de control queda acotado por ceil(X_N). En términos del exponente, pasa del corte previo de orden exp(d/30) a exp(d/330+O(1)). Sigue creciendo con N; no se ha eliminado el problema interior.

## 6. Alcance

Se obtuvo un corte ANALÍTICO para todos N, y un rango2..129 con cola positiva desde un mismo sitio. No se requiere una nueva matriz ni un certificado polinómico por cada N. Para N129, combinado con S129(2)>33/100 ya auditado, CELLTAIL vuelve a dar ERR129<−33/50 completo; ese caso ya estaba probado por025 y no se cuenta como nueva cobertura de W.

Para otros N siguen faltando los promedios interiores. Ninguna cota de cola aislada prueba el signo de W ni todos los bloques. Las nuevas fórmulas sirven para localizar y reducir cuantitativamente la obligación restante, conservando la aritmética firmada y todos los contactos.
