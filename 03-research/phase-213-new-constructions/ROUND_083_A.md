# Positividad del exponencial truncado y anchura de la franja de ceros

Para a>0 y T>0 poner F_{a,T}(t)=exp(at)1_{[−T,T]}(t). Para la forma completa W de P47 se tiene la equivalencia

    W_T(F_{a,T})≥0 para todo T suficientemente grande
    ⇔ |Re ρ−1/2|≤a para cada cero no trivial ρ.

Bajo la condición de la derecha hay, para TODO T>0, la cota explícita

    W_T(F_{±a,T})/||F_{±a,T}||² ≥ [1.9·2a/(a²+γ₁²)] tanh(aT),

donde γ₁ es la primera ordenada positiva. Por tanto es incondicional para cada a≥1/2, en cualquier ventana. En particular las dos diagonales exponenciales del plano polar de 082 son positivas, con cota >0.008 tanh(T/2) para a=1/2. No se afirma positividad en su span.

**Identidad.** Escribir z=ρ−1/2 y γ=Im z. La fórmula de Weil evaluada en F da
    
    W_T(F_{a,T})=2 Σ_ρ [cosh(2aT)−cosh(2zT)]/(a²−z²).

Es el producto de las integrales de exp((a±z)t). El vector está en el dominio de forma: su transformada decrece como O_T(1/(1+|ξ|)). Se puede alisar por convolución, con soportes en un compacto común, convergencia en norma logarítmica y variación uniformemente acotada. La fórmula pasa al límite por dominación O_{T,a}(1/(1+γ²)) en la suma de ceros. La autocorrelación no depende de cómo se definan los valores en los bordes. La norma al cuadrado es sinh(2aT)/a.

**Control simultáneo de todas las contribuciones negativas.** Sea b=Re z y supóngase |b|≤a. Para d=Re(1/(a²−z²)), r=|Im(1/(a²−z²))|/d se tiene
    
    d>0,   d≤1/(a²+γ²−b²),   r=|2bγ|/(a²+γ²−b²)≤1/|γ|,

usando también |b|≤1/2. Si H=cosh(2aT), la parte real del sumando, antes del factor 2, es ≥d[H−√(H²+r²(H²−1))]≥−d r²(H−1). Para la primera desigualdad se optimiza la fase 2γT y se usa |b|≤a; para la segunda basta elevar al cuadrado H+r²(H−1). En el primer par de ceros de la recta, 14<γ₁<15, la contribución en cambio es ≥2(H−1)/(a²+γ₁²).

Para explicitar el coste total recordar la identidad clásica de Hadamard Σ Re(1/[ρ(1−ρ)])=2+γ_E−log(4π)<0.05. Proviene de la derivada logarítmica de ξ en 0 y 1 y su ecuación funcional. Todos los |γ|≥γ₁>14 por el conteo verificado citado en P47. Para a=1/2, d=[(γ²+β(1−β))(1+r²)]^(−1), β=Re ρ, luego d≥0.99/γ² y Σ1/γ²<0.051. Para el a general considerado, (a²+γ₁²)d≤(a²+γ₁²)/(a²+γ₁²−1/4)<1.002. Por tanto el gasto total, aun incluyendo el primer par en el mayorante de pérdidas, es <0.052(H−1)/(a²+γ₁²). El primer par lo paga y queda la cota anunciada después de normalizar. Se usan las ubicaciones verificadas a baja altura y la masa total clásica, sin presuponer que los demás ceros estén en la recta crítica.

**Necesidad de la franja.** Tomar Laplace en T de la identidad sin normalizar, inicialmente en Re s>max(1,2a). La transformada es
    
    2 Σ_ρ [s/(s²−4a²)−s/(s²−4z²)]/(a²−z²).

En compactos sin polos la suma converge normalmente; las colas del primer término son O(Σγ⁻²) y las del segundo O(Σγ⁻⁴). Es regular en el eje real s>2a. Cada z con Re z>a da un polo efectivo en 2z: los únicos términos posibles son z y −z, con igual denominador y residuos del mismo signo algebraico, nunca cero. Si W_T(F_{a,T}) fuese no negativa en una cola, Landau para su transformada de Laplace impediría una abscisa de convergencia >2a, pues sería una singularidad real. La holomorfía resultante excluye ese polo. Por simetría se obtiene la franja completa. La misma prueba funciona si sólo se pide un minorante −C exp(2aT) eventual.

**Alcance y antecedentes.** Los criterios escalares de Bombieri–Suzuki y las fórmulas de P47 por cuartetos ya figuran en el índice; el argumento de Landau es heredado. Aquí la estimación constructiva paga la parte negativa de la suma por todos los ceros usando una sola pareja verificada, uniformemente en T para el exponencial sin modular. Para cerrar el signo mediante esta familia bastaría establecer la positividad eventual para una sucesión a↓0. La prueba dada para a≥1/2 no atraviesa esa frontera: si |b|>a, el coseno hiperbólico del cero puede crecer más que H. No se ha certificado una franja nueva ni una ventana completa mayor.
