# Signo del bloque completo con un primo grande al acercarse a la frecuencia cero

Usar los coeficientes completos b_t de 292, incluido el primo 2. Fijar 1/2≤α<1, L=log x, v=t²L, a=log 2 y b=(log 2)²/4. En el límite conjunto x→∞, t→0, sin restricción sobre v,

    Σ_(n≤x; P⁺(n)>x^α) b_t(n)
      = −2 U x/L⁵ · [24a²−12abv+2b²v²+o(1+v²)],    U>0.

El corchete principal es 2(bv−3a)²+6a². Esto establece un signo estrictamente negativo uniforme en la transición v acotado, v→0 y v→∞. En particular a frecuencia exactamente cero la contribución es asintótica a −48 U a² x/L⁵. Se incluyen todos los cofactores del primo grande. Por el techo de todo orden logarítmico del sumatorio completo, el bloque restante tiene el mismo término con signo positivo. El error en el saldo requerido por 299 sigue sin control a escala de raíz.

**El factor que cambia el orden.** Escribir B_t(s)=Σ b_t(n)n^(−s) por continuación. En h=s−1 se tiene exactamente, en una vecindad de (0,0),

    B_t(1+h) = V(h,t) h² [1−(1+cos(t log 2)) 2^(−1−h)]²,

donde V es analítica, par en t y U=V(0,0)>0. En efecto los dos factores L de 292 son no nulos en (1,0), ζ^(−2) aporta h² y los demás factores del producto corrector convergen localmente y son positivos en el punto real. El corchete interior es ah+bt²+O(h²+|h|t²+t⁴). Extrayendo los coeficientes en h se obtienen, con derivadas respecto a s evaluadas en 1,

    B'' = 2U b² t⁴+O(t⁶),   B''' = 12U ab t²+O(t⁴),
    B'''' = 24U a²+O(t²),   B=B'=0.

**Momentos uniformes.** La prueba de 294 para un único primo grande vale uniformemente en |t|≤1: χ sigue siendo no principal en t=0, tanto en las sumas torcidas como en el PNT en progresiones, y sólo se necesitan cotas superiores para la corrección Euler. Por tanto el bloque vale −2Σ b_t(m)li(x/m), con m≤x^(1−α), hasta error O_R(x/L^R). Para expandir hasta orden cinco aplicar el corte M=exp(√L) de 294; tomar 12 términos de li y desarrollar los denominadores hasta grado 24. La norma armónica absoluta hasta M cuesta O(L²), el resto integrado es O(x/L⁶) y los momentos pueden extenderse hasta infinito con ahorro logarítmico arbitrario. Los momentos de grado j son (−1)^j B^(j)(1). El término con k=1 de li y j=2,3,4 da respectivamente B''/L³, −B'''/L⁴ y B''''/L⁵ tras extraer x. Los demás términos cuestan O(t⁴/L⁴+t²/L⁵+1/L⁶), en esas mismas unidades. Al sustituir las tres derivadas, el error relativo a (1+v²)/L⁵ tiende a cero para cualquier sucesión t→0. Esta estimación es necesaria porque el equivalente de 294 a frecuencia fija pierde su término principal justo en t=0.

**Qué compensa la agrupación.** La fila cero contiene familias positivas mayores que la raíz (301). Al reunir todas las que tienen un primo mayor que x^α con los términos de signo opuesto del mismo bloque se obtiene la fórmula negativa anterior. El complemento es demasiado positivo para descartarlo, incluso con las dos potencias adicionales de ahorro logarítmico en t=0.
