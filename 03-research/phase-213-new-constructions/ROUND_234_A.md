# Por qué tampoco sirven los inversos impares pequeños y qué conserva una corrección por clases

Con V_a de 233, para todo 2≤b<q, a=b⁻¹ módulo q, se tiene la cota uniforme

    V_a ≥ M² [b−φ(b)]/(12 q b³).

Por tanto V_a≥q^(1−o(1)) si b=q^o(1), b≥2. El caso a=1 es excepcional en este razonamiento. El mismo resultado vale para a=−b⁻¹ por reflexión. La obstrucción es determinista y usa los primos auténticos con sus pesos originales.

**Geometría exacta de los arcos.** Para un primo del intervalo (q,2q] sea l∈{0,…,q−1} el residuo de a(p−q) y j=floor(bl/q). Entonces

    p=bl+(1−j)q,      (p−q)/q=b(l/q)−j.

Los puntos de j/b≤y<(j+1)/b provienen sólo de la clase p≡(1−j)q mod b, y cada primo de esa clase pertenece a ese arco porque j↦(1−j)q es biyectiva módulo b. Si (1−j,b)>1, tal p sería divisible por un factor primo de b, imposible porque p>q>b. Quedan vacíos b−φ(b) arcos enteros. Allí R_a−media es una recta de pendiente −M; independientemente de su intercepto la integral de su cuadrado sobre longitud 1/b es al menos M²/(12b³). Sumar prueba la cota. M∼q por PNT. No se usó distribución en progresiones, ni se necesita uniformidad de ese teorema en b.

**Cálculo de contraste para b primo fijo.** Hay sólo un arco vacío. En cada uno de los otros b−1 arcos la medida normalizada por M converge a densidad constante b/(b−1) por el PNT en clases de módulo fijo: en la coordenada u=by−j se cuentan los primos hasta q(1+u) en esa clase. Para cada u fijo la masa dividida por q tiende a u/(b−1). El puente dividido por M converge en L² por dominación. Su límite tiene pendiente −1 en el arco vacío y 1/(b−1) en el resto del círculo. Su variación entre el máximo y el mínimo es 1/b y su distribución en un punto uniforme del círculo es uniforme sobre ese rango (cada una de las dos ramas lineales lo recorre entero). Su varianza es por tanto 1/(12b²). Así V_(b⁻¹)/q→1/(12b²) cuando b primo se mantiene fijo. El cálculo de la constante no se usa para b variable.

**Qué ocurre al ajustar cada arco por separado.** Para c unidad módulo b y u∈[0,1], tomar el puente S_c(u)−M_c u, donde S_c es la masa de los primos en (q,q(1+u)] de clase c y M_c=S_c(1). Denotar por E_c este puente menos su propia media. Por el cambio u=by−j es exactamente el residuo en el arco correspondiente una vez ajustada allí la recta de extremos y restada su media. Los arcos vacíos dan cero tras este ajuste. La energía normalizada corregida es

    W_b = (bq)⁻¹ Σ_c ∫₀¹ |E_c(u)|² du.

Sea E=Σ_c E_c, el puente centrado de a=1. La identidad de varianza, exacta para cada q y b, da

    b φ(b) W_b = V₁ + [φ(b)/q] Σ_c ∫₀¹ |E_c−E/φ(b)|² du.

El segundo sumando mide exclusivamente las diferencias entre clases. Para b=2 desaparece exactamente y la corrección devuelve V₁/2. Para otros b la corrección contiene además un coste no negativo. Si se lograra W_b=q^o(1) para algún b=q^o(1) en una subsucesión, sí se cerraría el criterio por la desigualdad anterior. La cota de promedio de 233 corresponde a V_a sin corregir y no establece tal estimación para un inverso pequeño.

**Decisión.** La transferencia V₁≤b²V_(b⁻¹) de 233 no puede cerrar el signo mediante ningún inverso positivo o negativo de tamaño subpotencia distinto de ±1: su lado derecho ya es ≥M²[b−φ(b)]/(12qb)=q^(1−o(1)). Esta obstrucción cubre los inversos impares que quedaban abiertos. La descomposición corregida indica exactamente qué término de la dirección original persiste aun al eliminar los arcos vacíos.
