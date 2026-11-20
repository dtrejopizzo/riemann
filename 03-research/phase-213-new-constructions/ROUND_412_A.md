# Comparación integrada en el eje real que recupera la suma sin peso de los desplazamientos

**Estado: PROVED, con revisión independiente de la normalización al infinito, el factor2 y el límite extendido.**

Sean X(w)=ξ(1/2+w)/ξ(1/2) y P(w)=∏_{γ>0}(1+w²/γ²) usando TODAS las ordenadas con multiplicidad. Para w real ambos son positivos. Existe c=lim_{w→+∞}log(X(w)/P(w)). Si

    D(R)=∫_{−R}^R [log(X(w)/P(w))−c] dw,

entonces D(R)≥0 para R>0 y

    lim_{R→∞} R D(R) = 2 Σ_{γ>0} (Re ρ−1/2)²   en [0,∞].

Esto difiere del déficit de 410, que pesa los desplazamientos con orden γ^(−4). En particular una sucesión no acotada con D(R)=o(1/R) bastaría para RH. La afirmación no da esa estimación.

**Normalización.** Por Hadamard como en 410, para el cero superior con δ=Re ρ−1/2 tomar la contribución de su par conjugado log(((w−δ)²+γ²)/(δ²+γ²)). Sumar simétricamente las abscisas δ y −δ (sin duplicar la multiplicidad). La diferencia con P es la suma de log(γ²/(δ²+γ²)) más la suma de diferencias centradas

    [f_γ(w−δ)+f_γ(w+δ)]/2−f_γ(w),    f_γ(w)=log(w²+γ²).

La constante converge por Σγ^(−2)<∞; los restantes términos cuestan O(δ²/γ²) por Taylor, uniforme en w, y tienden individualmente a cero al tender w a infinito. Así la constante es precisamente c, también determinable como límite por el eje real sin introducir las abscisas en su definición. La suma se integra término a término en cada compacto.

**Positividad después de integrar.** Sea J(d)=∫_(−R)^R f_γ(w−d)dw. Es par y

    J''(d)=4R(R²+γ²−d²)/[((R−d)²+γ²)((R+d)²+γ²)].

Como |d|≤1/2 y γ>1, esta expresión es positiva y comparable a R/(R²+γ²), con constantes absolutas. La contribución integrada es J(δ)−J(0)=∫₀^|δ| (|δ|−t) J''(t)dt. Por tanto

    D(R) ≍ Σ_{γ>0} δ² R/(R²+γ²).

A γ fijo, R J''(t)→4 uniformemente para |t|≤1/2, de modo que R[J(δ)−J(0)]→2δ². Si Σδ² converge, domina Cδ² y se pasa al límite. Si diverge, la positividad permite tomar sumas parciales arbitrarias para el liminf. Esto prueba la fórmula completa: ningún cero alto puede compensar el aporte de uno bajo en esta integral.

**Registro de revisión.** Al agrupar primero cada cero con su conjugado aparecen los factores positivos((w−δ)²+γ²)/(δ²+γ²); las exponenciales lineales canónicas se cancelan al sumar las abscisasδ y−δ con sus multiplicidades. El promedio simétrico usado en la fórmula no duplica el conjunto superior: cada cero conγ>0 sigue contándose una vez. La constante es c=Σlog(γ²/(γ²+δ²)), finita y no positiva. La cota uniforme |[f(w−δ)+f(w+δ)]/2−f(w)|≤Cδ²/γ² permite tanto el paso al infinito como integrar en cualquier compacto; sin restar c habría un término lineal enR y la conclusión no sería válida.

La derivada segunda deJ indicada es positiva para todo R>0 porqueγ>|δ|, y es comparable aR/(R²+γ²) uniformemente en|δ|≤1/2. Cada contribución integrada es por tanto no negativa, aun cuando la diferencia centrada no tenga signo punto a punto. Para un cero superior fijo, R[J(δ)−J(0)]→2δ²; un cuarteto exterior tiene dos ceros superiores y aporta4δ², lo que confirma el factor2 por cero. SiΣδ²<∞ se domina porCδ²; siΣδ²=∞ las sumas parciales positivas fuerzan liminf R D(R)=∞, que prueba el límite extendido sin intercambiar una serie divergente. El valorD(R) sigue siendo finito para cadaR, porΣδ²/γ²<∞. BajoRH es idénticamente0, y con algún cero exterior es estrictamente positivo para cadaR>0.

**Obligación pendiente.** Aunque X sobre el eje real se evalúa mediante ζ y su factor arquimediano, P utiliza las ordenadas de todos los ceros y c exige normalización al infinito. Reemplazar P por el producto de sólo los ceros críticos verificados invalidaría la identidad. El método distingue desplazamientos que una Gram de ordenadas por sí sola no detecta, pero necesita una estimación independiente del cociente integrado a escala o(1/R). No se afirma prioridad externa.
