# El residuo de cocientes grandes en un rectángulo aislado aún detecta RH

Usar Y=√X e I_Y=(21Y/20,22Y/20] como en 340. En el primer rectángulo I_Y² y en el segundo I_(Y/2)² retirar todos los pares (d,e) con altura max(d,e)/(d,e)≤R, empleando el **mismo R**. Sea V(Y,R) la suma de μ(d)μ(e) en los pares restantes del primer rectángulo. Para cada δ=1/j, j≥16, tomar R=X^(1/6+δ/3). Entonces RH equivale a

    |V(Y,R)−2V(Y/2,R)| ≪_(δ,ε) Y^(1+δ+ε)     para cada ε>0 y todo Y grande.

Esta es sólo la medición a frecuencia cero del bloque de dos escalas (dividida por h∫η). Para cada producto la integral del pulso es completa en la ventana del rectángulo correspondiente.

**Cálculo.** Poner u(Y)=(Σ_{d∈I_Y}μ(d))². A cociente r/s fijo, d=gr,e=gs, el intervalo admisible J de g en el primer rectángulo se divide exactamente por dos en el segundo. Por 341, la diferencia de sus recuentos ponderados por μ(r)μ(s) cuesta O(τ(rs)√(Y/max(r,s))) porque se cancela la densidad. Sin k ni peso local, sumar v=max(r,s) como en 342 da

    V(Y,R)−2V(Y/2,R) = u(Y)−2u(Y/2) + O(Y^(1/2) R^(3/2) X^o(1)).

Con el R elegido el error es Y^(1+δ+o(1)). Bajo RH, 340 da u(Y)≪_ε Y^(1+ε), lo que prueba el techo anunciado. A la inversa se obtiene |u(Y)−2u(Y/2)|≪Y^(1+δ+ε). Iterar hasta Y/2^l acotado: los errores suman una progresión de razón 2^(−δ−ε) y el término inicial cuesta O(Y). Así u(Y)≪Y^(1+δ+ε). El telescopado en razón 21/22 de 340, seguido de j→∞, da RH. Al iterar se usa la desigualdad **para u**, que ya no depende de R; nunca se identifican residuos calculados con cortes distintos.

**Versión de segundo momento.** Si sólo se retiran alturas hasta R=X^(1/8), el criterio de segundo momento para el residuo aislado de las dos escalas también equivale a RH. En efecto, por la prueba de 342 aplicada a los dos rectángulos, con k=1, la diferencia de los pulsos retirados cuesta puntualmente O(X^(1/4+3/16+o(1)))=o(√(Xh)) para δ≤1/16. Bajo RH, ambos rectángulos completos cumplen la cota de 340 (la anchura a Y/2 sólo cambia por factor constante frente a su anchura natural; la prueba de Plancherel admite ese factor). Recíprocamente reinsertar el error y probar contra la función constante da la misma desigualdad para u que arriba. El mayor corte de la versión escalar no se afirma para este segundo momento.

**Implicación para el plan.** El resultado puntual de 342 retira componentes del observable total. Aplicar esa poda y luego intentar estimar de forma autónoma el rectángulo restante de 340 sigue imponiendo el criterio de Mertens, incluso si sólo se exige controlar su integral. El control conjunto de rectángulos conserva una posibilidad de cancelación que esa estimación separada pierde.
