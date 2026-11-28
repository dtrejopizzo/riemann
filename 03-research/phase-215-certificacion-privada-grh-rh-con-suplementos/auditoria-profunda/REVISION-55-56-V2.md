# Revisión de P55/P56 corregidos — V2

28-11-2026. Se leyó el `git diff` actual y se reconstruyeron las correcciones en sus contextos, sin modificar manuscritos. El dictamen distingue el cálculo corregido, su escritura literal y su propagación. No se presupone que la revisión simultánea de exchange53 ya esté cerrada.

## Resultado

- **(a)** Las reparaciones M3, generador tame G4 y restricción de BL(c) a γ_w en55 corrigen los defectos identificados, sin aumentar constantes.
- **(a), con la definición de nivel indicada abajo:** el nuevo promedio de conjugados sobre D preserva el tipo e_c y satisface exactamente la identidad de Higman con c₀=#D|N. Su uso en la prueba III no incurre en una nueva pérdida.
- **(b) literal, reparable por una definición:**55:6104 todavía define incorrectamente J_O^(1)=J_O∩J₁. Como J₁⊂J₀⊂J_O, eso es J₁, no el nivel J_O hecho principal solamente en los lugares auxiliares. Esta errata reaparece en58:67922 y contradice la identificación con invariantes H usada por el nuevo promedio.
- **(b) fidelidad de dos citas de56:** BL conserva el antiguo dominio F(O) en vez de e_cF(O); G4 conserva la explicación falsa mediante norma F_(q^n)→F_(q^d). Las correcciones correspondientes sí están en55 y58. Las otras modificaciones locales de56 son sólo estas citas: no se cambió su prueba de exponentes de cup products.

## 1. Reconstrucción del promedio, sin denominadores adicionales

Fuentes55:6045–6141; definición del tipo55:7535–7553. Se tienen J₀ libre, J₁ normal en J₀ y Γ=J₀/J₁, producto de grupos GL en los lugares auxiliares. En el modelo de funciones sobre representantes×Γ, sea S una sección de los cosets kΓ′. La multiplicación Ψ₁ por 1_S es integral y

\[
\sum_{h\in\Gamma'}h^{-1}\Psi_1h\,f(g,k)
=\#(S\cap k\Gamma')f(g,k)=f(g,k).
\]

Esta identidad no requiere dividir por |Γ′| y vale para cada subgrupo, incluidos K₁ y Γ utilizados más tarde.

En los lugares elegidos, D=∏GL_n(F_w) actúa sobre el espacio de nivel J₁: J₁ es principal allí y los representantes de D normalizan tanto J₁ como su carácter, trivial en esos factores. La elección de lift no cambia el operador. Los representantes son matrices integrales con inversa integral, también en los factores sobre ℓ cuando los hay; por ello R(d) y R(d)⁻¹ preservan los gauges de integridad. Sus soportes son disjuntos de los de Γ, así que ambas acciones conmutan.

Definiendo

\[
\Psi=\sum_{d\in D}R(d)^{-1}\Psi_1R(d)
\]

se obtiene un operador integral. Conjugar por R(a) permuta los sumandos mediante d↦da, de modo que Ψ conmuta con D. En particular conmuta con H=J_O/J₀ y con los operadores ϱ(u)=ψ(det u)R(diag(u,1)) que definen G_c; por linealidad conmuta con e_c. **No se aplica e_c de nuevo a Ψf**: no aparece su denominador. Finalmente,

\[
\sum_{h\in\Gamma'}h^{-1}\Psi h
=\sum_{d\in D}R(d)^{-1}1R(d)=|D|\,1.
\]

Si y es Γ-invariante y e_cy=y, entonces |D|y=Σ_h h⁻¹Ψy=Σ_h hΨy. Además Ψy sigue siendo de tipo e_c. Se ha comprobado la identidad de operadores, no sólo una igualdad en un cociente racional.

El tamaño es permitido: n=r′+t′≤r+t=6r≤5r²=rt para r≥2. La inclusión bloque diagonal GL_n(F_w)→GL_rt(F_w) implica divisibilidad de órdenes factor por factor; por tanto c₀=#D divide N_ch=∏#GL_rt(F_w). Los estabilizadores se inyectan en H⊂D. Que c₀ aumente desde #H a #D no altera ninguna cota escrita en términos de N.

### Definición de nivel que todavía falla literalmente

55:6061–6065 define J₁ como subgrupo de J₀ obtenido imponiendo nivel principal en los w_j. En55:6104 se escribe J_O^(1)=J_O∩J₁. Por inclusión esto da J_O^(1)=J₁. Sin embargo55:6130 identifica A(J_O^(1),χ_O) con A(J₁,χ)^H. Para H no trivial, la segunda condición añade invariancia que no impone el nivel J₁: la igualdad no se sigue y no es la identificación correcta de niveles.

La definición necesaria es

\[
J_O^{(1)}=J_O\cap\{k:k_{w_j}\equiv1\pmod{w_j}\text{ para todo }j\}.
\]

Así J₁⊲J_O^(1), J_O^(1)/J₁=H, y A(J_O^(1),χ_O)=A(J₁,χ)^H exactamente. Esta corrección de definición hace válidos los pasos de invariancia anteriores sin cambiar el grupo D, c₀, integridad o rango. El fallo literal empieza en6104; la deducción que lo usa está en6130. No es un contraejemplo a la posibilidad de construir Ψ.

## 2. Usos posteriores del operador y ausencia de nueva pérdida

Se inspeccionaron los usos enumerados por `rg` en55:2959–2974,3017–3035,3103–3128 y7465–7511.

1. La inserción para Γ′=K₁ usa únicamente integralidad y Σκ κ⁻¹Ψκ=c₀. La suma sobre D proporciona exactamente esa identidad.
2. La inducción de normas no supone que Ψ conmute con el álgebra de Hecke:55:3017–3019 lo advierte expresamente. Que ahora conmute con e_c no cambia ese orden de multiplicación.
3. El espacio Y de55:3103 se restringe expresamente a e_c; Hecke, grupos en w_j y Ψ lo preservan. Por ello los sistemas nuevos a nivel principal mantienen el tipo de las etiquetas y BL(c) se les aplica, una vez corregida la definición J_O^(1).
4. Para u=Ψ(d₁l), la norma es c₀d₁l; el cálculo55:3029–3035 da integridad de d₁c₀A∂_Jy. En la aplicación d₁=N y c₀|N, así Nc₀A∂_Jy integral implica N²A∂_Jy integral multiplicando por N/c₀. La condición de divisibilidad con n₀c₀² está dominada por la ya escogida con n₀N². No aparece un factor N³ por una nueva proyección.
5. El emparejamiento se calcula directamente al nivel J_O y conserva su factor N; el cambio de construcción de Ψ no renormaliza ese emparejamiento.

Estos pasos son independientes de la identidad exchange53. La existencia y las propiedades de los lifts que entran en los datos globales siguen siendo obligaciones anteriores distintas.

## 3. M3, G4 y BL(c)

**M3,55:883–890: (a).** Si una raíz pertenece a un factor irreducible de grado d≤r, su orden divide p_i^d−1. Este factor divide |GL_rt(F_w)| porque d≤rt. Si v_ℓ(ω−1)>0, ω es una raíz de orden ℓ^a, y v_ℓ(ω−1)=1/(ℓ^(a−1)(ℓ−1))≤1. Cada raíz contribuye como máximo1, de modo que v_ℓ det(R(γ)−1)≤r, y cuando hay contribución ℓ|N_ch, luego r≤rv_ℓ(N_ch). El caso ℓ=2 también queda incluido. No se necesita d|r. La ausencia de raíz1 sigue siendo la condición de buena etiqueta utilizada antes, no una conclusión circular de regularidad.

**G4,55:3943–3950: (a) la reparación de compatibilidad.** La inercia tame es pro-cíclica; la imagen de un generador topológico en F_(q^d)^× es un generador. Para cada d_k|d=lcm(d_k), θ_(d_k) es la norma de θ_d. Esto permite aplicar la descripción de profundidad cero simultáneamente a todos los factores sin el inexistente supuesto d|n. La elección es compatible con los generadores fijos de las convenciones; no se está afirmando que todos los elementos de inercia tengan el mismo espectro. El rango mixto2+3, n=5,d=6, está incluido por esta vía.

**BL(c),55:2260–2274 y6569–6576: (a) la restricción corregida.** La identidad con el polinomio fijo o_w se afirma ahora en γ_w. Para s distinto, sólo se afirma que los autovalores son las potencias correspondientes y1. En la aplicación de la condición(6),55:2854–2864, se escogen precisamente generadores tame δ_v en los lugares elegidos; se puede y se debe tomar δ_v=γ_w. No se necesita el polinomio fijo para todos s. La frase posterior «ρ_x|I_w ... eigenvalues» debe entenderse a esos generadores ya fijados: el argumento efectivo se escribe sobre δ_v. P56:7937–7988 usa polinomios q_s dependientes de s y no requiere recuperar la afirmación falsa para todos s.

La nueva definición base level=e_cF(O) figura en el enunciado BL, la definición del espacio y la aplicación a Y. Es la restricción necesaria para conservar las condiciones de etiquetas en sistemas a nivel auxiliar.

## 4. Propagación a58 y citas de56

La comparación de diffs y búsquedas de los fragmentos modificados da:

| Punto |55|58|56 apéndice|
|---|---|---|---|
|M3 grados irreducibles|883–890 corregido|22853 ss. corregido|No copia de esa prueba|
|BL dominio e_cF(O)|2262–2264 corregido|24230–24232 corregido|8194–8195 conserva F(O) y antiguo(a): **desincronizado**|
|BL polinomio sólo γ_w|2270 y6575 corregido|Misma corrección propagada|8202 corregido|
|G4 generador topológico y explicación|3946–3950 corregido|25911–25915 corregido|8329 cambia generador, pero8331–8333 conserva norma inválida: **desincronizado**|
|Promedio sobre D|6117–6141 incorporado|67935 ss. incorporado|No copia de `pri:forms`|
|Definición errónea J_O∩J₁|6104 persiste|67922 persiste|No copia de esa prueba|

Por tanto el dictamen de fidelidad «45 copias(a)» del informe V1 **no se transfiere a V2**: al cambiar la fuente, dos copias ya no coinciden en puntos matemáticamente relevantes. En particular la copia BL de56 tiene un dominio más amplio que el nuevo teorema55. Esto no invalida por sí mismo los cálculos locales de cup products; sí impide certificar fidelidad de esa unión tal como está escrita.

## 5. Obligaciones restantes para el dictamen global

Dentro del cambio aquí revisado, quedan corregir la definición del nivel auxiliar y sincronizar las dos citas de56. El promedio integral que preserva e_c y sus constantes ya están reconstruidos; no queda una obligación abierta de álgebra de Higman una vez hecha esa corrección de definición.

No se revalida en este documento todo el material automorfo anterior de55 ni toda la teoría local56: sus verificaciones están en SELMER/HODGE y sólo cambian los puntos indicados. La deducción de regularidad55 continúa dependiendo de IM54, incluido su caso z=1 y, por esa rama, de exchange53. El `git diff` de53 está siendo revisado separadamente: este informe no declara que la corrección nueva de53 falle ni que tenga éxito. Los cierres locales de M3/G4, normas/Higman y cup products no bastan para deducir por sí solos GRH.

## 6. Suplemento explícito utilizable para el dictamen privado

La reparación de nivel no es sólo una sugerencia: con J_O^(1) definido por imponer la congruencia únicamente en los w_j, todas las acciones necesarias se conservan. En cada lugar elegido, H_w tiene matrices de reducción `[[I,B],[0,C]]`. Conjugarlas por diag(u,I) vuelve a dar matrices de esa forma (B cambia a u⁻¹B o uB según el sentido); por tanto G_c normaliza H. En Q estos representantes son1, así que preservan χ_O. En los w_j también son1, así que preservan la condición principal añadida. La acción ϱ y e_c están pues bien definidas en A(J_O^(1),χ_O).

El cociente en los w_j es Γ y conmuta con H/G_c por soportes disjuntos. Los operadores de Hecke utilizados están fuera de los lugares elegidos; los operadores locales auxiliares son soportados en w_j. Ambos preservan el tipo e_c. El promedio Ψ sobre D no necesita preservar H término a término: la suma conmuta con H y por ello preserva sus invariantes. A su vez conmuta con G_c y conserva los invariantes e_c dentro de ellos. La prueba completa de identidad, integralidad y divisibilidad entera de§1 se aplica literalmente a este espacio corregido.

**Dictamen suplementario:** la obligación de construir operadores de Higman que permanezcan en el tipo e_c, con la pérdida presupuestada N_ch, queda demostrada por este argumento y puede usarse en una deducción privada complementada. El escrito requiere la corrección de una definición y las dos sincronizaciones de citas. Estas erratas no deben contarse como obstrucciones matemáticas nuevas una vez especificado el suplemento. El suplemento no aporta la identidad exchange53 ni ningún otro input automorfo distinto.

## 7. Cierre de I/II/III → regularidad: cuantificadores y frontera de dependencia

Se releyeron para esta revisión55:430–715, las formulaciones G1–G5 y(L)/(C), y46:4898–4935. Se cotejaron los pendientes históricos de SELMER/HODGE con sus tandas finales: no se conservan como pendientes las obligaciones SCC, I2/I4/I5, scheme, sparse/any/data, odd/triangle, Fitting, norm o cadena local ya reconstruidas. El suplemento de nivel de§6 descarga el obstáculo restante de preservación e_c. El resultado de este apartado es una deducción **condicional a los inputs de otros papers identificados**, no una validación automática de toda la serie.

### Cuantificadores

Se fija primero un par (ℓ,ι). Para ese par, I produce los summands R_(j,q) y R_(ν,z). El conjunto es finito: j≤m; el espacio de formas a nivel fijo es de dimensión finita y tiene un número finito de sistemas q; hay un número finito de main pairs. II se aplica **simultáneamente a esa lista**, no una vez distinta para cada q. Produce un mismo τ, sus potencias1≤j≤m, ambos signos en los cocientes de valores L, y condiciones Selmer para cada summand. Los exponentes elegidos para los caracteres en II son mayores que m, por lo cual las potencias usadas siguen ramificadas en Q y forman twists m-fold. No hay intercambio ilegítimo entre «para cada q existe τ» y «existe τ para todo q».

En I y II no se impone ℓ grande: si ℓ es un primo elegido, M4/M5 usan el otro; ℓ=2 usa ζ_*²−1 unidad, no división por2; los módulos de coeficientes pueden ser ramificados. En los argumentos con «para todo O suficientemente grande», el dato algebraico finito se mete en un mismo O y se permite después ampliarlo: los límites de longitud están normalizados por [O:Z_ℓ], y no dependen de haber fijado un O mínimo. P56 aporta los tres regímenes de pérdida, incluidos los pequeños ℓ, no una invocación oculta del rango Fontaine–Laffaille.

III se aplica a cada Z_j(τ^j) y a cada línea de main pair. En el primer caso la igualdad de multiplicidades lleva el sistema de W_j al listado de W_m elegido **antes** de escoger τ. Las etiquetas buenas contienen la etiqueta primitiva necesaria sobre cada primo; no se requiere que todas sean irreducibles. La reescala no introduce raíz1, porque tal raíz original estaría en F_w y sería q₂-torsión, prohibida por bondad. En el caso de rango1 las etiquetas son X−1 antes de reescalar, y ω_w^j≠1 porque q₂>m. Se conservan n_W,t′ impares y los demás rangos de III.

Para cada ι se elige su τ y se define θ_ι=τ. **No se exige que todas las inmersiones sobre el mismo ℓ usen el mismo twist.** Sí se exige que su cota sea la misma, y las expresiones e′_ℓ,β_ℓ dependen solamente de ℓ y de los datos admisibles. R1 resulta de Q primo aℓ. Para R2, la valoración de la razón invertida es ≥−e′_ℓ, así su valor absoluto es ≤ℓ^(e′_ℓ); la suma Σe′_ℓlogℓ≤x₁ da el presupuesto de altura con multiplicador1. Para R3 se usa B_ℓ=(β_ℓ+v_ℓ(h₁))logℓ, independiente deι; ΣB_ℓ≤fa(log b)³/(mk) para **cada conjunto finito de primos**, exactamente como pide46. No se necesita sumar sobre todas las inmersiones, ni dividir la cota por su número.

### Dos entradas de55 releídas expresamente

**(L),55:3992–4086.** Sobre el vacío integral, la suma de subespacios U contenidos en el núcleo de una matriz de rangoρ da ∏_(l<n−ρ)(1−q^lX). La identidad n−ρ=t+(r−ρ) separa el factor de longitudt y deja el polinomio del espacio de rango r en q^tX. Los factores de caracteres son α^(dimU),β^(dimU), así la variable final es q^tαβ⁻¹X. Transferir al lift usa la acción adjunta en el grupo de origen y cambia la barra de w; conserva exactamente el polinomio completo, no sólo su último factor. Esta cuenta no usa exchange ni regularidad. Importa la acción del kernel y la equivariancia L2 de54, no el resultado de determinantes que se pretende demostrar.

**(C),55:4096–4165.** El par escalar(z,zI) actúa trivialmente en Hom y por el carácter de splitting en el kernel; por tanto ϱ(z)⁻¹k(g)=k(gz). Sumar sobre el grupo finito de clases da invariancia de L. La unitariedad y centralidad dan el adjunto; representantes integrales sobreℓ existen por parametrización racional/weak approximation del toro norm-one. Preservan todos los retículos para todas las inmersiones sobreℓ. Si y es falso lift y ortogonal a L, la suma Y=Σϱ(s_c)y tiene descenso cero, porque su emparejamiento con k(g) es ⟨y,L⟩. Así el promedio de un test form queda ortogonal a todos los falsos lifts necesarios. En la línea, la suma introduce exactamente h₁ y la valoración de su escalar Λ es≤β_ℓ, dando el coste β_ℓ+v_ℓ(h₁). No aparece otro factor h₁ ni una dependencia deι en el presupuesto. Si la línea es cero, la desigualdad es trivial.

### Frontera mínima de inputs

| Entrada | Estado dentro de esta rama |
|---|---|
|Datos admisibles/tamaños46; nivel principal libre|Se usan sus hipótesis y cotas exactas; esta rama demuestra regularidad **para todo dato admisible**. La construcción/existencia de tales datos y su aplicación analítica pertenece a46.|
|Galois automorfo, base change y compatibilidad local|G123/G45 y normalizaciones reconstruidos; cotejo primario Labesse/BLGGT y compatibilidad ℓ=p en SELMER§12. Son teoremas publicados usados con sus hipótesis, no resultados que esta auditoría re-demuestre.|
|Teoría clásica cohomológica|Reciprocidad/Chebotarev, dualidad local/global y comparación cristalina/Fontaine son entradas estándar expresas; sus nuevas combinaciones y estimaciones integrales se reconstruyeron en SELMER/HODGE. No queda un nuevo lema de cup products tomado como caja negra.|
|Representaciones finitas de Green y profundidad cero|Se usa la propiedad cuspidal del tipo primitivo y la parametrización de inercias; el paso local al generador y el rango mixto están reconstruidos. El cotejo documental completo de Green no queda atribuido a esta rama; no es una nueva cota pendiente de P55.|
|Multiplicidades46/51|Necesario en main(c). La cuenta de multiplicidades está en MULTIPLICIDADES y las entradas arquimedianas en THETA; la revisión V2 de spanning confirma reparación de uniformidad/FJ sin pérdida. Su certificación global corresponde al ensamblaje de esos ledgers, no sólo a la prueba de55.|
|Kernel49/54, gauges/Gram53|Necesarios para(L), integridad de IM y pairing. La identidad Gram y su escala están cerradas independientemente de exchange. Las propiedades de fase realmente usadas pueden recibir el suplemento de fase49; no se necesita asumir una fórmula fuerte distinta del comportamiento requerido.|
|IM54 para z≥2|Reconstruido en SELMER§13 junto con SW/Rallis del agente theta, incluidos ℓ=d, ambos embeddings y factores Euler.|
|IM1, z=1|La reducción a exchange53 está reconstruida con N=a=2,b=0,e=1,μ=c≥1, y cancelación de caracteres en la expansión. Requiere el exchange con su no anulación y constante independiente del twist. Ésta sigue siendo una dependencia matemática externa a esta rama; su revisión V2 se realiza en53.|

**Dentro de55/56 no queda, tras el suplemento de niveles, un paso nuevo sin reconstrucción que se pueda esconder bajo el antiguo «c por amplitud».** El cierre de la regularidad para el dictamen privado es condicional a los inputs enumerados, especialmente a exchange53 para IM1 y a las propiedades necesarias del kernel/fase y multiplicidades que revisan los otros agentes. Una falta de cotejo documental de prioridad o una fórmula de fase más fuerte que no se usa no debe convertirse en un impedimento matemático ficticio.

### Ausencia de ciclos en esta deducción

Los tamaños46 preceden a los summands I. La construcción de representaciones y retículos de55 precede a la estimación local56:56 recibe los pesos, los tipos de inercia y la clase de cociclos, no la conclusión de su propia cota de pérdida. Luego55 usa la cota para III y suma. II usa IM54, cuya rama z≥2 proviene de Rallis; z=1 recibe exchange53. No se usa la regularidad que se está construyendo para probar exchange, el kernel, la igualdad de multiplicidades ni IM. La regularidad copiada en el apéndice55 es el resultado a obtener, no una premisa de I/II/III. Con estas entradas ordenadas, la cadena55→56→55→46 no contiene un ciclo lógico en el segmento auditado.

## 8. Cotejo primario de Green completado

Se accedió al [texto original de Green1955, AMS](https://www.ams.org/tran/1955-080-02/S0002-9947-1955-0072878-2/S0002-9947-1955-0072878-2.pdf) mediante el texto indexado del PDF. Descarga y captura directa devolvieron403; no se afirma inspección visual del facsímil.

Se verificaron: p.403 define ∘ como inducción parabólica; pp.436–437 construyen el homomorfismo de funciones simétricas hacia el álgebra de caracteres; p.439, Lemma7.7 identifica simplexes de grado r con polinomios irreducibles; Theorems12–13 parametrizan los irreducibles por particiones sobre simplexes, con suma de grados ponderados igual al rango.

La aplicación51:4951–4973 conserva esas hipótesis. Un carácter de rango r_i<r no contiene el simplex de grado r. Multiplicar funciones simétricas dentro de cada simplex sólo cambia sus particiones, sin crear otro simplex. Por tanto una inducción desde rangos propios no contiene el carácter primario (g^(1)) de grado r. Por reciprocidad de Frobenius, sus invariantes bajo el radical unipotente de todo parabólico propio son cero: exactamente(G). Una etiqueta primitiva satisface irreducibilidad, condición suficiente; no se necesita que todas las etiquetas lo sean. **Dictamen(a) para esta importación clásica**; queda descargado el pendiente documental de Green mencionado en§7 y MULTIPLICIDADES.

## 9. Actualización de coordinación V2

El responsable theta comunicó, tras su revisión V2, cancelación completa de los caracteres en `product` y en su aplicación efectiva con (γ,γ), también en `vantop`. No encuentra una obligación nueva en kernel49/fase necesaria para IM; el factor fijo positivo |d₀|_f^j omitido en una expresión de κ₀ se absorbe en la constante existencial y no cambia la calibración posterior. El responsable spanning confirmó cierre de uniformidad sobre compactos y FJ, sin cambio de constantes, y el suplemento suficiente de fase49. Estas comprobaciones están en sus respectivos informes V2; se registran aquí como entradas de la revisión en equipo, no como una segunda auditoría independiente de53.

Con ellas, con el cierre primario Green de§8 y con el suplemento de nivel de§6, **esta rama no identifica una obligación matemática adicional pendiente que impida I/II/III→regularidad46**. El dictamen del conjunto todavía debe tomar del responsable53 el cierre completo de exchange y sus otras entradas: eliminar la obstrucción de caracteres es una parte concreta de ese cierre, no un argumento para inferirlo por sí solo. Las erratas de citas56 y definición de nivel siguen siendo reparaciones editoriales expresamente identificadas del escrito V2.
