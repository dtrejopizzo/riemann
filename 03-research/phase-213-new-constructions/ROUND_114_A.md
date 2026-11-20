# Cola absolutamente controlada desde la altura de la raíz cuarta

Para el peso w de 109 y A,K≥0 fijos, poner H(x)=x^(1/4)/(log x)^A. Incondicionalmente, al crecer x,

    Σ_{|Im ρ|≥H(x)} |x^ρ V(ρ)| = o(√x/(log x)^K).

Aquí se suman módulos, incluso para ceros fuera de la recta y con multiplicidad. En 112 se pagaba O(x log H/H), suficiente en una ventana finita. La nueva estimación es asintótica, sin umbral numérico certificado.

**Insumos clásicos.** La versión con pérdida logarítmica de la densidad de Ingham es N(σ,2T)≪T^[3(1−σ)/(2−σ)]log⁵T uniformemente para 1/2≤σ≤1 (registrada en fase 37, documento 111 §referencias, y fase 54 documento 170). Sólo usamos el exponente mayor 3(1−σ). La forma más débil con +ε fijo en el exponente no basta para esta prueba en el borde. Por Korobov–Vinogradov (paper 01 §regiones libres), en T≤|γ|≤2T se tiene (1−β)log T≥c(log T/log log T)^(1/3) para alguna c>0 y todo T grande.

**Mayorante sumable.** Para cualquier B fijo, sobre β≥1/2 se tiene Σ (log |γ|)^B |γ|^[−4(1−β)]<∞. En un bloque diádico agrupar en j=floor((1−β)log T). La cardinalidad de cada grupo es ≪exp(3(j+1))log⁵T por densidad (si el umbral de conteo cae bajo 1/2 usar el conteo total O(T log T)). El peso sin logaritmo es ≤exp(−4j). Sumar j desde c(log T/log log T)^(1/3)−1 y luego T=2^k: el exponencial restante vence toda potencia de k. La simetría cubre ordenadas negativas.

**Aplicación.** En la cola de la afirmación log x≪log |γ| y x≤|γ|⁴(log x)^(4A). Para β≥1/2, |V(ρ)|≤2C/γ² por 112; así el término normalizado por √x y multiplicado por (log x)^K está dominado por una constante por (log |γ|)^(K+2A)|γ|^[−4(1−β)]. La cola del mayorante tiende a cero. Para β<1/2 usar x^(β−1/2)≤1 y Σ(log |γ|)^K/γ²<∞. Esto prueba la cota.

**Qué puede producir un exceso.** En todas las escalas grandes el aporte absoluto de los ceros sobre la recta, dividido por √x V(1/2), es <0.487 incluso sin RH global (argumento de 112 aplicado a todo el subconjunto crítico). Los cuadrados aportan (1/2+o(1)) en esa normalización por PNT. Por ello si E(x)≥0 a escalas arbitrariamente grandes, la suma firmada −Σ x^ρ V(ρ) de los ceros fuera de la recta por debajo de H(x) tendrá que aportar al menos (0.013−o(1))√x V(1/2) allí. Se puede exigir 1/2<β: el total con β<1/2 es o(√x) por convergencia dominada. La parte baja fuera de la recta sigue sin cota útil. No se afirma que la mera presencia de un cero cause un exceso en esa escala, ni se presupone que el supremo de partes reales se alcance.
