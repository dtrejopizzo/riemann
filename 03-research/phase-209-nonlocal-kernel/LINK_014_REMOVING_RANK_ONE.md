# LINK_014 — Quitar el rango uno no repara el mapa011

2026-10-19. Constructor. **PROVED, revisión favorable en AUDIT_014.md y su addendum**, con el mismo input CITED de Paper47 utilizado y verificado en LINK013. Sin nuevos cálculos numéricos.

**Resultado:** la energía gaussiana Π, por sí sola, sigue siendo demasiado grande sobre la familia explícita F_T de Paper47 para admitir una dominación `Q_T≥c·Π(a(F))` con c>0 independiente de T. Por tanto tampoco funciona quitar únicamente el término κvv* del kernel −R y conservar la misma aplicación de coeficientes a_d(F).

No se infiere este resultado del NO-GO de la norma completa en LINK013: se calcula de nuevo la componente Π sobre los mismos tests y se prueba que no se anula. D y otros mapas siguen abiertos.

## 0. Corpus y diferencia escrita

Consultados las reglas del proyecto, índice ROUTES-TRIED-INDEX (LINK011–013, rango uno, subkernels y familia del margen), grid y crucigrama, CONSTRUCTOR005 y LINK013. No se vuelve al test T=4/5 ni se usa el tamaño de un ínfimo como prueba de respuesta de un mapa.

**Diferencia exacta respecto de013:** su cota inferior usó κvv*. Quitar ese sumando cambia la forma y el argumento de013 deja de aplicar. Aquí se conserva el mapa explícito011 y se estudia el sumando gaussiano Π restante. El paso nuevo es un kernel positivo L¹ y el límite local de la misma familia de tests, que dan una cota inferior de orden T para Π.

## 1. Formas que se comparan, sin proyección implícita

Fijar α=1/4, s=1/2 y κ=−Z_(1/4)>0. Recordar

`S=−R=κG_s+κvv*+Π`, `v(d)=d^(−1/2)−d^(−1)`.

Los coeficientes son exactamente los de LINK011:

`a_d(F)=2∫F(x)e^(x/2)W_d(exp(2x))dx`,

`W_d(u)=τ(d²u)−τ(u)/d`, `q_d(y)=τ(d²y)/τ(y)`.

Defino las dos energías reducidas

`E_Π(F)=Σ conjugate(a_d(F))a_e(F)Π(d,e)`,

`E_red(F)=Σ conjugate(a_d(F))a_e(F)[S(d,e)−κv(d)v(e)]`.

Ambas son PSD y `E_red≥E_Π`. Se quita un sumando del **kernel**; no se supone que ello sea una proyección ortogonal por un vector definido en la completación de S. Los coeficientes y su normalización no cambian.

La convergencia se hereda de la serie absolutamente convergente de LINK011, pues `Π≤S` y `S−κvv*≤S` como formas.

## 2. Kernel positivo de la componente gaussiana

Para y>0 fijo, poner

`f_d(y)=q_d(y)−1/d<0`,

`K_y(x)=2e^(x/2)Σ_(d≥2)W_d(exp(2x))f_d(y)`.

Cada sumando es positivo: W_d<0 y f_d(y)<0 por la concavidad puncturada ya probada. En compactos de x la suma converge uniformemente, por W_d=O(1/d) y |f_d(y)|≤1/d.

**Lema 1 (PROVED).** K_y es no negativo e integrable en toda R, con

`∫_R K_y(x)dx=C(y)`

`=κΣ_(d≥2)v(d)[1/d−q_d(y)]`,                       (1)

`0<C(y)≤κ[ζ(3/2)−ζ(2)]<∞`.

**Prueba.** Cambiar u=exp(2x) y usar `W_d(u)=m(u)/d−m(d²u)` junto a la Mellin de m:

`∫_R 2e^(x/2)W_d(exp(2x))dx`

`=∫_0^∞u^(−3/4)W_d(u)du=κ/d−κd^(−1/2)=−κv(d)`.

El integral converge absolutamente porque W_d mantiene signo y las dos Mellin positivas de m son finitas. Tonelli se aplica a los productos positivos con f_d(y) y da (1). La suma es ≤κΣv(d)/d, que es el valor indicado. Es estrictamente positiva porque cada diferencia 1/d−q_d(y) lo es. ∎

Para un test F acotado de soporte compacto, intercambio de suma e integral —dominado por ||F||∞K_y— da

`B_F(y):=Σ_(d≥2)a_d(F)f_d(y)=∫_R F(x)K_y(x)dx`.     (2)

Esta función representa la componente gaussiana del vector U_TF y

`E_Π(F)=∫_0^∞y^(−3/4)τ(y)|B_F(y)|²dy`.              (3)

Para enlazar las identidades puntuales y las de Hilbert, pueden tomarse sumas parciales: convergen en el factor gaussiano por LINK011 y puntualmente por (2); ambos límites coinciden casi en todas partes.

## 3. La misma familia F_T y su límite local calculado

Usar exactamente la familia de LINK013/Paper47 para T≥1 (en particular k≥8):

`k=ceil(21T/e)`, `a=21/e`,

`G_T(x)=ω_k(x/T)`, `ω̂_k(u)=sinc(u/k)^k`,

`F_T=G_T''''+(γ₁²−1/4)G_T''−(γ₁²/4)G_T`.

F_T es par, está en el portador polar libre y tiene soporte [−T,T].

**Lema 2 (PROVED).** Para cada x fijo,

`G_T(x)/√T→g₀:=sqrt(3a/(2π))>0`,

mientras `sup_x|G_T(x)|/√T` permanece acotado. Además

`||G_T''||∞=O(T^(−1/2))`, `||G_T''''||∞=O(T^(−3/2))`. (4)

**Prueba del límite local.** Inversión de Fourier, v=u/k y z=√k v dan

`G_T(x)/√T=√(k/T)/(2π)`

` ·∫_R exp(i√k zx/T) sinc(z/√k)^k dz`.

Para z fijo, el integrando tiende a exp(−z²/6), y su fase tiende a1 porque √k/T→0. En |z|≤√k se domina el valor absoluto por exp(−z²/7), usando la cota elemental del seno de LINK013. El integral fuera de ese tramo tiende a0: para 1≤|v|≤2 se usa |sinc v|≤sin1<1, y para |v|≥2 se usa |sinc v|≤1/|v|. Por tanto el límite es

`√a/(2π)∫exp(−z²/6)dz=sqrt(3a/(2π))`.

La misma estimación absoluta da la cota uniforme del supremo. Para derivadas,

`||G_T^(j)||∞≤(T^(−j)k^(j+1)/(2π))∫|v|^j|sinc v|^k dv`

`=O_j(T^(−j)k^((j+1)/2))=O_j(T^((1−j)/2))`.

Los tramos se acotan igual; tomar j=2,4 prueba (4). ∎

En consecuencia, para cada x fijo,

`F_T(x)/√T→−γ₁²g₀/4`,                              (5)

y existe una cota uniforme en x,T grande de `|F_T(x)|/√T`. Estas afirmaciones son sobre las funciones extendidas por cero; para x fijo se está dentro del soporte cuando T es grande.

## 4. La componente Π no desaparece: energía al menos lineal

Para y>0 fijo, aplicar (2), el Lema1, (5) y convergencia dominada:

`B_(F_T)(y)/√T→−(γ₁²g₀/4)C(y)≠0`.                  (6)

La medida en (3) es positiva. Restringirla a y∈[1,2] y aplicar Fatou da

`liminf_(T→∞) E_Π(F_T)/T`

`≥(γ₁⁴g₀²/16)∫_1² y^(−3/4)τ(y)C(y)²dy=:L₀>0`.    (7)

El integral es finito por la cota uniforme de C(y) del Lema1 y positivo porque C(y)>0 para cada y. La función C es medible como suma positiva de funciones continuas. Para interpretar el liminf con T real, aplicar Fatou a cualquier sucesión T_j→∞; la cota no depende de la sucesión.

Por tanto, para T suficientemente grande,

`E_red(F_T)≥E_Π(F_T)≥(L₀/2)T`.                      (8)

No se usó el término κvv* en ninguna cota de este apartado.

## 5. Cotejo con Q y exclusión de todas las escalas constantes

**CITED, verificado en LINK013 contra la prueba de Paper47.** Para estos mismos F_T,

`|Q_T(F_T)|/||F_T||²≤4·10⁹ T exp(−15.449T)`.

El bound de las derivadas L² de LINK013 da `||F_T||²=O(T^(3/2))`. Luego

`|Q_T(F_T)|=O(T^(5/2)exp(−15.449T))`.

Junto a (8),

`|Q_T(F_T)|/E_Π(F_T)=O(T^(3/2)exp(−15.449T))→0`.     (9)

**Teorema 3 (PROVED, con input CITED anterior).** Para cada c>0, para todo T suficientemente grande se tiene

`Q_T(F_T)<cE_Π(F_T)≤cE_red(F_T)`.

Por ello son falsas, como afirmaciones uniformes en todas las ventanas y tests, tanto

`Q_T(F)≥cE_Π(F)`

como

`Q_T(F)≥cE_red(F)`.

Las refutaciones se trasladan a un core suave C_c∞ por la aproximación H¹ polarcorregida de LINK013: Q es continuo en H¹ y las dos formas reducidas son acotadas por la energía de U en cada ventana, que es continua en L².

Una escala dependiente de T no queda excluida. Si fuera válida para cualquiera de estas energías, esta familia impone la condición necesaria `c(T)=O(T^(3/2)exp(−15.449T))`; no se prueba su existencia.

## 6. Alcance exacto

Se estudió la reparación concreta «quitar κvv*», con los mismos coeficientes del mapa011, y se obtuvo una obstrucción independiente en el término gaussiano Π. No se transfirió ilegítimamente una obstrucción de una forma mayor a una menor.

No se excluyen otros mapas, otros cambios de dominio, escalas suficientemente pequeñas dependientes de la ventana ni el eventual uso de −R en una identidad diferente. La cota de Q, que usa información de ceros del paper, sirve aquí sólo para refutar estas dominaciones, no como nueva positividad para D. No se modifica ningún paper.

**Estado:** NO-GO PROVED para las dominaciones uniformes constantes de este memo; auditoría favorable en AUDIT_014.md, incluida la extensión§7. D sigue OPEN y activo.

## 7. Última pieza: también falla la covarianza aritmética G_s sola

Esta extensión usa la misma familia y los mismos coeficientes de011, sin otro mapa. Sea s=1/2 y

`L₂(F)=Σ_(d≥2)a_d(F)G_s(d,2)`.

Como

`G_s(d,2)=(1−1/√2)d^(−1/2)1_(2|d)`,

la suma converge absolutamente por a_d=O(1/d). Cauchy–Schwarz en la covarianza G_s da

`E_G(F):=Σ conjugate(a_d)a_eG_s(d,e)≥|L₂(F)|²/G_s(2,2)`,

`G_s(2,2)=1/√2−1/2>0`.                              (10)

Definir el perfil

`h₂(x)=2e^(x/2)Σ_(d≥2)W_d(exp(2x))G_s(d,2)`,

`β=(1−1/√2)/2>0`.

Entonces h₂ es continuo y acotado, `h₂(+∞)=0`, y

`h₂(−∞)=−κβ`.                                      (11)

**Prueba de (11).** Es el cálculo de Riemann de LINK013 restringido a los índices pares. Con N=y^(−1/2), g(r)=r^(−1/2)m(r²) e I=∫g=κ/2,

`N^(−1/2)Σ_(2|d)d^(−1/2)m((d/N)²)`

`=(1/N)Σ_(2|d)g(d/N)→I/2=κ/4`.

Los controles de origen y cola son los mismos, con malla2/N. El término `N^(−1/2)m(N^(−2))Σ_(2|d)d^(−3/2)` tiende a0. Multiplicar por `−2(1−1/√2)` da (11). La continuidad, acotación y límite derecho se obtienen de las mismas cotas de LINK013. ∎

Por intercambio absolutamente convergente, `L₂(F)=∫Fh₂`. Aplicar la masa que escapa de G_T/T y las cotas L¹ de sus derivadas, exactamente como en LINK013, produce

`L₂(F_T)/T→γ₁²κβ/8>0`.                             (12)

De (10), `E_G(F_T)≥c₂T²` para T suficientemente grande y alguna constante c₂>0. En consecuencia ninguna c>0 independiente de la ventana permite `Q_T≥cE_G` en todos los tests.

### Corolario para combinaciones de los tres sumandos existentes

Para constantes A,B,C≥0 no todas cero, conservar exactamente a_d(F) de011 y definir

`E_(A,B,C)(F)=AκE_G(F)+Bκ|M(F)|²+C E_Π(F)`.

LINK013 calcula `|M(F_T)|²≳T²`; (10)–(12) calculan `E_G(F_T)≳T²`; y (7)–(8) calculan `E_Π(F_T)≳T`. Como los tres sumandos son no negativos, cualquier combinación fija no nula satisface `E_(A,B,C)(F_T)≳T`. La cota CITED de Q en §5 implica

`|Q_T(F_T)|/E_(A,B,C)(F_T)→0`.

Por tanto **ninguna combinación fija no negativa no nula de κG_s, κvv* y Π, aplicada con el mismo mapa de coeficientes011, admite una dominación uniforme positiva por Q_T**. Esto incluye quitar uno o dos de los sumandos; no permite inferencias sobre otros coeficientes, otro mapa, combinaciones con cancelaciones firmadas ni factores que dependan de T.

La extensión sólo termina el examen de las tres piezas del candidato conservado. No abre una ruta nueva ni modifica el estado de D.
