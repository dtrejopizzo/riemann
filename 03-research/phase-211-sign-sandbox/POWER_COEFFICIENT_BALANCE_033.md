# POWER_COEFFICIENT_BALANCE_033 — Mezcla finita gamma, prefijo Erlang adverso y Abel ponderado

Estado: **PROVED**, revisión independiente aprobada en POWER_BALANCE_AUDIT_033.md y verificador PASS reproducido: mezcla finita y coeficientes Abel no negativos; **PROVED** funcional Erlang22 completo negativo. **FALSIFIED en034** la premisa de signo no negativo de TODOS los prefijos ponderados T_m (véase seguimiento al final). No se afirma nueva región W ni cierre. Papers intactos.

## 1. Corpus y razón nueva

Leídos las reglas del proyecto, ARCH_EXACT032, ROW_PATTERN029 y GAIN, INTERIOR_CONSTRAINT027 (mezcla gamma–Gaussian), GAMMA_BALANCE030 y sus auditorías; consultados ROUTES-TRIED-INDEX, grid maestro y CROSSWORD-TO-D.md sobre Euler/Möbius, sumas parciales de coeficientes, medias Riesz y mezclas. Búsquedas dirigidas Erlang/supervivencia/exponencial truncada no dieron una construcción POWER previa del objeto finito usado aquí.

La diferencia respecto a la mezcla Gaussian027 es que la representación es FINITA en perfiles de supervivencia Erlang y sus pesos proceden directamente de los coeficientes gamma decrecientes. No depende de convexidad de la forma completa, refutada para la mezcla Gaussian030. La sumación de Abel y los perfiles Erlang son clásicos; la nueva información acotada es qué desigualdad concreta de componentes falla en el dato aritmético y qué prefijos ponderados sí serían compatibles con los pesos reales.

Sólo se estudia el corte22, motivado por ulog2≈22 y el primer contacto aritmético. No se lanza una secuencia de nuevos cortes ni otra campaña por N. El criterio Abel se declara suficiente y OPEN; no se lo llama avance de signo por ser una identidad.

## 2. Funcional lineal de autocorrelación y mezcla finita EXACTA

Fije u=63/2. Para una función par real rho con rho(0)=1 y los decaimientos aquí presentes, defina la extensión lineal del funcional explícito por

    L[rho]=m0+int_0^infty k_gamma(t)[1−rho(t)]dt
             −2sum_(q>=2)Lambda(q)q^(−1/2)rho(logq)
             +4int_0^infty cosh(t/2)rho(t)dt,
    k_gamma(t)=2e^(−t/2)/(1−e^(−2t)), m0=psi(1/4)−logpi.

Se entiende la extensión homogénea usando m0rho(0) y rho(0)−rho(t) cuando rho no está normalizada. Para la autocorrelación gamma REAL rho_N, L[rho_N]=W[g_N]/norm². Una rho positiva como función temporal NO tiene por qué ser una autocorrelación admisible.

Con d=N−1, escriba

    rho_N(t)=e^(−ut)sum_(j=0)^d p_jt^j,
    a_Nj=p_j j!/u^j,
    a_N0=a_N1=1,
    a_N,j+1/a_Nj=2(d−j)/(2d−j),
    a_N,d+1=0.

Por tanto a_Nj decrece y los pesos

    w_Nj=a_Nj−a_N,j+1=a_Nj·j/(2d−j)>=0, j0..d,
    sum_(j=0)^d w_Nj=1

son exactos. Para S_j(t)=e^(−ut)sum_(r=0)^j (ut)^r/r!, intercambiar dos sumas FINITAS da

    rho_N=sum_(j=0)^d w_Nj S_j,
    W[g_N]/norm²=sum_(j=1)^d w_Nj E_j,
    E_j=L[S_j].                                          (MIX)

El término j0 pesa0. MIX conserva TODOS los contactos y el polar; no se supone positividad de los E_j ni positividad definida de cada S_j.

## 3. Coeficientes antes de acotar y el único corte22

ARCH_EXACT032, aplicado a los coeficientes u^r/r!, da EXACTAMENTE

    ARCH[S_J]=a(u)−sum_(r=1)^J (u/2)^r S_(r+1)(16),
    a(u)=psi(16)−logpi.

Aquí S_p(16) denota la suma Hurwitz, distinta del perfil temporal S_j; se mantiene el índice p para distinguirlos. La contribución polar lineal es

    POLAR[S_J]=2sum_(r=0)^J u^r[(u−1/2)^(−r−1)+(u+1/2)^(−r−1)],

mientras el peine completo es

    PRIME[S_J]=−2sum_(q>=2)Lambda(q)q^(−32)
                         sum_(r=0)^J (ulogq)^r/r!.

Todas estas series son absolutas. Cada contacto no nulo del peine es NEGATIVO porque S_J(t)>0. Los signos se conservan antes de estimar.

Para J22 el certificado racional prueba

    −1/100<E_22<−3/500.                                  (ERLANG-FAIL)

El upper usa el intervalo ARCH de032, el polar racional exacto y sólo los contactos2,3, cuyos valores reales son Lambda=log2,log3. TODOS los contactos restantes son adversos y omitirlos es legítimo sólo para ese upper.

Para el lower se acota la cola COMPLETA q>=4 usando Lambda(q)<=logq. Cada x^(−32)(logx)^ell,1<=ell<=23, decrece para x>=4. Así su suma se acota por el extremo4 más la integral desde4, calculada con

    I0=4^(−31)/31,
    I_ell=4^(−31)(log4)^ell/31+(ell/31)I_(ell−1).

La suma positiva de esos mayores con2u^r/r! prueba el lower de ERLANG-FAIL. No se toma el signo de un prefijo aritmético por el de la cola.

## 4. Por qué NO es un contraejemplo a W real

El perfil S22 NO es positivo definido. Para xi=tau/u>0, su transformada par es

    Fourier(S_J)(tau)=[2/(u xi)] Im(1−i xi)^(−J−1).

En J22,xi1, el cálculo racional complejo da Im((1+i)/2)^23=−1/4096, luego

    Fourier(S22)(u)=−1/(2048u)<0.

Así ERLANG-FAIL refuta sólo la premisa «cada componente de la mezcla Erlang aporta un funcional no negativo». No es una dirección admisible con W<0 y no refuta MIX ni el signo de la función gamma real.

Hay además una cota uniforme sobre el daño de ESTE componente a la mezcla real: para todo N>=23,d=N−1,

    w_N,22<=22/d,
    −11/(50d)<w_N,22 E_22<0.                              (WEIGHT)

Se usó a_N,22<=1 y2d−22>=d. Esta pérdida particular es O(1/N); WEIGHT no controla la suma de TODOS los componentes adversos, que no se identifican mediante una campaña. Tampoco dice que el resto la compense automáticamente.

## 5. Agrupación ponderada que sí respeta los pesos gamma

La condición más fuerte E_j>=0 falla. Una condición SUFICIENTE distinta conserva componentes negativos dentro de prefijos ponderados:

    T_m=sum_(j=1)^m j E_j.

Defina v_Nj=w_Nj/j=a_Nj/(2d−j),j>=1 y v_N,d+1=0. Para1<=j<d,

    v_N,j+1/v_Nj=2(d−j)/(2d−j−1)<=1.

La diferencia entre denominador y numerador es j−1>=0; en d>=2 la primera diferencia v_N1−v_N2 es exactamente0. En d1 hay sólo un coeficiente positivo y el resultado es inmediato. Sumación de Abel FINITA da exactamente

    W[g_N]/norm²
      =sum_(m=1)^d [v_Nm−v_N,m+1]T_m,                   (ABEL)
    v_Nm−v_N,m+1>=0.

Por tanto probar T_m>=0 para TODOS m implicaría el signo de TODA la fila k0 gamma. Es un criterio SUFICIENTE para esa fila, NO para todos k ni para el Paper47 completo. ERLANG-FAIL no lo refuta: jE_j puede ser negativo y quedar compensado en T_m.

El perfil de T_m antes de aplicar L es explícito:

    sum_(j=1)^m j S_j(t)
      =e^(−ut)sum_(r=0)^m [m(m+1)−r(r−1)](ut)^r/(2r!).

También, en un entorno convergente de z0, con v=u(1−z) y E0(v)=L[e^(−vt)]=2L_power(v+1/2) en la notación CONE001,

    sum_(m>=1)T_m z^m
       =z[E0(v)−vE0'(v)]/(1−z)^3.

La positividad real exterior de E0(v)−vE0'(v) de CONE001 NO prueba la positividad de todos los coeficientes de esta función. No se registra tal inferencia. Estas fórmulas describen la obligación aritmética de T_m, no la resuelven.

## 6. Alcance y siguiente desigualdad faltante

Queda **OPEN** si TODOS los T_m son no negativos para la Lambda real. No se ha obtenido aquí una desigualdad elemental uniforme que pruebe ese signo; la identidad de generación no se vende como tal. Tampoco se han añadido nuevos diagnósticos en una secuencia de m.

Los resultados firmes son MIX con pesos gamma explícitos, ERLANG-FAIL con el peine completo, la pérdida uniforme individual WEIGHT y ABEL como implicación correctamente limitada. La continuación constructiva debe controlar las compensaciones de T_m con la aritmética real o encontrar un criterio integrado más preciso que conserve el peso gamma, sin volver a suponer positividad de cada componente ya refutada.

Verificador exacto: tools/power_coefficient_balance_033_verify.py, Fraction/intervalos racionales y resto EM032; PASS. Un único corte22, dos contactos explícitos y una cola completa analítica. No nueva región W ni ventanaT. Papers intactos.


## Seguimiento034

POWER_WEIGHTED_COEFFICIENT_034, revisado en POWER_COMPARISON_AUDIT_034, demuestra infinitos términos positivos y negativos en T_m. La premisa suficiente que esta nota dejó abierta queda refutada, incluso salvo finitas excepciones. MIX y ABEL siguen siendo identidades válidas; el signo de sus combinaciones gamma no queda decidido por esta oscilación. No relanzar positividad de todos T_m como lema sin cambiar la agrupación o introducir una compensación real.
