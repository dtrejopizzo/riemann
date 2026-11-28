> **V1: registro histórico, revisado en V2.** No aplicar sus objeciones de caracteres ni sus estados de propagación a los manuscritos corregidos sin consultar el [estado V2](../revision-v2/ESTADO.md). La cancelación especializada de caracteres corrige el impacto global atribuido en V1; se están consolidando los demás resultados.

# P53: inyectividad y determinante de la cadena

Revisión directa, 28-11-2026: P53 491–641, 850–894, 1083–1415, 1510–1600, 6647–6695, 6955–7010, 7554–7587, 8193–8275, 8857–8905. Se compararon los enunciados destino `au:inj` y `au:factor` en P46. Esta ficha separa el álgebra de la construcción automorfa del triángulo. No se extiende el cierre de una deducción condicional a los inputs no reconstruidos aquí.

## Dictamen por obligación

| Obligación | Dictamen | Precisión |
|---|---|---|
| `pc:tri-inj`, 566–590 | **(a)** | T1–T3 bastan; no se presupone σ≠0. La inyectividad implica después σ≠0 cuando V≠0. |
| `pc:tri-gram`, 592–639 | **(a)** | Fórmula completa, conjugación de σ y orden de los S_i comprobados; no requiere conmutatividad. |
| `pc:index`, 1346–1365 | **(a)** bajo la definición de nivel indicada | Se conserva la distinción parahórico/principal y se verifica c_Q y el exponente e_m. |
| `pc:heckeclosure`, `pc:detcompare` | **(a)** bajo convergencia y M⁺ | Cierre en dimensión finita y Newton; M⁺ debe incluir lugares no split. |
| Norma de un lift → cancelación de determinantes, 1370–1413 | **(a) condicional** | Los c_Q^m y dimensiones se cancelan exactamente; la potencia final es −d_T y la potencia de norma es semientera. |
| `au:inj`, como prueba automorfa escrita | **No certificada; ruta afectada por (b) en exchange53** | El álgebra no elimina la necesidad de T1. El fallo de product53 afecta la prueba del input T1. No es un contraejemplo a la inyectividad. |
| `au:factor`, como prueba automorfa escrita | **No certificada; misma ruta afectada**, además de inputs precisos abajo | Requiere T4 y M⁺, aparte de T1–T3. No basta corregir la fórmula final de determinantes. |

## 1. Inyectividad sin dividir por las constantes de cuadrados

Sea X_(i,n)=(w_(n−1)a_(i,n−1))⋯(w₀a_(i,0)). Con T1 se obtiene por inducción

`X_(i+1,n) d_(i,0) a_(i,0) = τ_(i,n) d_(i,n) X_(i,n+1)`,

`τ_(i,n)=w_(n+1)/(w₀w₁) · ∏_(l<n)σ_(i,l)`.

Para n=0 el factor es1/w₀. El paso usa w_n a_(i+1,n)d_(i,n)=σ_(i,n)w_(n+2)d_(i,n+1)a_(i,n+1), de modo que el factor añadido es σ_(i,n)w_(n+2)/w_(n+1), exactamente el requerido. Todos los índices permanecen en i+n+2≤m.

Si X_(i,n+1)j_i y=0, T3 proporciona y′ con j_(i+1)y′=d_(i,0)a_(i,0)j_i y. La identidad anterior y la inyectividad inductiva dan y′=0, luego y=0. **No se divide por τ.** Si después algún σ fuese0 y V≠0, la misma identidad un nivel más arriba contradice la inyectividad ya establecida. Así κ^sharp≠0 no se introduce como una hipótesis circular de exchange.

La preservación de j_(i+1)(A₀) en T3 se comprueba mediante equivariancia de la primera lift bajo J_M: aρ(u⁻¹)=cρ(g)a, |c|=1, y d=a*. Los factores c y bar c se cancelan en el pairing; da d a x fijo por J_M. La inyectividad de a hace inyectivo d a. Este argumento no presupone que toda lift posterior esté en el rango estable de Rallis.

## 2. Forma Gram: constantes y orden de operadores

El inner product del texto es conjugado-lineal en la primera variable. La ley T4 y T2 producen

`<z,a_(i,n)X_(i,n)j_i y> = (∏_(l<n)κ_(i,l)) <d_(i,n)z,X_(i+1,n)j_(i+1)y>`.

Al sustituir dX=τ⁻¹Xda en la primera variable aparece **barτ⁻¹**, no τ⁻¹. Por eso β_(i,n)=1/barσ_(i,n). Para x′ definido por j_(i+1)x′=d a j_i x, la primera norma da

`<x′,v>=(C_i/w₀)<x,S_i v>`.

No se necesita resolver x′ mediante S_i*, ni conmutar S_i con los otros operadores. La recurrencia conserva el orden S_iS_(i+1)⋯S_(m−1). Las constantes satisfacen

`K_(i,n+1)=(w₁w_n/w_(n+1)) C_i (∏_(l<n)κ_(i,l)β_(i,l)) K_(i+1,n)`.

Su producto telescópico es w₀w₁^m/w_m. Cada cuadrado i+n+2≤m aporta una sola vez κβ; la biyección (i,n)↦(i+1,i+n+2) recorre exactamente los pares1≤i′<j′≤m.

## 3. Del Gram a Z(1)/Z(θ)

La primera lift aporta C_i/#Mat_((r+t)×r)(R_θ) y S_i=Ral_(i+1)(θ^(i+1)). Su normalización fuente es w₀=#GL_r(R_θ). La comparación algebraic/Petersson por Schur aporta [K_m:J_θ] y una constante arquimediana independiente deθ. En Q_θ el nivel final es el parahórico con bloques r,t,…,t, cuyo radical tiene dimensión

`e_m=mrt+m(m−1)t²/2`.

Es incorrecto sustituirlo por el principal congruence level de cada etapa; el texto no hace esa sustitución. Con g_N=#GL_N(F_q), el factor local del índice y los pesos del triángulo es

`g_(r+mt)/(g_r g_t^m q^e_m) · g_r g_(r+t)^m/g_(r+mt) · q^(−(r+t)rm)`

`=q^(−e_m) [q^(rt) ∏_(a=t+1)^(t+r)(1−q^(−a))]^m`.

Es exactamente q^(−e_m)c_(Q,w)^m. Los factores en los lugares elegidos no dependen del twist y van a C_M.

Para una lift aislada el dato de bloques tiene norma cuadrada g_r q^(rt) y el índice target es g_(r+t)/(g_r g_t q^(rt)); junto con #Mat=q^((r+t)r) se obtiene el MISMO c_(Q,w), una sola vez. El cambio de convención hacia P54/P55 multiplica la forma target por el carácter unitario χ∘det; es una isometría para Gram, aunque sí cambia las raíces de Hecke. No se usa esa isometría para afirmar integralidad sin más.

El operador Ral es un límite absolutamente convergente de elementos de la Hecke algebra. En la imagen conjunta sobre dos espacios finito-dimensionales, la imagen lineal de esa álgebra es cerrada; por eso hay un único elemento h que realiza las dos acciones. M⁺ aplicado a h^k, incluido k=0, da dimensión y todos los power sums iguales; Newton da igualdad de determinantes. Se requiere el álgebra de **todos** los lugares fuera deM: igualdad sólo en split no basta para este paso.

Así, con d_j=d_T,

`Z(θ)=[Λ(θ)c_Q(θ)^m]^d_T ∏_j det Ral_j(θ^j)`,

`Z_j(θ^j)=[A_j c_Q(θ)]^d_T det Ral_j(θ^j)`.

La cancelación da Z(θ)/∏Z_j(θ^j)=[Λ(θ)/∏A_j]^d_T. Ambos determinantes son positivos por inyectividad. Por tanto el lado derecho coincide con el módulo elevado a d_T; no se infiere de ello que Λ mismo sea positivo cuando d_T es par. La normalización porθ=1 elimina todas las constantes independientes y produce

`Z(1)/Z(θ)=[(Nm Q_θ)^(e/2) ∏_(1≤i<j≤m)ρ_ij(θ)]^(−d_T) ∏_(j=1)^m Z_j(1)/Z_j(θ^j)`.

No queda una raíz d_T-ésima ambigua ni un cambio de signo en e: e se define por |Λ(θ)/Λ(1)|. El caso d_T=0 se separa antes, de acuerdo con el determinante vacío.

## 4. Rangos del exchange y de los twists

Para el cuadrado(i,n), W=G_(i,n+1)⊕G_(i+1,n+1) tiene N=2(r+(n+1)t), A rango r+(n+2)t y A′ rango r+nt. Por ello e=t. La identidad de números de signos se verifica entrada por entrada en las tres regiones a≤i, i<a≤i+n+1 y a≥i+n+2 de la fórmula de stems. q≤2r y t=5r dan2q+2≤N; Δ=2r⁸ y los tamaños admisibles dan N≤2(n+1)Δ. Para el cuadrado invertido los targets tienen igual rango, e=0, y las mismas desigualdades deN,q; sólo entonces se usa L_*(…,0)=1.

El carácter del cuadrado es (ν_(n+1)θ^(n+1))⁻¹, de peso(n+1)Δ. Puesto que i+n+2≤m, el exponente n+1 está en1,…,m−1. Las potencias θ^j conservan Q por la definición de m-fold twist, y las partes tame elegidas tienen orden>2m. Los ratios ρ_ij tienen exactamente t factores con z=1,…,t, exponente j−i≤m−1 y peso(j−i)Δ≤4b; por Δ≥t son pares críticos. La constante de exchange da |c|²=C M^(ft²)(Nm Q)^t²∏|L|², de donde |β|² es un norm power porρ_ij², con constante independiente deθ.

En T4, el ensamblaje impreso da κ_(i,n)=c_n η κ_rev/(γ c_(n+1)). Con M_n=r+nt y |η|=1, la contribución norm de las tres constantes es

`−M_nM_(n+1)+M_(n+1)M_(n+2)−t(t+2M_n)=t²`.

Es un entero; κ_rev tiene módulo constante porque el exchange invertido tiene e=0. Este control no requiere que κ tenga módulo exactamente1: la definición sólo exige módulo1 **hasta potencias de la norma**.

## 5. Inputs que esta deducción no demuestra

**Estado histórico de la primera tanda:** la sección6 posterior descarga H/Hc/F; las obligaciones que allí se cierran no permanecen pendientes. Exchange sigue afectado.

La prueba automorfa `pc:tri` remite a obligaciones distintas del álgebra anterior:

1. **T1:** `ptr:square` combina exchange con multiplicidad uno archimedeana. Exchange sigue afectado por `pcu:product` (ERROR-53-CARACTERES y PLANO-53). La multiplicidad uno (H), `ptq:H`7554, usa `ptq:howe` y las propiedades(a)–(d) del proyector `ptq:P`. Se inspeccionó la deducción deH, pero no se reconstruye aquí toda la eliminación polinómica que prueba esas propiedades. Ésta es una obligación concreta, no cubierta por la corrección del álgebra del triángulo.
2. **T4:** `ptv:adjoint`8193–8240 se reconstruye condicionalmente desde RS, reversión y Fourier. RS8857 aplica otro exchange, ahora e=0, y exige multiplicidad uno con los grupos intercambiados (`ptw:Hc`, `ptw:revedge`). La fórmula final de potencias no prueba esas entradas ni subsana exchange.
3. **Primera lift:** `pc:first` usa `pc:rallis`, serie cercana a1 y la positividad arquimediana `ptv:arch`8244. Se comprobaron las sustituciones de nivel, datum sharp y caracteres. La positividad pasa por `ptq:F` para las primeras parejas; no se da aquí una nueva prueba de ese teorema. La reconstrucción SW01 de THETA para la lift compacta de P54 no autoriza por sí sola todo caso no compacto de esta primera fila.
4. **M⁺:** se importa de51; su auditoría es MULTIPLICIDADES. No se obtiene de la mera igualdad de rango ni de formas locales finitamente isométricas.

No hay círculo algebraico en demostrar primero la inyectividad y deducir después κ^sharp≠0. Tampoco hay un círculo en obtener la factorización desde los determinantes de lifts aisladas, pues sus normas se prueban antes mediante Rallis. No se afirma una ausencia de ciclos en todas las pruebas transitivas deH/Hc/F que esta ficha deja individualizadas.

## 6. Actualización: descarga de F, H y Hc

Se leyeron íntegramente 7094–7587 y 8347–8838, además de `ptr:Z`7033–7083; se cotejaron nuevamente las polarizaciones de49:1711–1750. **Los pendientes H/Hc/F de §5 quedan reemplazados por la reconstrucción siguiente**, bajo los inputs de series discretas y crecimiento ya individualizados en THETA/MULTIPLICIDADES. La prueba de RS continúa siendo condicional al exchange defectuoso; no se la declara demostrada por cerrar estos otros inputs.

### F: coeficientes positivos y no anulación del primer factor

**(a) para `ptq:coef`, `ptq:vac` y `ptq:F` bajo la acción de Weil indicada.** La covariancia de Heisenberg, separada en partes lineal y antilineal en w, da las dos fórmulas de ladder con el factorη_i correcto. La matriz C(u)=u_++⊕bar(u_--) es invertible para u∈U(η). Cuando el polinomio es armónico por columnas, los términos de signo opuesto desaparecen; invertir el bloque de C* da el coeficiente bar(A_ij). La inducción de Euler nP=Σz_j∂_jP conserva exactamente las condiciones armónicas y produce

`<Q,ω(u)P>=c_u<L_(C(u)⁻¹)Q,P>`.

La no anulación de c_u no se presupone: si fuese0, se anularían todos los coeficientes entre polinomios de signo+ y signo−. Las series exponenciales de Heisenberg del vacío convergen en norma porque ||A^n1||≤M^n√(n!). Así los coeficientes también se anulan entre sus traslaciones en W_+ y W_−. El bloque invertible(u⁻¹)_-- implica W_++u⁻¹W_−=W; la irreducibilidad de Heisenberg fuerza ω(u)⁻¹1=0, contradicción.

Para w=expX positivo, detw=1. Con JwJ=w⁻¹ y el vacío eigenvector deJ, c(exp(tX)) es real; continuidad y no anulación lo hacen positivo. C(u) y A=C(u)⁻¹ son hermitianos positivos. Escribir A=BB* convierte el coeficiente en c_u||L_(B*)P||²>0. La norma no es sólo no negativa: P≠0 y L_(B*) invertible.

En `ptr:Z`, dos promedios compactos por Schur dan exactamente d_Λ⁻¹, mientras el coeficiente de la serie discreta se expresa con denominador positivo m_(−μ)(u⁻¹zu). El resultado es

`bar A(κz)=d_Λ⁻¹∫_K <Φ,σ(u⁻¹zu)Φ>/m_(−μ)(u⁻¹zu) du >0`.

La integral total es finita por e_λ∈L¹, y Z_∞=∏d_λ⁻¹<Φ,PΦ>>0. Este paso depende de la fórmula Flensted–Jensen en la normalización auditada en la rama de spanning; la errata de traslación de aquella prueba requiere su reparación allí registrada. No requiere exchange ni `pcu:product` ni el teorema de multiplicidades global.

### H: proyector y eliminación de polinomios

**(a) para la deducción con los inputs de series discretas especificados.** La integración por partes usa derivadas L¹ de e_λ y conjugación real de gl_n: bar(E_ba)=−E_ab para signos iguales; por eso P E_ba=0 y P E_aa=Λ_aP. La imagen del proyector pertenece al isotypic H_λ por la rigidez peso/Casimir; ese input está reconstruido en THETA AR01–AR03 con Vogan–Zuckerman. La auto-adjunción permite matar Pσ(y)Q cuando el K-tipo deQ está fuera del cono positivo; no hace falta que P sea la proyección a TODO el isotypic.

El contenido que se usa de D4 es que los otros K-tipos difieren deΛ por suma de raíces positivas: el cono de la hipótesis `ptq:P(c)` incluye todas ellas. La versión más fuerte impresa con sólo raíces no compactas no se necesita para esta inferencia. La fuente primaria alternativa [Atiyah–Schmid, Theorem8.5, p.42](https://www.math.utah.edu/~ptrapa/math-library/schmid/atiyah-schmid.pdf), cotejada en THETA AR01, cubre el contenido utilizado.

Para D5 se descargó y leyó [Harish-Chandra, *Discrete series for semisimple Lie groups II*, §8, Theorem1, p.18](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6013-11511_2006_Article_BF02392813.pdf). El original exige finitud bajo el álgebra generada por el centro envolvente y el álgebra compacta; se cumple para e_λ por infinitesimal character y K-finitud. Da f*α=f con α suave de soporte compacto. Aplicarlo a f(g⁻¹), seguido de inversión y unimodularidad, da β*f=f como se utiliza. Por ello existe β₀ que fija PΦ bajo el grupo opuesto. No se deduce ese smoothing sólo de aproximar la identidad.

En Howe, el complemento N de G∩D_j es finito-dimensional. Los operadores compactos y sus adjuntos lo preservan; se escoge un highest vector de columnas. Las hipótesis(iv),(v) imponen exactamente el peso de filas y matan raising. Las Laplacianas de columnas bajan dos grados y Fischer las anula: su adjunto multiplicador está enG. Para las de filas, `ptq:tensor` es una inducción finita porλ_b−λ_a; los términos del conmutador tienen diferencia estrictamente menor. Si el peso desplazado queda fuera del cono, Fischer aplica; si queda dentro, λ_a>λ_b, y las polarizaciones de49 con el signo deξ eliminan una derivada de cada término. Se obtiene un pre-joint harmonic, proporcional aΦ por unicidad, incompatible conN⊥G. La diferenciación de la función suavizante conserva soporte compacto y da estabilidad por el álgebra opuesta, completando H. La igualdad se transporta a F_s por convergencia Bochner, no por una supuesta continuidad puntual en Hilbert.

### Hc: columnas no emparejadas y reversión

**(a) para Hc y la deducción revedge bajo los inputs indicados.** La inversión de filas/columnas cambiaη en−η. La hilera B de columnas no emparejadas no se ignora: w′_c=0, y polarización con ambos signos elimina todas sus variables. Para las columnas emparejadas, w′_(c(r))=−w_r y ξ′_(c(r))=−ξ_r dan el signo requerido. En la unicidad por Taylor en x₀, cada variable posible tiene un campo polarizador cuyo único coeficiente no nulo en x₀ apunta a esa variable; los casos diagonal, comparación menor y comparación mayor son exhaustivos. Así Hc no invoca sin justificación la simetría de una situación con distinto número de filas y columnas.

La reversión A_∞ es antilineal y antisimpléctica. La unicidad de la estructura compleja positiva que conmuta conK×K′ se comprueba bloque a bloque: el conmutante real de cada bloque Hom(S_±,T_±) esC, y la positividad escoge un solo signo. Resulta φJ=−J′φ. Las combinaciones ∂_y±i∂_(Jy) transportan por A_∞ creadores a creadores y aniquiladores a aniquiladores; por ello vacío→vacío y grado≤d→grado≤d, también inversamente.

`ptw:W7` calcula el carácter por la cobertura metapléctica: la conjugación antilineal cambia d enbar d, y d⁻²=det(g)^(−N′)det(h)^N. La ausencia de otro carácter continuo de Mp se sigue de conexión y álgebra de Lie perfecta. La forma global deW7 ya restringe el carácter a potencias deυ; por ello calcular esos exponentes en infinito basta, sin introducir un carácter finito residual arbitrario. La ley de flip cancela luego esos exponentes y da λ_S=λ_T=1.

Aplicar A_∞ aP′ requiere conjugar e_T y cambiar x↦x⁻¹; da exactamenteP^rev. Aplicarlo al smoothingHc conjuga β_Q, de modo queα_Q=barβ_Q. Los tipos de las lifts invertidas se obtienen conjugando el kernel y la forma: e_T→e_S ybar e_S→bar e_T, como se exige en RS. La deducción de RS sigue usando exchangee=0, cuyo defecto no se elimina con esta reconstrucción.

**Dependencias restantes:** no queda pendiente H/Hc/F por falta de recorrido de estas pruebas. Quedan sus entradas explícitas de modelos y series discretas, tratadas en las otras ramas, y el fallo estructural de exchange. No se introduce una circularidad nueva: F se demuestra antes de la positividad del primer lift; H/Hc usan rigidez y smoothing, no inyectividad de la cadena ni su determinante.
