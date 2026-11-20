# POWER_REAL_SECOND_PAIR_AND_TP2_112 — Segunda pareja positiva y TP2 de la familia real

## Actualización verificada: reproducción terminada y WM activada

Los logs constructor y reproducción independiente de110 son idénticos byte por byte, SHA256 `90a2ec137e806c8a7f8cce975f7af1cee375d9e48bdaf1c5bc302f7c06428539`. Driver: `c629d4ed4b5eeb625a69ee92f6000892b9493c50e825e9ade73bf3a5a9362108`; los cuatro módulos importados conservan los hashes auditados. Root comprobó por fracciones exactas el origen completo (16 hojas en lambda[0,1/4]) y 4198 hojas REST contiguas desde1/2 hasta845/32 en AMBOS logs. Ambos programas terminaron INCONCLUSIVE por8192 evaluaciones; no se cambia esa etiqueta ni se afirma FULLPASS hasta64.

La cola analítica104, auditada por root/casos/mapa, prueba Wmixed/Phi^4>6t^2/y^2 para todo t>=16. Por tanto la cobertura reproducida y esa cola se solapan y prueban WM para TODO t>0. Los tres prefijos103 completan MIXED4. Queda activada la aplicación real de las implicaciones auditadas112: segunda densidad Xi positiva para todos p,q>0, E/Psi decreciente, TP2 y confluencia estrictas. Root revisó también el literal§8 y las dos fuerzas verificadas independientemente por casos: se activan las comparaciones de la pareja límite estrella. No se afirma Xi_(p,q)/E_(p,q) decreciente para parámetros finitos, cinco potencias arbitrarias, todos los órdenes ni una ventana nueva.

Las menciones posteriores a réplica pendiente o aplicación condicional describen el estado anterior a esta actualización y quedan superadas exclusivamente por esta evidencia. El signo global permanece OPEN. Véase `POWER_REASSESSMENT.md` para el cambio de estrategia.


Estado: **IMPLICACIÓN ANALÍTICA PROBADA; aplicación global REAL CONDICIONAL hasta confirmar la reproducción independiente del compacto mixto.** Esta fuente NO declara todavía probado el signo mixto global. La cola t>=16 de104 está probada analíticamente; el cierre compacto y su reproducción deben confirmarse por separado antes de activar los resultados siguientes. No nuevos cómputos en esta fuente. Papers intactos.

## 1. Consulta y diferencia sustantiva

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README.md, R162_2300_MASTER_GRID.md y CROSSWORD-TO-D.md; cotejados083,099,102,103,104,106–110 y111. Los tres índices registran el criterio mixto103 y el NO-GO auxiliar111, pero no una prueba global activada de la segunda pareja ni de TP2 de la familia REAL.

103 ya identificó las fuerzas mixtas y el puente exacto entre los pivotes finitos y la pareja(J,K). Aquí se demuestra completa la consecuencia de cerrar ese signo: un nuevo numerador temporal positivo para TODOS los dos pivotes finitos, monotonía de la segunda pareja y TP2 estricta entre distintos resolventes reales. No se infiere TP2 de las monotonías individuales o de monotonía completa paramétrica:111 falsifica esa implicación para otra clase. La entrada que se usa aquí es específica y más fuerte, el sistema mixto real con sus cuatro Wronskianos.

No es la jerarquía Hankel abstracta083 ni una nueva escritura del objetivo global: se prueba un paso concreto de positividad temporal y comparación entre DOS parámetros. No se promueve ese paso a órdenes arbitrarios.

## 2. Hipótesis de activación, datos y conteo de raíces

Phi,J,K,a son exactamente los de102/103, con K PAR. Todas las funciones usadas son pares, reales analíticas y poseen supercolas con las derivadas necesarias. Definir Lp=D_t^2-p^2. La única hipótesis adicional a las fuentes ya probadas es

    W_t(K,J,Phi,J'')(t)>0 para TODO t>0.          (WM)

103 sección11.4 prueba ya que los tres Wronskianos iniciales del orden[K,J,Phi,J''] son estrictamente positivos. Bajo WM, Rolle ponderado da un sistema Chebyshev extendido de dimensión4: toda combinación no trivial tiene a lo sumo tres raíces positivas contando multiplicidades. Ésta es la propiedad denominada MIXED4 abajo.

Se usan los lemas con bordes102. Una función par h de supercolas con m raíces positivas produce al menos m+1 de Lp h: dividir por cosh(pt), derivar y usar el borde par en0 y los bordes de infinito; la identidad es

    [cosh(pt)^2(h/cosh(pt))']'=cosh(pt)Lp h.

Se conservan multiplicidades. Aplicar dos operadores Lp,Lq da al menos m+2 raíces positivas. Los argumentos se aplican a cualquier lista finita; no presuponen finitud de raíces antes de demostrarla. Las combinaciones nulas se descartan mediante el coeficiente explícito no nulo de la fuerza correspondiente y la independencia de MIXED4.

## 3. Segunda pareja: U tiene un cruce y Xi es positiva

Para p>0 escribir c=M(p), beta=ap^2/(ap-c), lambda=p^2c/(ap-c).102/103 prueban

    D_p>0, Psi_p>0,
    beta D_p+p^2Psi_p=lambda K,
    LpPsi_p=J-lambda K,
    (Psi_p/D_p)'<0.

Para q>0 definir, con transformadas bilaterales,

    F(z)=z ZPsi_p(z)/ZD_p(z)=G_p(z)/c,
    d=F(q)>0,
    E=G_q(dD_p-qPsi_p)>0,
    gamma=massPsi_p/massE>0,
    alpha=gamma q-q^2>0,
    C=d lambda/beta>0, D=dp^2/beta+q>0.

Aquí G_q es el Green anticausal102, no el resto G_p. Se tiene LqE=CK-DPsi_p y Cp^2-Dlambda=-qlambda. Los símbolos C,D en esta fuente son coeficientes; D_p sigue siendo la densidad del primer denominador.

El nuevo peso U=Psi_p-gamma E es par y de masa cero. El cálculo exacto103 da

    LpLqU=J''-a(lambda+gamma C)Phi
       +[lambda-q^2+gamma(C+D)]J-lambda alpha K. (U-FORCE)

La combinación MIXED4 no es trivial: su coeficiente de J'' es1. Si U tuviese dos raíces positivas contando multiplicidades, los dos lemas Rolle producirían al menos cuatro de U-FORCE, contradicción. U tiene a lo sumo una raíz positiva simple. No es nulo y tiene masa cero, por lo que debe tener exactamente un cambio de signo.

La orientación se fija usando únicamente un signo escalar no negativo YA PROBADO, sin inferir signos temporales de una transformada.099,102 y103 sección11.3 dan R_next(z)>=0 para todos p,q,z>0: los triples del kernel de F en nodos positivos pasan a un bloque auxiliar PSD al llevar un nodo a0, y sus dos pivotes d/q y aF-d/q son positivos. La doble congruencia de Schur deja R_next(z)/z no negativo. No se necesita trasladar estrictura mediante ese límite. Para Xi=G_0U, la masa cero asegura paridad suave y los bordes;102 da exactamente

    Xi''=U, Xi'(0)=0,
    R_next(z)=d z ZXi(z)/ZE(z).

Si el único cruce de U fuese positivo/negativo, todas sus integrales de cola serían negativas; Xi'>0 y Xi(infinito)=0 implicarían Xi<0. Esto haría ZXi(z)<0 y R_next(z)<0, contradicción. Luego

    U(t)<0 para 0<t<b, U(t)>0 para t>b,
    b es su único cruce positivo, simple,
    Xi(t)>0 para TODO t real.                    (SECOND-POSITIVE)

La estricta positividad de Xi sigue de la integral de cola de U, estrictamente positiva para todo t>0, y de Xi' negativa con límite0 en infinito. Ahora Xi>0 también implica R_next(z)>0, sin exigirlo en el argumento de orientación. Así E,Xi forman una NUEVA pareja positiva para TODOS los pivotes finitos p,q>0.

## 4. La segunda comparación temporal E/Psi_p también decrece

Para r>0 sea H_r=E-rPsi_p. Las mismas ecuaciones dan

    LpLqH_r=-rJ''+a(C+r lambda)Phi
       -[C+D+r(lambda-q^2)]J
       +lambda(q-rq^2)K.                         (RATIO-FORCE)

El coeficiente de J'' es-r, estrictamente negativo. MIXED4 y dos lemas Rolle implican que H_r tiene a lo sumo una raíz positiva simple. Un punto estacionario de E/Psi_p, con r=E(t)/Psi_p(t)>0, produciría una raíz doble de H_r. Por tanto (E/Psi_p)' nunca se anula para p,q,t>0.

La orientación se fija directamente en parámetros finitos, sin una estimación de cola ni un nuevo límite. La derivada continua nunca nula tiene signo constante en t. Por SECOND-POSITIVE,

    U=Psi_p[1-gamma E/Psi_p]

es negativa antes de su cruce y positiva después; por tanto E/Psi_p pasa desde valores mayores que1/gamma a valores menores. Su derivada no puede ser positiva. En consecuencia

    (E_(p,q)/Psi_p)'(t)<0
       para TODOS p,q,t>0.                      (SECOND-RATIO)

Este argumento no requiere convergencia uniforme en toda la semirrecta temporal ni transporte desde p infinito: utiliza el cruce real finito ya probado y la no anulación global de la derivada.

## 5. Diferencia dividida exacta y TP2 estricta

Poner V(x,t)=Psi_(sqrt(x))(t), x>0. Para q!=p,

    lambda_p=ZJ(p)/ZK(p),
    v_pq=(lambda_q-lambda_p)/(q^2-p^2).

La primera identidad procede de transformar LpPsi_p=J-lambda_pK y evaluar en z=p. Evaluar en z=q y usar el puente beta D_p=lambda_pK-p^2Psi_p da

    ZPsi_p(q)=v_pq ZK(q),
    d=q beta v_pq/(lambda_p-p^2v_pq),
    eta=q+dp^2/beta=q lambda_p/(lambda_p-p^2v_pq)>0,
    C=eta v_pq.

El denominador es positivo porque es beta ZD_p(q)/ZK(q); no se supone su signo a partir de una diferencia dividida abstracta. Aplicar Lq y usar los dos bordes prueba la identidad exacta

    E_(p,q)(t)=eta[Psi_p(t)-Psi_q(t)]/(q^2-p^2). (DIVIDED-GREEN)

En efecto Lq de su lado derecho es eta v_pq K-eta Psi_p=CK-DPsi_p, ya que eta=D. Es la fuerza de E. La diferencia homogénea con supercolas en ambos extremos es cero.

Al dividir por Psi_p y derivar en t, SECOND-RATIO implica

    derivative_t[Psi_q/Psi_p]
       =-(q^2-p^2)/eta * derivative_t[E_(p,q)/Psi_p]
       >0 para q>p.                             (CROSS-RATIO)

Así, para 0<x1<x2 y0<t1<t2,

    det[[V(x1,t1),V(x2,t1)],
         [V(x1,t2),V(x2,t2)]]>0.                 (STRICT-TP2)

Se ha usado el signo temporal específico obtenido mediante MIXED4. No se deduce STRICT-TP2 de la mera positividad de E ni de monotonías individuales;111 demuestra por qué ese atajo sería incorrecto.

## 6. Confluencia estricta

Las integrales anticausales y los coeficientes lambda son suaves en los parámetros positivos, con derivadas continuas en t sobre compactos. Se puede demostrar directamente el caso confluente, sin trasladar estrictura mediante un límite. Escribir lambda(x)=ZJ(sqrt(x))/ZK(sqrt(x)) y Lx=D_t^2-x. La identidad LxV=J-lambda(x)K da

    Lx(-partial_xV)=lambda'(x)K-V.

Derivar la identidad transformada y evaluar en z=p, x=p^2, prueba lambda'(p^2)=ZPsi_p(p)/ZK(p)>0. En la fuerza LpE_(p,p)=CK-DPsi_p, el balance transformado en z=p da C/D=lambda'(p^2). Por unicidad con los bordes,

    E_(p,p)(t)=-eta_(p,p) partial_x V(p^2,t),
    eta_(p,p)=D=p+F_p(p)p^2/beta>0.

La desigualdad SECOND-RATIO fue probada directamente también para q=p, mediante el mismo coeficiente-r de RATIO-FORCE. Dividir esta identidad por V(p^2,t) y derivar en t da

    partial_t partial_x log V(x,t)>0
       para TODO x,t>0.                         (STRICT-CONFLUENT)

Como E_(p,p)>0, también partial_xV(x,t)<0, pero no se afirma monotonía completa en x de todos los órdenes. STRICT-CONFLUENT y STRICT-TP2 son comparaciones de orden2; no constituyen TP de órdenes arbitrarios.

## 7. Alcance preciso y siguiente conservación no descargada

Una vez activada WM mediante reproducción independiente, los resultados sustantivos son SECOND-POSITIVE, SECOND-RATIO, STRICT-TP2 y STRICT-CONFLUENT para la familia REAL. La no negatividad del resto transformado escalar, suficiente para la orientación, estaba probada099/102/103; lo nuevo es la positividad de su densidad inversa seleccionada y las comparaciones temporales, que no se habían inferido de aquel signo escalar.

Para la pareja de parámetros FINITOS(p,q) no queda probado que Xi/E decrezca. Para H=Xi-rE, el cálculo de la siguiente obligación muestra por qué no se repite el mismo argumento automáticamente:

    LpLq(H'')=[1+r(C+D)]J''-raC Phi''
       -a[lambda+gamma C+rq lambda]Phi
       +[lambda-q^2+gamma(C+D)+rq lambda]J
       -lambda alpha K.

Aparece la quinta función Phi'', además de MIXED4. Haría falta una comparación nueva para esa familia o para sus coeficientes restringidos. No se afirma esa conservación, ni TP3/TPinf, ni un cono positivo cerrado de todos los órdenes.

Tampoco se obtiene nueva ventana T ni cinco potencias arbitrarias de la forma completa W. La cobertura de cuatro exponentes arbitrarios085 y la de trece exponentes>=32 de053 permanecen como estaban. Los nodos0 de las congruencias usadas son auxiliares, no nuevos tests admisibles. La prueba del signo global permanece OPEN.

Hasta confirmar y registrar la reproducción compacta que activa WM, TODOS los resultados globales nuevos de esta fuente permanecen CONDITIONAL. No se modifica ningún paper ni se ejecuta cómputo para esta deducción.

## 8. Comparación adicional de la pareja límite (J,K), para TODOS q>0

Esta ampliación también permanece **CONDITIONAL a WM**. Root y casos verificaron independientemente las identidades; no se ejecuta otro test. Para evitar confundirla con la pareja finita E_(p,q),Xi_(p,q), aquí se escriben estrellas para los objetos de103:

    d*_q=q ZK(q)/ZJ(q)=q/lambda_q,
    E*_q=G_q(d*_q J-qK)>0,
    gamma*_q=massK/massE*_q,
    U*_q=K-gamma*_q E*_q,
    Xi*_q=G_0U*_q>0.

La positividad y único cruce de esta pareja ESTRELLA ya están probados103 para todos q>0; lo nuevo bajo WM será su siguiente monotonía. Poner lambda0=massJ/massK=1/b0 y V0=lambda0H, con H de103. La convergencia V(x,t)->V0(t) en C1 local cuando x->0 procede de FINITE-GREEN y E*_q/q->H. Integrar LqPsi_q=J-lambda_qK da

    lambda_q-lambda0
       =q^2 massPsi_q/massK>0.

El puente exacto103 y las masas resultan

    E*_q=(q/lambda_q)V(q^2,.),
    gamma*_q=q lambda_q/(lambda_q-lambda0).

Además, diferenciar dos veces y usar los bordes verifica

    Xi*_q=[V0-V(q^2,.)]/(lambda_q-lambda0).        (STAR-IDENTITY)

En efecto, el numerador tiene segunda derivada (lambda_q-lambda0)K-q^2Psi_q, exactamente (lambda_q-lambda0)U*_q.

STRICT-TP2 extendida al parámetro0 por continuidad da que V(q^2,t)/V0(t) es NO DECRECIENTE en t. No se atribuye estrictura a este límite. Así

    Xi*_q/E*_q
      =[lambda_q/(q(lambda_q-lambda0))]
                    [V0/V(q^2,.)-1]

es no creciente. Para excluir estaciones, fijar r>0 y F=Xi*_q-rE*_q. Sus ecuaciones exactas dan

    Lq(F'')=a(1+rq)Phi
       -(1+gamma*_q d*_q+rq)J
       +(gamma*_q q-q^2)K-rd*_q J''.             (STAR-FORCE)

El coeficiente-rd*_q es no nulo. MIXED4 y los dos lemas Rolle, D2 seguido de Lq, excluyen una raíz doble positiva de F. Por tanto la derivada del cociente nunca se anula. Junto con el signo no positivo ya demostrado,

    (Xi*_q/E*_q)'(t)<0
       para TODOS q,t>0.                        (STAR-RATIO)

### Confluencia adicional q->0

103 prueba Xi*_q->Xi_lim y E*_q/q->H en C1 local. Así q Xi*_q/E*_q->Xi_lim/H en C1 local. STAR-RATIO sólo permite concluir de ese límite una derivada NO POSITIVA. Para obtener estrictura de forma independiente, fijar r>0 y F=Xi_lim-rH. Con gamma_bar=massK/massH y H''=b0J-K,

    F''''=a(1+r)Phi
       -(1+r+gamma_bar b0)J
       +gamma_bar K-rb0 J''.                     (ZERO-STAR-FORCE)

Es una combinación MIXED4 no trivial, con coeficiente-rb0. Dos aplicaciones del lema D2 excluyen una raíz doble positiva de F; por tanto la derivada de Xi_lim/H no se anula. Se concluye

    (Xi_lim/H)'(t)<0 para TODO t>0.               (ZERO-STAR-RATIO)

Esta ampliación prueba el siguiente cociente temporal para la pareja límite ESTRELLA, utilizando la misma comparación mixta bajo WM. No sustituye la obligación de cinco funciones para Xi_(p,q)/E_(p,q) de parámetros p,q FINITOS, exhibida en la sección7. No se afirma propagación indefinida, TP de órdenes superiores, cinco potencias W ni nueva ventana T. La reproducción que activa WM sigue siendo un requisito previo para declarar estas consecuencias globales como probadas.
