# Signo del error de cuadratura para la suma interior de divisores

Fijar 0<d≤1/4 como en 155. Sea b(r)=Σ_{qn²=r}Λ(q) y u=π(r/x)². La suma interior en A_d(x) es Σ_{m≥1}m^(−d)exp(−u m²). Después de restar su integral sobre (0,∞) y la constante ζ(d), su resto E_d(u) es estrictamente positivo y satisface

    E_d(u) ≍_d min(u,1)   (u>0).

Por tanto en cualquier prefijo 1≤r≤Y≤x, para Y suficientemente grande,

    Σ_{r≤Y} b(r) E_d(π(r/x)²) ≍_d Y³/x².

Esto controla el error del prefijo hasta Y=x^(5/6) a escala √x. También demuestra que el mismo reemplazo por integral más constante pierde esa escala cuando Y/x^(5/6) crece. Son cotas para el error del reemplazo, no para todo el promedio centrado.

**Monotonía elemental.** Sea G(v)=Σ_{n≥1}exp(−vn²)−√π/(2√v). Por Poisson, G(v)=−1/2+√(π/v)Σ_{n≥1}exp(−π²n²/v). Cada sumando variable tiene derivada positiva para v<2π². Para v≥2π², usar la serie original: G'(v)=√π/(4v^(3/2))−Σ n²exp(−vn²)>0, porque la suma es ≤7exp(−v) por n²≥1+(n−1) y Σ n²exp(−(n−1))<7. En ese intervalo 7v^(3/2)exp(−v)<√π/4. Luego G crece estrictamente desde −1/2 a cero, con derivada acotada cerca de cero y O(v^(−3/2)) en el infinito.

**Mezcla.** Escribir h=d/2. La diferencia entre suma e integral es
    J_d(u)=∫₀^∞ t^(h−1)G(u+t)dt / Γ(h).
La representación sale aplicando la integral gamma por separado a la suma y la integral para u>0. En u=0 la integral con G converge en ambos extremos. Su valor es ζ(d): la transformada de Mellin de Σ exp(−tn²) es Γ(h)ζ(2h) para h>1/2; separar en t=1 y sustraer √π/(2√t) continúa la identidad a 0<h<1/2 y da precisamente la integral con G. Así E_d=J_d−J_d(0) es creciente y tiende a −ζ(d)>0 por convergencia dominada. En cero tiene derivada derecha finita estrictamente positiva, pues se integra G'(t) con el mismo peso; para 0≤u≤1 dominan una constante cerca de cero y O(t^(−3/2)) en la cola. Esto prueba la comparación global.

**Suma aritmética.** Se tiene Σ_{r≤Y}b(r)∼ζ(2)Y por el teorema de los números primos sobre ψ(Y/n²) y dominación por Chebyshev. Así Σ_{r≤Y}r²b(r)≍Y³ (para el inferior basta el último intervalo [Y/2,Y]). En el prefijo considerado min(π(r/x)²,1) es comparable a (r/x)². La positividad impide cancelación interna del error.

**Antecedentes y alcance.** 046 localizaba otra cuadratura por variación de la derivada; 129–134 trataban restos factoriales. Aquí la mezcla positiva de gaussianas determina además el sentido y el orden inferior del error específico de 155. El término continuo y la corrección constante deben seguir agrupados con el resto fuera del prefijo: sumarlos por separado en toda la semirrecta daría divergencias. El techo centrado de 155 sigue abierto.
