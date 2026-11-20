# Una copia de cada producto reducido admite una cota inferior a la escala raíz

Sea S_λ la suma de 060 multiplicando el total de cada producto reducido r por λ^ω(r), incluida la diagonal r=1. El número original de pendientes es 2^ω(r) y todas dan el mismo total para un r fijo. Para λ=1/2 queda exactamente una copia de cada producto. Para todo ε>0,
    
    |S_{1/2}(x)| ≪_ε x^(1/3+ε)     (x≥1).

Se incluyen todos los órdenes y no hay corte en el producto. El criterio de 060 corresponde a λ=1. El cambio de multiplicidad es esencial: para cada 1/2<λ<1 y cada θ<1, limsup S_λ(j⁴)/(j⁴)^θ=+∞.

**Una copia.** Para Re s>1 la transformada en x con peso x^(−s)dx/x es
    
    2 M_G(2s) ∏_p (1−2λ p^(−s)/(1+p^(−2s))).

Se obtiene sumando absolutamente la fórmula de 067 sobre todos los d: el producto mayorante converge allí. En λ=1/2 el factor local con u=p^(−s) es (1+u³)/[(1+u)(1+u²)]. Por tanto el producto es ζ(3s)ζ(4s)/[ζ(6s)ζ(s)]. Usar ahora el perfil específico de 059 y 062:
    
    M_G(2s)=ζ(2s)[I'(2s)−b₀ I(2s)],
    I(v)=2^(v−1) V̂(v/2) η(v/2)²,     I'(1)=b₀ I(1).

El corchete contiene al menos un factor η(s), también después de derivar. Al dividirlo por ζ(s) queda una función entera, usando η(s)/ζ(s)=1−2^(1−s). Además el corchete se anula en s=1/2 por el centrado y ζ(1/2) es finita y no nula allí (serie alternada para η). Se elimina así el polo de ζ(2s). La transformada completa es holomorfa en Re s>1/3: allí 1/ζ(6s) tiene serie absolutamente convergente. En cada franja vertical compacta interior decrece más que cualquier potencia en altura. En efecto V es suave de soporte compacto alejado de cero, sus transformadas V̂ y V̂' tienen ese decaimiento, y los factores zeta, eta y sus derivadas tienen crecimiento a lo sumo polinómico en esas franjas, lejos de los polos removidos. Invertir Mellin primero sobre Re s>1 (inversión del perfil suave y suma absolutamente convergente), luego desplazar a cualquier recta 1/3+ε. Resulta la cota enunciada.

**Multiplicidades intermedias.** Para s=1+t, t>0 pequeño, dividir el producto general por ζ(s)^(−2λ). El cociente B_λ es holomorfo y positivo en 1: los factores tras quitar la potencia de (1−p^(−s)) son 1+O(p^(−2 Re s)) uniformemente cerca de 1, usando la rama real en el eje y el producto normalmente convergente. Así la transformada es t^(2λ) por una función analítica de valor 2M_G(2)B_λ(1)>0 en cero (062). Si 1<2λ<2, su segunda derivada tiende a +∞. Una cota superior S_λ(x)≤C x^θ eventual, θ<1, daría una cota superior uniforme de esa derivada integrando contra (log x)² x^(−s)dx/x. La suma se anula cerca de cero. En la malla de cuartas potencias se aplica la interpolación de 067: la derivada logarítmica de S_λ es O_δ(x^(1+δ)), pues la mayorante de Euler para el perfil derivado converge a 1+δ aun sumando sobre todos los órdenes. Queda probada la afirmación unilateral.

**Alcance.** El conteo a profundidad creciente ya aparece en 043 y aquí no se usa. El cálculo procede del producto de 067; la ganancia procede de la factorización ciclotómica con multiplicidad uno y de la cancelación de un factor η antes de desplazar el contorno. Se puede retirar una copia por producto a coste o(√x) en el representante original; el resto lleva multiplicidades 2^ω(r)−1. La cota para éste y la ventana T quedan abiertas. El fallo para toda multiplicidad intermedia estricta impide un paso por continuidad de las mismas cotas superiores entre ambos extremos.

Más precisamente, si F es la transformada del caso de una copia, el mismo desplazamiento hasta σ∈(1/6,1/4) da S_{1/2}(x)=Res_{s=1/3}F(s) x^(1/3)+Res_{s=1/4}F(s) x^(1/4)+O_σ(x^σ). En Re s>1/6 las únicas singularidades posibles restantes son esos dos polos simples, provenientes de ζ(3s) y ζ(4s); un residuo puede anularse. No se necesita conocer sus signos.
