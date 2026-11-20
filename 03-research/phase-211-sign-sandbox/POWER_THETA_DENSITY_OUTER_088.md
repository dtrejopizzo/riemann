# POWER_THETA_DENSITY_OUTER_088 — Signo exterior del Wronskiano de cuatro densidades

Estado: **PROVED, certificado polinómico/racional exit0/PASS, auditoría independiente y reproducciones aprobadas.** Véase `POWER_THETA_DENSITY_OUTER_AUDIT_088.md`. Sólo t>=1 para las densidades R4 de la Phi real. No se infiere el transporte global, una nueva región W o todos los órdenes. Papers intactos; sin mallas ni evaluaciones theta numéricas.

## 1. Antecedentes y objeto específico

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; releídos077,083–087.086 controla las tres densidades R3 mediante N>0 de077;087 decide el signo necesario del Wronskiano R4 en el origen, sin intervalo global. No se hereda el cuarto signo desde el tercero.

Con Phi real y V=−logPhi, definir para t>0

    p=V',q=V'',r=V''',s=V'''',v5=V^(5),v6=V^(6),
    A=p²−q−2p/t, B=p/t, C=(p³−3pq+r)/t,
    W4(t)=W_t(1,A,B,C), G(t)=t⁴W4(t).

El resultado es la cota cuantitativa uniforme

    G(t)<−4000 t² y⁶,
    W4(t)<−4000 y⁶/t²<0,
    TODOS t>=1, y=pi exp(2t).                       (OUTER)

Se conservan TODOS los modos theta. La nueva diferencia respecto del outer077 es un Wronskiano que contiene derivadas hasta orden6; sus signos no están incluidos en C,N077, que sólo alcanzan orden4.

## 2. Primer modo y un polinomio exacto

Para el primer modo poner b=2y−3 y g0=exp(5t/2−y), de modo que Phi1=pi b g0. Usar D=partial_t+2y partial_y sobre polinomios en t,y. Definir

    B0=2y−3,
    B_(j+1)=D B_j+(5/2−2y)B_j, j=0,1,2.

Entonces Phi1^(j)=pi g0 B_j y

    F=(tB0, tB2+2B1, −B1, −B3).

Al retirar el factor común pi g0 del Wronskiano de las cuatro densidades, se obtiene exactamente

    W4,0=det[D^iF_j]_(i,j=0)^3/(t b)^4.

El determinante del numerador es

    det[D^iF_j]=−16 y² P(t,y),                       (MODE-POLY)

donde P es un polinomio racional. El verificador lo genera mediante las recurrencias y el determinante, sin un dato flotante.

Se comprueba la desigualdad polinómica sobre el cuadrante MÁS GRANDE

    P(t,y)>4096 t² y⁸, TODOS t>=1,y>=21.             (MODE-MARGIN)

Prueba finita: sustituir t=1+T,y=21+Y en P−4096t²y⁸. Sus27coeficientes no nulos, incluido el constante, son ESTRICTAMENTE positivos. Por tanto el polinomio es positivo para T,Y>=0. No se requiere la relación entre t e y para este paso.

Como b<2y, MODE-POLY y MODE-MARGIN dan

    G0=t⁴W4,0<−65536 t²y^10/b⁴<−4096t²y⁶.          (MODE-BOUND)

Para el dato real t>=1, pi>3 y exp2>7 dan y>21; exp2>7 se prueba con la suma Taylor positiva hasta grado5.

## 3. Cola theta completa hasta el sexto orden

Escribir Phi=Phi1(1+Rtheta), Rtheta=Σ_(m>=2)r_m>0. Como en077/10343, con a=m²−1>=3 y z=ay,

    0<r_m<=(32/9)a²exp(−ay).

Poner h=3/(2y)<=1/14. El cociente tiene logaritmo

    log r_m=constante−ay+log(1−h/m²)−log(1−h).

Las contribuciones de logy se cancelan ANTES de derivar. Para1<=j<=6,

    |D^jlog r_m|
      <=2^j[z+Σ_(n>=1)n^(j−1)h^n]
      <=2^j[z+1]<2^(j+1)z.                         (LOG-TAIL)

La cota de la suma se obtiene de la identidad racional

    Σ_(n>=1)n⁵h^n
      =h(1+26h+66h²+26h³+h⁴)/(1−h)^6<1 en h<=1/14.

Los órdenes inferiores quedan dominados por n⁵ para n>=1. La fórmula de Bell para derivar exp(log r_m), con los bounds2^(j+1)z, da en orden6

    |D^6r_m|/r_m
      <=4096z⁶+30720z⁵+66560z⁴+46080z³+7936z²+128z
      <5000z⁶, z>=63.

El mismo majorante sirve para los órdenes0,...,5: los polinomios completos de Bell con argumentos positivos aquí crecen en el orden, porque el primer argumento4z es>=1. Por tanto

    |D^jRtheta|
      <=(160000/9)y⁶ Σ_(a>=3)a⁸exp(−ay), 0<=j<=6.

Se amplió la suma de a=m²−1 a TODOS los enteros a>=3; sólo se añadieron términos positivos. La suma Taylor racional de exp3 hasta grado11 prueba exp3>20. Para y>=21, la razón consecutiva de a⁸exp(−ay) es<=(4/3)^8/20^7<1/2. Además y⁶exp(−3y) decrece para y>=21. Así

    |D^jRtheta|<E, j=0,...,6,
    E=(320000/9)3⁸21⁶/20^21
      =62523502209/6553600000000000000000.            (TAIL)

Es una cota de la cola COMPLETA para cada derivada pertinente.

## 4. Error de las seis derivadas del potencial

Rtheta>=0 asegura denominadores1+Rtheta>=1. Las fórmulas de derivadas logarítmicas y TAIL dan, simultáneamente para1<=j<=6,

    |D^jlog(1+Rtheta)|
      <=E+31E²+180E³+390E⁴+360E⁵+120E⁶<2E=:eta.     (LOG-ERROR)

Los coeficientes son(k−1)!S(6,k); los órdenes inferiores están dominados por la misma suma. No se usa un signo del error, sólo su módulo.

Para el primer modo, V0=y−(5/2)t−log(2y−3)−logpi. En orden1,0<V0'<2y. Para los órdenes2,...,6, la expansión de log(1−h) ya usada da

    |V0^(j)|<=2^j(y+1)<68y.

Con eta<1 y y>=21, todos los segmentos entre los jets exactos y los del primer modo quedan dentro de la caja

    |p|,|q|,|r|,|s|,|v5|,|v6|<=128y.                (BOX)

No se supone que los modos posteriores sean despreciables en derivadas altas: LOG-TAIL y Bell pagan precisamente esos factores.

## 5. Propagación al polinomio genérico del Wronskiano

El mismo algoritmo de derivación formal, ahora con p'=q,q'=r,r'=s,s'=v5,v5'=v6, demuestra que

    G=t⁴W_t(1,A,B,C)

es un polinomio de55monomios en t,p,q,r,s,v5,v6. Cada exponente de t está entre0 y2 y cada grado total en los seis jets está entre3 y6. No aparece una derivada de v6: el verificador lo exige al aplicar la derivación.

Las sumas de coeficientes absolutos ponderados por el grado de jets, agrupadas por ese grado, son

    grado6:888, grado5:1580, grado4:644, grado3:66.

Por BOX, para t>=1,y>=21, la suma de módulos de las seis derivadas parciales del polinomio es<=K t²y⁵, donde

    K=888·128⁵+1580·128⁴+644·128³+66·128²
      =30936927338496.

El teorema del valor medio multivariable y LOG-ERROR prueban

    |G−G0|<=eta K t²y⁵.

La comparación racional exacta del verificador es

    eta K=59029694970340794273/100000000000000000
          <96·21<=96y.

Con MODE-BOUND,

    G<−4096t²y⁶+96t²y⁶=−4000t²y⁶,

que demuestra OUTER para TODO t>=1, no una colección de puntos.

## 6. Verificador finito y salida

Ejecutar

    python3 03-research/phase-211-sign-sandbox/tools/power_theta_density_outer_088_verify.py

El programa usa únicamente enteros, Fraction y operaciones exactas de polinomios; no necesita Sympy, FLINT ni evaluar pi o una suma theta en un punto. Certifica los27coeficientes positivos, los55monomios y K, y todas las desigualdades racionales de TAIL/LOG-ERROR/MVT. La corrida final terminó exit0 con los cuatro bloques PASS.

SHA256 de la versión estable:

    d2b1e479295cbf9eda602a2786b657cab5c83db1c74dee9a7d00b751723fc8f4.

Una comprobación simbólica auxiliar previa produjo las mismas identidades. El certificado final es autocontenido en operaciones racionales, no en muestreo de parámetros.

## 7. Consecuencia de transporte y límite

086 ya prueba B'>0 y J=(A'/B')'>0 para TODOt>0. Con Eraise=(C'/B')', la identidad

    W4=−(B')³J²(Eraise/J)'

implica(Eraise/J)'>0 para TODOt>=1. Rolle en la coordenada B da el signo negativo del determinante de cuatro densidades en cualesquiera cuatro puntos distintos TODOS>=1. El signo de primer modo sólo se usó después de pagar la cola completa.

Para aplicar Andreief a toda la semirrecta0<t<infinito todavía falta el tramo0<t<1.087 certifica el signo en el origen y algún entorno no cuantificado, pero no llena ese intervalo. No se omite su contribución ni se pasa de una región de nodos de densidad al signo de la integral completa.

No se afirma transporte PF4 global, una nueva región W, cinco generadores, todos los órdenes o una ventana temporal. La prueba global de cuatro potencias085 permanece independiente y válida. El objeto estructural pendiente es el signo del nuevo Wronskiano de densidades en el compacto restante.
