# Qué puede aportar un subconjunto de primos auténticos con pesos inalterados

Sea S un subconjunto de los primos, θ_S(x)=Σ_(p∈S,p≤x)log p, y C_(k,j)(S) la muestra de 224 usando únicamente esos primos, con peso exactamente log p. Para 1/2<β<1 y j fijo se obtiene la ley extremal

    sup_(S: θ_S(x)∼x^β) limsup_k log(1+|C_(k,j)(S)|)/k
        = j log M_(β−1/2)(3).

La cota superior vale incluso para θ_S(x)=O(x^β). En el extremo θ_S(x)=O_ε(x^(1/2+ε)) para todo ε, la tasa es cero por 224. Así toda parte de ese último tamaño puede retirarse sin cambiar las tasas del criterio. Justo por encima del exponente 1/2 existen subconjuntos de densidad cero, con conteo asintóticamente regular, cuya retirada produce crecimiento espurio para j=1. No hay pesos fraccionarios ni cambio de posición de los primos.

**Techo.** Tomar a=β−1/2>0, N=jk, m=log M_a(3). El contorno a da |c_N(log p;u)|≤Cu exp(Nm)p^(−a) por 208. Como 1/2+a=β, sumación parcial da Σ_(p∈S,p≤X) (log p)p^(−β)≤C(1+log X). En el corte de 210 log X=O(N), por lo que la suma de módulos, incluso antes de integrar en u≤N, cuesta poly(N) exp(Nm). Esto prueba el techo.

**Un conjunto base con el conteo prescrito.** Para n grande sea h(n)=n^β(log n)^(β−1). Su incremento está en (0,1) eventualmente. Incluir el primo de rango n en S₀ cuando floor h(n)>floor h(n−1). El número de seleccionados hasta x es h(π(x))+O(1)∼x^β/log x por PNT. Por sumación parcial θ_(S₀)(x)∼x^β, porque el término de borde cuenta como x^β y el integral de π_(S₀)(t)/t es O(x^β/log x). Usar S₀ permite conservar una ley regular de conteo durante toda la construcción.

**Intervalo con fase controlada.** Con v=∂_a log M_a(3)>0, X=exp(Nv), L=Nv+d, considerar el coeficiente I_k(L) de la muestra sin (log p)/√p. La prueba de 226, ahora con s=−√k+ik y k/N=1/j, da uniformemente para d compacto

    N^(3/2) I_k(Nv+d)/(3^(s−1) exp(Nm−aNv))
       = exp(−ad)[K exp(iφ+ixd) J₊ + conjugado(K) exp(−iφ−ixd) J₋]/2 + o(1),

con φ=Nθ, x=x_a(3)>0 y J₊,J₋=3/[v(a∓ix)−i/j]. En efecto u=3+r/N produce exp(ir/(3j)) y las dos ramas del perfil de 212 dan estos integrales; la dominación es C exp(−cr) porque a es fijo. El corte no corta la capa de extremo, pues v≤m'_3(1/2)<2log M₁(3). La función principal no puede anularse idénticamente en d, para ninguna fase φ, por independencia de las dos frecuencias y coeficientes no nulos. Compacidad y derivadas uniformes dan un subintervalo de longitud fija dentro de d∈[0,1], y una dirección compleja de proyección, sobre la que todo el perfil tiene parte real ≥c>0 (rotación posterior al prefactor común). Las constantes dependen de j,β, no de k.

**Alcanzar la tasa sin alterar pesos.** En dicho intervalo tomar floor(X^β/(k log X)) primos distintos fuera de S₀. Hay suficientes, pues PNT da ≫ X/log X uniformemente en estos subintervalos de longitud fija, mientras que S₀ tiene O(X^β/log X) en toda la celda. Si se añaden todos, el cambio de muestra tiene módulo ≥exp(Nm−o(k)): los términos se proyectan en la misma dirección, p^(−1/2) es comparable a X^(−1/2) y X^(β−1/2) cancela exp(−aNv). El coste en masa logarítmica añadida es O(X^β/k).

Elegir sucesivamente k cada vez mayor, con X superior a todos los cortes anteriores y la masa de los bloques ya añadidos ≤X^β/k. En cada paso hay dos opciones: añadir el bloque entero o no añadirlo. Por el triángulo, alguna opción deja el módulo de la muestra (incluido TODO S₀ y las adiciones anteriores) al menos a la mitad del cambio calculado. Fijar esa opción; ningún bloque futuro afecta el dato. La perturbación acumulada es o(y^β) a toda altura: durante el bloque y hasta el siguiente, la masa acumulada es O(X^β/k) y y≥X. Se obtiene un único S con θ_S(y)∼y^β y con el limsup anunciado.

**Consecuencia para la cancelación auténtica.** En j=1 el total de todos los primos tiene tasa cero por 224. Por linealidad el complemento de este S tiene el mismo limsup positivo que S, aunque conserve densidad uno entre los primos. En particular un corte que descarte una familia de densidad cero únicamente por su conteo global puede destruir incluso una muestra de tasa cero ya demostrada. Lo nuevo respecto de 221, 223 y 226 es una partición del conjunto auténtico, con los pesos originales y ley θ_S(x)∼x^β, y el exponente óptimo para ese tamaño. La construcción escoge S dependiendo de j,β y no afirma nada similar para una clase de congruencia concreta.
