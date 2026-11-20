# POWER_THETA_SCHUR_DENSITY_AUDIT_075

Estado: **APROBADO** POWER_THETA_SCHUR_DENSITY_075, tras lectura completa y la aclaración de Fubini en NEG-MASS. Prueba analítica, sin nuevos cómputos. Papers intactos.

Consultados los antecedentes de índice/grid/crucigrama, SCHUR003, THETA073 y el límite de alcance074. No se encontró la construcción literal de esta densidad en las búsquedas dirigidas. El algoritmo de Schur y su primer cociente son anteriores; el objeto nuevo es una representación POSITIVA del denominador regularizado para la MISMA Phi. La fuente no la identifica con una derivada logarítmica que no se haya probado.

## Primeros pesos y masa

073 da c=M(u)>0 y c<ua para todo u>0. V par implica V′(0)=0, y V‴>0 prueba que V′(x)/x es estrictamente creciente. Su promedio bajo x²Phi/(aZ0) es1/a por integración por partes; el límite en0 es estrictamente menor que ese promedio y, por tanto, menor queu/c. El límite infinito es infinito para la cola theta real. Esto proporciona exactamente un cruce de h_u en la semirrecta positiva, de negativo a positivo.

h_u es impar y de integral total0, así que su primitiva hacia infinito k_u es par y decae en ambas colas. En x>0, k′=−h hace que k crezca hasta el cruce deh y luego decrezca hacia0 desde valores positivos. Para NEG-MASS se aplica Fubini DESPUÉS de usar paridad:2integral_0∞ k=2integral_0∞ y h(y)dy, cuyo majorante absoluto es finito. No se intercambia el integral doble absoluto sobre todaR. La integración por partes resultante da Z0(c−ua)<0. Esto fuerza k(0)<0 y, por la monotonía descrita, exactamente un cruce negativo/positivo de k.

## Cancelación y densidad positiva

La transformada bilateral de h es D_u(z)=zcZ−uZ′. La identidad k′=−h da D_u=z Laplace(k), con bordes nulos. D_u(u)=0 implica la cancelación exacta de la masa firmada cosh(uy)k(y)dy en[0,∞).

El cociente w_x(y)=sinh(u(y−x))1_(y>=x)/cosh(uy) es continuo, no decreciente y tiene derivada u cosh(ux)/cosh²(uy)>0 para y>x. Restar su valor en el único cruce dek deja un integrando no negativo; es estrictamente positivo en una cola no vacía. Se preserva la cancelación antes de comparar pesos. El factor1/u es positivo y está correctamente incluido. Así Phi_u(x)>0 para todo x, incluido0.

## Ecuación y transformada

Dos derivaciones de la integral hacia infinito dan Phi_u″−u²Phi_u=k, con el signo positivo dek correcto. La primera derivada en0 es la negativa del integral cosh balanceado y por tanto se anula. La extensión par es suave: la ecuación con k par suave y el dato Neumann0 permite prolongar todas las derivadas sin salto ni masa delta.

Las colas theta de h y k son menores que cualquier exponencial; el kernel sinh preserva este hecho para cada u fijo, eligiendo un exponente mayor queu. Lo mismo vale para la primera derivada dePhi_u, suficiente para los bordes de la ecuación. Se obtiene exactamente

    H_u(z)=Laplace(Phi_u)(z)=D_u(z)/[z(z²−u²)].

Las singularidades0,±u son removibles por la identidad entera. En0 la masa es Z0(ua−c)/u²>0, sin factor2 perdido por el uso de semirrectas. La positividad dePhi_u y todos sus momentos justifican H_u>0 y(logH_u)″>0 sobre todo el eje real.

## Primer transformado y alcance

Verificada algebraicamente la identidad

    F1(z)=−cz/u+c² Z(z)/(u z H_u(z)).

El residuo en0 es u c²/(ua−c)>0; restarlo da exactamente la expresiónG_u de la fuente. Nada de lo probado convierte F1 en H_u′/H_u ni ordena automáticamente Z/H_u. No se preserva por supuesto la hipótesis V_u‴>0 ni se prueba un kernel Pick de orden dos paraF1.

La nueva densidad positiva es una restricción estructural real y específica del denominador regularizado. No contradice074, no demuestra tres generadores ni todos los órdenes y no añade una ventana temporal ni signo global deW. La comparación entrePhi yPhi_u que necesita el siguiente paso continúa explícitamente abierta.
