# Compensación de los sectores de 354 en cada centro

Tomar h=X^(−δ), 0<δ≤1/16 fijo, H=hX, y el umbral y y sectores U_h,V_h de 354. Poner D(x)=x(1−e^(−h))∏_{p≤y}(1−1/p). Para todo A fijo y **cada** centro X≤x≤2X,

    U_h(x)= D(x)+O_(A,δ)(H/log^A X),
    V_h(x)=−D(x)+O_(A,δ)(H/log^A X).

Se conserva el producto exacto en D para no perder precisión en el error. En particular ∫U_h V_h dx/x=−∫D² dx/x+O_A(H²/log^A X), ajustando las constantes. La compensación se produce a escala del perfil principal en la ventana misma; la precisión de raíz sigue pendiente.

**Primos con cofactor liso pequeño.** Para m≤√X la longitud de la ventana de primos es comparable a hX/m, con extremo de tamaño z≈X/m≥c√X. Para X grande esa longitud excede z^(0.86). La estimación uniforme sobre primos en intervalos cortos da el peso θ igual a x(1−e^(−h))/m con error relativo O_B(log^(−B) X); al pasar de Λ a θ el coste O(√z log²z) se absorbe. Si la longitud supera z^0.99, dividirla en tramos de longitud comparable a z^0.98, distribuyendo el extremo entre los tramos; sumar sus errores relativos conserva la precisión. Sumar en módulo los errores sobre los cofactores cuesta a lo sumo un factor O(log y) por 354. [Guth y Maynard, corolario 1.3 y demostración en §13](https://arxiv.org/html/2405.20552v1)

**Cofactores lisos grandes, uniformemente.** Para cada n del pulso procedente de un m>√X libre de cuadrados y y-liso, multiplicar divisores primos distintos de m hasta cruzar X^(1/4). Se obtiene un divisor d en [X^(1/4),X^(1/4)y], libre de cuadrados y liso. Para X grande todo ese rango está por debajo de H. Por tanto cada d aporta O(H/d) múltiplos en la ventana, sin coste de borde adicional. El peso absoluto de todas las representaciones de un n como pm es ≤Σ_{p|n} log p≤log(2X). Para todo B fijo, aplicar Rankin con α=B/log y:

    Σ_{d≥X^(1/4), liso} μ²(d)/d ≪_B (log X)^(−5B) log y.

En efecto Σ_{p≤y}(p^α−1)/p≪_B (1/log y)Σ log p/p=O_B(1). Eligiendo B suficientemente grande, toda la cola cuesta O_A(H/log^A X) en cada centro. El mismo techo armónico completa el producto en el término principal. Esto prueba la primera fórmula.

**Suma completa.** Por la identidad de 353, acotar primero Σ μ(n)log n en el pulso. La estimación de 350 para μ en todos los intervalos, seguida de sumación parcial, da O_A(H/log^A X): para prefijos de longitud <X^(2/3) usar la cota trivial, y para el resto el teorema con margen fijo sobre 5/8 (el extremo superior requerido tiene margen fijo según δ). En p^k≤√X, k≥2, el mismo teorema da |S_h(x/p^k)|≪_A (H/p^k)/log^A X, pues la longitud supera z^0.86 con z≈X/p^k y es ≤z^(1−ε_δ). Sumar con Σ_{p,k≥2}(log p)/p^k<∞. Para p^k>√X el techo por conteo cuesta O(H X^(−1/8)+√X log²X), al sumar (H/p^k+1)log p como en 354. Esto demuestra P_h=O_A(H/log^A X) en cada centro y por resta da la segunda fórmula. [Matomäki, Shao, Tao y Teräväinen, estimación uniforme para μ](https://arxiv.org/abs/2204.03754)

**Alcance.** 354 obtenía las medias lineales para todas las anchuras. Para la familia de potencias pequeñas ahora se conoce el perfil que se cancela y su signo en cada centro, incluso después de formar productos cuadráticos al nivel principal. El error H/log^A X sigue siendo mayor que √H para A fijo; no hay cota de raíz para el residuo.
