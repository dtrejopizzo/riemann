# Documento 173 — La representación estructural de $I(0^+)$: sumas-regla, el teorema sombra–señal, y la identidad de Green–Littlewood

**Programa:** Hipótesis de Riemann — Fase 55 (dos flechas)
**Fecha:** 2026-06-11
**Mandato (Problema A / Fase A):** representar $I(0^+)=\sum_j b_j^2$ como funcional aritmético natural — idealmente $I=\|F\|_{\mathcal H}^2$ — de modo que $I<\infty$ (y en última instancia $I=0$) sea una pregunta de regularidad/pertenencia y no de localización de ceros. NO se intenta probar RH ni positividad alguna.
**Maquinaria aceptada (no re-derivada):** ley de balance $\dot I=-2\kappa-D$ (Fase 54); $E(T)=\sum_{\gamma\le T}b^2\ll T/\log T$ (Selberg, certificado); RH $\iff I(0^+)=0$; techo $T/\log T$ para certificación por ventanas (Teorema 172.9 — aquí no se reintentan ventanas).
**Contrato:** [DEFINICIÓN-NUEVA] libre; [TEOREMA]/[PROP]/[LEMA] con prueba completa o sin etiqueta; [PUENTE] honesto; [GAP] declarado.

**Coordenadas (idénticas al Doc 170/175).** Cero off-crítico $\rho=\tfrac12+b+i\gamma$, $b\in(0,\tfrac12)$, $\gamma>0$; un representante por cuádruplo $\{\rho,\bar\rho,1-\rho,1-\bar\rho\}$. Ceros en línea: pares $\{\tfrac12\pm i\gamma\}$.
$$I=I(0^+):=\sum_{\text{cuád. }j} b_j^2,\qquad I(T):=\sum_{\gamma_j\le T}b_j^2 .$$

---

## 0. Resumen ejecutivo y veredicto

**El entregable duro se cumple en sus dos vertientes, y son complementarias:**

1. **[TEOREMA 173.A] (sombra–señal — la obstrucción).** En la clase $X$ de representaciones holomorfas autocontenidas ($\sum_\rho\Phi(\rho)$ con $\Phi$ holomorfa, la clase que alcanza la fórmula explícita), el peso cuadrático que multiplica a $b^2$ es **exactamente la curvatura de la sombra**: $w_\Phi(\gamma)=-2\,\varphi_r''(\gamma)$ donde $\varphi_r=\mathrm{Re}\,\Phi$ en la línea crítica. Consecuencias exactas: *no hay señal sin sombra*; si $w_\Phi\ge0$ entonces $\int_0^\infty w_\Phi=2\varphi_r'(0)<\infty$ (todo peso admisible es **integrable**: ni peso $1$ ni siquiera $1/\gamma$ son alcanzables) y $\int_0^\infty t\,w_\Phi(t)\,dt=2|\varphi_r(0)|$ (**ley de masa-altura**: peso hasta altura $T$ cuesta sombra de profundidad $T^2$). Esta es la razón estructural del techo 172.9 vista desde otra cara: no es un artefacto de las ventanas sino de la **holomorfía de la sonda**. La extensión a funcionales cuadráticas (Parseval, $\int|\mathcal E|^2$) es la [PROP 173.D].

2. **[TEOREMA 173.C] (la identidad de Green–Littlewood — la representación).** La salida es **no-holomorfa** ($\log|\zeta|=\mathrm{Re}\log\zeta$; tomar parte real no es holomorfo, exactamente el escape que 173.A predice). Identidad exacta e incondicional, **con peso 1 en $\gamma$** (sin peso decayente):
$$\boxed{\;I(T)\;=\;\frac1\pi\int_{1/2}^{\infty}\!\!\int_0^T \log|\zeta(\sigma+it)|\,dt\,d\sigma\;+\;\frac18\;-\;\frac{1}{2\pi}\int_{1/2}^\infty\!\Big(\sigma-\tfrac12\Big)^2\,\mathrm{Im}\,\frac{\zeta'}{\zeta}(\sigma+iT)\,d\sigma\;}$$
para todo $T$ que no sea ordenada de cero. El residuo ya **no es un peso multiplicativo** sino un **flujo aditivo de borde** a altura $T$, de tamaño $O(\log^2 T)$ en alturas buenas. $I$ es el **segundo momento transversal de la medida de Riesz de $\log|\zeta|$** en la semibanda derecha; el primer momento es Littlewood clásico, el momento cero es la densidad $N(\sigma,T)$.

3. **[PROP 173.E] (pertenencia, forma dicotómica).** Con $\tilde d$ = potencial de Green de los ceros off en el semiplano $\sigma>\tfrac12$ (sustraído el polo): RH $\iff \|\nabla\tilde d\|_{L^2}^2<\infty$, y la norma solo toma los valores $\{0,\infty\}$. Es la primera formulación literal de "RH = pertenencia a un espacio" dentro del programa — pero degenerada: la dicotomía atómica impide que la norma **gradúe** $I$. La obstrucción a $I=\|F\|^2$ exacta queda identificada: **la auto-energía infinita de los átomos** (los ceros son cargas puntuales). Programa de desingularización al final.

**Mejor representación lograda:** 173.C. **Peso que quedó:** ninguno en $\gamma$; el residuo es el flujo de borde $O(\log^2T)$ más la constante exacta $1/8$ (del polo en $s=1$), y el defecto de que el integrando $\log|\zeta|$ es *con signo* (es un momento de medida positiva, todavía no una norma cuadrática de objeto aritmético).

---

## 1. Preliminares: el cuádruplo y la clase de representaciones

**[DEFINICIÓN-NUEVA] (clase $X$ de representaciones holomorfas autocontenidas).** $\mathcal F\in X$ si existe $\Phi$ holomorfa en la franja abierta $0<\mathrm{Re}\,s<1$ con
(i) simetría real: $\Phi(\bar s)=\overline{\Phi(s)}$ y $\Phi(1-s)=\Phi(s)$;
(ii) decaimiento: $\varphi(t):=\Phi(\tfrac12+it)$ cumple $\varphi(t)\to0$, $\varphi'(t)\to0$ ($t\to\infty$), y $\sum_\rho|\Phi(\rho)|<\infty$ para toda configuración de ceros compatible con $N(T)\sim\frac{T}{2\pi}\log T$;
(iii) $\mathcal F=\sum_\rho\Phi(\rho)$.
Escribimos $\varphi_r:=\mathrm{Re}\,\varphi$ (la **sombra** de $\Phi$). La clase $X$ es exactamente la que alcanza la fórmula explícita de Weil: para $\Phi$ de tipo Mellin, $\sum_\rho\Phi(\rho)$ es un funcional aritmético explícito (lado de primos + término arquimediano). *Observación de simetrización:* el multiconjunto de ceros es invariante bajo $\rho\mapsto1-\rho$ y $\rho\mapsto\bar\rho$; por tanto, para cualquier $\Phi_0$ holomorfa, $\sum_\rho\Phi_0(\rho)=\sum_\rho\Phi(\rho)$ con $\Phi:=\tfrac14[\Phi_0(s)+\Phi_0(1-s)+\overline{\Phi_0(\bar s)}+\overline{\Phi_0(1-\bar s)}]$, que cumple (i). La hipótesis (i) no pierde generalidad dentro de $X$.

**[LEMA 173.0] (expansión del cuádruplo).** Sea $\Phi$ como en (i), holomorfa en un entorno del segmento $[\tfrac12-b,\tfrac12+b]\times\{\gamma\}$. Entonces la contribución del cuádruplo $\{\tfrac12\pm b\pm i\gamma\}$ es real y **par en $b$**, con
$$\Sigma_{\mathrm{cuád}}(b,\gamma)\;=\;4\,\varphi_r(\gamma)\;+\;b^2\,w_\Phi(\gamma)\;+\;R_4,\qquad
w_\Phi(\gamma):=2\,\mathrm{Re}\,\Phi''(\tfrac12+i\gamma)=-2\,\varphi_r''(\gamma),$$
$$|R_4|\;\le\;\frac{b^4}{6}\max_{|x|\le b}\big|\Phi^{(4)}(\tfrac12+x+i\gamma)\big| .$$
Un par en línea $\{\tfrac12\pm i\gamma\}$ contribuye $2\varphi_r(\gamma)$ exactamente.

*Prueba.* Por (i), $\Phi(\tfrac12+b-i\gamma)=\overline{\Phi(\tfrac12+b+i\gamma)}$, luego
$\Sigma_{\mathrm{cuád}}=2\,\mathrm{Re}\big[\Phi(\tfrac12+b+i\gamma)+\Phi(\tfrac12-b+i\gamma)\big]$.
Taylor en $b$ alrededor de $\tfrac12+i\gamma$: los órdenes impares se cancelan entre $+b$ y $-b$; quedan $2\,\mathrm{Re}[2\Phi+b^2\Phi''+\tfrac{2b^4}{4!}\Phi^{(4)}(\xi)]$ con resto de Lagrange en el segmento. La identidad $\mathrm{Re}\,\Phi''(\tfrac12+i\gamma)=-\varphi_r''(\gamma)$ sale de $\varphi(t)=\Phi(\tfrac12+it)\Rightarrow\varphi''(t)=-\Phi''(\tfrac12+it)$. La paridad en $b$ también se ve estructuralmente: $b\mapsto-b$ permuta el cuádruplo. $\square$

**Lectura.** En toda la clase $X$: el **orden cero** (la sombra $4\varphi_r(\gamma)$, evaluada en las ordenadas verdaderas, que no son datos aritméticos por separado) y la **señal** ($b^2w_\Phi$) están soldados por $w_\Phi=-2\varphi_r''$. Todo lo que sigue en §2–§4 explota o sufre esta soldadura.

---

## 2. Las sumas-regla de Hadamard: el álgebra exacta del cuádruplo

### 2.1. La suma-regla básica y la extracción exacta de $b^2$

Del producto de Hadamard de $\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$ (Hadamard 1893; Davenport, *Multiplicative Number Theory*, cap. 12):
$$\sum_\rho\frac1\rho\;=\;1+\frac{\gamma_E}2-\frac12\log 4\pi,\qquad\Longrightarrow\qquad
\sum_\rho\frac1{\rho(1-\rho)}\;=\;2+\gamma_E-\log 4\pi\;\approx\;0.0462,$$
usando $\frac1{\rho(1-\rho)}=\frac1\rho+\frac1{1-\rho}$ y que $\rho\mapsto1-\rho$ permuta los ceros. **Incondicional y aritmética.**

**Álgebra del cuádruplo (exacta, real).** Con $a:=\tfrac14+\gamma^2$, $A:=a-b^2$, $B:=2b\gamma$: para $\rho=\tfrac12+b+i\gamma$ se tiene $\rho(1-\rho)=\tfrac14-(b+i\gamma)^2=A-iB$, y $\rho$, $1-\rho$ dan el mismo valor; $\bar\rho$, $1-\bar\rho$ dan $A+iB$. Por tanto
$$\Sigma_{\mathrm{cuád}}\Big[\tfrac1{\rho(1-\rho)}\Big]\;=\;\frac{4A}{A^2+B^2}
\qquad\text{(real, exacto)} .$$
La extracción exacta de $b^2$ contra el valor en línea (con la multiplicidad 4 del cuádruplo):
$$\frac{4A}{A^2+B^2}-\frac4a\;=\;-\,\frac{4\,b^2\,\big(3\gamma^2-\tfrac14+b^2\big)}{a\,\big(A^2+B^2\big)}
\;=\;\frac{b^2\,(1-12\gamma^2)}{(\tfrac14+\gamma^2)^3}\;+\;O\!\Big(\frac{b^4}{\gamma^6}\Big).$$
*(Verificación cruzada con el Lema 173.0: $\Phi=1/(s(1-s))=(\tfrac14-u^2)^{-1}$, $u=s-\tfrac12$, da $2\,\mathrm{Re}\,\Phi''(\tfrac12+i\gamma)=(1-12\gamma^2)/a^3$. Coincide.)*

**Conclusión de la suma-regla básica:** la energía aparece con peso exacto $w(\gamma)=(1-12\gamma^2)/(\tfrac14+\gamma^2)^3\sim-12/\gamma^4$ — peso $1/\gamma^4$, **negativo** en $\gamma>1/\sqrt{12}$, y soldado a la sombra no-aritmética $\sum_j 4/a_j$. Tal como anunciaba el puntero del director.

### 2.2. La familia completa de momentos en $s=\tfrac12$

$\xi(\tfrac12+w)$ es par y entera de orden 1; sus ceros en $w$ son $\pm(b_j\pm i\gamma_j)$ (en línea: $\pm i\gamma_j$). Tomando $\log$ del producto de Hadamard ($\xi(\tfrac12+w)=\xi(\tfrac12)\prod_j(1-w^2/w_j^2)$, $w_j$ los ceros del semiplano superior):
$$\log\xi(\tfrac12+w)-\log\xi(\tfrac12)\;=\;-\sum_{k\ge1}\frac{M_k}{k}\,w^{2k},
\qquad M_k:=\sum_j\frac1{w_j^{2k}} .$$
Los $M_k$ son **aritméticos e incondicionales** (coeficientes de Taylor de $\xi$ en $\tfrac12$, computables desde la serie de $\eta$/constantes de Stieltjes; p.ej. $M_1=-\,\xi''(\tfrac12)/(2\,\xi(\tfrac12))$). Análogamente $\sum_\rho(\rho(1-\rho))^{-k}$ se expresa polinomialmente en $M_1,\dots,M_k$ vía $\rho(1-\rho)=\tfrac14-w^2$.

**Álgebra del cuádruplo para $M_k$ (exacta).** Los dos ceros superiores del cuádruplo son $b+i\gamma$ y $-b+i\gamma$, y $(-b+i\gamma)^{2k}=(b-i\gamma)^{2k}$:
$$\Sigma_{\mathrm{cuád}}\Big[\tfrac1{w^{2k}}\Big]\;=\;2\,\mathrm{Re}\,(b+i\gamma)^{-2k}
\;=\;\frac{2(-1)^k\cos\!\big(2k\arctan(b/\gamma)\big)}{(b^2+\gamma^2)^k}
\;=\;\frac{2(-1)^k}{\gamma^{2k}}\Big(1-\frac{2k^2b^2}{\gamma^2}+O\big(\tfrac{k^2b^2}{\gamma^2}\big)^2\Big)\Big(1+O\big(\tfrac{kb^2}{\gamma^2}\big)\Big).$$
**Señal:** $b^2$ con peso $\asymp k^2/\gamma^{2k+2}$. Subiendo $k$ el peso se concentra en el primer cero y decae aún más rápido en $\gamma$: la familia de momentos en un punto fijo **no des-pesa**; mueve el peso hacia abajo. Para des-pesar hay que superponer (punto móvil / familia infinita) — §3 y §4 dicen exactamente hasta dónde se puede.

---

## 3. El teorema sombra–señal: la obstrucción exacta en la clase $X$

**[TEOREMA 173.A] (sombra–señal).** Sea $\Phi$ de clase $X$ (Def. §1), con $\varphi_r\in C^2[0,\infty)$ y $w_\Phi:=-2\varphi_r''$. Entonces:

**(a) (soldadura)** En la expansión del Lema 173.0, el peso cuadrático es $w_\Phi=-2\varphi_r''$: la señal es exactamente $(-2)\times$ la curvatura de la sombra. En particular $w_\Phi\equiv0\iff\varphi_r$ afín $\iff$ (por $\varphi_r\to0$) $\varphi_r\equiv0$: **no hay señal sin sombra**, y la sombra $\sum_j4\varphi_r(\gamma_j)$ se evalúa en las ordenadas verdaderas (no es un dato aritmético separado del propio $\sum_\rho\Phi(\rho)$).

**(b) (ley de masa)** Si $w_\Phi\ge0$ en $[0,\infty)$, entonces $\varphi_r$ es cóncava, $\varphi_r\le0$, $\varphi_r'\ge0$ decreciente, y
$$\int_0^\infty w_\Phi(t)\,dt\;=\;2\,\varphi_r'(0)\;<\;\infty .$$
**Todo peso no negativo de la clase $X$ es integrable.** Peso constante, $w\sim1$, e incluso $w\sim1/\gamma$, son inalcanzables.

**(c) (ley de masa-altura)** Bajo (b), además
$$\int_0^\infty t\,w_\Phi(t)\,dt\;=\;-2\,\varphi_r(0)\;=\;2\,|\varphi_r(0)|\;\le\;2\,\|\varphi_r\|_\infty .$$
Colocar masa de peso $\ge\delta$ en alturas $\sim T$ cuesta profundidad de sombra $\gtrsim\delta T^2$ en $t=0$.

**(d) (cola negativa)** Si en cambio $\varphi_r\ge0$ y $\varphi_r\to0$ con $\varphi_r\not\equiv0$, entonces $w_\Phi<0$ en una sucesión $t_n\to\infty$ (toda sombra positiva decreciente tiene cola convexa). Las sumas-regla "naturales" (resolventes positivas, §2.1) tienen peso negativo en la cola **necesariamente**.

*Prueba.* (a) es el Lema 173.0 más: $\varphi_r$ afín y $\to0$ $\Rightarrow$ $\varphi_r\equiv0$.
(b) $w_\Phi\ge0\Rightarrow\varphi_r''\le0$: cóncava. Si $\varphi_r'(t_1)<0$ para algún $t_1$, la concavidad da $\varphi_r'\le\varphi_r'(t_1)<0$ en $[t_1,\infty)$ y $\varphi_r\to-\infty$, contra $\varphi_r\to0$. Luego $\varphi_r'\ge0$ en todas partes y decreciente; su límite es $0$ (si fuera $>0$, $\varphi_r\to\infty$). Entonces $\varphi_r$ es creciente con límite $0$, luego $\varphi_r\le0$; y $\int_0^\infty w_\Phi=-2\int_0^\infty\varphi_r''=2(\varphi_r'(0)-\lim\varphi_r')=2\varphi_r'(0)$.
(c) $\int_0^X t\,w_\Phi=-2\int_0^X t\varphi_r''=-2X\varphi_r'(X)+2(\varphi_r(X)-\varphi_r(0))$. Como $\varphi_r'\ge0$ decrece y $\int\varphi_r'=\varphi_r(\infty)-\varphi_r(0)$ converge, $X\varphi_r'(X)\le2\int_{X/2}^X\varphi_r'\to0$. Queda $-2\varphi_r(0)$.
(d) $\varphi_r\ge0$, $\to0$, $\not\equiv0$: si $w_\Phi\ge0$ a partir de algún $T_0$, por (b)-localizado $\varphi_r\le0$ en $[T_0,\infty)$, luego $\varphi_r\equiv0$ ahí; prolongación analítica de $\Phi$ (su parte real en la línea es real-analítica al ser $\Phi$ holomorfa en un entorno) fuerza $\varphi_r\equiv0$. Contradicción. $\square$

**[COROLARIO 173.A.1] (ceguera incondicional de la clase $X$).** Si $w_\Phi\ge0$ es admisible (luego integrable y, digamos, decreciente a trozos), entonces por sumación parcial contra el certificado de Selberg $E(T)\ll T/\log T$:
$$\sum_j b_j^2\,w_\Phi(\gamma_j)\;\ll\;\int_1^\infty w_\Phi(t)\,d\Big(\frac{t}{\log t}\Big)\;<\;\infty\qquad\textbf{incondicionalmente}.$$
Toda energía pesada representable en $X$ es finita venga o no RH: en la clase $X$, la pregunta "¿$I_w<\infty$?" **no tiene contenido**; solo el valor exacto lo tiene. La representación de $I$ (peso 1) como pregunta de pertenencia exige salir de $X$. *(Es la misma frontera del techo 172.9, vista sin ventanas: allí el límite era el ruido de las ordenadas en la sombra; aquí, la integrabilidad forzosa del peso.)*

**[LEMA 173.B] (rigidez de Stieltjes: el des-pesado por superposición de sondas reales muere).** Sea $m\in C^1(0,\infty)$ con $m(a)\to0$ ($a\to\infty$), $\int_0^\infty(1+a)\,|m'(a)|\,da<\infty$. Si la superposición de resolventes en el eje real $\Phi_m:=\int_0^\infty \tilde\Phi_a\,m(a)\,da$ (donde $\tilde\Phi_a(s)=\tfrac12[(\tfrac12+a-s)^{-2}+(s+a-\tfrac12)^{-2}]$, de sombra $\varphi_{r,a}(t)=(a^2-t^2)/(a^2+t^2)^2$) **anula la sombra**, es decir
$$\int_0^\infty m(a)\,\frac{a^2-t^2}{(a^2+t^2)^2}\,da\;=\;0\qquad\forall\,t>0,$$
entonces $m\equiv0$.

*Prueba.* $\frac{a^2-t^2}{(a^2+t^2)^2}=-\partial_a\frac{a}{a^2+t^2}$. Integrando por partes (los bordes se anulan: en $a=0$ por el factor $a$, en $\infty$ por el decaimiento de $m$): $\int_0^\infty m'(a)\frac{a}{a^2+t^2}\,da=0$ para todo $t>0$. Con $u=a^2$, $g(u):=\tfrac12 m'(\sqrt u)$: $\int_0^\infty\frac{g(u)}{u+t^2}\,du=0$ para todo $t^2>0$. La transformada de Stieltjes de $g\,du$ (definida por la hipótesis de integrabilidad) se anula en $(0,\infty)$, luego en $\mathbb C\setminus(-\infty,0]$ por prolongación, luego $g\,du=0$ por la inversión de Perron–Stieltjes (Widder, *The Laplace Transform*, cap. VIII). Así $m'\equiv0$, $m$ constante, y el decaimiento da $m\equiv0$. $\square$

**Ilustración exacta de la rigidez (el cálculo $J=0$).** La única "superposición" que anula la sombra sin decaer es $m\equiv$ const (Lebesgue, excluida del lema por no decaer): en efecto $\int_0^\infty\frac{a^2-t^2}{(a^2+t^2)^2}\,da=\big[-\tfrac{a}{a^2+t^2}\big]_0^\infty=0$. Pero Lebesgue **también anula la señal**: el peso de segundo orden de la familia es $\propto\frac{(a^2-\gamma^2)^2-4a^2\gamma^2}{(a^2+\gamma^2)^4}$ y, con $a=\gamma x$ y las integrales beta $\int_0^\infty\frac{x^4\,dx}{(1+x^2)^4}=\int_0^\infty\frac{x^2\,dx}{(1+x^2)^4}=\frac{\pi}{32}$, $\int_0^\infty\frac{dx}{(1+x^2)^4}=\frac{5\pi}{32}$:
$$\int_0^\infty\frac{x^4-6x^2+1}{(1+x^2)^4}\,dx\;=\;\frac{\pi}{32}-\frac{6\pi}{32}+\frac{5\pi}{32}\;=\;0 .$$
(Razón estructural: $\int_0^\infty(a-i\gamma)^{-2k}\,da=\frac{(-1)^k\,i^{\,1}\,\gamma^{1-2k}}{2k-1}\cdot(-1)$ es **imaginario puro** para todo $k\ge1$, luego su parte real — sombra y señal por igual — se anula.) Veredicto: en la familia de sondas sobre el eje real, *sombra y señal mueren juntas o viven juntas*; no hay des-pesado por superposición. Mover las sondas a la línea crítica = ventanas = techo 172.9 (no se reintenta).

---

## 4. El programa de des-pesado: dónde cruza y dónde muere

### 4.1. Coeficientes de Li: el des-pesado máximo dentro de $X$

$\lambda_n=\sum_\rho[1-(1-1/\rho)^n]$ (Li 1997, *J. Number Theory* 65; Bombieri–Lagarias 1999, *J. Number Theory* 77: RH $\iff\lambda_n\ge0\ \forall n$; los $\lambda_n$ son aritméticos vía constantes de Stieltjes — Bombieri–Lagarias, y las asintóticas de Voros/Coffey [GAP de literatura: referencia exacta de Voros, *c.* 2004, "Sharpenings of Li's criterion"]).

**Álgebra exacta del cuádruplo.** $z:=1-1/\rho$ manda la línea crítica al círculo unidad y el cuádruplo a $\{z,\bar z,1/z,1/\bar z\}$ (cálculo directo: $z(\bar\rho)=\bar z$, $z(1-\bar\rho)=1/\bar z$). Con $z=e^{-u+i\theta}$:
$$\Sigma_{\mathrm{cuád}}\big[1-(1-1/\rho)^n\big]\;=\;4-4\cosh(nu)\cos(n\theta)\qquad\text{(exacto, real)},$$
y bajo $b\mapsto-b$ (que permuta el cuádruplo): $u\mapsto-u$, $\theta\mapsto\theta$ — par en $b$, como debe. Datos exactos: $|z|^2=1-\frac{2b}{(\frac12+b)^2+\gamma^2}$, luego $u=\frac{b}{\frac14+\gamma^2}+O(b^2/\gamma^2)$ (impar en $b$), y $\theta=\theta_\gamma+O(b^2)$ con $\theta_\gamma=\pi-2\arctan(2\gamma)\sim1/\gamma$. Expansión:
$$\Sigma_{\mathrm{cuád}}\;=\;\underbrace{\big[4-4\cos(n\theta_\gamma)\big]}_{\text{sombra}}\;\underbrace{-\;2\,n^2u_1^2\cos(n\theta_\gamma)\,b^2\;+\;O(nb^2)}_{\text{señal}},\qquad u_1=\frac1{\frac14+\gamma^2}.$$
**El des-pesado que SÍ se logra:** el peso de la señal es $\asymp n^2\cos(n/\gamma)/\gamma^4$. Promediando $\sum_n c_n\lambda_n$ con $c_n=g(n/N)$, el coseno localiza $\gamma\asymp N$ y la masa de peso efectiva en $\gamma\sim N$ escala como $N^3/\gamma^4\sim1/\gamma$: la familia de Li **inclina** el peso desde $1/\gamma^4$ hasta (casi) $1/\gamma$ por dyadas.

**Dónde muere:** exactamente en la frontera del Teorema 173.A. La superposición sigue dentro de $X$ ($\Phi(s)=\sum_nc_n[1-(1-1/s)^n]$), su sombra es $\sum_nc_n[4-4\cos(n\theta_\gamma)]$ — masivamente no nula en $\gamma\lesssim N$ — y la ley de masa-altura (173.A.c) tasa el cruce: peso $\sim1$ hasta altura $T$ exige sombra de profundidad $\sim T^2$, cuyo valor sobre las ordenadas verdaderas es exactamente la información no aritmética. El peso límite alcanzable es la frontera integrable; nótese que **incluso peso $1/\gamma$ quedaría corto y a la vez es inalcanzable**: con $E(T)\ll T/\log T$, $\sum b^2/\gamma\ll\log\log T$ — diverge *apenas*; la brecha entera entre "representable en $X$" y $I$ es logarítmica. (Misma constante de la casa: el techo $T/\log T$.)

### 4.2. Veredicto del des-pesado

[TEOREMA 173.A] + [LEMA 173.B] + 4.1: dentro de la clase holomorfa el des-pesado se mueve a lo largo de la frontera $\{\,w\ge0,\ \int w<\infty\,\}$ y **no la cruza**; la razón estructural es la soldadura señal = curvatura de la sombra, no la elección de ventanas (cara nueva del techo 172.9). El cruce exige sondas no holomorfas — §6.

---

## 5. Cramér y la ventana de impureza: el segundo orden en coordenadas de Laplace

### 5.1. La función de Cramér: factorización exacta del cuádruplo

$V(t):=\sum_{\mathrm{Im}\,\rho>0}e^{i\rho t}$ ($t>0$), estudiada por Cramér ("Studien über die Nullstellen der Riemannschen Zetafunktion", *Math. Z.* 4 (1919), 104–130): $V$ se prolonga meromórficamente con singularidades logarítmicas en $t=m\log p$ (los primos entran como singularidades) y una singularidad principal en $t=0$. [GAP de literatura: las constantes exactas de la singularidad en $0$ no se citan aquí de memoria; no se usan.]

**[PROP 173.Cr] (la energía es el coeficiente $t^2$ de Cramér).** Para $t>0$, agrupando por cuádruplos/pares (los ceros con $\mathrm{Im}\,\rho>0$ de un cuádruplo son $\tfrac12\pm b+i\gamma$):
$$e^{-it/2}\,V(t)\;=\;\sum_{\text{pares}}e^{-\gamma t}\;+\;\sum_{\text{cuád.}}2\,e^{-\gamma_j t}\cos(b_j t)
\;=\;C(t)\;-\;t^2\,I_L(t)\;+\;O\big(t^4{\textstyle\sum}b^4e^{-\gamma t}\big),$$
donde $C(t):=\sum_{\mathrm{Im}\rho>0}e^{-\gamma_\rho t}$ (la sombra de Laplace) e $I_L(t):=\sum_j b_j^2e^{-\gamma_jt}$, con $I(0^+)=\lim_{t\to0^+}I_L(t)$ (monótono). En particular $e^{-it/2}V(t)$ es **real** para $t>0$.

*Prueba.* $e^{i(\frac12\pm b+i\gamma)t}=e^{it/2}e^{-\gamma t}e^{\pm ibt}$; sumar y usar $2\cos(bt)=2-b^2t^2+2\cdot\frac{(bt)^4}{4!}\cos(\xi)$. $\square$

**Lectura honesta.** La sonda de Cramér está en la clase $X$ (familia $\varphi_t(\gamma)=e^{-\gamma t}$): su peso es $w_t(\gamma)=-2\,\partial_\gamma^2$-curvatura $=-2t^2e^{-\gamma t}$, de masa total $|\int w_t|=2t\to0$ — el límite $t\to0^+$ ilustra la ley de masa (173.A.b) en acción: la ventana de Laplace pierde toda su masa de peso exactamente cuando intenta capturar $I(0^+)$. Y el coeficiente $t^2$ de $V$ está contaminado por el coeficiente $t^2$ de la fluctuación de la sombra $C(t)$ (las ordenadas verdaderas), del mismo tamaño: la soldadura otra vez. **Cálculo cerrado pedido por el director: sí, la singularidad de Cramér en $t=0$ porta $I$ en su coeficiente de segundo orden ($-t^2I_L(t)$, Prop. 173.Cr), y no, no es extraíble dentro de $X$ (Teorema 173.A aplicado a $\varphi_t$).**

### 5.2. Funcionales cuadráticas: la obstrucción sube de orden

**[PROP 173.D] (clase $X_2$).** Sea $\mathcal H$ un espacio de Hilbert, $s\mapsto f_s\in\mathcal H$ débilmente holomorfa en la franja con la simetría del cuádruplo en cada variable del núcleo $K(s,s'):=\langle f_s,f_{s'}\rangle$, y $F:=\sum_\rho f_\rho-A$ con $A$ (centrado) fijo. Entonces, en la expansión simultánea de todos los cuádruplos:
$$\|F\|^2\;=\;\|F_0\|^2\;+\;2\sum_j b_j^2\,\mathrm{Re}\big\langle F_0,\;\partial_s^2f\big|_{\frac12+i\gamma_j}\big\rangle\;+\;O\Big(\big({\textstyle\sum}b^2\big)^2\sup\|\partial^2f\|^2\Big),$$
donde $F_0=\sum_j(\text{sombra})-A$ es la **fluctuación de sombra**. No aparece término $\sum b_j^2\,(\text{peso autónomo}\ge0)$: el término lineal en los desplazamientos se anula (paridad del cuádruplo, como en 173.0), el coeficiente de $b^2$ está **acoplado multiplicativamente a $F_0$**, y el primer término autónomo en los $b$ es $O\big((\sum b^2)^2\big)$ — tipo $\sum b^4$ y cruzados.

*Prueba.* $f(\tfrac12+b+i\gamma)+f(\tfrac12-b+i\gamma)=2f(\tfrac12+i\gamma)+b^2f''(\tfrac12+i\gamma)+O(b^4)$ (par en $b$, como en 173.0, ahora con valores en $\mathcal H$; los compañeros conjugados del cuádruplo se tratan igual). Luego $F=F_0+\delta$, $\delta=\sum_jb_j^2\,f''_j+O(\sum b^4)$, y $\|F\|^2=\|F_0\|^2+2\mathrm{Re}\langle F_0,\delta\rangle+\|\delta\|^2$ con $\|\delta\|^2=O((\sum b^2)^2\cdot\sup\|f''\|^2)$. $\square$

**Consecuencias.** (1) El sesgo del espectro de impureza (D152: sesgo $\sim-2\sqrt\pi\,m\,Te^{b^2T^2}$ en $\tau=\gamma$) al cuadrarse produce $\sum b^4$-tipo, consistente con 173.D: las normas cuadráticas de objetos aritméticos capturan $I_2=\sum b^4$ como término autónomo, **no** $I$. (2) El candidato del director $I\overset{?}=\int_0^\infty|\mathcal E(x)|^2dx$ con $\mathcal E$ aritmético cae en $X_2$ (núcleos $K(\rho,\bar\rho')=\int x^{\rho+\bar\rho'}d\mu$, holomorfos por variable): obstruido en la misma forma. (3) **Diagnóstico estructural:** $I=\|F\|^2$ exigiría $F$ *lineal* en los desplazamientos $b_j$ — pero todo funcional holomorfo del multiconjunto de ceros es par en cada $b_j$ (simetría del cuádruplo). Romper la paridad = seleccionar **medio cuádruplo** (solo $\beta>\tfrac12$) = operación no holomorfa. Eso es exactamente lo que hace $\log|\zeta|$ vía $N(\sigma,T)$. Entramos.

---

## 6. La salida no-holomorfa: $I$ como momento de la medida de Riesz (Green–Littlewood)

### 6.1. La identidad exacta

**[TEOREMA 173.C].** Sea $T>0$ que no sea ordenada de ningún cero. Entonces, incondicionalmente,
$$I(T)\;=\;\frac1\pi\int_{1/2}^{\infty}\!\!\int_0^T \log|\zeta(\sigma+it)|\,dt\,d\sigma\;+\;\frac18\;-\;\frac{1}{2\pi}\int_{1/2}^\infty\!\Big(\sigma-\tfrac12\Big)^2\,\mathrm{Im}\,\frac{\zeta'}{\zeta}(\sigma+iT)\,d\sigma,$$
con todas las integrales absolutamente convergentes. Además, para cada $n$ existe $T\in[n,n+1]$ ("altura buena", a distancia $\gg1/\log n$ de toda ordenada) con
$$\Big|\tfrac{1}{2\pi}\int_{1/2}^\infty(\sigma-\tfrac12)^2\,\mathrm{Im}\,\tfrac{\zeta'}{\zeta}(\sigma+iT)\,d\sigma\Big|\;\ll\;\log^2T .$$

*Prueba.* Sea $u(s):=\log|\zeta(s)|$, $v(\sigma):=\tfrac12(\sigma-\tfrac12)^2$, y $R=R_{A,T}:=[\tfrac12,A]\times[-T,T]$ con $A>2$. **(1) Estructura local de $u$.** Por la descomposición en fracciones parciales de $\zeta'/\zeta$ (Davenport, cap. 15–16) e integración, en un entorno de $R$ vale $u(s)=\sum_{\rho\in\mathcal Z}\log|s-\rho|-\log|s-1|+h(s)$ con $\mathcal Z$ el conjunto (finito) de ceros en un rectángulo ligeramente mayor y $h$ armónica en ese entorno (logaritmo de una función holomorfa sin ceros, localmente univaluado). **(2) Green por piezas.** La identidad de Green $\iint_R(u\Delta v-v\Delta u)=\oint_{\partial R}(u\,\partial_nv-v\,\partial_nu)$ vale para $h$ y $v$ (clásica, ambas lisas) y para cada pieza $\log|s-w|$ contra $v$ lisa (cálculo clásico del potencial: aporta el término $2\pi v(w)$ si $w\in R^\circ$; los ceros/polo en $\partial R$ están excluidos por hipótesis sobre $T$, y los ceros con $\beta=\tfrac12$ caen en la arista $\sigma=\tfrac12$ donde $v=v'=0$, aportando $2\pi v(\rho)=0$ — consistente). Con $\Delta v=1$:
$$\iint_R u\;-\;2\pi\Big[\sum_{\rho\in R,\ \beta>1/2} v(\rho)\;-\;v(1)\Big]\;=\;\oint_{\partial R}\big(u\,\partial_nv-v\,\partial_nu\big).$$
**(3) Conteo.** Cada cuádruplo con $|\gamma|<T$ tiene exactamente dos miembros con $\beta>\tfrac12$ en $R$ ($\tfrac12+b\pm i\gamma$), cada uno con $v=b^2/2$: $\sum v(\rho)=I(T)$. Y $v(1)=\tfrac18$.
**(4) Bordes.** (i) $\sigma=\tfrac12$: $v=0$ y $\partial_nv=-v'(\tfrac12)=0$: nada. (ii) $\sigma=A\to\infty$: $|u|,|\partial_\sigma u|\ll2^{-\sigma}$ y $v\ll\sigma^2$: ambas piezas $\to0$ y $\iint_Ru$ converge absolutamente (cerca de $s=1$, $\log|s-1|$ es integrable). (iii) $t=\pm T$: $\partial_nv=\pm\partial_tv=0$; queda $-\oint v\,\partial_nu=-2\int_{1/2}^\infty v\,\partial_tu(\sigma,T)\,d\sigma$ usando la simetría $u(\sigma,-t)=u(\sigma,t)$ (de $\zeta(\bar s)=\overline{\zeta(s)}$), que también da $\iint_Ru=2\iint_{0<t<T}u$.
**(5) Ensamblaje.** $2\iint_{0<t<T}u-2\pi I(T)+\tfrac{2\pi}8=-2\int_{1/2}^\infty v\,\partial_tu(\sigma,T)\,d\sigma$, y $\partial_tu=\mathrm{Re}[i\zeta'/\zeta]=-\mathrm{Im}\,\zeta'/\zeta$. Despejar $I(T)$ da la identidad.
**(6) Cota del flujo.** Para $\tfrac12\le\sigma\le2$: $\zeta'/\zeta(\sigma+iT)=\sum_{|\gamma-T|\le1}(\sigma+iT-\rho)^{-1}+O(\log T)$ (Davenport, cap. 15); hay $O(\log T)$ términos y en alturas buenas cada uno es $O(\log T)$: total $O(\log^2T)$. Para $\sigma\ge2$: $|\zeta'/\zeta|\le\sum\Lambda(n)n^{-2}\cdot(n/2)^{-(\sigma-2)}\ll2^{-\sigma}$, y $\int_2^\infty\sigma^22^{-\sigma}d\sigma=O(1)$. $\square$

**Verificación de consistencia en $T\to0^+$** (control del término $\tfrac18$): $I(T)\to0$ y $\iint\to0$; el flujo: cerca de $s=1$, $\zeta'/\zeta\sim-1/(s-1)$, luego $\mathrm{Im}\,\zeta'/\zeta(\sigma+iT)=\frac{T}{(\sigma-1)^2+T^2}+O(1)\to\pi\delta_{\sigma=1}$, y el término de flujo $\to-\frac1{2\pi}\cdot(\tfrac12)^2\cdot\pi=-\tfrac18$, que cancela el $+\tfrac18$ exactamente. ✓ *(Cross-check independiente: iterando el lema de Littlewood clásico (Littlewood 1924; Titchmarsh, **The Theory of the Riemann Zeta-Function**, §9.9) en $\sigma_0\in[\tfrac12,1]$ vía la identidad de capas $\sum_jb_j^2=2\int_{1/2}^\infty\sum_j(\beta_j-\sigma_0)_+^{\phantom{1}}\,$…$\,d\sigma_0$, el término $+\tfrac18$ reaparece como $\frac1\pi\int_{1/2}^1\pi(1-\sigma_0)\,d\sigma_0=\tfrac18$, proveniente de $\arg\zeta=\pi$ en $(\sigma_0,1)$ — el polo otra vez. Coinciden.)*

### 6.2. Lectura estructural: los tres momentos transversales

**[DEFINICIÓN-NUEVA] (medida de Riesz derecha).** $\mu^+:=\frac1{2\pi}\Delta\log|\zeta|\,\big|_{\{\sigma>1/2\}}+\delta_1$-corregida $=\sum_{\beta>1/2}\delta_\rho$: la medida (atómica, positiva) de los ceros del semiplano derecho. La coordenada transversal es $x(\rho):=\beta-\tfrac12=b$.

Entonces la familia de Green con $v_m=(\sigma-\tfrac12)_+^m$ da exactamente:
- $m=0$: densidades $N(\sigma,T)$ — la entrada de los teoremas de densidad;
- $m=1$: $\sum_{\gamma\le T}b_j=\frac1{2\pi}\int_0^T\log|\zeta(\tfrac12+it)|\,dt+O(\log T)$ — **lema de Littlewood clásico** (Littlewood 1924; Titchmarsh §9.9): el primer momento es la masa de $\log|\zeta|$ **sobre la línea**;
- $m=2$: **[TEOREMA 173.C]** — el segundo momento ($=I$) es la masa de $\log|\zeta|$ **sobre la semibanda**. La pieza $m=2$ ensamblada como representación de $I$ es la aportación de este documento; los ingredientes son clásicos (es la misma maquinaria con la que Selberg prueba $E(T)\ll T/\log T$ — honestidad de procedencia).

**Por qué 173.C esquiva 173.A:** $\log|\zeta|=\mathrm{Re}\log\zeta$ no es holomorfa, y la restricción a $\sigma>\tfrac12$ selecciona medio cuádruplo — exactamente las dos operaciones que la clase $X$ (y $X_2$, Prop. 173.D) prohíben. El precio cambió de forma: ya no hay peso multiplicativo en $\gamma$ (es peso 1), hay (a) un **flujo aditivo de borde** a la altura del corte, $O(\log^2T)$ en alturas buenas, y (b) un integrando **con signo** (todavía no una norma).

**[COROLARIO 173.C.1] (RH como ecuación integral exacta).** RH $\iff$ para toda altura buena $T$:
$$\int_{1/2}^\infty\!\!\int_0^T\log|\zeta(\sigma+it)|\,dt\,d\sigma\;=\;-\frac\pi8\;+\;\frac12\int_{1/2}^\infty(\sigma-\tfrac12)^2\,\mathrm{Im}\,\frac{\zeta'}{\zeta}(\sigma+iT)\,d\sigma .$$
($\Rightarrow$ por 173.C con $I\equiv0$; $\Leftarrow$ porque $I(T)\ge0$ es no decreciente y 173.C la anula en todas las alturas.) La energía es el defecto de esta ecuación.

**Forma "campo de primos" [PUENTE].** Integrando por partes en $\sigma$ (los bordes se anulan como en (4)):
$$\frac1\pi\iint u\;=\;\frac1{2\pi}\iint_{\sigma>1/2,\,0<t<T}(\sigma-\tfrac12)\;\mathrm{Re}\Big(-\frac{\zeta'}{\zeta}(\sigma+it)\Big)\,d\sigma\,dt\;+\;\text{(borde en }\sigma=\tfrac12\text{)},$$
y $\mathrm{Re}(-\zeta'/\zeta)(\sigma+it)=\sum_n\Lambda(n)n^{-\sigma}\cos(t\log n)$ para $\sigma>1$: $I$ es el apareamiento del **campo de primos** con el brazo de palanca $(\sigma-\tfrac12)$ a través de la franja. En $\sigma>1$ la integral en $t$ es acotada ($\int_0^T\cos(t\log n)dt\ll1/\log n$): **toda la masa de $I$ vive en $\tfrac12<\sigma\le1$**, la zona donde la serie de Dirichlet no converge. El estatus de la serie en la franja es el mismo muro de siempre, ahora en coordenadas de Fase A; la divergencia logarítmica del borde ($\int(\sigma-\tfrac12)\,d\sigma/(2\sigma-1)^2$ al normalizar segundos momentos) reproduce una vez más la constante de la casa $T/\log T$. [GAP: convertir esta forma en identidad con la serie regularizada — no se hace aquí.]

### 6.3. Pertenencia y la obstrucción de auto-energía

**[DEFINICIÓN-NUEVA].** Sea $G(s,w)=\frac1{2\pi}\log\big|\frac{s-(1-\bar w)}{s-w}\big|$ la función de Green del semiplano $\Omega=\{\sigma>\tfrac12\}$, y
$$\tilde d(s)\;:=\;2\pi\sum_{\beta_\rho>1/2} G(s,\rho)\qquad(s\in\Omega)$$
el **potencial de los ceros off** (el polo $s=1$ ya no aparece: está sustraído por construcción; los ceros en línea están en $\partial\Omega$ y no contribuyen). $\tilde d\ge0$; $\tilde d\equiv0\iff$ RH; y $\tilde d=u_h-u-(\text{término explícito del polo})$ donde $u_h$ es la extensión armónica (Poisson) de $t\mapsto\log|\zeta(\tfrac12+it)|$ a $\Omega$ — es decir, $\tilde d$ mide el **defecto de armonicidad** de $\log|\zeta|$ a la derecha de la línea: una cantidad de regularidad pura.

**[PROP 173.E] (pertenencia dicotómica).**
$$\mathrm{RH}\iff\tilde d\in\mathcal D(\Omega):=\{\text{espacio de Dirichlet}\},\qquad\text{y}\qquad\|\nabla\tilde d\|_{L^2(\Omega)}^2\in\{0,\infty\}\ \text{siempre}.$$

*Prueba.* Si RH, $\tilde d\equiv0$. Si hay un cero off $\rho_0$ (con $b_0>0$), entonces cerca de $\rho_0$: $\tilde d(s)=-\log|s-\rho_0|+O(1)$ (los demás sumandos de la serie de Green son armónicos y acotados cerca de $\rho_0$: la serie converge localmente uniformemente fuera de los átomos porque $\sum G(s,\rho)\le C(s)\sum b_\rho/((\sigma_s-\dots)^2+(\gamma_s-\gamma_\rho)^2)$, sumable por $E(T)\ll T/\log T$ y $b<\tfrac12$). Luego $|\nabla\tilde d|\ge\frac{1}{|s-\rho_0|}-O(1)$ en un disco perforado, y $\int|\nabla\tilde d|^2\ge\int_0^{r_0}\frac{2\pi r\,dr}{r^2}(1-o(1))=\infty$. $\square$

**Lectura y obstrucción final de la Fase A.** 173.E es literalmente la forma "$I<\infty$ como pertenencia" pedida por el mandato — pero **degenerada**: la norma de Dirichlet no gradúa $I$, salta de $0$ a $\infty$ con el primer átomo. (Curioso eco de la dicotomía LP-112 $\Rightarrow I\in\{0,\infty\}$ del Doc 175: aquí la dicotomía es **incondicional** pero vive en la norma, no en $I$.) La razón por la que $I\ne\|F\|^2$ en esta clase queda identificada con precisión:

> **Obstrucción de atomicidad.** $I=\int_\Omega(\sigma-\tfrac12)^2\,d\mu^+$ es un momento **lineal** de la medida de ceros (Teorema 173.C); toda energía **cuadrática** natural de esa medida ($\|\nabla\tilde d\|^2=4\pi^2\sum_{\rho,\rho'}G(\rho,\rho')$) incluye las auto-energías $G(\rho,\rho)=\infty$ de las cargas puntuales. Lineal-en-medida vs. cuadrático-en-campo: ese es el defecto exacto que separa la representación lograda de la norma pedida.

**Programa de desingularización [PUENTE hacia Fase 54].** El suavizado natural de los átomos lo da el propio flujo DBN (escala $\sqrt t$): la energía renormalizada por átomo es $2\pi\log(2b_j/\varepsilon)+O(1)$ al suavizar a escala $\varepsilon$; con $\varepsilon\sim\sqrt t$ esto conecta la norma de Dirichlet regularizada con $\sum_j\log(b_j/\sqrt t)$ — primer candidato concreto a "norma que gradúa" compatible con la ley de balance $\dot I=-2\kappa-D$. No se desarrolla aquí; queda nombrado como el siguiente paso de Fase A.

---

## 7. de Branges / Hermite–Biehler: dónde vive $I$ y dónde no

Marco: $E(z):=\xi(\tfrac12-iz)$ es entera; sus ceros son $z=\pm\gamma_j+ib_j$ y $\pm\gamma_j-ib_j$ (en línea: $\pm\gamma_j$ reales). RH $\iff E$ tiene todos sus ceros reales (caso límite de la clase Hermite–Biehler; de Branges, *Hilbert Spaces of Entire Functions*, Prentice-Hall 1968; para el diccionario con $\zeta$: Lagarias, "Hilbert spaces of entire functions and Dirichlet L-functions", en *Frontiers in Number Theory, Physics, and Geometry I*, Springer 2006 — [GAP de literatura: detalles del diccionario citados de memoria; los cálculos de abajo son autónomos]).

**(a) El defecto HB natural es de PRIMER orden en $b$.** Los ceros ofensores (semiplano superior) son $\pm\gamma_j+ib_j$. La masa de Blaschke en el punto $z=i$ (que corresponde a $s=\tfrac32$), exacta por cuádruplo:
$$\mathfrak B\;:=\;-\log\Big|\prod_j\frac{(i-z_j)}{(i-\bar z_j)}\Big|\;=\;\sum_j\log\frac{\gamma_j^2+(1+b_j)^2}{\gamma_j^2+(1-b_j)^2}\;=\;\sum_j\frac{4b_j}{1+\gamma_j^2}\,\big(1+O(b_j^2)\big).$$
Primer orden en $b$, peso Poisson $1/(1+\gamma^2)$. La condición de Blaschke es la pertenencia natural de la teoría — y es **lineal en $b$**, no cuadrática.

**(b) $I$ NO es un defecto de Branges natural: el cálculo de la varianza de Cauchy.** La medida de fase de $E$ ve un cero en línea como $\delta_\gamma$ y un cuádruplo off como el par de densidades de Cauchy $\frac1\pi\frac{b}{(t\mp\gamma)^2+b^2}\,dt$. El segundo momento de Cauchy es **infinito**; truncado:
$$\int_{|t-\gamma|\le1}(t-\gamma)^2\,\frac{b/\pi}{(t-\gamma)^2+b^2}\,dt\;=\;\frac2\pi\,b\,\Big(1-b\arctan\frac1b\Big)\;=\;\frac{2b}\pi+O(b^2),$$
de nuevo **lineal** en $b$. La teoría HB/dB mide la borrosidad de fase en primer momento; $b^2$ no es su moneda. Veredicto honesto: de Branges es el hogar natural de $J:=\sum b_j$ (y de $\mathfrak B$), no de $I$.

**(c) Pero $J$ controla $I$ y $J$ ya tiene representación (es el $m=1$ de §6.2).** Como $b_j<\tfrac12$: $I(T)\le\tfrac12 J(T)$, y $J(T)=\frac1{2\pi}\int_0^T\log|\zeta(\tfrac12+it)|\,dt+O(\log T)$ (Littlewood). **Propuesta de pivote (se registra, no se ejecuta):** si la Fase A admite como objetivo intermedio la energía de primer orden $J$ — también equivalente a RH ($J=0\iff$RH) y cota superior de $2I$ — entonces el hogar de Branges/HB y la representación de Littlewood en la línea (una sola integral, no doble) están disponibles desde ya, con la masa de Blaschke $\mathfrak B$ como versión pesada exacta.

---

## 8. El entregable duro: balance final

**(i) Representación lograda.** [TEOREMA 173.C]: $I(T)$ = funcional aritmético-analítico explícito de $\log|\zeta|$ en la semibanda derecha, **peso 1 en $\gamma$**, incondicional, exacto. Lo que queda como residuo, declarado: (1) el corte $T$ con flujo de borde $O(\log^2T)$ en alturas buenas (local en la altura del corte, promediable); (2) la constante exacta $\tfrac18$ (el polo); (3) el integrando con signo: $I$ queda como **momento lineal de una medida positiva** ($I=\int(\sigma-\tfrac12)^2d\mu^+$), no aún como $\|F\|^2$.

**(ii) Teorema de obstrucción.** [TEOREMA 173.A] (+ [LEMA 173.B], [PROP 173.D]): toda representación autocontenida de la clase holomorfa $X$ (la de la fórmula explícita) tiene peso $w=-2\varphi_r''$ soldado a la sombra; si $w\ge0$ entonces $\int w<\infty$ y $\int t\,w\,dt=2|\varphi_r(0)|$ — peso necesariamente decayente (integrable), con ley cuantitativa de coste sombra-altura. La razón estructural del techo 172.9 reaparece sin ventanas: **holomorfía de la sonda + paridad del cuádruplo**. La clase cuadrática $X_2$ hereda la obstrucción y su término autónomo es $\sum b^4$, no $\sum b^2$.

**(iii) La frontera exacta entre (i) y (ii).** El par de operaciones que separa el éxito del muro: *tomar parte real* ($\log|\zeta|$) y *seleccionar medio cuádruplo* ($\sigma>\tfrac12$) — ambas no holomorfas. El precio de cruzar: el peso multiplicativo desaparece y reaparece como flujo aditivo de borde + signo del integrando. La obstrucción residual hacia $I=\|F\|^2$ es la **auto-energía atómica** ([PROP 173.E]): $I$ es lineal en la medida de ceros; las normas son cuadráticas en el campo y divergen en los átomos.

**Próximos pasos nombrados (Fase A, continuación).**
1. **Desingularización DBN de 173.E:** energía de Dirichlet de $\tilde d$ suavizada a escala $\sqrt t$ del flujo; calcular su renormalización ($\sum\log(b_j/\sqrt t)$-tipo) y confrontarla con $\dot I=-2\kappa-D$.
2. **Promediado del flujo de borde de 173.C en $T$** (Cesàro en el corte) para bajar $O(\log^2T)\to O(\log T)$ y aislar la parte media aritmética del flujo.
3. **El pivote $J=\sum b_j$** (§7c): decidir si la Fase A acepta la energía de primer orden como objetivo intermedio; si sí, el paquete Littlewood + Blaschke ($\mathfrak B$) está listo.
4. **Regularizar la forma "campo de primos"** (§6.2): dar sentido sumable a $\iint(\sigma-\tfrac12)\sum\Lambda(n)n^{-\sigma}\cos(t\log n)$ en $\tfrac12<\sigma\le1$ (Abel/Cesàro en $n$) y medir qué parte del flujo absorbe.

---

## Referencias

- J. Hadamard, *Étude sur les propriétés des fonctions entières et en particulier d'une fonction considérée par Riemann*, J. Math. Pures Appl. (1893). [Producto de Hadamard de $\xi$.]
- H. Davenport, *Multiplicative Number Theory*, 3.ª ed., GTM 74, Springer. Caps. 12 (sumas $\sum1/\rho$, constantes), 15–16 (fracciones parciales de $\zeta'/\zeta$, cotas en franjas).
- H. Cramér, "Studien über die Nullstellen der Riemannschen Zetafunktion", *Math. Z.* 4 (1919), 104–130.
- J. E. Littlewood, "On the zeros of the Riemann zeta-function", *Proc. Cambridge Philos. Soc.* 22 (1924), 295–318. [Lema de Littlewood.]
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2.ª ed. (Heath-Brown), Oxford. §9.9 (lema de Littlewood), cap. 9 (densidades).
- A. Selberg, "Contributions to the theory of the Riemann zeta-function", *Arch. Math. Naturvid.* 48 (1946). [Origen del certificado $E(T)\ll T/\log T$.]
- X.-J. Li, "The positivity of a sequence of numbers and the Riemann hypothesis", *J. Number Theory* 65 (1997), 325–333.
- E. Bombieri, J. C. Lagarias, "Complements to Li's criterion for the Riemann hypothesis", *J. Number Theory* 77 (1999), 274–287.
- L. de Branges, *Hilbert Spaces of Entire Functions*, Prentice-Hall, 1968.
- J. C. Lagarias, "Hilbert spaces of entire functions and Dirichlet L-functions", en *Frontiers in Number Theory, Physics, and Geometry I*, Springer, 2006. [GAP de literatura: usado solo como contexto.]
- D. V. Widder, *The Laplace Transform*, Princeton, 1941. Cap. VIII (inversión/unicidad de la transformada de Stieltjes).
- A. Voros, "Sharpenings of Li's criterion for the Riemann hypothesis", *Math. Phys. Anal. Geom.* (c. 2004). [GAP de literatura: referencia exacta no verificada; no se usa en ninguna prueba.]

**Documentos internos:** Doc 152 (espectro de impureza $S_T(\tau)$), Doc 170 (coordenadas), Doc 172 (techo $T/\log T$, Teorema 172.9), Doc 175 (dicotomía LP-112), Fase 54 (ley de balance $\dot I=-2\kappa-D$).
