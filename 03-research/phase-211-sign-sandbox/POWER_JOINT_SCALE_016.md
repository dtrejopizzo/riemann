# POWER_JOINT_SCALE_016 — Escala conjunta de dimensión y orden highpass

Estado: PROVED fórmulas beta, límite de paquete lineal, momentos temporales y obstrucciones a uniformizar los pesos. OPEN un cono de positividad de la forma completa. Sin campañas numéricas. Papers intactos.

## Antecedentes y razón nueva, registrados antes de construir

Leídos las reglas del proyecto, HIGHPASS015 y auditoría, GEOMETRIC_TRANSFER015, CONFLUENT_BRIDGE014; búsqueda conjunta en índice ROUTES-TRIED-INDEX, grid parte3 y CROSSWORD-TO-D (Jacobi/resolvente/escala conjunta/highpass). La coercividad de alta frecuencia y los límites de bloques prolates ya están registrados. La diferencia aquí es cuantificar la dependencia en N de la órbita racional exacta Q^kV_N, especialmente para P=1 y P=s^(N−1), no inferir una cola prolate ni positividad general desde un índice alto.

Se investiga por separado: (i) escala espectral real, (ii) uniformidad de los pesos temporales usados para sumar el peine, (iii) signo completo. Un falsificador de (ii) no será presentado como falsificador de (iii).

## 1. Extremo P=1: ley beta EXACTA para todo N,k

Sea u=63/2 y f_(N,k) de transformada F(s)=s^k/(s+u)^(N+k), N>=1,k>=0. Su densidad espectral normalizada es proporcional a tau^(2k)/(u²+tau²)^(N+k). Al cambiar

    Z=tau²/(u²+tau²),

se obtiene EXACTAMENTE

    Z~Beta(k+1/2,N−1/2),
    ||f_(N,k)||²=u^(1−2N)B(k+1/2,N−1/2)/(2pi).          (BETA)

El signo de tau es simétrico e independiente de Z. Para N>3/2,

    E tau²=u²(k+1/2)/(N−3/2).

Así la escala típica es u sqrt(k/N), no sqrt(k) con una constante independiente de N. La constante oculta en el teorema015 importa realmente al variar la dimensión.

## 2. Paquete en el cono LINEAL: los contactos no desaparecen

Suponga N->infinito y k/N->c, 0<c<infinito. La media y varianza beta son

    E Z=(k+1/2)/(k+N),
    Var Z=(k+1/2)(N−1/2)/[(k+N)²(k+N+1)].

Por Chebyshev, Z converge en probabilidad a c/(1+c). En consecuencia |tau| converge en probabilidad a u sqrt(c). Para todo t real fijo,

    c_f(N,k)(t)/||f_(N,k)||² ->cos(u sqrt(c)t).           (PACKET)

No se usa un teorema central del límite: la función cos es acotada y basta la concentración beta. La energía arquimediana normalizada converge a m(u sqrt(c)); la uniformidad integrable requerida se sigue de la cota uniforme de E tau², pues m tiene crecimiento logarítmico.

Este resultado falsifica la extrapolación «desaparición uniforme de cada contacto en todo cono k>=C N». Para cualquier C, elija un entero m suficientemente grande y c=[2pi m/(u log2)]²>=C; tome k=ceil(cN). Entonces

    c_f(N,k)(log2)/||f_(N,k)||² ->1.

El contacto 2 permanece y no tiende a cero. No se afirma que la forma completa sea negativa en esta sucesión: su suma infinita no se puede intercambiar con PACKET usando las cotas015, precisamente porque falla su uniformidad. El cono lineal queda sin prueba de signo, no refutado como enunciado de signo.

## 3. Otro extremo: P=s^(N−1) elimina la dificultad dimensional

Para ese numerador,

    Q(s)^k P(s)/(s+u)^N
      =s^(k+N−1)/(s+u)^(k+N)
      =Q(s)^(k+N−1)/(s+u).

Es EXACTAMENTE la órbita de dimensión inicial uno y orden k+N−1. Por HIGHPASS015 su forma normalizada crece como

    (1/2)log(k+N−1)+log[u/(2pi)]−(1/2)psi(1/2)+o(1),

y el peine y el polar normalizados desaparecen cuando k+N crece. Su ley beta es Beta(k+N−1/2,1/2). Este comportamiento es distinto del de P=1, aunque ambos numeradores pertenezcan al mismo espacio inicial. Un análisis de un único extremo no uniformiza todo el bloque.

## 4. La matriz Gram beta completa explica la dependencia en N

Para un numerador real P(s)=Σa_j s^j, la norma es una forma Gram cuyas entradas se calculan por beta. Las entradas con i+j impar se anulan por simetría; si i+j=2r,

    (1/2pi)∫tau^(2k)(i tau)^j conjugate[(i tau)^i]
                         /(u²+tau²)^(N+k)d tau
      =(−1)^(r+i) u^(1−2N+2r)
           B(k+r+1/2,N−r−1/2)/(2pi).                   (GRAM)

Aquí 0<=i,j<N, por lo que el segundo parámetro beta es positivo. GRAM es una fórmula de TODO el bloque, no solo de sus diagonales. El menor parámetro puede ser1/2 o puede crecer como N: esto contiene simultáneamente los dos regímenes extremos anteriores y no proporciona por sí solo un condicionamiento uniforme en N.

El cambio Z de§1 separa también los dos sectores reales. Escribiendo P(i tau)=E(tau²)+i tau O(tau²), se elimina el término cruzado. Si d es el grado máximo permitido por N en el sector (rellenando coeficientes nulos cuando sea necesario), poner R(Z)=(1−Z)^d E(u²Z/(1−Z)) (análogamente para O) convierte el sector en una Gram de polinomios de grado<=d para un peso Jacobi Z^alpha(1−Z)^beta. Los parámetros son alpha=k−1/2,beta=±1/2 en el sector par, y alpha=k+1/2,beta=±1/2 en el impar. Es una coordenatización exacta para estudiar la escala conjunta; no se atribuye signo de W a la positividad de esta Gram de normas.

## 5. Media temporal EXACTA independiente de k

Para P=1, la probabilidad temporal es |f_(N,k)(y)|²dy/||f_(N,k)||², y>=0. Su media es

    mu_(N,k)=E y=(N−1/2)/u.                              (MEAN)

Prueba por Parseval. Para tau!=0, la derivada de la fase de F(i tau) es −(N+k)u/(u²+tau²); la fase k arg(i tau) es constante en cada semirrecta. Si k>=1, el posible salto en tau=0 se multiplica por F(0)=0; k=0 no tiene ese término. Por tanto

    E y=(N+k)u E[1/(u²+tau²)]
       =(N+k)/u E(1−Z)=(N−1/2)/u.

Las funciones racionales decaen exponencialmente por polinomio, de modo que Parseval para la derivada y los momentos temporales es legítimo incluso si hay salto de la extensión en y=0: se deriva en FRECUENCIA para multiplicar por y, no en tiempo a través de ese borde.

Para cualquier eta>0 con eta<u, Jensen demuestra entonces

    ||e^(eta y)f_(N,k)||²/||f_(N,k)||²
       >=exp[2eta(N−1/2)/u], para TODO k.                (WEIGHT)

Así una constante ponderada uniforme en N es imposible incluso sobre k>=C N², k>=exp(N), o cualquier cono que permita N crecer: WEIGHT es independiente de k. No se refuta EVENTUAL015, cuya constante sí depende de N.

## 6. Centrar elimina la media, pero no la dispersión temporal

Para k>=1, otro cálculo de Parseval da

    E y²=(N−1/2)/u² [N−k+k²/(k−1/2)],
    Var y=(N−1/2)/u² [1+1/(4(k−1/2))].                 (VAR)

En efecto, |F'|²/|F|²=k²/tau²+(N²−k²)/(u²+tau²). Bajo BETA,

    E tau^-2=(N−1/2)/[u²(k−1/2)],
    E(u²+tau²)^-1=(N−1/2)/[u²(N+k)],

lo que produce las dos igualdades. Para k=0 se obtiene directamente la distribución gamma temporal y Var y=(N−1/2)/(2u²), consistente con la extensión algebraica de VAR.

Sea X=y−mu. Como cosh z>=1+z²/2,

    E e^(2eta X)+E e^(-2eta X)>=2+4eta²Var y.

Cada esperanza es >=1 por Jensen. Al menos una crece linealmente en N para k>=1. Incluso el producto de ambas crece al menos como1+2eta²Var y. Por consiguiente no existe una cota uniforme simultánea para los DOS pesos exponenciales centrados de amplitud eta fija, ni para el producto de normas usado en la correspondiente cota bilateral de correlaciones.

Esto no descarta pesos centrados con eta dependiente de N ni un análisis que use cancelación en vez de valores absolutos. Distingue un desplazamiento de una dispersión: centrar solo elimina el primero.

## 7. Consecuencia para el defecto complementario y estado del cono

Las mezclas geométricas015 conservan energías completas con pesos positivos e incorporan las normas de Q^k f. EVENTUAL015 controla la cola cuando N es fijo. PACKET refuta la desaparición uniforme de los contactos en el cono lineal; WEIGHT refuta una cota exponencial ponderada uniforme en N en cualquier cono. El comportamiento espectral del cono cuadrático queda abierto aquí.

El segmento complementario que queda antes del umbral efectivo K_N conserva una obligación de signo. Ni la identidad de mezcla ni GRAM ni la positividad eventual a N fijo lo controlan. La ruta apropiada debe cuantificar ese segmento o aportar una desigualdad aritmética para los regímenes de paquete, conservando la suma firmada completa.

**OPEN:** existencia de C tal que W>=0 para todos los numeradores y k>=C N, o k>=C N². No se produjo contraejemplo a esas dos afirmaciones de signo. **FALSIFIED:** su justificación mediante desaparición uniforme de cada contacto en el cono lineal, o mediante una constante exponencial ponderada uniforme en N en cualquier cono de k. La concentración/dispersión en el cono cuadrático requiere un análisis adicional; aquí no se la presenta como teorema ni como negativo de W.
