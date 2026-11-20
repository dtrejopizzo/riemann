# El extremo k=4 falla incondicionalmente, con oscilación mayor que el término principal

Para casi todo t∈[1,2] y cada k fijo con 0<k≤4, al poner L=log x se tiene, sin hipótesis sobre los ceros fuera de la recta,

    R_t(x,x/L^k) = Ω_±(x L^(−1−k/2) log L).

La notación significa que existen sucesiones arbitrariamente grandes con ambos signos y módulo superior a una constante positiva por la escala indicada. En particular k=4 no puede sustituir los exponentes estrictamente mayores que cuatro de 306. En el extremo las oscilaciones superan en un factor log log x la magnitud x/log³x del bloque con corte en √x.

**La frontera de la serie.** Fijar un cero conocido ρ=1/2+iγ de ζ con γ>10, de multiplicidad r≥1. En la factorización de 292 extraer el segundo grado del corrector Euler. Para p≠3 el coeficiente de p^(−2w) en su logaritmo es

    −(1−χ(p)cos θ)²−cos(2θ)+1 = −1/2+2χ(p)cos θ−(3/2)cos(2θ),    θ=t log p.

Por ello se extraen ζ(2w)^(−1/2), L(2w+it,χ)L(2w−it,χ) y el producto [ζ(2w+2it)ζ(2w−2it)]^(−3/4). El resto sobre primos grandes converge localmente, sin ceros, en Re w>1/3 por eliminación de los grados uno y dos. Los primos finitos se ajustan aparte; tomar las ramas desde la derecha en los entornos usados. Al acercarse por la derecha al punto real w=1/2, D_t(w) permanece acotada: ζ(w) no se anula allí y el factor ζ(2w)^(−1/2) tiende a cero. En ρ todos los factores extraídos de segundo grado son unidades locales, por ausencia de ceros en la recta 1 y γ>10. Las dos L de primer grado y los factores finitos del numerador tampoco se anulan allí salvo para un conjunto discreto de t por cada factor, como en 292. De este modo D_t tiene en ρ un polo de orden 2r. El conjunto excepcional para este cero puede excluirse una sola vez para todos los k.

**Comparación de Mellin.** Usar z=L^k, F=−LR_t/(2x) y la expansión de 306 con M/k>1/2. Para s=−1/2+h real, h↓0, su Mellin continuado es O(1/h): el término H₀ permanece acotado por el cálculo anterior, los términos desplazados de índice positivo sólo pueden tener polo en s=−j/k, simple por la fórmula de 306. Los índices j=0,1 tienen su polo en el origen de su propia variable removido; para k≤4 ningún polo real queda a la derecha de −1/2. Las demás evaluaciones reales de D_t y sus derivadas son regulares. El error del desarrollo tiene Mellin holomorfo en un semiplano que contiene la frontera.

Si algún punto ρ+j/k con j≥1 es polo de D_t, el más a la derecha produce un polo no cancelado dentro del semiplano por 306. En tal caso, incluso tras sumar o restar c z^(−1/2)log z, cualquier supuesto de signo eventual contradice Landau, para todo c>0. En caso contrario, en s₀=ρ−1 el término H₀ da un polo de orden 2r y los demás términos son regulares. Llamar A≠0 al coeficiente principal. Si F≤c z^(−1/2)log z eventualmente, el Mellin de la diferencia no negativa tras retirar un compacto converge en Re s>−1/2 por Landau. Su módulo en s₀+h está dominado por su valor en −1/2+h. En el punto complejo el término añadido es regular, de modo que el módulo es asintótico a |A|h^(−2r); en el punto real la cota es c h^(−2)+O(1/h), ya que el Mellin del peso desde 1 es (s+1/2)^(−2). Elegir 0<c<|A| da una contradicción. Aplicar el mismo argumento a −F da la otra orientación. Volver a x, con log z=k log L, prueba el enunciado.

**Comparación con antecedentes.** El índice ya registra el método de oscilación de Landau y el uso de polos múltiples en 058. El punto específico aquí es que el factor corrector en la recta crítica conserva el polo complejo y no produce un polo real competidor del mismo orden en el corte móvil. Es una obstrucción al signo de este bloque en el exponente extremo; la forma completa todavía puede ser positiva.
