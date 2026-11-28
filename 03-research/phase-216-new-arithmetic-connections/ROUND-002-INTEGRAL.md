# Ronda 002 — El coste exacto del proyector diagonal es la diferente

2026-11-28. Resultado: cálculo completo en el tensor regular de un cuerpo de números. **Es una consecuencia de álgebra clásica de separabilidad y diferentes, no una nueva área ni un teorema de prioridad reclamable.** Sirve para separar un coste aritmético real de un coste introducido por la elección de realización.

## 1. Enunciado exacto, con tres nociones de coste distintas

Sea E/Q un cuerpo de números, O=O_E, D=D_{E/Q} la diferente y Δ_E su discriminante. Para r≥2 escribimos A_r=E^{⊗_Q r}, T_r=O^{⊗_Z r}. Sea μ_r:A_r→E la multiplicación y e_r el idempotente correspondiente al factor diagonal: tras extender a una clausura algebraica, vale 1 en las tuplas de embeddings iguales y 0 en las demás. La aplicación

\[
\iota_r:E\longrightarrow e_rA_r,\qquad a\longmapsto(a\otimes1\otimes\cdots\otimes1)e_r
\]

es inversa de μ_r restringida al sumando diagonal. Valen:

\[
\boxed{\{a\in E:\iota_r(a)\in T_r\}=D^{r-1}}.\tag{1}
\]

Definiendo P_r=e_rT_r y J_r=T_r∩e_rA_r, tenemos

\[
\mu_r(P_r)=O,\qquad\mu_r(J_r)=D^{r-1},\qquad
P_r/J_r\simeq O/D^{r-1}.\tag{2}
\]

En consecuencia

\[
[P_r:J_r]=|\Delta_E|^{r-1}.\tag{3}
\]

Éste es un índice entre dos retículos del mismo espacio diagonal; **no** es el determinante del proyector en A_r, que tiene núcleo y determinante cero.

El entero positivo mínimo m_r tal que m_re_rT_r⊂T_r satisface

\[
v_p(m_r)=\max_{\mathfrak p\mid p}
\left\lceil\frac{(r-1)d_{\mathfrak p}}{e_{\mathfrak p}}\right\rceil,
\quad d_{\mathfrak p}=v_{\mathfrak p}(D),\quad
e_{\mathfrak p}=v_{\mathfrak p}(p).\tag{4}
\]

El ideal de (1), el índice de (3) y el denominador escalar de (4) son datos distintos. Confundirlos puede introducir pérdidas falsas. En particular m_r≤m_2^{r-1}, pero puede haber desigualdad estricta.

## 2. Prueba completa

Elegimos una base integral b₁,…,b_d de O y su base dual b₁*,…,b_d* para Tr_{E/Q}(xy). Por definición del dual de traza,

\[
D^{-1}=\bigoplus_i\mathbb Zb_i^*.
\]

El idempotente de separabilidad es e₂=Σ_i b_i*⊗b_i. Para comprobarlo, tras descomponer E sobre una clausura algebraica, la dualidad de traza se convierte en dualidad de coordenadas: esa suma tiene componente 1 en la diagonal y 0 fuera de ella. En particular es idempotente y μ₂(e₂)=1. No se necesita una base monógena ni una hipótesis de ramificación moderada.

Colocando e₂ en las posiciones 1,j obtenemos

\[
e_r=\prod_{j=2}^r e_{1j}
=\sum_{i_2,\ldots,i_r}
(b_{i_2}^*\cdots b_{i_r}^*)\otimes b_{i_2}\otimes\cdots\otimes b_{i_r}.
\]

La primera igualdad se verifica en componentes: exigir igualdad del primer embedding con cada uno de los restantes equivale a exigir que todos sean iguales. La segunda es la expansión literal del producto.

Ahora T_r es libre como O-módulo por el primer factor, con base b_{i₂}⊗⋯⊗b_{i_r} en los restantes. Por ello ι_r(a) pertenece a T_r si y sólo si todos los coeficientes a b_{i₂}*⋯b_{i_r}* están en O. Los productos de bases duales generan, como ideal fraccionario de O, exactamente (D⁻¹)^{r−1}. Como D es invertible en el dominio de Dedekind O, esto equivale a a∈D^{r−1}. Prueba (1).

Para t∈T_r, e_rt=ι_r(μ_r(t)). Puesto que μ_r(T_r)=O, se deduce (2). La identidad clásica N(D)=|Δ_E| y multiplicatividad de norma dan (3). Finalmente m_re_rT_r⊂T_r equivale a m_re_r∈T_r, porque T_r es un anillo con unidad. Por (1), equivale a m_r∈D^{r−1}. Comparar valoraciones en cada primo de O demuestra (4).

Estas pruebas cubren todos los primos, también los salvajemente ramificados. Para órdenes no maximales no se puede sustituir automáticamente el módulo dual por una potencia de un ideal invertible: se debe rehacer el paso de invertibilidad.

## 3. Cuatro factores y ejemplos que distinguen índice y denominador

Con r=4 la intersección integral del sumando diagonal corresponde a D³ y el índice a |Δ_E|³. Para E=Q(i), D=(2i) y Δ_E=−4: el índice es 64 pero el denominador escalar mínimo es 8. Aquí

\[
e_4=\frac18\prod_{j=2}^4(1-i_1i_j),
\]

donde i_j actúa en el j-ésimo factor. La expansión en la base tensorial tiene coeficientes ±1/8; el denominador 8 es realmente necesario.

Para E=Q(√5), D=(√5), Δ_E=5: con cuatro factores el índice es 125 y el denominador escalar mínimo es 25. Multiplicar tres veces el denominador de e₂ daría 125, una cota correcta pero no óptima. La fórmula (4) explica la mejora: e_𝔭=2, d_𝔭=1 y ceil(3/2)=2.

El programa [round002_projector.py](experiments/round002_projector.py) expande e_r con aritmética racional exacta y comprueba e_r²=e_r y denominadores mínimos para r=2,3,4,5 en ambos cuerpos. Resultados: Q(i): 2,4,8,16; Q(√5): 5,5,25,25. Es un control independiente de ejemplos, no un sustituto de la prueba general.

## 4. Lo que el cálculo NO dice: tensor sobre O frente a sumando dentro del tensor sobre Z

El cociente balanceado O⊗_O⋯⊗_O O≅O está definido integralmente. La multiplicación μ_r:T_r→O es sobreyectiva e integral; incluso admite la sección Z-lineal a↦a⊗1⊗⋯⊗1. Esa sección no tiene las propiedades de un sumando diagonal compatible con las distintas acciones de E.

El denominador aparece al exigir la sección canónica A_r-lineal de μ_r, es decir ι_r. Por tanto:

- Construir directamente el tensor balanceado sobre O no obliga a pagar |Δ_E|^{r−1}.
- Realizarlo como el sumando diagonal de T_r por e_r sí obliga a distinguir el retículo proyectado P_r de la intersección J_r; la diferencia está calculada exactamente arriba.
- Identificar un tensor geométrico con alguno de estos retículos exige una prueba adicional. La sola existencia de un proyector racional no la proporciona.

Para módulos libres M_i=O^{n_i}, descomponer por sus bases reduce a ∏_i n_i copias del cálculo regular. El índice correspondiente es |Δ_E|^{(r−1)∏n_i}; el denominador escalar sigue siendo m_r, si todos los n_i son positivos. No se afirma aquí ese exponente para retículos geométricos arbitrarios sin comprobar su relación con el modelo libre.

## 5. Aplicación posible a cuatro factores CM

Si cuatro objetos tienen acciones de un mismo cuerpo CM E y se exige conservar únicamente el componente donde coinciden las cuatro acciones, el modelo racional pertinente puede ser e₄. Si se conjuga alguna acción por un automorfismo de E, el idempotente se transporta por un automorfismo integral del tensor y el coste regular no cambia: la diferente es invariante por automorfismos de E.

Pero seleccionar ciertos tipos CM, pesos o caracteres no es necesariamente seleccionar toda la diagonal. Tampoco todo objeto con acción CM posee el retículo tensorial regular de este cálculo. Antes de insertar D³ en una fórmula de periodos o covolúmenes hay que identificar: cuerpo común de acción, tensor base, idempotente concreto y retículo de realización. Este documento no afirma que una construcción particular de los papers 49–56 cumpla esos requisitos.

## 6. Comparación fuerte con textos completos: el mecanismo es clásico

En *The Book of Involutions*, Knus–Merkurjev–Rost–Tignol, §18, pp. 285–286, las proposiciones 18.10 y 18.12 caracterizan el idempotente diagonal y dan su expresión mediante bases duales de traza. Se leyó el pasaje completo y sus demostraciones en el [PDF del texto](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/involutions.pdf).

El [Stacks Project, §49.6, lemas 49.6.6–49.6.7](https://stacks.math.columbia.edu/tag/0BVK), identifica el aniquilador del ideal de la diagonal con el dual del módulo dualizante; su imagen bajo multiplicación es la diferente de Noether. El [§49.8](https://stacks.math.columbia.edu/tag/0BW0) formula la diferente mediante el dual de traza. Ambos textos completos fueron consultados. Para el caso monógeno, el [ejemplo 49.12.5](https://stacks.math.columbia.edu/tag/0BWB) recupera el generador f′.

Así, el caso r=2 ya está descrito por la teoría clásica y r factores se obtiene por multiplicación y bases duales. No encontrar la fórmula (1) escrita con exactamente esta notación no la convierte en un descubrimiento independiente. La cuenta de cuatro factores es útil para normalizaciones, no evidencia de un área inexistente en la literatura.

## 7. Qué pregunta podría quedar después de retirar esta parte clásica

Una contribución sustantiva exigiría demostrar que un **retículo geométrico específico** realiza el tensor balanceado sin pagar toda la pérdida de la intersección diagonal, y a la vez conserva polarización, Frobenius y correspondencias de intercambio con sus constantes exactas. Si el dato exige precisamente J_r, (1) impide eliminar esa pérdida por una mera renormalización verbal. Si exige sólo el cociente balanceado, imponerla sería artificial.

El siguiente experimento matemático debe ser un cuadrado concreto de dos composiciones CM con cuatro retículos identificados: comparar sus imágenes integrales dentro del mismo espacio racional y calcular el ideal de discrepancia. Antes de conocer ese cuadrado, llamarlo una teoría nueva sería prematuro. La novedad potencial estaría en una identificación geométrica o una cancelación aritmética adicional que no se deduce de separabilidad; no en el proyector ni en la potencia de la diferente.
