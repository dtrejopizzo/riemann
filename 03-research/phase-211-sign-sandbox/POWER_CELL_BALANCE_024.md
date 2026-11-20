# POWER_CELL_BALANCE_024 — Presupuesto local de K negativo y celdas exteriores

Estado: **PROVED** desigualdad uniforme por celda que tolera K negativo; **PROVED** cola de celdas estrictamente positiva a todo N. La celda interior dirigida N129 está certificada separadamente en POWER_CELL_TEST_024.md. No se afirma signo de todas las celdas ni de W. Papers intactos.

## 1. Corpus y diferencia precisa

Leídos las reglas del proyecto, SIGNED_MEAN019 (PAIR), INVERSE_KERNEL020 (OUTER), CUMULATIVE_INVERSE022§§3,7 y CUMULATIVE_TEST023. Consultados índice (Euler/Möbius/sumación por intervalos), grid maestro y CROSSWORD-TO-D.md, con el estado023 que registra la refutación COMPLETA K129(1)<0.

La diferencia frente al criterio anterior es medir cuánto K NEGATIVO puede tolerar UNA celda, con un buffer explícito J(n) y una constante integrada exacta. No se vuelve a suponer positividad puntual universal ni se infiere el signo de una suma desde un prefijo. Las identidades auxiliares se usan para probar esa desigualdad unilateral y la localización de toda posible lesión a un número finito de celdas por N. La consecuencia exterior utiliza expresamente el teorema020 ya conocido, no se presenta como un nuevo mecanismo aritmético global.

## 2. Celda y notación

Conserve u=63/2, J_N(x)=int_x^infty h_N, K_N=J_N+xh_N=J_N−xJ_N'. Las sumas Möbius son COMPLETAS y su convergencia uniforme/absoluta está probada022. Para n>=2 defina

    S_N(n)=H_(n−1)int_(n−1)^n J_N(x)dx−logn J_N(n),
    b_n=H_(n−1)(1−1/(2n))−logn,
    a=3/4−log2>0.

Las pendientes−H_(n−1) y saltos logn del MISMO B dan

    sum_(n>=2)S_N(n)=−F_N/2.

Esta identidad por sí sola no prueba signo. El lema022 da b_n>=a para todos n>=2 y H_(n−1)/(2n)<=1/4.

## 3. Desigualdad unilateral que conserva K negativo

**Teorema.** Para todo N,n>=2, sin ninguna hipótesis sobre el signo de K o J,

    S_N(n)=b_n J_N(n)
       +(H_(n−1)/2)int_(n−1)^n [1−(n−1)²/t²]K_N(t)dt.       (LOCAL)

En particular, si M_N(n)=sup_(n−1<=t<=n)K_N^−(t),

    S_N(n)>=b_nJ_N(n)−[H_(n−1)/(2n)]M_N(n).                (BUFFER)

Prueba. La identidad diferencial exacta da, para n−1<=x<=n,

    J_N(x)=xJ_N(n)/n+x int_x^n K_N(t)/t²dt.

Integrar e intercambiar el triángulo FINITO (x,t) produce LOCAL. Descartar sólo la parte positiva de K da el bound, porque el peso es no negativo y

    int_(n−1)^n [1−(n−1)²/t²]dt=1/n.

No se pierde el salto logn ni se sustituye K por su módulo en una identidad de signo. QED.

**Criterio integrado suficiente.** Si J_N(n)>=0 y M_N(n)<=4a J_N(n), entonces S_N(n)>=0. En efecto BUFFER>=aJ_N(n)−M_N(n)/4. El criterio permite K<0 en la celda; es distinto de la hipótesis universal K>=0 refutada023. No se afirma que sus dos hipótesis estén probadas para toda celda real.

Una variante más fina conserva la integral de K^- en LOCAL en lugar de usar el supremo. BUFFER cuantifica un margen, pero no constituye por sí solo un bound aritmético de M_N(n).

## 4. Todas las celdas exteriores son favorables, para TODO N

Sea X_N=exp((N−1)/30). Por OUTER020, h_N(x)>=H_N(x)/4>0 para x>=X_N. Por tanto, en TODO n con n−1>=X_N,

    J_N(n)>=w_N(n)/4>0,
    J_N(x)>=J_N(n) para n−1<=x<=n.

En particular K_N>=0 allí por022, y LOCAL prueba la cota cuantitativa

    S_N(n)>=b_n J_N(n)>=a w_N(n)/4>0.                    (OUT-CELL)

De hecho la monotonía anterior da también el bound más fuerte (H_(n−1)−logn)w_N(n)/4; no se necesita para la conclusión. Así para cada N cualquier celda adversa posible está entre las FINITAS celdas cuyo extremo izquierdo es menor que X_N. Esto no prueba que exista una adversa ni que la suma total sea positiva; conserva una cola favorable explícita.

## 5. Prueba interior dirigida y coordinación

El único punto interior autorizado es la primera celda del MISMO N129 que refutó K>=0. Su certificado y cola Möbius completa pertenecen al otro constructor024; no se realiza aquí otro barrido ni se extrapola desde ese caso.

Para reproducir una integral sin cuadratura, escriba w_N=x^(−32)P_N(logx) y Q_N positivo resolviendo31Q_N−Q_N'=P_N:

    q_d=p_d/31,
    q_j=[p_j+(j+1)q_(j+1)]/31,
    T_N(x)=int_x^infty w_N(y)dy=x^(−31)Q_N(logx).

Entonces, con Möbius COMPLETO,

    int_1^2 J_N(x)dx
      =sum_(m>=1)mu(m)m^(−32)[Q_N(logm)−2^(−31)Q_N(log(2m))],
    J_N(2)=2^(−32)sum_(m>=1)mu(m)m^(−32)P_N(log(2m)).

Son identidades exactas con colas absolutas controlables por los mismos polinomios positivos e integrales gamma022. Aquí se incluyen como interfaz de cálculo, no como prueba de signo interior.

## 6. Qué falta para la forma completa

Incluso probar S_N(n)>=0 para TODAS las celdas sólo daría F_N<=0. La fórmula correcta es

    W[g_N]/C_N(0)=ARCH_sharp[g_N]/C_N(0)+2sum_(n>=2)S_N(n).

Si ARCH_sharp es negativo, falta el bound cuantitativo sum S_N(n)>=−ARCH_sharp/[2C_N(0)]. OUT-CELL no controla automáticamente las celdas interiores ni ese déficit. BUFFER puede permitir un certificado integrado que sobreviva a K129(1)<0, pero necesita estimar de verdad sus términos con el kernel aritmético real. No se declara que escribir LOCAL o sumar identidades Euler cumpla esa obligación.


## 7. Continuación aprobada025

POWER_INVERSE_LOGCONCAVITY_025.md prueba K129(x)>0 para TODOS x>=2 por logconcavidad específica de D129 y un corte racional. Por tanto todas las celdas n>=3 son favorables. Combinado con S129(2)>33/100 de CELL_TEST024, se obtiene ERR129<−33/50 COMPLETO. La comparación con ARCH_sharp sigue pendiente. Esta continuación no supone K>=0 en[1,2] y conserva el falsificador023. Auditoría independiente025 aprobada.
