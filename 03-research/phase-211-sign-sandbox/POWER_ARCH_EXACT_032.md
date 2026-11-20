# POWER_ARCH_EXACT_032 — Fórmulas estables y resto certificado para ARCH2111

Estado: **PROVED**, revisión independiente aprobada en POWER_CONTACT_AUDIT_032.md y verificador PASS reproducido. Para el MISMO átomo N211,k1,u63/2 de021 se obtiene un intervalo racional normalizado de ARCH de anchura<10^(-18), sin cuadratura ni matrices. Papers intactos. El balance con peine/polar es un certificado separado del constructor paralelo; no se afirma aquí signo global.

## 1. Corpus y razón nueva

Leídos las reglas del proyecto, CONTACT_BALANCE021 (diagnóstico numérico del único átomo), ROW_PATTERN029 (GAIN), INTERIOR_SCALE030 y sus auditorías; módulo exacto003 y auditoría002 de las constantes Euler/Bernoulli. Consultados índice/grid/crucigrama sobre Poisson, coeficientes gamma, derivadas y Euler–Maclaurin. La recurrencia de Poisson y EM son herramientas previas, no se presentan como nuevas.

La diferencia precisa frente021 es sustituir la cuadratura diagnóstica de ARCH por una fórmula de sumandos de signo controlado y un resto integral explícito. No se recorre otro N, no se construye una matriz de orden211 y no se aumenta masivamente la precisión. El único corte de series es32, con16 sumandos directos por Hurwitz y8 términos Bernoulli. La fórmula simbólica sirve a todos N, pero sólo se certifica el átomo ya autorizado.

El valor negativo de la suma parcial021 hasta300 NO se atribuye a error de cuadratura: faltaba una cola favorable real. El intervalo de ARCH se construye para poder decidir el balance completo con más contactos, manteniendo esa contabilidad.

## 2. Serie positiva para ARCH de k0, válida a TODO N

Sea u>1/2, N>=2,d=N−1, x=(u+1/2)/2 y

    rho_N(t)=e^(−ut)sum_(j=0)^d p_jt^j,
    p0=1,
    (j+1)p_(j+1)/p_j=2u(d−j)/(2d−j).

La probabilidad es la autocorrelación gamma normalizada exacta. Ponga

    b_j=p_j j!/2^j,
    b0=1, b_(j+1)/b_j=u(d−j)/(2d−j),
    S_p(x)=sum_(l>=0)(x+l)^(-p), p>1,
    a(u)=psi(x)−logpi.

El integral temporal de psi tiene kernel

    k_gamma(t)=2e^(−t/2)/(1−e^(−2t))=2sum_(l>=0)e^(−(1/2+2l)t).

Comparar rho_N con rho_1=e^(−ut), cuya energía es a(u) por Poisson, da por Tonelli de sumandos positivos

    A_(N,0)(u):=ARCH_(N,0)/norm²
       =a(u)−sum_(j=1)^d b_j S_(j+1)(x).                (A0)

No hay coeficientes alternantes de derivadas de alto orden. Todos los términos restados son positivos y la expresión converge absolutamente. La fórmula también se interpreta para N1 con suma vacía.

## 3. Primera columna: fórmula aún estable sin restar dos órdenes grandes

La identidad exacta GAIN029 es A_(N,1)=A_(N,0)+uA_(N,0)'. Como b_j es proporcional a u^j, a'(u)=S2(x)/2 y dS_p/du=−pS_(p+1)/2, derivar la suma FINITA A0 produce

    A_(N,1)=a(u)+(u/2)S2(x)
       −sum_(j=1)^d (j+1)b_j [S_(j+1)(x)−(u/2)S_(j+2)(x)]. (A1)

Cada corchete tiene signo positivo, pues

    S_p(x)−(u/2)S_(p+1)(x)
      =sum_(l>=0)(x+l)^(-p)[1−u/(2(x+l))]>0,
    x=u/2+1/4>u/2.

Así A1 evita incluso restar2N A_(N,0)−(2N−1)A_(N+1,0). Puede haber la cancelación física final entre cantidades de orden1, pero no se resta una lista de enormes derivadas con signos alternos. No se infiere de A1 positividad de la forma.

## 4. Resto Euler–Maclaurin explícito, sin hipótesis de término siguiente

Para x16, p>=2 y M32, se encierra S_p(16) mediante

    Z_p=sum_(n=16)^(M−1)n^(-p)+M^(1−p)/(p−1)+(1/2)M^(-p)
       +sum_(r=1)^8 B_(2r)/(2r)! ·(p)_(2r−1) M^(-p−2r+1),
    |S_p(16)−Z_p|<=E_p,
    E_p=|B16|/(16)! ·(p)_15 M^(-p−15).                  (EM)

Aquí (p)_r es el factorial ascendente y B16=−3617/510. La cota NO depende de que los términos de la expansión decrezcan ni de un supuesto signo del resto.

En efecto el resto integral periódico tiene módulo <=(p)_16/(16)!·sup|B16({t})| int_M^infty t^(-p−16)dt. La serie de Fourier absolutamente convergente del Bernoulli periódico da sup|B16({t})|<=|B16(0)|; integrar reduce el mayorante exactamente a E_p. Esta es una cota integral absoluta válida para TODOS los p usados, incluido p212.

Los ocho Bernoulli son B2=1/6,B4=−1/30,B6=1/42,B8=−1/30,B10=5/66,B12=−691/2730,B14=7/6,B16=−3617/510, todos racionales.

## 5. Control de errores estable y API compartida

El verificador calcula S_p para2<=p<=212 por (EM), guardando los extremos como Fraction SIN redondeo prematuro. En A1 se multiplica cada corchete por su coeficiente racional b_j antes de convertir a los intervalos de003. Esto es esencial: redondear primero una potencia16^(-p) a una malla fija y luego multiplicarla por un b_j grande perdería su información.

La contribución total del resto Hurwitz está acotada por la suma racional positiva

    E_ARCH=(u/2)E2
       +sum_(j=1)^210 (j+1)b_j[E_(j+1)+(u/2)E_(j+2)]
       <(1/2)10^(-18).                                 (ERROR)

El script comprueba además el ancho del intervalo FINAL, incluidos gamma, logpi y los redondeos exteriores de003: es <10^(-18). Los corchetes tienen extremo inferior estrictamente positivo y también se verifica ese hecho racionalmente, sin tomar su signo de una aproximación.

Para u63/2, a(u)=H15−gamma−logpi. Las constantes heredadas003 usan intervalos explícitos de series y restos ya auditados; no se consulta un valor decimal de funciones especiales.

La API del módulo `tools/power_arch_exact_032_verify.py` exporta `ARCH`, intervalo de ARCH2111/norm². Una envolvente exterior simple de sus extremos es

    −1094177384741806137370/10^21
      <=ARCH2111/norm²
      <=−1094177384741806136520/10^21.                    (ARCH2111)

Esta envolvente impresa es algo más ancha que el intervalo interno, pero sigue muy por debajo del error10^(-16) solicitado para el balance de021. No se persigue una precisión mayor que la necesaria.

## 6. Alcance del certificado y combinación

El constructor paralelo suma los contactos del mismo átomo y el polar mediante aritmética exacta, usando el extremo inferior de ARCH. Los contactos omitidos son TODOS favorables por ARITHMETIC_DIFFERENCES019, porque N211,u31.5 están en su rango; esa cola no debe descartarse para una cota superior, pero sí puede omitirse en una cota inferior legítima.

ARCH2111 por sí solo no prueba W>=0, y su signo negativo era conocido. La mejora real es un error analítico certificado pequeño suficiente para decidir el balance concreto, conservando TODOS sus términos y sin culpar al diagnóstico parcial anterior de un signo global que nunca afirmó.

No se amplía por inferencia la familia de N ni una nueva ventanaT. Papers intactos.

Reproducción:

    python3 03-research/phase-211-sign-sandbox/tools/power_arch_exact_032_verify.py

Resultado PASS. El módulo puede importarse sin imprimir resultados y comparte directamente `ARCH` con el certificado de contactos del constructor paralelo.


## 7. Combinación final auditada

POWER_CONTACT_DECISION_032.md combina este intervalo ARCH con el polar exacto y los contactos hasta512, y controla la cola completa. El certificado independiente POWER_CONTACT_AUDIT_032.md aprueba

    3.4·10^(-15)<W[f_(211,1)]/norm²<4.5·10^(-15), u=63/2.

Es un único átomo real resuelto; no una fila ni el signo global. El diagnóstico021/032 era de sumas parciales distintas y no afirmaba W negativa.
