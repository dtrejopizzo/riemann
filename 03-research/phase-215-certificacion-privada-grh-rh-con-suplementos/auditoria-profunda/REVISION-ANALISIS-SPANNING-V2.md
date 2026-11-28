# Revisión de correcciones: análisis, spanning y estimaciones auxiliares

Versión revisada: árbol de trabajo respecto de HEAD `97fb4e78`, 28-11-2026. No se modificaron manuscritos. Este dictamen sustituye los (b) locales correspondientes de la primera auditoría, sin certificar por extensión otras pruebas. La nueva corrección de caracteres de P53 se revisa en otro frente.

## Dictamen de los cambios

| Texto actual | Dictamen | Verificación de aplicación y constantes |
|---|---|---|
| P46:277, forma hermitiana | (a) | `a bar(b′)+b bar(a′)` es sesquilineal hermitiana y su diagonal es exactamente `2 Re(a bar b)`. No altera W ni sus coeficientes. |
| P46:1898, ε₉ | (a) | Se declara γ₁≥14.1347, compatible con el certificado ya reproducido. La estimación más débil 0.01576 usando 14.13 también da ε<0.016; permanece el denominador 0.484 y la constante final. No cambian cortes T. |
| P46:2093–2096, M_R | (a) | AM–GM sobre y,y,2(R²+a−y), todos no negativos, da `y²(R²+a−y)≤4(R²+a)³/27`. Para R²<a/2 la igualdad no se alcanza en y∈[a,R²+a], pero la cota sí vale. Se conserva M_R, y por tanto la desigualdad coerciva para todo R>0. |
| P49:2245–2251, FJ | (a) | La sustitución x=gh usa Haar izquierdo y `e(g⁻¹x)=d c(x⁻¹g)`. Integrabilidad por F∈L¹, |c|≤1. El vector de Bochner del paso siguiente y el grado formal d no cambian. Se elimina la identificación errónea de traslaciones de la prueba anterior. |
| P51:4452,4510–4518, `pm:siegel(c)` | (a) | Con g,x en compactos fijos se elige U común con γxU disjuntos. Los conjuntos Ω₁⁻¹γΩ₂U escapan de cada compacto cuando γ sale de un conjunto finito; el mayorante M′ es integrable. Se obtiene convergencia localmente uniforme. La cota de la suma total sigue siendo global en g. Basta para continuidad y para las aplicaciones posteriores; no se requiere uniformidad global de colas. |
| P51:10505–10515, tubo | (a) | β tiene peso1 y σ peso2; Q=2ρk+2ρ². La nueva Q satisface Q≤(k+2ρ+1)²/2=r²/2. Con radio Q²(T²+1)², el cociente de volúmenes es `(1+1/Q)^Q≤e<3`; se preservan T¹⁰ y el factor3. No cambia el rango de `pbo:local`. |
| P52:1810–1812, pisos | (a) | La acción preserva la bandera y es unitriangular, no puntual sobre todos sus vectores. Sobre V_l sólo añade combinaciones de pisos inferiores. Los usos en `pfr:ss-floors` dependen de esa bandera, de la normalización por G^(l) y de las medidas de convolución; no necesitan fijación vector por vector. No aparece un factor de jacobiano: los cambios triangulares tienen determinante1. |
| P52:4361–4367, corte dual | (a) | u invertible y u⁻¹→0 produce frecuencias exhaustivas y vecindades duales decrecientes a0. Con convergencia absoluta se aplica dominación; la continuidad de densidades de `pff:fibre(a)` da el límite de sus medias. Las dos medidas duales conservan producto1, sin factor residual ni cambio de parámetros. |
| P53:2252–2253,2640, P y S no vacíos | (a) | La prueba de decay elige un lugar del soporte. La hipótesis añadida es necesaria para ese argumento y se cumple en exchange: S es el conjunto de lugares de un módulo no trivial. En las grillas el módulo contiene las primas elegidas de π_M, incluso para twist trivial. Por tanto ninguna aplicación de la cadena pierde su rango. |
| P53:4431–4455, slices | (a) | Se sustituye falsa acotación Hilbert por continuidad en momentos. Para estados coherentes el mayorante es C(1+|y|)^(N+M). Superposición da la cota por ||v||_(N+M); para continuidad local en x basta M=0 y ||v||_N<∞. Con N=0,M=2p+1 se integra en dimensión real2p. Los vectores usados en M1/M2 tienen los momentos exigidos, también sus traslados por puntos de compactos. No se cambia la constante exacta del intercambio por esta reparación analítica. |
| P53:13765–13769, `pgq:slice` | (a) | El producto ahora es r₀⁻¹r, y el cambio de variable usa Haar izquierdo. La norma de la inversa del minimizador es t₀. Se mantiene s≥16n² y `2·16^(n²)Vτ` por el lema de bolas con s/2. |
| P53:14572–14576, covolumen | (a) en el campo de los datos | `det x·overline(det x)=1` implica módulo adélico total1: cancelación de lugares escindidos, valoración0 en los inertes. E/E⁺ es no ramificada en todos los lugares finitos de estos datos (P53:665), de modo que no se omite un caso ramificado dentro de su alcance. Se conserva `(2⁻ᶠ|D_E|^(1/2))^n`. La misma prueba valdría en un lugar ramificado sustituyendo «inert» por «non-split». |
| P53:16967, cita de `pm:siegel` | (a) | Reproduce la hipótesis corregida de compacidad de g y x. |

## Propagación al volumen 58

Se compararon por algoritmo los bloques modificados de los cinco archivos `main.tex` con el texto de58. **Los 30 bloques añadidos/modificados aparecen literalmente en58**, incluidos los de caracteres53 cuya validez matemática compete al otro frente. El resultado está guardado en `../evidencia/propagacion_v2_analisis.json`. Además se inspeccionaron los diffs de58 para FJ, tubo, bandera, corte y coercividad.

Esta comprobación certifica propagación textual de las correcciones, no reconstrucción automática de todas las pruebas de58. En particular, la fórmula fuerte de fase de49 no fue modificada y sigue requiriendo la distinción explicada en REVISION-FASE49-V2.

## Consecuencia para el dictamen privado

No persiste un fallo matemático en las reparaciones de esta tabla, y no se encontró pérdida de constantes ni restricción inadvertida del rango usado. Los resultados anteriores que dependían de ellas pueden usar las versiones corregidas. El dictamen de toda la serie aún debe integrar la revisión independiente del intercambio53, los demás frentes y la diferencia entre demostrar los lemas suficientes de fase y justificar literalmente su formulación fuerte.
