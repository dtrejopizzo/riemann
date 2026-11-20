# POWER_PAIR_OBSERVABLE_SCOPE_100 — Observable real de la pareja J/K

Estado: **PROVED; lectura final y auditoría independiente aprobadas.** Véase `POWER_PAIR_OBSERVABLE_SCOPE_AUDIT_100.md`. Para la pareja REAL positiva J,K de078, el observable eta=−K'/J es positivo en la semirrecta, parte de0 y vuelve a0. No pertenece a la clase de observables crecientes que permitiría reutilizar directamente073. No se refutan el signo de T_h, la positividad de sus kernels, otras clases de pares ni la recursión general. Papers intactos.

## 1. Consulta y diferencia precisa

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; cotejados073–078,081,090 y097–099.078 ya construye las densidades positivas J,K.081 ya estudia F(u)=a/M(u)−1/u=uB(u), prueba F>0 y F→0 y excluye heredar la monotonía de G_p por un límite normalizado. Esos resultados no se presentan de nuevo como novedad.

El objeto aquí es PUNTUAL en la variable temporal: eta(t)=−K'(t)/J(t) para la misma pareja real. La desigualdad0<eta(t)<a/t descarta reconstruir la siguiente media mediante un observable creciente de esta pareja. No se registra otra prueba de la obstrucción081 ni un NO-GO de todos los métodos de pares de Laplace.

## 2. Definiciones y signos ya establecidos

Sea Phi la densidad par positiva real, Z su transformada bilateral y a=M'(0)>0. Usar las densidades PARES de078

    J(t)=int_|t|^infinito sPhi(s)ds>0,
    K(t)=int_|t|^infinito(s−|t|)[aPhi(s)−J(s)]ds>0.

Aquí K es la densidad par, no la primitiva impar de093/095. Se tienen

    K''=aPhi−J, K'(0)=0,
    Z_J=Z'/u, u²Z_K=aZ−Z_J,
    b(u²)=Z_K/Z_J, h=1/b.

Para completar el signo de K', poner q=aPhi−J.077/078 prueban que tau=J/Phi decrece estrictamente y que q tiene un cruce negativo/positivo. Además int_0^infinito q=0, pues int J=a int Phi. Por ello int_t^infinito q>0 para TODO t>0: después del cruce el integrando es positivo; antes del cruce la integral es−int_0^t q>0. Así

    −K'(t)=int_t^infinito q(s)ds>0, t>0.

Los bordes y las colas superexponenciales proceden de las mismas integrales de Phi y no introducen términos distribucionales en0.

## 3. Desigualdad puntual real y ausencia de monotonía

Definir

    eta(t)=−K'(t)/J(t).

Es una función impar suave porque K,J son pares suaves y J>0. En particular eta(0)=0 y eta(t)>0 para t>0. La fórmula de K' da

    −K'(t)=a int_t^infinito Phi(s)ds
                      −int_t^infinito J(s)ds
            <a int_t^infinito Phi(s)ds.

Por otra parte

    J(t)=int_t^infinito sPhi(s)ds
           >t int_t^infinito Phi(s)ds, t>0,

con desigualdad estricta porque Phi es positiva más allá de t. Dividir ambas desigualdades por J(t)>0 prueba

    0<eta(t)<a/t, TODOS t>0.                       (POINTWISE)

Así eta(t)→0 cuando t→infinito. No se usaron asintóticos, cotas derivadas de un resto real, truncaciones de la aritmética ni un nuevo certificado.

Una función positiva en(0,infinito) que vuelve a0 no puede ser no decreciente. Tampoco eta puede ser no creciente en[0,infinito), porque eta(0)=0 y eta(t)>0. Por tanto la observable REAL no es monótona en ninguno de los dos sentidos globales. Posee al menos un máximo interior, sin que esto pruebe un único máximo o unimodalidad.

## 4. Reconstrucción exacta de h y antecedente081

Para u>0, considerar la ley positiva inclinada de densidad J(t)exp(ut)/Z_J(u). Una integración por partes en toda la recta, con bordes nulos, da

    int_R exp(ut)eta(t)J(t)dt
       =int_R exp(ut)[−K'(t)]dt=uZ_K(u).

En consecuencia

    E_(J,u)[eta]=uZ_K/Z_J=u b(u²)=a/M(u)−1/u,
    h(u²)=u/E_(J,u)[eta].                          (PAIR-MEAN)

La función del lado derecho es exactamente F(u) de081, que ya era positiva y tendía a0. No se reivindica como nueva su falta de monotonía en el parámetro u. La ganancia acotada de esta fuente es identificar la observable temporal correspondiente y probar POINTWISE, que descarta imponerle monotonía creciente.

## 5. Alcance para una clase invariante

073 usa una media de la coordenada bajo una ley positiva y una comparación condicional de dos copias. PAIR-MEAN podría motivar repetir ese mecanismo con eta en lugar de la coordenada; hacerlo bajo la hipótesis de que eta fuese creciente sería incorrecto para los propios datos reales, por§3.

Esto no decide qué comparación de dos copias podría funcionar con eta no monótona, ni excluye una clase dual que permita ascenso y descenso. Tampoco se afirma que el bound a/t se preserve bajo nuevos pasos de Green o secantes. No se ofrece aquí una clase cerrada de todos los órdenes; ese objetivo permanece OPEN.

La positividad T_h global de099 y sus consecuencias, ya probadas y auditadas con reproducción independiente FULL PASS, son compatibles con esta obstrucción puntual. No se deduce de ella un contraejemplo W ni se retira ninguna cobertura de signo ya probada.
