# Coste local de mayorar el peso primo mediante recuentos positivos de múltiplos

Para usar divisibilidad de factoriales en 092, considerar h(t)=∫_[1,∞) floor(t/u)dν(u), con ν una medida positiva localmente finita, y pedir h(t)≥log t sólo para 1≤t≤4. Incluso en esta banda corta hay pérdida fija:

    ∫₁⁴ [h(t)−log t] dt/t² ≥ (5/6)log(6/5)(1/3−5/16)>0.

En efecto G(t)=ν([1,t]) es creciente y h(t)=Σ_{n≤t}G(t/n). Para 3≤t<4 la inversión finita da G(t)=h(t)−h(t/2)−h(t/3). La misma combinación aplicada a log es log(6/t), decreciente. Escribir E=h−log, r=6t/5 y comparar G(r)≥G(t) en 3≤t≤16/5. Resulta E(r)+E(t/2)+E(t/3)≥log(6/5), retirando del lado izquierdo de la comparación los términos con signo negativo mediante E≥0. Integrar en dt/t²: tras los tres cambios de variable las bandas son disjuntas dentro de [1,4] y los factores son respectivamente 6/5,1/2,1/3. Esto da la cota.

Para cualquier mezcla fija de ese tipo, por PNT y sumas de Riemann (h monótona y acotada en la banda), el exceso ponderado Σ_{x/4≤p≤x} log p E(x/p) dividido por x tiende a la integral indicada. Por tanto incluso restringida a los primos grandes esa mayoración paga orden x, frente al margen raíz de 092. La afirmación asintótica aquí sólo se usa para una mezcla fija. El argumento no trata combinaciones con coeficientes firmados ni compensaciones entre bandas. En 045–047 ya se invierten dilataciones mediante Möbius; aquí el obstáculo cuantitativo usa sólo los índices 1,2,3 sin comportamiento asintótico de Möbius.
