# AUDIT_005 — Premisa de la ronda diagonal/mismo primo

2026-10-18. Revisión inicial y final de CONSTRUCTOR_005. No se construyeron candidatos paralelos. Objetivo íntegro D activo; ningún auxiliar lo completa.

**Veredicto final: PROVED la completación canónica SPD de −R_α sobre c_00 de divisores distintos d≥2 para 0<α<1/2; PROVED su herencia bajo borrados finitos en índices supervivientes. Enlace con Q_T OPEN.**

## 1. Corpus check y razón admisible

Releídos índice README (familias Gram, SOS, fase193 frenteK, INV_C/D/V, R183_006–008 y entradas209), 06_OPEN_RESIDUES (R1, R7–R9), P1_BBSTAR y los memos209. Lectura dirigida R183_006_GCD_FIBER_LAURENT_BRIDGE, incluida su corrección inicial; consultas grid/crucigrama e índice por diagonal, regularización, renormalización, laplaciano y dominancia.

Proximidades que no deben confundirse con la nueva cuenta:

- **R183_006–008:** un polo Gram positivo NO da positividad de su parte finita. La corrección documentada descubre un residuo de rango infinito. Aquí el objeto es distinto, pero la inferencia inválida sería la misma.
- **Fase193 frenteK / CA_K_001:** laplaciano con signo y Cheeger ya examinados. No presentar la elección de diagonal como mecanismo nuevo.
- **P1_BBSTAR / thm:sos:** Gram, raíz y cierre por suma de cuadrados están indexados. Clasificar como certificado no demuestra imposibilidad; tampoco construir una norma genérica identifica el nodo.
- **INV_C / formas sobre razones:** obtener una forma de pares no construye automáticamente una identidad con la forma de ventana.

**Razón nueva que admite esta ronda:** calcular la parte finita exacta del MISMO objeto B_y de CONSTRUCTOR_002–004, sobre diagonal y mismo primo, manteniendo el esquema de resta ya fijado; compararla con los cruces coprimos cuyo Mellin ordinario firmado acaba de probarse. No se reasigna diagonal para hacer una matriz favorable. No se reintenta Sonin ni el laplaciano de la matriz de Weil. Esta es una pregunta nueva interna al candidato específico, no una razón para reabrir familias cerradas.

## 2. Qué informa realmente el signo coprimo

**PROVED, álgebra elemental.** Conocer las entradas cruzadas −w<0 no determina las diagonales. En dimensión dos,

    [[a,−w],[−w,b]]≥0  iff  a≥0, b≥0, ab≥w².

El mismo w aparece en matrices positivas, indefinidas o negativas según a,b. Por tanto A_α(d,e)>0 para coprimos no identifica un valor diagonal ni su signo, ni da dominación gamma. La estructura de inversa positiva de ANTICORRELATION003 era para la covarianza NORMALIZADA o su Mellin positivo, no para una matriz desnormalizada renormalizada desconocida.

Asignar a cada diagonal la suma de pesos incidentes produciría un laplaciano PSD genérico. No hay todavía prueba de que esa diagonal coincida con el arquimediano/polar del nodo. Si se usa como control, etiquetarlo como identidad algebraica, no como enlace logrado.

## 3. Parte finita: orientación y esquema fijos

El objeto ya fijado para 0<α<1/2 es

    R_α(d,e)=∫_0^∞ y^(α−1)[B_y(d,e)−y^(−1/2)G₀(d,e)]dy,
    G₀=(gcd(d,e)−1)/(de).

Para coprimos, R_α=−A_α<0. Para diagonal o mismo primo G₀>0 y es indispensable la resta. No puede transferirse PSD desde ∫B en α>1/2 a R en α<1/2: se ha sustraído un kernel y el término explícito G₀/(α−1/2) tiene signo negativo. El esquema canónico de CONSTRUCTOR002 debe mantenerse.

Cambiar una función de corte en la sustracción cambia una parte finita por un múltiplo explícito de G₀. Si se modifica, hay que calcular y conservar ese cambio; no escogerlo para favorecer el signo. La unicidad requerida proviene de fijar la continuación Mellin original, no de una elección verbal de «renormalización natural».

La asintótica algebraica general, ya verificada en AUDIT004, es

    B_y=y^(−1/2)G₀−[(d−1)(e−1)/(de)]/(1−√y)+error exponencial.

El término constante regularizado es negativo para TODOS los d,e≥2; eso sólo describe y pequeño, no prueba el signo de su integral en toda escala.

## 4. Potencias del mismo primo y suma global

Antes de sumar todas las potencias de p, justificar expansión, suma del contratermino y error integrable. La suma formal de los G₀ locales es

    Σ_{j,k≥1}(p^min(j,k)−1)/p^(j+k)=p/(p−1)².

Se verifica mediante las probabilidades geométricas de divisibilidad 1/p^j y la identidad v_p=Σ_j1_{p^j|N}; o por dos series geométricas. Es un coeficiente positivo. Esto no justifica sin dominación intercambiar la suma de partes finitas.

Al sumar primos con pesos log²p, el coeficiente global Σ_p(log p)²p/(p−1)² diverge. No trasladar la regularización de cada primo a una suma global finita sin tratamiento adicional. Esto es un problema concreto de intercambio/límite, no un NO-GO para el candidato.

## 5. Mezcla euleriana y enlace

La identidad de covarianza total en σ>1 tiene diagonal explícita p^(−σ)/(1−p^(−σ))² y dos formas PSD. Su expresión escalar puede prolongarse por fórmulas; la identidad de PROBABILIDADES no sobrevive en σ=1/2. No deducir PSD de las formas prolongadas por mantener positiva esa diagonal escalar.

Para cualquier enlace con Q_T, el constructor debe definir un mapa de todos los tests del dominio declarado, conservar grado cuadrático en F, listar términos arquimedianos/polares y demostrar la identidad o dominación sin asignar signos por analogía. La diferencia entre índices de divisores y alturas Mellin sigue pendiente. Un resultado sobre R_α será positivo o negativo auxiliar según su prueba, no cierre D.

## 6. Veredicto inicial

Ronda admisible con la razón nueva de §1. No existe inferencia legítima del signo offdiagonal ya obtenido al signo de la diagonal ni al nodo. La oportunidad concreta es CALCULAR la diagonal/mismo-primo canónica y su interacción con los cruces, antes de proponer estructuras favorables. Revisión final pendiente de CONSTRUCTOR_005.

## 7. Verificación de la comparación de shells de un primo

Premisa comunicada por constructor005, verificada independientemente; revisión del memo final pendiente.

Sea p fijo y s_j(y)=τ(p^(2j)y)−τ(p^(2j+2)y), j≥0. Es la masa gaussiana no normalizada de v_p(|N|)=j. La referencia es g_j(y)=c(1−1/p)p^(−j), c=y^(−1/2). Poisson con z=p^(2j)y da

    s_j=c_z(1−1/p)+c_z[τ(1/z)−p^(−1)τ(1/(p²z))].

La concavidad puncturada implica q_u(p)=τ(p²u)/τ(u)<1/p para u>0 (cociente estrictamente decreciente desde su límite 1/p). Con u=1/(p²z), el corchete es negativo. Así 0<s_j<g_j para todo j,y.

Para un observable acotado f(j) y masas finitas positivas w_j,

    V_w(f)=min_{z∈ℂ}Σ_j w_j|f(j)−z|².

Por tanto, con m_g su media de referencia,

    V_s(f)≤Σ_j s_j|f(j)−m_g|²
          <Σ_j g_j|f(j)−m_g|²=V_g(f)

si f no es constante. La dirección de la comparación de mínimos es correcta; no se infiere por invertir una cota inferior. La estrictitud se sigue de g_j−s_j>0 para TODO j y algún valor f(j) distinto de m_g.

Para f(j)=Σ_{k≤j}a_k con un vector finito no nulo a sobre k≥1, f es acotado y no constante porque f(0)=0. Los dos lados son exactamente B_y[a] y cG₀[a] en el bloque de potencias de p. Esto prueba D_y=cG₀−B_y estrictamente positivo en cada bloque finito de un mismo primo. Su integral contra y^(α−1), 0<α<1/2, converge por las expansiones ya fijadas y es definida positiva: −R_α es SPD en cada bloque finito del mismo primo. **PROVED.** No determina el signo global entre varios primos.

## 8. Control hostil: la comparación puntual global es falsa

**PROVED para una clase precisa: D_y=cG₀−B_y sobre todos los indicadores de divisibilidad no es PSD para cada escala fija y>0.** Esto NO descarta la positividad del kernel integrado −R_α: integrar puede compensar escalas y no se ha justificado pasar al límite de la familia siguiente bajo Mellin.

Sea L_P el producto de todos los primos ≤P y f_P(n)=1_{gcd(|n|,L_P)=1}. Por inclusión-exclusión,

    f_P(n)=Σ_{d|L_P}μ(d)1_{d|n}.

El término d=1 es constante, así el mismo observable de varianza se realiza con coeficientes finitos a_d=μ(d), d|L_P,d>1. La forma G₀ sobre ese vector es la varianza de f_P bajo la medida uniforme de residuos módulo L_P:

    G₀[a]=δ_P(1−δ_P), δ_P=φ(L_P)/L_P=Π_{p≤P}(1−1/p)→0.

La convergencia δ_P→0 se obtiene, por ejemplo, de la divergencia armónica: δ_P^(−1) es el producto de Euler parcial y domina Σ_{n≤P}1/n.

Para cada n≠0, f_P(n)→1_{|n|=1}. Dominación por 1 da convergencia de medias y varianzas bajo la gaussiana puncturada fija. En consecuencia,

    B_y[a]→τ(y)Var_y(1_{|N|=1})>0,
    cG₀[a]→0.

Se sigue D_y[a]<0 para P suficientemente grande. Este resultado convive con: entradas individuales D_y(d,e)>0; bloques de UN primo SPD; y posible positividad del Mellin global, todavía no decidida. Impide usar el principio de shells uniprimo como comparación de masas conjunta sin verificar qué falla en los shells de varios primos.

Registrar el falsificador sólo con ese alcance puntual. No convertirlo en NO-GO de O1 ni de la diagonal integrada canónica.

## 9. Completación global integrada: verificación independiente

Prueba comunicada por constructor005 y verificada; memo final pendiente. **El contraejemplo puntual de §8 NO impide esta completación integrada.**

Para soporte finito de coeficientes a_d, d≥2, sea A(n)=Σ_da_d1_{d|n}. Las divisibilidades del soporte generan una partición FINITA en cilindros de valoraciones truncadas. Sea P_t la probabilidad sobre esa partición que hace independientes las valoraciones de cada primo involucrado, con colas P_t(v_p≥j)=p^(−tj), t>0. Es una probabilidad para CUALQUIER t>0 porque sólo involucra finitísimos primos; no es una ley zeta global normalizable cuando t≤1.

Escribir μ₁=E_{P₁}A=Σ_da_d/d y definir la medida firmada finita en esa partición

    ν_y=cP₁−τ(y)P_y, c=y^(−1/2).

Cada cilindro se representa por inclusión-exclusión finita entre eventos d|N. Para cada evento básico,

    ∫_0^∞y^(α−1)[c/d−τ(d²y)]dy=κ_α d^(−2α),
    κ_α=−Z_α=−2π^(−α)Γ(α)ζ(2α)>0,
    0<α<1/2.

La integral converge y el cambio de escala prueba el factor d^(−2α) exacto. La positividad de κ también se obtiene directamente de c−τ(y)>0 y la misma integral para d=1. Inclusión-exclusión da

    ∫ y^(α−1)ν_y(celda)dy=κ_α P_{2α}(celda).

No se integran probabilidades infinitas ni se suman todos los primos. La positividad surge después de integrar ν_y, que puede tener partes negativas en cada escala.

La identidad algebraica exacta es

    D_y[A]=cVar_{P₁}(A)−τ(y)Var_y(A)
           =ν_y(|A−μ₁|²)+τ(y)|E_yA−μ₁|².

Al integrar,

    −R_α[A]=κ_α E_{P_{2α}}|A−μ₁|²
          +∫_0^∞ y^(α−1)τ(y)|E_yA−μ₁|²dy ≥0.

Todos los pasos son legítimos: la primera función es constante en finitísimas celdas; el resto converge por E_yA−μ₁=O(√y) en cero y decaimiento de τ en infinito. Si a no es cero y d≥2 son distintos, A no es constante (N=1 y evaluación sucesiva en los índices ordenados). P_{2α} asigna masa positiva a todas las celdas, así el primer término es estrictamente positivo. **−R_α es definida positiva sobre todo vector finito no nulo de indicadores d≥2, no sólo bloques de un primo.**

Esto prueba una completación canónica de la diagonal en el OBJETO R ya fijado, sin asignarla a mano. No demuestra identidad con Q_T, no prueba acotación/realización en PW_T ni cierra D. Es un positivo auxiliar global en su dominio finito declarado.

## 10. Especificidad: la completación se hereda por borrado finito

**Verificado como filtro esencial, no como barrera de todos los enlaces.** Para un conjunto finito S de primos eliminados, definir

    τ_S(y)=Σ_{d|∏S}μ(d)τ(d²y),
    δ_S=Π_{p∈S}(1−1/p),
    κ_{α,S}=κ_α Π_{p∈S}(1−p^(−2α))>0.

τ_S es la masa gaussiana sobre n≠0 sin factores de S. La medida de referencia es cδ_SP₁^S, donde P_t^S fija v_p=0 para p∈S y mantiene las geométricas de parámetro p^(−t) para los otros finitísimos primos de la partición. La misma inclusión-exclusión, con la sustracción cδ_S, integra la medida firmada en κ_{α,S}P_{2α}^S. La misma identidad de varianza da PSD del kernel regularizado análogo para la medida borrada.

Si se incluyen indicadores divisibles por un primo eliminado, se anulan y la forma tiene radical; SPD sólo se mantiene en una familia independiente de indicadores supervivientes. No llamar SPD a toda la familia borrada.

Por tanto la positividad canónica de −R por sí sola NO es específica del Euler completo. Un eventual enlace con Q_T aún puede usar una identidad específica que falle tras el borrado; hay que demostrarla. La herencia del kernel no refuta todo enlace posible, pero obliga a localizar dónde entra esa información.

## 11. Veredicto final contra CONSTRUCTOR_005 completo

Leído el memo final §§0–10. **Todas las afirmaciones etiquetadas PROVED quedan aprobadas en su alcance.** Los experimentos previos no son necesarios para las demostraciones y no se usan como evidencia de signo una vez disponible (5).

Verificaciones específicas:

- ν se aplica a una álgebra generada por finitísimos indicadores. Todo producto X_dX_e es X_lcm y H=|A−μ₁|² tiene expansión FINITA incluyendo X₁. No hay problema de σ-aditividad global ni de una ley zeta divergente bajo s<1.
- El cambio de variable en (3), el factor 2 en Z, el signo −Z y la identidad de varianzas complejas están correctos. La estrictitud sobre divisores distintos d≥2 tiene prueba triangular válida; d=1 sería una constante y se excluye correctamente.
- En (6), H_s(d,e)=E_s[(X_d−1/d)(X_e−1/e)] se expande con exactamente los cuatro términos indicados. La separación H_s=G_s+v_sv_s* es correcta. Π es Gram real con integral convergente entrada a entrada. No se pretende identificar v_s con el polo del nodo.
- El control de bloque §6 usa la comparación de mínimos en la dirección correcta; la prueba global §5 no usa ni necesita la dominación puntual global falsa de §8 de esta auditoría.
- §7 recupera los cruces positivos: G_s=0 en coprimos; v_s(d)>0 y q_d−1/d<0 por concavidad, así ambas contribuciones son estrictamente positivas entrada a entrada. Esta observación no añade un enlace a Q_T.
- §10 limita correctamente las identidades de τ_P(k²y) a k coprimo con P. Su referencia de masa es δ_Pc y el factor Mellin es Z_αΠ_{p|P}(1−p^(−s)), NO δ_PZ_α. La diferencia entre estos dos factores está conservada. La ausencia de término constante en τ_P da cancelación exponencial en cero. El centro Haar para los índices supervivientes sigue siendo Σa_d/d. La afirmación SPD está restringida a esos índices, y los indicadores anulados no se cuentan como direcciones estrictas.

La completación PSD es una identidad exacta con R definido antes del argumento, de modo que no es una elección favorable de diagonal ni una raíz abstracta del nodo. A la vez, el test de borrado prueba que ese signo se hereda: no aporta aún la especificidad total. Ambas afirmaciones deben comunicarse juntas.

**Estado final:** auxiliar canónico resuelto, objetivo íntegro D sin resolver y activo. Lo que sigue es construir y verificar el mapa y el enlace a Q_T, incluidos dominio, colas, arquimediano, polar y todos los modos. Ninguna de esas obligaciones queda satisfecha por el resultado auxiliar.
