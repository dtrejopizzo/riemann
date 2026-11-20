# Anexo 211 — Kernel Gram por traslación, modelo hiperbólico y auditoría

Lectura completa, línea por línea, de tres archivos de `../phase-211-sign-sandbox/`:

- `POWER_GRAM_SLICES_OBSTRUCTION.md` (citado «GS», 2921 líneas);
- `POWER_HYPERBOLIC_MODEL_GRAM.md` (citado «HY», 966 líneas);
- `POWER_GRAM_SLICES_AUDIT.md` (citado «AU», 16 líneas).

Notación auxiliar de `POWER_CONE_001.md` y `POWER_BRIDGE_002.md` (citados CONE001, BRIDGE002). Los
números «l.» son líneas del archivo leído. Las etiquetas se copian tal como constan. El problema se
trata sólo como el signo de la forma explícita a_T sobre el subespacio primitivo (objetivo
λ_A(T) ≥ 0 para todo T); las equivalencias que aparecen son reducciones exactas internas entre
formulaciones de ese mismo signo.

---

## 0. Diccionario de objetos (fórmulas definitorias, una vez)

**Densidad theta.** h(x)=π e^{5x/2}(2π e^{2x}−3) exp(−π e^{2x}); Φ_n(t)=n^{−1/2}h(t+log n);
Φ=Σ_{n≥1}Φ_n (par, positiva, holomorfa en |Im t|<π/4; supercolas). Equivalente modal:
Φ((log(kt))/2+iy)=Σ_n n^{−1/2}h_{kn²}(t) con h_λ(t)=π(λt)^{5/4}(2π a_y λt−3)e^{5iy/2}e^{−π a_y λ t},
a_y=e^{2iy}. Forma radial: Φ(z)=w^{5/4}[wθ''(w)+(3/2)θ'(w)], w=e^{2z}. Cola: Φ(t)~2π²e^{9t/2}exp(−πe^{2t}) (HY l.120).

**Transformadas.** Z(u)=∫_R e^{ut}φ(t)dt; M=Z'/Z; K_M(u,v)=[M(u)+M(v)]/(u+v) (kernel de potencias;
CONE001 §1: Q_Φ=W sobre exponenciales). G(u,v)=1/(u+v) (Gram de Cauchy, GS §8.11).

**Kernel temporal A (GS (A), l.26).** A(t,s)=∫_0^∞ (t+s+2r)φ(t+r)φ(s+r)dr. Con τ=(t+s)/2, δ=(t−s)/2,
P_δ(σ)=φ(σ+δ)φ(σ−δ): A=∫_{|τ|}^∞ 2σP_δ(σ)dσ>0. Identidad (LT): (u+v)∫∫e^{ut+vs}A=Z'(u)Z(v)+Z(u)Z'(v),
de donde K_M(u,v)=∫∫e^{ut+vs}A/[Z(u)Z(v)].

**Capas (SLICE, l.123).** A=∫_0^∞ S_v dv, S_v(t,s)=φ(√(τ²+v)+δ)φ(√(τ²+v)−δ).
Normalizadas B_v=S_v/(φ(t)φ(s)); ∂_vB_v|_0=−K_f, K_f(t,s)=(f(t)+f(s))/(t+s), f=V'.

**Potencial.** V=−log φ (o −log Φ); p=V'=−Φ'/Φ; G(u)=V(√u) (GS §9, §12); a(u)=2G'(u)=p(r)/r, u=r²;
q=1/a. Momentos H=∫_0^∞ rΦ², J=∫r(Φ')², K=∫r(Φ'')² (GS §12; esta H no es la del modelo hiperbólico).

**Modelos de referencia (GS §4.3).** G0(t,s)=(t+s)/(e^{2t}+e^{2s}); H0(t,s)=sech²(t−s)−1/(t+s)²;
H(t,s)=∂_t∂_s log A.

**Escalas enteras complejas (GS §16–17).** z_k=(log k)/2+iy, ε=cos 2y, σ=sin 2y,
A_y(k,l)=A(z_k, z̄_l)=∫_1^∞ w_kl(t)Φ_k(t)conj(Φ_l(t))dt, w_kl=[log t+(log k+log l)/2]/(2t).
ρ(k,l)=gcd(a,b)/√(ab) si k=da², l=db² (d libre de cuadrados), 0 si no.
H(u)=|h_u(1)|²=π²u^{5/2}|2πa_yu−3|²e^{−2πεu}; I_λ=λ^{−1/2}∫_λ^∞H(u)/(2u)du;
J_λ=λ^{−1/2}∫_λ^∞log(u/λ)H(u)/(2u)du.
**R_res,y** = contribución de TODOS los pares modales con kn²=lm² (integral completo t≥1, ambos
términos del polinomio modal). **Off_y = A_y − R_res,y** (pares kn²≠lm²).
Por grupo libre de cuadrados d, coeficientes c_a (k=da²): f_q=Σ_{a|q}√a c_a, g_q=Σ_{a|q}√a log a c_a,
I_q=I_{dq²}, J_q=J_{dq²}, D_q=J_q+[log d+log q]I_q−Σ_{m≥2}Λ(m)I_{qm}.
E_y[c]=Σ_d √d Σ_q I_{dq²}|f_{d,q}|² (energía divisorial).

**Grafo térmico (GS §18).** P_κ(t)=κ^{5/4}Σ_n n²e^{−πκn²t}; Θ_κ(t)=Φ(½log(κt)); p=P_1;
T=πt^{5/4}(−2tD−3); Lg P(t)=∫_0^∞[e^{−πr}P(t)−P(t+r)]dr/r; (CF)(t)=Σ_{m≥2}Λ(m)m^{−1/2}F(m²t);
F(P)=TP, G(P)=½T Lg P−C TP; F(P_κ)=Θ_κ, G(P_κ)=½log κ Θ_κ (GRAPH).
Σc_i c̄_jA(x_i,x_j)=∫_1^∞[log t|F|²+2Re(G F̄)]dt/(2t) (A-GRAPH). Normas ‖P‖_{a,2}=max_{j≤2}sup e^{at}|P^{(j)}|,
H_γ=L²([1,∞),e^{γt}dt/t). B=Lg−2Σ_{m≥2}Λ(m)m²D_{m²} (Bp=0). T^{−1}F(t)=(1/2π)t^{−3/2}∫_t^∞u^{−3/4}F(u)du.

**Forma completa Q y Q_B (GS §19.1).** Q(P)=∫_1^∞[log t|TP|²+Re(TBP·conj(TP))]dt/(2t)=Q_log(P)+Q_B(P).
Momentos Tate ⇔ P(1)=0 y ∫_1^∞P=0 (GS §18.9).

**Core térmico E_j (GS §19.8).** w(t)=(t−1)p(t); q_j polinomios ortogonales mónicos de w (q_0=1);
E_j=p(t)(t−1)q_j(t), j≥1; Γ_ij=Q(E_i,E_j). E_1=p(t)(t−1)(t−a), a=1+(2/π)S_4/S_2, S_j=Σn^{−j}e^{−πn²}.

**Referencia de primer modo (GS §19.11).** p_0=e^{−πt}; Q_0(R)=∫[log t|T(p_0R)|²+Re(T Lg(p_0R)conj(T(p_0R)))]dt/(2t).

**Adjunto causal (GS §19.12).** k(h)=2cosh(h/2)−e^{−h/2}/(1−e^{−2h})−Σ_{n≥2}Λ(n)n^{−1/2}δ_{log n}(h);
g(r)=−∫_0^∞k(r+s)Φ(s)ds; V(f)=∫_0^∞Φ(r)g(r)|f(e^{2r})|²dr.

**Modelo hiperbólico (HY).** φ_a(t)=exp(−a cosh 2t), Z_a, M_a=Z_a'/Z_a;
y_x(r)=∫_0^∞exp(−a e^r cosh v)cosh(√x v)dv, Z_a(u)=y_{u²/4}(0), y_x''=[a²e^{2r}+x]y_x;
**H=−D_r²+a²e^{2r}** en la semirrecta, Dirichlet en 0; Green G_x(r,s)=y_x(r)y_x(s)∫_0^{min(r,s)}y_x^{−2};
REP: M_a(u)/u=½Tr(H+u²/4)^{−1}. Robin: φ_{a,β}=[β+a cosh 2t]e^{−a cosh 2t}, borde f'(0)=βf(0).
Prefactor: Y_ν(b)=∫_0^∞e^{−b cosh v}q(v)cosh(νv)dv, b=ae^r; q_θ(v)=Φ(v/2)e^{2π cosh v} (Y_{u/2}(2π)=Z(u)).

**Realización theta (HY §12.6).** ℋ=L²((0,∞),sech(πω/2)dω)⊕R³; λ_j=j+¼ (j=0,1,2);
Q(v)=(cos(ωv),cosh λ_0v,cosh λ_1v,cosh λ_2v); F(t)=sech t+Σcosh λ_jt;
C=mult. por −ω² (continuo), λ_j² (masas); D=mult. por d(ω)=1+ω coth(πω/2)+(15/2)cosh(πω/2)/cosh(2πω)
y masas (−29/4,−23/4,−9/4); B Q(v)=sinh v Q'(v)+cosh v DQ(v) en S=span{Q(v)}; h=(k/ρ,2d_{λ_j}) con
⟨Q(v),h⟩=q_θ(v); Y_rr=(b²+ν²)Y+2DY_r+(−C+2bB̄)Y, ⟨Y_ν(2π),h⟩=Z(2ν).

---

## 1. Entradas de `POWER_GRAM_SLICES_OBSTRUCTION.md` (GS), en orden

**GS l.1–5 — Título, Estado, auditoría adicional.** Estado: «PROVED como identidad y obstrucción de
una clase de certificados». No decide el signo de A completo ni de W. La auditoría adicional (l.5)
corrige el alcance: los descartes de cola valen para Φ_M con todo M≥1 y para Q_M sólo con M grande.

**GS §1 (l.7) Consulta y objeto que cambia.** Objetivo: un único kernel de dos variables cuya
representación positiva pagaría todos los tamaños. No reclama novedad del marco Gram/Pólya.
**l.15 Antecedente público.** Un borrador externo ya contiene el mismo kernel normalizado
(j=A/Z0²) y su respuesta logarítmica M; deja abierta la positividad de la forma. Consecuencia: **no
atribuir novedad a A ni al puente LT**. Reutilizable: sí, como cita de alcance.

**GS §2 (l.17) Kernel exacto y transformada.** Objeto: A, DOM 0<A≤[C²/(2N)]e^{−N(t²+s²)} si
φ≤Ce^{−Nt²}; (∂_t+∂_s)A=−(t+s)φ(t)φ(s); (LT). Resultado: identidades PROVED. Si A fuese PSD, K_M
sería PSD en todos los bloques («suficiencia precisa, NO una prueba de PSD de A real»). Reutilizable: sí.

**GS §2.1 (l.65) Recíproca bajo DOM.** PROVED. A PSD en R ⇔ K_M PSD en todos los bloques finitos de
nodos en cualquier intervalo abierto I⊂(0,∞). No vale a tamaño fijo ni para escaleras discretas. Para
el modelo hiperbólico da PSD de su A. Reutilizable: sí (reducción exacta).

**GS §2.2 (l.80) Para Φ real, positividad temporal local implica global.** PROVED. A es holomorfo en
|Im t|,|Im s|<π/4; PSD (todos los tamaños) en un intervalo abierto se propaga por jets/Taylor a toda R.
No da factorización ni signo. Reutilizable: sí (principio de continuación, usado en §§4.3, 8, 8.11, 19.10).

**GS §2.3 (l.100) Restricción de la factorización Hankel traslacional.** PROVED como restricción
(antecedente clásico citado). No existe A(t,s)=∫_0^∞⟨h(t+r),h(s+r)⟩dr en t,s>0: forzaría
(t+s)φ(t)φ(s) PSD, cuyo determinante 2×2 es −(t−s)²φ(t)²φ(s)²<0. No excluye PSD de A, Grams generales,
otras coordenadas ni sumas de dos productos Hankel. Reutilizable: sólo como descarte.

**GS §3 (l.119) Capas y certificado suficiente.** Objeto: SLICE. PROVED: si S_v PSD para todo v≥0,
A es PSD. Define la «clase de certificados por capas positivas». Reutilizable: como criterio suficiente.

**GS §4 (l.131) Modelo integrable.** φ=exp(−at⁴−bt²): S_v=φ(t)φ(s)e^{−2av²−2bv−4av(t²+s²)}e^{4avts};
todas las capas PSD y A PSD. No se extrapola a theta. Reutilizable: modelo positivo.

**GS §4.1 (l.144) Logaritmo condicionalmente positivo.** PROVED para el modelo, no para Φ. CPD de
log A (sumas c con Σc=0) es suficiente para A PSD; falla para el modelo cuártico b=0 (κ_5(V)<0,
coeficiente [t⁵s⁵]log A<0, seis nodos jh). Diagnósticos reales: NUMÉRICO, no certificado (autovalores
positivos en {0,¼,½,1,2}; [t⁵s⁵]log A≈+1.904 para Φ). Identidad: ∂_t∂_s log A=Cov_μ(p(t+r),p(s+r))−
Cov_μ(1/q,·)−(E_μ[1/q])², no Gram. Decisión: condición real OPEN.
- **l.184 Cúspides diagonales complejas (PROVED).** F²H(z,z̄)=4D+L²+2xbL−Fb, D proyección compleja;
  positivo eventualmente en la cúspide alternante x=0 (L≥cε^{−4}, F≤Cε^{−5}) y en la par x=h=log2/2
  (m(f)≥1/9375 para f=(1+2iu)^{−5/2}). Sólo estos dos tests; CPD y signo OPEN.
- **l.227 Límite de la proyección conjunta (PROVED).** No existe c>0 independiente de η con R≥cB
  (residual de proyección contra borde) en pares z0, z0+iτ. Además S=A^{⊙2}⊙H PSD no implica H PSD.
  Falsificador: evaluación en el primer vector coordenado.
- **l.235 Promedio horizontal (PROVED).** ε^{9/2}B_y→c_*=315(log2)²/(512√2), A(iy,−iy)≥cε^{−9/2};
  cruces n≠m acotados por integración por partes sin desechar casi resonancias; una cúspide aislada
  aporta O(√ε) relativo. Sólo B_y, no A completo (lo completa §16).

**GS §4.2 (l.285) A no es log-supermodular.** PROVED. H(t,s)=−1/(t+s)²+O_K(e^{−2t})<0 para t grande:
A no es TP2 en la semirrecta. Falsificador: menores rectangulares. NO descarta Gram firmado, PSD de H,
CPD ni PSD de A.

**GS §4.3 (l.331) El modelo de cola no es referencia PSD.** PROVED. G0 y H0 no son PSD en ningún
intervalo abierto de (0,∞) (G0(t,t)<0 para t<0 tras continuación; H0(¼,¼)=−3). A=[Φ(t)Φ(s)/2π]G0(1+O(e^{−2L})),
H=H0+O(e^{−2L}) en colas. Sándwich (1−ε)H0≤H≤(1+ε)H0 imposible. No excluye otras referencias positivas
ni compensación firmada exacta.

**GS §5 (l.363) Condición infinitesimal y fallo real.** PROVED. Capas PSD ⇒ K_f CND (JET); con nodos
(α,β,R), c=(1,−1−ε,ε), ε=−B/Q_bR, la forma vale Q_ab+B²/(−Q_bR)~(β−α)²f(R)/R³>0 si f(R)/R³→∞.
Φ real: f(R)=2πe^{2R}+O(1). Falsificador: capa S_v finita no PSD en tres nodos positivos (d_i=c_i/Φ(t_i)).

**GS §6 (l.423) Alcance.** Sólo se refutan las capas; no A, ni K_M, ni W. No excluye cancelación entre
capas, reordenamiento firmado ni otro Gram. A(t,t)=∫_t^∞2uφ²; A(t,−t)=∫_0^∞2rφ(r+t)φ(r−t)dr.

**GS §7 (l.440) Hipótesis genéricas y operaciones positivas.** PROVED. (i) V=g(t²) convexa (074) da A
no PSD. (ii) Mezclas positivas de gaussianas: uM'>M, menor u,u+h negativo. (iii) Convolución preserva K
(M=M1+M2), pero Φ no es convolución/mezcla positiva con factor exp(−at⁴−bt²). (iv) Integración por partes
con B(t,s)=(t+s)/(f(t)+f(s)) tiene corrección de diagonal negativa. (v) Un operador positivo Bop con
Bop(−Φ')=tΦ no controla la forma en la semirrecta. PSD real OPEN.

**GS §7.1 (l.455) Convolución gaussiana: recíproca.** PROVED. Lema rango uno: si K(u,R)→0, K(R,R)→0,
entonces K+b PSD ⇔ K PSD. Para Φ, M(u)/u→0; K_σ=K+σ² (M_σ=M+σ²u). Firmar UNA densidad suavizada
G_σ∗Φ cerraría el signo; suavizar no puede convertir indefinido en PSD. Obligación OPEN.

**GS §8 (l.485) Ningún modo theta individual da Gram local.** PROVED. A_n(t,t)→(2H/n)(m−log n)<0,
m<½log(5/(4π)); por §2.2 A_n no es PSD en ningún intervalo. No refuta A: faltan cruces n≠m.

**GS §8.1 (l.528) Prefijo theta completo Φ_M.** PROVED (M grande): ∫tΦ_M²~−H M log M; diagonal límite
negativa. **l.572 Fortalecimiento: todo M≥1** vía Z_{Φ_M}(u)=(u−½)H_M(u): test ZZ'/u<0.

**GS §8.2 (l.591) Cola continua Q_M=Φ_M+πM³e^{5t/2}e^{−πM²e^{2t}}.** PROVED: Q_M→Φ en L²((1+|t|)dt),
pero ∫tQ_M²=−[‖h‖²/(4M)]log M+O(·)<0: no PSD (M grande).

**GS §8.3 (l.636) Simetrizar S_M=[Q_M(t)+Q_M(−t)]/2.** PROVED todo M≥1: colas −D_Me^{−5|t|/2},
Z_M→−∞ en 5/2, punto con Z>0, Z'<0.
- **l.677 Alcance común: reparar sólo la izquierda.** Si ψ=f en [R,∞), A_ψ=A_f en t,s≥R; el menor
  negativo persiste. No excluye correcciones de la cola derecha.
- **l.680 Cortes suaves w_n≥0, Σw_n n²<∞.** PROVED: Z=(u−½)H_w, no PSD. No cubre w_n=1.

**GS §8.4 (l.693) Momento exponencial cancelado.** PROVED. Lema: si Z(c)=0 para algún c>0 (CANCEL),
A_φ no es PSD (y no PSD en ningún intervalo si holomorfo). Se aplica a φ_P=(D²−¼)[e^{t/2}P(q)]/4,
q=e^{−πe^{2t}} (∫e^{t/2}φ_P=0), y a los cortes P_J del producto de Jacobi. No pasa al producto infinito
(Z_Φ(½)>0).

**GS §8.5 (l.743) Simetrizar cortes de Jacobi.** PROVED J≥1: cola D_Je^{−β|t|}, β=2J+½; ε²det→−1/(16β²)<0.

**GS §8.6 (l.773) Pesos n^{−δ}.** PROVED δ≠0 real: Z_δ Z_δ'/u<0; ∫e^{t/2}|φ_δ−Φ|≥¼. δ=0 fuera.

**GS §8.7 (l.815) Perturbaciones positivas pares analíticas.** PROVED: ∀ε, ψ>0 par holomorfa con
sup|ψ/Φ−1|<ε, ψ/Φ→1, A_ψ no PSD en ningún intervalo. Construcción ψ=Φ(1−g_σ), g_σ=h_M∗γ_σ.

**GS §8.8 (l.862) Conservar momentos finitos.** PROVED: además ∫w_iψ=∫w_iΦ exactamente (familia finita
fijada antes); en particular igualdad de K(u_i,u_j) en bloques finitos preelegidos. Falsificador:
la misma ψ.

**GS §8.9 (l.901) Estabilidad de bloques de orden ≤4.** PROVED: ∃δ_*: ‖h‖_20<δ_* ⇒ K_ψ PD en todos
los bloques de ≤4 nodos u_i>½ (usa certificados 084/085: N_R>¼, N_S>19/4). Existe ψ así con A_ψ no PSD:
el bloque negativo tiene >4 nodos.

**GS §8.10 (l.967) Control relativo uniforme y trece polos.** PROVED. Lema de interpolación
contractiva: |Σc_ic̄_j[μ(u_i)+μ(u_j)]/(u_i+u_j)|≤2B_nΣc_ic̄_j/(u_i+u_j), B_n=Σ_{j<n}(2^j/j!)‖F^{(j)}‖_∞,
F(z)=μ(a(1+z)/(1−z)). Con 053 (W>‖f‖²/4000 en trece polos ≥63/2): Q_ψ>‖f‖²/8000. Existe ψ con todo eso
y K no PSD (bloque con >13 nodos). Reutilizable: el lema, a dimensión fija.

**GS §8.11 (l.1038) Ningún margen de Cauchy uniforme.** PROVED: M real analítica, M=O(u) en 0, c>0:
K_M−cG no es PSD en ningún intervalo I⊂(0,∞). Vale para K_Φ y el modelo hiperbólico. Si K_Φ fuese PSD,
ínf Q_Φ[f]/‖f‖²=0. A−a no es acretivo (traslación del semiplano no gratuita). Reutilizable: restricción.

**GS §9 (l.1064) Pares temporales.** PROVED: V'''>0 (073) ⇒ G(u)=V(√u) estrictamente convexa ⇒
S_v(t,s)²<S_v(t,t)S_v(s,s) (PAIR-SLICE) ⇒ [A(t_i,t_j)]_{2×2} PD para t_1≠t_2. Tamaño mínimo de
falsificador de capas: 3. Todos los órdenes OPEN.

**GS §10 (l.1106) Triples simétricos (−R,0,R).** PROVED: SPD para todo R≥8 (2c²<d_0 d; d−b>0); capas
inicialmente negativas en los mismos nodos (Q_R=2p'(R)−6p(R)/R+4p'(0)>0, w_R=(1/P,−2/Φ(0),1/P));
∫w_R^TS_vw_R dv>0: compensación probada para esa familia. No uniforme.

**GS §11 (l.1194) Andréief.** PROVED: det[A_ij]=(1/6)∫S; S(r,r,r+h)=−4det[g,f,f_h]det[g,f,g_h]<0 en un
abierto. Sólo refuta positividad puntual del integrando; no det A<0.

**GS §12 (l.1227) Recíproco del potencial.** PROVED (identidad, suficiencia, cota exterior).
(HK−J²)/H²=Var(a+ua')+E[u²(2a'²−aa'')]; si a>0 y (1/a)''≥0 entonces HK≥J². Cola: N=2r²p'²−r²pp''−rpp'−p²>2r²Y²
para r≥1, q''(u)>0 en u≥1.

**GS §12.1 (l.1265) Cierre compacto.** PROVED por certificado de bolas Arb (script y SHA256 en l.1267):
a(u)>0 y q''(u)>0 para todo u≥0; HK>J².

**GS §12.2 (l.1310) Triples pequeños.** PROVED: D(R)=d_0(d+b)−2c²=2(HK−J²)R⁴+O(R⁶)>0: SPD para 0<R<R0
(R0 no cuantificado). R intermedios OPEN.

**GS §12.3 (l.1324) Alcance frente a 074 y capas.** Consecuencias: el falsificador 074 viola q''>0;
V=r²/2+r⁴/4+εr⁶/6 cumple q''>0 pero sus capas fallan (§5). R intermedios y todos los órdenes OPEN.

**GS §13 (l.1340) Convexidad recíproca no basta.** PROVED (clase genérica): ψ positivas pares, cercanas a
Φ en C6 relativo, con V'''>0, a>0, (1/a)''>0, HK>J², y A_ψ no PSD.

**GS §14 (l.1390) Sin representación Laplace positiva de q.** PROVED: q no tiene extensión holomorfa a
Re u>0 (cúspides τ_m=16+2/m, sumas de Gauss |G_m|²=m, Q(z_m²)=0 acumulándose). Coeficientes 0–39
alternantes positivos: test no usado.

**GS §15 (l.1436) G convexa no basta para triples.** PROVED: φ=exp(−r²/2−εr⁶/6), ε=1/1000:
HK−J²<0 ⇒ triple (−R,0,R) indefinido para R pequeño.

**GS §16 (l.1467), §16.1 (l.1471) Equivalente en escalas enteras.** PROVED:
A(z_k,z̄_l)=[105/(512√2)]ρ(k,l)ε^{−9/2}L²+O_{k,l}(ε^{−9/2}L), L=log(1/ε); representación exacta (MAIN).
**§16.2 (l.1503)** NEAR: Σ'n⁴m⁴e^{−δ(kn²+lm²)}/|kn²−lm²|≤C_{k,l}δ^{−4}log(2+1/δ); (OFF) ≤Cε^{−4}log(2+1/ε),
casi resonancias conservadas. **§16.3 (l.1529)** resonancias n=(b/g)j, m=(a/g)j; constante 4π⁴F0=105/(128√2).
**§16.4 (l.1555)** corolario: [ρ(k_i,k_j)] PD (gcd=Σφ(q)); bloque complejo [A(z_{k_i},z̄_{k_j})] PD para
ε pequeño dependiente de la lista. No A PSD real.
**§16.5 (l.1570)** PROVED: con y fijo, |C_y(k,k+1)|→1 mientras ρ(k,k+1)=0: no existe c_y>0 con C_y≥c_yρ;
sup|C_y−ρ|≥1. Falsificador: pares consecutivos.

**GS §17 (l.1605) SOS exacta de la parte resonante.** PROVED. Objetos: R_res, I_λ, J_λ, H(u). Antecedentes
bibliográficos (cadenas de von Mangoldt, criticalidad en grafos) citados sin nombres aquí; no añaden signo.
**§17.1 (l.1624)** una frecuencia (k=1,4, λ=4): det=−2(log2)²I_4²<0 (sólo por frecuencia).
**§17.2 (l.1634)** g_q=log q f_q−Σ_{m|q,m≥2}Λ(m)f_{q/m};
(RES-SOS) R_res[c]/√d=Σ_qD_q|f_q|²+Σ_qΣ_{m|q,m≥2}Λ(m)I_q|f_q−f_{q/m}|².
**§17.3 (l.1662)** D_q>0 ∀d,q (log(N!)≥(X/2)Σ_{m≤X}Λ(m)/m).
**§17.4 (l.1683)** R_res definido positivo sobre cualquier conjunto finito de enteros distintos, todo
|y|<π/4 incl. 0. Falta control conjunto de la contribución no resonante.
**§17.5 (l.1693)** (UNIF-D) D_q≥c_*I_q, c_*=(log2/3)(4π−3)²e^{−6π}/[(4π+3)²+(4π−3)²e^{−6π}];
(DIV-LOWER) R_res[c]≥c_*E_y[c].
**§17.6 (l.1731)** PROVED: falsificador c^{(k)} en (k,k+1): E_y=1, Off_y=−log k+o(1), R_res=log k+o(1),
A_y=o(1). Excluye Off_y≥−C_yE_y y A_y≥δ_yR_res,y. No decide Off_y≥−R_res,y.
**§17.7 (l.1776)** PROVED: no existe M con |Q_C(F)|≤M W(F), W=∫(1+log t)|F|²dt/(2t), en el span finito de
Θ_k (y=0); span denso en H_γ (0<γ<2π); mesetas F_R=1_[1,R].
**§17.8 (l.1829)** PROVED: R̃_s=TR_sT^{−1} no todos acretivos en el producto físico dt/(2t)
(q=(π²/2)[7∫|u'|²−(9/16)∫|u|²]<0), transferido al span theta. No falsifica el logaritmo conjugado.

**GS §18 (l.1878) A entero ⇔ A real.** PROVED. **§18.1 (l.1889)** GRAPH, A-GRAPH. **§18.2 (l.1915)**
continuidad B_a²→H_γ×H_γ. **§18.3 (l.1933)** aproximación por escalas enteras, MOB-P
e^{−πkt}=k^{−5/4}Σμ(n)n^{−1/2}P_{kn²}. **§18.4 (l.1953)** transferencia; el signo entero completo sigue OPEN.
**§18.5 (l.1960)** PROVED: K(t,v)=t^{−1/4}v^{−3/4}−t^{5/4}v^{−5/4}/(v−t) (JUMP-K), positivo para 2<v/t<3;
TBT^{−1} no admite tasas positivas JF=∫[F(t)−F(v)]ν_t(dv)+VF.
**§18.6 (l.2010)** PROVED: (PDE-A); ΔA_ii(x,0)=4[I−Φ(x)²]>0: sin superarmonicidad.
**§18.7 (l.2037)** PROVED: cualquier cola k≥K basta; (TAIL-ZERO); (NO-FIN-MARGIN): no hay
A_0[c]≥δ|ℓ(c)|² con ℓ finitamente soportado; ni minorante Σw_k|c_k|² (w≥0 no todos nulos); ni SOS única
global con ℓ_α de soporte finito. No excluye observables globales continuos ni SOS no diagonales.
**§18.8 (l.2073)** PROVED: no hay A_0[c]≥δ|ℓ_σ(c)|², ℓ_σ momento exponencial real (A(−R,−R)/|ℓ_σ|²→0).
**§18.9 (l.2105)** PROVED como alcance: (1) λ_A(T)≥0 ∀T; (2) K_{M_Φ} PSD; (3) A PSD real; (4) A entero PSD
(o cualquier cola) — equivalentes. ℓ_σ(TP)=πP(1)+π(σ/2−¼)∫t^{σ/2+1/4}P. TAIL-ZERO vale primitivo.

**GS §19 (l.2151) Primer polinomio térmico.** **§19.1 (l.2157)** E_1, a=1+(2/π)S_4/S_2, P(1)=∫P=0.
**§19.2 (l.2188)** BP=Σe^{−πn²t}L_n(t), (POLY-QB). **§19.3 (l.2229)** Q_{B,11}(a_0)>1/1200.
**§19.4 (l.2261)** |δ|<1/40000. **§19.5 (l.2292)** |Q_{B,12}+Q_{B,21}|<1/4500.
**§19.6 (l.2351)** resto <1/30000. **§19.7 (l.2390)** PROVED: Q_B(E_1)>1/2000, Q(E_1)>1/2000.
**§19.8 (l.2406)** PROVED (densidad/alcance): span{E_j} es core; Γ_{1..N} PSD ∀N ⇔ λ_A(T)≥0 ∀T.
**§19.9 (l.2462)** PROVED por certificado racional/Arb (SHA256 l.2468): Q_11>179/100000, Q_22>17/10000,
|Q_12|<79/50000, det>2733/5·10⁹: bloque 2×2 PD; Q_B(E_1+E_2)<−1/20000 (falsificador del signo separado de Q_B).
**§19.10 (l.2653)** PROVED alcance: Γ_{J..N} PSD ∀N≥J ⇔ objetivo; (TAIL-MOM), (TAIL-SIGMA), lema CPD-m.
**§19.11 (l.2725)** PROVED: ∃R, R(1)=0, ∫pR=0, Q_0(R)<0 (déficit arquimediano 008: Arch≤−4‖f‖²+17‖f'‖²).
**§19.12 (l.2785)** PROVED: Q_phys(Θf)=−½∫ΘΘ|f(v)−f(t)|²dν+V(f) (POT-V); g(log2+)<−19/300;
V(f)<0 para bumps (también primitivos exactos). No Q negativo; término de diferencias de signo mixto.

## 2. Entradas de `POWER_HYPERBOLIC_MODEL_GRAM.md` (HY), en orden

**HY l.1–3 Título y Estado.** PROVED para el modelo; OPEN toda transferencia a Φ.
**§1 (l.5)** objeto φ_a; afirma K_{M_a} PSD en todos los tamaños.
**§2 (l.17)** y_x, Z_a=y_{u²/4}(0), (ODE), (RATIO) y_x(r+h)/y_x(r)≤exp(−ae^rh).
**§3 (l.38)** z_x=∂_x log y_x; (LOG-DER) con bordes justificados.
**§4 (l.62)** H, Green G_x (Gram continuo), Tr R_x=∂_x log y_x(0)≤1/(2a); (REP).
**§5 (l.83)** PROVED: K_ij=½Tr(HR_iR_j)+(u_iu_j/8)Tr(R_iR_j); (GRAM) Σc_ic_jK_ij=½‖H^{1/2}A‖²_HS+⅛‖B‖²_HS≥0,
A=Σc_iR_i, B=Σc_iu_iR_i. Todos los tamaños. Reutilizable: mecanismo Green de escala.
**§6 (l.106)** OPEN: no hay ODE/Green con REP para Z real; mezclas no transfieren.
**§7 (l.114)** PROVED; THETA-TAIL. **§7.1 (l.124)** no existe μ≥0 con Φ=∫e^{−a cosh 2t}dμ(a).
**§7.2 (l.138)** no existe ν≥0 finita con Φ=φ_a∗ν. No excluye prefactores temporales, combinaciones
firmadas ni otros Green; «No se registra una prohibición general de transferencias».
**§8 (l.161)** PROVED: Robin φ_{a,β}, (ROBIN) R_{β,x}=R_x+k_x⊗k_x/(m_x+β); GRAM vale con término
(β/2)∫|F(0,s)|². Transferencia OPEN (prefactor e^{2t} vs e^{9t/2}).
**§9 (l.200)** PROVED: D_a=−a∂_aK_a no PSD (A_nA_{n+2}−A_{n+1}²<0). Flujo de escala sin orden matricial.
**§10 (l.249)** PROVED: prefactor fijo q, F_ν=E(b)Y_ν en dos escalas ⇒ q constante; q_θ excluido.
**§10.1 (l.282)** PROVED: con deriva A(b): sólo q=C o C cosh(v/2). **l.316 Ampliación:** peso w(b)ν² forzado
w=1; cambio de escala h'²=1: sin reparación.
**§11 (l.335), §11.1 (l.345), §11.2 (l.368), §11.3 (l.377)** PROVED: no existe Φ=Ce^{−a cosh 2t}Πcosh(α_jt)
(a=2π, Σα_j=9/2, c1=π−3/(2π)∈(2,3) no entero).
**§11.4 (l.389)** PROVED: ni aproximación localuniforme a escala fija 2π.
**§12 (l.427)** PROVED: vector finito de prefactores sin deriva: sinh v Q'=BQ ⇒ Q acotado.
**§12.1 (l.458)** PROVED: con deriva matricial: operador racional anularía g; imposible.
**§12.2 (l.508)** PROVED: dimensión infinita simétrica (INF-SYM) ⇒ ‖Q(v)‖²=A+c log cosh v.
**§12.3 (l.554)** PROVED: deriva escalar constante α: (DRIFT-K), (DRIFT-HOL); cúspide par excluye theta.
**§12.4 (l.605)** PROVED: deriva escalar dependiente de escala forzada constante (β=0).
**l.650 Control operatorial** ejemplo Q=(1,2cosh v), D,C,B 2×2: la reducción escalar no se extiende;
potencial no simétrico salvo r=0. **l.662 Métrica local para ese ejemplo**: M'=−DM−MD, [E+D²,M]=0
⇒ M0=0: imposible. **l.675 Actualización**: GLOBAL refuta K_Φ≥εK_{2π} ∀ε>0.
**§12.5 (l.678)** PROVED: L(v,z)=⟨DQ(v),Q(z)⟩=[G(v+z)+G(v−z)]/2, G(t)=−coth(t/2)F'(t); L_vv=L_zz.
**§12.6 (l.720)** PROVED como realización, no signo: ℋ, Q, C, D, B, h con ⟨Q(v),h⟩=q_θ(v); B simétrico
clausurable no declarado autoadjunto; H_θ=O_b(e^{−|Re t|/4}). **l.800 Realización integral**: ecuación fuerte
y ⟨Y_ν(2π),h⟩=Z(2ν). Falta métrica y Green positivo.
**§12.7 (l.823)** PROVED (clase declarada): no existe M(r) acotado autoadjunto estrictamente positivo, C²,
local en r, con M'=−DM−MD (débil) y E=−C+D²+2bB̄ simétrico en ⟨M·,·⟩; contradicción en el par e_2,e_1
(exponentes 25/2, 21/2, 11/2, 8).
**§13 (l.873)** PROVED: productos cosh desplazados Π(cosh(b z)−c)/(1−c), −1<c<1, escala fija 2π: límites
enteros; cúspide par impide q_θ.
**§13.1 (l.927)** PROVED: escala positiva variable a_n acotada por concavidad; misma exclusión.

## 3. Entradas de `POWER_GRAM_SLICES_AUDIT.md` (AU)

**AU l.1–11.** APROBADO: verifica paridad, DOM, LT sin factor 2, SLICE, cuártico, CND, ε=−B/Q_bR,
cola 105§4. «PSD del integral sigue OPEN».
**AU l.14 Addendum de operaciones.** APROBADO §7; no decide A real.

---

## A. Lista deduplicada «no relanzar» (con condición de reapertura del texto)

1. Certificado por capas S_v PSD (GS §§3,5). Reabrir: sólo con cancelación entre capas o Gram distinto (GS §6).
2. Factorización Hankel traslacional en variables originales (GS §2.3). Reabrir: otras coordenadas o transformación adicional.
3. Inferir CPD de log A de A y capas PSD (GS §4.1). Reabrir: estimación específica para theta.
4. TP2 / log-supermodularidad de A en la semirrecta (GS §4.2). No excluye Gram firmado.
5. G0/H0 como referencia PSD; sándwich (1±ε)H0 (GS §4.3). Reabrir: otra referencia positiva o compensación firmada exacta.
6. Mezclas positivas de gaussianas; Φ como convolución con factor exp(−at⁴−bt²); integración por partes hazard con B=(t+s)/(f+f) certificando dos términos PSD; operador positivo para tΦ (GS §7).
7. Suavizar para obtener PSD (GS §7.1). Reabrir: prueba independiente del signo de UNA densidad suavizada.
8. Grams modales separados; prefijos Φ_M (todo M); Q_M (M grande); S_M; reparaciones sólo izquierdas; cortes w_n con Σw_nn²<∞; cortes y simetrizaciones de Jacobi; pesos n^{−δ}, δ≠0 (GS §§8–8.6). Reabrir: correcciones de la cola derecha, regularizaciones que conserven la compensación completa (δ=0).
9. Cercanía relativa, momentos finitos, bloques ≤4 o 13 polos como garantía (GS §§8.7–8.10). Reabrir: uso de la estructura theta exacta o comparación firmada en norma de formas.
10. Margen de Cauchy uniforme K_M ≥ cG (GS §8.11).
11. Positividad puntual del integrando Andréief (GS §11).
12. Convexidad recíproca q''>0 (con V'''>0, C6) como suficiente (GS §13); G convexa para triples (GS §15); representación Laplace positiva de q (GS §14).
13. Comparador ρ con dominación uniforme (GS §16.5).
14. PSD por frecuencia resonante individual (GS §17.1).
15. Off_y ≥ −C_yE_y; A_y ≥ δ_yR_res,y (GS §17.6). Abierto: Off_y ≥ −R_res,y.
16. |Q_C| ≤ M W en el portador theta (GS §17.7).
17. Acretividad de todos los T R_s T^{−1} en métrica física (GS §17.8).
18. Tasas positivas después de T (GS §18.5); principio mínimo por superarmonicidad (GS §18.6).
19. Minorantes de soporte finito / SOS única con observables finitos, también primitivos (GS §§18.7, 18.9); minorante por un momento exponencial real (GS §18.8).
20. Signo separado de Q_B en la familia E_j (GS §19.9); referencia de primer modo Q_0 PSD (GS §19.11); V(f) ≥ 0 en bumps locales (GS §19.12).
21. Transferencia del modelo hiperbólico por mezcla/convolución positivas (HY §7); monotonía matricial del flujo de escala (HY §9).
22. Ecuaciones de escala con prefactor fijo: escalar (HY §10), con deriva (HY §10.1), peso ν² variable/cambio de escala (HY l.316), vector finito (HY §12), deriva matricial finita (HY §12.1), infinito simétrico sin deriva (HY §12.2), deriva escalar constante o dependiente de escala (HY §§12.3–12.4). Reabrir: prefactores dependientes de b, deriva verdaderamente operatorial, métricas variables, otras representaciones.
23. Métrica local para el ejemplo 2×2 (HY l.662) y métrica local acotada para la realización theta (HY §12.7). Reabrir: métricas no locales, no acotadas, conexiones nuevas, otras realizaciones.
24. Productos cosh: representación exacta (HY §11), aproximación a escala fija (HY §11.4), desplazados con escala fija o variable positiva (HY §§13–13.1). No decidido: si un factor cosh conserva PSD.

**Cotejo con RULES_AVOID.md §D.** Presentes: 15 (D9), 23 parcial (D15), 8 parcial (D16 «sumación por
partes discreta en theta») y 24 sólo como etiqueta en §C («cierres por productos cosh»). **Faltan en §D:**
1–7, 9–14, 16–22 y la parte de 23 sobre el ejemplo 2×2.

Inexactitudes:
- RULES_AVOID D9: «Comparaciones Off frente a E_y o A frente a una fracción fija de R_res como
  consecuencia del margen de la suma de cuadrados resonante». GS §17.6 no habla de una consecuencia
  del margen: da un falsificador explícito, «No existe C_y finito tal que Off_y>=-C_y E_y …
  Tampoco existe delta_y>0 con A_y>=delta_y R_res,y». Además D9 dice «Off ≥ −R_res sí sigue
  abierta, sin margen adicional», pero en y=0 esa desigualdad es literalmente A_0 ⪰ 0 sobre bloques
  enteros (A=R_res+Off). Por GS §§18, 18.9, eso equivale al objetivo completo. No es un residuo menor.
- RULES_AVOID D15: «Métrica local positiva acotada para la realización theta». HY §12.7 exige
  además que sea autoadjunta, C² y estrictamente positiva, con «coeficiente principal -I y sin añadir
  conexiones», y declara «No se excluyen métricas no locales, métricas no acotadas con otros dominios,
  conexiones nuevas ni otras realizaciones». D15 menciona sólo las no locales.
- RULES_AVOID D16 / memoria las reglas del proyecto: «Cambio (m,n) a (m+n,m−n) … POWER_GRAM_SLICES_OBSTRUCTION.md
  §§17.1–17.2». En GS §§17.1–17.2 no aparece ese cambio. Contienen el bloque de una frecuencia
  (det=−2(log2)²I_4²) y la reindexación divisorial RES-SOS. La cita no es literal.

## B. Resultados positivos PROVED (enunciado y alcance exacto)

1. GS §2: (LT) y K_M=∫∫e^{ut+vs}A/(Z(u)Z(v)); A>0 puntual; DOM. Alcance: φ par positiva, cota gaussiana.
2. GS §2.1: A PSD en R ⇔ K_M PSD en todos los bloques de cualquier intervalo abierto I⊂(0,∞) (todos los tamaños).
3. GS §2.2: para Φ real, A PSD en algún intervalo abierto ⇔ A PSD en R.
4. GS §3: S_v PSD ∀v ⇒ A PSD.
5. GS §4: φ=exp(−at⁴−bt²): todas las capas y A son PSD.
6. GS §4.1: F²H(z,z̄)>0 eventualmente (ε→0) en x=0 y x=log2/2; ε^{9/2}B_y→c_*.
7. GS §7: convolución preserva K. GS §7.1: K+b PSD ⇔ K PSD si K(u,R),K(R,R)→0; K_σ=K+σ² PSD ⇔ K PSD.
8. GS §8.9: ∃δ_*: ‖h‖_20<δ_* ⇒ K_ψ PD en bloques ≤4 nodos u>½. GS §8.10: lema de interpolación
   contractiva (dimensión n fija); Q_ψ>‖f‖²/8000 en trece polos ≥63/2 si ‖h‖_100 pequeño.
9. GS §9: [A(t_i,t_j)]_{2×2} PD para t_1≠t_2 reales; S_v PD en pares, v>0.
10. GS §10: A en (−R,0,R) SPD para todo R≥8; ∫w_R^TS_vw_R>0 con integrando negativo cerca de v=0.
11. GS §§12–12.1: a(u)>0, q''(u)>0 ∀u≥0 (Arb); HK>J². GS §12.2: triples SPD para 0<R<R0.
12. GS §16.1: (INT-ASYM) para k,l fijos; GS §16.4: bloques complejos fijos PD para ε pequeño (umbral dependiente de la lista).
13. GS §17.2–17.5: (RES-SOS); D_q>0; R_res PD sobre cualquier conjunto finito de enteros distintos, ∀|y|<π/4;
    R_res ≥ c_*E_y con c_* explícita.
14. GS §18: A entero PSD ⇔ A real PSD; §18.7 cualquier cola basta; §18.9: λ_A(T)≥0 ∀T ⇔ K_{M_Φ} PSD ⇔
    A PSD real ⇔ A entero PSD (o cola); Tate ⇔ P(1)=0, ∫P=0.
15. GS §19.7: Q(E_1)>Q_B(E_1)>1/2000. §19.8: Γ_{1..N} PSD ∀N ⇔ objetivo. §19.9: bloque {E_1,E_2} PD.
    §19.10: Γ_{J..N} PSD ∀N ⇔ objetivo; lema CPD-m (m restricciones finitas).
16. HY §5: K_{M_a} PSD en todos los tamaños vía (GRAM); HY §8: lo mismo para φ_{a,β}, β≥0 (Robin).
17. HY §12.5: fórmula de ondas para L; HY §12.6: realización exacta con observación theta y ecuación fuerte (no signo).
18. HY §2.1 vía GS §2.1: A del modelo hiperbólico PSD.

## C. Obligaciones OPEN (enunciados precisos)

C1. **Objetivo global** (equivalentes, GS §§2.1, 2.2, 18, 18.7, 18.9, 19.8, 19.10): para toda familia
finita (x_i)⊂R y c∈C^n, Σc_ic̄_jA(x_i,x_j)≥0. Ya intentado: §§3–19 y HY completo.

C2. **Desigualdad crítica conjunta (GS §17).** Para y con |y|<π/4, todo soporte finito S⊂Z_{>0}
y todo c∈C^S: Σ_{k,l}c_kc̄_l Off_y(k,l) ≥ −Σ_{k,l}c_kc̄_l R_res,y(k,l). En y=0 esto es exactamente
A_0 ⪰ 0 sobre bloques enteros, equivalente a C1. Para y≠0 no se afirma equivalencia. Ya probado:
R_res,y ≻ 0 y R_res,y ≥ c_*E_y (§17.5).
- **§17.6 excluye**, para cada y∈[0,π/4) fijo, la existencia de C_y<∞ con Off_y ≥ −C_yE_y, y la de
  δ_y>0 con A_y ≥ δ_yR_res,y (es decir Off_y ≥ −(1−δ_y)R_res,y). Falsificador: pares (k,k+1), k→∞,
  con A_y[c^{(k)}]/R_res[c^{(k)}]→0.
- **§17.6 no excluye** Off_y ≥ −R_res,y (margen cero), constantes no uniformes, otros pesos, ni A negativo.
- **§17.7 excluye**, en y=0, |Q_C(F)| ≤ M·W(F) para F en el span finito de Θ_k, W con peso 1+log t.
- **§17.7 no excluye** el control del resto no resonante por R_res ni un balance firmado conjunto.
- Consecuencias de otras secciones: GS §8.11 (ningún margen de Cauchy), §18.7 (ningún margen sobre
  observables finitos) y §18.8 (ni sobre un momento real). Una prueba de C2 debe ser sin margen.

C3. **CPD de log A** (GS §4.1): Σc_ic_j log A(t_i,t_j) ≥ 0 si Σc_i=0; también PSD de H=∂_t∂_s log A (GS §4.2 l.329).

C4. **Triples** (−R,0,R) para R∈[R0,8) y triples arbitrarios (GS §§10, 12.2–12.3).

C5. **Familia térmica:** Γ_{1..N} ⪰ 0 ∀N, o Γ_{J..N} ⪰ 0 ∀N para un J fijo (GS §§19.8, 19.10). Firmado: N≤2.

C6. **Una densidad suavizada:** K_σ PSD para un σ>0 (GS §7.1).

C7. **Compensación entre capas** (GS §6), **término de diferencias contra V<0** (GS §19.12) y
**control conjunto de la parte no resonante** (GS §17.4).

C8. **Representación tipo Green para Φ** (HY §6): construir H positivo independiente de u con
M_Φ(u)/u = ½Tr(H+u²/4)^{−1}, o una identidad Green positiva que reproduzca A.
- **HY §12.6 construye** ℋ, Q, C, D (autoadjuntos), B (simétrico densamente definido y clausurable,
  no autoadjunto), una observación continua exacta h con ⟨Q(v),h⟩=q_θ(v), y la ecuación fuerte
  Y_rr=(b²+ν²)Y+2DY_r+(−C+2bB̄)Y con ⟨Y_ν(2π),h⟩=Z(2ν).
- **HY §12.7 excluye** toda M(r) autoadjunta, acotada, estrictamente positiva, C² en norma de
  operador y local en r con M'=−DM−MD (débil) y E=−C+D²+2bB̄ simétrico en ⟨M·,·⟩. Coeficiente principal −I, sin conexiones nuevas.
- **HY §12.7 no excluye** métricas no locales, métricas no acotadas con otros dominios, conexiones nuevas
  ni otras realizaciones. No produce negatividad de A.

## D. Contradicciones o debilitamientos respecto de RULES_AVOID.md / OBJECT_SPEC.md

1. RULES_AVOID D9 (ver A): «sí sigue abierta» presenta Off ≥ −R_res como residuo. En y=0 es el
   objetivo entero completo (GS §§17.6, 18, 18.9), y debe probarse con margen cero.
2. RULES_AVOID D15: alcance incompleto (ver A).
3. RULES_AVOID B4 cita «211/HYPERBOLIC §§6–13» como cierre de «mezclas, convoluciones, congruencias,
   transportes, interpolaciones». HY sólo excluye clases declaradas. HY §7.2 dice que no se registra
   una prohibición general de transferencias o de operadores positivos. HY §8 (Robin) es una operación
   positiva probada, y HY §§12.5–12.6 son construcciones positivas. GS §4.3: «No se excluyen otras
   referencias positivas ni una compensación firmada exacta».
4. RULES_AVOID §C «cierres por productos cosh»: HY §§11, 13 excluyen representación y aproximación.
   No deciden si multiplicar por cosh conserva PSD («No se ha demostrado ni refutado tal preservación»).
5. RULES_AVOID B2 («toda cota con resto pierde más»): hay bloques fijos firmados con cotas de resto
   explícitas (GS §§10, 12.1, 19.7, 19.9). B2 vale para el margen global, no para vectores fijos.
6. OBJECT_SPEC §1, forma (G) a_T=‖V_TF‖²+ρ_T. GS §18.7 (y §18.9 primitivo) impide, en coordenadas de
   escalas enteras, una identidad única Σw_α|ℓ_α|² con todos los ℓ_α de soporte finito. Impide también
   cualquier ρ_T diagonal con pesos no negativos (incluidos los observables f_{d,q}). GS §8.11 impide
   que ρ_T contenga un margen c‖f‖² uniforme, y GS §18.8 un minorante por un momento real. OBJECT_SPEC
   no registra estas restricciones: V_T debe usar observables globales no finitamente soportados.
7. OBJECT_SPEC §3 (L-comp, «sin revisar»): GS §8.11 ya prueba un caso, con comparador de Cauchy cG,
   para cualquier M real analítica con M=O(u) en 0 y en cualquier intervalo. HY l.675 registra que
   GLOBAL ya refuta K_Φ ≥ εK_{2π}. GS §§8.7–8.10 dan densidades positivas pares analíticas
   arbitrariamente próximas a Φ con K no PSD.
8. OBJECT_SPEC §1 «reducciones PROVED»: faltan las reducciones exactas de GS §§2.1, 7.1, 18, 18.7,
   18.9, 19.8, 19.10. No es contradicción.
9. GS l.15: el kernel A y el puente LT tienen antecedente público. No se debe atribuir novedad.

## E. Cobertura

- `POWER_GRAM_SLICES_OBSTRUCTION.md`: leído completo, líneas 1–2921 (última 2921). Lectura
  consecutiva en tramos de 200 líneas, sin saltos.
- `POWER_HYPERBOLIC_MODEL_GRAM.md`: leído completo, líneas 1–966.
- `POWER_GRAM_SLICES_AUDIT.md`: leído completo, líneas 1–16.
- También leídos completos `RULES_AVOID.md`, `OBJECT_SPEC.md`, `POWER_CONE_001.md` y `POWER_BRIDGE_002.md`.
- Rangos no leídos: ninguno. No se leyeron los archivos citados externamente (GLOBAL, 053, 073, 084,
  085, 088, 105 y otros).
