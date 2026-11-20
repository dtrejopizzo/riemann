# POWER_THETA_SCHUR_DENSITY_075 — Densidad positiva del denominador regularizado

Estado: **PROVED/APROBADO**, revisión independiente POWER_THETA_SCHUR_DENSITY_AUDIT_075.md. Propiedad de la Phi real de073. No prueba el signo del resto G, del kernel Schur de orden dos ni de tres generadores. Papers intactos; sin cómputos nuevos.

## 1. Corpus y cambio preciso

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; releídos POWER_SCHUR_003 y las fuentes theta073. Las búsquedas de denominador regularizado, densidad Schur y fórmulas sinh/cosh no encontraron este objeto en phase211/103 ni una construcción literal en el corpus. Los antecedentes de regularización Schur de otras fases pertenecen a otros operadores; no se presenta su algoritmo general como nuevo.

El paso003 daba positividad real del primer cociente, sin preservar su kernel. La continuación074 identificó pesos bilaterales con cambio de signo y dejó abierta la positividad del denominador después de quitar sus ceros reales conocidos. Aquí se resuelve exactamente ESA obligación por una densidad explícita positiva. No se sustituye por otra función ni se afirma que un cociente de transformadas positivas sea una derivada logarítmica positiva.

## 2. Datos theta y definiciones

Sea Phi la función par positiva y suave de CONE001/073; V=−logPhi. Se usan los resultados reales ya probados

    V'''(x)>0 para TODO x>0,
    Z(z)=∫_R Phi(x)e^(zx)dx,
    M(u)=Z'(u)/Z(u), M''(u)<0 para u>0.

Phi y sus derivadas decaen más rápido que cualquier exponencial. Por tanto Z es entera, todas las integraciones por partes siguientes tienen bordes nulos y todos los momentos utilizados son finitos. Además V'(x)/x tiende a infinito por la cola theta explícita.

Fijar u>0 y escribir

    c=M(u)>0, a=M'(0)=∫x²Phi(x)dx/Z(0)>0,
    D_u(z)=zcZ(z)−uZ'(z).

La concavidad estricta de M y M(0)=0 implican c<ua. Definir en toda la recta

    h_u(x)=−cPhi'(x)−uxPhi(x)
           =Phi(x)[cV'(x)−ux],
    k_u(x)=∫_x^infinito h_u(y)dy.

Finalmente, con x real,

    Phi_u(x)=(1/u)∫_|x|^infinito sinh(u(y−|x|))k_u(y)dy.  (NEW-PHI)

## 3. Dos cambios de signo controlados, uno en cada peso

Como V es par, V'(0)=0. Para x>0,

    d/dx[V'(x)/x]
      =[xV''(x)−V'(x)]/x²
      =(1/x²)∫_0^x tV'''(t)dt>0.

Integración por partes da∫xV'(x)Phi(x)dx=Z(0). Así el promedio de V'(x)/x bajo la probabilidad x²Phi(x)/(aZ(0)) es1/a. La función estrictamente creciente no es constante, por lo que su límite en0 es menor que1/a. Como u/c>1/a y el límite en infinito es infinito, existe UN único b>0 con V'(b)/b=u/c.

En consecuencia h_u es impar y tiene signo negativo en0<x<b y positivo en x>b. Su integral sobre toda la recta es0. Por ello k_u es par y k_u'=−h_u; en la semirrecta positiva primero crece estrictamente hasta b y luego decrece estrictamente hacia0 desde valores positivos.

La paridad permite aplicar Fubini sólo en la semirrecta positiva, donde ∫_0^infinito y|h_u(y)|dy es finita. Luego integración por partes da

    ∫_R k_u(x)dx=2∫_0^infinito k_u(x)dx
                 =2∫_0^infinito y h_u(y)dy
                 =∫_R x h_u(x)dx=Z(0)(c−ua)<0.          (NEG-MASS)

Esto fuerza k_u(0)<0: de lo contrario la monotonía anterior haría k_u>=0 en toda la recta. Puesto que k_u(b)>0, existe exactamente UN beta en(0,b) con

    k_u(x)<0 para0<=x<beta,
    k_u(x)>0 para x>beta.                              (ONE-CROSS)

Todos los intercambios son absolutamente convergentes por la cola theta; no se infiere el signo de k sólo del signo de su integral.

## 4. Cancelación exacta y positividad de la nueva densidad

La transformada bilateral de h_u es D_u(z), pues∫−Phi'(x)e^(zx)dx=zZ(z). Como k_u'=−h_u, otra integración por partes da

    D_u(z)=z∫_R k_u(x)e^(zx)dx.

La igualdad D_u(u)=0 y la paridad de k implican

    ∫_0^infinito cosh(uy)k_u(y)dy=0.                    (BALANCE)

Para cada x>=0, ponga

    w_x(y)=sinh(u(y−x))1_(y>=x)/cosh(uy), y>=0.

Esta función es continua, no decreciente y estrictamente creciente para y>x, porque allí

    w_x'(y)=u cosh(ux)/cosh²(uy)>0.

La medida firmada dnu(y)=cosh(uy)k_u(y)dy tiene masa total0 y UN cruce de signo negativo/positivo en beta. Por tanto

    ∫w_x dnu=∫[w_x(y)−w_x(beta)]dnu(y)>0.

El integrando del último integral es no negativo en ambos lados de beta. La estricta positividad procede, por ejemplo, de y>max(x,beta), donde k_u>0 y w_x(y)>w_x(beta). Las colas garantizan integrabilidad.

Por NEW-PHI,

    Phi_u(x)>0 para TODO x real.                       (POSITIVE)

Este paso conserva la cancelación BALANCE antes de comparar pesos, en lugar de tomar valores absolutos de k_u.

## 5. Ecuación diferencial y transformada exacta

Para x>0, diferenciar NEW-PHI da

    Phi_u'(x)=−∫_x^infinito cosh(u(y−x))k_u(y)dy,
    Phi_u''(x)−u²Phi_u(x)=k_u(x).

BALANCE implica Phi_u'(0+)=0. La extensión par es por tanto suave y satisface la ecuación en toda la recta, sin masa delta en0.

Para todo A>u, la cola theta permite|k_u(y)|<=C_Ae^(−Ay); NEW-PHI y su fórmula de primera derivada dan cotas del mismo tipo para Phi_u y Phi_u'. Como A es arbitrario, las transformadas bilaterales son enteras y los bordes de integración por partes se anulan para todo z complejo. Se obtiene exactamente

    ∫_R Phi_u(x)e^(zx)dx
      =D_u(z)/[z(z²−u²)].                              (TRANSFORM)

Los valores en0,±u son removibles por la identidad entera. En particular la masa positiva es

    ∫_R Phi_u(x)dx=Z(0)(ua−c)/u²>0.

Se ha construido una representación positiva explícita del denominador regularizado, no sólo demostrado que su valor sobre el eje real es positivo.

## 6. Corolario real: positividad y logconvexidad estricta

Definir H_u(z)=∫Phi_u(x)e^(zx)dx por TRANSFORM. Para todo z real, H_u(z)>0 y

    (log H_u)''(z)=Var_(Phi_u exp(zx)/H_u(z))(X)>0.

La identidad se obtiene diferenciando bajo la integral, justificado por la cola superexponencial. La varianza es estrictamente positiva porque Phi_u es positiva en toda la recta, no una masa puntual. Por paridad, H_u es par y su derivada logarítmica es impar y creciente. No se infiere el signo de (log H_u)''' ni convexidad del hazard de Phi_u.

## 7. Comparación que aún falta para el paso Schur

El transformado003 es

    F_1(z)=c[zM(z)−uc]/[zc−uM(z)].

Si H_u(z)=∫Phi_u(x)e^(zx)dx, álgebra exacta usando TRANSFORM da

    F_1(z)=(c²/u) Z(z)/[zH_u(z)]−cz/u.

El residuo en0 es R_u=uc²/(ua−c)>0. Por tanto

    G_u(z)=F_1(z)−R_u/z
      =(c²/(uz))[Z(z)/H_u(z)−Z(0)/H_u(0)]−cz/u.

POSITIVE no ordena automáticamente el cociente Z/H_u ni lo identifica con una derivada logarítmica. Falta una desigualdad específica que compare Phi y Phi_u y controle el kernel de G o el de F_1. La clase genérica de hipótesis de073 no implica positividad de orden tres, como ya registra074; este resultado no retira ese límite. No se deduce positividad de tres generadores, de todos los órdenes ni una nueva ventana temporal.
