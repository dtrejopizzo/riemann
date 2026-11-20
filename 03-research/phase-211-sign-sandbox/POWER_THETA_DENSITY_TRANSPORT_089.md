# POWER_THETA_DENSITY_TRANSPORT_089 — Del signo R4 al Turán global

Estado: **PROVED usando el certificado constructor089 FULL PASS auditado; reproducción independiente root87911 exit0/FULL PASS1024+8192 y hash coincidente.** Este archivo explicita el transporte, separado de las cotas computacionales de `POWER_THETA_DENSITY_COMPACT_089.md`. No nueva cobertura W; papers intactos.

## 1. Entradas y diferencia

Se usan073/077/086 y el signo Wt(1,A,B,C)<0 enTODOt>0 obtenido por BRIDGE/certificado089 en0<t<=1 y la prueba analítica088 ent>=1. La entrada nueva sobre086 es un cuarto Wronskiano global; no se hereda de los tres anteriores.087 sigue siendo una comprobación puntual independiente.

Las notaciones son A=p²−q−2p/t,B=p/t,C=(p³−3pq+r)/t, conPhi real y rho=(tPhi,(tPhi)'',−Phi',−Phi''')=tPhi(1,A,B,C).086 da k=B'>0 y J=(A'/B')'>0.

## 2. Los menores previos y el orden necesario

El sistema que se usa para Rolle es **[1,B,A,C]**. Sus Wronskianos iniciales son

    W1=1,
    W2=B'=k>0,
    W3=W(1,B,A)=k²J>0,
    W4=W(1,B,A,C)=−W(1,A,B,C)>0.

No se utiliza[1,A,B,C] como sistema inicial: A' no ha sido supuesto positivo. El intercambio de sus dos columnas centrales fija todos los signos.

Rolle ponderado demuestra que un sistema suave con estos Wronskianos iniciales estrictamente positivos es un sistema de Chebyshev extendido. Se divide primero por la función inicial no nula y se deriva; los Wronskianos del sistema reducido son cocientes de los anteriores por potencias positivas. Repetir reduce el número máximo de ceros. Una combinación no trivial de cuatro funciones tiene a lo sumo tres ceros; por tanto el determinante de evaluación no se anula para t1<...<t4. Su signo se fija por el límite confluente y W4>0. Volviendo al orden original y multiplicando filas por tiPhi(ti)>0,

    det[rho_j(t_i)]_(i,j=1)^4<0
    para TODO0<t1<t2<t3<t4.

Esto es un signo de TODOS los nodos de densidad, no sólo del jet confluente.

## 3. Transformación integral estricta

Sinh(ut) es estrictamente TP4 en nodos positivos: expandir su serie con coeficientes positivos y aplicar Cauchy–Binet produce determinantes de monomios positivos; el término de exponentes1,3,5,7 es estrictamente positivo. La positividad de determinantes generalizados de monomios se demuestra por Rolle ponderado y sus Wronskianos positivos.

Las transformadas bilaterales de rho son

    (Z',u²Z',uZ,u³Z).

Integrar por partes enTODA R elimina bordes por supercolas y evita un extremo artificial en0. Por imparidad, son2∫sinh(ut)rho(t)dt ensemirrecta. Andreief, expansión finita y Fubini absolutamente convergente, da

    det[Z'(ui),ui²Z'(ui),uiZ(ui),ui³Z(ui)]<0

para todos los nodos positivos distintos ordenados. El factor2⁴ es positivo; el4! de Andreief se cancela al restringir a la cámara ordenada. Las densidades pueden ser firmadas: cada término de la expansión está dominado por productos de integrales de |rhoj|exp(Ut), finitas por sus colas. No se supone que cada densidad sea positiva.

Dividir por Z'(ui)>0 da det[1,ui²,R(ui²),ui²R(ui²)]<0. Esto prueba signos de PfaffianosR4 en todos los nodos, pero para la desigualdad puntual estricta se necesita el siguiente paso confluente.

## 4. Turán puntual global

Conlambda=u² y L(lambda,t)=sinh(sqrt(lambda)t)/sqrt(lambda), el kernel de filas derivadas0,1,2,3 es estrictamente TP4. Cauchy–Binet aplicado a L=Σlambda^m t^(2m+1)/(2m+1)! tiene Wronskianos de monomios enlambda positivos y determinantes de monomios ent positivos; el término m0,1,2,3 fija la estrictitud.

Definir

    f=(Z'/u,uZ',Z,u²Z)
      =2∫L(lambda,t)rho(t)dt
      =f1(1,lambda,R(lambda),lambda R(lambda)), f1=Z'/u>0.

Las derivadas hastatres bajo la integral son legítimas en compactos delambda>0 por dominación exponencial uniforme. Andreief confluente y el signo global de densidades dan W(f)<0. La regla de Wronskianos por factor común da exactamente

    W(f)=f1⁴W(1,lambda,R,lambda R)
        =f1⁴[3(R'')²−2R'R''']
        =−f1⁴T_R.

Se concluye **T_R=2R'R'''−3(R'')²>0 para TODOlambda>0**. No se infiere una desigualdad puntual estricta de sólo determinantes distintos.

## 5. Consecuencia090 y límites

090 ya auditado se aplica ahora globalmente aR: R esC3hasta0 conR'0>0 por073/086. Da h=1/b estrictamente cóncava paraTODASx>0. Con086g_*=xb estrictamente cóncava y las fórmulas078, todos los pares distintos del resto regularizado Gp son PD para TODOp>0. El punto removible x=P se trata por los errores de tangente de segundo orden; no se presupone Gp creciente, por lo que081 no resulta contradicha.

Esto no demuestra la concavidad de ambos datos recíprocos del restoGp, sus desigualdadesTurán ni preservación por un segundo pasoSchur. No se transportaS4 aquí, ni cinco/todos los órdenes, ni nuevaW/T. Cuatro generadores siguen probados independientemente085. La reproducción independiente root87911 del certificado089 terminó exit0/FULL PASS1024+8192, con hash coincidente.
