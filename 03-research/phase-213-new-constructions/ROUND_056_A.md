# Un criterio cuadrático de Möbius fuera de la diagonal

Partimos de 054–055. Mantener y=4x, L=√x, K=C₀ L(log x)² y elegir D=cL/(log x)² con c fijo suficientemente pequeño. Definir β=ε*ε=1*α, donde * es convolución de divisores. Poner

    H(d,m)=(1/2) Σ_w β(w)V(dmw/y)[log(d/L)U(dw)+log(m/L)U(mw)].

El signo global equivale a una **cota superior** C L, uniforme para x=j⁴ grande, de

    Σ_{d,m>D, d≠m} μ(d)μ(m) H(d,m).

Sólo intervienen d,m entre D y C L(log x)² y w≤C(log x)⁴. Las constantes se fijan antes de variar x. La simetría permite sumar sobre d<m y multiplicar por dos. El coeficiente β y el logaritmo pueden cambiar de signo.

**Eliminación de los divisores pequeños.** Para q>1, Λ(q)=−Σ_{d|q}μ(d)log(d/L). Elegir C₀ suficientemente grande y c suficientemente pequeño para que la cota uniforme de 055 para cada modelo periódico acotado en d≤D sea O(x⁻²). Esto se sigue de la estimación exponencial de su último apartado y de la estimación de las filas pequeñas: se puede fijar de antemano cualquier potencia de ahorro aumentando las constantes de los exponentes, y usando un orden fijo suficientemente grande en la cuadratura del modelo completo. Por tanto en 054 los términos con d≤D cuestan en total O(D log x/x²) al probar cada indicador de divisibilidad por separado. No es necesario tomar su periodo común.

Tras esta resta se puede extender la suma de q>L a todos los q positivos. En los q≤L añadidos el peso aritmético truncado tiene módulo ≤τ(q)log L, y no hay término en q=1. Por 054 cada fila con U cuesta O((y/q)exp(−c₁√(K/(4q)))); al sumar con la cota trivial τ(q)≤q y elegir C₀ grande se obtiene o(1).

Escribir q=dh y w=hv. Sumar α(v) sobre los divisores v de w produce β(w). La suma inferior de 054 es entonces el negativo de la suma cuadrática con peso log(d/L)U(dw)V(dmw/y)β(w), con d>D y error O(L) o menor. Cuando U(dw)≠0, dw<eK, y el soporte de V obliga a m≥y/(16eK)>D por la elección de c. También m≤By/D, d≤eK y w≤eK/D. Intercambiar d y m en este dominio común y promediar da H. El signo menos convierte la cota inferior de 054 en la cota superior del enunciado.

**Cálculo de la diagonal.** Antes de excluir d=m su contribución es

    Σ_{d>D} μ(d)² log(d/L) Σ_w β(w)U(dw)V(d²w/y).

Para W=y/d²≥1, la suma interior es O_N(W^(1−N/2)log(2W)) para cada entero fijo N≥2. En efecto, poner w=ab, β(w)=Σ_{ab=w} ε(a)ε(b); en cajas diádicas suaves de tamaños A,B' con AB' comparable a W, alternar en la variable mayor gana max(A,B')^(−N). Las derivadas de U y V en esa variable están acotadas uniformemente a la escala de la caja por sus fórmulas logarítmicas y el soporte. Sólo hay O(log(2W)) cajas no vacías. Para W<1 la suma es O(1); se anula si d>2√B L, con B=16e. Estas estimaciones dan O(L) tras sumar los módulos en d **después** de la cancelación en w. Por ejemplo N=4 basta al agrupar d≤L en intervalos diádicos.

Más precisamente la diagonal vale C_diag L+o(L), donde

    C_diag=(1/ζ(2))∫₀^∞ log u · [Σ_w β(w)V(u²w/4)] du.

Para u=d/L en un compacto alejado de cero sólo aparecen finitos w y U(dw)=1 eventualmente, uniformemente. La densidad de los libres de cuadrados da el límite de esta suma de Riemann ponderada. Las estimaciones anteriores uniformes controlan la cola u↓0 tanto en la suma como en la integral (la misma prueba vale con U=1). La integral se entiende con la suma en w dentro. La eliminación de la diagonal cuesta así el orden permitido. Queda pendiente la cota firmada fuera de ella.

**Cotejo.** Se reutilizan la inversión exacta de 040, el corte equilibrado de 049 y la estimación en progresiones de 055. Las descomposiciones de Möbius y la simetrización son clásicas. La reducción aquí permite que los dos coeficientes sean la misma función μ en un dominio común, y estima su diagonal para este peso. No se infiere positividad del núcleo simétrico.
