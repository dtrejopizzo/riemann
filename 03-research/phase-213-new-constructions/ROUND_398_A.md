# Dos sillas conjugadas y suficiencia condicional del umbral de masa

**Estado: PROVED, con revisión independiente de Rouché, las dos bandas, la fase y el techo condicional.** Sean κ₀=8(1+log 2)log 4 y p_* el menor primo terminal de 393. Bajo RH,

    b(p_*/z−4) → κ₀.

La parte nueva es el techo condicional. Sin RH se obtienen, a cada x grande, valores de ambos signos del pulso finito en cualquier franja terminal Y/z∈[4+k₁/b,4+k₂/b], k₁<k₂ fijos, con amplitud comparable a la de su silla compleja. El argumento permite variar continuamente el peso del último primo de cero a uno, como en la definición de p_*.

**Silla exacta.** Escribir l_p=log p y h_p=1 salvo el peso terminal en [0,1]. Sean β la silla positiva exacta con esos pesos, a_p=h_p p^(−β), y G(s)=Ls+(s−1/2)²/2+Σ log(1−h_p p^(−s)), con ramas dadas por las series en Re s>0. Tomar m igual a la media de l_p−b con pesos l_p a_p/(1+a_p)² y t_c=π/(b+m). Por el PNT m→μ de 397 uniformemente en la franja. La ecuación positiva es L+β−1/2=Σ l_p a_p/(1+a_p). En s_c=β+it_c, poner δ_p=t_c l_p−π=O(1/b). La contribución de cada primo a G' es −l_p a_p exp(−iδ_p)/(1+a_p exp(−iδ_p)); su término lineal en δ_p suma cero por definición de m. Por tanto G'(s_c)=O(L/b²), G''(s_c)=(1+O(1/b))Σ l_p²a_p/(1+a_p)²+1 con suma ≍Lb, y |G'''|≪Lb² en |s−s_c|≤1/b². Por Rouché aplicado a G' frente a su parte lineal, hay una única silla s_* en |s−s_c|≤C/b³ para C suficientemente grande: en la circunferencia el término lineal en el desplazamiento domina tanto la constante como el resto cuadrático. Es simple y continúa al variar el peso. Las constantes son uniformes por compacidad de la franja y los PNT de 395–397, que se aplican también a todo κ acotado (los bloques interiores de primos son los mismos).

**Integrar en la vertical de Re s_*.** La inversión del producto finito permite escoger directamente esa vertical. En la banda |t−Im s_*|≤ε/b² con ε fijo pequeño, Re G''≍Lb y |G'''|≪Lb²; por Taylor en la dirección vertical hay caída ≥cLb(t−Im s_*)². En la escala 1/√(Lb) el error cúbico tiende a cero. La contribución local con la normalización de Mellin es

    Z=(exp(G(s_*))/sqrt(2π G''(s_*))) · (1+o(1)),

con la raíz de parte real positiva y error relativo complejo uniforme. La banda negativa da el conjugado. Para el exterior se aplica la prueba de 397 con σ=Re s_*: cambiar β en O(b^(−3)) cambia todos los a_p por un factor 1+O(b^(−2)), de modo que M∼L/b, la media límite y la varianza son las mismas. El mínimo de la pérdida a Im s_* vale (π²V/2+o(1))L/b³ porque Im s_*=π/(b+m)+O(b^(−3)) y m→μ. Fuera de ambas bandas hay un margen c_ε L/b³ por 397, independiente del factor común x^σ exp((σ−1/2)²/2)∏(1+h_pp^(−σ)). La cola gaussiana da el ahorro de 397. En consecuencia el pulso es

    [2 exp(Re G(s_*))/sqrt(2π |G''(s_*)|)] · [cos(Im G(s_*)) + o(1)],

pues arg G''=o(1). El error aquí es aditivo dentro del corchete, no relativo cerca de un cero. El logaritmo del prefactor difiere de log A(Y) en O(L/b³): la pérdida en la banda cuesta O(L/b³), y mover la silla positiva a σ cuesta O(Lb·b^(−6)); los logaritmos de los prefactores cuestan O(log L).

**La fase recorre ambos signos.** Al incorporar el primo p con peso λ de 0 a 1, la fase continua Ψ=Im G(s_*) satisface exactamente

    dΨ/dλ=Im[−p^(−s_*)/(1−λ p^(−s_*))].

La dependencia de la silla desaparece por G'=0. En el primo terminal l_p=b+log 4+O(1/b) se tiene δ=Im(s_*)l_p−π=(π/b)(log 4−μ+o(1)), estrictamente positivo. La derivada es −p^(−σ)sin δ/|1+λ p^(−σ)exp(−iδ)|² y está entre −C/(Lb) y −c/(Lb). Al pasar al primo siguiente con peso cero, el producto y su silla son los mismos. Por PNT con resto clásico la franja contiene ≍(k₂−k₁)z/b² primos; el error exp(−c√b) es menor que 1/b. La variación total de Ψ es por tanto ≫L/b³→∞. Por continuidad alcanza múltiplos pares e impares de π, donde el equivalente anterior determina signos opuestos.

**Comparación con S.** Bajo RH y κ₀<k₁<k₂, 395 da uniformemente log(A/|S|)≥c L/b²: basta incluso la monotonía de la masa y el extremo izquierdo, omitiendo a lo sumo un primo de peso relativo despreciable. El coste O(L/b³) de las sillas firmadas no consume ese exceso. Los extremos de fase construidos dan valores por encima de |S| y por debajo de −|S| para el mismo x. El pulso finito es continuo en la interpolación, luego alcanza el valor S. Así limsup b(p_*/z−4)≤k₂; dejar k₂↓κ₀ y usar 394 concluye. Con 393 resulta la equivalencia entre RH y p_*≤(log x)^(2+o(1)) eventualmente. Queda abierta la dirección aritmética sustantiva: demostrar esa localización sin suponer RH.

**Registro de revisión.** La definición de m anula exactamente Σl_p a_p δ_p/(1+a_p)². El término i t_c de la gaussiana no se anula, pero es O(1/b) y está incluido en G'(s_c)=O(L/b²). En el círculo de radio C/b³, |G''(s_c)(s−s_c)|≍CL/b², la constante G'(s_c) cuesta O(L/b²) y el resto O(Lb²|s−s_c|²)=O(C²L/b⁴). Elegir C fijo grande y después x grande permite Rouché frente al término lineal, con una sola raíz simple. Las ramas por series son regulares en Re s>0 y la raíz local única coincide en los empalmes al pasar del peso1 al peso0 del siguiente primo.

El desplazamiento real O(b^(−3)) mantiene β en la franja de395–397. Sus momentos y las pérdidas angulares conservan los mismos límites; en particular, fuera de bandas de radioε/b² en torno a las nuevas sillas hay una brecha c_εL/b³. Dentro, el cociente del resto cúbico por el cuadrático es O(ε/b), y en la escala gaussiana es O(sqrt(b/L)). Esto justifica el equivalente complejo con error uniforme aditivo después de sumar los conjugados; no se afirma error relativo cerca de cos Ψ=0. La raíz cuadrada de G'' tiene argumento o(1), de modo que omitir ese argumento en el coseno cuesta sólo o(1).

Para la fase, p^(−s_*)=−p^(−σ)exp(−iδ) y log4−μ=2−log4>0. Esto fija el signo negativo de dΨ/dλ y el tamaño1/(Lb), uniformemente en la franja y enλ. Las ramas y la silla coinciden en cada empalme, así que Ψ es una fase real continua, no sólo definida módulo2π. El PNT con resto clásico cuenta≍z/b² primos en la franja, y su error relativo es O(b²exp(−c sqrt b))=o(1); por ello la variación total≫L/b³ recorre ambos signos. BajoRH, la desigualdad log(A/|S|)≫L/b² vence uniformemente las pérdidas O(L/b³), también con un último peso0. Así el teorema del valor intermedio alcanza el valor exactoS, y el techo para p_* no depende de redondear el peso ni de conocer la fase asintótica inicial.
