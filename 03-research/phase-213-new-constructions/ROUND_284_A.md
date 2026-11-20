# Hay un cruce auxiliar en cada intervalo de razón fija suficientemente grande

Para el peso φ de 283 existen constantes finitas C>1 y X₀ tales que todo [X,CX], X≥X₀, contiene L con

    F(L)=Σ_n Λ(n)φ(n/L)−L=0.

El enunciado es incondicional y no proporciona valores numéricos para C,X₀. En consecuencia, para CADA escala grande x de 280 se pueden eliminar las dos colas como en 283, escogiendo L en [V,CV], V=x/U. El nuevo coste diagonal y el descarte de pares de máximo común divisor grande siguen siendo de raíz. El escalar auxiliar deja de restringir las escalas en las que hay que estudiar los pares.

**Si hay un cero a la derecha.** Fijar uno, ρ₀=β₀+iγ₀, y 1/2<σ<β₀. La estimación de densidad de Ingham usada en 230 implica Σ_(Re ρ≥σ) 1/|Im ρ|<∞, pues su exponente en altura es estrictamente menor que uno. Para cada cero distinto de parte real ≥σ tomar una probabilidad sobre 0 y h=π/|Im ρ| con razón de masas masa(h)/masa(0)=exp(−h Re ρ). Su momento en exp(ρv) se anula. La convolución de todas es una probabilidad en [0,H] con H=Σh finito. Convolucionarla con la uniforme en [0,H+2] da una probabilidad ν en [0,2H+2] cuya densidad es 1/(H+2) en [H,H+2] salvo extremos. Conserva todas las anulaciones.

La fórmula explícita suave da F(exp t)=−Σ_ρ Hφ(ρ)exp(ρt)+O(1) para t grande, con suma absoluta sobre los multiplicadores Hφ. Integrando en t+v contra ν se obtiene O(exp(σt)). Por otra parte en cualquier intervalo logarítmico de longitud uno con origen T grande se tiene

    ∫₀¹ |F(exp(T+v))|dv ≫ exp(β₀T).

Para esta segunda afirmación usar el filtro complejo fijo f de 230 con soporte [0,1], integral uno y momentos nulos en ρ−ρ₀ para todos los demás valores con Re ρ≥σ. Integrar f(v)exp(−ρ₀(T+v))F(exp(T+v))dv. Queda −mult(ρ₀)Hφ(ρ₀)+o(1), distinto de cero por 275. La cota inferior se deduce por la norma suprema fija de f. Si F tuviera signo constante en [exp t,exp(t+2H+2)], el módulo del promedio por ν sería ≥(H+2)^(−1)∫_H^(H+1)|F(exp(t+v))|dv. Esto contradice los dos exponentes distintos para todo t grande. Por continuidad el intervalo contiene un cruce.

**Si todos los ceros son críticos.** En este caso exp(−t/2)F(exp t)=P(t)+o(1), con P(t)=−Σ_ρ Hφ(ρ)exp(i Im(ρ)t), una función real casi periódica por convergencia uniforme absoluta. Su media es cero y su coeficiente en la primera ordenada es distinto de cero. Por tanto toma valores estrictamente positivos y estrictamente negativos: una función casi periódica continua no negativa con un valor positivo tendría media positiva, pues copias de un intervalo positivo se repiten con huecos acotados. Para justificar esa recurrencia basta aproximar uniformemente por una suma trigonométrica finita; los casi períodos simultáneos de sus fases son relativamente densos por compacidad de la clausura de la órbita en el toro. Así existen δ>0 y longitud fija B tales que cada intervalo de longitud B contiene valores de P mayores que δ y menores que −δ (aumentar B para incluir ambos). El error o(1) preserva los signos a partir de cierto punto. Volver a la escala multiplicativa concluye la prueba.

**Uso en 283.** Allí se eligió primero una raíz y luego x=2L². La identidad exacta de compensación sólo requiere F(L)=0, y sus cotas de soporte, coste y baja frecuencia sólo requieren L comparable con V. Ahora se fija primero cualquier x grande y se elige después su L. La condición sobre pares sigue abierta incluso en una sola subsucesión. Los cruces previos de 237–238 y los filtros de 230 dan antecedentes parciales; aquí se combinan un promedio positivo que elimina todos los ceros a la derecha de σ y un filtro local que retiene uno de ellos, para obtener huecos logarítmicos acotados en los cruces del peso calibrador.
