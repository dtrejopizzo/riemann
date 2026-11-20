# CONSTRUCTOR_015 — Dominio completado, no clausurabilidad y cono PSD exacto

2026-10-19. Constructor. **PROVED, revisión favorable en AUDIT_015.md:** la completación del kernel −R_α contiene todo el factor aritmético puro y se descompone como producto ortogonal `L²(P_s)⊕V`. Se construye una sucesión explícita que prueba que el operador gaussiano T no es clausurable. El cono PSD global en el espacio real generado por sus tres piezas es exactamente el ortante no negativo.

No se identifica V con todo el espacio gaussiano, no se prueba invariancia por FE y no se obtiene signo de D.

## 0. Corpus check y diferencia escrita

Consultados las reglas del proyecto, índice ROUTES-TRIED-INDEX (clausurabilidad, dominio, covarianzas, productos y notas209), archivo06, grid y crucigrama; CONSTRUCTOR005,007,008 y LINK014. En008 una sucesión de exclusiones primoriales tendía aritméticamente a0 pero su norma gaussiana divergía; no probó ni refutó clausurabilidad.

**Diferencia exacta:** la sucesión que se construye aquí no es ese primorial ni un cambio de nombre. Es un producto con pequeñas inclinaciones positivas sobre muchos primos altos, normalizado por su esperanza P_s. Su varianza aritmética y su norma gaussiana tienden simultáneamente a0 alrededor de la constante1. La cota decisiva usa el exponente `r=(s+1)/2>s` del **mismo** kernel Π ya calculado en011. Esto produce un límite fuerte nuevo y resuelve la cuestión de dominio que008 dejó abierta.

No se afirma que las inclinaciones de productos de Bernoulli sean por sí mismas novedosas ni una fuente de signo para Q_T. Se aplican aquí para determinar exactamente la completación de un kernel prefijado. Tampoco se extrapola la caracterización de un cono tridimensional a todo kernel positivo.

## 1. Dominio, espacios y constantes

Fijar `0<α<1/2`, `s=2α∈(0,1)`, `κ=−Z_α>0`. Sea P_t la ley producto de valuaciones geométricas de005, con `E_tX_d=d^(−t)`. L²(P_s) es el espacio de esa ley producto, equivalentemente la completación de los cilindros de valuaciones; para s<1 **no** es una ley zeta normalizable sobre enteros positivos.

Sobre el álgebra finita de divisibilidad, tomar el dominio **Haarcentrado**

`𝒜₀={A: E_1A=0}`.

El operador gaussiano es

`TA(y)=E_yA`, `ℒ_α=L²((0,∞),y^(α−1)τ(y)dy)`.

La isometría de005–007 es

`ι(A)=(√κ A,TA)` en `L²(P_s)⊕ℒ_α`,

`||ι(A)||²=κ Var_s(A)+κ|E_sA|²+||TA||²`.

Sea 𝓗_α la clausura de ι(𝒜₀), como en007–008. Para no confundir las medias: `E_1A=0` no significa `E_sA=0`. Precisamente esa diferencia permite la aproximación siguiente.

Usar la cota probada en LINK011:

`||T(X_d−1/d)||_(ℒ_α)≤C_α d^(−r)`, `r=(s+1)/2>s`.     (1)

## 2. Productos sobre bloques de primos altos

Elegir bloques finitos E_j de primos con

`P_j:=min E_j→∞`, `H_j:=Σ_(p∈E_j)p^(−s)→∞`.

Por ejemplo, tomar en orden todos los primos p≥max(2,j) hasta que la suma de p^(−s) alcance j³ por primera vez. Esto fija E_j de manera determinista y cumple ambas condiciones.

Existen sin PNT: la divergencia elemental de Σ_p1/p implica la de Σ_pp^(−s), y se pueden tomar sumas parciales cada vez más lejos. Para recordar la prueba elemental, el producto finito ∏_(p≤x)(1−1/p)^(−1) contiene la suma armónica hasta x, mientras su logaritmo es Σ_(p≤x)1/p+O(1); por ello esa suma y cualquiera de sus colas divergen. No hace falta controlar la longitud ni el mayor primo del bloque.

Poner `t_j=H_j^(−2/3)` y, para u>0,

`Z_(u,j)=∏_(p∈E_j)(1+t_j p^(−u))`.

Para abreviar, suprimir j en las siguientes fórmulas. Definir el polinomio finito

`B_j=∏_(p∈E_j)(1+t_jX_p)/Z_(s,j)`,

`A_j=B_j−Z_(1,j)/Z_(s,j)`.

Por independencia y porque los índices son squarefree,

`E_sB_j=1`, `E_1B_j=Z_1/Z_s`, y `A_j∈𝒜₀`.

## 3. Convergencia aritmética fuerte a1

Para u_p=p^(−s),

`E_sB_j²=∏_(p∈E_j)[1+t_j²u_p(1−u_p)/(1+t_ju_p)²]`

`≤exp(t_j²H_j)`.

Por ello

`Var_s(B_j)≤exp(H_j^(−1/3))−1→0`.                    (2)

Además, usando `log(1+x)≤x` y `log(1+x)≥x−x²/2`,

`log(Z_r/Z_s)≤t_jΣp^(−r)−t_jH_j+(t_j²/2)Σp^(−2s)`

`≤−t_jH_j[1−P_j^(−(r−s))−t_j/2]→−∞`.              (3)

Aquí `Σp^(−r)≤P_j^(−(r−s))H_j` y `Σp^(−2s)≤H_j`. Como 1>r, `Z_1≤Z_r`, así que

`θ_j:=Z_1/Z_s→0`.

En consecuencia,

`E_sA_j=1−θ_j→1`,

`E_s|A_j−1|²=Var_s(B_j)+θ_j²→0`.                    (4)

## 4. La norma gaussiana tiende a0, no diverge como en008

Sea Q_j el producto de los primos de E_j. La expansión centrada exacta es

`A_j=(1/Z_s)Σ_(d|Q_j) t_j^(ω(d))(X_d−1/d)`.

El término d=1 es cero. Todos los coeficientes restantes son positivos. Aplicar (1) y la desigualdad triangular en ℒ_α:

`||TA_j||≤(C_α/Z_s)Σ_(d|Q_j,d>1)t_j^(ω(d))d^(−r)`

`=C_α(Z_r−1)/Z_s→0`                                (5)

por (3). Se trata de la norma, no de su cuadrado; el cuadrado también tiende a0.

De (4)–(5),

`ι(A_j)→(√κ·1,0)` fuertemente.                       (6)

**Resultado clave:** el vector aritmético constante puro pertenece a 𝓗_α. No es la imagen de un polinomio constante en el dominio Haarcentrado; aparece en la completación porque ese centro no es continuo para la ley P_s.

## 5. Todo el factor aritmético puro y descomposición de la completación

Las acciones D_n de007 son acotadas en 𝓗_α y en ambos factores del producto. En el factor aritmético,

`D_n1=X_n`;

en el gaussiano, `T(D_nA)(y)=q_n(y)TA(n²y)`, un operador acotado que lleva0 a0. Aplicar D_n a (6) da

`ι(D_nA_j)→(√κ X_n,0)`.

Por tanto 𝓗_α contiene todos los vectores aritméticos puros de la forma `(X_n,0)` y su clausura. El span de X_n es denso en L²(P_s): las diferencias finitas de umbrales de valuación dan indicadores de cualquier patrón de valuaciones finitas; truncar los valores de esas coordenadas y después ampliar las coordenadas aproxima cualquier función L² de la ley producto. Así

`L²(P_s)⊕{0}⊂𝓗_α`.                                 (7)

Definir, sin ampliarlo por hipótesis,

`V:=closure_(ℒ_α){TA:A∈𝒜₀}`.

De cada ι(A) se puede restar su componente aritmética pura, disponible por (7), y obtener `(0,TA)∈𝓗_α`. Tomando clausuras,

`{0}⊕V⊂𝓗_α`.

La inclusión inversa es inmediata: todas las imágenes iniciales están en el producto cerrado `L²(P_s)⊕V`. Luego

**Teorema 1 (PROVED).**

`𝓗_α=L²(P_s)⊕V`                                    (8)

como suma ortogonal, con la normalización de la inmersión ι indicada en§1.

No se afirma `V=ℒ_α`. Tampoco se deduce que la inversión ambiental de008 preserve V: eso necesita otra prueba.

## 6. T es densamente definido y NO clausurable: sucesión explícita

La aproximación (6) y sus D_n muestran que 𝒜₀ es denso en L²(P_s). Sea

`f₂=X_2−1/2∈𝒜₀`, `Tf₂=q_2−1/2=:ψ₂≠0`.

Definir

`C_j=D_2A_j−(1/2)A_j∈𝒜₀`,

`F_j=f₂−C_j∈𝒜₀`.

Por la continuidad en ambos factores de las acciones utilizadas,

`C_j→f₂` en L²(P_s), `TC_j→0` en ℒ_α.

En consecuencia,

`F_j→0` en L²(P_s), `TF_j→ψ₂≠0` en ℒ_α.             (9)

Esta es la violación exacta del criterio de clausurabilidad. ψ₂ es no nulo porque q_2(y)<1/2 para todo y>0 y tiene norma finita por(1).

**Teorema 2 (PROVED).** El operador `T:𝒜₀⊂L²(P_s)→ℒ_α` es densamente definido y no clausurable.

La sucesión primorial008 sigue teniendo la divergencia allí probada; no se corrige esa prueba ni se atribuye a aquella sucesión el límite fuerte(9).

## 7. Los tres sumandos son ahora proyecciones ortogonales verdaderas

En (8), descomponer el factor aritmético en su constante y su subespacio de media P_s cero:

`𝓗_α=(L²_0(P_s)⊕0) ⊕ (C·1⊕0) ⊕ (0⊕V)`.

Las tres piezas del kernel se extienden a las energías de esas proyecciones:

- `κG_s(A)=κ Var_s(A)` es la energía del primer sumando.
- `κvv*(A)=κ|E_sA|²` es la del segundo.
- `Π(A)=||TA||²` es la del tercero.

En particular, para el vector unitario `e=(1,0)∈𝓗_α`,

`||Proj_e ι(A)||²=κ|E_sA|²`.

El rango uno de005 **sí** se realiza ahora como una proyección ortogonal sobre la constante aritmética pura, afirmación que no estaba justificada antes de(6)–(8). Esto no lo identifica con el polo de Q_T ni con cosh(x/2). De hecho la familia de LINK013 tiene momento cosh cero y M(F_T) de orden T: el mapa011 no entrelaza esas dos proyecciones. Este nuevo hecho del espacio auxiliar no paga el polo del paper.

## 8. Cono PSD real exacto en el span de las tres piezas

Para coeficientes reales a,b,c, considerar sobre **todo** 𝒜₀ la forma

`𝔈_(a,b,c)(A)=aκVar_s(A)+bκ|E_sA|²+c||TA||²`.

Cada sumando es ≤||ι(A)||², por lo que la forma firmada es continua en la norma de 𝓗_α y se extiende a (8).

**Teorema 3 (PROVED).** La forma 𝔈_(a,b,c) es PSD sobre todo 𝒜₀ si y sólo si

`a≥0`, `b≥0`, `c≥0`.

**Prueba.** La suficiencia es005. Para necesidad, PSD en el dominio denso se extiende a su completación. Probarla en tres vectores puros no nulos:

1. `(X_2−2^(−s),0)∈L²_0(P_s)⊕0` obliga a a≥0.
2. `(1,0)` obliga a b≥0.
3. `(0,ψ₂)∈0⊕V` obliga a c≥0.

Los tres vectores pertenecen a 𝓗_α por (8) y §6; sus normas respectivas son positivas. Si un coeficiente fuera negativo, aproximar el vector puro correspondiente por imágenes de 𝒜₀ daría un test algebraico de valor negativo. ∎

No se requiere trasladar una inferencia de entradas positivas a PSD, ni usar una divergencia exploratoria.

## 9. Consecuencia para el candidato011 y límite de la clasificación

En α=1/4, LINK014 ya excluye toda dominación uniforme por Q_T de una combinación fija **no negativa no nula** de esas piezas, aplicada con exactamente los coeficientes a_d(F) del mapa011.

El Teorema3 muestra ahora que permitir coeficientes reales firmados no amplía la clase **si se exige que la combinación sea PSD globalmente sobre 𝒜₀**. Toda combinación real fija no nula con esa propiedad ya pertenece al ortante excluido por014 para ese mismo mapa.

**Límites obligatorios:**

- No se clasifican formas firmadas que sólo sean positivas en un subespacio particular, por ejemplo únicamente sobre la imagen de a_d(F).
- No se excluyen transformaciones del mapa, otros kernels, coeficientes dependientes de T ni cancelaciones firmadas fuera de este span tridimensional.
- La descomposición de dominio no prueba invariancia/reductividad de V por la FE ambiental ni un enlace con gamma, peine o polar de Q_T.
- No se afirma que la no clausurabilidad impida toda realización alternativa. Es una propiedad exacta del operador T aquí definido.

**Estado final:** estructura del dominio, no clausurabilidad y cono PSD global PROVED, auditoría favorable en AUDIT_015.md. D permanece OPEN y activo; ningún paper modificado.
