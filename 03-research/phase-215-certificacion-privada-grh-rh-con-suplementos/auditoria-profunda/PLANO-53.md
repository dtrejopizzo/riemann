> **V1: registro histórico, revisado en V2.** No aplicar sus objeciones de caracteres ni sus estados de propagación a los manuscritos corregidos sin consultar el [estado V2](../revision-v2/ESTADO.md). La cancelación especializada de caracteres corrige el impacto global atribuido en V1; se están consolidando los demás resultados.

# P53: término constante, constancia y no anulación

Auditoría directa de `main.tex`, líneas 4610–5465 y 5544–6368, 28-11-2026. Se reconstruyeron las operaciones de esas pruebas. Dependencias explícitas: modelo de Weil W1–W5 de49, convergencia y normas de momentos, modelo mixto corregido sobre Schwartz según COVOLUMEN. No se certifica exchange por ensamblaje; el error `pcu:product` permanece.

| Obligación | Dictamen | Alcance |
|---|---|---|
| `pct:plane`, 4850; prueba 4897–5195 | **(a), bajo los inputs del modelo y convergencia indicados** | Se reconstruyen término cero, unfolding, factores locales, Mellin y los dos rangos. No usa `pcu:product`. |
| `pct:SA`, 5240–5300; `pcx:const`, 5302–5330 | **(a) bajo `pct:plane`** | La fuerte aproximación elimina radicales; la condición toral adicional elimina la obstrucción del determinante. No se invoca fuerte aproximación irrestricta para U(Y). |
| `pct:coneimage`, 5395–5438; `P-plane`, 5441–5465 | **(a), con el modelo mixto en normas de momentos** | La sección se elige simultáneamente para todos los caracteres de peso μ; B(x)>0; no requiere dividir por una integral oscilante. |
| `pct:vandesc`, 5551–5575 | **(a) bajo el término constante** | Se verifican el rango d≥−k, k≤μ y la no anulación de L(d+1). |
| `pcn:negcoeff`, 5719; prueba hasta 6352 | **(a) para el argumento reconstruido con las leyes locales indicadas** | No depende de unfolding global ni de product. Desciende una distribución al espacio de la órbita, luego a un funcional del estabilizador que se anula. |
| `pct:vantop` → `P-nonvan`, 5607–5652 | **(b) la prueba escrita** | Primera utilización defectuosa en esta prueba: 5632–5634, «by Lemma pcu:product». El período tiene el carácter residual ya identificado en ERROR-53-CARACTERES. No se prueba aquí que el enunciado sea falso. |

## 1. Reconstrucción de `pct:plane`

**Levi y rango.** Con d=r−N/2, el módulo del radical de V′ aporta |a|^(r+1). Las dos sucesiones de zero terms aportan respectivamente |au|^(−N/2) y |au|^(−N/2−1), además de |u|^(r+1) y ν̃(au). Es indispensable la hipótesis u=1 o r=N: sólo entonces χ_(r+2) y χ_r en u se identifican con ν̃⁻¹ con los exponentes impresos. Se mantiene esa restricción en const, plane y descenso; no se aplica la fórmula para u arbitrario en rango desigual.

**Términos de la expansión.** La media sobre el centro de N_A elimina Q(y)≠0. El término y=0 se anula localmente en cualquier w∈S: el zero term exige xe_A=0, pero la matriz formada por z·pr y x sería invertible y tendría columna e_A nula. Aquí S≠∅ está declarado en4618; no es el caso vacío defectuoso de `pcx:decay`. Para ξe_X≠0, el radical restante promedia las traslaciones de Hom(W,Ee_X); W2 identifica exactamente L_t(ξ). Las líneas isotrópicas constituyen P_X(E)\U(V′)(E), por Witt, y la integral parabólica da el exponente d+1. La prueba no necesita integrar la suma de valores absolutos de todos los y para todo h antes del regrouping: se usa la identidad puntual y luego la integrabilidad absoluta de Φ_x′ en el cociente parabólico.

**Factor local.** Fuera de S, la primitivad de la línea de lattice y su dual produce el indicador de α integral. En S, después del cambio unimodular de frames, la matriz tiene bloques

`[z 0 0; y 0 p; q α_w s; 0 0 t]`.

Su determinante es ±α_w t det[z;y]. Las variables p,q,s tienen volumen1; α_w,t deben ser unidades. La integral en t es una suma de Gauss de módulo q_w^(−1/2) y soporte v_w(overline(α_barw))=−1. Esto da λ_varpi para ambas orientaciones de la línea, no una potencia adicional de q dependiente de r. Los caracteres de los cambios de frame tienen módulo1. K′_f fija el dato porque χ(det k) del cambio de matriz cancela γ_W′(det k)=χ(det k)⁻¹.

**Mellin y extremos.** Para x>1, Tonelli y los factores locales dan el Euler product L^S(x,ν) y la integral arquimediana cone_x. La convergencia arquimediana usa x>0 cerca de0 y una norma de momento suficientemente alta en infinito. Poisson proporciona

`|a| Σξ≠0 Λ_t(ξa)=Σξ≠0 Λ_f(ξ bar(a)⁻¹)`.

Los términos ξ=0 son cero en ambas polarizaciones. El cambio a↦bar(a)⁻¹ conserva ν̃ y cambia |a| en |a|⁻¹, por lo que da la cota para el valor absoluto de la SUMA del lado t en exponentes1−x. Esto basta para el integrando de Z; no se afirma que Poisson preserve la suma de valores absolutos. Interpolar entre R y1−R produce convergencia para todo exponente real y analiticidad, con dominación de las derivadas logarítmicas. El caso x=1 se obtiene por continuidad; no se usa convergencia absoluta del Euler product allí.

Con K₀=c⁻¹α₀, |c⁻¹|=Q y |g_S|=Q^(−1/2), el factor es ε_β |α₀|^x Q^(x−1/2)L^S(x,ν), con |ε_β| independiente deν. Así no falta el Q^(−1/2). El factor |α₀|^x se absorbe en C únicamente después de fijar los espacios y, por tanto, x=d+1 o−d. Se usa d entero: d<0 implica−d≥1.

## 2. Constancia y adición de plano

En `pct:SA`, la aproximación fuerte usada es la del grupo aditivo, no la del toro U(1). Aproximar c y la coordenada skew de β fuera de un conjunto finito no vacío proporciona invariancia izquierda por N y N⁻, usando invariancia racional e invariancia derecha en S. La fórmula explícita de tres unipotentes de `pct:qref` da Levi m(λ,ρ), donde ρ es una quasi-reflexión de Y₀. Se verificó λ=(j barσ)⁻¹ y j barλ=−σ⁻¹. Al cortar componentes a un conjunto finito R se conserva la identidad; la generación por quasi-reflexiones permite todos los elementos racionales de U(Y₀). La condición(iv) permite sustituir λ por cualquier parámetro toral t. Luego aproximación débil por Cayley y la invariancia por compactos fuera deS eliminan las componentes finitas; aproximación débil en infinito concluye. Así la obstrucción del determinante no se ha descartado gratuitamente.

En `pcx:const`, la invariancia derecha por el grupo completo en S se deduce de `linfactor`: en b=0 las dos secciones son ξ(det x)⁻¹. La acción Sact(b) tiene η(det g)^0=1. La condición(iv) procede de `pct:plane` en r=N. Esto no usa `P-plane`, `P-equal` ni `P-nonvan` y por tanto no hay ciclo en esta subcadena.

La construcción `coneimage` usa una sección suave local de la órbita isotrópica, extendida por exp(φX) dentro de una carta del grupo. El modelo mixto produce slices prescritas en esa carta. La equivariancia del zero term cancela ν̃_∞(a), quedando β(κ⁻¹ae_X)|a|^(N/2)≥0. La integral B(x) es positiva porque el integrando vale1 en(1,1), y su soporte tiene |a_τ| en[2^(−1/2),2^(1/2)]; es analítica para todo x real. El vector resultante sólo depende de μ, no del twist finito. Al añadir el plano se usa const para reemplazar F(1) por su término constante y se cancela exactamente L^sharp(d+1)² contra L_*(d+1)/L_*(d). Esta construcción exige la reparación topológica sobre momentos registrada en COVOLUMEN; no vuelve correcta la frase falsa «evaluación Hilbert-acotada».

## 3. `negcoeff`: reconstrucción de la anulación local

Las hipótesis H1–H3 se cumplen en la aplicación: q′=b+q₀, p₀≥1 y N_τ=μ_τ+p₀−n/2=μ_τ+k≥1. El carácter del slice es γ_Xυ⁻ᵇ=γ_W₀; no γ_X sin corregir. La ley compacta da peso de vacío μ^flat−p₀ en una fila negativa. Por tanto una rotación de una línea negativa con eigenvalor barη multiplica el vacío por η^(N_τ).

Si el índice invertible β no es negativo definido, tiene una dirección positiva. Witt mueve esa dirección a una fila positiva estándar. Para cada valor z de las variables Fock hay una línea negativa perpendicular a las b columnas del frame y a las q₀ columnas negativas de z: en las b+q₀ filas negativas las primeras b condiciones tienen una dependencia, porque el frame contiene una fila positiva. La rotación de esa línea fija el frame. Sobre el hiperplano impuesto a z, la invariancia de un polinomio P da η^(N_τ)P(z+(η−1)z′)=P(z). Evaluar la identidad polinómica enη=0 prueba P(z)=0. No se toma η=0 como elemento del grupo; se usa continuación de una identidad polinómica válida en el círculo. Promediar por el estabilizador compacto y la densidad de polinomios en Schwartz elimina todo funcional invariante continuo.

Para pasar de un funcional del modelo grande a la fibra, el carácter central obliga primero a matar cada coordenada de Q(x)−β. Como β es invertible, dQ es sobreyectiva: ξ=(1/2)xβ⁻¹η produce dQ(ξ)=η. Hadamard demuestra entonces que se matan TODAS las funciones que se anulan sobre Q⁻¹(β), no sólo que el soporte de la distribución está allí; eso excluye derivadas normales. El espacio de la fibra es una órbita homogénea con estabilizador unitario unimodular. La aplicación

`F ↦ (gx₁ ↦ ∫_S ω^flat(gs)F(gs) ds)`

es sobreyectiva por una función compacta con promedio positivo. La invariancia izquierda convierte la distribución levantada en Haar tensor ε; la invariancia derecha torcida fuerza ε∘ω^flat(s)=ε. La anulación compacta anterior da ε=0. Se controla continuidad con seminormas Schwartz, no con evaluación acotada en Hilbert.

Finalmente el coeficiente global define ese funcional continuo: la cota de decay es uniforme sobre el compacto del centro y las normas de momentos dominan la integral. Tras absorber p_∞ en el vector, trasladar el centro da el carácter ψ_β con signo positivo, y trasladar h da invariancia U(T_τ). Por ello `negcoeff` se demuestra sin U1 ni integrabilidad de un término en el cociente del estabilizador. No usa `pcu:product`.

## 4. No anulación y dependencia que no se elimina

`vandesc` extiende analíticamente Z(x)=εP(x)L(x,ν̃)B(x)I. Si d≥−k y k≤μ, entonces j=d+1>−k y j+μ_τ>0; las funciones gamma del funcional equation son finitas y no nulas. L(j)≠0 sigue de no anulación en1−j≥1 cuando j≤0. El descenso de2k+1 planos llega exactamente a(J,0), donde el kernel es1.

Pero para iniciar ese descenso se necesita `vantop`. Su caso de índices no negativos usa el `negcoeff` correcto; su caso de índice J_U aplica explícitamente `pcu:product` al integral en l, líneas5632–5634. La fórmula correcta introduce β(det l), por lo que la hipótesis de anulación del período sin ese factor no basta. El problema reaparece incluso en esta prueba cuyo período supuesto es cero: multiplicar el integrando por un carácter variable no preserva integral cero. **No queda cerrada `P-nonvan`.** Reparación pendiente concreta: identificar y controlar ese período torcido, o suministrar una prueba alternativa de no anulación; no basta haber cerrado plane/const/negcoeff.
