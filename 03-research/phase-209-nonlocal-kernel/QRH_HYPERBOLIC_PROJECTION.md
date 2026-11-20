# QRH7/8 — balance compensado y geometría hiperbólica del portador

2026-10-19. **PROVED: cálculo geométrico, cota de momentos e inflexión.**
Revisión independiente de las fórmulas y asintóticas. **OPEN: enlace de
signo con Q_T.** No se afirma una nueva estimación de los primos.

## 0. Corpus, diferencia y fuente

Consultados las reglas del proyecto, índice ROUTES-TRIED-INDEX, grid maestro y
CROSSWORD-TO-D.md. Antecedentes: SKELETON_001/AUDIT_205_SKELETON_001,
RFIN_TRACT_001 y modelos hiperbólicos R186_043. No se reabre el kernel
Green polar ni la acotación genérica de psi−x como fuente de signo.
El cálculo adicional es la norma EXACTA del perfil proyectado, su
dependencia en la frecuencia y la posición de su inflexión. Es un
diagnóstico geométrico, no una nueva ruta que esquive aquellos fallos.

Fuente externa examinada: OpenAI30Sept2026, introducción y§§19–20,
https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf .
No se auditó integralmente el manuscrito externo.

## 1. Qué conservar del argumento7/8

El argumento combina estimaciones de momentos de polinomios inversos
y ordinarios, con selección de primos y un balance de parámetros.
Lemma20.2 y(20.9) certifican −E_*≥49/440640 para un EXPONENTE
COMPENSADO, mediante una identidad polinómica de signo explícito.
Ese número no es un margen de coercividad de Q_T.

La lección aplicable es conservar la compensación antes de estimar las
piezas. Para usarla en017 faltan estimaciones aritméticas válidas del
resto que permitan un balance semejante. La técnica no crea esas cotas.
No se importa un signo de la familia auxiliar a la forma del paper47.

## 2. Cota exacta de un momento hiperbólico

En H=L²_even(−T,T), o su complejificación, sea h_b(x)=cosh(bx), b>0,
y P_b la proyección ortogonal sobre h_b^perp. Definir

    I_T(z,b)=sinh((z+b)T)/(z+b)+sinh((z−b)T)/(z−b),
    I_T(b,b)=T+sinh(2bT)/(2b),

con los cocientes extendidos por continuidad. Para u_z(x)=cosh(zx),

    ||P_b u_z||²=||u_z||²−|I_T(z,b)|²/I_T(b,b).       (1)

Prueba: integrar cosh(zx)cosh(bx) por producto a suma y aplicar la
fórmula de proyección de rango uno. Para F⊥h_b, Cauchy–Schwarz da

    |<F,u_z>|² ≤ ||F||² ||P_bu_z||².                (2)

Es una cota efectiva para todo test de ese subespacio, sin información
de ceros. Para tests reales pares también acota el momento de Laplace
∫F(x)cosh(zx)dx. El factor es óptimo en el espacio complejificado.
En el portador par polar libre del proyecto, b=1/2.

## 3. Asíntota real y frecuencia compleja

Sean 0<a<b y gamma reales FIJOS, z=a+i gamma. Integración directa da

    ||u_z||²=sinh(2aT)/(2a)+sin(2 gamma T)/(2 gamma),

interpretando el segundo sumando como T si gamma=0. Cuando T→∞,

    ||u_z||² ~ exp(2aT)/(4a),
    I_T(z,b) ~ exp((a+b+i gamma)T)/(2(a+b+i gamma)).

Sustituir en(1) prueba

    ||P_bu_z||² / ||u_z||²
       → [(b−a)²+gamma²]/[(b+a)²+gamma²].            (3)

Para gamma=0, equivalentemente,

    ||P_b cosh(ax)||²
       ~ exp(2aT)(b−a)²/[4a(a+b)²].                (4)

El número3/8=7/8−1/2 motiva probar a=3/8 como PERFIL MODELO.
Con b=1/2 se obtiene

    ||P_(1/2)cosh(3x/8)||² ~ (2/147)exp(3T/4),
    razón residual → 1/49,
    razón compleja → [gamma²+1/64]/[gamma²+49/64].  (5)

La atenuación1/49 corresponde sólo al perfil real, sin oscilación.
La razón de(3) tiende a1 al tomar después |gamma|→∞. No se ha usado
uniformidad en un límite conjunto. Incluso para T fijo, la fórmula
explícita da I_T(a+i gamma,b)=O_T(1/|gamma|), mientras ||u_z||²
tiende a sinh(2aT)/(2a)>0. Así la proyección quita una fracción
tendente a cero al crecer la frecuencia.

Las asíntotas(3)–(4) no se extienden sin justificación a a=0. En ese
caso particular, para b=1/2, la fórmula exacta es

    ||P_(1/2)1||²
       =2T−16sinh²(T/2)/(T+sinh T)=2T−8+o(1).

## 4. Dónde sí aparece un cambio de convexidad

Cosh(ax) es convexa globalmente: su segunda derivada es a²cosh(ax)>0
para a≠0. Sinh(ax), a>0, cambia de convexidad en0. El perfil corregido

    v_T(x)=cosh(ax)−c_T cosh(bx),
    c_T=I_T(a,b)/I_T(b,b),

sí presenta otra geometría. Para0<a<b fijos,

    c_T ~ [2b/(a+b)]exp(−(b−a)T).

La razón cosh(ax)/cosh(bx) decrece estrictamente en x>0: su derivada
logarítmica es a tanh(ax)−b tanh(bx)<0. Por tanto v_T'' se anula
como máximo una vez en(0,T). Para T suficientemente grande v_T''(0)>0
y v_T''(T)<0, pues

    c_T b²cosh(bT)/(a²cosh(aT))
       → K=2b³/[a²(a+b)]>1.

Existe entonces una única inflexión positiva x_inf(T), y

    x_inf(T)=T−log(K)/(b−a)+o(1).                 (6)

Para justificar la posición, primero x_inf→∞ porque c_T→0; se pueden
entonces usar las equivalencias exponenciales en la ecuación v_T''=0.
En a=3/8,b=1/2 la distancia al borde tiende a8log(128/63).
En todo el intervalo hay dos inflexiones simétricas, no una sola.

## 5. Alcance para D

Las fórmulas son cotas y límites sobre el portador polar libre, pero no
identifican la fluctuación real de los primos con estos perfiles. Una
región libre7/8 no da una identidad E(e^x)exp(−x/2)=cosh(3x/8), ni
su signo, amplitud o frecuencia. El cambio de convexidad tampoco decide
el signo de Q_T(v_T).

Insight preciso: la eliminación polar reduce perfiles próximos a ella,
pero no proporciona una atenuación uniforme en frecuencia. El cálculo
deja visible qué parte no podría pagar un argumento basado solamente
en cercanía geométrica a cosh(x/2). No excluye controles aritméticos
adicionales. No se demostró el contratermino017 ni se integró paper47.
