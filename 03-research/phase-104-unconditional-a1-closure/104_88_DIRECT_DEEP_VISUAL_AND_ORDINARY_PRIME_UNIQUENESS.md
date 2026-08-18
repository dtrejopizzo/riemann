# 104_88 — Diagnóstico directo de Deep-\(\Lambda\) y unicidad de los primos ordinarios

**Resultado.** El límite Deep-\(\Lambda\) distingue visual y exactamente los
controles on-line y off-line de `104_81`. Para la zeta ordinaria, la
extracción diagnóstica a dos radios da

\[
 \lambda_n+\log(n+1)>0\qquad(1\le n\le2000),             \tag{1}
\]

con discrepancia máxima \(4.2\cdot10^{-5}\) entre los radios usados. Por
ello el indicador profundo es cero en ese rango finito. El cuarteto exterior
exacto, en cambio, produce una densidad que crece hacia \(1/8\); en
\(X=2,560,000\) vale aproximadamente \(0.0338716\).

La visualización está en
`deep_lambda_visual_diagnostic.svg` y
`deep_lambda_visual_diagnostic.png`. Es diagnóstico de doble precisión, no
certificado ni extrapolación a \(X\to\infty\).

Hay además una distinción lógica importante. No existe un **segundo modelo**
meromorfo que tenga exactamente los pesos ordinarios \(\Lambda(m)\), la misma
normalización, y ceros distintos de los de \(\zeta\). La derivada logarítmica
determina la función por unicidad analítica. Por tanto:

* construir un contraejemplo que conserve literalmente todos los
  \(\Lambda(m)\) ordinarios equivale a encontrar un cero exterior de la
  propia \(\zeta\);
* demostrar que tal contraejemplo no existe equivale a demostrar RH;
* los controles Euler de `104_81` son falsificadores válidos de mecanismos,
  pero necesariamente cambian alguna multiplicidad prima.

Un cero de \(\zeta\) no «corresponde a un primo» individual. Es una
singularidad global de la continuación analítica determinada conjuntamente
por todos los primos. La pertenencia o no a la línea crítica no puede
refutarse asignando el cero a un factor Euler aislado.

Este documento no prueba el límite Deep-\(\Lambda\) ni RH. Prueba que el
programa de buscar un contraejemplo distinto con los mismos pesos exactos no
puede decidirlos, y exhibe gráficamente la firma uniforme que todavía debe
excluirse.

---

## 1. El observable representado

Para una sucesión real \(\ell=(\ell_n)\), ponga

\[
 \mathcal D_X(\ell)
 ={1\over H_X}\sum_{n\le X}{1\over n}
 \mathbf 1_{\{\ell_n+\log(n+1)\le-e^{\sqrt X}\}}.       \tag{2}
\]

`104_75` y `104_81` prueban

\[
 \mathrm{RH}\quad\Longleftrightarrow\quad
 \mathcal D_X(\lambda)\longrightarrow0.                 \tag{3}
\]

La gráfica compara tres objetos:

1. \(x_n=\lambda_n+\log(n+1)\) para la zeta ordinaria en
   \(1\le n\le2000\), extraído por la integral de Cauchy de `zeta_tools`;
2. el cuarteto crítico, para el cual \(\mathcal D_X=0\) exactamente;
3. el cuarteto exterior de radio \(201/200\), para el cual
   \(\mathcal D_X\to1/8\) exactamente.

Para el tercer objeto,

\[
 \ell_n^{(R)}=4-2(R^n+R^{-n})\cos(\pi n/2).              \tag{4}
\]

Solo la clase \(4\mid n\) es negativa. El programa evalúa el evento en
dominio logarítmico, sin formar \(R^n\), y suma exactamente los pesos
armónicos de esa clase después de su primer cruce.

La diferencia visual esencial es ésta: una observación finita de valor cero
solo dice que todavía no apareció el cruce. Para un radio \(R\) cercano a
uno, la condición aproximada

\[
 n\log R\gtrsim\sqrt X                               \tag{5}
\]

puede empezar mucho después del rango en que se calcularon los coeficientes
ordinarios. Por eso (1) no tiene fuerza asintótica.

La convergencia roja de la figura es necesariamente lenta. Si
\(a=\log R\), la primera clase mala satisface
\(n_*(X)=\sqrt X/a+O(1)\), y la suma armónica exacta da

\[
 \mathcal D_X(\ell^{(R)})
 ={\,{1\over8}\log X+{1\over4}\log a+O(1)\,
   \over \log X+\gamma+o(1)}.                            \tag{5a}
\]

Por ello una curva cruda puede parecer pequeña durante un rango enorme
aun cuando su límite sea \(1/8\). La cantidad acelerada

\[
 \widetilde{\mathcal D}_X
 =\mathcal D_X{\log X+\gamma\over\log X}
  -{\log a\over4\log X}                                 \tag{5b}
\]

tiende a \(1/8\). En el control Euler exterior de 104_81 aparece de forma
análoga \(1/4\). Esta aceleración sirve para validar la geometría de los
falsificadores; no se aplica a la zeta ordinaria sin conocer primero un
modo exterior. La curva naranja discontinua de la figura representa
precisamente (5b): en el último punto mostrado vale
\(0.125007267602\), mientras la densidad cruda todavía vale
\(0.0338715807899\). Esto confirma que el aparente retraso rojo es el
término explícito \(1/\log X\), no evidencia de un límite cero.

## 2. Teorema de unicidad para pesos ordinarios

**Teorema 2.1.** Sea \(\Omega\) un dominio conexo que contiene el semiplano
\(\Re s>1\). Sean \(F\) y \(\zeta\) meromorfas en \(\Omega\), y suponga
que, en \(\Re s>1\),

\[
 -{F'(s)\over F(s)}
 =\sum_{m\ge2}{\Lambda(m)\over m^s}
 =-{\zeta'(s)\over\zeta(s)}.                            \tag{6}
\]

Si \(F(s_0)=\zeta(s_0)\ne0\) en un punto \(\Re s_0>1\), entonces

\[
 \boxed{F\equiv\zeta\quad\hbox{en }\Omega.}            \tag{7}
\]

**Demostración.** Fuera de polos y ceros, (6) da

\[
 {d\over ds}\log{F(s)\over\zeta(s)}=0.                 \tag{8}
\]

Luego \(F/\zeta\) es constante en el semiplano \(\Re s>1\). La
normalización en \(s_0\) hace esa constante igual a uno. La identidad
meromorfa se extiende a todo \(\Omega\) por el teorema de identidad.
\(\square\)

El teorema usa la secuencia completa de pesos, no solo positividad, PNT o
soporte en potencias primas. Explica por qué los modelos de control pueden
compartir propiedades Euler amplias pero no la secuencia exacta
\(\Lambda(m)\): si la compartieran, no serían modelos distintos.

## 3. Qué sería un contraejemplo válido

Un contraejemplo a RH compatible con los primos ordinarios es simplemente
un número complejo

\[
 \rho=\beta+i\gamma,qquad \zeta(\rho)=0,qquad
 \beta\ne{1\over2}.                                    \tag{9}
\]

No necesita ni admite una etiqueta prima. Si \(\beta>1/2\), el polo
interior correspondiente de `104_80` produce, tras reunir los modos
dominantes, constantes \(c>0\), \(R>1\) y un conjunto sindético de grados
en el que

\[
 \lambda_n\le-cR^n.                                    \tag{10}
\]

La desigualdad (10) fuerza una masa logarítmica positiva en (2). Probar que
esa masa tiende a cero para los pesos ordinarios excluye (9), pero eso es
exactamente la implicación pendiente de (3), no una consecuencia de la
unicidad (7).

## 4. Reproducción

Desde `tools/`:

```bash
python3 deep_lambda_visual_diagnostic.py
```

El script genera el SVG. La copia PNG se obtiene de forma mecánica con
ImageMagick. La extracción de \(\lambda_n\) usa dos radios y muestra su
discrepancia; esa estabilidad interna no convierte los valores en intervalos
certificados.
