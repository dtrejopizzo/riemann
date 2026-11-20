# LINK_011 — Mapa Mellin–Gauss explícito desde los tests continuos

2026-10-19. Constructor único. **PROVED, revisión favorable en AUDIT_011.md:** el mapa concreto definido abajo converge en 𝓗_α, su FE exhibe exactamente el momento polar del portador par, pero su forma es suavizante y **no coincide con Q_T**. No se excluyen otros mapas ni una dominación con resto positivo. Objetivo D activo.

## 0. Corpus check y razón de este cálculo

Leídos las reglas del proyecto, índice ROUTES-TRIED-INDEX (familias, residuos06, entradas209), grid maestro, crucigrama, CONSTRUCTOR005–008 y LINK009–010 con auditorías. Búsquedas dirigidas: theta y tests, mapas gaussianos, sampling/mollifier, co-Poisson, Hamburger y momentos cosh. Referencias pertinentes: SPEC005, R11_2_ORIGIN, Z_CARRIER, P1_BBSTAR y controles de compresión.

No se reintenta una interpolación continua de D_n ni una raíz abstracta de Q_T. Tampoco se usa sólo evaluación F(log d). **Razón nueva:** se fija el operador de análisis Mellin del factor Π del kernel −R ya construido, se aplica a tests continuos, se prueba su dominio y se calcula su FE y el fallo de igualdad con los tres términos de Q_T. Esto responde una pregunta de enlace concreta; no pretende eludir por nombres las clases indexadas.

## 1. Objetos y candidato sin parámetros ajustados a Q_T

Fijar T>0, 0<α<1/2 y s=2α. Usar 𝓗_α y S_α=−R_α de CONSTRUCTOR005–007. El representante Haarcentrado de cada divisor es

`f_d=X_d−1/d`, d≥2,

con `⟨f_d,f_e⟩_(𝓗_α)=S_α(d,e)`.

Sea `W_d(y)=τ(d²y)−τ(y)/d`. Para F∈L²([−T,T]) defino

`a_d(F)=∫_(exp(−2T))^(exp(2T)) y^(α−1) F((log y)/2)W_d(y)dy`

`       =2∫_(−T)^T e^(2αx)F(x)W_d(exp(2x))dx`,

`U_(T,α)F=Σ_(d≥2) a_d(F) f_d`.                    (1)

Este es el análisis de los perfiles de Π con la misma medida Mellin: en el factor gaussiano el perfil f_d es `q_d−1/d`, y `τ(q_d−1/d)=W_d`. La definición usa τ y el kernel S, no Q_T ni un minimizador.

En α=1/4, que es el candidato al enlace crítico, el peso del integral en x es e^(x/2).

## 2. Dominio y convergencia de la serie

**Lema 1 (PROVED).** Para todo d≥2 y 0<α<1/2,

`S_α(d,d)≤C_α d^(−s)`

con C_α finito independiente de d.

**Prueba.** Por CONSTRUCTOR005,

`S_α(d,d)=(−Z_α)[d^(−s)−2d^(−s−1)+d^(−2)]+Π_α(d,d)`.

La expresión entre corchetes es ≤2d^(−s). Las comparaciones de sumas gaussianas con integrales dan `τ(y)≤c(y)` y `τ(d²y)≥c(y)/d−1`. Junto a `q_d≤1/d`, obtenida de la concavidad puncturada,

`0≤1/d−q_d(y)≤min(1/d,√y)`.

Para la segunda cota, si c/d−1≥0 se divide ese límite inferior por τ≤c; si es negativo, basta q_d≥0. Por ello

`Π_α(d,d)≤∫_0^∞ y^(α−3/2)min(d^(−2),y)dy`

`=[1/(α+1/2)+1/(1/2−α)]d^(−2α−1)`.

Ambas integrales se separan en y=d^(−2). Esto prueba el lema. ∎

**Lema 2 (PROVED).** Para y∈[exp(−2T),exp(2T)] y cualquier entero j≥0,

`|∂_x^j W_d(exp(2x))|≤C_(T,j)/d`, `|x|≤T`.

**Prueba.** El sumando −τ(exp(2x))/d tiene esa cota en todo compacto. El otro sumando y sus derivadas son sumas gaussianas de factores polinomiales en d²n²exp(2x), y decaen exponencialmente en d² de modo uniforme en el compacto. La cota exponencial implica la cota C/d para d≥2. ∎

En particular `|a_d(F)|≤C_(T,α)||F||₂/d`. Por el Lema 1,

`Σ_d |a_d(F)|·||f_d|| ≤ C_(T,α)||F||₂ Σ_d d^(−1−s/2)<∞`.

Así (1) converge absolutamente en la norma de 𝓗_α y define un operador lineal acotado desde **todo** L²([−T,T]). No se supone pertenencia de una serie infinita formal al dominio.

## 3. Kernel continuo resultante: fórmula efectiva

Defino el vector de análisis

`b_(T,α)(x)=2e^(2αx)Σ_(d≥2)W_d(exp(2x)) f_d`, `|x|≤T`.

Los Lemas1–2 muestran convergencia uniforme en norma de Hilbert, también después de cada número finito de derivadas. Por tanto b es C∞ y

`U_(T,α)F=∫_(−T)^T F(x)b_(T,α)(x)dx`.

La forma positiva inducida es

`𝔈_(T,α)(F)=||U_(T,α)F||²`

`=∫∫ F(x)conjugate(F(x′)) L_(T,α)(x,x′)dx dx′`,

`L_(T,α)(x,x′)=4e^(2α(x+x′))`

` ·Σ_(d,e≥2)W_d(exp(2x))W_e(exp(2x′))S_α(d,e)`.

La suma tiene el sentido del producto interno de b(x),b(x′); la cota `|S(d,e)|≤sqrt(S(d,d)S(e,e))` también prueba su convergencia absoluta y la de todas las derivadas. **L es C∞ en el cuadrado compacto.** U es Hilbert–Schmidt, en particular compacto.

Éste es un kernel efectivo explícito en las coordenadas continuas x. No se declara automáticamente fuera de toda clase multiplicadora después de Fourier o restricciones; para decidir el enlace no hace falta esa clasificación, porque puede compararse directamente con Q_T.

## 4. FE y momento polar: identidad exacta del mapa crítico

Fijar α=1/4 y F par. La inversión x↦−x y la fórmula exacta de CONSTRUCTOR006 dan

`W_d(exp(−2x))`

`=e^x/d[τ(exp(2x)/d²)−τ(exp(2x))]−(1−1/d)`.

Sustituirla en a_d y usar paridad:

`a_d(F)= (2/d)∫_(−T)^T F(x)e^(x/2)`

`                   ·[τ(exp(2x)/d²)−τ(exp(2x))]dx`

`         −2(1−1/d)∫_(−T)^T F(x)cosh(x/2)dx`.       (2)

No hay un resto de fase estacionaria ni un término descartado. La igualdad es válida para todo F par en L² del intervalo.

En el portador polar libre, `∫F cosh(x/2)=0`, la última línea se anula exactamente. Así **el momento polar de este mapa sí coincide con la restricción lineal declarada**. Esto no identifica la contribución cuadrática completa de ese momento con el polo de Q_T: al calcular ||UF||² aparecen también productos cruzados entre los dos términos de (2). No se han probado los coeficientes del bloque polar del paper a partir de esa expansión.

La deducción de (2) usa F(−x)=F(x). Para F no par, el cambio de variable conserva F(−x) en los términos transformados; no se usa (2) sin esa reflexión ni se extrapola al sector impar.

**Límite de la expansión polar.** (2) es una identidad de cada coeficiente antes de sumar en d. Si C(F)≠0, no se suman por separado sus dos líneas como vectores de 𝓗: la serie formal `Σ_(d≥2)(1−1/d)f_d` diverge. En efecto, la componente positiva de rango uno de S da como cota inferior de la norma de sus sumas parciales `(-Z_α)|Σ_(d≤N)(1−1/d)(d^(−s)−d^(−1))|²`, que diverge para s<1. La cancelación entre ambas líneas debe efectuarse antes de tomar la serie. Para C(F)=0, el coeficiente backward es igual al a_d=O(1/d) ya controlado. Por tanto el cálculo no construye un vector polar separado ni una identidad del bloque polar cuadrático.

## 5. Cotejo de gamma y peine: el mapa no da igualdad con Q_T

En el portador polar libre par del Paper47, la forma buscada es la forma archimedeana menos el peine:

`Q_T(F)= (1/(2π))∫ m(t)|F̂(t)|²dt`

`         −Σ_(n<exp(2T)) (2Λ(n)/√n) c_F(log n)`.

Aquí `m(t)=Re ψ(1/4+it/2)−logπ~log|t|−log(2π)` por la asíntota de la digamma; la representación exacta y el dominio están en Paper47 eq:Aform y thm:A. Sólo se cita esa definición, no una afirmación nueva sobre su signo.

El peine en una ventana fija es un operador acotado: su forma en valor absoluto es ≤`(Σv_n)||F||²`. El término gamma tiene crecimiento logarítmico de frecuencia y es no acotado sobre la bola L² de tests suaves del portador polar libre. En contraste, 𝔈_(T,1/4) es una forma acotada y suavizante de kernel C∞.

### Test explícito de alta frecuencia conservando el polar

Escoger φ∈C_c∞((−T,T)) par no nula, y χ también par en ese espacio con `C(χ):=∫χcosh(x/2)≠0`. Poner

`g_λ(x)=φ(x)cos(λx)`,

`F_λ=g_λ−[C(g_λ)/C(χ)]χ`,

y normalizar F_λ a norma L²=1. Entonces C(F_λ)=0. Integración por partes da C(g_λ)=O_M(λ^(−M)) para todo M, y F_λ converge débilmente a0.

La transformada de g_λ son dos traslaciones de φ̂ a frecuencias ±λ. La asíntota del símbolo gamma y el decaimiento rápido de φ̂ dan

`gamma(F_λ)=logλ+O(1)`.

La corrección con χ no altera el término principal, por su coeficiente superpolinomialmente pequeño. La contribución del peine permanece uniformemente acotada. Por tanto

`Q_T(F_λ)→+∞`,

mientras compacidad de U implica

`𝔈_(T,1/4)(F_λ)→0`.

**Conclusión de clase exacta:** para el mapa (1), la identidad `Q_T=||U_(T,1/4)·||²` es falsa. No es una exclusión de todo mapa de tests a 𝓗, ni se usa LINK009 o010 como si lo demostraran.

### Peine comparado como kernel

El kernel L de §3 es suave. No produce por sí solo los átomos de traslación `x−x′=±log n` del peine. Tampoco produce el operador gamma de orden logarítmico, cuya energía de Lévy tiene kernel K(u)~1/u cerca del origen. Este hecho concuerda con el test anterior; no se intenta compensar esos términos llamándolos un resto positivo sin demostrarlo.

## 6. Resto exacto y pregunta no resuelta

Para este candidato el resto está perfectamente definido:

`𝔅_T(F)=Q_T(F)−𝔈_(T,1/4)(F)`.

No se ha demostrado `𝔅_T≥0`. La divergencia positiva en alta frecuencia sólo localiza allí un comportamiento favorable; **no decide su signo en las direcciones bajas ni sus acoplamientos**, que son la dificultad original.

Como identidad distribucional de formas, 𝔅 conserva el gamma singular y todos los átomos del peine, más el kernel suave −L. Esto indica exactamente por qué la FE polar de (2), aunque correcta, no completa el enlace. El mapa alisa los términos cuya cancelación se necesitaba conservar.

No se declara NO-GO para una dominación `Q_T≥𝔈`, para mapas no suavizantes, para compresiones irregulares de D_n ni para O1. Esos enunciados requieren otras construcciones y pruebas.

## 7. Resultado de la tentativa

Se calculó un único mapa desde los tests continuos al kernel positivo −R, con dominio y serie controlados y sin elegir coeficientes a partir de Q_T. Su FE muestra exactamente el momento cosh del portador par. Su forma efectiva es suave y falla como identidad del nodo por el cotejo explícito de gamma y peine.

**Resultado:** candidato (1) calculado, igualdad con Q_T refutada para ese candidato; dominación con resto positivo OPEN. No se modificó Paper47 ni se cerró el objetivo D.
