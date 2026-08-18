# 104_100 — Promedio funcional de dos hojas y gate del corrector de completamiento

## Resultado

Este documento ejecuta el promedio de las dos hojas de `104_98` usando
simultaneamente ecuacion funcional, conjugacion y el completamiento exacto de
Riemann. La diagonal de monodromia se centra efectivamente para
\(\log\xi\), pero **no** se transfiere a la energia aritmetica de
\(\Phi_N\).

Ponga

\[
 C(s)={1\over2}s(s-1)\pi^{-s/2}\Gamma(s/2),
 \qquad \xi(s)=C(s)\zeta(s),                              \tag{1}
\]

y, con las ramas compatibles de `104_98`,

\[
 \begin{aligned}
 A(s)&=\sum_{k\ge2}{\mu(k)\over k}\log\zeta(ks)
       -E_1((s-1)\log2)+R(s),\\
 G(s)&=A(s)-\log C(s).
 \end{aligned}                                             \tag{2}
\]

Entonces, localmente en \(\Re s>1/2\), fuera de los ceros,

\[
 \boxed{\Phi(s)=\log\xi(s)+G(s).}                          \tag{3}
\]

Sea \(\rho=1/2+b+i\gamma\), \(b>0\), un cero de multiplicidad
\(m\), y emparejelo con \(1-\bar\rho=1/2-b+i\gamma\). Conceda al
metodo su caso mas favorable: \(s_\gamma=1/2+i\gamma\) no es tambien
un cero critico y las dos orillas del corte simetrico se centran por
reflexion. Entonces pueden escribirse

\[
 (\log\xi)_\pm(s_\gamma)=\ell_\gamma\pm\pi i m,
 \qquad \ell_\gamma\in\mathbb R.                          \tag{4}
\]

Sin esa concesion, en cualquier cruce no nulo del corte se tiene la
forma mas general \((\log\xi)_\pm=\ell_0\pm\pi i m\), con
\(\ell_0\in\mathbb C\), y en (6) sobrevive adicionalmente
\(4\pi m\Im\ell_0\), tambien sin signo impuesto por las simetrias. El
resto estudia la normalizacion mas favorable (4), donde ese segundo
indeterminado se elimina por completo.

Por tanto las hojas del simbolo primo son exactamente

\[
 \Phi_\pm(s_\gamma)=\ell_\gamma+G(s_\gamma)\pm\pi i m,    \tag{5}
\]

y satisfacen

\[
 \boxed{
 \begin{aligned}
 { |\Phi_+|^2+|\Phi_-|^2\over2}
   &=|\ell_\gamma+G(s_\gamma)|^2+\pi^2m^2,\\
 |\Phi_+|^2-|\Phi_-|^2
   &=4\pi m\,\Im G(s_\gamma).
 \end{aligned}}                                             \tag{6}
\]

Asi, el completamiento mata la parte firmada **dentro de**
\(\log\xi\), pero al descompletar reaparece exactamente como
\(\pm2\pi m\Im G\). La ecuacion funcional no determina su signo.

Hay dos obstrucciones exactas adicionales.

1. Las transformaciones \(s\mapsto1-s\), conjugacion y su composicion
   preservan, en vez de invertir, el caracter local de monodromia
   \(2\pi i m\). Por ello ninguna de ellas entrega la hoja opuesta de la
   continuacion fisica.
2. El corrector real no es una perturbacion de energia finita. Cuando
   \(s=1/2+it\),

   \[
   \log|C(s)|=-{\pi\over4}|t|+{7\over4}\log|t|+O(1),        \tag{7}
   \]

   mientras \(A(1/2+it)=O(\sqrt{|t|}+\log(2+|t|))\) en ramas
   continuas. En consecuencia

   \[
   \Re G(1/2+it)={\pi\over4}|t|+O(\sqrt{|t|}+\log(2+|t|)), \tag{8}
   \]

   y

   \[
   \boxed{
   \int_T^{2T}\left|{G(1/2+it)\over1/2+it}\right|^2dt
      \ge \left({\pi^2\over16}+o(1)\right)T.}              \tag{9}
   \]

Por ello no se puede restar el corrector mediante desigualdad triangular
en el espacio de Plancherel de `104_98`: el termino gamma y el termino
completado poseen una cancelacion macroscopica que debe conservarse.

Finalmente se da un falsificador algebraico exacto. Existe una familia
con cuarteto exterior, completamiento entero, ecuacion funcional y
conjugacion en la que una de las dos hojas se cancela **exactamente** y la
otra duplica toda la diagonal. Esto prueba que las tres simetrias, incluso
juntas, no seleccionan la hoja aritmetica ni proporcionan la desigualdad
faltante.

**Veredicto.** El promedio funcional de dos hojas no prueba la energia
subpolinomial, Deep-\(\Lambda\), A1 ni RH. El termino que sobrevive es
\(2\pi m\Im G(s_\gamma)\), y el corrector que lo contiene tiene energia
lineal, no finita. Cerrar la ruta aun exige una estimacion aritmetica
global para los pesos ordinarios; la simetria del completamiento no la
reemplaza.

---

## 1. Descomposicion exacta del simbolo primo

La ecuacion (7) de `104_98` dice

\[
 \Phi(s)=\log\zeta(s)
 +\sum_{k\ge2}{\mu(k)\over k}\log\zeta(ks)
 -E_1((s-1)\log2)+R(s).                                  \tag{10}
\]

Como \(\log\zeta=\log\xi-\log C\), (10) es precisamente (3).
En un disco que no contiene \(0\), \(1\), polos gamma ni otro cero,
\(G\) es monovaluada y holomorfa. Toda la monodromia derecha de \(\Phi\)
esta, pues, en \(\log\xi\).

La ecuacion funcional y la realidad son

\[
 \xi(s)=\xi(1-s),\qquad
 \xi(\bar s)=\overline{\xi(s)}.                          \tag{11}
\]

Si \(L=\log\xi\) es una determinacion local, entonces, modulo constantes
en \(2\pi i\mathbb Z\),

\[
 L(1-s)=L(s),\qquad \overline{L(\bar s)}=L(s).             \tag{12}
\]

Estas igualdades no invierten la monodromia. En efecto, alrededor de un
cero, escriba \(z=s-\rho\). Las cuatro coordenadas locales relevantes
son

\[
 \log z,\quad \log(-z),\quad
 \overline{\log\bar z},\quad
 \overline{\log(-\bar z)}.                               \tag{13}
\]

Cuando \(z\) recorre una vuelta positiva, las cuatro expresiones ganan
\(2\pi i\). En los dos ultimos casos la inversion de orientacion causada
por conjugacion es invertida otra vez al conjugar el valor. Por tanto el
grupo generado por (11) actua trivialmente sobre el caracter de
monodromia. La hoja \(+\) y la hoja \(-\) siguen siendo dos datos
distintos; (11) no las promedia.

## 2. El corte simetrico del cuarteto

La ecuacion funcional y conjugacion fuerzan, junto con \(\rho\), los
ceros

\[
 \bar\rho,\quad1-\rho,\quad1-\bar\rho.                    \tag{14}
\]

Si \(s_\gamma\) no es otro cero, en un entorno de la pareja superior se
puede factorizar

\[
 \xi(s)=\{(s-s_\gamma)^2-b^2\}^{m}H_\gamma(s),            \tag{15}
\]

donde \(H_\gamma\) es holomorfa y no nula. La simetria
\(s\mapsto1-\bar s\) fija \(s_\gamma\). En la convencion de corte mas
favorable, las dos trazas se eligen conjugadas y su punto medio es real;
esto da (4). Si un cero critico ocupa \(s_\gamma\), se hace cruzar una
curva simetrica por un punto vecino no nulo de la recta critica. El punto
medio general puede tener parte imaginaria, pero entonces deja el termino
firmado adicional ya registrado despues de (4); la simetria tampoco fija
su signo.

Sumar (2) a ambas orillas da (5), y expandir
\(|z\pm i d|^2=|z|^2+d^2\pm2d\Im z\) prueba (6). Observe
que aqui no se hizo una estimacion: el residuo firmado que queda es una
identidad exacta.

En la recta critica tambien puede escribirse, con continuaciones de tipo
real,

\[
 \Phi(1-s)=\overline{\Phi(s)},\qquad s=1/2+it.             \tag{16}
\]

Por ello el promedio funcional solo produce

\[
 |\Phi(s)|^2
 =\left|{\Phi(s)+\Phi(1-s)\over2}\right|^2
 +\left|{\Phi(s)-\Phi(1-s)\over2}\right|^2.              \tag{17}
\]

Es la identidad pitagorica entre parte real e imaginaria. Ambos sumandos
son positivos, pero (17) es una **descomposicion inferior** de la energia,
no una cota superior subpolinomial para ella. Tampoco genera las dos
orillas de un mismo corte: empareja los puntos \(t\) y \(-t\).

La misma operacion puede realizarse antes de todo limite, literalmente
sobre los pesos ordinarios. Como los coeficientes de \(\Phi_N\) son
reales, defina

\[
 S_N(s)={\Phi_N(s)+\Phi_N(1-s)\over2},\qquad
 T_N(s)={\Phi_N(s)-\Phi_N(1-s)\over2}.                    \tag{17a}
\]

Si \(s=1/2+it\), entonces

\[
 S_N(s)=\Re\Phi_N(s),\qquad T_N(s)=i\Im\Phi_N(s),         \tag{17b}
\]

y la factorizacion de `104_98` se vuelve exactamente

\[
 \sum_{m=2}^N{P_m^2\over m(m+1)}
 ={1\over2\pi}\int_{\mathbb R}
 { |S_N(1/2+it)|^2+|T_N(1/2+it)|^2\over t^2+1/4}\,dt.    \tag{17c}
\]

Este es el promedio aritmetico de dos reflejos completo. No contiene una
desigualdad nueva: es \(|z|^2=(\Re z)^2+(\Im z)^2\). Tanto \(S_N\) como
\(T_N\) son enteros y monovaluados, de modo que ninguno posee la diagonal
de monodromia. Esa diagonal aparece solamente al continuar el limite
infinito a traves de su semiplano de convergencia. Demostrar que sobrevive
uniformemente en los prefijos seria ya demostrar la cota de energia de
`104_93`--`104_94`.

## 3. Falsificador exacto dentro de las simetrias

Ponga \(z=s-1/2\), elija \(b,\gamma>0\), y defina

\[
 Q_{b,\gamma}(s)=
 -{\{(z-i\gamma)^2-b^2\}\{(z+i\gamma)^2-b^2\}
    \over b^2(4\gamma^2+b^2)}.                            \tag{18}
\]

Es un polinomio entero de tipo real y satisface

\[
 Q_{b,\gamma}(1-s)=Q_{b,\gamma}(s),\qquad
 Q_{b,\gamma}(\bar s)=\overline{Q_{b,\gamma}(s)}.         \tag{19}
\]

Sus ceros son exactamente \(1/2\pm b\pm i\gamma\), y
\(Q_{b,\gamma}(s_\gamma)=-1\). Para \(X=Q_{b,\gamma}^{m}\),
las dos ramas simetricas de \(L=\log X\) en el punto medio son

\[
 L_\pm(s_\gamma)=\pm\pi i m.                             \tag{20}
\]

Ahora, para \(c\in\mathbb R\), ponga

\[
 \Phi_c(s)=L(s)+c(s-1/2),\qquad G_c(s)=c(s-1/2).           \tag{21}
\]

Restar \(G_c\) completa exactamente \(\Phi_c\) en la funcion \(L\),
que satisface (19). El corrector es entero y de tipo real, pero es
antisimetrico bajo \(s\mapsto1-s\), como puede serlo la parte eliminada
por un completamiento. En \(s_\gamma\),

\[
 (\Phi_c)_\pm=i(c\gamma\pm\pi m).                         \tag{22}
\]

Con \(c=-\pi m/\gamma\),

\[
 (\Phi_c)_+=0,
 \qquad
 (\Phi_c)_-=-2\pi i m.                                   \tag{23}
\]

La diagonal promedio es positiva, pero una hoja no conserva ninguna
fraccion positiva de ella. Cambiar el signo de \(c\) intercambia las
hojas. Este falsificador no pretende conservar los pesos ordinarios de
Mangoldt; prueba exactamente que **ecuacion funcional + conjugacion +
completamiento** no bastan para escoger el signo en (6). Los pesos
literales siguen siendo el input adicional que haria falta.

## 4. El corrector de Riemann tiene energia macroscopica

La formula de Stirling, uniforme en la recta \(\Re s=1/2\), da

\[
 \log\left|\Gamma\left({1\over4}+{it\over2}\right)\right|
 =-{\pi\over4}|t|-{1\over4}\log|t|+O(1).                 \tag{24}
\]

Como \(|s(s-1)|=t^2+O(1)\), sustituir (24) en (1) prueba (7).

Resta comprobar que los otros terminos de (2) no contienen otro termino
lineal oculto. Para el residuo discretizado de `104_98`, en
\(s=1/2+it\),

\[
 \left|\int_{m-1}^{m}{x^{-s}-m^{-s}\over\log x}\,dx\right|
 \ll \min\left\{{m^{-1/2}\over\log m},
                 {|s|m^{-3/2}\over\log m}\right\}.      \tag{25}
\]

Separar la suma en \(m\le |s|\) y \(m>|s|\) da

\[
 R(1/2+it)=O(\sqrt{|t|}).                                 \tag{26}
\]

El bloque \(k\ge3\) de (2) es uniformemente acotado. En \(k=2\), las
estimaciones clasicas sobre \(\zeta(1+2it)\), junto con una rama continua,
dan \(\log\zeta(1+2it)=O(\log(2+|t|))\). Finalmente,
\(E_1((-1/2+it)\log2)=O(1/|t|)\) en la rama principal; cualquier rama
compatible fija solo añade una constante. Esto prueba la cota declarada
para \(A\), y (7) implica (8).

De (8), uniformemente para \(T\le t\le2T\),

\[
 { |G(1/2+it)|^2\over t^2+1/4}
 \ge {\{\Re G(1/2+it)\}^2\over t^2+1/4}
 ={\pi^2\over16}+o(1).                                   \tag{27}
\]

Integrar prueba (9). Esta es la perdida decisiva: la energia finita de
las potencias propias de `104_94` no significa que el **corrector de
completamiento logaritmico** sea finito. El factor gamma es lineal en
\(|t|\), y solo se cancela si se mantienen juntos todos los terminos.

## 5. Por que tampoco cierran BSY o Weil

### 5.1 BSY

En la coordenada de disco de `104_89`,

\[
 w(s)={s-1\over s},\qquad w(1-s)={1\over w(s)}.           \tag{28}
\]

Un cero derecho da \(|w(\rho)|<1\); su reflejo funcional esta en el
reciproco exterior. Poisson--Jensen cuenta unilateralmente el cero
interior y produce

\[
 D_B=\sum_{\Re\rho>1/2}m_\rho\log{1\over|w(\rho)|}.       \tag{29}
\]

Promediar el punto interior con su reciproco exterior cancelaria el
defecto solo introduciendo un polo o un factor exterior que ya no es una
truncacion Euler cero-libre analitica en el disco. Por ello (28) no
controla la fuga unilateral de `104_89`; simplemente reescribe el mismo
factor de Blaschke.

### 5.2 Weil y Li

Agrupar un cuarteto por ecuacion funcional y conjugacion ya fue hecho en
`103_65`. Si

\[
 1-{1\over\rho}=e^{-a+i\theta},\qquad a>0,
\]

su contribucion a \(2\lambda_n\) es

\[
 8-8\cosh(na)\cos(n\theta).                              \tag{30}
\]

El factor \(\cosh(na)\cos(n\theta)\) tiene ambos signos. Esta es la
version discreta del termino firmado de (6). Elevar el promedio de hojas
a una positividad para todos los tests seria precisamente positividad de
Weil, equivalente a RH; no es una consecuencia adicional de (11).

## 6. Alcance exacto del no-go

El documento demuestra tres afirmaciones limitadas y rigurosas:

1. las simetrias funcionales no intercambian las dos determinaciones
   locales;
2. aun despues de centrar \(\log\xi\), queda exactamente
   \(2\pi m\Im G\) en una hoja del simbolo primo;
3. \(G\) no puede desecharse como perturbacion finita en la energia de
   `104_98`.

No se afirma que toda desigualdad aritmetica de dos hojas sea imposible.
Una estimacion nueva que use simultaneamente todos los pesos ordinarios
podria controlar la cancelacion entre \(\log\xi\) y \(G\); probarla seria
precisamente el teorema de energia equivalente a RH de `104_93`--`104_94`.

## 7. Reproduccion

Desde `tools/`:

```bash
python3 functional_two_sheet_completion_check.py
```

El checker:

1. verifica que las cuatro acciones locales de (13) tienen la misma
   monodromia;
2. comprueba las identidades de dos hojas (6) y el promedio aritmetico
   finito (17a)--(17c);
3. verifica las simetrias, el cuarteto y la cancelacion exacta (18)--(23);
4. evalua por Stirling el coeficiente \(-\pi/4\) y el termino
   \((7/4)\log t\) de (7).

Las evaluaciones numericas solo comprueban el algebra y los asintoticos
ya demostrados; no constituyen evidencia de RH.
