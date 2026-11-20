# Transferir la cola verificada a una cota en norma L²

Para T fijo y A entero positivo existe C(T,A), independiente de la altura G, tal que si todos los ceros hasta G≥2 están en la recta crítica, entonces

    W_T(f) ≥ −C(T,A) G^(−A) ||f||₂².

Vale para toda la forma por clausura desde el núcleo suave del paper 47. Frente a 172 se elimina la norma de derivadas de f. La idea es combinar dos extensiones exactas en una ventana un poco mayor. Una controla las frecuencias bajas por los ceros verificados y la otra tiene densidad positiva en frecuencias altas por el término archimediano.

**Dos extensiones.** Tomar el intervalo ampliado |u|<2T+1. En él usar la variante atómica de 172, μ=Σδ_γ+C(τ)dτ, donde para cada n
    |C(τ)|≤C(T,n) Σ_{|γ|>G} (1+|τ−γ|)^(−n).
En |τ|≤G/2 esto cuesta O_(T,n)(G^(1−n)log(2G)); en toda la recta cuesta O_T(log(2+|τ|)) por el conteo unitario. La segunda extensión es ν=b(τ)dτ, usando un peso suave compacto igual a uno en el intervalo ampliado en la fórmula fw del paper. En la normalización de medidas se divide la densidad fw por 2π. Por la fórmula archimediana de §7, b(τ)=m(τ)/(2π)+O_T(1): la diferencia con el multiplicador puro está soportada lejos de la singularidad en la variable de integración, el término primo es una suma finita y el término polar está acotado. Así b⁻ es acotada y está soportada en |τ|≤R(T) porque m(τ) crece como log|τ|. No se supone ninguna positividad dentro de ese compacto.

**Mezcla que conserva los datos.** Escribir sinc t=sin(t)/t y poner H=√G,
    φ(τ)=1−[1−sinc(τ/H)^(2k)]^m,    λ=φ μ+(1−φ)ν.
Aquí k,m son enteros positivos fijos. Se tiene 0≤φ≤1 y su transformada tiene soporte en [−2km/H,2km/H] por el soporte de la transformada de sinc. Para H>2km, la transformada de φ(μ−ν) se anula en |u|<2T, ya que la de μ−ν se anula en el intervalo ampliado. Se usa convolución de una distribución compactamente soportada con otra temperada. Por tanto λ reproduce exactamente la forma en la ventana pedida. Los átomos en λ son positivos.

**Acotación de la densidad negativa.** En |τ|≤G/2 el término φC hereda la cota de cola anterior. El otro término sólo puede ser negativo hasta R(T); allí 1−φ=O_(k,m,T)(G^(−m)) por la expansión cuadrática de sinc en cero. En |τ|>G/2, para G>2R(T), b es positiva y φ≤m |sinc(τ/H)|^(2k)≤m G^k |τ|^(−2k). Así la contribución negativa cuesta O_(T,k,m)(G^(−k)log(2G)). Tomar n=A+3 y k=m=A+1 da λ≥−C(T,A)G^(−A)dτ como medidas. Para G por debajo de los umbrales fijos basta ampliar la constante usando la cota inferior de b directamente. Plancherel, con su factor de normalización absorbido en C, prueba la afirmación.

**Alcance.** Para la altura ya verificada en el paper se obtiene un techo al tamaño de cualquier autovalor negativo en esa ventana en la norma original. La constante depende del orden A y de T, incluyendo R(T); no se la evaluó para ninguna ventana nueva. No se puede fijar la constante y enviar A al infinito. El pegado con pérdida de soporte se refiere a medidas espectrales para el MISMO dato local; los intentos de pegado de bloques de formas, como D.74–D.79, no proporcionan esa igualdad previa. La positividad exacta aún exigiría un margen positivo que pague el error, o una eliminación exacta de la parte negativa.
