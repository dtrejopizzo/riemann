# Papers 43 44 y 45 Marco de Weil

La identificación radial de row C con la fórmula explícita tiene los signos y la normalización correctos. La familia de medidas de row B satisface sus leyes principales de composición y contacto. Los teoremas principales declarados de43 fueron reconstruidos en [HOCHSCHILD-43.md](auditoria-profunda/HOCHSCHILD-43.md) y [FORMA-COMPLETACION-43.md](auditoria-profunda/FORMA-COMPLETACION-43.md), con dictamen **(a)** en sus alcances precisos. No se certifica por ello prioridad bibliográfica ni una positividad geométrica que el manuscrito no afirma. Estas conclusiones no validan la deducción automórfica de RH: el propio paper 46 excluye 43–45 de esa deducción.

## Paper 43

No hay un único teorema principal: la introducción contiene `introA`, `introH`, `introB`, `introC` y `introD`, además de resultados de completación y determinante. El dictamen para estos teoremas principales es **(a)** tras las dos tandas profundas citadas. La prioridad bibliográfica de sus construcciones adicionales sigue **(c)**; la distribución explícita y sus símbolos son clásicos.

| Afirmación | Dictamen y alcance |
|---|---|
| Descomposición `A_S^×=Γ_S×ker φ`, identificación de `C_S` y sección homomorfa | **(a)**, `thm:split`, línea 777; normalizar cada valoración finita produce un representante único, y la sección preserva productos. |
| Convolución de objetos smeared | **(a)** para la identidad formal dada la definición; no prueba una teoría geométrica de intersecciones sobre Spec Z. |
| Cálculo de Hochschild `thm:shadow`, línea 2800 | **(a)** tras auditoría profunda: reconstruidos `prop:crossed`, excisión, Künneth, contracciones locales y compatibilidad con las tensorizaciones completadas; véase HOCHSCHILD-43.md. |
| Fórmula del símbolo en la componente radial | **(a)**: las integrales geométricas finitas y la identidad digamma dan el símbolo usado en 45. |
| Fórmula de todas las componentes, no degeneración, firma y completación | **(a)**: revisadas las componentes ramificadas/impares, densidad dual, topología LF/dual fuerte y construcción de Gram de dimensión infinita. Véase FORMA-COMPLETACION-43.md. |
| Estabilización al aumentar S | **(a)**: `thm:chartcomp` y `thm:colimtrace`, 5242–5335, para el sistema de proyecciones definido en el texto. |
| Límites de rulings, determinante y pairing Riemann–Roch | **(a)**: límites incompatibles explícitos, cálculo de Mertens, inyección de la completación Banach y ramaLog verificados. El pairing RR es el par definido de exponenciales, no un teorema de índice. |

El pendiente inicial en `thm:shadow(a)`, líneas2841–2849, fue descargado: la acción es temperada con respecto a los pesos rápidos concretos; las comparaciones de resoluciones son continuas y preservan etiquetas. La contracción Koszul pierde un peso, absorbido por la familia completa de seminormas. Excisión y Künneth se construyen con complementos y filtraciones finitas por grado, y las contracciones de shells tienen estimaciones uniformes en el índice de shell. El ledger detalla las pruebas reconstruidas, sin suponer nuclearidad de los factores p-ádicos ni homotopías equivariantes inexistentes.
Para la estabilización sí puede darse una comprobación directa. Un nuevo primo `ℓ` aporta

`(log ℓ) Σ(k≠0) ℓ^{−|k|/2} F(δ_S(ℓ^{−k}))`.

En las unidades, el integrando regularizado es cero porque la inflación es constante en la nueva coordenada. Si `log ℓ` supera el radio del soporte, cada término restante es cero. El límite es por tanto una estabilización eventual de valores, no una convergencia espectral de operadores ni una permuta ilimitada de series.

La relación con la literatura debe formularse por resultados. La distribución de Weil y su lectura como traza no son nuevas: [Connes](https://arxiv.org/abs/math/9811068) desarrolla la realización geométrica de la fórmula explícita; [Meyer](https://arxiv.org/abs/math/0312305) calcula homología de crossed products adélicos, con objetos que deben distinguirse del álgebra y los coeficientes torcidos de este paper. El cálculo torcido semilocal propuesto aquí no queda identificado automáticamente con el resultado de Meyer, pero tampoco se ha establecido su prioridad bibliográfica. **Novedad del paquete Hochschild exacto: (c)**. El texto reconoce la independencia lógica entre sus dos construcciones y que el vínculo de coinvariantes con la densidad local no es una identificación con homología de Hochschild (introducción, 140–151).

## Paper 44

Para los dos teoremas principales expresamente formulados como `introA` e `introB`, el dictamen es **(a)** en las hipótesis indicadas; no se extiende este dictamen automáticamente a cada resultado secundario del paper.

La definición crucial es `Frob_n=μ_(c_n K_P(n))`, con `P(n)⊂S_f` y Haar de probabilidad. Los representantes y soportes están calculados en 1153–1200. Como la convolución de dos Haar de cosets en este grupo abeliano es Haar del coset producto, y `P(mn)=P(m)∪P(n)`, se obtiene `Frob_m*Frob_n=Frob_mn`. El módulo constante `1/n` recupera n. La inversa de semigrupo conserva A y reemplaza r por `1/r`; el producto con el adjunto es `μ_KA`, no siempre la unidad. Así no se introducen inversas inexistentes.

El argumento de no interpolación continua (`rem:nointerp`, 1232–1260) también es correcto. Proyectar en un primo `p≠q` da una masa puntual en `1/q` al tiempo `log q`. Las raíces por convolución y continuidad obligan a masas puntuales para todos los tiempos. Un homomorfismo continuo desde el intervalo conectado al grupo totalmente disconexo `Z_p^×` es constante, y la ley obliga a que sea 1, contradicción.

Para el contacto (`thm:frobcontact`, 1441–1510), la condición de soporte elimina todas las capas salvo `p^k` si `n=p^k`. La densidad en esa capa es `p^{-k/2}` y su volumen local es `log p`, dando exactamente `Λ(n)n^{-1/2}h(1/n)`. Para n con dos factores primos no queda ninguna capa. En el lugar real, las coordenadas finitas de `j_infty(x)` son 1; por ello el indicador exige `s^N | n−1` en cada primo ajeno a P(n). Con Haar `dx/(2|x|)` y el soporte real positivo, el cambio `x=e^{-t}` da `1/(4sinh(t/2))`. Este factor es compatible con el enunciado, sin un factor 2 perdido.

La hipótesis `P(n)⊂S_f` está activa en toda la sección, desde 1149; no falta en el teorema aunque se remita a la definición. Tampoco se puede reemplazar el contacto de funciones por `T(Frob_n)` como valor sobre una medida: el propio texto explica la falta de extensión débil continua. La terminología Frobenius es una analogía de composición, no una realización de un endomorfismo de una curva.

**Novedad:** los coeficientes de contacto son los de Weil; no son nuevos. Las leyes de cosets son consecuencias de Haar y semigrupos inversos. Puede haber una presentación particular útil del semigrupo semilocal y sus obstrucciones, pero no se ha probado prioridad de esa formulación. Comparar con [Connes–Consani–Marcolli](https://arxiv.org/abs/math/0703392), donde ya se conecta la acción de clases de ideles con correspondencias y positividad.

## Paper 45

**(a)** para el teorema de comparación `thm:comparison` y la normalización radial solicitada; **(a)** para `thm:sufficiency`, el criterio primitivo usado por 46. No se certifican por esta conclusión todos los resultados posteriores sobre radicales.

El cambio de variable tiene una convención importante: `Γ_h(w)=h(−log|w|_S)`, de modo que `λ_−(Γ_h)=Φ_h(1)` y `λ_+(Γ_h)=Φ_h(0)` (523–525). Invertir esas etiquetas por sí solo es inocuo en el término simétrico, pero deben conservarse en las identidades individuales.

En `lem:radial-trace` (582–634), el término real es

`W_infty(Γ_h)=(γ+log(4π))h(0)+∫₀∞ [e^{−t/2}/(1−e^{−2t})][h(t)+h(−t)−2h(0)e^{−t/2}]dt`.

Para comprobar la constante, sustituir `u=2t` en el símbolo da

`J(τ)=ψ(1/2)−Re ψ(1/4+iτ/2)`.

Como `ψ(1/2)=−γ−2log2`, el resultado es `logπ−Re ψ(1/4+iτ/2)`, exactamente **−m(τ)** de paper 46. El núcleo K de 45 es la mitad del K de 46, pues el primero multiplica la suma `h(t)+h(−t)`; esto no es una discrepancia de normalización.

Revisé el argumento de contorno de `lem:contour` y `thm:EF` (772–981). La simetría transforma la integral en la recta −1 en el negativo de la de la recta 2, por eso aparece `1/(πi)`, no `1/(2πi)`. Al parametrizar la recta crítica, el factor 1/2 de la derivada logarítmica gamma devuelve `1/(2π)` en la integral real. El término de Euler aporta `−Λ(n)/sqrt(n)` por cada `h(±log n)`. Las alturas elegidas evitan los ceros y hacen desaparecer las aristas horizontales. El soporte compacto vuelve finita la suma prima.

Al restar los términos, se obtiene

`T_lim(Γ_h)=Φ_h(0)+Φ_h(1)−Σρ Φ_h(ρ)`.

El producto de Mellin para `F*G†` es `Φ_F(s) overline(Φ_G(1−bar s))`; así coinciden también la fórmula hermitiana y la fórmula real que importa 46. Añadir `c h(0)` altera efectivamente la fórmula: el valor c=0 depende de la normalización previamente elegida, no queda seleccionado por un principio geométrico independiente.

**Novedad:** es una verificación de compatibilidad de normalizaciones y una exposición de la fórmula explícita clásica; no una nueva fórmula explícita. Los antecedentes directos incluyen [Connes–Consani, apéndices B, C y E](https://arxiv.org/html/2006.13771), [Meyer, interpretación espectral](https://arxiv.org/abs/math/0412277) y [Burnol, términos locales y operador conductor](https://arxiv.org/abs/math/9902080). La construcción explícita de tests pares e impares puede tener valor expositivo, pero el mecanismo de interpolar ceros y amortiguar la cola se atribuye correctamente a Yoshida/Connes–Consani.

## Uniones de rows A B C con la forma de 46

| Unión | Comprobación |
|---|---|
| 43 `thm:chartcomp`, `thm:colimtrace` → 45 `prop:colimit` | **(a)** en el caso radial y en las restricciones de soporte indicadas. |
| 43 `lem:radialtrace` → 45 `lem:radial-trace` | **(a)**, inversión del perfil compensada por la simetría de las sumas y del núcleo. |
| 44 álgebra radial → 45 convolución y momentos | **(a)**, Haar del compacto normalizado a 1. |
| 45 `thm:EF`, `thm:comparison` → 46 `comparison`, `eq:W` | **(a)**, signo, `2π`, conjugación y término polar compatibles. |
| 45 `thm:sufficiency` → 46 `thm:all-support` | **(a)**; cada test construido cabe en alguna ventana, no necesariamente una fijada de antemano. |

No hay una unión demostrada entre una positividad geométrica de Hochschild y la positividad de `W_T`: 43 no afirma tal resultado y 46 no lo usa. Esa ausencia no es un error lógico de la cadena declarada; limita la interpretación de «llevar la prueba de Weil a Spec Z».
