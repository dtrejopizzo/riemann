# Ceros de Mellin de un posible extremizador negativo

Si Γ>0, la transformada de Mellin U(s)=∫₀¹ u(x)x^(s−1)dx de cualquier extremizador de 034 tiene, en Re s>1/2, exactamente un cero: s=1, de orden uno. Se trata de la transformada del perfil; la conclusión no se refiere a los ceros de ζ.

**Cotejo.** P47, prueba de thm:nyq-cone, ya refleja un cero para conservar la autocorrelación. La compactificación de 033 usa el factor especial s/(s−1). La razón para usar la operación aquí es que la energía aritmética y la norma que normaliza su defecto se miden en dos rectas distintas. La conservación en una produce una mejora estricta en la otra.

**Reflexión admisible.** Sea g(t) la derivada de u(exp(−t)) en t≥0, extendida por cero al resto de la recta. Su norma L² al cuadrado vale I(u). Como u(1)=0, la primitiva de g desde cero es u(exp(−t)) y crece a lo sumo como √t ||g||₂. Por integración por partes su transformada de Laplace satisface G(s)=sU(s) en Re s>0. Sea z un cero de U con b=Re z>1/2. Definir en la recta

    h(t)=−∫ₜ^∞ exp(z(t−v))g(v)dv,     g₁=g+(2b−1)h.

El núcleo de convolución de h está en L¹. Además h(t)=−exp(zt)G(z)=0 para t≤0 y h′=zh+g. Por tanto h pertenece a H¹ y g₁ es causal y pertenece a L². Integrar g₁ desde cero define un perfil u₁ en X según la caracterización de 034 (traza cero en x=1 y energía finita). Transformando la ecuación de h, su factor en Laplace es 1/(s−z), con singularidad removible en el producto con G. En consecuencia

    U₁(s)=U(s) (s−1+conj(z))/(s−z).

Si z≠1 se conserva U₁(1)=0. Si z=1 basta que el cero original tenga orden al menos dos. En ambos casos u₁ pertenece a X₀.

**Dos normas.** En Re s=1/2 el factor tiene módulo uno, por lo que las integrales B_L de 033 son idénticas y también sus límites B∞. Sobre Re s=0, donde Plancherel para g da I, el cuadrado de su módulo en iτ es

    [(b−1)²+(τ−Im z)²]/[b²+(τ−Im z)²] < 1.

Esta identidad de multiplicadores en la frontera se obtiene también transformando h′=zh+g en Fourier. Como g no es nula, I(u₁)<I(u). Si B∞(u)=−Γ I(u)<0, el cociente de u₁ quedaría estrictamente por debajo del mínimo. Se permiten perfiles complejos en X₀; el mínimo de una forma real tampoco cambia al complejificar. Esto excluye todo cero propuesto excepto el cero simple en 1, que es obligatorio por la media.

**Consecuencia en momentos reales.** Orientar el extremizador real unitario como en 034. Entonces U(s)>0 para s real mayor que 1 y U(s)<0 para 1/2<s<1. En efecto u(exp(−t))/t→1 en t↓0 y |u(exp(−t))|≤√t. Integrando contra exp(−st) y separando una vecindad de cero y su cola exponencial se obtiene s²U(s)→1 al crecer s real. La continuidad y el cero simple en 1 dan los signos indicados. Estas restricciones describen un hipotético extremizador; queda pendiente una desigualdad aritmética que lo excluya.

Prueba de reflexión y pertenencia a X₀ revisada independientemente. PROVED como implicación condicional.

## Una franja uniforme que incluye la recta media

Sea λ₊=sup B∞(f)/I(f) sobre X₀ no nulo. Es finito por 033 y no negativo por compacidad en dimensión infinita. Bajo la hipótesis Γ>0, todo cero z de U en Re z>0, salvo el cero simple obligatorio en 1, satisface

    Re z ≤ λ₊/[2(λ₊+Γ)].

Así la distancia mínima desde cualquier cero opcional del semiplano derecho hasta la recta media, por su izquierda, es Γ/[2(λ₊+Γ)]. Es una cota dependiente del defecto hipotético, sin margen numérico incondicional.

**Prueba.** Escribir b=Re z. Usar la convolución causal h de la primera parte, que sólo requiere b>0. Su primitiva en variable logarítmica define v∈X y la Mellin de v es V(s)=U(s)/(s−z). Si z≠1 se conserva la media cero. Lo mismo ocurre en z=1 si el cero es múltiple. El vector v no es nulo. En la recta media U=(s−z)V y el multiplicador híbrido es real. Por tanto la parte real de su forma polarizada satisface Re B_L(u,v)=(1/2−b) B_L(v). Pasar al límite por 032–033. En la recta Re s=0 usar las transformadas de las derivadas en log, relacionadas por el mismo factor (ecuación h′=zh+g). Plancherel da Re I(u,v)=−b I(v). La ecuación del extremizador Au=−Γu implica exactamente

    (1/2−b) B∞(v) = Γ b I(v).

Para b=1/2 esto es imposible. Para b>1/2 el cociente de v sería estrictamente menor que −Γ. Para 0<b<1/2 el cociente es positivo y a lo sumo λ₊, lo que da la cota. El argumento sólo divide por s−z de manera removible en el perfil, incluso si z está sobre la recta de integración. PROVED como implicación condicional, con auditoría independiente.

La descomposición alternativa de módulos de numeradores racionales en sumas de cuadrados se cotejó con POWER_SCALAR_BRIDGE_017 y su auditoría. Al volver a un problema de signo en una familia de numeradores, se descartó como vía de cierre de esta ronda.

El antecedente más cercano encontrado para probar la ecuación propia contra un cociente es R160_X_C1 §5, Theorem G; su §6 estudia exclusión de ceros de extremizadores por Blaschke (auditoría R163_501 §§1–2). La diferencia aquí es la cota cuantitativa obtenida al evaluar el mismo cociente en dos rectas distintas. No incorpora una desigualdad nueva para los pesos de von Mangoldt.

## Filtros con polo a la izquierda: valor exacto del problema minimax

Sea a>0 fijo. Para u∈X₀ de Mellin U y γ real definir vγ por Vγ(s)=U(s)/(s+a−iγ). En la variable de la derivada logarítmica esto es convolución con exp((−a+iγ)t)1_{t≥0}, en L¹. Por tanto vγ pertenece a X y conserva la media nula. Para u≠0 es siempre no nulo. Escribir R=B∞/I, λ₋=inf R y k=a/(a+1/2). Entonces

    inf_{u≠0} sup_{γ∈ℝ} R(vγ) = k λ₋.

En particular, si hay un extremizador negativo, *cada centro* da el mismo cociente negativo kλ₋ al filtrar ese extremizador.

**Ecuación y promedio.** Para Au=λu, el mismo cálculo de dos rectas de la sección anterior da (a+1/2)B∞(vγ)=λ a I(vγ) sin suponer ningún cero de U. En general la integración en γ da

    ∫ I(vγ)dγ = (π/a) I(u),      ∫ B∞(vγ)dγ = [π/(a+1/2)] B∞(u).

La primera igualdad sigue por Plancherel y la integral del núcleo de Cauchy. Para la segunda fijar el corte L y aplicar Fubini (la integral con |h_L| contra |U|² en la recta media es finita). Pasar a B∞ usando la convergencia en norma de las formas y la primera igualdad. El promedio de R(vγ) con peso I(vγ) vale así kR(u); en particular el supremo es al menos ese valor. La igualdad minimax se obtiene evaluando en un autovector mínimo cuando existe. Si λ₋=0 no es autovalor, la compacidad proporciona autovectores con autovalores que tienden a cero, y para cada uno el cociente filtrado es constante en γ.

**Obligación de signo.** Para un ancho a fijo, bastaría que para cada u≠0 hubiese algún centro γ con B∞(vγ)≥0. En efecto, un mínimo negativo proporcionaría una familia estrictamente negativa en todos los centros. Recíprocamente, la positividad global implica esa condición. La identidad minimax cuantifica la equivalencia; no demuestra la existencia del centro favorable. En particular el modelo compacto B(u)=−|U(1/2)|² tiene mínimo negativo y satisface las mismas identidades (evaluar U(1/2) es continuo en X₀ y no es idénticamente cero allí). La fórmula de promedio en este modelo se comprueba directamente en s=1/2. La positividad del núcleo de Cauchy por sí sola no certifica los pesos originales.

Cotejo: R160_X_C1 §5 y los filtros de POWER_SIGNED_TRANSFER_014 y POWER_SCALAR_BRIDGE_017 anticipan el uso de cocientes. El valor minimax en la norma de 033 es la afirmación específica aquí. Identidad y limitaciones auditadas independientemente.

## Qué se pierde al aplicar el filtro dos veces

Sea u un autoestado con autovalor λ y sea v_j el perfil de Mellin U(s)/(s+a−iγ)^j para j=1,2. Poner d=a+1/2, B_j=B∞(v_j), I_j=I(v_j). Vale la identidad exacta

    B₂ = λ [ (a²/d²) I₂ − I₁/(4d³) ].

En efecto Re B∞(u,v₂)=2d²B₂−B₁: en la recta media la parte real del factor cuadrático es 2d²−|s+a−iγ|². La igualdad pasa de cada corte finito por continuidad. En la recta de energía se obtiene análogamente Re I(u,v₂)=2a²I₂−I₁. Usar la ecuación propia y B₁=λ(a/d)I₁. Así, para λ<0, el doble filtro produce energía positiva exactamente cuando I₁/I₂>4a²d. Una energía positiva obtenida tras dos filtros es por tanto compatible con un mínimo negativo.

**Verificación de esa posibilidad en un modelo real.** En el mismo X₀, sea e_y el representante unitario de evaluación de la Mellin en s_y=1/2+iy, con e_{−y} conjugado de e_y, y P_y su proyección ortogonal de rango uno. Considerar A₀=−P₀+(P₄+P_{−4})/8. Es compacto, real, y cada forma de evaluación escala por r bajo S_r. Para calcular los productos normalizados, en coordenadas de derivada logarítmica la evaluación en s es la integral de g contra exp(−st)/s y la media cero elimina la dirección exp(−t). El Gram proyectado de dos evaluaciones s,w es, salvo convención de conjugación,

    [(s−1)(conj(w)−1)]/[s conj(w)(s+1)(conj(w)+1)(s+conj(w))].

Al normalizar resulta |〈e₀,e_{±4}〉|²=1/17. El test e₀ da energía −1+1/68<0 y la parte negativa tiene rango uno, luego el mínimo es simple y admite un autovector real u. Sea −l su autovalor (0<l≤1), α su evaluación normalizada en 0 y b el vector de evaluaciones normalizadas en ±4; |b₊|=|b₋|. Evaluar la ecuación propia en esas dos frecuencias da (l Id+G/8)b=αc, con G el Gram de e₄,e_{−4} y ||c||²=2/17. Como ||G||≤2 se deduce |b₊|²/8≥2|α|²/(25·17). Aquí α≠0 por la energía negativa.

Tomar a=1/2 y γ=4. El doble filtro multiplica el término negativo por 1/289 y deja intacto el término positivo en +4. Como 2/(25·17)>1/289, la energía del doble filtro es estrictamente positiva, mientras la del primero es estrictamente negativa por la identidad del autoestado. Las identidades de las dos rectas son exactas también en este modelo de tres evaluaciones. El contramodelo conserva la simetría real y el escalado. No utiliza los pesos de von Mangoldt; distingue el criterio global con un filtro de una extrapolación inválida a dos. 

Antecedente de la cautela sobre iteración: POWER_PRIME_TRANSFER_014 §4 observa que aplicar el primer filtro cambia el dato de entrada. La identidad del segundo filtro y las cotas exactas del modelo simétrico recibieron revisión matemática independiente.

## Qué detecta realmente un centro de frecuencia grande

Fijar a>0 y suponer g(t)=(d/dt)u(exp(−t))∈H¹(0,∞). Escribir c=g(0), la traza desde la derecha. Con el primer filtro de arriba se tiene, cuando |γ|→∞,

    γ² B∞(vγ) → B∞(u),        γ² I(vγ) → I(u)+|c|²/(2a).

No se presupone esta regularidad para un extremizador de 034. Sí incluye todos los tests suaves compactos en (0,1), que son densos tras imponer la media cero.

**Prueba.** Si G(it) es la Fourier de g extendida por cero, el error en la derivada logarítmica de (−iγ)vγ−u tiene transformada −(a+it)G(it)/(a+i(t−γ)). Separar g=c exp(−at)+g₀ en la semirrecta. El primer término produce exactamente −c exp((−a+iγ)t)1_{t≥0} en la derivada del error. El segundo cumple g₀(0)=0, por lo que su extensión por cero está en H¹ de toda la recta. Su numerador está en L² y el denominador tiene módulo ≥a y crece puntualmente. Por convergencia dominada su contribución tiende fuertemente a cero. El término exponencial converge débilmente a cero por Riemann–Lebesgue y tiene norma al cuadrado |c|²/(2a). Esto prueba el segundo límite y la convergencia débil de (−iγ)vγ a u en X₀. La compacidad de la forma completa de 034 da el primer límite, incluidos todos los pesos aritméticos.

**Alcance para el signo.** Si existe un test negativo, por continuidad y densidad existe uno suave compacto negativo. Para ese test y cualquier ancho fijo, todos los centros de módulo suficientemente grande tienen energía filtrada estrictamente negativa. Por tanto, demostrar que para todo test suave negativo hay un centro favorable exigiría controlar centros en un intervalo acotado que puede depender del perfil. El límite no predice un cambio de signo en ese intervalo. Con c=0 se recupera incluso el cociente R(u) al enviar el centro al infinito. PROVED tras revisión independiente.
