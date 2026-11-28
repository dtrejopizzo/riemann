# Dictamen especializado: papers 55 y 56

Fecha de revisión: 28 de noviembre de 2026. Textos: `04-papers/55-covolume-theorem-regular-families-of-twists/main.tex` (8200 líneas) y `04-papers/56-explicit-cup-exponents-local-galois-representations/main.tex` (8380 líneas), copia de trabajo local. Las referencias de línea se refieren a esos archivos, abreviados P55 y P56. No se leyeron 47 ni 48.

## Actualización: la auditoría profunda reemplaza los pendientes de este informe inicial

El cuerpo siguiente conserva la primera revisión como registro histórico. **No usar sus (c) de falta de lectura como dictamen vigente.** La reconstrucción posterior está en [HODGE](auditoria-profunda/HODGE.md) y [SELMER](auditoria-profunda/SELMER.md).

| Pregunta | Dictamen vigente y alcance |
|---|---|
| P56: cota local, todos ℓ y caso tame | **(a)** bajo las hipótesis impresas; HODGE §§1–6 reconstruye la cadena integral y cohomológica. |
| P56: NM | **(a)** como condición suficiente; **no es necesaria**, según el ejemplo de abajo. |
| P55: Selmer, Ribet módulo potencias, pérdida local y clases impares | **(a)** para las obligaciones reconstruidas en SELMER §§1–10,12–14, bajo sus inputs explícitos. No falta una irreducibilidad residual en Ribet. |
| P55: prueba literalmente escrita de todos los inputs | **(b)** en frases concretas de §6 y §11.1 de SELMER; no son contraejemplos al teorema principal. Hay correcciones locales de igual costo. |
| P55: base level y e_c | Discrepancia de formulación y obligación de preservación; SELMER §11.2 da reparación explícita con la misma cota. No se presenta esa reparación como texto ya escrito. |
| Suma sobre todos los primos | **(a)** como ensamblaje aritmético; SELMER §14. |

Los dictámenes relativos a los inputs de kernel, exchange y Rallis se leen junto a las auditorías de P49/P53/P54. Ninguno certifica por sí solo la deducción global de GRH.

## Registro de la primera revisión

**Resultado global: (c), no verificado en su totalidad.** Esta revisión no establece un contraejemplo a los teoremas principales de estos dos papers. Tampoco certifica sus pruebas completas. Sí comprueba varias reducciones, descarta una objeción demasiado general sobre irreducibilidad y delimita los resultados que faltaría verificar independientemente. Una reducción correcta suponiendo sus lemas no constituye un dictamen (a) sobre el teorema final.

Se distinguen abajo dos sentidos de «falta»: un argumento ausente del manuscrito y una comprobación que esta auditoría todavía no ha completado. En los puntos (c) que siguen, el manuscrito normalmente **sí contiene** pruebas de los lemas señalados; lo pendiente es validarlas, no su mera existencia. No se atribuye este dictamen a ninguno de los matemáticos mencionados por el usuario.

## Respuestas a las preguntas de P55

| Pregunta | Dictamen | Paso concreto pendiente o resultado comprobado |
|---|---|---|
| Existencia para todo primo, `pg:I`, `pg:II`, `pg:III` | **(c)** | `pg:I` depende de la transferencia y de la comprobación local en `pga:G123`/`pga:G45`; `pg:II` del descenso `pse:step` y de los polinomios de valores L `pse:stick`; `pg:III` de los módulos de trazas y la realización por operadores auxiliares. No se ha completado una comprobación de todas esas pruebas y de todos los teoremas externos con sus hipótesis. |
| Paso Selmer → congruencias módulo potencias de ℓ | **(c)** para el argumento completo; **(a)** para la observación de que la irreducibilidad requerida está explícita | `pri:ribet(1)` exige que la imagen del bloque genere toda la álgebra de matrices. No hay que añadir esta hipótesis como si estuviera omitida. Falta certificar toda la construcción de los determinantes de filas ligadas y su realización automorfa. |
| Pérdida local `pg:loss` | **(c)** | La reducción por dualidad es comprobable; el exponente numérico depende de P56, `pki:crys`, y del caso tame. |
| Clases impares `pg:odd` | **(c)** | No se ha certificado el aniquilador `pod:annih` ni el descenso de Euler que transforma aniquilación en longitud con la constante declarada. |
| Suma sobre todos los primos | **(a) como reducción aritmética condicionada a las cotas declaradas**; **(c)** como consecuencia incondicional de la serie | La suma del término local y el cambio de unidades de valoración a logaritmo están bien planteados y se comprueban abajo. La cota para `C_odd` y las cotas locales no quedan certificadas por esa suma. |

### 1. La irreducibilidad residual no es una hipótesis tácita

P55, definición `pg:def-summand`, líneas 563–585, exige en (M4) que para toda retícula estable suficientemente definida los `u(g)` generen `M_n(O)`. El texto explica su interpretación en las líneas 586–589. La versión exacta `pri:ribet`, líneas 2565–2588, vuelve a exigirla en (1), para el bloque `rho_pi`.

El lema `pg:burnside`, líneas 805–830, da un argumento pertinente y correcto bajo sus hipótesis:

1. Los autovalores de la inercia son distintos módulo el ideal maximal; las diferencias son unidades y los proyectores espectrales son integrales.
2. La retícula se descompone en sus líneas propias.
3. Frobenius permuta esas líneas en un ciclo completo.
4. Un subespacio estable después de cualquier extensión residual es suma de líneas propias y estable por ese ciclo: es cero o todo.
5. Burnside sobre el cuerpo residual y Nakayama sobre `O` dan la generación integral de la álgebra de matrices.
6. `phi^n` preserva cada línea y conmuta con el ciclo, por lo que es escalar.

Esta comprobación no usa que ℓ sea grande: usa que ℓ sea distinto de la característica residual del lugar auxiliar y que los autovalores sean incongruentes. La estrategia de dos primos de nivel para poder escoger el otro cuando ℓ coincide con uno aparece expresamente en `pg:rem-primes`, líneas 475–487. Queda por certificar que **todos** los sistemas automorfos que se usan tienen las etiquetas y tipos locales necesarios: eso remite a `pga:G123`, `pga:G45` y a la selección de etiquetas. No es correcto sustituir esa tarea por la afirmación «Ribet necesita irreducibilidad y aquí no se supone».

### 2. Qué se comprobó del argumento de twists

Los lemas sobre raíces de unidad `pg:roots1` y `pg:roots`, líneas 922–990, tienen un mecanismo coherente: se compara la valoración de evaluación con la valoración de Gauss; se cuenta la contribución de raíces del polinomio sobre círculos de radio `rho_h`; el promedio truncado por 1 produce un punto sin pérdida mayor que `delta`; se especializan sucesivamente las variables. En la reducción de potencias `1≤j≤m`, escoger la raíz de mayor valoración de `(1+Y)^j-(1+x)` garantiza `v(Y)≥v(x)/j`, y no presupone `j` primo a ℓ. Este aspecto sí cubre primos pequeños.

El lema `pg:minor`, líneas 1068–1100, explica por qué los menores máximos controlan la longitud de un kernel módulo `ℓ^M`. La fórmula `sum min(M,v(d_i))` y el paso al grupo con coeficientes `K/O` cuando la longitud es menor que `M` son correctos. El resto de la existencia de la especialización útil depende del descenso de grupos de Selmer: `pse:mirror` (1780–1840), `pse:step` (1872 y siguientes), y de `pse:stick` (2051 y siguientes). **No se ha verificado íntegramente esa dependencia.** En particular, no basta verificar la especialización de polinomios para concluir la cota Selmer: primero hay que demostrar que existe un punto donde los menores poseen la valoración requerida.

### 3. Pérdida local: reducción comprobada, exponente pendiente

P55 `pll:D2`, líneas 3314–3358, no se limita a citar una forma integral de Bloch–Kato: escribe una prueba por longitudes. Sus pasos son apropiados:

- La imagen de `H_f^1(T)` en `H^1(T/ℓ^m)` es `H_f^1(T)/ℓ^m`, porque la preimagen de un subespacio racional es saturada.
- Su longitud es `m(h_f-h_0)+len H^0(T/ℓ^m)`.
- Las dimensiones tangentes de una representación de Rham y de su dual de Tate suman `[F:Q_ℓ] rank(T)`.
- La característica de Euler local y la dualidad de Tate dan que las dos imágenes ortogonales tienen longitudes complementarias.

Esto sustenta `pll:dual` (3360–3394), sin convertir por sí solo una cota racional de Bloch–Kato en la cota integral nueva del paper.

También se comprueba el mecanismo de `pll:ribet`, líneas 3408–3446. Se toma `Y=⊕End(u_x)` con **multiplicación por la izquierda**, no con la acción por conjugación. Por eso `Y` es suma de copias de las representaciones originales. El submódulo generado por `(u_x(g)-1)_x` es estable, y las relaciones permiten definir el morfismo hacia `T/ℓ^M`. La exactitud racional de `D_cris` sobre las representaciones que se vuelven cristalinas sobre una extensión común muestra que el cociclo en ese submódulo es cristalino. La elección de la acción por la izquierda es esencial y está hecha correctamente.

Lo que no está certificado es la cota nueva de `pll:exponent`, líneas 3487–3507, tomada de P56. La clasificación final de `pg:loss` sigue siendo (c).

### 4. Clases impares y ℓ=2

`pg:odd` (1373–1380), `pri:odd` (2313–2327) y `pod:odd` (4382–4404) tienen la misma estructura: para `e≠0` se trata de cociclos antiinvariantes por conjugación compleja con condición local ciclótica, y para `e=0` de homomorfismos no ramificados en todas partes. La segunda formulación explicita `chi^e = Z_ℓ(-e)` y que el anillo de coeficientes contiene los valores de los caracteres de Dirichlet.

El manuscrito no aplica sin explicación un resultado de Euler systems válido sólo para ℓ impar. `pod:rem-two`, líneas 4406–4416, separa los primos `ℓ≤(N+t+3)^2`, usando aniquiladores y puntos detectores, de los mayores, donde aplica el descenso. Esto responde a la objeción de cobertura formal de ℓ=2, pero no prueba el resultado: deben verificarse `pod:annih` (4879 y siguientes), `pod:detect` (4511 y siguientes), y el descenso de las secciones posteriores. En esta revisión no se certifican esos tres pasos. No hay un contraejemplo establecido aquí.

### 5. La suma de pérdidas, con todas las unidades

P55 define, líneas 416–433,

`lambda_ℓ = v_ℓ((2b)! · (∏_{b-30h³<n≤b+30h³} n)^{h³})`,

`loc_ℓ = 4f·10^6 (m/k) (b v_ℓ(M)+lambda_ℓ)`.

Para cualquier conjunto finito de primos `T`, la fórmula del producto aplicada a **un entero positivo fijo** da

`Σ_T lambda_ℓ log ℓ ≤ log((2b)!) + 60 h^6 log(b+30h³) ≤ 3b log b`,

con las separaciones de tamaño de los datos. Asimismo `Σ_T b v_ℓ(M)log ℓ ≤ b log M ≤22b log b`. Por tanto el factor `4·10^6·(3+22)=10^8` de `pg:sums` (520–522) es correcto.

La contribución `2^{-ℓ}` es sumable, y los términos que son valoraciones de `N_ch`, `C_odd` y `h_1` se suman como logaritmos de esos enteros. Al final, la absorción del término local en el presupuesto reduce a

`2·10^8 m² ≤ x (log b)²`,

que se obtiene de `m²≤4x` y `(log b)²≥8·10^8` (P55, 525–533). No hay que sumar la cota uniforme individual sin conservar el soporte finito o la estructura factorial: esa estructura es precisamente lo que permite la suma.

Este cálculo es una verificación de la **reducción aritmética**, no de la existencia previa del entero `C_odd` con el tamaño exigido.

## Respuestas a las preguntas de P56

| Pregunta | Dictamen | Alcance |
|---|---|---|
| Exponente principal sin restricción FL, para todo ℓ | **(c)** | La deducción numérica de `pki:crys` a partir de sus proposiciones centrales se ha revisado; no se certifican todos los lemas de retículas, frames y caminatas de los que dependen. |
| NM: necesaria y suficiente | **(a)** para la identificación de su papel de hipótesis suficiente en la reducción y para su verificación aritmética en la aplicación; **(c)** para la proposición genérica completa | El paper no afirma un «si y sólo si». NM no es necesaria para que el defecto se anule; se da un ejemplo abajo. |
| Caso potencialmente cristalino tame | **(c)** | El paso de los exponentes y la especialización a los datos encajan; pendiente la certificación del tame killer `pkw:T3` y sus insumos. |
| Novedad | **(c)** | La forma fina de la cota es una candidata a contribución; no queda establecida prioridad ni validez por contraste bibliográfico limitado. |
| Consistencia con FL | **Compatible en los subcasos comprobados; (c) como comparación completa de categorías y condiciones locales** | La anulación cuando `lambda=0` concuerda con lo esperado; el propio P55 no usa FL como sustituto de su prueba integral. |

### 6. La afirmación principal es más restringida que el título abreviado

`pki:crys` (552–623) no dice que cualquier pareja de representaciones cristalinas de pesos arbitrarios tenga el exponente anunciado. Exige (S1)–(S4), ventanas opuestas, que las letras lean espesor, y pocos saltos bajos o el caso alternativo `U'⊆[-eta,0]`. En particular, «todo ℓ» no elimina las hipótesis geométricas sobre la distribución de pesos y embeddings.

La deducción distingue:

- `ℓ≤Q`: se usa `pki:sparse` con `J=floor(log_ℓ h³)`, radio bajo `2G`, `vartheta=2K`, `M=K`.
- `ℓ>Q`, `lambda≥h³`: se usa `pki:any`, y se obtienen `b+delta<Kℓ²` y `2(G+delta)<Kℓ`.
- `ℓ>Q`, `lambda<h³`: se usa `pki:generic` con `a=2(lambda+1)`.

En el último caso el resultado es directamente una **longitud de defecto**, no necesariamente un exponente que mate cada clase con esa misma constante dividida por el rango. P55 conserva expresamente esta distinción en `pll:exponent`. No se encontró aquí el intercambio ilícito «longitud por rango → exponente uniforme».

La comprobación completa aún debe cubrir `pkf:main` (2868), los teoremas de profundización `pke:I2` (4829), `pkh:I4` (5793) y el esquema `pkd:scheme` (6882), con sus dependencias. Son pruebas escritas, pero esta auditoría no ha certificado cada una. En particular, comprobar las desigualdades 570–623 sin comprobar esos resultados no verifica el teorema.

### 7. NM: qué significa y dónde se usa

La definición de NM en P56, 380–382, excluye múltiplos **no nulos** de ℓ en tres intervalos alrededor de `0`, `b_z` y `-b_z`, de radio `n`. El lema `pkc:free`, 6310–6321, utiliza exactamente esa exclusión para que los costes de los pasos de nivel cero sean cero en una carta no ramificada. El valor convencional de la función de coste en `y=0` es cero; no se está afirmando que la valoración ordinaria de 0 sea cero.

En la aplicación `lambda<h³`, líneas 600–607:

1. Si ℓ dividiera un entero en `(b-30h³,b+30h³]`, la potencia `h³` de ese factor forzaría `lambda≥h³`.
2. Con `a=2(lambda+1)` se tiene `n=6(a+eta+W)<13h³`.
3. Todo múltiplo no nulo de ℓ tiene valor absoluto al menos `ℓ>198G`, por lo que queda fuera del intervalo bajo y de los intervalos alrededor de `±(G+delta)`.
4. Los intervalos alrededor de `±(b+delta)` quedan dentro del intervalo factorial ampliado anterior, porque `delta+n<30h³`.

Así se comprueba NM en **ambas** clases de letras, gruesas y finas; no se presupone sin control para `G`.

NM no es necesaria para la conclusión de defecto cero. Un ejemplo de rango positivo: `F=Q_23`, `U=U'={0}`, `L=Z_23` trivial, `a=2`, `eta=1`, `W=0`, `b_z=20` en todas las letras. Aquí `e=f=1`, `ℓ≥5`, `eta≥1`, las dos ventanas contienen 0 y no hay saltos en `[-a,0)=[-2,0)`. Se cumplen `b+W+eta=21≤(23-3)·2=40` y `6(a+eta+W)=18<20`. NM falla porque `y=23` es no nulo, divisible por 23 y está a distancia 3 de 20. Así se satisfacen todas las otras hipótesis de `pki:generic(i)`. Las representaciones cristalinas con todos sus pesos cero son no ramificadas, y sus retículas también. Para cualquier emparejamiento equivarante módulo `23^m` entre esas retículas y `L`, escojamos un elemento de inercia `g` cuyo carácter ciclótomico vale `-1` módulo 23. La equivariancia da `(epsilon(g)-1)b_psi(y,l)=0`; el factor es una unidad, por lo que el emparejamiento hacia `Z/23^m(1)` es cero. En consecuencia el defecto aquí es cero, aunque falle NM. Este ejemplo refuta **la interpretación de NM como condición necesaria**, no el enunciado unilateral de `pki:generic`.

### 8. Caso tame y dual de Tate

P56 `pki:tame` (464–474) y su repetición `pkc:tame` (6629–6638) imponen `F=Q_ℓ`, `e_0=lcm_{1≤i≤r}(ℓ^i-1)`, polinomios uniformes `K(s)` y la pertenencia del dual a la clase con `K^{-1}(s)=K(s^{-1})`. La desigualdad `ℓ>b+6(W+eta)+r²(N+1)²+2` es parte de la hipótesis.

La deducción de 6643–6681 conserva los costes: `e_0≤ℓ^{r²}`, un polinomio de grado `≤N²` para el tensor dual, `kappa=r²(N+1)²`, y un coste total de caminata acotado por `3kappa+150(eta+W+1)`. La elección de `K^{-1}` es importante: aplicar el mismo polinomio directamente al dual sin invertir inercia sería incorrecto. El texto sí hace la inversión.

La aplicación a P55, `pkd:data(iv)`, 7224–7281, usa `N=(r+t)r=6r²`, `eta=h²+1`, `W=4t`, `delta_j=j Delta+h-2t` y `p_i≥b^{10}`. La cota exigida es menor que `2b`, por lo que la separación `p_i≥b^{10}` da el rango. También se explicita `L_c^*∈C(U',K^{-1})`; no se ha encontrado una omisión de esta hipótesis en la unión.

La parte no certificada es la prueba de `pkw:T3`, líneas 7753 y siguientes, que obtiene la aniquilación integral del cokernel a partir de inercia y del polinomio monico, junto con la preparación de las cartas tame. La aritmética del exponente, aun correcta condicionalmente, no sustituye esa prueba.

## Uniones: identidad del insumo frente a prueba del insumo

| Unión | Identidad/rango comprobados | Validez del insumo |
|---|---|---|
| P46 `au:regular` → P55 `pg:main` + `pg:sums` | Sí, en la reducción de P55 535–545. R1 proviene de (a); R2 usa el cociente inverso y `|·|_iota=ℓ^{-v}`; R3 usa `beta(ℓ)=(beta_ℓ+v_ℓ(h_1))log ℓ`. No se omite `log ℓ`. | (c), por las dependencias de `pg:main` y `pg:odd`. |
| P46 R3(i),(ii) → P55 `pg:def-den`, `pg:main(c),(d)` | Los falsos lifts se definen lugar por lugar y la ortogonalidad se pide para todos esos lugares. La contribución `h_1` está añadida a la cota de pares principales. P46 4895–4912 y P55 394–411, 438–458, 460–473. | Reducción coherente; falta certificar toda la construcción del operador. |
| P55 `pg:loss` → `pll:main` → `pll:exponent` | La primera cota es por defecto dual de `L_c^*`, no de `L_c`; el factor `[E_v:Q_ℓ]` y `x_main=1`, `x_e=t` están presentes. | (c), exponente procedente de P56. |
| P55 `pll:exponent(a–d)` → P56 prueba después de `pki:crys` | Coinciden los exponentes `10^4 floor(2lambda/Q)(floor(log_ℓ h³)+1)`, `10^4 floor(2lambda/Q)m`, el caso tame y la salvedad de longitud sin exponente. P55 3487–3507; P56 624–636. | (c) para los teoremas centrales. |
| P55 (M2) → P56 `pkd:data(i–iii)` | Comprobación algebraica correcta: el dual tiene saltos `-u-1`; `delta_j=jDelta+h-2t`, ancho `4t`, radio `h²+1` contienen los saltos y la cota de multiplicidad baja se conserva. | Condicional a que las representaciones de P55 satisfagan efectivamente (M2). |
| P55 tipos tame → P56 `pkd:data(iv)` → `pki:tame` | Coinciden `N=6r²`, los polinomios uniformes y la inversión `K^{-1}`. El rango en `p_i` basta. | (c), pendiente tame killer y origen automorfo de tipos. |
| P56 genérico → aplicación de `pki:crys(d)` | NM se deriva de `lambda<h³`, con control independiente de las letras de peso G. | (a) para la verificación de hipótesis y las desigualdades; (c) para toda la prueba de `pki:generic`. |
| P55 → P54, insumo (IM) para valores L | P55 señala explícitamente P54 §3.1, y `pse:stick` es el punto que lo usa. Esta revisión no certifica (IM) ni su normalización; pertenece a la auditoría especializada de P54. | (c). |

La dependencia P55↔P56 **no muestra por sí misma una circularidad lógica**: P56 importa definiciones, la cota elemental rango→defecto y propiedades de representaciones de P55; devuelve el exponente local. Para denunciar un ciclo hay que exhibir que alguno de esos insumos de P55 depende del exponente, no sólo que ambos papers se citan.

## Novedad y comparación bibliográfica limitada

La aportación candidata de P56 es la sensibilidad de una **cota integral de defecto de compatibilidad módulo ℓ^m** a la distribución de pesos y a la escasez de letras gruesas, en vez de sólo al mayor peso. P55 explica por qué le importa: quiere un ahorro proporcional a `m/k` después de sumar sobre lugares y primos. Esa conexión con un presupuesto global de denominadores es una idea identificable, aunque su validez matemática completa siga pendiente.

No es nuevo, por sí mismo, estudiar retículas cristalinas fuera del rango Fontaine–Laffaille ni representaciones de torsión para ℓ=2. Fuentes primarias pertinentes:

- Fontaine–Laffaille, *Construction de représentations p-adiques* (1982), [texto original](https://www.numdam.org/item/10.24033/asens.1437.pdf).
- Tong Liu, *Torsion p-adic Galois representations and a conjecture of Fontaine* (2007), [publicación](https://www.numdam.org/item/?id=ASENS_2007_4_40_4_633_0).
- Tong Liu, *A note on lattices in semi-stable representations*, [preprint](https://arxiv.org/abs/0709.4523).
- Caruso–Liu, *Some bounds for ramification of p^n-torsion semi-stable representations*, [preprint](https://arxiv.org/abs/0805.4227), [texto de los autores](https://www.math.purdue.edu/~tongliu/pub/bound2.pdf).
- *Torsion representations arising from (phi, G-hat)-modules*, [preprint](https://arxiv.org/abs/1202.1858), cuyo alcance incluye p=2.

Esas referencias no verifican automáticamente el exponente de este manuscrito. Tampoco la ausencia de una cota idéntica en una búsqueda limitada demuestra prioridad. La comparación exacta exige identificar categorías de torsión, mapas y condiciones locales, y luego derivar o excluir una cota equivalente. P55 `pll:FL`, 3467–3479, reconoce que no usa el camino Fontaine–Laffaille como sustituto. En el rango donde `lambda=0`, la conclusión de anulación concuerda con la expectativa de exactitud integral, sin que eso certifique los casos de pesos grandes.

## Alcance de los registros Lean

Se inspeccionó únicamente el README de `06-alpoge-verification`. Contiene declaraciones de compilación y de axiomas, y distingue expresamente compilación de revisión matemática. No se repitió la compilación, no se inspeccionó todo el archivo Lean ni se estableció una correspondencia declaración por declaración con P55/P56. Por tanto no se usa ese README para cambiar ninguno de los (c) anteriores a (a).

## Comprobaciones prioritarias para cerrar este dictamen

1. Certificar `pkw:T3`, `pke:I2`, `pkh:I4` y `pkd:scheme`, incluyendo integridad, constantes y compatibilidad de las retículas definidas por órdenes.
2. Certificar la transferencia automorfa y los tipos locales de `pga:G123`/`pga:G45`, contrastando las hipótesis exactas de los resultados citados.
3. Certificar `pse:step` y la entrada de P54 en `pse:stick`, no sólo el lema de especialización en raíces de unidad.
4. Certificar `pod:annih`, la cantidad de puntos detectores y el descenso de Euler con su dependencia en ℓ=2.
5. Sólo después de esas verificaciones, elevar la correcta contabilidad final de pérdidas a un dictamen sobre la existencia de familias regulares para todos los datos admisibles.
