# POWER_CONTACT_OSCILLATION_065 — Número exacto de cambios de signo para todos N,k

Estado: **PROVED/APROBADO**, revisión independiente en POWER_CONTACT_OSCILLATION_AUDIT_065.md y revisión de root. Teorema sobre la autocorrelación y el signo de la cola aritmética; NO sobre el signo de W. Papers intactos.

## 1. Antecedentes y cambio de objeto

Leídos las reglas del proyecto, ROUTES-TRIED-INDEX/README, grid maestro R162_2300_MASTER_GRID y CROSSWORD-TO-D; revisados ARITHMETIC_DIFFERENCES019 y su auditoría, DESCENT016 y los antecedentes de derivadas Bessel, Laguerre, Descartes, bell-shaped y total positivity. La búsqueda dirigida no halló en el corpus POWER un enunciado de número exacto de raíces para TODOS k.

019 demuestra una sola frontera para k=1 mediante el cociente de coeficientes j(j+1)-2N y Descartes. No se relanza ese cálculo con otro nombre. Aquí cambia el objeto: se consideran las derivadas de orden2k de C_(N+k) y se cuenta su número exacto de raíces mediante cancelación de2k momentos y convoluciones exponenciales unilaterales. La prueba usa Rolle con un borde en infinito, no un supuesto de positividad total de otro kernel. La cota de última raíz obtenida aquí es deliberadamente más gruesa que la de019 para k=1.

## 2. Enunciado y coeficientes exactos

Sean u>0, enteros N>=1,k>=1 y

    F_(N,k)(s)=s^k/(s+u)^(N+k),
    K_(N,k)(t)=c_(f_(N,k))(t).

Entonces K_(N,k) tiene exactamente k raíces en(0,infinito), TODAS simples, y ningún otro cero allí. Es positiva en0 y sus signos alternan al atravesar esas raíces. Si chi_(N,k) es la mayor raíz en la coordenada x=u t, entonces

    chi_(N,k) < 4k(N+k-1).                              (LAST)

Para dar los coeficientes, ponga d=N+k-1 y

    p_d(x)=sum_(j=0)^d a_j x^j,
    a_j=(2d-j)!/[2^(d-j)(d-j)!j!],
    r_(d,k)(x)=(1-D_x)^(2k)p_d(x).

Las fórmulas gamma de019 y la regla de Fourier dan exactamente, para t>=0,

    K_(N,k)(t)=(-1)^k C_(N+k)^(2k)(t)
      =(-1)^k exp(-x)r_(d,k)(x)
                 /[2^(d+1)u^(2N-1)d!], x=ut.           (PROFILE)

Su coeficiente de x^j es

    [x^j]r_(d,k)
      =sum_(ell=0)^min(2k,d-j)
          (-1)^ell binom(2k,ell)(j+ell)! a_(j+ell)/j!.

Equivalentemente, usando potencias factoriales descendentes,

    [x^j]r_(d,k)/a_j
      =sum_(ell=0)^min(2k,d-j)
          binom(2k,ell)(-2)^ell
                    (d-j)_fall_ell/(2d-j)_fall_ell.     (COEFF)

El término ell=0 vale1. Todos los denominadores de los términos presentes son positivos. No se extiende la suma a términos con denominador cero. El grado de r es exactamente d y su coeficiente principal es1.

## 3. Dos hechos elementales de conteo

Como ilustración algebraica, en N=1 y x=u|t| los tres primeros perfiles NORMALIZADOS son

    K_(1,1)(t)/K_(1,1)(0)=exp(-x)(1-x),
    K_(1,2)(t)/K_(1,2)(0)=exp(-x)(1-5x/3+x²/3),
    K_(1,3)(t)/K_(1,3)(0)=exp(-x)(1-11x/5+4x²/5-x³/15).

Son sustituciones exactas en PROFILE, no nuevos cálculos de W. El argumento siguiente demuestra que tienen, respectivamente, una, dos y tres raíces positivas simples y extiende ese patrón a TODOS N,k sin enumerar casos.

**Momentos.** Para todo N>=1,k>=1,

    int_R t^ell K_(N,k)(t)dt=0, 0<=ell<2k.              (ZERO-MOMENTS)

En efecto, su transformada es tau^(2k)/(u²+tau²)^(N+k), que tiene un cero de orden2k en tau=0. Los momentos temporales son absolutamente convergentes: PROFILE es exponencial por un polinomio en cada semirrecta. Además

    K_(N,k)(0)=(1/(2pi))int_R tau^(2k)/(u²+tau²)^(N+k)dtau>0.

**Momentos obligan cambios.** Si una función real continua no nula tiene momentos absolutos hasta orden r-1 y todos esos momentos son cero, y tiene un número finito de ceros, debe tener al menos r cambios de signo. De lo contrario, multiplicarla por el polinomio producto de los factores(t-b) de sus s<r puntos de cambio produce, tras elegir un signo global, una función no negativa y no idénticamente cero. Su integral sería positiva, contradiciendo la anulación de los momentos hasta grado s.

## 4. Lema de convolución unilateral: ceros simples preservados

Sean

    e_+(t)=exp(-ut)1_(t>=0),
    e_-(t)=exp(ut)1_(t<=0).

Suponga que f es real continua, con colas exponencial por polinomio, exactamente r ceros simples, y momentos cero de órdenes0,...,r-1. Cada convolución e_+*f y e_-*f tiene también exactamente r ceros, todos simples, y conserva esos momentos cero.

La preservación de momentos se verifica por Fubini y la expansión binomial de(t+y)^ell; ambos factores tienen momentos absolutos de todos los órdenes. Las colas siguen siendo exponencial por polinomio. En la aplicación, cada semirrecta conserva exactamente la forma exp(-u|t|) por un polinomio. Ninguna convolución puede anularse idénticamente en un intervalo: su ecuación g'=f-u g (o g'=u g-f) forzaría que f también se anulara allí, contradiciendo sus ceros simples finitos. Así los polinomios de ambas semirrectas no son idénticamente cero y los intermedios tienen un número finito de ceros; la cuenta de Rolle de abajo proporciona además una demostración independiente de esa finitud.

Para g=e_+*f se tiene g'=f-u g. Ponga h(t)=exp(ut)g(t), de modo que

    h'=exp(ut)f(t), h(-infinito)=0.

Así h' tiene exactamente r ceros simples. Un cero de g es simple si f no se anula allí. Si g(b)=f(b)=0, entonces g'(b)=0 y g''(b)=f'(b)!=0, de modo que ese cero sería doble. La derivada existe en b por la simplicidad de f allí. No hay otros tipos de multiplicidad.

Si h tuviera m ceros contados con multiplicidad, Rolle obliga a h' a tener al menos m: hay los correspondientes ceros de multiplicidad reducida en cada cero múltiple, uno entre cada par de ceros distintos y UNO antes del primero. Este último existe porque h tiende a0 al extremo izquierdo, vale0 en el primer cero y no es idénticamente cero en el intervalo: alcanza un extremo interior no nulo. La cuenta total es

    sum multiplicidades - numero de ceros distintos
       + (numero de ceros distintos-1)+1 = m.

El mismo argumento sobre cualquier colección finita de ceros excluye infinitos ceros. Por tanto m<=r. La cancelación de momentos obliga a al menos r CAMBIOS de signo, de modo que m=r y todos los ceros son simples. En particular se excluyen las tangencias dobles.

Para e_-*f basta reflejar t; equivalentemente, usar h=exp(-ut)g, h'=-exp(-ut)f y el borde h(+infinito)=0. Esto prueba el lema sin invocar una propiedad general de otros kernels.

## 5. Caso base y propagación a TODO N

Para N=1, el polinomio r_(k,k) de PROFILE tiene grado k. Así K_(1,k) tiene a lo sumo k ceros positivos. Es par y no se anula en0, por lo que tiene a lo sumo2k ceros reales distintos. ZERO-MOMENTS obliga a al menos2k cambios de signo. Se concluye que tiene exactamente k raíces positivas, todas simples, y sus reflejos negativos.

La función C_1(t)=exp(-u|t|)/(2u) satisface exactamente

    C_1=e_+*e_-.

Por multiplicación de transformadas,

    K_(N+1,k)=C_1*K_(N,k).

Aplicar sucesivamente el lema unilateral a e_- y e_+ preserva los2k ceros simples y los2k momentos nulos. Inducción en N prueba que K_(N,k) tiene exactamente2k ceros reales simples para TODO N>=1. Como es par y positiva en0, exactamente k están en la semirrecta positiva.

El signo inicial es positivo. El coeficiente principal de r es positivo, de modo que el signo final en PROFILE es(-1)^k; coincide con alternar k veces desde el signo inicial.

## 6. Cota elemental del último cero

Para x>0, como todos los coeficientes de p_d son positivos,

    0<=p_d^(ell)(x)/p_d(x)<= (d)_fall_ell/x^ell
                                    <=(d/x)^ell.

La primera cota procede término a término de(j)_fall_ell<=(d)_fall_ell, y vale con derivada cero cuando ell>d. Por ello

    |r_(d,k)(x)-p_d(x)|/p_d(x)
      <=sum_(ell=1)^(2k)binom(2k,ell)(d/x)^ell
      =(1+d/x)^(2k)-1.

Si x>=4kd,

    (1+d/x)^(2k)<=exp(1/2)<2.

La última desigualdad se obtiene comparando la serie exponencial con la geométrica de razón1/2, estrictamente desde el término cuadrático. Así r_(d,k)(x)>0 para TODO x>=4kd. No hay ceros en ese intervalo y se obtiene LAST. No se afirma optimalidad ni se sustituye la mejor cota019 en k=1.

## 7. Cola aritmética completa, con su signo correcto

Suponga u>1/2 para garantizar convergencia absoluta del peine. Para TODOS los enteros q>=2 con

    u log q >= 4k(N+k-1),

PROFILE y LAST dan

    sign K_(N,k)(log q)=(-1)^k.

Por tanto cada término no nulo de la contribución

    -2 Lambda(q)q^(-1/2)K_(N,k)(log q)

tiene signo(-1)^(k+1). La suma sobre TODOS esos q tiene ese mismo signo estricto: hay potencias de2 arbitrariamente grandes con Lambda>0. No se trunca ni modifica Lambda. En particular la cola ayuda a W para k impar y es adversa para k par.

Para k=0 se separa el caso: K_(N,0)=C_N es estrictamente positiva, no tiene raíces y el peine completo es negativo, como ya registra019. No se usa la fórmula de corte con k=0 como si produjera una transición.

El teorema no estima la magnitud de la cola ni la compensación frente al prefijo, ARCH y polar. No prueba W>=0, una fila nueva, una ventana T nueva o el signo global. Su resultado es el patrón de oscilación para TODOS N,k y una frontera explícita después de la cual TODA la cola tiene signo conocido.
