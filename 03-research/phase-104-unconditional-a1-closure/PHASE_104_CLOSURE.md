# Phase 104 — Documento de cierre

## Veredicto

Phase 104 queda cerrada sin una demostración de A1 y sin una demostración
de la Hipótesis de Riemann. Su resultado permanente es una delimitación
adversarial del problema: identifica varias formulaciones exactamente
equivalentes, demuestra numerosos stop-gates con testigos y retira todas
las afirmaciones que confundían una equivalencia con una cota nueva.

El frente literal permanece

\[
 \boxed{
 \int_{\log2}^{T_n}
   (\psi(e^u)-e^u)e^{-u}L_{n-1}^{(2)}(u)\,du
 \le {3\over4}A_n+1-L_n^{(1)}(\log2),\qquad n\ge150.}
                                                               \tag{A1}
\]

Con A0 y los certificados finitos, A1 implica
(\lambda_n\ge0) para todo (n), y por el criterio de Li implica RH.
No existe en esta fase un argumento incondicional que pruebe (A1).

## 1. Cadena exacta conservada

Defina

\[
 E(u)=\psi(e^u)-e^u,qquad
 K_n(u)=e^{-u}L_{n-1}^{(2)}(u),
\]

\[
 R_n(T)=-\int_T^\infty E(u)K_n(u)\,du,
 \qquad A_n=\lambda_n^{\rm arch}.
\]

La identidad compacta--cola es

\[
 C_n^{1/4}(T)
 ={3\over4}A_n-n-\int_0^T E(u)K_n(u)\,du
 =\lambda_n-{1\over4}A_n-R_n(T).                         \tag{1}
\]

Como (E(u)=-e^u) en (0<u<\log2), el término (-n) se cancela
exactamente con el borde sin primos. Así (1) da

\[
 C_n^{1/4}(T)
 ={3\over4}A_n+1-L_n^{(1)}(\log2)
 -\int_{\log2}^T E(u)K_n(u)\,du.                         \tag{2}
\]

La cota A0 controla la cola. Por tanto (C_n^{1/4}(T_n)\ge0), es decir
A1, entrega (\lambda_n\ge0). Esta cadena está probada; el signo de la
integral compacta no lo está.

## 2. Ganancias permanentes

1. **Normalización exacta.** Se fijaron todos los bordes, signos y
   regularizaciones prima--polo. El erratum del término (-n) es
   vinculante.
2. **Cutoff cofinal.** Al ampliar el cutoff, la condición suficiente se
   aproxima a (4\lambda_n>A_n); las constantes (2002/501) no son una
   coercividad intrínseca.
3. **Cuantificador debilitado.** Si RH es falsa, los coeficientes de Li
   tienen excursiones exponenciales de ambos signos sobre conjuntos
   sindéticos. Bastan barreras subexponenciales en bloques de longitud no
   acotada.
4. **Localización de altura.** Para el umbral profundo (e^{\sqrt X}),
   la cola alta queda controlada y todo posible fallo se concentra en
   ceros de altura (O(X^{1/4})).
5. **Factor interior aislado.** El límite Deep satisface
   
   \[
    \Omega_X\to0
    \iff B_{\rm Blaschke}\equiv1
    \iff \mathrm{RH}.                                    \tag{3}
   \]
6. **Detector local.** El defecto Poisson--Jensen es exactamente el
   potencial de Green del factor interior; detecta cualquier cero derecho
   sin pérdida.
7. **Gate resolvente final.** El generador global de intercambios de
   torres no existe en el régimen Abel, y el cruzado escalar es cero.
   La identidad Mecke triangular sí fue demostrada, pero es circulación
   bilineal y no la fuente lineal prima--polo (B_{n,s}).

## 3. Familias cerradas como mecanismos autónomos

Quedaron descartadas, siempre con identidad o testigo explícito, las rutas
basadas únicamente en:

* cotas puntuales PNT/Vinogradov--Korobov y valores absolutos;
* positividad local, PSD, PF2/TP2, SOS o medidas completamente monótonas;
* Selberg--Riccati sin un input firmado nuevo;
* Markov/Stein/Palm de primer o segundo orden;
* filtros lineales, Fejér y promedios por bloques;
* resolventes translation-invariant y el resolvente escalar de torres;
* factorizaciones Euler locales, Möbius o Landau positivas;
* Jensen, Cartan, Turán o Blaschke usados solo como detectores;
* PNT continuo, regiones libres conocidas, densidad de ceros o
  verificación hasta altura finita.

Estos gates no prueban que A1 sea falsa. Prueban que esas fuentes de
información no suministran el signo que falta.

## 4. Dos blancos que no deben confundirse

### A1

A1 es una sucesión de desigualdades, una por cada (n\ge150). Si

\[
 J_n(U)=\int_{\log2}^{U}E(u)K_n(u)\,du,qquad
 q_n={3\over4}A_n+1-L_n^{(1)}(\log2),                    \tag{4}
\]

hay que probar

\[
 J_n(T_n)\le q_n\quad\hbox{para todo }n\ge150.           \tag{5}
\]

No es, por sí misma, una afirmación de convergencia en (n).

### Límite Deep

Para (S_X=e^{\sqrt X}),

\[
 \Omega_X={1\over H_X}\sum_{n\le X}{1\over n}
 \mathbf1_{\{\lambda_n+\log(n+1)\le-S_X\}}.             \tag{6}
\]

Aquí sí hay un límite literal:

\[
 \boxed{\Omega_X\longrightarrow0.}                      \tag{7}
\]

Bajo RH el observable termina siendo exactamente cero. Si existe un cero
fuera de la línea, su liminf es positivo. Probar (7) para los primos
ordinarios también probaría RH, pero Phase 104 no obtuvo ese límite.

## 5. Handoff a Phase 105

Phase 105 comienza con una representación gráfica reproducible de (4)--(7):

* la curva acumulada (J_n(U)), su barrera (q_n) y la región prohibida;
* la diferencia entre el tramo aritméticamente computable y el cutoff
  efectivo completo;
* el comportamiento de (\Omega_X) en el caso on-line y en un cuarteto
  off-line de control.

La nueva fase no hereda ningún supuesto de positividad ni ningún
certificado resolvente de Phase 104.

## Estado final

* **Probado:** identidades, equivalencias, cutoffs, localizaciones,
  detectores y stop-gates registrados en el README de la fase.
* **No probado:** A1 para todo (n\ge150), (\Omega_X\to0) para los
  primos ordinarios, la ausencia del factor de Blaschke interior y RH.
* **Prohibido citar:** Phase 104 como demostración de RH.

