# Qué hipótesis exigiría acotar un carácter no principal y cómo eliminar la condición auxiliar

Fijar incluso P=3 y el carácter cuadrático no principal χ, extendido con valor 1 en el primo P y multiplicativamente a los enteros; L(s,χ) designa la función L usual, que omite el factor en P. Para t∈[1,2] sea

    a_t(n)=μ²(n)∏_(p|n)(Re(χ(p)p^(it))−1),     b_t=a_t*a_t

con convolución de Dirichlet. Son los coeficientes a frecuencia fija de 290 y su autoconvolución. Para casi todo t, la cota de raíz con pérdida arbitraria para los sumatorios de a_t es equivalente a RH JUNTO CON la ausencia de ceros de multiplicidad impar de L(s,χ) en Re s>1/2. Para b_t, en cambio, basta y es necesaria RH. Además se puede prescindir por completo de escoger un t genérico:

    RH ⇔  ∫₁² max(0,Σ_(n≤x)b_t(n)) dt ≪_ε x^(1/2+ε) para todo ε>0.

La fórmula propone un criterio auxiliar para el mismo signo. No estima por sí sola el promedio original de 291.

**Producto y paridad del orden.** Para F_t(s)=Σ a_t(n)n^(−s), la comparación local da en Re s>1

    F_t(s)²= G_t(s)² L(s−it,χ)L(s+it,conj χ)/ζ(s)².

En G_t los factores grandes son 1+O(p^(−2 Re s)), por igualdad del término lineal. Las raíces cuadradas de los factores Euler locales del numerador se toman desde la derecha; 1−χ(p)p^(−s+it) no se anula en Re s>0. Los factores finitos, incluido P, son holomorfos en Re s>1/2. Así G_t es holomorfo y uniformemente acotado en cada Re s≥σ₀>1/2, para t∈[1,2]; puede tener ceros de factores pequeños.

Para cada cero fijo ρ de ζ a la derecha de 1/2, los dos factores L en ρ son no nulos salvo para un conjunto discreto de t. Para que G_t(ρ)=0 haría falta que 1+(Re(χ(p)p^(it))−1)p^(−ρ)=0 en uno de los finitos p con p^Reρ≤2, lo cual también da un conjunto discreto. Asimismo las coincidencias de ceros entre las dos copias desplazadas de L se evitan salvo en un conjunto numerable de t. Eliminar la unión numerable para todos los ceros. Para cualquier t restante, un cero exterior de ζ produce un polo de F_t², y un cero exterior de orden impar de L produce un cero o polo de orden impar en el cociente meromorfo: los factores cuadrados no cambian la paridad. Una cota de raíz para las sumas de a_t continuaría F_t holomórficamente al semiplano y ambas situaciones serían imposibles. Una cota de raíz para b_t continúa sólo F_t²; los ceros del numerador de cualquier orden son admisibles.

**Techos recíprocos.** Bajo RH el lado derecho que representa la serie de b_t es holomorfo en Re s>1/2. Para a_t, añadir la condición sobre multiplicidades: entonces el producto de las dos L admite raíz holomorfa en el semiplano simplemente conexo, incluidos sus ceros, y se elige el signo compatible con la serie en Re s>1. En cualquiera de los casos la integral del módulo de la serie prolongada sobre un bloque vertical T≤|Im s|≤2T es O_(σ₀,η)(T^(1+η)) para Re s∈[σ₀,2], T≥2. Se usa la cota clásica bajo RH para 1/ζ de tamaño O(T^η), y Cauchy–Schwarz con el segundo momento clásico e incondicional de una L de conductor fijo en σ≥σ₀>1/2. Las traslaciones t∈[1,2] mantienen las constantes uniformes. Para a_t basta la raíz cuadrada del módulo del producto de las L. [Titchmarsh, capítulo XIV](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf).

Para pasar al sumatorio ordinario tomar x semientero y suavizar la indicatriz de n/x≤1 en |n/x−1|<1/(3x), sin cambiar ninguna muestra entera. El Mellin del corte hasta cero es O_j((1+|v|)^(−1) min(1,(x/(1+|v|))^j)) en las franjas usadas, por partes j+1 veces. Mover la integral a σ₀; se pueden elegir cierres horizontales de altura tendiente a infinito con integral en σ de crecimiento polinómico, por la cota de bloques y Fubini. Sumando bloques sobre la nueva recta se obtiene O(x^(σ₀+η)) para η arbitrariamente pequeño. Los semienteros cubren todos los sumatorios. Esto prueba las suficiencias sin usar GRH para la L auxiliar.

**Criterio unilateral integrado.** Bajo RH el techo recién obtenido para b_t es uniforme en t. Para la recíproca, ante un cero exterior ρ elegir t₀ con numerador G²LL distinto de cero allí. Por continuidad hay un peso η(t) suave no negativo de integral uno, soportado en una vecindad de t₀, para el que la integral de ese numerador sigue sin anularse en ρ. El promedio η de las series de b_t tiene por tanto un polo en ρ, y es holomorfo en todos los puntos reales >1/2 (también en 1, donde el recíproco de ζ se anula). Si se cumpliera el techo anunciado de partes positivas, el sumatorio promediado tendría el mismo techo superior. Aplicar Landau a Kx^σ menos ese sumatorio, con 1/2<σ<Re ρ: su Mellin, que para el sumatorio es la serie promediada dividida por s, debería tener una singularidad real a la derecha de σ. La contradicción demuestra la necesidad de RH. El uso de la parte positiva permite cancelaciones entre coeficientes antes de medir cada sumatorio; el techo incondicional sigue abierto.
