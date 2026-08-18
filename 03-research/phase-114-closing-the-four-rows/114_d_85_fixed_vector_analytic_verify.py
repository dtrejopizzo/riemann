#!/usr/bin/env python3
"""Directed analytic Rayleigh/residual certificate for the fixed D.85 vector."""
from pathlib import Path
import os
import base64, struct, math
import numpy as np

# Reuse the fixed vector and audited analytic local-ODE implementation.
cap_path=Path(__file__).with_name('114_d_85_capacity_arb_prototype.py')
cap_text=cap_path.read_text()
v85=cap_text.split("V_B85 = '''",1)[1].split("'''",1)[0]
V2_B85='''a9N?Z0#>2Fc8`le0sMl$03ahL+STYj0D$@Sdlm-2000ss(WB))003NvV|~BA001BwCjOH?0001&5pZU{0000OFoQNe0002+!DIx!^Gr8r1{<-zqIV@*8YzUo0F&MZga;SD0Gx9K+(*$q06<usAsCrH002DYBP?vb004G+HjO<#005ADm?aIq0000Cq?g(~00000#d4;-;?TU)b`QG0d{h!7D-VUg0LuN<&;Rzm01P!=88X^F000?TwJTpf0D#__@b)mi006KH6D{>U008WR)JDL)003|_;v|SY002PSv_?_ASiwJ*jg-N^=kUBuWYC1aaBn!;g2D?w4^G4FqIcRpoHv%1i@Hm`IEYh@PEQrS(&NmcX!O554#=G<*>QrsAdaxR*y2S!JXgiCj&BIP;ynG62=m3i_ykTtMr4D(26#yIba@~@Z`ygjXye#EcGB;82LEBcDNcufc3ls?V4`kB(d(N%h??<47d%V7dYLKm+7=Q$fX8reWwOw`v+{2nm*dI5M$>WdSKNTVIw_B?=P)Th(S+*Z%@o!?#-M)kqYrDoTHF!xl^P4axGnCIz}S^N2&x=EunHYL97W5Z#Hivt@PdiZNYtUc#Xn%!3@pvR)gr;gBe8nFf>xkQ1XeIVjvcPB2RqU}{}IEQn`d#p<YXA_DUt@hJ^<!5q8^()Okf8`?e!}?09^emgj-&`4MhFe|44bfY^baFdz#O`eR|Kd!3lD|hQJ1T7f3TdP$4Nh&j!mrOg;yuoPBh@`w51*`SSq2L~VQR?rWeu!Q;?g!CEIh(07hmf`z@j^gA$auIyI49}>X0$%D|pl`wt)P+VZY**p)LpGq}9-fXy3drH7QMzQHGW1x1vhyC*_NXqoRKds-fHin`-W;}iv^v)eUOO<TI6JEl+_@kmu%ab|01Gf$YK&;Te*tVmRxH&^Vh$9cWszf$Fuq`&F+y|pR6TEGI?yz^hoTD>0$=un!C1b)XWTT@!CXK8FH^c=!9lW?T@K3|Mz+Oxj)e;cAnjaW@96->&N;w3qrDbYA<1fg|$|*KKo|pv9`WLLe91xf4zMgl!R>6pmYntFaKZi$PzO<t~qH}zQCb<B;0IrXAVHd-^u*Y*{gc2k?O6KgBC4kPqP%yZDP_B1BlX1vi*7`I*wY}*POnkz=rg1=m&S-YNt_8gJ`nvW#4Jfs+FTJ8YA2E-6YUCQd=s^rzgWJKp@Qirm>n%Dw$an-C5@^f6#;(GYe5-&z%`mXf^u;nipGEbBClk%SByG05XdQIEV=5j~;0OXfckpGWgU+BmMzJr1Hozslzvr|sj2ynaKqo3x+kQ<v5bJo4a#hE_Hb#*h1=@r^t|TKV?@KQ~a57;Fyd%@TnyL2x7TIvV<UGPVFVhD;xmTlM#wDCRgNbhhy}~QK0E+~`guJf2fJ5-@HGyV4-sCRt{Bgp+XbnXfMlOgyFbOH!8-gc4HLsX^s?*lK1j4vc<A-U!6F>te;DHQ2ahtlXyabj#;5UXJI3X&%pt|C(J!{20U~VX6`yh%u<#glnR^z$9fIyvoGk%IcP`}5>*c%-`@$!>_4r|%IbS7y8jS^tK(*0^7!yXVmoD)$YR#1~YAp1ia0&5*To_|Q}m{<5bz_CrVWmmR5X+Ir+`#`L}F7jmYMXZZIeyNzTF?j<&3|J^pTf^GE?hW_->2^iF3`oW2S+x>AsC)tmjMS$+*eq{CV8~`Yz|<x!aQiDg5Y$J1U_kCXZ+*ypT;+hjOxuV2Q>lwT@gw`7T{8r~h5ys4^O@SdL&7USC%#fXcctDE%jh6J0|RW?^HJJ8D1SO+a8IK>h`Je&w|Q$lV2#kT^tm!UQ|3+HJ4mBHs&P$t>3E7ik`QTY5zQRG6fJGUgWJ}=eHy=al-hwlUrqKqT$4~fZGYmL!9O29_}JH{zZUI1*q)-l3=_FM06gWds|AETYpm&*qN=n%=W{369c73=mpswPCto4I8HL7}^lIEb`r3%+d>F+(m>7Q~z-*j8xgIn<)AevZR8=*Hfc8N?(4gte*9Z|l;5siY?J?awzyg>3u=~D0KUv(JaV&yA1*s#NSrs+EsD>)sn_>7q?J*1A6ZO%)!ad9Q$b6_i54kU%Gg*GViW5z;L-tTUp5ThT{2w8{k}n(Ib!G28Ul;Rmi1)%jW<;ar3_yH82JK1NL?SJ}#CfxmiO|A63JLAy@~4o#^46|V<2+qHAX=wgiRCH2(>MLYSvvPU;PToNaXiGm`!wSN&AyO5%gs&0i>Jju3l%;ZIdyeEfxB)$d|xZS{QzQdFk_)UruFV$@-Ae))J&onc(E)#h!mlh-Usi!&-2k%kNvSd&??Igf`N9ukS=o;AJ{xS+?J>TD4)ka%KJ%r;LdG72{WGR2i7XT8hnCCj$@HNewNTpsmCY2kKNN|cH9d-6$c9dZuH2#^#0Kmb^d@on&}WUe?dUK;!-F1k5BtN^I7rGtm4Q&C-qf|9qM2|O3IgdfNLthZ0SbbwfK`h{uV{p1n)LJ$2Ybc<_6b2)$36?{(HK;v_*{lCbToXr02z@$~G#!^c(+-Hvh@Ig4=Eu40XvrG{o1g6Z}9wC9}EtOy()S_qc<J6Ec`SKvfu7B(ZnBTB1L}QTGYHf}xw6@bb{TGZtS%Sfr4>TIqUDFXdFd^=v^+5c?Rt@ZIw;rdi29)xcb+y;o4bFnLWnJ#{I+K%6i3p0s#An;pf#jLK@ho+zeG$N)RO==fzVUVjF@#7jOmIndI*C{?M;?%tlg#M|=(xfy7^<W9F#HIm3bm0!)0$+%>{&)QtoIZP|R)~X1mEtk>0TA9o`QzNXt?2>-BwEBU*fy-0*8_-m~9YlCzF5e}-1Ftq#KGyWTWGdbgGY`VOLCd|Fhs(x4#NI%Ik3ew0@f($LSkNKA`tApk`M$M2YR-?4H}{r4+FaI*i8^b(pM&?Z=k7f|>G1KCWLpis5TzheLay08fYLq!jxnUY&_%GyozcWUNo0QKSs--3#Tk<SKad;0@_)(H_XEp5k5_>FY1v^u^L6*{Cgmo+_3dw1gMRTn;L16wf62bR&^rE*Kk<k?0H9R$d!|yo>#=HE{d>YcMfW}1Xw`PVzRSP}9}5w`1`8ecb79Rsk`XIh<?TQ|c;@?~`V0uZsu$HGxtFj#U~YmxAGCM9z;%DPNrgZ?0JU~_#(o98puu#ju-d;rrg=P21Uz`Z5!SMDt6uoNs7L+!teMR|v&n=*0NF9Vz#6&L7Zn4(ms_EQ!!?6FAVO$-pCLEBAihe0#C-xi;58Emy_&<kIH&>fVwAc+f;2N<98q|`D^>UX5To)wCuR8-#8k{aJem8G1-VbYamQV)uAKqC=u9k(wFiJbfC`J>b(j}D*{tEW_chNv08b)H#uksf)a9ic(QLIpD(icA86$VUba63w|6dJ1w50pq$F#{l>P@TV^+{U3b$^per=b76tw8=m2kVACuME~xaakcf06?Pwj8`qZDj$S$9<^k=meKy+=%%ngtO}!T=g)M%!7ZLn1%wwrwEslK$KAy~v~LDVF0o<0NdiG>Tc`TH6V!llr!9^>KzXoq?$jPVaBEv}4#KItAgF0oJC{hjx~$K&Ec>WGikAW3PJ?m31uGBwf4Uw&ns)`Ty#T>J5(Hdi*j;75{))PKg>Uq|h_zy4*9?+9W=08$Hx3s)G}nYB!@;q<<ql&E(|kF+J1Lli{6V5W$b9B~is@><YnV`2!~P*ZOBh|fjJ38t*om(AN&jcQPkDXPV3F#*uQewzYYmh=V8o&P$<GQs-~aXY9m2G{5Y`Zn)POR)D%yRj0nwU21-_T>XUSo|>l-XO%7-IAP5f*^lE|b!#n<Tj@poyymn`E2c3jrIlmV`yPVJOEhzI6%Y-Qs-X;|<JfIPRnIKwB|#?&#qB0IG-bT5@ZW#pWnUS&|f7x_Gp9OolHDCkREc-ex!GyOJ=`?_hqZDqJr1(m@)+;Moi+K7}ruBk)h1GfXcMx3$rwJo~5O-{79)jvACQ3+&aI<u2MCT4HUn3E(wcAq^Tp&27TOfs)L?BA`v%CvZ#a?WVJ*mf}%nkVBuXh|ql!?cn;LUG6it{ND<=yLs<lb*l4q7(ia1AR=q?Yu_leleCmdl-{Bnl)5E{?*yd6DlD;5`SZqTgke<1VRGO?agMstHM;pY3uJj3&hf1C_auoIPw<D^H?RlU$7@|hJwbt(h9fL%GYAN>w78;=0co5g-d-G)4E|lXz>3Yd0!kqsosY$Shd2w4vhDhx9?-VXVq1LDv<O&PvFKob@hQg6nAN)fITw3Z;jlfr@z#^Se;s@A^3Z|nBG-ZFr=bC0Xeee<F98wdOb|d$(IyAstGSfp*_dG4xzlD^O0b_Rm8ErofGywx*4Sq6G~vc#HPwm1Xn@5L7#JUCX?yB=&iMNL%Nr|#CDRR205rd!qy?uLy~JhrN%!+ft3b7YCo#E1o6tgv1^P&5W`x&8qZHGPl@q8SYyEiz?hl6*H~XX?w(Y=xCI`&0Nw<>pcEWUU!1tS9JE6(mSe6z2X>$6z6@<Ym#EtDGzZ8&8}_f2jRVfU2q(tkq`+6c9JTD*o=U;J9I+V)S}?c0Zhad`FY0i;K!|i1aBL^N$QER}+s5I%M_rH;PfM~t%J+`#E7xm3dKi5~z}f}Bc$P4Vw5rg)7B@Pxz_MVz*Sk2*pDYu;RDQMEH2&AUAU8MZB$k%FP%~k!U@up_fFgQG6h0cgiDECBRvNWG&IUfTZ=PpA`}e4A&RH10{Sy35I8M~QSh;>QcV>FNn3xJQZXQ9t07>_-h-wPHAmDd8LyFbCuBbj)>u#dG0I>A2Z$odr5)HqMo<X-ihdh|=6a`;D8ba|%k(DODYlMyN+KT4Bw$Gazg?X~R-o<t1R11i{<zO7|FFIbn$hznEVT3Wh)Z8V=TXF)vQ2nAQ)1J}2'''
ODD_B85='''#|YydEJkcU(@@Fb4>C|c04;crOe_RH07!R<dSKo@0Km<KE2Oo)002P;6S<8(007v5yoF-E002NnM~XB)0000?EpG(A0001>zGKoo(ALk*Yde2GfB+2r^UPO201yfxg{Trg001xnSIDeB004k2li_#10002s3}!w)0001>9_9_c0001hk4fA;0001hAt<T600000L*;ZmxrfuNNAZh4%6vkB8=7E0YH_BMJ;@V40N}CwTk}%B0M6gC?lEP)06^fXIVJ`^006{dgC)wn006+&x{i`P003aITT@xR004l8??NFx#F@b5j4zfyZ<bWd?M`JsQh^2!z||5zni_)nM{A?Lg@3$*jB;VVn~?DoJPGYRI6b|LmtT^-(t?yOsX$#lKogaWD~24s8VbuI`BB_FA5?;ho-Lq1pD|F7&6R0CK1w3K%|#GDSUE=!UD>g|)vs4F*~wnM^Q}ae=z{7!qP{WDLvM6F5<eGiw&^oH4KeOm1?}*>fS%Ik;6SK6i?S!F!5gMOxYO4fPZ4cDM!<5^@0kccC`giS9Pzlm2!#NZW<grM`5Tr)AR_QR3T-}T%OZk3q{{6Y@m&Eu4qF_=T{F?VWS!mg!hC@|aJ?dQGOesX>@B4RYjAHr@7{CS0)+fNeBL{vn#sPt<<gF-f3;M;bIA1;8-(*ccG`)lc2R*n(F7<g=${F_Ll7J;gm1dMULJG;bg*JPd_iT;b<VLrIaFsNI5==WD#AF1u`kd*mYb-V(~!ZwdvDb%vsX;M>IWH}Qfl@+)W0acD#Us{T%YCMIWQKz){$hqC{U`rToujM?bl5_tWa!oq)fFx9(+Sd*xzqIOqiIVSOWLHR&!MASm46GpYQW;8+1Fqd{(iW)NJ@YG-()31k`Umpsh7a;s+bOxBE(c6)Ky&43R`V<KjU)7L?8R0;IS<iw(*Y#-MFK<=koHdZ-D%@>+XwvOmMVZCF`C(d7(2x>2Z9e^>cE>R@_8ZDmY7O||6Lo<<$L{k)*M7x;p_ny|agzJ@$JdB^d~S*5!_-v=#f#HwjOZ1?;kFWnQrUqSl?=%vEGvi&_y=ZZl-z~&T5Y7+T9l_wNV7O!HxQ*IJMsD2&2c!4_;lM;74BXpL4K0-P?@qDNdx*@(lgKr~Ekqcx$D74Shaeo@WJ>$Emr4_-x?eBh^b6!wBIli|CC!6;@4t{j+2kdpd@W2Sa1>76G?4Ip{BzlxQD9)#7bDTOnJ=)Z9<Ltjb7a)l!!OdAebo5Yf8!;fi{mOnhsye;CU~Yr0B~@2Gt}lDJ%>wm3sPo<w(XfEMOAd2Es8kret&G0$mQA8O02!&s2`WH5t@K!G%5T6w{LxWfOw>U?S)3LV44NXp1~*@I>8!TC4f(%u<WyZgVrlK~m2UAp)_Yb3Y-okO^iP`$A#D=9Ch1m3AvLZ%@RWS`qG3%uYS(Pd)oj2&raON_Is8Mvnov_oc~>OA*q}NxjgYOrvVB7sG7Mop`#9XF*gNVymga1RWoU@KxE-pf%8mcLxZP;4OYprsn8n!z&oE~^%LAp{_rt$G)s{~`<ThTvSVvd?gH0vB)y>B3yM&j%E5uV6qPk)}#!uDOSP$Vn5VW8TCc}rlfL0Uah0zi{Eae{|Rfg9*KxJovR6>qC%jD4iu#vq#C+w#9dU|QUQ12?WXJ{qA4ZrHX$$pJKOZ6_TufJnHN^K_yrSj7~lUv~?z4LRuihqML&Ei2l;OCb#*_{DBoN(DHdC9;$1>APoe?huGQpN)cYu9nVd1J>gt(zpjvpNayr(UZ*By)xvOsix*E^Jg;LJQ<QZNaQDtk<bMSo7+kb#-+;u;n;Z77#o=0CR^1Ye51%FmrbxGTya6*&eH+siJnjg}<0Q?$;u}|L27ms`<D+*TI2%k#1`~w~}#XEtDTVAJ1mJ=DO}Z`0!P+FTJ}xMtvGDxJ`#W00JaBAy861z)6KeD1fj(a)7;*s@8hH${|Yqq~#vJHI``K3RlfOT{TG7ATpLd))P;s6<2CLHKawjh4el?3!Nu1sW1>eslg&av~J!#5NBsEz~!ku3J>uEp|hkv`>Tz*{0D%)G+T~D8ZjKd%2-eec-zxHBe+c+ax$I1emO?Tefe`fh@HEdD6dGqBTFKkPKg^n>(&R80mkdSXgN_&4sy9YWpe<ouE2;tv!a_VENFqhahJU!C@2!Yd#?M%odm`{Y5e07PnTG}d+#BNbG#=$z$2C3Fo*TM0g@`c!Vbed>wo!SS%8qe1WEisIXhcD^qR8+i;|MR%mXqRHAI5HpNMJLub>3K(!oJV`OCyU+xCyS=N>1%v)WbK$*}M}cIH4nB15~q$+XyJn&y5zaS|s{8n;5dz=<k&ddCMnm{_L~R86VBk!hGmt*C;(^l>$JR9NM{g9KvHrIo}!F)=!Z&k`5DA)m$61+v1u+MaL52_}@i1_D*t9o$hpOlbxo-_8lW;~JU$)z8R0Odw#1q`I`fQW&{SMVErVngkChcAE1(9ffofv{S@Bzd5rA6$>Z6GYLf>ni$u;sJpjS*CR;1fZVQb&N)Fnb=nsa@nFw96gP5dt|qcP8=Gk;*R8z2DWW>kiV=dp?D+|;#jFTF<^dv!8{We{>LQgd9d9wdklMU5;kd!Quc#&wg{zr8!;VE9D@R{F3$Mz;MBgAiGc!``)biv!geTbiG$+Epn}N7H2pWOENpn8f*p?GNNbF!eV`;-a&fmomS~(NGk@2vo?V18Uyx|IVMY_^GfehQ<Pz#?u)tF-H1~+Lv>Bf@s8lf{ibIm;k#kIx1IdT<OOk{t*OfyAb=Kvc&GWv92k0ZuD*qV&e>fdxe6$SiMTr^ES@+ZMBSoa`4w2)NI?8osv-TVqvxaz<?5DOE~qfL!H!?_owke0~5h-pm`YtMSWToL2W*jgSxmzkA{=U=}*bquZtuQ_kNTJhY!F`PI)$AO@-W=0FXOdGdP;b+=C5X27yVA-a<0Fp}X!p?C$o9z8-b4Sa+hBtrx<kNP)m*50E8Ji(LA2q+g_-3{~AdU;Z9cx;?f&miP3RCJmr(SfJW`DrFpq58RxnhkyaM7NYu_9N!0Du4m+W{dxJI<w*uY%3LM1v^RAXjp~W@KcFbYUYu<9!MS$po-I$n*n0@UvOIcTbtFfh)Pa*aU))P?27}@H-$;!Q4tcP$+gNO41O$fTY;W+0oQIGNg>tRXoqX4MQ2aO#N!VB$w=frjR5*K_v9SYA>TcDOU#<LI+yD0L<D?t1Cpk_Pb;lxT}0U;2ht(VdoY-Ahf?4A0^nl(YvQ41yz+i6FDudIyTV1oUhGVao%9R(g4!@eJ3S9GaULq&SHr^bdWzjxs_SI5exw=zEj6N&X)|D$}@mH0JvLz^W}NG*h;o2h@!N-0HzIK?m}cdbAjG5jEB&_=Xn4l^lM7L+m0Uurzj;q$hHI4Ju8U5!_V*LRyJ6^r}|we=Zn`p47k;%Mz(%E=b}(?>2UkJn6-KvwgscS5d2ciQL;fiwGFJV7?RMx$WJVS!ZJKRoEq}qDV!ufs8^sN)P|wHl&1py?ekT>kI67lk}TmpLXv|WHq&}Ngly)I4rB$rOvFu{fhd{007A0}4c9L`{d-fKvRBZ*b;tu!{)bvW<)lf3I*%hinUuEhM6s*BW*^1+>*`Xzk77K|{<Y;jjI>cAO^kIt^p6*aDya&+?Tkr9Em@JgP#uEm$<--5fyE^}v$xN`C%<Qd>|<s>+z{Owl@lUA(4HqqcNnt1KS}FbkAzOXc17X|%qr<U$JrsxLZ)s#94w<}z!eU?&?Tx4@E?S{sAWx{a*rxJkXNL_{zlHfZf<IgmbGp_3{W)|n?4{v85FO^=wP+J5So@V4p2tE+*gFDMrZ3iMy7a}zZ_vbYnAz|_o5HIcdBZvDeqytJ_Z@AFL5nAT{p{xfN9LXYuUI`ya{tZh*Kg&jZhpvT~1Ya@te24NuxA&<~TdPHAZ`)Yg_C+UB-IC7rQz=&z5EjCL9mFQ*~51rs8@$tg1%U2a7R0zMzAeCN0XpF{S2w2Qqd)@~%Mn4Ad7tK#!kMBEY!5I@9%Z6+R=r{tQzf7Y*z^Sdl#c0$NkOo)5m)#1ss@IE$jWb}W)Sa+ZBoBT+a!R1<lt>Y&HJ4D*_9A<cL{a%yXADmxQD?apiIWYD<2?WkyG?zJ60K2Y%O$DHat1I>AM;HPB0cMRfh-hc(YM0+3cJ1U|)s^-Xix%WjpTJwl1Ce*~gAyTMhrP_Kw&`(z#h;I!)T8!Aru-do2&OhYv`AauGvi(VxyHV&prHl$TY=3LLc#dd%`-bqm#N_Jd{PD6p_=?dBE16q75+s+j>(#-(;+-Y324H+Yw-qV_rSJql|CP{PF7>s(`4%YPI?h5q7ktQG48P?)N@DRSG-_$RiBb;xh?@pIXL_U&d4kA1Dgw~zv;}xP^-h~8*J!=Jmn=d76=;1w(3}kii<|mBXjJuVA2_qVK^tib21rRho1Hb2%S_}whzpx4pt&MF*vGZ5Vc{)3x>Zcm6G`Sgz%<&4Mz5VbM^$9(%=osyl2`s=c>;bv+WE3FN>A%P>F8dJAY8A$|Fe69@&Hgi+-B(z4b130#VcC~uCI?h*Fz)=1zb`+%mH@ZP)HCx$;}-S!0gRD2;eDaRB^DsUQG4kmP39&JlsxC7Gljl2`b4qN-n0pr_g=&&gNA<<Dze)XmkHPqG_zET{pfxIHR%57$So`q%Y+If+9#gU<q8%(EAQOD1u`P=EbAGi>wREwMKqFEeop^Q|-UL=N{D#m`91e#iY{F4$Wyk@<>M|^PMg}k8FB2SQq;}M0}!A3lYdYx(KT}hjf%ZfReq<%4c9bK0GnM>aB{ux46=<4@Z7KNLs66CQ;lzgjz+ITnxuPBbit9`HrGKx)I6-zTkI0+Xvw-CXh@%D_CS^54RpZo11ksa>?yIpojVbLN>ZR'''
if os.environ.get('D85_VECTOR','1')=='2':v85=V2_B85
if os.environ.get('D85_VECTOR','1')=='odd':v85=ODD_B85
half=np.array(struct.unpack('<480d',base64.b85decode(v85.encode())))
coef=np.zeros(960)
parsign=-1 if os.environ.get('D85_VECTOR','1')=='odd' else 1
for ci in range(48):
    for k in range(10):
        coef[ci*10+k]=half[ci*10+k]/math.sqrt(2)
        coef[(95-ci)*10+k]=parsign*((-1)**k)*half[ci*10+k]/math.sqrt(2)

src=Path(__file__).with_name('114_d_77_log3_legendre_arb_verify.py').read_text()
src=src.replace('DEPTH = 80','DEPTH = 160').replace('T = arb(3).log()/2','T = arb(2).log()')
src=src.replace('C_PRIME = A/arb(2).sqrt()',
                'C_PRIME=A/arb(2).sqrt()\nC_THREE=arb(3).log()/arb(3).sqrt()')
src=src.replace('BVALS = [arb(2*j)+arb("0.5") for j in range(DEPTH)]',
                'BTAIL=arb("320.5")\nCTAIL=BTAIL/4\n'
                'TERMS=[(arb(2*j)+arb("0.5"),arb(1)) for j in range(DEPTH)]'
                '+[(BTAIL,CTAIL)]\nBVALS=[z[0] for z in TERMS]')
src=src.replace('sum((2/b for b in BVALS), arb(0))','sum((w*2/b for b,w in TERMS), arb(0))')
src=src.replace('for b in BVALS:\n        z = b*h/2','for b,wgt in TERMS:\n        z = b*h/2')
src=src.replace('plus.append(fp); minus.append(fm)',
                'plus.append(fp); minus.append(fm)')
src=src.replace('local[i][j] -= kij','local[i][j] -= wgt*kij')
# Return the exact local residual coefficient rows; skip the generic trace.
p0=src.index('    # Exact finite Gram of Q K_local P; trace bounds its operator norm^2.')
p1=src.index('\n\ndelta = 2*T-A',p0)
src=src[:p0]+'    return {"h":h,"plus":plus,"minus":minus,"local":local,"rows":residual_rows}\n'+src[p1:]
# Replace everything after function definitions by the log2 mesh packages.
cut=src.index('\ndelta = 2*T-A')
src=src[:cut]+r'''
b3=arb(3).log(); d=2*A-b3; e=2*b3-3*A; MD=20; ME=8
packages={"d":cell_package(d/MD),"e":cell_package(e/ME)}
types=["d"]*MD+["e"]*ME+["d"]*MD+["d"]*MD+["e"]*ME+["d"]*MD
left=[]; xx=-T
for typ in types:left.append(xx);xx+=packages[typ]["h"]
mid=[left[i]+packages[types[i]]["h"]/2 for i in range(len(types))]
'''
ns={};exec(compile(src,str(Path(__file__).with_name('114_d_77_log3_legendre_arb_verify.py'))+'::D85','exec'),ns)
arb,ctx=ns['arb'],ns['ctx'];ctx.prec=256
D=10;NC=96;TERMS=ns['TERMS'];packages=ns['packages'];types=ns['types'];mid=ns['mid'];left=ns['left']
if os.environ.get('D85_REFINE','0')=='1':
    M=np.zeros((960,960))
    for q,typ in enumerate(types):
        M[q*D:(q+1)*D,q*D:(q+1)*D]=np.array([[float(z.mid()) for z in row] for row in packages[typ]['local']])
    for it,(bb,ww) in enumerate(TERMS):
        b=float(bb.mid());w=float(ww.mid())
        for i in range(NC):
            fp=np.array([float(z.mid()) for z in packages[types[i]]['plus'][it]])
            for j in range(i+1,NC):
                fm=np.array([float(z.mid()) for z in packages[types[j]]['minus'][it]])
                z=-w*math.exp(-b*float((mid[j]-mid[i]).mid()))*np.outer(fp,fm)
                M[i*D:(i+1)*D,j*D:(j+1)*D]+=z;M[j*D:(j+1)*D,i*D:(i+1)*D]+=z.T
    starts=[0,20,28,48,68,76]
    for si,sj,n,cc in [(starts[0],starts[3],20,float(ns['C_PRIME'].mid())),
                       (starts[1],starts[4],8,float(ns['C_PRIME'].mid())),
                       (starts[2],starts[5],20,float(ns['C_PRIME'].mid())),
                       (starts[0],starts[5],20,float(ns['C_THREE'].mid()))]:
        for u in range(n):
            i,j=si+u,sj+u;M[i*D:(i+1)*D,j*D:(j+1)*D]-=cc*np.eye(D);M[j*D:(j+1)*D,i*D:(i+1)*D]-=cc*np.eye(D)
    for sig in (.5,-.5):
        gv=[]
        for i,typ in enumerate(types):
            ff=ns['feature'](arb(repr(sig))*packages[typ]['h']/2,packages[typ]['h'])
            gv.extend([math.exp(sig*float(mid[i].mid()))*float(z.mid()) for z in ff])
        gv=np.array(gv);M+=1000*np.outer(gv,gv)
    U=np.zeros((960,480));parsign=-1 if os.environ.get('D85_REFINE_ODD','0')=='1' else 1
    for ci in range(48):
        for k in range(D):U[ci*D+k,ci*D+k]=2**-.5;U[(95-ci)*D+k,ci*D+k]=parsign*(-1)**k*2**-.5
    ev,V=np.linalg.eigh(U.T@M@U)
    print('REFINED_RITZ',ev[:4],flush=True)
    print('REFINED_B85',base64.b85encode(struct.pack('<480d',*V[:,0])).decode(),flush=True)
    print('SECOND_B85',base64.b85encode(struct.pack('<480d',*V[:,1])).decode(),flush=True)
    raise SystemExit(0)
v=[arb(repr(float(x))) for x in coef]

# Exact projected action A_P v.
y=[arb(0) for _ in range(NC*D)]
for q,typ in enumerate(types):
    block=packages[typ]['local'];vq=v[q*D:(q+1)*D]
    for i in range(D):y[q*D+i]+=sum((block[i][j]*vq[j] for j in range(D)),arb(0))
for it,(b,w) in enumerate(TERMS):
    for i in range(NC):
        fp=packages[types[i]]['plus'][it]
        for j in range(i+1,NC):
            fm=packages[types[j]]['minus'][it];dec=(-b*(mid[j]-mid[i])).exp()
            vi=v[i*D:(i+1)*D];vj=v[j*D:(j+1)*D]
            si=sum((fm[k]*vj[k] for k in range(D)),arb(0))
            sj=sum((fp[k]*vi[k] for k in range(D)),arb(0))
            for k in range(D):y[i*D+k]-=w*dec*fp[k]*si;y[j*D+k]-=w*dec*fm[k]*sj
# Exact contacts.
starts=[0,20,28,48,68,76]
for si,sj,n,c in [(starts[0],starts[3],20,ns['C_PRIME']),
                  (starts[1],starts[4],8,ns['C_PRIME']),
                  (starts[2],starts[5],20,ns['C_PRIME']),
                  (starts[0],starts[5],20,ns['C_THREE'])]:
    for u in range(n):
        i,j=si+u,sj+u
        for k in range(D):y[i*D+k]-=c*v[j*D+k];y[j*D+k]-=c*v[i*D+k]
# Rank-two moment penalty.
for sig in (arb('0.5'),arb('-0.5')):
    gv=[]
    for i,typ in enumerate(types):
        f=ns['feature'](sig*packages[typ]['h']/2,packages[typ]['h'])
        gv.extend([(sig*mid[i]).exp()*z for z in f])
    s=sum((gv[i]*v[i] for i in range(len(v))),arb(0))
    for i in range(len(v)):y[i]+=ns['RHO']*gv[i]*s

norm=sum((z*z for z in v),arb(0));mu=sum((v[i]*y[i] for i in range(len(v))),arb(0))/norm
pres=sum(((y[i]-mu*v[i])**2 for i in range(len(v))),arb(0))/norm
print('norm=',norm);print('Rayleigh mu=',mu);print('projected residual^2=',pres)
if os.environ.get('D85_VECTOR','1')=='1':assert -mu < arb('1.747e-6')
elif os.environ.get('D85_VECTOR','1')=='2':assert mu > arb('0.00203')
else:assert mu > arb('8e-6')

# Exact Q residual.  On each target cell the ODE remainder is a linear
# combination of the 322 projected exponentials, plus the two moment
# exponentials.  Their Gram matrix is closed-form and depends only on cell
# type; no quadrature is used.
ctx.prec=512
moment_s={}
for sig in (arb('0.5'),arb('-0.5')):
    gv=[]
    for i,typ in enumerate(types):
        ff=ns['feature'](sig*packages[typ]['h']/2,packages[typ]['h'])
        gv.extend([(sig*mid[i]).exp()*z for z in ff])
    moment_s[str(sig)]=sum((gv[i]*v[i] for i in range(len(v))),arb(0))

gram_cache={}
for typ in ('d','e'):
    hcell=packages[typ]['h']; feats=[]
    for row in packages[typ]['rows']:feats.append((row[0]*row[1],row[2]))
    for sig in (arb('0.5'),arb('-0.5')):
        feats.append((sig,ns['feature'](sig*hcell/2,hcell)))
    nr=len(feats);G=[[arb(0) for _ in range(nr)] for _ in range(nr)]
    for i,(ri,fi) in enumerate(feats):
        for j in range(i,nr):
            rj,fj=feats[j]
            z=ns['exp_inner'](ri+rj,hcell)-sum((fi[k]*fj[k] for k in range(D)),arb(0))
            G[i][j]=G[j][i]=z
    gram_cache[typ]=G
    print('resolved residual Gram',typ,'dim',nr,flush=True)

qres=arb(0)
q_targets=[] if os.environ.get('D85_GENERIC_BOUNDS','0')=='1' else list(enumerate(types))
for q,typ in q_targets:
    rows=packages[typ]['rows'];vq=v[q*D:(q+1)*D];cc=[]
    for it,(b,w) in enumerate(TERMS):
        arow=rows[2*it][3];brow=rows[2*it+1][3]
        cp=-w*sum((arow[k]*vq[k] for k in range(D)),arb(0))
        cm=-w*sum((brow[k]*vq[k] for k in range(D)),arb(0))
        for j in range(q+1,NC):
            dec=(-b*(mid[j]-mid[q])).exp();vj=v[j*D:(j+1)*D]
            cmj=packages[types[j]]['minus'][it]
            cp-=w*dec*sum((cmj[k]*vj[k] for k in range(D)),arb(0))
        for j in range(q):
            dec=(-b*(mid[q]-mid[j])).exp();vj=v[j*D:(j+1)*D]
            cpj=packages[types[j]]['plus'][it]
            cm-=w*dec*sum((cpj[k]*vj[k] for k in range(D)),arb(0))
        cc.extend((cp,cm))
    for sig in (arb('0.5'),arb('-0.5')):
        cc.append(ns['RHO']*(sig*mid[q]).exp()*moment_s[str(sig)])
    G=gram_cache[typ];z=arb(0)
    for i in range(len(cc)):
        z+=cc[i]*cc[i]*G[i][i]
        for j in range(i+1,len(cc)):z+=2*cc[i]*cc[j]*G[i][j]
    qres+=z
    if (q+1)%12==0:print('Q residual cells',q+1,'partial=',qres,flush=True)
qres/=norm;total_res=pres+qres
print('Q residual^2=',qres);print('total residual^2=',total_res)
if q_targets:
    assert qres > 0 and total_res < arb('3e-17')
    print('PASS fixed-vector directed Rayleigh and full-space residual certificate')

if os.environ.get('D85_GENERIC_BOUNDS','0')=='1':
    r=D;hmax=max((packages[z]['h'] for z in packages),key=lambda z:z.upper())
    # Local QKP Hilbert--Schmidt bound, with all cross-resolvent terms retained.
    local_bounds=[]
    for typ in ('d','e'):
        C=[]
        rows=packages[typ]['rows']
        for it,(bb,ww) in enumerate(TERMS):
            C.append([-ww*z for z in rows[2*it][3]])
            C.append([-ww*z for z in rows[2*it+1][3]])
        G=gram_cache[typ];tr=arb(0)
        for k in range(D):
            for i in range(len(C)):
                tr+=C[i][k]*C[i][k]*G[i][i]
                for j in range(i+1,len(C)):tr+=2*C[i][k]*C[j][k]*G[i][j]
        local_bounds.append(tr.sqrt())
    beta_local=max(local_bounds,key=lambda z:z.upper())
    # Exact single-resolvent off-cell blocks, summed by the triangle
    # inequality.  This retains the exponential residual instead of the
    # catastrophically coarse uniform Taylor power b^r.
    beta_cross=arb(0);qq_cross=arb(0)
    for it,(bb,ww) in enumerate(TERMS):
        b2=arb(0);q2=arb(0)
        for ii in range(NC-1):
            hi=packages[types[ii]]['h'];fpi=packages[types[ii]]['plus'][it]
            rp=ns['exp_inner'](2*bb,hi)-sum((z*z for z in fpi),arb(0))
            nfp=sum((z*z for z in fpi),arb(0))
            for jj in range(ii+1,NC):
                hj=packages[types[jj]]['h'];fmj=packages[types[jj]]['minus'][it]
                rm=ns['exp_inner'](-2*bb,hj)-sum((z*z for z in fmj),arb(0))
                nfm=sum((z*z for z in fmj),arb(0))
                cc=ww*(-bb*(mid[jj]-mid[ii])).exp()
                b2+=cc*cc*(rp*nfm+rm*nfp)
                q2+=2*cc*cc*rp*rm
        beta_cross+=b2.sqrt();qq_cross+=q2.sqrt()
    taylor=hmax**r/arb.fac_ui(r)
    beta_H=ns['RHO']*taylor*(arb('0.5')**r)*4*ns['T'].sinh()
    beta=beta_local+beta_cross+beta_H
    dmin=sum((ww*ns['robin_local_gap'](bb,hmax) for bb,ww in TERMS),arb(0))
    alpha=dmin-ns['M0']-ns['C_PRIME']-ns['C_THREE']-qq_cross
    print('generic alpha=',alpha);print('beta local,cross,H=',beta_local,beta_cross,beta_H)
    print('generic beta^2=',beta*beta,'qq_cross=',qq_cross)
    assert alpha > arb('1.53') and beta*beta < arb('0.0362')
    print('PASS directed generic P--Q/high-Q bounds')
