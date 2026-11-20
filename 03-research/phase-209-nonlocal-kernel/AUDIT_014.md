# AUDIT_014 — componente gaussiana tras quitar el rango uno

2026-10-19. Revisor hostil. **PROVED, con input CITED de Paper47 declarado.**

Revisión de `LINK_014_REMOVING_RANK_ONE.md`. Se consultaron las reglas del proyecto, índice de rutas, grid y crucigrama. La diferencia frente a013 es sustantiva: su lower bound dependía de κvv*; aquí se estudia una subforma menor, Π, mediante un argumento independiente. No se deduce una obstrucción para una forma menor desde la obstrucción para una mayor.

## 1. Dominio y kernel positivo

Para d≥2, W_d(u)<0 y f_d(y)=q_d(y)−1/d<0. Cada sumando de K_y es positivo, y en compactos la convergencia es uniforme por una mayorante O(d⁻²). Su integral global se calcula por la Mellin absolutamente convergente de m:

`∫2e^(x/2)W_d(e^(2x))dx=−κ(d^(−1/2)−d⁻¹)`.

Tonelli prueba exactamente `∫K_y=κΣv_d(1/d−q_d(y))=C(y)`, con 0<C(y)≤κ[ζ(3/2)−ζ(2)]. No se requiere una mayorante uniforme en x para intercambiar suma e integral global: se usa positividad. Para F acotado, |F|K_y es integrable y justifica la identidad puntual de B_F. Las sumas parciales convergen además en el factor gaussiano por011; una subsucesión converge casi en todas partes y coincide con la suma puntual. Por ello la identidad de energía (3) es legítima.

## 2. Límite local y paso al integral

La inversión de Fourier tiene prefactor √(k/T)/(2π), fase √k zx/T y límite exp(−z²/6). Su integral da `g₀=√(3(21/e)/(2π))`, con la normalización correcta. La dominación gaussiana en |z|≤√k y las dos colas en v prueban tanto el límite local como el supremo uniforme. Los momentos Fourier dan `||G_T^(j)||∞=O(T^((1−j)/2))`; para j=2,4 sus contribuciones a F_T/√T desaparecen uniformemente.

En consecuencia F_T/√T converge puntualmente a −γ₁²g₀/4 y está uniformemente acotada. K_y∈L¹ permite convergencia dominada para cada y; no se supone convergencia en todo el espacio gaussiano. Fatou sobre [1,2] basta para obtener `liminf E_Π(F_T)/T≥L₀>0`. C(y) es medible y acotada, τ es positiva continua en ese intervalo y C(y)>0 en cada punto. El argumento por sucesiones justifica el liminf para T real.

Fijar T≥1 al presentar la familia garantiza k≥8, derivadas suficientes y pertenencia al dominio de forma; no afecta ninguna conclusión asintótica.

## 3. Cotejo con la forma declarada

La cota CITED se refiere a estos F_T concretos, como se verificó en013 contra la prueba de Paper47; no se extrae una cota para un test desde el ínfimo espectral. Con ||F_T||²=O(T^(3/2)), resulta |Q_T|=O(T^(5/2)e^(−15.449T)). Dividir por E_Π≥c₀T da el cociente O(T^(3/2)e^(−15.449T)) y excluye toda constante positiva fija para Π y para S−κvv*.

La aproximación suave en H¹ preserva polar y desigualdad estricta: Q es continua en H¹ y las energías reducidas son continuas en L² de cada ventana por011 y dominación por S. La necesidad para una posible escala c(T) es sólo una cota superior; no se afirma existencia ni imposibilidad de tal escala.

## Veredicto

**Favorable.** La eliminación del rango uno del kernel no repara la dominación uniforme con el mapa011. No se obtuvo positividad nueva de D, ni una obstrucción para otros mapas o para coeficientes dependientes de T. El uso de información de ceros está declarado y limitado al falsificador.

## Addendum final — §7 y combinaciones de las tres piezas

Revisada la extensión completa de §7. **Veredicto favorable, PROVED con el mismo input CITED.**

La covarianza con el índice2 es cero para d impar y `(1−1/√2)d^(−1/2)` para d par; G_s(2,2)=1/√2−1/2>0. La serie L₂ converge absolutamente y Cauchy–Schwarz se aplica a la forma PSD G_s, también para la serie límite porque κG_s≤S y la expansión de011 converge en S.

El Riemann sum sobre índices pares tiene densidad1/2: `(1/N)Σ_(2|d)g(d/N)→(1/2)∫g=κ/4`. El factor −2(1−1/√2) da h₂(−∞)=−κβ, β=(1−1/√2)/2. Las mismas mayorantes integrables de013 justifican las colas; el término positivo restante es O(N^(−1/2)) porque m≤1 y Σd^(−3/2)<∞. Continuidad local y límite derecho por las cotas gaussianas completan la acotación global del perfil.

La parte par del perfil tiende a −κβ/2 en ambos extremos. Por escape de masa de G_T/T y derivadas de norma L¹=o(T), `L₂(F_T)/T→γ₁²κβ/8`. Los factores de dos de (11) y (12) son correctos. Cauchy–Schwarz entrega E_G(F_T)≳T²; por tanto también esta pieza sola falla como dominación uniforme con escala fija positiva.

El corolario A,B,C≥0, no todos cero, es válido: cada energía es no negativa, la menor tasa de crecimiento garantizada entre las piezas es T y Q decae exponencialmente con un prefactor polinómico. La conclusión cubre cualquier combinación fija no negativa no nula con exactamente los coeficientes a_d(F) de011. No cubre cancelaciones firmadas, otro mapa ni factores dependientes de T. Es la finalización del examen de las tres piezas existentes; no un NO-GO general para D.
