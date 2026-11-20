# Mayorante unilateral para la paridad de Möbius y su primer fallo

Para un extremo N grande fijar κ>0 y δ=2 asinh(κ/(2√N)). Sea Wδ(v)=max(1−|v|/δ,0). Para n no libre de cuadrados poner Q(n)=0. Para n libre de cuadrados definir

    Q(n)=2^(−ω(n)) Σ_(d,e|n) μ(d)μ(e) Wδ(log(de/n)).

Para cada κ≤√3 se tiene Q(n)≥μ(n) para todo n≤N y

    Σ_(n≤N) |Q(n)−μ(n)| ≪ √N/log log N.

Para κ≤1 hay igualdad exacta. En cambio para cada √3<κ<2 hay infinitos N para los que Q(N)<μ(N). Así se localiza la primera pérdida de la mayoración puntual. La suma que define Q utiliza parejas de divisores y la condición de que n sea libre de cuadrados; no necesita multiplicar por el signo desconocido del entero completo.

**Complementar y cancelar.** En n libre de cuadrados cambiar e por n/e: μ(n/e)=μ(n)μ(e). En la suma resultante con Wδ(log(d/e)), la diagonal d=e aporta μ(n). Para un término fuera de ella escribir a=d/mcd(d,e), b=e/mcd(d,e), y m=n/(ab). Los tres factores a,b,m son coprimos dos a dos. Para cada par ordenado reducido hay 2^ω(m) elecciones del factor común, y μ(n)μ(d)μ(e)=μ(m). Así la corrección es exactamente la suma, sobre pares ordenados a≠b con ab|n y (a,b)=1, de

    μ(m) 2^(−ω(ab)) Wδ(log(a/b)).

Si a<b y h=b−a, el término es distinto de cero sólo si

    h√m = 2√n sinh(log(b/a)/2) < κ√(n/N) ≤ κ.

Para κ≤√3, sólo puede ser h=1 con m=1 ó 2. El caso m=2 exigiría que dos consecutivos fuesen ambos impares porque (ab,m)=1. Queda m=1, con signo positivo. Para κ≤1 ni siquiera esta posibilidad sobrevive. Esto controla el signo antes de promediar.

**Precio total.** Las únicas correcciones positivas aparecen en n=a(a+1) y cuestan como máximo 2·2^(−ω(a(a+1))) por n. Para a≤√N mayorar el peso usando sólo primos p≤z, z=c log N. En cada primo hay dos residuos distintos con p|a(a+1), por lo que el promedio de ese peso truncado en un período primorial es exactamente ∏_(p≤z)(1−1/p). Éste es ≪1/log z, pues su inverso incluye la suma armónica hasta z. Por Chebyshev el período es ≤N^(1/4) si c es bastante pequeño. Contar períodos completos y el resto prueba el coste anunciado uniforme también para cualquier subintervalo.

**Primer contraejemplo.** Tomar a≡1 mod 3 y a,a+1 ambos libres de cuadrados. El conjunto de tales a tiene densidad positiva: truncar los primos en z, usar el teorema chino, y acotar la densidad superior de la cola por 2Σ_(p>z)p^(−2), contando además O(√T) términos de redondeo hasta T. Para N=n=3a(a+1) el par (a,a+1) con m=3 está activo para a grande y todo κ>√3, por la identidad anterior. Si κ<2 todos los pares activos tienen h=1 y m=1,2,3. El caso 2 sigue excluido. El 1 exigiría 3a(a+1)=s(s+1), que implica s=√3 a+(√3−1)/2+O(1/a). Por equidistribución de los múltiplos del irracional √3, estos a tienen densidad cero (acotar primero por un entorno fijo y después reducirlo). En los demás sólo quedan términos negativos, por lo que falla la mayoración.

**Uso y alcance.** Para las subidas de 287 se puede sustituir μ por Q a la escala N del extremo derecho y el error en cualquier subintervalo cabe en el presupuesto. Equivalentemente Q es el promedio del cuadrado ordinario de Σ_(d|n)μ(d)exp(it log(d/√n)), normalizado por 2^ω(n), contra la densidad positiva cuya función característica es Wδ. El cuadrado ordinario puede ser negativo: no se está promediando un módulo cuadrado. El emparejamiento deja un mayorante explícito y una frontera exacta para su signo; falta una cota superior de raíz para las sumas de Q. La bilineal de 281–283 y la obstrucción de criba de 043 no evalúan esta primera colisión en la pareja de divisores complementarios.
