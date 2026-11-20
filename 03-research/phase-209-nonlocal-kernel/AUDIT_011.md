# AUDIT_011 — Mapa continuo Mellin–Gauss y cotejo con la forma del paper

2026-10-19. Revisor independiente. Leídos LINK_011, P47 eq:form, eq:Aform, eq:W, lem:combsine y la precisión añadida al criterio de CONSTRUCTOR006.
**Veredicto: PROVED convergencia, dominio, FE par y carácter suavizante del mapa; PROVED que su norma no coincide con Q_T. Dominación con resto positivo OPEN. Objetivo íntegro D activo.**

## 1. Forma exacta que debe representar o dominar el enlace

Para cada T, P47 fija el dominio

    D_T={F∈L²(−T,T): ∫log(2+|t|)|Fhat(t)|²dt<∞},
    P_T={A(F)=B(F)=0}.

Su forma primitiva es

    a_T(F)=C₀||F||²+∫₀∞[c_F(0)−Re c_F(u)]K(u)du
           −Σ_{log n<2T}2Λ(n)/√n Re c_F(log n).

La forma completa añade 2Re(A(F)conjugado(B(F))). En el portador par con C(F)=∫Fcosh(x/2)=0, ese término es cero y Q_T=a_T. El signo de sólo ese sector no resuelve automáticamente el impar; una afirmación sobre W fuera del primitivo debe conservar además su polo. No se sustituyen contactos por Λ(n)−1 sin el término continuo correcto.

Un enlace suficiente puede probar a_T(F)≥K(U_TF)≥0 sobre un core PRIMITIVO denso en norma de forma para todo T, con sus sectores y reducciones internas declarados. No necesita extender U si ya hay signo en el core y continuidad de la forma objetivo. Densidad L² sola no basta. Las correspondencias separadas G→peine, v→polar y Π→gamma de006 eran un posible esquema, no condiciones necesarias: basta igualdad o dominación TOTAL con restos de signo demostrado. La precisión añadida a006 corrige correctamente esa sobreexigencia.

## 2. Dominio real del mapa propuesto

La prueba de S_α(d,d)≤C_αd^(−s) es correcta. Del límite inferior τ(d²y)≥c/d−1, el superior τ≤c y q_d≤1/d resulta

    0≤1/d−q_d≤min(1/d,√y).

Si c/d−1 es negativo, 1/d≤√y; si no, dividir por τ≤c conserva el sentido requerido. Así

    Π_α(d,d)≤∫y^(α−3/2)min(d^(−2),y)dy
      =[1/(α+1/2)+1/(1/2−α)]d^(−2α−1).

Los exponentes y constantes son exactos y la integral converge en el intervalo α usado. El término H_s diagonal es O(d^(−s)).

En un compacto de x, la función τ(d²exp(2x)) y todas sus derivadas tienen decaimiento gaussiano en d² con factores polinomiales controlados. La otra parte W_d es una función suave fija dividida por d. Se obtienen las cotas C_(T,j)/d uniformes en cada orden de derivación.

Por tanto Σ|a_d(F)|·||f_d|| converge para todo F∈L² y define U lineal acotado. También converge uniformemente en norma de Hilbert la serie vectorial b(x), con todas sus derivadas. La integral de Bochner representa U y la fórmula de L(x,x′) es correcta; Cauchy–Schwarz para S controla absolutamente la doble serie y sus derivadas. El operador es Hilbert–Schmidt, compacto y su kernel es C∞. No se supone ningún dominio formal de series sin demostrarlo.

## 3. FE del coeficiente y límite de la expansión polar

Para F par y α=1/4, reflejar x y sustituir W_d(exp(−2x)) da exactamente la fórmula(2). El último momento es ∫Fexp(−x/2)=∫Fcosh(x/2) por paridad. La versión final no extrapola esta identidad a F no par sin conservar F(−x); esa corrección es necesaria y ya está incorporada.

El coeficiente muestra la misma restricción lineal cosh del portador par. NO prueba una identidad del polo cuadrático de Q_T. El control de las dos series separadas es particularmente importante: Σ(1−1/d)f_d diverge en H porque su componente PSD de rango uno tiene norma inferior

    (−Z_α)|Σ(1−1/d)(d^(−s)−d^(−1))|²→∞.

Por ello la cancelación debe realizarse EN CADA COEFICIENTE antes de sumar. La fórmula FE no produce un vector polar independiente. Sobre C(F)=0 se anula la línea polar y queda el coeficiente O(1/d) ya controlado. Todas estas afirmaciones son correctas y de alcance preciso.

## 4. Comparación con gamma y peine

El símbolo de P47 satisface

    m(t)=Re ψ(1/4+it/2)−logπ
         =log|t|−log(2π)+O(|t|^(−2)).

La normalización y el signo coinciden con eq:form. La energía de Lévy tiene K(u)~1/u: se trata de un operador de orden logarítmico, no de afirmar que su kernel físico sea log|u|. La redacción final incorpora esa precisión.

Para T fijo, la suma del peine es acotada en L² por Σv_n||F||², mientras el gamma no lo es. En lem:combsine el peine completo sobre la base de sines conserva las diferencias divididas D_T(ω_k)±D_T(ω_l) y su diagonal C_T(ω_k)+D_T(ω_k)/(2Tω_k). No se lo puede reemplazar por una matriz de un solo argumento ni por un promedio de fases; tampoco el gamma comprimido es por definición diag(m(ω_k)). El candidato011 no hace esas sustituciones.

## 5. Refutación exacta de la igualdad para este mapa

El test φ(x)cos(λx), con φ par suave de soporte interior, tiene norma L² que tiende a ||φ||/√2. Su momento cosh decrece más rápido que cualquier potencia. Restar el múltiplo correspondiente de una χ explícitamente PAR con momento no cero conserva paridad, soporte y dominio suave; tras normalizar, F_λ queda en el core primitivo par.

Sus Fourier son dos traslaciones de φhat a ±λ más una corrección superpolinomialmente pequeña. La asíntota de m y el decaimiento rápido de φhat dan gamma(F_λ)=logλ+O(1). La corrección no altera ese término; el peine permanece uniformemente acotado. Así Q_T(F_λ)→+∞.

Por otro lado F_λ converge débilmente a0 y U es compacto, luego ||UF_λ||²→0. **La identidad Q_T=||U·||² queda refutada para ESTE candidato y todo T fijo.** El argumento es independiente del signo desconocido en las direcciones bajas y no usa ceros.

## 6. Resto y alcance final

B_T=Q_T−||U·||² está definido como forma en el dominio de Q_T; conserva el gamma no acotado y las traslaciones del peine, restando sólo un kernel suave. No se ha demostrado B_T≥0. El crecimiento positivo en alta frecuencia no controla bajas frecuencias ni acoplamientos.

El resultado no refuta una dominación Q_T≥||U·||², ni otros mapas no suavizantes o con dominios distintos. No autoriza sustituir el resto por un símbolo positivo libre. El mapa efectivamente calculado NO es la forma del nodo, y la FE cosh no basta para identificarla.

**Candidato explícito auditado; igualdad descartada con prueba; dominación y enlace real todavía OPEN. El objetivo D continúa sin completar.**
