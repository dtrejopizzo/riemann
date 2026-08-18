# 104_94 — Núcleo de primos ordinarios y energía finita de las potencias

## Resultado

Ponga

\[
 S_m=\sum_{n=2}^m{1\over\log n},\qquad
 P_m=\pi(m)-S_m,
 \tag{1}
\]

y

\[
 Q_m=\sum_{2\le k\le \log_2m}{1\over k}\,
       \pi\!\left(m^{1/k}\right).
 \tag{2}
\]

Las raíces y el límite superior de (2) se entienden en el sentido
exacto: \(\pi(m^{1/k})\) cuenta los primos \(p\) tales que \(p^k\le m\).
Entonces el vector de `104_93` se descompone exactamente como

\[
 \boxed{B_m=P_m+Q_m.}
 \tag{3}
\]

El bloque entero de potencias propias tiene energía finita
incondicionalmente:

\[
 \boxed{
 \mathcal Q:=\sum_{m=2}^{\infty}{Q_m^2\over m(m+1)}<\infty.}
 \tag{4}
\]

En consecuencia, si

\[
 \mathcal E_B(N)=\sum_{m\le N}{B_m^2\over m(m+1)},
 \qquad
 \mathcal E_P(N)=\sum_{m\le N}{P_m^2\over m(m+1)},
 \tag{5}
\]

entonces

\[
 \boxed{
 \sup_N\mathcal E_B(N)<\infty
 \Longleftrightarrow
 \sup_N\mathcal E_P(N)<\infty,}
 \tag{6}
\]

y

\[
 \boxed{
 \mathcal E_B(N)=N^{o(1)}
 \Longleftrightarrow
 \mathcal E_P(N)=N^{o(1)}.}
 \tag{7}
\]

Si \(L_2(x)=\int_2^xdt/\log t\), el reemplazo de \(S_m\) por
\(L_2(m)\) también es una perturbación de energía finita. Por tanto

\[
 \boxed{
 \mathcal E_B(N)=N^{o(1)}
 \Longleftrightarrow
 \sum_{m\le N}{\{\pi(m)-L_2(m)\}^2\over m(m+1)}=N^{o(1)}.}
 \tag{8}
\]

Junto con `104_93`, (8) sigue siendo equivalente a RH. No es una prueba
de (8). Su contenido nuevo es localizar con exactitud el obstáculo:
**todas las potencias \(p^k\), \(k\ge2\), forman una perturbación de
energía finita; el exponente posible vive ya en los primos \(p\)**.

La identidad de lcm/factorial no evade esta reducción. En efecto,

\[
 \psi(x)=\log\operatorname {lcm}(1,\ldots,\lfloor x\rfloor),
 \qquad
 \vartheta(x)=\log\operatorname {rad}(\lfloor x\rfloor!),
 \tag{9}
\]

y

\[
 J(x)-\pi(x)
 =\int_{2^-}^x{d(\psi-\vartheta)(t)\over\log t}
 =Q(x).
 \tag{10}
\]

Así, pasar del radical del factorial al lcm añade precisamente el bloque
de energía finita (2), y nada más.

**Estado.** Se obtiene una reducción exacta y un no-go de coordenada para
las identidades \(J\), lcm y factorial. No se demuestra
\(\mathcal E_B(N)=N^{o(1)}\), Deep-\(\Lambda\), A1 ni RH.

---

## 1. Descomposición combinatoria exacta

En una potencia prima \(n=p^k\),

\[
 {\Lambda(n)\over\log n}={\log p\over k\log p}={1\over k},
 \tag{11}
\]

y el cociente es cero fuera de las potencias primas. Por tanto

\[
 \begin{aligned}
 J(m)
 &:=\sum_{2\le n\le m}{\Lambda(n)\over\log n}\\
 &=\sum_{k\ge1}{1\over k}\#\{p:p^k\le m\}\\
 &=\pi(m)+\sum_{2\le k\le\log_2m}{1\over k}\pi(m^{1/k}).
 \end{aligned}
 \tag{12}
\]

Como \(B_m=J(m)-S_m\), (12) prueba (3).

La transformación de torres no pierde información. La inversión de
Möbius da, también con sumas finitas,

\[
 \boxed{
 \pi(x)=\sum_{k\le\log_2x}{\mu(k)\over k}J(x^{1/k}).}
 \tag{13}
\]

En efecto, el coeficiente de \(\pi(x^{1/r})\) al sustituir (12) en el
lado derecho es

\[
 {1\over r}\sum_{k\mid r}\mu(k)
 =\begin{cases}1,&r=1,\\0,&r>1.\end{cases}
 \tag{14}
\]

Por ello (12) no puede crear por sí sola una ganancia: es un cambio de
coordenadas finito e invertible.

## 2. Las potencias propias tienen energía finita

Usaremos solamente la cota elemental de Chebyshev

\[
 \pi(y)\le C_\pi {y\over\log y}\qquad(y\ge2),
 \tag{15}
\]

con una constante absoluta. Por ejemplo, se puede tomar una constante
explícita grande: el hecho de que cada primo \(n<p\le2n\) divide
\({2n\choose n}<4^n\), seguido de una suma diádica, da
\(\vartheta(y)\ll y\); separar los primos \(p\le\sqrt y\) de los
restantes da (15). No se usa PNT ni localización de ceros.

Para cada término de (2), (15) da

\[
 {1\over k}\pi(m^{1/k})
 \le {C_\pi\over\log m}m^{1/k}.
 \tag{16}
\]

Si \(K=\lfloor\log_2m\rfloor\), entonces

\[
 \sum_{k=2}^{K}m^{1/k}
 \le \sqrt m+(K-2)m^{1/3}
 \le \sqrt m+{\log m\over\log2}m^{1/3}.
 \tag{17}
\]

De (16)--(17),

\[
 0\le Q_m\le
 C_\pi{\sqrt m\over\log m}
 +{C_\pi\over\log2}m^{1/3}.
 \tag{18}
\]

Finalmente,

\[
 {Q_m^2\over m(m+1)}
 \le
 2C_\pi^2{1\over m\log^2m}
 +{2C_\pi^2\over\log^22}m^{-4/3}.
 \tag{19}
\]

Ambas series convergen. Esto prueba (4).

## 3. Equivalencia de las energías

Para una sucesión real \(U=(U_m)\), escriba

\[
 \|U\|_N^2=\sum_{m=2}^{N}{U_m^2\over m(m+1)}.
 \tag{20}
\]

Es una norma euclínea finita con pesos positivos. De (3), la desigualdad
triangular y (4),

\[
 \big|\|B\|_N-\|P\|_N\big|
 \le\|Q\|_N\le\sqrt{\mathcal Q}.
 \tag{21}
\]

La equivalencia (6) es inmediata. Si una de las dos energías es
\(N^{o(1)}\), entonces para cada \(\varepsilon>0\)

\[
 \|P\|_N^2
 \le(\|B\|_N+\sqrt{\mathcal Q})^2
 \ll_\varepsilon N^\varepsilon,
 \tag{22}
\]

y recíprocamente. Esto prueba (7).

Para comparar la suma y la integral del comparador, la monotonía de
\(1/\log x\) da exactamente

\[
 0\le
 D_m:=S_m-L_2(m)
 \le {1\over\log2}.
 \tag{23}
\]

Luego

\[
 \sum_{m=2}^{\infty}{D_m^2\over m(m+1)}
 \le {1\over2\log^22}<\infty.
 \tag{24}
\]

Aplicando otra vez (21) con \(D\) se obtiene (8).

## 4. Lcm, radical del factorial y el mismo bloque

Las identidades de factorización prima dan (9): el máximo exponente de
\(p\) que divide \(1,\ldots,m\) produce \(\psi(m)\), mientras el
radical de \(m!\) contiene una sola copia de cada primo \(p\le m\) y
produce \(\vartheta(m)\).

Como los saltos de \(\psi\) en \(p^k\) pesan \(\log p\), y los de
\(\vartheta\) solamente en \(p\),

\[
 \int_{2^-}^x{d\psi(t)\over\log t}=J(x),
 \qquad
 \int_{2^-}^x{d\vartheta(t)\over\log t}=\pi(x).
 \tag{25}
\]

Su diferencia es (10), y la Sección 2 prueba que esa diferencia tiene
energía finita. En particular:

* el lcm conserva todas las potencias primas, pero las potencias propias
  no pueden ser el origen de un exponente positivo de \(\mathcal E\);
* el radical del factorial conserva exactamente el canal \(k=1\), que sí
  contiene todo el obstáculo;
* invertir (12) mediante (13) recupera ese mismo canal y no aporta una
  desigualdad de signo.

Esta es la razón exacta por la que las identidades combinatorias
lcm/factorial no cierran (8): después de quitar una perturbación de
energía finita queda el error cuadrático de los primos ordinarios.

## 5. Qué tendría que aportar un sucesor

La cota buscada ya puede escribirse sin potencias propias:

\[
 \sum_{m\le N}{\{\pi(m)-L_2(m)\}^2\over m(m+1)}=N^{o(1)}.
 \tag{26}
\]

No basta una cota de magnitud PNT. Por ejemplo, un error
\(O(xe^{-c(\log x)^{3/5}(\log\log x)^{-1/5}}/\log x)\) todavía produce,
por sustitución directa en (26), una cota con exponente logarítmico
superior igual a \(1\), no \(0\). El sucesor debe usar cancelación
cuadrática real de la colocación de los primos, no solamente el PNT ni
la contabilidad de sus potencias.

## 6. Auditoría de duplicación

* `103_66` ya prueba la telescopía de torres a
  \(\psi=\log\operatorname {lcm}\), pero no elimina el bloque
  \(k\ge2\) en la norma de Cramér.
* `E101_090` aísla la covarianza multiplicativa de cociente para
  \(\Lambda-1\), con otro cutoff y otra norma.
* `104_89` y `104_93` identifican la energía de Cramér y su equivalencia
  con RH.

Lo adicional aquí es (3)--(8): la separación exacta del canal
\(p\) y la prueba incondicional de que **todo** \(p^k\), \(k\ge2\), es
una perturbación de energía finita en la norma discreta exacta.

## 7. Reproducción

Desde `tools`:

```bash
python3 ordinary_prime_core_energy_check.py
```

El checker verifica con aritmética racional las identidades finitas
(12)--(14), comprueba (3) para cada prefijo y muestra separadamente las
energías de \(B\), \(P\), \(Q\) y el borde de Minkowski. La tabla
numérica es diagnóstica; las pruebas de (4)--(8) son las anteriores.
