# 104_02 — Erratum de signo y traducción corregida de Lagarias hacia A1

**Rol:** auditar el signo del término de Li incompleto antes de usar el Teorema 6.1 de
Lagarias. Este documento sustituye íntegramente la traducción anterior.

**Estado vinculante.** Las ecuaciones impresas (1.15), (1.17), (6.2) y el paso (6.7) de
Lagarias tienen el signo opuesto al residuo del integrando que aparece en su propia prueba.
Por tanto se retiran el antiguo Teorema A, su forma A′ y los antiguos corolarios B1–B2. La
coordenada exacta correcta de A1 contiene
\(-\lambda_n(\sqrt n)\), no \(+\lambda_n(\sqrt n)\).

La búsqueda realizada el 25-jul-2026 en la ficha de arXiv math/0404394, la página del artículo
en Numdam y los resultados enlazados desde ambas **no localizó un corrigendum**. Esto no
convierte el erratum en una corrección oficial del autor: es una auditoría interna basada en
el cálculo de residuos reproducido abajo.

---

## 1. Enunciado impreso y cálculo local del residuo

Lagarias define (ec. (1.14), también (6.1))

\[
\lambda_n(T,\pi)=
\sum_{\substack{\rho\in Z(\pi)\\ |\Im\rho|<T}}
\left[1-\left(1-\frac1\rho\right)^n\right]
\]

y en (6.4)

\[
k_n(s)=\left(1+\frac1s\right)^n-1.
\]

El integrando de la prueba del Teorema 6.1 es

\[
F_n(s)=k_n(s)\left(-\frac{L'}L(s+1,\pi)\right).
\]

Sea \(\rho\) un cero no trivial de multiplicidad \(m_\rho\), y sea
\(s_0=\rho-1\). Localmente,

\[
\frac{L'}L(s+1,\pi)=\frac{m_\rho}{s-s_0}+O(1).
\]

Luego, sin convención global ni estimación alguna,

\[
\boxed{
\mathop{\mathrm{Res}}_{s=\rho-1}F_n(s)
=-m_\rho k_n(\rho-1)
=m_\rho\left[1-\left(\frac{\rho}{\rho-1}\right)^n\right].}
\tag{1.1}
\]

El signo menos procede exclusivamente de \(-L'/L\). La prueba impresa usa en la deformación
el residuo \(+m_\rho k_n(\rho-1)\).

Sean \(C_1\) el círculo pequeño y \(C_2\) el rectángulo grande, ambos orientados en sentido
antihorario como en el artículo. Para contornos anidados,

\[
\frac1{2\pi i}\int_{C_2}F_n
-\frac1{2\pi i}\int_{C_1}F_n
=\sum_{C_2\setminus C_1}\mathrm{Res}\,F_n.
\tag{1.2}
\]

Hay aquí una segunda inconsistencia tipográfica en la fuente: §6 define
\(I_2=\int_{C_2}F_n(s)\,ds\), sin \((2\pi i)^{-1}\), pero la ecuación (6.7)
lo usa como integral normalizada. Para no heredar esa ambigüedad, definimos

\[
 \widehat I_2(n):={1\over2\pi i}\int_{C_2}F_n(s)\,ds.           \tag{1.3}
\]

La integral normalizada sobre \(C_1\) es \(S_f(n,\pi)\). Además, usando la simetría de ceros
empleada en el propio artículo,

\[
\sum_{\substack{\rho\in Z(\pi)\\|\Im\rho|<T}}
m_\rho k_n(\rho-1)
=-\lambda_n(T,\pi^\vee).
\tag{1.4}
\]

Al combinar (1.1)–(1.4), la ecuación (6.7) corregida y normalizada es

\[
\boxed{
\widehat I_2(n)=S_f(n,\pi)+\lambda_n(T,\pi^\vee)+O(1),}
\tag{1.5}
\]

no \(S_f-\lambda_n(T,\pi^\vee)+O(1)\). El resto de la estimación de contorno de §6 prueba
\(\widehat I_2(n)=O_\pi(\sqrt n\log n)\), pero no literalmente con su elección
impresa \(T=\sqrt n+\varepsilon_n\). Hay que reparar también ese punto antes de
extraer la conclusión.

### 1.1. Reparación del tramo horizontal

La ecuación impresa (6.12) solo da, al avanzar una unidad hacia la derecha,

\[
 {\lvert k_n(s+1)+1\rvert\over\lvert k_n(s)+1\rvert}
 \le e^{n/T^2}.
\]

Con \(T^2=n\), combinarla con el factor \(1/2\) del mayorante de la serie de
Dirichlet produce \(e/2>1\), no decrecimiento geométrico. Fijamos en cambio

\[
 T=2\sqrt n+\varepsilon_n,\qquad 0<\varepsilon_n<1,                 \tag{1.6a}
\]

escogido a distancia \(\gg_\pi1/\log n\) de toda ordenada de cero en esa
banda. Tal elección existe por el conteo local de ceros usado en el propio
artículo.

En los lados horizontales \(s=\sigma\pm iT\), para \(\lvert\sigma\rvert\le3\),

\[
 \left\lvert1+{1\over s}\right\rvert^2
 =1+{2\sigma+1\over\sigma^2+T^2}
 \le1+{7\over4n},
\]

de modo que \(\lvert k_n(s)\rvert\le e^{7/8}+1\); la fórmula (6.8) y la
separación elegida dan \(\lvert L'/L(s+1,\pi)\rvert\ll_\pi(\log n)^2\).
Para \(\sigma\ge3\), póngase

\[
 G_n(s)=k_n(s)+1=\left(1+{1\over s}\right)^n.
\]

La identidad exacta

\[
 {G_n(s+1)\over G_n(s)}
 =\left(1-{1\over(s+1)^2}\right)^n
\]

implica

\[
 \left\lvert{G_n(s+1)\over G_n(s)}\right\rvert
 \le(1+T^{-2})^n\le e^{1/4}.                       \tag{1.6b}
\]

Por convergencia absoluta del logaritmo de Euler, el **mayorante absoluto**
de la serie de Dirichlet de \(L'/L(s+1,\pi)\) gana un factor a lo sumo
\(1/2\) al aumentar \(\sigma\) en una unidad. Dentro de cada celda,
\(0\le t\le1\), se tiene además

\[
 \left({1+1/(s+t)\over1+1/s}\right)^n
 =\left(1-{t\over(s+t)(s+1)}\right)^n,
\]

cuyo módulo es a lo sumo \((1+T^{-2})^n\le e^{1/4}\). Por tanto el mayorante del
término \(G_n(s)L'/L(s+1,\pi)\) decrece por bloques con razón

\[
 q={e^{1/4}\over2}<1,                               \tag{1.6c}
\]

y el término procedente de \(k_n=G_n-1\) decrece al menos con razón
\(1/2\). Esto prueba la integrabilidad geométrica de los dos lados
horizontales. Los lados verticales conservan la cota
\(O_\pi(\sqrt n\log n)\), pues cambiar \(T\) por un factor fijo no altera
su argumento. En consecuencia,

\[
 \widehat I_2(n)=O_\pi(\sqrt n\log n).              \tag{1.6d}
\]

Finalmente, si \(\sqrt n\le\lvert\gamma\rvert\le2\sqrt n+1\) y
\(0<\beta<1\), entonces

\[
 \left\lvert1-{1\over\rho}\right\rvert^{2n}
 =\left(1+{1-2\beta\over\lvert\rho\rvert^2}\right)^n
 \le(1+1/n)^n\le e.                                \tag{1.6e}
\]

Cada sumando de Li en esa banda tiene módulo a lo sumo \(1+e^{1/2}\), y
el conteo de ceros da \(O_\pi(\sqrt n\log n)\) ceros. Por ello

\[
 \lambda_n(2\sqrt n+\varepsilon_n,\pi^\vee)
 -\lambda_n(\sqrt n,\pi^\vee)
 =O_\pi(\sqrt n\log n).                            \tag{1.6f}
\]

Las ecuaciones (1.5) y (1.9)--(1.11) prueban, ya con el hueco horizontal
reparado, que

\[
\boxed{
S_f(n,\pi)=-\lambda_n(\sqrt n,\pi^\vee)
+O_\pi(\sqrt n\log n).}
\tag{L1c}
\]

Ésta es la versión corregida de las ecuaciones impresas (1.15) y (6.2).

### 1.2. Otra errata de signo adyacente que no se importa

La especialización a \(\zeta\) impresa en (4.13) escribe

\[
 S_f(n,\pi_{\rm triv})
 =\sum_{j=1}^n(-1)^{j-1}{n\choose j}\eta_{j-1}.       \tag{1.6}
\]

Ese factor alternante contradice simultáneamente:

1. la Definición 4.2,
   \(-\zeta'/\zeta(1+s)=s^{-1}+\sum_{j\ge0}\eta_js^j\);
2. la definición general (4.8),
   \(S_f(n)=\sum_{j=1}^n{n\choose j}\eta_{j-1}\);
3. la extracción del residuo en el círculo pequeño (6.5), porque
   \(k_n(s)=\sum_{j=1}^n{n\choose j}s^{-j}\).

Ya en \(n=2\), (4.8)/(6.5) dan \(2\eta_0+\eta_1\), mientras (4.13) da
\(2\eta_0-\eta_1\). La cadena usada aquí adopta la definición y el residuo
general, sin alternancia. Esta errata adyacente no cambia (L1c), pero confirma
que los signos de §4--§6 deben recalcularse y no copiarse por referencia.

Para una representación no autodual, el PDF publicado también mezcla
\(\pi\) y \(\pi^\vee\) en (4.6). La forma compatible con la derivación es

\[
 \lambda_n(\pi)=S_\infty(n,\pi^\vee)-S_f(n,\pi^\vee)+\delta(\pi), \tag{1.7}
\]

o su dual. Como \(S_\infty(n,\pi)=S_\infty(n,\pi^\vee)\) y \(\zeta\) es
autodual, esta inconsistencia editorial tampoco altera la especialización A1.

---

## 2. Asintótica incondicional corregida

La fórmula aritmética exacta del artículo es

\[
\lambda_n(\pi)=S_\infty(n,\pi^\vee)-S_f(n,\pi^\vee)+\delta(\pi^\vee).
\tag{2.1}
\]

Con
\(S_\infty(n,\pi)=\frac N2n\log n+C_1(\pi)n+O_\pi(1)\)
y (L1c), resulta

\[
\boxed{
\lambda_n(\pi)=\frac N2n\log n+C_1(\pi)n
+\lambda_n(\sqrt n,\pi)+O_\pi(\sqrt n\log n).}
\tag{L2c}
\]

Así, la ecuación impresa (1.17) debe llevar signo **más** delante del coeficiente incompleto.
La fórmula bajo RH no cambia, porque bajo RH
\(\lambda_n(\sqrt n,\pi)=O_\pi(\sqrt n\log n)\).

Para \(\zeta\), \(N=1\), \(Q=1\), \(\pi^\vee=\pi\) y

\[
C_1=\frac12(\gamma-1-\log2\pi).
\]

Nuestro bloque exacto satisface

\[
A_n=\frac n2(\log n+\gamma-1-\log2\pi)+O(\log n).
\tag{2.2}
\]

Definimos el resto exacto con el signo corregido:

\[
\boxed{
\widetilde\varepsilon_n:=A_n-\lambda_n+\lambda_n(\sqrt n).}
\tag{2.3}
\]

Es un número real, no un símbolo \(O\). De (L2c) y (2.2) se obtiene

\[
\boxed{
|\widetilde\varepsilon_n|\le C_*\sqrt n\log n}
\qquad(n\ge2),
\tag{2.4}
\]

para alguna constante absoluta \(C_*>0\) no explicitada por el argumento de Lagarias.

La cantidad usada en la versión retirada era

\[
\varepsilon_n^-:=A_n-\lambda_n-\lambda_n(\sqrt n).
\]

Las dos se relacionan exactamente por

\[
\boxed{
\varepsilon_n^-=\widetilde\varepsilon_n-2\lambda_n(\sqrt n).}
\tag{2.5}
\]

Por tanto **no** se dispone incondicionalmente de
\(|\varepsilon_n^-|\ll\sqrt n\log n\). Si RH falla, el segundo término de (2.5) puede ser
exponencial sobre una subsucesión. La antigua afirmación de que solo faltaba efectivizar una
constante para \(\varepsilon_n^-\) queda retirada.

---

## 3. Forma lado-primo corregida

Sea

\[
\mathcal J_n:=\int_0^\infty E(u)K_n(u)\,du,
\qquad
\lambda_n=A_n-n-\mathcal J_n.
\tag{3.1}
\]

Por la definición (2.3), sin usar ninguna estimación,

\[
\boxed{
\mathcal J_n+n=-\lambda_n(\sqrt n)+\widetilde\varepsilon_n.}
\tag{A'_c}
\]

Ésta reemplaza el antiguo Teorema A′. El término incompleto entra con signo menos.

---

## 4. A1 en la coordenada corregida

Sea \(a=\log2\), \(\theta\in(0,\tfrac12)\), sea \(T_n(\theta)\) como en 104_01, y

\[
q_{n,\theta}=(1-\theta)A_n+1-L_n^{(1)}(a).
\]

La descomposición exacta ya probada da

\[
\mathrm{A1}_\theta
\iff
\mathcal J_n+n+R_n(T_n(\theta))\le(1-\theta)A_n.
\tag{4.1}
\]

Sustituyendo (A′c), obtenemos el enunciado exacto que sustituye al antiguo Teorema B:

\[
\boxed{
\mathrm{A1}_\theta
\iff
-\lambda_n(\sqrt n)+\widetilde\varepsilon_n
+R_n(T_n(\theta))\le(1-\theta)A_n.}
\tag{B_c}
\]

No hay un \(O\) en esta equivalencia. Tanto
\(\widetilde\varepsilon_n\) como \(R_n\) conservan su signo exacto.

Equivalentemente,

\[
\lambda_n(\sqrt n)
\ge -(1-\theta)A_n+\widetilde\varepsilon_n+R_n(T_n(\theta)).
\tag{4.2}
\]

Así, la traducción corregida reduce la dificultad a una **cota inferior**, no superior, para
el bloque incompleto.

### Corolarios unilaterales corregidos

Usando (2.4) y \(|R_n(T_n(\theta))|\le\theta A_n\):

\[
\boxed{
\lambda_n(\sqrt n)\ge
-(1-2\theta)A_n+C_*\sqrt n\log n
\quad\Longrightarrow\quad\mathrm{A1}_\theta.}
\tag{B1_c}
\]

Recíprocamente,

\[
\boxed{
\mathrm{A1}_\theta
\quad\Longrightarrow\quad
\lambda_n(\sqrt n)\ge-A_n-C_*\sqrt n\log n.}
\tag{B2_c}
\]

La brecha entre ambas condiciones sigue siendo
\(2\theta A_n+2C_*\sqrt n\log n\), pero ahora ambas son cotas **inferiores**. Ninguna puede
reemplazarse por una cota superior del coeficiente incompleto.

Para \(\theta=\tfrac14\), el objetivo exacto queda

\[
\boxed{
-\lambda_n(\sqrt n)+\widetilde\varepsilon_n+R_n(T_n(\tfrac14))
\le\frac34A_n,\qquad n\ge150.}
\tag{4.3}
\]

---

## 5. Qué sí controla una altura verificada

Si todos los ceros con \(|\gamma|<\sqrt n\) están en la línea crítica, cada par aporta

\[
2-2\cos(n\theta_\rho)\in[0,4],
\]

y por tanto

\[
0\le\lambda_n(\sqrt n)\le4N(\sqrt n).
\tag{5.1}
\]

Para la coordenada corregida importa ya la primera desigualdad. De (B1c), una condición
suficiente es

\[
C_*\sqrt n\log n\le(1-2\theta)A_n,
\tag{5.2}
\]

junto con la localización de los ceros hasta \(\sqrt n\). Como \(C_*\) no está explicitada,
esto no produce por sí solo un rango numérico certificado. Y, aunque se explicitara, seguiría
siendo un corolario finito: no prueba A1 uniformemente.

La discrepancia editorial entre
\(T^2/[2(\log T)^2]\) en el artículo publicado y
\(T^2/[4(\log T)^2]\) en la fuente arXiv se conserva como dato bibliográfico, pero no entra en
el cierre de A1.

---

## 6. Cuarteto fuera de la línea y dirección crítica

Sea \(w_\rho=1-1/\rho\). Para un cuarteto simétrico fuera de la línea puede escribirse
\(w=e^{\alpha+i\vartheta}\), con \(\alpha>0\), y la contribución completa es

\[
4-4\cosh(n\alpha)\cos(n\vartheta).
\tag{6.1}
\]

Una vez que la altura del cuarteto es menor que \(\sqrt n\), la misma contribución aparece en
\(\lambda_n(\sqrt n)\). Toma valores exponencialmente grandes de ambos signos a lo largo de
subsucesiones, con la formulación precisa de Bombieri–Lagarias para evitar suponer una fase
aislada. Por eso una cota inferior uniforme como (4.2) sigue siendo RH-strength.

El factor \(4\) corresponde al coeficiente de Li, que suma una vez los cuatro ceros. La forma
de Weil/autocorrelación \(2\mathrm{Re}\,\lambda_n\) duplica esta expresión y produce
\(8-8\cosh(n\alpha)\cos(n\vartheta)\); no deben mezclarse ambas normalizaciones.

El erratum no prueba A1; identifica correctamente el lado que debe atacarse.

---

## 7. Verificación diagnóstica

La herramienta tools/lagarias_translation_check.py calcula ahora

\[
\widetilde D_n:=\lambda_n-A_n-\lambda_n(\sqrt n)
=-\widetilde\varepsilon_n,
\tag{7.1}
\]

no el residual antiguo
\(\lambda_n-A_n+\lambda_n(\sqrt n)\). Usa dos radios para detectar inestabilidad de la
extracción de Cauchy. El resultado es exclusivamente diagnóstico en float64; no certifica
\(C_*\), ni A1, ni RH.

El test decisivo de signo es algebraico y está en (1.1): el programa solo comprueba que los
datos numéricos de bajo rango son consistentes con la traducción corregida.

**Corrida del 25-jul-2026.** Las filas estables entre los dos radios llegan hasta \(n=1600\);
\(n=2000\) y \(n=2400\) son descartadas por la guarda del 1 %. En la muestra estable,
\[
\max\frac{|\widetilde D_n|}{\sqrt n\log n}=0.2457
\]
se alcanza en \(n=8\). Estas cifras no son intervalos certificados ni una constante efectiva.

---

## 8. Ledger vinculante

1. **Retirado:**
   \(A_n-\lambda_n=+\lambda_n(\sqrt n)+O(\sqrt n\log n)\).
2. **Retirado:**
   \(|A_n-\lambda_n-\lambda_n(\sqrt n)|\ll\sqrt n\log n\) incondicional.
3. **Retirados:** los antiguos B1 y B2, que pedían cotas superiores del bloque incompleto.
4. **Adoptado:**
   \(A_n-\lambda_n=-\lambda_n(\sqrt n)+\widetilde\varepsilon_n\), con
   \(|\widetilde\varepsilon_n|\le C_*\sqrt n\log n\).
5. **Objetivo exacto:** (4.3), equivalente a A1, que exige controlar por abajo el bloque
   incompleto junto con los dos restos con signo.
