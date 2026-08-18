#!/usr/bin/env python3
"""Standalone Arb certificate for the positive deficit integral on [0,20]."""
import math
import base64
import struct
import numpy as np
from fractions import Fraction
from flint import arb, acb, ctx

ctx.prec=192
ctx.threads=4
D=10;NC=96;H=480
# Fixed binary64 half-vector selected once by the floating Galerkin search.
# From this point onward it is merely exact input data; every inequality is
# recomputed with directed balls.  Reflection makes the vector exactly even.
V_B85 = '''KseUWxuZKj4KGI&QHdu%0Iyr-9;oa-0D!R<Vz8$^003__GEHK>007vCPhvqn006*H0o)h90002Yn4s%D0000Gyg<CY00000Ed`1_tp4%jrMFZ+z)nt#Yo0VefVxDLi6izt06=;}q!Oh*0000sbwnsW0002c$kNcg00000P_ena00000FdL3N000000KQ(m0000005~Z<053}|Y3XG@00!jF3ZXzh0H8<UWFG!L007X{IM1a%0000`;EVaa0000~B30?V00000R0v%?00000T*fXv00000By<7200000aM#Z~aS@x^b>nkCt!{QkY~n~ibunK#LIVRo>O<hs2dSh!w2XD;QnoO@APVkzQ7PxW00=3VTtaC*003NUp9a)C004Lx<7TBi007j<;>l?|NclnzEoOi}(;#E5seDmC^|du_0G0+n&@jf}+PR@V<~m7JY+F9Qa9iT&)2ZaW0J0RrITdX^0H92@OjP_l007bpO6HzC000>IrD{>U73fyJt2T*0e^I&mcTrbAk9TAObax3qmRQpkU1yp;i0(|f%Oyp=?r|z!w4UL;h;%$4Vk&Yy06<qOSmFUa003b6N>gGy001Dbd?rD>H^u_x+*gu6=AaR(4ZK}H*J?8v!eI+Ps*xCUe@l%%_nB(qfe%W)LP|FEp}O0>pa%CSq5E|`04md;Z;Svv002DJ4%UXe0Pxhl9SkwNv^nYm3xb(H-ky1uu{>fwmeWjLc^eEr_8G_KZeK_~dWf@C4YN(Y#D0&J$Kukx3r%mZ8Z~)6fF<s>FK+of04V<TR-2N%0H~8c`oJQ**w5)suMwd?xz)idCY@zJq6l$l6nYCk;HtK^za@>ne6+TM``}N$U{6DO&<Dc3N|CJ)?rwWMfad8TBO2~JfcZ5j&6k$E05}$Js5BJ32UyzLo*AY;eRNG7t<z{fm_ckmAY=(YVEY#VtC^m@HPK<7JUmdoK6ap5Zfuu5&_wXPY;b%%fE%hPY}?5^VA<=a`gxeV0APOO2rT`(yGM^s(aNhoSAFtpm$GX=0G>ZEy3z$d7rrS~szIl|{3CcHvuaPiQ1Q}eeI>{}K5$2}xE_2xz}@k-+A`w2fY4q=(5;xf0FYGw0U7Z-QEopZum-U|?|KzDiVSW)Q2k{vJkkI^59+Gmp}(%aRYlVaY`jdqK&gCl08rLFK&r5o-FA9C=wvAfEF|^3058x90#%p10N|O7l{gMO?^cgT>R+@!U+SQW(Y9|t*{86R2?X^%qG2cb39+)i#K*CXD~3qErWqKEj<Mf8P@Ju~zKeG~fX{U+!w&$x(1j7>GHaB)008Io33VDg0o`!e``foaf`OSR&qZ)Q7o{#?!kXAVF=YhMV`jC!PaB|lCG$eQ<g1UC!s6pS1iDCX6ozv>0DK2NWt{}Q0Dyt@!+npu0Du`#rgtPfIA~Ri4r04MHnedf3N~;*x3dj(U*hDxaS;F(C|I|?n7_khuYEYa7?+x@;TGpTI29Et>rZVx0LbSFxwHqp0D#ST;PHUG001F+YEv*gyivljYSz9#%SDOo4nl7~G`mRo#wPr}NGF&~(q_26V8};bki;Usu+4((rd8=Z06I2ng0f;g0HC~PKy(Pb003V^E@W#w007`^S0Xw*GWbk{z74@Yu~6M)i2-dtJp%0gup|e+Y;^y-K76>oWZH>k#y%T9AWFYgNSNw90I+*ySLska0D!uDyDbL2004jj>Op`!008W=Srkyb-g6S;eu=_A>l@U(o2h9(YWJR+;06%CCSw^M?u)m+P-GBE3V$~~fc@@qf#T{t005u;MfpIz000QCv7{Wm008#$SwiEy004kWoxrfXzRgCAme0dKf6r<y2}NZ;3R7_*lQtB;bRGjJSCzHC<UkF0Fs(yA0O&iNwo~Oj0H7_5P12ja006?XuNZB;006;p_dYwl00026D^LWzM%Is*3ev<s{;1M;!_!|s;}&|W+4vW~bpzvh8bGtY08{<7UOX>806rW+)}b4|fCP#PiInrb0MLx;Sa-#}0Dv?Ibkmf*003->+9P7ULA#0^w#LOjOo1>XGD=iG+lwW)zWE%#_Wb)#8w<3)RO`-GSk!SoO!B#N6KFxc;1wj;c@-5t9LGK4K|bfb0Ix)F4Mw*;fKmb-6FG&wkEM#d%^=1<SoWs{EGsrYg`ca@6Sp6~(ac$2=ZU7ibjUWd80b|#Q2Pfo<X88-AP6fjO#8z<05QX%b{CPofHbsmHoaUu0G95Icugn0bfyy>=Mcs}`S<g^6?sIzqU7a#J*ptTmwzZ}KsTAb>F~;sB@a_R7!2`v#Dd1XfH#RA>0*gJ0NpnTQ{GR#0Lex6iX##|0HjW8YuMGiJP|x~hLOcT(pyyj;FMaw+n{jk83-Z2;Xm<)vsrq+LvzlzTa;2hK)FXYHd(H{06^;<J_t)a0AUOral#_K0AQ1{!WG~=07N?j)8Lo9oc>J1GoZvjg$)ySkBMc!y!T`H)%YO4@s(J0HfM)E&wISJ!ADX)*wWgN0Y|aD04D94=@(7C005Z%2>+wJ0DQmo9d*n+005I5(==l|ax-}!R6WB#TB&utL8ooM>)@P)QGOu5w+6|Fbf}#^qHpWc73onvK-<40ET*!(0F0q1Q~_5#09;dAVYDqh0Fce5{Auw#0DwcxS1q$VhP@i=8*ITp@k6jv47hT?g(KlA6g3~esCY|-QLCpu;~2tV$LUc%fB-}jFj2=n0I*QN_`je%035>p%vNkY0Qtme0b4db0Qdk28V&(HbL#$d2xY!M39?@8c35`5OU^{x3Y8qcm;QH%)ZVZ@C~y190qR;lz;DfD!CDzUfGQ?)9(3(J0E>cY(}2D`0MKQC!NrU{01)E!oXA)`^0~iw$@sWGEHf`0Ua)w-o+U_QU+ova^z?aHN6E21#A~~)1FuCs07xy44)WMN2s9{UTz|m50ARrhY?F{Z000ucrI%g30001ax$P%C$l=}$TU4_@0gfEH9AJCD>#FTRhGZ1KZWm~!>SVM&s>8XVJ1Rpy00@}4JUZXK008<7Z{>8o003~-ZP7kG001aEun!Eq0002EhL_qr2O_1G;ZCYQ=NY5>Set#ny8%j1A8Zi6JTw-oNp!Y8cwlbB_VYVFKn}Mss88X&0H95YAsSG<002z8BH#o)008KkBvrM%004mhR6>G0-Djm+T{4<KkT>H4QdWPzd}c_pphF11%W|9CrP;SW>-ZEB;|DQ5fZ0|0b+qBV000gB))^JO0D%9{@Z|qI0000TKu$(H006*18h{x*Q^tiXDBxGWs6XX;g+zeAmDvKLA(sBWQqP~?%8<A|GJDZ&en%KSxP%1>!*Jof0AM}a(?&@>0O0YFD$f5r0PJGgF8^S>005v~Po*Ec$UlZ4UHhHC|JO9Aw3mRty}VZ9y1MATM)aMjQ=GUyCy6rY%^4EDN}HTY3y9#oz$5FvDI!`u05sclnYjHt001aiZ83Pf0MK?p%OV)Ofgjt!=Vh(G$@i5Mlca#Zf#=^gPn_01TCCkbFa@|it}aB|jk+wpaM61J`U&2>FftM}CMsh+fY;*1`R@5V0I(*b9r}U10Km8BAL$Xig`t1dv)#47=b|#1&1`_bXdDG35Cr!=_G37cJleKCKannfQW!VB`xf|*RrcAv1aRKpg-U2W06u0)cH#6q0N747DM*IA0CD}Q3s?!fFJ_7m3*x-L#!r+5Zs&i$pD<tQw5bC>PQTGOfiJZ_e%QTiq-#FDtg}Unj|tVi3N8DUCN^w6KyKE6(%|hpfP_ecv>1uJ0KmBM4`uzkz`2QBSJJ`1l>#H}9ejSjONDfsuOACPiU{9@G99x%bNP%1kPbq=s=kTTqXN&pXCbs^|HW=S@Gq0vdHmo!zzPN}oJxwk002{^yJgh7^OM3vQU=ApcZaLud82&4Tk{2>P~i|i!c-sVfxfUlQHX9@U;{+HcbApx13|;RjBPwFe(7&LfRCiKIEBAFfF$Wdd#H)L09Y|!XeRhO+<ZJK*#XGE$<2Ly1#5c0mkQR&&Ak&pav6S0t6;1?>`4TU#S2BgCTFO+1y-%SHnrj*B&u&c5w*<uGk4Iu09VJev8;x?0O(p~J<Jb0lld`VRlCZ+LbRn8RN;5OJtp;QJ|7l8lzm;w`X8r04T?9hdnrY}CGQVhUI?K*xG#KD;WBPL0B6n}iyGp*P<*KfKpcR)0Px3PplcvJOAf^e%PP&kg5`3PVHI`1bItm2?gSV=)bVQk{qvzd*rE<>EoVf&yzVWv<3YYX_^Zl3W8-T*05HaUg&^m=06=8=_QX-V01yYno*yziBNsY?+ey#ANniMV?-g>t24JRZNpl%Lu72J;jwG5s@6>8oiPb{Bgx2F=(-+A-aLvG3MT==Y0Ejty{uJT70N^XNk_?bM0KoYtn!`vuwTp^a+lkP>t1~*R*WqoyPq8}rdvh8;RYD&nM_7?QP_xOlx`aT!_-)62V>{730D==b97Sn80AO*|@c-mI0HEA;TokfA0087hr!;3gTY392enQc|x<re{#${)}7_ji49TOWr$Y{wSIl_ZJsr^S91m!xuz$*5@?2Fbt0EE>WBSmpN0KlrqEAAIP005zn1fbPC0D#<|{MnE^BLZMn$Ia2d-=+D}@XTPp$h8i<USu0TyiFR_1-o!Q7-}jo7l$&wz^L5L6oueD0Cd+E*bIn0001Ah{b@u!0Kn|)StJHM000EIKi<eZbj4@;DJ#;yJks#+&`wmpL;_wf^MD&a2;5h`)htv#fE5xAoY4cmfU<S4a}@SH0KjasCj7TO0009Qq>_R?0Kl-1x~fe*006+zr!*Kntc>YSY+BO4Q~j2dgWo&9FRC-jucsS7&72kg619RppHDDeqM%$pfL=DO%8xQWfGd;mCkF*S0KUjp>6_L)0Ps1^Y)Ym*0092#loxb8'''
half=np.array(struct.unpack('<480d',base64.b85decode(V_B85.encode())))
coef=np.zeros(960)
for ci in range(48):
    for k in range(D):
        coef[ci*D+k]=half[ci*D+k]/math.sqrt(2)
        coef[(NC-1-ci)*D+k]=((-1)**k)*half[ci*D+k]/math.sqrt(2)

T=arb(2).log(); l3=arb(3).log(); dd=2*T-l3; ee=2*l3-3*T
MD,ME=20,8
hs=[dd/MD]*MD+[ee/ME]*ME+[dd/MD]*MD+[dd/MD]*MD+[ee/ME]*ME+[dd/MD]*MD
left=[];x=-T
for hh in hs:
    left.append(x);x+=hh
mid=[left[i]+hs[i]/2 for i in range(NC)]

# Exact rational coefficients of P_k and moments int P_k(t)t^n dt.
polys=[[Fraction(1)],[Fraction(0),Fraction(1)]]
for k in range(1,9):
    q=[Fraction(0)]*(k+2)
    for j,c in enumerate(polys[k]):q[j+1]+=Fraction(2*k+1,k+1)*c
    for j,c in enumerate(polys[k-1]):q[j]-=Fraction(k,k+1)*c
    polys.append(q)
NM=34
mom=[]
for p in polys:
    row=[]
    for n in range(NM):
        val=Fraction(0)
        for j,c in enumerate(p):
            if (j+n)%2==0:val+=c*Fraction(2,j+n+1)
        row.append(arb(val.numerator)/val.denominator)
    mom.append(row)

# Contract the ten Legendre modes before integration.  This reduces each
# Fourier evaluation from 960*NM to 96*NM ball operations.
cmom=[]
l1scale=arb(0)
for ci in range(NC):
    row=[]
    for n in range(NM):
        zc=arb(0)
        for k in range(D):
            cc=arb(repr(float(coef[ci*D+k])))
            scale=(arb(2*k+1)*hs[ci]).sqrt()/2
            if n == 0:l1scale+=abs(cc)*scale
            zc+=cc*scale*mom[k][n]
        row.append(zc)
    cmom.append(row)

def vhat(tau):
    out=acb(0)
    for ci in range(NC):
        zz=tau*hs[ci]/2
        phase=(-acb(0,1)*tau*mid[ci]).exp()
        term=acb(1);local=acb(0)
        for n in range(NM):
            if n: term*=(-acb(0,1)*zz)/n
            local+=term*cmom[ci][n]
        out+=phase*local
    # |int P_k(t)t^n dt| <= 2 gives this uniform omitted-series disk.
    tail=l1scale*2*arb('0.149').exp()*arb('0.149')**NM/arb.fac_ui(NM)
    out+=acb(arb(0,tail))
    return out

a=arb('160.25');B=arb('320.5');c=B/4;h=arb('0.0012')
def integrand(tau,analytic):
    vp=vhat(tau);vm=vhat(-tau)
    rp=((a+acb(0,1)*tau/2).digamma()+(a-acb(0,1)*tau/2).digamma())/2-a.digamma()
    rp-=c*2*tau*tau/(B*(B*B+tau*tau))
    return vp*vm*rp/(h*(h+rp))/arb.pi()

# Directed interval Riemann lower sum.  Every evaluation uses the whole
# subinterval as an Arb ball, hence no unproved quadrature error is present.
normsq=sum((arb(repr(float(x)))**2 for x in coef),arb(0))
NINT=2000;width=arb(20)/NINT;lower=arb(0)
def directed_r_lower(tau):
    """Positive tail lower bound, avoiding digamma-anchor cancellation."""
    lo=arb(tau.lower());up=arb(tau.upper());N=120
    bracket=arb(0)
    for kk in range(N):
        bb=B+2*kk
        bracket+=1/(bb*(bb*bb+up*up))
    x0=B+2*N
    # Convex trapezoid: the lattice tail is at least half the integral plus
    # half its first endpoint value (step size two).
    if up == 0:tail=1/(4*x0*x0)
    else:tail=(1+up*up/(x0*x0)).log()/(4*up*up)
    tail+=1/(2*x0*(x0*x0+up*up))
    bracket+=tail-1/(4*(B*B+lo*lo))
    assert bracket > 0
    return 2*lo*lo*bracket

for j in range(NINT):
    tau=arb((arb(j)+arb('0.5'))*width,width/2)
    # The chosen vector is reflected exactly, so its transform is real.  Use
    # the real enclosure and monotonicity in r>=0 (proved by the tail lemma),
    # avoiding the severe dependency loss in vp(tau)*vp(-tau).
    vr=vhat(tau).real
    sq=vr*vr
    rlo=directed_r_lower(tau)
    vlo=arb(sq.lower())
    if vlo < 0:vlo=arb(0)
    lower+=vlo*rlo/(h*(h+rlo))/arb.pi()*width
    if (j+1)%250==0:print('interval',j+1,'lower=',lower,flush=True)
lower/=arb(normsq.upper())
print('coefficient norm square=',normsq)
print('directed normalized delta[0,20] lower=',lower)
ell_upper=arb('0.000001746475')
eps2_upper=arb('4.441e-24')
eta=arb('0.0003')
ell_eff=ell_upper+eps2_upper/eta
threshold=ell_eff/(h*(h+ell_eff))
print('directed capacity threshold upper=',threshold)
assert lower > threshold
print('PASS directed finite deficit exceeds computed endpoint threshold')
