# POWER_THETA_AUDIT_073 — Hazard theta, dos copias y todos los pares reales

Estado: **APROBADO** el ensamblaje de POWER_THETA_HAZARD_COMPACT_073, el tramo exterior10343 y POWER_THETA_TWO_COPY_073. Reproducción independiente del certificado compacto: **exit0/PASS,4096 paneles**. Papers y phase103 intactos.

Consultados las reglas del proyecto, índice/grid/crucigrama, CONE001, BRIDGE002, SCHUR003 y los antecedentes10334/10339/10342/10343. La búsqueda dirigida no encontró previamente L''<0 y L−(a−1/2)L'>0 en TODO a>1, ni el cierre de TODOS los pares de potencias en ese rango. CONE001 dejaba ese rango por debajo32 abierto. Los bloques de tasas altas posteriores no resuelven esa extensión. La aplicación actual no usa el modelo ferromagnético sobre primos del antiguo frenteJ.

## Revisión independiente del tramo exterior

Se rederivaron explícitamente las constantes9–14 de10343, sin dar por supuesto su argumento histórico. Escriba z=ax, a=m²−1>=3 y x>=9/2. Para las logderivadas de r_m se tiene:

    Dlogr_m=−2ax+6/(2m²x−3)−6/(2x−3),
    D²logr_m=−4ax+A(x)−A(m²x), A(y)=24y/(2y−3)²,
    D³logr_m=−8ax+B(m²x)−B(x), B(y)=48y(2y+3)/(2y−3)³.

A yB decrecen para y>=9/2, con A(9/2)=3 y B(9/2)=12. Esto prueba las cotas3z,5z,10z declaradas; las fórmulas de derivación exponencial dan luego3zr_m,10z²r_m,35z³r_m porque z>=27/2.

La cota r_m<=2m⁴exp(−ax) y m⁴<=16a²/9 permiten ampliar la suma a TODOS los enteros a>=3. Las potencias de a relevantes son3,4,5. Sus primeros términos son1296,58320,2755620 divididos por729000. Separar a=3 deja razón inicial(4/3)^r/90 y razones posteriores<=(5/4)^r/90. Se comprobaron independientemente con Fraction la suma Taylor hasta grado14 que da exp(9/2)>90 y los tres majorantes geométricos: resultan<19/10000,83/1000,397/100, respectivamente. La combinación cúbica en la derivada de log(1+R) es<4. Los majorantes disminuyen conx, pues ax>=13.5 supera todos los grados usados.

El primer modo cumple ell_1'''<=−36+12=−24 por el mismo descenso deB. Por tanto(logPhi)'''<−20 para t>=1/4. No se detectó un hueco exterior ni una cola omitida.

## Certificado compacto y empalme

Leídos íntegros POWER_THETA_HAZARD_COMPACT_073 y tools/power_theta_compact_073_verify.py. El factor pi exp(5t/2) tiene logaritmo afín y no contribuye a la cuarta derivada. La recurrencia Q_(r+1)=2y(Q_r'−Q_r), sus cinco polinomios y el numeradorNUM de la cuarta logderivada son correctos.

Para m>=5, el majorante9600·3⁵m¹²2^(−4m²) controla CADA derivada0..4, usando y>=3m² y el descenso de y⁵exp(−y). Su razón desde5 es<1/2 y decrece después. El resto completo es exactamente4449462890625/4951760157141521099596496896 y se añade bilateralmente a cada suma antes deNUM.

Las operaciones enteras implementan suelo/techo exteriores correctos, incluidos productos de signos arbitrarios. Los recíprocos se usan sólo con intervalos positivos. Machin128 y el resto bilateral atan son válidos. Para exp, el argumento reducido es<=1, la cola Taylor128 está entre0 y2/129!, y siete cuadrados recuperan el argumento original; todos los rangos se comprueban. Las potencias y el Horner intervalar mantienen recintos aunque puedan ser conservadores.

Mi reproducción independiente con python3 terminó exit0: PASS en los4096 paneles fijos, conNUM.upper<0 yS.lower>0 en cada intervalo cerrado. La unión cubre[0,1/4] sin huecos. La salida imprime extremos racionales y losQ exactos; no utiliza signos flotantes. La paridad suave dePhi, ya establecida mediante su identidad modular, da(logPhi)'''(0)=0. Integrar la cuarta derivada negativa prueba(logPhi)'''<0 en0<t<=1/4 y empalma con el tramo exterior. Se obtiene V'''(t)>0 para TODO t>0, V=−logPhi.

## Argumento de dos copias

Revisado POWER_THETA_TWO_COPY_073 completo bajo sus hipótesis explícitas: V parC³, V'''>0 en la semirrecta positiva y crecimiento superlineal. Este crecimiento asegura todos los momentos inclinados; no se introducen hipótesis ocultas sobre la integrabilidad deV'.

El factor de la identidad M''=4Cov(S,D²) es correcto. Para0<=s1<s2, Delta'(d)=integral_(s1)^(s2)[V''(t+d)−V''(t−d)]dt es estrictamente positivo end>0, porque V'' aumenta estrictamente con|x|. Así el cociente de densidades condicionales decrece estrictamente con|d| y g(s)=E[D²|S=s] decrece estrictamente con|s|. El argumento usa covarianzas entre funciones de monotonías opuestas y momentos finitos; no diferencia un integral conV' no controlado.

La marginal deS tiene factor par por exp(2us), por lo que E[S||S|=r]=r tanh(2ur), estrictamente creciente parar>0,u>0. Condicionar otra vez daCov(S,D²)<0, con integrabilidad del producto garantizada por los momentos de orden3. De ahí M''(u)<0. Finalmente M(0)=0 y(M−uM')'=−uM''>0 prueban0<uM'(u)<M(u). Las estrictitudes se justifican por las densidades positivas en toda la recta.

## Corolario específico y alcance

El certificado compacto y el exterior descargan la hipótesis theta que aparecía CONDITIONAL en el memo de dos copias. Positividad, paridad, suavidad y decaimiento superexponencial son los del MISMO kernelPhi de CONE001. Su identidad real daM(u)=L(u+1/2). Por tanto, para TODO a>1,

    L'(a)>0, L''(a)<0,
    L(a)−(a−1/2)L'(a)>0.

Integrar el bound de cocientes permite aplicar el criterio exacto de CONE001 a TODOS los pares a,b>1. Para exponentes distintos, su matriz2x2 es definida positiva; al coincidir exponentes se combinan primero los coeficientes y permanece la positividad del único generador no nulo. Los términos aritméticos y el polar están incluidos por la identidad de polarización deCONE001; no es sólo una desigualdad del símbolo arquimediano.

Esto resuelve el rango de pares que CONE001 dejaba abierto por debajo32. No prueba matrices de orden arbitrario, la tabla suficiente completa, una ventana temporal nueva ni el signo global. La comparación de inclinaciones polinómicas superiores10343 sigue siendo otra obligación. La aprobación no convierte la concavidad escalar deL en un principio general Pick ni en una inducción de todos los órdenes.
