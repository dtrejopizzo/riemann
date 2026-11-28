# Revisión matemática de los papers 51 y 52

Fecha: 28 de noviembre de 2026. Fuentes examinadas: los `main.tex` locales de 51 y 52, los enunciados y aplicaciones correspondientes de 46 y el mapa 57. Los números de línea se refieren a esas fuentes, no a los PDF. No se leyeron 47 ni 48.

**Actualización tras auditoría profunda.** El estado preliminar de este informe ha sido superado por la reconstrucción documentada en [SPANNING.md](auditoria-profunda/SPANNING.md) y el frente independiente [MULTIPLICIDADES.md](auditoria-profunda/MULTIPLICIDADES.md). Se reconstruyeron las pruebas locales de P52, las cotas Bessel y estacionarias, los conteos G/C1/C2/S/O1, el covolumen unipotente, la razón exacta de masas y el ensamblaje de P51. La versión escrita contiene fallos locales reparables; no corresponde clasificarla como íntegramente correcta tal como está escrita.

## Dictámenes por pregunta actualizados

| Pregunta | Dictamen y alcance |
|---|---|
| Segundo momento uniforme y constante exacta | **(b) para la demostración literalmente escrita**, por los pasos locales siguientes y el error de orden de FJ P49:2250–2251. La reconstrucción con reparaciones preserva `1+9b^{-4}`, condicionada a los datos ambientales y las entradas externas de representación identificadas en los ledgers. No se obtuvo un contraejemplo al teorema. |
| Siegel y Poisson, constante principal | **(b)** en P52:4364–4365: el cutoff `u→0` contrae el dominio en vez de agotarlo. El ledger da un modelo local explícito y reconstruye la reparación `u→∞`, con dominación y constantes sin pérdidas. |
| Cobertura y cotas de los pares | **(b)** en P51:10499–10500: el exponente homogéneo es `2ρk+2ρ²`, no `2ρk+ρ²`. La reparación conserva la cota final. La cobertura completa de rangos y los conteos fueron reconstruidos; no apareció una familia de pares omitida. |
| Igualdad de multiplicidades | Véase MULTIPLICIDADES: se verifica en el alcance cuspidal y con los parámetros precisos; contiene una corrección local de uniformidad de una serie. No equivale a invariancia incondicional del espectro para todos los grupos con iguales lugares finitos. |

La hipótesis adicional de tamaño requerida por C0 está disponible en los datos ambientales; debe explicitarse si se presenta el lema aislado. La clasificación de Green no fue reprobada desde cero. Los referentes nombrados por el autor no participaron en esta revisión.

**Nota de lectura:** el texto restante conserva las comprobaciones y preguntas de la primera tanda como registro. Las frases que allí indican que R/F/S, DS, G/C1/C2/S/O1, covolumen o masas estaban pendientes quedan reemplazadas por sus cierres en SPANNING.md. No son pendientes actuales.

## Segundo momento y la constante del término principal

P46:4692–4706, `au:moment`, pide

\[
\sum_{s\in\overline G}\|P^*\varrho(s)P\|_{HS}^2
\le (1+9b^{-4})\frac{D_X^2}{\deg\,\operatorname{mass}_r}.
\]

P51:180–195 reproduce los mismos tres enunciados; `pb:thmB`, P51:1112–1128, los deduce de `pb:est` y la comparación de multiplicidades. La norma es Hilbert–Schmidt. No se la debe confundir con la norma operatorial, para la cual el paso a generación tendría otro contenido.

La necesidad de una constante principal próxima a uno es real. Si las imágenes de una aplicación isométrica se distribuyen en un subespacio de dimensión `d/C`, un segundo momento con constante `C` todavía puede ser compatible con esa concentración. Por eso una cota con constante absoluta arbitraria no sustituye a la escrita.

**Comprobación (a), reducción condicional de L2.** En P51:3994–4026, si se aceptan (R), (F), (S), el teorema de criba y las cotas (C0), (C1), los factores finales son

\[
(1+b^{-6})\left[(1+b^{-9})^2(1+b^{-6})+b^{-10}\right]
\le 1+b^{-4}.
\]

Esto vale para `b≥1000`; los términos distintos de uno son de orden `b^{-6}`, muy menores que `b^{-4}`. El factor `b^{-6k#A}` se recupera del término de error usando `#A≤f`. No hay una pérdida oculta de un factor absoluto en esta última deducción.

**Comprobación (a), cancelaciones de C0.** En P51:3925–3963, `pbm:const`, tomando `n=ρ+1`, `r=k+2ρ+1`, `v=(2/rd_E)^f`, se verifican las identidades de exponentes

\[
\tfrac12-k-n-2\rho(\rho+k)
=\rho-(2\rho+1)(k+\rho+\tfrac12),
\]

\[
k+n+2\rho(\rho+k)
=1+(2\rho+1)k+\rho(2\rho+1).
\]

Son precisamente los exponentes de `rd_E` y `2`. La identidad de volúmenes compactos utilizada allí se obtiene directamente de `vol U(j)=∏_{a=1}^j 2π^a/(a−1)!`. Aceptadas las masas y el covolumen indicados, queda la desigualdad escalar

\[
\mathsf L\le(1+b^{-9})(1-N^{-k})^f.
\]

Es incorrecto describir el término principal como una igualdad exacta sin corrección: el texto conserva `L` y `(1−N^{-k})^{-f}`, y absorbe su desviación en el margen explícito.

**Hipótesis de tamaño heredada que conviene explicitar.** La última estimación de (C0), P51:3961, usa `f·2^{3−k}≤b^{−10}`. No se deduce de las desigualdades enumeradas en el encabezado de `pbm:const` por sí solas: con `k,n,f` fijos, aumentar `b` preserva sus cotas superiores y hace fallar esa desigualdad. En los datos admisibles sí está disponible la información adicional `k≥x⁵/2` y `x≥(log b)¹⁰⁰`, que la garantiza. Una condición local suficiente es `k≥20 log b+4`, junto con `f≤b/1000`. Esto no refuta la aplicación a los datos del paper, pero la afirmación de suficiencia de una lista aislada de parámetros debe incorporar esa condición o citar explícitamente las cotas heredadas. Las cancelaciones algebraicas verificadas arriba no dependen de esta observación; el cierre numérico de C0 sí.

La razón exacta de masas está en P51:1336–1357, `pb:massratio`. Es compatible con el factor `2^{1-lf}` de Gan–Hanke–Yu para el género unimodular en el caso no ramificado: el factor global 2 cancela en la razón, pero `2^{-f}` no. Véanse las proposiciones 4.4–4.5 de [Gan, Hanke y Yu, *On an exact mass formula of Shimura*](https://web.math.princeton.edu/~jonhanke/Web-02/Mass-Formula-of-Shimura/shimura-mass.pdf). Esta comprobación no sustituye la auditoría de cada identificación de retículos que permite aplicar esa fórmula.

## Poisson, Siegel y las entradas locales

**(a), lema de Poisson unilateral `pbm:poisson`, P51:3661–3684.** En el grupo adélico utilizado, la periodización de una función integrable no negativa tiene coeficientes de Fourier `c_L^{-1} F̂(η)`. Si la suma absoluta de esos coeficientes es infinita la cota es trivial. Si es finita, representa una función continua, igual casi en todas partes a la periodización y acotada por dicha suma. La semicontinuidad inferior en el conjunto finito de puntos permite acercarse a cero por puntos de igualdad casi en todas partes. Esto prueba la desigualdad con el factor `1/c_L` escrito. No exige igualdad puntual de una fórmula de Poisson clásica para una función arbitraria.

**Comprobaciones de normalización de Siegel.** P52:5442–5460 obtiene correctamente los productos de medidas aditivas de covolumen uno:

\[
\operatorname{covol}(\mathcal O_E\subset\mathbb C^f)
=2^{-f}|D_E|^{1/2},\qquad
\operatorname{vol}(\widehat{\mathcal O}_E)=2^f|D_E|^{-1/2}.
\]

También usa `|D_E|=|D_{E^+}|²` cuando `E/E^+` es no ramificada en los lugares finitos. P52:5504–5513 calcula correctamente la densidad arquimediana

\[
\int_{\mathbb C^k}\delta(|x|^2-a)\,dx
=\frac{\pi^k a^{k-1}}{(k-1)!},\quad a>0.
\]

Se deduce derivando el volumen de la bola de radio `√a`; no aparece un factor 2 adicional.

El teorema de Siegel–Weil que el manuscrito invoca está expresado con medida **de masa uno** en el cociente unitario compacto, P52:5426–5440. No sería correcto insertar sin compensación una medida de Tamagawa de masa 2. El original citado es [Weil, *Sur la formule de Siegel dans la théorie des groupes classiques*](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5988-11511_2006_Article_BF02391774.pdf). Esta revisión no certificó toda la traducción de su teorema 5 a la representación de Weil y los caracteres del manuscrito; ese punto permanece (c).

**Límite concreto de la revisión:** aun aceptando esa traducción y las dos medidas anteriores, queda por demostrar el paso de la fórmula de representaciones a `pff:S`, con separación de fibras, pesos y pares de términos. Ese trabajo está en P52:4279–4556. El cálculo de la densidad no demuestra por sí solo la desigualdad de segundo momento. Las cotas de los sistemas reales y finitos dependen de los lemas de descenso, profundidad, frecuencias y suma de capas, P52:708–871 y sus pruebas posteriores; no se han certificado íntegramente.

## El rango del conteo de pares

Una objeción que **no** está justificada por la versión examinada es afirmar que el autor sólo cuenta `l≤n³` y olvida todos los demás corangos. El cierre del rango está escrito en `pbe:rank(c)`, P51:2941–2955:

\[
1\le\mathsf d,\qquad
\mathsf d^2\le(2/M)^{2if}b^{2n^3f},\qquad M/2\ge b^{18}
\ \Longrightarrow\ 18i\le n^3.
\]

Como `l≤i+1`, resulta `l≤n³` en el rango del manuscrito. Esta deducción es **(a) condicionada** a la ganancia (G), al límite de la gauge y a la integridad que da `d≥1`.

El paso de (C1) y (C2) a (C), P51:6632–6659, también es correcto como reducción. Dos términos se envían al mismo par `(t,L_{γγ′})`; el cuadrado de la cota para un término da `b^{4000n^6(l+1)f}`, que es a lo sumo `b^{kf/4}` porque `l+1≤2n³` y `k≥512000n⁹`. La suma ponderada sobre los retículos aplica entonces (C2).

Los puntos todavía abiertos en esta revisión son la demostración de (G) mediante cortes e índices (`pbg:main`, P51:8176), el conteo de marcos de (C1) (`pbc:C1`, P51:8468) y la altura y suma de subretículos de (C2) (`pbc:C2`, P51:8769). La cobertura de pares no próximos y de bloques no concordantes usa además el truncamiento y la anulación de amplitudes; no se ha certificado todo ese argumento. Por tanto no corresponde afirmar que el conteo completo sea correcto, pero tampoco señalar un rango omitido sin refutar antes esas reducciones.

## Multiplicidades y atribución

`pm:main`, P51:4299, es una comparación con:

- un dato de comparación de espacios hermitianos y niveles identificados;
- parámetros de serie discreta con separación al menos `500n³+10n⁵` entre coordenadas de signos distintos;
- grado real `f` par;
- una componente de prueba supercuspidal en un lugar finito descompuesto.

`pm:mult`, P51:4331–4343, se aplica después al idempotente `e_0`; una etiqueta irreducible en un lugar proporciona la componente cuspidal por la propiedad (G) de Green. La igualdad es para las multiplicidades de caracteres de la álgebra de Hecke especificada, en los espacios proyectados, con tipos arquimedianos fijados. La frase sin estas condiciones, «los grupos isométricos en todos los lugares finitos tienen las mismas multiplicidades», es demasiado amplia.

La comparación de clases estables `pm:classes`, P51:4729–4777, explica por qué aparece la paridad: el producto de los signos que se desean cambiar es `(-1)^{f(q−q′)}`. El argumento usa normas globales y el principio local-global hermitiano; no se obtiene de una mera identificación de los puntos adélicos finitos. La suma de integrales orbitales en P51:4819–4836 emplea además `pm:arch(b)`. La prueba completa de ésta se remite a `pbr:main`, P51:5122 y siguientes; no quedó certificada en esta revisión. También quedan pendientes las cotas globales que justifican la traza del núcleo sin truncamiento.

La atribución amplia a Labesse es razonable como antecedente de comparación y estabilidad. **No** se verificó que la proposición exacta de P51 sea una cita literal de un teorema suyo, y el manuscrito no debería presentarla así. [Labesse, *Changement de base CM et séries discrètes*](https://webusers.imj-prg.fr/~michael.harris/CBCM.pdf), introducción y teoremas 5.4–5.5, impone hipótesis de no ramificación en lugares inertes para sus resultados de multiplicidad uno y estabilidad. P51 anuncia, en cambio, una demostración específica por comparación directa y cita también la fórmula simple de Flicker–Kazhdan. No se debe eliminar esas distinciones.

## Uniones comprobadas

| Unión | Resultado de la comparación |
|---|---|
| P51 `pb:thmB` → P46 `au:moment` | Mismos tres límites, mismos factores `5b^{-4}` y `1+9b^{-4}`, y misma normalización de `D_X²/(deg mass_r)`. Comprobado como enunciado. |
| P52 `pfr:R` → P51 `pbm:inputs(R)` | Coinciden masa `(1+b^{-10})/deg_τ`, pesos y decaimiento. La identificación de la forma superior con la forma de Gram, necesaria para Siegel, figura en P52 (R-b) y en P51:3898–3900. |
| Hipótesis reales de P52 → uso en P51 | P52 exige `ρ≥10⁸`, además de otras cotas (H0)–(H5). P51:4033–4038 y P52:958–964 mencionan expresamente esa condición y su satisfacción por los datos. No basta `n≥100`, pero el uso no se limita a esa condición. La verificación completa de (H1)–(H5) queda (c). |
| P52 `pff:F` → P51 `pbm:inputs(F)` | Coinciden masa `(1+b^{-6})b^{-6k#A}`, pesos, exponente y denominador. El sistema depende del grupo intermedio `Z(A,d)`, no sólo de `T`. |
| P52 `pff:S` → P51 `pbm:inputs(S)` | Coinciden los factores `r_*²`, `(1+b^{-6})a_*`, el conjunto de valores distintos de `t` y la condición de usar la misma forma finita de (F). `T` debe contener también los lugares no unitarios de la base; está escrito en ambos. |
| P51 `pm:mult` → P46 `au:mult` | P46 pide además la álgebra esférica completa, no sólo los lugares split. P51:5021–5030, `pm:rem-full`, extiende expresamente la identidad a lugares inertes; por eso no hay discrepancia de alcance en esta versión. |
| Retículo de P51 → retículo de P49/P46 | No son idénticos. P51:1027–1110, `pb:lattice`, ofrece un transporte por una adele de norma uno y conjugación unitaria de las aplicaciones de Poincaré. La invariancia de las normas Hilbert–Schmidt bajo ese transporte sí está comprobada; la identificación íntegra de los datos originales de P49 queda a la auditoría de ese paper. |
| P51 → P53 | La comparación de multiplicidades es una entrada relevante para la cadena. Esta revisión no certificó todas las aplicaciones en P53 ni todas las reproducciones en sus apéndices. Estado (c), sin discrepancia concreta demostrada aquí. |

La reciprocidad de citas 51↔52 no prueba circularidad por sí misma: el texto separa las identidades de coordenadas y medidas, usadas por 52, de la estimación L2 que vuelve a 51. Para certificar ausencia de ciclos hay que seguir las pruebas de esos lemas de base; se comprobó el diseño de dependencias, no toda su expansión transitiva.

## Trabajo necesario para cambiar los dictámenes

Para pasar de (c) a (a) hacen falta tres verificaciones independientes y reproducibles: una de `pbe:ds` y del período estacionario `pbp:main`; otra de los sistemas locales (R), (F), (S), especialmente de la separación de fibras y de todas las estimaciones uniformes; y otra del núcleo de traza y las integrales orbitales de `pbr:main`. Para el conteo, conviene emitir certificados separados de (G), (C1) y (C2) con las desigualdades de parámetros incluidas. Las reducciones ya comprobadas indican qué constantes se deben preservar y evitan repetir objeciones que la versión actual sí trata.
