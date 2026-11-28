# Auditoría profunda de P56: registro de obligaciones

Fecha: 2026-11-28. Fuente: `04-papers/56-explicit-cup-exponents-local-galois-representations/main.tex`. Las líneas que siguen remiten a ese `main.tex`. No se modificó ningún paper.

Este registro reemplaza la mera anotación «no revisado» para los pasos indicados. **No es todavía un dictamen (a) sobre todo P56**, ni sobre la serie. (a) significa que la prueba de la obligación identificada fue reconstruida; no se utiliza como sinónimo de «no encontré un contraejemplo». Las dependencias internas recorridas y las externas aceptadas se hacen explícitas.

## Estado vigente después de la revisión profunda

**(a) para la cadena local de cup products, con las hipótesis impresas:** T3, I2, I4, I5, SCC, scheme y las especializaciones sparse/any/generic/tame/crys se reconstruyen en §§1–6. Incluye los primos pequeños en las alternativas que los admiten. **NM es suficiente, no necesaria**; el contraejemplo a necesidad está en el informe inicial. La aplicación data es (a) bajo los datos de P46 y M2/G4 de P55. Esos últimos se cotejaron posteriormente con las fuentes primarias y sus usos en SELMER §§6,12. Las frases de pendientes en las tandas anteriores son históricas, reemplazadas por §§5–6 y este estado. Persisten las correcciones literales de P55 indicadas en SELMER §§6,11; no pertenecen a la prueba local de P56. La existencia global de los datos de P46 corresponde a la auditoría de ese paper.

## Resultado de la primera tanda

| Obligación | Resultado de la revisión | Alcance |
|---|---|---|
| `pkw:T3`, líneas 7753–7782 | **(a)** | El anulador tame se obtiene con el exponente impreso, bajo las hipótesis impresas y las convenciones de side/tame chart. No se usa irreducibilidad residual ni un cambio del retículo. |
| `pkw:Z`, `pkw:step`, `pkw:count` | **(a)** | La división por `z` es integral; no es una división solamente en un anillo de períodos racional. |
| `pke:I2`, líneas 4829–4844 | **(a)** | La profundización tiene coste `vℓ(n)+d_v+3a`, con la convención expresa `vℓ(0)=0`. Incluye los niveles y los enteros negativos indicados. |
| `pkh:I4`, líneas 5793–5814 | **(a)** | La prueba da incluso `Σ((8a+1)n_i+3(W+1)r_i)`. Se verificó la eliminación de polos y la división auxiliar por ℓ. |
| `pkg:I5`, líneas 5180–5229 | **(a), para la construcción local** | Se reconstruyeron radius, series, Taylor y la corrección exacta de la imagen. El coste es `κ+4δ`. |
| `pkd:scheme`, líneas 6882–6992 | **(a), como deducción de walk/rule** | Se verifican los órdenes, shifts, costes y las dos utilizaciones del shift cero. La traducción última de safe paths a cociclos/cup products requiere la revisión separada del bloque inicial `pkp:letters` y su construcción de SCC. |

**Pendiente concreto para cerrar la afirmación principal de cup products:** reconstruir `pkp:letters` y sus lemas previos, incluida la identificación de SCC con anulación del cup product, y revisar después todas las especializaciones sparse/any/data, no sólo la aritmética de sus constantes. No se identifica ese pendiente con una falla de T3, I2 o I4. La regla `pkp:rule` y el ensamblaje formal de `pkm:walk` se leyeron; falta cerrar en esta tanda el bloque cohomológico del cual dependen.

## 1. T3: reconstrucción completa del descenso

Se trabaja en `A=A_inf`, no en su cuerpo de fracciones. `I_0(i)` es el ideal de escalares que levantan uniformemente todos los parámetros de la side; `J=I_0(i)+ℓ^(κ+1)A`. `pkm:zpow` (1711–1730) da un entero ν con

`z^ν ∈ J`, `(ℓ−1)ν ≤ e(n₀+κ)`.

La hipótesis `n₀+κ+2<ℓ` implica ν<e. El polinomio que debe matar la extensión es **Q=q(X)(X−1)**, no q. El factor adicional mata la representación trivial de parámetros. La exactitud de D_pcris en la categoría potencialmente cristalina permite aplicarlo a `X_S` (`pkw:ext`). Esto explica exactamente el `+1` de `m₀(deg q+1)`.

Sea ξ la raíz tame de orden e y a su reducción. Como e es primo a ℓ, los elementos `a^k`, `1≤k<e`, son distintos. La reducción de Q es monica y no nula. Por ello, el número de índices malos `Q(a^k)=0` es como máximo `deg q+1`, incluso con raíces múltiples. Si k es bueno, `Q(ξ^k)` es una unidad de A.

El invariante de inducción es

`ℓ^t z^k ∈ J`, `k<e`, `t+m₀ b(k)≤κ`,

con b(k) el número de índices malos entre 1 y k. Un paso bueno reduce k en uno sin coste mediante `pkw:step`. Un paso malo usa `pkm:lower(i)` y cuesta `vℓ(k)+1≤m₀`, pues `k<e≤ℓ^m₀`. Se puede aumentar el coste al entero m₀ sin perder la pertenencia al ideal. En k=0 se obtiene `ℓ^κ ∈ J` y, escribiendo `ℓ^κ=s+ℓ^(κ+1)b`, resulta `ℓ^κ(1−ℓb)=s∈I_0`. La unidad `1−ℓb` da `ℓ^κ∈I_0`. **No se necesita que I sea finitamente generado ni una versión no justificada de Nakayama.**

En particular, e=1 causa ν=0 y no exige un paso malo. Para ℓ=2 las hipótesis numéricas de T3 son vacías si los parámetros son no negativos; T3 no proporciona por sí mismo una cota no vacía en ℓ=2. Esto no es una omisión: los otros casos del teorema cristalino usan los anuladores generales, no T3. No aparece una hipótesis escondida `ℓ≠2` en el descenso.

### Por qué el paso bueno es integral

`pkw:Z` (7680–7710) parte de `x∈N∩M_inf` y produce

`z⁻¹ Σ_j Q_j s₀^j x ∈ M_inf`.

La acción de s₀ preserva M_inf, los parámetros, E y las letters. La retractación implica que los coeficientes de x en la base del frame están en S. Para una forma μ, las formas conjugadas satisfacen una relación exacta porque Q mata la acción de inercia sobre D_pcris; las constantes de valores están en el subcampo no ramificado y s₀ las fija. Por otra parte, para b∈S_B se tiene `s₀b−b∈zB⁺`, utilizando `ℓ^k b=λ+zw`, λ∈Λ. El test de coeficientes del frame da `E^(4a)s_j∈zB⁺` para cada coeficiente s_j∈A de la suma.

El paso de B⁺ a A se hace por `pkl:intdiv` (3919): si ν es no divisible por ℓ y divide `E−ℓβ`, la divisibilidad por ν de un elemento de A en B⁺ ya vale en A. Se aplica con ν=z y β=1. Después se cancela E porque `(E)=ker θ` es primo y `θ(z)≠0`: si `E^h s=zq`, la primalidad da E|q, y se cancela sucesivamente. **No se supone que z sea primo.**

Para la versión en J, `pkm:J-basic(iv)` da un único u∈S tal que los lifts de todos los c tienen proyección `(ℓ^t z^k−ru)ε_i(c)`, r=ℓ^(κ+1). Es esencial que u sea uniforme en c. Se escribe u=w+zv con w∈Λ; `Q(1)=0` elimina w. Aplicando Z se obtiene un escalar de I cuya diferencia con `Q(ξ^k)ℓ^t z^(k−1)` pertenece a rA. Esto prueba precisamente el paso requerido en J.

### Obligaciones de la infraestructura que se recorrieron

| Bloque | Verificación realizada |
|---|---|
| A1, 2999; A7, 3096 | Regularidad en ℓ de `A[X]/(ℓX−E)`, reducción módulo ℓ e intersección `A∩ℓ^n A_max=(ℓ,E)^n`. Cierre de `(δ)` con ℓ∤δ: no se presume noetherianidad de A. |
| A5/A6, 3179/3195 | Coordenadas S-lineales sobre A mediante aproximaciones `(ℓ,z)`-ádicas y separación; el argumento de rango finito utiliza esas coordenadas, no una base de tamaño finito de todo A. |
| A2–A4, 3259–3320 | Contracción por Frobenius, control de denominadores y aproximación; la división monica en la variable E/ℓ mantiene la integridad. |
| A8, 3365 | Extensión de aplicaciones S-lineales a B⁺; el bicomutante S_B las hace S_B-lineales. La propiedad con escalares K′ usa aproximación módulo E^n. |
| `pkf:key`, 2804 | El argumento de soporte mínimo se aplica sobre el cuerpo residual de valoración después de normalizar una coordenada a 1. La aproximación Ax–Sen–Tate y la separación por coordenadas contradicen `det Q≡0 mod ℓ`. No se sustituye una congruencia por una igualdad de invariantes. |
| `pkf:frame-pm`, 2845; `pkf:main`, 2868 | De la saturación y las divisibilidades se obtienen `QQ′=τ^(2a)`, `UZ=E^(2a)Q`, `YZ=E^(2a)` y el frame. Las matrices corresponden al retículo L original. |
| `pkn:frame`, 2130; `pkl:std`, 3593 | El test de coeficientes y la cancelación de τ identifican M_inf con el módulo libre del frame y `std_l=φ^l M_inf`. |
| `pkl:valret`, 3718; `pkl:R`, 3837 | La retractación se define respetando todas las relaciones, preserva las filtraciones y conmuta con la proyección de parámetros. No se aplica una retractación arbitraria a coeficientes sin comprobar sus relaciones. |
| `pkl:G0`, 3977; `pkm:lower`, 1668 | El cociente por zτ sigue siendo integral; la identidad ciclotómica produce el coste `vℓ(k)+1`. En ℓ=2 el término final tiene valoración estrictamente mayor gracias a v(π)>0. |
| `pkm:zpow`, 1711 | Se elige el menor exponente que funciona en todas las letters. Frobenius y el descenso de nivel dan `a≤floor((a+e(n₀+κ))/ℓ)`; ésta es la fuente de la desigualdad inicial. |

Los inputs externos utilizados son los enunciados clásicos P1–P3, P5–P6 impresos en 2260–2298: estructura de los anillos de Fontaine, comparación cristalina y filtrada, Ax–Sen–Tate e invariantes de C(j). No se ha intentado reprobar esos teoremas clásicos. La referencia primaria de Colmez, §III.1–2 y §III.4, identifica B_max y B_cris para las representaciones cristalinas y permite verificar que aquí se usan esos anillos y no un anillo de convergencia distinto: [Colmez, texto del autor](https://webusers.imj-prg.fr/~pierre.colmez/iwasawa-deRham.pdf). Para la comparación filtrada: [Fontaine, Exposé III](https://www.numdam.org/item/AST_1994__223__113_0.pdf). Son dependencias matemáticas estándar, no certificados de los nuevos límites numéricos.

## 2. I2: costes de profundización

Se leyó íntegramente 4480–4848. Tres puntos potencialmente delicados quedan resueltos:

1. **Valores al nivel a.** `K_a` es el campo de fracciones del anillo generado por K′, S_B y `φ^(−a)S`. Si f es S-lineal, `f′=φ^(−a)fφ^a` también lo es, aunque `φ^(−a)S` no esté contenido en S. La igualdad usa `φ^a(S)⊂S`. Al eliminar un denominador común, A8(c) prueba `pke:valret`; se conserva cualquier submódulo B_dR⁺, en particular todas las filtraciones. `pke:values` obtiene μ_a(x)∈K_a mediante una coordenada κ_j no nula sobre el denominador: no presupone lo que debe probar.
2. **n≠0 y todos los primos.** La identidad `δX=ω′^n−1` tiene `δ=zτ`; δ es unidad en B_dR⁺ a cada nivel, pero no en A. La divisibilidad integral se establece antes de usar esa unidad. Para n<0 se usa `ω^(−k)−1=−ω^(−k)(ω^k−1)`. La valoración de la potencia crece exactamente por vℓ(n), porque `v(θ(ω−1))≥v(π)+1/(ℓ−1)>1/(ℓ−1)`; esto incluye ℓ=2. El coste adicional `d_v+3a` cubre el diferente y la comparación de θ con θ_a. Se obtiene `p_a | υX−ℓ^cost`.
3. **n=0.** No se trata mediante una falsa valoración de cero. Se promedia sobre `ℓ^cost` traslaciones Kummer, con cost=d_v+3a≥a. La suma de raíces de unidad deja exactamente las potencias z^k con ℓ^a|k; sus valores están en K′. Tate da entonces un valor constante módulo Fil¹.

Para n≠0, si μ_a(x)=γ+y, y∈Fil^n, la operación `D=ℓ^cost x−υδ⁻¹(gx−x)` cancela el coeficiente principal de y. La retractación conserva la nueva congruencia. Además, por G0 y la estabilidad de los órdenes, D y su retractación tienen el coste requerido para **todos** los órdenes ya adquiridos. La composición no los destruye. La inducción `pke:A` elimina un par (a,n) de altura n máxima, evitando presuponer que los pares se pueden aplicar en un orden cualquiera. Finalmente, el ajuste por `ℓ^(e′−e−Σcost)` produce exactamente la proyección deseada en I2.

## 3. I4: longitud, pocos pesos bajos y la constante

Se leyó íntegramente 5270–5820, incluida la parte de `pkh:div` que quedaba fuera de una salida truncada. No se deriva una longitud a partir de un mero anulador: se controla también el número de generadores de la ℓ-torsión.

`pkh:lead` escoge un menor de **valor absoluto máximo** entre un número finito de menores. Cramer da coeficientes en O_C. Se levantan a A y se retraen a S. Reducir S módulo E deja Λ, de rango f sobre Zℓ. Por ello `fn+1` vectores admiten una relación primitiva con un coeficiente igual a 1. Esto explica el factor f y el uso de la multiplicidad del peso u; no cuenta simplemente el número de pesos distintos.

En `pkh:div`, de `ℓx−w` con profundidad incrementada no se concluye ilegalmente que x tenga esa profundidad integral. Se construye primero `w′=E^(−ℓ^a)Aw`, con A un operador de coste cero; la condición a-free asegura que existe. La identidad `E^(ℓ^a)−p_a=ℓr` da `m=rw′−(Ax−x)` en el módulo integral de orden c. Sólo **después**, sabiendo ya que `x−m` pertenece al módulo ambiente requerido, se cancela ℓ en las condiciones de filtración de B_dR⁺, donde ℓ es una unidad. Ésta es una cancelación válida.

`pkh:len(iv)` muestra que un cociente muerto por ℓ^t y con ℓ-torsión de dimensión ≤m tiene longitud ≤tm. Se prueba por inducción incluso si inicialmente no se supuso finitamente generado. Las relaciones primitivas anteriores establecen exactamente esa cota de dimensión.

La eliminación de polos contribuye `a n_i`. El coste al nivel cero en una ventana negativa es ≤`(a+1)n_i`: para pesos lejanos NM elimina todos los múltiplos; para los bajos se usa Legendre. Al nivel uno el coste es `3(W+1)r_(i−1)+6a n_(i−1)`, porque los únicos costes de valoración son cero, también para y=0 por la convención expresa. La suma sobre la permutación de letters da

`Σ_i [(8a+1)n_i+3(W+1)r_i] ≤ 11Σ_i[n_i(a+1)+r_i(W+1)]`.

La cota publicada 11 no necesita una pérdida adicional. NM se usa para la suficiencia de estos pasos; no se deduce aquí su necesidad. El contraejemplo a la necesidad de NM registrado en `04-selmer-hodge.md` permanece válido y no refuta I4.

## 4. I5 y el scheme: cierre local y obligación cohomológica restante

Para evitar tratar `pkd:scheme` como una caja negra, se leyeron 4860–5235 y 6730–6995. En I5, el anillo de series no se identifica informalmente con B⁺: `pkg:Shat` construye una inyección en Λ[[T]], T=z/ℓ, y prueba `∩ z^n S_B=0`. La serie de `pkg:series` usa esa separación para eliminar un resto; no necesita que ese resto tienda a cero en una norma que no se controló. El parámetro `X_l=z^(ℓ^l)/ℓ²` pertenece a ℓ·Shat precisamente por `ℓ^l≥3`.

La aproximación simultánea de V y V⁻¹ cuesta dos veces `2δ`. Las columnas de M y de `ℓ^(4δ)−MM′` tienen valores constantes módulo E^A y generan un módulo que contiene `ℓ^(4δ)S^d`. De allí procede **4δ**, sin una constante dependiente del rango. La extracción del coeficiente de grado N de un polinomio monico da la proyección correcta módulo E^A; la corrección del error utiliza el anulador ℓ^κ en la letter de origen. El resultado final tiene proyección exactamente `ℓ^(κ+4δ)c`, no sólo una congruencia.

En scheme se verificaron por separado:

- Las condiciones `(C)` cubren todos los pasos de profundización, pues los órdenes coinciden para niveles mayores que l.
- El requisito `s_i=0 o s_i<β_i` excluye los pesos que impedirían obtener órdenes ρ_(−η).
- En una long gap, I5 se aplica a la side de ventana negativa del pivote; los pesos de las letters intermedias están acotados por ω, con `N<β_pivot≤A`.
- Transportar por φ^t da profundidad 1 antes del pivote y 0 entre el pivote y el corte. Los únicos pasos añadidos son `(a,0)`, t<a<l, con coste 3a porque el chart es no ramificado.
- En el pivote, la desigualdad crítica de rule es `A+min(η−u,0)≥1`; resulta de u≤A y η≥1. Fuera del pivote se obtiene 1+0.
- El shift cero del corte anterior se utiliza **dos veces**: para el anulador puro en I5 y para `rule_(l,0)`. No puede borrarse de las hipótesis.
- El exponente final de walk es `e+e′+κ=2e*+κ`.

La lectura del ensamblaje de walk confirma la telescopía por Frobenius y la separación de movimientos. Falta en esta tanda reconstruir desde su definición el criterio SCC y la prueba previa de que estos movimientos producen el cup-product cero. **Próxima acción:** comenzar por 650–820 (`pkp:def-pairing`, safe pairs, SCC, `pkp:letters`), recorrer el operador φ−1 en el módulo residual y comprobar la integralidad del coborde, antes de elevar el dictamen parcial a un (a) del teorema principal.

## 5. Segunda tanda: cierre de SCC, cup products y walk

**Actualización posterior a las secciones anteriores: la obligación cohomológica allí indicada quedó cerrada.** Se leyeron y reconstruyeron `pkp:AS` (915–986), la prueba íntegra de `pkp:pairing` (1001–1071), `pkp:letters` (1074–1086), `pkp:cut` y `walk-arith` (1131–1186), `pkm:walk` (1368–1398) y `pkc:cup` (6323–6354). Dictamen de estos pasos: **(a)**.

La comprobación no consiste en citar la palabra «cup». En M=W(C^flat)/ℓ^m(1), Artin–Schreier–Witt hace φ−1 sobreyectivo. Si `(φ−1)d` tiene todos sus primeros m componentes en la maximal ideal del tilt, entonces d difiere de una constante de Z/ℓ^m(1) por un elemento pequeño. La constante es única porque `F_ℓ∩m^flat=0`. Esto se prueba coordenada a coordenada y no usa ℓ impar.

Para los dos puntos x,x′ y los intermediarios w,w′, se escoge y con

`(φ−1)y = <w,φx′−w′> + <x,w′−x′>`.

La cochain f impresa en 1009 satisface dos identidades, verificadas expandiendo el coborde:

- `(φ−1)f(g)` es la suma con signos de los cuatro emparejamientos que definen los movimientos seguros;
- `ℓ^(e₁+e₂+κ) P(α(g),gα′(h)) = <gx−x,g(hx′−x′)> + (df)(g,h)`.

Los términos adicionales pertenecen a la parte pequeña. Escribir `f(g)=k(g)+δ(g)` con k constante y δ pequeña convierte la segunda igualdad en una igualdad **exacta** con dk: una constante pequeña es cero. No se descarta un término pequeño solamente porque tenga valoración positiva.

La continuidad de k también está probada: cerca de 1 los cociclos y la acción en los retículos son cero módulo ℓ^m, y la continuidad de las primeras m coordenadas de Witt hace f pequeña. Por unicidad, k=0 allí. La ecuación del coborde implica luego que k es localmente constante en todo Γ′. No se utiliza una solución arbitraria de Artin–Schreier como si fuera automáticamente continua en g.

La restricción a Γ′ no pierde una potencia de ℓ: corestricción tras restricción multiplica por el índice, que es primo a ℓ por la definición de chart. La clase es ℓ^m-torsión; por Bézout su anulación en Γ′ implica su anulación en Γ. Finalmente `pkc:cup` usa explícitamente Hilbert 90 y la sucesión de Kummer para inyectar `H²(Γ,μ_(ℓ^m))` en `H²(Γ,Qbar_ℓ^×)`. Por ello SCC sí implica el coborde en los coeficientes finitos que exige el defecto local de P55.

Las letters no interactúan porque P procede de una forma O-bilineal: `P(ζv,v′)=P(v,ζv′)`. Si sus letters son distintas, su diferencia Teichmüller es unidad y P(v,v′)=0. La aplicación final de walk no introduce factores por el número de letters. Se verificaron las tres desigualdades de `walk-arith` separando a<l, a=l, a>l, y sus casos con d=0.

**Estado actualizado:** `pkd:scheme` queda certificado con su conclusión SCC, no sólo como deducción condicional de una regla cohomológica no revisada. Para cerrar todo el teorema principal de P56 siguen las especializaciones `sparse`, `any`, `generic`, `tame` y `data` con todos sus rangos y con la identidad de las clases de retículos en P55. Algunas conversiones numéricas ya constan en el informe inicial; faltan su recorrido completo y ensamblaje en un único dictamen.

## 6. Tercera tanda: las especializaciones y su alcance global

Se reconstruyeron `pkt:add` y `pkt:I3` (4166–4440): la pertenencia al módulo integral se prueba antes de sumar órdenes; la desigualdad se exige para **u+u′≤v**, no solamente igualdad. El test de formas de Hodge prueba esa condición con los pesos que sí ocurren. La forma de la extensión dual tiene término `ℓ^m φ+aψ`; su equivariancia usa precisamente el cociclo de defecto de ψ. El caso simétrico de la regla contiene g aplicado al movimiento de la segunda side, como exige la identidad del coborde.

Se leyeron íntegramente los ensamblajes `pkc:generic` (6460–6590), `pkc:tame` (6629–6690), `pkd:sparse` (7050–7119), `pkd:any` (7124–7188), `pki:crys` (552–623), `pkj:chart` y su prueba (5840–6150), y `pkd:data` (7190–7295). Resultados:

| Resultado | Dictamen de esta tanda | Precisión |
|---|---|---|
| `pki:sparse` / `pkd:sparse` | **(a)** | Se verifican los tres requisitos K,C,G de scheme, y el rango ℓ=2 queda en la alternativa de signo constante, no en la long gap. |
| `pki:any` / `pkd:any` | **(a)** | Los cortes tienen distancia ≤2; la única configuración no plana tiene pivote 0 y exige `G+7K≤floor(b/ℓ)`. La desigualdad N<b y el coste `22K+3` se siguen de ella. |
| `pki:generic` | **(a), como criterio suficiente** | El argumento de pocos pesos bajos y la longitud normalizada se verifican; NM no se declara necesario. |
| `pki:tame` | **(a)** | Los polinomios en K(s₀) y K(s₀⁻¹) se usan en el sentido correcto para L y para la dual del tensor. |
| `pki:crys` | **(a)** | Deducción uniforme de los cuatro criterios bajo S1–S4 y la definición de letters reading thickness. |
| `pkj:chart` | **(a), bajo los datos citados de P46** | Se comprueban las raíces prime-to-ℓ, ambos sentidos de los ratios, la constancia del signo en primos del conductor y la transferencia de sparseness. |
| `pkd:data` | **(a), bajo M2/G4 y los datos citados** | Los pesos de la dual son −u−1, y la clase tame de la dual usa K⁻¹. No certifica por sí mismo que las representaciones automorfas de P55 satisfagan M2/G4. |

### Controles que hacen válida la uniformidad

**Sparse.** La distancia entre cortes es ≤2J+1, incluso si no hay letters gruesas. Si una configuración no es plana, hay un único pivote grueso interior y su distancia al corte anterior es J+1. Con `κ=4ϑ+(J+1)M`, `e*=8ϑ+6(J+1)M`, el exponente de scheme es `20ϑ+13(J+1)M`, menor que el publicado. En la alternativa ramificada de signo constante no se invoca I5. El coste de valoración se suma en dos intervalos de radio ≤3η, no sobre una ventana de tamaño b.

**Any.** Con q=floor(b/ℓ), el shift es max(q−7K,0), y κ=14K. Si el sucesor es delgado, kill-J basta; si es grueso, `(ℓ−3)(7K+q)>b+M`. El presupuesto de profundización es `62K+6 lgℓ(2(b+M))`, que con κ da exactamente e*. La long gap restante tiene A=b+V y δ=2K. No se omite una configuración de signos distinta.

**Generic.** La elección de V depende solamente de L, antes de escoger Y y el pairing. Esto es indispensable para acotar la longitud del cociente por el ortogonal de **toda** C(U). En la ventana negativa la comprobación al nivel uno se divide exhaustivamente en: peso de L bajo; peso de L lejano y peso de Y bajo; ambos lejanos. En el último caso las ventanas tienen signos opuestos y `|u+u′|≤W`, que da la suma de órdenes ≥1. La longitud de Zℓ se divide por `[O:Zℓ]=len_Zℓ(O/ℓ)`; no se confunde con el grado residual o con el índice de ramificación.

**Tame.** `e₀≤ℓ^(r²)` y los polinomios que matan las tres sides tienen grados ≤N, ≤N y ≤N²; κ=r²(N+1)² cubre cada `r²(deg q+1)`. El chart usa ζ=1, de modo que no necesita agrandar O para contener todas las raíces de su grado residual. El paso gap usa a=0 y NM porque todos los enteros examinados tienen módulo <ℓ. El resultado no tiene una dependencia oculta del rango de Y.

**Uniforme.** Para ℓ≤Q, la condición de thickness proporciona o bien un chart no ramificado con ℓ≥7 o bien signo constante; se emplea sparse con radio 2G. Para ℓ>Q y λ≥h³ se emplea any. Para λ<h³ el producto incluido en λ excluye los múltiplos de ℓ en `(b−30h³,b+30h³]`; los de la ventana baja se excluyen por `ℓ>198G`. Así se obtiene NM con a=2(λ+1). Si λ<floor(h/5), la separación de pesos negativos excluye `[-a,0)`. Si no, `K≥W+1` y la cota I4 da la longitud publicada. En los dos primeros rangos, la cota de rango de Z_f de P55 convierte exponente en longitud; en el tercero se conserva directamente la longitud. No se vuelve a multiplicar por el rango en el caso (d).

**Chart.** Fuera del conductor, una letter determina la restricción a E_v porque ese campo es no ramificado y generado por μ_(ℓ^f−1). En un primo del conductor, las letters no necesitan distinguir embeddings delgados: éstos quedan absorbidos en el radio 2G. Para ℓ|q₀, la igualdad hipotética de signos opuestos contradice la valoración de `(1+sqrt(−d))/2`; para ℓ=d, contradice `d≡q₀/2−1 mod q₀`. La sparseness se transfiere con el orden inverso de los tres puntos si se usa la lectura R⁻. Se contrastaron en P46 las cláusulas `q₀` múltiplo de 18480, `d≡q₀/2−1`, `q₁=q₀·3l₀(s)2^s`, `27s<l₀(s)`, la definición de sparse y (D5) (P46, 2888–2971). No se afirma aquí haber reprobrado la existencia global de los datos de P46.

**Conclusión de alcance local:** las obligaciones matemáticas profundas de P56 que se dejaron abiertas en el primer informe ya tienen una reconstrucción hasta la cota uniforme y su aplicación condicional a los summands. No se encontró una línea fallida en esa cadena local. El enlace todavía no certificado globalmente es la premisa de P55 que identifica los retículos automorfos con las clases y pesos usados aquí (M2, G4 y base level), además de la existencia y demás propiedades de los datos de P46, que corresponden a sus respectivas auditorías. Esta conclusión no demuestra GRH: certifica el segmento local indicado bajo esas premisas.

## 7. Novedad y comparación primaria con Fontaine–Laffaille

**Novedad absoluta: (c), no certificada por esta búsqueda.** No se identificó en las fuentes primarias cotejadas el mismo teorema de exponentes explícitos de cup products, con la dependencia en ventanas, letras y grosor de P56. Esto no prueba prioridad. El componente potencialmente novedoso que sí se puede aislar es el cálculo cuantitativo que traduce separación de pesos y unos pocos índices malos en costo integral de anulación, y después en la pérdida local sumable de P55. Su construcción concreta está reconstruida arriba; no hace falta declarar creada una teoría completamente distinta para describirla.

La teoría integral más allá de Fontaine–Laffaille ya existía. [Fontaine–Laffaille, *Construction de représentations p-adiques*, §§6–8](https://www.numdam.org/item/10.24033/asens.1437.pdf) estudia plena fidelidad y módulos filtrados en sus rangos de pesos. [Liu, *Torsion p-adic Galois representations and a conjecture of Fontaine*, Thm.1.0.1 e introducción](https://www.numdam.org/item/ASENS_2007_4_40_4_633_0.pdf) da la caracterización cristalina/semestable por todos los cocientes de torsión de pesos acotados sin la restricción de Fontaine–Laffaille. [Liu, *Filtration associated to torsion semi-stable representations*, introducción](https://www.math.purdue.edu/~tongliu/pub/filtrationnew.pdf) estudia filtraciones y rigidez del tipo Hodge–Tate bajo congruencias suficientemente profundas, sin restringir ramificación ni pesos. [Caruso–Liu, *Some bounds for ramification of p^n-torsion semi-stable representations*](https://arxiv.org/abs/0805.4227) da cotas explícitas de ramificación para p impar, en función de n, e y el rango de pesos. Esos objetos y conclusiones son distintos del cup product de P56; no sustituyen su prueba.

**Compatibilidad con FL:** no se halló contradicción. Para el solapamiento utilizado en P55, ℓ≥4b+2 y ℓ∤q₁dM, los pesos están en [−2b,2b], intervalo de longitud ≤ℓ−2 que contiene 0; la base local es no ramificada. La conclusión de pérdida cero se deriva aquí de P56 y dualidad, no de afirmar que cualquier congruencia de retículos cristalinos se controla automáticamente por plena fidelidad FL. P55 3470–3480 declara expresamente que no usa esta última ruta y que haría falta formular los enunciados integrales sobre subcocientes. Esa cautela es correcta: una comparación de categorías en un rango común no es por sí sola una prueba del anulador de un cup product. La coincidencia en ese solapamiento es una comprobación de compatibilidad y de hipótesis, no una segunda demostración independiente por FL.
