# Splitting P3: reconstrucción alternativa y alcance documental

**Estado vigente:** el dictamen matemático de P3 es **(a), reconstruido**, según §§6–9. Las obligaciones provisionales descritas antes de esas secciones quedaron descargadas por la fórmula explícita reproducida por Chan y su comparación gaussiana con Murase. No queda pendiente matemático por la falta de acceso al original de Kudla; esa limitación es documental.

28-11-2026. P3 de49:538–560 y conversión a acciones izquierdas49:576–587. **No se obtuvo el texto íntegro de Kudla1994:** Springer sólo entrega la página de acceso. Se leyó [Murase2001, texto original reproducido](https://scispace.com/pdf/on-metaplectic-representations-of-unitary-groups-i-splitting-uq1lp9d5j5.pdf); el [DOI editorial](https://doi.org/10.3792/pjaa.77.59) lleva a ProjectEuclid, cuyo acceso directo quedó bloqueado. No se afirma un cotejo visual con Kudla.

Murase§§1.2–1.8 define, para A(w,w′)=Tr(w*Qw′), el operador M(g) mediante integración de ψ(A(w,gw)/2)ρ((1−g)w), con medida autodual para A(w,(g−1)w′). Su factor es λ_E(ψ)^(−ν_g)χ(Δ(Q(g−1))), ν_g=dim_E W/ker(g−1), χ|F×=ε. Theorem1.8 hace de su producto una representación. Remark1 incluye el caso arquimediano; Remark2 afirma coincidencia con Kudla en el modelo split. La prueba no restringe la característica residual a distinta de2: Q₂ está incluido.

No usamos Remark2 para adivinar la normalización: los siguientes cálculos fijan los escalares. Los símbolos de Murase no son automáticamente los del manuscrito; **su χ debe ser ξ⁻¹** en el diccionario de acciones izquierdas de49.

## 1. Convenciones comunes

Escribimos ψ=ψ_k y N(z)=bar(z)z. En una polarización del espacio skew-hermitiano se eligen coordenadas columnas w=(x,y) con

\[
A(w,w')=\operatorname{Tr}_{E/F}(x^*y'-y^*x'),\qquad Q=\begin{pmatrix}0&I\\-I&0\end{pmatrix}.
\]

En las coordenadas originales de49 esto corresponde a Q=−jH si H es la matriz hermitiana: A(w,w′)=Tr(j⟨w′,w⟩)=Tr(−j⟨w,w′⟩). El cambio a coordenadas hiperbólicas elimina j de Q; no cambia A. El operador de Heisenberg es

\[
\rho(x,y)f(t)=\psi\bigl(\operatorname{Tr}(t^*y)+\tfrac12\operatorname{Tr}(x^*y)\bigr)f(t+x).
\]

Su multiplicador es ψ(A/2), exactamente P2. Para leer la forma de Kudla A/2 con el mismo operador se requiere ψ_K(u)=ψ_k(2u). Entonces η(u)=ψ_K(u/2)=ψ_k(u). Esta conversión afecta tanto el operador como su medida autodual: no se puede cambiar sólo el nombre de ψ.

Sea λ=λ_E(ψ), la constante gaussiana de la forma N con medida autodual para ψ(Tr(bar u v)). Usaremos

\[
\int_E\psi(aN(u))\,du=\lambda\,\epsilon(a)|a|_F^{-1},\qquad \lambda^2=\epsilon(-1),
\]

interpretando la integral como gaussiana estabilizada/distribucional. Por diagonalización hermitiana, con medida autodual del pairing correspondiente a B, la integral de ψ(u*Bu) es λ^sε(det B), s=rangoB. Ésta es la normalización explícita que permite evitar una identificación informal de índices de Weil.

## 2. Unipotentes

Sea g_B=[[I,0],[B,I]], B*=B de rango s. Entonces Q(g_B−1) tiene bloque B y bloque cero; ν_g=s y ξ_g=det B módulo normas. En el cociente por el núcleo, el integrando de M(g_B) aplicado a f(t) es

\[
\psi(u^*Bu-\operatorname{Tr}(t^*Bu))f(t)
=\psi((u-t)^*B(u-t)-t^*Bt)f(t).
\]

Luego M(g_B)=λ^sε(det B)T_B, donde T_Bf(t)=ψ(−t*Bt)f(t). El factor de splitting λ^(−s)χ(det B) cancela exactamente esa constante, ya que χ(det B)=ε(det B). Así M_χ(g_B)=T_B. El cálculo vale para B singular pasando al cociente y no divide por2 dentro de un retículo.

## 3. Levi y elección del carácter

Para m(a)=diag(a,(a*)⁻¹), primero supóngase a−I invertible. Se tiene ν=2d y

\[
\Delta(Q(m(a)-1))\equiv(-1)^d\overline{\det a}^{-1}\pmod{N(E^\times)}.
\]

Por χ(bar z⁻¹)=χ(z) y λ²=ε(−1), el factor de Murase es χ(det a). En la integral M(m(a)), integrar en la variable y impone la ecuación lineal (I−a)u+(I−a⁻¹)t=0. El jacobiano |det(I−a)|_E⁻¹ cancela ese factor en la medida autodual, dejando

\[
M(m(a))f(t)=|\det a|_E^{-1/2}f(a^{-1}t).
\]

La identidad se extiende por continuidad desde el abierto a−I invertible. Por tanto

\[
M_\chi(m(a))f(t)=\chi(\det a)|\det a|_E^{-1/2}f(a^{-1}t).
\]

En49, la acción izquierda sobre Y es (a*)⁻¹, y su factor exigido es ξ(det(m(a)|Y))⁻¹=ξ(det a)⁻¹. **Elegir χ=ξ⁻¹ da exactamente ese factor.** Ambas restricciones a F× siguen siendo ε. Tomar χ=ξ sin cambiar las convenciones daría, en general, el carácter inverso equivocado; la afirmación de coincidencia de Murase debe leerse con este diccionario.

## 4. Weyl: cálculo del factor2

En un plano hiperbólico sea τ=[[0,−1],[1,0]]. Entonces ν_τ=2 y det(Q(τ−1))=2. Para w=(u,v), el producto de las dos fases del integrando de M(τ) es

\[
\psi\bigl(2N(v)+\operatorname{Tr}(t^*(v-u))\bigr)f(t+u+v).
\]

Poniendo z=t+u+v, el exponente se convierte en 2N(v+t)−Tr(t*z). La medida autodual de W para A(w,(τ−1)w′) es |2|_F veces la medida producto. Integrar v da λ ε(2)|2|_F⁻¹, por lo que

\[
M(\tau)=\lambda\epsilon(2)\mathcal F_-,\qquad
\mathcal F_-f(t)=\int_Ef(z)\psi(-\operatorname{Tr}(t^*z))\,dz.
\]

El factor de splitting es λ⁻²χ(2)=λ⁻²ε(2), y por ello

\[
M_\chi(\tau)=\lambda^{-1}\mathcal F_-.
\]

Los factores |2| se cancelan **también en característica residual2**. En j planos ortogonales el cálculo factoriza y da λ^(−j) veces la transformada Fourier parcial. Para F=R,E=C,ψ(t)=exp(−2πit), λ=−i, coincidiendo con el escalar gaussiano negativo utilizado en la cuenta arquimediana de49.

## 5. Fórmula Bruhat y límite del cotejo literal

El parabólico de Y y los Weyl parciales generan U(W) split. Los tres cálculos anteriores, junto con el teorema de Murase, construyen una representación con las fases requeridas sobre esos generadores. En la descomposición derecha p₁τ_jp₂, las composiciones con los operadores del parabólico sólo efectúan cambios lineales de variables y multiplicaciones cuadráticas: sus jacobianos son positivos. No introducen una fase gaussiana adicional. La fase de la transformada parcial es λ^(−j), y los caracteres de los dos factores parabólicos se multiplican para dar ξ(det(p₁p₂|Y)). Así se obtiene el suplemento explícito

\[
\omega(g)=\xi(x(g))\lambda_E(\psi_k)^{-j(g)}r_Y(g)
\]

leído con la conversión de acciones de49. La medida de r_Y se fija positiva y unitaria; no queda una libertad de signo escondida en Haar.

**(a) reconstruido:** existencia y normalización de la representación split, acciones de Levi/unipotente/Weyl, carácter, factor2 y fase gaussiana, mediante la fórmula explícita con λ. **(c) documental aún delimitado:** no se pudo verificar en la página364 de Kudla que su símbolo exacto γ_F(η∘RV), con la definición original de RV y de «carácter de segundo grado», sea literalmente λ_E(ψ_k), y no una notación para una forma escalada cuya conversión deba escribirse. Remark2 de Murase respalda la identificación, pero no sustituye ese cotejo de definiciones. No se afirma haber leído Theorem3.1 de Kudla.

Para un argumento reconstruido, se puede sustituir P3 por la fórmula anterior **con λ definido explícitamente** y los cálculos de§§1–4; los usos de Levi, Fourier y el escalar arquimediano quedan determinados. Para certificar palabra por palabra la cita de Kudla falta su convención original RV. Tampoco se debe concluir sólo de estos cálculos toda la compatibilidad de doubling(P4), tensor/producto global y racionalidad del theta: son obligaciones distintas auditadas en la rama Weil, que deben usar consistentemente esta misma normalización. Este suplemento no es una mera afirmación de que «algún splitting existe».

## 6. Cierre de la identificación RV mediante otra fuente primaria

**Actualiza el pendiente de§5.** Se cotejó [Chan, *Period identities of CM forms on quaternion algebras*, §5.1, p.10, Definition5.1 y Theorem5.2](https://web.math.princeton.edu/~charchan/CM.pdf), investigación original disponible en la página de la autora. Allí se reproduce el splitting de Kudla con la misma definición x(g)=det(p₁p₂|Y), j(g), restricción ξ|F×=ε^m y factor γ_F((ψ/2)∘RV). Para E=F(√u), define este último por

\[
(u,\det V)_F\,\gamma_F(-u,\psi/2)^m\gamma_F(-1,\psi/2)^{-m}.
\]

En nuestro caso m=1,detV=1,ψ_K/2=ψ_k. Sea G_ψ(a) el índice de la gaussiana ψ(ax²). Tanto si γ_F(a,ψ) denota G_ψ(a) como su versión normalizada G_ψ(a)/G_ψ(1), el cociente que aparece es el mismo. La identidad G_ψ(−1)=G_ψ(1)⁻¹ se obtiene conjugando la gaussiana. Por tanto

\[
\gamma_F(\eta\circ RV)
=\frac{G_{\psi_k}(-u)}{G_{\psi_k}(-1)}
=G_{\psi_k}(1)G_{\psi_k}(-u)
=\gamma(\psi_k(x^2-u y^2))
=\lambda_E(\psi_k).
\]

La penúltima igualdad es multiplicatividad de la integral gaussiana en coordenadas ortogonales; x²−uy²=N_(E/F)(x+y√u). Las medidas autoduales transforman con el jacobiano positivo correspondiente, sin fase. Se obtiene así la igualdad **exacta**, no sólo igualdad de módulos ni un posible carácter cociente. Vale también sobre Q₂: ninguna identidad usa que2 sea una unidad. En el lugar real la cuenta da−i paraψ_k negativo, como ya se comprobó.

**Dictamen actualizado(a) para P3 en su normalización matemática**, con cotejo indirecto del enunciado publicado de Kudla mediante la reproducción precisa de Chan y reconstrucción independiente de los generadores mediante Murase. Permanece solamente la limitación documental de no haber abierto las páginas originales de Kudla1994; no queda de ella una constante matemática indeterminada.

## 7. Propagación: no se está cambiando de representación

La igualdad de§6 identifica exactamente el coeficiente γ deP3 conλ. Las acciones sobre parabólico y Weyl, que generan el grupo split, coinciden; por tanto no queda un carácter local no detectado. No se sustituye el splitting por otro que sólo coincida globalmente.

**Doubling y sumas ortogonales(P4).** La fórmula de Murase funciona sin suponer W split. Para W=W₁⊥W₂ y g=(g₁,g₂), el cociente W/ker(g−1) es suma de los dos cocientes; la fase es suma, la medida autodual es producto, ν=ν₁+ν₂ y Δ=Δ₁Δ₂ módulo normas. En tensores de vectores suaves, Fubini para integrales estabilizadas (y Gaussianas distribucionales en infinito) da M(g)=M(g₁)⊗M(g₂); los factores de splitting también multiplican. En particular ω_(W⊕W⁻)(g,1)=ω_W(g)⊗1, sin escalar. Naturalidad bajo isometrías sigue por cambiar variables en esa misma integral y conservarΔ módulo normas. Puesto que el splitting split ya coincide conP3, su restricción al doble es exactamente la definiciónD2 del paper. AsíP4 y `pwf:sum` conservan sus operadores, incluso en espacios no split.

**Cambio de carácter, usado en54.** Para R_g=Q(g−1), sobre el cociente no degenerado se tiene R_g*=R_g g⁻¹. Luego Δ/overlineΔ=det g, pues g actúa como identidad en su núcleo. Cambiarυ porυ·(μ∘bc) cambia χ_Murase=υ⁻¹ porχ_Murase·(μ∘bc)⁻¹; el cociente de splittings es μ(det g)⁻¹. El signo universal en acciones izquierdas es−1. La afirmación vale también enD2 y no procede de atribuir un signo arbitrario al cambio de carácter.

**Vacío, fase finita e integridad.** Como se identifican los mismos operadores locales en todo U(W), cualquier cálculo del escalar sobre una línea de vacío y su evaluación en0 usa el mismo operador, no sólo uno proporcional. Por eso la revisión existente de `vacfix` y del suplemento de fase49 se aplica sin añadir una raíz de unidad nueva. Esta observación no pretende demostrar por sí sola cada fórmula fuerte de fase: permanece la distinción del informe REVISION-FASE49-V2 entre fórmula fuerte y consecuencias suficientes. El aporte aquí es eliminar una ambigüedad de splitting que pudiera alterar esas consecuencias.

**Theta, Poisson, constantes CM/CS.** Se conserva la acción del Heisenberg, el carácter aditivo, las medidas autoduales y el factor gaussiano arquimediano. La prueba de invariancia racional49:872–914 usa la acción de Levi y la unicidad del funcional theta, más doubling; todos ellos permanecen iguales. No necesita una compensación informal de fases sobre los lugares. Así se conserva su identificación con la acción racional de Weil usada por Poisson/Siegel. En particular no se ha reescalado el funcional theta, el vacío de Fock ni el argumento de las funciones theta, por lo que esta sustitución explicativa deγ porλ no introduce una modificación de períodos CM, constantes Chowla–Selberg, normas ni integrales locales. Sus verificaciones aritméticas siguen siendo las de THETA; el presente cotejo no las reemplaza, pero elimina este posible cambio de normalización.

**Estado final de esta obligación:** no queda una discrepancia de caracteres, un factor2, un índice de Weil o un escalar de doubling sin determinar en la comparaciónP3/Murase. La identificación exacta permite utilizar los cálculos anteriores de la rama Weil y las aplicaciones49–56 con sus normalizaciones originales.

## 8. Dictamen inequívoco y cotejo final con el suplemento de fase

**Dictamen matemático(a), reconstruido con las fórmulas explícitas anteriores. El acceso pendiente al original de1994 no constituye una obligación matemática restante.** La fuente primaria alternativa fija la fórmula y la reconstrucción por generadores fija el operador, sus signos y constantes.

Se releyó íntegramente REVISION-FASE49-V2. Sus premisas se reducen a: carácterυ construido con tipo infinito y no ramificación declarados; finitud de clases de ideales; Heisenberg y retículos autoduales; operadores de Rao y cambios de polarización aritméticos; P3 y doubling exactos; carácter del estabilizador sobre la línea vacía; modelos split sobre2 y cálculo de vacío unimodular no split en característica impar. El informe de fase ya coteja Rao y la cuenta de vacío en Pan; P3 y doubling, que allí permanecían(c), quedan descargados por§§1–7 de esta ficha. No surge una nueva premisa global por esa descarga.

El campoA del suplemento es estable por conjugación yσ conmuta con ella enA porque cada generadorυ(a) tiene todos sus conjugados de módulo1. Las identidades de Gram son sumas finitas algebraicas tras fijar soportes y subgrupos de constancia; no se aplicaσ a integrales infinitas. La integralidadℓ usa operadores e inversos en p≠ℓ y el carácter suave de imagen finita del estabilizador en p=ℓ. La transición a representantes racionales requiere sólo integridad sobreℓ por aproximación, no componente exactamente cero. Por ello el cierre deP3 permite concluir las dos propiedades suficientes deδ_g sin ninguna pérdida y sin invocar Short Forms, auxcore oGRH. La clasificación fuerte de la fase permanece distinta y no necesaria.

## 9. Revisión cruzada limitada de la corrección ν^flat en54

Se compararon las definiciones54:2695 y7584 con el cálculo operativo2730–2736 y con REVISION-54-TRES-EXCHANGES-V2. Con la definición impresa ν^flat=ν″υ^m/χ′, la igualdad α=χ′ν^flatυ^m=ν″υ^m es falsa: el lado izquierdo esν″υ^(2m). No se puede tratar como un factor constante inocuo.

La sustitución suplementaria ν^flat=ν″/χ′ hace simultáneamente verdaderas: α=ν″υ^m; αβ⁻¹=υ^m conβ=ν″; el peso deν^flatυ^m igualm−#ι; y

\[
j+(t+k-1)/2+m-3m-(7m+k)/2=j+(t-11m-1)/2=n'.
\]

Así el factorL del tercer exchange es el declarado, no uno desplazado enm. La corrección elimina exactamente elυ^m extra en las dos definiciones; conserva esefactor en las fórmulas deF_i. El cocienteν″/χ′ sigue siendo independiente del twist y sin parte tame. Por tanto no cambia conductores ni condiciones de integridad locales. Se confirma la necesidad y coherencia de esta corrección con el intercambio, no un cierre independiente de todos los pasos de generación global de54, revisados en sus otras fichas.
