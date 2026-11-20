# POWER_AUDIT_007 — Falsificador de transporte uniforme en dimensión alta

Estado: PROVED, revisión independiente de POWER_HIGH_ORDER_PM_NOGO_007.md. No refuta signo ni transporte de signo; no afecta el teorema local de cuatro polos. Papers intactos.

## 1. Cota de digamma comprobada

La serie positiva para tau m'(tau) es correcta, con t=|tau|/2 y a_k=k+1/4. Para t<=1, el término inicial se acota por 1/(2a0)=2. La cola se acota por 2sum_(k>=1)(k+1/4)^-3; el primer término más la integral desde1 es exactamente208/125. Así el total es <=458/125<4.

Para t>=1, la función f(a)=2at²/(a²+t²)^2 tiene integral1 y máximo3sqrt(3)/(8t)<1. La comparación unimodal de retícula por integral más dos máximos es válida: aparte hasta dos sitios cuyos paneles adyacentes tocan el máximo continuo; en la rama creciente asigne a cada sitio su panel derecho y en la decreciente su panel izquierdo. Los paneles restantes son disjuntos y la función en cada uno domina el valor asignado. Los sitios omitidos cuestan a lo sumo dos máximos. Así sum f(a_k)<=integral_0^infinito f+2max f<3. Queda demostrado globalmente 0<=tau m'(tau)<4. Se puede derivar la serie en compactos por convergencia uniforme de las derivadas; en tau0 la expresión se prolonga por0.

## 2. Polar y derivada exactos

La norma Gamma de y^(n-1)e^(-uy) y sus momentos producen exactamente

    P_n=4^n/[u binom(2n-2,n-1)]*(1-1/(4u²))^-n>=4/u.

La derivada logarítmica, calculada tanto desde esta fórmula como desde los momentos sin simplificar, es

    uP_n'=-(1+n/[2(u²-1/4)])P_n.

La escala de la probabilidad espectral es u^-1 veces una densidad fija de tau/u. La cota global de §1 proporciona dominación uniforme para diferenciar su promedio de m y prueba uA_n'<4 sin asumir asintóticos de Stirling ni cotas espectrales.

En u63/2, u²-1/4=992, n131072 y n/1984=2048/31. La pérdida polar inferior es exactamente

    (4/u)(1+n/[2(u²-1/4)])=(8/63)(2079/31)=264/31.

Por tanto uE_diag'<4-264/31=-140/31. Todas estas son comparaciones racionales exactas.

## 3. Movimiento individual y alcance

El cociente de la función racional 1/prod(s+u_j) es diferenciable y simétrico para u_j>1/2. Por regla de la cadena en la diagonal, E_diag'=sum partial_jE=n partial_1E. La derivada diagonal recién acotada es por tanto n veces cada movimiento individual; el signo negativo no procede de confundir dos parametrizaciones. En una pequeña dirección positiva individual todos los polos permanecen >=31.5 y el cociente ARCH+POLAR disminuye.

La clase falsificada es la monotonía de este cociente para todos los numeradores y todos los órdenes en el rango alto. No se demuestra energía negativa, no se incluyen contactos primos y no se refuta una regla de transporte que preserve sólo el signo. El caso n4 local positivo y el movimiento exclusivamente arquimediano quedan intactos.

Precisación adicional de alcance: el falsificador sólo disminuye el Rayleigh de un numerador fijo. No es un contraejemplo suministrado a la monotonía de lambda_min ni a otra eigenenergía comprimida de ARCH+POLAR. El mínimo del espacio puede permanecer no decreciente aunque disminuya uno de los cocientes particulares. Tampoco se hace esa inferencia en esta auditoría.
