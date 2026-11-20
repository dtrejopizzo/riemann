# POWER_REAL_PAIR_DOUBLE_LIMIT_103 — Límite real normalizado y transferencia a parámetros finitos

Estado: **PROVED analítico y test puntual NEGATIVO, con auditorías independientes aprobadas y reproducción del certificado.** Véase `POWER_REAL_PAIR_DOUBLE_LIMIT_AUDIT_103.md`. Las extensiones analíticas posteriores prueban H/K estrictamente decreciente y, para la pareja REAL límite (J,K), E_q/K estrictamente decreciente, el único cruce global de U_*(q) y su primitiva doble positiva para TODO q>0. No se afirma cruce global para p finito ni nuevo signo W. Papers intactos.

La sección11 añade un puente EXACTO a p finito: (Psi_p/K)'<0 y (D_p/K)'>0. El cruce global del siguiente U finito queda condicionado a una comparación mixta distinta de EVEN4, todavía abierta.

## 1. Consulta y objetivo concreto

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README.md, R162_2300_MASTER_GRID.md y CROSSWORD-TO-D.md; cotejados075/077/078/081/089/099 y102 con su corolario auditado. La búsqueda en esos tres índices y el corpus POWER de `B−gamma E`, `B-gamma E`, `NEXT-REST`, `J4` y `ECT5` no encontró este límite puntual ni su test.102 ya construye E>0 y localiza U=B-gamma E, pero no decide el cruce de U.

La diferencia es estudiar un valor puntual de ese U REAL mediante dos límites rigurosos y escalas positivas. Un signo positivo en el límite refutaría el cruce negativo/positivo propuesto para parámetros FINITOS; un signo negativo sólo verificaría una condición de origen. No es una nueva reformulación de W ni un test de potenciales genéricos.

## 2. Escalas positivas que preservan el signo de U

Mantener todas las definiciones de102. Para p>0, escribir c=M(p), a=M'(0) y

    Q_p=J-beta D_p, beta=ap^2/(ap-c), Psi_p''=Q_p.

Normalizar la pareja por

    A_p=pD_p, B_p=(ap/c)Psi_p.                     (SCALE)

Ambas escalas son positivas. Para una pareja arbitraria A,B, el paso102 con q>0 usa

    F(z)=z ZB(z)/ZA(z), d=F(q),
    E=G_q(dA-qB), gamma=ZB(0)/ZE(0), U=B-gamma E,
    G_q h(t)=(1/q)int_|t|^infinito sinh[q(s-|t|)]h(s)ds.

Si A se multiplica por s>0 y B por t>0, entonces F,d se multiplican por t/s; el forzante dA-qB, E y U se multiplican por t, y gamma no cambia. Para SCALE, por tanto,

    d_hat=(a/c)d, E_hat=(ap/c)E,
    gamma_hat=gamma, U_hat=(ap/c)U.                (SIGN-SCALE)

Todas las afirmaciones de signo sobre U_hat son afirmaciones del mismo signo sobre el U original.

## 3. Convergencia p hacia infinito con derivadas y momentos

075/081 prueban c/p->0 y c->infinito; basta además pc->infinito. Definir la convolución probabilística bilateral

    R_p f(t)=(p/2)int_R exp[-p|t-s|]f(s)ds.

La solución de D_p''-p^2D_p=cPhi-pJ con los bordes de075 da exactamente

    A_p=R_pJ-(c/p)R_pPhi.                         (A-EXACT)

No se usa la representación anticausal con factores crecientes para tomar este límite.

Para sigma>0 y un entero k>=0 usar la norma

    ||f||_(sigma,k)=int_R exp(sigma|t|)|f(t)|dt
          +sum_(j=0)^k sup_t exp(sigma|t|)|f^(j)(t)|.

Phi y J tienen estas normas finitas para todo sigma,k. Para p>sigma, R_p conmuta con derivadas y su norma en cada uno de estos espacios es a lo sumo p/(p-sigma). Se obtiene usando exp(sigma|t|)<=exp(sigma|s|)exp(sigma|t-s|) y la integral exacta del kernel. Dos integraciones por partes, o Taylor integral de f(t+r)+f(t-r)-2f(t), dan

    R_pf-f=R_p f''/p^2.

Así R_pf->f en cada norma declarada, con coste a lo sumo [p/(p-sigma)]||f''||_(sigma,k)/p^2. A-EXACT implica A_p->J en todas ellas.

Para B_p, poner epsilon=c/(ap), que tiende a0. La ecuación de Psi_p y la identidad de resolvente dan la otra fórmula exacta

    B_p''=[a R_pPhi-J-a R_pJ''/(pc)]/(1-epsilon).
                                                               (B-EXACT)

En efecto beta D_p=[R_pJ-(c/p)R_pPhi]/(1-epsilon) y R_pJ-J=R_pJ''/p^2. Por tanto B_p''->aPhi-J en todas las normas anteriores.

Para funciones pares f con masa cero definir

    G_0 f(t)=int_|t|^infinito(s-|t|)f(s)ds.

Este operador es continuo en los espacios declarados: en las partes de orden0, la norma ponderada de salida se acota por sigma^-2 veces la de entrada; para la primera derivada el factor es sigma^-1, y desde la segunda derivada se usa (G_0 f)''=f. La masa cero asegura (G_0f)'(0)=0; la paridad de f asegura la suavidad de las derivadas restantes. Estos bounds salen de integrar los kernels r exp(-sigma r) y exp(-sigma r) sobre r>=0. Todas las fuerzas B_p'' tienen masa cero por077, al igual que aPhi-J.

Como B_p=G_0(B_p'') y K=G_0(aPhi-J), resulta

    A_p -> J, B_p -> K
    en TODAS las normas ||.||_(sigma,k).          (PAIR-LIMIT)

En particular convergen los valores y derivadas en compactos, todos los momentos polinomiales, y todas las transformadas bilaterales y sus derivadas en cada compacto real. No se ha requerido una cota uniforme superexponencial en p.

## 4. Continuidad del siguiente paso para cada q fijo

Fijar q>0 y aplicar102 a la pareja normalizada A_p,B_p. PAIR-LIMIT con sigma>q implica convergencia de d_hat_p=q ZB_p(q)/ZA_p(q) hacia d_*=q ZK(q)/ZJ(q). El denominador límite es positivo.

El operador G_q es continuo con los pesos sigma>q: el coste para orden0 es la integral

    int_0^infinito exp(-sigma r)sinh(qr)/q dr
      =1/(sigma^2-q^2).

Para la primera derivada se usa la integral con cosh y para las superiores la ecuación (G_qh)''-q^2G_qh=h. Los bordes pares se conservan por el balance cosh ya probado102. Así, para q fijo, E_hat_p converge con momentos y valores a

    E_*(q)=G_q[d_*J-qK]>0.

La positividad y masa positiva de E_* siguen directamente de102 aplicado a J,K, porque K/J es estrictamente decreciente hacia0. Por continuidad de las masas,

    U_hat_(p,q) -> U_*(q)
      =K-[ZK(0)/ZE_*(q)(0)]E_*(q)                 (FIXED-Q)

puntualmente, con derivadas y momentos. Por tanto el primer límite p hacia infinito es lícito para cada q positivo fijo.

## 5. Límite q hacia cero de la pareja (J,K)

Poner Jmass=int_0^infinito J, Kmass=int_0^infinito K y b0=Kmass/Jmass>0. Usar masas de semirrecta o bilaterales da los mismos cocientes. Por las supercolas,

    d_*/q=ZK(q)/ZJ(q) -> b0.

Entonces

    E_*(q)/q
      =G_q[(d_*/q)J-K] -> H=G_0(b0J-K).           (H-LIMIT)

La convergencia vale con derivadas y momentos. Se justifica por dominación de sinh(qr)/q por r exp(q0r), para 0<q<=q0 fijo, usando cualquier peso sigma>q0. También los kernels de primera derivada convergen; las derivadas superiores siguen de la ecuación diferencial. No se permuta una integral no dominada con el límite q->0.

Como K/J decrece estrictamente hacia0, b0 es un promedio estricto de ese cociente bajo J; por tanto 0<b0<(K/J)(0). La fuerza b0J-K tiene masa cero y un único cruce negativo/positivo. Su integral de cola es estrictamente positiva; de ahí H'<0 y H>0, por el mismo argumento elemental usado para Psi_p. En particular

    Hmass=int_0^infinito H>0.

H-LIMIT y la convergencia de masas implican

    U_*(q) -> U_lim=K-(Kmass/Hmass)H.              (U-LIMIT)

Este orden es precisamente p->infinito primero, q->0 después. No se necesita uniformidad conjunta en p,q ni una elección diagonal no demostrada.

## 6. Fórmula puntual exacta con I0,...,I6

Definir I_m=int_0^infinito t^mPhi(t)dt para m=0,...,6. Fubini absolutamente convergente da

    a=I2/I0, Jmass=I2,
    K(0)=aI1-I3/2,
    Kmass=aI2/2-I4/6,
    b0=Kmass/I2=a/2-I4/(6aI0),
    H(0)=(b0/2-a/6)I3+I5/24,
    Hmass=(b0/6-a/24)I4+I6/120.                   (FORMULAS)

Por ejemplo int tJ=I3/2 e int tK=aI3/6-I5/24; las fórmulas de H siguen de H=G_0(b0J-K). Para la masa de H se usa int G_0f=(1/2)int t^2f. Todos los denominadores son estrictamente positivos por las construcciones anteriores.

El test puntual exacto es

    U_lim(0)=K(0)-[Kmass/Hmass]H(0).

Es preferible decidir el numerador sin divisiones

    N=K(0)Hmass-Kmass H(0),
    sign U_lim(0)=sign N,                         (POINT-TEST)

con la normalización a=I2/I0 conservada o con I0 positivo limpiando los denominadores. Aquí NO se ha evaluado su signo. El diseño puntual separado debe fijar de antemano los parámetros de integración de los siete momentos y aceptar cualquiera de ambos signos, sin campaña ni ajuste tras observarlo.

## 7. Implicación a parámetros finitos y límites de la inferencia

Si POINT-TEST diese U_lim(0)>0, U-LIMIT permitiría elegir un q>0 FINITO con U_*(q)(0)>0. Para ese q fijo, FIXED-Q permitiría elegir p>0 FINITO y suficientemente grande con U_hat_(p,q)(0)>0. SIGN-SCALE implicaría U_(p,q)(0)>0 para el resto REAL original. Por continuidad, U sería positivo en un entorno del origen, lo que refutaría su patrón propuesto negativo/positivo de un único cruce.

Si el valor fuese negativo, sólo se verificaría el signo del origen en este límite; no se probaría el cruce global ni todos los parámetros. Un valor nulo o un encierro que no lo separase dejaría el test inconcluso. Ninguna alternativa implica por sí sola signo negativo de W o cierre del signo global. No se modifica ningún resultado102.

## 8. Único resultado puntual y reproducción independiente

Tras la auditoría previa de prueba, diseño y literal, la ÚNICA corrida constructora68812 terminó exit0/FULL PASS128 paneles. La reproducción independiente root91737 también terminó exit0/FULL PASS128 con el mismo resultado y hash:

    P=[-3.1683047444094325e-13 +/- 2.16e-30],
    U_lim(0)=[-1.35855717857699839e-6 +/- 8.09e-24],
    hash=5090a71fd7dd4ae786a3f785ca8a4c32d6691cf92af912d4e5fffff9e583d080.

Estos son encierros outward producidos por `tools/power_real_pair_limit_origin_103_verify.py`, no aproximaciones usadas como prueba. Ambos extremos de cada encierro son estrictamente negativos. Se mantuvieron todos los parámetros del diseño sin ajustes y no se ejecutaron tests adicionales.

Por tanto U_lim(0)<0. Los límites probados permiten además elegir q>0 suficientemente pequeño y FIJO con U_*(q)(0)<0, y para ese q elegir p FINITO suficientemente grande con U_(p,q)(0)<0; las escalas son positivas. No se obtiene un umbral cuantitativo de esos parámetros. Esto verifica una condición necesaria del cruce en el origen y NO es un falsificador. No prueba el cruce global de U, la positividad de Xi, conservación bajo nuevas reducciones, nueva cobertura W/T ni todos los órdenes. La rama positiva de la sección7 permanece como implicación condicional correcta, pero no es el resultado de esta corrida.

## 9. Extensión analítica posterior: H/K decrece y el U límite tiene un único cruce

Estado: **PROVED analítico, auditorías independientes aprobadas.** Esta deducción se obtuvo DESPUÉS del test puntual de la sección8. No requiere nuevos datos ni certificados. La búsqueda de `H/K`, `H−rK`, `H-rK` y `Xi_limit` en los tres índices y el corpus POWER no encontró esta monotonía; las apariciones de U_lim eran sólo las fórmulas y el resultado puntual103. Se utiliza directamente EVEN4, ya probado102 desde089.

Recordar b0=Kmass/Jmass>0, H>0 y

    H''=b0J-K, K''=aPhi-J.

Para r>0 poner F_r=H-rK. Diferenciar cuatro veces, conservando todas las contribuciones, da

    F_r''''=(b0+r)J''-raPhi''-aPhi+J.             (FOURTH)

Es una combinación de EVEN4=[J,Phi,J'',Phi''] no idénticamente nula: su coeficiente de J es1. Por102 tiene a lo sumo tres raíces positivas contando multiplicidades. Todas las funciones y derivadas de FOURTH tienen las mismas paridades y supercolas ya justificadas; F_r y F_r'' son pares y ninguna es idénticamente nula.

Si F_r tuviese dos raíces positivas contando multiplicidades, el lema D2 de102 forzaría al menos tres raíces positivas de F_r'' y, aplicándolo de nuevo a esta función par, al menos cuatro de F_r''''. Contradice la cota de EVEN4. Luego F_r tiene a lo sumo una raíz positiva simple.

Sea rho_H=H/K>0. Si rho_H'(t0)=0 en t0>0, elegir r=rho_H(t0) produciría una raíz doble de F_r, imposible. Así rho_H' no se anula en la semirrecta.

La dirección se determina de forma temporal. Para t suficientemente grande, tau(t)<=a/2. Con I(t)=int_t^infinito(s-t)Phi(s)ds>0 y usando que tau decrece,

    K(t)=int_t^infinito(s-t)[aPhi(s)-J(s)]ds
           >=(a/2)I(t),
    H(t)=int_t^infinito(s-t)[b0J(s)-K(s)]ds
           <=b0 int_t^infinito(s-t)J(s)ds
           <=b0 tau(t)I(t).

Por tanto

    0<rho_H(t)<=2b0 tau(t)/a ->0.

La derivada continua nunca nula tiene signo constante. Positividad y límite0 excluyen el signo positivo, de modo que

    (H/K)'(t)<0 para TODO t>0.                    (H-RATIO)

Ahora definir gamma_lim=Kmass/Hmass>0. Su recíproco Hmass/Kmass es el promedio de rho_H bajo la densidad positiva K en la semirrecta, por lo que

    0<1/gamma_lim<rho_H(0).

Por continuidad, H-RATIO y su límite0, existe un único t0>0 donde rho_H(t0)=1/gamma_lim. En consecuencia

    U_lim=K-gamma_lim H=K[1-gamma_lim rho_H]

es estrictamente negativo antes de t0 y estrictamente positivo después. El cruce es simple: en t0 su derivada es -gamma_lim K(t0)rho_H'(t0)>0. Además U_lim tiene masa cero por la elección de gamma_lim. Se concluye

    Xi_lim(t)=int_|t|^infinito(s-|t|)U_lim(s)ds>0,
    Xi_lim''=U_lim, Xi_lim'(0)=0.                 (LIMIT-PRIMITIVE)

La positividad sigue del único cruce y masa cero: la integral de cola de U_lim es positiva para t>0; por tanto Xi_lim'<0 y Xi_lim tiende a0 desde valores positivos. Paridad, suavidad y supercolas se conservan como en las primitivas anteriores.

Esta prueba GLOBAL para el objeto límite implica retrospectivamente U_lim(0)<0, de modo que el certificado puntual anterior queda lógicamente redundante para ese signo. Se conserva su cronología, diseño y resultado; no se lo presenta como consecuencia computacional de este teorema posterior.

La convergencia secuencial103 no transfiere automáticamente el conteo GLOBAL de raíces a parámetros finitos: no aporta control uniforme de las colas ni excluye raíces adicionales que escapen de los compactos. Por tanto el único cruce de U_(p,q) para TODOS los parámetros finitos, la positividad de su Xi y la conservación indefinida siguen OPEN. No se obtiene aquí nueva cobertura W/T ni todos los órdenes.

## 10. Pareja límite (J,K): cruce global para TODO q>0 sin segundo límite

Estado: **PROVED analítico, auditorías independientes aprobadas.** Esta segunda ampliación se obtuvo después de la sección9 y tampoco usa nuevos certificados. La búsqueda adicional de `E_q/K`, `E_*(q)/K`, `E−rK`, `E-rK` y la fórmula del forzante en los tres índices y el corpus POWER no encontró esta consecuencia. Se conserva aquí p->infinito, pero ya NO se necesita q->0 para concluir el cruce.

Para q>0, escribir en esta sección

    d_q=q ZK(q)/ZJ(q)>0,
    E_q=G_q(d_qJ-qK)>0,
    E_q''-q^2E_q=d_qJ-qK.

Es exactamente E_*(q) de las secciones4-5. Todas sus derivadas tienen los bordes pares y supercolas ya justificados102. Para r>0 fijar F=E_q-rK. Usando K''=aPhi-J y conmutando los operadores constantes,

    Lq(F'')=(d_q+r)J''-raPhi''
             +a(rq^2-q)Phi+(q-rq^2)J.            (ALL-Q-FORCING)

La combinación de EVEN4 es no trivial, pues d_q+r>0 es su coeficiente de J''. Por tanto tiene a lo sumo tres raíces positivas contando multiplicidades. Si F tuviese dos, D2 seguido de Lq forzaría al menos cuatro de ALL-Q-FORCING, por GAIN102. Luego F tiene a lo sumo una raíz positiva simple.

En consecuencia, para cualquier q,t>0,

    derivative_t [E_q(t)/K(t)] != 0:

un punto estacionario y r=E_q(t)/K(t)>0 producirían una raíz doble prohibida de F. Para fijar su signo NO se presupone una estimación de cola del cociente. Fijar cualquier t>0. La función

    q -> derivative_t [E_q(t)/K(t)]

es continua en q>0: d_q y el kernel Green dependen continuamente de q, con dominación superexponencial uniforme en cada compacto de q. La sección5 ya prueba la convergencia C1 E_q/q->H cuando q->0. Así

    (1/q) derivative_t[E_q(t)/K(t)]
       -> derivative_t[H(t)/K(t)]<0.

Para ese t fijo la derivada es negativa cuando q es suficientemente pequeño. Como es continua y nunca cero, no puede cambiar de signo en el intervalo conexo q>0. Puesto que t era arbitrario,

    derivative_t[E_q(t)/K(t)]<0
      para TODOS q,t>0.                          (ALL-Q-RATIO)

Para cada q definir gamma_q=Kmass/Emass_q>0 y rho_q=E_q/K. La función rho_q es positiva, estrictamente decreciente, y por tanto posee un límite ell_q>=0 en infinito. El promedio de rho_q bajo la densidad positiva K es estrictamente interior:

    ell_q<Emass_q/Kmass<rho_q(0).

Las desigualdades son estrictas porque rho_q decrece estrictamente y K es positiva en toda la semirrecta. No se necesita probar ell_q=0. El nivel Emass_q/Kmass=1/gamma_q se alcanza una sola vez en un t_q>0. Por tanto

    U_*(q)=K-gamma_q E_q=K[1-gamma_q rho_q]

tiene exactamente un cruce negativo/positivo, simple por ALL-Q-RATIO. La masa de U_*(q) es cero y se obtiene

    Xi_q(t)=int_|t|^infinito(s-|t|)U_*(q)(s)ds>0,
    Xi_q''=U_*(q), Xi_q'(0)=0,
      para TODO q>0.                             (ALL-Q-PRIMITIVE)

La positividad y suavidad siguen del mismo argumento de cola y masa cero de las primitivas anteriores. Si se conserva la normalización del siguiente resto102 para F_*(z)=zZK(z)/ZJ(z), su resto regularizado es exactamente

    R_*(q;z)=d_q z ZXi_q(z)/ZE_q(z)>0
      para TODOS q,z>0.

Ésta es positividad del resto escalar de la pareja límite, no una afirmación sobre todos los menores de su kernel.

El alcance final de103 mejora el solo test puntual y el doble límite: para p->infinito, la pareja (J,K) admite el siguiente numerador positivo PARA TODOS q>0. No se transfiere ese conteo global a p FINITO por convergencia en compactos o momentos. El cruce global de U_(p,q) para todos p,q finitos, la conservación posterior y todos los órdenes permanecen OPEN. Se mantienen el certificado puntual previo y su cronología; no se ejecutaron tests adicionales.

## 11. Puente exacto a p FINITO y criterio mixto suficiente aún abierto

Estado: **Identidades y monotonías PROVED, auditorías independientes aprobadas; criterio adicional CONDITIONAL.** Los antecedentes093/095, los tres índices y el corpus se cotejaron antes de plantear el criterio. La comparación mixta no se presenta como nueva bajo otro nombre: se identifica abajo su relación con el Wronskiano particular ya registrado. No se ejecuta otro certificado.

### 11.1. La pareja finita contiene exactamente el Green de la pareja (J,K)

Fijar p>0 y mantener c=M(p), beta=ap^2/(ap-c), lambda=p^2c/(ap-c). Las identidades numéricas exactas son

    beta c=a lambda, beta p-p^2=lambda.

D-EQ, PSI-EQ y K''=aPhi-J implican

    (beta D_p+p^2Psi_p)''
      =beta(cPhi-pJ+p^2D_p)+p^2(J-beta D_p)
      =a lambda Phi-lambda J=lambda K''.

La diferencia beta D_p+p^2Psi_p-lambda K tiene segunda derivada cero y decae en infinito junto con su primera derivada. Es por tanto idénticamente nula:

    beta D_p+p^2Psi_p=lambda K,
    LpPsi_p=J-lambda K.                           (FINITE-BRIDGE)

Tomar la transformada bilateral de la segunda ecuación y evaluar en z=p da ZJ(p)=lambda ZK(p). Para el d_p de la sección10,

    d_p=pZK(p)/ZJ(p)=p/lambda,
    Lp E_p=(p/lambda)(J-lambda K).

La solución con los dos bordes superexponenciales es única: una diferencia homogénea sería combinación de exp(pt),exp(-pt), incompatible con ambos bordes. Luego

    Psi_p=(lambda/p)E_p.                         (FINITE-GREEN)

ALL-Q-RATIO de la sección10 se aplica ahora EXACTAMENTE, sin límite en p. Como lambda/p>0,

    (Psi_p/K)'<0,
    (D_p/K)'=-(p^2/beta)(Psi_p/K)'>0,
      para TODOS p,t>0 FINITOS.                  (FINITE-RATIOS)

Son comparaciones temporales adicionales de la pareja real; no una transferencia informal desde p infinito.

### 11.2. Fuerza mixta del nuevo numerador

Para el siguiente paso de102, escribir A=D_p, B=Psi_p, F(z)=zZB(z)/ZA(z), d=F(q)>0 y E=G_q(dA-qB)>0. Definir

    C=d lambda/beta>0, D=dp^2/beta+q>0,
    gamma=massPsi_p/massE>0,
    alpha=gamma q-q^2>0,
    U=Psi_p-gamma E.

alpha>0 es precisamente la positividad del residuo102: gamma-q=r_q/d>0. Usando FINITE-BRIDGE,

    LqE=CK-DPsi_p,
    Cp^2-Dlambda=-qlambda.

Conmutar los dos operadores constantes y conservar todas las contribuciones da

    LpLqU=J''-a(lambda+gamma C)Phi
       +[lambda-q^2+gamma(C+D)]J
       -lambda alpha K.                          (MIXED-FORCING)

Así basta estudiar una combinación de la familia MIXTA

    [K,J,Phi,J''].                               (MIXED4)

No aparece J^(4), pero MIXED4 NO es EVEN4=[J,Phi,J'',Phi''];102 no demuestra que MIXED4 sea Chebyshev. Se mantienen las restricciones reales de coeficientes de MIXED-FORCING en vez de convertirlas en una afirmación genérica ya supuesta.

### 11.3. Qué probaría una cota mixta, y por qué es sólo suficiente

Si MIXED4 fuese Chebyshev de dimensión4 en toda la semirrecta con multiplicidades, MIXED-FORCING tendría a lo sumo tres raíces positivas. No sería idénticamente nula, pues su coeficiente de J'' es1. Dos aplicaciones del lema Lp/Lq de102, con paridad y bordes superexponenciales, implicarían que U tiene a lo sumo una raíz positiva contando multiplicidad. Su masa es cero y no sería nulo, de modo que tendría exactamente un cruce simple.

Para orientar ese cruce no se toma un límite de parámetros.099 prueba todos los triples del kernel de G_p en nodos positivos, y por tanto también del kernel de F=G_p/c. Al llevar un nodo a0 se obtiene un bloque auxiliar PSD en {0,q,z}.102 prueba que sus dos pivotes sucesivos son positivos: d/q>0 y aF-d/q>0, con aF=F'(0). La doble congruencia de Schur de099 deja la diagonal R_next(z)/z; en consecuencia

    R_next(z)>=0 para z>0.                       (SCALAR-INPUT)

Para orientación basta esta desigualdad no estricta, que se conserva al pasar al nodo auxiliar0. Para z distinto de q se usa directamente la congruencia; el valor removible z=q se obtiene por continuidad. Por la masa cero de U, Xi=G_0U tiene bordes pares correctos incluso antes de conocer su signo. NEXT-REST102 da exactamente R_next(z)=d z ZXi(z)/ZE(z).

Si el único cruce de U fuese positivo/negativo, todas sus integrales de cola serían negativas, de modo que Xi'>0 y Xi(infinito)=0 implicarían Xi<0. Su transformada bilateral sería estrictamente negativa y R_next(z)<0, contradiciendo SCALAR-INPUT. Por tanto el cruce sería negativo/positivo y Xi>0, como en las primitivas anteriores. Entonces también R_next(z)>0.

El criterio Chebyshev MIXED4 es SUFICIENTE; no se ha demostrado que sea necesario. MIXED-FORCING ocupa una clase restringida de combinaciones, y una prueba directa para esa clase también serviría. No se afirma aquí ninguna de ambas cotas de raíces.

La ruta suficiente global tiene un antecedente exacto093/095. Si K_odd=-K'/a, entonces K_odd''=v-w/a, con w=tPhi,v=-Phi', y K_odd(0)=K_odd(infinito)=0. La derivada de MIXED4 es, salvo factores constantes y orden de columnas,

    [w,v,w'',K_odd].

Es el Wronskiano PARTICULAR de093/095. Un sistema Chebyshev extendido global de esas cuatro funciones impares implicaría MIXED4 por el lema de un extremo en infinito.093 controla un entorno existente del origen y095 toda la cola t>=64; el intervalo intermedio sigue abierto. No se oculta ese antecedente ni se extrapolan sus signos locales a toda la semirrecta.

El avance incondicional de esta sección es FINITE-RATIOS y la identificación exacta FINITE-GREEN. El siguiente cruce de U para p finito, su numerador Xi positivo, la conservación posterior y todos los órdenes permanecen OPEN. No se ha abierto una campaña ni se ha modificado ningún paper.

### 11.4. Los tres primeros niveles mixtos sí se controlan globalmente

Esta comparación se deduce de EVEN4 sin asumir el criterio MIXED4. Para coeficientes reales no todos nulos, sea

    f=A K+B Phi+C J.

Entonces

    f''=AaPhi-AJ+B Phi''+C J''

es una combinación no trivial de EVEN4: sus coeficientes no pueden ser todos cero salvo A=B=C=0. Por tanto tiene a lo sumo tres raíces positivas contando multiplicidades. Si f tuviese tres raíces positivas, el lema D2 produciría al menos cuatro de f'', contradicción. Así [K,Phi,J], y cualquier reordenación de esas tres funciones, es Chebyshev3 en toda la semirrecta con multiplicidades.

Se puede fijar además la convexidad temporal que contiene este resultado. Poner

    tau=J/Phi, kappa=K/Phi=tau(K/J),
    S=kappa'/tau'.

tau'<0 por077 y (K/J)'<0 por102 implican kappa'<0, por lo que S>0. Ambos cocientes tau,kappa tienden a0 en infinito. El Wronskiano es exactamente

    W(Phi,J,K)=Phi^3 tau'^2 S'.

Chebyshev3 con multiplicidades implica que ese Wronskiano no se anula: si lo hiciese, una combinación no trivial de las tres funciones tendría una raíz positiva de multiplicidad al menos3. Por tanto S' es continuo, no se anula y tiene signo constante.

Supóngase S'>0. Para cualquier t>0, los límites tau,kappa->0 dan la identidad de promedio de cola

    kappa(t)/tau(t)
      =[int_t^infinito S(s)(-tau'(s))ds]
                    /[int_t^infinito(-tau'(s))ds]
      >S(t).

La integrabilidad del numerador es exactamente kappa(t), no una hipótesis adicional sobre S. En consecuencia

    derivative_t[kappa/tau]
       =tau'[S-kappa/tau]/tau>0,

contradiciendo kappa/tau=K/J estrictamente decreciente. Se concluye

    S'<0,
    d^2 kappa/d tau^2=S'/tau'>0.                 (MIXED-CONVEXITY)

Así kappa es estrictamente convexa como función de la coordenada tau, en todo su intervalo de valores. En el orden MIXED4=[K,J,Phi,J''], sus tres primeros Wronskianos son estrictamente positivos:

    W1=K>0,
    W2=W(K,J)=K^2(J/K)'>0,
    W3=W(K,J,Phi)=-W(Phi,J,K)>0.

La tercera igualdad es el intercambio de las columnas extremas. Sólo queda sin descargar el CUARTO Wronskiano mixto, o una cota directa suficiente para la clase restringida MIXED-FORCING. No se infiere ese cuarto signo de MIXED-CONVEXITY ni se afirma herencia de orden4.
