# 104_105 — Auditoría adversarial de Deep-Λ y de la energía discreta

**Veredicto.** Las dos equivalencias auditadas resisten:

\[
 \mathrm{RH}\iff
 {1\over H_X}\sum_{n\le X}{1\over n}
 \mathbf 1_{\{\lambda_n+\log(n+1)\le-e^{\sqrt X}\}}
 \longrightarrow0,                                      \tag{D}
\]

y, con

\[
 b_n={\Lambda(n)-1\over\log n},\qquad
 B_m=\sum_{2\le n\le m}b_n,
\]

\[
 \mathrm{RH}\iff
 \sup_N\sum_{m=2}^N{B_m^2\over m(m+1)}<\infty
 \iff
 \sum_{m=2}^N{B_m^2\over m(m+1)}=N^{o(1)}.              \tag{E}
\]

No se encontró una implicación circular, un cambio de orientación de los
modos exteriores ni una pérdida en la sumación de Abel. Estos son criterios
equivalentes a RH, no estimaciones ya demostradas para los primos. Esta
auditoría no prueba el límite de (D), la cota de (E), A1 ni RH.

---

## 1. Convención del modo exterior

Ponga

\[
 z_\rho=1-{1\over\rho}={\rho-1\over\rho},\qquad
 u_\rho=z_\rho^{-1}={\rho\over\rho-1}.
\]

La orientación usada en `104_56` es correcta, pues

\[
 |u_\rho|^2-1
 ={|\rho|^2-|\rho-1|^2\over|\rho-1|^2}
 ={2\Re\rho-1\over|\rho-1|^2}.                         \tag{1}
\]

Así, un cero a la derecha de la línea produce \(|u_\rho|>1\). La aparente
discrepancia con la definición usual
\(\lambda_n=\sum_\rho^*(1-z_\rho^n)\) desaparece al aplicar la simetría
\(\rho\mapsto1-\bar\rho\):

\[
 z_{1-\bar\rho}=\overline{u_\rho}.                     \tag{2}
\]

Reindexar el multiconjunto de ceros y usar que \(\lambda_n\) es real
convierte la suma en la versión con \(u_\rho^n\). Por tanto los modos
dominantes de una hipotética violación son precisamente los de la derecha,
no sus inversos contractivos.

Si RH falla, \(|u_\rho|\to1\) al crecer \(|\Im\rho|\), de modo que el
máximo \(R>1\) se alcanza en un conjunto finito. Separando esos modos se
obtiene, con multiplicidades positivas,

\[
 \lambda_n=-R^nS(n)+O(n^2R_1^n+n^2),\qquad
 S(n)=\sum_{j=1}^K\cos(n\phi_j),\quad 1<R_1<R.           \tag{3}
\]

Éste es exactamente el signo que requiere Deep-Λ: cerca del origen del
toro, \(S(n)>0\) y \(\lambda_n\) es exponencialmente negativo.

## 2. Densidad y sindicidad

Sea \(H=\overline{\{n\alpha:n\in\mathbb Z\}}\), con
\(\alpha=(\phi_1,\ldots,\phi_K)\). La rotación por \(\alpha\) es mínima y
únicamente ergódica en el grupo compacto monotético \(H\). Como
\(S(0)=K\), existe un nivel regular \(\eta\in(K/2,K)\) para el cual

\[
 U=\{x\in H:\textstyle\sum_j\cos x_j>\eta\}
\]

tiene borde de medida de Haar cero y medida \(d>0\). En consecuencia,

\[
 D=\{n\ge1:n\alpha\in U\}                               \tag{4}
\]

tiene densidad natural \(d\). Es además sindético: las traslaciones
\(U-j\alpha\), \(j\ge0\), cubren \(H\), y una subcubierta finita da una
cota uniforme para los huecos de (4). Por (3), salvo un prefijo,

\[
 \lambda_n\le-cR^n\qquad(n\in D).                       \tag{5}
\]

La densidad natural se transfiere sin pérdida a densidad logarítmica. Si
\(D(x)=dx+o(x)\), la sumación parcial da

\[
 \sum_{\substack{n\le X\\n\in D}}{1\over n}
 ={D(X)\over X}+\int_1^X{D(t)\over t^2}\,dt
 =d\log X+o(\log X).                                    \tag{6}
\]

No se usa una constante universal de densidad: \(d\) puede depender de la
configuración exterior hipotética.

## 3. Implicaciones del observable profundo

Bajo RH, \(\lambda_n\ge0\); por ello el indicador de (D) es idénticamente
cero.

Si RH falla, fije \(K>1/\log R\). Para
\(n\in D\cap[K\sqrt X,X]\), (5) da, desde cierto \(X\),

\[
 \lambda_n+\log(n+1)\le-e^{\sqrt X}.                   \tag{7}
\]

Usando (6),

\[
 {1\over H_X}
 \sum_{\substack{K\sqrt X\le n\le X\\n\in D}}{1\over n}
 \longrightarrow {d\over2}>0.                          \tag{8}
\]

Así el límite de (D) no puede ser cero. Esto audita también los dos puntos
que podían ocultar una pérdida: retirar \(n<K\sqrt X\) cuesta exactamente
la mitad de la masa logarítmica, no toda ella, y el factor constante \(c\)
de (5) es absorbido por la desigualdad estricta
\(K\log R>1\).

La traducción diagonal de `104_75` tampoco altera el criterio. La cota
uniforme de `104_69`,

\[
 \sup_{n\le X}|\lambda_{n,e^{-X/100}}-\lambda_n|=o(1),   \tag{9}
\]

es despreciable frente a \(e^{\sqrt X}\). No se usa continuidad de un
indicador duro: las inclusiones con umbrales desplazados, o directamente
la distancia creciente del umbral profundo, justifican el paso.

## 4. Identidades finitas de la energía

Con \(B(x)=B_m\) en \([m,m+1)\), la telescopía exacta es

\[
 \mathcal E(N)=\int_2^{N+1}{B(x)^2\over x^2}\,dx
 =\sum_{r,s\le N}b_rb_s
 \left({1\over\max(r,s)}-{1\over N+1}\right).           \tag{10}
\]

El borde \(-B_N^2/(N+1)\) está presente. El checker adjunto verifica (10)
en aritmética racional para datos firmados arbitrarios.

Para \(\Re s>1\),

\[
 G(s)=\sum_{n\ge2}b_nn^{-s}
      =\log\zeta(s)-C(s),\qquad
 C(s)=\sum_{n\ge2}{n^{-s}\over\log n},                 \tag{11}
\]

y \(C'(s)=1-\zeta(s)\). Por tanto

\[
 G'(s)={\zeta'(s)\over\zeta(s)}+\zeta(s)-1.             \tag{12}
\]

La sumación de Abel no tiene término omitido:

\[
 G(s)=s\int_2^\infty B(x)x^{-s-1}\,dx.                 \tag{13}
\]

En particular, si se trunca una sucesión después de \(M\), el valor
constante \(B_M\) sobre \([M,\infty)\) suministra exactamente el borde
\(B_M(M+1)^{-s}\) que completa la identidad. Esto también se verifica
de manera racional en el checker.

## 5. De energía subpolinomial a RH

Suponga \(\mathcal E(N)=N^{o(1)}\). Para todo \(\delta>0\), sumación por
partes contra los incrementos positivos de \(\mathcal E\) da

\[
 \int_2^\infty B(x)^2x^{-2-\delta}\,dx<\infty.           \tag{14}
\]

Si \(\sigma>1/2\), elija \(0<\delta<2\sigma-1\). Entonces
Cauchy--Schwarz aplicado a (13) da

\[
 \int_2^\infty|B(x)|x^{-\sigma-1}\,dx<\infty.           \tag{15}
\]

La elección puede hacerse uniformemente en compactos, de modo que (13)
prolonga \(G\) holomórficamente a \(\Re s>1/2\). Si allí hubiera un cero
\(\rho\) de multiplicidad \(m\), el lado derecho de (12) tendría residuo
\(m\) en \(\rho\), mientras \(G'\) y \(\zeta-1\) serían holomorfas. La
identidad meromorfa, prolongada desde \(\Re s>1\), lo impide. La ecuación
funcional excluye entonces los ceros simétricos a la izquierda.

Este argumento no presupone una rama global de \(\log\zeta\): después de
derivar, (12) es una identidad meromorfa monovaluada.

## 6. De RH a energía finita

El único input externo profundo en esta dirección está correctamente
etiquetado como **condicional a RH**: la cota media cuadrática de Cramér

\[
 \int_Y^{2Y}|\psi(x)-x|^2\,dx\ll Y^2.                   \tag{16}
\]

No se la usa incondicionalmente. Es un teorema clásico bajo RH; resultados
explícitos modernos prueban incluso una constante absoluta para el cociente
por \(Y^2\).

La identidad de Stieltjes

\[
 J(x)-\mathrm{Li}_2(x)
 ={\psi(x)-x\over\log x}
 +\int_2^x{\psi(t)-t\over t\log^2t}\,dt+{2\over\log2}  \tag{17}
\]

junto con (16) da una contribución \(O(1/j^2)\) al primer término en el
bloque \(x\asymp2^j\), y el término integral es
\(O(\sqrt x/\log^2x)+O(1)\). Ambos cuadrados, divididos por \(x^2\), son
integrables. Finalmente,

\[
 0\le\sum_{n=2}^m{1\over\log n}-\int_2^m{dt\over\log t}
 \le {1\over\log2}                                      \tag{18}
\]

muestra que reemplazar el comparador continuo por el discreto solo añade
una función acotada. Esto prueba \(\sup_N\mathcal E(N)<\infty\).

## 7. Resultado de la auditoría

1. La convención \(u_\rho=\rho/(\rho-1)\) tiene la orientación correcta.
2. Las excursiones negativas forman un conjunto de densidad natural
   positiva y sindético; no se supone una densidad universal.
3. El umbral \(-e^{\sqrt X}\) conserva una masa logarítmica positiva bajo
   no-RH.
4. La identidad de Abel y el borde móvil de la energía son exactos.
5. \(\mathcal E(N)=N^{o(1)}\) realmente excluye todo cero con
   \(\Re\rho>1/2\); RH realmente implica energía finita mediante (16).

Por tanto ninguno de los dos blancos se vuelve más fácil por un error de
formulación. Probar cualquiera de los límites aritméticos pendientes para
los pesos ordinarios de Mangoldt probaría RH.

---

## 8. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 deep_energy_equivalence_audit_check.py
```

El checker certifica solo las identidades algebraicas finitas y la
orientación racional del modo exterior. Los pasos asintóticos y analíticos
están demostrados arriba; el programa no pretende certificarlos por punto
flotante.
