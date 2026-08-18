# 104_57 — Presupuesto exacto del bloque bajo de ceros

**Rol.** Convertir la traducción corregida de Lagarias en una cota, no en una
mera coordenada. Este documento no prueba A1 ni RH. Aísla el único bloque de
ceros que conserva fuerza RH, fija su cardinalidad con todas las convenciones
de factor dos y da un criterio algebraico para descartar estimaciones con un
error incompatible con el margen que reclaman.

**Dependencias vinculantes.** Se usan el erratum de signo de `104_02`, la
normalización A1 de `104_01` y la cota de conteo completamente numérica de
`103_58` §2. No se importa el signo impreso de (1.15), (1.17) o (6.7) de
Lagarias.

---

## 1. Convenciones y descomposición exacta

Sea

\[
 \lambda_n(T):=
 \sum_{\substack{\rho\text{ cero no trivial}\ |\Im\rho|<T}}
 m_\rho\left[1-\left(1-{1\over\rho}\right)^n\right]             \tag{1}
\]

el coeficiente incompleto de Lagarias. La desigualdad en la altura es
**estricta**. Así, la definición no necesita decidir qué hacer si una ordenada
fuera exactamente igual al cutoff.

Definimos

\[
 L_n^{<}:=\lambda_n(\sqrt n),\qquad
 L_n^{>}:=\lambda_n-L_n^{<}.                                  \tag{2}
\]

La segunda cantidad significa la diferencia entre el coeficiente completo,
con su convención canónica de suma simétrica, y la suma finita (1). No se
afirma que sea una suma absolutamente convergente obtenida restando términos
uno por uno.

El erratum `104_02`, ecuaciones (2.3)--(2.4), define

\[
 \widetilde\varepsilon_n:=A_n-\lambda_n+L_n^{<}
\]

y prueba incondicionalmente que existe una constante absoluta \(C_*>0\) tal
que

\[
 |\widetilde\varepsilon_n|\le C_*\sqrt n\log n.                 \tag{3}
\]

La constante existe pero no quedó explicitada por ese argumento.

### Teorema 1 (la cola alta reproduce el bloque arquimediano) `[INC]`

Para todo \(n\ge2\),

\[
 \boxed{
 L_n^{>}=A_n-\widetilde\varepsilon_n,\qquad
 |L_n^{>}-A_n|\le C_*\sqrt n\log n.}                            \tag{4}
\]

En particular,

\[
 \boxed{\lambda_n=A_n+L_n^{<}-\widetilde\varepsilon_n.}         \tag{5}
\]

**Demostración.** De la definición de

\(
\widetilde\varepsilon_n=A_n-\lambda_n+L_n^{<}
\)

se obtiene

\(
\lambda_n-L_n^{<}=A_n-\widetilde\varepsilon_n
\).
La cota es (3). No interviene RH. \(\square\)

Ésta es la forma precisa de la frase «los ceros con
\(|\gamma|\ge\sqrt n\) reproducen \(A_n\)»: es una identidad para la cola
**canónicamente regularizada** y un error incondicional
\(O(\sqrt n\log n)\). No es una positividad término a término de esos ceros.

---

## 2. Traducción exacta de A1 y del margen cuártico

Para \(\theta=1/4\), `104_02` prueba

\[
 \mathrm {A1}_{1/4}
 \iff
 -L_n^{<}+\widetilde\varepsilon_n+R_n(T_n)
 \le {3\over4}A_n.                                             \tag{6}
\]

Por tanto la forma de cota inferior es

\[
 \boxed{
 \mathrm {A1}_{1/4}
 \iff
 L_n^{<}\ge-{3\over4}A_n+\widetilde\varepsilon_n+R_n(T_n).}    \tag{7}
\]

Separadamente, para cualquier \(c\in\mathbb R\), (5) da la equivalencia
puramente algebraica

\[
 \boxed{
 \lambda_n\ge cA_n
 \iff
 L_n^{<}\ge-(1-c)A_n+\widetilde\varepsilon_n.}                 \tag{8}
\]

En particular,

\[
 \boxed{
 4\lambda_n\ge A_n
 \iff
 L_n^{<}\ge-{3\over4}A_n+\widetilde\varepsilon_n.}             \tag{9}
\]

Usando solo (3), se obtiene el sandwich unilateral

\[
 L_n^{<}\ge-{3\over4}A_n+C_*\sqrt n\log n
 \quad\Longrightarrow\quad
 4\lambda_n\ge A_n,                                           \tag{10}
\]

y

\[
 4\lambda_n\ge A_n
 \quad\Longrightarrow\quad
 L_n^{<}\ge-{3\over4}A_n-C_*\sqrt n\log n.                    \tag{11}
\]

Las dos fronteras están separadas por \(2C_*\sqrt n\log n\). Como \(C_*\)
no es efectivo, (10) no produce por sí sola un umbral numérico.

**Estado lógico.** (4)--(11) son incondicionales. Probar la cota inferior de
(7) o (9) uniformemente sigue siendo el paso RH-strength; ninguna de estas
identidades lo prueba.

---

## 3. Cuántos términos quedan realmente

Sea

\[
 N_{<}(T):=\sum_{\substack{\rho=\beta+i\gamma\text{ cero}\\0<\gamma<T}}m_\rho
                                                                    \tag{12}
\]

el conteo de ordenadas **positivas**, con multiplicidad y cutoff estricto.
La simetría por conjugación implica que (1) contiene exactamente
\(2N_{<}(T)\) etiquetas de cero.

La fórmula de Riemann--von Mangoldt da incondicionalmente `[INC]`

\[
 N_{<}(T)={T\over2\pi}\log{T\over2\pi e}+O(\log T).             \tag{13}
\]

Cambiar \(<T\) por \(\le T\) no cambia esta asintótica. En \(T=\sqrt n\),

\[
 \boxed{
 N_{<}(\sqrt n)
 ={\sqrt n\over4\pi}\log n
 -{\sqrt n\over2\pi}\log(2\pi e)+O(\log n).}                 \tag{14}
\]

Así, el bloque bajo contiene

\[
 \boxed{
 2N_{<}(\sqrt n)
 ={\sqrt n\over2\pi}\log n+O(\sqrt n)}                       \tag{15}
\]

sumandos etiquetados. El factor \(1/(4\pi)\) corresponde al conteo de
**ordenadas positivas**; el factor \(1/(2\pi)\), al número de etiquetas en
la suma simétrica. Mezclarlos duplica o divide erróneamente el presupuesto.

Hay además una cota completamente numérica ya probada en `103_58` §2. Si
\({\cal N}(T)\) cuenta ambos signos, entonces

\[
 {\cal N}(T)\le25T\log T\qquad(T\ge10).                         \tag{16}
\]

Por tanto, para \(n\ge100\),

\[
 \boxed{
 2N_{<}(\sqrt n)\le {25\over2}\sqrt n\log n,
 \qquad
 N_{<}(\sqrt n)\le {25\over4}\sqrt n\log n.}                 \tag{17}
\]

Estas constantes son deliberadamente gruesas; su función es que ningún
argumento futuro esconda una constante de Riemann--von Mangoldt.

### Calibración local `[COND: RH para \(|\gamma|<\sqrt n\)]`

Si los ceros del bloque están en la línea crítica, cada par conjugado aporta

\[
 2-2\cos(n\vartheta_\rho)\in[0,4].
\]

Luego

\[
 \boxed{
 0\le L_n^{<}\le4N_{<}(\sqrt n)
 ={\sqrt n\over\pi}\log n+O(\sqrt n).}                         \tag{18}
\]

La escala natural del bloque bajo bajo RH es, por tanto,
\(\sqrt n\log n\), la misma que el error de transporte (3). La desigualdad
(18) no es un input incondicional.

---

## 4. Escala exacta de un cero fuera de la línea `[INC]`

Sea \(\rho=\beta+i\gamma\), \(\beta>1/2\), y

\[
 w_\rho:=1-{1\over\rho}={\rho-1\over\rho}.
\]

Entonces

\[
 |w_\rho|^2
 ={\gamma^2+(1-\beta)^2\over\gamma^2+\beta^2}
 =1-{2\beta-1\over\gamma^2+\beta^2}<1.                        \tag{19}
\]

Escribamos \(w_\rho=e^{-a_\rho+i\vartheta_\rho}\), \(a_\rho>0\). Con

\[
 d:=2\beta-1,\qquad x:={d\over\gamma^2+\beta^2}\in(0,1),
\]

se tiene exactamente

\[
 a_\rho=-{1\over2}\log(1-x).                                  \tag{20}
\]

Las desigualdades \(x\le-\log(1-x)\le x/(1-x)\) dan la cota efectiva

\[
 \boxed{
 {2\beta-1\over2(\gamma^2+\beta^2)}
 \le a_\rho\le
 {2\beta-1\over2(\gamma^2+(1-\beta)^2)}.}                     \tag{21}
\]

Uniformemente en \(0<\beta<1\), cuando \(\gamma\to\infty\),

\[
 \boxed{
 a_\rho={2\beta-1\over2\gamma^2}+O(\gamma^{-4}).}             \tag{22}
\]

El cuarteto funcional completo aporta a \(L_n^{<}\), una vez que
\(|\gamma|<\sqrt n\),

\[
 Q_n(\rho)=4-4\cosh(na_\rho)\cos(n\vartheta_\rho).             \tag{23}
\]

Su parámetro de activación es, por (21),

\[
 {n(2\beta-1)\over2(\gamma^2+\beta^2)}
 \le na_\rho\le
 {n(2\beta-1)\over2(\gamma^2+(1-\beta)^2)}.                  \tag{24}
\]

Por ello el módulo hiperbólico solo empieza a ser grande cuando

\[
 \gamma^2\lesssim {n(2\beta-1)\over2};                         \tag{25}
\]

en la aproximación de gran altura. En particular, si
\(|\gamma|\ge\sqrt n\), entonces \(na_\rho\le1/2\) por (21). Esta
es una afirmación **por cuarteto individual**: su factor hiperbólico no puede
activarse exponencialmente fuera del bloque bajo. No es una cota colectiva
para la suma de los ceros altos.

**Advertencia.** (23)--(25) describen un cuarteto. No dan una cota inferior
para la suma creciente de todos los cuartetos: las fases
\(n\vartheta_\rho\) pueden interferir. Bombieri--Lagarias es el input correcto
para afirmar que, si RH falla, el bloque incompleto tiene excursiones
exponenciales sobre una subsucesión. No se sustituye ese teorema por un
argumento de «cero dominante» no demostrado.

---

## 5. Criterio exacto de presupuesto para mecanismos futuros `[INC]`

Supóngase que un mecanismo incondicional produce, con
\(\alpha_n\ge0\), \(E_n\ge0\),

\[
 L_n^{<}\ge-\alpha_n A_n-E_n.                                  \tag{26}
\]

De (5) y (3),

\[
 \lambda_n\ge(1-\alpha_n)A_n-E_n-C_*\sqrt n\log n.             \tag{27}
\]

Por tanto, para demostrar \(\lambda_n\ge cA_n\) mediante (26), basta y es
necesario para esta transferencia de peor caso que

\[
 \boxed{
 E_n+C_*\sqrt n\log n
 \le(1-c-\alpha_n)A_n.}                                       \tag{28}
\]

Para el margen cuártico \(c=1/4\),

\[
 \boxed{
 E_n+C_*\sqrt n\log n
 \le\left({3\over4}-\alpha_n\right)A_n.}                      \tag{29}
\]

Para A1 exacta, si además solo se conoce una cota unilateral
\(R_n(T_n)\le r_n^+\), (7) muestra que el test correspondiente es

\[
 \boxed{
 E_n+C_*\sqrt n\log n+r_n^+
 \le\left({3\over4}-\alpha_n\right)A_n.}                      \tag{30}
\]

Esto corrige dos posibles falsos diagnósticos.

1. **Un error \(\gg\sqrt n\log n\) no mata automáticamente una ruta.** Si
   \(\alpha_n\le3/4-\delta\) para algún \(\delta>0\), cualquier
   \(E_n=o(A_n)=o(n\log n)\) satisface eventualmente (29), aunque sea mucho
   mayor que \(\sqrt n\log n\).
2. **La escala \(\sqrt n\log n\) sí es bloqueante cuando ésa es toda la
   ganancia firmada.** Si un mecanismo pretende resolver el bloque a su
   escala natural --por ejemplo \(L_n^{<}\ge-O(\sqrt n\log n)\)--, un error
   no controlado de orden mayor borra exactamente la información que dice
   producir. Y si \(\alpha_n=3/4\), ningún error no negativo cierra (29) sin
   usar signo adicional de \(\widetilde\varepsilon_n\).

Así, el stop-gate correcto no es «error mayor que \(\sqrt n\log n\)» en
abstracto. Es la desigualdad de presupuesto (28), con el margen proporcional
del mecanismo escrito explícitamente.

---

## 6. Qué cambia y qué no

**Cerrado incondicionalmente.** La cola alta es \(A_n\) con error
\(O(\sqrt n\log n)\); el bloque restante es una suma finita de
\(\asymp\sqrt n\log n\) etiquetas; la escala de activación de un cuarteto es
\(na_\rho\asymp n(2\beta-1)/(2\gamma^2)\); y (28)--(30) deciden si la
precisión reclamada por un mecanismo alcanza el objetivo.

**No cerrado.** No se obtuvo ninguna cota inferior nueva para
\(L_n^{<}\), ningún control colectivo de las fases fuera de la línea, A1 ni
RH.

**Consecuencia operativa.** Los próximos mecanismos deben enunciar antes de
empezar su par \((\alpha_n,E_n)\) en (26). Si no pueden satisfacer (29), o
(30) con la cota de cola que realmente usen, se descartan sin desarrollar la
maquinaria restante.

---

## 7. Reproducción diagnóstica

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 low_zero_block_budget_check.py
```

El programa comprueba la identidad racional (19), las dos cotas de (21), la
normalización del cuarteto (23) y las equivalencias algebraicas de
(8)/(28) sobre datos racionales. Los teoremas de conteo y de Lagarias no se
«certifican» por muestreo: sus pruebas son los inputs citados arriba.
