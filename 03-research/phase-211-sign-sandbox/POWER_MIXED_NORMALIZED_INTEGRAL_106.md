# POWER_MIXED_NORMALIZED_INTEGRAL_106 — Control holomorfo uniforme para el sistema mixto

Estado: **LEMA ANALÍTICO PROBADO; auditorías independientes aprobadas. SIGNO GLOBAL OPEN.** No nuevo dato theta, punto, cuadratura o corrida. El presupuesto final de ejecución permanece PENDIENTE. Se demuestra control uniforme de dominio y errores para habilitar un certificado, no positividad del Wronskiano. Papers intactos.

## 1. Consulta y diferencia precisa

Consultados las reglas del proyecto, README ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; cotejados077/089/093/095/099/103/104 y las obligaciones Volterra de105. El objeto es el sistema PAR mixto[K,J,Phi,J''], suficiente para el siguiente cruce REAL de103, no el sistema impar más fuerte093/095 ni la condición T_h ya cerrada099.

104 sólo prueba el signo en el origen sin radio y en t>=64. Aquí no se repite ese test ni se afirma una nueva conservación. Se resuelve una dificultad distinta: las integrales normalizadas se hacen holomorfas con bounds independientes de la amplitud superexponencial de Phi y con colas explícitas. Eso permite evaluar jets DIRECTAMENTE, evitando que un error de valores iniciales se amplifique al propagar una ODE rígida.

Mantener p=−Phi'/Phi,a=M'(0),0<a<1,

    J(z)=int_z^infinito sPhi(s)ds,
    K(z)=int_z^infinito(s−z)[aPhi(s)−J(s)]ds,
    tau=J/Phi, kappa=K/Phi, X=zp−1=J''/Phi.

Las identidades de integrales se entienden primero en reales; su continuación holomorfa se justifica abajo. La cota a<1 ya está contenida en los certificados completos098/103; no se estima a mediante datos nuevos.

## 2. Phi y Theta no se anulan en un strip uniforme

Sea

    S={z: Re z>=−1/16, |Im z|<=1/16},
    y=pi exp(2z), Y=|y|,
    Theta(y)=sum_(m>=1)m²(2m²y−3)exp[−(m²−1)y].

Phi(z)=pi exp(5z/2)exp(−y)Theta(y). Las cotas pi>3,exp(−1/8)>7/8 y cos(1/8)>31/32 dan

    Y>21/8,
    Re y>(31/32)Y>5/2.

Escribir Theta(y)=(2y−3)(1+Rtheta(y)). Para todos m>=2,

    |m²(2m²y−3)/(2y−3)|
       <=m^4(2Y+3)/(2Y−3)<4m^4.

Los términos m^4 exp[−(5/2)(m²−1)] tienen razones menores que1/2 desde m=2: basta(3/2)^4 exp(−25/2)<1/2. La serie exponencial da exp(5/2)>8. Por tanto la cola COMPLETA cumple

    |Rtheta|<128exp(−15/2)<1/4.                 (ZERO-FREE)

Así ni Theta ni Phi se anulan en S. El argumento no usa muestras, truncaciones sin resto ni un lower de Phi real trasladado informalmente a complejo.

También, para w=y+v,v>=0 real, |w|>=Y,Re w>5/2. La misma prueba se aplica a Theta(w). En particular

    |Theta(y)|>9Y/14,
    |Theta(w)|<55|w|/14,
    |Theta(y+v)/Theta(y)|<(55/9)|y+v|/Y
                            <7|y+v|/Y.         (THETA-RATIO)

Esta forma con |y+v| permite cancelar exactamente el jacobiano en el bound siguiente; no se sustituye indebidamente |y+v| por Y+v en un denominador complejo.

## 3. Integrales exactas normalizadas con cola exp(−v)

Poner, para v>=0,

    r(z,v)=(1/2)Log(1+v/y),
    A(z,v)=exp(−v)(1+v/y)^(5/4)
              Theta(y+v)/[2(y+v)Theta(y)].

Log y la potencia usan la rama principal. Son holomorfas en z dentro del strip: Re(1+v/y)>0, Re(y+v)>0 y ZERO-FREE excluye los denominadores. Además

    |r(z,v)|<=v/[2 Re y]<v/Y.

La desigualdad se obtiene integrando1/(y+s) desde0 hasta v; no supone que el logaritmo complejo esté ordenado.

En z real, el cambio EXACTO v=y(z+s)−y(z) transforma la cola anticausal, con ds=dv/[2(y+v)]. Fubini para K da

    tau(z)=int_0^infinito (z+r)A(z,v)dv,
    kappa(z)=int_0^infinito [a r−(z+r)r²/2]A(z,v)dv. (NORMALIZED)

La segunda fórmula usa

    K(z)=a int_0^infinito sPhi(z+s)ds
            −(1/2)int_0^infinito(z+s)s²Phi(z+s)ds.

Para z complejo no se afirma que un cambio de variable en una integral horizontal produzca automáticamente v real. Se procede por identidad analítica: ambas expresiones de NORMALIZED coinciden en el eje real; el lado derecho es holomorfo en S y localmente dominado por la cota integrable de§4. El lado izquierdo también lo es por las primitivas enteras y ZERO-FREE. Por identidad analítica coinciden en el strip conectado. Esto evita una deformación de contorno no justificada.

El factor exp(−v) es independiente de y. No se computa una razón de dos cantidades exp(−pi exp(2t)) casi nulas ni se resta una cola pequeña de momentos globales.

## 4. Bounds uniformes de columnas y cola v completa

THETA-RATIO implica exactamente

    |A(z,v)|<7/(2Y) exp(−v)(1+v/Y)^(5/4)
             <=7/(2Y) exp(−v)(1+v)^2.

Para |z| acotado, NORMALIZED se domina por funciones integrables independientes de z. Usar

    int_0^infinito(1+v)^2exp(−v)dv=5,
    int_0^infinito v(1+v)^2exp(−v)dv=11,
    int_0^infinito v²(1+v)^2exp(−v)dv=38,
    int_0^infinito v³(1+v)^2exp(−v)dv=174.

Se obtiene, con todas las colas incluidas,

    Y|tau(z)|<(7/2)(5|z|+11)<100(1+|z|),
    Y²|kappa(z)|<(7/2)(98+19|z|)<1000(1+|z|). (COLUMN)

Para |z|<65, las mismas estimaciones punto a punto del integrando dan

    Y |integrando_tau|<512 exp(−v)(1+v)^5,
    Y²|integrando_kappa|<512 exp(−v)(1+v)^5.

Al usar constantes de centro Yc=pi exp(2c),c en[0,64], y |z−c|<=1/32, Yc/Y<16/15<2 y(Yc/Y)^2<2. Puede usarse el bound común conservador

    2048exp(−v)(1+v)^5

para AMBOS integrandos escalados por Yc y Yc². Si se fija L=512, la cola completa de esas funciones es menor que

    2048exp(−512)sum_(j=0)^5 binom(5,j)513^(5−j)j!
      <2^62 exp(−512)<2^(−450).                 (V-TAIL)

La suma finita es menor que2*513^5<2^51; exp1>2 paga la última desigualdad. Es un bound holomorfo uniforme, no un valor observado. Cauchy en el disco de radio1/32 convierte V-TAIL en errores de coeficientes<=2^(−450)32^j para los jets directos. No se deben obtener esos jets propagando valores iniciales inciertos mediante ODE.

## 5. Cola completa de modos y su efecto en la función integrada

Sea Theta16 la suma m=1,...,16 y T16=Theta−Theta16. En cualquiera de los argumentos w=y o y+v de§3,

    |T16(w)|<=8*17^4 |w| exp(−720).

La razón consecutiva para m>=17 es menor que(18/17)^4exp(−175/2)<1/2. Dividir por el lower9|w|/14 de Theta da el bound conservador

    |delta(w)|=|T16(w)/Theta(w)|<2^(−698).       (MODE-TAIL)

Se usaron17^4<2^17 y exp1>2; el prefactor8*14/9 es menor que16. Theta16 tampoco se anula, pues Theta16=Theta(1−delta).

Sustituir Theta por Theta16 en ambos factores del cociente cambia A en menos de4*2^(−698)|A|. Por las estimaciones integrables de§4, el error TOTAL de función para Yc tau y Yc² kappa, antes de truncar v, es menor que2^(−675). El bound es deliberadamente conservador: integrar2048exp(−v)(1+v)^5 cuesta menos que2^20. Por Cauchy sus errores de coeficientes en un centro son<=2^(−675)32^j.

Para completar también la columna local X, poner p16=2y−5/2−derivative_z logTheta16(y). Como delta(y(z)) es holomorfa en S y de módulo menor que2^(−698), |log(1−delta)|<2^(−697). Cauchy de radio1/32 alrededor de cada z en|z−c|<=1/32 permanece en S y da

    |p−p16|<2^(−692),
    |(X−X16)/Yc|<2^(−687), X16=zp16−1.

Se usaron|z|<65,Yc>3. Su error de coeficientes es<=2^(−687)32^j, y por tanto el bound conservador2^(−675)32^j cubre TODAS las columnas no constantes. No se deriva informalmente la cola de modos real.

Estos bounds pagan TODOS los modos omitidos en numerador y denominador. No basta añadir un error sólo al numerador ni tratar una aproximación del denominador como si fuera exacta. La cola V-TAIL y MODE-TAIL son errores distintos y se suman antes de pedir un signo.

## 6. Budget Cauchy del Wronskiano y origen removible

Este paso es un bound, no un diseño de ejecución cerrado. Para c en[0,64] mantener constantes las escalas Yc²,Yc,1,Yc^(−1) y definir las cuatro columnas

    [Yc² kappa,Yc tau,1,X/Yc].

Su Wronskiano es Yc² Wmixed/Phi^4. En |z−c|<=1/32, COLUMN da bounds2^17 y2^13 para las dos primeras. Para la primera columna se conserva el factor preciso (Yc/Y)^2<(16/15)^2: 1000*66*256/225<2^17; no se sustituye aquí por el bound2 más grueso. ZERO-FREE y Cauchy de log(1+Rtheta) en un disco de radio1/32 dentro de S dan |p|<10Y, luego |X/Yc|<2^10. En el disco interior|z−c|<=1/64, cada derivada de orden j<=3 cuesta a lo sumo j!64^j<2^21. La columna constante tiene derivadas superiores cero. El bound de24productos proporciona

    |Yc² Wmixed/Phi^4|<2^108<2^120.             (W-BOUND)

Por paridad, los cuatro cocientes son pares holomorfos cerca0; su Wronskiano tiene un cero de orden al menos6. La función

    F_c(z)=Yc² Wmixed(z)/[Phi(z)^4 z^6]

es holomorfa después de quitar ese cero. En |z−c|<=1/128, si |z|>=1/256, W-BOUND da |F_c|<2^168. Si |z|<=1/256, entonces c<=3/256 yYc²/pi²<2. Aplicar el principio del máximo a Wmixed/[Phi^4 z^6] en el círculo|z|=1/128, donde W-BOUND con centro0 vale, da de nuevo

    |F_c(z)|<2^168.                             (REGULARIZED-BOUND)

Éste es un presupuesto Cauchy uniforme posible para eliminar la cancelación t^6 en el origen. No se ha elegido todavía grado ni número de paneles finales, ni demostrado un lower del signo en el compacto.

## 7. Ejecución pendiente y controles que no pueden omitirse

El futuro diseño debe fijar, ANTES de datos, una cuadratura rigurosa para la integral finita v en[0,512], tolerancias y límites, precisión, orden de jets, partición temporal y bound del resto de Taylor. Si se usa acb.integral, el callback debe respetar analytic: sólo declarar holomorfía cuando las bolas prueben Re(y+v)>0 y Re(1+v/y)>0, con Theta16(y) separado de0; en caso contrario debe devolver un valor no finito y permitir subdivisión rigurosa. Las constantes y ramas se auditarán antes de ejecutar.

El cambio a una integral normalizada no prueba que el signo sea positivo. Tampoco la subdivisión interna de una cuadratura rigurosa decide una familia de parámetros: deberá aplicarse sólo a la obligación compacta fija. No se ejecutó ninguna cuadratura, jet, muestra o probe nuevo para esta fuente. SIGNO GLOBAL y conservación siguen OPEN.

## 8. Ampliación: cuadratura vectorial fija con control complejo

Estado: **LEMA ANALÍTICO PROBADO; revisión matemática independiente aprobada antes de datos.** Es una herramienta para el futuro programa, no la ejecución de107 ni un certificado de signo. Se reutilizan las columnas normalizadas y el dominio de esta fuente. La consulta de los tres índices y de104–106 no encontró este presupuesto de cuadratura; no se vuelve a evaluar ninguno de sus datos.

Partir la variable de integración en los DIEZ intervalos

    [0,1], [1,2], [2,4], ..., [256,512].

Para cada uno, sean b su centro, h su semiancho y R=2h. En el disco complejo |v-b|<=R, el primer intervalo tiene Re v>=-1/2 y |v|<=3/2. Los restantes tienen b=3h, Re v>=h y |v|<=5h. En todos ellos Re(y+v)>2. Para 0<=s<=1 se verifica además

    Re(1+s v/y)>4/5.

En efecto, el mínimo de Re(v/y) es (b cos(arg y)-2h)/Y. En el primer disco es mayor que -1/5 usando cos(arg y)>31/32 y Y>21/8; en los restantes es positivo. Por ello la rama principal y los denominadores son holomorfos en estos discos, y

    |r(z,v)| <= 5|v|/(8Y) < |v|/Y.

Para w=y+v, Re w>2 y |w|>2. La suma absoluta da

    |Theta16(w)| <= (7/2)|w| sum_(m>=1) m^4 exp[-2(m^2-1)]
                  <7|w|.

La suma es menor que2: el primer término es1, el término m=2 es menor que1/4 y las razones posteriores son menores que1/2. Por MODE-TAIL,

    |Theta16(y)|>9Y/28.

En consecuencia el cociente acoplado, incluido el jacobiano, satisface

    |Theta16(y+v)/[(y+v)Theta16(y)]|<22/Y.

Con |z|<65 y las escalas constantes Yc,Yc^2 de§4, las DOS funciones integrando truncadas, para tau y kappa respectivamente, quedan acotadas por

    4096 exp(-Re v)(1+|v|)^5.

Por ejemplo, usando Yc/Y<2 y (Yc/Y)^2<2, sus factores polinomiales se acotan por 22(65+u)(1+u)^2 y 22[u+(65/2)u^2+u^3/2](1+u)^2, con u=|v|; ambos son menores que4096(1+u)^5. Esta estimación es para Theta16, de modo que puede usarse directamente al acotar el error de cuadratura. Los errores de modos completos de§5 se añaden por separado.

En el primer disco la cota es menor que2^20. En los demás, h>=1/2, 1+5h<=7h y h^5 exp(-h)<=5!=120, por lo que

    4096 exp(-h)(1+5h)^5 <=4096*7^5*120<2^34.

Así M=2^34 es un mayorante común. Para cualquier centro real t en[0,64], Cauchy en la variable temporal, con radio1/32, acota el coeficiente temporal de orden j del integrando por

    M_j=2^34*32^j.

El argumento es uniforme también para los coeficientes en un subintervalo real de semiancho a lo sumo1/64, con escalas fijas en su centro c. Los discos de radio1/32 alrededor de sus puntos quedan en |z-c|<=3/64, dentro de S; allí Yc/Y<2 y (Yc/Y)^2<2, y |z|<65. Esto paga expresamente el ancho del parámetro, sin reutilizar una cota local fuera de su dominio. No se propagan valores iniciales inciertos mediante una ODE.

En cada intervalo de v, usar Gauss–Legendre de64 nodos y pesos positivos. Su exactitud hasta grado127 permite comparar tanto la integral como la cuadratura con el Taylor de grado127 en b. En los nodos y en el intervalo, el resto de ese Taylor es a lo sumo M_j(h/R)^128/(1-h/R). La integral cuesta2h veces ese bound y la suma de pesos de la cuadratura también es2h. Por tanto el error analítico por intervalo es

    4h M_j (1/2)^128/(1-1/2)=8h M_j 2^(-128).

Como la suma de todos los semianchos es256, el error total para el coeficiente j es

    2^(-83+5j),
    en particular <=2^(-68) para j=0,1,2,3.       (GAUSS-ERROR)

Esta prueba no usa un error de derivada estimado numéricamente ni supone que el integrando sea real para parámetros complejos. Sólo usa holomorfía, el mayorante, exactitud polinomial y pesos positivos. La implementación deberá encerrar rigurosamente nodos y pesos: la API local `arb.legendre_p_root(64,k,weight=True)` proporciona esas bolas. Sus errores de redondeo se propagan mediante aritmética de intervalos y son ADICIONALES al error analítico anterior, no absorbidos informalmente en él.

Los640 nodos totales permiten evaluar juntos los jets temporales de orden0 a3. Antes de formar el Wronskiano deberán sumarse GAUSS-ERROR, las colas v y de modos, y todos los errores aritméticos; para obtener derivadas, multiplicar los coeficientes por sus factoriales. Sigue pendiente el diseño completo de la partición temporal, el tratamiento del origen, la precisión y los límites de ejecución. No se ha ejecutado ninguna evaluación theta ni prueba de signo para esta ampliación.
