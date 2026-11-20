# Estado035 — Filas escalares 1–17 completas a tasa fija

Estado: PROVED y auditado. Sustituye STATE034. Goal activo; signo global OPEN. Papers intactos.

## Positividad de la forma completa

Para F_(N,k,u)(s)=s^k/(s+u)^(N+k), a u=63/2, queda probado:

    W[f_(N,k,u)] > ||f_(N,k,u)||²/40,  1 <= N <= 17, k >= 0.

POWER_BOUNDARY_BALANCE_035 certifica un único terminal N17,k0: ARCH/norma² > −.868, polar/norma² > .911 y módulo del peine aritmético completo < .002. Por tanto el terminal tiene margen > .041. La recurrencia exacta normalizada

    A_N0 = A_N1/(2N) + (2N−1) A_(N+1),0/(2N)

conserva todas las partes de W. La columna k1 positiva de034 y este terminal permiten descender hasta N3; las filas1,2 ya estaban probadas. Todos k>=1 hasta N17 están cubiertos por034. La diferencia respecto de018 es disponer de ambos datos reales de signo; la recurrencia sola no basta.

Son átomos escalares individuales: no se certifican todas sus combinaciones lineales. Los certificados de espacios V12 fijo007 y ocho polos arbitrarios014 mantienen su alcance propio. No se certifica una nueva ventana T ni superar T=log(5)/2.

## Promedio firmado específico

POWER_SIGNED_TRANSFORM_035 prueba que A_N0 es un promedio de t_m=T_m/[m(m+1)/2] con una ley positiva explícita P_(N−1). Se obtienen su cola exacta, cotas uniformes y concentración en m de orden sqrt(N); la variable m(m−1)/(4(N−1)) converge en distribución a Gamma de forma2. La sustitución cuadrática del generador reconstruye exactamente los pesos.

Cualquier prefijo adverso fijo tiene costo acotado explícitamente por O(N^−2). Esto no controla los términos adversos en la ventana móvil ni sus magnitudes. La oscilación infinita034 permanece válida; no se vuelve a suponer positividad de cada T_m. El promedio aritmético firmado sigue OPEN.

## Auditoría y resto

POWER_BOUNDARY_AUDIT_035 aprueba ambas construcciones. Verificadores terminal racional y transformado simbólico: PASS independiente por constructor, root y auditor. Las pruebas uniformes son analíticas; no se hizo un barrido de casos.

A tasa fija queda pendiente desde N18 por debajo del cono k>=10000N², salvo el átomo N211,k1 ya decidido032. Se conservan las regiones de tasas variables029/034 y demás resultados previos. El objetivo global no está cerrado. La continuación036 aborda compensación en la ventana móvil, con consulta previa del corpus y diferencia explícita frente a criterios refutados.
