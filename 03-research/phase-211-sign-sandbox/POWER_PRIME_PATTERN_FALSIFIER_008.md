# POWER_PRIME_PATTERN_FALSIFIER_008 — En la misma familia, los contactos bajos también pueden agravar el déficit

Estado: PROVED (vector explícito, polar nulo, déficit arquimediano y signo perjudicial de cada contacto <=1024). No se afirma negatividad de la forma completa. Papers intactos.

## 1. Antecedentes y diferencia declarada

Leídos POWER_POLYNOMIAL_003, POWER_ARITHMETIC_WITNESS_006, POWER_POLE_MOVEMENT_004 y Paper47, teorema de sub-comb negativity (§Partial prime combs); búsquedas de Laguerre, Levinson, finite differences y Toeplitz prime en índice, grid y crucigrama. La necesidad de la aritmética y el fracaso de monotonía por añadir contactos ya constan. No se propone un NO-GO global nuevo. La diferencia exacta es un test cerrado en la MISMA familia confluente fija usada por los certificados: en 006 todos los contactos ayudan y el 2 repara; aquí TODOS los contactos hasta 1024 perjudican una dirección con polar exactamente cero y parte arquimediana negativa. No se hace búsqueda de matrices ni campaña numérica.

## 2. Vector racional explícito en el espacio confluente

Fije u=63/2, n=2^17 y

    g(y)=y^{n-1}exp(-uy)1_{y>0},
    f(y)=(d²/dy²-1/4)g(y).

Como n>3, g(0)=g'(0)=0 y las integraciones por partes no tienen términos de borde. Tanto g como todas las derivadas necesarias decaen exponencialmente en infinito. La transformada de Laplace es

    F(s)=(n-1)!(s²-1/4)/(s+u)^n.

Es un numerador racional FIJO de grado dos en el espacio confluente de n polos u, por lo que f pertenece al span de las primeras n funciones Laguerre e^-uy L_j(2uy). No es necesario imprimir n coeficientes: la fórmula diferencial los determina exactamente.

Los momentos polares son exactamente

    A(f)=F(-1/2)=0, B(f)=F(1/2)=0.

Así el polar se anula. La densidad espectral normalizada es proporcional a

    (tau²+1/4)²/(u²+tau²)^n.                              (S)

## 3. Cota racional del segundo momento espectral

Use primero la probabilidad base proporcional a (u²+tau²)^-n. Si M_{2k} es su momento, integración por partes o la integral beta dan

    M2=u²/(2n-3),
    M4=3u^4/[(2n-3)(2n-5)],
    M6=15u^6/[(2n-3)(2n-5)(2n-7)].

Para n=2^17, u²<1024 y cada denominador de los tres productos es mayor que n. Por tanto

    M2<1/128, M4<3/128², M6<15/128³.

Al ponderar por (tau²+1/4)², el segundo momento de (S) es

    E_f tau²=[M6+(1/2)M4+(1/16)M2]
                  /[M4+(1/2)M2+1/16]
             <=16M6+8M4+M2
             <1231/131072<1/100.                         (M)

Todas las comparaciones son racionales; no se estiman factoriales grandes.

## 4. Déficit arquimediano estricto

La serie positiva del multiplicador da, para a_k=k+1/4,

    m(tau)-m(0)
      =Σ [(tau²/4)/(a_k(a_k²+tau²/4))]
      <=(tau²/4)Σ a_k^-3 <17tau².

La última cota usa Σ_{k>=1}(k+1/4)^-3<=104/125, sumando el primer término y comparando con una integral; el término k=0 aporta 64. Además m(0)=-gamma-pi/2-3log2-logpi<-4 (de hecho <-9/2), usando gamma>0, pi>3, log2>2/3 y logpi>1. Por (M),

    Arch[f]/||f||² <-4+17/100=-383/100.

El polar es cero, así que Arch+Polar es estrictamente negativa en este test, sin ningún diagnóstico numérico.

## 5. TODOS los contactos bajos perjudican el signo

Por cos x>=1-x²/2 y Parseval,

    c_f(t)/||f||²=E_f cos(tau t)
                 >=1-(t²/2)E_f tau² >1-t²/200.

Para cada entero q con 2<=q<=1024, logq<=10log2<10. Luego

    c_f(logq)>||f||²/2.

Cada contacto primo-potencia no nulo de ese intervalo aporta

    -2Lambda(q)q^-1/2 c_f(logq)
       <-Lambda(q)q^-1/2 ||f||² <0.

En particular añadir el contacto 2 agrava el déficit; añadir el 3 también lo agrava; y lo mismo sucede con todas las potencias primas hasta 1024. Es el comportamiento opuesto al vector de dimensión doce de POWER_ARITHMETIC_WITNESS_006, donde todos ayudan. El patrón depende de la autocorrelación del vector, no de una sucesión universal de primos reparadores.

## 6. Desigualdad aritmética concreta que exige este test

La serie completa del peine converge absolutamente, pues c_f(t) es exponencial e^-ut por un polinomio finito. Si la forma completa es no negativa sobre este test, necesariamente el segmento q>1024 satisface

    -Σ_{q>1024}2Lambda(q)q^-1/2 c_f(logq)/||f||²
       >383/100 + Σ_{2<=q<=1024}Lambda(q)q^-1/2.           (TAIL)

Esta es una obligación explícita sobre la cola del MISMO vector: el segmento bajo no puede producir su reparación. No se usa (TAIL) como prueba de su propio signo, ni se afirma haberla demostrado aquí. La propiedad aritmética necesaria debe conservar la suma con autocorrelaciones de ambos signos; las contribuciones favorables de un vector concreto no se transfieren a todo el subespacio.

No se afirma W[f]<0: precisamente la cola q>1024 permanece sin evaluar. El resultado no refuta ningún certificado completo del paper ni de esta fase; refuta sólo el patrón universal «los contactos bajos siempre reparan las direcciones arch+polar negativas» dentro de la familia confluente fija.
