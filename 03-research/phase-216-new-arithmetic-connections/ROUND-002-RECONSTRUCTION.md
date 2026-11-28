# Reconstrucción de perfiles CM con soporte impar completo

28/11/2026. PROVED como lema de Fourier; prioridad no establecida y no propuesta como teorema nuevo independiente del método clásico de k-decks.

## Enunciado exacto

Sea G un grupo abeliano finito con involución c. Sean f,h:G→{0,1} con f(cx)=1−f(x), h(cx)=1−h(x). Supongamos que la transformada de Fourier de f no se anula en ningún carácter χ tal que χ(c)=−1. Si todas las correlaciones de cuatro puntos de f y h coinciden, entonces h es una traslación de f.

La hipótesis es explícitamente de Fourier. No se afirma aquí sin demostrarlo su equivalencia con una definición geométrica de no degeneración CM. Tampoco se sustituye «todas» por los únicos desplazamientos e,g,g²,g³.

## Prueba

Escribimos el grupo dual Γ multiplicativamente. H={χ:χ(c)=1} es un subgrupo de índice dos y el coset impar es ηH. La condición CM implica que el soporte de f̂ es exactamente {1}∪ηH: f̂(1)=|G|/2, los pares no triviales se anulan y los impares no se anulan por hipótesis.

La igualdad de cuatro puntos implica igualdad de dos puntos, poniendo dos desplazamientos repetidos en cada extremo y usando f²=f. Luego |f̂|=|ĥ| y ambos soportes coinciden. Definir r(χ)=ĥ(χ)/f̂(χ) en ηH. Tiene módulo uno y r(χ⁻¹)=r(χ)⁻¹ porque f,h son reales.

La transformada de la correlación de cuatro puntos implica

    r(χ₁)r(χ₂)r(χ₃)r(χ₄)=1

cuando los cuatro χ_i son impares y su producto es 1. Por tanto r(a)r(b)=r(d)r(e) para a,b,d,e impares con ab=de, usando χ₃=d⁻¹,χ₄=e⁻¹.

Para u∈H definir ψ(u)=r(ηu)/r(η). Aplicando la relación a ηu,ηv,ηuv,η se obtiene ψ(uv)=ψ(u)ψ(v). Además ψ(η⁻²)=r(η⁻¹)/r(η)=r(η)⁻², así que ψ(η²)=r(η)².

Existe entonces un carácter R de Γ dado por R(u)=ψ(u) y R(ηu)=r(η)ψ(u). La última identidad verifica la multiplicación de dos elementos del coset impar. Por dualidad finita, R es evaluación en un elemento de G. En el soporte, ĥ=Rf̂; fuera de él ambas transformadas son cero. Invertir Fourier muestra que h es la traslación correspondiente de f. □

## Interpretación Hodge

Por el formalismo del frente 01, los valores |G|T₄(g₁,g₂,g₃,g₄) son h^(4,0) de los tensores sobre E de las cuatro E-líneas CM trasladadas. Así esos números, con todas sus etiquetas y la hipótesis de soporte, reconstruyen el tipo hasta traslación. No se afirma reconstrucción a partir de números de Hodge sin etiquetas, de un tensor único, o de los períodos.

## Antecedentes y límite de originalidad

La identidad de Fourier que inicia la prueba está en §1, ecuaciones (2)–(3), de [Keleti–Kolountzakis, 2006](https://arxiv.org/pdf/math/0603415). Se revisaron esa sección y el inventario §1.1: allí se describen resultados anteriores de Grünbaum–Moore para cuatro y seis puntos, con hipótesis de no anulación. No se auditó toda la prueba del artículo ni se leyó directamente Grünbaum–Moore. Nuestra demostración es una especialización del método de recuperar fases en el soporte, con un coset completo; debe tratarse como lema auxiliar clásico hasta completar la comparación.

Se revisaron asimismo las definiciones, Theorem 1 y la construcción de Theorem 2/Corollary 3 de [Pebody, Set Reconstruction on the Hypercube](https://arxiv.org/html/1607.05675). Los números mínimos de reconstrucción bajo acciones de grupos tienen una teoría anterior. La ficha editorial de [Reconstructing Odd Necklaces](https://doi.org/10.1017/S0963548306007875) se consultó; el texto completo de ese artículo no se revisó.

La pregunta que merece continuar no es renombrar esta reconstrucción, sino qué sucede al imponer simultáneamente restricciones de soporte aritmético, realizaciones integrales y normalizaciones de períodos. No hay en esta nota un resultado nuevo de esa clase.
