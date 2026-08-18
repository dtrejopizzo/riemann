# Validación mecánica de cobertura

## Dictamen

La cobertura documental es completa para los tres ámbitos declarados. No se detectaron enlaces rotos, referencias de catálogo inexistentes, desequilibrios LaTeX ni contradicciones entre las fórmulas centrales y el plan de reinicio.

## Inventario contrastado

- Paper 36: `04-papers/36-obstruction-ledger/main.tex` tiene 8.806 líneas y 54.962 palabras. Existen la auditoría principal y su fragmento lógico.
- RH1--RH9: hay 626 directorios `task`, distribuidos como 89, 94, 83, 83, 60, 68, 43, 27 y 79. Cada serie es continua desde `task1` hasta su máximo y pertenece a una auditoría de bloque.
- Fases: hay 101 directorios `phase-*`. Los rótulos 001 y 002 no existen y el 044 tiene dos rutas; ambas anomalías están registradas. Las cinco auditorías cubren todos los intervalos desde 000 hasta 101.
- El bloque 076--089 contabiliza los 512 Markdown presentes. El barrido nominal de cierres no encontró candidatos fuera de los directorios auditados.

## Navegación y tamaño

Los 42 enlaces Markdown locales resuelven. Los ocho documentos del orden de lectura, las referencias textuales del alcance y el mapa del índice existen.

Excluyendo este informe para evitar circularidad, los otros diecinueve Markdown contienen 45.101 palabras, 320.961 caracteres Unicode y 326.879 bytes. La cota mecánica de un token por byte queda en 326.879 tokens. Al incorporar este informe, el dossier conserva veinte Markdown, menos de 50.000 palabras y menos de 350.000 bytes, dentro del límite declarado.

## Balance LaTeX

En todos los Markdown coinciden los delimitadores de matemática de bloque e inline, los pares `begin`/`end` y los pares `left`/`right`. No quedan filas alineadas terminadas con una sola barra inversa ni secuencias de espaciado RDI mal formadas.

## Fórmulas verificadas

La fórmula unilateral es una consecuencia algebraica exacta del split declarado:

\[
\lambda_n=\lambda_n^{\rm arch}+\lambda_n^{\rm prime},
\qquad
\lambda_n\ge0
\Longleftrightarrow
\lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch}.
\]

Su tratamiento por signo es correcto. La fórmula exacta de la parte arquimediana, junto con la convexidad discreta, da

\[
I_-:=\{n\ge1:\lambda_n^{\rm arch}<0\}=\{1,2,\ldots,7\}.
\]

El contraste numérico independiente reproduce \(d_3\approx0{,}00626036\), \(\lambda_7^{\rm arch}\approx-0{,}355731\) y \(\lambda_8^{\rm arch}\approx0{,}020900\). Por ello, fuera de \(I_-\) puede formularse el control de la parte negativa; dentro de \(I_-\) debe conservarse el lower bound completo.

El límite Laguerre está correctamente pareado. Para \(\varepsilon>0\), el primer sumando es la integral de \(f_{n,\varepsilon}\) contra Lebesgue y el segundo es la integral contra \(d\psi\); ambos usan el mismo regulador. En \(n=1\), la diferencia tiende a \(\gamma\), como exige \(\lambda_1^{\rm prime}\).

Con

\[
f_{n,\varepsilon}(y)=y^{-1-\varepsilon}L_{n-1}^{(1)}(\log y),
\qquad f_{n,\varepsilon}(1)=n,
\]

la integración por partes conserva el signo y el borde inferior:

\[
\lambda_n^{\rm prime}
=\lim_{\varepsilon\downarrow0}
\left[-n+\int_1^\infty(\psi(y)-y)f'_{n,\varepsilon}(y)\,dy\right]
=\lim_{\varepsilon\downarrow0}
\int_1^\infty(\psi(y)-y+1)f'_{n,\varepsilon}(y)\,dy.
\]

Las dos formas coinciden porque \(\int_1^\infty f'_{n,\varepsilon}=-n\). La normalización asintótica también es consistente:

\[
\lambda_n^{\rm arch}
=\frac n2\log\frac n{2\pi}
+\frac{\gamma-1}{2}n
+\frac34+O(n^{-1}).
\]

El término lineal no se absorbe en \(O(\sqrt n\log n)\), y toda cota con ese factor comienza en \(n\ge2\).

## Consistencia del plan RDI

La ruta RDI permanece abierta y subordinada al resultado del triage LP/GAP-Z. El plan no la presenta como requisito del ataque unilateral ni como cierre ya obtenido. Si sobrevive la atribución, congela una sola coordenada, `C_core`, exige orden de límites y fuente Gamma--Euler explícitos, y rechaza nuevas reformulaciones sin una estimación adicional. Esta jerarquía coincide con `MASTER_CONTEXT.md`, `PHASES_AUDIT.md` y el registro de retiros.

## Controles de forma

El barrido completo no encuentra las dos voces restringidas ni campos temporales de metadatos. Los conteos de formatos auxiliares certifican presencia, no contenido matemático.
