# Dos pesos positivos y una contribución de Möbius de signo determinado

Para z>0 poner V(z)=Σ_{k≥1 impar}exp(−k²z). Para X>0 hay identidad absolutamente convergente

    F(X)=Σ_r μ(r)V(r/X)=Σ_{4∤n} λ(n) exp(−n/X).

En efecto la convolución de μ con el indicador de cuadrados vale λ; quitar los cuadrados de raíz par resta 1_{4|n}λ(n/4), y λ(n/4)=λ(n). En ambos lados los pesos de los coeficientes aritméticos que se conservan son positivos. En 140 el peso en μ era positivo y rápidamente decreciente en ambos extremos, pero aparecía un coeficiente −2 en una clase de Liouville.

**El precio de la positividad y cómo pagarlo.** Por Poisson para la gaussiana (restar la subserie par) se tiene

    V(z)=√π/(4√z) + O(z^(−1/2) exp(−π²/(4z)))   (0<z≤1).

El término constante se cancela exactamente. La singularidad de raíz era previsible: para un peso positivo φ en lugar de la exponencial, la Mellin del perfil Σ_{k impar}φ(k²z) en Re s>1/2 es (1−4^(−s))ζ(2s) φ̂(s), con φ̂(s)=∫φ(u)u^(s−1)du. Si φ̂ es finita y continua en 1/2, su valor es positivo para un peso no nulo casi en todas partes en el sentido de no ser idénticamente cero como elemento de L¹ ponderado. El factor ζ(2s) fuerza divergencia al acercarse por la derecha. Un perfil simultáneamente positivo en esta clase no puede ser plano y decreciente a cero en ambos extremos si además decae rápidamente en infinito.

Sea c₀=1/ζ(1/2)<0. Existen infinitos enteros D arbitrariamente grandes, caracterizados por el cruce del nivel c₀, con

    |Σ_{r≤D} μ(r)/√r − c₀| ≤ D^(−1/2).

En efecto la Mellin unilateral de la función escalonada de la izquierda antes de tomar módulo es 1/[sζ(s+1/2)]−c₀/s para Re s>1/2. Es regular en el eje real s≥0, incluido el origen por la elección de c₀. Un cero no trivial con Reρ≥1/2 da un polo en ρ−1/2. Si el escalón centrado tuviera signo débil constante desde algún punto, la abscisa de convergencia de la integral estaría entre 0 y 1/2 (un polo en la frontera basta para la cota inferior); por Landau tendría una singularidad real en esa abscisa. Esto contradice la regularidad. Los saltos tienen módulo ≤1/√D, lo que da la cota al cambiar el signo o pasar por cero.

**Resultado de signo incondicional.** Para cada uno de esos D y simultáneamente para todo X≥2D log D,

    (1/√X) Σ_{r≤D} μ(r)V(r/X)
       = √π/(4ζ(1/2)) + O(D^(−1/2)).

En efecto el error normalizado de la fórmula de Poisson es ≪Σ_{r≤D}r^(−1/2)exp(−π²X/(4r))≪√D exp(−π²X/(4D)) y el error del cruce cuesta O(D^(−1/2)). El término es, por tanto, estrictamente negativo uniformemente para D grande. No se necesita una ley de espaciado entre los cruces. Para cada X grande se puede elegir el último de estos D con 2D log D≤X: existe y tiende a infinito con X, sin tasa aquí probada.

**Obligación restante.** Con esa elección D(X), basta y es necesario para el signo un techo unilateral Oε(X^(1/2+ε)) para Σ_{r>D(X)} μ(r)V(r/X), para todo ε>0. La equivalencia sigue porque el bloque retirado es O(√X). Para el total, la Mellin es Γ(s)(1−4^(−s))ζ(2s)/ζ(s). Sobre Re s>1/2 el numerador no se anula, el eje real es regular y se aplica Landau como en 140. Bajo RH el techo bilateral se obtiene del de las sumas de λ, quitando la escala de los múltiplos de 4 y sumando por partes. La cola r>10X log X puede además retirarse en valor absoluto por el decaimiento de V. La constante negativa hallada para el bloque no demuestra un signo del total.

**Cotejo.** 073 ya usa la recurrencia μ*Λ=−μ log, por lo que repetirla sin una estimación nueva no fue la ruta seguida. 134 elige cruces del momento de exponente 1 al nivel cero. Aquí el cruce al exponente crítico exige el nivel no nulo c₀ para cancelar la singularidad real de la transformada; ese nivel determina el signo del término theta uniforme. 140 y las transformaciones theta del corpus dan los antecedentes del peso; no se atribuye novedad a la identidad de Poisson ni a Landau.
