# Positividad estricta de la forma completa hasta T=21/10

Para 0<T≤21/10 y todo f del dominio de la forma completa del paper 47,
    W_T(f) ≥ exp(−32000000001)||f||₂².
Usar Z1–Z3 tal como en 175, en particular la altura ya verificada G=3·10¹². Se mantienen ambas paridades y los dos momentos polares. No se postula RH. Damos los parámetros y el certificado escalar para evitar extrapolar la ley asintótica de 177.

**El peine comprimido.** Probar sólo el extremo T=21/10. Usar U=log 9, R=1500000, k=16, m=1200000000 par, H=240000000000 y N=10¹⁰. Con u=1−sinc^(2k)(τ/H), g definido por ĝ=u^(m/2)f̂ tiene soporte en [−2.18,2.18] dentro de [−U,U]. En el cociente de Schur de 081/177 poner x=exp(t); por simetría basta 1≤x≤9. La fila normalizada es
    [xL(9x)+ψ(9x)+L(9/x)+xψ(9/x)]/(1+x).
Entre los puntos de salto es una función lineal fraccionaria monótona o constante. En el punto mismo el convenio inclusivo en las dos sumas da un mayorante de los dos límites, por positividad de los sumandos. El conjunto de puntos que hay que revisar es {1,9} y q/9,9/q dentro de [1,9] para todas las potencias primas q≤81. La prueba adjunta enumera los primos por división entera, las potencias por multiplicación y los extremos como fracciones exactas. En cada extremo la evaluación intervalar da <12. Por Schur, ||Π_U||≤12. Así m_arch−12≥1/3 fuera de [−R,R] por el menorante explícito del paper para la digamma; en toda la recta el corchete es ≥−18.

**Piso para el filtro.** En la prueba de fuga de 175 tomar Ω=2R y n=63000000=10ΩT, conservando el coeficiente 256^n para la interpolación. El resto √(Ω/π)(3eΩT/n)^n es <1/(4√T), y 256^(−2n)/64≥η=exp(−230TR). El argumento de proyección da esta misma cota inferior para la fracción de masa Fourier de f fuera de [−2R,2R]. Con a=kR²/(3H²), u≤a en |τ|≤R y u≥2a para |τ|≥2R por las desigualdades de 175 para k=16. En el término archimediano menos el peine reservar la mitad del corchete en |τ|>G/2. La parte restante integrada contra u^m|f̂|²/(2π) da por lo menos
    a^m(2^mη/6−18)||f||² > 3a^m ||f||²,
ya que m log2−230TR>10. Se tiene a^m>exp(−32000000000).

**Polo.** A(g) y B(g) son los de f multiplicados por u(i/2)^(m/2). Para v=1/(2H), sinh(v)/v≤exp(v²) por la serie, de modo que |u(i/2)|≤exp(2kv²)−1≤4kv²=k/H²<a/2. Por Cauchy–Schwarz 2|A(f)B(f)|≤4exp(T)||f||². De aquí el costo polar es menor que a^m||f||².

**Cola.** Para la extensión μ proyectada de 172 usar χ como en 175 cambiando la indicatriz a [−7,7]. Es uno al menos hasta |t|=5.5>2U, por lo que W_T(f)=W_U(g)+∫(1−u^m)|f̂|²dμ como en 177. El prefactor para la corrección de un cero antes de (1+|s|)^(−2)min(1,N/|s|)^N es ≤2·14·exp(8.5/2)·25/(2π)<10⁵. Siguen vigentes los techos 10⁹log(3+|τ|) y, para |τ|≤G/2, el factor adicional 100^(−N), que ahora deja |C|<exp(−32000000002). En |τ|>G/2 la densidad correctora con máscara tiene módulo <1/1000 por (1−u^m)≤m(H/|τ|)^(2k); el mismo mayorante para la máscara es <1/2. La reserva de corchete vale al menos (1/6)(1/2)/(2π)=1/(24π) por unidad de |f̂|²dτ. Absorbe toda la corrección alta. Los átomos de μ retenidos tienen peso no negativo. En bajas el costo en unidades de ||f||² es ≤2π exp(−32000000002)<a^m. Sumar con el piso y la cota polar prueba, con margen sobrante, la desigualdad anunciada. Densidad del núcleo suave e inclusión de soportes dan el resultado completo.

**Reproducción y alcance.** Ejecutar python3 verify_178.py con python-flint; usa bolas Arb a 192 bits. Las desigualdades funcionales provienen de los argumentos de 172–177, no de muestrear la forma. La norma asintótica de 177 es antecedida por 081; aquí se usa la fila exacta y no la aproximación asintótica. La ventana previamente certificada en esta fase era 6/5 en 175. No se conoce un margen uniforme para todas las ventanas.
