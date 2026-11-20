# POWER_STATE_074 — La hipótesis probabilística073 no se extiende automáticamente a tres

Estado: **PROVED/APROBADO** para el contraejemplo auxiliar; signo global OPEN. Papers intactos.

## Resultado y diferencia

Fuente [POWER_TWO_COPY_SCOPE_074.md](POWER_TWO_COPY_SCOPE_074.md), auditoría [POWER_TWO_COPY_SCOPE_AUDIT_074.md](POWER_TWO_COPY_SCOPE_AUDIT_074.md). Constructor, root y auditor reprodujeron el verificador racional con exit0/PASS.

El potencial explícito

    V(x)=A[x²/2+x^(2p)/(2p·2^(2p-2))],
    p=1000000, A=400000000,

es par, polinómico, fuertemente convexo, superlineal y satisface V'''(x)>0 para TODOS x>0. Por073, su media inclinada M cumple M''<0 y M-uM'>0; TODOS los pares distintos positivos del kernel K(u,v)=(M(u)+M(v))/(u+v) son definidos positivos.

Sin embargo, en los tres nodos A,2A,3A, el vector c=(40,-40,3) cumple

    c^T K c < -53111/(10000 A)<0.

La prueba controla modos y medias por convexidad fuerte e integración por partes, no por una aproximación de punto de silla sin error. Las medias quedan a menos de1/10000 de(1,2,2); la matriz racional límite da c^T B0 c=-6 y el error cuadrático es menor que6889/10000. No hay cuadratura, barrido de potenciales ni campaña de nodos.

La diferencia frente SCHUR003 es conservar EXACTAMENTE toda la hipótesis fuerte de potencial073. Los auxiliares anteriores no la verificaban. La investigación prescrita de V=x^6 dio un primer determinante coalescente positivo, demostrado con momentos gamma exactos; no se lo presentó como contraejemplo ni se buscó un signo por una campaña.

## Lo que permanece probado para el dato real

073 permanece íntegro: para el kernel theta REAL, el compacto del hazard está certificado, M''<0 y M-uM'>0 para TODO u>0, y la forma COMPLETA es positiva en TODOS los planos de dos potencias con exponentes a,b>1, incluidos polar y todos los contactos. Exponentes distintos dan matriz definida positiva; exponentes coincidentes dan semidefinitud por redundancia y energía positiva sólo para la función representada no nula.

074 no es un contraejemplo a Phi real ni a W. No añade ni retira una región de signo W, ni una ventana T. Para avanzar a tres generadores reales hace falta una propiedad específica adicional de Phi o una comparación cuantitativa de su cruce.

## Obligación local cuantitativa, NO estimación probada

Para el M REAL de073 y un u>0, ponga

    r=uM'(u)/M(u), t=-u²M''(u)/M(u).

073 proporciona0<r<1 y t>0. El primer jet de tres nodos coalescentes exigiría además

    t <= (1-r)(1+2r).                                  (OPEN-JET)

Es la condición local ya asociada al primer transformado de SCHUR003§4, escrita con estas variables. Para precisar el alcance, la matriz de coeficientes Taylor de K alrededor de(u,u), con índices0,1,2 y división por los factoriales respectivos, tiene determinante

    M(u)^3/(64u^9) ·(1-r+t)·[(1-r)(1+2r)-t].

Como1-r+t>0, un determinante local no negativo requiere OPEN-JET. Esta fórmula es una identificación algebraica de la obligación, no una prueba de su signo para Phi. La concavidad de M sólo conoce el signo de la covarianza de dos copias; falta controlar su MAGNITUD. Tampoco probar este jet puntual sustituiría la comparación global entre tres nodos distintos. No se crea otro memo de identidades ni se declara resuelta esa obligación.
