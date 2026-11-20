# Error uniforme al sustituir sólo la cola de primos por densidad continua

**Antecedentes.** P47 prop:sharp y su cuadratura de Chebyshev separan la densidad continua; 213-013/020/021 extraen constantes mediante momentos. Aquí se estima el error en la norma de saltos de 031 simultáneamente para todos los tamaños. Sea f constante en las celdas físicas 1,...,N, extendida por cero, H=N+1, y J=Σ_{j=1}^H j|b_j|² con b_j=f(j)−f(j−1) (representante continuo por la derecha). Para L≥2 sustituir, sólo para n>L, la medida con masas Λ(n)/n por dt/t en (L,∞), en la expresión del peine 2 Re ∫ conj(f(y)) Σ_{n≥2} f(y/n)Λ(n)/n dy. Denotar por a_L la forma sin polos resultante, conservando el lado arquimediano. Si ∫f=0, existe una constante absoluta C tal que

    |a(Uf)−a_L(Uf)| ≤ C (1+log L)^(−1/2) N J.

Se usa aquí la estimación clásica cuantitativa del teorema de los números primos, por ejemplo ψ(t)=t+O(t/(1+log t)²). Por sumación parcial, E(t)=Σ_{n≤t}Λ(n)/n−log t−c satisface |E(t)|≤C/(1+log t) para t≥2: el error integrado converge y su cola es O(1/log t). No se supone una cota a escala de raíz cuadrada.

**Cálculo exacto.** Como f(x)=Σ_j b_j 1_{x≥j}, el error interior (suma menos integral para t>L) vale

    Σ_{j≤y/L} b_j E(y/j) − E(L)f(y/L).

Esto fija el tratamiento del extremo aunque L sea una potencia prima. Para la suma, Cauchy–Schwarz da la cota √J (Σ_{j≤y/L}|E(y/j)|²/j)^(1/2). En cada franja r≤log(y/j)<r+1 la suma de 1/j está acotada por 2 por comparación con la integral de 1/x (la razón de extremos es ≤e). Sumando (1+r)⁻² desde r=⌊log L⌋ se obtiene O(√J/√(1+log L)). La norma L¹ de f es ≤N√J por la estimación de 031.

Para el término de borde, restar f(H/L) de f(y/L) bajo la integral contra conj(f(y)), por el momento ordinario nulo. Para 1≤y<H,
    
    |f(y/L)−f(H/L)| ≤ √J (1+log(H/y))^(1/2).

En efecto, los saltos implicados están en (y/L,H/L] y la suma de sus inversos es ≤1+log(H/y), también si y/L<1. Por Cauchy–Schwarz en y, ∫|f(y)|√(1+log(H/y))dy≤||f||₂√(2H)≤2N√J. Multiplicar por |E(L)|, incorporar el factor 2 del peine y sumar prueba la cota. No se utilizó el momento inverso para estimar el error.

**Cota de tamaño en el portador primitivo.** Se obtiene sin hipótesis de signo β_N=O(N), con β_N de 031. Basta fijar L=2. El contacto n=2 cuesta O(||f||₂²) por Cauchy–Schwarz y cambio de variable. Para la densidad continua, ∫₂^∞ f(y/t)dt/t=∫₀^{y/2} f(u)du/u=−∫_{y/2}^H f(u)du/u por el momento inverso. Para 1≤u≤H, telescopar desde H da |f(u)|≤√J√(1+log(H/u)). Para y∈[1,H], la integral de la cola continua queda acotada por C√J(1+log(2H/y))^(3/2). Su emparejamiento con f cuesta O(NJ) por Cauchy–Schwarz, usando ∫₀ᴴ(1+log(2H/y))³dy=O(H). Finalmente m≥m(0) y ||f||₂²≤NJ. El error ya probado completa la cota.

Por 031, o(N) en una subsucesión cofinal sí bastaría. La estimación actual controla el efecto de la cola discreta menos continua, pero la suma del bloque de primos hasta L con la densidad continua y la parte arquimediana sigue requiriendo una desigualdad inferior firmada. La aproximación de cola se conserva al modificar un número finito de pesos y tomar L después del último cambio. PROVED tras auditoría matemática independiente.

## Hay cortes arbitrariamente grandes cuya forma híbrida es negativa

Aplicando P47 prop:sharp al peine híbrido, su símbolo global en el subespacio primitivo es

    h_L(t)=m^sharp(t)−2 Σ_{n≤L} Λ(n)cos(t log n)/√n + 2∫₁ᴸ cos(t log x)dx/√x.

En efecto la discrepancia respecto de la densidad completa sólo tiene soporte en el prefijo. La forma es la integral de este símbolo contra |F̂|²/(2π). Si h_L(0)<0, los paquetes primitivos de P47 thm:kappa centrados en frecuencia cero dan un test negativo al aumentar su ventana (fijado L). Para L=2 se obtiene b−√2 log 2+4(√2−1)<0, b=m^sharp(0)=m(0)+4. El obstáculo persiste para cortes arbitrariamente grandes, como sigue.

Sea h(L)=h_L(0)=b+4(√L−1)−2Σ_{n≤L}Λ(n)/√n, definido también en 1≤L<2 por la misma fórmula. La transformada de Laplace de h(exp x) en x≥0 vale

    [b + 2/(z−1/2) − 2S(z+1/2)]/z,    Re z>1/2.

El polo del numerador en 1/2 se cancela por el residuo 1 de S en s=1, y el polo aparente en z=0 se cancela por 030, 2S(1/2)=m(0). Así se prolonga localmente por todo el eje real hasta z=−1/2 inclusive. Para verificar este último extremo, Z(s)=Σ n^(−s) satisface por sumación parcial, inicialmente para Re s>1,

    Z(s)=s/(s−1)−1/2−s∫₁^∞ ({u}−1/2)u^(−s−1)du.

La primitiva desde 1 de la función entre paréntesis es acotada; una integración por partes prolonga la última integral a Re s>−1. En particular Z(0)=−1/2, de modo que S=−Z'/Z es regular cerca de cero. Para los demás puntos reales positivos de s se usa la serie alternante de 028.

Si h tuviera signo constante débil eventualmente, la cola de h(exp x) o de su opuesta sería no negativa. El argumento de Landau de 028 excluye una abscisa real de convergencia en [−1/2,1/2]. Por ello ∫₁^∞ |h(L)|dL/√L sería finita al evaluar la integral de Laplace en z=−1/2. Pero en cada intervalo (n,n+1) la pendiente es 2/√L. Emparejar L∈(n,n+1/2) con L+1/2: la suma de los dos módulos es como mínimo su diferencia, ≥1/√(n+1). Se sigue que la integral de |h(L)|/√L en esa celda es ≥1/(2(n+1)). La suma diverge.

Hay así valores estrictamente positivos y negativos para cortes reales arbitrariamente grandes. En particular hay también cortes enteros arbitrariamente grandes con h(n)<0, por crecimiento en [n,n+1). Queda descartada la positividad global del híbrido para todos los cortes grandes; permanece abierta la posibilidad de una subsucesión cofinal favorable, y el signo para el peine original. La prueba es una aplicación del método clásico de oscilación; el antecedente directo del corpus para la transformada de cruces es N_BUILD_015_XI_LANDAU, §§1–2. PROVED tras auditoría matemática independiente.
