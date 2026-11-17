import json,os,urllib.request as u
E=os.getenv("MAKEFUN_ENV_URL") or exit("?")
N=[-33,-31,-18,-14,14,18,31,33]
G=[-17,-16,-15,-1,1,15,16,17]
D=[-17,-15,15,17,-16,-1,1,16]
V=[0,100,320,330,500,900,20000]
VE=[0,120,300,310,520,950,20000]
PH=[0,0,1,1,2,4,0]
CR={0:2,7:1,112:8,119:4}
P0=[0,0,0,0,0,0,0,0,50,50,50,50,50,50,50,50,10,10,20,30,30,20,10,10,5,5,10,25,25,10,5,5,0,0,0,20,20,0,0,0,5,-5,-10,0,0,-10,-5,5,5,10,10,-20,-20,10,10,5,0,0,0,0,0,0,0,0]
P0E=[0,0,0,0,0,0,0,0,80,80,80,80,80,80,80,80,50,50,50,50,50,50,50,50,30,30,30,30,30,30,30,30,20,20,20,20,20,20,20,20,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,0,0,0,0,0,0,0,0]
P1=[-50,-40,-30,-30,-30,-30,-40,-50,-40,-20,0,0,0,0,-20,-40,-30,0,10,15,15,10,0,-30,-30,5,15,20,20,15,5,-30,-30,0,15,20,20,15,0,-30,-30,5,10,15,15,10,5,-30,-40,-20,0,5,5,0,-20,-40,-50,-40,-30,-30,-30,-30,-40,-50]
P2=[-20,-10,-10,-10,-10,-10,-10,-20,-10,0,0,0,0,0,0,-10,-10,0,5,10,10,5,0,-10,-10,5,5,10,10,5,5,-10,-10,0,10,10,10,10,0,-10,-10,10,10,10,10,10,10,-10,-10,5,0,0,0,0,5,-10,-20,-10,-10,-10,-10,-10,-10,-20]
P3=[0,0,0,0,0,0,0,0,5,10,10,10,10,10,10,5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,0,0,5,10,10,5,0,0]
P4=[-20,-10,-10,-5,-5,-10,-10,-20,-10,0,0,0,0,0,0,-10,-10,0,5,5,5,5,0,-10,-5,0,5,5,5,5,0,-5,0,0,5,5,5,5,0,-5,-10,5,5,5,5,5,0,-10,-10,0,5,0,0,0,0,-10,-20,-10,-10,-5,-5,-10,-10,-20]
P5=[-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-20,-30,-30,-40,-40,-30,-30,-20,-10,-20,-20,-20,-20,-20,-20,-10,20,20,0,0,0,0,20,20,20,30,10,0,0,10,30,20]
P6=[-50,-40,-30,-20,-20,-30,-40,-50,-30,-20,-10,0,0,-10,-20,-30,-30,-10,20,30,30,20,-10,-30,-30,-10,30,40,40,30,-10,-30,-30,-10,30,40,40,30,-10,-30,-30,-10,20,30,30,20,-10,-30,-30,-30,0,0,0,0,-30,-30,-50,-30,-30,-30,-30,-30,-30,-50]
PM=[0,P0,P1,P2,P3,P4,P5]
PE=[0,P0E,P1,P2,P3,P4,P6]
WM={};WE={}
for p in range(1,7):
 WM[p]=[0]*128;WM[-p]=[0]*128;WE[p]=[0]*128;WE[-p]=[0]*128
 for r in range(8):
  for f in range(8):
   q=r*16+f
   WM[p][q]=V[p]+PM[p][(7-r)*8+f]
   WM[-p][q]=-(V[p]+PM[p][r*8+f])
   WE[p][q]=VE[p]+PE[p][(7-r)*8+f]
   WE[-p][q]=-(VE[p]+PE[p][r*8+f])
WM[0]=WE[0]=[0]*128
T={};R=set();GH=set();H={}
K=[[0,0] for _ in range(64)]
ND=[0]
BG=60000
class A(Exception):...
def sq(s):return (int(s[1])-1)*16+"abcdefgh".index(s[0])
def en(f,t,p):return f|(t<<7)|(p<<14)
def ps(f):
 a=f.split();B=[0]*128;r=7;x=0;mg=0;eg=0;ph=0
 for c in a[0]:
  if c=="/":r-=1;x=0
  elif c.isdigit():x+=int(c)
  else:
   q=r*16+x;p=("pnbrqk".index(c.lower())+1)*(1 if c.isupper() else -1)
   B[q]=p;mg+=WM[p][q];eg+=WE[p][q];ph+=PH[abs(p)];x+=1
 s=1 if a[1]=="w" else -1
 c=sum(1<<i for i,k in enumerate("KQkq") if k in a[2])
 return B,s,c,-1 if a[3]=="-" else sq(a[3]),B.index(6),B.index(-6),mg,eg,ph
def ak(B,q,s):
 for o in N:
  t=q+o
  if not t&136 and B[t]==2*s:return 1
 for o in G:
  t=q+o
  if not t&136 and (B[t]==6*s or B[t]==s and abs(o+16*s)==1):return 1
 for i,o in enumerate(D):
  t=q+o
  while not t&136 and not B[t]:t+=o
  if not t&136 and B[t]*s>0 and abs(B[t]) in ((3,5) if i<4 else (4,5)):return 1
 return 0
def gn(B,s,c,e):
 M=[]
 for q in range(128):
  p=B[q]
  if p*s<=0 or q&136:continue
  a=abs(p);r=q>>4
  if a==1:
   d=16*s;sr=1+5*(s<0);lr=7*(s>0)
   for t in (q+d,q+d-1,q+d+1):
    if t&136:continue
    if t==q+d:
     if B[t]:continue
    elif B[t]*s>=0 and t!=e:continue
    if (t>>4)==lr:
     for pr in (5,4,3,2):M.append(en(q,t,pr))
    else:
     M.append(en(q,t,0))
     if t==q+d and r==sr and not B[q+2*d]:M.append(en(q,q+2*d,0))
  elif a==2 or a==6:
   for o in (N if a==2 else G):
    t=q+o
    if not t&136 and B[t]*s<=0:M.append(en(q,t,0))
   if a==6:
    for b,k,rk,ts,tt in ((1,4,7,(5,6),6),(2,4,0,(3,2,1),2)) if s>0 else ((4,116,119,(117,118),118),(8,116,112,(115,114,113),114)):
     if q==k and c&b and B[rk]==s*4 and all(not B[t] for t in ts) and all(not ak(B,t,-s) for t in (k,)+ts[:2]):M.append(en(k,tt,0))
  else:
   for o in (D[:4] if a==3 else D[4:] if a==4 else D):
    t=q+o
    while not t&136 and B[t]*s<=0:
     M.append(en(q,t,0))
     if B[t]:break
     t+=o
 return M
def mk(st,m):
 B,s,c,e,kw,kb,mg,eg,ph=st;f=m&127;t=m>>7&127;pr=m>>14;p=B[f];cp=B[t];B2=B[:]
 mg-=WM[p][f]+WM[cp][t];eg-=WE[p][f]+WE[cp][t];ph-=PH[abs(cp)]
 if abs(p)==1 and t==e and not cp:
  ep=t-16*s;B2[ep]=0;mg-=WM[-s][ep];eg-=WE[-s][ep]
 np=s*pr if 2<=pr<=5 else p
 B2[t]=np;B2[f]=0;mg+=WM[np][t];eg+=WE[np][t]
 if pr:ph+=PH[pr]
 if abs(p)==6:
  kw,kb=(t,kb) if s>0 else (kw,t)
  if abs(t-f)==2:
   rf=f+3 if t>f else f-4;rt=f+1 if t>f else f-1;rp=s*4
   B2[rf]=0;B2[rt]=rp;mg+=WM[rp][rt]-WM[rp][rf];eg+=WE[rp][rt]-WE[rp][rf]
 c2=c
 if abs(p)==6:c2&=~(3,12)[s<0]
 for q2 in (f,t):c2&=~CR.get(q2,0)
 e2=f+16*s if abs(p)==1 and abs(t-f)==32 else -1
 return B2,-s,c2,e2,kw,kb,mg,eg,ph
def ev(st):
 B,s,c,e,kw,kb,mg,eg,ph=st
 p=min(ph,24);t2=(mg*p+eg*(24-p))//24
 if ph<6 and abs(t2)>150:
  w=1 if t2>0 else -1;a,b=(kb,kw) if w>0 else (kw,kb);r=a>>4;f=a&7
  t2+=w*(12*(max(3-r,r-4)+max(3-f,f-4))+5*(14-abs(r-(b>>4))-abs(f-(b&7))))
 return t2*s
def sc(st,dep,al,be,ply):
 if ply>63:ply=63
 B,s,c,e,kw,kb,mg,eg,ph=st;ND[0]+=1
 if ND[0]>BG:raise A
 key=(tuple(B),s,c,e)
 if ply>0 and (key in R or key in GH):return 0
 en_=T.get(key);tt=0
 if en_:
  tt=en_[3]
  if ply>0 and en_[0]>=dep:
   v,fl=en_[1],en_[2]
   if fl==0 or (fl==1 and v>=be) or (fl==2 and v<=al):return v
 ck=ak(B,(kw,kb)[s<0],-s)
 if ck:dep+=1
 if dep<=0:
  v=ev(st)
  if v>=be:return be
  if v>al:al=v
  ms=[m for m in gn(B,s,c,e) if B[m>>7&127] or m>>14 or (m>>7&127)==e]
  ms.sort(key=lambda m:10*V[abs(B[m>>7&127])]-V[abs(B[m&127])],reverse=True)
  for m in ms:
   t=m>>7&127
   if m>>14==0 and t!=e and v+V[abs(B[t])]+180<al:continue
   st2=mk(st,m)
   if ak(st2[0],st2[4+(s<0)],-s):continue
   sv=-sc(st2,dep-1,-be,-al,ply+1)
   if sv>al:al=sv
   if al>=be:break
  return al
 pv=be-al>1;v0=ev(st)
 if not pv and not ck:
  if dep<=3 and v0-85*dep>=be:return v0
  if dep>2 and ph>0 and v0>=be and sc((B,-s,c,-1,kw,kb,mg,eg,ph),dep-3,-be,1-be,ply+1)>=be:return be
 R.add(key)
 ms=gn(B,s,c,e)
 def os_(m):
  if m==tt:return 20000000
  t=m>>7&127;v=B[t]
  if v:return 1000000+10*V[abs(v)]-V[abs(B[m&127])]
  if m>>14:return 900000+V[m>>14]
  if m==K[ply][0]:return 800000
  if m==K[ply][1]:return 700000
  return H.get(m&16383,0)
 ms.sort(key=os_,reverse=True)
 bs=-10**9;bm=0;oa=al;lm=0
 for m in ms:
  st2=mk(st,m)
  if ak(st2[0],st2[4+(s<0)],-s):continue
  lm+=1;cp=B[m>>7&127] or m>>14
  if lm==1:sv=-sc(st2,dep-1,-be,-al,ply+1)
  else:
   r=1 if lm>3 and dep>2 and not ck and not cp else 0
   if lm>10 and dep>3 and not ck and not cp:r=2
   sv=-sc(st2,dep-1-r,-al-1,-al,ply+1)
   if sv>al and r>0:sv=-sc(st2,dep-1,-al-1,-al,ply+1)
   if sv>al and pv:sv=-sc(st2,dep-1,-be,-al,ply+1)
  if sv>bs:bs=sv;bm=m
  if sv>al:al=sv
  if al>=be:
   if not cp:
    if K[ply][0]!=m:K[ply][1]=K[ply][0];K[ply][0]=m
    k2=m&16383;H[k2]=min(H.get(k2,0)+dep*dep,500000)
   break
 R.discard(key)
 if bs==-10**9:return -99999+ply if ck else 0
 if abs(bs)<90000 and len(T)<300000:
  T[key]=(dep,bs,2 if bs<=oa else 1 if bs>=be else 0,bm)
 return bs
def uc(u):
 return en(sq(u[:2]),sq(u[2:4]),"nbrq".index(u[4])+2 if len(u)>4 else 0)
def po(p,b):
 r=u.Request(E+p,data=json.dumps(b).encode())
 with u.urlopen(r) as x:return json.load(x)
def rt(st,legal):
 ms=[uc(x) for x in legal];bm=ms[0];ND[0]=0;R.clear()
 B,s,c,e,kw,kb,mg,eg,ph=st
 for k in list(H):H[k]>>=2
 for dep in range(1,9):
  try:
   al=-10**9;cb=bm
   ms.sort(key=lambda m:(m==bm,10*V[abs(B[m>>7&127])]-V[abs(B[m&127])],H.get(m&16383,0)),reverse=True)
   for i,m in enumerate(ms):
    st2=mk(st,m)
    if ak(st2[0],st2[4+(s<0)],-s):continue
    if i==0:sv=-sc(st2,dep-1,-10**9,-al,1)
    else:
     sv=-sc(st2,dep-1,-al-1,-al,1)
     if sv>al:sv=-sc(st2,dep-1,-10**9,-al,1)
    if sv>al:al=sv;cb=m
   bm=cb
   if al>90000:break
  except A:break
 if B[bm>>7&127] or abs(B[bm&127])==1:GH.clear()
 else:
  GH.add((tuple(B),s,c,e));k=mk(st,bm);GH.add((tuple(k[0]),-s,k[2],k[3]))
 return bm
LG=[0]
while (g:=po("/game",{}))["status"]!="done":
 if g["game"]!=LG[0]:LG[0]=g["game"];T.clear();GH.clear();H.clear()
 while g["status"]=="your_move":
  f0=g["fen"]
  if f0.split()[4]=="0":GH.clear()
  m=rt(ps(f0),g["legal_moves"]);f=m&127;t=m>>7&127;g=po("/move",{"game":g["game"],"move":"abcdefgh"[f&7]+str((f>>4)+1)+"abcdefgh"[t&7]+str((t>>4)+1)+("nbrq"[(m>>14)-2] if m>>14 else "")})
