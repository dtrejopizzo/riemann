# VIRTUAL_SOURCE_017 — Métrica virtual: fuente positiva calculada y fallo del enlace

2026-10-19. Constructor. **PROVED, auditado en AUDIT_017.md:** una modificación explícita de la métrica elimina el defecto de adjunto de008 y da una fuente positiva con un mapa continuo unitario. Al calcular Q_T completo, reaparece un contratermino estrictamente negativo que esta construcción no controla. **No se obtuvo una fuente de signo funcional para D.**

## 0. Corpus y diferencia escrita antes del ensayo

Consultados las reglas del proyecto, índice ROUTES-TRIED-INDEX, grid y crucigrama base `CROSSWORD-TO-D.md`. Entradas pertinentes: CONSTRUCTOR008 (defecto b_n de la inversión), INV_T (gauges), INV_N (energía de saltos y potencial), P1_BBSTAR (polarización y coste total del peine), normas/Helson y LINK011–016.

**Cambio explícito respecto de008:** se conservan las fórmulas algebraicas G_n, pero se cambia la métrica gaussiana de `y^(α−1)τ(y)dy` a `y^(α−1)τ(y)²dy`. Esto permite comprobar una virtualización concreta; no se supone que sea una isometría de la completación original005/015 ni que preserve su enlace aritmético.

No se reabre un gauge ya excluido como prueba de signo. El objeto se calcula para saber si el cambio de métrica añade un mecanismo; al final se identifica su reducción a una descomposición de saltos ya indexada. No se atribuye novedad a esa descomposición ni se construye otro índice, fase o kernel del nodo.

## 1. Espacio virtual y acción exacta

Sea τ(y)=θ(y)−1>0. Para α>0 definir

`ℒ_α^virt=L²((0,∞),y^(α−1)τ(y)²dy)`.

Conservar, para n>0 real,

`(G_nf)(y)=n^α τ(n²y)/τ(y) f(n²y)`.

El operador

`S:ℒ_α^virt→L²((0,∞),y^(α−1)dy)`, `Sf=τf`,

es unitario, y

`SG_nS^(−1)g(y)=n^α g(n²y)`.

El último operador es unitario por cambio de variable. Así G_n es unitario en la métrica virtual para todo n>0 y

`G_n* =G_n^(−1)=G_(1/n)`.

Definir

`(J_virt f)(y)=y^(−α)τ(1/y)/τ(y) f(1/y)`.

Es el conjugado por S de `J_0g(y)=y^(−α)g(1/y)`, luego es una involución unitaria y

`J_virt G_n J_virt=G_n*`.                           (1)

Todas estas identidades se verifican en el espacio completo, no sólo formalmente en una colección de perfiles.

**Diferencia con009:** este grupo continuo vive en otro espacio de Hilbert y con otra norma. No interpola ni comprime las acciones V_n del módulo original mediante los mapas acotados fijos que009 excluyó.

## 2. La métrica incluye los perfiles conocidos

Para `ψ_d(y)=q_d(y)−1/d=W_d(y)/τ(y)`,

`||ψ_d||²_virt=∫_0^∞y^(α−1)|W_d(y)|²dy`.

Como `W_d=m(y)/d−m(d²y)<0`, se cumple

`|W_d(y)|≤m(d²y)≤min(1,1/(d√y))`.

Por tanto, para 0<α<1,

`||ψ_d||²_virt≤[1/α+1/(1−α)]d^(−2α)`.              (2)

La integral se separa en y=d^(−2). En particular la métrica es finita sobre todos los perfiles del caso crítico α=1/4. No se postula una norma infinita como si fuera un espacio ya realizado.

Si se reutilizaran los coeficientes a_d(F) de011, la serie `Σa_d(F)ψ_d` también convergería en esta norma, porque a_d=O_T(||F||/d) y Σd^(−1−α)<∞. Su mapa seguiría siendo suavizante por las mismas cotas de derivadas de011. Esto sólo verifica dominio; no lo propone como reparación del mapa cerrado en011–016.

## 3. Mapa continuo unitario: se puede calcular el portador total

Para F∈L²(R), definir

`(𝒞_αF)(y)=2^(−1/2)y^(−α/2)τ(y)^(−1)F((log y)/2)`.

Con y=exp(2x),

`||𝒞_αF||²_virt=∫_R|F(x)|²dx`.

Es una aplicación unitaria sobre todo ℒ_α^virt: la fórmula inversa se obtiene despejando F. Para F soportado en [−T,T], su imagen se soporta en [exp(−2T),exp(2T)].

Cálculo directo da

`G_n𝒞_αF=𝒞_α[F(·+log n)]`,

`J_virt𝒞_αF=𝒞_α[F(−·)]`.                         (3)

Los factores τ y las potencias n^α cancelan exactamente. Este es un enlace calculado con el portador continuo, no una existencia abstracta de raíces de Q_T.

## 4. Fuente positiva explícita y recuperación del peine

Fijar una ventana T y poner `v_n=2Λ(n)/√n`, n<exp(2T), como en Paper47. Para `f=𝒞_αF`, definir la energía finita positiva

`E_prime^virt(f)=(1/2)Σ_n v_n||(I−G_n)f||²_virt`.

Por (3) y la norma de una diferencia de traslaciones,

`E_prime^virt(𝒞_αF)`

`=A_T||F||²−Σ_n v_n Re c_F(log n)`,

`A_T=Σ_n v_n≥0`.                                  (4)

Se recupera exactamente el peine lineal en Λ, junto con su coste constante A_T. La fuente es positiva para Λ y para cualquier selección no negativa de esos pesos; no hay todavía una propiedad de completitud.

La parte positiva del gamma puede escribirse en el mismo espacio usando el grupo para n real:

`E_Γ^virt(f)=(1/2)∫_0^∞K(u)||(I−G_(exp u))f||²_virt du`,

`K(u)=1/[2sinh(u/2)]+1/[2cosh(u/2)]>0`.

Por (3),

`E_Γ^virt(𝒞_αF)=∫_0^∞K(u)[||F||²−Re c_F(u)]du`

`=Levy(c_F)`.

Su dominio es exactamente el dominio de energía gamma de Paper47. No se ignora el infinito del integral en tests fuera de ese dominio.

La fuente virtual independiente de signo es, por tanto,

`E_pos^virt=E_Γ^virt+E_prime^virt≥0`.                (5)

## 5. Identidad total con Q_T en el sector polar libre

En el portador par con `∫F cosh(x/2)=0`, el polo de la forma del paper se anula. Su definición exacta es

`Q_T(F)=C₀||F||²+Levy(c_F)−Σ_n v_n Re c_F(log n)`,

`C₀=ψ(1/4)−logπ<0`.

Combinarla con (4)–(5) da la identidad **total**, sin resto omitido,

`Q_T(F)=E_pos^virt(𝒞_αF)−(A_T−C₀)||F||²`.          (6)

El contratermino `A_T−C₀` es estrictamente positivo. Así la diferencia entre Q_T y la fuente positiva propuesta es estrictamente negativa para todo F≠0. No se puede usar (5) para concluir el signo de (6).

La positividad de la energía residual `E_pos^virt−(A_T−C₀)||F||²` requeriría una desigualdad adicional que acople los saltos aritméticos con el gamma en el portador restringido. Definir esa diferencia como «fuente positiva» sería volver a asumir el signo objetivo; **no se hace**.

La identidad(6) es la polarización término a término indexada en P1_BBSTAR/INV_N. Aquí reaparece después de calcular la métrica virtual; no se presenta como un nuevo puente. En particular la cancelación de b_n en(1) no redujo el coste A_T del peine.

Fuera del sector polar libre se debe añadir el bloque polar del paper. El cambio de métrica no demuestra una identidad nueva para ese bloque; no se deduce del hecho de que J_virt actúe como reflexión.

## 6. Especificidad: el signo virtual no ve el producto completo

Los cálculos de §§1–3 funcionan al sustituir τ por **cualquier función medible, finita y estrictamente positiva casi en todas partes** a(y), usando el espacio `L²(y^(α−1)a(y)²dy)`, S_a f=af y las fórmulas conjugadas correspondientes. También funcionan para τ_P del borrado finito, que es positiva.

Después del mapa 𝒞, todos esos datos se cancelan y se obtiene la misma representación de traslaciones y reflexión de L²(R). Por tanto la unitariedad y la identidad(1) no seleccionan la FE de conductor1 ni el producto de Euler completo.

Las únicas apariciones de Λ en(4) son los pesos v_n introducidos explícitamente. Su no negatividad es heredada por el borrado. El contratermino cambia con la masa de esos pesos, pero no aparece una identidad aritmética adicional de signo que lo pague.

Éste es el punto exacto donde falla la fuente propuesta: su positividad y su «dualidad virtual» son de gauge; la realización que genera los pesos del nodo no aporta un control independiente del término negativo en(6).

## 7. Resultado y alcance

Se construyó y calculó una fuente virtual explícita, positiva por energía de diferencias, con espacio, dominio, involución, acción y mapa unitario realizados. Se cotejó el peine y la parte gamma mediante una identidad total del nodo polar libre.

**Resultado del ensayo: fuente no funcional para D.** El cambio de métrica quita un defecto de adjunto auxiliar pero no la cancelación exigida por Q_T; el residuo exacto sigue siendo el potencial negativo(6). No se prueba imposibilidad de otros contraterminos, realizaciones o fuentes; no se afirma un NO-GO general contra toda virtualización.

No se modificó Paper47, no se abrió una fase nueva y no se cuenta este diagnóstico como avance positivo de D. El objetivo íntegro permanece OPEN. La investigación se reanudó; el estado registrado sigue siendo `blocked`.
