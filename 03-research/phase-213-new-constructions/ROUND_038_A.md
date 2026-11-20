# Norma traza de la cola y traza exacta de la forma aritmética completa

Sea A el operador autoadjunto en X₀ que representa B∞ en el producto de energía I, y A_L el del corte de 032–033. Entonces A es de clase traza y

    ||A−A_L||₁ ≤ C/√(1+log L),       Tr A = (2/3) ξ′(2)/ξ(2) > 0.

La norma traza controla la suma de valores singulares. La convergencia en norma de operadores de 033 por sí sola no permite pasar la traza al límite.

**Cola en norma traza.** Escribir f(t)=u(exp(−t)), g=f′ en t>0. La integración Jg(t)=∫₀ᵗg(z)dz es Hilbert–Schmidt de L²(dz) a L²(exp(−t)dt): su núcleo indicador tiene norma al cuadrado ∫₀^∞t exp(−t)dt=1. Para comparar dos cortes L<K escribir R=log L, S=log K y usar la medida μ en coordenada r con masas Λ(n)/n en log n menos dr. En el contacto de 032, el momento ordinario cero permite reemplazar f(t+r) por f(t+r)−f(r), pues ∫conj(f(t))exp(−t)dt=0. Expresar el incremento como la integral de g desde r hasta r+t. Por Fubini en la franja finita de cortes el núcleo restante es

    D(t,z)=μ((R,S] ∩ [z−t,z]).

Los valores en los extremos móviles no afectan la integración en z. D se anula para z<R. Para z≥R la cota de discrepancia de 032 da |D(t,z)|≤C/(1+max(R,z−t)), uniformemente en S. Separar [R,R+t] de su cola para obtener

    ∫|D(t,z)|² dz ≤ C [t/(1+R)² + 1/(1+R)].

Así D entre los mismos dos espacios tiene norma Hilbert–Schmidt O((1+R)^(-1/2)). La diferencia de formas es −2 Re〈Jg,Dg〉 en el espacio ponderado; comprimir −J*D−D*J a la restricción de media cero da la cota anunciada para ||A_K−A_L||₁. La identidad se obtiene primero sobre un núcleo suave y pasa por continuidad.

**Traza de los cortes.** Sea s=1/2+it. El funcional de Mellin de u en coordenada g tiene núcleo exp(−sz)/s; la condición de media cero restringe g al complemento ortogonal de exp(−z). Por proyección, su norma al cuadrado ahí es

    [1/(2 Re s)−2/|s+1|²]/|s|² = 1/(t²+9/4)     (Re s=1/2).

Como |h_L(t)|=O_L(1+log(2+|t|)), multiplicar la aplicación de Mellin por √|h_L| produce un operador Hilbert–Schmidt con medida dt/(2π). Factorizar A_L usando entre los dos factores el signo de h_L prueba que es de clase traza. Por una base ortonormal y convergencia absoluta,

    Tr A_L = ∫ h_L(t)/(t²+9/4) dt/(2π).

La completitud en norma traza y la identificación del límite en norma de operadores con A justifican ahora Tr A=lim Tr A_L.

**Evaluación.** El peso de la integral es un tercio del núcleo de Poisson de altura 3/2. Su integral contra cos(t log x), x≥1, es x^(−3/2)/3. Para m♯(t)=Re ψ(5/4+it/2)−log π, la integral vale [ψ(2)−log π]/3: la extensión armónica al semiplano superior es Re ψ(5/4−it/2) en la variable compleja t, con crecimiento logarítmico, por lo que se aplica la fórmula de Poisson. También se obtiene integrando término a término la serie de fracciones simples de P47 prop:sharp. Usando ψ(2)=1−γ_E se sigue

    3 Tr A_L = 1−γ_E−log π −2 Σ_{n≤L} Λ(n)/n² +2(1−1/L).

Al retirar L queda 2ξ′(2)/ξ(2) por la definición de ξ y el logaritmo derivado del producto de Euler en 2. Su signo estricto se ve en la suma de Hadamard emparejada de P47 rem:fe: en s=2 los términos reales Re(1/(2−ρ)) son positivos, ya que los ceros no triviales cumplen 0<Re ρ<1.

**Alcance.** La traza positiva permite que haya valores propios negativos compensados por positivos. La suma de sus módulos es exactamente (||A||₁−(2/3)ξ′(2)/ξ(2))/2, por el teorema espectral de clase traza. El signo global equivaldría a probar la cota superior ||A||₁≤(2/3)ξ′(2)/ξ(2). La estimación de cola anterior no demuestra esa cota. El valor escalar del logaritmo derivado es conocido; el objeto calculado aquí es la traza del operador normalizado de 033 con todos los pesos de von Mangoldt.

Cotejo exacto: POWER_CONE_001 §§1–2 ya obtiene el mismo escalar como energía del generador a=2. La factorización en producto de dos operadores Hilbert–Schmidt y la evaluación de la traza recibieron revisiones independientes. La identificación como traza no convierte el signo de ese generador en positividad global.

## Traza con una dilatación: qué basta controlar a grandes distancias

Para r≥0 poner S=S_exp(−r) y k(r)=exp(r/2) Tr(AS). Es real por la realidad de A y S. La traza exacta anterior da k(0). El signo global equivale a k(r)≤k(0) para todo r suficientemente grande.

**Cálculo sin presuponer signo.** Para el corte L, S multiplica la Mellin por exp(−rs). Por la factorización de clase traza de la sección previa y su diagonal de evaluación se obtiene

    k_L(r)=∫ cos(rt) h_L(t)/(t²+9/4) dt/(2π).

La convergencia en norma traza prueba convergencia uniforme en cada intervalo compacto a k, y |k_L(r)|≤C exp(r/2) con C uniforme en L. Por tanto k es continua. La cota exponencial no implica la desigualdad buscada. Para z real >1/2, su transformada unilateral es

    ∫₀^∞ e^(−zr) k(r) dr
       = [ z k(0) − (ξ′/ξ)(1/2+z) ]/(z²−9/4).

En efecto, al corte fijo la integración de cos(rt) produce z/(z²+t²). Separar las dos fracciones cuadráticas. El término de altura 3/2 aporta z k_L(0); el otro es la mitad de la integral de Poisson de h_L a altura z, con signo negativo en el numerador. Al retirar L, esa integral de Poisson vale 2(ξ′/ξ)(1/2+z): el coseno de t log n da n^(−z), la parte continua da 2/(z−1/2) y la arquimediana da ψ(5/4+z/2)−log π. Usar la recurrencia de ψ y la serie de Euler absolutamente convergente. La identidad se extiende holomórficamente a Re z>1/2 y meromórficamente más allá; z=3/2 es removible por el valor de k(0).

**Equivalencia.** Si A≥0, la identidad de compresión S*AS=exp(−r)A y la desigualdad de Cauchy–Schwarz para operadores Hilbert–Schmidt A^(1/2) y A^(1/2)S dan |k(r)|≤k(0) para todo r. Para la vuelta, si k(0)−k(r)≥0 eventualmente, su transformada de Laplace no tiene singularidad sobre el eje real positivo: es k(0)/z menos la expresión anterior y ξ carece de ceros reales allí. Quitar un tramo inicial sólo resta una función entera. El argumento de Landau usado en 028 implica que la abscisa de convergencia es ≤0, pues una abscisa positiva finita sería una singularidad real. La transformada resulta holomorfa en Re z>0. La fórmula excluye entonces ceros de ξ en Re s>1/2, pues cada uno daría un polo de su derivada logarítmica. Por la equivalencia de Weil de P47 se obtiene el signo global.

Si k(r)>k(0) en un solo r, se tiene explícitamente Tr[(Id−exp(r/2)S)* A (Id−exp(r/2)S)]=2[k(0)−k(r)]<0, lo que obliga a una dirección negativa. No se ha establecido ninguna violación ni una cota superior eventual.

**Cotejo.** P47 thm:oneprofile ya reduce el objetivo a una correlación definida positiva, y POWER_CONE_001, 028–030 y los criterios de función tornillo anticipan el enfoque de traslado y transformada. Aquí se identifica la correlación con una traza en X₀ y basta una desigualdad escalar unilateral eventual gracias a la fórmula meromorfa explícita. No usar la equivalencia como prueba de esa desigualdad.
