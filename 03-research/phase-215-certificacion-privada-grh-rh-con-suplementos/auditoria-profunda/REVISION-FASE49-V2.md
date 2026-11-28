# Coeficiente δ_g de P49: consecuencias suficientes y alcance literal

Versión corregida revisada el 28-11-2026. P49 sólo cambió FJ; siguen las afirmaciones fuertes de fase en 5471–5473 y 5569–5572. Este suplemento no modifica el manuscrito.

## Dictamen

**(c) para la clasificación literal de la fase** como una raíz de unidad por UN valor de υ y el índice prescrito: no se certifica aquí esa fórmula más fuerte. **(a) para las dos consecuencias necesarias**, mediante la prueba suplementaria siguiente: el módulo en cada conjugado es exactamente I_g^(-1/2), y, si g es integral sobre l, δ_g es una unidad l-ádica. Estas consecuencias bastan para `pk:conj(i)` y `pk:std(S1)` y no necesitan clasificar la fase individual. No se ha encontrado una dependencia circular con Short Forms ni con auxcore.

Se toma como definición de los operadores la fórmula explícita P3/D1–D3 del paper (538–625), incluidas sus correcciones de carácter y de índice de Weil. La prueba no identifica un operador arbitrario que satisfaga sólo las relaciones de Heisenberg con el operador normalizado: esa distinción es esencial.

## Lema suficiente

Para la representación finita normalizada de P49 y un retículo autodual L, se escribe la expansión de la línea vacía

`ω(g)v_L = δ_g Σ_(r∈gL/(L∩gL)) ζ_r ρ°(r)v_L`,

con ζ_r raíces de unidad y los vectores de la suma ortonormales. Sea I_g el número de términos.

1. δ_g es algebraico y para toda σ∈Aut(C), `|σδ_g|²=1/I_g`.
2. Si g estabiliza el retículo local sobre l, entonces δ_g es unidad para toda inmersión C→C_l. Los representantes r pueden elegirse integrales sobre l.

La expansión y la igualdad de módulos de sus coordenadas son consecuencias de las relaciones de Heisenberg y la línea vacía (parte geométrica de W4). Lo que se prueba abajo es la aritmética del coeficiente común, que **no** se deduce de unitariedad compleja sola.

## Prueba del módulo de todo conjugado

### 1. Campo de coeficientes y conjugación

Sea A el campo generado por raíces de unidad, raíces cuadradas de racionales positivos y los valores de υ en ideles finitos. Cada valor de υ es algebraico y todos sus conjugados tienen módulo uno. En efecto, para un idele a se escoge h con `a^h=z u_f`, z∈E× y u_f unidad; la no ramificación de υ y su tipo infinito dan

`υ(a)^h=|N_(E/K)(z)|/N_(E/K)(z)`.

El denominador pertenece al cuadrático imaginario K y el numerador es la raíz cuadrada de su norma racional. Tanto para embeddings que fijan K como para los que lo conjugan, el cociente tiene módulo uno. Por tanto cada raíz υ(a) tiene todos sus conjugados de módulo uno. Esto sólo usa el carácter, clase ideal finita y su tipo infinito; no usa theta ni la conclusión que queremos demostrar.

Para cada generador a de A, `σ(bar a)=overline(σa)`: es inmediato para raíces de unidad y raíces cuadradas racionales; para υ(a), se usa `bar(υ(a))=υ(a)^(-1)` y el módulo uno de TODOS sus conjugados recién demostrado. Se extiende a todo A por las operaciones de campo.

### 2. Operadores aritméticos en Schrödinger

La normalización de Rao expresa los operadores mediante cambios lineales con factor raíz cuadrada del módulo, multiplicación por caracteres cuadráticos y Fourier parciales; respeta sumas ortogonales. Esto se cotejó en Lemma3.2, Theorem3.5 y Proposition3.7 del [artículo original de Rao](https://msp.org/pjm/1993/157-2/pjm-v157-n2-p09-p.pdf), especialmente pp.351–358. Los Haar autoduales sobre un cuerpo p-ádico dan volúmenes potencias de p y sus raíces cuadradas.

Aquí va el argumento aritmético adicional, no una inferencia de mera unitariedad. Para una cantidad finita de funciones de Schwartz–Bruhat y sus imágenes por esos operadores, se elige un subgrupo abierto común de constancia y un soporte compacto común. Todos los coeficientes e integrales que se necesitan son entonces **sumas finitas**. Las fases son raíces de unidad; los volúmenes y factores de normalización pertenecen a Q(p^(1/2)). Por ello todos los coeficientes están en A. Las correcciones P3 son un valor de υ por una potencia de un índice de Weil, que es raíz de unidad; siguen en A.

Las identidades de productos escalares de un número finito de esos vectores son identidades algebraicas finitas en A. Como σ conmuta con conjugación en A y fija los volúmenes racionales (el signo eventual de una raíz cuadrada no afecta su cuadrado), aplicar σ a la identidad de Gram conserva exactamente la identidad. Así los operadores conjugados preservan la norma en estos espacios de prueba. No se ha aplicado σ a una integral infinita, ni supuesto que todo operador complejo unitario sea unitario después de conjugar sus coeficientes.

### 3. Espacios no split y base vacía

En el espacio doblado se escogen polarizaciones simplécticas compatibles con la suma W⊕W⁻. El cambio de polarización se obtiene por las mismas generadoras aritméticas de Rao. D2 define, sin escalar adicional libre,

`ω_(W⊕W⁻)(g,1)=A_g⊗1`.

Los coeficientes de A_g se recuperan tomando en el segundo factor un indicador de norma uno: son coeficientes del operador doblado entre productos de indicadores. El razonamiento algebraico de Gram anterior se aplica a ellos y conserva la norma de A_g después de σ. Esto cubre el caso no split sin elegir una fase por unicidad abstracta.

La base de traslaciones de una línea vacía puede construirse aritméticamente: las ecuaciones de invariancia de Heisenberg en un cociente finito fijan los coeficientes no nulos salvo una constante común, y sus razones son raíces de unidad. Se elige uno igual a1 y se normaliza por la raíz cuadrada de la medida racional de su soporte. Los coeficientes de estos vectores también están en A. Al conjugar, siguen siendo ortonormales, porque su matriz de Gram es finita con entradas en A.

El vector ω(g)v_L tiene norma uno después de cualquier σ por2–3. Sus I_g coordenadas siguen siendo `σδ_g` por raíces de unidad. Por tanto

`1=Σ_r |σδ_g·σζ_r|²=I_g |σδ_g|²`.

Sólo un número finito de lugares contribuye al vector adélico, así que el mismo argumento da la afirmación global. El caso de un vacío elegido con otra fase común no cambia δ_g: esa fase aparece en ambos miembros de la expansión. La convención ρ° sólo multiplica las razones por raíces de unidad.

## Prueba de integralidad en l

Se fija una inmersión en C_l. En un lugar de característica residual p≠l, las generadoras de Rao y sus inversas preservan el módulo de funciones de Schwartz con valores en O_(C_l): las sustituciones preservan valores, las fases son raíces de unidad y los denominadores de Fourier y de volumen son potencias de p. También los normalizadores p^(k/2) son unidades l-ádicas. Los valores locales de υ apoyados fuera de l son unidades l-ádicas: en la relación de clase ideal anterior z es unidad sobre l, y lo son el numerador y denominador de υ(a)^h.

En un lugar sobre l, g estabiliza L; su acción en la línea vacía es un carácter suave del estabilizador compacto. El vector es suave, por lo que ese carácter tiene núcleo abierto, imagen finita y valor raíz de unidad. No se necesita una fórmula de Fourier con denominadores l en este caso.

Las bases vacías de lugares p≠l tienen normalizadores potencias de p y fases raíces de unidad, por lo que son bases integrales para este cálculo. El argumento de doblamiento utiliza cambios de polarización con denominadores potencias de p y se conserva. En consecuencia ω(g) y su inversa preservan el retículo integral relevante. El vector v_L es primitivo; su imagen también. Todas las coordenadas no nulas de la imagen difieren por raíces de unidad; si su coeficiente común tuviera valoración positiva, la imagen no sería primitiva. Por ello `v_l(δ_g)=0`.

Además `(gL/(L∩gL))_l=0` cuando g estabiliza L sobre l; se escogen representantes r cuya componente sobre l sea cero. Esto demuestra también la condición de integralidad de las traslaciones usadas en S1. El argumento cubre l=2: en los lugares p=2 se usa el estabilizador, y en los demás lugares los denominadores de Fourier son unidades 2-ádicas.

## Aplicaciones y ausencia de circularidad

- **P49:5470–5476 (`pk:conj`)** necesita sólo `|σδ_g|=I_g^(-1/2)` para comparar las normas del conmutador semilineal. El lema lo proporciona con igualdad exacta, sin una constante extra. La continuidad del carácter del conmutador y la sobreyectividad del operador semilineal fueron comprobadas por separado en THETA/CJ05a; no se reemplazan por Schur sin hipótesis.
- **P49:5567–5574 (`pk:std(S1)`)** necesita sólo que el coeficiente sea unidad en l y los representantes r sean integrales sobre l. La segunda parte del lema lo proporciona, sin exigir el idele específico det(u) de la fórmula fuerte.
- **Short Forms** usa S1 para transportar datos estándar y `pk:conj` para el módulo arquimediano exacto; ambas consecuencias están cubiertas. Las constantes CM no se alteran.
- **Auxcore53** hereda integralidad de los jets y cotas de todos sus conjugados por esas entradas49. La corrección suficiente de fase no añade factor de rango, índice o twist; N₀ y las cotas exp(x^99 b²), exp(2x^201 b²) permanecen iguales. Esto no decide el intercambio de caracteres53, revisado independientemente.

El orden lógico es: carácter υ y normalización explícita de Rao → aritmética de coeficientes/Gram → módulo conjugado e integralidad → pk:conj/S1 → Short Forms y sus aplicaciones. En ningún paso se presupone Short Forms, auxcore, GRH o la unitariedad Galois que se intenta establecer.

## Qué falta incorporar al texto

Para una prueba literalmente autosuficiente, sustituir las dos invocaciones de la fase fuerte por el lema suficiente y su prueba, o probar la fórmula fuerte por separado. **El suplemento cierra las consecuencias necesarias; no certifica aquella clasificación adicional ni afirma que ya esté escrita en el manuscrito corregido.** La atribución completa de la fórmula P3 a Kudla no se volvió a cotejar con una copia íntegra de su artículo: aquí se toma la fórmula P3 como la normalización explícita definida en P49, y se coteja directamente el componente Rao. Esa limitación bibliográfica no se oculta como verificación del original de Kudla.

## Control adicional solicitado: splitting clásico y vacío fijo

**Precisión de alcance que prima sobre una lectura incondicional del dictamen inicial:** el suplemento aritmético anterior demuestra las consecuencias de δ_g para los operadores explícitamente normalizados P3/D1–D3. Para usarlo como certificado de toda la cadena hay que verificar además que P3 sea el splitting clásico con esas convenciones. Definir β(g)r(g) no demuestra por sí solo la ley de representación. Esa identificación exacta queda **(c)** en esta revisión por el límite de fuentes especificado abajo; no se reemplaza por una afirmación de unitariedad.

### Fuentes primarias efectivamente consultadas

Se abrieron el [original de Pan2001](https://msp.org/pjm/2001/199-1/pjm-v199-n1-p10-p.pdf), §§3.2–3.4 y6.1, y las [notas de Kudla1996](https://www.math.utoronto.ca/skudla/castle.pdf). Pan compara el modelo de Schrödinger con el de retículo mediante un factor α y el splitting mediante β; el producto αβ es un carácter del estabilizador, no automáticamente uno. Sus hipótesis son característica residual impar. Las notas de1996 desarrollan el caso ortogonal/simpléctico y no proporcionan el cotejo explícito del caso unitario necesario aquí.

Se intentó el PDF oficial de Kudla1994 por DOI, enlace editorial y descarga directa; la respuesta fue la [página de suscripción](https://link.springer.com/article/10.1007/BF02773003), no el artículo completo. No se presenta ese original como leído. Pan§3.2 confirma el procedimiento de doblamiento de D2. Esto resuelve el fundamento de esa construcción condicionado al splitting del espacio split; no coteja por sí solo el factor exacto de P3.

### Los lugares sobre2 sí quedan cubiertos para los datos de la serie

K=Q(√−d) y d≡7(mod8). Luego −d≡1(mod8) es cuadrado en Q₂; para cada lugar v de E⁺ sobre2, el polinomio de √−d ya se descompone sobre E⁺_v. Puesto que E=E⁺(√−d), E⊗_(E⁺)E⁺_v≅E⁺_v×E⁺_v. Por tanto **todos los lugares sobre2 de estos datos son split**, y se aplica D3, no la parte de Pan que excluye2.

D3 es una representación por multiplicación y sustitución directa. En los retículos O_E-estables usados por la cadena, sus componentes son A⊕A^∨. Si g estabiliza el retículo, g_wA=A, por lo que |det g_w|=1; como υ_w es no ramificado, υ_w(det g_w)=1. El indicador de A queda fijo exactamente. La normalización a_wO_w en las primas donde α no es unidad no modifica este argumento: g_w preserva A y el indicador correspondiente. Así no hay una obligación dyádica residual para estos datos, aunque no se certifique aquí W4 para todo retículo simpléctico arbitrario que su formulación pueda permitir.

### Qué aporta Pan al vacío en lugares impares no split

Para un retículo hermitiano unimodular, el modelo de retículo autodual tiene vacío y el estabilizador actúa sobre esa línea por αβ. En Pan§3.3, la restricción a SU del carácter αβ es trivial cuando uno de los cocientes de retículos es cero, como ocurre en el caso unimodular. Basta comprobar un subgrupo que sobreyecte sobre el determinante: una línea ortogonal de norma unidad de la base unimodular y su U(1). La existencia de esa línea usa la extensión no ramificada y la característica impar, y una vez extraída se aplica inducción ortogonal.

El cálculo de rango1 puede comprobarse en Pan§6.1 sin declarar trivial un carácter por unitariedad. En notación de allí, t=x+δy tiene norma1 y el retículo autodual corresponde a paridad par de `ord(ψ₀)+ord(%)`. Si t−1 es unidad, α=1 y el carácter no ramificado χ vale1 en (t−1)δ. Si t≡1, la relación de norma implica `ord(t−1)=ord(y)` y `ord(x−1)=2ord(y)`. En la fórmula de α de§6.1, los símbolos de Hilbert de la extensión no ramificada y el índice de Weil se reducen a `(-1)^ord(y)` porque la paridad anterior es par. El factor β es `χ((t−1)δ)=(-1)^ord(y)`. Su producto es1. Los cambios de signo y el factor2 entre los caracteres aditivos considerados tienen valoración0 aquí, y no alteran este cálculo. El caso t=1 es inmediato.

Esto demuestra que **el splitting de Kudla leído en Pan fija exactamente el vacío unimodular**. La reducción de SU y la línea del determinante utiliza la compatibilidad por sumas ortogonales del modelo normalizado. No se deduce que cualquier splitting de la misma cubierta lo haga: torcer por un carácter del determinante puede cambiar el resultado.

### Obligación exacta restante para el certificado

Queda cotejar o probar la identidad de P3: para el espacio skew-hermitiano `jmath·〈,〉` y la línea hermitiana de norma1, el cociclo de Rao se cancela exactamente por

`β_Y(g)=υ(x(g)) γ_F(η∘RV)^(-j(g))`,

con `η(t)=ψ_K(t/2)`, `ψ_K(t)=ψ_k(2t)`, la definición de x(g) y el paso a acciones izquierdas del manuscrito. El teorema preciso invocado es Kudla1994, Theorem3.1 caso3₊, con (1.11)–(1.14); deben verificarse también las convenciones de RV y el índice de Weil, no sólo la existencia de algún splitting. La página de resumen editorial y el caso O/Sp de castle.pdf no bastan para ello. Pan confirma resultados compatibles y permite el chequeo de vacío anterior, pero no se usó como si reprodujera todas esas convenciones del teorema3.1.

**Estado actualizado:** la aritmética Galois/integral de δ_g y el cálculo del vacío en la normalización clásica están reconstruidos; la igualdad de esa normalización clásica con P3 sigue siendo un input clásico exacto no verificado íntegramente por esta auditoría. Si otro frente lo coteja, este suplemento descarga las consecuencias para SF/auxcore sin otra pérdida. Mientras tanto debe conservarse esta (c) concreta al emitir el dictamen global, y no describir la fase como cerrada incondicionalmente.
