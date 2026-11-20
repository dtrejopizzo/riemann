# POWER_REAL_PAIR_LIMIT_ORIGIN_DESIGN_103 — Diseño único puntual de U_lim(0)

Estado: **DISEÑO FIJO auditado y ejecutado; resultado NEGATIVO con reproducción independiente aprobada.** Véase `POWER_REAL_PAIR_DOUBLE_LIMIT_AUDIT_103.md` y la sección7 al final de esta fuente. Los parámetros siguientes fueron fijados antes de datos y no cambiaron. Papers intactos.

## 1. Objeto, antecedente y test exacto

La consulta de las reglas del proyecto y de los tres índices, y la diferencia respecto de102, constan en POWER_REAL_PAIR_DOUBLE_LIMIT_103.md. Se estudia exclusivamente el valor puntual de U_lim(0) para la pareja REAL límite (J,K); no una familia de órdenes, parámetros o ventanas. La prueba analítica103 justifica la inferencia desde un signo positivo a un fallo del cruce negativo/positivo para p,q FINITOS.

Se integrarán sólo los siete momentos completos

    I_r=int_0^infinito t^r Phi(t)dt, r=0,...,6.

Usar las definiciones exactas

    a=I2/I0, K0=aI1-I3/2, Kmass=aI2/2-I4/6,
    b0=Kmass/I2,
    H0=(b0/2-a/6)I3+I5/24,
    Hmass=(b0/6-a/24)I4+I6/120.

103 prueba I0,I2,Kmass,Hmass>0. El único test principal será el polinomio que limpia todos los denominadores:

    P=720 I0^2 (K0 Hmass-Kmass H0)
     =-3 I0^2 I3 I6+5 I0^2 I4 I5
       +6 I0 I1 I2 I6-20 I0 I1 I4^2
       -15 I0 I2^2 I5+25 I0 I2 I3 I4
       +30 I1 I2^2 I4-30 I2^3 I3.                 (TEST)

La igualdad es algebraica exacta, y sign(P)=sign(U_lim(0)). P es homogéneo de grado4 en los momentos. El assert debe aceptar P>0 O P<0, sin predeterminar cuál. Si el intervalo contiene0, el resultado será INCONCLUSO con estos parámetros, sin ajustar precisión, grado, paneles o modos durante la corrida. Los cocientes anteriores pueden imprimirse sólo como lecturas auxiliares tras comprobar denominadores positivos; no reemplazan TEST.

## 2. Parámetros fijados antes de datos

Se reutiliza la geometría de093/098:

    intervalo compacto [0,2], 128 paneles,
    centros exactos (2j+1)/128, j=0,...,127,
    semiancho h=1/128, radio Cauchy R=1/32,
    razón h/R=1/4,
    aritmética Arb 512 bits, Taylor grado64, cap65,
    modos theta m=1,...,16.

Se deben fijar explícitamente ctx.prec=512 y ctx.cap=65. Comprobar que los coeficientes Phi[0],...,Phi[64] son finitos en cada centro y que el jet tiene precisión suficiente. No se importa ni ejecuta una malla de otro certificado. No se hará búsqueda de parámetros.

## 3. Cota holomorfa y cola completa de modos

Los discos declarados están contenidos en

    -1/32<=Re t<=65/32, |Im t|<=1/32, |t|<3.

La cota completa093 da |Phi(t)|<2^22 allí; procede de la serie theta completa y no de muestras. Por tanto, para r=0,...,6,

    |t^r Phi(t)|<3^6*2^22<10^12=B.

La cola completa de modos m>=17 se acota por la misma cantidad fija093/098

    EPS=2^25*17^4/8^289.

En cada centro se agregan errores simétricos outward EPS*32^k a TODOS los coeficientes Phi[k], k=0,...,64, ANTES de multiplicar el jet por t^r. Así se conserva la cola de modos antes de formar cada momento. No se truncan derivadas reales de un resto ni se omite el prefactor de Phi.

## 4. Integración exacta de Taylor y resto completo

Para cada r y panel, multiplicar el jet Phi por el polinomio exacto t^r. Integrar el polinomio de Taylor hasta grado64 en el panel simétrico: sólo contribuyen k pares, con factor exacto 2 h^(k+1)/(k+1). Arb controla todos los redondeos hacia afuera.

El bound B controla la serie entera de cada t^rPhi en el disco. El error de Taylor de cada punto del panel es a lo sumo B*(1/4)^65/(1-1/4). La longitud total de los paneles es2. Por tanto a CADA momento compacto se añade simétricamente

    REM=2*10^12*4^(-65)/(1-1/4)<10^(-24).

Este coste paga todos los términos omitidos, no sólo el siguiente coeficiente. Se conservará su expresión racional exacta en el verificador, sin sustituirla por la cota decimal.

## 5. Cola temporal completa

Para t>=2, las fuentes093/098 dan el bound de toda la serie theta

    Phi(t)<64 exp[9t/2-3exp(2t)].

La comprobación racional exp4>54 fija Phi(2)<2^(-140), y la derivada logarítmica del mayorante es menor que -300. Así para s>=0,

    Phi(2+s)<2^(-140)exp(-300s).

Para todos r<=6 puede usarse el bound ya válido hasta10:

    (2+s)^r<=1024 exp(5s).

Por consiguiente

    0<int_2^infinito t^r Phi(t)dt
       <[1024/295]2^(-140)<2^(-138).

A cada momento se añade el intervalo POSITIVO [0,2^(-138)]. No se integra sólo una densidad truncada ni se reemplaza esta cola por un cero.

## 6. Condiciones de ejecución, lectura y auditoría

Antes de ejecutar, debe auditarse el literal del script y la prueba de los dos límites103. Después de integrar, comprobar I0,...,I6 estrictamente positivos, y evaluar TEST mediante operaciones intervalares outward. Las cantidades Kmass y Hmass deben tener encierros estrictamente positivos si se imprimen los cocientes; su positividad analítica ya está probada103.

Resultados permitidos:

- **P>0:** U_lim(0)>0, que por103 refuta el único cruce negativo/positivo de U para algunos p,q FINITOS de la pareja REAL. No implica W negativo.
- **P<0:** sólo verifica el signo puntual del origen en este límite; no prueba cruce global, conservación bajo Schur ni todos los órdenes.
- **P contiene0:** INCONCLUSO, sin cambiar el diseño durante la corrida.

No se usarán estos siete momentos para lanzar tests adicionales no diseñados. No se hará campaña y no se modificará ningún paper. El resultado y su auditoría se registrarán sólo después de la ejecución autorizada y su reproducción independiente.

## 7. Resultado final del único test diseñado

La prueba analítica, este diseño y el literal fueron auditados ANTES de la corrida. El constructor68812 terminó exit0/FULL PASS128 paneles; root91737 reprodujo independientemente exit0/FULL PASS128 y el mismo hash:

    P=[-3.1683047444094325e-13 +/- 2.16e-30],
    U_lim(0)=[-1.35855717857699839e-6 +/- 8.09e-24],
    hash=5090a71fd7dd4ae786a3f785ca8a4c32d6691cf92af912d4e5fffff9e583d080.

El encierro principal separa0 por el lado NEGATIVO. Sólo queda probado el signo del origen en el límite y, por la convergencia secuencial103, ese mismo signo para q suficientemente pequeño fijo y después p suficientemente grande. No se ha dado un umbral cuantitativo, no se ha probado el cruce global y no se ha obtenido un falsificador. No se ejecutaron otros tests ni se ajustaron los parámetros tras observar el resultado. Las consecuencias globales y la conservación bajo Schur permanecen OPEN.

Nota cronológica posterior: después de este test se obtuvo una prueba analítica global para U_lim, mediante (H/K)'<0; véase la sección9 de POWER_REAL_PAIR_DOUBLE_LIMIT_103.md. Esa prueba vuelve redundante el test para el signo de U_lim(0), pero no cambia su diseño ni resultado. Tampoco transfiere por sí sola el cruce global a los U de parámetros finitos.

Una ampliación analítica posterior, sección10 de la misma fuente, prueba también el cruce global de U_*(q) y Xi_q>0 para TODOS q>0 de la pareja límite (J,K), sin nuevos tests. Se mantiene p->infinito; el caso general de p finito no se deduce de esa ampliación.
