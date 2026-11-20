# AUDIT_017 — Ensayo de métrica virtual y fuente de saltos

2026-10-19. Revisor hostil independiente. **PASA / PROVED con el alcance
declarado.** Revisado `VIRTUAL_SOURCE_017_METRIC_TEST.md`, con008,011,
NODE_001, las entradas del índice de rutas, grid y crucigrama actual.
No se construye una ruta adicional ni se modifica Paper47.

## 1. Métrica y dominio

Multiplicar por τ es una isometría sobreyectiva del espacio virtual al
L² de peso y^(α−1): la inversa divide por τ>0. Las fórmulas conjugadas
de dilatación e inversión son correctas. Por ello G_n es unitario,
J_virt es una involución unitaria y J_virt G_n J_virt=G_n^*=G_(1/n).
Se ha cambiado el espacio de Hilbert respecto de008; estas afirmaciones
no reparan los adjuntos en la métrica anterior ni prueban invariancia
de su módulo aritmético completado.

La cota de §2 es correcta. De W_d=m(y)/d−m(d²y)<0 y
0<m(t)≤min(1,t^(-1/2)) resulta
|W_d|≤min(1,(d√y)^(-1)). Integrar su cuadrado antes y después de
y=d^(-2) da exactamente

`[1/α+1/(1−α)]d^(-2α)`, para 0<α<1.

La convergencia con los coeficientes de011 sigue de la suma de normas
Σd^(-1−α). No se la usa para recuperar un enlace ya refutado.

## 2. Mapa y energías

El factor1/√2 de C_α es correcto: tras y=exp(2x), su norma virtual
se convierte exactamente en la norma L²(dx). La fórmula inversa prueba
sobreyectividad. G_n corresponde a F(x+log n) y J_virt a F(−x).

Para la extensión por cero de los tests de ventana,

`(1/2)||F−F(·+u)||²=||F||²−Re c_F(u)`.

Esto verifica (4), incluido el coste A_T. La energía gamma usa todo
el intervalo u∈(0,∞), con el mismo kernel positivo K que NODE_001/P47.
Para u>2T la correlación es cero; su contribución es precisamente la
cola κ_T||F||² que aparece al escribir la fórmula sólo hasta2T.
Así no falta un término de borde o de cola. La integral puede ser
infinita fuera del dominio de forma, como advierte el memo; sobre el
dominio gamma ambas expresiones coinciden.

La suma finita del peine incluye sólo n<exp(2T); no hay problema con
n=1 porque Λ(1)=0, ni con el extremo porque c_F(2T)=0. Las partes reales
permiten la versión hermítica; en el portador real coinciden con las
fórmulas bilineales de NODE_001.

## 3. Identidad total y alcance del fallo

En el sector par de momento cosh nulo, Q_T=𝔞_T. Sustituir la energía
de saltos en la fórmula gamma da exactamente

`Q_T(F)=E_pos^virt(C_αF)−(A_T−C₀)||F||²`.

C₀=ψ(1/4)−logπ<0 y A_T≥0, por lo que el contratermino es estrictamente
negativo para F≠0. Esto refuta la identificación de Q_T con la fuente
positiva propuesta y la dominación Q_T≥E_pos para esta fuente. No
refuta Q_T≥0: la energía positiva puede superar ese coste, pero el
ensayo no demuestra la desigualdad necesaria. El memo mantiene esta
distinción correctamente.

La representación virtual funciona para cualquier perfil medible,
finito y estrictamente positivo casi en todas partes; en particular
para los perfiles de theta con borrado finito mencionados. Después
de C_α, ese perfil desaparece. Por tanto la unitariedad y la inversión
no seleccionan la completitud del Euler ni el conductor1. Los pesos
Λ del peine se introducen explícitamente, y su signo no paga por sí
solo el contratermino.

La diferencia escrita respecto de008 es un cambio concreto de métrica
para diagnosticar esa realización; la descomposición final vuelve a
la energía de saltos y potencial de P1_BBSTAR/INV_N, como reconoce017.
No se registra como nuevo puente ni como reapertura de ese mecanismo
de signo. Tampoco es un NO-GO para otras virtualizaciones, otros
contraterminos o un enlace adicional futuro.

**Veredicto:** fuente auxiliar positiva bien realizada, identidad total
correcta, fuente aún no funcional para el signo del nodo. Ningún nuevo
signo de Q_T ni cierre de la fila D.
