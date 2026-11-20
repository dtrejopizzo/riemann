# El centrado cambia la estabilidad del corte crítico

A tasa fija u≥3 usar v*, a*, l y c_N de 212, α=a*−1/2. Poner L=Nv*−κ√N. Para κ positivo suficientemente pequeño, la suma corta centrada

    S_N(L)=Σ_{p≤exp L} (log p)c_N(log p;u)/√p − ∫₀ᴸ exp(t/2)c_N(t;u)dt

reproduce la suma prima infinita con error o(1). En esta misma escala el error de corte de la suma sin centrar tiene magnitud al menos C exp(ακ√N)/√N para uno de dos corrimientos acotados en L por cada N grande. Ambos resultados admiten u fijo fuera de la banda verificada. El primero preserva también los criterios a tasa racional de 208–209.

**Error tras el centrado.** El PNT cuantitativo usado en R161_078 da |θ(x)−x|≤Cx exp(−c√log x) para alguna c>0 (pasar de ψ a θ cuesta O(√x log² x) contando potencias). La integración por partes en (exp L,∞) contra d(θ−x) y la envolvente de 212 para c_N y su derivada dan, incluido el extremo,

    |cola centrada| ≤ C_u N^(−1/2) exp(Nl(a*)−αL−c√L).

En efecto, en la integral se domina exp(−c√t) por exp(−c√L) y se integra exp(−αt). Basta elegir 0<κ<c√v*/α. La estimación sigue vigente con cualquier corrimiento acotado. La integral continua completa es H(i/2)^N−∫₀^∞ exp(−t/2)c_N(t;u)dt por simetría e inversión de 208. El primer término decae y el segundo es O_u(1/√N) por 211. Esto prueba la comparación con la suma prima infinita sin centrar.

**Error sin centrar en el mismo extremo.** En la fórmula de 212 usar a=a*, t=Nv*−κ√N+d. Se conserva la fase exp(iNθ+ix_a(d−κ√N)), y el coeficiente K se multiplica por exp(−κ²/(2Q)), Q=−h''(x_a+ia), de parte real positiva. En efecto al reescalar el pico por w=√N(x−x_a) queda dentro de la gaussiana el factor exp(−iκw); su integral da exactamente ese multiplicador no nulo. La misma dominación que en 212 justifica el límite para cada d fijo. Integrando en d=c₀+r, r≥0, con mayorante C exp(−αr), se recupera el denominador α−ix_a de la cola continua y el centrado anterior permite sustituir dx por dθ. Los corrimientos c₀=0,π/(2x_a) vuelven a dar fases en cuadratura, y el exponente sin normalizar es ακ√N−αc₀. De ahí el piso anunciado para el máximo de las dos colas. Este piso por sí solo no excede la tasa raíz uno.

**La pendiente excepcional de 212 también falla para estabilidad bajo corrimientos.** Para a=1/2 y v=l'(1/2) la dominación de una semirrecta se pierde. Comparar en cambio DOS incrementos consecutivos del corte inicial, en los intervalos de logaritmos [Nv+jD,Nv+(j+1)D], j=0,1, con D=π/(2x_a); usar convención abierto a izquierda. El PNT por partes en estos intervalos de longitud fija da error o(exp(Nl(a))/√N) con la envolvente de 212. El perfil allí, tras multiplicar por exp(t/2), tiene coeficiente común K exp(iNθ) y fases exp(ix_a d). Las integrales de estas fases en los dos intervalos difieren por el factor i, y la primera vale (i−1)/(ix_a)≠0. Por tanto uno de los incrementos, y con él al menos uno de los TRES cortes iniciales, tiene módulo ≥C exp(Nl(1/2))/√N. Esto completa la obstrucción bajo corrimientos para todas las pendientes interiores de 212, sin determinar cuál de los tres extremos gana para cada N.

**Alcance.** El centrado ya figura en 208 y el PNT cuantitativo en fase 161. La comparación simultánea de un corte estable centrado y un corte inestable sin centrar usa la nueva escala de borde de 212. El ahorro demostrado en log X es sublineal; la estimación no domina la suma centrada que queda por debajo del corte. No aporta una ventana T nueva.
