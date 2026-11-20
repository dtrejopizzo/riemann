# El déficit logarítmico de 153 es la masa exacta de los cuadrados perfectos

Poner f(t)=exp(−πt⁴), I=∫₀^∞ f(t)dt y J=∫₀^∞ log(t)f(t)dt. Completar S de 153 a
    V(x)=Σ_{p,k,n≥1} log p exp(−π(p^k n²/x)²).
Vale incondicionalmente, con x→∞,

    V(x)−S(x)=(I/2)√x log x + (J+I D)√x + o(√x),
    D=Σ_{p, k impar ≥3}(log p)p^(−k/2).

**Identidad puntual.** Los k pares corresponden a p^(2l)n²=m². Para m fijo la suma de sus pesos es Σ_{p|m} v_p(m)log p=log m. Por tanto toda esa parte es exactamente Σ_m log m f(m/√x). Con Y=√x, la suma de f(m/Y) difiere de YI por O(1) por monotonía. La suma de log(m/Y)f(m/Y), dividida por Y, tiende a J por sumas de Riemann impropias: cerca de cero se controla uniformemente por la integral de |log t| en (0,δ), y en la cola por una mayorante decreciente integrable. Esto da YI log Y+YJ+o(Y). Para cada p,k impar ≥3, la suma en n dividida por Y tiende a I/p^(k/2) y está acotada por ese mismo valor comparando con la integral decreciente. D converge absolutamente. Convergencia dominada da el término restante.

**Consecuencia.** I=Γ(1/4)/(4π^(1/4)); por la definición de ξ, I/2=−ξ(1/2)/ζ(1/2). Así el término secundario entero de 153 se cancela al completar el conteo. El signo global equivale al techo eventual V(x)≤ζ(2)x/2+O(√x). La contribución adicional de tamaño √x tiene incluso la constante explícita J+ID. El antecedente 073 ya identificaba una deriva armónica de los cuadrados de primos y 152 la transfería a un núcleo con límite constante. La observación aquí es que en el conteo positivo de 153 se puede reagrupar toda la parte par exactamente, entero por entero, sin ningún teorema sobre la distribución de los primos.

**Límite.** La serie de Dirichlet del conteo completo es ζ(2s)(−ζ'/ζ)(s). En particular la identidad para los cuadrados explica la corrección secundaria pero deja en V toda la dificultad de las fluctuaciones de Λ. Como ζ(2s) no se anula en Re s>1/2, completar las potencias no elimina ningún posible polo fuera de línea. Repetir la completación como argumento espectral volvería a 150–153.
