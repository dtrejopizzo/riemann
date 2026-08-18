# 104_54 — Gate Gibbs--Chernoff del defecto Palm unitario

**Resultado.** El frente no aditivo sugerido por `104_50` no admite una
cota de Chernoff. Para

\[
 f_{n,s}(x)=L_{n-1}^{(1)}(sx),\qquad s>1,                 \tag{1}
\]

sea el defecto unitario

\[
 D_{n,s}(N)=
 \sum_{p^{a_p}\parallel N}(\log p)
       \sum_{k=1}^{a_p}f_{n,s}(k\log p)
 -{1-L_n(s\log N)\over s}.                               \tag{2}
\]

Entonces, para todo entero \(n\ge4\), en particular para todo
\(n\ge150\),

\[
 \boxed{\mathbb E_s e^{tD_{n,s}}=+\infty
        \quad\hbox{para cada }t\in\mathbb R\setminus\{0\}.} \tag{3}
\]

La obstrucción es bilateral y aritmética. Sobre primos grandes,
\(D_{n,s}\) tiene signo \((-1)^{n-1}\) y tamaño
\(\asymp(\log p)^n\). Sobre productos de dos primos con logaritmos
comparables tiene el signo contrario y el mismo orden. El peso zeta
\(N^{-s}\) solo aporta \(-s\log N\) al logaritmo del sumando; no puede
competir con \(c(\log N)^n\).

Reinsertar el polo no cambia el veredicto. La variable completada de
`104_50`,

\[
 Z_{n,s}=D_{n,s}+T_s(f_{n,s}),                              \tag{4}
\]

difiere de \(D_{n,s}\) por una constante finita. Lo mismo ocurre al
restar el presupuesto \(\kappa A_n/s\),
\(\kappa=1501/2002\). Por tanto ninguna de las tres variables posee un
momento exponencial no trivial en ninguno de los dos signos.

La forma variacional de Gibbs confirma que esto no es una mala elección
del parámetro. Para \(t\ne0\), medidas delta apoyadas en las sucesiones
prima o semiprima hacen

\[
 t\,\mathbb E_QD_{n,s}-\operatorname{KL}(Q\|\mathbb P_s)
 \longrightarrow+\infty.                                  \tag{5}
\]

Así, el mejor bound entrópico es literalmente \(+\infty\). No aparece
una desigualdad finita que pueda compararse con

\[
 B_n\le{1501\over2002}A_n.                                 \tag{6}
\]

El falsificador desplazado pasa este gate. Para
\(Z_c(s)=\zeta(s+c)\zeta(s-c)\), el selector correcto coincide
**exactamente** con el unitario sobre primos y semiprimos squarefree. Las
mismas dos sucesiones prueban divergencia bilateral de su Gibbs funcional,
aunque la completada \(\xi(s+c)\xi(s-c)\) tenga ceros fuera de la línea
crítica.

Queda descartado el mecanismo estrecho

```text
defecto Palm unitario antes de centrar
+ tilt exponencial / Gibbs / Chernoff
+ optimización en t
    => cota unilateral proporcional para B_n.
```

No se descarta una transformación acotada o truncada acompañada de un
teorema aritmético uniforme de colas. Tal teorema tendría que controlar
precisamente las dos sucesiones que causan (3), y no sería una consecuencia
de Chernoff. Este documento no prueba (6), A1 ni RH.

## 0. No duplicación interna

`104_49` prueba que el defecto (2) cambia de signo en grado \(151\).
`104_50` construye su covarianza y demuestra que el cuadrado completado
pierde la orientación del margen. `104_52`--`104_53` prueban que cumulantes
conectados cancelan las interacciones entre torres distintas.

Aquí no se cuenta de nuevo ninguno de esos resultados. La adición es la
clasificación completa de integrabilidad exponencial para **cada**
\(n\ge4\), la divergencia de la fórmula variacional por medidas delta y la
transferencia exacta de los dos testigos al divisor desplazado.

## 1. Dos expansiones exactas del defecto

Escriba

\[
 P_n(x)=L_{n-1}^{(1)}(x).
\]

Su coeficiente principal es

\[
 P_n(x)={(-1)^{n-1}\over(n-1)!}x^{n-1}+O_n(x^{n-2}).       \tag{7}
\]

La primitiva exacta es

\[
 \int_0^X P_n(sx)\,dx={1-L_n(sX)\over s}.                 \tag{8}
\]

### 1.1. Fibra prima

Si \(N=p\) y \(x=\log p\), (2) da

\[
 D_{n,s}(p)=xP_n(sx)-{1-L_n(sx)\over s}.                   \tag{9}
\]

Comparando los coeficientes principales de (7)--(8),

\[
 \boxed{
 D_{n,s}(p)
 ={(-1)^{n-1}s^{n-1}(n-1)\over n!}x^n
 +O_{n,s}(x^{n-1}).}                                      \tag{10}
\]

Por tanto existe \(x_0(n,s)\) tal que, para todo primo
\(p>e^{x_0}\),

\[
 \operatorname{sgn}D_{n,s}(p)=(-1)^{n-1},\qquad
 |D_{n,s}(p)|\ge c_{n,s}(\log p)^n                         \tag{11}
\]

con algún \(c_{n,s}>0\).

### 1.2. Fibra de dos torres

Si \(N=pq\), con \(p\ne q\) primos, \(x=\log p\), \(y=\log q\),
la multiplicidad unitaria produce exactamente

\[
 D_{n,s}(pq)=xP_n(sx)+yP_n(sy)
             -{1-L_n(s(x+y))\over s}.                     \tag{12}
\]

Su parte homogénea de grado \(n\) es

\[
 \boxed{
 {(-1)^{n-1}s^{n-1}\over(n-1)!}
 \left\{x^n+y^n-{(x+y)^n\over n}\right\}.}               \tag{13}
\]

Para cada \(J\ge1\), el postulado de Bertrand permite escoger

\[
 2^J<p_J<2^{J+1},\qquad
 2^{J+1}<q_J<2^{J+2}.                                      \tag{14}
\]

Los intervalos son disjuntos y

\[
 {\log p_J\over J\log2}\longrightarrow1,\qquad
 {\log q_J\over J\log2}\longrightarrow1.                \tag{15}
\]

Al dividir (13) por \((J\log2)^n\), el corchete converge a

\[
 2-{2^n\over n}<0\qquad(n\ge4).                            \tag{16}
\]

Los términos de grado menor desaparecen. En consecuencia, para todo
\(J\) suficientemente grande,

\[
 \operatorname{sgn}D_{n,s}(p_Jq_J)=(-1)^n,\qquad
 |D_{n,s}(p_Jq_J)|\ge c'_{n,s}
       \{\log(p_Jq_J)\}^n                                 \tag{17}
\]

con \(c'_{n,s}>0\). Las ecuaciones (11) y (17) dan colas no acotadas de
ambos signos para todo \(n\ge4\).

## 2. Clasificación completa de los momentos exponenciales

La esperanza bajo la ley zeta es

\[
 \mathbb E_se^{tD_{n,s}}
 ={1\over\zeta(s)}\sum_{m\ge1}m^{-s}e^{tD_{n,s}(m)}.       \tag{18}
\]

Todos sus sumandos son positivos. Si \(t(-1)^{n-1}>0\), use la sucesión
prima de (11). Si \(t(-1)^{n-1}<0\), use la sucesión semiprima de (17).
En ambos casos existe \(m_j\to\infty\) tal que

\[
 tD_{n,s}(m_j)-s\log m_j-\log\zeta(s)
 \ge |t|c\{\log m_j\}^n-s\log m_j-\log\zeta(s)
 \longrightarrow+\infty.                                  \tag{19}
\]

Los sumandos de (18) ni siquiera tienden a cero sobre esa subsucesión.
Esto prueba (3).

En contraste, la media ordinaria existe absolutamente. Para una constante
\(C_{n,s}\),

\[
 |D_{n,s}(m)|\le C_{n,s}\{1+(\log m)^n\},                 \tag{20}
\]

y \(\sum m^{-s}(\log m)^n<\infty\). Así, el fallo de Gibbs no
proviene de que el funcional lineal esté indefinido: proviene de colas
más pesadas que cualquier exponencial lineal en \(D_{n,s}\).

Como \(T_s(f_{n,s})\) y \(\kappa A_n/s\) son constantes finitas,

\[
 \mathbb E_s e^{tZ_{n,s}}
 =e^{tT_s(f_{n,s})}\mathbb E_s e^{tD_{n,s}},               \tag{21}
\]

y la misma identidad, con otro factor finito, vale para
\(Z_{n,s}-\kappa A_n/s\). Por (3), ambas esperanzas son infinitas para
todo \(t\ne0\).

## 3. El mejor bound variacional es infinito

La fórmula extendida de Gibbs es

\[
 \log\mathbb E_s e^{tD_{n,s}}
 =\sup_{Q\ll\mathbb P_s}
 \left\{t\mathbb E_QD_{n,s}
             -\operatorname{KL}(Q\|\mathbb P_s)\right\}.  \tag{22}
\]

No hace falta importar (22) para probar la divergencia: sus testigos son
explícitos. Para \(Q_j=\delta_{m_j}\),

\[
 \operatorname{KL}(Q_j\|\mathbb P_s)
 =s\log m_j+\log\zeta(s).                                  \tag{23}
\]

Por (19),

\[
 t\mathbb E_{Q_j}D_{n,s}
 -\operatorname{KL}(Q_j\|\mathbb P_s)\longrightarrow+\infty.
                                                                    \tag{24}
\]

Para \(t>0\), la desigualdad de Jensen--Chernoff solo produce

\[
 \mathbb E_sD_{n,s}\le{1\over t}
       \log\mathbb E_se^{tD_{n,s}}=+\infty.                \tag{25}
\]

Para \(t<0\), la cota inferior análoga es igualmente vacía. Optimizar en
\(t\) no ayuda: el dominio efectivo de la transformada log-Laplace es el
singleton \(\{0\}\).

## 4. El divisor desplazado conserva exactamente los testigos

Sea

\[
 Z_c(s)=\zeta(s+c)\zeta(s-c)
       =\sum_{m\ge1}{a_c(m)\over m^s},\qquad 0<c<{1\over2}, \tag{26}
\]

y \(s>1+c\). Sus pesos logarítmicos son

\[
 \omega_c(d)=2\Lambda(d)\cosh(c\log d)>0.                 \tag{27}
\]

El selector correcto es

\[
 J_{f,c}(m)={1\over a_c(m)}\sum_{d\mid m}
       \omega_c(d)a_c(m/d)f(\log d).                       \tag{28}
\]

Para un primo \(p\),

\[
 a_c(p)=p^c+p^{-c},\qquad
 \omega_c(p)=(\log p)a_c(p),                               \tag{29}
\]

y por tanto

\[
 J_{f,c}(p)=(\log p)f(\log p).                             \tag{30}
\]

Si \(p\ne q\) son primos, la multiplicatividad da

\[
 a_c(pq)=a_c(p)a_c(q),
\]

mientras \(\omega_c(pq)=0\). Por ello

\[
 \boxed{J_{f,c}(pq)
 = (\log p)f(\log p)+(\log q)f(\log q).}                  \tag{31}
\]

Las variables desplazadas

\[
 D_{n,s,c}(m)=J_{f_{n,s},c}(m)
       -{1-L_n(s\log m)\over s}                            \tag{32}
\]

coinciden exactamente con (9) y (12) sobre las dos sucesiones testigo.
Además, \(a_c(p),a_c(pq)>1\). Así, en la ley positiva

\[
 \mathbb P_{s,c}(N=m)={a_c(m)m^{-s}\over Z_c(s)},          \tag{33}
\]

los términos correspondientes de
\(\mathbb E_{s,c}e^{tD_{n,s,c}}\) son mayores que los de (18), salvo una
constante normalizadora. La divergencia bilateral (3) vuelve a valer.

Puede tomarse el ejemplo exacto

\[
 c={\log2\over\log5}\in(0,1/2),                           \tag{34}
\]

porque \(2<\sqrt5\). La completada
\(\Xi_c(s)=\xi(s+c)\xi(s-c)\) posee ceros
\(1/2\pm c+i\gamma\) fuera de la línea crítica. Por tanto la falla de
integrabilidad de Gibbs es compatible con un sistema off-line y no puede
codificar el margen de Li.

## 5. Veredicto y sucesor

Queda probado incondicionalmente:

1. los dos signos exactos de las fibras prima y semiprima (10)--(17);
2. la divergencia bilateral de todos los momentos exponenciales (3);
3. la existencia de la media ordinaria (20);
4. la divergencia explícita del supremo de Gibbs mediante deltas (23)--(24);
5. la estabilidad exacta de los testigos bajo el divisor desplazado
   (29)--(33).

Queda descartado:

```text
tilt lineal exp(t D_{n,s}) para cualquier t != 0;
Chernoff unilateral en cualquiera de los dos signos;
Gibbs/Donsker--Varadhan como generador automático de coercividad;
regularizar solo por el polo o por el presupuesto arquimediano.
```

El sucesor mínimo, si se insiste en un método variacional, debe truncar o
comprimir no linealmente \(D_{n,s}\) **y** demostrar una cota uniforme del
error de truncación con signo. Las identidades presentes no aportan esa
cota; al retirar el truncamiento se reencuentran las dos colas de (11) y
(17).

## 6. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 gibbs_chernoff_unit_palm_gate_check.py
```

El checker usa solo enteros, `Fraction` y polinomios racionales. Verifica
los coeficientes principales de (10) y (13), los signos de (16), la
dominancia superlineal exacta para grados pares e impares, y las identidades
locales desplazadas (29)--(31). No evalúa zeta, A1 ni RH.
