# Control del cruce aritmético ligado por el módulo de traslación

Antecedentes 213-10-A y 213-11-A, BUILD084(1), 106_109 §§1,3 y 106_118 §§1–3. La diferencia específica consiste en mantener la misma función en los dos extremos de la celda lejana al estimar el cruce. El cotejo habilitó un lema auxiliar para la regularidad indicada.

Fijar 0<δ≤1. Escribir el perfil físico f_k de BUILD084 mediante sus saltos β_j, con f_k(x)=Σ_j β_j 1_{x≥j}. Para k≥4 los saltos de cabeza están en 1,2,3 y son uniformemente acotados. Los de cola son d y −d en k,k+1, con d=log(4/3). Para una combinación de traslaciones V_sF_k con coeficientes z_s, 0≤s≤δ, sustraer cF_k con c=Σ_s z_s exp(−s/2). El resto es exactamente

    exp(t/2) Σ_j β_j H(t−log j),
    H(u)=Σ_s z_s exp(−s/2)(1_{u≥s}−1_{u≥0}).

Esta H está soportada en [0,δ]. Dividir el resto en cabeza A y cola D por los índices de salto. El mismo par de fórmulas define A y D para toda H de L² soportada en [0,δ]. Escribir w=log(1+1/k) y ω=||H−V_w H||₂. En la cola aparece exactamente exp(t/2)d (H−V_wH)(t−log k). Por los soportes,

    ||A||₂ ≤ Cδ ||H||₂,       ||D||₂ ≤ Cδ √k ω,

donde Cδ denota constantes dependientes sólo de δ y de los coeficientes fijos de BUILD084.

Para k>3 exp(δ), la cabeza precede a la cola. Un cruce del peine sólo puede ocurrir para k/(3 exp(δ))≤n≤(k+1)exp(δ), por intersección de soportes. Cada emparejamiento entre una traslación de A y D tiene módulo a lo sumo ||A||₂ ||D||₂. En esa banda la cota elemental de Chebyshev Σ_{n≤x}Λ(n)≤Cx da Σ Λ(n)/√n≤Cδ√k. De la fórmula física del peine con peso 2Λ(n)/√n se deduce, para la contribución mixta completa al cuadrado,

    |cruce aritmético cabeza–cola| ≤ Cδ k ||H||₂ ||H−V_w H||₂.

En particular, para H fija de H¹(ℝ) con ese soporte, ω≤w||H′||₂ y kw≤1. El cruce permanece acotado al crecer k. La cota con módulo vale también para la H escalonada original. La cota con derivada concierne a H regulares. Falta una estimación de signo para las combinaciones arbitrarias y de los restantes términos de la forma. PROVED en la clase indicada tras revisión independiente.
