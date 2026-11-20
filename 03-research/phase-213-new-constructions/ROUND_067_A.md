# El sector completo de semiprimos excede la escala raíz tras cualquier número finito de diferencias

Usamos los representantes S_h de 062, con h≥0 fijo. Se incluyen todos los productos reducidos y todas las potencias en sus máscaras, sin corte en pq. Sea E_{d,h}(x) la contribución de los productos con exactamente d primos distintos, d≥1 fijo, con las 2^d pendientes por producto. Entonces para todo θ<1
     
    limsup_{j→∞} (−1)^d E_{d,h}(j⁴)/(j⁴)^θ = +∞.

En particular el exceso positivo de los semiprimos (d=2) persiste al completar la suma para estos representantes. Para d=1 se obtiene un exceso negativo. La prueba de 066 con un prefijo del promedio infinito no daba este enunciado. Aquí h es finito, condición esencial en la demostración.

**Transformada.** Escribir M_G(u)=∫G(z)z^(−u)dz/z y a_p(s)=p^(−s)/(1+p^(−2s)). Para s real >1, la integral de E_{d,h}(x) x^(−s) dx/x sobre (0,∞) vale
    
    2^(d+1) (−1)^d (4−4^s)^h M_G(2s) e_d((a_p(s))_p),

donde e_d suma los productos de d entradas con índices distintos sin orden. En efecto, para cada r y cada n de la máscara, sustituir x=r n² z² en la integral. Las potencias de cada primo dan la serie alternada en p^(−2s); el signo μ(r)=(−1)^d y el número de pendientes son constantes. El intercambio absoluto se obtiene reemplazando los denominadores por 1−p^(−2s) y usando Σp^(−s)<∞. G_h se anula cerca de cero y decrece rápidamente en infinito.

**Singularidad real.** Poner t=s−1 y ℓ=log(1/t). La primera suma de potencias de las entradas a_p es ℓ más una función analítica en t=0: restar log ζ(s), usando el producto de Euler; la diferencia converge localmente de forma normal cerca de 1 y tζ(1+t) es analítica y vale 1 en cero. Las sumas de potencias de órdenes ≥2 son analíticas allí. Por las identidades de Newton, e_d es un polinomio en ℓ con coeficientes analíticos y término superior ℓ^d/d!. Por 062, M_G(2)>0. Al tomar (−1)^h veces la derivada de orden h de la transformada de (−1)^d E_{d,h}, el término principal es

    [2^(d+1) (4 log 4)^h M_G(2) h!/d!] ℓ^d.

En efecto (4−4^(1+t))^h=(−4 log 4)^h t^h+O(t^(h+1)). Cada derivada que cae sobre ℓ en lugar de t^h pierde al menos un grado logarítmico. El resto es O(1+ℓ^(d−1)). En particular la integral ponderada por (log x)^h tiende a +∞ cuando s↓1. La parte x<1 es acotada por el umbral inferior fijo de G_h. Una cota superior eventual C x^θ con θ<1 en la semirrecta positiva daría una cota superior uniforme para esa integral, contradicción.

**Cuartas potencias.** Para cualquier ε>0 la derivada respecto de log x de la suma del sector tiene módulo O_{h,d,ε}(x^(1+ε)): acotar la derivada logarítmica de G_h(z) por C z^(2+2ε) y sumar la serie absolutamente convergente de arriba con s=1+ε. La malla j⁴ tiene paso logarítmico O(x^(−1/4)). Una cota eventual sobre esa malla implicaría en el continuo una cota superior de orden x^θ+x^(3/4+ε), aún sublineal como potencia si ε<1/4. Esto prueba la afirmación.

**Consecuencia para el método.** En particular ningún número finito de diferencias de 062 permite pagar por separado el sector completo de semiprimos con el margen O(√x). En toda truncación 1≤d≤D el término de grado logarítmico D domina en el mismo argumento, con signo (−1)^D. Estos excesos son subsecuenciales; para la forma completa intervienen todos los órdenes con signos alternos. El promedio infinito de 063 tiene un cero plano y la derivada finita decisiva aquí no está disponible para él.

La desaparición de las ramas al sumar todos los órdenes se ve exactamente en Re s>1: incluyendo d=0, el factor aritmético es ∏_p(1−2a_p)=∏_p(1−p^(−s))²/(1+p^(−2s))=ζ(4s)/(ζ(s)²ζ(2s)). Cerca de 1 tiene un cero doble, mientras que ningún truncamiento no constante es regular allí. Esta identidad explica por qué el exceso sectorial es compatible con la regularidad en 1 ya establecida en 060; no aporta una cota en la franja crítica.
