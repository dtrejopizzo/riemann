# 104_12 — M5: convolución Möbius–divisor y obstrucción del adjunto positivo

**Estado:** se obtiene la convolución firmada exacta que M5 pedía, pero la desigualdad
resultante es exactamente el gate de primera diferencia, no una cota nueva. El intento
adicional de convertir la inversión Möbius en una factorización de Gram positiva se
descarta en el poset divisor mínimo \(\{1,p\}\). La razón estructural es que la
inversión de Dirichlet es holomorfa, mientras que un cuadrado de Hilbert introduce el
adjunto y, con él, cocientes \(n/m\).

Este documento profundiza la Sección 7 de `104_11`; no repite el stop-gate del kernel
`max`. No se prueba A1 ni RH.

## 1. Prerregistro y falsificadores

M5 puede usar:

1. \(\Lambda=\mu*\log\) en el álgebra de convolución de Dirichlet;
2. convergencia absoluta para \(a=1+\varepsilon>1\);
3. las fórmulas exactas de adición y generación de Laguerre;
4. el emparejamiento del polo con el término primo antes de
   \(\varepsilon\downarrow0\).

No puede inferir un signo de:

* los coeficientes de Möbius por separado;
* una norma de cada factor por separado;
* la simetría funcional sin los pesos reales de von Mangoldt;
* una métrica construida después de asumir la positividad buscada.

Los falsificadores son:

* **nivel de convolución relajado:** un solo factor o un movimiento de masa produce una
  respuesta Laguerre con ambos signos;
* **nivel espectral relajado:** el cuarteto
  \(8-8\cosh(n\alpha)\cos(n\theta)\);
* **nivel de factorización positiva:** el poset divisor \(\{1,p\}\), tratado en la
  Sección 5.

## 2. Teorema de convolución de grado

Sea \(a=1+\varepsilon>1\). Defínanse

\[
 M_j(a)=\sum_{d\ge1}{\mu(d)\over d^a}L_j(\log d),
 \qquad
 B_k(a)=\sum_{m\ge1}{\log m\over m^a}L_k^{(-1)}(\log m).
\tag{1}
\]

Las dos series convergen absolutamente. La fórmula de adición

\[
 L_n(x+y)=\sum_{j=0}^nL_j(x)L_{n-j}^{(-1)}(y)
\tag{2}
\]

y la identidad \(\Lambda=\mu*\log\) dan

\[
 \boxed{
 P_n(a):=\sum_{r\ge2}{\Lambda(r)\over r^a}L_n(\log r)
 =\sum_{j=0}^nM_j(a)B_{n-j}(a).}
\tag{3}
\]

La prueba es una reagrupación absolutamente convergente:

\[
 \begin{aligned}
 P_n(a)
 &=\sum_{dm\ge1}{\mu(d)\log m\over (dm)^a}
                   L_n(\log d+\log m)\\
 &=\sum_{j=0}^n
   \left(\sum_d{\mu(d)\over d^a}L_j(\log d)\right)
   \left(\sum_m{\log m\over m^a}L_{n-j}^{(-1)}(\log m)\right).
 \end{aligned}
\]

Con \(t=z/(1-z)\), las funciones generatrices son las siguientes. Se entienden
inicialmente en una vecindad de \(z=0\) donde \(\Re(a+t)>1\), y por tanto como
igualdades de gérmenes analíticos en \(z=0\). No se afirma convergencia ni
ausencia de singularidades en todo \(|z|<1\): al continuar,
\(1/\zeta(a+t)\) puede encontrar ceros de \(\zeta\).

\[
 \boxed{
 \sum_{j\ge0}M_j(a)z^j={1\over1-z}{1\over\zeta(a+t)},
 \qquad
 \sum_{k\ge0}B_k(a)z^k=-\zeta'(a+t).}
\tag{4}
\]

Por tanto

\[
 \sum_{n\ge0}P_n(a)z^n
 ={1\over1-z}\left(-{\zeta'\over\zeta}(a+t)\right).
\tag{5}
\]

La importancia de (3) no es una positividad inexistente: es que mantiene la
cancelación entre todos los grados \(j+(n-j)=n\) antes de estimar.

## 3. Emparejamiento exacto con el polo

El término continuo correspondiente es

\[
 J_{n,\varepsilon}
 =\int_1^\infty x^{-1-\varepsilon}L_n(\log x)\,dx
 ={(\varepsilon-1)^n\over\varepsilon^{n+1}}.
\tag{6}
\]

Su generatriz es

\[
 \sum_{n\ge0}J_{n,\varepsilon}z^n
 ={1\over1-z}{1\over\varepsilon+t}.
\tag{7}
\]

Así, el costo regulado de `103_67` es

\[
 \boxed{
 C_{n,\varepsilon}
 =\sum_{j=0}^nM_j(1+\varepsilon)B_{n-j}(1+\varepsilon)
 -J_{n,\varepsilon}.}
\tag{8}
\]

Los dos términos de (8) no tienen límite separado cuando
\(\varepsilon\downarrow0\). La forma que preserva automáticamente la colisión es

\[
 F_\varepsilon(z)
 =(\varepsilon+t)\zeta(1+\varepsilon+t).
\tag{9}
\]

Desde (9) hasta (12), todas las series y derivadas se interpretan igualmente
como gérmenes analíticos en \(z=0\), dentro de una vecindad donde
\(\Re(1+\varepsilon+t)>1\). Ninguna de estas fórmulas presupone una
continuación libre de ceros hasta \(|z|=1\).

Como

\[
 -{d\over dt}\log\{(\varepsilon+t)\zeta(1+\varepsilon+t)\}
 =- {1\over\varepsilon+t}
   -{\zeta'\over\zeta}(1+\varepsilon+t),
\]

y \(dt/dz=(1-z)^{-2}\), se obtiene

\[
 \boxed{
 \sum_{n\ge0}C_{n,\varepsilon}z^n
 =-(1-z)F_\varepsilon(z)^{-1}F_\varepsilon'(z).}
\tag{10}
\]

Si

\[
 F_\varepsilon(z)=\sum_{k\ge0}f_kz^k,
 \qquad F_\varepsilon(z)^{-1}=\sum_{j\ge0}g_jz^j,
\]

y

\[
 h_n=\sum_{j=0}^ng_j(n-j+1)f_{n-j+1},
\tag{11}
\]

entonces

\[
 C_{0,\varepsilon}=-h_0,
 \qquad
 \boxed{C_{n,\varepsilon}=h_{n-1}-h_n\quad(n\ge1).}
\tag{12}
\]

Ésta es la versión normalizada y finita en el polo de la convolución firmada de
grado.

## 4. Comparación exacta con los antecedentes internos

### 4.1 E70.11

E70.11 establece en el álgebra del semigrupo multiplicativo

\[
 Z^{-1}\delta Z=\sum_{r\ge2}\Lambda(r)e_r.
\tag{13}
\]

Las ecuaciones (3)--(5) son exactamente el pullback de (13) por la transformada
Laguerre y el mapa \(s=a+z/(1-z)\):

| E70.11 | 104_12 |
|---|---|
| inverso \(Z^{-1}\) | coeficientes \(M_j(a)\) |
| derivada \(\delta Z\) | coeficientes \(B_k(a)\) |
| producto de Dirichlet | convolución en el grado (3) |
| conexión \(Z^{-1}\delta Z\) | derivada logarítmica (10) |

Por tanto (3) es una identidad útil y más concreta para A1, pero no es una fuente
independiente de signo respecto de E70.11.

### 4.2 E70.12

Si \({\cal A}=F^{-1}F'\), entonces

\[
 {\cal A}'+{\cal A}^2=F^{-1}F''.
\tag{14}
\]

Tras deshacer el cambio \(s=1+\varepsilon+t\), (14) es la identidad de Riccati

\[
 \Lambda\log+\Lambda*\Lambda=\mu*\log^2
\tag{15}
\]

de E70.12. La composición con Cayley agrega factores de cadena, no un término
Gamma ni un signo. Usar (14) como desigualdad sin un input adicional sería citar
como lema el objetivo Euler–Gamma que E70.12 dejó abierto.

### 4.3 103_71

La desigualdad de Cauchy

\[
 \left|\sum_{j=0}^nM_jB_{n-j}\right|
 \le
 \left(\sum_{j=0}^n|M_j|^2\right)^{1/2}
 \left(\sum_{j=0}^n|B_{n-j}|^2\right)^{1/2}
\tag{16}
\]

es exactamente la separación de normas descartada en 103_71. El factor positivo
ya tiene tamaño exponencial en un lóbulo central; (16) exigiría una compensación
exponencial en la norma de Möbius y elimina los signos relativos que (3) preserva.

Conclusión: M5 solo puede avanzar estimando (3), (8) o (10) **como una única
convolución firmada**.

## 5. Nueva prueba de viabilidad: ¿puede Möbius ser el adjunto?

La factorización holomorfa

\[
 Z^{-1}\delta Z
 =Z^{-1/2}(\delta Z)Z^{-1/2}
\tag{17}
\]

parece una congruencia. Para convertirla en un cuadrado o una forma de Gram
positiva, el inverso holomorfo tendría que comportarse como el adjunto en alguna
métrica positiva. Esto falla algebraicamente.

Sea \({\cal D}\) un conjunto divisor-finito, ordenado por divisibilidad, y sea

\[
 (Z_{\cal D})_{d,n}=\mathbf1_{d\mid n}
\tag{18}
\]

su matriz zeta. Su inversa es la matriz de Möbius \(M_{\cal D}=Z_{\cal D}^{-1}\).

**Teorema 1 (obstrucción unipotente).** Si \({\cal D}\) contiene una relación de
divisibilidad no trivial, no existe una matriz hermitiana positiva definida \(G\)
tal que

\[
 M_{\cal D}=Z_{\cal D}^{\dagger_G}
 :=G^{-1}Z_{\cal D}^*G.
\tag{19}
\]

**Prueba.** La igualdad (19) implicaría

\[
 Z_{\cal D}^{\dagger_G}Z_{\cal D}=I,
\]

es decir, \(Z_{\cal D}\) sería unitaria para el producto interno positivo dado por
\(G\). Entonces \(G^{1/2}Z_{\cal D}G^{-1/2}\) sería una matriz unitaria ordinaria,
y en particular diagonalizable. Pero \(Z_{\cal D}\) es unipotente triangular y,
si la divisibilidad no es trivial, tiene una parte de Jordan no nula. No es
diagonalizable. Contradicción. \(\square\)

El falsificador mínimo es \({\cal D}=\{1,p\}\):

\[
 Z=\begin{pmatrix}1&1\\0&1\end{pmatrix},
 \qquad
 M=\begin{pmatrix}1&-1\\0&1\end{pmatrix}.
\tag{20}
\]

Si \(G=\begin{pmatrix}a&b\\\bar b&c\end{pmatrix}>0\) y \(Z^*GZ=G\), la entrada
\((1,2)\) da \(a+b=b\), luego \(a=0\), imposible para \(G>0\).

Este teorema separa dos multiplicaciones que no deben confundirse:

* \(MZ=I\) usa convolución de Dirichlet y productos \(mn\);
* un cuadrado de Hilbert usa \(Z^*Z\) y genera cocientes \(n/m\).

La inversión Möbius cancela la primera geometría, no la segunda. Si se reemplaza el
inverso por el adjunto real, reaparece el peine de cocientes y la masa diagonal de
E70.10. Si se fuerza (19) mediante una métrica indefinida, se pierde precisamente la
positividad que se quería demostrar.

Por tanto la factorización adicional más natural de M5 queda descartada antes de
una búsqueda extensa.

## 6. Segunda variable probada: filtración por factores de Euler

Otra posibilidad es introducir un cutoff de primos \(Y\) y activar los factores de
Euler uno por uno. El incremento correspondiente a un primo \(p\) es

\[
 P_{n,p}(a)=\log p\sum_{k\ge1}p^{-ak}L_n(k\log p).
\tag{21}
\]

La respuesta (21) cambia de signo al variar el grado y la posición del factor
respecto de los ceros de Laguerre. Por tanto la filtración \(Y\) no es monótona en
el funcional buscado. Éste es exactamente el falsificador de cutoff primo de
`103_19` y el movimiento de masa de `103_59`; agregar la variable \(Y\) no crea una
desigualdad nueva.

## 7. La desigualdad que queda no es todavía un mecanismo

La condición requerida por el ataque M1/M5 sería

\[
 \limsup_{\varepsilon\downarrow0}C_{n,\varepsilon}
 \le {1\over2}\Delta A_n.
\tag{22}
\]

Por la identidad exacta de `103_59`,

\[
 \Delta D_n
 =\Delta A_n-2\lim_{\varepsilon\downarrow0}C_{n,\varepsilon},
\tag{23}
\]

(22) es exactamente \(\Delta D_n\ge0\). Es un blanco suficiente más fuerte que
A1, no una consecuencia de (3) ni de (10). Enunciar

\[
 \text{«la convolución completa (8) satisface (22)»}
\]

sin un lema adicional sería renombrar el objetivo.

En la extensión a todos los vectores Hardy, la desigualdad de conexión
Euler–Gamma es AHM, como ya registra E70.11. En la familia Laguerre actual, (22) es
su diagonal de primera diferencia. Ninguna de las dos versiones se obtiene de la
identidad de conexión.

El cuarteto off-line muestra el nivel exacto de fuerza: cualquier derivación que
use solo ecuación funcional y conjugación viola (22) en subsecuencias. Un teorema
válido debe volver a usar cuantitativamente los pesos reales
\(\Lambda(p^k)=\log p\).

## 8. Única factorización M5 que no fue refutada

Después de los Teoremas 1 y (21), una continuación M5 no puede ser:

* una congruencia ordinaria con \(Z^{-1/2}\);
* un cuadrado de Hilbert del inverso de Möbius;
* una suma monótona por factores de Euler;
* Cauchy entre las dos sucesiones de grado;
* la identidad de Riccati sin un término Gamma independiente.

La única arquitectura no refutada dentro de esta familia sería un **complejo
graduado Euler–Gamma** con tres propiedades demostradas antes de usar positividad:

1. su diferencial Euler produce el término cruzado (3);
2. sus correlaciones de cociente \(n/m\) son fronteras exactas o pares
   supersimétricos que cancelan algebraicamente;
3. el cociente físico conserva una métrica positiva y su diagonal restante es
   exactamente el presupuesto Gamma \(\Delta A_n/2\).

La palabra «supersimétrico» no constituye el mecanismo. Sin una construcción que
pruebe simultáneamente 1–3, esta opción es solo una especificación. Una cancelación
mediante supertraza o métrica de Krein no sirve: cancela las diagonales usando signos
negativos y no produce una desigualdad de Hilbert.

No se encontró tal complejo en este ataque. La obstrucción unipotente demuestra que
debería contener información adicional a la inversión Möbius ordinaria.

## 9. Decisión

```text
probado:
  convolución Möbius–divisor exacta en el grado Laguerre;
  normalización polo–primos como -(1-z)F^{-1}F';
  identificación fórmula por fórmula con E70.11 y E70.12;
  equivalencia de la cota faltante con el gate de primera diferencia;
  imposibilidad de realizar Möbius = adjunto en una métrica positiva;
  retorno del peine de cocientes al usar el adjunto verdadero.

descartado:
  M5 como Gram ordinario o congruencia por Z^{-1/2};
  filtración monótona por factores de Euler;
  normas separadas en la convolución de grado;
  Riccati como fuente autónoma de signo.

no probado:
  una desigualdad nueva para la convolución firmada real;
  un complejo graduado Euler–Gamma positivo;
  (22), A1 o RH.

decisión:
  M5 aporta una coordenada exacta, pero no un mecanismo de cierre actual.
  Siguiendo el orden de Phase 104, se activa M3 no local; M5 solo debe
  reabrirse si aparece una construcción concreta del complejo 1–3.
```
