# 104_17 — Bloque incompleto: stop-gate Abel--Fejér tras el erratum

**Rol.** Primer ataque a la cota inferior que queda después de corregir el
signo de Lagarias. No prueba A1. Descarta una familia precisa: obtener el
signo coeficiente a coeficiente desde positividad radial Abel o desde
promedios Cesàro/Fejér del bloque incompleto.

La coordenada correcta de `104_02` es

\[
 \mathrm {A1}_{\theta}
 \iff
 -\lambda_n(\sqrt n)+\widetilde\varepsilon_n
 +R_n(T_n(\theta))\le(1-\theta)A_n.                 \tag{1}
\]

Por tanto hace falta una cota **inferior** para
\(\lambda_n(\sqrt n)\). El promedio no puede sustituirla sin un teorema
Tauberiano firmado.

## 1. Auditoría de no duplicación interna

`103_27` y `103_28` ya prueban que la positividad puntual de Fejér sobre el
círculo no sobrevive a un cuarteto recíproco fuera de la línea. Este
documento no repite ese resultado. Añade:

1. las sumas acumulada y triangular exactas del cuarteto;
2. un teorema de positividad Abel radial para **todo** cuarteto, incluso
   fuera de la línea;
3. un testigo racional donde el germen Abel es positivo pero el coeficiente
   y el promedio triangular son negativos.

La extensión identifica por qué un argumento Tauberiano radial no puede ser
el mecanismo faltante.

## 2. Contribución exacta de un cuarteto

Sea \(\rho=\beta+i\gamma\), con \(0<\beta<1\), \(\gamma\ne0\) y
\(\beta\ne\tfrac12\), y sea

\[
 \mathcal O(\rho)=\{\rho,\bar\rho,1-\rho,1-\bar\rho\}.
\]

Póngase

\[
 w_\eta=1-{1\over\eta},\qquad
 w=w_\rho=re^{i\vartheta}=e^{a+i\vartheta}.
\]

Las simetrías dan

\[
 w_{\bar\rho}=\bar w,qquad
 w_{1-\rho}=w^{-1},\qquad
 w_{1-\bar\rho}=\bar w^{-1}.                       \tag{2}
\]

La contribución del cuarteto al coeficiente de Li es, por tanto,

\[
\begin{aligned}
 Q_n
 &:=\sum_{\eta\in\mathcal O(\rho)}(1-w_\eta^n)\\
 &=4-(w^n+\bar w^n+w^{-n}+\bar w^{-n})\\
 &=\boxed{\,4-2(r^n+r^{-n})\cos(n\vartheta)\,}\\
 &=4-4\cosh(an)\cos(n\vartheta).                  \tag{3}
\end{aligned}
\]

El factor es \(4\), no \(8\). La forma de Weil
\(2\mathrm{Re}\,\lambda_n\) duplica (3); esa es la fuente del factor
\(8\) en `103_69` y `104_14`.

## 3. Los dos promedios finitos conservan la obstrucción exponencial

Defínanse

\[
 G_N(z)=\sum_{n=1}^Nz^n={z(1-z^N)\over1-z},
\]

y

\[
 V_N(z)=\sum_{n=1}^N(N+1-n)z^n
 ={z\{N-(N+1)z+z^{N+1}\}\over(1-z)^2}.             \tag{4}
\]

Sumando (3) se obtiene exactamente

\[
 \sum_{n=1}^NQ_n
 =4N-2\mathrm{Re}\,\{G_N(w)+G_N(w^{-1})\},     \tag{5}
\]

y, para el promedio triangular,

\[
 \sum_{n=1}^N(N+1-n)Q_n
 =2N(N+1)-2\mathrm{Re}\,\{V_N(w)+V_N(w^{-1})\}.\tag{6}
\]

Si \(r>1\), las partes dominantes de (5)--(6) son, respectivamente,

\[
 2\mathrm{Re}{w^{N+1}\over1-w},
 \qquad
 -2\mathrm{Re}{w^{N+2}\over(1-w)^2}.        \tag{7}
\]

Luego las dos sumaciones retienen una carga de tamaño \(r^N\); no la
convierten en un error polinómico. El mismo cálculo, tras un número fijo de
sumaciones, solo añade una potencia fija de \((1-w)^{-1}\) y conserva
\(r^N\).

## 4. Teorema: positividad Abel radial de toda órbita funcional

Defínase

\[
 \mathcal A_\rho(q)=\sum_{n\ge1}Q_nq^n.
\]

La serie converge ordinariamente para
\(0<q<e^{-|a|}=\min(r,r^{-1})\).

**Teorema.** Para todo \(q\) en ese intervalo,

\[
 \boxed{
 \mathcal A_\rho(q)
 ={2q(1+q)\over(1-q)^3}{X\over X^2+Y^2}>0,}         \tag{8}
\]

donde

\[
 x={q\over1-q},\qquad
 X=(x+\beta)(x+1-\beta)+\gamma^2>0,qquad
 Y=\gamma(1-2\beta).                                \tag{9}
\]

El miembro racional de (8) continúa como función estrictamente positiva
sobre todo \(0<q<1\). La igualdad con la **serie** se afirma solo dentro de
su radio de convergencia.

*Demostración.* Para cada \(\eta\in\mathcal O(\rho)\),

\[
\begin{aligned}
 \sum_{n\ge1}q^n(1-w_\eta^n)
 &= {q\over1-q}-{qw_\eta\over1-qw_\eta}\\
 &= {q(1-w_\eta)\over(1-q)(1-qw_\eta)}
  ={q\over(1-q)^2}{1\over x+\eta}.                 \tag{10}
\end{aligned}
\]

En la última igualdad se usaron
\(1-w_\eta=1/\eta\) y
\(1-qw_\eta=((1-q)\eta+q)/\eta\). Sumando el cuarteto,

\[
 \mathcal A_\rho(q)
 ={2q\over(1-q)^2}\mathrm{Re}
 \left({1\over x+\rho}+{1\over x+1-\rho}\right).  \tag{11}
\]

El paréntesis es

\[
 {1+2x\over(x+\rho)(x+1-\rho)},                   \tag{12}
\]

y

\[
 (x+\rho)(x+1-\rho)=X+iY.                         \tag{13}
\]

Como \(\mathrm{Re}(X+iY)^{-1}=X/(X^2+Y^2)\) y
\(1+2x=(1+q)/(1-q)\), (8) sigue de (11)--(13). Todos
los factores son estrictamente positivos. \(\square\)

Si \(\beta=\tfrac12\), las cuatro etiquetas duplican el par conjugado; se
divide (8) por dos y la positividad permanece.

## 5. Testigo racional exacto

Tómese

\[
 \rho={1+2i\over5},\qquad w=2i.
\]

La aritmética exacta de (3) da

\[
\begin{array}{c|rrrrrrrr}
n&1&2&3&4&5&6&7&8\\ \hline
Q_n&4&25/2&4&-225/8&4&4225/32&4&-65025/128.
\end{array}                                                     \tag{14}
\]

Con

\[
 C_N=\sum_{n=1}^NQ_n,qquad
 F_N=\sum_{n=1}^N(N+1-n)Q_n,
\]

se obtiene

\[
 \boxed{
 Q_4=-{225\over8},\quad C_4=-{61\over8},\quad
 F_4={267\over8}>0,\quad F_8=-{10885\over128}<0.} \tag{15}
\]

Así, \(F_4\) enmascara el coeficiente negativo, pero \(F_8\) prueba que
el promedio tampoco conserva positividad. En cambio, para \(0<q<1/2\),

\[
 \boxed{
 \mathcal A_\rho(q)
 ={4q\over1-q}+{8q^2\over1+4q^2}+{2q^2\over4+q^2}>0,}          \tag{16}
\]

aunque

\[
 Q_{4k}=4-2(2^{4k}+2^{-4k})\longrightarrow-\infty.             \tag{17}
\]

## 6. Por qué no hay transferencia al cutoff móvil

Para una altura fija \(T\), si

\[
 \lambda_n(T)=\sum_{|\Im\rho|<T}(1-w_\rho^n),
\]

entonces

\[
 \Delta^k\lambda_n(T)
 =(-1)^{k-1}\sum_{|\Im\rho|<T}{w_\rho^n\over\rho^k},
 \qquad k\ge1.                                      \tag{18}
\]

No tiene signo. Para \(T=\sqrt n\), la diferencia contiene además los
ceros del cascarón
\([\sqrt n,\sqrt{n+1})\), también sin signo. Las identidades de recuperación

\[
 Q_N=C_N-C_{N-1},qquad
 Q_N=F_N-2F_{N-1}+F_{N-2}                           \tag{19}
\]

muestran la pérdida exacta: una cota de tamaño para \(C_N\) o \(F_N\) no
controla la diferencia firmada requerida. Una hipótesis de variación fuerte
suficiente para (19) ya excluiría (15)--(17) y contendría el mismo dato
RH-strength.

## 7. Decisión

```text
probado:
  fórmulas exactas del cuarteto y de sus dos sumaciones;
  positividad Abel radial estricta incluso para cuartetos off-line;
  testigo racional con coeficiente y promedio Fejér negativos;
  ausencia de signo en las diferencias con cutoff fijo o móvil.

descartado como fuente autónoma de A1:
  positividad Abel radial;
  un número fijo de promedios Cesàro/Fejér;
  transferencia Tauberiana sin una hipótesis angular o de variación nueva.

no descartado:
  una identidad específica de los pesos reales de zeta que controle
  simultáneamente el ángulo y la recuperación coeficiente a coeficiente.

no probado:
  la cota inferior de lambda_n(sqrt n), A1 o RH.
```

El sucesor natural no es otro promedio radial. El control angular uniforme
es el gate Toeplitz--Herglotz/Weil ya auditado en phases 102--103. El frente
que se ensaya a continuación conserva, en cambio, el cociclo Euler--polo a
desplazamiento finito correlacionado \(u=c\varepsilon\), que `104_16` no
eliminó.

## 8. Reproducción exacta

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 incomplete_abel_stop_gate_check.py
```

El programa usa solo `Fraction`: certifica (14)--(15) y compara las dos
formas racionales de (8)/(16) en tres valores racionales de \(q\). La
positividad para todo el intervalo es el argumento algebraico de (8)--(13),
no un muestreo numérico.
