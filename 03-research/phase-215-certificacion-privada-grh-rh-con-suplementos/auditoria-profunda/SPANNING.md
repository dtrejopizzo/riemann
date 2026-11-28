# Auditoría profunda de Spanning y sistemas de criba

Este registro continúa la revisión de P51/P52. Las líneas son de los `main.tex` locales. Estados: **demostrado** significa que se reconstruyó la obligación indicada; **fallo literal** identifica una inferencia falsa escrita; **pendiente** identifica la siguiente dependencia que falta cerrar. No se modifican los papers.

## Tanda 1 Paso de Siegel a cuadrados de sumas orbitales

Objeto: P52 `pff:S`, líneas 4223–4238; prueba 4279–4556. Se leyeron esas líneas completas, y las pruebas de medidas, soportes y fibras en 4640–5096 y 5220–5520. La estimación de criba real (R) y el límite de masa finita (F) no se infieren de esta auditoría: aquí se separa el paso de ensamblaje (S) de esos otros resultados.

### Hallazgo literal con reparación ya disponible en el manuscrito

**P52:4364–4365, `pff:offT`: fallo literal.** Se corta la frecuencia a `b∈u bar(u) O_skew` y luego se dice que al tender `u→0` los integrales cortados convergen al integral sobre todo el espacio. Bajo la topología local usada, esos dominios se contraen a cero. La región dual `(u bar(u))^{-1} O_self` se expande; tampoco es una aproximación de la identidad. No hay una convención de tamaño inverso declarada en este párrafo que cambie el significado de `u→0`.

Modelo exacto: sea `E_v/Q_5` cuadrática no ramificada, `k≥3`, forma estándar `Q(x)=Σbar(x_i)x_i`, `α=1`, y `Ψ=1_{e_1+5O_E^k}`. Normalizamos ambas retículas aditivas a volumen uno y el carácter como en `pfg:duality`. Para `u=5^j`, todo `b∈5^{2j}O_skew` da fase trivial sobre ese soporte, de modo que el integral cortado es `5^{-2j}·5^{-2k}→0`. La densidad de `Q=1` en ese soporte es `5^{1−2k}>0`: el mapa `Q−1` lleva el soporte a `5Z_5`; su coordenada real en la primera variable tiene derivada unidad después de extraer el factor 5, y las fibras se cuentan por Hensel o por cambio de variable local. El promedio normalizado sobre la fibra es por tanto `vol(soporte)/vol(5Z_5)`.

**Reparación sin pérdida:** tomar `u=varpi_1^{-j}` con `varpi_1` de `pfg:psi(c)`. Los dominios `u bar(u)O_skew=varpi_1^{-2j}O_skew` agotan el grupo y los duales se contraen. Más directamente, el manuscrito ya contiene el argumento correcto en `pfg:orth` y `pfg:fibres(a)` (P52:4970–5080): usa `B_l=varpi_1^{-l}O_skew`, que crece, y una cota integrable independiente de `α`. `pfg:rem-fibres` aplica expresamente ese resultado a `pff:offT`. Por eso esta errata no deja sin prueba la identidad local ni cambia la constante de (S).

### Obligaciones cerradas por reconstrucción

| Obligación | Estado y justificación |
|---|---|
| Dualidad skew/self-adjoint, incluso en residual 2, `pfg:psi`, `pfg:duality` (4899–4967) | **Demostrado.** Existe elemento de traza uno y unidad skew en la extensión no ramificada; la descomposición integral en dos coordenadas prueba que las retículas de volumen uno son duales. No se divide por 2 en la prueba local. |
| Cota de Gauss `pfg:gauss` (4993–5022) | **Demostrado.** Diferenciar la fase deja un carácter lineal; la unimodularidad identifica su anulador con `I_b^κ`. El volumen del estrato de frecuencias de índice `I` es ≤`|g|^{-1}[O:I]^{1/2}`. Sumando se obtiene `∫|G|≤ζ_O(μ)|g|^{κ−1}` cuando `κ≥2μ+1`. |
| Construcción de `ν_β`, `pfg:fibres` (5024–5096) | **Demostrado.** Combinación finita de indicadores de clases, Fourier absoluto, ortogonalidad en `B_l`, dominación independiente de `β`, límite positivo y soporte en la fibra. La continuidad y desintegración siguen por convergencia dominada; la unicidad se recupera con promedios sobre slabs decrecientes. |
| Coarea `pfg:coarea` (5228–5248) | **Demostrado.** Cambio de base de determinante `bar(π_N)^{-1}` y cambio `t→−N^{-1}t` dejan exactamente `|π_N|_T^{-1}`. Sólo aparecen finitas funciones `φ_t`; la dominación anterior permite pasar el límite bajo la integral. |
| Soporte compacto orbital `pfg:Op` (5295–5320) | **Demostrado, con axiomas de gauge explícitos.** `pfg:cramer` acota las columnas del unipotente; `pfg:unipinv` y `pfg:sizehead` acotan `y` por `60n²`. Aplicar lo mismo al head conjugado acota también la segunda posición; el soporte de `l` es compacto. La invariancia por el abierto `K_M` da constancia local uniforme en `l`. |
| Extensión de la fibra `pfg:fibrepairing` (5322–5362) | **Demostrado a partir del soporte anterior.** La integral sobre `H_T` tiene soporte compacto; la aplicación orbital es abierta (Baire). Una cubierta finita por bolas da un módulo común de constancia y una extensión compactamente soportada e invariante. No se requiere que `H_T` sea compacto. |
| Finitud del conjunto de heads | **Demostrado.** P51:3557–3564 define `B` por cota de todas las conjugadas de enteros algebraicos y `T_entries={δ/δ′}`. Es finito. Así el uso de `pff:headsum`, formulado para conjuntos finitos, no encierra un intercambio de sumas infinitas. |
| Separación `pff:sep` (4464–4475) | **Demostrado, suponiendo el nivel libre citado.** Igualdad de `σz` hace `σ_1^{-1}σ_2∈H(E⁺)`; la congruencia local y la integridad exterior lo sitúan entre los mismos dos representantes de clase, con elemento de `J_X`; la trivialidad del estabilizador da igualdad. |
| Conteo de cosets `pff:headsum` (4443–4462) | **Demostrado como álgebra de matrices de Gram.** Para cada reducción `s_i` se seleccionan exactamente `#C` coordenadas distintas en `C×C`. Cada sumando es no negativo; descartar los demás sólo disminuye el lado derecho. No se usa desigualdad triangular con una pérdida `#heads`. |
| Suma sobre una fibra `pff:fibresum` (4477–4492) | **Demostrado.** Los puntos `l_θ=k_θl_0` ocupan cosets disjuntos de `H_T∩K_M`. La función integrada es no negativa y constante en cada coset por (W2). Cada coset tiene el mismo volumen por unimodularidad. |
| Pesos y masa `pff:weights`, `pff:rhoD` (4494–4521) | **Demostrado.** La fórmula del producto para cada entrada cancela `κ_ρ(p,1)` con los valores absolutos arquimedianos. Queda `ρ_p κ_ρ(p,1)=r_*√G_t`. Además `r(Z)=μ_H(H∩K_M)vol(K_M)^2 #C·(#Hbar #Ubar²)` exactamente. |
| Ensamblaje final (4523–4556) | **Demostrado como implicación de los insumos identificados.** Agrupar por `t`, luego por `(c,v)` y por `(c′,σ)`; aplicar cosets, separación y Siegel; dividir por `G_t r(Z)/D`. Esto deja exactamente `(1+b^{-6})a_* ΣR_pq J^T_n(p,q)`. |

### La fórmula de Siegel y su constante

Se descargó el original de Weil en `fuentes/weil-1965.pdf`, con extracción `fuentes/weil-1965.txt`. Fuente: [Weil, Sur la formule de Siegel dans la théorie des groupes classiques](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5988-11511_2006_Article_BF02391774.pdf).

El teorema 5, páginas 76–77 impresas, usa medida de masa uno y condición `m>2n+4ε−2`; en el caso unitario `ε=1/2`, `n=1`, exige `k>2`. La proposición 8 permite el caso anisótropo. La hipótesis local de transividad puede satisfacerse en un lugar finito split: el grupo es lineal general y actúa transitivamente sobre pares con producto prescrito y rango máximo. Ésta no requiere RH. Así, el rango y la normalización de masa uno citados en `pfg:weil` coinciden con la fuente primaria.

En P52:5462–5520 se reconstruyó la extracción del coeficiente `α>0`. El coset de identidad no contribuye; Bruhat parametriza los demás por `E⁺`. La representación de Weil usa el carácter racional estándar y la medida adélica de covolumen uno. La Fourier arquimediana de la gaussiana da `π^k α^{k−1}/(k−1)!`. La descomposición del cociente compacto en clases de nivel libre da peso `1/#C` por clase. El factor restante es `|disc E|^{1/4}` por la normalización de la variable self-adjoint finita. **No hay un factor 2 de Tamagawa faltante**, porque el cociente del grupo se integra desde el inicio con masa uno.

La cota exterior a `T` puede justificarse limpiamente como producto de densidades locales, todas con `O_E` de medida uno, multiplicado por `v^k`. Weyl differencing y el conteo de caracteres de cada ideal dan `≤ζ_E(μ)v^k`, con `μ=3ρ+4` y `k≥2(μ+1)`. Para los datos, `2f·2^{2−μ}` es mucho menor que `b^{-6}`: se usa `ρ≥√x/2−1`, `f≤x^{12}`, `log b≤x^{1/100}`. Esta última relación es heredada de P46; no debe reemplazarse por la sola cota `b≥1000`.

### Obligaciones todavía abiertas de esta tanda

1. **Identificación global-local de Kloosterman (`pff:locKl`, 4414–4441):** la expansión local en cosets está reconstruida y conserva `vol(K_M)`. Para cerrar la igualdad global hay que comprobar que, fuera de `T`, las soluciones unipotentes son integrales cuando el head tiene entradas unidades y `σ` es integral. El texto lo comprime en «all data are integral». La vía concreta es usar la eliminación por pivotes unidad de la celda grande, P51 `pbm:cell` (3450), y verificar que su inversa está definida sobre el anillo de enteros, sin introducir denominadores que no sean esos pivotes.
2. **Nivel libre y estabilizadores:** verificar el argumento de P46 `au:free`/lema 14.5 citado por la separación y por los pesos `1/#C`. Debe demostrarse para todos los representantes del género, no sólo para el retículo estándar.
3. **Caracteres y bases:** cotejar `ψ_f` bajo la conjugación por los representantes `h_c∈H`, y el uso del retículo de P51 `pb:KR`. El requisito relevante es que `H` normalice `U` y preserve el carácter Bessel; se revisará en sus definiciones.

Siguiente acción: cerrar 1–3 antes de emitir dictamen definitivo sobre (S), y luego reconstruir `pbc:C1` y `pbc:C2`. El fallo de dirección de límite no es la obligación pendiente: tiene reparación demostrada con dominación, incluso un argumento correcto ya presente en el mismo paper.

## Cierre de la tanda (S), 28-11-2026

Las tres obligaciones anteriores quedan cerradas:

1. **Celda integral:** P51:3450–3502 construye `u_1,u_2` por el emparejamiento perfecto de `A` y `γA`, seguido por eliminación LDU. Cuando todos los pivotes son unidades, las bases normalizadas y la eliminación son integrales. El retículo es suma ortogonal del bloque hiperbólico unimodular y el bloque medio. La fórmula `ux=x−Σ bar(h(e′_a,x))e_a` no divide por 2. Fuera de T los representantes `h_c` se absorben por conjugación y los pivotes son unidades, por lo que las variables unipotentes de la suma global son integrales. Los caracteres son triviales allí. Esto cierra el paso comprimido de `pff:locKl`, sin factor adicional.
2. **Nivel libre en todo el género:** P46:3598–3610 considera expresamente `Γ∩gJg^{-1}` para cualquier `g`. Para `H=U(X_0)` el grupo real es compacto, por lo que el grupo aritmético de un retículo fijo es finito. En una plaza split elegida, un elemento es conjugado a `1+p_0M_k(Z_p)`. Sus autovalores de orden finito distintos de 1 tendrían grado ≥`p_0−1>k`; imposible. La finitud y característica cero eliminan el caso unipotente. Esto justifica simultáneamente la separación y la igualdad de masas de las clases.
3. **Carácter y retículo:** P51:529–549 define `σ(u)` por las entradas en el marco; `H` fija el marco y sus duales, de modo que `σ(huh^{-1})=σ(u)` y lo mismo para `ψ_f`. P51:554–580 prueba `K_R=K_U⋊K_H` por el cociente `A^⊥/A`, describe el retículo medio y obtiene `K_H∩J=J_X`. No hay cambio de carácter causado por `h_c`.

**Dictamen local de (S): (b) literal por P52:4364–4365, pero con reparación completa y sin pérdida de constantes ya contenida en `pfg:fibres`.** Reemplazando el límite decreciente por el agotamiento creciente demostrado allí, la cadena Siegel → fibras → cuadrados de sumas orbitales se reconstruye correctamente, con las medidas y parámetros identificados arriba. Esto es un cierre de esta obligación, no una certificación del resto de P51/P52.

## Tanda C2: conteo medio de retículos

Se leyó y reconstruyó P51:8615–8823, junto con `pbc:disc`, `pbc:pack` y el nivel libre anterior. **Dictamen del argumento de C2: (a), bajo sus condiciones de tamaño expresas.**

- `pbc:average`: refinar a un subgrupo común convierte todas las fibras en conjuntos de cardinal `vol(J_X)/vol(J′)`; la conjugación conserva volumen. El nivel libre evita pesos de estabilizadores.
- `pbc:index`: los cosets corresponden a filas no nulas en cada plaza de `π_N`; `∏(q_w^k−1)≥N^{kf}/2`. No se confunden filas con rectas: no se divide por `N−1`.
- `pbc:forms`: descomponer la saturación como sumando directo deja `N^{fl}` formas en el complemento y a lo sumo el índice `i` en la saturación. Válido también para retículos proyectivos no libres.
- `pbc:zeta`: Hermite local da exactamente `∏_{j=0}^{r−1}ζ_E(s−j)`. La estimación `≤2^r` usa `s≥r+2ρ+4` y `2f≤2^{2ρ}`.
- `pbc:siegel`: Minkowski en dimensión real `2lf`, covolumen `2^{-lf}|D_E|^{l/2}disc`, y escoger sucesivos vectores independientes sobre E en índices `2f(i−1)+1`, dan `∏||X_i||^{2f}≤(lf rd)^{lf}disc`. El discriminante del complemento coincide por unimodularidad.
- `pbc:height`: cada subespacio se determina por una tupla independiente elegida; sumar sobre todas las tuplas sólo aumenta. La separación mínima ≥1 y packing dan `Σ||X||^{-2f(k+1)}≤5^{2f(k+1)}`. El caso `l=0` se trata por separado.
- Ensamblaje: con `D=b^{n³f}`, `μ=2ρ+4`, `disc=d_V i`, la desigualdad `i(d_Vi)^{-k}≤D^{μ+2}d_V^{-(k+1)}i^{-(r+μ)}` usa `i,d_V≥1`, `r≤k`. La suma queda acotada por `2^kD^{2ρ+6}[N^f(25n³f rd)^{f(k+1)}]^l`. Cada factor se absorbe en `β_*=b^{kf/4}`, conservando `1/2`. No hay sumas infinitas sin control.

**Rango de aplicación:** `l≤n³` es esencial en la última absorción; el paso de pares a corango ya auditado en `ppi:pillars` da `18i≤n³` y `l≤i+1≤n³`. No se aplica C2 en el intervalo `n³<l≤k`. Las condiciones Z4/Z5 dependen de los datos de P46, no de suponer solamente `b≥1000`.

## Tanda C1: conteo por retículo fijo

Se leyó íntegramente P51:8234–8613 y las dependencias de separación y celda P51:2569–2581, 6483–6595. **Dictamen del mecanismo de conteo: (a), con los datos ambientales de nearness y celda declarados.** La reducción de términos a esos datos sigue siendo una obligación distinta del teorema de segundo momento completo.

La convención en P51:8241–8251 es expresamente conjugada-lineal en la primera variable. Por ello `h(υ,·)` sí es lineal y el levantamiento proyectivo de Step 2 no tiene el supuesto fallo de conjugación que produciría leerlo bajo Cv1.

- Step 0: igualdad de marcos modulo movimientos conduce a `R_0`, luego la etiqueta fija da igual reducción; `K_R=K_U⋊K_H` y nivel libre dan la misma clase y el mismo doble coset elegido.
- Step 1: packing integral de `Z` y la cota de sus menores dejan `≤b^{270n³f}` valores; los módulos `Mδ` y `Mδ barδ` tienen norma `≤b^{2n³f}`.
- Step 2: `L′` es proyectivo (Dedekind), así que la aplicación al cociente se levanta. El cokernel del dual hermitiano tiene orden `disc(L′)^2`; colorear las ρ coordenadas cuesta `≤b^{2n³ρf}`. Los movimientos igualan los productos con `L′`.
- Step 3: la diferencia de las partes medias pertenece a `L_c∩(EL′)^⊥`, de rango l. Colorear módulo `Mδ` cuesta `≤b^{2n⁴lf}`. La adjunta de Y permite movimientos integrales. Las columnas compartidas son cero; la columna excepcional tiene norma cuadrada `≤4/N<1` en todas las plazas. Integridad y positividad la fuerzan a cero.
- Step 4: los vectores compartidos son fijos por los movimientos. Sus coeficientes se acotan usando la independencia cuantitativa del marco boxed; el exponente escrito `180n²−73n−23` es menor que `182n²`. Packing da `≤b^{366n⁴f}`.
- Step 5: tras colorear la parte A módulo `Mδ barδ`, se construye S integral y skew por la fórmula explícita de P51:8590–8603. Multiplicando por P se obtiene `SP=δ barδ Θ`; no se divide por 2. El movimiento correspondiente identifica los marcos y Step 0 concluye unicidad. La suma de exponentes es menor que `2000n⁶(l+1)f`.

`pbc:moves` se verificó expandiendo unitariedad: `W+W*=MG`, de modo que las partes lineal y cuadrática cancelan; `ν³=0` da inversa integral y congruencia de nivel. `pbc:shared` se verifica por Y y la forma de `f`; `ppi:cell` usa positividad de X_0 y el argumento de climbing mediante caracteres racionales. La identidad de Eichler requiere el elemento integral de traza uno ya declarado para el campo ambiental. No se está afirmando existencia de tal elemento para un CM arbitrario ramificado en 2.

**Siguiente obligación global:** estos cierres eliminan S, C1 y C2 del frente pendiente. Para certificar el segundo momento total queda reconstruir el uso de los pares de términos en `ppi:G`/`G′` y sus índices de intersección, y verificar la contribución espectral/multiplicidades (que no es consecuencia de C1/C2).

## Tanda G′ y cobertura de pares

Leído íntegramente P51:7604–8206, incluidos `pbg:climbp`, y cotejado con `pbe:link` (2838–2904) y `pbe:rank/pairs/two/XL1` (2941–3045).

**G′: mecanismo demostrado para los datos declarados.** La cadena de índices es real, no una sustitución de índice por determinante:

1. En el cociente unimodular por `I=A∩γA`, Jacobi con dos bordes da exactamente `d(L¹_γ)·ι=μ(γ)`; aquí se aplica con `c=N`, real positivo. Los subretículos `L_1⊂L_2⊂L_3⊂L_4` hacen dividir `i_γ`, `i′_γ` y `t(γ)` los tres índices sucesivos. Su producto divide ι, de modo que no se cancela indebidamente un índice.
2. El homomorfismo al retículo de filas módulo M tiene rango j′ y kernel contenido en `L⁺_γ`; su coste es `M^{2j′f}`.
3. La descomposición ortogonal en parte común, parte vista por los dos funcionales z y complemento da producto de discriminantes. La imagen de la parte común sólo se incluye en `C_γ`; se usa la desigualdad de discriminantes en la dirección correcta.
4. En `pbg:climbp` se verificó el papel de las dos plazas conjugadas: las coordenadas levantadas se soportan en una plaza y sus conjugadas en la otra. Esto produce matrices transvección distintas sin introducir la falsa positividad residual. La igualdad de caracteres para todo r fuerza una congruencia por dualidad con la diferente. `pbg:meet` hace dividir el determinante por cada primo conjugado distinto, con factor total `mn(s)`.
5. La forma de enlace entre los dos complementos es no degenerada y toma valores en `M O_E`: ambos términos están en el mismo bloque. Cauchy–Schwarz de Gram, aplicada después de dividir un retículo por M, y `||1−u||≤2`, dan `1≤(2/M)^{2if}d(L_y)d(L′_y)`.
6. Para el índice común, `v∈C_γ` produce `w=−M^{-1}(γ′γ^{-1}−1)y∈Λ∩(A+γ′A)`. Esto prueba la inclusión de imágenes que permite aplicar `pbg:indexmap`; el índice divide `t(γ′)`, sin irreductibilidad ni saturación supuesta. Multiplicar los dos cortes y la cota de los complementos da G′ exactamente.

**Observación de enunciado:** `pbg:jacobi` P51:7693 permite escribir `c∈O_E` arbitrario aunque llama hermitiana a `h+c^{-1}Σbar(h(p_i,x))h(p_i,y)`. Esa forma sólo es hermitiana para c fijo por conjugación (o perturbación cero). La identidad de determinantes es algebraica y sigue válida; todas las aplicaciones aquí usan `c=N>0`. Conviene corregir la hipótesis de ese lema. No es una ruptura de G′ ni requiere alterar sus cotas.

**Cobertura de todos los pares:** bajo la cota de tamaño (S) de `pbs:S`, ahora queda demostrada la parte combinatoria completa. G da `18i≤n³`; la dimensión del espacio común da `l≤i+1`, o `l≤i` en el caso degenerado. Por tanto C2 cubre todo par. Si i=0, ambos enlaces son iguales y ambos son degenerados o ambos no degenerados. Esto divide exhaustivamente en: enlaces iguales no degenerados, enlaces iguales degenerados, y enlaces diferentes (i≥1). Los segundos quedan en el error con `D=β_*^{-16}D_id`; los terceros usan el ahorro `(M/2)^{if}` y la cota `D_main≤(M/b⁶)^{kf}D_id`. No queda un rango intermedio sin contar.

La cota de `pbe:pairs` se obtiene sumando por l y cuesta `n³+1≤β_*`. Los pares en cada fibra `(etiqueta,L_{γγ′})` son a lo sumo el cuadrado de C1; esta sobrecuenta pares de clases distintas, lo cual sólo aumenta la cota. Cada par real determina su bloque y sus piezas estables, así que las sumas de `pbe:XL1` no omiten multiplicidades ni necesitan otro factor de número de clases.

**Pendiente precisa:** la cobertura anterior es condicional únicamente en la cota analítica `pbs:S` y en los tamaños `pb:sizes`. La auditoría sigue con `pbs:S`/`pbo:O1`, los sistemas locales que alimentan el Poisson iterado y la igualdad espectral que fija la constante principal.

## Tamaño analítico: avance y nuevo fallo local

Se reconstruyeron las secciones de Schur ponderado P51:9182–9707: proyección de un espacio negativo semidefinido a uno negativo definido, determinante de volumen, bases triangulares por Cholesky, Ostrowski–Taussky e integral de Hua. La elección de la última columna de una matriz triangular inferior es usada correctamente para dejar fijo el último vector. El jacobiano de Hua es `|det S|^{2k}`, y la pérdida `π^k/k!≤1` requiere k≥7, satisfecha. Colorear el módulo de filas cuesta `i_γ^k`; los desplazamientos se integran sobre un dominio fundamental de volumen ≥1. Esto último está justificado porque el campo ambiental sí contiene Q(i), P46:3354. No se necesita tal afirmación para un CM general.

El packing de marcos controla la multiplicidad dentro de cada color; las dos desigualdades de Schur, una para γ y otra para γ^{-1}, hacen aparecer `i_γi′_γ` con el exponente correcto. El argumento cubre las celdas degeneradas y la parte de la celda abierta donde `Nm(g)≤N^f μ`. La otra parte usa O1. No hay un hueco de rango entre ambas.

En O1 se reconstruyeron la sección explícita, la normalización GF, el añadido de vectores, la medida media, unfolding, Sobolev de dimensión `2n²`, la aplicación de Schur y la tensorización (P51:10050–10590). El factor GF es `V(r)/2^r`, obtenido por la integral gaussiana matricial; añadir los duales isotrópicos cuesta `2^{-ρ}`, sin otro factor por entradas fuera de diagonal. El producto final da exactamente `c_G`, no un factor desconocido.

**Fallo literal P51:10499–10500 (`pbo:tube`):** la dilatación `β→tβ`, `σ→t²σ` multiplica la medida por `t^{2ρk+2ρ²}`, no por `t^{2ρk+ρ²}`. El texto llama Q a la dimensión real y la usa como dimensión homogénea. Modelo mínimo: ρ=1, β∈C^k y σ∈iR; el jacobiano es `t^{2k+2}`.

**Reparación comprobada sin cambiar la cota:** definir `Q=2ρk+2ρ²` en todo el argumento del tubo. Se conserva `Q≤r²/2` porque `r=k+2ρ+1`, y el radio elegido `R_tube=Q²(T²+1)²` sigue dando `||vy||≤T^9≤T^10`. El cociente de volúmenes se convierte correctamente en `(1+1/Q)^Q≤e<3`. Así sobreviven exactamente el factor 3 y el exponente `10^5 n^4` de O1. No se corrigieron los papers.

La parte de O1 basada en Bessel pairs queda reconstruida después de esta reparación. **Dependencias pendientes:** comprobar externamente la entrada de lowest K-type y la fórmula Flensted–Jensen P49:teorema3.17, y auditar DS4 (la positividad cuantitativa del período Bessel). Se ha reconstruido DS1(i,ii) por Schur y DS3 P51:6124–6205 por Casimir, Lipschitz local y packing de bolas; DS2 P51:6054–6123 es correcto condicional en dicha fórmula explícita. La formal degree exacta depende de `pbr:degree`, que se coordina con el agente principal.

## DS4 y fórmula explícita de P49

Se leyó íntegramente DS4, P51:6712–7577. Se reconstruyó su argumento **condicional en la fórmula FJ y en la identidad del tipo K**:

- La escala `κ_τ=Mτ(varpi)/(2πi)` absorbe exactamente el carácter aditivo; invertir su signo se realiza por una isometría diagonal de orden 2 que preserva Haar.
- Los residuos de interpolación en los nodos enteros μ_i producen un marco con el Gram prescrito; Witt da la posición estacionaria. La longitud se acota por Gram–Schmidt usando también los vectores de índice hasta 2ρ, de modo que no se pierde el control de los vectores duales.
- El desarrollo de un menor tiene resto uniforme en dimensión por la norma de Frobenius. Al escalar sólo las partes que cruzan la proyección, el resto es función holomorfa par; Schwarz mejora `O(δ³)` a `400δζ²`. El paso `pbp:minorconj` compara las proyecciones conjugadas y conserva el error `10³δ(x²+κ²)`.
- FJ y la independencia del factor bloque diagonal eliminan los factores unipotentes. El peso de menores compactos satisface `|m_Λ(k)|²≤exp(−Q_Λ(k)/2)`, y `d_Λ≤e^{2T}` absorbe el complemento de la región gaussiana. La forma gaussiana da un cono con error `12e^{-100T}`.
- La posición estacionaria también permite localizar modulo `U(k−1)`: las filas y columnas fuera de X se controlan por la parte no compacta. La igualdad de trazas pasa a logaritmos por inducción de potencias. Esto justifica la fase, no sólo su derivada de primer orden.
- La combinación de error uniforme y decaimiento da `|θ|−2Re θ≤6EG`. Packing de la bola pequeña en la grande, el límite inferior local `|c|≥1/2` y el coeficiente monomial `h_kk^a` dan `vol(B_y)≤b^{60(r+k)²}|∫θ|` con el exponente escrito.

**P49 `pco:FJ`, 1848–2271:** leídos productos de menores, densidades de bandera, independencia del factor bloque, comportamiento K, Casimir, decaimiento e identificación. Las reducciones hasta `pco:rigid` son reconstruidas. En particular la invariancia de la densidad usa el módulo real `|b^{2ρ_c}|²`; la polarización holomorfa separa las dos variables y prueba constancia, por lo que no se está sustituyendo gratuitamente la descomposición polar por una holomorfa. El Casimir actúa con `|μ|²−2<μ,ρ>=|λ|²−|ρ|²`. La integrabilidad usa exponente h>n(n−1), satisfecha por h≥n²+1. La rigidez queda a cargo del frente de P49 (D1–D3), explícitamente coordinado.

**Fallo local de orden, P49:2250–2251:** se identifica `∫bar(F(xh))F(gh)dh` con `<R(x)F,R(g)F>`, aunque el operador declarado es `R(x)F(h)=F(hx)`. El cambio de orden no está justificado en un grupo no conmutativo. **Reparación directa exacta:** la línea anterior ya da `F(g)=∫e(h)F(gh)dh`. Sustituir `x=gh` y usar `e(h)=d·bar(c(h))=d·c(h^{-1})` da inmediatamente `F(g)=d∫F(x)c(x^{-1}g)dx`. Se omite la doble integral problemática; su conclusión y los Steps 2–4 permanecen con la misma constante. El cálculo no necesita centralidad de F.

Por tanto no se encontró una obstrucción nueva a FJ después de esta reparación: la obligación sustancial restante es exactamente la rigidez espectral D1–D3, que se verifica en el frente P49. El agente principal confirmó por separado la formal degree `pbr:degree` de P51 condicionada en esos mismos insumos.

## Cierre de entradas espectrales y avance en masas locales

El frente P49 contrastó las entradas externas con fuentes primarias: Atiyah–Schmid (1977), Theorem 8.5, p. 42, establece multiplicidad uno del tipo K mínimo `λ+ρ_n−ρ_c` y la forma de los restantes tipos; Vogan–Zuckerman (1984), Theorem 1.4, p. 54, proporciona la unicidad unitaria por Casimir y el tipo K cohomológico, y §§5.3–5.6, pp. 74–75, justifican la transcripción de D3(c). Fuente consultada por dicho frente: https://www.math.utah.edu/~ptrapa/math-library/schmid/atiyah-schmid.pdf . Con esa comprobación coordinada, la dependencia espectral pendiente de FJ y DS queda cerrada, tras la reparación local indicada arriba. El agente principal reconstruyó además `pbr:basic–degree`, P51:5199–5833, incluida la constante exacta de grado formal. No se atribuye esta comprobación externa a una lectura duplicada de este agente.

**Reducción global reconstruida:** P51:1483–1535, amplitudes → E1–E3. El uso de `pb:basic` después de E1 no es circular: sólo requiere E1 para `β(s)≤2 dim X`. Para E2 se separan todos los cosets escalares y su complemento; sus contribuciones son respectivamente ≤T/4 y ≤T/2. Para E3 la apertura excluye todos los cosets escalares, incluso R; así desaparece realmente el término inducido. Se usa `D_id≤b^{-11kf}D_main≤b^{-6k#A}D_main`. Todos los errores de raíz cuadrada conservan el factor final `1+4b^{-4}`.

**Masa real reconstruida:** P52:1072–1183 con H0–H5 en 909–924. La comparación L² entre el vector y su corte, integrada en la bola, cuesta `b^{6300nr³}` y se absorbe por `f_W≥4000n`, hipótesis explícita H5. La contribución sin corte es exactamente `c λ³ (#I)²/deg`, que se reduce a `(vol U(k)/vol U(r))λ/deg≤1/deg`. La cola utiliza el ahorro de posición remota; no se sustituye la constante principal por una constante implícita. Quedan como obligaciones del sistema local los lemas compartidos de pisos/gauges que producen esos ahorros.

**Masa finita reconstruida condicional en dichos lemas compartidos:** lectura de P52:3370–3840 y 4010–4222. La identidad de unfolding de `pff:unfold` respeta el orden `uyx(uy)^{-1}` y produce exactamente el factor λ. De aquí `m(Z)=λ²∫|k₀|²`; sobre K(M) la integral interior es `vol Z`, por normalidad, dando la parte principal `vol(Z)² vol(K(M))`. En la estimación de la norma del vector, aunque varias coordenadas puedan ser no nulas, todas representan el mismo coset `U K(M) g`: no se pierde un factor del número de coordenadas en la masa de soporte `vol(K(M))/λ`.

La construcción explícita de la base hiperbólica en `pff:L1` usa norma −1 y traza 1 en la extensión no ramificada, también en característica residual 2; su determinante es la unidad −c. La cota inferior de volumen del piso superior se obtiene por el coeficiente b unidad en `a u+b u′+y′`, transporte integral a z y la aplicación traza sobreyectiva, cuyo pushforward de Haar normalizada es Haar normalizada. Así no aparece un factor 2 perdido.

`pff:oneplace` conserva el índice exacto `p₀^r−1` de un **vector no nulo**, no una recta. Para `t=k−10¹⁰n⁴` y `k≥3·10¹⁰n⁴`, se verifica `6k≤9t`; el índice absorbe `B^{t+1}`, B=b⁹. La estimación de masa y la cota inferior para K dan precisamente el ahorro `b^{-6k}`. Al multiplicar lugares conjugados, el cambio de normalización Haar cuesta λ³ en m y λ en volumen, que cancelan en ambos lados: ahorro total `b^{-6k#A}` con constante principal 1. Las hipótesis fuertes se satisfacen en los datos ambientales; el resultado no está validado aquí para parámetros generales fuera de ellos.

**Frente restante delimitado:** lectura y reconstrucción completa de los lemas compartidos de pisos (P52:376–878 y 1183–3336), y del decay finito (3841–4009), para descargar las dependencias de masa y sistema local. No basta que las constantes finales encajen: ese frente sigue pendiente. E4 de P51 tiene además la entrada combinatoria `pbm:Phi`; su aplicación final 3396–3414 es aritméticamente correcta, pero esa entrada aún requiere reconstrucción específica.

## Pisos y descenso: cierre parcial detallado

Reconstruidos P52:376–878 y 1183–1756: medida de cuadrica, charts, invariancia Weyl, peso inverso, separación de marcos, corte en el primer vector profundo, sumación de shells y descenso exacto. La densidad de cuadrica conserva `κ_C=2`, `κ_T=1`; el mayorante `mod(t)^{-1/2}` es localmente integrable, también en el producto de campos finitos. La sección de Heisenberg cuesta exactamente `mod(c^{-1})^{1/2}` después de cancelar el jacobiano `mod(c)^{d_a}`. El paso de disintegración en bloque elimina sólo un conjunto nulo común a una familia numerable de bounds, suficiente para las integrales posteriores.

La invariancia Weyl no se supone para la medida singular de pisos: se prueba al completar con Haar del grupo superior y comparar integrales de funciones invariantes. La separación cruza los pesos antes de Cauchy–Schwarz y usa `w_p^{-1}=w_{bar p}`, preservando el mismo producto de módulos. El corte en primer vector profundo se justifica por inducción descendente; para j=0 ambos pivotes coinciden y dan el doble exponente, utilizado en la masa finita. La sumación de shells conserva un factor geométrico 2, absorbido explícitamente.

El descenso 1693–1756 compara leyes por traslación derecha de un piso sobre su cociente; no requiere que la propia medida del piso sea Haar. El cambio `τ→w_c^{-1}nσ` lleva exactamente a `Π(x;w w_c;nσg)` y al peso `mod(c)^{d_a}`. La hipótesis de integrabilidad del piso inferior controla por Tonelli la integral expandida antes de Fubini; no hay intercambio formal de integrales condicionales.

**Errata local adicional:** P52:1810, convención(iii), dice que `U_(<l)` fija los e_b para b<l. En general sólo preserva su bandera y actúa unitriangularmente: con l=2, `N_0` puede enviar e₁ a e₁+a e₀. La frase siguiente describe correctamente ese comportamiento, y el uso efectivo en las pruebas leídas es trivialidad sobre `Y^(l)` y congruencia módulo el span inferior, que sí se cumplen. Sustituir «fixes» por «acts unitriangularly on» repara esta línea sin cambiar cota ni identidad.

Pendientes tras esta tanda: pruebas de one-frame/ganancias por frecuencia y dos heads (desde1757), verificación de gauges reales y finitos que alimentan G4/G5, y decay finito. Los resultados anteriores están reconstruidos condicionalmente en esas entradas expresamente identificadas.

## Cierre del sistema real y de los tres teoremas compartidos

Leídos y reconstruidos completos P52:1757–3336. Se descargan ahora las dependencias one-frame, frecuencia y dos heads, y los gauges reales, de las tandas anteriores.

La desigualdad de Plancherel se prueba por regularización gaussiana y Fatou, con constante `P=π²` para el carácter `exp(c−bar c)`. En la cuadrica se usan **dos bloques disjuntos**: uno elimina la dependencia de su fibra en y mediante Cauchy–Schwarz, y el otro elimina la fibra de v; la fase restante permite Plancherel en X′. No se aplica incorrectamente Fourier a una medida singular. Parseval sobre Heisenberg conserva `mod(ξu)` y `c_a(u)`. El climbing usa `ξ=M^{-1},u=M`, por lo que se cancela exactamente el módulo del nivel en esa fase.

En one-frame el cambio de Weyl-ratio produce `J=∏mod(p_a/q_a)^{d_a+1}`. Al combinar con la densidad y los pesos se obtiene **exactamente** `κ_j²DJ=mod((q₀⋯q_{j−1})^{-1})≤Λ`; no queda un producto arbitrario de alturas de p. La ganancia por dos heads usa `M^{-1}(p_i/q_i−1)=−ξp_i` y luego `u=p_i^{-1}`, por lo que no se pierde un factor p_i en la frecuencia. Todas las integraciones de funciones positivas se realizan con Tonelli antes de las aplicaciones de Cauchy–Schwarz.

G5 real se verifica escogiendo un subespacio de dimensión s+1 en el que **ambas** isometrías preservan la norma euclídea: se imponen como máximo 3n ecuaciones y se usa `rank X′=s+3n+1`. La función `φ=36/q` tiene potencia s integrable, porque la ley radial tiene densidad proporcional a `t^s`; esto evita la divergencia que habría en dimensión s. El factor factorial absorbe el coste exponencial y da el exponente declarado `99n(i+1)`.

La normalización de Haar se reduce a las fibras de Gram ya reconstruidas en P51: cada par hiperbólico cuesta 1/4, z cuesta 1/2, y el bloque compacto cuesta `vol U(k)/2^k`. Con r=k+2ρ+1 todos los factores 2 cancelan. Sólo se necesita la desigualdad de Haar que se demuestra; la constante principal de masa sigue siendo ≤1/deg. El piso superior se identifica con el Gram de orbitales mediante `σ=h₁σ_c h₂`, un operador unitario independiente del head, y la igualdad `N(p^c)N(q^c)=c λ² h(c)κ_ρ(p,q)` conserva la normalización exacta.

H1–H5 se cotejan en 3252–3307: H2 se deduce con igualdad de reproducción B7 y Schur, H3 del producto de grado formal, H4 de DS3, H5 de S7(b) de P46. Tras las reparaciones locales ya registradas en FJ y O1, el sistema real R queda reconstruido para los datos ambientales, sujeto a la construcción de los vectores Bessel de P51 y a los datos admisibles de P46 (no se convierte esta frase en una certificación independiente de esas construcciones).

**Siguiente obligación:** finalizar decay/gauge finito (P52:3841–4009 y sus dependencias en §6), luego entrada E4/Phi y construcción Bessel/global si no están cubiertas por otro frente.

## Cierre de F: gauge, decay y piso superior finitos

Reconstruidos P52:3841–4009 y 5097–5227; con las dependencias de §6 ya reconstruidas en las primeras tandas, esto descarga el frente local finito F.

G5 finito usa Smith sobre cada DVR para imponer 3ρ ecuaciones sin denominadores en la base del kernel. Los vectores obtenidos son fijados por el unipotente conjugado; el factor k∈K(M) produce la congruencia de cercanía. La función de contenido satisface su integral por suma sobre ideales, con `d−s=m′+4>0`; se conserva exactamente `|β|^{-a-(d−s)}`. G4 utiliza fibras de una forma unimodular de rango2m′+2 y la cota de zeta, sin restricción adicional en2.

El piso superior3841–3937 fue reconstruido con orden de multiplicación explícito: al poner `l=(h′τ)(hσ)^{-1}`, la fase es `ω(l^{-1})`, y el orbital es `O_p(l)`. Por tanto el carácter final es `ψ_T(ξt)`, sin conjugación extra. Tonelli aplicado primero al valor absoluto y el soporte compacto de orbitales justifican Fubini aun cuando H_T no sea compacto. La coarea mantiene `|π_N|_T^{-1}`. Positividad y continuidad se deducen de Gram y de las fibras continuas, no de una identificación formal de distribuciones.

Para el decay, `α=M bar(βγ)βγ` controla simultáneamente inversos de los productos parciales y de los entries. En caso frecuencia, se escoge componente a componente η generando `(ξ,α^{200n²})`; la igualdad de caracteres en el soporte permite usar η. En caso dos heads se toma η=ξ. El ahorro se descompone en potencia `n(ξ)^{t/2}` y denominador `den(ξ)^{-6}`, pagando `Λ^{1200n²}`. Aquí `n(ξ)=|ξ|_T^{-1}` es el módulo inverso, **no** la norma de un ideal numerador; con esa definición, su multiplicatividad utilizada en3996 es correcta. `4E≤10¹⁰n⁴≤K` descarga todo el coste en los pesos de F.

**Estado de P52:** sus sistemas R/F y paso S han quedado reconstruidos para los datos ambientales, con la corrección de dirección del cutoff4364–4365 y la errata unitriangular1810 ya registradas. Esto es un cierre de los mecanismos locales y sus constantes, no una afirmación de que el texto original esté literalmente correcto sin esas correcciones. La dependencia que se traslada ahora a P51 es la construcción Bessel/global y E4/Phi; los datos numéricos/admisibles se controlan en el frente de P46.

## E4 y construcción Bessel/Poincaré

Reconstruidos P51:771–821, 3139–3414: positividad de la función de intersección como matriz de Gram; recursión exacta al quitar un par hiperbólico (celda abierta `NwLN` con parametrización biyectiva); recursión al fijar el primer vector (dos factores `q^{r−1}`, uno por ortogonalidad de caracteres y otro por N); bound de intersección de subespacios mediante Gaussian binomials; y desigualdad de menores singulares por Fourier tensorizado con los vectores de tipo positivo. Se verifica el exponente residual `j²−m/2≤−2` y la recurrencia `(1−4/q)Φ_j≤Φ_{j−1}+128(ρ+1)/q²`. La cota inferior1 se justifica directamente por `pbm:pos(c)` y el valor1 de la función inducida en la identidad. E4≤2 queda cerrado en el rango ambiental.

Reconstruidos P51:2229–2695: la longitud es continua por las dos desigualdades con g y g^{-1}; Gram–Schmidt es invariante bajo modificaciones unitriangulares. El covering de R tiene dimensión real2r² y exponente4r², absorbido por9r². El promedio que construye W converge absolutamente, es reproducido por e, y su norma L² es exactamente el período dividido por deg. La positividad del período se deduce de esa identidad; DS4 aporta su límite inferior. El cutoff conserva continuidad/tipo H y su error L² está controlado con el exponente escrito.

En el conteo global `pbe:count`, la reducción de representantes usa transvecciones integrales/Eichler con traza1, también al nivel N; el orden de reducción de los coeficientes de Gram–Schmidt es triangular. Dos clases con el mismo marco difieren por U: la parte H desaparece por nivel libre, previamente contrastado. Para marcos próximos, integridad en todos los conjugados fuerza igualdad de los Gram, positividad de X₀ elimina su componente, y el mayor índice no nulo de la componente isotrópica se elimina por la longitud escalada. Packing en dimensión2nrf da el conteo uniforme en y, no una afirmación de uniformidad término a término. Así la serie de Poincaré es acotada, reproducida y continua por continuidad L¹ de traslaciones del kernel.

El unfolding final B4 conserva `c_W=vol(R_f∩J)/vol(J) ·∏deg_τ/c₀τ`. La conjugación se maneja por la dualidad entre W y su contragrediente; al sustituir s por s^{-1} aparece justamente el promedio local construido. No se encontró una obstrucción adicional a B1–B7 bajo DS y los datos declarados. La dimensión finita de A_z se cita de P49 y no se sustituye por la mera convergencia de la serie.

## Cierre de las dos normalizaciones globales

Reconstruido P51:1573–2010 íntegro: los funcionales de fila y las partes imaginarias centrales se ordenan triangularmente; la traslación por un elemento bajo es aditiva en la coordenada siguiente. Las transvecciones de Eichler alcanzan todas las filas integrales permitidas. La existencia de un elemento de traza1 evita introducir 1/2 incluso en2. La caja fundamental se obtiene sucesivamente sin suponer que todas las coordenadas sean homomorfismos simultáneamente. La matriz triangular de traslación tiene jacobiano1. Invertir la caja convierte cosets derechos en izquierdos porque U es unimodular.

Se verifican los covolúmenes: la dualidad de filas cancela el factor del nivel N con el escalado de z; el centro usa `O_E^−=i O_{E⁺}` (i es una unidad del campo ambiental), de modo que su covolumen es `|D_E|^{1/4}`. Las sumas de dimensiones son `Σm_a=ρ(ρ+k)` y `Σ(2m_a+1)=ρ(2k+2ρ+1)`; los escalados restantes son `N^{−kf}Λ^{−1}`. Esto prueba el valor exacto ν_* para cada clase c bajo los datos del paper.

Contrastada la razón de masas1336–1357 con la fuente primaria [Gan–Hanke–Yu, ecuaciones(4.2),(4.3), proposiciones4.4–4.5](https://web.math.princeton.edu/~jonhanke/Web-02/Mass-Formula-of-Shimura/shimura-mass.pdf). El grupo es totalmente definido; el retículo estándar unimodular es maximal y su estabilizador hiperespecial en los lugares no ramificados. La norma de unidades de una extensión no ramificada es sobreyectiva, por lo que el determinante unidad no introduce lugares excepcionales. La fuente da `Mass_l=2^{−lf}·2·∏_{j≤l}|L(1−j,χ^j)|`; el factor2 cancela entre rangos. La ecuación funcional con conductor relativo trivial da el factor `2^f` por cociente, que cancela `2^{−f}`. Así se obtiene exactamente el cociente declarado, sin constante indeterminada dependiente del rango.

## Ensamblaje final del segundo momento

Reconstruidos P51:837–998 y1027–1110. El operador β es positivo; aplicar la estimación singular al vector que maximiza su forma cuadrática controla los términos fuera de la celda abierta. Un par es abierto si existe un Weyl para el cual todos los menores principales requeridos son no nulos; si no existe, el control singular se aplica al Weyl fijado. Las alternativas E2/E3 cubren respectivamente todos los bloques fijos y al menos uno no fijo. El margen acumulado es el `1+9b^{−4}` escrito. No se detectó un rango de pares ausente.

La comparación con el retículo original usa una conjugación unitaria de P y de su adjunto, no igualdad literal de ambos retículos; conserva exactamente la norma Hilbert–Schmidt. La estimación de etiquetas malas y el paso a la parte cuspidal están reconstruidos como argumentos algebraicos condicionados a la descripción de Green de los caracteres cuspidales del grupo lineal finito; no se ha reprobado esa clasificación externa en esta auditoría. Multiplicidades y grado formal se remiten al ledger MULTIPLICIDADES y a la revisión independiente de las entradas de P49.

**Dictamen actualizado por preguntas:** (1) la prueba escrita requiere las reparaciones locales registradas (FJ de49 y exponente homogéneo O1 de51); reconstruido el ensamblaje con constante exacta y uniformidad bajo las entradas ambientales y de representación indicadas. (2) **(b) literal**, primer fallo del límite en P52:4364–4365, reparable invirtiendo el cutoff sin alterar constantes; las fibras, Siegel y Poisson fueron reconstruidos. (3) **(b) literal** en el exponente homogéneo de P51:10499–10500; la reparación conserva la cota final y se reconstruyó el conteo exhaustivo. (4) revisión del frente independiente MULTIPLICIDADES, incluida su errata local sobre uniformidad global de una serie. Estos fallos de pasos no son contraejemplos al enunciado final de segundo momento ni a RH.
