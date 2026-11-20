# Compensación firmada entre dos sectores complementarios de filas completas

Sea U de 069 y v₀>0 tal que k₀(v)=0 para v<v₀, con k₀=U₁ como en 070. Fijar el corte Y=√(x/v₀). Partir toda la suma en V, filas de numerador reducido divisible por algún primo q>Y, y W, todas las demás. Para x real grande,
    
    V(x)=−D x/(log x)³+O(x/(log x)⁴),
    W(x)= D x/(log x)³+O(x/(log x)⁴),      D=Û''(1)>0.

Ambos sectores contienen los denominadores completos, con todas las multiplicidades de 069. Se determina el saldo de cada sector entero. La construcción de subfamilias de un signo en 071 no determinaba esos saldos, y su corte friable era otro.

**Identidad física.** Expandir la fila de 069 en potencias de los inversos locales, como en 070. Cada término evalúa k₀ en x/(mn), con rad(n)|m (es decir, todos los primos de n dividen m) y el factor exterior μ(m). En particular m≤x/v₀. Si q>Y divide m, es único y q no divide n en ningún término no nulo, pues q²>x/v₀. Al escribir m=qb, queda exactamente −U_b(x/q). Recíprocamente en la suma de filas a escala x/q toda fila no nula satisface b≤x/(qv₀)<q, de modo que no hay restricción residual sobre b. Por ello
    
    V(x)=−Σ_{q>Y primo} U(x/q).

Los extremos con q²=x/v₀ quedan en W según la definición.

**Momentos del perfil completo.** Se tiene U(u)=O(u exp(−c√log u)) para u grande. Para S esto se probó en 063 por PNT cuantitativo. En la media en k⁶ de 069 se conserva: para k≤u^(1/12) el argumento es ≥√u, y para el resto usar |S(z)|≪z junto a Σ_{k>u^(1/12)} k^(−6)≪u^(−5/12). Las diferencias finitas conservan la estimación. En particular todos los momentos absolutos de U(u)du/u² con potencias de log u convergen; U se anula por debajo de v₀. La transformada de 067, con los factores adicionales de 069, es
    
    Û(s)=2 M_G(2s) ζ(4s)ζ(6s)(1−4^(1/3−s))(1−4^(1/4−s)) / [ζ(s)²ζ(2s)].

En s=1 tiene cero de orden exactamente dos por M_G(2)>0 de 062 y los factores restantes positivos. Por convergencia dominada desde la derecha, los momentos logarítmicos de grados cero y uno son cero, y el de grado dos es D=Û''(1)>0.

**Suma prima.** En un bloque de razón dos de q entre Y y x/v₀, la norma suprema y la variación total de U(x/q) son O(x/q_inicial) por las cotas de la primera derivada logarítmica de 069. Por sumación parcial y el PNT cuantitativo el error de sustituir la suma por la integral de densidad 1/log q es O(x exp(−c'√log x) log x) en total. Cambiar u=x/q en la integral da
    
    x ∫_{v₀}^{x/Y} U(u) du / [u²(log x−log u)].

En ese intervalo el denominador es comparable a log x. La expansión geométrica hasta el término cuadrático tiene resto ≤C |log u|³/(log x)⁴. Se pueden completar los tres momentos hasta infinito con error O_N((log x)^(−N)) antes de multiplicar por x, por el decaimiento probado y x/Y comparable a √x. Queda D x/(log x)³ con el signo menos en V. La cota incondicional anterior para U=V+W da la asintótica de W.

**Límite del resultado.** Queda verificada una cancelación entre sectores firmados de todos los órdenes en la misma escala. La igualdad exacta reduce la comparación global a W(x)−Σ_{q>Y}U(x/q); sus dos términos son individualmente de tamaño mayor que la raíz. El control O(x/log⁴x) no decide la precisión O(√x). La descomposición por primo grande y la expansión de densidad son clásicas; la identidad con el propio U y la orientación de los sectores proceden de las filas de 069 y del momento positivo de 062.
