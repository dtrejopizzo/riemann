# El cosh con tasa 1/2 detecta un extremo alcanzado en toda rejilla

Supóngase que Δ=sup Re(ρ−1/2)>0 es alcanzado. Fijar cualquier h>0. Para g=2cosh(t/2) cortado a [−T,T] hay c>0 y un entero L(h) tales que en cada bloque de L(h) enteros consecutivos suficientemente grandes aparece n con W(g)/‖g‖²≤−c exp(2Δnh) en T=nh. No se requiere independencia racional de las ordenadas. En particular, si ese único cosh fuese eventualmente no negativo en una sola rejilla, un fallo del signo requeriría un supremo no alcanzado.

En la notación de 088 tomar a=1/2. Por dominación usando Σ|a+z|⁻²<∞,
    
    exp(−2ΔT)J(T)=P(T)+o(1),   P(T)=Σ_{Re z=Δ} exp(2iγT)/(a+z)².

El resto tiende a cero incluso sin separación de los demás ceros respecto de Δ. P(0)<0: por conjugación es real y cada término tiene parte real ((a+Δ)²−γ²)/|a+z|⁴<0, pues |γ|>14 y a+Δ≤1. Sea d=−P(0)>0. Truncar el borde simétricamente con cola de módulos <d/8. Cuando todas las fases finitas estén suficientemente cerca de uno, la diferencia del polinomio truncado respecto de su valor inicial es <d/4, y P(T)<−d/2. En los múltiplos de h las fases forman la órbita de una rotación en un toro finito. El cierre de la órbita entera es un grupo compacto; los traslados por potencias enteras del entorno elegido del neutro recubren ese grupo por densidad. Un subrecubrimiento finito da retornos al entorno con huecos acotados en el índice n, también para órbitas finitas. Por 088 la energía multiplicada por exp(−(2a+2Δ)T) difiere de 2P(T) en o(1), y la norma al cuadrado dividida por exp(2aT) tiende a 1/a. Esto da la afirmación.

**Cotejo.** Fase 159 G2_B5_R5 utiliza recurrencia del término extremo en tiempo continuo y monotonía del mínimo al variar el test. Aquí el test está prefijado, la rejilla es arbitraria y el valor negativo está en la identidad del grupo de fases; así se evitan las resonancias sin desplazar el origen. El modelo impar de 089 no contradice esta conclusión par. Sin extremo alcanzado el término P desaparece, y queda abierta la detección en una sola rejilla.
