# Auditoría105 — kernel Volterra mixto bruto

Estado: **Prueba matemática y lectura literal de la fuente APROBADAS.** Sin cálculos nuevos. Papers intactos.

Se cotejan103 (CT3 y prefijos mixtos), los jets completos088/095 y091 (Peano). El objeto105 es un kernel Volterra para la pendiente temporal, distinto del cociente de cofactores Peano091. El alcance es sólo la candidata positividad del kernel BRUTO, no toda representación Volterra, gauges, W4 mixto o W.

## Identidad exacta

Con p=V',q=V'',r=V''', tau=J/Phi, kappa=K/Phi, E=−tau'>0, S=kappa'/tau'>0, w=−S'>0, D=tau S−kappa, X=tp−1 y Y=p²−q, partir de

`kappa''−2p kappa'+Y kappa=a−tau`.

Usar kappa'=−SE, tau'=−E y E'=1−q tau+pE. Al derivar resulta exactamente

`E w'+(2−2q tau)w+X'S−Y'D=E`.

Así B=(2−2q tau)/E, R=X'/E,T=Y'/E y w'+Bw+RS−TD=1. No se omiten derivadas ni términos de borde.

CT3 da S estrictamente decreciente; kappa/tau es su promedio en cola y tiende a0, por tanto S(infinito)=0. Entonces S=int_t^infinito w; D'=−tau w y D(infinito)=0 dan D=int_t^infinito tau(s)w(s)ds. El término integral es el kernel R(t)−T(t)tau(s), s>=t.

## Cambio de signo real del kernel

Los jets theta completos dan p→infinito, q/p→2 y r/p²→0. Para tau(t)=int_0^infinito(t+h)Phi(t+h)/Phi(t)dh, cambiar u=p(t)h. La convexidad de V domina el integrando normalizado por(1+u)e^(−u), para pt>=1. Los jets dan convergencia puntual del exponente a u; así tau p/t→1 por dominación, sin derivar un O real.

Luego `[X'−tau Y']/(tp)→2−4=−2`. El numerador diagonal es negativo para t grande y, por continuidad en s, también para algunos s>t. Para t fijo, tau(s)→0 y X'(t)=p+tq>0 implican kernel positivo cuando s es suficientemente grande; no hace falta suponer T>0 para ese paso. El kernel bruto no es no negativo en todo su dominio. Nada de esto determina el signo del integral firmado, w', W4 mixto, U particular ni W.

Lectura final completa de `POWER_MIXED_VOLTERRA_OBSTRUCTION_105.md` aprobada: identidad intermedia Ew+XS−YD=a−tau, bordes de S/D, integrabilidad absoluta Volterra y paso DOMCONV todos correctos. El cambio de signo se prueba para s>t, no sólo en una diagonal excluida. No quedan pendientes de auditoría de esta fuente.
