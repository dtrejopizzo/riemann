# POWER_COMMON_TRANSFER_010 — Criterio común de déficit y dos controles ponderados

Estado: PROVED. Extrae las hipótesis exactas del transporte FOUR009 y FIVE010; incorpora una mejora de norma propuesta por el constructor principal. No afirma signo a dimensión arbitraria. Papers intactos.

## 1. Hipótesis suficientes explícitas

Fije entero n>=1 y u>1/2. Sea V0 el espacio racional de transformadas P(s)/(s+u)^n, gradoP<n. Suponga disponibles b,C,c,X,D, con X>0,D>=0,c>0, tales que

    AP[f0]>=b||f0||²,
    |Polar[f0]|<=C||f0||², para todo f0 en V0;
    m(tau)>=c cuando tau²>=X;
    tau²(c-m(tau))_+<=D, para todo tau.

Los dos primeros son hipótesis de TODO el bloque confluente, no pruebas sobre un vector; los dos últimos son cotas del símbolo en todo el dominio indicado. Defina

    K_n=[(1+X/u²)^n-1]/X,
    eta=b-c-DK_n-Cn/(4u²).

Si eta>0, entonces AP[f]>c||f||² para TODOS los polos v_j>=u, permitiendo multiplicidades, y cualquier numerador real de grado<n.

## 2. Prueba única de transporte

Se mantienen el mismo numerador y el mapa H(s)=prod(s+u)/(s+v_j). Con R=|H(i tau)|²,R0=prod u²/v_j²,r0=H(-1/2)H(1/2), se tiene

    R>=R0,
    R/R0<= (1+tau²/u²)^n,
    1-n/(4u²)<=r0/R0<=1.

La última cota usa r0/R0>= (1-1/(4u²))^n y Bernoulli. Incluso si el lado inferior de Bernoulli es negativo, la cota de pérdida1-r0/R0<=n/(4u²) sigue siendo válida. El cociente [(1+x/u²)^n-1]/x tiene coeficientes no negativos y crece para x>=0; sobre x<=X está acotado por K_n.

La identidad exacta es

    AP[f]-c||f||²=R0(AP[f0]-c||f0||²)
       +integral (R-R0)(m-c)|fhat0|²/(2pi)
       +(r0-R0)Polar[f0].

Fuera de x<=X, la integral adicional es no negativa. Dentro se pierde a lo sumo R0 DK_n||f0||². La pérdida polar es a lo sumo R0 Cn/(4u²)||f0||². Así el lado izquierdo es >=R0 eta||f0||²>0. La norma objetivo es la de f NUEVA; no se necesita una comparación uniforme entre R0||f0||² y ||f||².

No es una afirmación de monotonía del cociente AP ni de eigenenergías AP. Cada uso debe verificar sus propios b,C,c,X,D y eta; no se heredan automáticamente de otro grado.

## 3. Control ponderado por Young, ya usado en las pruebas

Fije 0<alpha<1 y sigma=alpha u. La base racional ortonormal de Malmquist se forma a partir de una exponencial sqrt(2v_j)e^(-v_j y) y j factores all-pass (s-v_k)/(s+v_k). La exponencial inicial tiene norma ponderada al cuadrado v_j/(v_j-sigma)<=(1-alpha)^-1. El núcleo all-pass delta0-2v e^(-vy), al ponderar por e^(sigma y), tiene variación total

    1+2v/(v-sigma)<=(3-alpha)/(1-alpha)=r_Y.

Young y Cauchy--Schwarz en los n coeficientes dan

    ||e^(sigma y)f||²<=B_Y||f||²,
    B_Y=(1-alpha)^-1 sum_(j=0)^(n-1) r_Y^(2j).

Esta es la cota válida utilizada previamente. Para alpha2/3, B_Y=(49^n-1)/16; para alpha3/4, B_Y=(81^n-1)/20; para alpha1/2, B_Y=(25^n-1)/12.

## 4. Mejora exacta por multiplicador Fourier ponderado

Se puede sustituir Young por Parseval sin ninguna suposición nueva de signo. Todas las funciones racionales causales decaen como polinomio por exponencial con tasas>=u>sigma; por tanto su ponderación está en L² antes de estimarla. Ponderar un filtro equivale a evaluar su Laplace en s=-sigma+i tau. Para un factor de tasa v>=u,

    |(-sigma+i tau-v)/(-sigma+i tau+v)|²
      =[(v+sigma)²+tau²]/[(v-sigma)²+tau²]
      <=[(v+sigma)/(v-sigma)]²
      <=[(1+alpha)/(1-alpha)]²=r_F².

Así cada factor tiene norma de operador ponderada <=r_F. La exponencial inicial conserva la cota anterior. Por Parseval sucesivo y Cauchy--Schwarz,

    ||e^(sigma y)f||²<=B_F||f||²,
    B_F=(1-alpha)^-1 sum_(j=0)^(n-1) r_F^(2j).

Como r_F<r_Y, ésta mejora la cota sin invalidar los certificados anteriores. Para alpha1/2, B_F=(9^n-1)/4; para alpha2/3, B_F=(25^n-1)/8; para alpha3/4, B_F=(49^n-1)/12. La base sigue ortonormal sólo en la norma SIN peso; Cauchy--Schwarz es lo que permite sumar sus normas ponderadas, sin atribuirles ortogonalidad ponderada.

## 5. De una cota ponderada al peine completo

Cualquiera de B_Y,B_F da

    |c_f(t)|<=sqrt(B)e^(-sigma t)||f||²,
    |Comb[f]|<=L||f||²,
    L=2sqrt(B) sum_(q>=2)Lambda(q)q^(-sigma-1/2).

La suma converge si sigma>1/2; ésta es una hipótesis adicional necesaria para usar este majorante de TODOS los contactos. Si sigma>3/2 se puede usar Lambda(q)<=q y p=sigma-1/2>1:

    L<=2sqrt(B)2^-p[1+2/(p-1)].

Más ajustado, para beta=sigma+1/2>1 y beta log2>=1, la función logx*x^-beta decrece para x>=2, por lo que

    L<=2sqrt(B)2^-beta[log2+2log2/(beta-1)+2/(beta-1)^2].

Si se reemplaza beta por un entero inferior todavía >1, debe conservarse la monotonía requerida. Puede usarse cualquier cota racional superior de log2 dentro del último corchete. Estos majorantes no presumen signo favorable de ningún contacto individual.

Si eta>0 en §1 y se certifica L<c, el resultado completo es W[f]>(c-L)||f||² en todos esos espacios de n polos. El criterio no exige un margen de error independiente de n; deben verificarse todas las constantes para cada aplicación.

## 6. Mejora adicional: traza ponderada máxima en la confluencia

Nueva observación del constructor principal, revisada independientemente. Mantenga sigma=alpha u fijo, 0<alpha<1. Para la base ortonormal racional de tasas v_j>=u, ponga

    R_j(tau)=[(v_j+sigma)²+tau²]/[(v_j-sigma)²+tau²].

La transformada del modo j en la recta desplazada s=-sigma+i tau satisface exactamente

    |phi_jhat(-sigma+i tau)|²
       =(R_j-1)/(2sigma) prod_(k<j)R_k.

Sumar telescópicamente da

    sum_j |phi_jhat(-sigma+i tau)|²
       =[prod_j R_j-1]/(2sigma).                         (TR)

Integrar por Parseval es la traza de la matriz Gram de la norma ponderada. La transformada inversa de R_j-1 es la función positiva

    k_v(t)=2v sigma/(v-sigma) exp(-(v-sigma)|t|).

Para sigma fijo y v>sigma, d_v log k_v(t)=-sigma/[v(v-sigma)]-|t|<0. Al expandir prod_j R_j-1 en subconjuntos no vacíos, cada integral espectral es la evaluación en cero de una convolución de funciones k_v positivas. Estas funciones son integrables y acotadas; las convoluciones son finitas, continuas y decrecen al aumentar cualquiera de sus tasas. Por tanto la traza ponderada es no creciente en cada v_j y alcanza su máximo cuando todos los v_j=u.

En la confluencia, el modo j es sqrt(2u)e^(-uy)L_j(2uy). Con s=1-alpha, su norma ponderada al cuadrado es

    integral_0^infinito e^(-sx)L_j(x)^2 dx
      =s^(-2j-1) sum_(k=0)^j binom(j,k)^2 alpha^(2k).

La identidad se prueba finitamente usando la conexión polinómica

    L_j(x)=s^-j sum_(k=0)^j binom(j,k)(s-1)^(j-k)L_k(sx)

y la ortogonalidad tras cambiar variable t=sx; reindexar k↔j-k produce la fórmula escrita. Así se obtiene la cota uniforme adicional

    ||e^(sigma y)f||² <=B_T||f||²,
    B_T=sum_(j=0)^(n-1) sum_(k=0)^j
                binom(j,k)^2 alpha^(2k)/(1-alpha)^(2j+1). (BT)

Aquí se usa que la norma de una matriz Gram positiva está acotada por su traza. Se probó MONOTONÍA DE LA TRAZA bajo movimiento de polos; no se probó monotonía del mayor eigenvalor de la matriz Gram. La cota del operador procede de operatornorm<=trace y trace(v)<=trace(u), que es suficiente y evita esa inferencia no justificada.

B_T puede reemplazar B_Y o B_F en §5 sin cambiar el criterio de transporte ni suponer localización temporal monotónica. Su prueba vale para polos repetidos directamente y para tasas arbitrariamente grandes, con sigma<min v_j asegurado por alpha<1.
