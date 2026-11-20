# POWER_THETA_DENSITY_ORIGIN_087 — Signo exacto del siguiente Wronskiano en el origen

Estado: **PROVED para UN punto y un entorno no cuantificado, auditoría independiente aprobada y reproducción independiente exit0/NEGATIVE con hash coincidente.** Véase `POWER_THETA_DENSITY_ORIGIN_AUDIT_087.md`. Se decide una condición necesaria del transporte puntual de cuatro densidades de la Phi REAL. No se afirma el signo global de ese Wronskiano, un nuevo signo de W ni el cierre de todos los órdenes. Papers intactos; sin campañas.

## 1. Objeto y diferencia frente086

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; leídos073–086, en particular las identidades de densidades lineales y el criterio de Rolle/Hankel de083/084.086 controla tres densidades usando exactamente N>0 de077. El siguiente paso requiere una desigualdad de orden mayor; no se hereda por positividad de los menores anteriores.

Para t>0, fijar V=−logPhi,p=V',q=V'',r=V''' y las cuatro densidades impares

    rho1=tPhi, rho2=(tPhi)'', rho3=−Phi', rho4=−Phi'''.

Al dividir por tPhi>0 se obtienen

    (1,A,B,C),
    A=p²−q−2p/t,
    B=p/t,
    C=(p³−3pq+r)/t.

Todas las razones tienen extensión par analítica al origen. Esta fuente certifica el signo del Wronskiano con variable lambda=t² ENlambda=0, reteniendo toda la suma theta. Se eligió ese punto por ser condición necesaria antes de proponer cualquier certificado global; no se buscaron pivotes o rangos con un signo deseado.

## 2. Forma Darboux exacta y nueva obligación

Con k=B'>0, J=(A'/B')'>0 y E=(C'/B')',086 da exactamente

    J=tN077/[p(tq−p)²]>0.

El cambio de coordenada B y la regla de Wronskianos dan

    W_t(1,A,B,C)=−k³J²(E/J)'.                       (RAISE)

Por tanto la condición(E/J)'>0 sería suficiente para el signo negativo del determinante puntual de cuatro densidades, por Rolle, usando la base de tres ya controlada. Es una condición NUEVA, no una consecuencia automática del signo de J.

De hecho el Wronskiano de cuatro filas es afín en V^(6)(t), con coeficiente exacto

    [V^(6)]W_t=−N077/[p t⁴].

077 controla N a través de derivadas hasta V''''; por sí solo no fija el jet nuevo. Esta observación no permite variar libremente los jets de la Phi real ni da un NO-GO: sólo localiza el dato cuantitativo adicional que debe probarse.

## 3. Límite simbólico sin cancelaciones singulares

Escribir la serie par normalizada

    Phi(t)/Phi(0)=sum_(j>=0)a_j lambda^j,
    lambda=t², a_j=Phi^(2j)(0)/[(2j)!Phi(0)], a0=1.

Multiplicar las cuatro funciones(1,A,B,C) por Phi/Phi(0) elimina todos los cocientes antes de calcular el límite. Las columnas resultantes son

    phi,
    (tphi)''/t,
    −phi'/t,
    −phi'''/t,

con phi=Phi/Phi(0). El Wronskiano de las razones enlambda=0 es exactamente detH, donde

    H=[[a0, 6a1, −2a1, −24a2],
       [a1, 20a2, −4a2, −120a3],
       [2a2, 84a3, −12a3, −672a4],
       [6a3, 432a4, −48a4, −4320a5]].                (ORIGIN-MATRIX)

En general la matriz con coeficientes no normalizados se divide por Phi(0)^4. Sólo se requieren derivadas pares hasta orden10, no12. Las filas incluyen los factores k! de las derivadas enlambda: no son coeficientes Taylor sin normalizar.

Además W_t=(2t)^6 W_lambda para t>0, por la regla de cambio de variable de Wronskianos. Como los factores previos de RAISE son positivos en la coordenada lambda cerca de0, un W_lambda(0)>0 refutaría esa condición suficiente de transporte cerca del origen, NO el signo de W. El certificado siguiente obtiene el signo opuesto y por tanto no da tal obstrucción.

## 4. Único encierro racional de la suma theta completa

El verificador tools/power_theta_density_origin_087_verify.py reutiliza las operaciones intervalares outward70dígitos de077, copiadas SIN importar ni ejecutar su malla. Se usa pi por Machin128 y exp por Taylor128 después de dividir el argumento por2048 y once cuadrados exteriores.

Definir S por Phi(t)=pi exp(5t/2)S(t), y

    Q0(y)=2y−3,
    Q_(j+1)(y)=2y(Q_j'−Q_j),
    S^(j)(0)=Σ_(m>=1)m²Q_j(pi m²)exp(−pi m²).

Se generan Q0,...,Q10 exactamente. Su máximo de sumas absolutas de coeficientes es B=1745986560; todos los grados son<=11. Se retienen m1,...,8. Para TODOS m>=9, pi m²>3m²>=243>11, y y^11exp(−y) decrece. Con exp3>16,

    m²|Q_j(y)|exp(−y)<=B·3^11 m^24 2^(−4m²).

La razón consecutiva es<=(10/9)^24·2^(−76)<1/2. La cola COMPLETA de cada S^(j),j<=10, queda encerrada en[−epsilon,epsilon], con

    epsilon=2B·3^11·9^24·2^(−324)
      =24093226761510505348366812581954355/
       16687398718132110018711107079449625895333629080911349765211262561111091607661254297054391304192.

Antes de formar los a_j se conserva TODO el prefactor:

    Phi^(n)(0)=pi Σ_(r=0)^n binom(n,r)(5/2)^(n−r) S^(r)(0).

Se añaden las colas a todas las Sder y luego se propagan por las operaciones intervalares. No se usa la derivada de S como si fuera la de Phi. Se comprueba que los encierros de Phi^(1),Phi^(3),...,Phi^(9) contienen0, de acuerdo con la paridad conocida; esas comprobaciones son validaciones de la implementación, no la prueba de paridad.

El determinante H se evalúa por sus24permutaciones con redondeos exteriores. El assert sólo exige que el intervalo resultante separe0, sin imponer anticipadamente qué signo debe aparecer. No hay una elección de precisión, número de modos o cola a partir del signo obtenido.

## 5. Resultado certificado y reproducción

La corrida puntual final, tras corregir el encabezado heredado y renombrar el script a087, terminó exit0:

    CERTIFIED origin Wronskian sign: NEGATIVE.

El intervalo exacto fue

    lower=−35600018069828449972375574599599903124108706418423624372844374475370483826219849/10^70,

    upper=−2225001129364278123273473412474993945256794144848122636536351986556379522095569/
           625000000000000000000000000000000000000000000000000000000000000000000.

En particular ambos extremos son negativos; la cifra aproximada−3.56000180698·10^9 sólo sirve para lectura, no como prueba.

Ejecutar

    python3 03-research/phase-211-sign-sandbox/tools/power_theta_density_origin_087_verify.py

SHA256 de la versión final:

    f8f28e5f33659ec7245e23906ab11addc5a04243f1d502a8a070dbf12d13d7b7.

El primer encierro del mismo punto ya había dado el mismo intervalo con el nombre provisional086. El único cambio antes de la corrida final fue el nombre y el docstring; no se alteró el objeto, precisión, cola o parámetro para obtener el signo. No es una campaña de casos.

## 6. Patrón de coeficientes que conserva el nivel anterior

Sea v_j=V^(j)(0) para j par. La expansión simbólica exacta da para las tres primeras densidades

    W_R3,lambda(0)=[(3v2²+v4)v6−20v2v4²]/180.

El Wronskiano de cuatro densidades es afín en v10 y su coeficiente es

    [v10]W_R4,lambda(0)
       =[(3v2²+v4)v6−20v2v4²]/151200
       =W_R3,lambda(0)/840.                        (JET-RAISE)

El resto sólo depende de v2,v4,v6,v8 y está dado explícitamente por ORIGIN-MATRIX sustituyendo la serie de exp[−v2lambda/2−v4lambda²/24−...]. JET-RAISE es un enlace triangular entre niveles, no una prueba de que el resto preserve el signo. El nuevo término v10 exige información real adicional aunque el coeficiente del nivel anterior ya tenga signo.

## 7. Alcance exacto

El signo requerido para la condición suficiente puntual R4 PASA en el origen. Por continuidad analítica también pasa en algún entorno positivo, sin radio cuantificado aquí. No se ha probado(E/J)'>0 para todo t>0, ni el signo puntual de los cuatro determinantes de densidades en todos sus nodos. Tampoco se ha tratado aquí el bloque de densidades S4.

La positividad global de cuatro generadores085 permanece como resultado independiente.087 no prueba otra región W, cinco generadores, todos los órdenes o una ventana temporal. Su resultado específico es decidir sin campaña un posible falsificador real de la nueva estrategia de transporte y mostrar el término de jet que debe controlarse en el siguiente nivel.
