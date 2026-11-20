# POWER_QUADRATIC_017 — Paquete cuadrático y obligación de controlar el peine completo

Estado: PROVED cota de autocorrelación uniforme en el cono cuadrático y positividad eventual para P=1; PROVED aproximación de TODA la suma aritmética por una serie gaussiana modulada. Revisado independientemente en POWER_INTERIOR_AUDIT_017.md. Sin campañas numéricas. Papers intactos.

## Antecedentes y razón nueva registrados antes de construir

Consultados las reglas del proyecto, JOINT_SCALE016, HIGHPASS015 y TATE_CHAIN009; índice ROUTES-TRIED-INDEX y su inventario R2/R5 (criticidad, E_gamma, paquetes y familias moduladas); grid parte3; CROSSWORD-TO-D (paquetes, fluctuación Chebyshev, pesos gaussianos). No se relanza una cota genérica para paquetes ni se atribuye signo a un teorema central del límite.

La diferencia concreta es la escala conjunta k~cN² del MISMO test racional P=1: se busca su autocorrelación cuantitativa y se exige justificar por separado cualquier paso a la suma infinita del peine. Las cotas ponderadas uniformes falsificadas en016 no se reutilizarán. Un resultado sobre contactos fijos o truncamientos no se declarará control del peine completo.

## 1. Teorema: una banda analítica de la DENSIDAD conserva cancelación

Fije u=63/2, N>=2, k entero, y

    F_(N,k)(s)=s^k/(s+u)^(N+k),
    rho_(N,k)(z)=z^(2k)/(u²+z²)^(N+k),
    I_(N,k)=∫_R rho_(N,k)(x)dx>0,
    R_(N,k)(t)=c_f(N,k)(t)/||f_(N,k)||².

Para cualquier c>0, si k>=max(cN²,4N), se prueba

    ∫_R |rho_(N,k)(x+i)|dx/I_(N,k) <=C(c),
    C(c)=1+2[exp(4/(25c))+exp(1/c)].                     (STRIP)

Desplazar el contorno dentro de la banda sin polos |Im z|<u da entonces

    |R_(N,k)(t)|<=C(c)exp(−|t|), para TODO t real.       (CORR)

Esta cota no contradice016: se desplaza la DENSIDAD racional completa, conservando el producto de sus dos factores, no se separa en las normas ponderadas de F y su conjugada. Esa separación perdía una compensación esencial.

## 2. Prueba elemental de STRIP: región principal

Ponga M=N+k, y=sqrt(x²+1), T=u²/(y²+u²). La identidad algebraica exacta es

    |rho(x+i)|=rho(y)[1−(4/u²)T²]^(-M/2).               (MOD)

En |x|>=sqrt(3), y>=2 y dx/dy=y/sqrt(y²−1)<=2. Como M<=2k y 4/(u²−4)<1/100, la desigualdad −log(1−a)<=a/(1−a) da

    [1−(4/u²)T²]^(-M/2)<=exp(kT²/100).

Bajo la probabilidad rho(y)dy/I sobre toda la recta, T tiene distribución Beta(b,a), con b=N−1/2 y a=k+1/2. Basta acotar E exp(kT²/100). Divida en T<=4N/k y su complemento.

En el primer segmento,

    exp(kT²/100)<=exp[4N²/(25k)]<=exp[4/(25c)].

En el complemento, use T²<=T y exp(kT/100)<=(1−T)^(-k/100). El peso cambia la beta a a'=99k/100+1/2. La contribución queda acotada por

    [B(a',b)/B(a,b)] P_(a',b)(T>4N/k).                  (BT)

Dos desigualdades gamma elementales son suficientes. Para b>=1,

    Gamma(a+b)/Gamma(a)<=(a+b)^b,
    Gamma(a'+b)/Gamma(a')>=(a')^b.

La primera se obtiene integrando psi(x)<=log x; esta última es Jensen para log de una variable gamma. La segunda es Jensen para su potencia b. Por tanto

    B(a',b)/B(a,b)
       <=[(k+N)/(99k/100)]^N
       <=exp(N²/k)(100/99)^N.

Por Markov usando el momento entero N de la nueva beta,

    P_(a',b)(T>4N/k)
       <=(k/(4N))^N (b)_N/(a'+b)_N
       <=(50/99)^N.

Aquí (b)_N<(2N)^N y (a'+b)_N>=(99k/100)^N. Así BT es menor que

    exp(1/c)(5000/9801)^N<=exp(1/c).

La región principal de la integral normalizada de MOD es por ello <=2[exp(4/(25c))+exp(1/c)].

## 3. Región pequeña y normalización beta

En |x|<=sqrt(3), |x+i|²<=4 y |u²+(x+i)²|>=u²−1. La longitud del segmento es menor que4. Por otra parte,

    I=u^(1−2N)B(k+1/2,N−1/2).

Usando la integral beta en T∈[N/(2k),N/k], válida porque k>=4N y N>=2,

    B(k+1/2,N−1/2)
       >=[N/(2k)]^(N−1/2) exp(−2N).                    (BL)

Se usaron T^(N−3/2) creciente y (1−N/k)^k>=exp(−2N). Defina A=u²/(u²−1)<2 y r=4/(u²−1)<1/100. La contribución pequeña normalizada es menor que

    (4/u) A^N r^k [2k/N]^(N−1/2)exp(2N).

Para t=k/N>=4, (2t)^N<exp(k)<3^k y A^N exp(2N)<18^N<3^k. La expresión es menor que (4/u)(9r)^k<1. Combinada con§2 prueba STRIP.

Para CORR, el integrando rho(z)exp(izt) es racional y holomorfo entre Im z=0 y1. Las caras verticales desaparecen al llevar Re z a infinito, por el decaimiento O(|z|^(-2N)). Desplazar hacia arriba para t>=0 introduce exp(−t). La simetría de la autocorrelación cubre t<0. No se desplazó una norma temporal ni se supuso una constante ponderada falsa.

## 4. Control de TODO el peine y signo eventual en el cono

CORR implica, sin signo supuesto de contactos,

    |Comb[f]|/||f||²
      <=2C(c)Σ(q>=2)Lambda(q)q^(-3/2)<14C(c).            (PRIME)

Se usó Lambda(q)<=logq y Σ(q>=2)(logq)q^-3/2<7. Esta última cota sigue de f(2)+∫_2^infinito f(x)dx, pues f(x)=(logx)x^-3/2 decrece desde2, y log2<7/10. PRIME controla la suma infinita completa uniformemente en N,k de este cono.

La ley beta exacta016 da

    E log|tau|=log u+(1/2)psi(k+1/2)−(1/2)psi(N−1/2).

Con psi(x)>=logx−1/x, psi(x)<=logx y el lower global del símbolo m(tau)>=log(|tau|/(2pi))−4,

    Arch[f]/||f||²
       >=(1/2)logN+log[u sqrt(c)/(2pi)]−5.              (ARCH)

El polar tiene valor absoluto normalizado

    (4pi/u)[u²/(u²−1/4)]^N
       [1/(4u²−1)]^k /B(k+1/2,N−1/2).

Aplicar BL como en§3, con A<2 y r=1/(4u²−1)=1/3968, muestra

    |Polar[f]|/||f||²<400^-k,                            (POL)

porque 4pi/u<1 y 9/3968<1/400. Así

    W[f]/||f||²
      >(1/2)logN+log[u sqrt(c)/(2pi)]−5−14C(c)−400^-k.

**Teorema de signo:** para cada c>0 existe N0(c) explícitamente acotable tal que W[f_(N,k)]>0 para TODOS N>=N0(c), TODOS k>=cN². Basta exigir N>=max(2,4/c) y

    (1/2)logN+log[u sqrt(c)/(2pi)]>6+14C(c).

No es un certificado de todos los numeradores: se mantiene P=1, como se declaró. El umbral es deliberadamente muy conservador, pero la prueba es uniforme y controla todos los contactos.

## 5. Autocorrelación cuadrática: aproximación cuantitativa de contactos

Si k=ceil(cN²), ponga mu_N=u sqrt(k/N). La misma beta se representa mediante variables independientes X~Gamma(k+1/2,1),Y~Gamma(N−1/2,1): |tau|=u sqrt(X/Y). Para cualquier T finito,

    sup_(|t|<=T)|R_(N,k)(t)
        −exp(−u²ct²/8)cos(mu_N t)| <=C_(c,u,T)/sqrt(N)  (GAUSS)

para N suficientemente grande. Se demuestra elementalmente así:

* Los momentos gamma hasta orden cuatro muestran que, en L¹,
  |tau|=mu_N−(u sqrt(c)/2)(Y−N)/sqrt(N)+O(N^-1/2).
  En el evento X/k,Y/N∈[1/2,3/2] se usa Taylor con resto cuadrático de sqrt(X/k)/sqrt(Y/N). Su esperanza multiplicada por sqrt(N) es O(N^-1/2). En el complemento, los cuartos momentos dan probabilidad O(N^-2); Cauchy–Schwarz y E tau²=O(N) dan el mismo error. La contribución lineal de X es O(N^-1/2).
* La función característica exacta de (Y−N)/sqrt(N) es exp(−iz sqrt(N))(1−iz/sqrt(N))^(-N+1/2). Taylor de log(1−iz/sqrt(N)) da exp(−z²/2)+O_T(N^-1/2), uniformemente para z en un compacto.
* |exp(ita)−exp(itb)|<=|t||a−b| y la simetría de tau convierten esas dos estimaciones en GAUSS.

El mismo argumento vale con k/N²->c, reemplazando el error explícito por o(1) uniforme en compactos de t. En ese caso puede mantenerse c_N=k/N² en la amplitud gaussiana antes de pasar al límite.

## 6. La aproximación pasa a la suma infinita, no solo a contactos fijos

CORR, que es independiente de GAUSS, proporciona el majorante sumable que faltaba en016. La envolvente gaussiana también es sumable contra Lambda(q)q^-1/2. Separando un segmento finito y su cola, se obtiene para k=ceil(cN²)

    Comb[f]/||f||²
      =−2Σ(q>=2)Lambda(q)q^-1/2
          exp[−u²c(logq)²/8]cos(mu_N logq)+o(1).         (ALL)

La serie de ALL es absolutamente convergente y uniformemente acotada en mu_N. No se afirma que su signo sea favorable, ni se reemplaza por cero mediante una oscilación no demostrada. El control de su magnitud basta, porque ARCH crece logarítmicamente.

Más precisamente, E tau^-2=(N−1/2)/[u²(k−1/2)]=O(1/N). Las cotas elementales ya probadas en Paper47, lem:mbounds, dan |m(tau)−log(|tau|/(2pi))|<=1/|tau|+1/(2tau²) para tau distinto de0. Por Cauchy--Schwarz y la fórmula beta, su esperanza es O(N^-1/2), pues E tau^-2=O(1/N). Esto y la fórmula de Elog dan

    W[f]/||f||²=(1/2)logN+log[u sqrt(c)/(2pi)]
      −2Σ(q>=2)Lambda(q)q^-1/2
          exp[−u²c(logq)²/8]cos(mu_N logq)+o(1).         (PROFILE)

Así la autocorrelación no tiene por qué desaparecer en cada contacto; queda una serie modulada acotada. La nueva herramienta no necesita que desaparezca.

## 7. Alcance y límite preciso

Se obtuvo una herramienta que evita las normas temporales uniformes falsificadas016: desplazar conjuntamente la densidad espectral racional. El resultado prueba signo eventual en el cono cuadrático para P=1 y suma toda la aritmética con un majorante uniforme. No prueba ese cono para TODOS los numeradores ni controla las primeras dimensiones, ni convierte la serie de PROFILE en un objeto no negativo. Tampoco se invoca criticidad como descarte: se ha demostrado directamente el lower necesario en esta familia concreta.


## Apéndice A. Bounds globales elementales de digamma usados en ARCH

Se incorpora una prueba propia del constructor principal, revisada independientemente. Para a>0,t real, ponga g(x)=x/(x²+t²). La serie de digamma y el límite armónico dan

    Re psi(a+it)=lim_(n->infinito)[logn-sum_(j=0)^(n-1)g(a+j)].

En cada intervalo unitario, la diferencia entre el valor en el extremo izquierdo y la integral se acota en valor absoluto por la integral de |g'| sobre ese intervalo. Por tanto el error total es<=integral_a^(a+n)|g'|. Si |t|<=a, g decrece y su variación en[a,infinito) es g(a)<=1/a. Si |t|>=a, g crece hasta|t| y luego decrece; su variación total es2g(|t|)-g(a)<=1/|t|<=1/a. En ambos casos

    Re psi(a+it)>=log|a+it|-1/a,

porque integral_a^(a+n)g=(1/2)log[((a+n)²+t²)/(a²+t²)] y el término logn cancela su extremo superior al pasar al límite. Aplicar a1/4,t=tau/2 da, para tau distinto de0,

    m(tau)>=log(|tau|/(2pi))-4.

En t0 produce también psi(x)>=logx-1/x. La otra cota psi(x)<=logx se obtiene de la integral gamma: psi(x)=ElogX con X~Gamma(x,1), EX=x, y Jensen para log. Estas demostraciones justifican las dos desigualdades gamma integradas en BT y las cotas de ARCH sin una cita especial no verificada.
