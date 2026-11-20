# Un corte conservativo para repartos que dependen de la escala

Sea ν positiva sobre (u,y), u≥1, 0<y<1, con masa finita donde u≤R para cada R. Se admite dependencia arbitraria entre u e y. Escribir h(t)=∫ K_y(t/u)dν con el acarreo de 099. Existen R finito y ε>0 independientes de ν tales que

    ∫₁ᴿ |h(t)−log t|dt/t² ≥ ε.

**Corte.** Cada reparto aporta una unidad de medida en u y resta unidades en u/y y u/(1−y). La medida firmada resultante σ es localmente finita. El acumulado ponderado C_h(X)=∫_[1,X]dσ(v)/v es no negativo: antes del padre no entra nada, después sólo se han sustraído partes de 1/u, que suman exactamente 1/u. Para G(t)=σ([1,t]), h(t)=Σ_{n≤t} G(t/n). Por inversión G(t)=Σ_{n≤t} μ(n)h(t/n). Integración por partes da C_h(X)=G(X)/X+∫₁ˣ G(t)dt/t², incluyendo cualquier átomo inicial.

**Perfil forzado por el objetivo.** Para h=log en t≥1 (cero debajo), G es continuo, G(1)=0 y G'(t)=M(t)/t casi por doquier, donde M es la suma de Möbius. Luego C_log(X)=∫₁ˣ M(t)dt/t². Para Re s>0 su Mellin respecto de dX/X es 1/[s(s+1)ζ(1+s)], por integración y convergencia absoluta. Esta función es regular en todo el tramo real s>−1: en cero el polo de ζ cancela s. Sin embargo hay un polo en s=ρ−1 para el primer cero crítico. Si C_log fuera eventualmente no negativa, Landau (retirar un intervalo compacto sólo añade una función entera) forzaría abscisa ≤−1, imposible por ese polo. Vale igualmente para −C_log. Por continuidad existe un intervalo compacto I con C_log estrictamente negativa.

**Separación estable.** Integrar C_h sobre I en dX. En términos de h esto es un funcional lineal acotado en L¹([1,R],dt/t²), R=max I: en G sólo ocurren n≤R y tras t=n v cada integral de |h(t/n)| con t en [1,R] se acota por una constante finita por la norma indicada. Para el término G(X)/X vale el mismo argumento al integrar en X. El funcional da valor ≥0 para todo h admisible y valor estrictamente negativo para log. Su brecha dividida por su norma da ε. Para una mayoración fija punto a punto en [1,R], PNT vuelve esta pérdida en un exceso de orden x en la banda prima [x/R,x]: h es de variación acotada en el compacto por finitud local de los padres y la cota uniforme de saltos de cada núcleo.

**Alcance.** La constante y la banda aquí son existenciales. 099 exigía un reparto independiente de la escala; aquí se usa conservación de tamaños en vez de factorizar su promedio Mellin. El mismo corte sirve para repartos en cualquier número finito prefijado de partes positivas que sumen uno. No se excluye una estimación que compense errores de signos opuestos en la suma prima.
