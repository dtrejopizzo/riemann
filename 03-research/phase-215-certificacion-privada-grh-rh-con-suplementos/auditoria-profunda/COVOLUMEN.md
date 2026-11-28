> **V1: registro histórico, revisado en V2.** No aplicar sus objeciones de caracteres ni sus estados de propagación a los manuscritos corregidos sin consultar el [estado V2](../revision-v2/ESTADO.md). La cancelación especializada de caracteres corrige el impacto global atribuido en V1; se están consolidando los demás resultados.

# Paper 53: exchange y determinante, auditoría profunda en curso

**Hallazgo que afecta a la ruta del intercambio:** [incompatibilidad de caracteres en `pcu:product`](ERROR-53-CARACTERES.md). El cálculo directo da un factor dependiente de la variable que se integra en `pcu:period`. Esta obligación debe resolverse antes de certificar el intercambio y la cadena de covolumen por esta demostración. Las comprobaciones condicionales de las secciones siguientes siguen siendo locales.

## `pcx:decay`: hipótesis no vacía necesaria

**(b) para el enunciado literal permitiendo P=∅.** La subsección de convergencia introduce un conjunto P de primos con P∩bar(P)=∅, sin exigir que sea no vacío. En `pcx:decay(a)` la condición de sobreyectividad «en cada lugar de P» es entonces vacía. La primera inferencia inválida de la demostración es la aplicación de `pcx:meanzero` en el párrafo que afirma que el emparejamiento es no nulo en algún lugar porque x es sobreyectivo en P. No puede elegirse ese lugar si P=∅.

Contraejemplo al alcance literal: tomar S₁=0, S₂ un plano hiperbólico, P=∅, caracteres triviales y el vector 1 en la representación de Fock de Hom(0,S₂)=0. El manuscrito usa explícitamente el espacio cero y normaliza su theta funcional como 1 en `pcx:twice`. El kernel es por tanto 1. En la cúspide del grupo unitario del plano, la altura ht(h) es no acotada: para h infinito que escala un vector isotrópico racional por t y su dual por t⁻¹, con parte finita fija, un múltiplo integral del primero tiene longitud O(t⁻¹) en Λ_h. Para N₀>0, la desigualdad afirmada exigiría ht(h)^N₀≤C‖1‖_M, imposible.

**Corrección:** añadir P≠∅ a `pcx:decay` y mantenerla en `pcx:conv` cuando se formule fuera del contexto de exchange. En `pcx:X` ya se exige m≠(1), por lo que S tiene al menos un lugar. No es un contraejemplo al intercambio ni a la conclusión global. Debe comprobarse esta condición en cada otra aplicación del lema.

## Ensamblaje del intercambio: reconstrucción

Leídas y reconstruidas las líneas 1730–2260 y el argumento de convergencia hasta `pcx:conv`, con la corrección anterior y condicionado a las proposiciones intermedias que se señalan abajo.

- La transposición de índices entre las dos convenciones de splitting es exacta por definición. Al pasar de α=1, α′=γ a αα′=γ, ambos lados se multiplican por α(det g)⁻¹; c no cambia.
- La identidad de determinantes de los datos estándar da Φ(k^[a])=χ(det k)Ψ(k_[b]) con el signo correcto. Los soportes se identifican mediante extensión de una familia primitiva a una base sobre cada DVR. Para módulos con potencias, levantar una matriz invertible de la reducción conserva invertibilidad: no hace falta módulo squarefree.
- El cambio U→U⁻ en `P-matches` transforma q_U en b−q_U, exactamente la condición de signos de `P-std`. El adjunto introduce d con módulo constante; C se transforma en C/d₀².
- En `pcx:twice`, las dos aplicaciones con triples (J,J,0) y (J,0,J) dan ξ=c₁c₂ por Fubini sobre el cociente compacto. Los volúmenes positivos vol₀ y vol_J se cancelan. Como L_*(k)L_*(-k)=1, el cuadrado de la razón de rango igual es independiente del carácter. No se divide por una razón que podría ser cero.
- `P-equal` primero elige un vector no nulo para un carácter; `twice` lo convierte en el **mismo vector** que funciona para todos. La razón es no negativa por definición, por lo que igualdad de cuadrados implica igualdad. Añadir planos y transportar espacios con iguales signos conserva la independencia del carácter, si se suministran `P-plane` y `P-signs`.
- En el ensamblaje final, C₁|c|²=L_*C₀, con C₀≠0 y L_*>0, obliga a C₁≠0 y c≠0. La positividad de C=C₀/C₁ resulta de esta identidad, no de una suposición sobre el signo inicial de C₁. El caso sin caracteres se trata por vacuidad.

La no anulación de L_* usa el producto de Euler para z>1 y el teorema clásico de no anulación en Re(s)=1 para el carácter unitario no trivial. El peso positivo excluye el carácter trivial; quitar factores en S no introduce ceros en s=1. Ésta es una entrada analítica clásica, no una prueba nueva de no anulación dentro de la auditoría.

## Convergencia: mecanismo comprobado

`pcx:reduce` normaliza los parámetros idelicos mediante clases de ideales y unidades antes de estimar normas infinitas. El vector isotrópico racional e₁ proporciona la comparación entre el mayor parámetro de la cúspide y la inversa del primer mínimo. El compacto de la parte finita permite un denominador entero uniforme.

`pcx:thetagrowth` utiliza sumas sobre traslaciones de una red con exponente 2s>dim_R X: el supremo sobre la traslación es finito. Después de reducción, el dato finito recorre un conjunto finito salvo fases unitarias. La cota resultante depende de las alturas y no de la traslación de Heisenberg.

En `pcx:diffgain`, la inducción se realiza sobre vacíos trasladados y sus derivadas polinómicas; cada diferencia gana una potencia del tamaño de la traslación. La hipótesis de media cero se aplica a cada vector, evitando asumir una contracción de norma de operador. La superposición del vacío extiende la cota a vectores con momentos finitos.

`pcx:mean` usa un dominio fundamental compacto de E\A_E y un entero que fija el dato finito. Las traslaciones adélicas sobre el subespacio isotrópico se convierten en traslaciones reales pequeñas, sin cociclo en ese subespacio. La norma del funcional medio está controlada por la misma norma uniforme bajo traslaciones. En `pcx:meanzero`, una partición finita del soporte permite elegir un carácter no trivial local en cada pieza.

Finalmente un vector isotrópico corto d y una base corta de la fuente dan mapas de rango uno dλ de tamaño δ≪ht(g)^n/ht(h). Con P≠∅ y sobreyectividad local se anula la media. Elegir l=N₀+A da ht(h)^{A−l}=ht(h)^{-N₀}. El caso inyectivo intercambia fuente y destino. Esto justifica la convergencia absoluta de las integrales de exchange para los datos de rango completo y módulo no trivial.

## Obligaciones siguientes

No se certifica `pcx:X`. La lista inicial de pendientes queda actualizada por las tandas inferiores: `P-match` fue reconstruido; `P-slice` tiene una reparación explícita de topología; el álgebra del descenso fue comprobada condicionada a su fórmula de término constante. `P-top` encuentra el fallo concreto de `pcu:product`, documentado por separado. Siguen sin un cierre independiente completo en este ledger `P-flip`, `P-nonvan`, `P-plane` y `P-signs`, incluidas sus constantes y rangos. El ensamblaje anterior muestra para qué se necesitan y no sustituye sus demostraciones.

## Segunda tanda: `P-match` comprobado

Reconstruidas las líneas 2680–2910, condicionado al modelo local de Weil de 49 y a la convergencia ya revisada para S no vacío.

La partición Surjᵃ=⊔r Prᵃ es correcta: rOᵃ es precisamente la imagen de la matriz sobre Oᴺ, de modo que la clase lateral rGL_a(O) es única. La integral que define la sección tiene soporte compacto en GL_a(F), porque el soporte de Φ es compacto dentro del abierto de matrices sobreyectivas; no se usa compacidad en el espacio ambiente permitiendo degeneración de rango.

En `linfactor`, la invariancia de Λ permite promediar un número finito de traslaciones sobre GL_a(O), reduciendo Φ a 1_Prᵃ S_Φ. La extensión lineal a todas las funciones sólo sirve para definir T fuera de la imagen de los pares: en cada par usado la función vuelve a ser la sección localmente constante requerida. No se necesita continuidad de esa extensión ni se integra respecto de ella.

`generate` usa el idempotente e=x₀s y d=varpi^{-c}(1−e)+e para concentrar un dato estándar cerca de una órbita primitiva. La periodicidad a escala varpi^c y la equivariancia derecha de Ψ dan la identidad puntual del texto. El promedio sobre GL_N(O) es una suma finita por suavidad uniforme de la acción sobre la función de soporte compacto. El factor I(x₀)>0 porque p(dx₀)=1; no se divide por una integral oscilante que podría anularse, ya que se promedia |p|.

En `Sact`, el factor del lado grande es υ_w(det g)^{r−N}|det g|^{(r−N)/2}=η(det g)^{-b}. En el lado pequeño, el modelo en la plaza conjugada aporta υ_w^b|det g|^{-b/2}, y el twist υ^b aporta υ_w^{-2b}; se obtiene el mismo factor. Se conserva así la estabilidad del núcleo de la diferencia D y se extiende la identidad estándar a todos los datos matched. Esto cierra `P-match`, pero no las restantes proposiciones de exchange enumeradas arriba.

## Tercera tanda: error de topología en las restricciones puntuales

**(b) para la afirmación de que sl(x):F′→F es acotado como operador entre espacios de Hilbert.** Se declara en las líneas 4409–4410, antes de `pcu:eq-mixed`, y se usa en `pcu:slicedecay` y en la última parte de (M1). La prueba de `pcu:mixedmodel` también invoca esa acotación al hablar de unicidad.

El propio `pcu:mixedmodel` identifica F′, salvo una constante de norma, con L²(V_ℓ;F), y sl(x) con evaluación en x. Para dim_R V_ℓ=d>0, tomar una función suave de soporte compacto φ con φ(0)=1, un vector Schwartz v₀≠0 de F y

`G_ε(x)=φ(x/ε)v₀`.

Su norma L² es ε^{d/2}‖φ‖₂‖v₀‖→0; su valor en 0 es siempre v₀. La inversa de Bargmann de G_ε es un vector Schwartz, de modo que tiene todos los momentos finitos exigidos. Por tanto la evaluación no es acotada ni siquiera sobre ese subespacio provisto de la norma de Hilbert. No basta decir que los vectores usados son suaves.

### Reparación con las normas de momentos

La afirmación necesaria es continuidad de sl(x) **desde el espacio de vectores con norma de momento adecuada**, no desde todo F′ con norma de Hilbert. Puede reconstruirse sin suponer la afirmación falsa:

1. Definir primero la restricción sobre vacíos trasladados por la fórmula explícita del modelo mixto: sl(x)ρ(y)e es una fase por exp(−|x+Ay|²)ρ(Wy)e. Esta fórmula se obtiene directamente del inverso de Bargmann.
2. Para un vector con momentos finitos, definir sl(x)v por la integral de esa fórmula contra v(y). La desigualdad de `slicedecay`, probada primero sobre un vacío trasladado, da un mayorante integrable y produce

   `(1+|x|)^M ‖sl(x)v‖_N ≤ C‖v‖_{N+M}`.

3. La aplicación M al modelo mixto sí es acotada en norma de Hilbert. Por ello M puede pasar dentro de la superposición coherente en L². El resultado coincide casi en todas partes con la integral puntual anterior, que es continua en x por convergencia dominada. Esto identifica la restricción canónica sin usar evaluación acotada sobre L².
4. En (M1), la integral que construye Λ converge en **todas** las normas de momentos, según su cálculo de integración por partes. Usar la cota anterior con M=N=0 permite pasar sl(x) dentro de esa integral. La inversión de Fourier da entonces exactamente las secciones prescritas. No se necesita la inferencia incorrecta «converge en Hilbert, por tanto pasa la evaluación».

Así se conserva la conclusión de (M1) y `P-slice` después de corregir la topología y el orden de construcción. La reparación emplea las mismas estimaciones del manuscrito, pero debe escribirse: el texto literal sí contiene una afirmación falsa. El caso d=0 no presenta este problema; los pasos con planos hiperbólicos sí tienen d>0 cuando la otra dimensión es positiva.

La normalización de `P-slice` es correcta bajo esta reparación: κ=(c_D∫τ)⁻¹, con τ≥0 no nula, y el cambio de polarización convierte la integral de las secciones en el valor cero en la polarización opuesta. Aplicar el argumento con las dos polarizaciones intercambiadas da el valor prescrito en la orientación requerida.

## Unión 53 → 55: matriz de Gram integral

Se cotejaron las líneas 9770–9804 de 53 con 6221–6268 de 55 (`pax:gram`, `pax:pairing`). La escala de la forma es coherente: W_λ(Z)=Σ_μ^# se identifica con m(C_μ∩T_μ(Z)), y la forma es la restricción de la forma tensorial de base ortonormal, conforme a 49 §5.2.6. La identidad ⟨m(u),b_U⟩=(u,e_U) convierte la dualidad con todos los productos de menores en integralidad de todas las coordenadas tensoriales. Usar los productos estándar basta porque constituyen una base de Σ_μ.

Por tanto los e_T son tensores integrales y su matriz de Gram tiene entradas enteras. La identidad G_λ=H_μF_μ⁻¹ no introduce un cambio de norma: expresa esa misma forma en la base dual, mientras que H_μ⁻¹F_μ es la matriz en la base de productos de menores. La aplicación de 55 cancela los gauges conjugados mediante la identidad algebraica de invariancia y, en nivel libre, las ponderaciones de estabilizadores son 1. Esta unión queda comprobada a partir del modelo tensorial y la identidad de dualidad de 49; no depende del intercambio defectuoso `pcu:product`.

## Descenso: comprobación de exponentes, condicionada a `pct:plane`

La deducción de `pct:descent` en 5512–5530 conserva la función ℓ y cambia el exponente de d+1 a d. Se divide por κ_ν, no nulo por la no anulación clásica de L en los puntos usados. Para d≥0, L_*(d+1)/L^sharp(d+1)²=L_*(d); para d<0, poner d=−(z+1) da L_*(−z)/L^sharp(z+1)²=L_*(−z−1). La identidad vale también al cruzar d=−1 hacia 0. El factor Q tiene exponentes sucesivos (d+1)²−d²=2d+1, exactamente el de L^sharp(d+1)² en el caso positivo.

Esto comprueba el álgebra del descenso si se suministran la fórmula del término constante `pct:plane` y el término pequeño `pct:small`. No certifica por sí solo esos dos lemas ni repara el fallo de producto de caracteres usado en la construcción del triple grande.

## Leyes del modelo mixto: `pcu:laws`

Revisadas las líneas 3766–3838. El Levi aporta α(q/\bar q)⁻¹ υ(q)^a |q|^{a/2}, conforme a (W2). El factor υ(h)⁻ᵇ del modelo destino transforma βυᵇ en β; no queda un carácter residual en h. La acción del radical se obtiene de la fórmula de Heisenberg con fase ψ(−j tr(z x*J_Vx)/2), primero para el centro y después con z₂=−c*Jc/2. La evaluación en x=0 fija el escalar de normalización. Esta contabilidad de caracteres es correcta y no reproduce el error de `pcu:product`. Para las restricciones puntuales sigue siendo necesaria la reparación de topología descrita arriba.

## Conjugación de normas: `pcj:CL`

Leída la demostración completa, líneas 15456–16070. Su reconstrucción es condicional a la reciprocidad CM exacta de 49 y a la no anulación de la lift de 54, proposición 3.4. No usa la identidad defectuosa `pcu:product` dentro de esta sección. Debe conservarse la comprobación del orden de dependencias: la no anulación usada para construir ρ_σ tiene que estar disponible sin invocar CL.

**Comprobación del orden completada con el agente theta:** para z≥2, que es exactamente el rango de CL, la proposición 3.4 de 54 obtiene la no anulación mediante Siegel–Weil de 53, el dato `clean` y los factores locales de Euler. No usa CL. La constante no nula de `clean` y la positividad del producto de Euler dan norma no nula. No hay círculo en esta importación particular. La rama z=1 que sí emplea exchange no interviene en CL.

La aplicación semilineal Λ se define sobre trasladados racionales del vacío mediante jets. La inyectividad del desarrollo de Taylor prueba independencia de las relaciones. El paso de puntos racionales a adélicos usa igualdad eventual por constancia local, no continuidad de un automorfismo arbitrario de C. La identidad de caracteres aditivos se obtiene primero sobre racionales y se extiende por densidad y constancia local. La irreducibilidad suave de Heisenberg da sobreyectividad.

Después de escribir B=ua, con u de norma uno y a unidad, la normalización Λ′=ω(u)⁻¹Λ transforma el vacío en un múltiplo no nulo del vacío. Los vectores S_k son sumas ortogonales de trasladados, con |δ_k|²=1/I_k. De ahí salen el multiplicador m_σ(k)=σ(δ_k)/δ_k y la identidad m_σ(k)·conj(m_{cσc}(k))=1. Para el dato en las plazas elegidas, a_w=1 permite identificar Λ′ con conjugación de los valores de la función; las indicatrices 0–1 permanecen fijas.

La lift es una suma finita de jets con volumen común w₀, independiente del carácter ν. El carácter de parte finita σ∘ν_f se prolonga con el peso permutado: es unitario porque el cociente adélico del toro es compacto. La comparación de un jet no nulo bajo una traslación racional demuestra que ρ_σ es trivial sobre U(1)(E⁺). También es trivial sobre K¹, por lo que tiene orden finito. La corrección ν^σ=ν^(σ)ρ_σ⁻¹ conserva peso y ramificación; no se necesita demostrar ρ_σ=1.

La fórmula de coordenadas contiene C_{σ,p}, cuyo módulo no depende de p: |t_σ|=|s₀|, |σ(π_M)|²=M, y todos los factores de caracteres restantes tienen módulo uno. Para conjugar la norma hay que usar σ′=cσc, como hace el texto, en lugar de suponer que σ conmuta con conjugación sobre todo C. Las permutaciones de los embeddings CM coinciden para σ y σ′; las multiplicidades tensoriales n_β y los pesos de estabilizadores r_h son racionales. La identidad de los multiplicadores elimina su dependencia de h. Resulta el factor positivo a_σ(z), independiente de ν, que se cancela al comparar un par principal y uno plano del mismo z. Éste es exactamente el alcance requerido por la aplicación en 54; no afirma racionalidad individual de cada norma.

## Adjunto y cambio de espacio: cierre condicional localizado

Revisadas 2912–3025. En `P-flip`, el determinante de la acción sobre Hom(U,W) es det(g)^b det(h)⁻ᴺ. La ley (W6) lleva por tanto los caracteres (γ,γ) a (γ⁻¹υᵇ,γ⁻¹υᴺ) en el par invertido. Como γ=ν⁻¹υᴺᐟ², el carácter de destino resulta νυᴺᐟ²; retirar γ⁻¹ del carácter de fuente aporta γ(det g), con el signo correcto. No se repite el defecto de producto de caracteres.

El ajuste central u de los retículos se elimina por traslación en la variable integrada, pagando sólo un valor de carácter de módulo uno. La transposición introduce −X; la invariancia derecha del dato matched convierte ese signo en otro valor de carácter de módulo uno. La constante restante c_θ depende de la identificación de modelos y de los espacios, no de ν. La convergencia usa soporte inyectivo y el conjunto de plazas no vacío ya previsto en esta aplicación. Así `P-flip` queda reconstruido bajo (W6), el diccionario de retículos y la convergencia, sin requerir el exchange defectuoso.

En `pcx:move`, el transporte racional de los espacios y los cambios de marcos adelizados transforman los datos por ω(k,k′). El cociente de twists es α(det k)β(det k′)⁻¹. Trasladar h a hk′ conserva Haar; su módulo es uno. El argumento de `P-signs` es entonces válido **condicionado a `pcx:const`**: la evaluación en k se reemplaza por la evaluación en 1 porque esa función sería constante. La prueba de `pcx:const` remite al término constante del plano; esta lectura no lo convierte en una obligación ya cerrada. Queda delimitada la dependencia, en lugar de certificar `P-signs` aisladamente.

## Término constante y no anulación: revisión especializada posterior

La reconstrucción completa de 4610–5465 y 5544–6368 está en [PLANO-53](PLANO-53.md). Se cierran condicionalmente `pct:plane`, `pcx:const`, `pct:coneimage`, `P-plane` y `pct:vandesc`, bajo el modelo de Weil y la reparación del modelo mixto en normas de momentos. La restricción u=1 o r=N se respeta. Esto cierra la premisa const del argumento `P-signs` anterior; no utiliza exchange ni `pcu:product`.

También se reconstruyó `pcn:negcoeff`, con descenso de la distribución a la fibra y anulación por rotaciones compactas; no usa unfolding global. **`P-nonvan` sigue sin quedar probado por la ruta escrita:** su input `pct:vantop`, caso(a), utiliza otra vez `pcu:product` en5632–5634. La anulación supuesta del período sin twist no implica la del período con β(det l). Ésta es una dependencia defectuosa identificada, no una mera falta de lectura ni un contraejemplo al enunciado.

## Álgebra de la cadena y determinantes

[CADENA-53](CADENA-53.md) reconstruye `pc:tri-inj`, `pc:tri-gram`, los índices de nivel, la comparación de determinantes por M⁺ y la cancelación que da `au:factor`. Conserva el orden de operadores sin suponer conmutatividad, la conjugación de σ, el factor c_Q y la potencia final −d_T. Verifica los rangos del exchange de exceso t y del invertido de exceso0, y la conversión de constantes a potencias de norma. Son cierres condicionales: la prueba de los cuadrados sigue recibiendo el exchange defectuoso. La ficha individualiza además las obligaciones archimedeanas H/Hc/F no sustituidas por esa comprobación algebraica.

**Actualización H/Hc/F:** CADENA-53 §6 reconstruye las tres obligaciones archimedeanas que la primera tanda dejó abiertas, incluyendo los no emparejados en Hc y la fuente primaria del smoothing de Harish-Chandra. Esto no cierra RS ni T1 porque ambos siguen usando exchange.
