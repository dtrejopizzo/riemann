# CONSTRUCTOR_001 — O1: prueba de clase, sin candidato positivo

2026-10-18. Constructor único. Estado: **PARTIAL / NO CANDIDATE**. El nodo y O1 siguen **OPEN**.
No se usa ninguna equivalencia externa de D. Matemática pura; sin experimento numérico.

## 1. Resultado y límite

No obtuve un núcleo con positividad aritmética propia. Sí obtuve un control exacto para una subclase de O1:

> **PROVED.** Una corrección integral compacta de la involución FE conserva infinitas direcciones negativas sobre cualquier subespacio cerrado de codimensión finita. En un intervalo acotado de alturas, esto sigue siendo visible sobre el ideal lineal de polinomios de Dirichlet generado por un peine aritmético fijo no nulo, incluso imponiendo finitísimas restricciones lineales continuas.

La clase es `J + C_b`, con `C_b` compacto autoadjunto; no la de todos los núcleos O1. El resultado **no exige** positividad ambiental al objeto buscado. Dice que esa subclase sólo puede servir si la positividad se afirma sobre un dominio aritmético bastante menor que los ideales lineales aquí considerados. No se prueba nada contra una intersección no lineal de Euler completo y FE, ni contra una compresión a PW_T.

La salida `corrección no compacta` tampoco produce signo: el ejemplo `C=I−J`, que da `J+C=I`, es una norma genérica y se descarta antes de intentar un enlace con el nodo.

## 2. Corpus check y razón escrita

Fuentes consultadas: las reglas del proyecto; README del índice de rutas (familias y entradas CELL_001, P1_BBSTAR, SPEC_005); archivo 06 (residuos R7 y tabla W₂); CELL_001 §§1,4,6,8; AUDIT_207_001 §§B.7–B.10; P1_BBSTAR_001 §§1–4; SPEC_SIGN_OBJECT_005 §§3–5; R185_005B §§1–3; Paper 47 `thm:sos`, `def:PD`; grid maestro (Sonin/compactos y BB*); crucigrama (Sonin, BR y W₂).

Búsqueda dirigida adicional en índice/grid/crucigrama: `compact`, `essential/esencial`, `Hilbert–Schmidt`, correcciones de J y densidad de polinomios de Dirichlet. El corpus ya contiene restos compactos de Sonin y barreras al intento de acotarlos. **No se reintenta Sonin ni se acota ninguno de esos restos.** Tampoco se construye un BB* nuevo.

**Razón nueva y alcance de esta comprobación.** CELL calcula la clase de multiplicadores más J y detecta que las proyecciones puras FE no contienen polinomios finitos. Aquí se pregunta por correcciones arbitrarias compactas *fuera* de esa álgebra: pueden mezclar dos alturas sin colapsar a un peso del producto mn. La prueba usa las infinitas direcciones −1 de J y compacidad, no Gonek, fase estacionaria, el símbolo del peine ni un margen del nodo. El resultado no aparece en las entradas identificadas; es un lema funcional elemental, no una nueva fuente de signo.

**Corrección importante sobre Gonek.** El Lema G lleva resto y régimen asintótico. No se usa como identidad exacta ni como clasificación de todos los núcleos de peso ½.

## 3. Puertas antes de construir

### 3.1 SOS y BB*

`thm:sos` excluye la identidad puntual `Σ|D_i|²=μ₀−S_T` junto a `m_T−μ₀≥0`. P1.A permite frecuencias reales. No excluye todo núcleo integral ni toda identidad abstracta de normas.

Nuestra familia de prueba `J+C_b` no tiene esa identidad puntual como hipótesis y no reserva una constante arquimediana. Por tanto **thm:sos no la excluye literalmente**. Esto no le concede positividad.

Una eventual identidad exacta `Q_T=U*KU`, con K positivo por una factorización, seguiría sujeta al colapso P1 §1: el trabajo entero estaría en construir `K^{1/2}U` sin usar Q_T. No se ha encontrado tal U ni se reclama haber evitado P1 en un enlace real. Si se permite una parte PD convolutiva libre, aplica la clase dual de `def:PD`, no nuestro teorema compacto.

### 3.2 Dos significados de W₂

El kernel de dos variables de P36-4 y el conjunto relajado W₂ de BR(M2) son objetos diferentes. Nuestro operador de alturas no es ninguno de ellos por definición.

Para aplicar BR habría que suministrar: tests admisibles K de tipo acotado; identidad `Z_K=A_K−Tail_K`; familia de restos convexa y la sentencia aritmética en la clase declarada. No se ha dado esa traducción para `J+C_b`. Por eso BR no se invoca para descartarlo ni para certificar una evasión. Tampoco se invoca ρ1‴: no se ha construido resto sin cotas inferiores ni suma de conos no cerrada.

Las paredes de paridad/Kronecker y correlación de pares anotadas para P36-4 no son demostraciones sobre cualquier kernel de alturas. Nuestro lema no las esquiva: responde otra pregunta y deja su posible aplicación al enlace pendiente.

## 4. La subclase de prueba: FE más núcleo regular

Para separar la altura de la ventana del nodo, uso A>0 para el recorte en altura y reservo T para el soporte en x. Sea

`H_A=L²([-A,A],dt)`, `χ_t=χ(½+it)`, `(Jf)(t)=χ_t f(−t)`.

Se usa únicamente `|χ_t|=1` y `χ_tχ_{−t}=1`. Entonces J es autoadjunto unitario. Los autoespacios V₊ y V₋ tienen dimensión infinita: se puede escoger libremente f sobre (0,A) y prolongar mediante `f(−t)=±χ_{−t}f(t)`.

Sea b un peine real. A cada b se permite asignar **cualquier** kernel hermitiano

`c_b(t,t′)∈L²([-A,A]²)`, `(C_bf)(t)=∫c_b(t,t′)f(t′)dt′`.

C_b es acotado compacto autoadjunto. El ensayo de operador es

`K_b=J+C_b`.

El kernel de K_b es distribucional: `χ_t δ(t+t′)+c_b(t,t′)`. La parte integral regular puede ser genuinamente de dos variables; la clase no exige `w(t+t′)`. **No afirmamos que sea el kernel regular final pedido por el encargo**: es una primera clase de reparación de la FE que se examina antes de buscar positividad.

### Lema 4.1 — La corrección no es localidad decorativa (PROVED)

El álgebra de multiplicadores y J sobre H_A no contiene compactos no nulos; por tanto, si C_b≠0, K_b queda fuera de esa álgebra sobre H_A.

**Prueba.** Identificar H_A con `L²((0,A);C²)` emparejando t y −t y absorbiendo las fases unitarias. Cada elemento del álgebra es multiplicación por una matriz medible 2×2 esencialmente acotada. Si tal operador B es no nulo, existen ε>0, un vector constante v entre una familia finita que genera C² y un conjunto E de medida positiva donde `|B(t)v|≥ε`. Partir E en infinitos conjuntos disjuntos de medida positiva y normalizar `1_Ej v`. Sus imágenes son ortogonales y de norma ≥ε, contradiciendo compacidad. El mismo argumento cubre la clausura en norma, pues sigue siendo multiplicación matricial. ∎

**Límite efectivo.** Esta afirmación se refiere a H_A, que no es PW_T. Tras otra restricción o cambio de representación hay que repetir el análisis. No se ha demostrado que la compresión de C_b al dominio del nodo quede fuera del álgebra efectiva; no se reclama ese paso.

### Teorema 4.2 — Una reparación compacta no da signo sobre un dominio grande (PROVED)

Sea C compacto autoadjunto en H_A. Para todo subespacio cerrado L⊂H_A de codimensión finita, la restricción de `J+C` a L tiene infinitas direcciones negativas. Más precisamente, para cada ε∈(0,1) hay un subespacio infinito-dimensional E⊂L∩V₋ donde

`⟨f,(J+C)f⟩≤−(1−ε)‖f‖²`.

**Prueba.** Por compacidad hay un operador de rango finito R con `‖C−R‖<ε`. El espacio `E=L∩V₋∩ker R` sigue teniendo dimensión infinita. Para f∈E: `Jf=−f`, `Rf=0`, y por ello la forma es `−‖f‖²+⟨f,(C−R)f⟩≤−(1−ε)‖f‖²`. ∎

Esto es una obstrucción exacta, no una cota sobre primos. No afirma que la corrección real deba ser compacta ni que el dominio aritmético deba tener codimensión finita.

## 5. Un dominio aritmético explícito donde el ensayo también falla

Para X>2 fijo, sea

`P_b(t)=Σ_{2≤n≤X} b(n)n^{−½−it}`,

y sea 𝒟 el espacio de todos los polinomios de Dirichlet finitos de coeficientes complejos libres. Defino el **ideal de prueba**

`𝕀_{b,X}={P_b D_a : D_a∈𝒟}`.

Los coeficientes de cada elemento son la convolución de Dirichlet de b truncado con a, con peso ½. Esto introduce la aritmética como generador fijo del dominio; no es la variedad de productos de Euler completos. No se identifica con ella.

### Lema 5.1 — Densidad (PROVED)

𝒟 es denso en H_A. Si P_b no es idénticamente cero, 𝕀_{b,X} también es denso.

**Prueba.** Si h es ortogonal a todas las funciones `n^{−it}`, su transformada entera `H(z)=∫_{−A}^A h(t)e^{itz}dt` satisface `|H(z)|≤C e^{A|Im z|}` y tiene ceros en `log n`, n≥1. Si H no fuera idénticamente cero, la fórmula de Jensen, centrada en un punto donde no se anula, daría O(r) ceros en discos de radio r/2: cada cero de ese disco contribuye al menos log2 en el disco de radio r y `log|H|≤O(r)`. Pero hay al menos `exp(r/3)` ceros `log n` en ese disco para r grande. Contradicción. Luego H=0 y h=0 por unicidad de Fourier.

P_b es analítico no nulo y sólo se anula en un conjunto de medida cero. Si h es ortogonal a `P_b𝒟`, entonces `overline(P_b)h` es ortogonal a 𝒟 (P_b acotado en el intervalo); por lo anterior es cero, y h=0 casi en todas partes. ∎

### Corolario 5.2 — Fracaso de la reparación sobre ese ideal (PROVED)

Si P_b≠0, la forma de J+C_b tiene un valor negativo sobre 𝕀_{b,X}. Lo mismo ocurre tras imponer cualquier número finito de restricciones lineales continuas a ese ideal.

**Prueba.** La forma es continua y el ideal es denso. Para restricciones `L:H_A→C^r`, la intersección `𝕀_{b,X}∩ker L` es densa en ker L: escoger en el ideal preimágenes de una base de `L(H_A)` y corregir una aproximación densa mediante esa familia finita. El Teorema 4.2 proporciona un vector negativo en ker L, que se aproxima conservando las restricciones. ∎

**Qué no prueba.** Esta densidad usa a libre. No dice que los coeficientes eulerianos completos sean densos, ni que su intersección con la FE sea grande. Tampoco convierte el dominio de tests de D en un ideal de polinomios. Sólo descarta un dominio explícito y natural que podría confundirse con una restricción aritmética suficiente.

## 6. Borrado interior y especificidad

Para un primo p, defino exactamente

`b^(p)(n)=0 si n=p^k (k≥1); b^(p)(n)=b(n) en otro caso`.

Si `p<e^{2T}`, la identidad completa `Σ_{d|n}Λ(d)=log n` falla para b=Λ^(p) ya en n=p: su lado izquierdo es 0 y el derecho log p. Es un separador exacto; no se le atribuye signo.

La clase anterior permite que c_b dependa arbitrariamente de esa identidad. Aun así, los Teoremas 4.2 y 5.2 valen tanto para Λ como para Λ^(p) siempre que el polinomio generador sea no nulo. **No obtenemos una positividad para Λ que se rompa al borrar:** el ensayo falla antes, ya para Λ. El caso extremo P_b=0 es un ideal nulo, no un éxito de especificidad.

En consecuencia no se intenta enlazar esta forma con Q_T. No se han controlado el complemento de N(T), el acoplamiento, los impares ni el sector polar. No hay afirmación sobre ventanas certificadas.

## 7. Cribado de salidas no compactas: ninguna se construye

| Ensayo | Por qué se considera | Puerta que no supera |
|---|---|---|
| `J+C_b`, C_b integral Hilbert–Schmidt | Corrección genuina de dos alturas fuera del álgebra ambiental | Teorema 4.2 en dominio grande y Cor. 5.2 en el ideal aritmético explícito; no-go sólo ahí |
| `J+(I−J)=I` | Corrección no compacta que elimina exactamente el sector negativo | Norma genérica, sin especificidad; no se propone como avance |
| `U*AU` con A≥0 independiente y U construido de b | No localidad por conjugación | La norma sola es heredada; una identidad específica de enlace podría fallar al borrar. Sin tal identidad no hay candidato. No se declara NO-GO de toda esa clase |
| Núcleo definido por identidad de divisores + FE pero sin ley de signo | El borrado interior rompe una hipótesis exacta | Sólo separador: las hipótesis no proporcionan positividad. No se anuncia un kernel inexistente |
| `P_T M_a P_T` presentado en coordenadas de alturas | Tiene fórmula de dos variables | Compresión de multiplicador sobre PW_T; no localidad decorativa. No se reintenta |

No encontré una razón nueva que habilite construir una de las salidas genéricas ya indexadas. Por tanto el resultado constructivo de esta ronda es **NO CANDIDATE**, no un objeto positivo parcial.

## 8. Residuo que deja esta comprobación

Para el ansatz J+C compacto, un dominio de positividad que sea subespacio lineal cerrado tendría que tener codimensión infinita; además, no puede contener uno de los ideales densos examinados. Para una variedad aritmética no lineal no se impone aquí una noción de codimensión. Otra posibilidad es cambiar el operador por una corrección no compacta y demostrar una positividad o un enlace específico. Son posibilidades de búsqueda, no motores demostrados.

Este lema no es una barrera absoluta de O1 y no recomienda abandonar O1. Evita un ensayo específico: mantener la signatura completa de J e intentar curarla con una corrección compacta mientras la aritmética sólo restringe un ideal denso o finitísimas condiciones lineales.

**Fila D: OPEN. O1: OPEN. Nuevo resultado: NO-GO PROVED exclusivamente para esa clase. Revisión hostil: AUDIT_001 §8, teoremas aceptados; precisiones editoriales incorporadas.**
