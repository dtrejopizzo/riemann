# Cota uniforme del bloque cruzado y encierro explícito del mínimo completo

En una ventana fija, dividir I_T en N celdas iguales de longitud h. Sea λ_h el mínimo de la matriz de 078 en la base de indicadores normalizados. Definir
     
    b_T=Σ_{2≤n<exp(2T)} v_n + 4 sinh T,
    d=m(π/h)−b_T,    B=45+b_T.

Entonces, en toda la forma completa,
     
    (λ_h+d−√((d−λ_h)²+4B²))/2 ≤ λ_W(T) ≤ λ_h.

La constante del cruce no crece con N. En particular, si d>0 y λ_h>B²/d se certifica signo estricto. Para cualquier T fijo con λ_W(T)>0 la condición se cumple a partir de algún refinamiento suficientemente fino. No exige una constante Sobolev estimada sobre el minimizador.

**Cruce arquimediano.** Extender la malla a toda la recta, sea P su proyector por medias y Q=1−P. Por traslación tomar el origen en un borde. Las funciones constantes en celdas tienen transformada igual a la transformada del indicador de una celda multiplicada por una función periódica de período 2π/h. Por Plancherel, agrupando ξ=(θ+2πk)/h, −π≤θ≤π, esto identifica P en cada fibra ℓ² con la proyección a una recta cuyo vector unitario tiene pesos de módulo cuadrado
     
    w_k=(2 sin(θ/2)/(θ+2πk))²,     Σ_k w_k=1.

La normalización resulta de Parseval para los coeficientes de Fourier de exp(iθt) sobre [0,1]. m(D) es diagonal en la fibra. La norma al cuadrado de su cruce desde esa recta a su ortogonal es la varianza ponderada de los valores m((θ+2πk)/h). Se puede mayorar tomando como centro el valor k=0. Esta estimación también justifica la identidad primero en entradas de soporte finito en celdas (sus saltos logarítmicos están en L²); el cruce así acotado se prolonga.

Para M₁=sup |t m'(t)| vale M₁≤10. De 078 se tiene t m'(t)=Σ 4t²c_j/(c_j²+t²)² ≤Σ 4t²/(c_j²+t²)^(3/2), c_j=1/2+2j. El primer sumando es ≤8 y el resto se acota por la mitad de la integral de la función decreciente sobre c≥0, igual a 2. Para k≠0 y r=|θ|/π≤1, w_k≤r²/k², y el cociente |θ+2πk|/|θ| está entre 1 y 3|k|/r. Así el módulo del cruce queda acotado por
     
    M₁ [2Σ_{k≥1}(log(3k)+1/e)²/k²]^(1/2) < 45.

En efecto r log(1/r)≤1/e; para a=log3+1/e, la suma de (log k+a)²/k² es ≤a²+∫₁^∞(log t+a)²/t² dt=2a²+2a+2<10. El punto θ=0 es irrelevante. La restricción a I_T no aumenta el cruce: el proyector de soporte conmuta con P porque la ventana es unión de celdas. La parte prima y polar tiene norma a lo sumo b_T por P47. Resulta la cota B indicada.

**Paso a la forma completa.** Descomponer F=u+v en medias y complemento de medias dentro de I_T. De 078, W(v)≥d||v||², mientras W(u)≥λ_h||u||². La cota de cruce da el término −2B||u||||v||. Minimizar la matriz escalar de orden dos prueba el encierro. Si d>λ_h, la anchura es a lo sumo B²/(d−λ_h). Para una ventana fija, d→∞ y λ_h queda uniformemente acotada por arriba ensayando la constante de toda la ventana. Así el encierro converge, aunque el coste de lograr d muy grande puede ser prohibitivo. La cota de 078 por regularidad tiene mejor tasa asintótica, pero llevaba una constante no evaluada.

**Cotejo.** El método de Schur y el control de complementos ya figuran en P47 y 026. La comparación nueva frente a 078 es el control del cruce por una varianza explícita en las fibras de la malla, con una cota independiente del refinamiento. Es un certificado suficiente en cada ventana: no se ha probado λ_h>B²/d para una familia de ventanas que tienda a infinito, ni se ha ejecutado un nuevo certificado numérico.
