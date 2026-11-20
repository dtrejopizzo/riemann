# POWER_THREE_002 — Tres potencias por concentración elemental

Estado: PROVED (rango explícito grande); no da uniformidad en el número de generadores. Papers intactos.

Antecedentes consultados: POWER_CONE_001, PROPOSAL_POWER_CASES_2026_11_04; índice README:393,655, NODE_001:195, grid part3:12 y part5:7, crucigrama (theta/cosh/Pick). Razón nueva respecto de la positividad general de Pick ya registrada: se prueba un rango finito mediante concentración cuantitativa de un subespacio explícito de tres exponenciales. No se propone otra caracterización general.

## 1. Auditoría del término cruzado

Escriba u=a-1/2, v=b-1/2, h_u(y)=exp(-uy)1_{y>0}, g(a)=(psi(a/2)-log pi)/2 y D(a)=zeta'(a)/zeta(a). La correlación simetrizada es

    [exp(-ut)+exp(-vt)]/[2(u+v)].

La integral directa del multiplicador arquimediano da [g(a)+g(b)]/(u+v), y el peine da [D(a)+D(b)]/(u+v). El término polar bilineal completo es

    1/[(a-1)b]+1/[a(b-1)].

Con R(a)=1/a+1/(a-1), esto es EXACTAMENTE [R(a)+R(b)]/(a+b-1), pues 1/a+1/(b-1)=(a+b-1)/[a(b-1)], y análogamente para el otro par. Por tanto K_ab=[L(a)+L(b)]/(a+b-1) es correcto; no requiere inferir cross a partir de diagonales. La integración arquimediana usa Re psi como función armónica en Re z>0 y su integral de Poisson, o su serie absolutamente convergente tras restar psi(1/4).

## 2. Teorema de tres generadores

Sean A>=2^31 y 0<h<=A/2. Para cualesquiera c_0,c_1,c_2 reales no todos nulos,

    rho(X)=Σ_{j=0}² c_j X^{-(A+jh)}

satisface Q[rho]>0. Más precisamente, con f(y)=Σ c_j zeta(A+jh)exp(-(A+jh-1/2)y), y>0,

    Q[rho]>=9 ||f||_2².

La constante es deliberadamente muy conservadora. Prueba a continuación. En particular P3 vale en este rango, sin computar un determinante mal condicionado.

## 3. Base racional y concentración en frecuencia

Considere cualquier espacio de tres exponenciales con tasas u<=u_j<=3u, u>=2^30, distintas. Tiene base ortonormal cuyas transformadas de Fourier son

    F_j(tau)=sqrt(2u_j)/(u_j+i tau) Π_{k<j}(i tau-u_k)/(i tau+u_k).

La ortonormalidad se comprueba por integración de fracciones racionales (cerrar el contorno en el semiplano sin polos); equivalentemente cada factor (s-u_k)/(s+u_k) conserva la norma en el eje imaginario y anula la evaluación de Laplace en s=u_k. Parseval usa d tau/(2pi). Como cada factor tiene módulo uno,

    |fhat(tau)|² <=||f||² Σ_j 2u_j/(u_j²+tau²)<=6||f||²/u.

La densidad de probabilidad p=|fhat|²/(2pi||f||²) está acotada por M=3/(pi u). Entre densidades de masa uno acotadas por M, la integral de log|tau| se minimiza por M 1_{|tau|<=1/(2M)}. Por integración directa,

    ∫ log|tau| p(tau)d tau >= log(pi u/6)-1.

Atención al factor DOS: la longitud del intervalo extremal es 1/M, su radio 1/(2M). Esta es la normalización usada en las cotas siguientes.

## 4. Cota arquimediana sin constantes especiales numéricas

La serie de digamma da, poniendo y=tau/2,

    Re psi(1/4+iy)=psi(1/4)+Σ_{k>=0} y²/[(k+1/4)((k+1/4)²+y²)].

El sumando decrece con k; comparación integral da suma >=(1/2)log(1+4tau²). Además psi(1/4)=-gamma-pi/2-3log2>-6, y log pi<2. Por tanto

    m(tau)>=log|tau|-8.

Combinando con §3,

    <m(D)f,f>/||f||² >= log(pi u/6)-9
       > log u-10 >10,

porque pi>3, log2<1 y log u>=30log2>20. Todas las desigualdades son estrictas en el rango declarado.

## 5. Cotas de cola y del polar

La transformada inversa de cada factor all-pass es delta_0-2u_k exp(-u_k y)1_{y>0}. Expandiendo la convolución de hasta dos factores y usando u_j<=3u se obtiene

    |f(y)|<=sqrt(6u)||f|| exp(-uy)[3+18uy+18(uy)²].

Se usó Cauchy--Schwarz en los tres coeficientes ortonormales y después suma de valores absolutos; los coeficientes mayores que los necesarios facilitan las cotas. Para z>=0, z<=2exp(z/2), z²<=16exp(z/2), de modo que

    |f(y)|<=327sqrt(6u)||f||exp(-uy/2),
    ||f 1_{y>=t}||<=327sqrt6 exp(-ut/2)||f||.

En consecuencia |c_f(t)|<=327sqrt6 exp(-ut/2)||f||². El valor absoluto del peine es a lo sumo

    654sqrt6 Σ_{n>=2} Lambda(n)n^{-(u+1)/2}||f||²
       <=1602 Σ_{n>=2}n^{-(u-1)/2}||f||² < ||f||²/10.

La última desigualdad ya vale si (u-1)/2>=16, usando Σ n^{-p}<=2^{-p}(1+2/(p-1)).

Para los dos momentos polares, integrar la cota polinómica original, usando u-1/2>=u/2, da

    |∫ f(y)exp(±y/2)dy| <=366sqrt(6/u)||f||.

En detalle los tres términos integrados son a lo sumo 6/u, 72/u y 288/u. Por tanto

    |2AB|<=12*366² ||f||²/u <||f||²/10

para u>=2^30. Sumando §§4--5 da Q[rho]>(10-1/10-1/10)||f||²>9||f||².

## 6. Alcance y siguiente orden

Para el triple del teorema u=A-1/2>=2^30 y u_2=A+2h-1/2<=3u. La prueba cubre incluso triples desiguales contenidos en [u,3u]. No requiere separación mínima; por continuidad cubre límites confluyentes y exponenciales multiplicadas por polinomios de grado <=2.

## 7. Todos los órdenes con umbral creciente (PROVED)

Para cada entero n>=1, cualquier familia de n tasas distintas u_i en [u,3u], con u>=2^{40n}, satisface

    W[Σ_i d_i exp(-u_i y)1_{y>0}]>=9||Σ_i d_i exp(-u_i y)||².

Esto prueba positividad de todas las matrices de orden n del kernel de §1 cuyos exponentes a_i=u_i+1/2 estén en ese rango. No es uniformidad en n.

Prueba con constantes: la misma base racional da p(tau)<=n/(pi u), luego

    arch/||f||² >=log(pi u/(2n))-9 >log u-log n-9 >10.

La última desigualdad usa log u> (80/3)n y log n<=n-1. La expansión de convoluciones da

    |f(y)|<=sqrt(6u)||f|| exp(-uy) P_n(uy),
    P_n(z)=Σ_{k=0}^{n-1}binom(n,k+1)6^k z^k/k!.

Aquí se usó la identidad Σ_{j=k}^{n-1}binom(j,k)=binom(n,k+1). Como z^k/k!<=2^k exp(z/2), se obtiene P_n(z)<=13^n exp(z/2). Por tanto

    tailnorm(t)<=sqrt6 13^n exp(-ut/2)||f||,
    |∫ f exp(±y/2)dy|<=2sqrt6 13^n ||f||/sqrt u.

La segunda cota integra P_n exactamente contra exp(-uy/2): Σ binom(n,k+1)12^k<13^n. De aquí

    |polar|/||f||² <=48*169^n/u <1/10.

Para el peine, p=(u-1)/2>=u/4>=20n+10 y

    |peine|/||f||² <=2sqrt6 13^n Σ_{q>=2}q^{-p}
       <=6sqrt6 13^n 2^{-p}<15*16^n*2^{-(20n+10)}<1/10.

También 48*169^n/u<48*2^{-32n}<1/10, como se usó arriba. Suma de términos: W>9.8||f||²>9||f||². La dependencia exponencial 2^{40n} es muy burda y explícita; no se ha optimizado.

## 8. Obstrucción cuantitativa a extrapolar estos rangos

Para f normalizado de la familia del teorema de orden n,

    ||f 1_{y>=delta}||<=sqrt6 13^n exp(-2^{40n}delta/2).

En particular para delta=1 esto es menor que 1/100 para todo n>=1: usar log13<3 y 2^{40n}/2>3n+10. Así la unión de estas familias NO es densa en L²(0,infinito): toda función unitaria soportada en [1,2] queda a distancia al menos sqrt(2-2/100)>1.4 de cada miembro normalizado, por Cauchy--Schwarz. Incluso con escalares arbitrarios la distancia a la recta generada por cada f es >=sqrt(1-10^{-4}).

Trasladar los paquetes puede eliminar esta localización alrededor de cero, pero el teorema sólo prueba el signo de cada paquete por separado; no controla los términos cruzados de sumas de paquetes trasladados. No se puede pasar de una unión positiva a su envolvente lineal.

Por tanto este resultado, aunque vale a todo orden con umbral creciente, no da un dominio denso positivo para la forma. El umbral debe bajar hasta permitir una familia común de exponentes, o hay que controlar explícitamente los términos cruzados entre paquetes. El resultado no resuelve el signo del paper.
