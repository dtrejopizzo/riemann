# ROUND 003 — Obstrucción integral exacta para tres graduados de Tate

28/11/2026. Estado: teorema demostrado utilizando dualidad local, teoría de Kummer y equivalencia de Colmez–Fontaine. No se afirma prioridad: el mecanismo es la obstrucción cup clásica a extensiones mezcladas. El ejemplo da dos clases racionalmente independientes y cristalinas cuyo pegado integral, con los graduados y las clases fijados, falla antes de escalar.

## 1. El problema y dos convenciones de coste

Sea K/Qp una extensión finita. Sean ξ,η∈H¹(K,Zp(1)) clases cuya imagen racional pertenece a H¹_f(K,Qp(1)); en particular sirven clases de Kummer de unidades de O_K. Buscamos un módulo libre T de rango tres con acción continua de G_K, una bandera saturada y graduados identificados, de abajo hacia arriba, con Zp(2), Zp(1), Zp. Exigimos que las dos extensiones adyacentes, tras destorcer la inferior, tengan clases p^aξ y p^bη, y que T⊗Qp sea cristalino.

La palabra «cristalino integral» significa aquí exclusivamente una red estable en una representación racional cristalina. No se pide una estructura integral adicional de Breuil, Kisin o Fontaine–Laffaille.

Definimos coste total como el mínimo de a+b, con a,b≥0; y coste común como el mínimo c cuando a=b=c. Son problemas distintos: fijar clases y graduados evita trivializar el problema cambiando arbitrariamente sus identificaciones.

**Teorema K3.** Si ξ∪η tiene orden p^s en H²(K,Zp(2)), tomando s=0 para la clase cero, entonces

\[
 c_{\mathrm{total}}=s,\qquad c_{\mathrm{común}}=\lceil s/2\rceil.
\]

Más precisamente, el pegado cristalino integral existe con exponentes (a,b) si y sólo si a+b≥s.

## 2. Necesidad y suficiencia cohomológicas integrales

Denotemos χ el carácter ciclotómico. Elegimos cociclos x,y representantes de las clases adyacentes. En una base compatible con la bandera toda representación buscada puede escribirse

\[
\rho(g)=\begin{pmatrix}
\chi(g)^2&\chi(g)x(g)&z(g)\\
0&\chi(g)&y(g)\\
0&0&1
\end{pmatrix}.
\]

Multiplicar las matrices y comparar la entrada (1,3) muestra que

\[
(dz)(g,h)=-x(g)\chi(g)y(h)=-(x\cup y)(g,h),
\]

con el diferencial inhomogéneo para Zp(2). Por tanto existe una función continua integral z que completa la representación si y sólo si [x]∪[y]=0. La condición de continuidad forma parte de la cohomología continua; no se elige una solución abstracta sin topología.

Al escalar las aristas, el cup se multiplica por p^{a+b}. De aquí la condición exacta a+b≥s para existencia galoisiana integral. La matriz tiene determinante χ³, una unidad, y sus submódulos de bandera y cocientes son libres: no queda una condición de saturación oculta.

Aún falta demostrar que puede exigirse cristalinidad racional. La sola anulación de H²(K,Qp(2)) no bastaría para ese paso.

## 3. Existencia de una realización racional cristalina

Sea K0 el subcampo maximal no ramificado de K y σ su Frobenius. Consideremos D=K0e0⊕K0e1⊕K0e2, con φ(e_i)=p^{−i}e_i y N=0. Para A,B,C∈K ponemos en D_K:

\[
\mathrm{Fil}^0D_K=K(e_0+A e_1+C e_2),
\]
\[
\mathrm{Fil}^{-1}D_K=\mathrm{Fil}^0D_K+K(e_1+B e_2),
\qquad \mathrm{Fil}^{-2}D_K=D_K,
\]

con Fil¹=0. La bandera W1=K0e2⊂W2=K0e1⊕K0e2⊂D es estricta para las filtraciones inducidas y sus graduados son los objetos de Tate 2,1,0.

El cociente D/W1 tiene parámetro A; W2, tras destorcer, tiene parámetro B. Toda extensión cristalina racional entre dos Tate consecutivos posee esta forma: la extensión de los módulos φ se escinde de manera única, pues el operador de diferencia entre las dos pendientes es invertible (una potencia de σ es identidad y p no es unidad de valor absoluto uno). En ese desdoblamiento el único dato restante es el parámetro de la recta de filtración, que pertenece a K. Por tanto elegimos A y B para que las aristas sean las imágenes racionales prescritas. C es libre, por ejemplo cero.

Verifiquemos admisibilidad débil. Tenemos t_H(D)=−3=t_N(D). Para cualquier submódulo φ-estable D', intersectamos la bandera W. Sus graduados se inyectan, como espacios filtrados, en los respectivos graduados de Tate. Cada graduado no nulo tiene dimensión uno y peso de Hodge a lo sumo el peso de ese Tate. Sumando obtenemos t_H(D')≤t_N(D'). Es la prueba elemental de estabilidad de la admisibilidad débil por extensiones estrictas; no se supone que cualquier extensión galoisiana sea cristalina.

Por [Colmez–Fontaine, Construction des représentations p-adiques semi-stables](https://webusers.imj-prg.fr/~pierre.colmez/CF.pdf), D es admisible. Como N=0, la representación correspondiente es cristalina y realiza simultáneamente las dos aristas racionales.

## 4. Toda realización racional con esas aristas es cristalina

Fijemos representantes racionales x,y. Una realización cristalina del apartado anterior puede ponerse con estos representantes mediante cambios de base superiores que ajustan cobordes. Si z y z' son dos soluciones de la ecuación matricial con los mismos x,y, su diferencia es un cociclo con valores en Qp(2).

La identidad H¹(K,Qp(2))=H¹_f(K,Qp(2)) implica que toda extensión central que modifica esa diferencia es cristalina. Este hecho y la identificación de unidades con clases cristalinas de Tate 1 se encuentran en [Berger, On p-adic Galois representations, §16, p. 15](https://mahalex.net/teaching/seminars/cristalline/Berger%20On%20p-adic%20Galois%20representations.pdf).

Para ver explícitamente que la modificación conserva cristalinidad, sea V la realización de rango tres y E_z una extensión cristalina de Qp por Qp(2) correspondiente a la diferencia. Formamos V×_{Qp}E_z usando los mapas a la cima Qp y cocientamos por la antidiagonal de los dos fondos Qp(2). Es un subcociente de una suma de representaciones cristalinas y su entrada superior cambia por el cociclo deseado, con el signo ajustado en la antidiagonal. Sus aristas quedan fijas.

Así, la solución integral obtenida en §2 tiene racionalización cristalina. Esto demuestra la suficiencia del Teorema K3, y la necesidad ya estaba probada.

Finalmente, el orden p^s siempre es finito: por dualidad local, H²(K,Qp(2)) es dual de H⁰(K,Qp(−1))=0. En versión integral,

\[
H^2(K,\mathbf Z_p(2))^\vee\simeq
H^0(K,\mathbf Q_p/\mathbf Z_p(-1)),
\]

un grupo finito. La versión integral se obtiene también pasando al límite en la dualidad finita: los grupos H¹ con coeficientes finitos son finitos, de modo que no aparece una obstrucción lim¹. Referencia: [Milne, Arithmetic Duality Theorems, I §2](https://www.jmilne.org/math/Books/ADTnot.pdf).

## 5. Ejemplo explícito con p=3 e independencia racional

Sea K=Q3(ζ), donde ζ es una raíz cúbica primitiva de la unidad, y π=ζ−1. Normalizamos vπ(π)=1, así vπ(3)=2. Definimos

\[
\beta=1+\pi^2=1-3\zeta,\qquad
\gamma=1+\pi^3,\qquad
\alpha=\zeta\gamma^3.
\]

Los tres son unidades. Sean ξ=κ(α), η=κ(β), con κ la aplicación de Kummer integral.

### 5.1 El símbolo de Hilbert no es trivial

Módulo cubos, α tiene la misma clase que ζ. El elemento ζ tiene raíz cúbica ζ9, así que su extensión de Kummer es K(ζ9)/K. Calculamos exactamente

\[
N_{K/\mathbf Q_3}(\beta)
=(1-3\zeta)(1-3\zeta^2)=13\equiv4\pmod9.
\]

Por compatibilidad de reciprocidad local con la norma, la acción de β sobre ζ9 es la de 13 en la reciprocidad de Q3. Con la convención de Frobenius aritmético, los elementos unidad actúan por el inverso: 13^{-1}≡7 mod9. Por tanto ζ9 se envía a ζ9⁷, cuya razón con ζ9 es ζ²≠1. Si se invierte la convención, sale ζ en lugar de ζ²; la no trivialidad es independiente de ese signo. Véase [Milne, Class Field Theory, I, Example 3.13(b), p. 44](https://www.jmilne.org/math/CourseNotes/CFT.pdf).

El símbolo normo-residuo de (ζ,β), y por ello el cup de las reducciones módulo 3 de ξ y η, es no nulo. La identificación de μ3⊗μ3 con μ3 requiere elegir ζ; sólo se usa no anulación, independiente de esa elección. Por functorialidad de reducción de coeficientes, ξ∪η no puede ser cero integralmente.

### 5.2 No son dos copias de una sola clase racional

El logaritmo 3-ádico se anula en ζ. Para vπ(t)>1, el primer término de log(1+t) tiene valoración estrictamente menor que los demás; por tanto

\[
v_\pi(\log\beta)=2,\qquad
v_\pi(\log\gamma)=3,\qquad
v_\pi(\log\alpha)=5.
\]

La razón de los dos logaritmos tiene valoración impar 3. Ningún elemento no nulo de Q3 tiene valoración vπ impar. En consecuencia logα y logβ son linealmente independientes sobre Q3. Kummer y el logaritmo de unidades, tras tensorizar con Q3, identifican sus clases racionales con esos logaritmos; las imágenes de ξ y η son independientes y cristalinas.

La torsión de κ(ζ) sí importa integralmente: desaparece racionalmente, pero no en el cup. Multiplicar γ por un cubo permitió asegurar independencia racional sin borrar ese test integral. No se confunden independencia racional y reducción residual.

### 5.3 Orden y coste exactos

La imagen de χ en G_K es 1+3Z3. Los invariantes de Q3/Z3(−1) son exactamente su subgrupo de orden tres: χ−1 genera el ideal 3Z3. Por dualidad,

\[
H^2(K,\mathbf Z_3(2))\simeq\mathbf Z/3\mathbf Z.
\]

El cup no nulo tiene orden tres, o sea s=1. El Teorema K3 da

\[
c_{\mathrm{total}}=1,\qquad c_{\mathrm{común}}=1.
\]

Sin escalar no existe ninguna realización integral con esas clases y graduados, aunque cada arista sea cristalina y aunque exista una realización racional cristalina simultánea. Escalar una sola arista por 3 ya basta; escalar ambas por 3 también basta. Es una obstrucción real en un primo impar, no un fenómeno exclusivo de denominadores factoriales en p=2.

## 6. Qué queda para una frontera original

La matriz superior y la obstrucción cup son mecanismos clásicos. El ejemplo concreto y la formulación exacta de coste son útiles para auditar propuestas, pero no acreditan prioridad de publicación.

Para tres graduados consecutivos no hay aquí una obstrucción cristalina adicional a la binaria: el teorema elimina esa posible fuente de novedad. Una investigación posterior debe pasar a cuatro o más graduados, fijar todas las identidades y elecciones de extensiones intermedias, y preguntar si el coste mínimo excede el impuesto por los cups binarios. No se puede llamar «obstrucción de Massey» a cualquier exceso sin construir el producto, su dominio de definición y su indeterminación.

También sería distinto pedir redes con una estructura integral p-ádica prescrita: nuestro teorema no controla módulos de Kisin, bases de comparación ni constantes theta. Cualquier aplicación al paper 56 requiere cotejar sus hipótesis y su noción concreta de clase cristalina integral; no se declara aquí un contraejemplo a ese paper.
