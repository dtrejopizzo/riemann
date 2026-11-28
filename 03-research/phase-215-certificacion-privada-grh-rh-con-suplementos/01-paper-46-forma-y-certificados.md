# Paper 46 Forma de Weil y certificados numéricos

**Actualización de la segunda auditoría:** ambas ventanas quedaron verificadas mediante programas y argumentos reproducibles: [primera ventana](auditoria-profunda/NUMERICA-46.md), [segunda ventana](auditoria-profunda/VENTANA-28022.md) y [puente funcional](auditoria-profunda/VENTANA-28022-PUENTE.md). Z1 se verificó mediante aislamiento y recuento certificado de todos los ceros hasta 21. Las secciones detalladas inferiores conservan el registro inicial; sus afirmaciones de certificados ausentes o inercias pendientes quedan superadas.


Revisión de los tres puntos pedidos, sobre el `main.tex` local identificado en `evidencia/fuentes.json`. Los números de línea corresponden a ese archivo, no a páginas del PDF. **(a)** significa argumento comprobado en el alcance indicado; **(b)**, fallo localizado; **(c)**, paso no verificado. Una conclusión (c) no afirma que el enunciado sea falso.

| Punto | Dictamen | Motivo |
|---|---|---|
| Positividad de `W_T` para todo T equivalente a RH | **(a)** | Fórmula explícita, densidad en norma de forma y test primitivo negativo de paper 45. |
| Cotas `10^-18` y `2.5·10^-12` | **(a)** mediante reconstrucción | Cuatro inercias verificadas con Arb; resto analítico y colas comprobados. Conservar redondeos dirigidos. |
| Hechos Z1–Z3 | **(a)** en el alcance usado | Z1 aislado y contado con Arb; Z2 y Z3 cotejados con fuentes. |
| Cota hasta `T=2.8022` y uso de Z1–Z3 en ella | **(a)** con anexos de investigación | Programa encontrado, 17 comprobaciones reproducidas y puente funcional revisado dos veces. El paper por sí solo omite ese desarrollo. |

## Equivalencia con RH

Las definiciones están en paper 46, líneas 248–316, y la demostración de `thm:all-support` en 5460–5505. Con la transformada `Fhat(τ)=∫F(t)e^{iτt}dt`, el símbolo es

`m(τ)=Re ψ(1/4+iτ/2)−log π`,

y cada potencia prima lleva `2Λ(n)/sqrt(n)` en el símbolo coseno. La fórmula explícita para una autocorrelación da

`W_T(F)=Σρ Φ_F(ρ) overline(Φ_F(1−barρ))`.

El término polar es `2Re(A overline B)`, no `|A|²+|B|²`. Bajo RH cada sumando es `|Φ_F(ρ)|²`. Para tests reales suaves la fórmula está en las líneas 260–271; la complejificación es válida porque la suma cruzada para dos tests reales es real al emparejar ceros conjugados.

La extensión a `D_T` no requiere suponer a priori convergencia de la suma para todo test rugoso: la densidad en norma ponderada de `lem:form-density` (457–487) y la positividad para diferencias hacen las transformadas una sucesión de Cauchy en `ell²`. La convergencia en `L²(-T,T)` identifica cada coordenada. El argumento de contracción del soporte seguido de mollificación demuestra la densidad; la continuidad de los momentos y el crecimiento logarítmico de `m` dan continuidad de la forma.

Para la recíproca revisé la prueba concreta de paper 45, `thm:sufficiency`, líneas 1403–1559. Un cero fuera de la recta produce una órbita de cuatro puntos `±z0,±bar z0`. Un polinomio anula los demás ceros de altura acotada y los puntos `±i/2`; una potencia convolutiva de un bump controla la cola. El ajuste con `α+βz0²`, posible porque `Im(z0²)≠0`, hace contribuir `−4m0` a la órbita. La cola es `O(4^-N)` con constantes independientes de N, pues `Σ m(z)/(1+|z|)²<∞`. Los tests construidos son reales, primitivos y compactamente soportados. Una ventana suficientemente grande contiene el soporte y tiene forma negativa. El soporte depende de N: no se afirma que una ventana prefijada detecte todos los ceros.

Esta equivalencia no demuestra que la forma sea positiva. Es compatible con que la prueba automórfica posterior quede sin verificar. El antecedente clásico es [Connes–Consani, apéndice C, con atribución a Yoshida](https://arxiv.org/html/2006.13771).

## Certificados en la ventana de log 5

El primer paso que no puedo certificar es paper 46, líneas **1616–1617**: las ball enclosures darían las cuatro cotas y el programa no se reproduce. El texto desarrolla la reducción, pero la tabla de pivotes (1772–1783) es el resultado que debe probarse, no un sustituto de la prueba computacional.

La proposición `prop:lowercert` (1695–1732) tiene una justificación funcional correcta: en el complemento de los primeros Legendre el operador es acotado inferiormente por `q_Y>0`; el complemento de Schur se domina por la matriz `R`; la inercia del borde con `c=0` resta exactamente una dirección negativa; con `c=−1/2` y `c=+1/2` se recuperan, respectivamente, los términos polares par e impar. Las estimaciones mediante la traza de la compresión del operador de limitación de banda también son suficientes como método.

Para completar la verificación numérica hacen falta:

1. Valores exactos o intervalos con redondeo dirigido para `T`, `s_infty`, nodos, pesos, entradas y cotas de colas.
2. Código de la cuadratura y demostración de la cota analítica del resto que efectivamente implementa.
3. Matrices certificadas o un generador reproducible de ellas, con los cuatro valores de μ.
4. Verificaciones de `q_Y>0`, invertibilidad del cambio de base, signo del bloque de borde y todos los pivotes del Schur complement, incluidas las contribuciones de las colas.

El notebook de paper 58 no contiene los parámetros identificadores de estos certificados: `193.13`, `640` o `120110026807`. Su README declara expresamente que contiene chequeos pequeños de consistencia, no prueba de los teoremas en su rango. No ejecuté esos chequeos como sustituto de las inercias ausentes.

El script `evidencia/comprobar_constantes_46.py` reproduce **con precisión múltiple, sin intervalos**, estas consistencias:

| Cantidad | Valor aproximado |
|---|---|
| `240T` | `193.132549492092…` |
| `A` | `2.94197352522362…` |
| `m(240)−A` | `0.700787608327198…` |
| `Lambda*_280` | `4.4046093678·10^-20` |
| `Lambda*_330` | `3.8625471440·10^-70` |

Las dos últimas son consistentes con las cotas impresas `4.5·10^-20` y `3.9·10^-70`; no certifican las matrices. Hay una corrección editorial necesaria en los datos de la línea 1766: si `omega_-` se emplea como cota superior definida en 1688, entonces `omega_-≥2A=5.88394705…`; **el decimal `5.8839` no es una cota superior válida**. Como resumen redondeado es admisible; como constante literal del certificado debe reemplazarse por una cota hacia arriba. No se infiere de esto que las cotas espectrales sean falsas. También `c_*=193.13` es sólo una presentación abreviada de `240T`, no su valor exacto.

## Ceros y ventana mayor

Z2 (1795–1796) usa una altura menor que la de [Platt–Trudgian, teorema 1](https://arxiv.org/pdf/2004.09765): `3·10^12 < 3 000 175 332 800`. Esta reducción de altura es correcta y no asume RH global.

Los coeficientes y rango de Z3 (1797–1798) se cotejaron con la formulación de Rosser que reproduce el artículo de [Faber–Kadiri](https://www.cs.uleth.ca/~kadiri/articles/New-Bounds-for-Psi-Math-Comp-Faber-Sept2013.pdf). Para `N(t)` definido con `γ≤t`, la versión no estricta de la desigualdad se obtiene también tomando límites derechos en las alturas de ceros. El paso `N(t)≤t log t/(2π)` para `t≥21` es correcto: la diferencia inferior impresa es positiva en 21 y creciente. La integración de Stieltjes de `lem:zerosum` conserva el término de borde con el signo correcto; descartarlo aumenta la cota.

Z1 (1790–1794) afirma simplicidad e inexistencia de otros ceros hasta 21, además de un intervalo para la primera ordenada. Es consistente con los valores clásicos, pero no he reconstruido desde los certificados originales el recuento y aislamiento: **(c)** para esa verificación independiente. Evaluar numéricamente `ζ(1/2+it)` no bastaría para descartar ceros omitidos fuera de la recta.

En `thm:margin` (1864–1890), Z1 elimina la primera pareja, Z2 convierte las contribuciones de altura intermedia en cuadrados y el recuento controla el resto por valor absoluto. Es un argumento de **cota superior** de la mínima forma, no una cota inferior. No hay una deducción válida de positividad por tender esa cota superior a cero, y el texto no la hace allí.

Para la cota **inferior** en 2.8022, el primer paso pendiente es **1915–1930**, `eq:power-window`: se anuncian un filtro compacto, 2048 filas continuas de Schur y 17 verificaciones; faltan sus fórmulas y ejecución. Z1–Z3 por sí solas no permiten comprobar el exponente `120110026807`. La sección declara que ninguna otra afirmación del paper depende de esta cota; su falta de certificación no refuta por sí misma la cadena automórfica.
