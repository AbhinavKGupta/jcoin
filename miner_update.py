max_confrm=5
me=-1

import pandas as pd
import os
import random

rej=0
ttl=0
flag=2
def confirm_updater(r,el):
    #print("\n\n*************************************\ninside confirm updater :")
    #print("\t the row is :"+str(r))
    df=pd.read_csv("request.txt")
    v=int(df.iloc[[r]]['confirm'])
    
    #print("initial votes :"+str(v))
    
    vr=v+1
    df.at[r,'confirm']=vr
    k=df.iloc[0:,1:]
    
    k.to_csv("request.txt",sep=',')
    f=open("request.txt","r")
    f1=open("request1.txt","a")
    for k in f:
        f1.write(k)
    f1.close()
    f.close()
    #f=open("request.txt","a")
    f1=open("request.txt","w+")
    f=open("request.txt","w")
    f.truncate(0)
    for k in f1:
        f.write(k)
    f1.truncate(0)
    f1.write("row")	
    f.close()
    f1.close()
    os.rename("request.txt","req.txt")
    os.rename("request1.txt","request.txt")
    os.rename("req.txt","request1.txt")

    if vr==max_confrm:
        print("confirmed :",str(r))
        print("by :",str(me))
        cs=pd.read_csv(str(el[2])+'.txt')
        dt=cs[['amt','ggt']]
        lr=len(dt)
        st=str(el[3])+',0,'+str(el[4])+','+str(el[1])+','+str(lr)+'\n'
        obj_r=open(str(el[2])+'.txt',"a+")
        obj_r.write(st)
        return 1
    else:
        return 0
    
def verifying(el):
    cost=0
    fn=el[1]+'.txt'
    row=el[5]   
    fil=pd.read_csv(fn)		#0<-deposit; 1=waiting ;2->transmitted
    data=fil[['amt','ggt']]
    i=0
    print("\tinside verifying :")
    
    print(el)
    print("i :",i,"<> r :",row)		# logic of cost calculator
    while i<row:
        print("i :",str(i),"<> r :",str(row))
        print("value[i] "+str(data['ggt'][i]))
        if data['ggt'][i]==0:
            cost+=float(data['amt'][i])
        else:
            cost-=float(data['amt'][i])
        i+=1
    if cost>=el[3]:
        cc=confirm_updater(el[0],el)
        return cc
   
    return 0 # not confirming
            
            #print("Yes! \t @",el,"\t by :<> ",str(me))
    
    
#confirm_updater(2)
def submit():
    csv=pd.read_csv("request.txt")
    data=csv[['row','sender','reciever','amount','date','unq','confirm']]
    el=[]
    n=10
    cf=int(input("mine randomly or specificly 1/0:"))
    if cf==1:
        n=random.randint(0,len(data)-1)
    else:
        n=int(input("enter the transaction id :"))
    
    if int(data['confirm'][n])>=max_confrm:
        '''
        if rej==len(data)**3:
            print("Total coins mined :"+str(ttl)+" by <"+me+">")
            flag=-2
            return 0
        '''
        return -1
    el.append(data['row'][n])
    el.append(data['sender'][n])
    el.append(data['reciever'][n])
    el.append(data['amount'][n])
    el.append(data['date'][n])
    el.append(data['unq'][n])
    el.append(data['confirm'][n])

    print(el)
    print("verifying @el :")
    return verifying(el)

def mine():
    c=1
    while c==1:
        s=submit()
        if s==0:
            mine()
        c=int(input("continue 1/0:"))
        
    #print("Mine :"+str(c))
       
        #c=int(input("continue :1/0"))
'''    
if submit() ==-1:
    print("already confirmed")
'''
me=int(input("Enter me :"))
mine()



