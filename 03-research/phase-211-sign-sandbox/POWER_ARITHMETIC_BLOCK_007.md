# POWER_ARITHMETIC_BLOCK_007 — Signo en todo el bloque Laguerre de dimensión doce

Estado: PROVED, certificado racional exacto ejecutado y revisado independientemente en POWER_BLOCK_AUDIT_007.md. Papers intactos.

## Diferencia respecto de antecedentes

Se consultan las reglas del proyecto y los antecedentes índice/grid/crucigrama registrados en POWER_BRIDGE_002, así como la familia semilocal/exterior. No se propone como nueva la reducción semilocal. El objeto nuevo es un bloque EXPLÍCITO completo de dimensión doce, con todos sus términos cruzados: POWER_ARITHMETIC_WITNESS_006 solo decidía un vector. Ese vector prueba que ARCH+POLAR es indefinida aquí. Por tanto la positividad de todo este bloque necesita una compensación aritmética real, y no sigue de las regiones anteriores ARCH o ARCH+POLAR positivas.

## 1. Teorema finito

Sea u=63/2 y V12=span{sqrt(63)e^-uy L_j(63y)1_(y>0):0≤j≤11}. Entonces

    W[h] > (1/10000)||h||² para todo h real no nulo en V12.

No se prueba todos los órdenes ni todos los conjuntos de tasas. Las imágenes exteriores correspondientes son las combinaciones de potencias y sus primeras once derivadas en el exponente a=32. El test negativo de ARCH+POLAR de WITNESS006 pertenece a V12, por lo que el teorema atraviesa realmente esa región indefinida.

## 2. Matrices Toeplitz exactas

La base es ortonormal y todas las piezas son Toeplitz. La banda arquimediana diagonal es d=psi16−log pi. Para k>=1,

    b_k=(1/2)Σ(r=1..k)binom(k−1,r−1)u^r psi^(r)(16)/r!.

La banda polar es

    p_k=(63/992)(−1)^k[(32/31)^k+(31/32)^k].

Ponga q_k(x)=L_k(x)−L_(k−1)(x), L_-1=0. La banda del contacto n es

    a_0(n)=−2Lambda(n)n^-32,
    a_k(n)=−Lambda(n)n^-32 q_k(63log n), k>=1.

El factor dos distinto en diagonal es esencial: la autocorrelación tiene una sola suma triangular, mientras la matriz simétrica cuenta dos veces sus términos extradiagonales. Ninguna pieza individual del peine se presume positiva como matriz.

## 3. Certificado exacto de ARCH+POLAR+contacto 2

El verificador adjunto usa solamente Fraction, factoriales y coeficientes binomiales. Para las sumas S_p=Σ(m>=16)m^-p, p2..12, usa m16..255 y las cotas de Euler con resto de signo

    T_p(M)=M^(1−p)/(p−1)+(1/2)M^-p+(p/12)M^(-p−1),
    T_p(M)−p(p+1)(p+2)M^(-p−3)/720
      <Σ(m>=M)m^-p<T_p(M), M=256.

Este es el lema estándar de Euler–Maclaurin para potencias positivas, con resto alternante; se puede obtener también integrando la expansión de coth con resto de signo. Para gamma se usa

    g0=H256−log256−1/(2·256)+1/(12·256²)−1/(120·256⁴),
    g0<gamma<g0+1/(252·256⁶).

Log2 y log pi se encierran con series geométricas integradas; pi mediante la identidad exacta 16atan(1/5)−4atan(1/239) y series alternantes con treinta términos. Los signos y restos están explícitos en el script. Así se obtienen intervalos racionales de todas las bandas, incluido q_k(63log2), sin evaluación flotante.

Cada banda se reemplaza temporalmente por su punto medio redondeado hacia abajo a denominador 10^12. La máxima suma absoluta de fila del error es <10^-8. El LDL de la matriz central racional menos (1/1250)I tiene TODOS sus doce pivotes positivos. En consecuencia

    ARCH+POLAR+contacto2 > (1/1250−10^-8)I.                (B12)

La aritmética exacta de esta afirmación está enteramente reproducida por `tools/power_arithmetic_block_007_verify.py`.

## 4. Cola de todos los contactos n>=3 en norma de operador

El majorante por coeficientes absolutos de q_k(x) en potencias de x pierde demasiado. Se conserva su cancelación expandiendo en x−40:

    q_k(x)=Σ(j=0..k) a_kj (x−40)^j.

El script verifica exactamente que (−1)^k a_kj>=0 para todos k≤11,j≤k. Como 63log n>42, resulta

    |q_k(63log n)|=Σ_j |a_kj|(63log n−40)^j.

Para cada j≤11, f_j(x)=log x(63log x−40)^j x^-32 decrece en x≥3: su derivada logarítmica con respecto a t=log x es 1/t+63j/(63t−40)−32<1+693/23−32<0. Por comparación suma-integral y 1<log3<11/10=a,

    Σ(n>=3)f_j(n) ≤3^-32 a(63a−40)^j
       +3^-31 Σ(r=0..j+1) R_jr(a) r!/31^(r+1),

donde R_jr(a) es el coeficiente de z^r en (a+z)[63(a+z)−40]^j. Todos son no negativos y aumentan con a>40/63; por ello reemplazar log3 por a conserva la cota. Esta fórmula integra exactamente el polinomio trasladado, sin introducir valores de otros primos.

Multiplicando por |a_kj|, usando Lambda(n)≤log n y el factor dos diagonal, se obtienen majorantes racionales t_k para la suma de los valores absolutos de cada banda de cola. El verificador prueba

    max_i Σ(j=0..11)t_|i−j| <3/5000.

Por el criterio de Schur simétrico, la norma de TODA la cola es <3/5000. No se presume que sea positiva; se resta su norma de B12. Finalmente

    W > [1/1250−10^-8−3/5000]I > (1/10000)I.

## 5. Límites y siguiente requisito

El resultado controla todos los vectores y todos los contactos sobre V12, y usa decisivamente el contacto 2. No se afirma que ese contacto aislado tenga signo matricial positivo, ni que este margen se mantenga al añadir más modos. El paso a dimensión trece o más requiere nuevos certificados o un principio uniforme; aquí queda abierto. El puente POWER_BRIDGE_002 identifica por qué una regla para todos los grados sí tendría alcance sobre todos los tests, pero no sustituye esa regla.
