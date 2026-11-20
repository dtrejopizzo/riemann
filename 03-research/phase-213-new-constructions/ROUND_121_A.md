# Qué bloque aritmético conserva la tasa de la matriz completa

En la base ortonormal par de 119 fijar 0<a<1 y X=exp(2T). Definir la matriz real simétrica K por su cuadrática para los tests F de esa base,

    K[F]=2Σ_{X^a<p≤X} (log p)c_F(log p)/√p
         −2∫_{X^a}^X c_F(log v)dv/√v,

donde c_F es la autocorrelación de la extensión por cero. La misma definición vale en el hiperplano primitivo. En ambos espacios, si Δ>0, la parte positiva del mayor autovalor de K tiene exponente exacto Δ, con normalización 1/(2T) en cada ventana grande. Si Δ=0 dicha parte tiene exponente cero usando log(1+parte positiva). En consecuencia su techo subexponencial en cualquier sucesión no acotada basta para el signo.

**Compensación de la densidad.** En la forma completa el polar para F real es 2∫∫cosh((s−t)/2)F(s)F(t)dsdt. Restando 2∫₁ˣ c_F(log v)dv/√v queda 2∫₀^{2T}exp(−u/2)c_F(u)du, de módulo ≤4 para ∥F∥₂=1. La diferencia entre peine de Λ y peine primo tiene norma O(1+T): los cuadrados cuestan O(Σ_{p≤√X}(log p)/p)=O(log X) por Chebyshev y los exponentes ≥3 tienen suma absolutamente convergente. El símbolo arquimediano cuesta O(log(2+T)) en esta base por la derivada L² y Jensen como en 119.

**Error del bloque inferior.** Para Θ=sup Reρ y cada ε>0 vale θ(v)−v=O_ε(v^(Θ+ε)) para v≥2: es la cota clásica de la fórmula explícita truncada de ψ (altura comparable a v, suma de 1/|ρ| hasta esa altura O(log²v)); para enteros o cercanías de saltos basta evaluar en semienteros y usar monotonía. Retirar las potencias propias cuesta O(√v log²v); si Θ=1 basta Chebyshev. Para nuestra base |c_F|≤1 y |c_F'|≤∥F'∥₂≤πN/T. Integración por partes de la discrepancia contra c_F(log v)/√v entre 1 y X^a acota bordes y variación por O_ε((1+N/T)(X^a)^(Δ+ε)). Todo es uniforme en los vectores unitarios y, por tanto, en norma matricial.

Resulta ∥W+K∥≤O_ε((1+T)^3 exp(2a(Δ+ε)T)). Si Δ>0 escoger ε con a(Δ+ε)<Δ. Por 119 y la desigualdad variacional entre los extremos, el error tiene tasa estrictamente menor que la profundidad del mínimo de W y se obtiene la afirmación. Para Δ=0 usar 119 y luego ε arbitrario. No se usa una cota numérica conocida para Θ, ni se concluye que K sea positiva. La comparación no afirma un error subexponencial cuando Δ>0: identifica un error de orden exponencial estrictamente menor.

**Cotejo.** El lema combsine de P47 ya descompone el peine en esa familia. 104 centra un corte X^a para un único peso fijo. Aquí todos los vectores de un espacio creciente comparten el control del corte, y la conclusión es sobre el peor cociente matricial de una banda móvil. Queda abierta la cota unilateral para el bloque superior.
