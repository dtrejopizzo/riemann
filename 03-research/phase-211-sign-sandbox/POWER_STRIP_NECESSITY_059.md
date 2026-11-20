# POWER_STRIP_NECESSITY_059 — Un bound de contorno uniforme requiere al menos escala cuadrática

Estado: **PROVED**, prueba exacta propuesta y revisada por root, desarrollada aquí por el auditor; revisión adicional de casos APROBADA sin cambios. Sólo obstrucción a una clase declarada de bounds de contorno. No es un contraejemplo a W ni al signo de un cono. Papers intactos.

## Antecedentes y diferencia

Consultados las reglas del proyecto, índice ROUTES-TRIED-INDEX, grid maestro y CROSSWORD-TO-D; releídos JOINT_SCALE016, QUADRATIC017, QUADRATIC_EXPLICIT017, INVERSE_COEFFICIENT054 y EFFECTIVE_HIGHPASS054. PACKET016 trata j/n tendiendo a una constante: una autocorrelación no desaparece en todo cono lineal. Aquí se utiliza la MISMA densidad aritmética admisible con P=1 y se demuestra una obstrucción cuantitativa en TODA sucesión n<=j=o(n²), incluso cuando su frecuencia central diverge. No se extrapola el límite lineal a frecuencias crecientes sin controlar su varianza.

## Clase de estimaciones

Fije u>0 y0<eta<u. Para el átomo real causal

    F_(n,j)(s)=s^j/(s+u)^(n+j),
    rho_(n,j)(z)=z^(2j)/(u²+z²)^(n+j),

considere la estimación, con D finita independiente de n,j,

    ∫_R |rho_(n,j)(x+i eta)|dx <=D∫_R rho_(n,j)(x)dx.  (STRIP)

No puede valer simultáneamente a lo largo de ninguna sucesión n→infinito, n<=j=o(n²). En particular, para ningún C>0 y p<2 puede valer sobre TODOS los enteros n,j con j>=C n^p. La conclusión sigue siendo cierta si STRIP se pide para todos los numeradores de V_n, pues P=1 es uno de ellos.

## Varianza exacta del paquete

Normalice rho sobre la recta como una probabilidad espectral y escriba Z=|tau|. La ley beta-prima, obtenida directamente por tau²/u², tiene parámetros alpha=j+1/2 y beta=n−1/2. Para n>=3,

    E Z² =u²(j+1/2)/(n−3/2),
    mu=E Z
       =u Γ(alpha+1/2)/Γ(alpha) ·Γ(beta−1/2)/Γ(beta).

Las desigualdades elementales gamma dan

    Γ(alpha+1/2)/Γ(alpha)>=sqrt(alpha−1/2)=sqrt j,
    Γ(beta−1/2)/Γ(beta)>=1/sqrt(beta−1/2)=1/sqrt(n−1).

La primera se obtiene por Cauchy como en EFFECTIVE054§2. Para la segunda, aplicar Jensen a sqrt(X) con X de ley Gamma(beta−1/2): Γ(beta)/Γ(beta−1/2)=E sqrt(X)<=sqrt(beta−1/2). Por tanto mu>=u sqrt(j/(n−1))>=u cuando j>=n. Restar el cuadrado de este lower a E Z² prueba

    Var Z <= u²{j/[2(n−3/2)(n−1)] +1/[2(n−3/2)]}.     (VAR)

La cota tiende a cero bajo n<=j=o(n²). No se aproxima la fase mediante una frecuencia central determinista insuficientemente precisa: se utiliza la media real mu de cada paquete.

## Correlaciones que contradicen STRIP

Para T>0 fijo, elija

    t_n=2pi ceil(T mu/(2pi))/mu.

Se tiene T<=t_n<=T+2pi/u y t_n mu es múltiplo de2pi. La densidad espectral es par, así que la autocorrelación normalizada real satisface

    c_(n,j)(t_n)/||f_(n,j)||²
      =E cos(t_n tau)=E cos(t_n Z)
      >=1−(t_n²/2)Var Z ->1.                           (PACKET)

Por otro lado, la densidad racional es analítica en la franja de altura eta y decae al menos como|z|^−2. Desplazar el contorno en su transformada Fourier y usar STRIP implica

    |c_(n,j)(t)|/||f_(n,j)||² <=D exp(−eta t), t>=0.

Tomar T suficientemente grande para que D exp(−eta T)<1/2 contradice PACKET. Todas las funciones usadas son los átomos originales reales; no se cambia el símbolo, el peine, el polar o la forma W.

Finalmente, para p<2 tome j_n=max{n,ceil(C n^p)}. Entonces j_n>=C n^p, j_n>=n y j_n=o(n²); por lo anterior no puede existir D uniforme en ese cono.

## Alcance

El resultado exige p>=2 sólo como condición NECESARIA para esta estrategia de contorno con eta y D fijos. No demuestra su suficiencia para todos los numeradores, ni refuta un bound con D dependiente de n, ni descarta un cono de signo W con p<2. No prueba una obstrucción p>=3 mediante argumentos heurísticos de Hermite. Los resultados017 de contorno escalar a escala cuadrática y054 con constante creciente en n permanecen intactos. No hay barrido numérico ni nuevo certificado de dimensión aislada.
