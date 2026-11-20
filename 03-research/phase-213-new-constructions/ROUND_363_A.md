# Ventana gaussiana y truncación a raíz de log x

En 362 se puede usar un peso bilateral g(u)=exp(−u²/2)/√(2π) y reducir la banda exigida a T=√(2 log x). Con c=1+1/log x y D_z de 362, RH equivale a que para cada ε>0 el módulo de

    (1/(2π)) ∫_{−T}^T x^(c+it) exp((c+it)²/2) D_z(c+it) dt

sea O_ε(x^(1/2+ε)) uniformemente en x grande y (log x)²≤z≤4(log x)². La cola retirada en esta nueva integral cuesta sólo O((log x)²) en módulo.

**Observable bilateral.** Mantener S,P,Q con sus coeficientes de 360, cambiando el peso a g(log(x/n)). El transformado bilateral de g es G(s)=exp(s²/2), entero sin ceros. Las sumas y sus derivadas convergen localmente de manera absoluta. Para 0<x≤1 cada observable y la derivada logarítmica de S son O_N(x^N) para cada N>1, uniformemente en z, ya que |g(u)|+|g'(u)|≪_N exp(Nu) para u≤0 y los coeficientes por entero cuestan O(log(2n)). Así se pueden usar dilataciones arbitrariamente pequeñas sin suponer soporte causal.

**Reemplazo del término de memoria.** En v=log x, la identidad μ log=−μ*Λ y g'(u)=−u g(u) dan

    dS(e^v)/dv + v S(e^v) = −P(e^v)−Σ_{k≥2,p}(log p) S(e^v/p^k).

Bajo RH la cota de Mertens y sumación parcial contra g y g' dan |S|+|dS/dv|≪_ε x^(1/2+ε) para x≥1: tras el cambio n=x exp(−u) las integrales de |g'| y |g''| con peso exponencial fijo convergen. La identidad controla P con una pérdida logarítmica. La inversión Q_z=K_z(P−L_z S) de 359 y la norma de Euler x^o(1) dan el techo requerido para Q, empezando con exponente menor.

**Sentido inverso sin estimar a priori la derivada.** Fijar σ=1/2+ε, 0<ε<1/4. Usar dos envolventes finitas en 0<t≤X,

    A(X)=sup |S(t)|/t^σ,     B(X)=sup |P(t)|/(t^σ log(2+t)).

Para todo λ>0 hay una constante C_λ tal que B(X)≤C_λ+λ(A(X)+B(X)). En efecto en el bloque escalar x aplicar P=L_z S+U_z Q_z de 359 con z=log²x. En unidades de x^σ, el coste de L_z S es O_ε((log x)^(1−2ε) A(x)); las ramas d≤√x usan la hipótesis con pérdida ε/2 y cuestan O(x^(−ε/2+o(1))). Para d>√x, la primera identidad Q_z=K_z(P−L_z S) en cada hijo t=x/d cuesta, en sus propias unidades t^σ, (A(x)+B(x))x^o(1): la norma Euler se calcula al corte congelado y log(2+t)≪log x incluso en los hijos pequeños. La cola de retorno cuesta x^(−ε/4+o(1)) como en 359. Estas identidades siguen siendo válidas para el peso bilateral por convergencia absoluta, usando el decaimiento a escalas pequeñas. Dividir por log(2+x), tomar x grande y absorber el tramo compacto en C_λ.

Por otra parte A(X)≤C+3B(X). Para verlo, tomar F(v)=e^(−σv)S(e^v). Su ecuación tiene lado izquierdo F'+(v+σ)F y el módulo del derecho está acotado por B(X)log(2+e^v)+C_σ A(X) para v≤log X. Aquí C_σ=Σ_{k≥2,p}(log p)p^(−kσ)<∞. Por encima de v₀ fijo suficientemente grande el derecho cuesta a lo sumo (v+σ)(2B(X)+A(X)/4). El factor integrante exp(v²/2+σv) da |F(v)|≤|F(v₀)|+2B(X)+A(X)/4. Incorporar el tramo anterior, tomar el supremo y reordenar da la desigualdad afirmada. Elegir λ pequeño en la primera desigualdad acota ambas envolventes. Como ε puede ser arbitrariamente pequeño, la transformada bilateral de S prolonga G(s)/ζ(s) holomórficamente en Re s>1/2. G no pierde ningún polo de 1/ζ.

**Truncación.** En la recta c, |G(c+it)|=exp(c²/2−t²/2) y |D_z(c+it)|≪(log x)² por 362. Invertir absolutamente y usar ∫_T^∞exp(−t²/2)dt≤exp(−T²/2)/T. Con T=√(2 log x), el factor x^c exp(−T²/2)=e; queda el error polilogarítmico anunciado. Esto es una reducción de altura en la integral del nuevo peso. La cancelación en la banda interior no está demostrada y no se obtiene una nueva ventana de soporte del paper 47.
