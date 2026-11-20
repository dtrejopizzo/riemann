# Una extensión firmada para todos los ceros con costo ponderado sumable

Sea ρ=β+iγ un cero no trivial y δρ=|β−1/2|. Sumar siempre con multiplicidad. En la ventana (−2T,2T) el dato espectral de KEP(T) del paper 47 es, en distribuciones y con su normalización espectral, la suma de exp(iγu)cosh(δρ u). Esto usa la simetría respecto de la recta crítica, sin suponer RH. Para cualquier k>1 y L suficientemente grande existe una medida real simétrica ν_L con transformada de soporte [−L,L], que coincide exactamente con ese dato local y cumple

    ∫ (1+|τ|)^(−k) dν_L⁻(τ)
       ≤ C(T,k) Σρ [L^(−2)+δρ²](1+|γ|)^(−k).

La constante no depende del número de ceros ni de su separación. Aquí se usa la libertad de extensión de KEP(T); la medida no requiere un multiplicador flat-top común aplicado al dato entero.

**Construcción y convergencia.** Tomar b y χ de 170, con χ=1 en la ventana. Para cada cero usar como transformada
    exp(iγu){ b(u/L)+χ(u)[cosh(δρ u)−b(u/L)] }.
El primer término tiene densidad espectral no negativa, trasladada a γ. En el soporte fijo de χ, las derivadas hasta cualquier orden N de la corrección son O_(T,N)(δρ²+L^(−2)), por δρ≤1/2, paridad y Taylor. La densidad correctora trasladada es por tanto acotada por C_(T,N)(δρ²+L^(−2))(1+|τ−γ|)^(−N). Para N>k+1, multiplicar por el peso del enunciado e integrar cuesta a lo sumo C_k(1+|γ|)^(−k), por 1+|γ|≤(1+|τ|)(1+|τ−γ|). El conteo de ceros por bandas O(log(2+|γ|)) da convergencia absoluta en la norma ponderada de las correcciones. La suma de los términos positivos es localmente finita y temperada por el mismo conteo y la rapidez de decaimiento de la densidad de b para L fijo. Se puede verificar la identidad local contra cada prueba suave por integración por partes y paso al límite. La parte negativa de la suma está dominada por el módulo de las correcciones. Se obtiene la cota anunciada sobre el espectro completo.

**Sin corte en u.** También se puede tomar sencillamente b=1 y mantener la misma χ. Se obtiene una extensión temperada con átomos positivos en las ordenadas y la misma cota sin L^(−2); desaparece entonces la exigencia de soporte compacto de la transformada. Si se conoce RH hasta altura G≥2, el costo ponderado es ≤C(T,k)G^(1−k)log(2G), por δρ²≤1/4 y el conteo unitario. En particular se puede insertar la altura G de Z2 del paper. Las constantes no han sido evaluadas y G es fijo. Aumentar k cambia la norma y la constante.

**Consecuencia directa para la forma.** Para f suave con soporte compacto en (−T,T), en la convención de KEP, el valor W_T(f) es ∫|f̂(τ)|²dν(τ). La extensión anterior implica
    W_T(f) ≥ −C(T,k) sup_τ [(1+|τ|)^k |f̂(τ)|²] · Σρ δρ² (1+|γ|)^(−k).
Así una dirección negativa concreta impondría un mínimo cuantitativo a esa suma de desplazamientos. La desigualdad no da positividad: ni la suma se sabe nula ni se ha obtenido un margen positivo uniforme para absorberla. No es lícito hacer k→∞ conservando fija la norma de las pruebas.

**Cotejo.** Las cotas de cola por suavizado y los controles por cuartetos tienen antecedentes en el paper 47 y R7-01. La aportación respecto de 170–171 es pasar a una extensión firmada del dato real completo con correcciones sumables, cada una cargada a su propio δρ². La masa negativa total sin peso de 171 no tiene aquí un mayorante finito demostrado. El problema que queda es producir una extensión positiva o absorber la corrección en la forma original.
