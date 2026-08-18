# 104_96 — Diagnóstico visual diádico de la energía discreta de Cramér

**Resultado (diagnóstico, no prueba de RH).** Para los pesos ordinarios
literales, ponga

\[
 b_n={\Lambda(n)-1\over\log n},\qquad
 B_m=\sum_{2\le n\le m}b_n,
 \tag{1}
\]

y use la energía exacta de `104_93`,

\[
 \mathcal E(N)=\sum_{m=2}^{N}{B_m^2\over m(m+1)}.
 \tag{2}
\]

El nuevo checker calcula (1)--(2) hasta \(N=10^7\), sin aproximar
\(\Lambda\): usa la identidad combinatoria

\[
 {\Lambda(p^k)\over\log(p^k)}={1\over k}
 \tag{3}
\]

en todas las potencias primas. Solo \(1/\log n\) y la acumulación final
son numéricas.

Si

\[
 \Delta_j:=\mathcal E(2^j)-\mathcal E(2^{j-1}),
 \tag{4}
\]

los datos dan

\[
 0.0519113<j^2\Delta_j<0.0981871
 \qquad(9\le j\le23).
 \tag{5}
\]

Esto sugiere el blanco concreto

\[
 \boxed{\Delta_j\le {1\over8j^2}\quad(j\ge9).}
 \tag{C}
\]

No es un ajuste vacío: la potencia \(j^{-2}\) es la escala crítica que
separa una energía sumable de la contribución de un cero exterior, y la
constante racional \(1/8\) deja un margen observado de más del \(21\%\).
Si (C) se demostrara para todos los bloques, entonces

\[
 \sup_N\mathcal E(N)
 \le \mathcal E(2^8)+{1\over8}\sum_{j\ge9}{1\over j^2}<\infty,
 \tag{6}
\]

y `104_93` daría RH. Pero (C) es estrictamente más puntual que la mera
convergencia de la energía; RH no ha sido usada aquí para probar esa
constante. `104_97` demuestra que la mera localización de un espectro en
la línea crítica no impone (1/8), sin afirmar por ello que (C) falle
para la zeta ordinaria. El rango finito (5) es evidencia, no certificado
asintótico.

El mismo cálculo **refuta** dos atajos naturales:

* \(j^2\Delta_j\) no es monótona;
* la cota más fuerte \(\Delta_j\le1/(20j^2)\) ya falla en el rango
  calculado.

Por tanto no hay una extrapolación por monotonía escondida en (C).

---

## 1. Coordenada aritmética exacta

La identidad (3) reescribe el primitivo como

\[
 B_m=\pi(m)-\sum_{n=2}^{m}{1\over\log n}
       +\sum_{k\ge2}{1\over k}\pi(m^{1/k}),
 \tag{7}
\]

que coincide con la separación probada en `104_94`. El programa criba
los primos, inserta cada primo con peso uno e inserta cada potencia propia
\(p^k\) con peso \(1/k\). Una segunda rutina por división de prueba
reconstruye independientemente la tabla hasta \(10^4\) y exige igualdad
entrada a entrada antes de producir el gráfico.

Los valores globales obtenidos son

\[
\begin{array}{c|c}
N&10^7\\ \hline
\#\{p^k\le N\}&665134\\
B_N&-90.8934853592657\\
\mathcal E(N)&0.117735413945729
\end{array}
\tag{8}
\]

En todo el prefijo,

\[
 \min B_m=-98.4290621774\quad(m=9993078),
 \qquad
 \max B_m=96.2514194808\quad(m=7105253).
 \tag{9}
\]

Algunos bloques relevantes son

\[
\begin{array}{c|c|c}
j&\Delta_j&j^2\Delta_j\\ \hline
9 &9.78943751\cdot10^{-4}&0.0792944439\\
10&9.81870687\cdot10^{-4}&0.0981870687\\
13&3.35784779\cdot10^{-4}&0.0567476276\\
17&1.79624130\cdot10^{-4}&0.0519113735\\
19&2.61153355\cdot10^{-4}&0.0942763610\\
23&1.35757677\cdot10^{-4}&0.0718158110
\end{array}
\tag{10}
\]

Las subidas de \(j=9\) a \(10\), de \(13\) a \(14\), y de \(18\) a
\(19\) son contraejemplos finitos a la monotonía propuesta.

## 2. Controles crítico y exterior

Para comprobar que la visualización distingue la escala correcta, se
prescribe exactamente el primitivo de control

\[
 B_m^{(\beta,\gamma)}
 ={m^\beta\cos(\gamma\log m)\over\log m},
 \qquad \gamma=7,
 \tag{11}
\]

y se define su incremento por
\(b_m^{(\beta,\gamma)}=B_m^{(\beta,\gamma)}-
B_{m-1}^{(\beta,\gamma)}\). Por tanto no hay una reconstrucción ni un
ajuste: (11) es el primitivo exacto que entra en (2).

Una comparación suma--integral, seguida de \(t=\log x\), da

\[
\begin{aligned}
 \Delta_j^{(\beta,\gamma)}
 &\asymp
 \int_{2^{j-1}}^{2^j}
 {x^{2\beta-2}\cos^2(\gamma\log x)\over\log^2x}\,dx\\
 &\asymp {2^{(2\beta-1)j}\over j^2}.
\end{aligned}
\tag{12}
\]

Para \(\beta=1/2\), \(j^2\Delta_j\) queda en escala constante. Para el
control exterior \(\beta=0.65\), crece en escala
\(2^{0.3j}\). En los cinco últimos bloques del gráfico, el control
crítico da

\[
 0.6422\le j^2\Delta_j^{(1/2,7)}\le0.9025,
 \tag{13}
\]

mientras el exterior da

\[
 37.26\le j^2\Delta_j^{(0.65,7)}\le80.84.
 \tag{14}
\]

Dividiendo (14) por \(2^{0.3j}\), los valores quedan entre \(0.58\) y
\(0.81\), como predice (12). Éste es el control visual de la obstrucción
cuantitativa \(2\beta-1\) de `104_93`; no afirma que (11) sea una función
zeta alternativa.

## 3. Auditoría de estabilidad

La ejecución publicada realiza tres controles distintos:

1. tabla de potencias primas contra factorización independiente hasta
   \(10^4\);
2. acumulación `float64` contra `longdouble` hasta \(10^6\);
3. repetición del prefijo con cortes de bloque distintos.

En el segundo control se obtuvo

\[
 |B_{10^6}^{(64)}-B_{10^6}^{(LD)}|=6.148\cdot10^{-13},
 \qquad
 |\mathcal E_{10^6}^{(64)}-\mathcal E_{10^6}^{(LD)}|
 =3.064\cdot10^{-15}.
 \tag{15}
\]

Estas cifras auditan estabilidad de punto flotante, no convierten (5) en
aritmética intervalar certificada. El margen de (C) es, sin embargo, más
de doce órdenes mayor que la discrepancia energética observada.

## 4. Qué enseña y qué no

La figura separa limpiamente tres comportamientos:

```text
Lambda ordinaria, rango medido:       j^2 Delta_j ~ 0.05--0.10
control crítico beta=1/2:             j^2 Delta_j ~ constante
control exterior beta=0.65:           j^2 Delta_j ~ 2^(0.3j)
```

La desigualdad (C) es ahora un blanco unilateral concreto, expresado solo
con los pesos ordinarios reales. También es un enunciado de fuerza RH:
ningún dato finito, ni el gráfico, ni la estabilidad numérica lo prueban
para todo \(j\). El aporte de este documento es localizar visualmente la
escala sumable, registrar una constante candidata falsable y descartar la
monotonía que habría permitido una extrapolación ilegítima.

En particular, este documento **no prueba** (C), Deep-\(\Lambda\), A1 ni
RH.

## 5. Reproducción

Desde `tools/`:

```bash
python3 discrete_cramer_energy_visual.py --limit 10000000 \
  --chunk 500000 --audit-limit 1000000
```

Archivos producidos:

* `discrete_cramer_energy_dyadic.csv`;
* `discrete_cramer_energy_visual.svg`;
* `discrete_cramer_energy_visual.png` (conversión reproducible del SVG).
