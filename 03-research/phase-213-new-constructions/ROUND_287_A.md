# Para los incrementos ordinarios de Möbius basta controlar una dirección

Sea C(X)→∞ tan lentamente como se quiera, con log C(X)=o(log X), y sean

    D₊(X)=max_(X≤u≤v≤XC(X)) [M(v)−M(u)],
    D₋(X)=max_(X≤u≤v≤XC(X)) [M(u)−M(v)].

Para cada una de las dos direcciones por separado,

    lim log(1+D_±(X)²/X)/log X = 2Θ−1.

En particular basta hallar bandas arbitrariamente lejanas en que el exceso de enteros libres de cuadrados con número par de factores primos sobre los de número impar no supere X^(1/2+o(1)) en ningún subintervalo. También se puede elegir desde el principio el exceso opuesto. Aquí se deja variar el extremo inicial del subintervalo. El coste frente a 285 es usar una banda multiplicativamente más ancha.

**La compensación ocurre con ambos signos.** Fijar un cero exterior ρ₀ y 1/2<σ₁<σ₂<β₀. Del test complejo de 285 con h=1, eligiendo el factor polinomial que deja simple el polo objetivo, se obtiene un peso fijo W suave, compacto en [1,e], con |Σ μ(n)W(n/Z)|≫Z^β₀ para todo Z grande. Al integrar por partes con la función escalonada M resulta ∫₀¹|M(Z exp v)|dv≫Z^β₀, pues la derivada del peso en coordenada logarítmica está acotada y desaparecen los términos de borde.

Aparte construir la probabilidad de dos puntos de 284 para cada cero con Re ρ≥σ₁, repitiendo los factores según multiplicidad. La suma de sus anchuras H es finita por la densidad de 230. Convolucionar con la uniforme en [0,H+4] y después con una densidad Gevrey dos de masa uno en [0,1]. La densidad resultante k es no negativa, de soporte fijo [0,2H+5], y vale 1/(H+4) en [H+1,H+2]. Su transformada positiva P(s)=∫k(v)exp(sv)dv cancela con multiplicidad todos los polos de 1/ζ en Re s≥σ₁ y tiene decaimiento vertical exp(−c√|Im s|) en franjas fijas.

En la recta 2 la inversión suavizada de Perron da para ∫k(v) M(X exp v)dv el integrando X^s P(s)/(sζ(s)). Se justifica integrando primero el escalón suavizado por k, o por inversión de Mellin absolutamente convergente después del suavizado. Mover al camino entre σ₁ y σ₂ de 285. No se cruza ningún polo efectivo y el factor Gevrey domina el crecimiento del recíproco sobre el camino. Así el promedio firmado es O(X^σ₂). Su promedio en valor absoluto es ≫X^β₀ por la meseta de k y la integral inferior del párrafo anterior. Como k es una probabilidad, cada una de las dos masas ∫k max(±M,0) es ≫X^β₀. En consecuencia en CADA [X,BX] suficientemente lejano, B=exp(2H+5) fijo para este cero, hay valores de M superiores a c X^β₀ e inferiores a −c X^β₀.

**Orientación temporal.** Aplicar el resultado en [X,BX] y [BX,B²X]. Un valor negativo en la primera banda y uno positivo en la segunda producen un incremento positivo de tamaño ≫X^β₀. Eligiendo los signos al revés se obtiene un incremento negativo. Para cada cero fijo, C(X) termina superando B². Tomar el límite inferior y después el supremo sobre los ceros exteriores. El techo se deduce de M(y)≪_θ y^θ para Θ<θ<1, o del conteo trivial si Θ=1. En Θ=1/2 basta la normalización positiva como en 285.

**Implicación para la prueba del signo.** La asimetría es utilizable: basta un mayorante para las sumas de μ de izquierda a derecha que valga en todos los subintervalos de una banda elegida. No bastaría controlar desde un máximo seleccionado a posteriori sin variar el inicio. En el falsificador real multiplicativo de 286, el defecto f*1 es de hecho no negativo: sus factores locales son potencias de serie con coeficientes 1,2,2,… en primos alterados, e identidad en el resto. Su promedio firmado por tanto no ofrece una cancelación adicional para reparar la inversión. La localización en ambas direcciones para la μ verdadera usa que 1/ζ carece de polos reales a la derecha de 1/2; el polo real artificial de 286 impide ese argumento para f. La existencia de las bandas con techo unilateral de raíz sigue abierta.
