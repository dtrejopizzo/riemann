# LINK_013 — Ninguna escala positiva fija repara el mapa011 en todas las ventanas

2026-10-19. Constructor. **PROVED, revisión favorable en AUDIT_013.md**, usando como input CITED la cota para la familia explícita de Paper47 lem:testfam y la prueba de thm:margin/cor:margin1. No hay cálculo numérico nuevo.

**Enunciado:** para cada constante c>0 existen ventanas arbitrariamente grandes —de hecho todas las suficientemente grandes— y tests pares polar libres F_T tales que

`Q_T(F_T)<c ||U_TF_T||²`.

U_T es exactamente el mapa Mellin–Gauss de LINK011, sin cambiar su normalización. Se descarta una reparación por una constante universal pequeña. No se excluye una escala dependiente de T ni otro mapa. D sigue OPEN y activo.

## 0. Corpus y diferencia frente a012

Consultados las reglas del proyecto, índice ROUTES-TRIED-INDEX (LINK011/012, margen y familia42/e, residuos06), grid maestro y crucigrama. Verificación directa en Paper47: lem:testfam, thm:margin **y su prueba**, cor:margin1. No se confunde un ínfimo pequeño con un test que no anule U.

**Razón nueva escrita:** LINK012 sólo falsificó la escala1 en T=4/5. Aquí se usa T→∞ y se calcula la respuesta del **mismo** U sobre la familia explícita del paper que tiene cociente Q pequeño. El dato nuevo a probar es que U no comparte su anulación: su componente de rango uno crece linealmente en T. Sólo entonces se aplica la cota del paper.

La cota superior CITED del paper utiliza información certificada de ceros y la fórmula explícita. Se usa aquí exclusivamente para refutar una dominación propuesta, no como una fuente nueva de signo positivo para D ni mediante equivalencias externas.

## 1. Componente de rango uno del mapa U

Usar κ=−Z_(1/4)>0 y v(d)=d^(−1/2)−d^(−1). Por CONSTRUCTOR005 y LINK012,

`||U_TF||²≥κ|M(F)|²`,

`M(F)=Σ_(d≥2)a_d(F)v(d)=∫_(−T)^T F(x)h(x)dx`,

`h(x)=2e^(x/2)Σ_(d≥2)v(d)W_d(exp(2x))`.

El perfil h no depende de T: las ventanas sólo restringen el integral. Definir

`m(y)=y^(−1/2)−τ(y)`, `z_c=ζ(3/2)−ζ(2)`.

Como W_d(y)=m(y)/d−m(d²y), la misma serie es

`h(x)=2y^(1/4)[z_c m(y)−Σ_(d≥2)(d^(−1/2)−d^(−1))m(d²y)]`, `y=exp(2x)`.  (1)

Ambas expresiones convergen absolutamente para cada x; no se separa un vector polar divergente.

## 2. Asíntotas del perfil: h(−∞)=−κ y h(+∞)=0

**Lema 1 (PROVED).** h es continuo y acotado en R y

`lim_(x→−∞)h(x)=−κ`, `lim_(x→+∞)h(x)=0`.

**Prueba.** De Poisson y la comparación gaussiana,

`0<m(y)<min(1,y^(−1/2))`.

Poner N=y^(−1/2) y

`g(r)=r^(−1/2)m(r²)`.

La función g es continua en (0,∞), con cota integrable `g(r)≤min(r^(−1/2),r^(−3/2))`. La suma de Riemann satisface

`N^(−1/2)Σ_(d≥2)d^(−1/2)m((d/N)²)`

`=(1/N)Σ_(d≥2)g(d/N)→∫_0^∞g(r)dr`.

Para justificar la singularidad y la cola uniformemente, el tramo d≤εN es ≤2√ε+o(1); el tramo d≥RN es ≤2/√R+o(1); entre ambos extremos se aplica la suma de Riemann usual. La omisión de d=1 cuesta O(N^(−1/2)).

El integral es

`I=∫_0^∞r^(−1/2)m(r²)dr=(1/2)∫_0^∞y^(−3/4)m(y)dy=κ/2`.

Mientras tanto,

`Σ_(d≥2)d^(−1)m((d/N)²)=O(1+logN)`

por separar en d≤N y d>N y usar las dos cotas de m. Multiplicado por N^(−1/2), ese término tiende a0, igual que `N^(−1/2)z_c m(N^(−2))`. La fórmula (1) da h(−∞)=−2I=−κ.

En +∞ se usa la representación con τ: todos los términos decaen gaussianamente en exp(2x), y su suma, multiplicada por exp(x/2), tiende a0. La convergencia local uniforme se sigue de las cotas de LINK011. Las sumas de Riemann anteriores también son uniformemente acotadas, y dan acotación global de h. ∎

Para el perfil par `h_ev(x)=[h(x)+h(−x)]/2` se concluye

`h_ev(x)→−κ/2` cuando |x|→∞.                         (2)

## 3. La familia precisa del paper, no un minimizador abstracto

Trabajar desde ahora con T≥1, de modo que k≥8. Sea γ₁ la primera ordenada usada en Paper47 lem:testfam y fijar

`k=k(T)=ceil(21T/e)`,

`b_k=(k/2)1_[-1/k,1/k]`, `ω_k=b_k^{*k}`,

`G_T(x)=ω_k(x/T)`,

`P(D)=D⁴+(γ₁²−1/4)D²−γ₁²/4`,

`F_T=P(D)G_T`.

Por el lema citado, F_T es real, par, soportado en [−T,T], de energía finita, y sus dos momentos exponenciales ±1/2 son cero. Por tanto pertenece al portador polar libre, con `Q_T(F_T)=𝔞_T(F_T)`.

Además G_T≥0 y `∫G_T=T`. No se normaliza F_T todavía: la comparación de las dos formas es homogénea.

## 4. Estimaciones de spline necesarias para calcular M(F_T)

**Lema 2 (PROVED).** Para cada entero fijo j≥0,

`||ω_k^(j)||₂²=O_j(k^(j+1/2))`, `||ω_k||∞=O(√k)`.

**Prueba.** Por Plancherel y `ω̂_k(u)=sinc(u/k)^k`,

`||ω_k^(j)||₂²=(k^(2j+1)/(2π))∫v^(2j)|sinc(v)|^(2k)dv`.

Para |v|≤1, la serie alternada del seno da `|sinc v|≤1−v²/7≤exp(−v²/7)`, y el integral con el peso v^(2j) es O_j(k^(−j−1/2)). Para 1≤|v|≤2, `|sinc v|≤sin1<1`; para |v|≥2 se usa `|sinc v|≤1/|v|`. Las dos últimas contribuciones decrecen exponencialmente y quedan absorbidas en la cota indicada para k grande. El argumento con `∫|ω̂_k|` y exponente k, sin el peso, da `||ω_k||∞=O(√k)`. ∎

Como k~T, el cambio de escala da

`||G_T^(j)||₂=O_j(T^(3/4−j/2))`.

En particular,

`||G_T''||₁=O(T^(1/4))`,

`||G_T''''||₁=O(T^(−3/4))`,

`||F_T||₂²=O(T^(3/2))`.                             (3)

Las dos cotas L¹ usan el soporte de longitud2T y Cauchy–Schwarz; no se deriva h para obtenerlas.

### La masa de G_T/T escapa de todo compacto

Es una probabilidad par. Para R fijo,

`(1/T)∫_|x|≤R G_T(x)dx≤(2R/T)||ω_k||∞=O_R(T^(−1/2))→0`.

Por (2), acotación de h y paridad de G_T,

`(1/T)∫G_T(x)h(x)dx→−κ/2`.                         (4)

La prueba es separar un compacto donde su masa tiende a0 y su complemento donde h_ev está uniformemente próximo a−κ/2.

## 5. U no comparte la anulación de la familia: M crece como T

Por definición de F_T,

`M(F_T)=−(γ₁²/4)∫G_T h`

`       +(γ₁²−1/4)∫G_T''h+∫G_T''''h`.

El perfil h está acotado. Las dos cotas L¹ de (3) hacen que los términos de derivadas sean o(T). Con (4), se obtiene la asíntota exacta

`M(F_T)/T→γ₁²κ/8>0`.                               (5)

Por consiguiente,

`||U_TF_T||²≥κ|M(F_T)|²`,

`liminf_(T→∞) ||U_TF_T||²/T² ≥γ₁⁴κ³/64>0`.          (6)

Éste es el paso que no se deduce de un margen pequeño: se calculó la respuesta del mapa sobre los mismos tests que se usarán para acotar Q.

## 6. Cota de Q para ESTA familia y comparación

**CITED y verificado contra la prueba de Paper47.** La prueba de thm:margin toma precisamente F_T de lem:testfam; su paso(6) acota `𝔞_T(F_T)` por una suma de valores absolutos, y su paso(7) divide por una cota inferior de `||F_T||²`. La optimización k=ceil(21T/e) de cor:margin1 da, para T≥1,

`|Q_T(F_T)|/||F_T||²≤4·10⁹ T exp(−15.449T)`.            (7)

No se infiere (7) de `inf Q/||F||²` por un cambio lógico ilegítimo: se usa la familia concreta de la prueba. El input de ceros del paper queda limitado a esta cota superior CITED.

Por (3),

`|Q_T(F_T)|≤O(T^(5/2)exp(−15.449T))`.

Por (6), el denominador `||U_TF_T||²` es ≥c₀T² para alguna constante c₀>0 y T suficientemente grande. Así

`|Q_T(F_T)|/||U_TF_T||²=O(T^(1/2)exp(−15.449T))→0`     (8)

sin presuponer Q_T≥0. Si algún Q fuera negativo, la dominación positiva ya fallaría allí. El valor absoluto en (7) procede de la suma absoluta del paso(6) de la prueba del paper, aunque el enunciado del corolario sólo necesita su cota superior sin valor absoluto.

## 7. Teorema de exclusión de escala universal

**Teorema 3 (PROVED, con input CITED(7)).** Para cada c>0 existe T_c tal que para todo T≥T_c,

`Q_T(F_T)<c||U_TF_T||²`.

Por tanto no existe una constante positiva c independiente de T con

`Q_T(F)≥c||U_TF||²`

para todas las ventanas y todos los tests pares polar libres del portador.

La misma refutación alcanza un core C_c∞: para cada ventana que dé una desigualdad estricta, aproximar F_T en H¹ por tests pares suaves y corregir el momento cosh. Q_T es continuo en H¹ y U_T en L²; el margen estricto se conserva.

### Escalas dependientes de T

El resultado no excluye c(T)>0. Si una dominación de ese tipo fuera válida, la familia calculada obligaría a

`c(T)≤O(T^(1/2)exp(−15.449T))`

para T grande. Es sólo una condición necesaria; no demuestra que exista tal escala ni que su elección produzca signo útil.

## 8. Alcance

LINK012 refutó la escala1 en una ventana. Esta nota excluye **toda constante universal positiva** para el mismo mapa, porque su componente de rango uno no desaparece sobre la familia explícita de energía Q pequeña.

No se cambia el kernel −R, no se presenta otro mapa ni una norma genérica como prueba de D. No se excluyen mapas diferentes, compresiones generales ni un eventual enlace exacto que cambie de clase. El objetivo D continúa abierto y activo.
