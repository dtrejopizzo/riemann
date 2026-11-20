# Positividad estricta hasta T=5/2 mediante una cota directa de fuga Fourier

Para 0<T≤5/2 se tiene W_T(f)≥exp(−9000000001)||f||₂² en el dominio completo del paper 47. Se usa la altura G=3·10¹² de Z2. El paso que cambia la escala del cálculo respecto de 178 es una cota explícita sin interpolación de alto grado.

**Lema de fuga.** Para f con soporte [−T,T] y F=f̂, la fracción de su energía en |τ|>Ω es al menos
    η=[1+(1+TΩ)exp(2TΩ+2)]^(−1).
Para probarlo denotar E_in y E_out las dos integrales de |F|², d=1/T, A=Ω+d, F#(z)=conj(F(conj z)). La función entera J(z)=∫_{−d}^d F(z+s)F#(z+s)ds tiene módulo ≤C_f exp(2T|Im z|) por soporte compacto. Sobre los rayos reales |x|≥A se tiene 0≤J(x)≤E_out. Poner z=A sin θ en la tira |Re θ|<π/2. La función J(A sin θ)exp(−2TA cos θ) es holomorfa acotada allí, pues Re(A cos θ)≥|Im(A sin θ)|. En ambos bordes su módulo es ≤E_out. El principio de tres líneas da esa misma cota en toda la tira. En el intervalo real [−A,A] se deduce J(x)≤exp(2TA) E_out. Integrando, 2d E_in≤∫_{−A}^A J≤2A exp(2TA) E_out, ya que para cada |τ|≤Ω el intervalo [τ−d,τ+d] está incluido. Esto da el lema, también para f compleja. El método de la tira y la fuga espectral son herramientas clásicas; se verifica aquí la constante usada por el certificado.

**Parámetros y peine.** Tomar T=5/2, U=log(25/2), R=55000000, k=20, m=500000000, H=400000000000 y N=10¹⁰. Mantener u, g, φ y la extensión espectral con indicatriz [−7,7] de 178. Se cumple T+km/H=2.525<U y 2U<5.5. En 1≤x≤s=25/2 la fila de Schur de 081 es
    [xL(sx)+ψ(sx)+L(s/x)+xψ(s/x)]/(1+x).
Las fracciones de ruptura son 1,s y q/s,s/q cuando pertenecen al intervalo, con q potencia prima hasta floor(s²)=156. El cálculo Arb adjunto en cada extremo inclusivo da una cota común 79/5. Como en 178 domina ambas trazas laterales y el interior de cada celda. El corchete m_arch−79/5 es ≥1/10 en |τ|≥R y ≥−22 en toda la recta.

**Margen.** Escribir a=kR²/(3H²). En |τ|≤R, u≤a por Taylor y Bernoulli. En el extremo 2R la evaluación con bolas demuestra u>(7/2)a. Hasta |τ|/H=2 se prolonga por monotonía de sinc en el intervalo positivo, y después por |sinc|≤1/2. En reserva alta y en el costo polar se procede como en 178. Tras reservar la mitad del corchete en |τ|>G/2, la parte integrada por unidad de ||f||² aporta al menos
    a^m[(7/2)^mη/20−22] > 3a^m,
con Ω=2R. El lema de fuga da −log η≤log(2(1+TΩ))+2TΩ+2. El verificador comprueba que m log(7/2) menos este mayorante supera 10 y que a^m>exp(−9000000000). El término polar cuesta menos de a^m||f||² por |u(i/2)|≤k/H²<a/2.

**Espectro restante.** Las cotas de 178 para C siguen sin cambios puesto que χ y G son idénticos. En |τ|≤G/2 el costo está por debajo de exp(−9000000002) por unidad de |f̂|²dτ. En |τ|>G/2 el techo 10⁹log(3+G)m(2H/G)^(2k) es <1/1000 y la máscara allí es <1/2. La densidad reservada es al menos 1/(80π)>1/1000. Los átomos son positivos y el costo bajo, aun multiplicado por 2π, queda por debajo de a^m en norma L². Esto cierra el margen anunciado en ambas paridades. La extensión a ventanas menores es por inclusión.

**Reproducción.** Ejecutar python3 verify_179.py con python-flint. La enumeración de primos y extremos usa enteros y fracciones exactas, y las desigualdades escalares usan Arb a 192 bits. El límite anterior certificado aquí era 2.1, en 178. Esta prueba no establece positividad para todas las ventanas.
