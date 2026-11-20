# Completitud en cuadrados y potencias perfectas: falsificadores de suficiencia

Estado: **PROVED algebraico y por transferencia de un certificado existente; auditorías matemática y literal independientes aprobadas (incluida la sección11).** No se ejecuta ningún cómputo nuevo. No se modifica un paper. La conclusión refuta sólo la suficiencia de las hipótesis declaradas para la forma de fondo fijo; no concierne al signo de la forma original de Lambda.

Ampliación de la sección11: normalización exacta del residuo mediante factores altos; auditorías matemática y literal aprobadas. Se distingue su cota N<=C de la condición N<=1 de ejemplos anteriores.

## 1. Consulta y antecedentes exactos

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README.md y06R7, R162_2300_MASTER_GRID.md, CROSSWORD-TO-D.md, el ledger C1–C51 de phase211 y POWER_REASSESSMENT.md. Leídos R186_005 y su corrección lógica en R186_092, los memos Euler finitos de phase197 y L2_BUILD_016_FROBENIUS_DOUBLING de phase188.

La búsqueda en el corpus de las fórmulas locales1+c_p z, N(n^2)=1, square completeness y variantes no encontró la familia continua presentada aquí. SÍ apareció el extremo que se usa como falsificador: R163_102_BOUNDED_ERROR_VS_LATTICE.md, Cor F, ejemplo T={2},Q={4}, registra el cociente A(s)=1/(1+2^(-s)); R163_191_AUDIT_101_102.md confirma ese ejemplo. Allí se estudia el error de conteo, no se prueba la negatividad primitiva utilizada abajo. Ese antecedente no se presenta como nuevo.

Phase197 contiene clases Euler con coeficientes N en{0,1}, de las que este extremo es miembro; sus conclusiones para defectos pequeños no se trasladan automáticamente a este parámetro. La dilatación de188 trata un transporte de ventanas y sus pesos, distinto de imponer N(n^2)=1. Ninguno de esos argumentos sustituye la prueba siguiente. El certificado negativo reutilizado es ROUND_007_C, teorema1; no se vuelve a ejecutar su script.

## 2. Familia exacta con completitud parcial no identificante

Elegir independientemente0<=c_p<=1 para cada primo y definir, con z formal,

    F_p(z)=(1+c_p z)/(1-z^2).

Sus coeficientes locales son

    N_c(p^(2j))=1,
    N_c(p^(2j+1))=c_p, j>=0.

El producto Euler determina una función multiplicativa N_c y una serie absolutamente convergente para Re s>1:

    F_c(s)=prod_p F_p(p^(-s))
          =zeta(2s) prod_p(1+c_p p^(-s))
          =sum_n N_c(n)n^(-s).

Para n=prod p^k,

    N_c(n)=prod_(k impar)c_p,
    0<=N_c(n)<=1,
    N_c(n^2)=1 para TODO entero n>=1.             (SQUARES)

Definir los coeficientes logarítmicos ell_c por -F_c'/F_c=sum ell_c(n)n^(-s). Expansión elemental de los dos logaritmos da

    log F_p(z)=sum_(k>=1)
       [(-1)^(k+1)c_p^k+2*1_(k par)]z^k/k.

Por tanto ell_c está soportada en poderes primos y

    ell_c(p^k)/log p=c_p^k,         k impar,
    ell_c(p^k)/log p=2-c_p^k,       k par.        (ELL)

En particular ell_c>=0 y ell_c<=2Lambda. Si todos los c_p=1 se recuperan N_c=1 y ell_c=Lambda. SQUARES no identifica ese miembro: si c_2=0, entonces N_c(2)=0 y ell_c(2)=0, aunque N_c(n^2)=1 para todo n. Es una familia concreta de completitud parcial, no una hipótesis vacía ni identificación total.

## 3. Extremo finito ya conocido y forma que se contrasta

Fijar ahora c_2=0 y c_p=1 para todos los primos p distintos de2. Entonces

    F_square(s)=zeta(s)/(1+2^(-s)),
    ell_square(2^k)=0 si k impar,
    ell_square(2^k)=2log2 si k par,
    ell_square(p^k)=log p si p distinto de2.

Este es el extremo cuyo cociente respecto de zeta figura en R163_102. Sus coeficientes N toman sólo0 y1, y SQUARES se mantiene en TODOS los cuadrados.

Además F_square tiene polo simple en s=1 con residuo2/3, NO residuo1. No se afirma que posea la ecuación funcional del miembro original. La obstrucción no debe usarse para clases que impongan esas hipótesis adicionales sin revisar si contienen el ejemplo.

La forma contrastada es EXACTAMENTE la forma primitiva de fondo arquimediano fijo de ROUND_007_C/Paper47, con pesos de contacto

    v_n=2ell(n)/sqrt(n).

Para una misma función F del portador primitivo P_T, los dos momentos de Tate son cero y el término polar es cero. Se cambia sólo ell en los contactos; el portador y el fondo arquimediano permanecen los mismos. No se atribuye a F_square una ecuación funcional compatible con ese fondo. Ninguna ecuación funcional para la deformación forma parte de las hipótesis que se refutan.

Escribir C_F(u) para la autocorrelación real de F. La diferencia entre dos formas con ese mismo fondo es exactamente la diferencia firmada de sus contactos, por la definición de la forma.

## 4. Testigo certificado existente, sin nueva evaluación

Usar literalmente el testigo de ROUND_007_C, teorema1, con

    T0=(log5)/2+1/10000,
    L=2T0=log5+1/5000.

En la coordenada s=t+T0, la función es cero fuera de[0,L] y

    f(s)=a1 sin(pi s/L)+x sin(3pi s/L)
          +a5 sin(5pi s/L)+a7 sin(7pi s/L),
    a1=-384199/10^6,
    a5=172109/10^6,
    a7=-4131/125000.

El coeficiente x es EL MISMO real que anula exactamente el momento A(F). El certificado007_C prueba x>1, más precisamente lo encierra en1.0000005632467671625 +/-4.3*10^(-20). Sólo aparecen índices impares, así que F es par y el otro momento de Tate también es cero. No se reemplaza x por un decimal ni se reajusta la función.

Si a_3 designa la deformación con el primo2 borrado en TODOS sus poderes, el certificado existente da

    a_(T0)^(a_3)(F)/||F||^2 <= -0.50528<0.       (CERT007)

La norma es positiva. Esta fuente USA ese resultado certificado y auditado; no introduce una nueva cuadratura ni un testigo numérico.

## 5. Signo elemental del contacto adicional en4

Poner delta=L-log4>0. Se tiene delta<L/7: la desigualdad es equivalente a

    log(128/125)>3/5000,

y la integral de1/u entre125 y128 es mayor que3/128>3/5000. Para0<s<delta, theta=pi s/L satisface

    0<theta<pi/7<1/2.

Entonces sin(3theta)=(3-4sin(theta)^2)sin(theta)>2sin(theta), sin(5theta)>0 y sin(7theta)<=7sin(theta). La última desigualdad se sigue, por ejemplo, de la suma de siete exponenciales que representa sin(7theta)/sin(theta). Con x>1,

    f(s)>[2-384199/10^6-7*4131/125000]sin(theta)
         =(1384465/10^6)sin(theta)>0.             (EDGE)

Por paridad f(L-s)=f(s). En consecuencia

    C_F(log4)=int_0^delta f(s)f(s+log4)ds
             =int_0^delta f(s)f(delta-s)ds>0.     (CONTACT4)

Es una prueba de signo analítica; no se ha evaluado la autocorrelación.

## 6. Transferencia del certificado y conclusión limitada

En la ventana T0 los únicos contactos relevantes de ell_square son3,4,5. Los de3 y5 coinciden con a_3; en2 ambas deformaciones tienen peso0. En4,

    ell_square(4)=2log2,
    v_4=2ell_square(4)/sqrt4=2log2.

Por tanto, sobre el MISMO testigo primitivo y con el MISMO fondo,

    a_(T0)^(ell_square)(F)
      =a_(T0)^(a_3)(F)-2log2*C_F(log4)
      <a_(T0)^(a_3)(F)
      <=-0.50528||F||^2<0.                       (NEGATIVE)

Así ell_square es un falsificador PROBADO de la suficiencia de

    ell>=0, soporte en poderes primos, N_ell multiplicativa,
    0<=N_ell(n)<=1 y N_ell(n^2)=1 para TODO n,
    polo simple en1, con residuo positivo NO impuesto igual a1

para garantizar la no negatividad de esta forma de fondo fijo en todas las ventanas. El mismo testigo extendido por cero da negatividad para todo T>=T0, por el lema2 de007_C; no se necesitan valores adicionales.

La nueva familia es no identificante, pero esa observación no la hacía viable como mecanismo de signo: contiene el extremo NEGATIVE. Esto no demuestra un NO-GO de cualquier uso imaginable de completitud parcial. Una hipótesis adicional que excluya ell_square tendría que especificarse y probarse por separado; en particular aquí no se ha supuesto una condición funcional global para la deformación. No se refuta el miembro ell=Lambda ni se modifica el objetivo original. No se ejecutó ningún certificado nuevo ni se tocó un paper.

## 7. Imponer residuo1 colapsa ESTE ansatz al miembro original

Para un número finito de parámetros c_p distintos de1, el cociente exacto es

    F_c(s)/zeta(s)=prod_p (1+c_p p^(-s))/(1+p^(-s)).

Es analítico y estrictamente positivo en s=1, de modo que F_c tiene polo simple con residuo

    R_c=prod_p (p+c_p)/(p+1).

Cada factor es positivo y a lo sumo1. Si alguno c_p<1, el residuo es estrictamente menor que1. Para c_2=0 y los demás1 da R_c=2/3.

La misma conclusión de identificación vale para modificaciones infinitas si se exige residuo1. Para todo sigma>1 real, el producto converge absolutamente y todos sus factores son a lo sumo1. Por cada primo fijo p0,

    0<F_c(sigma)/zeta(sigma)
       <=[1+c_(p0)p0^(-sigma)]/[1+p0^(-sigma)].

Si F_c tiene residuo R_c en1, tomar sigma hacia1 por la derecha da

    R_c<=(p0+c_(p0))/(p0+1).

Un solo parámetro c_(p0)<1 obliga R_c<1. Por tanto R_c=1 implica c_p=1 para TODOS los primos, y F_c=zeta. Es identificación dentro de ESTE ansatz, no una nueva prueba de signo. No se afirma ese colapso para toda clase imaginable con completitud parcial y residuo1.

## 8. Corolario uniforme: cada orden fijo de potencias perfectas es insuficiente

Para CADA entero fijo m>=2, reemplazar el primo2 por2^m y mantener todos los otros primos. Su producto exacto es

    F_m(s)=zeta(s)(1-2^(-s))/(1-2^(-ms)).

El factor local en2 es1/(1-z^m); los otros son los ordinarios. Así

    N_m(n)=1 si m divide la valuación de2 en n, y0 si no,
    N_m(n^m)=1 para TODO n,
    ell_m(2^k)=m log2 si m divide k, y0 si no,
    ell_m(p^k)=log p para p distinto de2.

En particular N_m es multiplicativa y toma sólo0 y1, y ell_m>=0. El cociente respecto de zeta pertenece a la misma familia de reemplazos finitos del antecedente R163_102, Cor F, con T={2},Q={2^m}; no se presenta ese producto como desconocido en el corpus.

Para m=2 es el ejemplo ya tratado: el contacto adicional en4 hace la forma estrictamente menor que la forma a_3 sobre el testigo certificado. Para TODO m>=3, el primer contacto adicional de2 está en2^m>=8, fuera de la ventana T0, cuyo extremo exponencial es menor que7. Por tanto sobre el MISMO testigo007_C,

    a_(T0)^(ell_m)(F)=a_(T0)^(a_3)(F)
        <=-0.50528||F||^2<0, m>=3.

Es una identidad uniforme, no una campaña de parámetros ni una nueva evaluación. Por extensión por cero vale también negatividad en toda ventana mayor.

Cada F_m tiene polo simple en1 con residuo

    R_m=1/[2(1-2^(-m))]<1.

No se le atribuye residuo1 ni la ecuación funcional del miembro original. La conclusión de ESTE corolario es que, para CADA orden FIJO m>=2, la completitud N(n^m)=1 en todas las potencias perfectas de ese orden no basta, junto con las hipótesis positivas declaradas, para garantizar el signo de la forma de fondo fijo. Este argumento por sí solo no impone simultáneamente varios órdenes; la sección9 trata esa condición más fuerte con OTRO ejemplo.

## 9. Todos los órdenes simultáneamente: falsificador con coeficientes no enteros

Considerar el factor local en2

    F_2(z)=1+z/2+sum_(k>=2)z^k
          =(1-z/2+z^2/2)/(1-z),

y mantener los factores ordinarios en los demás primos. El producto es

    F_all(s)=zeta(s)[1-2^(-s)/2+2^(-2s)/2].

Sus coeficientes multiplicativos satisfacen N_all(2)=1/2 y N_all(2^k)=1 para k>=2; todos los otros factores locales son completos. Por tanto

    0<=N_all(n)<=1,
    N_all(n^m)=1 para TODOS n>=1 Y m>=2
      SIMULTÁNEAMENTE.                          (ALL-POWERS)

Es importante que N_all(2) NO es entero. No se atribuye al ejemplo integridad de los coeficientes.

Para comprobar positividad de TODOS los coeficientes logarítmicos, escribir r_+=(1+i sqrt7)/4 y r_-=(1-i sqrt7)/4. Satisfacen r_++r_-=1/2, r_+r_-=1/2 y |r_+|=|r_-|=1/sqrt2. La identidad polinómica

    1-z/2+z^2/2=(1-r_+z)(1-r_-z)

y las series formales de los logaritmos dan

    ell_all(2^k)/log2=1-r_+^k-r_-^k.

Para k=1 vale1/2. Para k>=2, |r_+^k+r_-^k|<=2^(1-k/2)<=1, así que ell_all(2^k)>=0. En particular ell_all(4)=(7/4)log2. En los otros primos ell_all coincide con Lambda. Es una comprobación finita algebraica de un bound uniforme en k, no una búsqueda de coeficientes.

La búsqueda literal del polinomio1-z/2+z^2/2 y sus variantes en el corpus no encontró este ejemplo. Su forma es próxima al movimiento Euler finito de retorno1-z^k+z^(k+1) discutido en phase197; no se presenta el mecanismo Euler finito como nuevo. Aquí el coeficiente1/2 permite verificar ell>=0 en TODOS los niveles y ALL-POWERS; el argumento de forma siguiente usa el certificado anterior.

En la ventana T0, respecto de a_3 aparecen sólo los contactos de2 y4, con pesos

    v_2=(sqrt2 log2)/2,
    v_4=(7/4)log2.

CONTACT4 es estrictamente positivo. Para cualquier traslación, Cauchy–Schwarz aplicado al F extendido por cero da |C_F(u)|<=||F||^2. Así

    a_(T0)^(ell_all)(F)
      =a_(T0)^(a_3)(F)-v_2 C_F(log2)-v_4 C_F(log4)
      <[-0.50528+v_2]||F||^2.

Las cotas sqrt2<10/7 y log2<7/10 implican v_2<1/2. La primera es cuadrar98<100; para la segunda, el Taylor positivo de exp(7/10) hasta grado3 es12013/6000>2. Por tanto

    a_(T0)^(ell_all)(F)<-0.00528||F||^2<0.        (ALL-NEGATIVE)

No se ha evaluado un contacto nuevo ni repetido el certificado. La extensión por cero da negatividad para todo T>=T0.

F_all tiene polo simple en1 con residuo7/8, y no se le atribuye la ecuación funcional del miembro original. Se mantiene el mismo fondo y el mismo portador PRIMITIVO de las secciones3–6. En consecuencia, ALL-POWERS, N multiplicativa con0<=N<=1 y ell>=0 no bastan ni siquiera imponiendo TODOS los órdenes de potencias perfectas simultáneamente, si no se exige integridad, residuo1 u otras hipótesis que excluyan el ejemplo. No es una refutación de cualquier clase con completitud parcial, ni del dato original.

## 10. Si además se exige integridad, las potencias simultáneas identifican el dato

Hay una conclusión distinta, que NO es un NO-GO de signo. Supóngase N multiplicativa, N(1)=1,

    N(n^m)=1 para TODOS n>=1,m>=2,
    N(p) entero no negativo para cada primo,
    ell(p^k)>=0 para todos los poderes primos,

donde ell son los coeficientes logarítmicos del Euler formal de N. Fijar un primo y poner c=N(p). La primera hipótesis da N(p^k)=1 para todos k>=2. Su factor es

    F_p(z)=1+cz+sum_(k>=2)z^k.

El coeficiente de z^2 en z F_p'/F_p es2-c^2. Su no negatividad y c entero no negativo fuerzan c en{0,1}. Si c=0,

    F_p(z)=(1-z+z^2)/(1-z)=(1+z^3)/(1-z^2),
    z F_p'/F_p=3z^3/(1+z^3)+2z^2/(1-z^2).

El coeficiente de z^6 es2-3=-1, contradiciendo ell(p^6)>=0. Luego c=1 para TODOS los primos; todos los factores son1/(1-z), y

    N(n)=1 para TODO n,
    ell=Lambda.                                 (IDENTIFICATION)

Esto es identificación algebraica exacta por hipótesis, sin necesidad de asumir residuo1. No prueba el signo de la forma del dato identificado ni hace imposible una futura desigualdad que lo use. El ejemplo no entero de la sección9 no pertenece a esta clase, y su negatividad no debe atribuirse a ella. Se distinguen así tres hechos: las condiciones no enteras declaradas admiten falsificadores; residuo1 colapsa el ansatz específico de la sección2; e integridad más ALL-POWERS y ell>=0 identifican el dato por la presente prueba elemental.

## 11. Reparación exacta del residuo con factores altos invisibles al testigo

Esta ampliación sólo refuta otra clase declarada; no propone una nueva ruta al signo. La búsqueda adicional en el corpus y en los tres índices no encontró el producto compensador preciso siguiente. Hay antecedentes generales que se conservan: R163_102, lemaS, da el conteo de zeta multiplicada por una serie absolutamente sumable; R163_802 ya considera normalizaciones con valor1 en s=1. No se invocan otros argumentos de esa fuente. La nueva comprobación aquí conserva además ALL-POWERS y ell>=0 en factores locales concretos y transfiere el MISMO testigo negativo.

### 11.1. Factores locales positivos que aumentan el residuo

Mantener en2 el factor de la sección9, cuyo cociente respecto del ordinario es1-z/2+z^2/2 y cuyo residuo relativo es7/8. En un primo p>=7 permitir un parámetro racional0<=delta_p<=2/5 y reemplazar el factor ordinario por

    F_(p,delta)(z)=[1+delta z-delta z^2]/(1-z).

Entonces N(p)=1+delta y N(p^k)=1 para TODOS k>=2. Por tanto esta modificación no altera ALL-POWERS.

También conserva positividad de TODOS los coeficientes logarítmicos. Para delta>0 escribir

    1+delta z-delta z^2=(1-rz)(1+sz),
    s-r=delta, rs=delta, 0<r<s<1.

La última desigualdad se obtiene del polinomio s^2-delta s-delta: es negativo en0 y positivo en1, porque1-2delta>=1/5. Para delta=0 se interpreta r=s=0. La expansión formal de los logaritmos da

    ell(p^k)/log p=1-r^k+s^k,       k impar,
    ell(p^k)/log p=1-r^k-s^k,       k par.

El valor impar es positivo. Si k>=2 es par,

    r^k+s^k<=r^2+s^2=delta^2+2delta<=24/25,

de modo que el valor par es al menos1/25. En los primos no modificados se mantiene Lambda; en2 la positividad ya está probada en la sección9.

El factor relativo de residuo es exactamente

    1+delta a_p, a_p=(p-1)/p^2>0.

### 11.2. Elección finita y racional que compensa exactamente7/8

Se tiene sum_(p>=7) a_p=infinito. Para recordar una prueba elemental, si sum_p1/p convergiese, los productos finitos prod_(p<=X)(1-1/p)^(-1) estarían uniformemente acotados, usando -log(1-1/p)<=2/p. Pero cada producto contiene en su expansión positiva todos los términos1/n con n<=X, contradiciendo la divergencia armónica. Restar la serie convergente sum_p1/p^2 no altera la divergencia. Así diverge la suma de a_p.

Los productos finitos prod_(p>=7)(1+(2/5)a_p) son entonces no acotados: log(1+(2/5)a_p)>=a_p/5, pues(2/5)a_p<1 y log(1+u)>=u/(1+u). Enumerar los primos>=7 como p1,p2,... y elegir el primer j cuyo producto con todos los deltas iguales a2/5 alcanza o supera8/7. Si B es el producto de los j-1 factores anteriores, fijar

    delta_(p_i)=2/5 para i<j,
    delta_(p_j)=[8/(7B)-1]/a_(p_j),
    delta_p=0 en los demás primos>=7.

Por minimalidad,0<delta_(p_j)<=2/5. Todos los parámetros son racionales y

    prod_(p>=7)(1+delta_p a_p)=8/7 EXACTAMENTE.

Es una elección existencial finita determinada por desigualdades exactas; no se listan primos, no se ejecuta su búsqueda y no hay campaña numérica.

### 11.3. Propiedades simultáneas y negatividad sin cambios en la ventana

El producto resultante es

    F_norm(s)=zeta(s)R(s),
    R(s)=[1-2^(-s)/2+2^(-2s)/2]
          *prod_(p>=7)[1+delta_p p^(-s)-delta_p p^(-2s)].

R es un polinomio de Dirichlet FINITO con coeficientes racionales y R(1)=(7/8)(8/7)=1. Así F_norm tiene polo simple en1 de residuo EXACTAMENTE1. Sus coeficientes N son multiplicativos y no negativos; todas las potencias locales de nivel k>=2 siguen teniendo coeficiente1. Por tanto

    N(n^m)=1 para TODOS n>=1,m>=2 simultáneamente,
    ell>=0, con soporte en poderes primos,
    0<=N(n)<=C, C=prod_(p>=7)(1+delta_p)<infinito.

No se afirma N<=1: alguno de los primos altos tiene N(p)>1, y N(2)=1/2 sigue siendo no entero. Esta es la diferencia exacta que evita el colapso del ansatz de la sección7 y la identificación integral de la sección10.

Escribir R(s)=sum_d a_d d^(-s), suma finita. Por multiplicar las series y sumar coeficientes,

    sum_(n<=x)N(n)=sum_d a_d floor(x/d)
                   =x sum_d a_d/d+O(sum_d|a_d|)
                   =x+O(1).

Es precisamente el argumento del lemaS de R163_102; no se reivindica novedad para esa identidad de conteo. N es aquí un conteo ponderado no entero, no una multiset de enteros con multiplicidades integrales.

Todos los primos compensadores son>=7, y sus potencias también quedan fuera de la ventana T0 de007_C. Por tanto los contactos de F_norm en esa ventana son EXACTAMENTE los de F_all de la sección9. Con el mismo F primitivo,

    a_(T0)^(ell_norm)(F)=a_(T0)^(ell_all)(F)
                         <-0.00528||F||^2<0.

No se evalúa un contacto adicional, no se reajusta el testigo y no se repite la cuadratura. Como antes, la extensión por cero conserva esta negatividad en todas las ventanas mayores.

### 11.4. Alcance y distinción de los antecedentes197

El ejemplo prueba que residuo1, polo simple, conteo x+O(1), N multiplicativa no negativa y acotada, ALL-POWERS y ell>=0 no bastan para el signo de la forma de fondo fijo si no se añade integridad, N<=1 u otra compatibilidad que lo excluya. No se le atribuye la ecuación funcional del miembro original ni un defecto funcional pequeño.

El enunciado de phase197 sobre ausencia de compensación de cola corresponde al defecto de Bohr Delta, cuyos factores son>=1. Aquí se compensa ÚNICAMENTE el residuo; no se afirma compensación ni control de aquel defecto. Los factores locales relativos aquí son polinomios1+delta z-delta z^2; no se identifica esta construcción con los factores geométricos específicos de197. No hay contradicción con esos resultados ni se deduce un NO-GO sobre clases que exijan sus hipótesis adicionales. La conclusión sigue limitada a las hipótesis escritas y no afecta al signo del dato original.
