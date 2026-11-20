# AUDIT_015 — dominio completado, no clausurabilidad y cono global

2026-10-19. Revisor hostil. **PROVED; veredicto final favorable.** Revisado `CONSTRUCTOR_015_DOMAIN_AND_CONE.md`, con005,007,008,011 y014. Consultados las reglas del proyecto, índice, grid y crucigrama. No se modifica ningún paper.

## 1. Diferencia y construcción de la sucesión

La diferencia escrita frente a008 es real: el primorial anterior tenía norma gaussiana divergente y no probaba no clausurabilidad. Los productos inclinados nuevos producen una constante aritmética pura mediante convergencia fuerte en ambos factores.

Los bloques finitos existen por divergencia de Σp⁻¹ y s<1. Para hacer la elección completamente determinista puede tomarse E_j como los primos consecutivos desde el primero ≥j hasta alcanzar H_j≥j³; no se necesita estimación de su último primo. La libertad de elección del texto tampoco afecta la prueba.

La independencia de X_p bajo P_s da exactamente la fórmula de segundo momento; `Var_s B_j≤exp(t_j²H_j)−1→0`. La cota logarítmica (3) tiene el signo correcto: r>s, min E_j→∞ y t_jH_j=H_j^(1/3)→∞, mientras t_j→0. Así Z_r/Z_s→0 y, porque r<1, Z_1/Z_s≤Z_r/Z_s→0. Se sigue A_j→1 en L²(P_s), aunque cada A_j esté Haarcentrado.

La expansión centrada de §4 es exacta, incluido el término d=1 nulo. La cota de011 es una cota de norma, `||Tf_d||≤C d⁻ʳ`; triangular sobre la expansión finita da `||TA_j||≤C(Z_r−1)/Z_s→0`. No hay intercambio de productos infinitos ni ley zeta sobre los enteros para s<1. Esto prueba `(√κ1,0)∈H`.

## 2. Completación y operador

D_n es acotado en ambos factores y preserva H por007. Aplicarlo al límite nuevo produce `(√κX_n,0)`. La envolvente de X_n es densa en L² de la ley producto de valuaciones: diferencias finitas de umbrales generan indicadores de patrones finitos, con truncación de las coordenadas no acotadas. Por ello todo el factor aritmético puro está en H.

Restar ese factor a cada imagen inicial entrega `(0,TA)`, y cerrar da exactamente `H=L²(P_s)⊕V`, V=closure(TA₀). La inclusión inversa usa el producto cerrado; no se supone que V sea todo el ambiente gaussiano.

A₀ es ahora denso en L²(P_s). La sucesión explícita `F_j=f₂−(D₂A_j−A_j/2)` satisface F_j→0 aritméticamente y TF_j→Tf₂≠0 en norma gaussiana. El paso emplea las acciones acotadas de007, no evaluación puntual de un límite L². Es una prueba completa de no clausurabilidad del operador T de este dominio. No se extrapola a operadores asociados a otros portadores.

## 3. Proyecciones y cono

Con la normalización de ι, e=(1,0) es unitario y el límite obtenido antes es √κe; no hay conflicto de factores. El rango uno es exactamente `||Proj_eι(A)||²=κ|E_sA|²`. Las otras piezas son las energías de la parte aritmética de media cero y del factor V. Esta afirmación, antes injustificada en007, queda demostrada por la nueva descomposición; no identifica e con el polo de Q.

Cada forma está dominada por S, por lo que cualquier combinación real fija es continua en H. PSD sobre A₀ denso se extiende a H. Los tres vectores puros de §8 son no nulos y aíslan los tres coeficientes, probando necesidad del ortante no negativo; la suficiencia ya era005. No hace falta la sucesión divergente008 para el cono.

## 4. Alcance final

La combinación con014 es correcta: ninguna combinación fija real no nula de las tres piezas que sea PSD **sobre todo A₀**, aplicada con el mapa011 intacto, proporciona la dominación uniforme declarada. No se clasifican combinaciones firmadas positivas sólo en la imagen del pullback ni otros mapas, otros kernels, coeficientes dependientes de T o invariancia de V bajo la inversión ambiental. No se obtuvo signo nuevo para D.

**Veredicto:** los tres teoremas son PROVED en el alcance escrito. La aplicación negativa al mapa011 conserva el input CITED de014; las pruebas internas de estructura, no clausurabilidad y cono no necesitan ese input espectral.
