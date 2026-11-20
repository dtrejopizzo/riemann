# POWER_STATE_075 — Densidad positiva del denominador Schur

Estado: **PROVED/APROBADO**, fuente POWER_THETA_SCHUR_DENSITY_075.md y auditoría independiente POWER_THETA_SCHUR_DENSITY_AUDIT_075.md. Prueba analítica; sin nuevos parámetros numéricos ni matrices. Papers intactos.

## Resultado específico

`POWER_THETA_SCHUR_DENSITY_075.md`, `POWER_THETA_SCHUR_DENSITY_AUDIT_075.md` y `POWER_STATE_075.md`. Para la Phi REAL de073, Z(z)=∫Phi(x)e^(zx)dx, u>0,c=M(u),a=M'(0), el denominador D_u=zcZ−uZ' admite la representación positiva explícita H_u(z)=D_u(z)/[z(z²−u²)]=∫Phi_u(x)e^(zx)dx. Aquí h_u=−cPhi'−uxPhi, k_u(x)=∫_x∞h_u(y)dy y Phi_u(x)=u^−1∫_|x|∞sinh(u(y−|x|))k_u(y)dy>0. h_u y k_u tienen cada uno UN cruce negativo/positivo en la semirrecta; la cancelación exacta∫cosh(uy)k_u(y)dy=0 y un cociente creciente prueban el signo antes de tomar valores absolutos. La ecuación Phi_u''−u²Phi_u=k_u, sin delta en0, da la transformada entera y sus valores removibles.

Diferencia frente003/074: se construye una medida positiva para el denominador regularizado que quedaba pendiente, no sólo valores positivos reales del cociente Schur. H_u>0 y(logH_u)''>0 en la recta. Se conserva exactamente F1=−cz/u+c²Z/(uzH_u), con residuo R=uc²/(ua−c)>0 en0. No se identifica F1 con una derivada logarítmica ni se obtiene G=F1−R/z positivo: falta comparar Phi con Phi_u. Sin positividad de tres generadores, todos los órdenes o nueva ventanaT. Sin cómputos ni campañas; papers intactos y signo global OPEN.

## Obligación siguiente

Si R=uc²/(ua−c), el resto exacto es

    G_u(z)=c²/(uz)·[Z(z)/H_u(z)−Z(0)/H_u(0)]−cz/u.

La positividad de Phi_u no controla el cociente Z/H_u. Falta una comparación cuantitativa entre las DOS densidades que implique el bound mixto de Schur; no basta aplicar otra vez Cauchy a una forma cuya positividad no está probada. La hipótesis general de073 ya tiene un límite de orden tres registrado074.075 no elimina ese límite y sólo resuelve la construcción positiva declarada.

## Consulta076 — comparación de masas y criterio suficiente preciso

Casos, insight048, mapa y root revisaron las siguientes identidades. Definir J(x)=int_|x|^infinito y Phi(y)dy y tau(x)=J(x)/Phi(x). Para x>0, V'>0 y V'/x estrictamente creciente dan

    J(x)<[x/V'(x)] Phi(x),
    tau'(x)=V'(x)tau(x)−x<0.

La primera desigualdad integra y/V'(y)<x/V'(x) contra V'(y)Phi(y)dy. Esta comparación sí está probada, pero no implica la comparación necesaria con Phi_u.

Poner beta=u²a/(ua−c) y definir el defecto

    T_u(z)=Z(z)−[Z(0)/H_u(0)+z²/c]H_u(z).

Su densidad bilateral exacta, usando k_u=cPhi−uJ y la ecuación de075, es

    t_u(x)=Phi(x)−[Z(0)/H_u(0)]Phi_u(x)−Phi_u''(x)/c
          =(u/c)[J(x)−beta Phi_u(x)].

Las masas cumplen int_R J=aZ(0)=beta H_u(0); por tanto int_R t_u=0. Además G_u(z)=c²T_u(z)/(uzH_u(z)). Si la diferencia J−beta Phi_u tuviera exactamente un cruce negativo/positivo en x>0, su emparejamiento con cosh(zx) sería positivo para todo z>0 y se obtendría G_u(z)>0. Una condición suficiente más fuerte es que J/Phi_u sea estrictamente creciente, es decir,

    J'(x)Phi_u(x)−J(x)Phi_u'(x)>0, x>0.

No se ha demostrado ese Wronskiano para la Phi real. Tampoco G_u>0 por sí solo probaría el kernel de dos nodos del transformado: se distingue esta obligación de la positividad completa de orden tres.

La comparación más sencilla r=Phi_u/Phi tampoco quedó decidida. Su ecuación exacta es

    r''−2V'r'+[(V')²−V''−u²]r=c−u tau.

Aunque el lado derecho es creciente, eso no fija r' sin controlar los otros términos. No se convierte una sugerencia asintótica de cola en monotonía global.

El límite genérico074 sigue siendo pertinente incluso después de construir Phi_u: su potencial auxiliar también cumple las condiciones usadas075. En ese mismo auxiliar, u=A, delta=1/10000 y c=M(A), las identidades de integración por partes dan c<1 y Aa<=1;074 da c>1−delta, mientras073 da c<Aa. Así0<Aa−c<delta. Con m3=M(3A) en(2−delta,2+delta),

    F1(3A)<(5+4delta)/(1−4delta)<6,
    R/(3A)> (1−delta)²/(3delta)>3000,
    G_A(3A)<0.

Para c<1 se usa E[v'(X)]=1 y la positividad de la media del monomio impar bajo inclinación positiva; para Aa<=1, E[X V'(X)]=1>=A E[X²] en inclinación cero. No son nuevas evaluaciones numéricas. Es una aplicación del MISMO auxiliar074 que impide suponer el cruce como consecuencia genérica de073/075, no un fallo de la Phi real ni una dirección negativa de W. La consulta identifica la comparación específica pendiente; no amplía la cobertura de signo.
