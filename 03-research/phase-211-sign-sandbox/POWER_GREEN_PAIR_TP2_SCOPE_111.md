# POWER_GREEN_PAIR_TP2_SCOPE_111 — Monotonías individuales insuficientes para TP2

Estado: **PROVED analítico; auditorías matemática y literal independientes aprobadas.** Contraejemplo auxiliar compacto a una implicación genérica precisa. No es la pareja theta real. No se ejecuta cómputo alguno ni se modifica un paper.

Ampliación de la sección5.3: la misma familia es completamente monótona en x=p^2 para cada t fijo; argumento matemático root aprobado, auditoría independiente de esa ampliación pendiente. Tampoco esta condición adicional implica TP2.

## 1. Consulta, clase y diferencia respecto del programa real

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README.md, R162_2300_MASTER_GRID.md y CROSSWORD-TO-D.md; cotejados074/083/091/101/103/105. La búsqueda específica de `sinh(px0)`, `sinh(pL)`, `Vp/K`, `V_p/K`, `ratio individual`, `monotonías individuales` y `Green compacto` en los tres índices y el corpus POWER no encontró este falsificador.

074/101 estudian suficiencia de desigualdades de potenciales para kernels de sumas divididas;091/105 estudian signos de kernels auxiliares concretos. Aquí se considera otra implicación: si una pareja par J,K tiene J/K no decreciente y TODOS sus Green balanceados V_p son positivos y V_p/K estrictamente decrecientes, ¿la familia V(p,t) es TP2? El contraejemplo satisface esas tres condiciones para TODO p>0, pero produce menores de orden2 de ambos signos con los MISMOS dos parámetros.

La clase declarada permite densidades pares acotadas, compactas y suaves a trozos, positivas en el interior de un soporte común; los Green son pares C1 y satisfacen la ecuación global en sentido distribucional sin deltas. La construcción inicial tiene J/K no decreciente, y una perturbación analítica preserva todas las monotonías individuales para TODO p mientras vuelve J/K estrictamente creciente. Se demuestra además estabilidad LOCAL de los dos signos bajo regularización suave de ambas densidades para dos parámetros fijos; no se afirma la monotonía global para todos los parámetros después de esa segunda regularización.

Es esencial que la compatibilidad REAL J'=-tPhi, K''=aPhi-J no forma parte de esta clase; este ejemplo no la satisface. Tampoco se impone MIXED4 ni su análogo. No se refuta una inducción que use esas propiedades específicas, ni la familia real de103, ni el objetivo de todos los órdenes. Se excluye únicamente reemplazarlas por las tres condiciones genéricas indicadas.

## 2. Pareja, balance y solución global exacta

Fijar, sin parámetros por buscar,

    K(t)=1_(|t|<2),
    J(t)=[1+1_(1<|t|<2)]K(t).

Son funciones pares, acotadas, de soporte [-2,2]. En el interior t>=0, J/K vale1 hasta1 y2 después: es no decreciente. Para p>0 definir el promedio y el Green exactamente como en103:

    lambda_p=[int_0^2 cosh(ps)J(s)ds]
                  /[int_0^2 cosh(ps)K(s)ds]
             =2-1/[2cosh(p)],
    V_p(t)=(1/p)int_|t|^2 sinh[p(s-|t|)]
                            [J(s)-lambda_p K(s)]ds
             para |t|<=2,
    V_p(t)=0 para |t|>=2.

La fórmula de lambda usa sinh(2p)=2sinh(p)cosh(p), y garantiza el balance cosh exacto. Poner B_p=1/[2cosh(p)] y A_p=1-B_p. La fuerza vale -A_p en0<t<1 y B_p en1<t<2. Integrar sus dos partes da

    V_p(t)=[A_p-B_p cosh(pt)]/p^2,       0<=t<=1,
    V_p(t)=B_p[cosh(p(2-t))-1]/p^2,      1<=t<=2. (EXPLICIT)

Las dos fórmulas y sus primeras derivadas coinciden en1; V_p(2)=V_p'(2)=0 y V_p'(0)=0. La extensión par por cero es por tanto C1, compacta, y satisface en TODA R

    V_p''-p^2V_p=J-lambda_p K.

No hay deltas en0,1,2 ni en sus reflejos: V_p y V_p' son continuas en esos puntos. La ecuación también se verifica directamente a trozos.

## 3. Positividad y monotonía individual para TODOS los parámetros

En1<t<2, EXPLICIT da V_p>0 y

    V_p'(t)=-B_p sinh[p(2-t)]/p<0.

En0<t<1,

    V_p'(t)=-B_p sinh(pt)/p<0.

Como V_p(1)>0 y decrece hasta ese punto, también es positiva antes de1. Las derivadas en1 coinciden y son negativas. Así, para TODO p>0,

    V_p(t)>0 y (V_p/K)'(t)=V_p'(t)<0
      en TODO el interior 0<t<2.                 (INDIVIDUAL)

El cociente no se define fuera del soporte, donde ambas densidades se anulan. INDIVIDUAL es una afirmación global en el interior común, no una comprobación de algunos puntos.

## 4. Dos parámetros fijos y menores de ambos signos

Para cualquier q>p>0 y1<t<2, poner delta=2-t. Los factores B_q/potencias son positivos e independientes de t, y

    V_q/V_p=constante_positiva
                *[cosh(q delta)-1]/[cosh(p delta)-1].

La derivada logarítmica respecto de delta es

    q coth(q delta/2)-p coth(p delta/2)>0.

La desigualdad sigue de que z coth(z) es estrictamente creciente para z>0: su derivada es [sinh(z)cosh(z)-z]/sinh(z)^2>0. Por tanto V_q/V_p DECRECE respecto de t en todo1<t<2.

Para mostrar que no basta invertir la orientación, fijar ahora p=1,q=2. Para0<t<=1/2, poner c=cosh(1), z=cosh(t) y c2=2c^2-1. EXPLICIT y la identidad del ángulo doble dan

    V_2/V_1=[c/(2c2)]*[c2-z^2]/[2c-1-z].

El denominador es positivo. El signo de su derivada respecto de z es el de

    F(z,c)=z^2-2(2c-1)z+2c^2-1.

Tenemos c>3/2 y1<=z<=cosh(1/2)<8/7. La última cota sale del Taylor positivo: cosh(1/2)<=1+1/8+(1/384)/(1-1/120)<8/7. Como derivative_c F=4(c-z)>0,

    F(z,c)>F(z,3/2)=z^2-4z+7/2
              >=F(8/7,3/2)=23/98>0.

Así V_2/V_1 AUMENTA en0<t<=1/2. Los mismos dos parámetros producen, por tanto,

    det[[V_1(1/4),V_2(1/4)],
         [V_1(1/2),V_2(1/2)]]>0,

    det[[V_1(3/2),V_2(3/2)],
         [V_1(7/4),V_2(7/4)]]<0.                 (OPPOSITE-MINORS)

La familia no es TP2 ni tiene signo regular de orden2 después de invertir la orientación de un eje. Cambiar la coordenada p por x=p^2 no altera los signos, porque es estrictamente creciente.

## 5. Cociente J/K estrictamente creciente y estabilidad local

### 5.1. Perturbación que conserva las monotonías individuales para TODO p

Si se exige J/K estrictamente creciente, mantener K=1_(|t|<2) y, para delta>0, definir

    J_delta(t)=[1+1_(1<|t|<2)+delta t^2]K(t).

Su cociente r_delta=J_delta/K es estrictamente creciente en0<t<2, con un salto positivo en1. Definir lambda_(delta,p) mediante el mismo promedio cosh y V_(delta,p) mediante el mismo Green anticausal. Los bordes siguen siendo V'(0)=V'(2)=0, pues el primero procede del balance cosh y el segundo de la integral terminal.

Poner W=V_(delta,p)' en el intervalo abierto(0,2). La ecuación exacta, en sentido distribucional dentro de ese intervalo, es

    W''-p^2W=2delta t+delta_1,
    W(0)=W(2)=0,

donde delta_1 designa la masa de Dirac de peso1 en t=1, no el parámetro delta. El Green Dirichlet de este problema es

    G_D(t,s)=-sinh[p min(t,s)]sinh[p(2-max(t,s))]
                     /[p sinh(2p)]<0

para0<t,s<2. Integrar contra la medida positiva2delta s ds+delta_1 da W(t)<0 para TODO0<t<2 y TODO p>0. Como V_(delta,p)(2)=0, también V_(delta,p)>0 en ese interior. Así r_delta es estrictamente creciente y V_(delta,p)/K sigue estrictamente decreciente para TODOS los parámetros, no sólo los dos usados en los menores.

Para p=1,2 y los cuatro tiempos fijados, V_(delta,p) depende continuamente de delta: el promedio lambda y la fuerza son afines en delta, y lo mismo sucede con el Green. Por tanto los dos menores de OPPOSITE-MINORS conservan sus signos para todo delta>0 suficientemente pequeño. No se requiere elegir un valor numérico ni buscarlo. Esta variante prueba que la falta de crecimiento estricto de J/K no explica el contraejemplo.

También puede suavizarse sólo el escalón INTERIOR de r_delta, conservando K indicador: escoger una transición suave no decreciente cerca de1 y mantener delta t^2. Entonces r_delta'>0 para t>0, el mismo Green Dirichlet prueba W<0 para TODO p, y los dos menores persisten por continuidad para una transición suficientemente estrecha. Esto no suaviza el borde compacto de K ni produce una pareja positiva en toda R.

### 5.2. Suavización de ambas densidades: sólo se afirma estabilidad local

Tomar un mollificador par no negativo de soporte [-epsilon,epsilon], con integral1, y definir K_epsilon como su convolución con1_[-2,2]. Entonces K_epsilon es suave, par, no negativa, vale1 en |t|<=2-epsilon y tiene soporte [-2-epsilon,2+epsilon]. Elegir una función par suave r_epsilon, no decreciente para t>=0, que aproxima1+1_(|t|>1), con transición dentro de1-epsilon<|t|<1+epsilon, y poner J_epsilon=r_epsilon K_epsilon.

J_epsilon,K_epsilon convergen a J,K en L1 con cualquier peso exponencial fijo; sus soportes quedan en [-3,3] para epsilon pequeño. Para p=1 y p=2, los promedios lambda_p convergen y los Green convergen en C1 local mediante dominación de sinh y cosh en ese compacto. Por tanto los dos menores estrictos de OPPOSITE-MINORS conservan sus signos para epsilon suficientemente pequeño.

Además K_epsilon=1 en vecindades de los cuatro puntos escogidos. Las derivadas estrictamente negativas de V_1,V_2 allí permanecen negativas por convergencia C1; las monotonías individuales se conservan LOCALMENTE en esas vecindades para esos dos parámetros. La positividad de los Green regulares sigue del mismo cruce negativo/positivo y balance cosh.

No se ha probado que V_(epsilon,p)/K_epsilon sea globalmente decreciente en TODO el soporte para TODOS p simultáneamente. Por ello la regularización no se usa para afirmar un falsificador de una clase suave más fuerte. Su papel es sólo mostrar que los menores estrictos opuestos no dependen de evaluar en una discontinuidad.

### 5.3. La familia también es completamente monótona en x=p^2

Esta ampliación no utiliza nuevos datos. Se refiere al K indicador y al J original, o a J_delta de5.1; no atribuye esa propiedad a la pareja real. Escribir

    V(x,t)=V_(sqrt(x))(t), q_x(t)=-partial_t V(x,t), x>0.

En el intervalo(0,2), el argumento Dirichlet de5.1 da

    (-D_t^2+x)q_x=mu,
    q_x(0)=q_x(2)=0,
    mu=Dirac_1 para el ejemplo original,
    mu=Dirac_1+2delta t dt para J_delta.

mu es una medida positiva no nula, independiente de x. El Green del operador -D_t^2+x con estos bordes es el NEGATIVO del G_D escrito en5.1, por lo que es estrictamente positivo en el interior. Se tiene q_x>0.

La dependencia en x es suave: puede verse directamente en el Green explícito, cuyos denominadores son distintos de0 para x>0, en cualquier compacto de x. Permite diferenciar bajo las integrales contra la medida finita mu y después integrar en t. Sea q_n=partial_x^n q_x. Diferenciar n veces la ecuación, conservando los mismos bordes, da la recurrencia elemental

    (-D_t^2+x)q_n=-n q_(n-1), n>=1,
    q_n(0)=q_n(2)=0.

Por inducción y el Green positivo,

    (-1)^n q_n(t)>0
       para TODO n>=0, x>0, 0<t<2.

Como V(x,2)=0,

    V(x,t)=int_t^2 q_x(s)ds,
    (-1)^n partial_x^n V(x,t)
       =int_t^2 (-1)^n q_n(s)ds>0
       para TODO n>=0, x>0, 0<=t<2.             (COMPLETE-MONOTONICITY)

Así la monotonía completa PARAMÉTRICA de orden no acotado también se cumple en esta contraclase. Los dos menores opuestos de la sección4 permanecen para el ejemplo original y, por continuidad, para la variante estricta de5.1. Por tanto añadir monotonía completa en x a las positividades y monotonías individuales no implica TP2 de la familia en(x,t).

No se ha demostrado ni refutado COMPLETE-MONOTONICITY para las densidades reales de103. Tampoco se afirma que monotonía completa equivalga a TP de todos los órdenes ni que sea inútil en un argumento que use más estructura. Aquí sólo queda refutada la implicación genérica concreta hacia TP2, incluso bajo ese requisito paramétrico adicional.

## 6. Alcance del NO-GO limitado

La implicación refutada es únicamente: pareja compacta par con J/K no decreciente (incluso estrictamente creciente), todos los Green V_p positivos y todos los cocientes V_p/K decrecientes en el interior común, AUN AÑADIENDO monotonía completa de V en x=p^2 para cada t fijo, IMPLICA TP2 de la familia paramétrica. Las hipótesis se cumplen exactamente y los dos menores opuestos son analíticos, sin datos numéricos. La variante estricta usa existencia por continuidad de un delta positivo suficientemente pequeño, no una elección numérica presentada como explícita.

La pareja no es Phi/J/K real y no satisface la compatibilidad diferencial del programa ni sus comparaciones específicas de cuatro densidades. No se infiere fracaso de la ruta real103, no se retira ningún signo previamente probado y no se afirma imposibilidad de construir un cono con más estructura. No se ejecutó certificado ni campaña.
