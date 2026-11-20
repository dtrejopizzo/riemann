# Umbral polinómico para un contraejemplo en celdas

Cotejo. 010 prueba descenso con error dependiente del perfil. P47 prop:nearfree ya comprime el peine sobre contactos divisoriales y estima por Schur con pesos j⁻¹ᐟ². Aquí se aplica ese control al salto de dos réplicas consecutivas de cualquier test en N celdas, para elegir una pareja de réplicas y un umbral uniformes a tamaño N.

Para H=N+1, definir B=2 log H, R=2π exp(4) H², Q=⌈max(2H, HR(B+2−m(0)))⌉, d=log(1+1/Q), p=exp(−d/2). Si r es el cociente de Rayleigh de un test primitivo F no nulo de las celdas 1,...,N y

    r < τ_N := tanh(d/4)/N,

entonces U(f_Q+f_{Q+1}) tiene energía estrictamente negativa, con f_q(x)=q⁻¹ᐟ²f(x/q). En particular el signo global exige que el menor cociente de toda compresión primitiva no vacía sea ≥τ_N. El umbral es de orden 1/(N⁴ log N) al crecer N; no se pretende optimizar el exponente.

**Salto exacto.** Sean a_j los valores físicos de f, a_0=a_H=0. Para g=V_dF−pF todos los trozos no nulos son copias de la misma función −exp((u−d)/2)1_[0,d)(u), desplazada a log j con coeficiente √j(a_j−a_{j−1}). Los soportes son disjuntos, pues d<log(1+1/H). Así ||g||²=(1−p²)J con J=Σ_{j=1}^H j|a_j−a_{j−1}|². Telescopando hacia a_H y aplicando Cauchy–Schwarz, |a_i|²≤J Σ_{j=i+1}^H 1/j. La suma en i da ||F||²≤NJ.

**Contactos.** Un desplazamiento log n sólo conecta dos pulsos si nj=l exactamente: con 1≤l≤H todo entero distinto de l dista de l en logaritmo al menos log(1+1/H). Para pulsos normalizados el peine comprimido vale Λ(n)/√n en las dos posiciones simétricas del par j,nj. El peso de Schur j⁻¹ᐟ² da en la fila j una suma ponderada ≤Σ_{n≤H/j}Λ(n)/n+Σ_{n|j}Λ(n). La segunda es log j. Para x≥1, con h=⌊x⌋, usar ⌊h/n⌋≥h/(2n) cuando n≤h y Σ_{n≤h}Λ(n)⌊h/n⌋=log(h!) para acotar la primera por 2log x. Luego la norma es ≤B sobre estos pulsos.

**Piso y competidor.** Por P47 lem:mbounds, m≥B+2 para |t|≥R y m≥m(0) en todo t. El soporte de g tiene medida ≤Hd. La masa de Fourier en [−R,R] con medida dt/(2π) es ≤RHd||g||²/π por Cauchy–Schwarz. Con la elección de Q resulta (B+2−m(0))RHd/π≤1. La parte arquimediana domina (B+1)||g||² y la forma completa primitiva cumple a(g)≥||g||². Para el cruce real entre F y V_dF, la polarización da la identidad

    p a(F+V_dF)=(1+p)²a(F)−a(g).

El lado derecho es estrictamente negativo si r<(1−p²)/(N(1+p)²)=τ_N. Trasladar por log Q da la pareja entera anunciada, con última celda posible (Q+1)H−1. Las cotas Q de orden H³ log H y tanh(d/4) de orden 1/Q prueban la tasa. La estimación es condicional como piso y es incondicional como regla de construcción a partir de una violación certificada. No establece que tal violación ocurra ni que el fondo continuo de la misma ventana tenga ese piso. PROVED tras auditoría matemática independiente.

## Umbral reforzado con las posiciones reales de los saltos

Adaptación de P47 prop:nearfree a los pulsos exponenciales rectangulares de 031. En las fórmulas anteriores se puede sustituir Q por ⌈e¹³ H log(2H)⌉ y el umbral por

    τ'_N = (1+log log(2H)) tanh(d/4)/N,     d=log(1+1/Q).

Esto da orden (log log N)/(N² log N) al crecer N. Se conserva la misma regla explícita de falsificación.

Para la cota del peine, ψ(x)=Σ_{n≤x}Λ(n)≤4(log 2)x para x≥1: cada potencia prima en (h,2h] contribuye su peso a log binom(2h,h), y sumar en potencias de dos y redondear x a la potencia superior da la cota. Para h=⌊x⌋ la identidad factorial implica h Σ_{n≤h}Λ(n)/n ≤ log(h!)+ψ(h). Con los pesos de Schur anteriores esto da norma ≤log H+4log 2.

Para un solo pulso φ de longitud d normalizado en L², ||φ||₁²≤d. P47 lem:mbounds da m(t)≥log|t|−7 (usar m(0)>−6 en |t|<1). Al integrar log|dt| en su parte negativa, la estimación |φ̂|²≤d cuesta a lo sumo (1/π)∫₀¹−log u du=1/π. La diagonal arquimediana vale al menos log(1/d)−7−1/π. Para dos pulsos a distancia u=|log(j/k)|≥|j−k|/H≥2d, la fórmula separada de P47 prop:nearfree y K(v)≤2/v dan cruce en módulo ≤2d/u: la autocorrelación tiene norma L¹≤d y el núcleo se evalúa a distancia ≥u/2. (La cota para K resulta de sinh(v/2)≥v/2 y cosh(v/2)≥v/2.) Las sumas de filas arquimedianas fuera de diagonal quedan ≤4dH(1+log H)≤8e⁻¹³. Esto controla el bloque para coeficientes arbitrarios de los pulsos disjuntos. Los contactos aritméticos siguen siendo exactamente los divisoriales.

Como log(1/d)≥13+log H+log log(2H), al restar las cotas anteriores queda a(g)≥(1+log log(2H))||g||² para H≥2. La identidad de polarización de 031 concluye. La mejora utiliza la separación geométrica de los pulsos y la cota divisorial aguda ya presentes para otros resonadores en P47. Las constantes se escogieron por simplicidad. PROVED tras auditoría matemática independiente.

## Umbral de orden N⁻² con una segunda diferencia

El antecedente NEAR_CASES_RESULTS_2026_11_04 §1 elimina el logaritmo en la escala de resonadores suaves fijados de antemano. Para el test arbitrario F de 031 se puede fabricar un pulso de media cero con dos traslaciones y recuperar el control de F mediante dos identidades exactas.

Tomar Q=⌈exp(13)H⌉, d=log(1+1/Q), p=exp(−d/2), V=V_d, g=(V−pI)F y h=(I−V)g. En cada sitio log j el pulso de h es el de g menos una copia contigua suya. Tiene media cero, ancho 2d y norma al cuadrado doble de la del pulso de g. Dado que 2d<log(1+1/H), los sitios son disjuntos, los contactos del peine siguen siendo exactamente los divisoriales y ||h||²=2(1−p²)J.

Para su pulso normalizado ψ, repetir la diagonal de 031 con ancho 2d da piso log(1/d)−log 2−7−1/π. Queda el cruce arquimediano separado a distancia u≥1/H≥4d. Se tiene ∫c_ψ=0, ||c_ψ||₁≤2d y soporte en [−2d,2d]. Por convexidad decreciente del núcleo K y K(x)≤2/x, |K'(x)|≤2K(x/2)/x≤8/x². En la integral separada restar K(u) de K(u−v). El factor 1/2 del cruce y el teorema del valor medio dan cota 64d²/u². Por u≥|j−k|/H y Σ_{n≥1} n⁻²≤2, la suma fuera de diagonal por fila es ≤256(dH)². La norma del peine sigue ≤log H+4log 2. Por tanto, después de restar todos estos costes queda un piso ≥13−5log 2−7−1/π−256 exp(−26)>1. Así a(h)≥||h||².

Si ambos tests Y₁=(I+V)F e Y₂=(I+V)g tienen energía no negativa, entonces

    4(1+p)²a(F) ≥ 4a(g) = a(h)+a(Y₂) ≥ 2(1−p²)J,

usando la identidad de 031 para Y₁ en el primer paso. Luego el cociente de Rayleigh de F está por encima o en

    τ''_N = tanh(d/4)/(2N),     Q=⌈exp(13)(N+1)⌉.

Si el cociente es estrictamente menor, al menos uno de esos dos tests tiene energía negativa. Ambos son primitivos y se realizan en celdas enteras: trasladar por log Q² convierte los factores 1, exp d y exp(2d) en Q², Q(Q+1) y (Q+1)² para las réplicas normalizadas. La última celda posible es (Q+1)²H−1. El precio del umbral de orden N⁻² es que se pueden necesitar tres réplicas y comparar dos energías; no es el mismo competidor de dos réplicas de las secciones anteriores. PROVED tras auditoría matemática independiente.

## Qué escala de error en los saltos conservaría el signo

Como corolario de la aproximación de celdas de 212-75 y de la reformulación de 212 ROUND_022_B, poner β_N=max(0,sup(−a(Uf)/J_N(f))) sobre vectores no nulos de las N celdas que cumplen los dos momentos, con β_N=0 si no hay tales vectores. Entonces el signo global equivale a liminf_{N→∞} β_N/N=0. En particular, una cota inferior −o(N)J_N sólo en una subsucesión cofinal bastaría. Es una equivalencia; la estimación sublineal no está probada.

Para ver la implicación decisiva, si falla el signo elegir f suave real compacto en (0,b) con ambos momentos nulos y q=a(Uf)<0, por densidad en norma de forma. En la malla de paso 1/K muestrear por extremos izquierdos a f y a dos funciones suaves correctoras, todas con soporte en un compacto interior de (0,b). Elegir las correctoras con matriz invertible de los funcionales ∫u dx, ∫u dx/x (por ejemplo dos bumps positivos con soportes separados). Los dos momentos de las aproximaciones escalonadas convergen a los continuos con error O(1/K) por el teorema del valor medio. Resolver el sistema de dos momentos muestreados da coeficientes O(1/K) que reparan exactamente al perfil muestreado.

Al deshacer el escalamiento, estos escalones reparados convergen a f en norma de forma sobre un intervalo logarítmico compacto común: convergen en L¹ y tienen variación total uniformemente acotada, también después de aplicar U. Sus transformadas quedan dominadas por C/(1+|τ|); Plancherel ponderado por log(2+|τ|) y convergencia dominada bastan para la parte arquimediana, y el peine en esa ventana es acotado. Dilatar físicamente por K y multiplicar por K^(−1/2) produce un vector en celdas enteras, con energía →q por invariancia. Escribir f_K para f más las dos correctoras suaves con sus coeficientes, antes de muestrear. La identidad

    K J_N = Σ_j (1/K)(j/K) |K(f_K(j/K)−f_K((j−1)/K))|²

y la convergencia uniforme de las derivadas dan K J_N→I_f=∫x|f'(x)|²dx>0. Tomar K=⌊N/b⌋; el soporte interior permite rellenar las celdas sobrantes por cero para todos los N suficientemente grandes. Se obtiene

    liminf β_N/N ≥ −q/(b I_f)>0.

En sentido directo β_N=0 bajo positividad global. El índice sublineal de 025/026 cuenta dimensiones y no acota este cociente de energías. El argumento usa refinamiento y dilatación del perfil suave; añadir celdas nulas a un único vector fijo no produciría el factor 1/N en J_N. PROVED tras auditoría matemática independiente.
