from tkinter import *
import pandas as pd
from sentw import *
from pathlib import Path


class user:
    def __init__(self,unm):
        self.uroot=Tk()
        self.uf=Frame(self.uroot,height=450,width=700)
        self.uname=unm
        self.uf.propagate(0)
        self.uf.pack()
        #self.transfer()

        self.msgshow("welcome :@"+unm+" !",10,10)
        self.home()
    def msgshow(self,st,xx,yy):
            
            self.lm=Label(self.uf,text=st)
            self.lm.place(x=xx,y=yy)
    def viewal(self):
        csv=pd.read_csv('request.txt')
        data=csv[['row','sender','reciever','amount','date','unq','confirm']]
        xx=200
        yy=250
        xc=20
        i=0
        l=len(data)
        self.msgshow("row,sender,reciever,amount,date,unq,confirm",xx,yy-xc)
        while i<l:
            stn=str(data['row'][i])+' '+str(data['sender'][i])+') \t'+str(data['reciever'][i])+' \t'+str(data['amount'][i])+' '+str(data['date'][i])+' '+str(data['unq'][i])+' '+str(data['confirm'][i])+''
            self.msgshow(stn,xx,yy)
            yy+=xc
            i+=1

    def home(self):
        self.b1=Button(self.uf,text="view J",width=10,height=3,command=lambda:self.viewmy())
        self.b2=Button(self.uf,text="transfer J",width=10,height=3,command=lambda:self.transfer())
        self.bb=Button(self.uf,text="view all",width=5,height=3,command=lambda:self.viewal())
        self.bb.place(x=50,y=25)
        #self.b1.bind('<Button-1>',ask_sutoshi)
        #self.b2.bind('<Button-1>',transfer)
        self.b1.place(x=30,y=20,width=100,height=50)
        self.b1.pack()
        self.b2.place(x=50,y=70,width=100,height=50)
        self.b2.pack()

    def ask_satoshi(self):
        print("submitting request")

    def viewmy(self):
        xx=200
        blc=0
        yy=250
        xc=20
        csv=pd.read_csv(self.uname+'.txt')
        data=csv[['amt','ggt','date','prs','unq']]
        i=0
   
        l=len(data)
        self.msgshow("amount : credit/d :\t date\t :from : id ",xx,yy-xc)
        while i<l:
            stn=str(data['amt'][i])+' \t('+str(data['ggt'][i])+') \t'+str(data['date'][i])+' \t'+str(data['prs'][i])+' '+str(data['unq'][i])+' '
            self.msgshow(stn,xx,yy)
            if int(data['ggt'][i])==0:
                blc+=float(data['amt'][i])
            else:
                blc-=float(data['amt'][i])
            yy+=xc
            i+=1
        bstr="balance :"+str(blc)+" Jcoin "
        
        self.msgshow(bstr,xx,xx)
        

    def transact(self):
        rcvr=str(self.e2.get())
        rcvpt=rcvr+'.txt'
        print(rcvpt)
        mypth=Path(rcvpt).is_file()
        if mypth==False:
            self.msgshow("sorry no user with given key"+rcvr+" available",120,220)
        else:                        
            sentwa(self.uname,self.e2.get(),self.e1.get())
        

    def transfer(self):
        self.nlist=[]
        csv=pd.read_csv("account.txt")
        data=csv[['uname','pass']]
        l=len(data['uname'])
        i=1
        while i<l:
            if str(data['uname'][i])!=str(self.uname):
                self.nlist.append(data['uname'][i])
            i+=1

        print(self.nlist)
        self.l1=Label(self.uf,text='amount      :')
        self.l2=Label(self.uf,text='reciever key:')

        self.e1=Entry(self.uf,width=25,fg='blue',bg='gold',font=('arial',15))
        self.e2=Entry(self.uf,width=25,fg='blue',bg='gold')
        #self.e2.bind("<Return>",self.check)
        self.cnf=Button(self.uf,text="confirm",width=10,height=3,command=lambda: self.transact())
        self.l1.place(x=50,y=100)
        self.e1.place(x=200,y=100)
        self.l2.place(x=50,y=150)
        self.e2.place(x=200,y=150)
        self.cnf.place(x=100,y=200)

 
        


#uroot=Tk()
#u=user("bx123")
