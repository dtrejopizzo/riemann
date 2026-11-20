# POWER_POLAR_MOVEMENT_005 — Transporte de polos con polar: identidad, sector favorable y obstrucción real

Estado: PROVED (identidades, sector P<=0, falsificador general, orden uno en rango alto y derivada uniforme positiva de orden cuatro en confluencia); OPEN (transporte global de signo de orden cuatro para tasas>=63/2). Papers intactos.

## 1. Antecedentes y razón nueva

Consultados índice ROUTES-TRIED-INDEX, grid y crucigrama (polar movement, pole filter, positive polar, confluent), además de POWER_POLE_MOVEMENT_004, POWER_CONFLUENT_004 y su auditoría. La parte arquimediana ya posee un transporte exacto. La diferencia nueva es conservar el polar POSITIVO, que resulta esencial en orden cuatro: el diagnóstico confluente tiene mínimo arquimediano cercano a -.17005, mientras que arch+polar tiene mínimo cercano a +.32259. No se trata el polar como pérdida uniforme ni se extrapola el movimiento arquimediano.

## 2. Identidad exacta con numerador racional fijo

Para tasas v_j>=u_j>1/2, sea H(s)=Π_j(s+u_j)/(s+v_j), fhat_nuevo=H(i tau)fhat_antiguo. Defina

    R(tau)=|H(i tau)|²=Π_j(u_j²+tau²)/(v_j²+tau²),
    r0=H(-1/2)H(1/2)=Π_j(u_j²-1/4)/(v_j²-1/4).

Normalice f_antiguo a norma uno, y use la probabilidad dμ=|fhat_antiguo|²d tau/(2pi). Sean Aold=Eμ m y Pold=2A(f)B(f), ambos cocientes Rayleigh con la norma antigua. Entonces

    Enew-Eold=[Covμ(m,R)+(r0-EμR)Pold]/EμR.               (F)

Todos los factores polares son reales positivos, y si al menos un polo crece,

    0<r0<R(0)<=R(tau)<=1.

La primera desigualdad estricta sale de (u²-1/4)/(v²-1/4)<u²/v² para u<v. Por tanto la covarianza arquimediana sigue siendo favorable, pero el segundo término tiene signo OPUESTO a Pold.

### Sector que sí se transporta

Para todo numerador con Pold<=0, (F) prueba Enew>=Eold. El signo del polar se conserva al mover polos porque se multiplica por r0>0. Esto incluye los subespacios A=0 o B=0. Para Pold>0 la identidad sola no da comparación: es exactamente el sector que puede rescatar una dirección arquimediana negativa.

## 3. Falsificador al transporte general, sin tocar el rango alto

Se obtuvo el siguiente contraejemplo exacto. En orden uno, numerador fijo 1, tasa u>1/2, el cociente arch+polar es

    E(u)=psi((u+1/2)/2)-log pi+4u/(u²-1/4).

Para u=1 y v=2, las identidades de reflexión y recurrencia de psi dan

    E(2)-E(1)=(4-pi)+(32/15-16/3)=4/5-pi<0.

Así el teorema general «arch+polar aumenta al aumentar polos» es FALSO incluso en dimensión uno. Los sitios están fuera del rango u>=63/2; NO refuta el transporte de signo o monotonía en el rango relevante de orden cuatro.

## 4. Orden uno en el rango alto: PROVED

Sí hay una prueba elemental del transporte completo para n=1 y u>=8. Por la serie de trigamma y comparación integral, psi'(x)>=1/x. Luego

    E'(u)>=1/(u+1/2)-4(u²+1/4)/(u²-1/4)².

Para u>=8, el primer término es >=16/(17u). El segundo es menor que 5/u², pues u²+1/4<=(257/256)u², u²-1/4>=(255/256)u², y 4*(257/256)/(255/256)²<5. Finalmente 16/(17u)>5/u² para u>=8. Así E'>0 en ese rango, incluyendo todas las tasas del proyecto. El falsificador §3 no se extiende automáticamente al rango alto.

## 5. Derivada confluente exacta para orden cuatro

Una reducción adicional conserva el acoplamiento. Fije u y use la base Laguerre ortonormal con transformadas

    F_j(s)=sqrt(2u)/(s+u)*[(s-u)/(s+u)]^j, j=0,...,3.

La matriz arch+polar es Toeplitz, M_ij=m_|i-j|. Con g(s)=[psi((s+1/2)/2)-log pi]/2 y r=(u+1/2)/(u-1/2), sus entradas exactas son

    m0=2g(u)+4u/(u²-1/4),
    mk=Σ_{j=1}^k g^(j)(u)(2u)^j binom(k-1,j-1)/j!
          +[2u/(u²-1/4)](-1)^k(r^k+r^-k), k>=1.

Mover UN polo con numerador fijo multiplica la transformada por (s+u)/(s+u+delta). A delta=0, su derivada temporal es -(F_j-F_{j+1})/(2u), pues 1/(s+u)=(1-z)/(2u). Para un vector real normalizado x de cuatro coordenadas, ponga c_k=Σ_j x_jx_{j+k}. La derivada del cociente completo satisface exactamente

    u E'=m1+m2 c1+(m1+m3)c2+(m2+m4)c3
             -2c1(m1 c1+m2 c2+m3 c3).                       (D4)

El término m0 cancela contra la derivada de la norma; omitirla produce un resultado incorrecto. Esta es una desigualdad cuártica concreta en cuatro variables, no una equivalencia abstracta con el objetivo global.

## 6. Derivada uniforme positiva de orden cuatro en u=63/2: PROVED

Para todo numerador no nulo de grado menor que cuatro, al aumentar UN polo desde la configuración confluente (u,u,u,u), u=63/2, el cociente arch+polar cumple

    dE/dv_j >3/(40u)=1/420.

Se demuestra mediante una única identidad SOS racional finita, no por optimización de autovectores. La razón nueva respecto de SOS aritmético registrado en el corpus es que aquí se certifica una cuártica explícita en CUATRO coeficientes de numerador, en UN punto declarado de tasas; no se busca una factorización universal de la forma aritmética.

Primero, las series de polygamma en el entero 16, con colas acotadas por integrales, prueban

    |m1-8887/10000|<1/10000,
    |m2-1116/10000|<1/10000,
    |m3-2213/10000|<1/10000,
    |m4-1126/10000|<1/10000.

Sea Dbar la cuártica homogénea (D4) usando esos cuatro centros racionales y N=Σx_i². Con z=(x0²,x0x1,x0x2,x0x3,x1²,x1x2,x1x3,x2²,x2x3,x3²), la identidad exacta es

    Dbar-(2/25)N²=z^t Q z,

donde Q es la siguiente matriz dividida por 10000:

```text
 8087   558  5550  1121 -5250  -358 -1663  1687   558   937
  558  8900  -200  5000   558 -4324  1005 -1358 -2787   558
 5550  -200 12800     0 -7900   800 -7200  5550  1005 -1663
 1121  5000     0 14300 -1000 -10000    0 -1000  5000  1121
-5250   558 -7900 -1000  8087   558  5550 -5450 -1358  1687
 -358 -4324   800 -10000 558  9300   800   558 -4324  -358
-1663  1005 -7200     0  5550   800 12800 -7900  -200  5550
 1687 -1358  5550 -1000 -5450   558 -7900  8087   558 -5250
  558 -2787  1005  5000 -1358 -4324  -200   558  8900   558
  937   558 -1663  1121  1687  -358  5550 -5250   558  8087
```

La eliminación LDL exacta de Q da DIEZ pivotes mayores que 1/5. Por tanto es positiva definida; equivale a una suma de diez cuadrados de combinaciones racionales de los monomios z, con coeficientes racionales positivos. Como |c_k|<=N, las sensibilidades de D4 respecto a m1,m2,m3,m4 están acotadas respectivamente por 4N²,4N²,3N²,N². La pérdida por sustituir los cuatro coeficientes es menor que (12/10000)N². Por ello

    D4>(2/25-12/10000)N²>(3/40)N².

Para N=1, esto demuestra la cota de derivada declarada. Todos los cuatro intervalos, la identidad de 35 coeficientes cuárticos, los diez pivotes y la desigualdad final se verifican únicamente con `Fraction` en `tools/polar_derivative_sos_005.py`; el verificador no contiene optimizador, coma flotante ni funciones especiales numéricas.

Comando: `python3 03-research/phase-211-sign-sandbox/tools/polar_derivative_sos_005.py`. Una optimización de la única cuártica concreta sirvió para descubrir el Gram; no interviene en la prueba final ni se hizo un barrido de tasas.

### Estructura elemental del término dominante

La observación del constructor principal explica la coercividad subyacente: sea J la matriz de camino de cuatro vértices con entradas 1/2 fuera de diagonal inmediata. Entonces

    N²+c2 N-2c1²
      =2[||Jx||²N-<Jx,x>²]+(x0²+x3²)N/2 >=0.

El primer término es una varianza y el segundo una energía de borde. El certificado Q retiene suficiente margen de esta estructura al incorporar m2,m3,m4 y sus errores. No se afirma que las otras tres contribuciones sean positivas por separado.

### Alcance del transporte local

La cota de derivada vale para TODO numerador de grado menor que cuatro en el punto confluente, no sólo para el autovector inferior. Como la esfera de numeradores es compacta y los kernels dependen continuamente de las tasas, existe una vecindad de (u,u,u,u) en la que todas las derivadas individuales siguen siendo positivas. No se declara un radio explícito. Esto prueba un transporte local de cocientes y de eigenenergías; no permite recorrer por sí solo todo el ortante de tasas>=u.

## 7. Residuo preciso

Para signo de orden cuatro no basta una cota absoluta de |polar|: elimina la contribución positiva que compensa el mínimo arquimediano negativo. Hace falta dominar en (F) la pérdida (EμR-r0)Pold por la covarianza cuando Pold>0, o probar directamente un transporte de signo más débil. Esta nota no prueba ninguna de esas dos desigualdades en orden cuatro. El contraejemplo general §3 impide afirmarlas sin hipótesis de rango y dimensión; el caso alto n=1 y el sector Pold<=0 sí están cerrados por prueba.
