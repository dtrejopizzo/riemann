# Binomiales enteros exactos y coste de su representación firmada

Para x≥2 poner N=⌊2x⌋. En los enteros 1≤m≤N se quiere reproducir exactamente g(m/x), con g de 257, mediante acarreos de binomiales enteros de argumento superior ≤N. Sean V(x) el coste mínimo (suma de valores absolutos de los coeficientes reales) y

    S_j=Σ_(d≤N/j) μ(d)g(dj/x),     b_j=S_j−S_(j+1),     S_(N+1)=0.

Entonces se tiene el certificado aritmético bilateral

    (1/3)Σ_(j≤N)|b_j| ≤ V(x) ≤ 2Σ_(j≤N)|b_j|.

Esto da una fórmula finita que controla el óptimo con factor seis, con una construcción explícita de coste superior. La representación coincide en cada entero y por tanto también en cada potencia prima. En concreto,

    RH equivale a V(x)≪_ε x^(1/2+ε) para todo ε>0.

**Inversión finita.** Escribir F_j(m)=⌊j/m⌋ y F₀=0. Estos N vectores forman una base triangular con diagonal uno. La igualdad Σ_j b_j F_j(m)=Σ_(l≥1)S_(lm)=g(m/x) se obtiene telescopando y usando Σ_(d|k)μ(d)=1_(k=1). En m=1 da Σ_j j b_j=0. Cada acarreo genuino es F_n−F_k−F_(n−k), de norma de coeficientes en esta base ≤3. Esto prueba el piso, incluidos los repartos simétricos.

**Construcción cíclica para el techo.** Para cada j promediar sobre r=0,...,N−1. Escribir r+j=q+eN, con 0≤q<N y e∈{0,1}. El vector F_j+F_r−F_q−eF_N, si e=0, es menos un acarreo. Si e=1 es la diferencia entre el acarreo que reparte j en q y N−r, y el que reparte N en r y N−r. Las particiones con un lado cero aportan cero y se omiten. Cada término cuesta ≤2 en variación y sólo usa argumentos ≤N. Al promediar, q recorre los mismos residuos que r y hay exactamente j casos con e=1. Así se representa F_j−jF_N/N. Multiplicar por b_j y sumar cancela F_N por la relación de balance. La fórmula no necesita redondear en los átomos ni elegir argumentos factoriales mayores que 2x. Multiplicada por Λ(m) y sumada en m, da directamente una combinación de log binom(n,k) para el conteo con potencias primas.

**Tamaño de los coeficientes.** Interpolar S(v)=Σ μ(d)g(dv/x) para 1≤v≤N+1. El peso es C¹ y t g'(t) tiene variación acotada con soporte [1,2]. Bajo RH la cota de Mertens y sumación parcial dan |S'(v)|≪_ε (x/v)^(1/2+ε)/v en el soporte. Integrar para acotar Σ|S_j−S_(j+1)| prueba el techo de raíz. Incondicionalmente el mismo argumento hasta v=√x usa M(t)≪t exp(−c√log t), y para v≥√x basta M(t)≪t. Da V(x)≪x exp(−c'√log x).

Recíprocamente |S₁|≤Σ|b_j|≤3V(x). El Mellin respecto de x de S₁(x)=Σ μ(d)g(d/x) en Re s>1, integrando desde 0, es H(s)/ζ(s); el soporte inferior es x≥1/2. Una cota de raíz con pérdida arbitraria prolongaría esa transformada holomórficamente a Re s>1/2. Allí H no se anula, de manera que ningún cero de ζ puede estar en ese semiplano. Incluso bastaría acotar V en x enteros: |dS₁/dx|=O(1) por la suma absoluta y la acotación de g'. El argumento recíproco usa exactitud en todos los enteros, incluidas las entradas compuestas que Λ no ve. No establece la misma necesidad para una representación que sólo ajuste los átomos de Λ.

**Antecedentes y diferencia.** 259 daba inversión continua y presupuesto de aproximación en L¹. 260 resolvía una barrera para mezclas positivas en los átomos primos. Aquí el balance de la base de pisos permite convertir una inversión entera en binomiales genuinos con coste uniforme mediante el promedio cíclico. La inversión de Möbius por sí sola es clásica. Sigue abierta la cota incondicional de raíz para la variación aritmética explícita.
