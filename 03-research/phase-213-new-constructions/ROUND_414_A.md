# Eliminar la normalización desconocida sin perder el signo de cada cero

**Estado: PROVED, con revisión independiente de la derivada enR², la identidad diádica y la constante3.**

Sean X,P,D de 412, y definir con datos sólo a abscisas reales finitas

    B(R)=2∫₀ᴿ log(X(w)/P(w))dw − 2∫ᴿ^(2R) log(X(w)/P(w))dw.

Entonces B(R)=2D(R)−D(2R) y B(R)≥0. Más precisamente

    B(R) ≍ Σ_{γ>0} δ² R³/(R²+γ²)²,      R B(R) → 3 Σ_{γ>0}δ²

(incluido infinito). La constante c de 412 cancela exactamente. La fórmula no usa tapas de argumento. P aún requiere las ordenadas con multiplicidad.

**Positividad por cero.** En la prueba de 412, para J_R(d)=∫_(−R)^R log((w−d)²+γ²)dw se tiene

    J_R''(d)/R = 4a/(a²+4γ²d²),    a=R²+γ²−d².

Para |d|≤1/2 y γ≥2 se tiene a≥γ²−1/4>2γ|d|, con margen relativo absoluto. La derivada de la expresión respecto de R² es negativa y su opuesto es comparable a 1/(R²+γ²)². Integrar esa derivada entre R² y 4R² da 2J_R''(d)−J_(2R)''(d)≍R³/(R²+γ²)² con signo positivo. Dos integraciones respecto de d como en 412 dan el mayorante y menorante afirmados para B. Para cada cero superior fijo su contribución multiplicada por R tiende a 3δ² por el equivalente individual de 412. Domina Cδ² si la suma es finita; en el caso infinito bastan sumas parciales positivas. En particular B(R)=o(1/R) sobre una sucesión implicaría RH.

**Qué parte de la cola real es aritmética.** Como D(U)→0 por 413, D(R)=−2∫_R^∞ [log(X/P)−c]dw como integral impropia. Para R>1, X(w)=A(w)ζ(w+1/2), con A(w)=s(s−1)π^(−s/2)Γ(s/2)/(2ξ(1/2)), s=w+1/2. La porción de esta cola aportada por log ζ se calcula absolutamente por

    ∫_R^∞ log ζ(w+1/2)dw = Σ_{n≥2} Λ(n)n^(−R−1/2)/(log n)² = O(2^(−R))  (R≥2).

La identidad de cola no confiere ese ahorro al término log(A/P)−c. En la versión finita B se cancela c sin tomar una diferencia de integrales divergentes.

**Robustez al truncar alturas en la identidad por desplazamientos.** Para H≥R grande, la parte de B procedente de γ>H es O(R³/(H³ log H)) por M(T)≪T/log T de 413 y bloques diádicos. Este error corresponde a la expansión positiva en δ²; no autoriza reemplazar P por el producto truncado en las dos integrales reales con el mismo error. La desigualdad global pendiente es todavía una cota sobre la contribución de todas las alturas, no sobre el factor ζ en la cola derecha.

**Registro de revisión.** Para q=R², la derivada de4a/(a²+4γ²d²) es4(4γ²d²−a²)/(a²+4γ²d²)². La condiciónγ≥2, |d|≤1/2 da un margen absoluto entre a y2γ|d|; el opuesto de la derivada es comparable a1/(q+γ²)². Además2J_R''−J_(2R)''=2R[Q(R²)−Q(4R²)], con Q=J_R''/R, así que el factorR³ y su signo son correctos. La combinación2D(R)−D(2R) cancela exactamente los dos términos lineales en c y coincide con las integrales finitas definidas. El límite individual es2·(2δ²)−δ²=3δ² después de multiplicar porR, con un término por cero superior y sus multiplicidades; la dominación y las sumas parciales positivas cubren también el límite infinito.

El uso deD(U)→0 sólo establece la integral impropia de la cola completa, no convergencia absoluta de cada parte arquimediana por separado. La expansión positiva de log ζ permite Tonelli y da el factor(log n)^(−2) exacto. Finalmente, truncar la suma del déficit y truncarP son operaciones distintas: incluso bajoRH, cuando el déficitB es0, sustituirP porP_H deja log(P/P_H), creciente en w>0, y su diferencia diádica es negativa y no nula. No puede obedecer una cota basada sólo en los desplazamientosδ², todos nulos en ese caso.
