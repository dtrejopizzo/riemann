# Positividad estricta hasta 131/50 con un filtro de Chebyshev

Para toda función del dominio del paper 47 y 0<T≤131/50, W_T(f)≥exp(−20000000001)||f||₂². Se usa la misma altura de verificación G=3·10¹² de 175–189. El tramo adicional es (2.58,2.62].

**Elección del filtro.** Sea u(τ)=1−sinc(τ/H)^(2k), a=kR²/(3H²), d=m/2 y D_d el polinomio de Chebyshev de primera especie. Tomar

    h(u)=D_d(2u/a−1)/D_d(2/a−1),   P(u)=h(u)²,   B=D_d(2/a−1)^(−2).

El dato filtrado tiene transformada h(u(τ)) f̂(τ). Como el grado es d, su soporte adicional es a lo sumo 2kd/H. El argumento de 178 para la extensión espectral conserva exactamente la identidad con máscara 1−P: en la recta P es el cuadrado de un multiplicador real par, y ambas autocorrelaciones tienen soporte dentro de la zona donde el corte de extensión vale uno. Para 0≤u≤a, P≤B. Para a≤u≤1 es creciente hasta uno; por tanto la máscara es no negativa en todos los átomos reales. Para u≥7a/2 se tiene P≥B exp(m arcosh(6))/4. La ganancia usa D_d(cosh v)=cosh(dv). A grado fijo, el factor D_d(6) es el máximo posible en ese punto entre polinomios reales de grado ≤d acotados por uno en el intervalo bajo, tras reescalar a [−1,1]: una superación estricta daría d cambios de signo de la diferencia en los extremos alternantes más un cero en 6 al reescalar el presunto extremizador para igualar allí a D_d.

**Parámetros y margen.** Usar T=131/50, s=29/2, U=log s, R=240000000, k=20, m=1020000000, H=400000000000, N=10¹⁰. El cálculo racional de dos filas de 189 da ||C||≤17.31 al comprobar 1911 extremos. Se tiene T+km/H<U y 2U<5.5. El corchete arquimediano menos peine es ≥1/10 para |τ|≥R y ≥−24 globalmente por 178. Como en 179, u≤a en |τ|≤R y u≥7a/2 desde |τ|≥2R. Reservando la mitad del margen en |τ|>G/2 y usando la fuga η de 179 en Ω=2R, el piso integrado, en unidades de B||f||², es

    η exp(m arcosh(6))/80 −24.

El filtro tiene un valor polar mayor que en el filtro monomial. Con |u(i/2)|≤k/H², el costo en estas mismas unidades es a lo sumo 4 exp(T) exp(m arcosh(1+2k/(H²a))). El certificado verifica que el logaritmo del término positivo del piso supera al logaritmo de este costo en más de diez, y es mayor que diez. Se conserva así más de 2B||f||² tras pagar el polo.

**Cola espectral.** Para a≤u≤1, P es convexa: D_d tiene una expansión en potencias de x−1 con coeficientes no negativos (usar D_d(1+2v)=Σ_j binom(2d,2j)(1+v)^(d−j)v^j por la fórmula hiperbólica). Entonces 1−P(u)≤P'(1)(1−u); derivando la fórmula hiperbólica se obtiene P'(1)=m tanh(d arcosh(2/a−1))/√(1−a)≤2m. En |τ|>G/2 tenemos u≥7a/2, luego la máscara es ≤2m(2H/G)^(2k). Como en 178 la potencia de |τ| en la máscara también domina el crecimiento logarítmico de la densidad correctora. Su costo alto es <1/1000 y lo absorbe la densidad reservada ≥1/(80π). El costo bajo es ≤2π exp(−20000000002)||f||² mientras B≥exp(−m arcosh(2/a−1))>exp(−20000000000). El costo bajo es menor que B||f||². Por inclusión de soportes y densidad se concluye para todo el dominio indicado.

**Comprobación.** Ejecutar python3 verify_190.py con python-flint. El cálculo usa bolas Arb de 192 bits y no forma un polinomio de mil millones de grados: verifica las identidades hiperbólicas mediante sus cotas logarítmicas. El método minimax de Chebyshev es clásico. Aquí se lo aplica a la máscara de 179 y se comprueban el soporte, la positividad real, los polos complejos y las dos correcciones de la fórmula completa.

Se revisó independientemente la sustitución en la identidad de la medida proyectada, el signo de la máscara real, la ganancia alta y el costo polar.
