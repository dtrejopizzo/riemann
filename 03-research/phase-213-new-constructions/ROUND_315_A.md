# Coste inevitable de las dos orientaciones del saldo para toda la matriz de divisores

Sea D=x^o(1), λ₁=1 y w_λ la familia de pesos de 314. Para casi todo t fijo en [1,2] y cada V fijo arbitrariamente grande, existen dos intervalos fijos de argumentos contenidos en (V,∞), uno con B_t estrictamente positivo y otro con B_t estrictamente negativo. En cada intervalo la suma de los valores absolutos w_λ(n)|B_t(x/n)|, sobre los índices cuyo argumento pertenece al intervalo, es al menos

    c_(V,t) x log x / log²(2D).

El umbral y la constante pueden depender de los intervalos, pero la desigualdad es simultánea en todos los vectores reales normalizados, incluso elegidos según x. Vale también para v_λ de 314, que domina a w_λ punto a punto. Por tanto ningún vector de esa matriz puede hacer despreciables las contribuciones negativas en módulo conservando la muestra principal con coeficiente uno. La estimación no excluye su cancelación firmada con las positivas.

**El mínimo exacto de la densidad.** Usar la base ortogonal y la inversión de 314, ahora en s=1. Si N_d=||Z_d||², la normalización dice 1=Σ μ(d)q(d)b_d y h_λ(1)=Σ N_d b_d². Por Cauchy–Schwarz y la invertibilidad del cambio triangular,

    min_(λ₁=1) h_λ(1) = 1/G_D,    G_D=Σ_(d≤D) μ²(d) ∏_(p|d) q_p(1)/(1−q_p(1)).

Aquí q_p(1)=2/p−1/p² es la probabilidad de exponente al menos uno; se alcanza el mínimo tomando b_d proporcional a μ(d)q(d)/N_d. Los índices no libres de cuadrados están incluidos en la optimización. Por el producto de Mertens, G_D≤∏_(p≤D)(1−1/p)^(−2)≪log²(2D). Además, sin normalizar, h_λ(1)≥D^(−10)||λ||∞² por la misma inversión: cada probabilidad de cola es ≥p^(−e) y 1−r_e≥1/4, suficiente para N_d≥d^(−8).

**Masa en cualquier intervalo proporcional.** Con A=h_λ(1) y E como en 311, para v≥D⁴ el sumatorio de w_λ hasta v vale v(A log v+E)+O(√v D⁶||λ||∞²), por la norma de 314 y la fórmula del divisor. Congelar λ y D, incluso si dependen de x. En v=√x la no negatividad obliga a E≥−(A/2)log x−o(A), ya que D=x^o(1). Restar las fórmulas en v=bx y v=ax con 0<a<b fijos. Los términos con log a y log b cuestan O_(a,b)(Ax), y el error es o(Ax) uniformemente en λ. Queda una masa ≥(b−a)Ax log x/3 para x grande. Así la cota del párrafo anterior se convierte en un límite inferior para muestras en intervalos reales, no sólo para un multiplicador de Dirichlet.

**Existen ambos signos a argumentos arbitrariamente grandes.** Para las frecuencias genéricas de 307, D_t tiene un polo de orden ≥2 en un cero crítico fijo ρ. El Mellin del sumatorio B_t(v) es D_t(s)/s. Si B_t tuviera eventualmente un solo signo, Landau y la regularidad real en s>1/2 darían convergencia absoluta en ese semiplano. En s=1/2+h el Mellin permanece acotado según 307. Tras quitar un compacto, la transformada a esa abscisa real dominaría el módulo en ρ+h, contradiciendo el polo (si hay un polo interior, la convergencia ya es imposible). De ahí que para cada V existan dos intervalos entre enteros mayores que V con signos estrictamente opuestos. En cada uno B_t es una constante no nula. Los índices n correspondientes ocupan un intervalo proporcional a x y la estimación de masa prueba el enunciado.

En particular para 0≤t≤1 y antes del recorte de 311 se pueden usar directamente los argumentos [1,2) y [2,3), donde B_t vale 1 y 1−2(1+cos(t log 2)), respectivamente. El argumento de polos es lo que permite situar las dos contribuciones después de cualquier recorte fijo, a frecuencia genérica. No se afirma una constante uniforme para un recorte V(x) prescrito que crezca con x. El mínimo cuadrático es la optimización elemental de tipo Selberg; lo que restringe aquí es su consecuencia para las dos orientaciones del saldo B_t en el problema de extracción.
