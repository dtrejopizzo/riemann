# Coste exacto de separar los primos después de la oscilación de Mellin

Para N=k² escribir la muestra D_k=B_N(k) de 215 como suma sobre primos, efectuando primero TODO el integral oscilatorio en u. Sea V_N(t) la suma de los módulos de esos aportes a B_N(t). Para toda sucesión real t=o(N),

    lim V_N(t)^(1/N)=M_(1/2)(3)=2/(1+√(8/9))>1.

Por tanto, a t=k y N=k², el procedimiento de mayorar después de integrar en la tasa paga exp(c k²+o(k²)), aunque la muestra completa está acotada por exp(O(k)) por 215. La comparación vale incondicionalmente y prueba que la oscilación en u por sí sola deja una pérdida de orden exponencial cuadrático en k. A diferencia de 211 (cuadrados de términos individuales antes del integral), acá se evalúa la norma absoluta de los coeficientes ya integrados.

**Coeficiente de un primo.** Denotar m(a)=log M_a(3), a=1/2, v=m'(a), x=x_a(3)>0 y usar K,θ de 212 a tasa 3. Para L=log p definir

    I_N(L;t)=∫_[3,N] 1_{L≤2N log M₁(u)} u^(−5/2+it)c_N(L;u)du.
    V_N(t)=Σ_p (log p) exp(−L/2)|I_N(L;t)|.

Para la cota superior trasladar el contorno a altura a: ∫|H_u(τ+ia)|dτ≤Cu por escala y a/u≤1/6. Así |c_N(L;u)|≤Cu exp(Nm(a)−L/2) por 208 y monotonía en u. Como L≤2N log M₁(3) y Σ_(p≤X)(log p)/p≪1+log X por Chebyshev, V_N≤C(1+N)exp(Nm(a)).

**Perfil del coeficiente integrado.** Para L=Nv+d y d en un compacto fijo, la tasa u=3 está estrictamente dentro del corte en la desigualdad para L: v<v*<2log M₁(3) por 212. Cambiar a u=3+r/N y usar c_N(L;u)=(u/3)c_N(uL/3;3). En cada intervalo acotado de r, el argumento nuevo es Nv+d+rv/3+o(1). El perfil de 212, uniforme en desplazamientos compactos por dominación gaussiana, da

    N^(3/2) exp(−Nm(a)+aL) 3^(−it) I_N(L;t)
        = 3^(−5/2) Re[K exp(iNθ+ixd) · 3/(v(a−ix))] + o(1).

En efecto (u/3)^(it)→1 localmente porque t=o(N). Tras la normalización, la envolvente de 212 a tasa fija y la escala anterior dominan el integrando por C exp(−arL/(3N)), integrable uniformemente para N grande. El indicador converge a uno para cada r fijo. Integrar la exponencial compleja del perfil produce el factor 3/(v(a−ix)). El error es uniforme en d compacto por el mismo argumento. Aunque el coeficiente original es complejo, sólo su fase constante 3^(it) sobrevive a esta escala.

**Piso aritmético.** En 0≤d≤2π/x, el módulo del perfil principal supera una constante positiva en algún intervalo de longitud fija independiente de N: se puede escoger un subintervalo alrededor de un máximo interior del módulo, que tiene período π/x. Sobre ese intervalo, para N grande, |I_N|≥c N^(−3/2)exp(Nm(a)−aL). El teorema de los números primos da Σ (log p)/p≥c' en dicho intervalo de logaritmos, uniformemente incluso si se mueve con N dentro del compacto. En efecto los extremos multiplicativos tienen cociente fijo >1 y θ(X)/X→1 uniformemente para X≥exp(Nv). Ya que a=1/2, estos términos de V_N suman al menos c''N^(−3/2)exp(Nm(a)). Concluye la tasa exacta.

**Qué parte del integral necesita cancelación.** Existe un complemento que sí admite una cota absoluta suficiente en la escala de 215. Restringiendo el integral a u≥U_N, 3≤U_N≤N, la misma prueba superior da V_N^(alto)≤C(1+N)exp(N log M_(1/2)(U_N)). Si N=k² y U_N/√k→∞, entonces log(1+V_N^(alto))=o(k) porque log M_(1/2)(U_N)=O(U_N^(−2)). Así se puede, por ejemplo, retirar u≥√k log(2k) antes de plantear la estimación prima de D_k. También se puede retirar un compacto fijo [3,U] con U<G−1 usando el control uniforme de 209–210 en tasas verificadas (en esa banda |h_u|≤1 por 207 y Z2 con el margen unitario). El crecimiento que falta controlar queda en las tasas intermedias. El extremo inferior artificial 3 produce el piso de variación total arriba; el mismo argumento con un extremo fijo mayor tiene constantes dependientes de ese extremo. No se ha obtenido el techo subexponencial para la suma firmada de esas tasas.
