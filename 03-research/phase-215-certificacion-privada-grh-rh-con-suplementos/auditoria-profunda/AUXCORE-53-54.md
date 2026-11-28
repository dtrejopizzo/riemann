> **V1: registro histórico, revisado en V2.** No aplicar sus objeciones de caracteres ni sus estados de propagación a los manuscritos corregidos sin consultar el [estado V2](../revision-v2/ESTADO.md). La cancelación especializada de caracteres corrige el impacto global atribuido en V1; se están consolidando los demás resultados.

# Auxcore de P53, descenso acotado y altura de P54

Auditoría del texto local `main.tex`; referencias de línea a la copia auditada. No se editaron los papers. Dictámenes: (a) correcto en el alcance indicado; (b) argumento incorrecto como está escrito; (c) paso no verificado. Una deducción condicional correcta no convierte sus premisas pendientes en teoremas certificados.

## Resultado y alcance

- **P54 `ppe:bdd`, 4383–4411: (a)**, con R2/R3 y el lema de media de P53 y la anulación `ppe:zero` como entradas auditadas. El crecimiento de la distribución theta se cancela con vectores isotrópicos cortos. No se usa continuidad de evaluación theta para la sola norma de Hilbert.
- **P54 `psu:arch`, 9217–9253: (a) como deducción de CL, `psu:normL`, `psu:I` y las cotas explícitas**. Se comprobó el multiplicador de altura y la cancelación de las constantes exactas. Este argumento no cita directamente `pc:auxcore`; no debe confundirse con la producción de lifts integrales por la segunda grilla. La certificación de las entradas se remite a COVOLUMEN/THETA y los otros ledgers.
- **P53 `pc:auxcore`, 1616–1631: no queda probado incondicionalmente por esta cadena.** La deducción 9436–9497 es correcta condicionada a sus proposiciones. Las proposiciones de intercambio de cuadrados usadas en los giros dependen de `pcx:X`, cuya demostración contiene el fallo de caracteres de `pcu:product` documentado en ERROR-53-CARACTERES. Es **(b) para la prueba presentada**, no un contraejemplo al enunciado de auxcore. Sigue **(c)** la existencia de una reparación global que preserve los períodos, su no anulación y sus constantes.
- Dos errores adicionales **(b) locales**, en `pgq:slice` y `pgk:lat(c)`, admiten las reparaciones completas siguientes; ambas conservan las constantes. No son nuevas obstrucciones globales.

## 1. Dos errores locales con reparación demostrada

### 1.1 Orden matricial en `pgq:slice`

P53:13740–13742 identifica `rr₀⁻¹` con el producto `(g(r₀⊕1))⁻¹g(r⊕1)`. Este producto es `(r₀⁻¹r)⊕1`. La igualdad escrita no es una regla válida de matrices; no se puede permutar los factores de un grupo unitario indefinido.

Reparación: mantener el minimizador r₀ y escribir

`||r₀⁻¹r|| ≤ ||(g(r₀⊕1))⁻¹|| · ||g(r⊕1)|| = t₀ ||g(r⊕1)|| ≤ ||g(r⊕1)||²`.

La función alcanza su mínimo por la cota de coercividad que abre la prueba; en este grupo unitario la norma de un elemento y la de su inversa coinciden. Por tanto

`∫ ||g(r⊕1)||⁻ˢ dr ≤ ∫ ||r₀⁻¹r||⁻ˢ/² dr = ∫ ||r||⁻ˢ/² dr ≤ 2·16^(n²)Vτ`.

La igualdad de integrales usa Haar **izquierdo**. No cambia el Haar fijado (el grupo es unimodular), ni el exponente mínimo s≥16n². `pgq:balls` requiere s/2≥8n², exactamente satisfecho. El arreglo conserva la dominación que necesita el período profundo.

### 1.2 Determinante finito en `pgk:lat(c)`

P53:14549–14551 afirma que, por preservar la forma unimodular, `det x_f` es una unidad en cada lugar finito. Es falso en un lugar escindido v de F=E⁺: para U(1)(F_v), el elemento `(π,π⁻¹)` cumple la condición unitaria pero ninguno de esos dos componentes tiene valoración cero.

Reparación: de `det x · overline(det x)=1` se deduce que el **módulo finito total** es uno. En lugares no escindidos la valoración es cero; en los dos lugares sobre uno escindido, las valoraciones opuestas tienen iguales normas residuales, y sus módulos se cancelan. Así `x_f Ô_E^n` tiene el mismo volumen adélico que `Ô_E^n`. El argumento de covolumen posterior es válido. El jacobiano arquimediano es `Πτ |det Pτ|⁻² |det xτ|⁻²`; el segundo factor es uno y el primero es la norma absoluta de la unidad `det H`, también uno. Queda exactamente `(2⁻ᶠ |D_E|^(1/2))^n`. No se altera ninguna cota de redondeo o de altura posterior.

## 2. Reconstrucción de `ppe:bdd`

Se cotejaron P54:4364–4411 con P53 R2/R3 (2292–2415) y `pcx:mean` (2519–2577).

1. La media theta sobre el subespacio isotrópico Z es theta₀. `ppe:zero` anula la integral de ese término contra Y, de modo que puede sustituirse theta por theta−theta₀. La forma Y y el dato finito están fijados.
2. R2 da el crecimiento `ht(g)^A` en una norma de momentos; se puede escoger A suficientemente grande, en particular para los umbrales del lema de media. Un vector polinómico de Fock pertenece a todos esos espacios de momentos. La cota no pretende que theta sea una funcional acotada en Hilbert.
3. Para ht(g)>2, R3 proporciona un vector isotrópico racional no nulo d de longitud ≤2/ht(g). Witt permite llevar su línea a Ee por γ racional. La identidad de retículos `Λ_(γg)=γΛ_g` es isométrica, por lo que **ht(γg)=ht(g)**; no aparece una altura incontrolada de γ.
4. Como V es definido, el cociente de U(V) es compacto. Elegido un conjunto compacto de representantes h, existe un entero N que hace integrales simultáneamente todos los `Nh⁻¹d_i` en los lugares finitos. Los vectores `z_i=N d_i〈·,γd〉` pertenecen al retículo requerido y generan Z sobre E; sus longitudes son ≤C/ht(g), uniformemente en h.
5. En `pcx:mean` se toma l=A y δ=C/ht(g). Su factor δ^A cancela exactamente ht(g)^A. Las otras constantes dependen del dato fijo, no de g. La región ht(g)≤2 se cubre directamente por R2. Finalmente se integra la cota sobre el cociente compacto contra Y.

Esto prueba acotación global, que es lo requerido para la aplicación posterior. No se necesita una constante uniforme en todos los rangos/pesos del paper. Si se trabaja con una altura equivalente en vez de la convención ht(h)=1, la compacidad absorbe su máximo y la misma conclusión vale.

## 3. Reconstrucción de la altura `psu:arch`

Se cotejaron 9180–9253 y las entradas declaradas. Para p=(ν,z), se toma la pareja plana q=(υ⁻ᶻ,z) del **mismo rango z** y

`H=I_q(1)/||φ_(p,1)||²`, `h_l=0`.

El producto H||φ_p||²=I_q(1) es integral en todos los lugares por `psu:I(b)`. Así la parte finita de la altura es cero; no hay suma infinita de pérdidas escondida.

Para un conjugado σ, basta el caso σ que fija K: K es cuadrático imaginario y componer con conjugación compleja conserva el valor absoluto. CL aplicado a p y q introduce el mismo factor `a_σ(z)`, porque z coincide; `psu:normL` introduce el mismo B(z). Ambos se cancelan en el cociente. Los grados lτ son permutados, así que permanece exactamente

`Στ (log(lτ!)+lτ log(M/Ω)) = Στ s∞(lτ)`.

El grado plano es cero y su d es uno; el término `−log d_(p^σ)` es no positivo. Los dos logaritmos de Euler contribuyen como máximo 2f. Como M/Ω≥1 y lτ≥κ(τ), se obtiene

`log|σH| ≤ log N_z +8fz log M +2f −Στ s∞(κ(τ)) ≤ budget−Στ s∞(κ(τ))`.

Las dos últimas desigualdades son exactamente (N5), (N6). No se reemplaza el período CM por una estimación, ni se pierde un factor arquimediano por tomar valores absolutos. El alcance es la deducción condicional indicada arriba, no una nueva prueba de CL/Rallis.

## 4. Auxcore: piezas efectivamente reconstruidas

### 4.1 Deducción final, índices y delta

Se reconstruyeron 9057–9707, 9900–10106 y 11540–11795; se leyó además el cierre de diagonal 10640–10715 y el último camino 11998–12065. La transformación combinatoria usa m² giros. Los giros no diagonales tienen factor de cota uno; los diagonales pagan V. La cota final es `L=V^(m²) E^(2m)`.

El nivel principal J° NO se identifica con el nivel parabólico Jθ. El índice del primero es `#GL_(r+mt)(R_m)` y el cociente de índices del segundo contiene las órdenes de bloques y el radical unipotente; no es una simple potencia de norma. La prueba 9390–9497 mantiene esta distinción y cancela el índice correcto en la identidad de período.

Las delta forms se construyen en nivel libre, lo que elimina ambigüedad de estabilizadores; el promedio arquimediano de Schur produce el factor `1/dim λ′`. La identidad obtenida es

`〈v,(cθ/c1)ιθ(rφ)(x_f)〉du = β′ Λ(Ψθ;δ_(x_f,v),φ)`.

Escoger sβ′=h ε N₀, ε∈{0,1}, es válido incluso si β′=0: no se divide por cero. La integralidad se verifica mediante gauges, traslado racional a puntos integrales sobre l, y la dualidad integral con denominador h. Para θ=1 se obtiene

`||σ ι1(srφ)(x_f)||² ≤ Cdu h² exp(2(x^99+x^200)b²) B ≤ exp(2x^201 b²) B`.

La sobreyectividad de r usa primera transposición, no se sigue sólo de la estimación final. Esa transposición tiene una dependencia de intercambio indicada en 4.4.

### 4.2 Denominadores, conjugados y formas cortas

Se reconstruyeron 13048–13575 y 14027–14389. En el último camino todos los nodos son definidos. La invariancia conjunta del dato de camino elimina denominadores de estabilizadores al expandir las sumas de clases. El factor de jets d y el factor de ramificación `M_branch` dan `N₀=M_branch d^(2m)≤exp(x^99 b²)`; las primas de Qθ están explícitamente excluidas. En la cota arquimediana, la normalización de promedios divide por su cardinal, por lo que no se cuenta de nuevo un factor de tamaño de grupo. Las cotas B1/B2/B3 cubren respectivamente jets, ramificación y clases, incluidos los rangos hasta 2n_m de esta segunda grilla.

Para las formas cortas (9900–10106), los exponentes de determinante de cada componente pueden ser negativos. Se aplica la construcción de bases cortas al retículo ya torcido x^(eτ); no se eleva ciegamente una misma cota a un exponente negativo. El cálculo de gauge transforma el determinante en el de una matriz integral. Las evaluaciones en raíces de unidad son Zariski densas y generan la representación; esto justifica «spanned», sin afirmar que constituyan una base integral. La norma de todos los conjugados queda controlada por las cotas de rango y número de cajas prescritas.

### 4.3 No anulación del período profundo

Se reconstruyeron 13583–14026, 14395–14742, 14776–15052 y las estimaciones de coeficientes 15078–15420. El esquema consta de control de cúspide C, reproducción Q y restricción S.

Q usa separación de vecindarios y una cota de la **suma total**, no la afirmación incorrecta de convergencia uniforme de colas para g global hallada en P51. C utiliza redondeo en la red dual de la traza, vectores cortos isotrópicos y los radicales unipotentes escritos. La corrección de covolumen en 1.2 basta aquí. S usa un punto estacionario de la fase, localizado por los pesos intercalados, y una cota gaussiana alrededor suyo; el factor de volumen `Vτ` se conserva. La corrección de slices de 1.1 conserva la cota de la cola.

Con D=b^(x^36), las cotas de separación y variación dan el esquema de contradicción `S_sup≤S_sup/2`; no requiere que se alcance el supremo. Se verificó el uso de tamaños para Π/D≤1/20 y el descenso de los umbrales de exponentes a los de las integrales de bolas. Las entradas de tipos mínimos/discrete series se remiten a las auditorías THETA/MULTIPLICIDADES ya realizadas; no se volvieron a dar por demostradas por el solo nombre de un teorema.

### 4.4 Dónde persiste la dependencia global

Se reconstruyeron 12604–13012: las transposiciones I/P usan una segunda grilla de rangos pares y verifican los signos de caracteres, el rango convergente y la suma de errores para la inyectividad. Sin embargo, su T1 usa explícitamente `pcx:X`. Lo mismo ocurre con la ley del cuadrado que entra en los giros de 4.1.

El fallo de caracteres en P53:3359–3360 no se resuelve porque los caracteres tengan módulo uno: la variable correspondiente se integra. La reparación puede cambiar el período y su no anulación. Por ello no es legítimo concluir que auxcore está certificado incondicionalmente sólo porque sus cotas y su deducción final estén bien.

## 5. Continuación: inversión de línea, giro diagonal y G1–G4

Se completó la lectura y reconstrucción de 10330–10639, 10728–11466 y 12065–12603. El pendiente de lectura registrado al inicio de esta tanda queda sustituido por los siguientes resultados; no se modifica la obstrucción global de exchange.

**Inversión de línea:** el caso general `pgx:line` usa datos soportados en `A=a_w O_w^n`, no en las matrices integrales sin escalar. La imagen de Fourier del vacío está en `B′=bar(α)_w O_w^n`; el elemento diagonal fijado tiene componente `u_w=bar(α)_w/(α_w π^k)`, de modo que `u_w A′=π^(-k) B′`. El coeficiente de Fourier del indicador de un coset es `γ q^(-kn)`; tras la dilatación unitaria, su módulo se determina por normas: el indicador de entrada tiene norma al cuadrado q^(-kn), mientras que la suma de los q^(kn) indicadores de salida, con coeficientes de módulo uno y soportes disjuntos, tiene norma al cuadrado uno. Por tanto el módulo local es exactamente q^(-kn/2), también cuando α no es unidad. Al ensamblar se obtiene `|c_line|²=C₀(Nm m)^(-n)` con C₀ independiente del twist. El factor de carácter que aparece al mover u es `β_(L′)(u)^(-1)`; aquí u es un punto fijo, y absorber su valor de módulo uno sí es legítimo. A diferencia del fallo de `pcu:product`, no es un carácter de una variable que todavía se integra.

**Seesaw y giro:** la funcional doble en `pgu:seesaw` es continua en una norma de momentos, gracias a R2 y al decaimiento rápido de ambas formas; Fubini tiene dominación. El conjunto de vectores cuya imagen pertenece a la línea CΞ es cerrado para esa topología (también cuando Ξ=0). La densidad de polinomios se aplica en momentos, no sólo en Hilbert. Los datos girados son la transformada finita en la columna de la línea seguida del matching: la invariancia se obtiene por el cambio v→g_S v, y los factores de determinante se cancelan utilizando que las aristas opuestas tienen el mismo carácter. La condición de inversa izquierda se hereda del bloque x₂; añadir la fila v′ no la destruye. La suma tiene como máximo `(#R)^n≤(#R)^(2n_m)=V` términos. La descomposición en bloques `(S,y,v)` y `(S,x,v′)` es biyectiva, por lo que no falta una fibra multiplicativa. El cierre da `c_jj=c⁰_jj/c′_line`, preservando el módulo requerido hasta potencias de norma.

**G1/G2/G4:** las fórmulas de rango y signos se verifican contando las coordenadas de tallo negativas. En particular N¹_(j,j+1)=N⁰_(j+1,j)=r+(2j+1)t y sus signos negativos coinciden. Sólo se identifican espacios/grupos/retículos; los tipos distintos no se identifican. G2 usa los redondeos floor/ceiling de rangos de paridad diferente y produce exactamente β^c=1, α^r=υ. G4 usa u=bar(u₀)/u₀ y coincide con el elemento del cálculo local general anterior.

**G3 y cuadrados:** se verificó la extensión del matching de exceso t a t±1: las clases de medios enteros, la cadena del bloque nuevo, el cambio de signo del tallo y la distancia de al menos Δ/2−1/2. Los signos distintos se separan por al menos Δ−t; los rangos son ≤2n_m. Las aplicaciones a armónicos, proyecciones y tipos se apoyan en las entradas de P49 ya auditadas; no requieren mantener t impar en el exceso local. En E2 los productos de caracteres de aristas valen `ν⁻¹υ^M₀`: en la primera grilla floor+ceiling=M₀, en la segunda ambos rangos son pares y sus mitades suman M₀. Las cuatro orientaciones de E1 se verifican con la conjugación explícita de tipos para las aristas ascendentes. Pasar de una forma y₂ a una funcional arbitraria l es válido porque las imágenes de datos puntuales caen en un espacio de nivel fijo y dimensión finita, con producto de Petersson positivo definido.

**Dictamen de esta continuación: (a) para las deducciones locales con las entradas declaradas.** No se encontró otro fallo en estos bloques. La ley del cuadrado sigue dependiendo de `ptr:square`/`pcx:X`; el cálculo correcto de E2 no repara la identidad incorrecta que se usa dentro de su demostración. La siguiente obligación global continúa siendo reconstruir ese intercambio con sus caracteres y verificar de nuevo los períodos resultantes, no una lectura pendiente de estos tres bloques.
