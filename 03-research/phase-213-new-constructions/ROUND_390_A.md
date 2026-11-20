# Dos cruces en el orden de los primos y distancia entre ellos

**Estado: PROVED, con revisión independiente de la orientación, los empates y la escala condicional.**

Fijar la banda v=log(x/y²)∈[E/2−1/2−1,E/2−1/2+1] de 386. Enumerar en orden creciente los primos de la banda. Para cada primo p, evaluar inmediatamente después del salto W(p) y C(p) de 386. Sean i_W el primer índice con W(p)≥0 e i_C el primero con C(p)≤0. Entonces ambos existen para x suficientemente grande. Escribir N=i_C−i_W y

    D_x=2J sqrt(x) exp(E/4−1/4)/log x.

Si |N|→∞ se tiene S(x)=(1+o(1))N D_x. En todo x suficientemente grande vale |S(x)−N D_x|≤o(1)|N|D_x+O(D_x). En particular RH equivale al orden i_C≤i_W eventualmente. El conteo usa posiciones en la lista de primos y no aproxima distancias entre primos consecutivos por su media.

**Prueba.** En los extremos de la banda, W tiene signos opuestos y módulo ∼2Jx/L² por 386, mientras |S|=o(x/L²) por 377. Por ello C=S−W cambia también de signo, en sentido contrario. Si el valor en el extremo superior del umbral se alcanza en una meseta, el primo anterior de la banda ya lo alcanza. Los saltos de W son positivos por 387 y los de C, sus negativos. En el primo de cada cruce, W queda a distancia a lo sumo un salto de su nivel objetivo (0 para i_W y S para i_C). En toda la banda ese salto es O(D_x); por el perfil de 386 y S=o(x/L²), los dos primos satisfacen v=E/2−1/2+o(1). Por monotonía de v en p ocurre lo mismo entre ambos. Así, **cada** salto intermedio vale (1+o(1))D_x por 387, uniformemente. Restar W en los dos índices da la estimación, incluidos N negativo y los dos overshoots de extremo. Si N<0 entonces S<0, y si N>0 entonces S>0, por la definición de primeros cruces. En un empate |S|=O(D_x).

**Lectura del criterio.** Bajo RH se tiene S<0 eventualmente por 368, y por ello i_C≤i_W. Recíprocamente, si i_C≤i_W eventualmente, el único posible exceso positivo está en empates y es O(D_x)=o(√x) por 387. Esto excluye un cero exterior por 372. Más cuantitativamente, si Θ>1/2, la fórmula y 372 dan para cada signo e la igualdad

    limsup log(1+max(eN,0))/log x = Θ−1/2,

ya que D_x=x^(1/2+o(1)) y los errores de redondeo sólo cuestan O(1) en unidades de salto. Bajo RH los equivalentes de 367–368 incluso dan −N→∞: log(|S|/√x)=(1+log 2+o(1))L/log z por la silla real (véase también [la calibración para potencias fijas](SADDLE_FIXED_POWER_CALIBRATION.md)). En consecuencia log(−N) tiene el mismo equivalente. Esta escala condicional es subpotencial pero supera toda potencia de log x.

**Registro de revisión.** Los signos de los extremos tienen tamaño≫D_x, por lo que ambos cruces están dentro de la lista y sus estados anteriores también están disponibles. Escribir W(i_W)=r_W y W(i_C)=S+r_C, con0≤r_W,r_C≤O(D_x). La resta da S=W(i_C)−W(i_W)+r_W−r_C y fija el signo de la distancia N sin invertirlo. Si i_C<i_W, entonces S≤W(i_C)<0; si i_C>i_W, entonces S>W(i_W)≥0. Sólo en un empate cabe cualquier signo, y |S|≤O(D_x). La equivalencia del orden eventual admite precisamente ese margen, que es o(√x) y excluye las excursiones positivas de372 bajo una alternativa a RH. Los dos primos de cruce se localizan a v=E/2−1/2+o(1), y todo primo intermedio comparte esa localización por monotonía de v; por eso sumar un número variable de saltos conserva el error relativo uniforme. Bajo RH, log(D_x/√x)=O(h), despreciable frente a L/log z; dividir la silla de368 por D_x y usar |N|→∞ justifica la escala de log(−N), no sólo una cota de potencia.

Los niveles se definen mediante las sumas aritméticas separadas. La identidad W+C=S hace dependientes los dos cruces; la monotonía por sí sola no decide su orden. Falta una comparación aritmética entre sus índices.
