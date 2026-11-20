# POWER_THETA_DENSITY_CONCAVITY_086 — Curvatura global por densidades lineales

Estado: **PROVED, auditoría independiente aprobada.** Véase `POWER_THETA_DENSITY_CONCAVITY_AUDIT_086.md`. Para la Phi real, R(lambda)=sqrt(lambda)/M(sqrt(lambda)) satisface R''(lambda)<0 para TODO lambda>0. La prueba usa las desigualdades reales ya probadas077 y una transformación integral de tres densidades. No necesita el certificado080. No afirma orden arbitrario ni signo global de W. Papers intactos.

## 1. Consulta y diferencia precisa

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; cotejados073–085 y antecedentes SCHUR003/074.079 reducía tres generadores a una curvatura real;078 probaba su cola,080 ofrece una descarga compacta independiente.083 y su apéndice explicitan una jerarquía abstracta, pero no prueban sus signos reales.

Aquí cambia el objeto: se eliminan los cocientes multiplicando cada fila por Z'(u)>0 y se estudian TRES densidades LINEALES de Phi. Su determinante puntual es controlado EXACTAMENTE por N>0 de077, dato específico que no contienen las hipótesis genéricas refutadas074. Este enlace descarga la curvatura en toda la semirrecta, sin nuevos certificados, campañas o supuestos sobre momentos del cociente.

## 2. Datos reales ya probados y enunciado

Sea Phi la densidad par real de073–077, Z(u)=int_R exp(ut)Phi(t)dt y M=Z'/Z. Phi es positiva, suave, y sus derivadas pertinentes decaen más rápido que cualquier exponencial. Poner, para t>0,

    V=−logPhi, p=V', q=V'', r=V''',
    D=tq−p,
    C=p³+tp²q−pq−tpr+tq²,
    N=DC'−trC.

077 prueba p>0,D>0,C>0,N>0 en TODO t>0. Sólo p,D,N intervienen en el signo siguiente. El teorema es

    R(lambda)=u/M(u)=uZ(u)/Z'(u), lambda=u²,
    R''(lambda)<0, TODOS lambda>0.                  (GLOBAL-CURVATURE)

Las primas de R significan derivadas respecto de lambda; las de p,C,etc. respecto de t. Z'(u)>0 para u>0 porque Phi es par y positiva.

## 3. El determinante de densidades y la cancelación nueva

Considerar las tres densidades impares

    rho_1=tPhi, rho_2=(tPhi)'', rho_3=−Phi'.

En t>0, dividirlas por tPhi>0 da

    (rho_1,rho_2,rho_3)=tPhi·(1,A,B),
    A=p²−q−2p/t, B=p/t.

Se tiene B'=D/t²>0. Escribir A0=p²−q, de modo que A0'=2pq−r. Expansión directa de C da

    C=tp A0'−D A0,
    C'=2p A0'+tp A0''−tr A0,
    N=p{D[2A0'+tA0'']−t²rA0'}.

Por otro lado,

    A'/B'=t²A0'/D−2,
    (A'/B')'=t{D[2A0'+tA0'']−t²rA0'}/D²
               =tN/(pD²)>0.                       (DENSITY-CURVATURE)

Es la misma N certificada077, sin término residual. Por tanto A, visto como función de la coordenada estrictamente creciente B, es estrictamente convexa. Para TODO0<t1<t2<t3,

    det[(1,A(t_i),B(t_i))]_(i=1)^3<0,
    det[(rho_1(t_i),rho_2(t_i),rho_3(t_i))]_(i=1)^3<0. (DENSITY-SIGN)

El signo se fija intercambiando las dos últimas columnas: det[1,B,A]>0 es la desigualdad estricta de secantes de una función convexa.

## 4. Positividad estricta del kernel sinh

Para u_i,t_j positivos y estrictamente crecientes,

    det[sinh(u_i t_j)]_(i,j=1)^3>0.                (SINH-TP3)

Prueba elemental: truncar la serie sinh y aplicar Cauchy–Binet. Cada término es un producto de determinantes de monomios con exponentes impares estrictamente crecientes y coeficientes positivos. Estos determinantes son positivos en nodos positivos ordenados. Para justificar esa propiedad de monomios, Rolle ponderado muestra por inducción que una combinación de j potencias distintas tiene a lo sumo j−1 ceros positivos; su Wronskiano tiene signo positivo, fijado por la Vandermonde de sus exponentes. El límite confluente fija entonces el signo positivo del determinante de evaluación. Los truncamientos convergen en cada conjunto de nodos; ya el término con exponentes1,3,5 es estrictamente positivo. Esto prueba SINH-TP3.

También se necesita la versión confluente en lambda=u²:

    L(lambda,t)=sinh(sqrt(lambda)t)/sqrt(lambda)
                =sum_(m>=0)lambda^m t^(2m+1)/(2m+1)!,
    det[(partial_lambda)^i L(lambda,t_j)]_(i=0,1,2;j=1,2,3)>0
        para lambda>0, 0<t1<t2<t3.                (CONFLUENT-TP3)

La misma expansión Cauchy–Binet aplica. Los determinantes de las derivadas de lambda^(m_j) son sus Wronskianos: positivos para m1<m2<m3. Los otros determinantes son de las potencias t^(2m+1) y también positivos. El término m=0,1,2 garantiza la desigualdad estricta. Las series de derivadas convergen en compactos de lambda>0, lo que justifica el paso al límite.

## 5. Transferencia integral y bordes

Integrar por partes sobre TODA R, sin introducir un borde artificial en0, da

    LT(rho_1)=Z'(u),
    LT(rho_2)=u²Z'(u),
    LT(rho_3)=uZ(u).

Todos los términos de borde en infinito se anulan. Como las tres densidades son impares, sus transformadas se pliegan exactamente como

    (Z',u²Z',uZ)=2int_0^infinito sinh(ut)(rho_1,rho_2,rho_3)dt. (ODD-LT)

No se integra por partes en la semirrecta y no se pierde un valor en0. La suavidad y paridad reales hacen regulares allí todas las densidades; normalizarlas por tPhi en§3 sólo se hizo para t>0.

Andreief, que aquí es sólo expandir dos determinantes y aplicar Fubini, da para u1<u2<u3

    det[(Z'(u_i),u_i²Z'(u_i),u_iZ(u_i))]
      =8int_(0<t1<t2<t3)
          det[sinh(u_i t_j)]det[rho_l(t_j)]_(j,l=1)^3 dt1dt2dt3<0.

La integral es absolutamente convergente: para nodos u en un compacto, cada densidad y sus factores polinomiales son integrables contra exp(Ut), por las colas reales de Phi y sus derivadas. Cada término de la expansión de los determinantes queda dominado por un producto de tres de esas integrales. Los signos SINH-TP3 y DENSITY-SIGN son estrictos en toda la cámara, de medida positiva.

Dividir cada fila por Z'(u_i)>0 prueba det[1,u_i²,R(u_i²)]<0. Esto ya demuestra concavidad estricta de secantes en toda la semirrecta. Por sí sola, esa afirmación NO bastaría para asegurar R''<0 en cada punto; la siguiente sección justifica la versión puntual.

## 6. Curvatura puntual estricta por el kernel confluente

Definir las tres funciones de lambda>0

    (f_1,f_2,f_3)(lambda)
       =(Z'(u)/u,uZ'(u),Z(u))
       =2int_0^infinito L(lambda,t)(rho_1,rho_2,rho_3)dt.

Derivar hasta dos veces bajo la integral es legítimo por la misma dominación, uniformemente en compactos de lambda>0. Andreief aplicado a las tres filas de derivadas, CONFLUENT-TP3 y DENSITY-SIGN dan

    W(f_1,f_2,f_3)(lambda)<0.

Pero f_1>0 y exactamente

    (f_1,f_2,f_3)=f_1·(1,lambda,R(lambda)).

La regla de Wronskianos al multiplicar todas las funciones por la misma función da

    W(f_1,f_2,f_3)=f_1³ W(1,lambda,R)=f_1³R''.

Así R''(lambda)<0 para TODO lambda>0, demostrando GLOBAL-CURVATURE sin inferirlo indebidamente de la concavidad estricta de secantes.

## 7. Consecuencia y alcance

Con a=M'(0), g(lambda)=aR(lambda)−1 cumple g''<0 en TODA lambda>0. Junto a BASE073 y el criterio079, esto prueba matrices de tres nodos positivos distintos definidas positivas. Para exponentes originales ai=ui+1/2>1, se conserva exactamente la forma completa y su transferencia por congruencia; nodos repetidos sólo permiten afirmar PSD de la matriz de coeficientes, con energía estricta para la función representada no nula.

080 y las cotas exteriores078 permanecen válidos como pruebas independientes;086 aporta un mecanismo global distinto y no requiere sus certificados para la curvatura. Tampoco prueba que el mismo argumento controle las densidades superiores de083. Para órdenes mayores hay más funciones y Wronskianos; el signo de su determinante no se obtiene de este menor de tres filas. No hay conclusión de todos los órdenes, ni cierre global de W.
