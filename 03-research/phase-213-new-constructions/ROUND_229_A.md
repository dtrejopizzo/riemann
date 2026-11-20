# Diagnóstico sin núcleo: el error ordinario en cada banda de potencias

Sea E(x)=ψ(x)−x+1 para x≥1 y B=sup_ρ |Re ρ−1/2|. Para cada 0<α<1 fijo se tiene el límite ordinario

    lim_(X→∞) log(1+∫_(X^α)^X E(x)² dx/x²)/log X = 2B.

En particular bastaría un techo X^o(1) para esa media en una sucesión X→∞, para un solo α fijo. La afirmación vale aunque no exista un cero extremo. Reemplazar E por ψ−x conserva el límite por desigualdad triangular en L²(dx/x²), ya que la diferencia tiene norma acotada. Es una consecuencia sobre medias del error clásico, no una cota aritmética nueva para B.

**Quitar la acumulación ponderada de 228.** Escribir t=log x, T=2N, g=g_N, F(t)=exp(−t/2)P_N(exp t), Y(t)=exp(−t/2)g(t)E(exp t). En [0,T], integración por partes contra dE da

    F(t)=Y(t)+∫₀ᵗ exp(−(t−s)/2) (s/(2N))Y(s)ds.

A la inversa, integrar g⁻¹ contra dP_N y multiplicar por exp(−t/2)g(t): Y=F menos el mismo operador aplicado a F, con factor adicional g(t)/g(s)≤1. No hay término inicial porque E(1)=0. Como s/(2N)≤1, ambas normas L² en [0,T] se mayoran entre sí con factor 3 por Young. En la cola de 228, ∫_X^∞P_N(r)²dr/r²=F(T)² con X=exp(T). En el extremo Y(T)=O(1/√N) por Chebyshev; la convolución que se añade en F(T) cuesta O(||Y||₂) por Cauchy–Schwarz. Además ∫dν_N(x)/x=∫P_N(r)dr/r², cuyo cuadrado está dominado por ∫P_N(r)²dr/r². En un intervalo fijo próximo y a la derecha de 1 donde E(x)=1−x, se ve ||Y||₂²≳1/N. Así V_N de 228 es comparable, con constantes absolutas, a ||Y||₂². Al extender el integral de |Y|² sin corte hasta t=∞, Chebyshev da para la cola O(1/N) por t−t²/(2N)≤−(t−2N) si t≥2N. En consecuencia, poniendo dμ(t)=exp(−t)E(exp t)²dt,

    W(N)=∫₀^∞ exp(−t²/(2N)) dμ(t),       log W(N)/N→2B².

El factor 4πN retirado es sólo polinomial. Por monotonía de W, el límite se extiende de enteros a N real positivo.

**En qué escala se concentra la energía.** Si B>0, para cada 0<ε<2B, la fracción de W(N) en |t/N−2B|≥ε decae exponencialmente. Para t≥(2B+ε)N comparar con W((1+h)N): el logaritmo del cociente con W(N), dividido por N, tiene limsup a lo sumo

    2B² h − h(2B+ε)²/[2(1+h)] < 0

si h>0 es suficientemente pequeño. Para t≤(2B−ε)N comparar con W((1−h)N); el techo correspondiente es −2B²h+h(2B−ε)²/[2(1−h)]<0. Sólo se usa positividad de μ y el límite ordinario de 228.

**Quitar la gaussiana.** Poner L=log X. Si B>0, con N=L/(2B) se tiene μ([0,L])≤exp(L²/(2N))W(N), de tasa superior 2B por unidad de L. Si B=0 tomar N=cL y hacer c→∞ para obtener tasa superior cero. El 1 del enunciado da el piso en este último caso.

Para el piso cuando B>0 fijar α<λ<1 y tomar N=λL/(2B). Elegir ε suficientemente pequeño para que [(2B−ε)N,(2B+ε)N] esté dentro de [αL,L]. Ese intervalo recibe (1−o(1))W(N) con la gaussiana. Al retirarla su masa sin peso es al menos exp((2B−ε)²N/2)(1−o(1))W(N). Por tanto el límite inferior por unidad de L es ≥λ[2B²+(2B−ε)²/2]/(2B). Hacer ε↓0 y después λ↑1 concluye para TODOS los X grandes, sin seleccionar alturas favorables.

**Consecuencia para la búsqueda.** Si B>0, para cada α y cada η>0, en toda banda [X^α,X] suficientemente alta hay un punto x con |E(x)|/√x≥X^(B−η), pues la longitud de la banda en t es sólo (1−α)log X. No se afirma lo mismo para bandas [X,2X]. La transferencia inversible muestra que separar el acumulado de 228 de su gaussiana no aporta una desigualdad adicional. El paso nuevo respecto de 219 (control uniforme puntual en todas las celdas) es que aquí basta UNA subsucesión de medias cuadráticas en bandas de potencias. No se establece ese techo para ninguna subsucesión ni prioridad frente a la literatura tauberiana.
